#!/usr/bin/env python3
"""Normalize the brand to its full form everywhere it appears as a name.

Answer engines build an entity around a string. "AE Tax", "AE Tax Advisors" and
"AE" read as three different organizations to a retrieval index, which splits
the citations the site earns. Every human-visible occurrence becomes
"AE Tax Advisors".

Lowercase slugs (/ae-tax-vs-traditional-cpa/, compare/kbkg-vs-ae-tax/) are left
alone: they are URLs, and rewriting them would break every inbound link.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# "AE Tax" not already followed by "Advisors", and not part of a longer
# capitalized proper noun we own (there are none) — the negative lookahead on
# "Advisor" also catches the possessive form handled below.
# The trailing (?!") guard leaves the JSON-LD value "AE Tax" alone. That string
# is the deliberate alternateName telling an engine the short form is the same
# entity; expanding it would erase the alias the whole exercise depends on.
BARE = re.compile(r'\bAE Tax(?!\s+Advisor)(?!")')
POSSESSIVE = re.compile(r"\bAE Tax(?!\s+Advisor)'s\b")

# Left in place: these are file paths, CSS classes and IDs, not prose.
SKIP_LINE = re.compile(r"^\s*(?:@|\.|#)")

FIXUPS = [
    # The title-suffix pattern "<Page> | AE Tax Advisors" doubles up when the
    # page name itself ended in the brand.
    ("AE Tax Advisors | AE Tax Advisors", "AE Tax Advisors"),
    ("AE Tax Advisors Advisors", "AE Tax Advisors"),
    # Possessive reads better with the apostrophe after the full name.
    ("AE Tax Advisors's", "AE Tax Advisors'"),
]


def convert(html: str) -> str:
    html = POSSESSIVE.sub("AE Tax Advisors'", html)
    html = BARE.sub("AE Tax Advisors", html)
    for old, new in FIXUPS:
        html = html.replace(old, new)
    return html


def main() -> None:
    changed = 0
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts:
            continue
        html = path.read_text(encoding="utf-8")
        out = convert(html)
        if out != html:
            path.write_text(out, encoding="utf-8")
            changed += 1
    print(f"brand normalized on {changed} pages")


if __name__ == "__main__":
    main()
