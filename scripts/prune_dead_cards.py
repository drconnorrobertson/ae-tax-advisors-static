"""Remove blog index cards pointing at pages that no longer exist.

The blog index carries cards left over from an earlier site migration whose
target directories were removed. Each dead card is a broken link on one of the
most-crawled pages on the site, so they are stripped rather than left in place.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "blog", "index.html")

CARD = re.compile(
    r'[ \t]*<a href="(/[^"]*)" class="blog-index-card".*?</a>\n?',
    re.S,
)


def resolves(href):
    rel = href.strip("/").replace("/", os.sep)
    return os.path.exists(os.path.join(ROOT, rel, "index.html"))


def main():
    src = open(INDEX).read()
    removed = []

    def repl(m):
        href = m.group(1)
        if resolves(href):
            return m.group(0)
        removed.append(href)
        return ""

    out = CARD.sub(repl, src)

    if not removed:
        print("No dead cards found.")
        return

    open(INDEX, "w").write(out)
    for href in removed:
        print(f"  - {href}")
    print(f"\n{len(removed)} dead cards removed from blog index.")


if __name__ == "__main__":
    main()
