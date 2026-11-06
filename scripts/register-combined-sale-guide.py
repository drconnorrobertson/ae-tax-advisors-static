#!/usr/bin/env python3
"""Merge one reviewed route into current discovery files, never copy snapshots.

Default: show a read-only plan. --apply writes only missing exact route entries,
then uses the maintained archive renderer. Existing different entries fail
closed. Run in the checkout containing the reviewed article and manifest.
"""
from pathlib import Path
import argparse
import html
import json
import re
import xml.etree.ElementTree as ET
import blog_archive as archive

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'content/combined-sale-guide-20261106/registration.json'


def plans(root=ROOT):
    root = Path(root)
    spec = json.loads((root / MANIFEST.relative_to(ROOT)).read_text())
    route = spec['route']
    assert route == '/blog/selling-business-and-building-1031-exchange/'
    updates = {}

    def put_json(path, key, value):
        p = root / path
        old = p.read_text()
        data = json.loads(old)
        if key in data:
            assert data[key] == value, 'Conflicting route record: ' + path
        else:
            data[key] = value
            updates[path] = json.dumps(data, indent=2, ensure_ascii=False) + '\n'

    catalog_path = 'scripts/blog-catalog.json'
    entries = json.loads((root / catalog_path).read_text())
    existing = [e for e in entries if e['url'] == route]
    if existing:
        assert existing == [spec['catalog']], 'Conflicting catalog record'
    else:
        entries.append(spec['catalog'])
        updates[catalog_path] = json.dumps(sorted(entries, key=lambda e: e['url']), indent=2, ensure_ascii=False) + '\n'

    for entry in spec['xml_sitemaps']:
        path = entry['file']
        old = (root / path).read_text()
        tree = ET.fromstring(old)
        found = [x for x in tree if x.findtext('{*}loc') == entry['loc']]
        if found:
            assert len(found) == 1 and found[0].findtext('{*}lastmod') == entry['lastmod'], 'Conflicting sitemap entry: ' + path
        else:
            assert old.count('</urlset>') == 1
            addition = '  <url><loc>' + entry['loc'] + '</loc><lastmod>' + entry['lastmod'] + '</lastmod></url>\n'
            updates[path] = old.replace('</urlset>', addition + '</urlset>', 1)

    put_json('content/reviewed-content-lastmod.json', route, spec['publication_date'])
    put_json('content/discovery-reviewed-copy-20261106.json', route, spec['reviewed_discovery_copy'][route])
    path = 'content/seo-refresh-20261106/pages.json'
    pages = json.loads((root / path).read_text())
    assert pages.count(route) <= 1
    if route not in pages:
        pages.append(route)
        updates[path] = json.dumps(pages, indent=2, ensure_ascii=False) + '\n'

    for path in ['llms.txt', 'llms.md', '.well-known/llms.txt', 'llms-full.txt']:
        old = (root / path).read_text()
        line = '- [' + spec['discovery_link']['label'] + '](' + spec['discovery_link']['url'] + ')'
        if spec['discovery_link']['url'] in old:
            assert old.count(spec['discovery_link']['url']) == 1 and line in old, 'Conflicting discovery entry: ' + path
        else:
            updates[path] = old + ('\n' if not old.endswith('\n') else '') + line + '\n'

    path = 'sitemap/index.html'
    old = (root / path).read_text()
    addition = '<li><a href="' + route + '">' + html.escape(spec['discovery_link']['label']) + '</a></li>'
    if 'href="' + route + '"' in old:
        assert old.count('href="' + route + '"') == 1 and addition in old, 'Conflicting HTML sitemap entry'
    else:
        marker = r'(<h2>Planning for your next ownership decision</h2>\s*<ul[^>]*>)'
        new, count = re.subn(marker, lambda m: m[1] + addition, old)
        assert count == 1, 'HTML sitemap owner-decision section changed; inspect before merging'
        updates[path] = new
    return spec, updates


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    spec, updates = plans()
    assert archive.article(spec['route'], spec['catalog']['category']) == spec['catalog'], 'Article/catalog mismatch'
    print(json.dumps({'route': spec['route'], 'pending_files': sorted(updates), 'mode': 'apply' if args.apply else 'plan'}, indent=2))
    if args.apply:
        for path, value in updates.items():
            (ROOT / path).write_text(value)
        # Generates discovery only from the explicit catalog; preserves the
        # independently authored companion section through blog_archive.py.
        archive.render()


if __name__ == '__main__':
    main()
