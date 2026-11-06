#!/usr/bin/env python3
"""Check the nine metadata-only buyer snippet edits and retained generators.

Usage: python3 scripts/test-buyer-snippets.py [--root REPO]
       python3 scripts/test-buyer-snippets.py --root REPO/public --built-output --policy-root REPO

Frozen source hashes mask only search/social descriptions and Article-family
schema descriptions. This intentionally does NOT mask WebApplication descriptions:
the tax-savings calculator's separate model disclaimer must remain unchanged.
The public cohort is routes.json, not pages.json, to avoid changing review dates.
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse, ast, hashlib, html, importlib.util, json, re, tempfile, subprocess

SPECS = {'/business-owner-tax-calculator/': {'description': 'Compare 2026 federal income-tax scenarios for '
                                                    'an owner with business income and rentals '
                                                    'using a reviewed taxable-income change. See '
                                                    'preparer handoff steps.',
                                     'meta_count': 2,
                                     'article_types': ['BlogPosting'],
                                     'normalized_sha256': 'fb9939e296c6b32b71a97b147b8fd6fad82fd90c27bdcc17ebdb815f3b6cca10',
                                     'body_normalized_sha256': '68622f93e344228f90db53abc63ff7c19c94c43223de3c8670e57d9e9965f762'},
 '/tax-savings-calculator/': {'description': 'Estimate the 2026 federal ordinary-income tax '
                                             'difference from a reviewed deduction across tax '
                                             'brackets. This scenario tool does not calculate '
                                             'refunds.',
                              'meta_count': 3,
                              'article_types': ['Article'],
                              'normalized_sha256': 'ec60569de930907821f1304a16ffbf675c596e47606a8863576ba0e87b123ae2',
                              'body_normalized_sha256': '04d95b82befc5e4c4763edcf1d66a7a462afa9b727171652fc640b233c23543b'},
 '/compare/business-owner-provider-shortlists/': {'description': 'Compare tax providers for '
                                                                 'business owners by planning, '
                                                                 'accounting, return preparation '
                                                                 'and specialist scope. Review '
                                                                 'sourced profiles and shortlist '
                                                                 'questions.',
                                                  'meta_count': 3,
                                                  'article_types': ['Article'],
                                                  'normalized_sha256': 'b1486e45489158c40369a73eb223b982e4530084d59e44bb1b5ff0a28786c3d8',
                                                  'body_normalized_sha256': 'eea27773ec30f5493ae39bbed9ecc719b8169db140608f4ac87d70c83242f0e8'},
 '/compare/high-income-provider-shortlists/': {'description': 'Compare tax advisors for '
                                                              'high-income professionals and '
                                                              'owners across tax planning, wealth '
                                                              'coordination and rental needs using '
                                                              'sourced service profiles.',
                                               'meta_count': 3,
                                               'article_types': ['Article'],
                                               'normalized_sha256': '702bde714d242df69a4972b6b942aa06b7b77d03adbe71238adf663a174cb3a5',
                                               'body_normalized_sha256': '3bd569a9833ed593b1b7368a75faa3480b94787ed70ea4e535ae25a19ae5f7f2'},
 '/compare/provider-comparison-library/': {'description': 'Search tax provider profiles and '
                                                          'firm-to-firm comparisons by service '
                                                          'model. Use official sources and scope '
                                                          'questions to build your advisor '
                                                          'shortlist.',
                                           'meta_count': 3,
                                           'article_types': ['Article'],
                                           'normalized_sha256': '3ba76de4fa911fa371df9802dae8d10ead19a014ec7a639ff66bbde4c9bd9f63',
                                           'body_normalized_sha256': 'e0d0c9c67f4128a331809c9e8d9e65b8f8da7c68498cb9b829701f15ccbbd86d'},
 '/compare/real-estate-study-provider-shortlists/': {'description': 'Compare real estate tax '
                                                                    'advisors and cost segregation '
                                                                    'study providers by service '
                                                                    'scope, CPA coordination and '
                                                                    'filing responsibilities '
                                                                    'before requesting proposals.',
                                                     'meta_count': 3,
                                                     'article_types': ['Article'],
                                                     'normalized_sha256': '07174b4d09823d2da2a82c04d8a0b0ff6dac9c12b381c8dcbc0f134fbb16455f',
                                                     'body_normalized_sha256': '2789f7e59b6d34ae9027d1d5cbcb1eb5d93eb37e213232fccde3eb024ecc6c40'},
 '/compare/physician-business-real-estate-tax-advisors/': {'description': 'Compare tax advisors '
                                                                          'for physicians with '
                                                                          'practice, locum or '
                                                                          'rental income. Review '
                                                                          'coordination needs, '
                                                                          'implementation scope '
                                                                          'and questions to ask '
                                                                          'each firm.',
                                                           'meta_count': 3,
                                                           'article_types': ['Article'],
                                                           'normalized_sha256': '81185043cd43c6509150e9eb9ae380f3e85eefa8f6a6379913a632fefa1e2f5a',
                                                           'body_normalized_sha256': 'fe0f0886631b875234472c9673aa9b481563383f9d4bb7c1bce02b9d72e13ecc'},
 '/compare/tax-planning-implementation-firms/': {'description': 'Compare tax planning firms by '
                                                                'implementation support, preparer '
                                                                'handoffs and filing '
                                                                'responsibilities. Identify who '
                                                                'carries out each step before '
                                                                'hiring.',
                                                 'meta_count': 3,
                                                 'article_types': ['Article'],
                                                 'normalized_sha256': 'd3b0b16293ed8b4d98abfcaccc862052376602057e03112b881f9c4b31d17696',
                                                 'body_normalized_sha256': '27d44d625d5d8d8b063ec67140f8cd7afbd76db57f4a8b02a623ebd8cb6f3061'},
 '/compare/tax-strategy-accounting-cfo-firms/': {'description': 'Compare tax strategy, accounting '
                                                                'and CFO firms for owners and '
                                                                'growing businesses. Separate '
                                                                'planning projects from monthly '
                                                                'books, reporting and forecasts.',
                                                 'meta_count': 3,
                                                 'article_types': ['Article'],
                                                 'normalized_sha256': '5b1fabd19e004fbd69ea4a07702c6143c5ef4767f635e8820bac5125e9533719',
                                                 'body_normalized_sha256': '6065ac1dc3169aad7678dbaa440f0578f50a4b26d0826e8b8f6f53b24f1eceee'}}
ARTICLE_TYPES = {'Article', 'BlogPosting', 'NewsArticle'}
MODEL_DESCRIPTION = 'Compare baseline and proposed 2026 taxable ordinary income using reviewed deductions. No assumed strategy eligibility, payroll savings or amendment refunds.'
SCHEMA = re.compile(r'(<script\b[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)', re.S)
META = re.compile(r'(<meta\s+(?:name|property)="(?:description|og:description|twitter:description)"\s+content=")[^"]*(")')
JSON_DESCRIPTION = re.compile(r'("description"\s*:\s*)"(?:\\.|[^"\\])*"')

class Tags(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.meta = {}; self.canonicals = []
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta':
            key = attrs.get('name', attrs.get('property', ''))
            self.meta.setdefault(key, []).append(attrs.get('content', ''))
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs.get('href'))

def normalize(source):
    source = META.sub(lambda m: m[1] + '__SEARCH_DESCRIPTION__' + m[2], source)
    def normalize_article(m):
        data = json.loads(m[2])
        if not isinstance(data, dict) or data.get('@type') not in ARTICLE_TYPES:
            return m[0]
        content, count = JSON_DESCRIPTION.subn(lambda d: d[1] + '"__SEARCH_DESCRIPTION__"', m[2], count=1)
        assert count == 1, 'Article-family description missing'
        return m[1] + content + m[3]
    return SCHEMA.sub(normalize_article, source)

def sha(source):
    return hashlib.sha256(source.encode()).hexdigest()

def validate(route, source, expected_hash=None, expected_body_hash=None):
    spec = SPECS[route]; desc = spec['description']; tags = Tags(source)
    keys = ['description', 'og:description', 'twitter:description']
    actual_keys = [key for key in keys if key in tags.meta]
    assert len(actual_keys) == spec['meta_count'], (route, 'search/social tag count')
    assert all(tags.meta[key] == [desc] for key in actual_keys), (route, 'search/social mismatch or duplicate')
    assert tags.canonicals == ['https://www.aetaxadvisors.com' + route], (route, 'canonical')
    for key in ['robots', 'googlebot']:
        assert all('noindex' not in value.lower() for value in tags.meta.get(key, [])), (route, 'not indexable')
    article_types = []; applications = []
    for m in SCHEMA.finditer(source):
        data = json.loads(m[2])
        if isinstance(data, dict) and data.get('@type') in ARTICLE_TYPES:
            article_types.append(data['@type'])
            assert data['description'] == desc, (route, 'Article-family mismatch')
        if isinstance(data, dict) and data.get('@type') == 'WebApplication':
            applications.append(data)
    assert article_types == spec['article_types'], (route, 'Article-family schema changed')
    if route == '/tax-savings-calculator/':
        assert len(applications) == 1, 'Calculator application schema missing'
        # Keep the explicit model-scope disclaimer even though the search snippet differs.
        assert applications[0]['description'] == MODEL_DESCRIPTION, 'Calculator model disclaimer changed'
        assert applications[0]['description'] != desc, 'Do not sync the search snippet over the model disclaimer'
    normalized = normalize(source)
    assert sha(normalized) == (expected_hash or spec['normalized_sha256']), (route, 'non-description bytes changed')
    body = re.search(r'<body\b.*?</body>', normalized, re.S)
    assert body, (route, 'body missing')
    assert sha(body[0]) == (expected_body_hash or spec['body_normalized_sha256']), (route, 'body changed')

def test_generators(root):
    # Execute only isolated save functions with fake templates. Never run a generator.
    class Template:
        SITE = 'https://www.aetaxadvisors.com'
        def article_schema(self, **kw): return kw
        def breadcrumb_schema(self, trail): return {'trail': trail}
        def page_header(self, **kw): return 'VISIBLE:' + kw['subtitle']
        def build_page(self, **kw): self.output = kw; return 'markup'
        def write_page(self, *args): pass
    sources = [
        ('scripts/build_provider_comparisons_20261011.py', 'HUB_SEARCH_DESCRIPTIONS',
         [r for r in SPECS if 'provider-shortlists' in r or 'provider-comparison-library' in r]),
        ('scripts/competitor_name_search_20261001.py', 'GUIDE_SEARCH_DESCRIPTIONS',
         [r for r in SPECS if r.startswith('/compare/') and 'provider-' not in r]),
    ]
    for rel, constant, routes in sources:
        tree = ast.parse((root / rel).read_text())
        assignments = [n for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == constant for t in n.targets)]
        assert len(assignments) == 1, (rel, 'metadata source missing')
        mapping = ast.literal_eval(assignments[0].value)
        assert mapping == {r: SPECS[r]['description'] for r in routes}, (rel, 'source drift')
        save = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'save')
        with tempfile.TemporaryDirectory() as directory:
            t = Template()
            ns = {'T': t, 'ROOT': Path(directory), constant: mapping, 'HUB': '/compare/provider-comparison-library/',
                  'E': html.escape, 'DATE': '2026-10-01', 'paths': [], 'CHANGED': [],
                  'sources': lambda f: [f['source']]}
            exec(compile(ast.Module(body=[save], type_ignores=[]), rel, 'exec'), ns)
            for route in routes + ['/untouched-existing-example/']:
                old = 'Existing visible introduction.'
                if constant == 'HUB_SEARCH_DESCRIPTIONS':
                    ns['save'](route, 'Preserved title', old, 'BODY', ['https://example.com/source'])
                    assert t.output['body'] == 'VISIBLE:' + old + 'BODY'
                else:
                    ns['save'](route, 'Preserved title', old, 'BODY', [{'name': 'Example provider', 'source': 'https://example.com/source'}])
                    assert t.output['body'] == 'BODY'
                expected = mapping.get(route, old)
                assert t.output['description'] == expected
                assert t.output['schemas'][0]['description'] == expected
                assert t.output['title'] == 'Preserved title'
    print('PASS two targeted generator sources; untouched paths and visible bodies retained')

def release_baseline(source, policy, route, helper):
    """Run exact existing shared transforms on an in-memory page, never the repo."""
    source = helper.normalize_baseline_html(source, policy, route=route)
    # Existing exported navigation helper; stdin/stdout only, no writes.
    js = "const fs=require('node:fs');const {ensureSharedUx}=require(process.argv[1]);process.stdout.write(ensureSharedUx(fs.readFileSync(0,'utf8')));"
    source = subprocess.check_output(['node', '-e', js, str(policy / 'scripts/ensure-shared-ux.cjs')], input=source, text=True)
    # Lift only the existing editorial HTML loop and literal route groups. Fake
    # files keep its precise styling/case-panel behavior confined to memory.
    editorial = ast.parse((policy / 'scripts/improve-editorial-discovery.py').read_text())
    group_assignment = next(n for n in editorial.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'groups' for t in n.targets))
    loop = next(n for n in editorial.body if isinstance(n, ast.For) and isinstance(n.target, ast.Name) and n.target.id == 'file')
    class Page:
        def __init__(self, content): self.content = content
        def read_text(self): return self.content
        def write_text(self, content): self.content = content
        def relative_to(self, out): return Path(route.strip('/') + '/index.html')
    class Output:
        def rglob(self, pattern):
            assert pattern == '*.html'
            return [page]
    page = Page(source)
    ns = {'OUT': Output(), 'cases': json.loads((policy / 'scripts/calendar_planning_cases.json').read_text()),
          'groups': ast.literal_eval(group_assignment.value), 'html': html, 're': re, 'styled': 0, 'linked': 0}
    exec(compile(ast.Module(body=[loop], type_ignores=[]), 'existing-editorial-html-transform', 'exec'), ns)
    source = page.content
    # Exact existing runtime installer string, checked against its source first.
    snippet = '<script>window.si=window.si||function(){(window.siq=window.siq||[]).push(arguments)};</script><script defer src="/_vercel/speed-insights/script.js"></script>'
    assert "const snippet = '" + snippet + "';" in (policy / 'scripts/install-speed-insights.cjs').read_text(), 'Runtime transform changed; review the normalization'
    if '/_vercel/speed-insights/script.js' not in source:
        source = re.sub(r'</body\s*>', lambda m: snippet + m[0], source, count=1, flags=re.I)
    return source

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--built-output', action='store_true')
    parser.add_argument('--policy-root', type=Path)
    args = parser.parse_args(); root = args.root.resolve()
    policy = args.policy_root.resolve() if args.policy_root else root
    if args.built_output:
        assert args.policy_root, '--built-output needs --policy-root'
        p = policy / 'scripts/tax_review_build_normalization.py'
        spec = importlib.util.spec_from_file_location('build_normalization', p)
        helper = importlib.util.module_from_spec(spec); spec.loader.exec_module(helper)
    manifest = policy / 'content/buyer-snippets-20261106/routes.json'
    cohort = json.loads(manifest.read_text())
    assert cohort == list(SPECS) and len(cohort) == 9, 'Exact nine-route cohort required'
    assert not manifest.with_name('pages.json').exists(), 'Metadata-only cohort must not reset dates'
    descriptions = [s['description'] for s in SPECS.values()]
    assert len(set(descriptions)) == 9, 'Descriptions must be distinct'
    assert all(110 <= len(d) <= 165 and d.endswith('.') and '...' not in d and '…' not in d for d in descriptions), 'Complete concise descriptions required'
    for route in cohort:
        rel = route.strip('/') + '/index.html'; source = (root / rel).read_text()
        if args.built_output:
            baseline = (policy / rel).read_text()
            validate(route, baseline)
            baseline = normalize(release_baseline(baseline, policy, route, helper))
            body = re.search(r'<body\b.*?</body>', baseline, re.S)[0]
            validate(route, source, sha(baseline), sha(body))
        else:
            validate(route, source)
    print('PASS nine unique snippets; search/social/Article parity; exact normalized HTML/body hashes')
    print('PASS titles, URLs, timestamps, prices, citations, scripts, calculator behavior and application disclaimer preserved')
    test_generators(policy)
    # The preservation guard must reject mutation beyond the intended descriptions.
    route = '/tax-savings-calculator/'; source = (policy / route.strip('/') / 'index.html').read_text()
    mutants = [
        source.replace('<title>', '<title>Unreviewed ', 1),
        source.replace('No assumed strategy eligibility', 'Assumed eligibility', 1),
        source.replace('$7,800', '$7,900', 1),
        source.replace('2026-11-06', '2026-11-07', 1),
        source.replace('<main', '<main data-unreviewed="true"', 1),
        source.replace('application/ld+json', 'text/plain', 1),
        source.replace(SPECS[route]['description'], 'Truncated search description...', 1),
    ]
    for changed in mutants:
        assert changed != source
        try: validate(route, changed)
        except (AssertionError, ValueError, KeyError): pass
        else: raise AssertionError('Preservation guard accepted a prohibited change')
    print('PASS seven negative mutation fixtures')

if __name__ == '__main__':
    main()
