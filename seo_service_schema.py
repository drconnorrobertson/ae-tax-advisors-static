#!/usr/bin/env python3
"""Add Service schema to service pages and rewrite robots.txt for crawl efficiency."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://aetaxadvisors.com"
ORG_ID = f"{SITE}/#organization"

# url slug -> (service name, service type, short description)
SERVICES = {
    "cost-segregation-study": ("Cost Segregation Study", "Cost Segregation",
        "Engineering-based cost segregation studies that reclassify building components into 5, 7, and 15-year MACRS classes for immediate bonus depreciation."),
    "business-owner-small-business-tax": ("Business Owner Tax Advisory", "Tax Planning",
        "Strategic tax planning for business owners covering entity structure, reasonable compensation, retirement plan design, and year-round advisory."),
    "real-estate-tax-planning": ("Real Estate Tax Planning", "Tax Planning",
        "Tax strategy for real estate investors including depreciation planning, passive activity analysis, and real estate professional status."),
    "short-term-rental-tax-strategy": ("Short-Term Rental Tax Strategy", "Tax Planning",
        "Short-term rental tax planning covering the seven-day exception, material participation documentation, and cost segregation."),
    "rental-property-tax-planning": ("Rental Property Tax Planning", "Tax Planning",
        "Long-term rental tax planning including depreciation strategy, Form 3115 catch-up filings, and entity structure."),
    "real-estate-investor-cpa": ("CPA Services for Real Estate Investors", "Accounting",
        "Tax preparation and advisory for real estate investors, including K-1 integration and multi-entity returns."),
    "retirement-exit-ma-tax-strategy": ("Retirement, Exit and M&A Tax Strategy", "Tax Planning",
        "Exit planning covering purchase price allocation, installment sales, qualified small business stock, and retirement plan design."),
    "individual-tax-planning-high-earners": ("Advanced Income and Entity Planning", "Tax Planning",
        "Tax planning for high-income individuals covering deduction capacity, entity structure, and charitable strategy."),
    "estate-trust-wealth-transfer": ("Estate, Trust and Wealth Transfer Planning", "Tax Planning",
        "Coordination of income tax strategy with transfer tax planning and the basis step-up under IRC Section 1014."),
    "tax-compliance-irs-representation": ("Tax Compliance and IRS Representation", "Tax Preparation",
        "Federal and state tax return preparation plus representation before the IRS in examinations, appeals, and collections."),
    "multi-state-global-tax": ("Multi-State Tax Planning", "Tax Planning",
        "Nexus, apportionment, residency, and pass-through entity tax elections for clients earning across state lines."),
    "equipment-leasing-section-179": ("Equipment and Section 179 Planning", "Tax Planning",
        "Depreciation planning for equipment purchases using Section 179 expensing, bonus depreciation, and MACRS."),
    "crypto-mining-tax-strategy": ("Digital Asset Tax Strategy", "Tax Planning",
        "Tax planning for cryptocurrency mining, staking, and digital asset dispositions."),
    "deferred-equity-compensation": ("Deferred Compensation and Equity Planning", "Tax Planning",
        "Planning around restricted stock units, incentive stock options, and deferred compensation."),
    "audit-defense-compliance": ("IRS Audit Defense", "IRS Representation",
        "Representation in IRS examinations, appeals, and collection matters under a power of attorney."),
    "services/bookkeeping": ("Bookkeeping Services", "Bookkeeping",
        "Monthly bookkeeping and financial statement preparation that supports proactive tax planning."),
    "services/entity-structuring": ("Entity Structuring", "Tax Planning",
        "Entity selection and restructuring across LLC, S corporation, C corporation, and holding structures."),
    "services/tax-planning": ("Strategic Tax Planning", "Tax Planning",
        "Comprehensive tax strategy engagements including a three-year lookback and an IRC-cited plan."),
    "services/cost-segregation": ("Cost Segregation Services", "Cost Segregation",
        "Engineering-based cost segregation with Form 3115 catch-up filings and passive activity analysis."),
}

LD_INSERT = "</head>"


def service_node(slug: str, name: str, stype: str, desc: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "serviceType": stype,
        "description": desc,
        "url": f"{SITE}/{slug}/",
        "provider": {"@id": ORG_ID},
        "areaServed": {"@type": "Country", "name": "United States"},
        "audience": {
            "@type": "Audience",
            "audienceType": "Business owners, real estate investors, and high-income professionals",
        },
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": f"{name} engagements",
            "itemListElement": [
                {"@type": "Offer", "name": "Strategic Tax Advisory Engagement",
                 "price": "7800", "priceCurrency": "USD",
                 "priceSpecification": {
                     "@type": "PriceSpecification", "price": "7800",
                     "priceCurrency": "USD",
                     "description": "Comprehensive advisory engagement, payable in two installments."}},
                {"@type": "Offer", "name": "Cost Segregation Study",
                 "priceCurrency": "USD",
                 "priceSpecification": {
                     "@type": "UnitPriceSpecification", "price": "1",
                     "priceCurrency": "USD",
                     "unitText": "per square foot",
                     "minPrice": "2000",
                     "description": "$1 per square foot with a $2,000 minimum."}},
            ],
        },
    }


def add_service_schema() -> int:
    n = 0
    for slug, (name, stype, desc) in SERVICES.items():
        path = ROOT / slug / "index.html"
        if not path.exists():
            print(f"  skip (missing): /{slug}/")
            continue
        html = path.read_text(encoding="utf-8")
        if '"@type": "Service"' in html:
            continue
        block = ('<script type="application/ld+json">\n'
                 + json.dumps(service_node(slug, name, stype, desc),
                              indent=2, ensure_ascii=False)
                 + "\n</script>\n")
        at = html.find(LD_INSERT)
        if at == -1:
            continue
        path.write_text(html[:at] + block + html[at:], encoding="utf-8")
        n += 1
    return n


ROBOTS = """# robots.txt for aetaxadvisors.com
# AE Tax Advisors serves clients nationwide from Billings, Montana.

User-agent: *
Allow: /

# Staging duplicates of live blog posts. These carry noindex and canonicals
# pointing at /blog/, but blocking them here keeps crawl budget on real pages.
Disallow: /blog-staging/

# Query-string variants create duplicate crawl paths with no unique content.
Disallow: /*?utm_
Disallow: /*?fbclid
Disallow: /*?gclid
Disallow: /*?ref=
Disallow: /*?v=

# Let every major crawler through at full speed. No crawl-delay: it slows
# indexing and the major engines ignore it anyway.
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: DuckDuckBot
Allow: /

# AI answer engines. Allowed deliberately: the site is built to be cited.
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot
Allow: /

User-agent: Applebot-Extended
Allow: /

# Aggressive SEO crawlers that consume budget without sending traffic.
User-agent: AhrefsBot
Disallow: /

User-agent: SemrushBot
Disallow: /

User-agent: DotBot
Disallow: /

User-agent: MJ12bot
Disallow: /

Sitemap: https://aetaxadvisors.com/sitemap.xml
"""


def main() -> int:
    n = add_service_schema()
    print(f"Service schema added to {n} service pages")
    (ROOT / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    print("robots.txt rewritten for crawl efficiency")
    return 0


if __name__ == "__main__":
    sys.exit(main())
