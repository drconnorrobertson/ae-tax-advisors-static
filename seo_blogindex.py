#!/usr/bin/env python3
"""Add the new long-tail posts to the blog index and refresh upgraded cards."""
import html
import re
from pathlib import Path

import seo_build

# post category -> the filter button values already used on the index
FILTER = {
    "Depreciation": "Cost Segregation",
    "Real Estate Tax Strategy": "Real Estate",
    "Business Owner Tax": "Business Owners",
    "Tax Planning": "Tax Planning",
}

CARD = """                <a href="/blog/{slug}/" class="blog-index-card" data-categories="{cat}">
                    <div class="blog-card-category blog-badge">{cat}</div>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                    <span class="blog-card-date">{date}</span>
                </a>
"""

DATE = "August 13, 2026"


def main():
    idx = Path("blog/index.html")
    t = idx.read_text()

    posts = []
    for post in seo_build.ALL:
        p = dict(post)
        p["slug"] = seo_build.REMAP.get(p["slug"], p["slug"])
        p.update(seo_build.OVERRIDES.get(p["slug"], {}))
        posts.append(p)

    added = refreshed = 0
    new_cards = []
    for p in posts:
        cat = FILTER.get(p["category"], "Tax Planning")
        card = CARD.format(
            slug=p["slug"], cat=cat,
            title=html.escape(p["title"], quote=False),
            desc=html.escape(p["description"], quote=False),
            date=DATE,
        )
        href = f'/blog/{p["slug"]}/'
        existing = re.search(
            r'\s*<a href="' + re.escape(href) + r'" class="blog-index-card".*?</a>\n',
            t, re.S)
        if existing:
            # upgraded URL: replace the stale card in place
            t = t[:existing.start()] + "\n" + card.rstrip("\n") + "\n" + t[existing.end():]
            refreshed += 1
        else:
            new_cards.append(card)
            added += 1

    anchor = '<div class="blog-index-grid" id="blogGrid">\n'
    assert anchor in t, "blog grid anchor not found"
    t = t.replace(anchor, anchor + "".join(new_cards), 1)

    idx.write_text(t)
    print(f"blog index: {added} cards added, {refreshed} refreshed")


if __name__ == "__main__":
    main()
