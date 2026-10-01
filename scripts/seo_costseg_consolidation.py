#!/usr/bin/env python3
"""Consolidate national cost-segregation search intent and internal links."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace(path: str, old: str, new: str, minimum: int = 1) -> int:
    file = ROOT / path
    source = file.read_text()
    count = source.count(old)
    if count < minimum:
        if new in source:
            return 0
        raise RuntimeError(f"Expected at least {minimum} matches in {path}, found {count}: {old[:80]}")
    file.write_text(source.replace(old, new))
    return count


def bulk_navigation() -> None:
    old_nav = '<a href="/cost-segregation-studies-for-real-estate-investors/" class="dropdown-item">Cost Segregation Studies (Detailed)</a>'
    old_nav_short = '<a href="/cost-segregation-studies-for-real-estate-investors/" class="dropdown-item">Cost Segregation Studies</a>'
    new_nav = '<a href="/tax-advisor-for-businesses-under-5-million-profit/" class="dropdown-item">Tax Advisor for Businesses Under $5M</a>'
    old_footer = '<a href="/cost-segregation-studies-for-real-estate-investors/">Cost Segregation Studies</a>'
    new_footer = '<a href="/cost-segregation-study/">Cost Segregation Studies</a>'
    priority_pages = [
        ROOT / "index.html",
        ROOT / "services/index.html",
        ROOT / "cost-segregation-study/index.html",
        ROOT / "cost-segregation-calculator/index.html",
        ROOT / "cost-segregation-study-cost-pricing/index.html",
        ROOT / "cost-segregation-airbnb/index.html",
        ROOT / "blog/cost-segregation-study-cost/index.html",
        ROOT / "blog/cost-segregation-for-airbnb-short-term-rental-properties/index.html",
        ROOT / "tax-advisor-for-businesses-under-5-million-profit/index.html",
    ]
    for file in priority_pages:
        source = file.read_text(errors="ignore")
        updated = source.replace(old_nav, new_nav).replace(old_nav_short, new_nav).replace(old_footer, new_footer)
        updated = updated.replace('href="/cost-segregation-studies-for-real-estate-investors/"', 'href="/cost-segregation-study/"')
        updated = updated.replace('href="/blog/cost-segregation-short-term-rental-airbnb-properties/"', 'href="/blog/cost-segregation-for-airbnb-short-term-rental-properties/"')
        updated = updated.replace('href="/blog/cost-segregation-study-airbnb-property-owners/"', 'href="/blog/cost-segregation-for-airbnb-short-term-rental-properties/"')
        updated = updated.replace('href="/blog/cost-segregation-study-str-properties-guide/"', 'href="/blog/cost-segregation-for-airbnb-short-term-rental-properties/"')
        if updated != source:
            file.write_text(updated)


def update_main_service() -> None:
    path = "cost-segregation-study/index.html"
    replacements = {
        "Cost Segregation Study Services &amp; Pricing | AE Tax Advisors": "Cost Segregation Study Services for Rental Property | AE Tax",
        "Cost segregation studies for rental and commercial property owners. Review pricing, report scope, depreciation implementation and whether deductions are usable.": "Nationwide cost segregation studies for residential rentals, Airbnb and short-term rentals, long-term rentals, and small multifamily. Review pricing, scope, and usable tax benefit.",
        "Cost Segregation Studies for Property Owners": "Cost Segregation Studies for Rental Property Owners",
    }
    for old, new in replacements.items():
        replace(path, old, new)
    replace(
        path,
        "A cost segregation study identifies supported building costs that belong in shorter depreciation categories. The business decision is whether moving those deductions forward produces enough usable tax benefit to justify the study and implementation costs.",
        "A cost segregation study identifies supported building costs that belong in shorter depreciation categories. AE Tax Advisors focuses on residential investment property nationwide, including Airbnb and other short-term rentals, long-term rentals, single-family portfolios, duplexes, and small to mid-sized multifamily. The decision is whether moving those deductions forward produces enough usable tax benefit to justify the study and implementation costs.",
    )
    replace(
        path,
        '<p>Start with a feasibility review if you purchased, constructed or substantially improved income-producing real estate, or if an existing property\'s depreciation schedule has never been evaluated. Common situations include an owner who bought the building used by their business, a landlord adding rental units, and an investor reviewing a commercial portfolio.</p><ul><li><a href="/cost-segregation-airbnb/">Short-term rental and Airbnb owners</a>: coordinate property classification and participation records with the depreciation analysis.</li><li><a href="/cost-segregation-for-multifamily/">Multifamily owners</a>: reconcile each building, unit improvements and shared site costs.</li><li><a href="/cost-segregation-owner-occupied-commercial/">Business owners with commercial buildings</a>: separate the operating business from the property\'s ownership and tax treatment.</li><li><a href="/cost-segregation-for-warehouse/">Warehouse owners</a> and <a href="/cost-segregation-for-medical-office/">medical-office owners</a>: identify the actual use of building systems rather than relying on a generic reclassification percentage.</li></ul>',
        '<p>Start with a feasibility review if you purchased, constructed, or substantially improved income-producing residential real estate, or if an existing rental\'s depreciation schedule has never been evaluated.</p><ul><li><a href="/cost-segregation-airbnb/">Short-term rental and Airbnb owners</a>: coordinate property classification and participation records with the depreciation analysis.</li><li><a href="/rental-property-tax-planning/">Long-term rental owners</a>: evaluate the accelerated deduction together with passive-loss limits and existing rental income.</li><li><a href="/blog/cost-segregation-sfr-buy-and-hold-rentals/">Single-family rental owners</a>: reconcile land, furnishings, improvements, and the placed-in-service date.</li><li><a href="/blog/cost-segregation-duplex-triplex-fourplex/">Duplex, triplex, and fourplex owners</a>: separate shared building systems from unit-level assets and improvements.</li><li><a href="/cost-segregation-for-multifamily/">Small and mid-sized multifamily owners</a>: reconcile each building, unit improvements, and shared site costs.</li></ul>',
    )


def update_calculator() -> None:
    path = "cost-segregation-calculator/index.html"
    replacements = {
        "Cost Segregation Calculator: Test Your Tax Benefit | AE Tax": "Free Cost Segregation Calculator for Rental Property | AE Tax",
        "Estimate additional first-year depreciation and usable federal tax benefit. Adjust land, asset allocation, recovery period, loss usability and study fee.": "Use AE's free cost segregation calculator for residential rentals, Airbnb, STRs, long-term rentals, and small multifamily. Estimate depreciation and usable tax benefit.",
        "Cost Segregation Calculator: Accuracy, Inputs and Tax Savings": "Free Cost Segregation Calculator for Rental Property",
        "Cost segregation calculator: test a first-year scenario": "Estimate Your Cost Segregation Tax Benefit",
    }
    for old, new in replacements.items():
        replace(path, old, new)


def update_pricing_article() -> None:
    path = ROOT / "blog/cost-segregation-study-cost/index.html"
    source = path.read_text()
    old_desc = "Cost segregation study pricing for 2026. Learn typical costs by property type, what affects pricing, and why the ROI makes cost seg one of the best tax investments."
    new_desc = "How much does a cost segregation study cost in 2026? Compare AE's $1 per square foot pricing, $2,000 minimum, scope, implementation fees, and usable value."
    source = source.replace(old_desc, new_desc).replace('"dateModified": "2026-09-06"', '"dateModified": "2026-10-01"')
    body = '''<div class="blog-content fade-in-section" itemprop="articleBody">

<p>A cost segregation study commonly costs a few thousand dollars, but a useful price comparison starts with the work included, not an unsupported industry average. <strong>AE Tax Advisors publishes standard pricing of $1 per square foot with a $2,000 minimum per study.</strong> Complex or specialized work may be quoted separately, and the signed engagement controls the final scope.</p>

<p>The fee is only one part of the decision. Property owners should compare the study cost with the <em>incremental</em> depreciation, whether the resulting deduction can be used now, state conformity, tax-return implementation fees, the expected holding period, and potential depreciation recapture. A large projected deduction is not automatically an immediate tax refund.</p>

<h2>AE Tax Advisors Cost Segregation Pricing</h2>

<table class="blog-table"><thead><tr><th>Property size</th><th>Illustrative standard fee</th></tr></thead><tbody>
<tr><td>1,500 square feet</td><td>$2,000 minimum</td></tr>
<tr><td>2,000 square feet</td><td>$2,000</td></tr>
<tr><td>3,000 square feet</td><td>$3,000</td></tr>
<tr><td>5,000 square feet</td><td>$5,000</td></tr>
</tbody></table>

<p>These examples show the pricing formula only. They do not estimate a deduction or confirm eligibility. AE primarily serves residential investment properties, Airbnb and other short-term rentals, long-term rentals, single-family portfolios, duplexes, and small to mid-sized multifamily. Very large commercial campuses and highly specialized industrial projects are not the firm's core engagement type.</p>

<h2>What Should a Cost Segregation Proposal Include?</h2>

<p>Ask each provider to identify the property, square footage used for billing, tax years, records required, analysis method, report deliverables, review process, and support after delivery. The proposal should also state who is responsible for updating the depreciation schedule and preparing any tax forms.</p>

<ul>
<li><strong>Basis reconciliation:</strong> purchase price, land, closing costs, separately stated personal property, and later improvements should not be counted twice.</li>
<li><strong>Engineering-based classification:</strong> the report should explain the methodology, component costs, recovery periods, and legal support.</li>
<li><strong>Depreciation schedules:</strong> the deliverables should identify the classified assets and year-specific depreciation assumptions.</li>
<li><strong>Implementation responsibility:</strong> a report, a Section 481(a) catch-up calculation, and preparation of Form 3115 are related but distinct services.</li>
<li><strong>State treatment:</strong> states may decouple from federal bonus depreciation or require an addback.</li>
<li><strong>Support terms:</strong> confirm how preparer questions, revisions, and an examination are handled and priced.</li>
</ul>

<h2>Report Fee vs. Tax-Return Implementation Fee</h2>

<p>Do not assume the study fee includes every filing step. A current-year property may require updates to Form 4562 and the fixed-asset schedule. A property placed in service in a prior year may require a separate accounting-method analysis and, when appropriate, Form 3115 with a Section 481(a) adjustment. The engagement should identify the responsible preparer and any separate fee before work begins.</p>

<h2>How to Decide Whether the Study Is Worth the Cost</h2>

<p>Start with depreciable basis after land. Estimate a property-specific range for shorter-life components, apply the correct bonus-depreciation rules for the acquisition and placed-in-service dates, and subtract the depreciation available without the study. Then test whether passive-loss, material-participation, basis, at-risk, or excess-business-loss rules delay the benefit.</p>

<p>For example, if a reviewed projection shows $12,000 of current incremental federal tax benefit and the combined study and implementation cost is $4,000, the initial net cash benefit is $8,000 before state and later-year effects. If the loss is suspended, the immediate benefit can be much smaller even though the deduction remains potentially valuable later.</p>

<p>Use the <a href="/cost-segregation-calculator/">free cost segregation calculator</a> to screen a range, then compare the result with the written proposal and your actual loss limitations.</p>

<h2>How 100% Bonus Depreciation Affects the Analysis</h2>

<p>Current federal law generally permits 100% bonus depreciation for eligible property acquired after January 19, 2025, subject to the statutory requirements and transition rules. Cost segregation can identify qualifying 5-year, 7-year, and 15-year property, but it does not make land or the building shell bonus-eligible. A lookback study must apply the rules and elections for the property's original dates rather than automatically using the current rate.</p>

<h2>Questions to Ask Before Choosing a Provider</h2>

<ul>
<li>What property and square footage does the quote cover?</li>
<li>Who performs and reviews the engineering-based analysis?</li>
<li>How will land, improvements, furnishings, and prior depreciation be reconciled?</li>
<li>Does the fee cover the report only, or tax-return implementation too?</li>
<li>Who answers questions from the return preparer?</li>
<li>What happens if records are incomplete or the property changes before filing?</li>
<li>What support is included if the IRS examines the depreciation classification?</li>
</ul>

<p><em>Updated October 1, 2026. Pricing and examples are general information, not a guarantee of deductions or tax savings. Confirm the written engagement and your tax facts before proceeding.</em></p>

</div>'''
    pattern = r'<div class="blog-content fade-in-section" itemprop="articleBody">.*?</div>\n\n<div class="blog-cta-box fade-in-section">'
    source, count = re.subn(pattern, body + '\n\n<div class="blog-cta-box fade-in-section">', source, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("Could not replace pricing article body")
    source = source.replace(
        "AE Tax Advisors delivers engineering-based cost segregation studies at $1 per square foot, with full audit defense documentation and Form 3115 support included. Find out how much you could save.",
        "AE Tax Advisors provides engineering-based cost segregation studies at $1 per square foot with a $2,000 minimum. Review the written scope, implementation responsibility, and usable benefit before ordering.",
    )
    faq_corrections = {
        "Cost segregation study fees typically range from $3,000 to $25,000, depending on the property type, size, and complexity. Single-family rentals and STRs generally cost $3,000 to $7,000, while large commercial and hospitality properties can cost $10,000 to $25,000. AE Tax Advisors offers cost seg studies at $1 per square foot.": "AE Tax Advisors publishes standard pricing of $1 per square foot with a $2,000 minimum per study. Complex or specialized work may be quoted separately, and the signed engagement controls the property, scope, deliverables, and final fee.",
        "Yes. The fee for a cost segregation study is a fully deductible business expense under IRC Section 162. You can deduct the entire study fee in the year it is paid, which further reduces the net cost of the engagement.": "A study fee may be deductible or capitalized depending on the engagement and the taxpayer's facts. Confirm the treatment and timing with the return preparer instead of assuming the full fee is immediately deductible.",
        "Most property owners see a return of 5:1 to 20:1 on their cost segregation study investment. For example, a $5,000 study on a property worth $500,000 could generate $25,000 to $75,000 or more in accelerated depreciation deductions, translating to significant tax savings in the first year alone.": "There is no reliable universal ROI. Compare the current incremental tax benefit after loss limitations with the study and implementation fees, state treatment, expected holding period, and later recapture. A projected deduction is not automatically current tax savings.",
        "A desktop study uses blueprints, appraisals, photos, and public records to classify building components without a physical inspection. A site-visit study includes an on-site engineering inspection. Desktop studies cost less but are appropriate for smaller or simpler properties. Site-visit studies are recommended for larger or more complex properties and provide stronger audit defense.": "A remote study relies on available plans, closing records, invoices, photographs, and other property evidence. A site visit adds direct physical observation. The appropriate method depends on the property, records, complexity, and documented scope rather than a universal value threshold.",
        "The One Big Beautiful Bill Act (OBBBA) made 100% bonus depreciation permanent, which dramatically increases the value of cost segregation studies. While the OBBBA does not directly change study fees, the permanent availability of full first-year bonus depreciation under IRC Section 168(k) means every dollar reclassified through cost seg now delivers its maximum tax benefit immediately, making the ROI even stronger.": "The law generally permits 100% bonus depreciation for eligible property acquired after January 19, 2025, subject to statutory requirements and transition rules. It does not change the study fee, make every reclassified asset eligible, or determine whether the resulting deduction is currently usable.",
        "Be cautious of firms offering cost segregation studies for unusually low fees, such as under $1,500 for a standard property. Low-cost providers may use automated software without proper engineering analysis, skip required asset classifications, or produce reports that will not hold up to IRS scrutiny. A quality study should include detailed engineering-based analysis, proper IRC Section 1245 and 1250 asset classifications, and a complete depreciation schedule.": "Price alone does not establish quality. Red flags include an undefined property or scope, no basis reconciliation, unsupported reclassification percentages, guaranteed tax savings, unclear engineering review, and no written assignment of tax-return implementation responsibilities.",
    }
    for old, new in faq_corrections.items():
        source = source.replace(old, new)
    path.write_text(source)


def update_str_pillar() -> None:
    path = "blog/cost-segregation-for-airbnb-short-term-rental-properties/index.html"
    file = ROOT / path
    source = file.read_text()
    source = source.replace("Airbnb and Short-Term Rental Cost Segregation Guide (2026) Properties?", "Airbnb and Short-Term Rental Cost Segregation Guide")
    source = source.replace("How Does Cost Segregation Work for Airbnb and Short-Term Rental Properties?", "Airbnb and Short-Term Rental Cost Segregation Guide")
    source = source.replace("How Does Cost Segregation Work for Airbnb and Short-Term Rental", "Airbnb and Short-Term Rental Cost Segregation Guide (2026)")
    source = source.replace("Learn how cost segregation applies to Airbnb and short-term rentals, including the STR loophole that lets you offset W-2 income with rental depreciation.", "Learn how cost segregation works for Airbnb and short-term rentals, including basis, 27.5 vs. 39-year recovery, material participation, bonus depreciation, and loss limits.")
    file.write_text(source)


def clean_sitemaps() -> None:
    redirected = {
        "/cost-segregation-studies-for-real-estate-investors/",
        "/blog/cost-segregation-short-term-rental-airbnb-properties/",
        "/blog/cost-segregation-study-airbnb-property-owners/",
        "/blog/cost-segregation-study-str-properties-guide/",
    }
    for file in ROOT.glob("sitemap*.xml"):
        source = file.read_text()
        for route in redirected:
            block = r"\s*<url>(?:(?!</?url>).)*?<loc>https://www\.aetaxadvisors\.com" + re.escape(route) + r"</loc>(?:(?!</?url>).)*?</url>"
            source = re.sub(block, "", source, flags=re.S)
        file.write_text(source)


def main() -> None:
    bulk_navigation()
    update_main_service()
    update_calculator()
    update_pricing_article()
    update_str_pillar()
    clean_sitemaps()
    print("Cost segregation SEO consolidation complete")


if __name__ == "__main__":
    main()
