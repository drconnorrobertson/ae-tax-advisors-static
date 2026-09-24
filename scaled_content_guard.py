#!/usr/bin/env python3
"""Reject new indexable pages that substantially repeat an existing page.

The check compares changed page bodies after removing page chrome and CTAs.
It is intended as a pre-publish guard, not a ranking prediction. Closely related
pages can pass when their procedures and examples are genuinely different.
"""

from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CANON = re.compile(r'<link rel="canonical" href="https://(?:www\.)?aetaxadvisors\.com([^\"]*)"', re.I)
NOINDEX = re.compile(r'<meta name="robots" content="[^\"]*noindex', re.I)
TITLE = re.compile(r'<title>(.*?)</title>', re.I | re.S)


def url_for(path: Path) -> str:
    rel = path.parent.relative_to(ROOT).as_posix()
    return "/" if rel == "." else f"/{rel}/"


def page(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    url = url_for(path)
    cm = CANON.search(text)
    if NOINDEX.search(text) or not cm or cm.group(1) != url:
        return None
    main = re.search(r"<main[^>]*>(.*?)</main>", text, re.I | re.S)
    body = main.group(1) if main else text
    body = re.sub(r'<section class="page-header".*?</section>', " ", body, flags=re.I | re.S)
    body = re.sub(r'<section class="sticky-cta".*?</section>', " ", body, flags=re.I | re.S)
    body = re.sub(
        r'<section class="content-section fade-in-section" style="background:var\(--light-bg\);">.*?</section>',
        " ", body, flags=re.I | re.S,
    )
    body = re.sub(r'<(?:script|style)[^>]*>.*?</(?:script|style)>', " ", body, flags=re.I | re.S)
    words = re.findall(r"[a-z0-9]+", html.unescape(re.sub(r"<[^>]+>", " ", body)).lower())
    shingles = {tuple(words[i:i + 5]) for i in range(max(0, len(words) - 4))}
    tm = TITLE.search(text)
    title = html.unescape(re.sub(r"<[^>]+>", " ", tm.group(1))).strip() if tm else url
    return {"path": path, "url": url, "title": title, "words": len(words), "shingles": shingles}


def new_index_files() -> set[Path]:
    result = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        cwd=ROOT, text=True, capture_output=True, check=True,
    )
    out = set()
    for line in result.stdout.splitlines():
        if len(line) < 4:
            continue
        # Existing pages may already overlap for reasons unrelated to the
        # current change. The publish gate focuses on newly introduced URLs.
        if line[:2] != "??":
            continue
        rel = line[3:].split(" -> ")[-1]
        if rel.endswith("/index.html") or rel == "index.html":
            path = ROOT / rel
            if path.exists():
                out.add(path)
    return out


def main() -> int:
    pages = []
    by_path = {}
    for path in ROOT.rglob("index.html"):
        if ".git" in path.parts:
            continue
        parsed = page(path)
        if parsed:
            pages.append(parsed)
            by_path[path] = parsed
    changed = [by_path[p] for p in new_index_files() if p in by_path]
    errors = []
    warnings = []
    seen = set()
    for left in changed:
        if left["words"] < 250:
            warnings.append(f'{left["url"]}: only {left["words"]} comparison words')
        for right in pages:
            if left["path"] == right["path"]:
                continue
            pair = tuple(sorted((left["url"], right["url"])))
            if pair in seen:
                continue
            seen.add(pair)
            a, b = left["shingles"], right["shingles"]
            if not a or not b:
                continue
            containment = len(a & b) / min(len(a), len(b))
            if containment >= 0.60:
                errors.append((containment, left["url"], right["url"]))
            elif containment >= 0.42:
                warnings.append(f'{containment:.1%} shared phrasing: {left["url"]} vs {right["url"]}')
    print(f"new indexable pages checked:     {len(changed)}")
    print(f"comparison corpus:              {len(pages)}")
    print(f"scaled-content errors:          {len(errors)}")
    for score, left, right in sorted(errors, reverse=True)[:30]:
        print(f"  ERROR {score:.1%} shared phrasing: {left} vs {right}")
    print(f"scaled-content warnings:        {len(warnings)}")
    for warning in warnings[:30]:
        print(f"  WARN  {warning}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
