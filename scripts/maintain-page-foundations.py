#!/usr/bin/env python3
"""Repair missing page schema and main landmarks on approved public pages.

Existing specialist schema, robots directives, redirects and review holds are
preserved. No ratings, FAQs, dates, credentials or service claims are invented.
Run --fix for source repair; the default is a read-only release check.
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from discovery_inventory import BASE, Metadata, eligible, redirects

def text_of(markup):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', markup))).strip()

def repair(path, source):
    issues = []
    if not re.search(r'<main\b', source, re.I):
        header = re.search(r'</header\s*>', source, re.I)
        footer = re.search(r'<footer\b', source, re.I)
        if not header or not footer or header.end() >= footer.start():
            raise ValueError(f'Cannot safely locate main boundary: {path}')
        issues.append('missing main landmark')
        opening = '<main' + (' id="main-content"' if 'id="main-content"' not in source else '') + ' tabindex="-1">'
        source = source[:footer.start()] + '</main>\n' + source[footer.start():]
        source = source[:header.end()] + '\n' + opening + source[header.end():]
    if not re.search(r'<script\b[^>]*type=["\']application/ld\+json', source, re.I):
        issues.append('missing page schema')
        meta = Metadata(source)
        match = re.search(r'<h1\b[^>]*>(.*?)</h1>', source, re.S|re.I)
        name = text_of(match.group(1)) if match else meta.title
        data = {'@context': 'https://schema.org', '@type': 'WebPage',
                '@id': meta.canonical + '#webpage', 'url': meta.canonical,
                'name': name, 'description': meta.description, 'inLanguage': 'en-US',
                'publisher': {'@type': 'Organization', 'name': 'AE Tax Advisors', 'url': BASE+'/'}}
        # This guide's visible content is an editorial article. A booking page
        # remains a WebPage; it is not misrepresented as an article or product.
        if path.as_posix() == 'guides/estimated-tax-payment-methods/index.html':
            data['mainEntity'] = {'@type': 'Article', 'headline': name,
                'description': meta.description, 'mainEntityOfPage': {'@id': data['@id']},
                'author': data['publisher'], 'publisher': data['publisher'],
                'image': BASE+'/assets/ae-tax-og.png'}
        source = source.replace('</head>', '<script type="application/ld+json">\n'+json.dumps(data, indent=2)+'\n</script>\n</head>', 1)
    return source, issues

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fix', action='store_true')
    args=parser.parse_args(); mapping=redirects(); count=0; checked=0
    for file in sorted(ROOT.rglob('index.html')):
        if any(p in ('.git','public','node_modules') for p in file.relative_to(ROOT).parts): continue
        source=file.read_text()
        if not eligible(file, source, mapping): continue
        checked+=1
        updated, issues=repair(file.relative_to(ROOT), source)
        if issues:
            count+=1
            print(str(file.relative_to(ROOT))+': '+', '.join(issues))
            if args.fix: file.write_text(updated)
    print(f'Checked {checked} approved pages; {"repaired" if args.fix else "remaining"}: {count}')
    return 0 if args.fix or not count else 1

if __name__=='__main__': raise SystemExit(main())
