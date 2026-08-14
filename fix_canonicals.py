#!/usr/bin/env python3
"""Repair self-referencing canonical/og:url/schema URLs.

Only touches pages whose canonical points at an unrelated page due to a
template bug, or at a URL that does not exist. Deliberate duplicate
consolidation (canonical -> a real, different page) is left alone.
"""
import re
from pathlib import Path

BASE = "https://aetaxadvisors.com"
BUG_TARGET = "/tax-planning-for-high-net-worth-real-estate-investors/"

def page_url(p):
    d = str(p.parent).replace("\\", "/")
    return "/" if d == "." else "/" + d + "/"

def target_exists(t):
    t = "/" + t.strip("/") + "/" if t != "/" else "/"
    return Path("." + t + "index.html").exists()

fixed_canon = fixed_og = fixed_schema = added = 0
touched = []

for p in sorted(Path(".").rglob("index.html")):
    if ".git" in p.parts:
        continue
    url = page_url(p)
    t = p.read_text(errors="ignore")
    orig = t
    m = re.search(r'<link rel="canonical" href="' + BASE + r'([^"]*)"', t)

    if m:
        cur = m.group(1)
        if cur == url:
            continue
        # Leave intentional consolidation alone: canonical points at a real page.
        if cur != BUG_TARGET and target_exists(cur):
            continue
        t = t.replace(f'<link rel="canonical" href="{BASE}{cur}">',
                      f'<link rel="canonical" href="{BASE}{url}">')
        fixed_canon += 1
        # og:url and schema URLs on these pages carry the same wrong value.
        if f'<meta property="og:url" content="{BASE}{cur}">' in t:
            t = t.replace(f'<meta property="og:url" content="{BASE}{cur}">',
                          f'<meta property="og:url" content="{BASE}{url}">')
            fixed_og += 1
        n_schema = t.count(f'"{BASE}{cur}"')
        if n_schema:
            t = t.replace(f'"{BASE}{cur}"', f'"{BASE}{url}"')
            fixed_schema += n_schema
    else:
        # No canonical at all: insert one after the title tag.
        mt = re.search(r"</title>", t)
        if not mt:
            continue
        i = mt.end()
        t = t[:i] + f'\n    <link rel="canonical" href="{BASE}{url}">' + t[i:]
        added += 1

    if t != orig:
        p.write_text(t)
        touched.append(url)

print(f"canonicals rewritten : {fixed_canon}")
print(f"canonicals added     : {added}")
print(f"og:url corrected     : {fixed_og}")
print(f"schema URLs corrected: {fixed_schema}")
print(f"pages touched        : {len(touched)}")
for u in touched[:10]:
    print("   ", u)
