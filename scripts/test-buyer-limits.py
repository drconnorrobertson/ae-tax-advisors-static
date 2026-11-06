#!/usr/bin/env python3
"""Check the five 2026 buyer-limit corrections without builds or network access.

Usage: python3 scripts/test-buyer-limits.py [content-root] [--built-output] [--policy-root ROOT]
Built-output mode allows only the shared, verified release transformations on
the preservation baseline. Candidate output is never normalized or exempted.
The baseline protects publication, discovery, prices, case outcomes and navigation.
Negative fixtures are in-memory mutations; this script does not change content.
"""
from pathlib import Path
from collections import Counter
from decimal import Decimal as D
from html.parser import HTMLParser
from urllib.parse import urlsplit
import argparse, html, importlib.util, json, re, subprocess

REPO = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('content_root', type=Path, nargs='?', default=REPO)
parser.add_argument('--policy-root', type=Path, default=REPO)
parser.add_argument('--built-output', action='store_true')
args = parser.parse_args()
ROOT, POLICY = args.content_root.resolve(), args.policy_root.resolve()
if args.built_output:
    helper_path = POLICY / 'scripts/tax_review_build_normalization.py'
    assert helper_path.is_file(), 'Built-output mode needs the shared helper in --policy-root/scripts.'
    spec = importlib.util.spec_from_file_location('tax_review_build_normalization', helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
BASE = 'f2d5962a0b96bf7b9933bf1c764ed7778b6eea88'
COHORT = json.loads((REPO / 'content/buyer-limits-20261106.json').read_text())
AIR = 'airbnb-tax-deductions/index.html'
HIGH = 'for/high-income-500k/index.html'
EQUIP = 'equipment-leasing-section-179/index.html'
TRUCK = 'blog/trucking-company-equipment-depreciation-fleet/index.html'
RET = 'blog/how-to-maximize-retirement-contributions-as-s-corp-owner/index.html'
EXPECTED = {AIR, HIGH, EQUIP, TRUCK, RET}
SCHEMA = r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>'

def plain(s):
    return ' '.join(html.unescape(re.sub('<[^>]+>', '', s)).split())

def walk(o):
    if isinstance(o, dict):
        yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o, list):
        for v in o: yield from walk(v)

class Elements(HTMLParser):
    def __init__(self, s):
        super().__init__(); self.anchors=[]; self.meta={}; self.canon=[]; self.ids=[]; self.h1=0
        self.feed(s)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag == 'a' and 'href' in a: self.anchors.append(a['href'])
        if tag == 'meta': self.meta[a.get('name', a.get('property', ''))] = a.get('content', '')
        if tag == 'link' and a.get('rel') == 'canonical': self.canon.append(a.get('href'))
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'h1': self.h1 += 1

REQUIRED = {
    AIR: ['$2,560,000', '$4,090,000', 'noncorporate-lessor', 'annual election',
          '72.5 cents per mile for January 1 through June 30', '76 cents for July 1 through December 31',
          '$870 plus $912', '$1,782', 'personal travel', 'commuting', 'Do not also deduct'],
    HIGH: ['$24,500', '$72,000', '$8,000', '$80,000', '$11,250', '$83,250',
           '$43,750', '$68,250', '$290,000', 'not a universal annual contribution',
           'Section 404(a)(7)', 'eligible employees', 'Roth', '$111,000', 'age 70½',
           'donor-advised funds do not qualify', 'not independent savings amounts', 'not automatically added to wages or active S-Corp operating income',
           'rather than assuming planning will achieve a particular effective rate'],
    EQUIP: ['$2,560,000', '$4,090,000', '$6,650,000', '$32,000', '14,000 pounds',
            'six feet', 'An open bed or enclosed cab alone is not sufficient',
            'A true lease generally gives the lessee rent deductions', '$65,000', '$450,000',
            '$185,000', 'off-the-shelf software', 'after January 19, 2025',
            '100% bonus', 'transition rules', 'taxable-business-income', 'at-risk', 'permitted amended return'],
    TRUCK: ['$2,560,000', '$4,090,000', '$6,650,000', '$4,360,000', '$270,000', '$2,290,000',
            '$156,000', '$1.08 million', '$420,000', 'not a guaranteed refund',
            'after January 19, 2025', '100% bonus', 'true lessee', 'at-risk',
            'does not automatically reduce payroll tax', 'do not infer a tax offset from the number of vehicles'],
    RET: ['$24,500', '$72,000', '$47,500', '$80,000', '$83,250', '$184,500',
          '$290,000', 'not an annual contribution allowance', 'Section 404(a)(7)',
          '$4,278', '$2,900', '$450', '$7,628', 'employee-only', '$125,000',
          'prior-year wages', '$150,000', 'Roth', 'not retirement-plan compensation',
          'reasonable compensation', 'eligible employees'],
}
FORBIDDEN = {
    AIR: ['$1,220,000', '67 cents', '$1,608'],
    HIGH: ['$23,500', '$69,000', '$76,500', '$105,000', '$24,150', '$12,350', 'effective rate into the low 20s', 'combined effective rate above 45%'],
    EQUIP: ['$1,250,000', '$3,130,000', '$30,500', '$1.25 million', '$3.13 million'],
    TRUCK: ['$1,250,000', '$3,130,000', '$4.38 million', 'Why Fleets Skip Section 179', 'bonus depreciation beats Section 179 outright', 'the timing is worth six figures'],
    RET: ['$176,100', '$23,500', '$73,500', '$3,800', '$9,250'],
}

assert COHORT['review_date'] == '2026-11-06' and COHORT['tax_year'] == 2026
assert len(COHORT['pages']) == 5 and {p['path'] for p in COHORT['pages']} == EXPECTED
assert not any(v in json.dumps(COHORT) for v in ['/workspace/', 'gsc_ae_raw', 'clicks', 'impressions'])
BEFORE = {p: subprocess.check_output(['git', 'show', f'{BASE}:{p}'], cwd=REPO, text=True) for p in EXPECTED}
if args.built_output:
    BEFORE = {p: helper.normalize_baseline_html(s, POLICY, route='/' + p.removesuffix('index.html'))
              for p, s in BEFORE.items()}
RECORDS = {p['path']: p for p in COHORT['pages']}
CONFIG = json.loads((POLICY / 'vercel.json').read_text())
HOLDS = (POLICY / 'discovery_review_holds.json').read_text()

def validate(path, s):
    before=BEFORE[path]; p=Elements(s); old=Elements(before); route='/' + path.removesuffix('index.html')
    canonical='https://www.aetaxadvisors.com' + route
    assert p.canon == old.canon == [canonical], (path, 'canonical changed')
    assert p.meta.get('og:url') == old.meta.get('og:url'), (path, 'og:url changed')
    assert p.h1 == 1 and len(p.ids) == len(set(p.ids)), (path, 'heading or duplicate ID')
    assert not any('noindex' in p.meta.get(k, '').lower() for k in ['robots', 'googlebot'])
    assert not any(r.get('source', '').rstrip('/') == route.rstrip('/') for r in CONFIG.get('redirects', []))
    assert route.strip('/') not in HOLDS, (path, 'held route')
    for tag in ['title', 'header', 'footer']:
        pattern=rf'<{tag}\b[^>]*>.*?</{tag}>'
        assert re.findall(pattern, s, re.S) == re.findall(pattern, before, re.S), (path, tag + ' changed')
    for key in ['og:title', 'twitter:title']:
        assert p.meta.get(key) == old.meta.get(key), (path, key + ' changed')
    published=r'"datePublished"\s*:\s*"([^"]+)"'
    assert re.findall(published, s) == re.findall(published, before), (path, 'publication changed')
    assert not (Counter(old.anchors) - Counter(p.anchors)), (path, 'link removed')
    for match in re.finditer(r'<(p|li|tr)\b[^>]*>.*?</\1>', before, re.S):
        block = match[0]
        if re.search(r'\$[\d,]+', block) and re.search(r'\bclients?\b|advisory engagement|prior-year amendments', plain(block), re.I):
            assert block in s, (path, 'client outcome or price changed')
    for a in re.findall(r'<a\b[^>]*href="[^"]*(?:/case-studies/|/pricing/)[^"]*"[^>]*>.*?</a>', before, re.S):
        assert a in s, (path, 'case/pricing anchor changed')
    if path not in [EQUIP, TRUCK]:
        assert p.meta.get('description') == old.meta.get('description'), (path, 'description changed')
    else:
        assert p.meta['description'] == p.meta['og:description'] == p.meta['twitter:description']
    pairs={plain(q):plain(a) for q,a in re.findall(r'<h[23][^>]*>([^<>]*)</h[23]>\s*<p[^>]*>(.*?)</p>', s, re.S)}
    faq=0
    for block in re.findall(SCHEMA, s, re.S):
        for o in walk(json.loads(block)):
            if 'dateModified' in o: assert o['dateModified'] == '2026-11-06'
            if path in [EQUIP, TRUCK] and o.get('@type') in ['BlogPosting', 'Article', 'WebPage'] and 'description' in o:
                assert o.get('description') == p.meta['description'], (path, 'description/schema mismatch')
            if o.get('@type') == 'Question':
                assert o['name'] in pairs, (path, 'missing visible question', o['name'])
                assert plain(o['acceptedAnswer']['text']) == pairs[o['name']], (path, 'FAQ/schema mismatch', o['name'])
                faq += 1
    section=re.search(r'<section[^>]+id="buyer-limits-sources".*?</section>', s, re.S)
    assert section, (path, 'sources missing')
    for source in RECORDS[path]['sources']:
        assert urlsplit(source['url']).netloc in ['www.irs.gov', 'www.ssa.gov']
        assert f'href="{source["url"]}"' in section[0]
        assert html.escape(source['title']) in section[0]
    main=plain(re.search(r'<main\b[^>]*>(.*?)</main>', s, re.S)[1])
    for value in REQUIRED[path]: assert value in main, (path, 'required', value)
    for value in FORBIDDEN[path]: assert value not in s, (path, 'stale claim', value)
    return faq, len(p.anchors)

PAGES = {p: (ROOT / p).read_text() for p in EXPECTED}
faq_total=links=0
for path, text in PAGES.items():
    f,l=validate(path,text); faq_total+=f; links+=l

# Independent calculations, including Section 179 boundary cases.
def allowance(placements): return max(0, 2560000 - max(0, placements - 4090000))
assert allowance(0) == allowance(4090000) == 2560000
assert allowance(4090001) == 2559999 and allowance(4360000) == 2290000
assert allowance(6649999) == 1 and allowance(6650000) == allowance(7000000) == 0
assert 72000 - 24500 == 47500
assert 72000 + 8000 == 80000 and 72000 + 11250 == 83250
assert D(175000)*D('.25') + 24500 == 68250
assert D(1200)*D('.725') == 870 and D(1200)*D('.76') == 912
assert D(1200)*(D('.725')+D('.76')) == 1782
assert D(500000)*D('.10') + D(500000)*D('.03') == 65000
assert 500000 - 50000 == 450000 and D(500000)*D('.37') == 185000
assert D(1200000)*(D('.10')+D('.03')) == 156000
assert 1200000 - 120000 == 1080000 and D(1200000)*D('.35') == 420000
assert D(34500)*D('.124') == 4278
assert D(100000)*D('.029') == 2900 and D(50000)*D('.009') == 450
assert 4278 + 2900 + 450 == 7628

# Each fixture must be rejected by the same validator used on the real files.
fixtures = [
    (HIGH, 'not automatically added to wages or active S-Corp operating income', 'always added to all income', 'NIIT income character'),
    (EQUIP, 'permitted amended return', 'never an amended return', 'Section 179 election eligibility'),
    (TRUCK, 'do not infer a tax offset from the number of vehicles', 'unit count guarantees an offset', 'fleet recapture qualification'),
    (AIR, '$7,800', '$0', 'provider price preservation'),
    (AIR, '$75,000', '$99,000', 'existing client outcome preservation'),
    (AIR, '$2,560,000', '$1,220,000', 'stale Section 179'),
    (AIR, '72.5 cents', '67 cents', 'stale mileage'),
    (AIR, '$1,782', '$1,608', 'wrong mileage arithmetic'),
    (HIGH, '$72,000', '$69,000', 'stale retirement cap'),
    (HIGH, '$68,250', '$69,000', 'wrong compensation-dependent total'),
    (EQUIP, '$6,650,000', '$6,380,000', 'wrong phase-out endpoint'),
    (EQUIP, '$32,000', '$30,500', 'stale SUV cap'),
    (EQUIP, 'A true lease generally gives the lessee rent deductions', 'Every lease gives the lessee a purchase-price deduction', 'ownership eligibility'),
    (TRUCK, '$2,290,000', '$2,560,000', 'wrong fleet phase-out math'),
    (RET, '$184,500', '$176,100', 'stale Social Security base'),
    (RET, '$7,628', '$3,800', 'wrong employment-tax math'),
    (RET, '$47,500', '$50,000', 'annual additions overflow'),
]
negative=0
for path, old, new, label in fixtures:
    assert old in PAGES[path]
    bad=PAGES[path].replace(old,new)
    try: validate(path,bad)
    except AssertionError: negative+=1
    else: raise AssertionError(('fixture accepted',label))

extra=[]
base=PAGES[AIR]
extra.append((AIR,base.replace('rel="canonical" href="https://www.', 'rel="canonical" href="https://',1),'canonical host'))
# Target the actual canonical form rather than assuming attribute order.
if extra[-1][1] == base:
    extra[-1]=(AIR,re.sub(r'(<link\b[^>]*rel="canonical"[^>]*href=")https://www\.',r'\1https://',base,count=1),'canonical host')
extra.append((AIR,base.replace('id="buyer-limits-sources"','id="sources-missing"',1),'source section'))
extra.append((AIR,base.replace('href="/contact/"','href="/missing-navigation/"',1),'navigation'))
extra.append((AIR,re.sub(r'("datePublished"\s*:\s*")[^"]+',r'\g<1>2026-11-06',base,count=1),'publication'))
# Change only the JSON answer, leaving the visible FAQ intact.
extra.append((AIR,base.replace('"text": "Potentially. For 2026,','"text": "Wrong answer. For 2026,',1),'FAQ/schema'))
if args.built_output:
    extra.extend([
        (AIR, base.replace('>Upload My Documents</a>', '>Removed Upload Link</a>', 1), 'required build footer upload'),
        (AIR, base.replace('>Book a Call</a>', '>Unexpected Booking Caption</a>', 1), 'unexpected build navigation'),
        (AIR, base.replace('href="/business-owner-small-business-tax/"', 'href="/unexpected-consolidation-target/"', 1), 'unexpected consolidation destination'),
    ])
for path,bad,label in extra:
    assert bad != PAGES[path], ('fixture did not mutate',label)
    try: validate(path,bad)
    except AssertionError: negative+=1
    else: raise AssertionError(('fixture accepted',label))
print(f'PASS ({"built-output" if args.built_output else "source"}): {len(PAGES)} pages, {faq_total} synchronized FAQs, {links} retained/added links; {negative} negative fixtures rejected; statutory and dependent arithmetic checked.')
