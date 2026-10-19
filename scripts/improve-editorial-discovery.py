"""Apply consistent shared-page presentation and relevant links in public output."""
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / 'public').resolve()
cases = json.loads((ROOT / 'scripts/calendar_planning_cases.json').read_text())
groups = {
 '/business-owner-small-business-tax/': [0, 5, 6, 10],
 '/short-term-rental-tax-strategy/': [2, 3, 4],
 '/rental-property-tax-planning/': [3, 8, 11],
 '/cost-segregation-study/': [4, 8, 11],
 '/retirement-exit-ma-tax-strategy/': [6, 10],
 '/services/reasonable-compensation/': [5, 1],
 '/real-estate-tax-planning/': [2, 4, 7],
 '/individual-tax-planning-high-earners/': [0, 2, 7],
 '/services/quarterly-estimates/': [0, 9, 10],
 '/compare/': [5, 7, 10],
 '/compare/business-owner-provider-shortlists/': [5, 6, 10],
 '/compare/high-income-provider-shortlists/': [0, 2, 7],
 '/compare/small-business-tax-firms/': [5, 6, 9],
}
styled = linked = 0
for file in OUT.rglob('*.html'):
    route = '/' + file.relative_to(OUT).as_posix()
    if route.endswith('/index.html'):
        route = route[:-10]
    text = file.read_text()
    original = text
    text = re.sub(r'(<a\b[^>]*class="[^"]*(?:nav-cta|header-cta)[^"]*"[^>]*>)[^<]*(</a>)', r'\1Book a Call\2', text, flags=re.I)
    if 'src="/assets/booking-events.js' not in text:
        text = text.replace('</head>', '<script defer src="/assets/booking-events.js?v=20261019"></script></head>', 1)
    if route == '/' or re.search(r'<meta[^>]+content=[\"\x27][^\"\x27]*noindex', text, re.I):
        if text != original:
            file.write_text(text)
        continue
    shared = 'id="primary-nav"' in text and 'class="page-header"' in text and '/assets/style.css' in text
    if shared:
        def body(m):
            tag = m[0]
            if 'ae-editorial' in tag:
                return tag
            if re.search(r'class=[\"\x27]', tag):
                return re.sub(r'(class=[\"\x27])', r'\1ae-editorial ', tag, count=1)
            return tag[:-1] + ' class="ae-editorial">'
        text = re.sub(r'<body\b[^>]*>', body, text, count=1)
        styled += 1
    if route in groups:
        text = re.sub(r'<!-- ae-planning-links:start -->.*?<!-- ae-planning-links:end -->', '', text, flags=re.S)
        panel = '<!-- ae-planning-links:start --><section class="ae-planning-links"><div class="container narrow"><h2>Planning examples for this decision</h2><p>Explore anonymized composite scenarios with recommendations and the records needed to evaluate them. These examples do not claim completed client results.</p><ul>'
        for index in groups[route]:
            c = cases[index]
            panel += '<li><a href="/case-studies/' + c['slug'] + '/">' + html.escape(c['title']) + '</a><p>' + html.escape(c['summary']) + '</p></li>'
        panel += '</ul></div></section><!-- ae-planning-links:end -->'
        if '</main>' not in text:
            raise ValueError('Missing main landmark: ' + route)
        text = text.replace('</main>', panel + '</main>', 1)
        linked += 1
    if shared or route in groups:
        if 'src="/assets/booking-events.js' not in text:
            text = text.replace('</head>', '<script defer src="/assets/booking-events.js?v=20261019"></script></head>', 1)
        if 'href="/assets/editorial-consistency.css' not in text:
            text = text.replace('</head>', '<link rel="stylesheet" href="/assets/editorial-consistency.css?v=20261019"></head>', 1)
    if text != original:
        file.write_text(text)
missing = [route for route in groups if not (OUT / route.strip('/') / 'index.html').exists()]
if linked != len(groups):
    raise ValueError('Not every service/comparison owner received its case links')
if missing:
    raise ValueError('Missing service pages: ' + ', '.join(missing))
ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
for sitemap in OUT.glob('sitemap*.xml'):
    tree = ET.parse(sitemap)
    changed = False
    for row in tree.getroot():
        loc = row.find('{*}loc')
        if loc is not None and loc.text in {'https://www.aetaxadvisors.com' + route for route in groups}:
            lastmod = row.find('{*}lastmod')
            if lastmod is None:
                lastmod = ET.SubElement(row, '{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod')
            lastmod.text = '2026-10-19'
            changed = True
    if changed:
        tree.write(sitemap, encoding='utf-8', xml_declaration=True)
print(json.dumps(dict(shared_editorial_pages=styled, service_comparison_hubs_with_case_links=linked)))
