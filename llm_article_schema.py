#!/usr/bin/env python3
"""Add Article schema to content pages that were missing it.

Article markup is what tells a retrieval index that a page is an authored piece
with a subject, an author, and a revision date, rather than an unclassified
document. It is added only to pages that actually are articles: booking pages,
onboarding forms and calendar embeds are excluded, because marking a scheduling
widget as an Article is noise that costs trust on the pages that matter.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://www.aetaxadvisors.com"
BRAND = "AE Tax Advisors"
AUTHOR = "AE Tax Advisors Team"
MODIFIED = "2026-08-15"
PUBLISHED = "2026-01-06"

# Scheduling, intake and thank-you pages. Not articles.
UTILITY = re.compile(
    r"(^|/)("
    r".*-\d+min|.*-zoom|.*-survey|.*consultation|.*-followup|.*-recap|"
    r".*onboarding.*|.*thank-you.*|.*-form|discovery|booking|schedule.*|"
    r"portal|login|privacy.*|terms.*|disclaimer.*|sitemap"
    r")$"
)

TITLE = re.compile(r"<title>(.*?)</title>", re.S)
DESC = re.compile(r'<meta name="description" content="(.*?)"', re.S)
H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
TAG = re.compile(r"<[^>]+>")


def text(s: str) -> str:
    import html as H

    return H.unescape(re.sub(r"\s+", " ", TAG.sub("", s))).strip()


def page_dates(html: str) -> tuple[str, str]:
    """Reuse an existing page date instead of inventing a second timeline."""
    published = re.search(
        r'article:published_time["\']\s+content=["\'](\d{4}-\d{2}-\d{2})', html, re.I
    ) or re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})', html)
    modified = re.search(
        r'article:modified_time["\']\s+content=["\'](\d{4}-\d{2}-\d{2})', html, re.I
    ) or re.search(r'"dateModified"\s*:\s*"(\d{4}-\d{2}-\d{2})', html)
    published_value = published.group(1) if published else PUBLISHED
    modified_value = modified.group(1) if modified else published_value
    return published_value, max(published_value, modified_value)


def article(
    url: str, headline: str, description: str, published: str, modified: str
) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": headline[:110],
        "description": description,
        "url": url,
        "datePublished": published,
        "dateModified": modified,
        "inLanguage": "en-US",
        "author": {
            "@type": "Organization",
            "name": BRAND,
            "url": f"{SITE}/",
        },
        "publisher": {
            "@type": "Organization",
            "name": BRAND,
            "url": f"{SITE}/",
            "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/ae-tax-logo.png"},
        },
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "isAccessibleForFree": True,
    }


def apply(path: Path) -> bool:
    slug = str(path.parent.relative_to(ROOT)).strip(".").strip("/")
    if not slug or UTILITY.match(slug):
        return False
    html = path.read_text(encoding="utf-8")
    if '"Article"' in html or '"BlogPosting"' in html:
        return False

    m_t, m_d, m_h = TITLE.search(html), DESC.search(html), H1.search(html)
    if not m_t:
        return False
    headline = text(m_h.group(1)) if m_h else text(m_t.group(1))
    description = text(m_d.group(1)) if m_d else headline
    url = f"{SITE}/{slug}/"

    published, modified = page_dates(html)
    body = json.dumps(
        article(url, headline, description, published, modified),
        indent=2,
        ensure_ascii=False,
    )
    html = html.replace(
        "</head>", f'<script type="application/ld+json">\n{body}\n</script>\n</head>', 1
    )
    path.write_text(html, encoding="utf-8")
    return True


def main() -> None:
    n = 0
    for path in sorted(ROOT.rglob("index.html")):
        if ".git" in path.parts or "blog-staging" in path.parts:
            continue
        if apply(path):
            n += 1
    print(f"Article schema added to {n} pages")


if __name__ == "__main__":
    main()
