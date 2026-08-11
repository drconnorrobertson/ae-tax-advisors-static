"""Insert cards into blog/index.html for any post missing from the grid.

Scans every blog/<slug>/index.html, pulls the h1, meta description, category
and publish date out of the page itself, and prepends a card for anything the
index does not already link to. Newest first.
"""

import os
import re
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG = os.path.join(ROOT, "blog")
INDEX = os.path.join(BLOG, "index.html")
GRID_OPEN = '<div class="blog-index-grid" id="blogGrid">'

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def find(pattern, text, group=1, default=""):
    m = re.search(pattern, text, re.S)
    return m.group(group).strip() if m else default


def clean(text):
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()


def read_post(slug):
    src = open(os.path.join(BLOG, slug, "index.html")).read()
    title = clean(find(r"<h1[^>]*>(.*?)</h1>", src))
    desc = find(r'<meta name="description" content="([^"]*)"', src)
    date = find(r'"datePublished": "(\d{4}-\d{2}-\d{2})"', src)
    category = find(r'"articleSection": "([^"]*)"', src) or "Tax Strategy"
    if not (title and desc and date):
        return None
    y, m, d = (int(x) for x in date.split("-"))
    return {
        "slug": slug,
        "title": title,
        "desc": desc,
        "category": category,
        "sort": date,
        "pretty": f"{MONTHS[m - 1]} {d}, {y}",
    }


def card(p):
    return (
        f'                <a href="/blog/{p["slug"]}/" class="blog-index-card" '
        f'data-categories="{escape(p["category"], quote=True)}">\n'
        f'                    <div class="blog-card-category blog-badge">'
        f'{escape(p["category"])}</div>\n'
        f'                    <h3>{escape(p["title"])}</h3>\n'
        f'                    <p>{escape(p["desc"])}</p>\n'
        f'                    <span class="blog-card-date">{p["pretty"]}</span>\n'
        f"                </a>\n"
    )


def main():
    index = open(INDEX).read()
    linked = set(re.findall(r'href="/blog/([^"/]+)/"', index))

    slugs = sorted(
        d for d in os.listdir(BLOG)
        if os.path.isdir(os.path.join(BLOG, d))
        and os.path.exists(os.path.join(BLOG, d, "index.html"))
    )
    missing = [s for s in slugs if s not in linked]
    posts = [p for p in (read_post(s) for s in missing) if p]
    posts.sort(key=lambda p: (p["sort"], p["title"]), reverse=True)

    if not posts:
        print("Blog index already current.")
        return

    at = index.index(GRID_OPEN) + len(GRID_OPEN)
    index = index[:at] + "\n" + "".join(card(p) for p in posts) + index[at:]
    open(INDEX, "w").write(index)

    for p in posts:
        print(f'  + {p["slug"]}')
    print(f"\n{len(posts)} cards added to blog index.")
    if len(missing) != len(posts):
        skipped = len(missing) - len(posts)
        print(f"{skipped} post(s) skipped for missing title, description, or date.")


if __name__ == "__main__":
    main()
