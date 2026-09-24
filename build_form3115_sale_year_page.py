#!/usr/bin/env python3
"""Build the buyer-intent guide for sale-year rental depreciation corrections."""

from __future__ import annotations

import re
from pathlib import Path

from site_template import (
    SITE,
    article_schema,
    breadcrumb_schema,
    build_page,
    definition,
    page_header,
    related_section,
    section,
    takeaways,
    write_page,
)

ROOT = Path(__file__).resolve().parent
DATE = "2026-09-23"
PATH = "/form-3115-year-of-sale-rental-property/"


def build() -> str:
    title = "Form 3115 in the Year You Sell a Rental | AE Tax"
    description = (
        "Can you file Form 3115 in the year you sell a rental? Review the "
        "disposed-property rules, allowed-or-allowable risk, timing, and records."
    )
    body = [
        page_header(
            h1="Can I File Form 3115 in the Year I Sell a Rental Property?",
            subtitle=description,
            trail=[
                ("Home", "/"),
                ("Amended Business Returns", "/amended-business-tax-return-services/"),
                ("Form 3115 in a Rental Sale Year", PATH),
            ],
            cta="Book a Sale-Year Depreciation Review",
        ),
        section(
            "The short answer",
            definition(
                "Often, yes—but not simply because the property was sold. Revenue Procedure "
                "2025-23 includes an automatic accounting-method change for certain disposed "
                "depreciable property when the taxpayer used an impermissible depreciation "
                "method and claimed less depreciation than was allowable. The sale-year return "
                "must coordinate Form 3115, the Section 481(a) adjustment, adjusted basis, the "
                "sale calculation, passive-loss treatment, and any state differences. A 1031 "
                "exchange, election problem, one-year error, excess depreciation, or sale in an "
                "earlier year can require a different analysis."
            ),
        ),
        takeaways(
            [
                "The IRS has a disposed-property procedure specifically addressing certain missed depreciation in the year of sale.",
                "Allowed-or-allowable depreciation can reduce basis even when the deduction was never claimed.",
                "Form 3115 is not the universal fix: the error pattern, disposition type, ownership, and filing timing control the remedy.",
                "The depreciation correction and sale workpapers must use the same asset history and adjusted basis.",
            ]
        ),
        section(
            "When the disposed-property procedure may fit",
            """
<p>Section 6.07 of <a href="https://www.irs.gov/irb/2025-24_IRB#REV-PROC-2025-23">Revenue Procedure 2025-23</a> addresses a change from an impermissible to a permissible depreciation method for property disposed of during the year of change. The procedure generally targets property for which the taxpayer claimed no depreciation, or claimed less than the depreciation allowable, in the sale year or an earlier year.</p>
<p>A common fact pattern is a rental placed in service several years ago with no building depreciation, an incorrect recovery period, or a depreciable basis that was understated under a consistently used method. If the repeated treatment created an accounting method and the property is sold in the current year, the disposed-property change may allow the omitted pre-sale depreciation to be measured through a Section 481(a) adjustment on the current return.</p>
<p>That conclusion requires more than comparing the purchase price with the depreciation schedule. The preparer must establish the correct placed-in-service date, land allocation, building and improvement basis, prior methods, depreciation actually claimed, allowable depreciation, disposition date, and whether the transaction is taxable or subject to a nonrecognition rule.</p>
""",
        ),
        section(
            "Why fixing the error before reporting the sale matters",
            """
<p>The IRS explains that the greater of depreciation allowed or allowable generally must be considered at disposition. That means an owner can lose basis for depreciation that should have been claimed even if the deduction never appeared on a prior return. Leaving the old schedule untouched can therefore produce a double economic cost: the owner missed the annual deductions and still reports the sale using basis reduced for allowable depreciation.</p>
<p>A sale-year correction should rebuild one continuous asset ledger. The same schedule should support the Section 481(a) adjustment, current-year depreciation through the disposition date under the applicable convention, adjusted basis, Form 4797 or other sale reporting, Section 1245 or Section 1250 character, and any unrecaptured Section 1250 gain. Treating Form 3115 and the sale as separate projects is how basis and recapture inconsistencies arise.</p>
<p>Suspended passive losses also require a separate review. A fully taxable disposition of the taxpayer's entire interest can affect when passive losses are released, but a related-party transfer, installment sale, partial sale, or like-kind exchange can change the result. The depreciation correction should not assume that every sale automatically frees every carryforward.</p>
""",
        ),
        section(
            "When Form 3115 may not be the right correction",
            """
<p>The disposed-property change is not a shortcut for every rental error. Revenue Procedure 2025-23 excludes or separately treats several situations. A different route may be required when:</p>
<ul>
<li>The property was sold in a prior tax year rather than during the requested year of change.</li>
<li>The disposition is part of a Section 1031 exchange or another nonrecognition transaction, unless a stated exception and election applies.</li>
<li>The taxpayer is trying to make or revoke a depreciation election rather than correct an accounting method.</li>
<li>The problem is a mathematical or posting error, an incorrect placed-in-service date, or another item that is not treated as a method change.</li>
<li>The taxpayer has not used the treatment long enough to adopt an accounting method and an amended return remains the permitted correction.</li>
<li>The property was over-depreciated, the proposed method is not permissible, or other automatic-change eligibility limits apply.</li>
</ul>
<p>The filing form follows the technical classification of the error. It should not be chosen only because Form 3115 produces a current-year adjustment or because older refund years are closed.</p>
""",
        ),
        section(
            "Example: rental sold after six years of missed depreciation",
            """
<p>Assume an investor bought a rental for $620,000, properly assigned $120,000 to land, and placed the $500,000 building in service six years before selling it. The filed returns consistently omitted building depreciation. Before the sale-year return is prepared, the tax team verifies that the repeated omission is an impermissible depreciation method, reconstructs the depreciation allowable through the beginning of the year of change, and computes the current-year amount through disposition.</p>
<p>The analysis does not stop at the catch-up number. The team reconciles the negative Section 481(a) adjustment with the basis reduction used in the sale schedule, reviews the character of building and separately stated asset gain, and traces any passive-loss carryforward. If the closing was structured as a 1031 exchange, if the basis allocation itself was wrong, or if prior returns contain inconsistent depreciation rather than a repeated method, the workflow changes.</p>
<p>This example is intentionally not a tax-savings promise. Whether the adjustment produces a usable current deduction depends on the taxpayer, activity, transaction, limitations, and complete return.</p>
""",
        ),
        section(
            "Sale-year filing timing and duplicate-copy requirement",
            """
<p>For an automatic change request, the IRS currently instructs taxpayers to attach the original Form 3115 to a timely filed federal income tax return, including extensions, for the year of change. A signed duplicate is also filed under the current automatic-change delivery procedure no later than the date the original is filed with the return. The current <a href="https://www.irs.gov/filing/where-to-file-form-3115">IRS Form 3115 filing page</a> should be checked before delivery because addresses and temporary procedures can change.</p>
<p>Waiting until after the sale-year return has been filed can materially narrow the procedural options. An extension creates preparation time; it does not fix an ineligible change or replace the requirement for a timely, complete filing. The study, depreciation reconstruction, return, and duplicate-copy process should be scheduled backward from the extended due date.</p>
""",
        ),
        section(
            "Documents AE reviews before recommending the filing",
            """
<ul>
<li>Purchase closing statement, settlement allocation, and evidence supporting land value</li>
<li>Placed-in-service date and the first rental listing, lease, or availability records</li>
<li>Every federal and state depreciation schedule from acquisition through sale</li>
<li>Prior returns, including Schedule E, Form 4562, passive-loss forms, and carryforwards</li>
<li>Capital improvements, casualty adjustments, partial dispositions, and prior cost-segregation reports</li>
<li>Sale closing statement, contract, installment terms, and any related-party facts</li>
<li>1031 exchange documents or qualified-intermediary records, if applicable</li>
<li>A year-by-year bridge from depreciation claimed to depreciation allowable</li>
</ul>
<p>The deliverable should show the correction procedure, Section 481(a) computation, current depreciation, adjusted basis, sale reporting, passive-loss effect, and state follow-up in one reconciled file.</p>
""",
        ),
        section(
            "Get the correction reviewed before the sale-year return is filed",
            """
<p>A sale can expose a depreciation error that has been accumulating for years. AE Tax Advisors can review whether the disposed-property automatic change applies, reconstruct the asset history, and coordinate the correction with the sale return.</p>
<p><a href="/discovery/" class="btn-cta">Book a Sale-Year Depreciation Review</a></p>
""",
        ),
        section(
            "Primary sources and editorial review",
            """
<p>This guide was prepared under the <a href="/editorial-policy/">AE Tax Advisors editorial policy</a>. Eligibility depends on the complete facts and the procedures in effect for the filing year.</p>
<ul>
<li><a href="https://www.irs.gov/irb/2025-24_IRB#REV-PROC-2025-23">Revenue Procedure 2025-23, section 6.07</a></li>
<li><a href="https://www.irs.gov/instructions/i3115">IRS Instructions for Form 3115</a></li>
<li><a href="https://www.irs.gov/filing/where-to-file-form-3115">IRS: Where to file Form 3115</a></li>
<li><a href="https://www.irs.gov/publications/p946">IRS Publication 946, How To Depreciate Property</a></li>
<li><a href="https://www.irs.gov/publications/p544">IRS Publication 544, Sales and Other Dispositions of Assets</a></li>
<li><a href="https://www.irs.gov/faqs/sale-or-trade-of-business-depreciation-rentals">IRS rental sale, depreciation, and recapture FAQs</a></li>
</ul>
""",
        ),
        related_section(
            [
                ("/blog/form-3115-missed-depreciation/", "Claiming missed rental depreciation with Form 3115"),
                ("/amended-return-vs-form-3115/", "Amended return versus Form 3115"),
                ("/wrong-rental-depreciation-basis/", "Correcting the wrong rental depreciation basis"),
                ("/catch-up-depreciation-section-481a/", "Section 481(a) catch-up depreciation"),
                ("/passive-loss-carryforward-correction/", "Correcting a rental passive-loss carryforward"),
            ]
        ),
    ]
    schemas = [
        article_schema(
            title="Can I File Form 3115 in the Year I Sell a Rental Property?",
            description=description,
            url=f"{SITE}{PATH}",
            published=DATE,
            modified=DATE,
            section="Rental Property Tax Corrections",
            keywords=[
                "Form 3115 year of sale rental property",
                "missed depreciation when selling rental property",
                "disposed property depreciation correction",
            ],
            citations=[
                "https://www.irs.gov/irb/2025-24_IRB#REV-PROC-2025-23",
                "https://www.irs.gov/instructions/i3115",
                "https://www.irs.gov/publications/p946",
                "https://www.irs.gov/publications/p544",
            ],
        ),
        breadcrumb_schema(
            [
                ("Home", "/"),
                ("Amended Business Returns", "/amended-business-tax-return-services/"),
                ("Form 3115 in a Rental Sale Year", PATH),
            ]
        ),
    ]
    return build_page(
        title=title,
        description=description,
        path=PATH,
        body="\n".join(body),
        schemas=schemas,
        published=DATE,
        modified=DATE,
        active_nav="/services/",
    )


def inject_related_link(relative_path: str) -> None:
    page = ROOT / relative_path / "index.html"
    text = page.read_text(encoding="utf-8")
    marker = "<!-- sale-year-form3115-link:start -->"
    end = "<!-- sale-year-form3115-link:end -->"
    block = f'''{marker}<section class="content-section fade-in-section"><div class="container narrow"><h2>Are You Selling the Rental This Year?</h2><p>The filing procedure changes when missed depreciation is discovered in the disposition year. Read <a href="{PATH}">whether Form 3115 can be filed in the year a rental property is sold</a>, then <a href="/discovery/">book a sale-year depreciation review</a> before the return is filed.</p></div></section>{end}'''
    if marker in text:
        text = re.sub(re.escape(marker) + r".*?" + re.escape(end), block, text, flags=re.S)
    else:
        text = text.replace("</main>", block + "\n</main>", 1)
    page.write_text(text, encoding="utf-8")


def main() -> None:
    rendered = build()
    main_html = re.search(r"<main[^>]*>(.*?)</main>", rendered, re.S).group(1)
    words = len(re.findall(r"\b[\w'-]+\b", re.sub(r"<[^>]+>", " ", main_html)))
    if words < 1_100:
        raise ValueError(f"buyer-intent guide is too thin: {words} words")
    if rendered.count('/discovery/') < 3:
        raise ValueError("buyer-intent guide needs direct booking paths")
    write_page(PATH, rendered)
    for relative_path in [
        "blog/form-3115-missed-depreciation",
        "wrong-rental-depreciation-basis",
        "catch-up-depreciation-section-481a",
        "amended-business-tax-return-services",
    ]:
        inject_related_link(relative_path)
    print(f"Built {PATH} ({words} main-content words)")


if __name__ == "__main__":
    main()
