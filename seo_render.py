#!/usr/bin/env python3
"""Renderer for AE Tax Advisors long-tail blog posts.

Chrome (header/footer) is lifted from a live page so generated posts stay in
sync with the rest of the site. Every post ships with Article, BreadcrumbList
and FAQPage schema, a definition-style opening, and an internal link block.
"""
import html
import json
import re
from pathlib import Path

BASE = "https://aetaxadvisors.com"
CHROME_SOURCE = "blog/tax-strategy-for-professional-athletes/index.html"


def _chrome():
    src = Path(CHROME_SOURCE).read_text()
    header = src[src.index("<body>") + len("<body>"): src.index("<main>")]
    footer = src[src.index("</main>") + len("</main>"):]
    return header, footer


HEADER, FOOTER = _chrome()


def _esc(s):
    return html.escape(s, quote=True)


def _plain(s):
    """Strip tags for use inside JSON-LD answer text."""
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip()


def render_post(post):
    """post keys: slug, title, h1, description, category, date, breadcrumb,
    lead, body, faqs, related, cta_head, cta_text, howto (optional)."""
    url = f"{BASE}/blog/{post['slug']}/"
    title_tag = post.get("title_tag") or f"{post['title']} | AE Tax Advisors"
    desc = post["description"]
    date = post.get("date", "2026-08-13")

    schemas = []

    schemas.append({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post["h1"],
        "description": desc,
        "datePublished": date,
        "dateModified": date,
        "author": {
            "@type": "Organization",
            "name": "AE Tax Advisors",
            "url": BASE,
        },
        "publisher": {
            "@type": "Organization",
            "name": "AE Tax Advisors",
            "logo": {"@type": "ImageObject", "url": f"{BASE}/assets/logo.svg"},
        },
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "url": url,
        "image": f"{BASE}/assets/logo.svg",
        "articleSection": post["category"],
        "inLanguage": "en-US",
    })

    schemas.append({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{BASE}/blog/"},
            {"@type": "ListItem", "position": 3, "name": post["breadcrumb"], "item": url},
        ],
    })

    if post.get("faqs"):
        schemas.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": _plain(a)},
                }
                for q, a in post["faqs"]
            ],
        })

    if post.get("howto"):
        ht = post["howto"]
        schemas.append({
            "@context": "https://schema.org",
            "@type": "HowTo",
            "name": ht["name"],
            "description": ht["description"],
            "step": [
                {
                    "@type": "HowToStep",
                    "position": i + 1,
                    "name": n,
                    "text": _plain(txt),
                }
                for i, (n, txt) in enumerate(ht["steps"])
            ],
        })

    schema_blocks = "\n".join(
        '    <script type="application/ld+json">\n'
        + json.dumps(s, indent=2)
        + "\n    </script>"
        for s in schemas
    )

    faq_html = ""
    if post.get("faqs"):
        items = "\n".join(
            f'            <div class="faq-item">\n'
            f"                <h3>{_esc(q)}</h3>\n"
            f"                <p>{a}</p>\n"
            f"            </div>"
            for q, a in post["faqs"]
        )
        faq_html = (
            '\n        <h2 id="faq">Frequently Asked Questions</h2>\n'
            f'        <div class="faq-section">\n{items}\n        </div>\n'
        )

    related_html = ""
    if post.get("related"):
        links = "\n".join(
            f'                <li><a href="{href}">{_esc(label)}</a></li>'
            for href, label in post["related"]
        )
        related_html = (
            "\n        <h2>Related Reading</h2>\n"
            f'        <ul class="related-articles">\n{links}\n        </ul>\n'
        )

    cta_html = (
        '\n        <div class="cta-box" style="background:#f8f9fa;border:2px solid #1a365d;'
        'border-radius:12px;padding:40px;text-align:center;margin:40px 0;">\n'
        f'            <h3 style="color:#1a365d;margin-bottom:10px;">{_esc(post["cta_head"])}</h3>\n'
        f'            <p>{_esc(post["cta_text"])}</p>\n'
        '            <a href="/discovery/" class="btn-cta btn-lg" style="margin-top:15px;'
        'display:inline-block;">Request Your Free Assessment</a>\n'
        "        </div>\n"
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{_esc(title_tag)}</title>
    <meta name="description" content="{_esc(desc)}">
    <link rel="canonical" href="{url}">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
    <meta property="og:title" content="{_esc(title_tag)}">
    <meta property="og:description" content="{_esc(desc)}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{BASE}/assets/ae-tax-logo.png">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="AE Tax Advisors">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{_esc(title_tag)}">
    <meta name="twitter:description" content="{_esc(desc)}">
    <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/style.css">
{schema_blocks}
</head>
<body>{HEADER}<main>

    <section class="page-header"><div class="container">
        <div class="breadcrumbs"><a href="/">Home</a> &raquo; <a href="/blog/">Blog</a> &raquo; {_esc(post['breadcrumb'])}</div>
        <h1>{_esc(post['h1'])}</h1>
        <p class="blog-meta">Published {post.get('date_display', 'August 13, 2026')} | {_esc(post['category'])} | AE Tax Advisors</p>
    </div></section>
    <section class="content-section fade-in-section"><div class="container narrow">

        <p class="lead-text">{post['lead']}</p>
{post['body']}
{faq_html}{related_html}{cta_html}
    </div></section>

</main>{FOOTER}"""


def write_post(post, root="."):
    out = Path(root) / "blog" / post["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_post(post))
    return out
