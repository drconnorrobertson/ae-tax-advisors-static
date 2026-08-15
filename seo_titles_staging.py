#!/usr/bin/env python3
"""Two SEO cleanups.

1. blog-staging duplicates live /blog/ pages, is absent from the sitemap, and is
   still crawlable. Each staging page gets noindex,nofollow and a canonical
   pointing at its live counterpart so it cannot compete in search.
2. Titles longer than ~70 characters truncate in results. Shorten them by
   dropping the brand suffix first, then trimming trailing subtitle clauses on a
   natural boundary.
"""

from __future__ import annotations

import html as _html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://aetaxadvisors.com"
BRAND_SUFFIX = " | AE Tax Advisors"
MAX_TITLE = 70

TITLE_RE = re.compile(r"(<title>)(.*?)(</title>)", re.DOTALL)
ROBOTS_RE = re.compile(r'<meta name="robots" content="[^"]*">')
CANON_RE = re.compile(r'<link rel="canonical" href="[^"]*">')


def deindex_staging() -> int:
    base = ROOT / "blog-staging"
    if not base.is_dir():
        return 0
    n = 0
    for path in sorted(base.rglob("index.html")):
        html = path.read_text(encoding="utf-8", errors="replace")
        slug = path.parent.name
        live = ROOT / "blog" / slug / "index.html"
        canonical_target = (f"{SITE}/blog/{slug}/" if live.exists()
                            else f"{SITE}/blog/")

        robots = '<meta name="robots" content="noindex, nofollow">'
        if ROBOTS_RE.search(html):
            html = ROBOTS_RE.sub(robots, html, count=1)
        else:
            html = re.sub(r"(</title>)", r"\1\n    " + robots, html, count=1)

        canonical = f'<link rel="canonical" href="{canonical_target}">'
        if CANON_RE.search(html):
            html = CANON_RE.sub(canonical, html, count=1)
        else:
            html = re.sub(r"(</title>)", r"\1\n    " + canonical, html, count=1)

        path.write_text(html, encoding="utf-8")
        n += 1
    return n


def shorten(title: str) -> str | None:
    original = title
    t = _html.unescape(title).strip()
    if len(t) <= MAX_TITLE:
        return None

    # 1. Drop the brand suffix.
    if t.endswith(BRAND_SUFFIX):
        t = t[: -len(BRAND_SUFFIX)].strip()
    if len(t) <= MAX_TITLE:
        return t if t != _html.unescape(original) else None

    # 2. Drop a trailing subtitle after a colon, em dash, or pipe, keeping the
    #    leading phrase which carries the keyword.
    for sep in (": ", " — ", " - ", " | "):
        if sep in t:
            head = t.split(sep)[0].strip()
            if 25 <= len(head) <= MAX_TITLE:
                t = head
                break
    if len(t) <= MAX_TITLE:
        return t

    # 3. Trim on a word boundary as a last resort.
    cut = t[:MAX_TITLE].rfind(" ")
    if cut < 25:
        return None
    return t[:cut].rstrip(" ,;:-—")


def shorten_titles() -> int:
    n = 0
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts or "blog-staging" in path.parts:
            continue
        html = path.read_text(encoding="utf-8", errors="replace")
        m = TITLE_RE.search(html)
        if not m:
            continue
        new = shorten(m.group(2))
        if not new:
            continue
        escaped = _html.escape(new, quote=False)
        html = html[: m.start(2)] + escaped + html[m.end(2):]
        # Keep og:title and twitter:title consistent with the document title.
        for prop in ('property="og:title"', 'name="twitter:title"'):
            html = re.sub(
                r'(<meta ' + re.escape(prop) + r' content=")(.*?)(">)',
                lambda mm: mm.group(1) + _html.escape(new, quote=True) + mm.group(3),
                html, count=1, flags=re.DOTALL,
            )
        path.write_text(html, encoding="utf-8")
        n += 1
    return n


def main() -> int:
    s = deindex_staging()
    t = shorten_titles()
    print(f"blog-staging pages set to noindex + canonical: {s}")
    print(f"titles shortened to {MAX_TITLE} chars or fewer:  {t}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
