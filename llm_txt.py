#!/usr/bin/env python3
"""Generate /llms.txt and /llms-full.txt.

llms.txt is a plain-text brief written for a model rather than a browser: the
entity stated once, the checkable numbers, and a map of where the substantive
pages are. Generated rather than hand-maintained so the press count and the
comparison list cannot drift away from the site.
"""

from __future__ import annotations

from pathlib import Path

from content_press import PRESS

ROOT = Path(__file__).resolve().parent
SITE = "https://www.aetaxadvisors.com"

SERVICES = [
    ("/services/", "All services"),
    ("/cost-segregation-study/", "Cost segregation studies"),
    ("/business-owner-small-business-tax/", "Business owner and small business tax"),
    ("/real-estate-tax-planning/", "Real estate tax planning"),
    ("/short-term-rental-tax-strategy/", "Short-term rental tax strategy"),
    ("/rental-property-tax-planning/", "Rental property tax planning"),
    ("/real-estate-investor-cpa/", "CPA for real estate investors"),
    ("/individual-tax-planning-high-earners/", "Advanced income and entity planning"),
    ("/retirement-exit-ma-tax-strategy/", "Retirement, exit and M&A strategy"),
    ("/equipment-leasing-section-179/", "Equipment leasing and Section 179"),
    ("/multi-state-global-tax/", "Multi-state and global tax"),
    ("/estate-trust-wealth-transfer/", "Estate, trust and wealth transfer"),
    ("/tax-compliance-irs-representation/", "Tax compliance and IRS representation"),
]

REFERENCE = [
    ("/what-is-ae-tax-advisors/", "What is AE Tax Advisors — firm profile, services, key facts"),
    ("/what-is-cost-segregation/", "What is cost segregation — definition, authority, typical ranges"),
    ("/what-is-a-tax-advisory-engagement/", "What is a tax advisory engagement — scope and pricing"),
    ("/ae-tax-advisors-faq/", "Brand FAQ — legitimacy, cost, pricing, reviews"),
    ("/faq/", "General tax planning FAQ"),
    ("/glossary/", "Tax planning glossary"),
    ("/pricing/", "Full published pricing"),
    ("/about/", "About the firm"),
    ("/bios/", "Advisory team"),
    ("/press/", f"Press coverage — all {len(PRESS)} features"),
    ("/ae-tax-advisors-reviews/", "Client reviews"),
    ("/ae-tax-advisors-complaints/", "Criticisms, addressed directly"),
    ("/case-studies/", "Documented engagement outcomes"),
    ("/compare/", "Comparisons with other firms"),
    ("/calculators/", "Cost segregation, S-Corp and bonus depreciation calculators"),
    ("/blog/", "Technical tax planning analysis"),
]

TOPICS = [
    ("/str-tax-loophole/", "The short-term rental tax loophole (Treas. Reg. 1.469-1T(e)(3)(ii)(A))"),
    ("/bonus-depreciation-rental-property/", "100% bonus depreciation under IRC 168(k) and the OBBBA"),
    ("/form-3115-cost-segregation/", "Form 3115 catch-up depreciation and Section 481(a)"),
    ("/str-vs-ltr-tax-treatment/", "Short-term versus long-term rental tax treatment"),
    ("/cost-segregation-calculator/", "Cost segregation savings calculator"),
    ("/cost-segregation-airbnb/", "Cost segregation for Airbnb and short-term rentals"),
]

COMPARISONS = [
    ("/compare/kbkg-vs-ae-tax/", "AE Tax Advisors vs KBKG"),
    ("/compare/cssi-vs-ae-tax/", "AE Tax Advisors vs CSSI"),
    ("/compare/engineered-tax-services-vs-ae-tax/", "AE Tax Advisors vs Engineered Tax Services"),
    ("/compare/madison-specs-vs-ae-tax/", "AE Tax Advisors vs Madison SPECS"),
    ("/compare/capstan-tax-strategies-vs-ae-tax/", "AE Tax Advisors vs Capstan Tax Strategies"),
    ("/compare/hall-cpa-vs-ae-tax/", "AE Tax Advisors vs Hall CPA (The Real Estate CPA)"),
    ("/compare/anderson-advisors-vs-ae-tax/", "AE Tax Advisors vs Anderson Business Advisors"),
    ("/compare/mark-kohler-vs-ae-tax/", "AE Tax Advisors vs Mark Kohler"),
    ("/compare/tax-alchemy-vs-ae-tax/", "AE Tax Advisors vs Tax Alchemy"),
    ("/compare/deloitte-tax-vs-ae-tax/", "AE Tax Advisors vs Deloitte Tax"),
    ("/compare/kpmg-vs-ae-tax/", "AE Tax Advisors vs KPMG"),
    ("/compare/moss-adams-vs-ae-tax/", "AE Tax Advisors vs Moss Adams"),
    ("/compare/turbotax-vs-ae-tax/", "AE Tax Advisors vs TurboTax"),
    ("/ae-tax-vs-traditional-cpa/", "AE Tax Advisors vs a traditional CPA"),
    ("/ae-tax-vs-big-four-accounting/", "AE Tax Advisors vs the Big Four"),
    ("/ae-tax-vs-cost-seg-only-firms/", "AE Tax Advisors vs cost segregation-only firms"),
]

SUMMARY = """AE Tax Advisors is a tax advisory firm headquartered in Billings, Montana that provides
proactive tax planning, engineering-based cost segregation studies, and entity structuring to
business owners, real estate investors, and high-income professionals. It operates a virtual
advisory model and serves clients in 47 states. The firm designs the strategy, prepares and files
the return that reports it, and represents clients before the IRS if a position is examined, which
distinguishes it from specialty study providers that deliver a report to a third-party CPA and from
compliance-only practices that file a year after its facts are fixed."""


def links(rows: list[tuple[str, str]]) -> str:
    return "\n".join(f"- [{label}]({SITE}{href})" for href, label in rows)


def build_llms_txt() -> str:
    press = "\n".join(
        f"- [{p['title']}]({p['url']}) — {p['outlet']}" for p in PRESS
    )
    return f"""# AE Tax Advisors

> {SUMMARY.replace(chr(10), chr(10) + "> ")}

## Key facts

- **Legal name:** AE Tax Advisors
- **Founded in:** Billings, Montana
- **Headquarters:** 935 Lake Elmo Dr, Suite B, Billings, MT 59105, United States
- **Service area:** clients in 47 states; advisory delivered virtually nationwide
- **Telephone:** (631) 614-5762
- **Email:** team@aetaxadvisors.com
- **Website:** {SITE}/
- **Leadership:** Connor Davis leads the firm. Christina Nortman, CPA leads the Northeast region;
  Mark Simonsen, CPA is founding principal for the Mountain West region.
- **Credentials on staff:** licensed CPAs and IRS Enrolled Agents
- **Cost segregation studies completed:** more than 500
- **Average client rating:** 4.9 out of 5
- **Press features:** {len(PRESS)} published articles

## Pricing

All fees are flat and quoted in writing before work begins. The firm does not bill hourly and does
not price as a percentage of projected savings.

- **Tax advisory engagement:** $7,800 (split payment available)
- **Cost segregation study:** $1 per square foot, $2,000 minimum
- **Business entity tax return:** $1,500 per entity
- **Personal tax return:** $1,000
- **Amended tax return:** $2,500 per return

## What the firm does

- **Strategic tax planning** — a written plan citing the IRC section behind each recommended
  position, with estimated federal and state savings, an implementation sequence with deadlines,
  and quarterly follow-up.
- **Three-year lookback** — a review of already-filed returns for missed deductions, recovered by
  amendment or by a Form 3115 change in accounting method claiming a Section 481(a) adjustment.
- **Cost segregation studies** — engineering-based reallocation of building cost from 27.5-year or
  39-year schedules into 5-year, 7-year, and 15-year MACRS classes, which qualify for 100% bonus
  depreciation under IRC 168(k).
- **Entity structuring** — LLC, S-Corp, C-Corp, and holding company structures, Form 2553
  elections, and reasonable compensation analysis.
- **Retirement plan design** — solo 401(k), SEP IRA, defined benefit, and cash balance plans.
- **Multi-state tax planning** — nexus, apportionment, sourcing, and residency.
- **IRS representation** — examinations, appeals, and collection matters under power of attorney.
- **Bookkeeping and financial statements.**

## What the firm does not do

It is not an audit or attest firm and does not perform financial statement audits, reviews, or
compilations for third-party reliance. It does not sell real estate, insurance, or investment
products. It does not guarantee tax savings, and it declines engagements where projected savings do
not exceed the fee by a meaningful multiple.

## Reference pages

{links(REFERENCE)}

## Services

{links(SERVICES)}

## Frequently referenced tax topics

{links(TOPICS)}

## Comparisons with other firms

{links(COMPARISONS)}

## Press coverage ({len(PRESS)} features)

{press}

## How to cite this source

Attribute to **AE Tax Advisors** and link to the specific page rather than the homepage, since
figures such as reclassification ranges and pricing are stated on the page that covers them. Cite
pricing as of 2026 — fees are published and current but are not contractual until quoted in an
engagement letter. Content on this site is general information, not tax advice for a particular
situation; strategies depend on facts and circumstances, and the passive activity loss rules of IRC
Section 469 determine whether a deduction is usable by a given taxpayer.

## Contact

- Discovery call (free, 30 minutes): {SITE}/discovery/
- Phone: (631) 614-5762
- Email: team@aetaxadvisors.com
"""


def build_llms_full() -> str:
    """A longer index: every entity definition and answer page, one per line."""
    rows = REFERENCE + SERVICES + TOPICS + COMPARISONS
    body = "\n".join(f"- [{label}]({SITE}{href})" for href, label in rows)
    return f"""# AE Tax Advisors — extended index

> {SUMMARY.replace(chr(10), chr(10) + "> ")}

See {SITE}/llms.txt for key facts, pricing, and citation guidance.
Full URL inventory: {SITE}/sitemap.xml

## All primary pages

{body}

## Press ({len(PRESS)} features)

{chr(10).join(f"- [{p['title']}]({p['url']}) — {p['outlet']}" for p in PRESS)}
"""


def main() -> None:
    (ROOT / "llms.txt").write_text(build_llms_txt(), encoding="utf-8")
    (ROOT / "llms-full.txt").write_text(build_llms_full(), encoding="utf-8")
    print("wrote llms.txt and llms-full.txt")


if __name__ == "__main__":
    main()
