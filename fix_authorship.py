#!/usr/bin/env python3
"""Move every piece of published content off an individual byline.

All site content is authored by "AE Tax Advisors Team". That means three
distinct things, and each needs its own handling:

  1. Meta tags   -- author / article:author become the team name.
  2. JSON-LD     -- a Person author is not merely renamed, it becomes an
                    Organization. Renaming the Person would leave structured
                    data asserting a human wrote the page, which is the thing
                    we are removing. Brace matching is used rather than a
                    regex so nested worksFor/affiliation objects come along.
  3. Prose       -- bylines, "who is" FAQ entries, and press contact lines.

Connor Davis stays on engagement letters and tax plans, which are separate
PDFs generated outside this repo. Nothing on the site should carry the name.

Idempotent: safe to re-run after regenerating pages.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NAME = "Connor Davis"
TEAM = "AE Tax Advisors Team"
BRAND = "AE Tax Advisors"
SITE = "https://www.aetaxadvisors.com"

SKIP_DIRS = {".git", "node_modules", "assets"}
SUFFIXES = {".html", ".txt", ".xml", ".json"}


# --------------------------------------------------------------------------
# 1. JSON-LD: Person author -> Organization author
# --------------------------------------------------------------------------

def _match_brace(text: str, open_idx: int) -> int:
    """Index just past the '}' closing the '{' at open_idx. String-aware."""
    depth, i, in_str, esc = 0, open_idx, False, False
    while i < len(text):
        ch = text[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
        elif ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return -1


AUTHOR_KEY = re.compile(r'"author"\s*:\s*\{')


def fix_jsonld_author(text: str) -> tuple[str, int]:
    """Replace any author object naming the individual with the Organization."""
    out, pos, n = [], 0, 0
    for m in AUTHOR_KEY.finditer(text):
        if m.start() < pos:
            continue
        end = _match_brace(text, m.end() - 1)
        if end == -1:
            continue
        block = text[m.end() - 1 : end]
        if NAME not in block:
            continue

        # Reuse the indentation of the line the key sits on so the emitted
        # JSON stays as readable as what it replaces.
        line_start = text.rfind("\n", 0, m.start()) + 1
        pad = text[line_start : m.start()]
        inner = pad + "  "
        org = (
            "{\n"
            f'{inner}"@type": "Organization",\n'
            f'{inner}"name": "{BRAND}",\n'
            f'{inner}"url": "{SITE}/"\n'
            f"{pad}}}"
        )
        out.append(text[pos : m.end() - 1])
        out.append(org)
        pos = end
        n += 1
    out.append(text[pos:])
    return "".join(out), n


# --------------------------------------------------------------------------
# 2 & 3. Meta tags and prose
# --------------------------------------------------------------------------

# Ordered: longer / more specific forms first so a broad rule never eats the
# context a narrow one needs.
REPLACEMENTS: list[tuple[str, str]] = [
    # -- meta tags -----------------------------------------------------
    (f'<meta name="author" content="{NAME}, {BRAND}">',
     f'<meta name="author" content="{TEAM}">'),
    (f'<meta name="author" content="{NAME}">',
     f'<meta name="author" content="{TEAM}">'),
    (f'<meta property="article:author" content="{NAME}">',
     f'<meta property="article:author" content="{TEAM}">'),
    (f'<meta name="twitter:creator" content="{NAME}">',
     f'<meta name="twitter:creator" content="{TEAM}">'),

    # -- visible bylines -----------------------------------------------
    (f"By {NAME}, {BRAND}", f"By {TEAM}"),
    (f"| By {NAME}", f"| By {TEAM}"),
    (f"| {NAME}, {BRAND}", f"| {TEAM}"),
    (f"{NAME}, {BRAND}", TEAM),

    # -- prose ---------------------------------------------------------
    (f"{NAME} and the {BRAND} team work with",
     f"The {BRAND} team works with"),
    (f"{NAME} leads {BRAND} and is the author of the firm's published tax planning analysis.",
     f"All published analysis is written and reviewed by the {TEAM}."),
    # Trailing space consumed here so no doubled space is left behind; a
    # global whitespace collapse would corrupt unrelated HTML indentation.
    (f"{NAME} leads the firm. ", ""),
    (f"{NAME} leads the firm.", ""),
    (f"{NAME} leads {BRAND}.", f"{BRAND} was founded in Billings, Montana."),
    (f"{NAME} leads {BRAND}", BRAND),
    (f"{NAME} is available for comment",
     f"The {BRAND} team is available for comment"),
]

# Person-identity FAQ entries: the question itself has to go, not just the name.
FAQ_HEADING = (
    f"Who is {NAME} at {BRAND}?",
    f"Who writes the tax planning analysis published by {BRAND}?",
)

# Whatever survives the passes above.
BARE = re.compile(re.escape(NAME))


def fix_text(text: str) -> str:
    text = text.replace(*FAQ_HEADING)
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    text, _ = fix_jsonld_author(text)
    return BARE.sub(TEAM, text)


def main(dry_run: bool = False) -> int:
    changed, remaining = 0, 0
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in SUFFIXES:
            continue
        if SKIP_DIRS & set(path.parts):
            continue
        try:
            before = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if NAME not in before:
            continue
        after = fix_text(before)
        if NAME in after:
            remaining += 1
            print(f"  ! name survived in {path.relative_to(ROOT)}")
        if after != before:
            changed += 1
            if not dry_run:
                path.write_text(after, encoding="utf-8")

    verb = "would change" if dry_run else "changed"
    print(f"fix_authorship: {verb} {changed} files, {remaining} with surviving references")
    return 0


if __name__ == "__main__":
    sys.exit(main(dry_run="--dry-run" in sys.argv))
