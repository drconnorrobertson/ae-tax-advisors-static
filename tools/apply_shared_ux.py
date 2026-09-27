"""Apply shared navigation fixes to the generated static HTML pages.

Run after regenerating site pages so the shared markup stays consistent.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_TAG = '    <script defer src="/assets/site-ux.js"></script>\n'
OLD_RESOURCES = '<a href="#" class="nav-link">Resources'
NEW_RESOURCES = '<a href="/resources/" class="nav-link">Resources'


def main() -> None:
    changed = 0
    for page in ROOT.rglob("*.html"):
        if ".git" in page.parts:
            continue
        original = page.read_text(encoding="utf-8")
        if 'class="mobile-toggle"' not in original:
            continue
        updated = original.replace(OLD_RESOURCES, NEW_RESOURCES)
        if '/assets/site-ux.js' not in updated:
            updated = updated.replace('</head>', f'{SCRIPT_TAG}</head>', 1)
        if updated != original:
            page.write_text(updated, encoding="utf-8")
            changed += 1
    print(f"Updated shared navigation on {changed} HTML pages")


if __name__ == "__main__":
    main()
