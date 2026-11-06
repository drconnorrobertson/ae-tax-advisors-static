#!/usr/bin/env python3
"""Focused tax-copy, schema and preservation regression checks. Does not rebuild.

Use --baseline-root for an unmodified checkout, or --baseline-ref for a git
revision. --output-root can check built HTML after the normal release build.
The route cohort contains public release information only.
"""
import argparse
import ast
import html
import json
import re
import subprocess
import sys
from tax_review_build_normalization import normalize_baseline_html
from pathlib import Path
from html.parser import HTMLParser

REPO = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--baseline-root', type=Path)
parser.add_argument('--baseline-ref', default='f2d5962')
parser.add_argument('--output-root', type=Path, default=REPO)
parser.add_argument('--policy-root', type=Path, default=REPO)
parser.add_argument('--built-output', action='store_true', help='Allow only the exact documented release presentation/link transforms.')
parser.add_argument('--include-s-corp-illustrations', action='store_true',
    help='Validate the reviewed five-route numerical cohort with its dedicated math/price checks.')
args = parser.parse_args()
ROOT, POLICY = args.output_root.resolve(), args.policy_root.resolve()
cohort = json.loads((REPO / 'content/shared-tax-claims-20261106.json').read_text())
routes = [r for values in cohort['groups'].values() for r in values]
assert len(routes) == len(set(routes)) == 25
assert [len(v) for v in cohort['groups'].values()] == [19, 3, 3]
assert cohort['reviewed_date'] == '2026-11-06'
assert all(r.startswith('/') and r.endswith('/') and not r.startswith('/case-studies/') for r in routes)
illustration_routes = set()
if args.include_s_corp_illustrations:
    numerical = json.loads((REPO / 'content/s-corp-illustrations-20261106.json').read_text())
    illustration_routes = {r for values in numerical['groups'].values() for r in values}
    assert illustration_routes == {
        '/how-to-legally-reduce-self-employment-tax-through-entity-design/',
        '/s-corp-tax-strategies-high-net-worth-business-owners/',
        '/blog/late-s-corp-election-form-2553-strategies/',
        '/blog/can-i-get-a-refund-for-overpaying-self-employment-tax/',
        '/s-corp-vs-llc-tax-comparison-2026/',
    }
    assert illustration_routes.issubset(routes)
    # Numerical corrections have a separate review boundary. Never exempt them
    # without running their independent math, fee, case and FAQ checks.
    subprocess.run([sys.executable, str(REPO / 'scripts/test-s-corp-illustrations.py'),
        '--output-root', str(ROOT), '--policy-root', str(POLICY),
        '--baseline-ref', args.baseline_ref] + (['--built-output'] if args.built_output else []), check=True)
config = json.loads((POLICY / 'vercel.json').read_text())
holds = json.loads((POLICY / 'discovery_review_holds.json').read_text())

def baseline(path):
    if args.baseline_root:
        value = (args.baseline_root / path).read_text()
    else:
        value = subprocess.check_output(['git', 'show', args.baseline_ref + ':' + path], cwd=REPO, text=True)
    return normalize_baseline_html(value, POLICY, route="/" + path.removesuffix("index.html")) if args.built_output else value

def text(value):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', value))).strip()

def objects(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from objects(child)

def schemas(value):
    return list(objects([json.loads(raw) for raw in re.findall(
        r'<script\b[^>]*type=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script>', value, re.S)]))

def route_matches(pattern, route):
    if pattern == '/(.*)':
        return True
    if ':' in pattern:
        prefix = pattern.split(':', 1)[0]
        return route.startswith(prefix) or (pattern.endswith('*') and route.rstrip('/') == prefix.rstrip('/'))
    return pattern.rstrip('/') == route.rstrip('/')

class Page(HTMLParser):
    def __init__(self, value):
        super().__init__()
        self.canonical = []
        self.h1 = 0
        self.indexable = True
        self.feed(value)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'link' and 'canonical' in a.get('rel', '').split():
            self.canonical.append(a.get('href'))
        if tag == 'h1':
            self.h1 += 1
        if tag == 'meta' and a.get('name', '').lower() in ('robots', 'googlebot') and 'noindex' in a.get('content', '').lower():
            self.indexable = False
        if tag == 'meta' and a.get('http-equiv', '').lower() == 'refresh':
            self.indexable = False

shared_answer = ('An S election can reduce employment taxes on business profit remaining after reasonable compensation. '
                 'Income-tax results can also change, including through the Section 199A qualified business income deduction, '
                 'so compare the combined tax effect rather than assuming income tax is unchanged.')
old_scorp = [
    'The election reduces employment tax only', 'It is not a saving on income tax.',
    'An S election does not reduce income tax.', 'It reduces employment tax only.',
    'The election saves employment tax only, never income tax.',
    'The saving is confined to payroll tax', 'Income tax does not change.',
    'An S-corp election saves payroll tax only', 'it does not reduce income tax.',
]
old_3115 = [
    'Form 3115 has no statute of limitations', 'Form 3115 is not subject to the three-year or two-year window',
    'There is no statute of limitations restriction', 'there is no statute of limitations concern',
    'Form 3115 is required for changes in accounting method and has no time limit',
    'You claim everything in the current year with no amendments.',
    'Cost segregation catch-up depreciation changes are automatic changes.',
    'No additional audit risk on closed years.',
    'unlocks every dollar of missed accelerated depreciation in a single tax year.',
    'The adjustment must account for depreciation actually claimed, not depreciation allowable.',
]
changed_answers = 0
checked_answers = 0
changed_blocks = 0
unchanged_preexisting_schema_summaries = 0
for route in routes:
    path = route.strip('/') + '/index.html'
    current = (ROOT / path).read_text()
    old = baseline(path)
    page = Page(current)
    assert page.canonical == ['https://www.aetaxadvisors.com' + route], route
    assert page.canonical == Page(old).canonical and page.h1 == 1 and page.indexable, route
    assert route not in holds, route + ' is on discovery hold'
    assert not any(route_matches(r['source'], route) for r in config.get('redirects', [])), route + ' redirects'
    for rule in config.get('headers', []):
        if route_matches(rule['source'], route):
            assert not any(h['key'].lower() == 'x-robots-tag' and 'noindex' in h['value'].lower() for h in rule['headers']), route
    old_schema, new_schema = schemas(old), schemas(current)
    assert [x['datePublished'] for x in old_schema if 'datePublished' in x] == [x['datePublished'] for x in new_schema if 'datePublished' in x], route
    assert re.findall(r'<meta[^>]*property="article:published_time"[^>]*>', old) == re.findall(r'<meta[^>]*property="article:published_time"[^>]*>', current), route
    modified = [x['dateModified'] for x in new_schema if 'dateModified' in x]
    assert modified and set(modified) == {cohort['reviewed_date']}, route
    assert all(x.startswith(cohort['reviewed_date']) for x in re.findall(r'article:modified_time" content="([^"]+)', current)), route
    assert all(x == cohort['reviewed_date'] for x in re.findall(r'Updated (\d{4}-\d\d-\d\d)', current)), route
    # Compare actual values and order, not a fixed list of known prices.
    dollars = lambda s: [x.rstrip('.,') for x in re.findall(r'\$\s*\d[\d,.]*(?:\s*(?:million|billion|thousand))?', html.unescape(s))]
    if route not in illustration_routes:
        assert dollars(old) == dollars(current), route + ' dollar sequence changed'
    for historical in re.findall(r'<a\b[^>]*href="[^"]*/case-studies/[^"]*"[^>]*>.*?</a>', old, re.S):
        assert current.count(historical) == old.count(historical), route + ' historical case link changed'
    # Navigation, tables, provider quotations and all old links remain intact.
    for tag in ('table', 'blockquote'):
        assert re.findall(fr'<{tag}\b[^>]*>.*?</{tag}>', old, re.S) == re.findall(fr'<{tag}\b[^>]*>.*?</{tag}>', current, re.S), (route, tag)
    old_links = re.findall(r'<a\b[^>]*>.*?</a>', old, re.S)
    for link in old_links:
        assert current.count(link) == old.count(link), (route, 'old link altered', link)
    # FAQ schema can describe adjacent prose rather than a separate FAQ section.
    visible = text(re.sub(r'<script\b[^>]*>.*?</script>', '', current, flags=re.S))
    old_questions = {x['name']:x['acceptedAnswer']['text'] for x in old_schema if x.get('@type') == 'Question'}
    new_questions = {x['name']:x['acceptedAnswer']['text'] for x in new_schema if x.get('@type') == 'Question'}
    assert old_questions.keys() == new_questions.keys(), route
    old_visible = text(re.sub(r'<script\b[^>]*>.*?</script>', '', old, flags=re.S))
    for question, answer in new_questions.items():
        changed = old_questions[question] != answer
        was_verbatim = text(question) in old_visible and text(old_questions[question]) in old_visible
        if changed or was_verbatim:
            assert text(question) in visible and text(answer) in visible, (route, 'FAQ parity', question)
            checked_answers += 1
        else:
            # Some legacy service schema summarizes prose instead of quoting it.
            # This focused correction preserves those untouched answers exactly.
            assert old_questions[question] == answer, (route, question)
            unchanged_preexisting_schema_summaries += 1
        if route not in illustration_routes:
            changed_answers += changed
    # Compare visible block positions to detect unexpected block insertions/deletions.
    old_body = re.sub(r'<script\b[^>]*>.*?</script>', '', old, flags=re.S)
    new_body = re.sub(r'<script\b[^>]*>.*?</script>', '', current, flags=re.S)
    blocks = lambda s: [text(x) for x in re.findall(r'<(?:p|li)\b[^>]*>.*?</(?:p|li)>', s, re.S)]
    before, after = blocks(old_body), blocks(new_body)
    if route not in illustration_routes:
        assert len(before) == len(after), route + ' block count changed'
    delta = [(a,b) for a,b in zip(before,after) if a != b and not a.startswith('By AE Tax Advisors Team')]
    if route not in illustration_routes:
        changed_blocks += len(delta)
    old_claims = old_3115 if route in cohort['groups']['form_3115'] else old_scorp
    for claim in old_claims:
        assert claim not in text(current), (route, 'stale claim', claim)
    if route in cohort['groups']['s_corp_shared_faq']:
        assert new_questions['Does an S-Corp election reduce income tax?'] == shared_answer, route
        if route not in illustration_routes:
            assert len(delta) == 1, route
    if route in cohort['groups']['form_3115']:
        assert 'open and closed' in visible and 'filing deadlines' in visible and 'deduction limits' in visible, route
        assert 'https://www.irs.gov/irb/2025-24_IRB#REV-PROC-2025-23' in current, route
assert changed_answers == (18 if illustration_routes else 23), changed_answers
assert changed_blocks == (40 if illustration_routes else 48), changed_blocks

# Review follow-up: distinguish allocated income from cash distributions and
# independently compare SE tax with employer/employee payroll tax.
strategy = (ROOT / 's-corp-tax-strategy/index.html').read_text()
assert "Wages and allocated business income generally enter the owner's income-tax calculation" in strategy
assert 'Both streams remain subject to ordinary income tax.' not in strategy
comparison = (ROOT / 's-corp-vs-llc-tax-comparison-2026/index.html').read_text()
assert 'The saving is therefore 15.3% of the amount characterized as distribution' not in comparison
for phrase in ('92.35%', 'employer and employee payroll taxes', 'Social Security wage base', 'applicable Medicare taxes'):
    assert phrase in comparison, phrase
catchup = (ROOT / 'blog/form-3115-cost-segregation-catch-up/index.html').read_text()
assert 'Form 3115 is the required filing to make that change legally and correctly.' not in catchup
assert catchup.count('Errors, first-year corrections and late or revoked elections') == 2
lookback = (REPO / 'content_posts_a.py').read_text().split('"slug": "form-3115-cost-segregation-lookback"', 1)[1].split('# ---------------------------------------------------------------- 5', 1)[0]
for stale in ('Neither is true here.', 'and it qualifies for automatic consent.', 'No, and generally you cannot.',
              'A late partial disposition election is itself an automatic change', 'Automatic consent applies, so',
              'lets you claim every missed deduction', 'with no three-year limit.'):
    assert stale not in lookback, stale
# Source protection without importing/executing generators.
for filename in ('seo_topics.py', 'content_posts_c.py', 'cluster_c1.py', 'build_tools.py', 'content_posts_a.py'):
    source = (REPO / filename).read_text()
    ast.parse(source)
    for phrase in ('reduces employment tax only, never income tax', 'An S election does not reduce income tax.',
                   'no statute of limitations cap', 'no statute of limitations problem'):
        assert phrase not in source, (filename, phrase)
for filename in ('seo_topics.py', 'content_posts_c.py'):
    assert shared_answer in (REPO / filename).read_text(), filename

# All case-study files and generators must remain identical to the baseline.
protected = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', args.baseline_ref,
    '--', 'case-studies', 'case_engine.py', 'case_data.py'], cwd=REPO, text=True).splitlines()
for filename in protected:
    assert (REPO / filename).read_bytes() == subprocess.check_output(['git', 'show', args.baseline_ref + ':' + filename], cwd=REPO), filename
print(f'PASS: 25 active canonical routes; {changed_blocks} visible corrections and {changed_answers} changed FAQ answers outside {len(illustration_routes)} separately tested numerical routes; {checked_answers} verbatim FAQ answers checked ({unchanged_preexisting_schema_summaries} legacy summaries unchanged); prices, publication, cases, tables and existing links preserved; five source modules parse.')
