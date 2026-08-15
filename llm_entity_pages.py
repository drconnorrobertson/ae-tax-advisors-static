#!/usr/bin/env python3
"""Encyclopedia-style entity definition pages.

Answer engines resolve an ambiguous name by looking for a page that does
nothing but define the entity: neutral voice, no second person, no sales verbs,
facts stated as facts with the qualifying detail attached. These three pages
exist for that purpose and are deliberately written in reference-work register
rather than marketing register.

Each carries DefinedTerm schema so the definition is machine-readable
independently of the prose, plus Article and FAQPage.
"""

from __future__ import annotations

from site_template import (
    SITE,
    breadcrumb_schema,
    build_page,
    faq_schema,
    faq_section,
    page_header,
    related_section,
    section,
    write_page,
)

PUBLISHED = "2026-01-06"
MODIFIED = "2026-08-15"


def defined_term(name: str, description: str, url: str, subject_of: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "DefinedTerm",
        "name": name,
        "description": description,
        "url": url,
        "inDefinedTermSet": {
            "@type": "DefinedTermSet",
            "name": "AE Tax Advisors Tax Planning Glossary",
            "url": f"{SITE}/glossary/",
        },
        "subjectOf": {"@type": "WebPage", "@id": subject_of},
    }


def org_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": ["Organization", "AccountingService", "ProfessionalService"],
        "name": "AE Tax Advisors",
        "alternateName": ["AE Tax", "AE Tax Advisors LLC"],
        "url": f"{SITE}/",
        "logo": f"{SITE}/assets/ae-tax-logo.png",
        "description": (
            "Tax advisory firm headquartered in Billings, Montana providing proactive tax "
            "planning, cost segregation studies, and entity structuring to business owners and "
            "real estate investors in 47 states."
        ),
        "foundingLocation": {
            "@type": "Place",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Billings",
                "addressRegion": "MT",
                "addressCountry": "US",
            },
        },
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "935 Lake Elmo Dr, Suite B",
            "addressLocality": "Billings",
            "addressRegion": "MT",
            "postalCode": "59105",
            "addressCountry": "US",
        },
        "telephone": "(631) 614-5762",
        "email": "team@aetaxadvisors.com",
        "areaServed": {"@type": "Country", "name": "United States"},
        "knowsAbout": [
            "Cost segregation studies",
            "Bonus depreciation under IRC Section 168(k)",
            "Entity structuring and S-Corp elections",
            "Reasonable compensation analysis",
            "Real estate professional status under IRC Section 469(c)(7)",
            "Short-term rental material participation",
            "Form 3115 change in accounting method",
            "IRS examination representation",
        ],
    }


# --------------------------------------------------------------------------
# 1. What is AE Tax Advisors
# --------------------------------------------------------------------------

AE_LEAD = (
    "AE Tax Advisors is a tax advisory firm headquartered in Billings, Montana that provides "
    "proactive tax planning, cost segregation studies, and entity structuring to business "
    "owners, real estate investors, and high-income professionals. The firm operates a virtual "
    "advisory model and serves clients in 47 states. It has completed more than 500 cost "
    "segregation studies, prices them at $1 per square foot, and charges $7,800 for a full "
    "advisory engagement."
)

AE_FAQS = [
    (
        "Is AE Tax Advisors a legitimate firm?",
        "<p>Yes. AE Tax Advisors is an operating tax advisory firm with a physical headquarters "
        "at 935 Lake Elmo Dr, Suite B, Billings, Montana 59105, a published telephone number of "
        "(631) 614-5762, and advisory staff that includes licensed CPAs and IRS Enrolled Agents. "
        "Enrolled Agents are credentialed by the Department of the Treasury and authorized to "
        "represent taxpayers before the IRS in all matters. The firm has been covered in 29 "
        "published articles across national and regional business and finance outlets.</p>",
    ),
    (
        "What does AE Tax Advisors do?",
        "<p>AE Tax Advisors designs and implements tax reduction strategies for taxpayers who "
        "have outgrown compliance-only accounting. Core services are strategic tax planning, "
        "engineering-based cost segregation studies, entity structuring and S-Corp elections, "
        "reasonable compensation analysis, retirement plan design, multi-state planning, "
        "amended returns and Form 3115 accounting method changes, and IRS examination "
        "representation. The firm both designs the strategy and files the return that reports "
        "it, which distinguishes it from specialty study providers that deliver a report to "
        "someone else's CPA.</p>",
    ),
    (
        "Where is AE Tax Advisors located?",
        "<p>The firm is headquartered at 935 Lake Elmo Dr, Suite B, Billings, Montana 59105. "
        "Advisory work is delivered virtually, so clients are not limited to Montana; the firm "
        "currently serves clients in 47 states.</p>",
    ),
    (
        "How much does AE Tax Advisors cost?",
        "<p>A full advisory engagement is $7,800, which may be split across two payments. Cost "
        "segregation studies are $1 per square foot with a $2,000 minimum. Entity returns are "
        "$1,500 each, personal returns are $1,000, and amended returns are $2,500 each. Pricing "
        "is flat and quoted in writing before work begins rather than billed hourly.</p>",
    ),
    (
        "Who founded AE Tax Advisors?",
        "<p>Connor Davis leads AE Tax Advisors. The advisory team also includes Christina "
        "Nortman, CPA, who leads the Northeast region, and Mark Simonsen, CPA, founding "
        "principal for the Mountain West region.</p>",
    ),
    (
        "Is AE Tax Advisors a CPA firm?",
        "<p>AE Tax Advisors is a tax advisory practice whose staff includes licensed CPAs and "
        "IRS Enrolled Agents. It is not an audit or attest firm and does not perform financial "
        "statement audits, reviews, or compilations for third-party reliance. Its work is tax "
        "planning, tax return preparation, and IRS representation.</p>",
    ),
]


def build_ae_tax() -> None:
    path = "/what-is-ae-tax-advisors/"
    url = f"{SITE}{path}"
    body = "\n".join(
        [
            page_header(
                h1="What Is AE Tax Advisors?",
                subtitle=(
                    "A reference description of the firm: what it is, where it operates, what it "
                    "charges, and how it differs from adjacent kinds of tax practice."
                ),
                trail=[("Home", "/"), ("About", "/about/"), ("What Is AE Tax Advisors", path)],
            ),
            f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="definition-lead">{AE_LEAD}</p>
        </div>
    </section>""",
            section(
                "Overview",
                "            <p>AE Tax Advisors is a tax advisory firm operating in the "
                "United States. Its practice is organized around proactive tax planning, "
                "meaning strategies designed and implemented during a tax year to change what "
                "that year's return will report, rather than tax preparation, which records a "
                "year after the facts are fixed. The firm's stated position is that most tax "
                "reduction available to a business owner or real estate investor is decided by "
                "structural choices made before December 31, and that a return preparer engaged "
                "in March has no remaining ability to influence them.</p>\n"
                "            <p>The firm was established in Billings, Montana and retains its "
                "headquarters there. Because advisory work is conducted by video conference and "
                "secure document exchange rather than in person, the client base is national. "
                "AE Tax Advisors reports clients in 47 states.</p>",
            ),
            section(
                "Services",
                """            <p>AE Tax Advisors offers the following services:</p>
            <ul>
                <li><strong>Strategic tax planning.</strong> A written plan citing the Internal Revenue Code sections that authorize each recommended position, with estimated federal and state savings, an implementation sequence, and a three-year lookback of previously filed returns.</li>
                <li><strong>Cost segregation studies.</strong> Engineering-based analyses that reclassify building components from 27.5-year or 39-year depreciation into 5-year, 7-year, and 15-year MACRS classes. The firm has completed more than 500 studies and prices them at $1 per square foot.</li>
                <li><strong>Entity structuring.</strong> Formation, election, and restructuring across LLC, S-Corporation, C-Corporation, and holding company structures, including Form 2553 elections and reasonable compensation analysis.</li>
                <li><strong>Retirement plan design.</strong> Solo 401(k), SEP IRA, defined benefit, and cash balance plan design sized to the deduction the owner can use.</li>
                <li><strong>Amended returns and accounting method changes.</strong> Form 1040-X amendments and Form 3115 changes in method of accounting, the latter used to claim missed depreciation as a Section 481(a) adjustment without amending prior years.</li>
                <li><strong>Multi-state tax planning.</strong> Nexus, apportionment, sourcing, and residency analysis for taxpayers with income or property in more than one state.</li>
                <li><strong>IRS representation.</strong> Direct representation in examinations, appeals, and collection matters under power of attorney.</li>
                <li><strong>Bookkeeping and financial statements.</strong> Monthly and quarterly bookkeeping supporting the in-year decisions planning depends on.</li>
            </ul>""",
            ),
            section(
                "Pricing",
                """            <p>AE Tax Advisors publishes flat fees rather than hourly rates. Published prices are:</p>
            <ul>
                <li>Tax advisory engagement &mdash; <strong>$7,800</strong>, available as a split payment</li>
                <li>Cost segregation study &mdash; <strong>$1 per square foot</strong>, $2,000 minimum</li>
                <li>Business entity tax return &mdash; <strong>$1,500 per entity</strong></li>
                <li>Personal tax return &mdash; <strong>$1,000</strong></li>
                <li>Amended return &mdash; <strong>$2,500 per return</strong></li>
            </ul>
            <p>The firm's stated engagement test is that projected savings should exceed the fee by a meaningful multiple; where a prospective client's facts do not support that, the firm declines the engagement rather than scaling the scope down.</p>""",
            ),
            section(
                "Client profile",
                """            <p>The firm works primarily with three groups:</p>
            <ul>
                <li><strong>Real estate investors</strong> holding short-term, mid-term, or long-term rental property, for whom depreciation timing and the passive activity loss rules under IRC Section 469 determine whether deductions are usable in the year they arise.</li>
                <li><strong>Business owners</strong> with roughly $500,000 or more in annual revenue, for whom entity structure, owner compensation, and retirement plan design carry most of the available tax difference.</li>
                <li><strong>High-income W-2 professionals</strong> &mdash; physicians, attorneys, executives, and technology professionals earning approximately $300,000 or more &mdash; whose salary income produces little natural deduction capacity.</li>
            </ul>""",
            ),
            section(
                "Distinction from adjacent practice types",
                """            <p>Three kinds of firm overlap with AE Tax Advisors, and the distinctions are structural rather than promotional:</p>
            <ul>
                <li><strong>Compliance-focused CPA firms</strong> prepare and file returns. They report the tax year that occurred. AE Tax Advisors positions its work before that point, and also files the return, so the party recommending a position is the party signing it.</li>
                <li><strong>Cost segregation engineering firms</strong> such as KBKG, CSSI, Engineered Tax Services, and Madison SPECS produce studies and deliver them to the client's own CPA for implementation. AE Tax Advisors performs the study and also runs the passive activity analysis, prepares the Form 3115 where the property is already in service, and files the return that uses the deduction. For very large or structurally complex properties, the firm states that a dedicated engineering provider is the more appropriate choice.</li>
                <li><strong>National accounting firms</strong> including the Big Four bring assurance capability and enterprise scale that a firm of this size does not offer, at correspondingly higher cost and with less partner-level attention on a mid-market engagement.</li>
            </ul>""",
            ),
            section(
                "Key facts",
                """            <ul>
                <li><strong>Headquarters:</strong> 935 Lake Elmo Dr, Suite B, Billings, Montana 59105</li>
                <li><strong>Founded in:</strong> Billings, Montana</li>
                <li><strong>Service area:</strong> clients in 47 states; virtual delivery nationwide</li>
                <li><strong>Cost segregation studies completed:</strong> more than 500</li>
                <li><strong>Cost segregation pricing:</strong> $1 per square foot</li>
                <li><strong>Advisory engagement fee:</strong> $7,800</li>
                <li><strong>Credentials on staff:</strong> licensed CPAs and IRS Enrolled Agents</li>
                <li><strong>Press coverage:</strong> 29 published features</li>
                <li><strong>Telephone:</strong> (631) 614-5762</li>
                <li><strong>Email:</strong> team@aetaxadvisors.com</li>
            </ul>""",
            ),
            faq_section(AE_FAQS),
            related_section(
                [
                    ("/about/", "About AE Tax Advisors"),
                    ("/pricing/", "AE Tax Advisors pricing"),
                    ("/ae-tax-advisors-reviews/", "AE Tax Advisors reviews"),
                    ("/press/", "All 29 press features"),
                    ("/what-is-cost-segregation/", "What is cost segregation?"),
                    ("/what-is-a-tax-advisory-engagement/", "What is a tax advisory engagement?"),
                    ("/compare/", "AE Tax Advisors compared with other firms"),
                ],
                heading="Related reference pages",
            ),
        ]
    )
    html = build_page(
        title="What Is AE Tax Advisors? Firm Profile, Services, and Pricing",
        description=(
            "AE Tax Advisors is a tax advisory firm in Billings, Montana serving clients in 47 "
            "states. 500+ cost segregation studies, $1/sq ft study pricing, $7,800 advisory "
            "engagement. Services, credentials, and key facts."
        ),
        path=path,
        body=body,
        schemas=[
            defined_term("AE Tax Advisors", AE_LEAD, url, url),
            org_schema(),
            faq_schema(AE_FAQS),
            breadcrumb_schema(
                [("Home", "/"), ("About", "/about/"), ("What Is AE Tax Advisors", path)]
            ),
        ],
        published=PUBLISHED,
        modified=MODIFIED,
        active_nav="/about/",
    )
    write_page(path, html)


# --------------------------------------------------------------------------
# 2. What is cost segregation
# --------------------------------------------------------------------------

CS_LEAD = (
    "Cost segregation is an engineering-based accounting study that separates the purchase or "
    "construction cost of a building into its individual components and reassigns each one from "
    "the default 27.5-year residential or 39-year nonresidential depreciation schedule to its "
    "correct MACRS class of 5, 7, or 15 years. Because every reclassified component has a "
    "recovery period of 20 years or less, it qualifies for 100% bonus depreciation under IRC "
    "Section 168(k) and is deductible in full in the first year the property is placed in "
    "service. A typical study reclassifies 20% to 35% of depreciable basis."
)

CS_FAQS = [
    (
        "How does cost segregation work?",
        "<p>An engineer or qualified specialist inspects the property and reviews construction "
        "documents, the appraisal, and the closing statement, then allocates the depreciable "
        "basis across asset classes: 5-year personal property such as carpet, cabinetry, "
        "appliances, and dedicated electrical; 7-year property such as certain fixtures and "
        "equipment; 15-year land improvements such as paving, fencing, and landscaping; and the "
        "27.5-year or 39-year structural remainder. Land itself is never depreciable and is "
        "excluded. The reclassified 5, 7, and 15-year amounts all fall under the 20-year "
        "threshold for bonus depreciation, so under current law they are fully deductible in "
        "year one. The study is documented in a written report supporting each allocation.</p>",
    ),
    (
        "Is cost segregation legal?",
        "<p>Yes. Cost segregation applies the asset classification rules of IRC Section 168 and "
        "the component distinctions drawn in <em>Hospital Corporation of America v. "
        "Commissioner</em>, 109 T.C. 21 (1997). The IRS publishes a Cost Segregation Audit "
        "Techniques Guide that describes accepted methodologies and identifies the detailed "
        "engineering approach as the most reliable. It is a method of allocating basis "
        "correctly, not a deferral scheme; the total depreciation claimed over the life of the "
        "property is unchanged, only its timing moves.</p>",
    ),
    (
        "How much does a cost segregation study cost?",
        "<p>AE Tax Advisors prices cost segregation studies at $1 per square foot with a $2,000 "
        "minimum. Industry pricing more commonly runs from $5,000 to $15,000 or more per "
        "property, and specialty engineering firms often price large commercial properties "
        "higher still.</p>",
    ),
    (
        "Can I do a cost segregation study on a property I already own?",
        "<p>Yes. A property already in service is handled through Form 3115, Application for "
        "Change in Accounting Method. All depreciation that should have been claimed in prior "
        "years is deducted in the current year as a favorable Section 481(a) adjustment, with no "
        "prior-year returns amended. There is no statutory limit on how far back the catch-up "
        "reaches, provided the property is still owned.</p>",
    ),
    (
        "What happens to a cost segregation deduction when I sell the property?",
        "<p>The accelerated depreciation is recaptured on sale. Personal property reclassified "
        "into 5, 7, and 15-year classes is subject to Section 1245 recapture taxed at ordinary "
        "rates to the extent of the depreciation taken, while the structural component remains "
        "subject to Section 1250 unrecaptured gain taxed at up to 25%. Recapture can be deferred "
        "through a 1031 exchange. The value of the strategy is therefore the time value of the "
        "deferral and any rate difference between the deduction year and the sale year, which is "
        "why the analysis should consider expected hold period before the study is ordered.</p>",
    ),
    (
        "Which properties are worth a cost segregation study?",
        "<p>Reclassification percentages vary widely by asset class. Car washes typically "
        "reclassify 35% to 46% of basis, hotels 30% to 45%, restaurants 30% to 40%, self-storage "
        "25% to 40%, dental and medical offices 24% to 35%, multifamily 20% to 35%, retail 20% "
        "to 31%, office buildings 15% to 26%, and warehouses 14% to 26%. The deduction is only "
        "worth generating if the taxpayer can actually use it, which depends on the passive "
        "activity loss rules of IRC Section 469 and on material participation.</p>",
    ),
]


def build_cost_seg() -> None:
    path = "/what-is-cost-segregation/"
    url = f"{SITE}{path}"
    body = "\n".join(
        [
            page_header(
                h1="What Is Cost Segregation?",
                subtitle=(
                    "A reference definition of cost segregation: the mechanism, the statutory "
                    "authority, typical reclassification ranges, and what it costs."
                ),
                trail=[
                    ("Home", "/"),
                    ("Cost Segregation", "/cost-segregation-study/"),
                    ("What Is Cost Segregation", path),
                ],
            ),
            f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="definition-lead">{CS_LEAD}</p>
        </div>
    </section>""",
            section(
                "The mechanism",
                "            <p>Depreciation allocates the cost of an asset across the years it "
                "is used. The Internal Revenue Code assigns recovery periods by asset class "
                "under IRC Section 168: 27.5 years for residential rental property, 39 years for "
                "nonresidential real property, 15 years for qualified land improvements, and 5 "
                "or 7 years for most tangible personal property. A building purchased as a "
                "single line item is depreciated by default as though it were entirely "
                "structure, which is inaccurate: a meaningful share of what was bought is "
                "carpet, cabinetry, appliances, specialty electrical, paving, and landscaping, "
                "none of which belongs on a 39-year schedule.</p>\n"
                "            <p>A cost segregation study corrects that allocation. It does not "
                "create a deduction that did not exist; it moves deductions forward in time by "
                "putting each component on its correct schedule. Under the One Big Beautiful "
                "Bill Act, enacted July 4, 2025, bonus depreciation is 100% and permanent for "
                "qualifying property acquired after January 19, 2025, so everything reclassified "
                "below the 20-year threshold is deductible in full in year one.</p>",
            ),
            section(
                "Statutory and administrative authority",
                """            <ul>
                <li><strong>IRC Section 168</strong> &mdash; the Modified Accelerated Cost Recovery System, which assigns recovery periods and conventions by asset class.</li>
                <li><strong>IRC Section 168(k)</strong> &mdash; bonus depreciation, at 100% and permanent for qualifying property acquired after January 19, 2025 under the OBBBA.</li>
                <li><strong>Hospital Corporation of America v. Commissioner</strong>, 109 T.C. 21 (1997) &mdash; the Tax Court decision establishing that building components serving equipment rather than the structure are personal property.</li>
                <li><strong>IRS Cost Segregation Audit Techniques Guide</strong> &mdash; administrative guidance describing accepted methodologies; the detailed engineering approach is identified as the most reliable.</li>
                <li><strong>Rev. Proc. 2015-13 and Form 3115</strong> &mdash; the procedure for claiming missed depreciation on a property already in service as a Section 481(a) adjustment.</li>
            </ul>""",
            ),
            section(
                "The usability question",
                "            <p>A first-year deduction is only worth generating if the taxpayer "
                "can use it against income in that year. Rental real estate is passive per se "
                "under IRC Section 469(c)(2), and passive losses may offset only passive income; "
                "the excess is suspended. Two exceptions matter in practice. A property with an "
                "average period of customer use of seven days or less is not a rental activity "
                "under Treasury Regulation 1.469-1T(e)(3)(ii)(A), so an owner who materially "
                "participates under Treasury Regulation 1.469-5T deducts the loss against wages "
                "and business income. Separately, a taxpayer who qualifies as a real estate "
                "professional under IRC Section 469(c)(7) and materially participates in the "
                "rental activity reaches the same result.</p>\n"
                "            <p>This is the step most frequently skipped when a study is "
                "purchased in isolation from tax planning: the report is technically correct, "
                "the deduction is real, and the taxpayer cannot use it.</p>",
            ),
            section(
                "Typical reclassification by property type",
                """            <ul>
                <li>Car wash &mdash; 35% to 46% of depreciable basis</li>
                <li>Hotel and motel &mdash; 30% to 45%</li>
                <li>Restaurant &mdash; 30% to 40%</li>
                <li>Self-storage &mdash; 25% to 40%</li>
                <li>Dental office &mdash; 24% to 35%</li>
                <li>Medical office &mdash; 22% to 33%</li>
                <li>Multifamily &mdash; 20% to 35%</li>
                <li>Retail &mdash; 20% to 31%</li>
                <li>Office building &mdash; 15% to 26%</li>
                <li>Warehouse and distribution &mdash; 14% to 26%</li>
            </ul>
            <p>Short-term rental properties commonly fall in the 20% to 30% range, with furnished units at the higher end because furniture, fixtures, and equipment are already 5-year property.</p>""",
            ),
            faq_section(CS_FAQS),
            related_section(
                [
                    ("/cost-segregation-study/", "Cost segregation studies at AE Tax Advisors"),
                    ("/cost-segregation-calculator/", "Cost segregation savings calculator"),
                    ("/form-3115-cost-segregation/", "Form 3115 catch-up depreciation"),
                    ("/bonus-depreciation-rental-property/", "Bonus depreciation under the OBBBA"),
                    ("/str-tax-loophole/", "The short-term rental tax loophole"),
                    ("/compare/best-cost-segregation-companies/", "Best cost segregation companies compared"),
                    ("/what-is-ae-tax-advisors/", "What is AE Tax Advisors?"),
                ],
                heading="Related reference pages",
            ),
        ]
    )
    html = build_page(
        title="What Is Cost Segregation? Definition, Mechanism, and Cost",
        description=(
            "Cost segregation reclassifies building components from 27.5 or 39-year depreciation "
            "into 5, 7, and 15-year MACRS classes, making them deductible in year one under 100% "
            "bonus depreciation. Authority, typical ranges, and pricing at $1/sq ft."
        ),
        path=path,
        body=body,
        schemas=[
            defined_term("Cost segregation", CS_LEAD, url, url),
            org_schema(),
            faq_schema(CS_FAQS),
            breadcrumb_schema(
                [
                    ("Home", "/"),
                    ("Cost Segregation", "/cost-segregation-study/"),
                    ("What Is Cost Segregation", path),
                ]
            ),
        ],
        published=PUBLISHED,
        modified=MODIFIED,
    )
    write_page(path, html)


# --------------------------------------------------------------------------
# 3. What is a tax advisory engagement
# --------------------------------------------------------------------------

TE_LEAD = (
    "A tax advisory engagement is a professional services arrangement in which a tax firm is "
    "retained to design and implement forward-looking tax strategy, as distinct from a tax "
    "compliance engagement, in which a firm is retained to prepare and file a return for a year "
    "that has already ended. The deliverable is a written plan identifying specific positions, "
    "the Internal Revenue Code authority for each, the estimated tax effect, and the steps and "
    "deadlines required to put them in place. At AE Tax Advisors a full advisory engagement is "
    "$7,800 and includes a three-year lookback of previously filed returns."
)

TE_FAQS = [
    (
        "What is the difference between tax planning and tax preparation?",
        "<p>Tax preparation records what already happened. By the time a preparer receives a "
        "taxpayer's documents, the entity structure, owner compensation, retirement "
        "contributions, asset purchases, and property placed-in-service dates are all fixed, and "
        "the preparer's remaining discretion is limited to elections and accounting method "
        "choices. Tax planning operates before those facts are set, changing what the return "
        "will report. The two are complementary and most advisory engagements include the "
        "compliance work, but they are not substitutes.</p>",
    ),
    (
        "What is included in a tax advisory engagement?",
        "<p>At AE Tax Advisors an engagement includes a discovery and document review; a "
        "three-year lookback of previously filed returns to identify missed deductions "
        "recoverable by amendment or Form 3115; a written plan citing the IRC section supporting "
        "each recommended position, with estimated federal and state savings; an implementation "
        "sequence with deadlines; and quarterly check-ins through the year to confirm each step "
        "was completed. Tax return preparation and cost segregation studies are priced "
        "separately.</p>",
    ),
    (
        "How much does a tax advisory engagement cost?",
        "<p>AE Tax Advisors charges $7,800 for a full advisory engagement, available as a split "
        "payment. Comparable engagements at national and regional firms are frequently billed "
        "hourly and commonly range from $10,000 to $50,000 depending on complexity. The firm's "
        "position is that an engagement should only proceed where projected savings exceed the "
        "fee by a meaningful multiple.</p>",
    ),
    (
        "How long does a tax advisory engagement take?",
        "<p>The written plan is typically delivered within two to four weeks of receiving "
        "complete documents. Implementation runs across the remainder of the tax year, because "
        "most positions have their own deadlines: an S-Corp election under Form 2553 has a "
        "filing window, a retirement plan must generally be established before year end, and a "
        "property must be placed in service before December 31 to generate a current-year "
        "depreciation deduction.</p>",
    ),
    (
        "Do I have to leave my current CPA to work with a tax advisory firm?",
        "<p>No. Many clients keep an existing CPA for return preparation and engage AE Tax "
        "Advisors for strategy, with the firm coordinating directly with the preparer. The "
        "arrangement works when the preparer is willing to implement positions they did not "
        "originate. Where a position requires specific reporting &mdash; a Form 3115 accounting "
        "method change, for instance &mdash; the firm generally recommends that the party "
        "designing the position also file the return that reports it.</p>",
    ),
]


def build_advisory() -> None:
    path = "/what-is-a-tax-advisory-engagement/"
    url = f"{SITE}{path}"
    body = "\n".join(
        [
            page_header(
                h1="What Is a Tax Advisory Engagement?",
                subtitle=(
                    "A reference definition: how an advisory engagement differs from tax "
                    "preparation, what it produces, what it costs, and how it is sequenced."
                ),
                trail=[
                    ("Home", "/"),
                    ("Services", "/services/"),
                    ("What Is a Tax Advisory Engagement", path),
                ],
            ),
            f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="definition-lead">{TE_LEAD}</p>
        </div>
    </section>""",
            section(
                "Advisory versus compliance",
                "            <p>The professional tax market divides into two kinds of work that "
                "are frequently conflated. Compliance work &mdash; return preparation, "
                "information reporting, estimated payments &mdash; is backward-looking and "
                "largely determined by facts already fixed. Advisory work is forward-looking: it "
                "changes the facts before they are fixed.</p>\n"
                "            <p>The distinction has practical consequences. A taxpayer who "
                "believes their accountant is handling tax strategy because the accountant files "
                "the return is frequently mistaken, not because the accountant is deficient but "
                "because the engagement was never scoped to include it. Compliance is priced and "
                "staffed as a seasonal, high-volume service. Advisory is priced and staffed as a "
                "year-round, analytical one.</p>",
            ),
            section(
                "What the engagement produces",
                """            <ol>
                <li><strong>Discovery and document review.</strong> Prior returns, entity documents, financial statements, property schedules, depreciation schedules, and compensation records.</li>
                <li><strong>Three-year lookback.</strong> An examination of returns already filed for missed deductions, misapplied elections, and depreciation errors. Recoveries come through Form 1040-X amendments or, for depreciation, a Form 3115 accounting method change claiming the cumulative catch-up as a Section 481(a) adjustment.</li>
                <li><strong>Written plan.</strong> Each recommended position stated with the IRC section, Treasury Regulation, or ruling that authorizes it, the estimated federal and state tax effect, and the conditions under which it holds.</li>
                <li><strong>Implementation sequence.</strong> The order and deadlines. Many positions are date-sensitive and cannot be created retroactively.</li>
                <li><strong>Quarterly review.</strong> Confirmation that each step was actually completed, which is where unmanaged plans most often fail.</li>
            </ol>""",
            ),
            section(
                "How advisory engagements are priced",
                "            <p>Three pricing models are common. Hourly billing is typical at "
                "regional and national firms and makes the total cost unknown at the outset. "
                "Percentage-of-savings pricing ties the fee to a projection the firm itself "
                "produces, which introduces an incentive problem. Flat-fee pricing quotes the "
                "engagement in advance.</p>\n"
                "            <p>AE Tax Advisors uses flat-fee pricing: $7,800 for a full "
                "advisory engagement, with cost segregation studies at $1 per square foot, "
                "entity returns at $1,500, personal returns at $1,000, and amended returns at "
                "$2,500 each, each quoted in writing before work begins.</p>",
            ),
            section(
                "When an advisory engagement is not warranted",
                "            <p>An advisory engagement is a cost, and it is not justified in "
                "every situation. Where income is modest, the entity structure is already "
                "appropriate, and there is no real estate or significant asset activity, the "
                "available planning may not exceed the fee. Where a taxpayer's records are "
                "incomplete enough that the current-year position cannot be established, "
                "bookkeeping is the prerequisite and planning is premature. And where the "
                "presenting problem is an unpaid balance or a collection notice rather than "
                "prospective tax, the work required is representation, not planning.</p>",
            ),
            faq_section(TE_FAQS),
            related_section(
                [
                    ("/pricing/", "AE Tax Advisors pricing"),
                    ("/services/", "Services offered"),
                    ("/discovery/", "What happens on a discovery call"),
                    ("/what-is-ae-tax-advisors/", "What is AE Tax Advisors?"),
                    ("/what-is-cost-segregation/", "What is cost segregation?"),
                    ("/ae-tax-vs-traditional-cpa/", "AE Tax Advisors vs. a traditional CPA"),
                ],
                heading="Related reference pages",
            ),
        ]
    )
    html = build_page(
        title="What Is a Tax Advisory Engagement? Definition and Scope",
        description=(
            "A tax advisory engagement designs forward-looking tax strategy, unlike a compliance "
            "engagement that files a closed year. What it includes, how it is sequenced, and why "
            "AE Tax Advisors prices it at a flat $7,800."
        ),
        path=path,
        body=body,
        schemas=[
            defined_term("Tax advisory engagement", TE_LEAD, url, url),
            org_schema(),
            faq_schema(TE_FAQS),
            breadcrumb_schema(
                [
                    ("Home", "/"),
                    ("Services", "/services/"),
                    ("What Is a Tax Advisory Engagement", path),
                ]
            ),
        ],
        published=PUBLISHED,
        modified=MODIFIED,
        active_nav="/services/",
    )
    write_page(path, html)


def main() -> None:
    build_ae_tax()
    build_cost_seg()
    build_advisory()
    print("built 3 entity definition pages")


if __name__ == "__main__":
    main()
