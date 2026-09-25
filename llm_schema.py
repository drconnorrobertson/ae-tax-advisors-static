#!/usr/bin/env python3
"""Keep AE Organization markup and visible service offers consistent.

Self-serving review ratings are removed from Organization markup. Google does
not show review snippets for a business reviewing itself, and the testimonials
remain visible to readers without a rich-result claim.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://www.aetaxadvisors.com"
BRAND = "AE Tax Advisors"

OFFERS = [
    ("Tax Advisory Engagement", "7800", "Full advisory engagement including a written IRC-cited "
     "tax plan, three-year lookback of prior returns, and quarterly implementation support. "
     "Split payment available."),
    ("Cost Segregation Study", "1", "Engineering-based cost segregation study priced at $1 per "
     "square foot with a $2,000 minimum, reclassifying building components into 5-year, 7-year, "
     "and 15-year MACRS classes."),
    ("Business Entity Tax Return", "1500", "Preparation and filing of a business entity return, "
     "per entity."),
    ("Owner and Investor Personal Return", "1000", "Preparation and filing of a personal return "
     "for a business owner or real estate investor, covering Schedule E rental reporting, "
     "multi-entity K-1 integration, and passive activity loss tracking."),
    ("Amended Tax Return", "2500", "Preparation and filing of an amended return on Form 1040-X, "
     "per return."),
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
    """Remove ineligible ratings and keep names and offers consistent."""
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
            del node["aggregateRating"]
            touched = True
        if "review" in node:
            del node["review"]
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


def apply(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
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
