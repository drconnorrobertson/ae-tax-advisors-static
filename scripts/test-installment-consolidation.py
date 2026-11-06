#!/usr/bin/env python3
"""One-route retirement tests. Mutations are in memory; no generator is run."""
import argparse
import ast
import copy
import hashlib
import importlib.util
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

from installment_consolidation_contract import (
    SITE, SOURCE, DESTINATION, SECTION731, SOURCE_FILE, DESTINATION_FILE,
    SECTION731_FILE, RETIRED_ITEM, RELATED, FALLBACK_HTML,
    reconcile_sale_baseline, redirect_errors, remove_retired_related_item,
)

REPO = Path(__file__).resolve().parents[1]
SPEED = '<script>window.si=window.si||function(){(window.siq=window.siq||[]).push(arguments)};</script><script defer src="/_vercel/speed-insights/script.js"></script>'
BOOKING = '<script defer src="/assets/booking-events.js?v=20261019"></script>'
HTML_FILES = [SOURCE_FILE, DESTINATION_FILE, SECTION731_FILE, 'sitemap/index.html']
DISCOVERY = ['llms-full.txt', 'llms.txt', 'llms.md', '.well-known/llms.txt', 'feed.xml',
             'assets/blog-search-index.json']
SOURCE_CHANGES = set(HTML_FILES + ['vercel.json', 'scripts/content-consolidation.json',
    'sitemap.xml', 'llms-full.txt', 'scripts/generate_site.py', 'scripts/test-sale-buyer-guides.py'])
ADDITIONS = {'scripts/installment_consolidation_contract.py', 'scripts/test-installment-consolidation.py'}
PUBLIC_CHANGES = set(HTML_FILES + ['sitemap.xml', 'llms-full.txt'])


class Tags(HTMLParser):
    def __init__(self, value):
        super().__init__(); self.tags = []; self.feed(value)
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


def hrefs(value):
    return [a['href'] for tag, a in Tags(value).tags if tag == 'a' and 'href' in a]


def canonicals(value):
    return [a.get('href') for tag, a in Tags(value).tags if tag == 'link' and a.get('rel') == 'canonical']


def noindex(value):
    return any('noindex' in re.split(r'[,\s]+', a.get('content', '').lower())
               for tag, a in Tags(value).tags if tag == 'meta' and a.get('name', '').lower() in ('robots', 'googlebot'))


def incoming_errors(name, value):
    result = []
    for target in hrefs(value):
        url = urlsplit(target)
        if (not url.netloc or url.netloc in ('www.aetaxadvisors.com', 'aetaxadvisors.com')) and url.path.rstrip('/') == SOURCE.rstrip('/'):
            result.append(name + ': incoming retired href')
    return result


def content_errors(docs, staged=False):
    errors = []
    def check(ok, message):
        if not ok: errors.append(message)
    expected = FALLBACK_HTML.replace('</head>', BOOKING + '</head>').replace('</body>', SPEED + '</body>') if staged else FALLBACK_HTML
    check(docs[SOURCE_FILE] == expected, 'exact fallback, including noindex/follow and canonical/link')
    check(noindex(docs[SOURCE_FILE]), 'fallback indexability')
    check(canonicals(docs[SOURCE_FILE]) == [SITE + DESTINATION], 'fallback canonical')
    check(canonicals(docs[DESTINATION_FILE]) == [SITE + DESTINATION], 'destination canonical')
    check(not noindex(docs[DESTINATION_FILE]), 'destination must remain indexable')
    for name in HTML_FILES:
        errors += incoming_errors(name, docs[name])
    for name in (DESTINATION_FILE, SECTION731_FILE):
        related = RELATED.findall(docs[name]); check(len(related) == 1, name + ': Related Reading count')
        if related:
            check(hrefs(related[0]).count(DESTINATION) == (0 if name == DESTINATION_FILE else 1), name + ': destination Related Reading count')
    check(hrefs(docs['sitemap/index.html']).count(DESTINATION) == 1, 'HTML sitemap destination count')
    xml = '\n'.join(v for k, v in docs.items() if re.fullmatch(r'sitemap.*\.xml', k))
    check(xml.count('<loc>' + SITE + DESTINATION + '</loc>') == 1, 'XML sitemap destination count')
    for name, value in docs.items():
        if name not in HTML_FILES:
            check(SOURCE.strip('/') not in value, name + ': retired discovery string')
    return errors


def hashes(root, source=False):
    result = {}
    for file in root.rglob('*'):
        relative = file.relative_to(root)
        if any(p in ('.git', '__pycache__') or (source and p == 'public') for p in relative.parts): continue
        if file.is_file(): result[str(relative)] = hashlib.sha256(file.read_bytes()).hexdigest()
    return result


def exact_page_delta_errors(old, current):
    return [] if remove_retired_related_item(old) == current else ['unrelated page bytes changed']


def registry_errors(value):
    tree = ast.parse(value)
    posts = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'POST_SLUGS' for t in n.targets))
    return ['retired legacy POST_SLUGS registry entry'] if SOURCE.strip('/') in posts else []


def exact_source_changes(base):
    errors = []
    before, after = hashes(base, True), hashes(REPO, True)
    changed = {f for f in before.keys() & after.keys() if before[f] != after[f]}
    if changed != SOURCE_CHANGES: errors.append('source changed-file set: ' + repr(sorted(changed ^ SOURCE_CHANGES)))
    if after.keys() - before.keys() != ADDITIONS or before.keys() - after.keys(): errors.append('source added/removed files differ')
    expected = {}
    read = lambda f: (base / f).read_text()
    old = json.loads(read('vercel.json')); old['redirects'] += [dict(source=s, destination=DESTINATION, permanent=True) for s in (SOURCE, SOURCE.rstrip('/'))]
    expected['vercel.json'] = json.dumps(old, indent=2) + '\n'
    old = json.loads(read('scripts/content-consolidation.json')); old['redirects'][SOURCE] = DESTINATION
    expected['scripts/content-consolidation.json'] = json.dumps(old, indent=2) + '\n'
    expected[SOURCE_FILE] = FALLBACK_HTML
    for f in (DESTINATION_FILE, SECTION731_FILE): expected[f] = remove_retired_related_item(read(f))
    item = '    ' + RETIRED_ITEM
    assert read('sitemap/index.html').count(item) == 1
    expected['sitemap/index.html'] = read('sitemap/index.html').replace(item, '', 1)
    pattern = r'  <url>\n    <loc>' + re.escape(SITE + SOURCE) + r'</loc>\n(?:(?!</url>).)*?  </url>\n'
    expected['sitemap.xml'], count = re.subn(pattern, '', read('sitemap.xml'), flags=re.S)
    assert count == 1
    lines = read('llms-full.txt').splitlines(keepends=True)
    assert sum(SOURCE in line for line in lines) == 1
    expected['llms-full.txt'] = ''.join(line for line in lines if SOURCE not in line)
    line = '    ' + json.dumps(SOURCE.strip('/')) + ',\n'
    assert read('scripts/generate_site.py').count(line) == 1
    expected['scripts/generate_site.py'] = read('scripts/generate_site.py').replace(line, '', 1)
    old = read('scripts/test-sale-buyer-guides.py')
    old = old.replace('from tax_review_build_normalization import normalize_baseline_html\n', 'from tax_review_build_normalization import normalize_baseline_html\nfrom installment_consolidation_contract import reconcile_sale_baseline, retirement_errors\n')
    old = old.replace('def preservation(i,old,new):\n errors=[]', 'def preservation(i,old,new):\n old=reconcile_sale_baseline(old,new,ROUTES[i])\n errors=[]')
    expected['scripts/test-sale-buyer-guides.py'] = old.replace("  if (REPO/placeholder).read_bytes()!=(base/placeholder).read_bytes():errors.append('audit-only fifth page changed')", "  if (REPO/placeholder).read_bytes()!=(base/placeholder).read_bytes():errors+=retirement_errors(REPO)")
    for f, value in expected.items():
        if (REPO / f).read_text() != value: errors.append(f + ': unrelated source bytes changed')
    # The exact destination/Section731 comparisons cover all article text, facts,
    # prices, original publication dates, review dates, schema, CTAs and links.
    return errors


def negative_fixtures(docs, staged, config, mapping):
    count = 0
    def bad_content(name, value, expected_error):
        nonlocal count
        mutated = dict(docs); mutated[name] = value
        assert any(expected_error in e for e in content_errors(mutated, staged)), expected_error
        count += 1
    for route in (SOURCE, SOURCE.rstrip('/')):
        for field, value in [('permanent', False), ('destination', SOURCE), ('destination', '/unrelated/')]:
            bad = copy.deepcopy(config); next(r for r in bad['redirects'] if r['source'] == route)[field] = value
            assert redirect_errors(bad, mapping); count += 1
        bad = copy.deepcopy(config); bad['redirects'] = [r for r in bad['redirects'] if r['source'] != route]
        assert redirect_errors(bad, mapping); count += 1
        bad = copy.deepcopy(config); bad['redirects'] += [next(r for r in bad['redirects'] if r['source'] == route).copy()]
        assert redirect_errors(bad, mapping); count += 1
    for target in (SOURCE, '/unrelated/'):
        bad = copy.deepcopy(config); bad['redirects'].append(dict(source=DESTINATION, destination=target, permanent=True))
        assert redirect_errors(bad, mapping); count += 1
    for bad in ({k:v for k,v in mapping.items() if k != SOURCE}, dict(mapping, **{SOURCE: '/unrelated/'}), dict(mapping, **{DESTINATION: SOURCE})):
        assert redirect_errors(config, bad); count += 1
    for old, new, error in [('noindex, follow', 'index, follow', 'fallback indexability'), ('noindex, follow', 'noindex, nofollow', 'exact fallback'), (SITE + DESTINATION, SITE + SOURCE, 'fallback canonical')]:
        bad_content(SOURCE_FILE, docs[SOURCE_FILE].replace(old, new), error)
    bad_content(DESTINATION_FILE, docs[DESTINATION_FILE].replace('</head>', '<meta name="robots" content="noindex">\n</head>'), 'destination must remain indexable')
    bad_content(DESTINATION_FILE, docs[DESTINATION_FILE].replace('</head>', '<meta name="googlebot" content="follow, noindex">\n</head>'), 'destination must remain indexable')
    bad_content(DESTINATION_FILE, docs[DESTINATION_FILE].replace('rel="canonical"', 'rel="alternate"'), 'destination canonical')
    for name in ('llms-full.txt', 'sitemap.xml', 'assets/blog-search-index.json'):
        bad_content(name, docs[name] + SOURCE, 'retired discovery string')
    bad_content('sitemap.xml', docs['sitemap.xml'] + '<loc>' + SITE + DESTINATION + '</loc>', 'XML sitemap destination count')
    bad_content('sitemap/index.html', docs['sitemap/index.html'] + '<a href="' + DESTINATION + '">Duplicate</a>', 'HTML sitemap destination count')
    for name, link in [(DESTINATION_FILE, DESTINATION), (SECTION731_FILE, DESTINATION), (SECTION731_FILE, SOURCE)]:
        value = RELATED.sub(lambda m: m[0].replace('</section>', '<a href="' + link + '">Bad link</a></section>'), docs[name])
        bad_content(name, value, 'incoming retired href' if link == SOURCE else 'destination Related Reading count')
    for href in (SOURCE, SOURCE.rstrip('/'), SITE + SOURCE, 'https://aetaxadvisors.com' + SOURCE + '?x=1#related'):
        assert incoming_errors('fixture.html', '<a href="' + href + '">Old</a>'); count += 1

    # Reconciliation fails closed on a second removed link, changed label,
    # duplicate placeholder, wrong route, or a change outside Related Reading.
    current = docs[DESTINATION_FILE]
    before = RELATED.sub(lambda m: m[0].replace('<ul class="related-articles">\n', '<ul class="related-articles">\n' + RETIRED_ITEM), current)
    assert reconcile_sale_baseline(before, current, DESTINATION) == current
    for wrong_route in (SECTION731, SOURCE):
        assert reconcile_sale_baseline(before, current, wrong_route) == before; count += 1
    for bad in (current.replace('href="/real-estate-tax-planning/"', 'href="/unrelated/"'), current.replace('Real Estate Tax Planning (Pillar Guide)', 'Unexpected label')):
        assert reconcile_sale_baseline(before, bad, DESTINATION) == before; count += 1
    duplicate = before.replace(RETIRED_ITEM, RETIRED_ITEM * 2)
    assert reconcile_sale_baseline(duplicate, current, DESTINATION) == duplicate; count += 1
    # Independently call sale4's preservation guard to show that its narrowly
    # reconciled case passes and unrelated navigation/publication mutations fail.
    spec = importlib.util.spec_from_file_location('sale_tests', REPO / 'scripts/test-sale-buyer-guides.py')
    sale = importlib.util.module_from_spec(spec); spec.loader.exec_module(sale)
    assert sale.preservation(0, before, current) == []
    assert exact_page_delta_errors(before, current) == []
    for bad in (current.replace('$120,000', '$125,000'), current.replace('60%', '70%'), current.replace('IRS Publication 537', 'Unsupported source')):
        assert bad != current and exact_page_delta_errors(before, bad); count += 1
    assert registry_errors('POST_SLUGS = ' + repr([SOURCE.strip('/')])); count += 1
    assert registry_errors('POST_SLUGS = ' + repr([DESTINATION.strip('/')])) == []
    for bad in (current.replace('href="/discovery/"', 'href="/unrelated/"', 1), current.replace('href="/real-estate-tax-planning/"', 'href="/unrelated/"', 1), re.sub(r'("datePublished":\s*)"[^"]+"', r'\1"2000-01-01"', current, count=1)):
        assert sale.preservation(0, before, bad); count += 1
    return count


def main():
    p = argparse.ArgumentParser(); p.add_argument('root', nargs='?', default=str(REPO)); p.add_argument('--baseline'); a = p.parse_args()
    root = Path(a.root).resolve(); staged = root != REPO
    config = json.loads((REPO / 'vercel.json').read_text()); mapping = json.loads((REPO / 'scripts/content-consolidation.json').read_text())['redirects']
    files = HTML_FILES + DISCOVERY + [x.name for x in root.glob('sitemap*.xml')]
    docs = {f:(root / f).read_text() for f in files}
    errors = redirect_errors(config, mapping) + content_errors(docs, staged)
    scanned = 0
    for f in root.rglob('*.html'):
        if any(x in ('.git', 'scripts', '__pycache__') or (not staged and x == 'public') for x in f.relative_to(root).parts): continue
        value = f.read_text(); scanned += 1
        # Only parse potential stale links; independent fixtures cover all forms.
        if SOURCE.strip('/') in value: errors += incoming_errors(str(f.relative_to(root)), value)
    errors += registry_errors((REPO / 'scripts/generate_site.py').read_text())
    for f in ['discovery_review_holds.json', 'scripts/blog-catalog.json', 'scripts/blog-archive-migration.json']:
        if SOURCE.strip('/') in (REPO / f).read_text(): errors.append(f + ': unnecessary retired route registration')
    if a.baseline:
        base = Path(a.baseline); errors += exact_source_changes(base)
        if staged:
            before, after = hashes(base / 'public'), hashes(root)
            changed = {f for f in before.keys() & after.keys() if before[f] != after[f]}
            if changed != PUBLIC_CHANGES: errors.append('staged changed-file set: ' + repr(sorted(changed ^ PUBLIC_CHANGES)))
            if before.keys() != after.keys(): errors.append('staged files added or removed')
    negative = negative_fixtures(docs, staged, config, mapping)
    print(json.dumps(dict(root=str(root), scanned_html=scanned, negative_fixtures=negative, baseline_checks=bool(a.baseline), errors=errors), indent=2))
    return bool(errors)


if __name__ == '__main__': sys.exit(main())
