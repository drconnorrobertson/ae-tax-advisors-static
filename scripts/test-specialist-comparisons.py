#!/usr/bin/env python3
"""Check the Nov 6 specialist comparison cohort without building or publishing.

Data and unchanged-scope checks use the verified original commit, not mutable HEAD.
The pricing generator is inspected through selected AST nodes; it is never run.
"""
from pathlib import Path
from html.parser import HTMLParser
import ast
import copy
import html
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASELINE = 'f2d5962a0b96bf7b9933bf1c764ed7778b6eea88'
COHORT = 'content/specialist-comparisons-20261106/routes.json'
ROUTES = json.loads((ROOT / COHORT).read_text())
CSA = 'cost-segregation-authority'
EXPECTED = {
    '/compare/cost-seg-authority-vs-ae-tax/': '2026-08-10',
    '/compare/cost-segregation-authority-pricing/': '2026-10-08',
    '/compare/cost-segregation-authority-alternatives/': '2026-09-28',
    '/compare/capstan-tax-strategies-vs-ae-tax/': '2026-08-15',
    '/compare/engineered-tax-services-vs-ae-tax/': '2026-08-11',
}

def baseline(path):
    return subprocess.check_output(['git', 'show', BASELINE + ':' + path], cwd=ROOT).decode()

def plain(s):
    return ' '.join(html.unescape(re.sub('<[^>]*>', ' ', s)).split())

def schema(s):
    return [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', s, re.S)]

def price_card(s):
    return re.search(r'<section\b[^>]*id="competitor-price-review"[^>]*>.*?</section>', s, re.S)[0]

class BalancedMain(HTMLParser):
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
    def __init__(self):
        super().__init__()
        self.stack = []
        self.ids = []
    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID:
            self.stack.append(tag)
        if 'id' in dict(attrs):
            self.ids.append(dict(attrs)['id'])
    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, f'Unbalanced {tag}: {self.stack}'
        self.stack.pop()

assert set(ROUTES) == set(EXPECTED) and len(ROUTES) == 5
pages = {}
for route in ROUTES:
    rel = route.strip('/') + '/index.html'
    s = (ROOT / rel).read_text()
    pages[route] = s
    old = baseline(rel)
    main = re.search(r'<main\b[^>]*>(.*?)</main>', s, re.S)[1]
    canonical = 'https://www.aetaxadvisors.com' + route
    assert re.findall(r'<link rel="canonical" href="([^"]+)"', s) == [canonical]
    assert re.findall(r'<link rel="canonical"[^>]*>', s) == re.findall(r'<link rel="canonical"[^>]*>', old)
    assert re.findall(r'<meta property="article:published_time"[^>]*>', s) == re.findall(r'<meta property="article:published_time"[^>]*>', old)
    assert 'noindex' not in s.lower()
    assert len(re.findall(r'<h1\b', main)) == 1
    parser = BalancedMain()
    parser.feed(main)
    assert not parser.stack and len(parser.ids) == len(set(parser.ids))
    data = schema(s)
    articles = [x for x in data if x.get('@type') == 'Article']
    faqs = [x for x in data if x.get('@type') == 'FAQPage']
    assert len(articles) == len(faqs) == 1
    article, faq = articles[0], faqs[0]
    assert article['datePublished'] == EXPECTED[route]
    assert article['dateModified'] == '2026-11-06'
    assert article['url'] == canonical and article['mainEntityOfPage']['@id'] == canonical
    assert article['mainEntityOfPage']['dateModified'] == '2026-11-06'
    assert article['headline'] == plain(re.search(r'<h1[^>]*>(.*?)</h1>', main, re.S)[1])
    for name in ('description', 'og:description', 'twitter:description'):
        assert html.unescape(re.search(r'<meta (?:name|property)="' + name + r'" content="([^"]*)"', s)[1]) == article['description']
    title = html.unescape(re.search(r'<title>(.*?)</title>', s)[1])
    assert len(title) <= 70 and 110 <= len(article['description']) <= 170
    for name in ('og:title', 'twitter:title'):
        assert html.unescape(re.search(r'<meta (?:name|property)="' + name + r'" content="([^"]*)"', s)[1]) == title
    assert 'content="2026-11-06T00:00:00-06:00"' in s
    assert 'Updated November 6, 2026' in main
    assert len(faq['mainEntity']) == 5
    visible = re.search(r'<section[^>]*id="faq"[^>]*>(.*?)</section>', main, re.S)[1]
    assert [(plain(q), plain(a)) for q, a in re.findall(r'<h3>(.*?)</h3><p>(.*?)</p>', visible, re.S)] == [(q['name'], q['acceptedAnswer']['text']) for q in faq['mainEntity']]
    assert article['citation'] and any('irs.gov' in u for u in article['citation'])
    for u in article['citation']:
        assert 'href="' + u + '"' in main, f'Citation not visible: {u}'
    for link in re.findall(r'href="([^"]+)"', main):
        if not link.startswith('/'):
            continue
        target, _, fragment = link.partition('#')
        path = ROOT / target.strip('/')
        if path.is_dir():
            path /= 'index.html'
        assert path.is_file(), f'Missing destination: {route} -> {link}'
        if fragment:
            assert f'id="{fragment}"' in path.read_text(), f'Missing fragment: {link}'
    assert '/cost-seg-discovery/' in main and '/pricing/' in main
    assert '$7,800' in main and 'separately scoped and priced' in main
    assert 'Form 3115' in main and ('prior-year' in main.lower() or 'older property' in main.lower())
    assert not any(x.lower() in main.lower() for x in ('IRS-approved', 'guaranteed savings', 'audit-proof', 'guaranteed refund', 'no audit risk'))
    assert len(re.findall(r'id="competitor-price-review"', s)) == 1
    print('PASS:', route, 'metadata, dates, canonical, 5 identical visible/schema FAQs, sources, internal links, balanced HTML')

# Published CSA study price and old AE budget remain clearly separate on all three routes.
for route in ROUTES[:3]:
    main = re.search(r'<main\b[^>]*>(.*?)</main>', pages[route], re.S)[1]
    assert 'Studies begin at $3,000' in main
    assert 'Published starting study fee' in main
    assert 'CSA starting study fee verified November 6, 2026.' in main
    assert 'Historical AE comparable-work budget, reviewed October 24, 2026' in main
    assert '$2,500–$5,000+ per property study' in main
    assert 'not a published CSA fee or quote' in main
    assert 'A numeric fee for Cost Segregation Authority was not verified' not in main
    for source in ('https://csap.com/', 'https://csap.com/cost-segregation/', 'https://csap.com/about-us/', 'https://csap.com/terms-of-service/'):
        assert 'href="' + source + '"' in main
    assert 'does not prepare' in plain(main)

# Preserve other specialist budgets byte-for-byte, including their old review dates.
for route in ROUTES[3:]:
    rel = route.strip('/') + '/index.html'
    assert price_card(pages[route]) == price_card(baseline(rel))
    assert '$2,500–$5,000+ per property study' in price_card(pages[route])
for route in (ROUTES[0], ROUTES[3], ROUTES[4]):
    s = pages[route]
    for fee in ('$7,800', '$9,800', '$1 per square foot', '$2,000 minimum', '1,500-square-foot', '3,000-square-foot', '$3,000 base price'):
        assert fee in s
    assert max(1500 * 1, 2000) == 2000
    assert max(3000 * 1, 2000) == 3000
for route in ROUTES[1:3]:
    assert '$3,900' in pages[route] and '30 days apart' in pages[route]
assert 3900 * 2 == 7800
assert 'id="provider-review"' in pages[ROUTES[2]]
assert 'repair' in pages[ROUTES[3]].lower() and 'partial disposition' in pages[ROUTES[3]].lower()
assert 'June 30, 2026' in pages[ROUTES[4]]
assert 'construction begins after June 30, 2026' in pages[ROUTES[4]]
assert 'homes acquired after June 30, 2026' in pages[ROUTES[4]]
assert 'not blanket deadlines for cost segregation studies' in pages[ROUTES[4]]
print('PASS: distinct buyer decisions, unchanged AE prices and other specialist budget cards, arithmetic, and dated energy eligibility')

# Exact byte comparison outside the CSA record, not just equivalent JSON values.
def without_csa_record(raw):
    slug_index = raw.index('"slug": "' + CSA + '"')
    start = raw.rfind('{', 0, slug_index)
    _, length = json.JSONDecoder().raw_decode(raw[start:])
    return raw[:start] + '{}' + raw[start + length:]

current_rows = None
for rel in ('compare/competitor-pricing/prices.json', 'content/vendor-pricing-20261024.json'):
    raw = (ROOT / rel).read_text()
    old_raw = baseline(rel)
    assert without_csa_record(raw) == without_csa_record(old_raw), f'Other data changed: {rel}'
    data, old_data = json.loads(raw), json.loads(old_raw)
    if isinstance(data, dict):
        assert data['reviewed'] == old_data['reviewed'] == '2026-10-24'
        data, old_data = data['providers'], old_data['providers']
    assert len(data) == len(old_data) == 100
    record = next(r for r in data if r['slug'] == CSA)
    old = next(r for r in old_data if r['slug'] == CSA)
    assert record['kind'] == 'published' and record['fee'] == 'Studies begin at $3,000'
    assert record['source'] == 'https://csap.com/cost-segregation/'
    assert record['reviewed'] == record['sourceVerifiedAsOf'] == '2026-11-06'
    assert record['status'] == 'Published starting study fee'
    assert 'not tax advisory or return preparation' in record['qualification']
    for k in ('fee', 'qualification', 'reviewed', 'estimateBasis', 'benchmarkSources'):
        assert record['historicalComparableBudget'][k] == old[k]
    if current_rows is not None:
        assert data == current_rows
    current_rows = data
assert (ROOT / 'content/vendor-pricing-20261008.json').read_bytes() == baseline('content/vendor-pricing-20261008.json').encode()
print('PASS: only CSA changed in both pricing datasets; all other bytes and October 8 historical snapshot unchanged')

# Test renderer and normalization in isolation without executing filesystem-writing code.
def render_namespace(source):
    tree = ast.parse(source)
    ns = {'html': html, 're': re, 'json': json, 'E': html.escape, 'DATE': '2026-10-24'}
    chosen = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in ('p', 'section', 'anchors', 'card', 'metadata')]
    exec(compile(ast.Module(body=chosen, type_ignores=[]), 'isolated-renderer', 'exec'), ns)
    return tree, ns

rel = 'scripts/refresh-competitor-pricing.py'
tree, current = render_namespace((ROOT / rel).read_text())
_, previous = render_namespace(baseline(rel))
for r in current_rows:
    output = current['card'](r)
    if r['slug'] != CSA:
        assert output == previous['card'](r), 'Renderer changed for ' + r['slug']
    else:
        assert 'Studies begin at $3,000' in output and 'not verified' not in output
        assert '$2,500–$5,000+' in output and 'Historical AE comparable-work budget' in output
        assert 'November 6, 2026' in output and 'October 24, 2026' in output
        for route in ROUTES[:3]:
            assert price_card(pages[route]) == output
        transformed = current['metadata'](pages[ROUTES[0]], [r['source']], r['reviewed'])
        assert next(x for x in schema(transformed) if x.get('@type') == 'Article')['dateModified'] == '2026-11-06'
# The first row loop must preserve the later CSA verification and published kind.
loop = next(n for n in tree.body if isinstance(n, ast.For))
record = copy.deepcopy(next(r for r in current_rows if r['slug'] == CSA))
loop_ns = {'rows': [record], 'DATE': '2026-10-24'}
exec(compile(ast.Module(body=[loop], type_ignores=[]), 'isolated-CSA-normalization', 'exec'), loop_ns)
assert record == next(r for r in current_rows if r['slug'] == CSA)
print('PASS: current generator retains CSA published price, evidence dates, and historical budget; other 99 card outputs unchanged')

# Keep the visible directory synchronized with its current JSON without rerendering
# the 99 unrelated rows or relabeling the historical directory-wide review.
directory_rel = 'compare/competitor-pricing/index.html'
directory = (ROOT / directory_rel).read_text()
old_directory = baseline(directory_rel)
def directory_rows(source):
    result = {}
    for row in re.findall(r'<tr data-provider=.*?</tr>', source, re.S):
        href = re.search(r'<th scope="row"><a href="([^"]+)"', row)[1]
        result[href] = row
    return result
visible_rows, old_visible_rows = directory_rows(directory), directory_rows(old_directory)
assert len(visible_rows) == len(old_visible_rows) == 100
assert set(visible_rows) == set(old_visible_rows)
csa_path = '/compare/cost-segregation-authority-pricing/'
for path, row in visible_rows.items():
    if path != csa_path:
        assert row == old_visible_rows[path], f'Unrelated directory row changed: {path}'
    record = next(r for r in current_rows if r['path'] == path)
    assert 'data-kind="' + record['kind'] + '"' in row
    assert '<td>' + html.escape(record['fee']) + '</td>' in row
csa_row = visible_rows[csa_path]
assert 'data-kind="published"' in csa_row
assert 'data-provider="cost segregation authority costseg studies begin at $3,000 cost segregation"' in csa_row
assert 'Published starting study fee' in csa_row
assert 'Study only; scope and quote vary. Verified November 6, 2026.' in csa_row
assert 'href="https://csap.com/cost-segregation/"' in csa_row
assert '$2,500' not in csa_row and 'AE budget estimate' not in csa_row
published_count = sum(r['kind'] == 'published' for r in current_rows)
assert published_count == 37
assert f'100 providers: {published_count} with sourced published prices and {100-published_count} with AE budget estimates' in directory
assert 'Directory-wide review: October 24, 2026. CSA Partners’ starting study fee was separately verified and updated November 6, 2026.' in directory
assert 'reviewed on October 24, 2026, except CSA Partners’ starting study fee, separately verified November 6, 2026.' in directory
# Preserve publication and all other head metadata while recording the actual
# directory modification. The visible review note still distinguishes old evidence.
def normalized_head(source):
    head = source.split('</head>')[0]
    head = re.sub(r'(<meta property="article:modified_time" content=")[^"]*', lambda m: m[1]+'MODIFIED', head)
    def schema(match):
        data=json.loads(match[1])
        def walk(value):
            if isinstance(value,dict):
                if 'dateModified' in value: value['dateModified']='MODIFIED'
                for child in value.values(): walk(child)
            elif isinstance(value,list):
                for child in value: walk(child)
        walk(data)
        return '<script type="application/ld+json">'+json.dumps(data,sort_keys=True)+'</script>'
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', schema, head, flags=re.S)
assert normalized_head(directory)==normalized_head(old_directory)
assert 'article:modified_time" content="2026-11-06' in directory

# Execute only the pure intro and directory-row assembly AST. No generator file IO.
def directory_render(source, records):
    parsed, ns = render_namespace(source)
    labels = next(n for n in parsed.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'LABELS' for t in n.targets))
    ns['LABELS'] = ast.literal_eval(labels.value)
    ns['rows'] = records
    ns['published'] = sum(r['kind'] == 'published' for r in records)
    ns['coverage'] = {r['slug']: r for r in json.loads((ROOT / '_gen/competitor-coverage-20261008.json').read_text())['brands']}
    ns['table_rows'] = []
    intro = next(n for n in parsed.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'intro' for t in n.targets))
    loop = next(n for n in parsed.body if isinstance(n, ast.For) and any(isinstance(c, ast.Call) and isinstance(c.func, ast.Attribute) and isinstance(c.func.value, ast.Name) and c.func.value.id == 'table_rows' and c.func.attr == 'append' for c in ast.walk(n)))
    exec(compile(ast.Module(body=[intro, loop], type_ignores=[]), 'isolated-directory-renderer', 'exec'), ns)
    return ns['intro'], directory_rows(''.join(ns['table_rows']))

current_source = (ROOT / rel).read_text()
intro, generated_rows = directory_render(current_source, current_rows)
_, old_generated_rows = directory_render(baseline(rel), current_rows)
assert '100 providers: 37 with sourced published prices and 63 with AE budget estimates' in intro
assert 'Directory-wide review: October 24, 2026.' in intro
assert 'CSA Partners’ starting study fee was separately verified and updated November 6, 2026.' in intro
for path in generated_rows:
    if path != csa_path:
        assert generated_rows[path] == old_generated_rows[path], f'Unrelated generated row changed: {path}'
assert 'Studies begin at $3,000' in generated_rows[csa_path]
assert 'data-kind="published"' in generated_rows[csa_path]
assert 'Study only; scope and quote vary. Verified November 6, 2026.' in generated_rows[csa_path]
assert 'href="https://csap.com/cost-segregation/"' in generated_rows[csa_path]
assert 'reviewed on October 24, 2026, except CSA Partners’ starting study fee, separately verified November 6, 2026.' in current_source
print('PASS: visible directory and generator agree on CSA price, evidence, date exception and 37/63 counts; other 99 rows unchanged')

# Preserve the production guard's exact search identity and sourced service facts.
facts_rel = 'content/comparison-source-corrections-20261024.json'
facts = json.loads((ROOT / facts_rel).read_text())
assert (ROOT / facts_rel).read_text() == baseline(facts_rel)
for route, slug in [(ROUTES[0], 'cost-segregation-authority'), (ROUTES[3], 'capstan-tax-strategies'), (ROUTES[4], 'engineered-tax-services')]:
    s = pages[route]
    title = html.unescape(re.search(r'<title>(.*?)</title>', s, re.S)[1])
    h1 = plain(re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)[1])
    assert 'vs AE Tax Advisors' in title and 'vs AE Tax Advisors' in h1
    assert title == h1
    main = re.search(r'<main\b[^>]*>(.*?)</main>', s, re.S)[1]
    assert '<p>' + html.escape(facts[slug]['offering']) + '</p>' in main
    assert 'href="' + facts[slug]['source'] + '"' in main
    assert 'guaranteed tax result' in main or 'particular tax result is guaranteed' in main or 'not a promise that every service is included' in main
print('PASS: direct-comparison title/H1 identities and unchanged verified official service summaries satisfy production content guard')
