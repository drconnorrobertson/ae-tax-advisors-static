"""Author-time approved blog catalog and deterministic archive renderer.

Only explicitly registered routes can enter the archive. Deployment stages the
committed output; it does not discover or generate new editorial content.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import collections, html, json, re, xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://www.aetaxadvisors.com'
CATALOG = ROOT / 'scripts/blog-catalog.json'
PAGE_SIZE = 36
NS = 'http://www.sitemaps.org/schemas/sitemap/0.9'

class Metadata(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.meta = {}; self.canonical = ''; self.h1 = []; self.in_h1 = False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta': self.meta[a.get('name', a.get('property', '')).lower()] = a.get('content', '')
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = a.get('href', '')
        if tag == 'h1': self.in_h1 = True
    def handle_endtag(self, tag):
        if tag == 'h1': self.in_h1 = False
    def handle_data(self, value):
        if self.in_h1: self.h1.append(value)

def clean(value):
    return ' '.join(html.unescape(re.sub('<[^>]+>', '', value)).split())

def restrictions():
    holds = set(json.loads((ROOT / 'discovery_review_holds.json').read_text()))
    redirects = dict(json.loads((ROOT / 'scripts/content-consolidation.json').read_text())['redirects'])
    for item in json.loads((ROOT / 'vercel.json').read_text()).get('redirects', []):
        source = item.get('source', '')
        if ':' not in source and '*' not in source and '(' not in source:
            redirects[source] = item['destination']
    return holds, redirects

def article(route, category=None, strict=True):
    """Resolve explicit approved links to canonical article metadata, never scan."""
    holds, redirects = restrictions(); seen = set()
    for _ in range(12):
        if route in seen: raise ValueError('Canonical/redirect cycle: ' + route)
        seen.add(route)
        if not re.fullmatch(r'/blog/[a-z0-9][a-z0-9-]*/', route): raise ValueError('Not a blog article route: ' + route)
        if route in holds: raise ValueError('Article is held: ' + route)
        destination = redirects.get(route) or redirects.get(route.rstrip('/'))
        if destination:
            route = urlsplit(destination).path
            continue
        directory = ROOT / route.strip('/') / 'index.html'
        flat = ROOT / (route.strip('/') + '.html')
        candidates = [p for p in (directory, flat) if p.is_file()]
        if not candidates: raise ValueError('Missing article: ' + route)
        source = candidates[0]
        if len(candidates) == 2 and directory.read_bytes() != flat.read_bytes():
            override_file = ROOT / 'scripts/blog-archive-source-overrides.json'
            overrides = json.loads(override_file.read_text()) if override_file.exists() else {}
            selected = overrides.get(route)
            permitted = {p.relative_to(ROOT).as_posix(): p for p in candidates}
            if selected not in permitted:
                raise ValueError('Conflicting directory and flat article sources: ' + route)
            source = permitted[selected]
        text = source.read_text(); metadata = Metadata(text)
        if 'noindex' in metadata.meta.get('robots', '').lower(): raise ValueError('Article is noindex: ' + route)
        if re.search(r'nth\s*degree|nthdegreecpas|dan\s+nicholson', text, re.I): raise ValueError('Excluded provider in article: ' + route)
        canonical = urlsplit(metadata.canonical)
        if canonical.scheme != 'https' or canonical.netloc != 'www.aetaxadvisors.com': raise ValueError('Invalid canonical: ' + route)
        if canonical.path != route:
            route = canonical.path
            continue
        title = clean(' '.join(metadata.h1)); description = clean(metadata.meta.get('description', ''))
        if not title or not description: raise ValueError('Missing title/description: ' + route)
        date = ''; section = ''
        for raw in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', text, re.S):
            def visit(obj):
                nonlocal date, section
                if isinstance(obj, dict):
                    if obj.get('@type') in ('Article', 'BlogPosting'):
                        date = date or obj.get('datePublished', '')[:10]
                        section = section or obj.get('articleSection', '')
                    for value in obj.values(): visit(value)
                elif isinstance(obj, list):
                    for value in obj: visit(value)
            visit(json.loads(raw))
        date = date or metadata.meta.get('article:published_time', '')[:10]
        if date and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', date): raise ValueError('Invalid publication date: ' + route)
        return dict(url=route, title=title, description=description, category=clean(category or section or 'Tax Strategy'), date=date)
    raise ValueError('Too many canonical hops: ' + route)

def load():
    return json.loads(CATALOG.read_text())

def register_routes(routes):
    """Called by a reviewed authoring batch with its explicit article routes."""
    entries = {e['url']: e for e in load()}
    for value in routes:
        route = value if isinstance(value, str) else value.get('url', value.get('path'))
        if not route.startswith('/blog/'): continue
        category = value.get('category') if isinstance(value, dict) else None
        entry = article(route, category or entries.get(route, {}).get('category'))
        entries[entry['url']] = entry
    CATALOG.write_text(json.dumps(sorted(entries.values(), key=lambda e:e['url']), indent=2, ensure_ascii=False) + '\n')
    render()

def archive_path(page):
    return '/blog/' if page == 1 else f'/blog/page/{page}/'

def card(e):
    esc = html.escape
    date = f'<time class="blog-date" datetime="{e["date"]}">{e["date"]}</time>' if e['date'] else ''
    return f'<article class="blog-card"><div class="blog-body"><div class="blog-meta"><span class="blog-cat">{esc(e["category"])}</span>{date}</div><h3><a href="{e["url"]}">{esc(e["title"])}</a></h3><p>{esc(e["description"])}</p></div></article>'

def render():
    entries = load(); unique = set()
    for e in entries:
        checked = article(e['url'], e['category'])
        if checked['url'] != e['url']: raise ValueError('Catalog entry now redirects; explicitly reconcile: ' + e['url'])
        if e['url'] in unique: raise ValueError('Duplicate catalog entry: ' + e['url'])
        unique.add(e['url'])
    entries = sorted(entries, key=lambda e:(e['date'], e['url']), reverse=True)
    pages = (len(entries) + PAGE_SIZE - 1) // PAGE_SIZE
    if not pages: raise ValueError('Empty catalog')
    template = (ROOT/'scripts/blog-archive-template.html').read_text()
    counts = collections.Counter(e['category'] for e in entries)
    options = '<option value="">All categories ('+str(len(entries))+')</option>' + ''.join(f'<option value="{html.escape(k,quote=True)}">{html.escape(k)} ({v})</option>' for k,v in sorted(counts.items()))
    for page in range(1, pages+1):
        route = archive_path(page); visible = entries[(page-1)*PAGE_SIZE:page*PAGE_SIZE]
        heading = 'Tax Strategy Blog' + (f': Page {page}' if page > 1 else '')
        title = heading + ' | AE Tax Advisors'
        description = f'Browse page {page} of {pages}: tax planning articles for business owners and real estate investors. Explore depreciation, entities, retirement and filing decisions.'
        nav = (f'<a rel="prev" href="{archive_path(page-1)}">Previous</a> ' if page > 1 else '')
        nav += ' '.join(f'<span aria-current="page">{i}</span>' if i==page else f'<a href="{archive_path(i)}" aria-label="Archive page {i}">{i}</a>' for i in range(1,pages+1))
        nav += (f' <a rel="next" href="{archive_path(page+1)}">Next</a>' if page < pages else '')
        schema = {'@context':'https://schema.org','@type':'CollectionPage','name':heading,'url':SITE+route,'mainEntity':{'@type':'ItemList','numberOfItems':len(visible),'itemListElement':[{'@type':'ListItem','position':i+1,'url':SITE+e['url'],'name':e['title']} for i,e in enumerate(visible)]}}
        body = f'''<main id="main-content" tabindex="-1"><section class="page-header"><div class="container"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/blog/">Blog</a>{f' › Page {page}' if page>1 else ''}</nav><h1>{html.escape(heading)}</h1><p>{len(entries)} articles for business owners and real estate investors. Page {page} of {pages}.</p><p><a href="/business-owner-tax-planning/">Business owner planning</a> · <a href="/real-estate-tax-planning/">Real estate planning</a> · <a href="/cost-segregation-study/">Cost segregation</a> · <a href="/tax-movement-explained/">Illustrated tax lessons</a> · <a href="/feed.xml">Article feed</a></p><p><a href="/editorial-policy/">How we review tax content</a> · <a href="/tax-return-mistakes/">Return-review guides and checklist</a></p></div></section><section class="content-section"><div class="container"><form id="blog-search-form" action="{route}" method="get" role="search"><div class="blog-toolbar"><label for="blog-search-input">Search all articles</label><input class="blog-search" type="search" id="blog-search-input" name="q" placeholder="Topic, strategy or IRC section"><label for="blog-category">Category</label><select id="blog-category" name="category">{options}</select><button type="submit">Search</button><button type="reset">Clear filters</button></div></form><noscript><p>Interactive search requires JavaScript. Browse every article using the numbered archive links below.</p></noscript><p id="blog-result-status" role="status" aria-live="polite" tabindex="-1">Showing articles {(page-1)*PAGE_SIZE+1}–{min(page*PAGE_SIZE,len(entries))} of {len(entries)}.</p><div class="blog-grid" id="blog-grid">{''.join(card(e) for e in visible)}</div><button id="blog-load-more" class="blog-more" type="button" hidden>Show more results</button><nav id="blog-pagination" class="blog-pagination" aria-label="Blog archive pages">{nav}</nav></div></section></main>'''
        output = template.replace('{{TITLE}}',html.escape(title)).replace('{{DESCRIPTION}}',html.escape(description,quote=True)).replace('{{CANONICAL}}',SITE+route).replace('{{SCHEMA}}',json.dumps(schema,ensure_ascii=False).replace('<','\\u003c')).replace('{{MAIN}}',body)
        target = ROOT/route.strip('/')/'index.html'; target.parent.mkdir(parents=True,exist_ok=True); target.write_text(output)
    # Only remove obsolete generated archive pages, never editorial directories.
    for p in (ROOT/'blog/page').glob('*/index.html'):
        if p.parent.name.isdigit() and int(p.parent.name)>pages and 'data-blog-archive="1"' in p.read_text(): p.unlink(); p.parent.rmdir()
    (ROOT/'assets/blog-search-index.json').write_text(json.dumps(entries,ensure_ascii=False,separators=(',',':'))+'\n')
    urls = ''.join(f'<url><loc>{SITE+archive_path(i)}</loc></url>\n' for i in range(1,pages+1))
    (ROOT/'sitemap-blog-archive.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="{NS}">\n{urls}</urlset>\n')
    for name in ['sitemap-index.xml','sitemap_index.xml']:
        p=ROOT/name; text=p.read_text()
        if '/sitemap-blog-archive.xml' not in text: p.write_text(text.replace('</sitemapindex>',f'<sitemap><loc>{SITE}/sitemap-blog-archive.xml</loc></sitemap>\n</sitemapindex>'))
    print(f'Rendered {len(entries)} approved articles across {pages} committed archive pages.')

def discovery_html(root):
    """Read visible archive coverage for author-time batch verification."""
    root=Path(root)
    paths=[root/'blog/index.html']+sorted((root/'blog/page').glob('*/index.html'))
    return '\n'.join(p.read_text() for p in paths)

if __name__ == '__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--register',nargs='+',help='Explicit approved /blog/article/ routes; never a directory scan')
    args=parser.parse_args()
    register_routes(args.register) if args.register else render()
