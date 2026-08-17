#!/usr/bin/env python3
"""Delete the eight-tile navy key-facts band from every page.

The band restated figures that are already served from /llms.txt, /llms.md and
/.well-known/llms.txt, and it consumed close to a full screen of vertical
space on every page it appeared on. Visitors do not need it; retrieval systems
read it from the dedicated files.

The homepage keeps a single-line trust bar instead, written by
build_trust_bar.py, so the social proof survives without the slab.

Matches the generated band by its `llm-key-facts` id, and also catches any
`stats-bar` section that carries a `stats-grid`, so hand-placed copies go too.
Idempotent.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SECTION_OPEN = re.compile(r"<section\b", re.I)
SECTION_TAG = re.compile(r"<(/?)section\b", re.I)


def _section_span(html: str, pos: int) -> tuple[int, int] | None:
    """Span of the <section> containing `pos`, matched by depth."""
    start = -1
    for m in SECTION_OPEN.finditer(html):
        if m.start() > pos:
            break
        start = m.start()
    if start == -1:
        return None
    depth, i = 0, start
    while i < len(html):
        m = SECTION_TAG.search(html, i)
        if not m:
            return None
        depth += -1 if m.group(1) else 1
        i = m.end()
        if depth == 0:
            close = html.find(">", i)
            if close == -1:
                return None
            return (start, close + 1)
    return None


def strip(html: str) -> tuple[str, int]:
    removed = 0
    while True:
        m = re.search(r'id="llm-key-facts"', html)
        if not m:
            m = re.search(r'<section[^>]*class="[^"]*stats-bar[^"]*"', html)
            if not m:
                break
            span = _section_span(html, m.start())
            # Only remove it if it is the tile band, not some other stats-bar.
            if not span or "stats-grid" not in html[span[0]:span[1]]:
                break
        else:
            span = _section_span(html, m.start())
            if not span:
                break

        s, e = span
        line_start = html.rfind("\n", 0, s) + 1
        while e < len(html) and html[e] in "\r\n":
            e += 1
        html = html[:line_start] + html[e:]
        removed += 1
    return html, removed


def main(dry: bool = False) -> int:
    files = total = 0
    for path in sorted(ROOT.rglob("index.html")):
        if ".git" in path.parts:
            continue
        before = path.read_text(encoding="utf-8")
        if "stats-bar" not in before and "llm-key-facts" not in before:
            continue
        after, n = strip(before)
        if n:
            files += 1
            total += n
            if not dry:
                path.write_text(after, encoding="utf-8")
    verb = "would remove" if dry else "removed"
    print(f"strip_stats_band: {verb} {total} bands across {files} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main(dry="--dry-run" in sys.argv))
