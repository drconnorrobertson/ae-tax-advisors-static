#!/usr/bin/env python3
"""Shared page builder for AE Tax Advisors.

The header, footer and sticky CTA are lifted verbatim out of the live homepage
rather than duplicated here, so every page this module generates is guaranteed
to carry the same navigation, footer and design as the rest of the site. If the
homepage nav changes, regenerating picks the change up automatically.
"""

from __future__ import annotations

import html as _html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://www.aetaxadvisors.com"
BRAND = "AE Tax Advisors"
AUTHOR = "Connor Davis"
PHONE = "(631) 614-5762"


def _slice(source: str, start: str, end: str) -> str:
    i = source.index(start)
    j = source.index(end, i) + len(end)
    return source[i:j]


class Chrome:
    """Header / footer / CTA markup extracted from the homepage."""

    def __init__(self) -> None:
        home = (ROOT / "index.html").read_text(encoding="utf-8")
        self.header = _slice(home, "<header>", "</header>")
        self.footer = _slice(home, "<footer>", "</footer>")
        self.sticky = _slice(home, '<section class="sticky-cta">', "</section>")
        self.script = _slice(home, "<script>\n    // Scroll fade-in", "</script>")
        # The generated page is never the homepage, so drop the "active" state
        # the homepage sets on its own nav item.
        self.header = self.header.replace(
            '<a href="/" class="nav-link active">Home</a>',
            '<a href="/" class="nav-link">Home</a>',
        )

    def header_for(self, active_href: str | None = None) -> str:
        h = self.header
        if active_href:
            h = h.replace(
                f'<a href="{active_href}" class="nav-link">',
                f'<a href="{active_href}" class="nav-link active">',
                1,
            )
        return h


CHROME: Chrome | None = None


def chrome() -> Chrome:
    global CHROME
    if CHROME is None:
        CHROME = Chrome()
    return CHROME


def esc(text: str) -> str:
    """Escape for use inside an HTML attribute."""
    return _html.escape(text, quote=True)


def jsonld(data: dict) -> str:
    body = json.dumps(data, indent=2, ensure_ascii=False)
    return f'<script type="application/ld+json">\n{body}\n</script>'


def faq_schema(faqs: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)},
            }
            for q, a in faqs
        ],
    }


def article_schema(
    *,
    title: str,
    description: str,
    url: str,
    published: str,
    modified: str,
    section: str = "Tax Strategy",
    keywords: list[str] | None = None,
) -> dict:
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "url": url,
        "datePublished": published,
        "dateModified": modified,
        "articleSection": section,
        "author": {
            "@type": "Person",
            "name": AUTHOR,
            "jobTitle": "Tax Strategist",
            "worksFor": {"@type": "Organization", "name": BRAND},
        },
        "publisher": {
            "@type": "Organization",
            "name": BRAND,
            "logo": {
                "@type": "ImageObject",
                "url": f"{SITE}/assets/ae-tax-logo.png",
            },
        },
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
    }
    if keywords:
        data["keywords"] = ", ".join(keywords)
    return data


def breadcrumb_schema(trail: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i,
                "name": name,
                "item": f"{SITE}{href}",
            }
            for i, (name, href) in enumerate(trail, start=1)
        ],
    }


TAG_RE = re.compile(r"<[^>]+>")


def strip_tags(markup: str) -> str:
    text = TAG_RE.sub("", markup)
    return re.sub(r"\s+", " ", text).strip()


def page_header(
    *,
    h1: str,
    subtitle: str,
    trail: list[tuple[str, str]],
    cta: str = "Request Your Free Tax Assessment",
) -> str:
    """The site's standard article masthead: breadcrumb, H1, subtitle, CTA."""
    crumbs = []
    for name, href in trail[:-1]:
        crumbs.append(f'<a href="{href}">{name}</a>')
    crumbs.append(f"<span>{trail[-1][0]}</span>")
    crumb_html = " &rsaquo; ".join(crumbs)
    return f"""    <section class="page-header">
        <div class="container narrow">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                {crumb_html}
            </nav>
            <h1>{h1}</h1>
            <p class="subtitle">{subtitle}</p>
            <div class="cta-buttons">
                <a href="/discovery/" class="btn-cta btn-lg">{cta}</a>
            </div>
        </div>
    </section>"""


def section(heading: str, body: str) -> str:
    """One standard content block."""
    return f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <h2>{heading}</h2>
{body}
        </div>
    </section>"""


def faq_section(faqs: list[tuple[str, str]], heading: str = "Frequently Asked Questions") -> str:
    items = "\n".join(
        f"""            <div class="faq-item">
                <h3>{q}</h3>
                {a}
            </div>"""
        for q, a in faqs
    )
    return f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <h2>{heading}</h2>
{items}
        </div>
    </section>"""


def related_section(links: list[tuple[str, str]], heading: str = "Related Reading") -> str:
    items = "\n".join(
        f'                <li><a href="{href}">{label}</a></li>' for href, label in links
    )
    return f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <h2>{heading}</h2>
            <ul class="related-links">
{items}
            </ul>
        </div>
    </section>"""


def takeaways(points: list[str], heading: str = "Key Takeaways") -> str:
    items = "\n".join(f"                <li>{p}</li>" for p in points)
    return f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <h2>{heading}</h2>
            <ul class="takeaway-list">
{items}
            </ul>
        </div>
    </section>"""


def definition(text: str) -> str:
    """Lead paragraph styled as a definition, for AI overview extraction."""
    return f'            <p class="definition-lead">{text}</p>'


CTA_BLOCK = """    <section class="content-section fade-in-section" style="background:var(--light-bg);">
        <div class="container narrow center-text">
            <h2>Talk Through Your Situation</h2>
            <p>Every situation turns on its own facts. Schedule a discovery call and we will
            walk through what applies to you, what it is worth, and what it would take to
            put it in place.</p>
            <div class="center-cta" style="margin-top:20px;">
                <a href="/discovery/" class="btn-cta btn-lg">Schedule Your Free Discovery Call</a>
            </div>
        </div>
    </section>"""


def build_page(
    *,
    title: str,
    description: str,
    path: str,
    body: str,
    schemas: list[dict],
    published: str,
    modified: str,
    active_nav: str | None = None,
    og_type: str = "article",
    extra_head: str = "",
) -> str:
    """Assemble a complete, standards-compliant page."""
    c = chrome()
    url = f"{SITE}{path}"
    t, d = esc(title), esc(description)
    schema_markup = "\n".join(jsonld(s) for s in schemas)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t}</title>
    <meta name="description" content="{d}">
    <link rel="canonical" href="{url}">
    <meta name="author" content="{AUTHOR}">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
    <meta property="og:title" content="{t}">
    <meta property="og:description" content="{d}">
    <meta property="og:url" content="{url}">
    <meta property="og:type" content="{og_type}">
    <meta property="og:site_name" content="{BRAND}">
    <meta property="og:image" content="{SITE}/assets/ae-tax-logo.png">
    <meta property="article:published_time" content="{published}T00:00:00-06:00">
    <meta property="article:modified_time" content="{modified}T00:00:00-06:00">
    <meta property="article:author" content="{AUTHOR}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{t}">
    <meta name="twitter:description" content="{d}">
    <meta name="twitter:image" content="{SITE}/assets/ae-tax-logo.png">
    <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/style.css">
{schema_markup}
{extra_head}
</head>
<body>
{c.header_for(active_nav)}

    <main>
{body}
{CTA_BLOCK}
    </main>

{c.footer}

{c.sticky}

    {c.script}
</body>
</html>
"""


def write_page(path: str, html_text: str) -> Path:
    """Write to <path>/index.html, creating the directory."""
    out = ROOT / path.strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_text, encoding="utf-8")
    return out
