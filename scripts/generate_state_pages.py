#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the AE Tax Advisors state location landing pages.

Header, footer, sticky CTA, and the fade-in script are lifted verbatim from an
existing published page so the new pages stay in sync with the rest of the site
and use the same design system (/assets/style.css, Inter + Playfair Display,
--primary / --accent / --dark / --light-bg).

Usage:  python3 scripts/generate_state_pages.py
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from state_data import STATES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PAGE = os.path.join(ROOT, "blog", "cost-segregation-complete-guide", "index.html")
SITE = "https://aetaxadvisors.com"
BOOKING_URL = "https://api.leadconnectorhq.com/widget/booking/5bPhybfzi6mKUTgn5GMg"
TODAY = "2026-08-09"


def extract_chrome():
    """Pull the shared header and the footer-through-close-of-document blocks."""
    with open(TEMPLATE_PAGE, encoding="utf-8") as fh:
        html = fh.read()
    header = re.search(r"( *<header>.*?</header>)", html, re.S).group(1)
    footer = re.search(r"( *<footer>.*</html>)", html, re.S).group(1)
    return header, footer


def esc(text):
    """Escape for a JSON string literal inside a ld+json block."""
    return text.replace("\\", "\\\\").replace('"', '\\"')


def html_esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def paras(items):
    return "\n\n".join("        <p>%s</p>" % p for p in items)


def build_schema(st):
    title = "Cost Segregation Study in %s | %s Tax Advisor" % (st["name"], st["name"])
    url = "%s/%s/" % (SITE, st["slug"])

    organization = """{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "AE Tax Advisors",
  "url": "https://aetaxadvisors.com",
  "logo": "https://aetaxadvisors.com/assets/ae-tax-logo.png",
  "email": "team@aetaxadvisors.com",
  "telephone": "(631) 614-5762",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "935 Lake Elmo Dr., Suite B",
    "addressLocality": "Billings",
    "addressRegion": "MT",
    "postalCode": "59105",
    "addressCountry": "US"
  },
  "areaServed": "US",
  "serviceType": ["Tax Advisory", "Cost Segregation", "Entity Structuring", "Tax Planning"]
}"""

    professional_service = """{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "AE Tax Advisors",
  "url": "%s",
  "priceRange": "$$$$",
  "telephone": "(631) 614-5762",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "935 Lake Elmo Dr., Suite B",
    "addressLocality": "Billings",
    "addressRegion": "MT",
    "postalCode": "59105",
    "addressCountry": "US"
  },
  "areaServed": {
    "@type": "State",
    "name": "%s"
  },
  "knowsAbout": ["Cost Segregation", "S-Corporation", "C-Corporation", "Tax Planning", "Real Estate Tax Strategy", "Bonus Depreciation", "Section 179"]
}""" % (url, esc(st["name"]))

    faq_items = ",\n".join(
        """    {
      "@type": "Question",
      "name": "%s",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "%s"
      }
    }""" % (esc(q), esc(a))
        for q, a in st["faqs"]
    )
    faq = """{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
%s
  ]
}""" % faq_items

    breadcrumb = """{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "%s/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Locations",
      "item": "%s/locations/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "%s"
    }
  ]
}""" % (SITE, SITE, esc(st["name"]))

    service = """{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Cost Segregation Study in %s",
  "serviceType": "Cost Segregation",
  "description": "%s",
  "provider": {
    "@type": "Organization",
    "name": "AE Tax Advisors",
    "url": "https://aetaxadvisors.com"
  },
  "areaServed": {
    "@type": "State",
    "name": "%s"
  },
  "url": "%s"
}""" % (esc(st["name"]), esc(st["meta"]), esc(st["name"]), url)

    blocks = [organization, professional_service, service, faq, breadcrumb]
    return "\n".join(
        '    <script type="application/ld+json">\n%s\n    </script>' % b for b in blocks
    ), title, url


def build_page(st, header, footer):
    schema, title, url = build_schema(st)
    name = st["name"]
    meta = st["meta"]

    faq_html = "\n".join(
        """            <div class="faq-item">
                <h3>%s</h3>
                <p>%s</p>
            </div>""" % (html_esc(q), html_esc(a))
        for q, a in st["faqs"]
    )

    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>%(title)s | AE Tax Advisors</title>
    <meta name="description" content="%(meta)s">
    <link rel="canonical" href="%(url)s">
    <meta name="geo.region" content="US-%(abbr)s">
    <meta name="geo.placename" content="%(name)s">
    <meta property="og:title" content="%(title)s | AE Tax Advisors">
    <meta property="og:description" content="%(meta)s">
    <meta property="og:url" content="%(url)s">
    <meta property="og:image" content="https://aetaxadvisors.com/assets/ae-tax-logo.png">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="AE Tax Advisors">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="%(title)s | AE Tax Advisors">
    <meta name="twitter:description" content="%(meta)s">
    <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/style.css">
%(schema)s
</head>
<body>
%(header)s

    <main>
    <section class="page-header"><div class="container">
        <div class="breadcrumbs"><a href="/">Home</a> &raquo; <a href="/locations/">Locations</a> &raquo; %(name)s</div>
        <h1>Cost Segregation Study in %(name)s</h1>
        <p class="post-meta">%(name)s tax advisory for real estate investors and business owners | Updated %(today_long)s</p>
    </div></section>

    <section class="content-section fade-in-section"><div class="container">
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">%(rate_stat)s</div>
                <div class="stat-label">%(rate_label)s</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">%(ptet_stat)s</div>
                <div class="stat-label">%(ptet_label)s</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">%(conformity_stat)s</div>
                <div class="stat-label">%(conformity_label)s</div>
            </div>
        </div>
    </div></section>

    <section class="content-section fade-in-section"><div class="container narrow">

%(intro)s

        <h2>How %(name)s Income Tax Interacts With Federal Strategy</h2>

%(rate_section)s

        <h2>%(name)s Pass-Through Entity Tax</h2>

%(ptet_section)s

        <h2>%(name)s Depreciation Conformity</h2>

%(conformity_section)s

        <h2>Cost Segregation Considerations Specific to %(name)s</h2>

%(cost_seg_section)s

        <h2>Working With AE Tax Advisors in %(name)s</h2>

        <p>AE Tax Advisors works with real estate investors, business owners, and high-income professionals across %(name)s and all fifty states. We are a licensed CPA and IRS Enrolled Agent practice based in Billings, Montana, and we handle the engineering-based cost segregation study, the %(name)s conformity adjustments, the entity structuring, and the return preparation as one engagement rather than three vendors who do not talk to each other.</p>

        <p>That matters more in %(name)s than it does in a state with simple conformity. A cost segregation provider who delivers a federal-only report leaves you and your preparer to work out the %(name)s treatment after the fact, which is where the errors happen. We model the federal and %(name)s outcome together before the study is commissioned, so you know what the number actually is on both returns before you spend anything.</p>

        <p>Related reading: <a href="/blog/cost-segregation-complete-guide/">the complete guide to cost segregation</a>, <a href="/cost-segregation-study/">our cost segregation study service</a>, <a href="/blog/str-vs-ltr-which-saves-more-tax/">short-term versus long-term rental tax treatment</a>, <a href="/form-3115-cost-segregation/">lookback studies and Form 3115</a>, and <a href="/multi-state-global-tax/">multi-state tax planning</a>.</p>

    </div></section>

    <section class="faq-section fade-in-section"><div class="container narrow">
        <h2>%(name)s Cost Segregation and Tax Questions</h2>
%(faq_html)s
    </div></section>

    <section class="content-section fade-in-section"><div class="container narrow">
        <div style="background: var(--light-bg); padding: 40px; border-radius: 12px; text-align: center;">
            <h2 style="font-family: var(--font-heading); font-size: 26px; margin-bottom: 8px; color: var(--primary);">Book a %(name)s Tax Strategy Call</h2>
            <p style="color: #666; margin-bottom: 28px; font-size: 15px;">Pick a time below. We will walk through your %(name)s property or business, model the federal and %(name)s outcome side by side, and tell you plainly whether a study is worth running.</p>
            <div id="ghl-calendar" style="min-height: 600px; border-radius: 8px; overflow: visible; -webkit-overflow-scrolling: touch;">
                <iframe class="ghl-calendar-iframe" src="%(booking)s" style="width: 100%%; height: 700px; border: none; border-radius: 8px;" frameborder="0" scrolling="yes" title="Book a %(name)s tax strategy call with AE Tax Advisors"></iframe>
            </div>
        </div>
    </div></section>

    <section class="content-section fade-in-section"><div class="container narrow">
        <p style="font-size: 13px; color: #888; border-top: 1px solid rgba(0,0,0,0.08); padding-top: 20px;">%(name)s tax rates, pass-through entity tax rules, and depreciation conformity provisions described on this page reflect law in effect as of %(today_long)s and are provided for general information only. State conformity changes frequently and often retroactively. Nothing here is tax advice for your situation, and no client relationship is created by reading it. Talk to us about your facts before acting.</p>
    </div></section>
    </main>

%(footer)s
""" % {
        "title": title,
        "meta": meta,
        "url": url,
        "name": name,
        "abbr": st["abbr"],
        "schema": schema,
        "header": header,
        "footer": footer,
        "booking": BOOKING_URL,
        "today_long": "August 2026",
        "rate_stat": st["rate_stat"],
        "rate_label": st["rate_label"],
        "ptet_stat": st["ptet_stat"],
        "ptet_label": st["ptet_label"],
        "conformity_stat": st["conformity_stat"],
        "conformity_label": st["conformity_label"],
        "intro": paras(st["intro"]),
        "rate_section": paras(st["rate_section"]),
        "ptet_section": paras(st["ptet_section"]),
        "conformity_section": paras(st["conformity_section"]),
        "cost_seg_section": paras(st["cost_seg_section"]),
        "faq_html": faq_html,
    }


def build_index(states, header, footer):
    """A /locations/ hub so the state pages are internally linked, not orphaned."""
    cards = "\n".join(
        """            <a href="/%s/" class="blog-index-card">
                <h3>Cost Segregation in %s</h3>
                <p>%s tax rate %s. %s. %s.</p>
                <span class="card-link">Read the %s guide &rarr;</span>
            </a>""" % (
            s["slug"], s["name"], s["name"], s["rate_stat"],
            "PTET " + s["ptet_stat"] if s["ptet_stat"] not in ("N/A", "None") else "No PTET",
            "State bonus depreciation: " + s["conformity_stat"],
            s["name"],
        )
        for s in states
    )

    items = ",\n".join(
        """    {
      "@type": "ListItem",
      "position": %d,
      "name": "Cost Segregation Study in %s",
      "url": "%s/%s/"
    }""" % (i + 1, esc(s["name"]), SITE, s["slug"])
        for i, s in enumerate(states)
    )

    schema = """    <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "AE Tax Advisors",
  "url": "https://aetaxadvisors.com",
  "logo": "https://aetaxadvisors.com/assets/ae-tax-logo.png",
  "email": "team@aetaxadvisors.com",
  "telephone": "(631) 614-5762",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "935 Lake Elmo Dr., Suite B",
    "addressLocality": "Billings",
    "addressRegion": "MT",
    "postalCode": "59105",
    "addressCountry": "US"
  },
  "areaServed": "US",
  "serviceType": ["Tax Advisory", "Cost Segregation", "Entity Structuring", "Tax Planning"]
}
    </script>
    <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "AE Tax Advisors",
  "url": "%s/locations/",
  "priceRange": "$$$$",
  "telephone": "(631) 614-5762",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "935 Lake Elmo Dr., Suite B",
    "addressLocality": "Billings",
    "addressRegion": "MT",
    "postalCode": "59105",
    "addressCountry": "US"
  },
  "areaServed": "US",
  "knowsAbout": ["Cost Segregation", "S-Corporation", "C-Corporation", "Tax Planning", "Real Estate Tax Strategy", "Bonus Depreciation", "Section 179"]
}
    </script>
    <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "AE Tax Advisors State Tax Guides",
  "itemListElement": [
%s
  ]
}
    </script>
    <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "%s/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Locations"
    }
  ]
}
    </script>""" % (SITE, items, SITE)

    desc = ("State-by-state cost segregation and tax advisory guides from AE Tax Advisors. "
            "Each guide covers that state's income tax rate, pass-through entity tax rules, "
            "bonus depreciation conformity, and the cost segregation considerations specific to it.")

    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>State Tax Guides for Real Estate Investors | AE Tax Advisors</title>
    <meta name="description" content="%(desc)s">
    <link rel="canonical" href="%(site)s/locations/">
    <meta property="og:title" content="State Tax Guides for Real Estate Investors | AE Tax Advisors">
    <meta property="og:description" content="%(desc)s">
    <meta property="og:url" content="%(site)s/locations/">
    <meta property="og:image" content="https://aetaxadvisors.com/assets/ae-tax-logo.png">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="AE Tax Advisors">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="State Tax Guides for Real Estate Investors | AE Tax Advisors">
    <meta name="twitter:description" content="%(desc)s">
    <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/style.css">
%(schema)s
</head>
<body>
%(header)s

    <main>
    <section class="page-header"><div class="container">
        <div class="breadcrumbs"><a href="/">Home</a> &raquo; Locations</div>
        <h1>State Tax Guides for Real Estate Investors</h1>
        <p class="post-meta">Rates, pass-through entity tax rules, and depreciation conformity, state by state</p>
    </div></section>

    <section class="content-section fade-in-section"><div class="container narrow">
        <p class="lead-text">Cost segregation is a federal strategy, but what you actually keep depends on the state. Some states allow the full 100%% bonus depreciation deduction. Some disallow all of it. Some allow a fraction now and return the rest over five or seven years. Some have no income tax but tax the entity instead.</p>

        <p>These guides cover the details that change the answer: the state income tax rate, whether a pass-through entity tax election is available and on what terms, how the state conforms to federal bonus depreciation and Section 179, and the cost segregation issues specific to that state's property mix and rules.</p>
    </div></section>

    <section class="blog-index-section fade-in-section"><div class="container">
        <div class="blog-index-grid">
%(cards)s
        </div>
    </div></section>

    <section class="content-section fade-in-section"><div class="container narrow">
        <div style="background: var(--light-bg); padding: 40px; border-radius: 12px; text-align: center;">
            <h2 style="font-family: var(--font-heading); font-size: 26px; margin-bottom: 8px; color: var(--primary);">Not Seeing Your State?</h2>
            <p style="color: #666; margin-bottom: 28px; font-size: 15px;">We work with clients in all fifty states. Book a call and we will walk through your state's rules and your specific situation together.</p>
            <div id="ghl-calendar" style="min-height: 600px; border-radius: 8px; overflow: visible; -webkit-overflow-scrolling: touch;">
                <iframe class="ghl-calendar-iframe" src="%(booking)s" style="width: 100%%; height: 700px; border: none; border-radius: 8px;" frameborder="0" scrolling="yes" title="Book a tax strategy call with AE Tax Advisors"></iframe>
            </div>
        </div>
    </div></section>
    </main>

%(footer)s
""" % {
        "desc": desc,
        "site": SITE,
        "schema": schema,
        "header": header,
        "footer": footer,
        "cards": cards,
        "booking": BOOKING_URL,
    }


def main():
    header, footer = extract_chrome()
    written = []

    for st in STATES:
        out_dir = os.path.join(ROOT, st["slug"])
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "index.html")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(build_page(st, header, footer))
        written.append("/%s/" % st["slug"])
        print("wrote %s" % path)

    hub = os.path.join(ROOT, "locations")
    os.makedirs(hub, exist_ok=True)
    with open(os.path.join(hub, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(build_index(STATES, header, footer))
    written.append("/locations/")
    print("wrote %s" % os.path.join(hub, "index.html"))

    print("\n%d pages written" % len(written))
    return written


if __name__ == "__main__":
    main()
