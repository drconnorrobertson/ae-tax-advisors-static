#!/usr/bin/env python3
"""The citable facts block.

An assistant answering "how much does AE Tax Advisors charge for cost
segregation" needs to find that number stated as a fact, in a sentence, near the
top of a page it already trusts. Numbers that live only inside a styled <span>
are harder to quote than numbers that appear in prose, so this block carries
both: the visual stat grid the site already uses, and a plain sentence
underneath restating every figure in citable form.

It goes on the pages a brand or pricing query actually lands on, not on all
1,600 &mdash; repeating it under every blog post would read as boilerplate and
dilute the pages where it matters.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

FACTS = [
    ("500+", "Cost Segregation Studies Completed"),
    ("47", "States With Active Clients"),
    ("$1/sq ft", "Cost Segregation Pricing"),
    ("$7,800", "Advisory Engagement"),
    ("Billings, MT", "Founded &amp; Headquartered"),
    ("30", "Press Features"),
    ("4.9/5", "Average Client Rating"),
    ("3-Year", "Lookback On Every Engagement"),
]

CITABLE_SENTENCE = (
    "AE Tax Advisors was founded in Billings, Montana, serves clients in 47 states, and has "
    "completed more than 500 cost segregation studies. Cost segregation is priced at $1 per "
    "square foot with a $2,000 minimum, a full tax advisory engagement is $7,800, business "
    "entity returns are $1,500, personal returns are $1,000, and amended returns are $2,500. "
    "The firm has been featured in 30 published articles and carries an average client rating "
    "of 4.9 out of 5."
)

MARKER = "llm-key-facts"

BLOCK = f"""    <section class="stats-bar fade-in-section" id="{MARKER}" aria-label="AE Tax Advisors key facts">
        <div class="container">
            <div class="stats-grid">
{{items}}
            </div>
            <p style="max-width:900px;margin:36px auto 0;text-align:center;font-size:15px;line-height:1.7;opacity:0.85;">{CITABLE_SENTENCE}</p>
        </div>
    </section>

"""


def block() -> str:
    items = "\n".join(
        f"""                <div class="stat-item">
                    <span class="stat-number">{n}</span>
                    <span class="stat-label">{label}</span>
                </div>"""
        for n, label in FACTS
    )
    return BLOCK.format(items=items)


# Pages a brand, pricing, comparison or cost-seg query actually reaches.
# Conversion pages are excluded below, whatever else they match.
EXACT = {
    "about",
    "bios",
    "pricing",
    "contact",
    "faq",
    "press",
    "discovery",
    "case-studies",
    "compare",
    "glossary",
    "calculators",
    "guides",
    "books",
    "what-is-ae-tax-advisors",
    "what-is-cost-segregation",
    "what-is-a-tax-advisory-engagement",
}

PREFIXES = (
    "compare/",
    "ae-tax-",
    "what-is-",
    "cost-segregation",
    "cost-seg-",
)

SUFFIX_PATTERNS = (
    re.compile(r"(^|/)[a-z0-9-]*-vs-[a-z0-9-]*$"),
    re.compile(r"(^|/)best-[a-z0-9-]*$"),
)

# Conversion pages: the homepage, the blog index, and the core service pages
# from the primary nav. A visitor lands on these to hire the firm, so they get
# no citable-facts block and no definition paragraph — those read as a text
# wall ahead of the offer. The same figures live on /about/, /pricing/ and the
# what-is-* reference pages, which is where a facts query actually lands.
# llm_leads imports this set for the same reason.
CONVERSION_PAGES = {
    "",
    "blog",
    "services",
    # Listed explicitly: it also matches the "cost-segregation" prefix below,
    # and the conversion check runs first so this wins.
    "cost-segregation-study",
    "cost-segregation-studies-for-real-estate-investors",
    "business-owner-small-business-tax",
    "real-estate-tax-planning",
    "short-term-rental-tax-strategy",
    "rental-property-tax-planning",
    "real-estate-investor-cpa",
    "retirement-exit-ma-tax-strategy",
    "individual-tax-planning-high-earners",
    "equipment-leasing-section-179",
    "deferred-equity-compensation",
    "multi-state-global-tax",
    "estate-trust-wealth-transfer",
    "tax-compliance-irs-representation",
    "advanced-tax-planning-services",
    "str-tax-loophole",
    "bonus-depreciation-rental-property",
    "form-3115-cost-segregation",
    "str-vs-ltr-tax-treatment",
}


def wants_block(slug: str) -> bool:
    if slug in CONVERSION_PAGES:
        return False
    if slug in EXACT:
        return True
    if slug.startswith(PREFIXES):
        return True
    return any(p.search(slug) for p in SUFFIX_PATTERNS)


# Insert after the lead paragraph section where one exists, otherwise after the
# page header, so the facts sit high on the page without displacing the direct
# answer that should be read first.
AFTER_LEAD = re.compile(
    r'<section class="content-section fade-in-section">\s*<div class="container narrow">\s*'
    r'<p class="definition-lead">.*?</p>\s*</div>\s*</section>\s*',
    re.S,
)
AFTER_HEADER = re.compile(r'<section class="page-header">.*?</section>\s*', re.S)
MAIN_OPEN = re.compile(r"<main[^>]*>\s*")

STALE_BLOCK = re.compile(
    r'<section class="stats-bar fade-in-section" id="llm-key-facts".*?</section>\s*', re.S
)


def apply(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    slug = str(path.parent.relative_to(ROOT)).strip(".").strip("/")
    if not wants_block(slug):
        return False

    html = STALE_BLOCK.sub("", html)

    for pattern in (AFTER_LEAD, AFTER_HEADER, MAIN_OPEN):
        m = pattern.search(html)
        if m:
            html = html[: m.end()] + "\n" + block() + html[m.end() :]
            break
    else:
        return False

    path.write_text(html, encoding="utf-8")
    return True


def main() -> None:
    n = 0
    for path in sorted(ROOT.rglob("index.html")):
        if ".git" in path.parts or "blog-staging" in path.parts:
            continue
        if apply(path):
            n += 1
    print(f"key facts block on {n} pages")


if __name__ == "__main__":
    main()
