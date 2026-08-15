#!/usr/bin/env python3
"""Mobile optimization pass.

1. Guarantees every page with a `.nav-links` menu also has a working
   `.mobile-toggle` button (the menu is display:none on small screens, so a
   page without the button has no reachable navigation at all).
2. Wraps bare <table> elements in a horizontally scrollable container so wide
   comparison tables never force the whole page to scroll sideways.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKIP_DIRS = {".git", "assets", "blog-staging"}

TOGGLE = (
    '            <button class="mobile-toggle" aria-label="Open menu" '
    'aria-expanded="false" '
    "onclick=\"var n=document.querySelector('.nav-links');"
    "var o=n.classList.toggle('open');"
    'this.setAttribute(\'aria-expanded\',o);">\n'
    "                <span></span><span></span><span></span>\n"
    "            </button>\n"
)

# A logo anchor immediately followed by the nav: the toggle belongs between them.
LOGO_THEN_NAV = re.compile(
    r'(<a href="/" class="logo">.*?</a>\s*\n)(\s*<nav class="nav-links">)',
    re.DOTALL,
)
# Non-standard toggle markup used by a handful of pages.
LEGACY_TOGGLE = re.compile(
    r'\s*<button class="mobile-menu-toggle"[^>]*>.*?</button>\s*\n',
    re.DOTALL,
)

TABLE_OPEN = re.compile(r"<table(?![^>]*\bclass=)", re.IGNORECASE)


def html_files():
    for path in ROOT.rglob("*.html"):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts[:-1]):
            continue
        if ".git" in path.parts:
            continue
        yield path


def fix_toggle(html: str) -> tuple[str, bool]:
    if '<nav class="nav-links">' not in html:
        return html, False
    # Normalize legacy toggle markup to the standard button.
    if "mobile-menu-toggle" in html:
        html = LEGACY_TOGGLE.sub("\n", html)
    if 'class="mobile-toggle"' in html:
        return html, False
    new_html, n = LOGO_THEN_NAV.subn(r"\1" + TOGGLE + r"\2", html, count=1)
    if n == 0:
        # Fall back to inserting directly before the nav element.
        new_html, n = re.subn(
            r'(\s*<nav class="nav-links">)',
            "\n" + TOGGLE + r"\1",
            html,
            count=1,
        )
    return new_html, n > 0


def wrap_tables(html: str) -> tuple[str, bool]:
    if "<table" not in html:
        return html, False
    if "ae-table-scroll" in html:
        return html, False
    out = []
    idx = 0
    changed = False
    for m in re.finditer(r"<table[^>]*>", html, re.IGNORECASE):
        start = m.start()
        # Already inside a scroll wrapper?
        preceding = html[max(0, start - 260):start]
        if "overflow-x" in preceding or "table-wrap" in preceding:
            continue
        end = html.lower().find("</table>", m.end())
        if end == -1:
            continue
        end += len("</table>")
        if start < idx:
            continue
        out.append(html[idx:start])
        out.append('<div class="ae-table-scroll">')
        out.append(html[start:end])
        out.append("</div>")
        idx = end
        changed = True
    if not changed:
        return html, False
    out.append(html[idx:])
    return "".join(out), True


def main() -> int:
    toggled = tables = 0
    for path in html_files():
        html = original = path.read_text(encoding="utf-8")
        html, t1 = fix_toggle(html)
        html, t2 = wrap_tables(html)
        if html != original:
            path.write_text(html, encoding="utf-8")
            toggled += bool(t1)
            tables += bool(t2)
    print(f"mobile nav toggles added/normalized: {toggled}")
    print(f"pages with tables made scrollable:   {tables}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
