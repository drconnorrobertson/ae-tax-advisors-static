#!/usr/bin/env python3
"""Validate the deployed cohort, including generated additions and navigation anchors."""
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote

REPO = Path(__file__).resolve().parents[1]
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else REPO
BASE = 'https://www.aetaxadvisors.com'
COHORT = sys.argv[2] if len(sys.argv) > 2 else 'five-competitors-20261106'
assert re.fullmatch(r'[a-z0-9-]+', COHORT)
DATA = REPO / 'content' / COHORT
pages = json.loads((DATA / 'pages.json').read_text())
sources = json.loads((DATA / 'sources.json').read_text())
config = json.loads((REPO / 'vercel.json').read_text())
redirects = {r['source']: r['destination'] for r in config['redirects'] if not re.search(r'[:*()]', r['source'])}
sitemaps = {e.text for f in ROOT.glob('sitemap*.xml') for e in ET.parse(f).findall('.//{*}loc')}
errors = []
titles = set()
links_checked = 0

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links = []; self.ids = []; self.canonicals = []; self.metas = {}; self.h1 = 0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'h1': self.h1 += 1
        if tag == 'a': self.links.append(a.get('href', ''))
        if tag == 'link' and a.get('rel') == 'canonical': self.canonicals.append(a.get('href'))
        if tag == 'meta': self.metas[a.get('name', a.get('property', ''))] = a.get('content', '')

def resolve(path):
    f = ROOT / unquote(path).lstrip('/')
    for candidate in (f, f / 'index.html', Path(str(f) + '.html')):
        if candidate.is_file(): return candidate
    return None

for path in pages:
    file = resolve(path)
    if not file:
        errors.append(path + ': missing'); continue
    text = file.read_text(); page = Page(text)
    title = html.unescape(re.search(r'<title>(.*?)</title>', text, re.S)[1])
    if title in titles: errors.append(path + ': duplicate title')
    titles.add(title)
    if page.h1 != 1 or page.canonicals != [BASE + path]: errors.append(path + ': heading/canonical')
    if 'noindex' in page.metas.get('robots', '') or BASE + path not in sitemaps: errors.append(path + ': indexability/sitemap')
    if not 60 <= len(page.metas.get('description', '')) <= 200: errors.append(path + ': description length')
    if len(page.ids) != len(set(page.ids)): errors.append(path + ': duplicate anchor')
    for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
        obj = json.loads(raw)
        if obj.get('@type') == 'Article' and obj.get('dateModified') != '2026-11-06': errors.append(path + ': modified date')
        if obj.get('@type') in ('Review', 'AggregateRating'): errors.append(path + ': unsupported review rating')
    if 'AE Tax Advisors provides tax planning' not in text: errors.append(path + ': AE service positioning')
    if text.count('src="/assets/booking-events.js"') != 1: errors.append(path + ': booking event hook')
    if 'alternatives/' in path:
        if text.count('id="provider-review"') != 1: errors.append(path + ': review anchor')
        if text.find('Which ') > text.find('id="provider-review"'): errors.append(path + ': shortlist not first')
    for href in page.links:
        if not href or href.startswith(('tel:', 'mailto:', 'javascript:')): continue
        url = urlsplit(urljoin(BASE + path, href))
        if url.hostname not in ('www.aetaxadvisors.com', 'aetaxadvisors.com'): continue
        target = url.path; visited = set()
        while target in redirects:
            if target in visited:
                errors.append(path + ': redirect loop'); break
            visited.add(target)
            dest = urlsplit(urljoin(BASE, redirects[target]))
            if dest.hostname != 'www.aetaxadvisors.com': target = None; break
            target = dest.path
        if target is None: continue
        f = resolve(target)
        if not f: errors.append(path + ': broken link ' + href); continue
        links_checked += 1
        if url.fragment and f.suffix == '.html' and unquote(url.fragment) not in Page(f.read_text()).ids:
            errors.append(path + ': missing anchor ' + href)

directory = json.loads((ROOT / 'compare/competitor-pricing/prices.json').read_text())
for r in directory['providers']:
    if r['slug'] in sources:
        if r['fee'] != sources[r['slug']]['fee'] or r['reviewed'] != '2026-11-06': errors.append(r['slug'] + ': stale directory evidence')
if (DATA / 'preservation.json').exists():
    import hashlib
    for path, digest in json.loads((DATA / 'preservation.json').read_text()).items():
        if hashlib.sha256((REPO / path.strip('/') / 'index.html').read_bytes()).hexdigest() != digest:
            errors.append(path + ': prior cohort source changed')
assert not errors, '\n'.join(errors)
print(json.dumps({'pages': len(pages), 'internal_links_checked': links_checked, 'errors': errors}))
