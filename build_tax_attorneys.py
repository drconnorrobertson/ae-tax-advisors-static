#!/usr/bin/env python3
"""Build /tax-attorneys/.

Explains how AE Tax Advisors works alongside independent tax and business
attorneys on audit defense, IRS controversy and entity work. The attorneys
named here sit on the Board of Advisors and run their own firms, so the page
is written to make that relationship explicit rather than implying they are
employees of AE Tax Advisors.
"""

from __future__ import annotations

import site_template as T

PATH = "/tax-attorneys/"
PUBLISHED = "2026-08-17"
MODIFIED = "2026-08-17"

TITLE = "Tax Attorneys: Audit Defense and IRS Representation | AE Tax Advisors"
DESCRIPTION = (
    "How AE Tax Advisors works with independent tax and business attorneys on IRS "
    "examinations, tax controversy, and entity structuring for business owners."
)

LEAD = (
    "AE Tax Advisors is a tax advisory practice, not a law firm. For matters that call for "
    "legal representation, including IRS examinations that escalate, Tax Court petitions, and "
    "the legal side of entity restructuring, the firm works alongside independent attorneys "
    "who serve on its Board of Advisors. Each attorney runs their own practice and is engaged "
    "directly by the client."
)

BODY = [
    (
        "Where an Attorney Is the Right Call",
        "<p>Most of what a profitable business owner needs is advisory and compliance work: "
        "designing the structure, documenting the position, filing the return, and responding "
        "to routine notices. Enrolled Agents and CPAs are authorized to represent taxpayers "
        "before the IRS in examinations, collections, and appeals, and that covers the large "
        "majority of matters.</p>"
        "<p>Some situations genuinely call for counsel:</p>"
        "<ul>"
        "<li><strong>Litigation.</strong> Petitioning the United States Tax Court, or "
        "proceedings in district court or the Court of Federal Claims.</li>"
        "<li><strong>Attorney-client privilege.</strong> The limited practitioner privilege "
        "under IRC Section 7525 does not extend to criminal matters, and it does not apply in "
        "the same way as attorney-client privilege. Where exposure is uncertain, privileged "
        "advice matters.</li>"
        "<li><strong>Anything with criminal exposure.</strong> Unreported income, unfiled "
        "returns over multiple years, or a matter referred to Criminal Investigation.</li>"
        "<li><strong>Complex entity and transactional work.</strong> Drafting operating "
        "agreements, purchase agreements, and governance documents is the practice of law.</li>"
        "</ul>"
    ),
    (
        "How the Two Roles Fit Together",
        "<p>The division is usually clean. The advisory firm builds and documents the tax "
        "position: the reasonable compensation analysis, the cost segregation study, the "
        "grouping election, the depreciation schedules, the contemporaneous logs. Counsel "
        "handles the legal posture: privilege, procedure, and any proceeding before a court.</p>"
        "<p>In an examination, that means AE Tax Advisors produces and defends the substantive "
        "analysis behind a position while an attorney advises on strategy and, where the matter "
        "escalates beyond administrative appeals, carries it forward. Documentation built at the "
        "planning stage is what either party has to work with, which is why the two functions "
        "are more effective when the planning was done deliberately in the first place.</p>"
    ),
    (
        "Board of Advisors",
        "<p><strong>Jacob Simany, Esq.</strong> is a tax attorney, former IRS Office of Chief "
        "Counsel litigator, and founder of "
        '<a href="https://simanylaw.com/" target="_blank" rel="noopener noreferrer">Simany Law</a>. '
        "He advises on tax controversy and IRS dispute resolution, drawing on insider experience "
        "with how the IRS develops, negotiates, and settles cases.</p>"
        "<p><strong>Michael A. Zara, Esq.</strong> is a business attorney with nearly two decades "
        "of experience and a background in accounting, which lets him read a transaction "
        "financially and legally at the same time. He advises on entity structuring, business "
        "formation, contracts, mergers and acquisitions, and corporate governance through "
        '<a href="https://zarainjurylaw.com/" target="_blank" rel="noopener noreferrer">Zara Law</a>. '
        "He is licensed in Colorado, Arizona, Georgia, and North Carolina.</p>"
        '<p>Full biographies for both are on the <a href="/bios/">team page</a>.</p>'
    ),
    (
        "What AE Tax Advisors Handles Directly",
        "<p>No attorney referral is needed for the work that makes up most engagements:</p>"
        "<ul>"
        '<li><a href="/tax-compliance-irs-representation/">IRS representation</a> in '
        "examinations, collections, and administrative appeals, by Enrolled Agents and CPAs "
        "authorized to practice before the IRS.</li>"
        "<li>Notice response, penalty abatement requests, and installment agreements.</li>"
        '<li><a href="/audit-defense-compliance/">Audit defense</a> built on the documentation '
        "produced when the position was designed.</li>"
        '<li><a href="/entity-structuring-business-owners/">Entity structuring</a> analysis and '
        "the tax elections that implement it.</li>"
        "</ul>"
        "<p>Where a matter needs counsel, we say so early rather than late. The cheapest point "
        "to involve an attorney is before a position is filed, not after a notice arrives.</p>"
    ),
    (
        "Independent Relationships",
        "<p>The attorneys described here are not employees of AE Tax Advisors. Each operates "
        "their own firm, is engaged directly by the client under a separate agreement, and "
        "provides their own representations regarding their services. AE Tax Advisors does not "
        "practice law, does not provide legal advice, and receives no fee for referrals.</p>"
    ),
]

TAKEAWAYS = [
    "AE Tax Advisors is a tax advisory practice, not a law firm.",
    "Enrolled Agents and CPAs can represent taxpayers in IRS exams, collections, and appeals.",
    "Counsel is needed for litigation, privilege, criminal exposure, and drafting legal documents.",
    "The advisory firm builds the documented position; counsel handles legal posture and procedure.",
    "Board attorneys run independent firms and are engaged directly by the client.",
]

FAQS = [
    (
        "Do I need a tax attorney or a CPA for an IRS audit?",
        "<p>For most examinations, a CPA or an IRS Enrolled Agent is sufficient. Both are "
        "authorized to represent taxpayers before the IRS in examinations, collections, and "
        "appeals. An attorney becomes necessary where the matter heads to Tax Court, where "
        "attorney-client privilege matters, or where there is any criminal exposure.</p>",
    ),
    (
        "Does AE Tax Advisors provide legal services?",
        "<p>No. AE Tax Advisors is a tax advisory and compliance practice whose staff includes "
        "licensed CPAs and IRS Enrolled Agents. It does not practice law. Where a matter "
        "requires counsel, clients are introduced to independent attorneys who are engaged "
        "directly and separately.</p>",
    ),
    (
        "Is the tax practitioner privilege the same as attorney-client privilege?",
        "<p>No. The federally authorized tax practitioner privilege under IRC Section 7525 is "
        "narrower. It applies to non-criminal tax matters before the IRS and in federal court, "
        "and it does not extend to criminal proceedings or, generally, to tax shelter "
        "promotion. Where the boundary is uncertain, engaging counsel first is the safer "
        "sequence.</p>",
    ),
    (
        "Do you receive a referral fee for introducing an attorney?",
        "<p>No. The attorneys on the Board of Advisors operate independent firms and are "
        "engaged directly by the client. AE Tax Advisors receives no fee for the introduction, "
        "which is deliberate: the recommendation should turn on fit, not on compensation.</p>",
    ),
    (
        "When should an attorney be involved in tax planning?",
        "<p>Before a position is filed rather than after a notice arrives. Legal documents such "
        "as operating agreements and purchase agreements are drafted by counsel, and getting "
        "them consistent with the intended tax treatment at the outset avoids the most "
        "expensive category of correction later.</p>",
    ),
]

RELATED = [
    ("/tax-compliance-irs-representation/", "IRS representation and tax compliance"),
    ("/audit-defense-compliance/", "Audit defense and compliance"),
    ("/entity-structuring-business-owners/", "Entity structuring for business owners"),
    ("/bios/", "Our team and Board of Advisors"),
    ("/tax-planning-vs-tax-preparation/", "Tax planning vs tax preparation"),
]


def main() -> int:
    trail = [("Home", "/"), ("Tax Attorneys", PATH)]
    body = "\n".join([
        T.page_header(
            h1="Tax Attorneys, Audit Defense, and IRS Representation",
            subtitle=(
                "AE Tax Advisors is not a law firm. Here is how the advisory work and legal "
                "counsel fit together, and when you actually need an attorney."
            ),
            trail=trail,
        ),
        f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="article-intro">{LEAD}</p>
        </div>
    </section>""",
        "\n".join(T.section(h, html) for h, html in BODY),
        T.takeaways(TAKEAWAYS),
        T.faq_section(FAQS),
        T.related_section(RELATED),
    ])

    schemas = [
        T.article_schema(
            title=TITLE,
            description=DESCRIPTION,
            url=f"{T.SITE}{PATH}",
            published=PUBLISHED,
            modified=MODIFIED,
            section="IRS Representation",
            keywords=["tax attorney", "irs representation", "audit defense",
                      "tax controversy", "tax litigation"],
        ),
        T.faq_schema(FAQS),
        T.breadcrumb_schema(trail),
    ]

    html = T.build_page(
        title=TITLE,
        description=DESCRIPTION,
        path=PATH,
        body=body,
        schemas=schemas,
        published=PUBLISHED,
        modified=MODIFIED,
    )
    out = T.write_page(PATH, html)
    print(f"wrote {out.relative_to(T.ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
