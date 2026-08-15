#!/usr/bin/env python3
"""Build the long-tail keyword posts from the content modules."""

from __future__ import annotations

import sys

import site_template as T
import content_posts_a
import content_posts_b
import content_posts_c

PUBLISHED = "2026-08-15"
MODIFIED = "2026-08-15"

ALL_POSTS = content_posts_a.POSTS + content_posts_b.POSTS + content_posts_c.POSTS


def paragraphs(items: list[str]) -> str:
    out = []
    for item in items:
        # Pre-built block markup (tables, wrappers) is emitted as-is.
        if item.lstrip().startswith("<div") or item.lstrip().startswith("<table"):
            out.append(f"            {item}")
        else:
            out.append(f"            <p>{item}</p>")
    return "\n".join(out)


def build(post: dict) -> str:
    path = f"/{post['slug']}/"
    url = f"{T.SITE}{path}"

    body_parts = []

    body_parts.append(
        T.page_header(
            h1=post["h1"],
            subtitle=post["subtitle"],
            trail=[("Home", "/"), ("Blog", "/blog/"), (post["title"], path)],
        )
    )

    # Definition-style opening paragraph, for AI overview extraction.
    body_parts.append(
        f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="post-meta">By {T.AUTHOR}, {T.BRAND} &middot; Billings, Montana &middot;
            Updated {MODIFIED}</p>
{T.definition(post['definition'])}
        </div>
    </section>"""
    )

    for heading, items in post["sections"]:
        body_parts.append(T.section(heading, paragraphs(items)))

    body_parts.append(T.takeaways(post["takeaways"]))
    body_parts.append(T.faq_section(post["faqs"]))
    body_parts.append(T.related_section(post["related"]))

    schemas = [
        T.article_schema(
            title=post["h1"],
            description=post["description"],
            url=url,
            published=PUBLISHED,
            modified=MODIFIED,
            keywords=post.get("keywords"),
        ),
        T.faq_schema(post["faqs"]),
        T.breadcrumb_schema([("Home", "/"), ("Blog", "/blog/"), (post["title"], path)]),
    ]

    return T.build_page(
        title=post["title"] + " | AE Tax Advisors",
        description=post["description"],
        path=path,
        body="\n\n".join(body_parts),
        schemas=schemas,
        published=PUBLISHED,
        modified=MODIFIED,
    )


def main() -> int:
    slugs = set()
    for post in ALL_POSTS:
        if post["slug"] in slugs:
            print(f"DUPLICATE SLUG: {post['slug']}")
            return 1
        slugs.add(post["slug"])

        html = build(post)
        out = T.write_page(post["slug"], html)
        words = len(T.strip_tags(html.split("<main>")[1].split("</main>")[0]).split())
        flag = "" if words >= 1500 else "  << UNDER 1500"
        print(f"{words:>5} words  {out.relative_to(T.ROOT)}{flag}")
    print(f"\n{len(ALL_POSTS)} posts built.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
