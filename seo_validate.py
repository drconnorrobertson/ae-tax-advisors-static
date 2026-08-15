#!/usr/bin/env python3
"""Site validator: JSON-LD parseability, internal link targets, and SEO basics.

Usage:
    python3 seo_validate.py            # whole site
    python3 seo_validate.py <path>...  # limit to given directories
"""

from __future__ import annotations

import html as _html
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://aetaxadvisors.com"

LD_RE = re.compile(
    r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL
)
HREF_RE = re.compile(r'href="(/[^"#?]*)"')
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
DESC_RE = re.compile(r'<meta name="description" content="(.*?)"', re.DOTALL)
CANON_RE = re.compile(r'<link rel="canonical" href="(.*?)"')
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.DOTALL)


def html_files(targets: list[str]) -> list[Path]:
    if targets:
        out: list[Path] = []
        for t in targets:
            p = ROOT / t.strip("/")
            if p.is_dir():
                out.extend(sorted(p.rglob("*.html")))
            elif p.suffix == ".html":
                out.append(p)
        return out
    return [p for p in sorted(ROOT.rglob("*.html")) if ".git" not in p.parts]


def target_exists(href: str) -> bool:
    href = href.split("#")[0].split("?")[0]
    if not href.startswith("/"):
        return True
    rel = href.strip("/")
    if not rel:
        return (ROOT / "index.html").exists()
    p = ROOT / rel
    if p.is_dir() and (p / "index.html").exists():
        return True
    if p.exists() and p.is_file():
        return True
    # Extensionless path that maps to a file
    return (ROOT / (rel + ".html")).exists()


def main() -> int:
    files = html_files(sys.argv[1:])
    bad_json: list[str] = []
    broken: Counter[str] = Counter()
    broken_where: dict[str, str] = {}
    no_title: list[str] = []
    no_desc: list[str] = []
    no_canon: list[str] = []
    bad_h1: list[str] = []
    long_title: list[str] = []
    dup_titles: Counter[str] = Counter()
    faq_count = 0

    for path in files:
        rel = str(path.relative_to(ROOT))
        html = path.read_text(encoding="utf-8", errors="replace")

        for block in LD_RE.findall(html):
            try:
                json.loads(block)
            except json.JSONDecodeError as e:
                bad_json.append(f"{rel}: {e}")
        if "FAQPage" in html:
            faq_count += 1

        m = TITLE_RE.search(html)
        if not m or not m.group(1).strip():
            no_title.append(rel)
        else:
            t = m.group(1).strip()
            dup_titles[t] += 1
            if len(_html.unescape(t)) > 70:
                long_title.append(f"{rel} ({len(_html.unescape(t))})")

        if not DESC_RE.search(html):
            no_desc.append(rel)
        if not CANON_RE.search(html):
            no_canon.append(rel)

        h1s = H1_RE.findall(html)
        if len(h1s) != 1:
            bad_h1.append(f"{rel} (h1 count={len(h1s)})")

        for href in set(HREF_RE.findall(html)):
            if not target_exists(href):
                broken[href] += 1
                broken_where.setdefault(href, rel)

    print(f"Files checked:            {len(files)}")
    print(f"Pages with FAQPage:       {faq_count}")
    print(f"Invalid JSON-LD blocks:   {len(bad_json)}")
    for b in bad_json[:15]:
        print(f"   {b}")
    print(f"Broken internal targets:  {len(broken)}")
    for href, n in broken.most_common(25):
        print(f"   {href}  (x{n}, e.g. {broken_where[href]})")
    print(f"Missing <title>:          {len(no_title)}")
    for x in no_title[:10]:
        print(f"   {x}")
    print(f"Missing description:      {len(no_desc)}")
    for x in no_desc[:10]:
        print(f"   {x}")
    print(f"Missing canonical:        {len(no_canon)}")
    for x in no_canon[:10]:
        print(f"   {x}")
    print(f"Pages without exactly 1 H1: {len(bad_h1)}")
    for x in bad_h1[:10]:
        print(f"   {x}")
    print(f"Titles over 70 chars:     {len(long_title)}")
    for x in long_title[:10]:
        print(f"   {x}")
    dups = [(t, n) for t, n in dup_titles.items() if n > 1]
    print(f"Duplicate titles:         {len(dups)}")
    for t, n in sorted(dups, key=lambda x: -x[1])[:10]:
        print(f"   x{n}  {t[:80]}")

    return 1 if (bad_json or broken) else 0


if __name__ == "__main__":
    sys.exit(main())
