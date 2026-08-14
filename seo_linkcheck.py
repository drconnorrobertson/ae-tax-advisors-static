#!/usr/bin/env python3
"""Check every internal href resolves to a real page."""
import re, sys
from pathlib import Path
from collections import defaultdict

def exists(href):
    h = href.split('#')[0].split('?')[0]
    if not h or h.startswith(('http', 'mailto:', 'tel:', 'javascript:')):
        return True
    if not h.startswith('/'):
        return True  # relative, skip
    p = h.lstrip('/')
    if p == '':
        return Path('index.html').exists()
    if h.endswith('/'):
        return Path(p + 'index.html').exists()
    return Path(p).exists() or Path(p + '/index.html').exists()

broken = defaultdict(list)
scope = sys.argv[1] if len(sys.argv) > 1 else '.'
for f in sorted(Path(scope).rglob('index.html')):
    if '.git' in f.parts:
        continue
    t = f.read_text(errors='ignore')
    for href in set(re.findall(r'href="([^"]+)"', t)):
        if not exists(href):
            broken[href].append(str(f.parent))

total = sum(len(v) for v in broken.values())
print(f"broken internal link targets: {len(broken)}  (occurrences: {total})")
for href, pages in sorted(broken.items(), key=lambda kv: -len(kv[1]))[:40]:
    print(f"  {len(pages):4d}x  {href}")
    if len(pages) <= 3:
        for pg in pages:
            print(f"           on /{pg}/")
