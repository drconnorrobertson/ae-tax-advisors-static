#!/usr/bin/env python3
"""Merge the newly inserted "Related Reading" block into any pre-existing one.

The SEO pass keyed off the `related-links` class, so pages whose existing
related section used a different class (`related-articles`) ended up with two
"Related Reading" headings. This folds the new links into the existing list,
skipping hrefs already present, and removes the duplicate section.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# The block the SEO pass inserts, matched exactly enough to be safe.
INSERTED = re.compile(
    r'\n    <section class="content-section fade-in-section">\n'
    r'        <div class="container narrow">\n'
    r'            <h2>Related Reading</h2>\n'
    r'            <ul class="related-links">\n'
    r'(?P<items>.*?)\n'
    r'            </ul>\n'
    r'        </div>\n'
    r'    </section>\n',
    re.DOTALL,
)

OTHER_LIST = re.compile(
    r'<ul class="(?:related-articles|related-list|related)"[^>]*>(?P<body>.*?)</ul>',
    re.DOTALL,
)
RELATED_HEADING = re.compile(r">\s*Related (?:Reading|Articles|Resources|Guides)\s*<")
HREF = re.compile(r'href="([^"]+)"')


def main() -> int:
    merged = removed_only = untouched = 0
    for path in ROOT.rglob("index.html"):
        if ".git" in path.parts or "blog-staging" in path.parts:
            continue
        html = path.read_text(encoding="utf-8", errors="replace")
        m = INSERTED.search(html)
        if not m:
            continue
        # Is there another related section besides the one we inserted?
        without = html[: m.start()] + html[m.end():]
        if not RELATED_HEADING.search(without):
            untouched += 1
            continue

        new_items = [li for li in m.group("items").split("\n") if li.strip()]
        stripped = without

        target = OTHER_LIST.search(stripped)
        if target:
            existing_hrefs = set(HREF.findall(target.group("body")))
            add = [li for li in new_items
                   if (HREF.search(li) and HREF.search(li).group(1) not in existing_hrefs)]
            if add:
                indent = "            "
                addition = "\n" + "\n".join(indent + li.strip() for li in add)
                insert_at = target.end("body")
                stripped = stripped[:insert_at] + addition + stripped[insert_at:]
                merged += 1
            else:
                removed_only += 1
        else:
            removed_only += 1

        path.write_text(stripped, encoding="utf-8")

    print(f"pages where new links merged into existing list: {merged}")
    print(f"pages where duplicate block removed only:        {removed_only}")
    print(f"pages left as-is (no pre-existing section):      {untouched}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
