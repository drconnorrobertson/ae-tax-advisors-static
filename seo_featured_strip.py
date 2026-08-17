#!/usr/bin/env python3
"""Add the "As Featured In" press strip below the hero on key pages.

Kept to high-traffic entry points rather than every page, so it reads as a trust
signal instead of boilerplate.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import content_press as P

ROOT = Path(__file__).resolve().parent

TARGETS = [
    "index.html",
    "about/index.html",
    "pricing/index.html",
    "cost-segregation-study/index.html",
    "real-estate-tax-planning/index.html",
    "business-owner-small-business-tax/index.html",
    "short-term-rental-tax-strategy/index.html",
    "services/index.html",
    "contact/index.html",
    "discovery/index.html",
    "case-studies/index.html",
    "ae-tax-advisors-reviews/index.html",
]

# A representative spread of outlets, not all 30.
SHOWCASE = ["US Insider", "The Chicago Journal", "Wall Street Times", "Market Daily",
            "Economic Insider", "NY Weekly", "LA Wire"]

MARKER = 'class="featured-strip"'


def strip_html() -> str:
    outlets = "\n".join(
        f"                <span>{o}</span>" for o in SHOWCASE
    )
    return f"""
    <section class="featured-strip" aria-label="Press coverage">
        <div class="featured-strip-inner">
            <p class="featured-strip-label">As Featured In</p>
            <div class="featured-strip-outlets">
{outlets}
            </div>
            <a href="/press/" class="featured-strip-more">See all {len(P.PRESS)} features &rsaquo;</a>
        </div>
    </section>
"""


def insert_point(html: str) -> int | None:
    """Just after the hero or page header, before the rest of the content."""
    m = re.search(r'<section class="hero[^"]*".*?</section>', html, re.DOTALL)
    if m:
        return m.end()
    m = re.search(r'<section class="page-header">.*?</section>', html, re.DOTALL)
    if m:
        return m.end()
    m = re.search(r"<main[^>]*>", html)
    return m.end() if m else None


def main() -> int:
    added = 0
    for rel in TARGETS:
        path = ROOT / rel
        if not path.exists():
            print(f"skip (missing): {rel}")
            continue
        html = path.read_text(encoding="utf-8")
        if MARKER in html:
            print(f"skip (already present): {rel}")
            continue
        pos = insert_point(html)
        if pos is None:
            print(f"skip (no anchor): {rel}")
            continue
        path.write_text(html[:pos] + strip_html() + html[pos:], encoding="utf-8")
        added += 1
        print(f"featured strip added: {rel}")
    print(f"\n{added} pages updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
