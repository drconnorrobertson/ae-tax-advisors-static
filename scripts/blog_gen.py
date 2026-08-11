"""Generate AE Tax Advisors blog articles from structured data.

Each article dict supports:
    slug, title (h1), meta_title, meta_desc, category, date (YYYY-MM-DD),
    intro (list of paragraphs), sections (list of (h2, [paragraphs])),
    faqs (list of (question, answer)), cta_head, cta_body, cta_link,
    cta_label, related (list of (href, anchor text)).

Body paragraphs may contain inline HTML (links, <ul>, <strong>).
"""

import html
import json
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_chrome import HEADER, FOOTER  # noqa: E402

SITE = "https://aetaxadvisors.com"
BOOKING = "https://api.leadconnectorhq.com/widget/booking/5bPhybfzi6mKUTgn5GMg"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def pretty_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{MONTHS[m - 1]} {d}, {y}"


def strip_tags(text):
    out, depth = [], 0
    for ch in text:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif depth == 0:
            out.append(ch)
    return "".join(out)


def esc(text):
    """Escape for attribute or JSON-LD string values."""
    return html.escape(strip_tags(text), quote=True)


def blogposting_ld(a, url):
    return {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": strip_tags(a["title"]),
        "description": a["meta_desc"],
        "datePublished": a["date"],
        "dateModified": a["date"],
        "author": {
            "@type": "Organization",
            "name": "AE Tax Advisors",
            "url": SITE,
        },
        "publisher": {
            "@type": "Organization",
            "name": "AE Tax Advisors",
            "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/logo.svg"},
        },
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "url": url,
        "image": f"{SITE}/assets/logo.svg",
        "articleSection": a["category"],
    }


PROFESSIONAL_SERVICE_LD = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "AE Tax Advisors",
    "description": ("Proactive tax planning for high-income professionals, "
                    "executives, physicians, attorneys, and business owners "
                    "earning $500K or more."),
    "url": SITE,
    "telephone": "(631) 614-5762",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "935 Lake Elmo Dr, Suite B",
        "addressLocality": "Billings",
        "addressRegion": "MT",
        "postalCode": "59105",
        "addressCountry": "US",
    },
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "reviewCount": "127",
        "bestRating": "5",
        "worstRating": "1",
    },
    "priceRange": "$$$",
    "openingHours": "Mo-Fr 09:00-17:00",
}


def faq_ld(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": strip_tags(q),
                "acceptedAnswer": {"@type": "Answer", "text": strip_tags(ans)},
            }
            for q, ans in faqs
        ],
    }


def breadcrumb_ld(a):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home",
             "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog",
             "item": f"{SITE}/blog/"},
            {"@type": "ListItem", "position": 3, "name": strip_tags(a["title"])},
        ],
    }


def ld_block(obj):
    return ('    <script type="application/ld+json">\n'
            + json.dumps(obj, indent=2, ensure_ascii=False)
            + "\n    </script>\n")


def word_count(a):
    parts = list(a["intro"])
    for _, paras in a["sections"]:
        parts.extend(paras)
    for q, ans in a["faqs"]:
        parts.append(q)
        parts.append(ans)
    return len(strip_tags(" ".join(parts)).split())


def render(a):
    url = f"{SITE}/blog/{a['slug']}/"
    mt = esc(a["meta_title"])
    md = esc(a["meta_desc"])

    head = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{mt}</title>
    <meta name="description" content="{md}">
    <link rel="canonical" href="{url}">
    <meta property="og:title" content="{mt}">
    <meta property="og:description" content="{md}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{SITE}/assets/ae-tax-logo.png">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="AE Tax Advisors">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{mt}">
    <meta name="twitter:description" content="{md}">
    <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/style.css">
"""
    head += ld_block(blogposting_ld(a, url))
    head += ld_block(PROFESSIONAL_SERVICE_LD)
    head += ld_block(faq_ld(a["faqs"]))
    head += ld_block(breadcrumb_ld(a))
    head += "</head>\n"

    title = a["title"]
    body = [
        HEADER,
        '    <main>\n',
        '    <section class="page-header"><div class="container">\n',
        f'        <div class="breadcrumbs"><a href="/">Home</a> &raquo; '
        f'<a href="/blog/">Blog</a> &raquo; {title}</div>\n',
        f"            <h1>{title}</h1>\n",
        f'        <p class="blog-meta">Published on {pretty_date(a["date"])} | '
        f'{a["category"]} | AE Tax Advisors</p>\n',
        "    </div></section>\n",
        '    <section class="content-section fade-in-section">'
        '<div class="container narrow">\n\n',
    ]

    for p in a["intro"]:
        body.append(f"        <p>{p}</p>\n\n")

    for heading, paras in a["sections"]:
        body.append(f"        <h2>{heading}</h2>\n\n")
        for p in paras:
            tag = "p" if not p.startswith("<") else None
            body.append(f"        <p>{p}</p>\n\n" if tag else f"        {p}\n\n")

    body.append("        <h2>Frequently Asked Questions</h2>\n\n")
    for q, ans in a["faqs"]:
        body.append(f"        <h3>{q}</h3>\n")
        body.append(f"        <p>{ans}</p>\n\n")

    if a.get("related"):
        body.append("        <h2>Related Reading</h2>\n")
        body.append('        <ul class="related-links">\n')
        for href, text in a["related"]:
            body.append(f'            <li><a href="{href}">{text}</a></li>\n')
        body.append("        </ul>\n\n")

    body.append('        <hr style="margin: 48px 0; border: none; '
                'border-top: 1px solid #e5e7eb;">\n\n')
    body.append(f"""        <div style="background: #f0f4ff; border-left: 4px solid #2563eb; padding: 24px 28px; border-radius: 8px; margin-top: 32px;">
            <h3 style="margin-top: 0; color: #1e3a8a;">{a['cta_head']}</h3>
            <p style="margin-bottom: 20px;">{a['cta_body']}</p>
            <iframe src="{BOOKING}" allow="payment" style="width:100%;border:none;overflow:hidden;min-height:700px;border-radius:8px;background:#fff;" scrolling="no" title="Book a tax strategy call with AE Tax Advisors"></iframe>
            <p style="margin-top:18px;margin-bottom:0;font-size:15px;">Prefer to talk first? Call <a href="tel:+16316145762">(631) 614-5762</a> or email <a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a>.</p>
        </div>

    </div></section>
""")
    body.append(FOOTER)
    return head + "".join(body)


def write(a, verbose=True):
    out_dir = os.path.join(ROOT, "blog", a["slug"])
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "index.html")
    with open(path, "w") as fh:
        fh.write(render(a))
    if verbose:
        print(f"{word_count(a):5d} words  blog/{a['slug']}/")
    return path


def write_all(articles):
    for a in articles:
        wc = word_count(a)
        if wc < 780:
            print(f"WARNING short ({wc}): {a['slug']}")
        write(a)
    print(f"\n{len(articles)} articles written.")
