#!/usr/bin/env python3
"""Build nationwide cost segregation coverage without thin city doorway pages."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.aetaxadvisors.com"
UPDATED = "September 23, 2026"

MISSING_STATES = {
    "alabama": ("Alabama", "AL", ["Birmingham", "Huntsville", "Mobile", "Montgomery", "Gulf Shores and Orange Beach"], "single-family rentals and small multifamily in Birmingham and Huntsville, plus furnished coastal vacation rentals around Gulf Shores and Orange Beach"),
    "alaska": ("Alaska", "AK", ["Anchorage", "Fairbanks", "Juneau", "Wasilla", "the Kenai Peninsula"], "residential rentals in Anchorage and Fairbanks, seasonal furnished rentals, lodges, and vacation properties across the Kenai Peninsula and Southeast Alaska"),
    "arkansas": ("Arkansas", "AR", ["Little Rock", "Fayetteville", "Bentonville", "Hot Springs", "Jonesboro"], "long-term rentals in central Arkansas and Northwest Arkansas, together with furnished rentals in Hot Springs and the Ozarks"),
    "delaware": ("Delaware", "DE", ["Wilmington", "Newark", "Dover", "Rehoboth Beach", "Bethany Beach"], "long-term residential rentals in northern Delaware and short-term vacation rentals along the Delaware beaches"),
    "idaho": ("Idaho", "ID", ["Boise", "Coeur d'Alene", "Idaho Falls", "Sun Valley", "McCall"], "Boise-area residential rentals, Coeur d'Alene vacation properties, and furnished mountain-market rentals in Sun Valley and McCall"),
    "iowa": ("Iowa", "IA", ["Des Moines", "Cedar Rapids", "Davenport", "Iowa City", "Ames"], "single-family rentals, duplexes, small apartment properties, and student housing in Iowa's major employment and university markets"),
    "kansas": ("Kansas", "KS", ["Wichita", "Overland Park", "Kansas City", "Lawrence", "Topeka"], "long-term rentals and small multifamily properties in Wichita and the Kansas City suburbs, plus student housing in Lawrence"),
    "louisiana": ("Louisiana", "LA", ["New Orleans", "Baton Rouge", "Lafayette", "Shreveport", "Lake Charles"], "historic residential rentals, furnished urban rentals, small multifamily, and investor-owned housing across southern Louisiana"),
    "maine": ("Maine", "ME", ["Portland", "Bangor", "Lewiston", "Bar Harbor", "Kennebunkport"], "long-term residential rentals around Portland and Bangor and seasonal coastal or lake vacation rentals throughout southern and Downeast Maine"),
    "mississippi": ("Mississippi", "MS", ["Jackson", "Gulfport", "Biloxi", "Hattiesburg", "Oxford"], "residential rentals and small multifamily, Gulf Coast vacation properties, and student rentals in Oxford and Hattiesburg"),
    "montana": ("Montana", "MT", ["Billings", "Bozeman", "Missoula", "Kalispell", "Whitefish"], "long-term rentals in Billings and Missoula, rapidly growing housing markets in Bozeman and Kalispell, and furnished vacation properties around Whitefish"),
    "nebraska": ("Nebraska", "NE", ["Omaha", "Lincoln", "Bellevue", "Grand Island", "Kearney"], "single-family rentals, small multifamily, and student housing concentrated in Omaha, Lincoln, and the state's regional employment centers"),
    "new-hampshire": ("New Hampshire", "NH", ["Manchester", "Nashua", "Concord", "Portsmouth", "the Lakes Region"], "residential rentals in southern New Hampshire and short-term vacation rentals in the Lakes Region, White Mountains, and Seacoast"),
    "new-mexico": ("New Mexico", "NM", ["Albuquerque", "Santa Fe", "Las Cruces", "Taos", "Ruidoso"], "long-term rentals in Albuquerque and Las Cruces, plus furnished tourism properties in Santa Fe, Taos, and Ruidoso"),
    "north-dakota": ("North Dakota", "ND", ["Fargo", "Bismarck", "Grand Forks", "Minot", "Williston"], "long-term rentals, workforce housing, small multifamily, and furnished units serving the state's university, energy, and healthcare markets"),
    "oklahoma": ("Oklahoma", "OK", ["Oklahoma City", "Tulsa", "Norman", "Broken Bow", "Stillwater"], "long-term rentals in Oklahoma City and Tulsa, student housing in Norman and Stillwater, and cabin-based short-term rentals around Broken Bow"),
    "south-dakota": ("South Dakota", "SD", ["Sioux Falls", "Rapid City", "Aberdeen", "Brookings", "the Black Hills"], "residential rentals in Sioux Falls and Rapid City, student housing, and seasonal short-term rentals throughout the Black Hills"),
    "vermont": ("Vermont", "VT", ["Burlington", "Montpelier", "Rutland", "Stowe", "Killington"], "long-term rentals in Burlington and central Vermont, together with ski, mountain, and four-season vacation properties"),
    "west-virginia": ("West Virginia", "WV", ["Charleston", "Morgantown", "Huntington", "Wheeling", "the New River Gorge"], "long-term rentals and student housing, plus furnished outdoor-recreation properties near the New River Gorge and mountain destinations"),
    "wyoming": ("Wyoming", "WY", ["Cheyenne", "Casper", "Laramie", "Jackson", "Cody"], "long-term rentals and workforce housing in Cheyenne and Casper, student housing in Laramie, and furnished tourism properties around Jackson and Cody"),
}

ALL_STATES = [
    ("Alabama", "alabama"), ("Alaska", "alaska"), ("Arizona", "arizona"), ("Arkansas", "arkansas"),
    ("California", "california"), ("Colorado", "colorado"), ("Connecticut", "connecticut"), ("Delaware", "delaware"),
    ("Florida", "florida"), ("Georgia", "georgia"), ("Hawaii", "hawaii"), ("Idaho", "idaho"),
    ("Illinois", "illinois"), ("Indiana", "indiana"), ("Iowa", "iowa"), ("Kansas", "kansas"),
    ("Kentucky", "kentucky"), ("Louisiana", "louisiana"), ("Maine", "maine"), ("Maryland", "maryland"),
    ("Massachusetts", "massachusetts"), ("Michigan", "michigan"), ("Minnesota", "minnesota"), ("Mississippi", "mississippi"),
    ("Missouri", "missouri"), ("Montana", "montana"), ("Nebraska", "nebraska"), ("Nevada", "nevada"),
    ("New Hampshire", "new-hampshire"), ("New Jersey", "new-jersey"), ("New Mexico", "new-mexico"), ("New York", "new-york"),
    ("North Carolina", "north-carolina"), ("North Dakota", "north-dakota"), ("Ohio", "ohio"), ("Oklahoma", "oklahoma"),
    ("Oregon", "oregon"), ("Pennsylvania", "pennsylvania"), ("Rhode Island", "rhode-island"), ("South Carolina", "south-carolina"),
    ("South Dakota", "south-dakota"), ("Tennessee", "tennessee"), ("Texas", "texas"), ("Utah", "utah"),
    ("Vermont", "vermont"), ("Virginia", "virginia"), ("Washington", "washington"), ("West Virginia", "west-virginia"),
    ("Wisconsin", "wisconsin"), ("Wyoming", "wyoming"),
]


def chrome() -> tuple[str, str]:
    source = (ROOT / "blog/cost-segregation-complete-guide/index.html").read_text()
    header = re.search(r"( *<header>.*?</header>)", source, re.S).group(1)
    footer = re.search(r"( *<footer>.*</html>)", source, re.S).group(1)
    return header, footer


def state_page(slug: str, data: tuple[str, str, list[str], str], header: str, footer: str) -> str:
    name, abbr, markets, profile = data
    url = f"{SITE}/{slug}/"
    market_list = "".join(f"<li><strong>{html.escape(market)}</strong></li>" for market in markets)
    service_schema = {
        "@context": "https://schema.org", "@type": "Service",
        "name": f"Cost Segregation Studies in {name}", "serviceType": "Cost Segregation Study",
        "provider": {"@type": "Organization", "name": "AE Tax Advisors", "url": f"{SITE}/"},
        "areaServed": {"@type": "State", "name": name}, "url": url,
        "audience": {"@type": "Audience", "audienceType": "Residential real estate investors"},
    }
    faq = [
        (f"Do you provide cost segregation studies throughout {name}?", f"Yes. AE Tax Advisors serves residential real estate investors throughout {name}, including {', '.join(markets[:-1])}, and {markets[-1]}. The engagement is coordinated remotely, with property records, photographs, plans, and site information collected securely."),
        (f"What {name} properties are the best fit?", "The best fit is generally an income-producing residential property with enough depreciable basis to justify the study, including short-term rentals, long-term rentals, single-family rental portfolios, duplexes, small multifamily properties, and furnished rentals."),
        ("Can a prior-year property still qualify?", "Often, yes. A lookback study may support a Form 3115 accounting-method change and a Section 481(a) catch-up adjustment. The placed-in-service date, prior depreciation, ownership continuity, and current facts must be reviewed before filing."),
        ("Does a cost segregation deduction automatically offset W-2 income?", "No. The study determines depreciation classification. Whether the resulting loss is currently usable depends on basis, at-risk rules, passive activity rules, material participation, the short-term rental rules, and other limitations."),
        ("Do you handle very large commercial buildings?", "AE Tax Advisors focuses on residential investment property, short-term rentals, long-term rentals, single-family portfolios, and small to mid-sized multifamily. Very large commercial campuses and highly specialized industrial projects are not our core engagement type."),
    ]
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq
    ]}
    faq_html = "".join(f'<div class="faq-item"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></div>' for q, a in faq)
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cost Segregation in {name} for Rentals and STRs | AE Tax</title>
<meta name="description" content="Cost segregation studies in {name} for short-term rentals, long-term rentals, residential portfolios, and small multifamily. Audit-ready engineering reports nationwide.">
<link rel="canonical" href="{url}"><meta name="geo.region" content="US-{abbr}"><meta name="geo.placename" content="{name}">
<meta property="og:title" content="Cost Segregation in {name} for Rentals and STRs"><meta property="og:description" content="Engineering-based cost segregation studies for residential investment property across {name}."><meta property="og:url" content="{url}"><meta property="og:type" content="website"><meta property="og:site_name" content="AE Tax Advisors">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg"><link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{json.dumps(service_schema)}</script>
<script type="application/ld+json">{json.dumps(faq_schema)}</script>
</head><body>{header}
<main>
<section class="page-header"><div class="container"><div class="breadcrumbs"><a href="/">Home</a> &raquo; <a href="/locations/">Cost Segregation by State</a> &raquo; {name}</div><h1>Cost Segregation Studies in {name}</h1><p class="post-meta">Residential rentals, short-term rentals, long-term rentals, and small multifamily | Updated {UPDATED}</p></div></section>
<section class="content-section fade-in-section"><div class="container narrow">
<p class="lead-text">AE Tax Advisors provides engineering-based cost segregation studies for residential real estate investors across {name}. Our core work includes short-term rentals, long-term rentals, single-family portfolios, duplexes, small multifamily, and furnished rental properties.</p>
<p>In {name}, the most common opportunities are {html.escape(profile)}. The federal classification rules are consistent nationwide, but state depreciation conformity and the owner's ability to use the deduction must be modeled separately.</p>
<div style="background:var(--light-bg);padding:28px;border-radius:12px;margin:28px 0"><h2 style="margin-top:0">Our Engagement Fit</h2><p><strong>Best fit:</strong> residential investment property, Airbnb and VRBO properties, long-term rentals, SFR portfolios, duplexes, small to mid-sized multifamily, and qualifying renovations.</p><p><strong>Not our core fit:</strong> very large commercial campuses, institutional industrial facilities, and unusually specialized mega-projects.</p></div>
<h2>{name} Markets We Serve</h2><p>We work remotely with owners, preparers, and property managers throughout the state. Major markets include:</p><ul>{market_list}</ul>
<p>A property's city does not change the federal MACRS classification rules. Location still matters because local property mix, land allocation, construction type, site improvements, furnishing levels, and state conformity can change the economics of the study.</p>
<h2>Property Types We Study in {name}</h2>
<h3>Short-Term Rentals and Vacation Rentals</h3><p>Furnished rentals can contain substantial 5-year personal property and 15-year land improvements. Furniture, appliances, removable finishes, certain dedicated electrical components, driveways, fencing, patios, pools, exterior lighting, and landscaping must be evaluated component by component. The study does not itself make a tax loss nonpassive. Average stay, services, and material participation remain separate tax questions.</p>
<h3>Long-Term Residential Rentals</h3><p>Single-family rentals, duplexes, and small apartment properties generally begin with a 27.5-year residential recovery period for the building. A study identifies assets that properly belong in shorter MACRS classes. The benefit should be compared with the owner's expected hold period, passive-loss position, and eventual recapture.</p>
<h3>Residential Portfolios and Small Multifamily</h3><p>Owners with several similar properties may gain efficiency by coordinating documentation and timing across the portfolio. Repeated unit layouts, appliances, flooring, site work, and exterior improvements can create meaningful reclassification while still requiring property-level schedules that tie to each tax return.</p>
<h2>How a Study Works</h2><ol><li><strong>Eligibility review.</strong> Confirm ownership, placed-in-service date, depreciable basis, land allocation, and prior depreciation.</li><li><strong>Document collection.</strong> Gather the closing statement, depreciation schedule, property records, plans when available, renovation invoices, and current photographs.</li><li><strong>Engineering analysis.</strong> Identify and cost building components using property facts, construction data, and recognized estimating methods.</li><li><strong>Tax classification.</strong> Assign supported 5-year, 7-year, 15-year, 27.5-year, or 39-year treatment and document the authority.</li><li><strong>Return coordination.</strong> Provide schedules for Form 4562 or, where appropriate, coordinate a Form 3115 lookback with the tax preparer.</li></ol>
<h2>Current Federal Bonus Depreciation Rule</h2><p>The current 100% additional first-year depreciation rule generally applies to qualified property acquired and placed in service after January 19, 2025. It did not retroactively convert 2023 and 2024 property to 100%. Prior-year property may still produce a current catch-up deduction through correct depreciation and Form 3115, but the applicable bonus percentage depends on the acquisition and placed-in-service facts. See the <a href="https://www.irs.gov/newsroom/treasury-irs-issue-guidance-on-the-additional-first-year-depreciation-deduction-amended-as-part-of-the-one-big-beautiful-bill">IRS guidance</a>.</p>
<h2>What Makes a Study Defensible</h2><p>The IRS Cost Segregation Audit Technique Guide describes the detailed engineering approach as the most methodical and accurate approach. A defensible report should identify the property, reconcile to depreciable basis, explain the methodology, provide component-level classifications, document assumptions, and give the tax preparer usable schedules. Review the <a href="https://www.irs.gov/businesses/small-businesses-self-employed/audit-techniques-guides-atgs">IRS Cost Segregation Audit Technique Guide</a>.</p>
<h2>Pricing and Next Step</h2><p>AE Tax Advisors prices cost segregation studies at $1 per square foot with a $2,000 minimum. Scope can change for unusual properties or incomplete records. Before starting, we review whether the likely timing benefit justifies the fee and whether the owner appears able to use the deduction.</p>
<p><a href="/discovery/" class="btn-cta">Request a Cost Segregation Review</a></p>
</div></section>
<section class="content-section fade-in-section" id="faq"><div class="container narrow"><h2>Cost Segregation in {name}: Frequently Asked Questions</h2>{faq_html}</div></section>
<section class="content-section fade-in-section"><div class="container narrow"><h2>Related Cost Segregation Resources</h2><ul class="related-links"><li><a href="/cost-segregation-study/">Complete Cost Segregation Study Guide</a></li><li><a href="/cost-segregation-airbnb/">Cost Segregation for Airbnb and Short-Term Rentals</a></li><li><a href="/blog/cost-segregation-basics-rental-properties/">Cost Segregation for Residential Rental Property</a></li><li><a href="/cost-segregation-calculator/">Cost Segregation Calculator</a></li><li><a href="/locations/">Cost Segregation by State</a></li></ul></div></section>
</main>{footer}'''


def update_hub() -> None:
    path = ROOT / "locations/index.html"
    text = path.read_text()
    text = re.sub(r"<title>.*?</title>", "<title>Cost Segregation by State: All 50 States | AE Tax Advisors</title>", text, count=1)
    text = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Cost segregation services in all 50 states for short-term rentals, long-term rentals, residential portfolios, and small multifamily properties.">', text, count=1)
    text = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="Cost Segregation Services in All 50 States">', text, count=1)
    text = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="Nationwide cost segregation for short-term rentals, long-term rentals, residential portfolios, and small multifamily properties.">', text, count=1)
    text = text.replace("<h1>State Tax Guides for Real Estate Investors</h1>", "<h1>Cost Segregation Services in All 50 States</h1>")
    text = text.replace("Rates, pass-through entity tax rules, and depreciation conformity, state by state", "Residential rentals, short-term rentals, long-term rentals, and small multifamily nationwide")
    start = text.index('        <div class="blog-index-grid">')
    end = text.index("        </div>\n    </div></section>", start) + len("        </div>")
    cards = ['        <div class="blog-index-grid">']
    for name, slug in ALL_STATES:
        cards.append(f'''            <a href="/{slug}/" class="blog-index-card"><h3>Cost Segregation in {name}</h3><p>Residential rentals, STRs, LTRs, portfolios, and small multifamily.</p><span class="card-link">Read the {name} guide &rarr;</span></a>''')
    cards.append("        </div>")
    text = text[:start] + "\n".join(cards) + text[end:]
    text = text.replace("Not Seeing Your State?", "Own Property in More Than One State?")
    text = text.replace("We work with clients in all fifty states. Book a call and we will walk through your state's rules and your specific situation together.", "We work nationwide and can coordinate a portfolio review across multiple states. We model federal treatment, state conformity, deduction usability, and filing logistics before the studies are finalized.")
    path.write_text(text)


def correct_bonus_errors() -> None:
    replacements = {
        "cost-segregation-study/index.html": [
            ("The OBBBA's restoration of 100% bonus depreciation applies retroactively to property placed in service after December 31, 2022. This means that investors who placed properties in service during 2023, 2024, or 2025 and claimed reduced bonus depreciation (80%, 60%, or 40%) may be entitled to file amended returns or Form 3115 to claim the additional depreciation they missed. Our <a href=\"/blog/\">blog</a> covers the latest updates on how to take advantage of these retroactive provisions.", "The restored 100% rate generally applies to qualified property acquired and placed in service after January 19, 2025. It did not retroactively increase the 2023 or 2024 bonus percentages. A prior-year property may still qualify for a lookback cost segregation study and a Form 3115 catch-up adjustment, but the applicable bonus rate depends on the acquisition and placed-in-service facts. See the <a href=\"https://www.irs.gov/newsroom/treasury-irs-issue-guidance-on-the-additional-first-year-depreciation-deduction-amended-as-part-of-the-one-big-beautiful-bill\">IRS guidance on the effective date</a>."),
        ],
        "blog/bonus-depreciation-obbba-real-estate-changes/index.html": [
            ("One of the most overlooked aspects of the OBBBA restoration is its retroactive reach. Investors who placed property in service during the phasedown years (2023 through 2025) and only claimed the reduced bonus depreciation percentages can now recover the difference.", "The effective date is critical. The restored 100% rate generally applies to qualified property acquired and placed in service after January 19, 2025. It does not retroactively increase the bonus percentage for property acquired and placed in service in 2023 or 2024. Prior-year property can still benefit from a lookback study, but the catch-up calculation must use the bonus rate that actually applied to that property."),
        ],
        "blog/bonus-depreciation-obbba-permanent-100-percent/index.html": [
            ("One of the most consequential features of the OBBBA is its retroactive application. The Act applies the restored 100% rate to property placed in service during the phasedown years, meaning investors who claimed only 80% bonus depreciation in 2023 or 60% in 2024 are now entitled to the full 100% deduction for those years. Consider an investor who completed a cost segregation study on a property acquired in 2023 and reclassified $500,000 of components into five-year and fifteen-year recovery periods. At the 80% bonus rate, only $400,000 was deducted in the first year. Under the OBBBA retroactive provision, that investor can now claim the additional $100,000 through an amended return (Form 1040-X or 1120-X) or through a change in accounting method under IRC Section 481(a).", "The restored 100% rate is not retroactive to property acquired and placed in service in 2023 or 2024. It generally applies to qualified property acquired and placed in service after January 19, 2025. Investors can still conduct a lookback cost segregation study on older property and may claim a Form 3115 catch-up adjustment, but the calculation must use the bonus percentage that applied when the property was acquired and placed in service."),
        ],
        "blog/what-is-bonus-depreciation-and-how-does-it-affect-rental-property/index.html": [
            ("However, the One Big Beautiful Bill Act (OBBBA), signed into law in 2025, restored 100% bonus depreciation retroactively and made it permanent. This eliminates the phase-down schedule and ensures that qualifying assets can be fully expensed in the year placed in service for the foreseeable future.", "However, the One Big Beautiful Bill Act (OBBBA), signed into law in 2025, restored 100% bonus depreciation permanently for qualified property acquired and placed in service after January 19, 2025. It did not retroactively increase the bonus rate for 2023 or 2024 property."),
        ],
        "bonus-depreciation-rental-property/index.html": [
            ("The One Big Beautiful Bill Act restored 100% first-year bonus depreciation with no phasedown and no sunset date. Property placed in service in 2026 and every year going forward qualifies for the full deduction. This applies retroactively to property placed in service after December 31, 2022, meaning investors who took reduced bonus during the 2023, 2024, and 2025 phasedown years may be able to recover the difference.", "The One Big Beautiful Bill Act restored 100% first-year bonus depreciation with no scheduled phasedown or sunset. The restored rate generally applies to qualified property acquired and placed in service after January 19, 2025. It does not retroactively increase the bonus percentage for property acquired and placed in service in 2023 or 2024."),
        ],
        "blog/obbba-tax-planning-checklist-business-owners-2026/index.html": [
            ("The OBBBA permanently restored 100% bonus depreciation under IRC Section 168(k) and applied it retroactively to property placed in service during the phasedown years of 2023, 2024, and 2025.", "The OBBBA permanently restored 100% bonus depreciation under IRC Section 168(k) for qualified property generally acquired and placed in service after January 19, 2025. It did not retroactively increase the bonus rate for property acquired and placed in service in 2023 or 2024."),
        ],
    }
    for rel, pairs in replacements.items():
        path = ROOT / rel
        text = path.read_text()
        for old, new in pairs:
            if old not in text:
                if new in text:
                    continue
                raise RuntimeError(f"Expected bonus text not found in {rel}")
            text = text.replace(old, new)
        path.write_text(text)


def consolidate_canonicals() -> None:
    targets = {
        "what-is-a-cost-segregation-study/index.html": "/cost-segregation-study/",
        "what-is-cost-segregation/index.html": "/cost-segregation-study/",
        "cost-segregation-explained/index.html": "/cost-segregation-study/",
        "services/cost-segregation/index.html": "/cost-segregation-study/",
        "services/cost-segregation-airbnb/index.html": "/cost-segregation-airbnb/",
    }
    for rel, destination in targets.items():
        path = ROOT / rel
        text = path.read_text()
        text = re.sub(r'<link rel="canonical" href="[^"]+">', f'<link rel="canonical" href="{SITE}{destination}">', text, count=1)
        path.write_text(text)


def enhance_pillar() -> None:
    path = ROOT / "cost-segregation-study/index.html"
    text = path.read_text()
    if "id=\"nationwide-cost-segregation\"" in text:
        return
    links = " ".join(f'<a href="/{slug}/">{name}</a>' for name, slug in ALL_STATES)
    section = f'''
    <section class="content-section fade-in-section" id="nationwide-cost-segregation"><div class="container narrow">
        <h2>Cost Segregation Services Across All 50 States</h2>
        <p>AE Tax Advisors serves residential real estate investors nationwide. Our core cost segregation work covers short-term rentals, Airbnb and VRBO properties, long-term residential rentals, single-family rental portfolios, duplexes, small multifamily, and qualifying renovation projects. Very large commercial campuses and highly specialized industrial projects are not our primary engagement type.</p>
        <p>Federal MACRS classification rules apply nationwide. State treatment still matters because states differ in bonus-depreciation conformity, addbacks, recovery schedules, and entity-level tax rules. Each state guide identifies the markets we serve and the state issues that should be modeled before the deduction is filed.</p>
        <p class="state-link-list">{links}</p>
        <p><a href="/locations/" class="btn-secondary">View the Nationwide Cost Segregation Directory</a></p>
    </div></section>
'''
    marker = "    <!-- Section 10: Common Misconceptions -->"
    if marker not in text:
        raise RuntimeError("Pillar insertion marker not found")
    path.write_text(text.replace(marker, section + "\n" + marker, 1))


def main() -> None:
    header, footer = chrome()
    for slug, data in MISSING_STATES.items():
        out = ROOT / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(state_page(slug, data, header, footer))
    update_hub()
    correct_bonus_errors()
    consolidate_canonicals()
    enhance_pillar()
    print(f"Built {len(MISSING_STATES)} state pages, upgraded the 50-state hub, consolidated duplicate intent, and corrected bonus timing.")


if __name__ == "__main__":
    main()
