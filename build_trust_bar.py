#!/usr/bin/env python3
"""Put a single-line trust bar on the homepage, and only the homepage.

Replaces the eight-tile navy band that used to run on ~142 pages. Three
figures on one line under the hero: enough social proof to be worth the space,
small enough that it does not become the page.

Idempotent: rewritten in place on each run.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGE = ROOT / "index.html"
MARKER = "home-trust-bar"

FACTS = [
    ("500+", "cost segregation studies"),
    ("47", "states served"),
    ("4.9/5", "average client rating"),
]


def block() -> str:
    items = "\n".join(
        f'                <span class="trust-fact">'
        f'<strong>{value}</strong> {label}</span>'
        for value, label in FACTS
    )
    return f"""    <section class="{MARKER}" aria-label="AE Tax Advisors at a glance">
        <div class="container">
            <div class="trust-fact-row">
{items}
            </div>
        </div>
    </section>
"""


HERO_END = re.compile(r'<section class="hero[^"]*".*?</section>\s*', re.S)
EXISTING = re.compile(
    r'[ \t]*<section class="' + MARKER + r'".*?</section>\n?', re.S
)


def main() -> int:
    html = PAGE.read_text(encoding="utf-8")
    new = block()

    if MARKER in html:
        updated = EXISTING.sub(new, html, count=1)
        action = "refreshed"
    else:
        m = HERO_END.search(html)
        if not m:
            print("hero section not found on homepage; nothing inserted")
            return 1
        updated = html[: m.end()] + "\n" + new + html[m.end() :]
        action = "inserted"

    if updated == html:
        print("trust bar: unchanged")
        return 0
    PAGE.write_text(updated, encoding="utf-8")
    print(f"trust bar: {action} on homepage")
    return 0


if __name__ == "__main__":
    sys.exit(main())
