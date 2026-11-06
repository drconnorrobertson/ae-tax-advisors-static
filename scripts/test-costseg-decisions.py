#!/usr/bin/env python3
"""Focused source checks for the November 6 cost segregation decision cohort.

Run from any directory. Does not build, publish, or access a remote service.
"""
from pathlib import Path
from html.parser import HTMLParser
from decimal import Decimal, ROUND_HALF_UP
import html
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ROUTES = json.loads((ROOT / 'content/costseg-decisions-20261106/routes.json').read_text())
EXPECTED = {
    '/blog/do-i-need-an-engineering-based-cost-segregation-study/': '2026-08-11',
    '/compare/diy-cost-segregation-vs-ae-tax/': '2026-08-15',
    '/blog/what-happens-to-depreciation-when-i-sell-after-cost-segregation/': '2026-09-03',
}


def plain(s):
    return ' '.join(html.unescape(re.sub('<[^>]*>', ' ', s)).split())


def schemas(s):
    return [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', s, re.S)]


class BalancedMain(HTMLParser):
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self):
        super().__init__()
        self.stack = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID:
            self.stack.append(tag)
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])

    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, f'Unbalanced {tag}: {self.stack}'
        self.stack.pop()


assert set(ROUTES) == set(EXPECTED) and len(ROUTES) == 3
pages = {}
for route in ROUTES:
    p = ROOT / route.strip('/') / 'index.html'
    s = p.read_text()
    pages[route] = s
    main = re.search(r'<main>(.*?)</main>', s, re.S)[1]
    canonical = 'https://www.aetaxadvisors.com' + route
    assert re.findall(r'<link rel="canonical" href="([^"]+)"', s) == [canonical]
    assert 'noindex' not in s.lower()
    assert len(re.findall(r'<h1\b', main)) == 1
    parser = BalancedMain()
    parser.feed(main)
    assert not parser.stack and len(parser.ids) == len(set(parser.ids))
    data = schemas(s)
    article = [x for x in data if x.get('@type') in ('Article', 'BlogPosting')]
    faq = [x for x in data if x.get('@type') == 'FAQPage']
    assert len(article) == 1 and len(faq) == 1
    article = article[0]
    assert article['datePublished'] == EXPECTED[route]
    assert article['dateModified'] == '2026-11-06'
    assert article['url'] == canonical and article['mainEntityOfPage']['@id'] == canonical
    assert article['headline'] == plain(re.search(r'<h1[^>]*>(.*?)</h1>', main, re.S)[1])
    for name in ('description', 'og:description', 'twitter:description'):
        desc = html.unescape(re.search(r'<meta (?:name|property)="' + name + r'" content="([^"]*)"', s)[1])
        assert desc == article['description']
    title = html.unescape(re.search(r'<title>(.*?)</title>', s)[1])
    assert len(title) <= 70 and 110 <= len(article['description']) <= 170
    for name in ('og:title', 'twitter:title'):
        assert html.unescape(re.search(r'<meta (?:name|property)="' + name + r'" content="([^"]*)"', s)[1]) == title
    assert 'content="2026-11-06T00:00:00-06:00"' in s
    assert 'Updated November 6, 2026' in main
    assert len(faq[0]['mainEntity']) == 5
    visible_faq = re.search(r'<section[^>]*id="faq"[^>]*>(.*?)</section>', main, re.S)[1]
    visible_pairs = [(plain(q), plain(a)) for q, a in re.findall(r'<h3>(.*?)</h3><p>(.*?)</p>', visible_faq, re.S)]
    structured_pairs = [(q['name'], q['acceptedAnswer']['text']) for q in faq[0]['mainEntity']]
    assert visible_pairs == structured_pairs, f'FAQ mismatch: {route}'
    # Citations must describe sources the reader can actually open in the body.
    assert article['citation'] and any('irs.gov' in url for url in article['citation'])
    for source in article['citation']:
        assert f'href="{source}"' in main, f'Hidden source {source}'
    for link in re.findall(r'href="([^"]+)"', main):
        if not link.startswith('/'):
            continue
        target, _, fragment = link.partition('#')
        path = ROOT / target.strip('/')
        if path.is_dir():
            path /= 'index.html'
        assert path.is_file(), f'Missing local destination: {link}'
        if fragment:
            assert f'id="{fragment}"' in path.read_text(), f'Missing fragment: {link}'
    assert 'href="/cost-seg-discovery/"' in main
    assert not any(x in s for x in ('Why the Cheap Study Is Expensive', 'typical outcome is a negotiated reduction', 'Everything else is a compromise', '$9,775', '$22,225'))
    print('PASS:', route, 'canonical, original publication, modified date, metadata, five visible/schema FAQs, sources, local links, balanced HTML')

eng = pages[ROUTES[0]]
diy = pages[ROUTES[1]]
sale = pages[ROUTES[2]]

# Existing engagement figures and limitations must remain; do not import competitor fees.
for text in ('$7,800', '$3,900', '30 days apart', 'No required recurring annual planning fee', 'separately scoped and priced', 'free annual filing'):
    assert text in diy
for text in ('$1,200', '$11,500', '$2,600,000', '$2,150,000'):
    assert text in eng
assert '$495' not in diy and '$1,295' not in diy
assert diy.index('Compare the complete scope') < diy.index('id="ae-engagement-pricing"')

# Verify the illustrative basis and rate multiplication independently.
basis = Decimal('2150000')
a, b = basis * Decimal('.24'), basis * Decimal('.27')
assert a == 516000 and b == 580500 and b-a == 64500
assert (b-a) * Decimal('.37') == 23865
for text in ('$516,000', '$580,500', '$64,500', '$23,865', '$10,300', 'not a tax-savings estimate'):
    assert text in eng

# Recompute every displayed cash-flow table value using the explicitly stated timing.
flows = [Decimal('-5000'), Decimal('37000'), Decimal('-1500'), Decimal('-29500')]
rate = Decimal('1.08')
pvs = [x / rate**year for year, x in enumerate(flows)]
def dollars(x):
    amount = f'${abs(x).quantize(Decimal(".01"), rounding=ROUND_HALF_UP):,.2f}'
    return '(' + amount + ')' if x < 0 else amount
for value in pvs:
    assert dollars(value) in sale
assert sum(flows) == Decimal('1000')
assert dollars(sum(pvs)) == '$4,555.20' and '$4,555.20' in sale
assert 'all annual tax cash flows occur at year-end' in sale
assert 'exclude this sale tax so it is counted only once' in sale
assert 'Ignore any tax deduction or capitalization benefit from the fee' in sale

# Cross-check against the existing calculator implementation, without editing or building it.
code = "const {compare}=require('./assets/holding-period-cashflow.js'); console.log(JSON.stringify(compare({years:3,fee:5000,exitTax:28000,discount:8,benefits:[37000,-1500,-1500]})));"
result = json.loads(subprocess.check_output(['node', '-e', code], cwd=ROOT, text=True))
assert result['nominal'] == 1000
assert abs(result['presentValue'] - float(sum(pvs))) < 1e-8
print('PASS: preserved fees, scope separation, illustrative basis arithmetic, annual NPV arithmetic and existing calculator agreement')
