"""Publish editorial planning examples; private source notes stay outside this repo."""
import collections
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import site_template as T

DATE = '2026-10-19'
DISCLOSURE = ('Anonymized composite planning example informed by recurring discovery-call themes. '
              'Facts are generalized to protect privacy. This is educational analysis, not a '
              'testimonial or a report of completed client work, verified savings or investment results.')


def main():
    cases = json.loads((ROOT / 'scripts/calendar_planning_cases.json').read_text())
    cards = []
    for c in cases:
        path = '/case-studies/' + c['slug'] + '/'
        paragraphs = lambda text: '<p>' + html.escape(text) + '</p>'
        body = T.page_header(h1=T.esc(c['title']), subtitle=T.esc(c['summary']),
                             trail=[('Home', '/'), ('Case Studies', '/case-studies/'), (c['title'], path)])
        body += T.section('About this planning example', paragraphs(DISCLOSURE))
        for heading, key in [('The situation', 'situation'), ('The decision', 'decision'),
                             ('Tax rule to verify', 'rule'), ('Our recommendation', 'recommendation')]:
            body += T.section(heading, paragraphs(c[key]))
        body += T.section('Records needed before implementation', '<ul>' + ''.join(
            '<li>' + html.escape(x) + '</li>' for x in c['records']) + '</ul>')
        body += T.section('What could change the recommendation', paragraphs(c['alternative']))
        body += T.section('The planning deliverable', paragraphs(c['deliverable']))
        sources = [c['source']] + ([c['extra_source']] if c.get('extra_source') else [])
        body += T.section('Source and further reading', '<p><a href="' + c['source'] + '">' +
                          T.esc(c['source_label']) + '</a></p>' +
                          ('<p><a href="' + c['extra_source'] + '">IRS Topic 705: Installment Sales</a></p>' if c.get('extra_source') else '') +
                          '<p>Reviewed October 19, 2026. Apply the rules for the relevant tax year with your preparer; state treatment may differ.</p>')
        body += T.related_section([(c['related'], 'Explore the related AE service'),
                                   ('/case-studies/', 'Browse all case studies and planning examples')])
        schemas = [T.article_schema(title=c['title'], description=c['summary'], url=T.SITE+path,
                                    published=DATE, modified=DATE, section='Illustrative Tax Planning Case',
                                    citations=sources),
                   T.breadcrumb_schema([('Home', '/'), ('Case Studies', '/case-studies/'), (c['title'], path)])]
        T.write_page(path, T.build_page(title=c['title']+' | AE Tax Advisors', description=c['summary'],
                     path=path, body=body, schemas=schemas, published=DATE, modified=DATE, active_nav='/case-studies/', extra_head='<style>main .content-section{padding:28px 0}main .content-section:first-of-type{padding-top:48px}main .content-section h2{margin-bottom:14px}main .content-section p{line-height:1.8}main .content-section li{margin-bottom:8px}</style>'))
        cards.append('<article class="cs-card" data-cat="'+c['category']+'" data-income="unknown" data-ownership="'+c['ownership']+
                     '" data-estate="'+c['estate']+'" data-text="'+T.esc((c['title']+' '+c['summary']).lower())+'">'+
                     '<span class="cs-tag">'+c['category']+'</span><h3><a href="'+path+'">'+T.esc(c['title'])+'</a></h3>'+
                     '<div class="cs-profile-tags"><span>Composite planning example</span><span>Income not specified</span></div>'+
                     '<p>'+T.esc(c['summary'])+'</p><a class="btn-secondary" href="'+path+'">Read the recommendation</a></article>')
    hubpath = ROOT / 'case-studies/index.html'
    hub = hubpath.read_text()
    hub = re.sub(r'<!-- calendar-cases:start -->.*?<!-- calendar-cases:end -->', '', hub, flags=re.S)
    hub = hub.replace('<div class="cs-grid" id="cs-grid">', '<div class="cs-grid" id="cs-grid"><!-- calendar-cases:start -->'+''.join(cards)+'<!-- calendar-cases:end -->', 1)
    total = hub.count('class="cs-card"')
    # Derive counts from complete card tags, irrespective of attribute order.
    counts = collections.Counter(re.search(r'data-cat="([^"]+)"', tag)[1] for tag in re.findall(r'<article\b[^>]*class="cs-card"[^>]*>', hub))
    hub = re.sub(r'(data-cat="all"[^>]*>All \()\d+', lambda m: m[1]+str(total), hub)
    for cat, count in counts.items():
        hub = re.sub(r'(data-cat="'+re.escape(cat)+r'"[^>]*>'+re.escape(cat)+r' \()\d+', lambda m: m[1]+str(count), hub)
    hub = re.sub(r'\b250(?= tax planning| Tax Planning| case studies)', str(total), hub)
    hub = hub.replace('On illustrative examples, the card explicitly identifies assumed profit. On illustrative examples, the card explicitly identifies assumed profit.', 'On illustrative examples, the card explicitly identifies assumed profit.')
    hub = re.sub(r'<meta (property="og:title"|name="twitter:title") content="[^"]*">', lambda m: '<meta '+m[1]+' content="Tax Planning Case Studies and Examples | AE Tax Advisors">', hub)
    notice = '<p id="calendar-planning-note"><strong>New: 12 planning examples with recommendations.</strong> Explore rental conversions, partnership cash flow, owner payroll, business exits and more. These anonymized composites explain decisions and required records; they do not claim completed client outcomes.</p>'
    hub = re.sub(r'<p id="calendar-planning-note">.*?</p>\n?', '', hub, flags=re.S)
    hub = hub.replace('<label for="cs-search"', notice+'\n<label for="cs-search"', 1)
    def schema(match):
        d = json.loads(match[1])
        if d.get('@type') == 'CollectionPage':
            items = [x for x in d['mainEntity']['itemListElement'] if not any(x.get('url', '').endswith('/'+c['slug']+'/') for c in cases)]
            items = [dict(position=i+1, **{'@type':'ListItem'}, name=c['title'], url=T.SITE+'/case-studies/'+c['slug']+'/') for i,c in enumerate(cases)] + items
            for i,item in enumerate(items): item['position'] = i+1
            d['mainEntity']['itemListElement'] = items
            d['mainEntity']['numberOfItems'] = len(items)
            d['dateModified'] = DATE
            d['description'] = f'{total} case studies and clearly labeled planning examples, including anonymized composites with recommendations.'
        return '<script type="application/ld+json">'+json.dumps(d, ensure_ascii=False, indent=2)+'</script>'
    hub = re.sub(r'<script type="application/ld\+json">(.*?)</script>', schema, hub, flags=re.S)
    hub = re.sub(r"(?m)^[ \t]+$", "", hub)
    hubpath.write_text(hub)
    for filename in ['sitemap.xml', 'sitemap-case-studies.xml']:
        p = ROOT / filename
        xml = p.read_text()
        for c in cases:
            url = T.SITE+'/case-studies/'+c['slug']+'/'
            if '<loc>'+url+'</loc>' not in xml:
                xml = xml.replace('</urlset>', '<url><loc>'+url+'</loc><lastmod>'+DATE+'</lastmod></url>\n</urlset>')
        p.write_text(xml)
    print(f'Built {len(cases)} unique composite cases; {total} cards in hub.')


if __name__ == '__main__':
    main()
