#!/usr/bin/env python3
"""Remove content images from blog posts.

Blog articles are text only: no hero image, no inline photography, no stock
imagery. Images elsewhere on the site (homepage, services, team, logos) are
untouched, and so is the site chrome inside a post, so the header logo and
footer logo survive.

Only images inside <main> are considered, and the logo is excluded by path so
the in-content branding used by a few templates is not mistaken for a photo.

Idempotent.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BLOG = ROOT / "blog"

# Each pattern takes the element plus its own leading indent and trailing
# newline, and nothing more. A greedy \s* here would swallow the next line's
# indentation and reflow the surrounding markup.
IMG = re.compile(r"[ \t]*<img\b[^>]*>[ \t]*\n?", re.I)
FIGURE = re.compile(r"[ \t]*<figure\b.*?</figure>[ \t]*\n?", re.I | re.S)
PICTURE = re.compile(r"[ \t]*<picture\b.*?</picture>[ \t]*\n?", re.I | re.S)

# Chrome that lives inside <main> on some templates and must stay.
KEEP = ("ae-tax-logo", "/assets/favicon", "logo-white", "logo-shield")


def strip_main(html: str) -> tuple[str, int]:
    m = re.search(r"<main[^>]*>(.*?)</main>", html, re.S | re.I)
    if not m:
        return html, 0
    body = m.group(1)
    before = body
    removed = 0

    for pattern in (FIGURE, PICTURE):
        def drop_block(mo: re.Match) -> str:
            nonlocal removed
            if any(k in mo.group(0) for k in KEEP):
                return mo.group(0)
            removed += 1
            return ""
        body = pattern.sub(drop_block, body)

    def drop_img(mo: re.Match) -> str:
        nonlocal removed
        if any(k in mo.group(0) for k in KEEP):
            return mo.group(0)
        removed += 1
        return ""

    body = IMG.sub(drop_img, body)

    if body == before:
        return html, 0
    return html[: m.start(1)] + body + html[m.end(1):], removed


def main(dry: bool = False) -> int:
    files = total = 0
    for path in sorted(BLOG.rglob("index.html")):
        if path == BLOG / "index.html":
            continue  # the index is handled by build_blog_index.py
        html = path.read_text(encoding="utf-8")
        new, n = strip_main(html)
        if n:
            files += 1
            total += n
            if not dry:
                path.write_text(new, encoding="utf-8")
    verb = "would remove" if dry else "removed"
    print(f"strip_blog_images: {verb} {total} images across {files} posts")
    return 0


if __name__ == "__main__":
    sys.exit(main(dry="--dry-run" in sys.argv))
