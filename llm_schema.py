#!/usr/bin/env python3
"""Structured data pass: Review, Offer pricing, and Organization consistency.

Three things this fixes.

1. The site published testimonials as prose but carried no Review markup, so
   nothing machine-readable backed the rating claim. The reviews below are the
   ones already published on /ae-tax-advisors-reviews/ &mdash; this only makes
   the existing content parseable, it does not invent testimony.

2. The Organization schema claimed a 5.0 rating while the reviews page claimed
   4.9. A model that sees a source contradict itself on a checkable number
   discounts the whole source. Both now say 4.9.

3. The published prices existed only as prose. They are now Offer nodes with
   priceSpecification, so "what does AE Tax Advisors charge" is answerable from
   the markup alone.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://www.aetaxadvisors.com"
BRAND = "AE Tax Advisors"

RATING = "4.9"
REVIEW_COUNT = "127"

# Verbatim from the testimonials already published on /ae-tax-advisors-reviews/.
REVIEWS = [
    {
        "author": "David M.",
        "role": "Business Owner",
        "headline": "Finally, a CPA Who Thinks Strategically",
        "body": (
            "I spent 15 years with a big accounting firm that prepared my tax return annually. "
            "I always owed $30,000-40,000 in taxes. After one consultation with AE Tax Advisors, "
            "they restructured my business as an S-corp and identified $50,000 in deductions I'd "
            "been missing. My tax bill dropped to $12,000. The investment in strategic planning "
            "paid for itself in the first year."
        ),
    },
    {
        "author": "Jennifer R.",
        "role": "Real Estate Investor",
        "headline": "They Saved Me $150,000",
        "body": (
            "I own three rental properties worth $2.5M. My previous CPA had never mentioned cost "
            "segregation. AE Tax Advisors recommended a cost seg study on one property, which "
            "generated $120,000 in depreciation deductions in year one. That single "
            "recommendation has saved me $30,000+ in annual taxes."
        ),
    },
    {
        "author": "Michael T.",
        "role": "Physician",
        "headline": "Professional, Knowledgeable, and Responsive",
        "body": (
            "As a surgeon, I wanted to minimize my tax burden without taking on risky strategies. "
            "AE Tax Advisors understood exactly what I needed: aggressive but compliant planning. "
            "They recommended a backdoor Roth strategy, helped me set up a Solo 401(k), and "
            "reviewed my W-4 withholding. They also prepared my return and defended me in an IRS "
            "inquiry."
        ),
    },
    {
        "author": "Kevin P.",
        "role": "Consultant",
        "headline": "Great for Business Owners",
        "body": (
            "Running a consulting business means managing 1099 income from multiple clients. AE "
            "Tax Advisors helped me organize my 1099 tracking, maximize business deductions, and "
            "stay compliant with estimated tax payments. They also fielded a CP2000 notice from "
            "the IRS, had it resolved in three weeks with zero liability."
        ),
    },
    {
        "author": "Rachel S.",
        "role": "Attorney",
        "headline": "They Prepare for Audits, Not Just Tax Returns",
        "body": (
            "What impressed me most about AE Tax Advisors was their focus on building an "
            "audit-proof return. Every recommendation came with documentation and justification. "
            "When I asked if a strategy was aggressive, they explained the case law and IRS "
            "guidance backing it up."
        ),
    },
]

OFFERS = [
    ("Tax Advisory Engagement", "7800", "Full advisory engagement including a written IRC-cited "
     "tax plan, three-year lookback of prior returns, and quarterly implementation support. "
     "Split payment available."),
    ("Cost Segregation Study", "1", "Engineering-based cost segregation study priced at $1 per "
     "square foot with a $2,000 minimum, reclassifying building components into 5-year, 7-year, "
     "and 15-year MACRS classes."),
    ("Business Entity Tax Return", "1500", "Preparation and filing of a business entity return, "
     "per entity."),
    ("Personal Tax Return", "1000", "Preparation and filing of an individual Form 1040."),
    ("Amended Tax Return", "2500", "Preparation and filing of an amended return on Form 1040-X, "
     "per return."),
]


def review_nodes() -> list[dict]:
    return [
        {
            "@type": "Review",
            "name": r["headline"],
            "reviewBody": r["body"],
            "author": {"@type": "Person", "name": r["author"], "jobTitle": r["role"]},
            "reviewRating": {
                "@type": "Rating",
                "ratingValue": "5",
                "bestRating": "5",
                "worstRating": "1",
            },
            "itemReviewed": {"@type": "Organization", "name": BRAND, "url": f"{SITE}/"},
        }
        for r in REVIEWS
    ]


def offer_catalog() -> dict:
    return {
        "@type": "OfferCatalog",
        "name": "AE Tax Advisors Services and Pricing",
        "itemListElement": [
            {
                "@type": "Offer",
                "name": name,
                "description": desc,
                "priceSpecification": {
                    "@type": "PriceSpecification",
                    "price": price,
                    "priceCurrency": "USD",
                    **(
                        {"unitText": "square foot"}
                        if name == "Cost Segregation Study"
                        else {}
                    ),
                },
                "itemOffered": {"@type": "Service", "name": name, "description": desc},
            }
            for name, price, desc in OFFERS
        ],
    }


def review_page_schema() -> dict:
    """A standalone node carrying the reviews, for the reviews page itself."""
    return {
        "@context": "https://schema.org",
        "@type": ["Organization", "AccountingService"],
        "name": BRAND,
        "url": f"{SITE}/",
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": RATING,
            "reviewCount": REVIEW_COUNT,
            "bestRating": "5",
            "worstRating": "1",
        },
        "review": review_nodes(),
    }


JSONLD = re.compile(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', re.S)


def _walk(node, fn):
    if isinstance(node, dict):
        fn(node)
        for v in node.values():
            _walk(v, fn)
    elif isinstance(node, list):
        for v in node:
            _walk(v, fn)


def normalize_org(data):
    """Bring every Organization node in line on rating, alt names, and offers."""
    touched = False

    def fix(node: dict):
        nonlocal touched
        t = node.get("@type")
        types = t if isinstance(t, list) else [t]
        if not any(x in ("Organization", "AccountingService", "ProfessionalService", "LocalBusiness") for x in types):
            return
        if node.get("name") != BRAND:
            return
        if "aggregateRating" in node:
            ar = node["aggregateRating"]
            if ar.get("ratingValue") != RATING or ar.get("reviewCount") != REVIEW_COUNT:
                ar["ratingValue"] = RATING
                ar["reviewCount"] = REVIEW_COUNT
                touched = True
        if node.get("alternateName") != ["AE Tax", "AE Tax Advisors LLC"]:
            node["alternateName"] = ["AE Tax", "AE Tax Advisors LLC"]
            touched = True
        # Replace the name-only offer catalog with one that carries prices.
        if "hasOfferCatalog" in node:
            new = offer_catalog()
            if node["hasOfferCatalog"] != new:
                node["hasOfferCatalog"] = new
                touched = True

    _walk(data, fix)
    return touched


REVIEW_PAGES = {"ae-tax-advisors-reviews", "ae-tax-advisors-faq", "about", "pricing", "", "what-is-ae-tax-advisors"}


def apply(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    slug = str(path.parent.relative_to(ROOT)).strip(".").strip("/")
    changed = False

    def repl(m: re.Match) -> str:
        nonlocal changed
        raw = m.group(1)
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return m.group(0)
        if normalize_org(data):
            changed = True
            body = json.dumps(data, indent=2, ensure_ascii=False)
            return f'<script type="application/ld+json">\n{body}\n</script>'
        return m.group(0)

    html = JSONLD.sub(repl, html)

    # Attach the Review nodes on the pages where a reputation query lands.
    if slug in REVIEW_PAGES and '"@type": "Review"' not in html:
        body = json.dumps(review_page_schema(), indent=2, ensure_ascii=False)
        block = f'<script type="application/ld+json">\n{body}\n</script>\n</head>'
        html = html.replace("</head>", block, 1)
        changed = True

    if changed:
        path.write_text(html, encoding="utf-8")
    return changed


def main() -> None:
    n = 0
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts:
            continue
        if apply(path):
            n += 1
    print(f"schema normalized on {n} pages")


if __name__ == "__main__":
    main()
