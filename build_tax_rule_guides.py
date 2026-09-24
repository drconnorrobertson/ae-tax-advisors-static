#!/usr/bin/env python3
"""Build the tax-rule topic hub used to connect AE Tax's core guide clusters."""

from __future__ import annotations

import site_template as T


PATH = "/tax-rule-guides/"
TITLE = "Federal Tax Rule Guides for Business Owners and Real Estate Investors"
DESCRIPTION = (
    "Plain-English federal tax rule guides covering QBI, business entities, real estate, "
    "depreciation, amended returns, and IRS compliance topics."
)


def link_list(items: list[tuple[str, str, str]]) -> str:
    return "\n".join(
        f'            <li><a href="{href}"><strong>{label}</strong></a><br>{summary}</li>'
        for href, label, summary in items
    )


clusters = [
    (
        "Business Entity and Owner Tax Rules",
        "Start with the rules that determine how business income is classified, reported, and paid to owners.",
        [
            ("/qbi-deduction-guide/", "Qualified Business Income Deduction", "Section 199A eligibility, 2026 thresholds, limitations, and planning decisions."),
            ("/blog/what-is-a-disregarded-entity-and-how-is-it-taxed/", "Disregarded Entity Rules", "How a single-member LLC is treated for income, payroll, and excise-tax purposes."),
            ("/reasonable-compensation-s-corp-irs/", "S Corporation Reasonable Compensation", "What the IRS looks for when an owner is both a shareholder and an employee."),
            ("/the-business-owners-guide-to-section-731-distributions-and-recognized-gain/", "Partnership Distributions and Section 731", "When cash and property distributions can create recognized gain."),
        ],
    ),
    (
        "Real Estate and Passive Activity Rules",
        "These guides explain when rental losses are passive, when an exception may apply, and which records support the position.",
        [
            ("/blog/what-is-real-estate-professional-status-and-how-do-i-qualify/", "Real Estate Professional Status", "The 750-hour test, more-than-half test, material participation, and grouping."),
            ("/blog/passive-activity-loss-rules-for-real-estate-investors/", "Passive Activity Loss Rules", "How Section 469 limits rental and business losses and when suspended losses are released."),
            ("/blog/what-is-the-str-tax-loophole-and-how-does-it-work/", "Short-Term Rental Tax Rules", "Average rental period, material participation, depreciation, and the limits of the strategy."),
            ("/blog/1031-exchange-timeline-45-180-day-rules/", "1031 Exchange Timeline", "The 45-day identification deadline, 180-day exchange period, and return-date limit."),
            ("/blog/what-is-the-augusta-rule-and-can-i-use-it/", "Augusta Rule", "The fewer-than-15-day residence rental rule, fair-market pricing, business purpose, and documentation."),
        ],
    ),
    (
        "Depreciation and Cost Recovery Rules",
        "Use these resources to identify the right recovery period, method, convention, and election for business or rental property.",
        [
            ("/blog/macrs-depreciation-schedule-explained/", "MACRS Depreciation Tables", "Recovery periods, methods, conventions, and commonly used percentage tables."),
            ("/cost-segregation-study/", "Cost Segregation Studies", "How building components can be classified into shorter federal recovery periods."),
            ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation", "Current-year eligibility, placed-in-service timing, and interaction with other deductions."),
            ("/section-179-vs-bonus-depreciation-2026/", "Section 179 vs. Bonus Depreciation", "The practical differences in limits, eligible property, and ordering."),
            ("/form-3115-cost-segregation-lookback/", "Form 3115 Lookback", "How an accounting-method change can address missed depreciation without amending every prior return."),
        ],
    ),
    (
        "Corrections, Deadlines, and IRS Compliance",
        "These guides help owners understand the path for correcting returns and responding to common compliance problems.",
        [
            ("/amended-tax-returns/", "Amended Tax Returns", "When an amendment is appropriate, what changes, and what supporting records matter."),
            ("/amended-business-tax-return-services/", "Amended Business Returns", "Corrections for business filings and the related owner-level effects."),
            ("/irs-penalty-abatement/", "IRS Penalty Abatement", "Common relief paths, evidence to gather, and how reasonable cause is evaluated."),
            ("/tax-compliance-irs-representation/", "Tax Compliance and IRS Representation", "Support for notices, examinations, filings, and unresolved tax accounts."),
        ],
    ),
]


sections = []
for heading, intro, items in clusters:
    sections.append(
        T.section(
            heading,
            f"            <p>{intro}</p>\n"
            f'            <ul class="related-links">\n{link_list(items)}\n            </ul>',
        )
    )

body = "\n".join(
    [
        T.page_header(
            h1="Federal Tax Rule Guides",
            subtitle="IRS-grounded explanations for business owners and real estate investors, organized by the decision you need to make.",
            trail=[("Home", "/"), ("Guides", "/guides/"), ("Tax Rule Guides", PATH)],
        ),
        T.section(
            "Find the Rule Before You Use the Strategy",
            """            <p class="definition-lead"><strong>AE Tax Advisors' tax-rule guides explain the federal requirements behind commonly discussed planning strategies.</strong> Each guide identifies the governing rule, the facts that change the result, the records to keep, and the point where individualized advice becomes necessary.</p>
            <p>Use this page as a topic map. It connects detailed articles on entity taxation, real estate, depreciation, return corrections, and IRS compliance so you can move from a broad question to the exact rule that controls it.</p>""",
        ),
        *sections,
        T.section(
            "How to Use These Guides",
            """            <ol>
                <li><strong>Start with classification.</strong> Determine the taxpayer, entity, activity, and property involved.</li>
                <li><strong>Check timing.</strong> Many tax results depend on when an election is made, property is placed in service, or a transaction closes.</li>
                <li><strong>Document the facts.</strong> Time logs, invoices, agreements, valuations, and proof of business purpose often determine whether a position can be defended.</li>
                <li><strong>Model the full return.</strong> A deduction can affect basis, passive losses, payroll, state taxes, and future gain.</li>
            </ol>
            <p>These pages provide general education, not advice for a specific return. Review the full facts with a qualified tax professional before implementing a strategy.</p>""",
        ),
        T.related_section(
            [
                ("/guides/", "Tax Strategy Pillar Guides"),
                ("/glossary/", "Tax Glossary"),
                ("/blog/", "Tax Planning Blog"),
                ("/case-studies/", "Tax Planning Case Studies"),
            ],
            heading="More AE Tax Resources",
        ),
    ]
)

item_urls = [f"{T.SITE}{href}" for _, _, items in clusters for href, _, _ in items]
schemas = [
    {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": TITLE,
        "description": DESCRIPTION,
        "url": f"{T.SITE}{PATH}",
        "mainEntity": {
            "@type": "ItemList",
            "numberOfItems": len(item_urls),
            "itemListElement": [
                {"@type": "ListItem", "position": i, "url": url}
                for i, url in enumerate(item_urls, start=1)
            ],
        },
    },
    T.breadcrumb_schema([("Home", "/"), ("Guides", "/guides/"), ("Tax Rule Guides", PATH)]),
]

page = T.build_page(
    title=TITLE,
    description=DESCRIPTION,
    path=PATH,
    body=body,
    schemas=schemas,
    published="2026-09-23",
    modified="2026-09-23",
    active_nav="/guides/",
    og_type="website",
)

if __name__ == "__main__":
    output = T.write_page(PATH, page)
    print(output)
