#!/usr/bin/env python3
"""Build a small set of researched, transaction-specific AE Tax guides."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = (ROOT / "1031-exchange-replacement-property-new-llc-owner-review/index.html").read_text()
DOMAIN = "https://www.aetaxadvisors.com"

PAGES = [
    dict(
        slug="s-corp-owner-pay-across-related-companies",
        title="S-Corp Owner Pay Across Related Companies",
        question="How should I pay myself when I own several S corporations?",
        description="Own multiple profitable S corporations? Review duties, payroll, distributions, and related-company pay before setting owner compensation.",
        audience="Business Owners",
        subtitle="An owner who works across several profitable companies needs an actual pay plan for the services performed in each business.",
        sections=[
            ("Start with the work, not the distributions", ["Suppose you oversee two operating S corporations and a management company. One entity runs payroll, while all three distribute cash to you. The first question is which corporation receives your services and what each company actually pays for them. The IRS expects reasonable compensation for services before nonwage distributions from an S corporation. A salary from one company should not be assumed to settle the question for every related company.", "Write down your responsibilities, hours, delegated work, and who signs each company's contracts. Compare the pay arrangement with similar roles, the economics of each entity, and any bona fide intercompany services agreement. Document the answer before year-end distributions are finalized."]),
            ("Does a common paymaster solve the payroll problem?", ["The common paymaster rule is narrow. It can apply when related corporations concurrently employ the same individual and one corporation disburses remuneration on behalf of the group. Merely routing cash through a management company does not establish the rule. Have the payroll adviser confirm related-corporation status, concurrent employment, payment records, and employment-tax reporting before using it.", "A management fee also needs its own support: what services were provided, how the fee was set, which entity deducts it, and how each company reports the transaction. Payroll convenience cannot substitute for these facts."]),
            ("What to bring to a compensation review", ["Bring the prior two years of entity returns, ownership chart, payroll registers, distribution ledger, management agreements, and a description of your role at each company. AE can reconcile the compensation and intercompany payments with the returns, identify unsupported gaps, and propose a prospective payroll plan. If the entities have different owners, states, or elections, those differences belong in the analysis."])
        ],
        sources=[("IRS: S corporation compensation", "https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues"), ("IRS: Common paymaster", "https://www.irs.gov/government-entities/common-paymaster")],
        related=[("S-corp owner pay service", "/services/reasonable-compensation/"), ("Business owner tax planning", "/business-owner-tax-planning/")],
    ),
    dict(
        slug="business-equipment-delivered-not-installed-year-end",
        title="Equipment Delivered Before Year-End: Deduction Timing",
        question="Can my business deduct equipment delivered in December but installed in January?",
        description="Bought equipment before year-end but could not use it until January? Check the placed-in-service date before claiming depreciation or Section 179.",
        audience="Business Owners",
        subtitle="A paid invoice and a delivery receipt do not establish when equipment became ready and available for business use.",
        sections=[
            ("The date that controls", ["A profitable manufacturer orders a new production line in November. It arrives on December 27, but an electrician connects it and the vendor completes commissioning in January. The owner wants a December deduction because the purchase was paid for. For depreciation, the controlling date is when property is placed in service: ready and available for its specific business use. On these facts, delivery alone is weak evidence of a December placed-in-service date.", "The answer can differ for a machine that is fully installed, tested, and available to produce goods in December even if the owner first runs a customer order in January. Preserve the facts that show readiness, rather than selecting the date from a bill or payment confirmation."]),
            ("Build a date file for each major asset", ["Keep the purchase contract, freight receipt, installation work orders, utility sign-off, vendor acceptance test, insurance start date, and first production log. Separate a complete machine from optional later upgrades. An unfinished installation and a usable machine awaiting routine production have different facts.", "Financing does not by itself change the readiness test. Nor does a year-end journal entry make equipment available for use. Section 179 and any applicable bonus depreciation should be modeled only after the asset's qualifying cost, business use, and placed-in-service year are established. Limits and elections can change the best choice."]),
            ("Plan the return and next purchase", ["Give AE an asset-by-asset schedule with dates and supporting records before the return is signed. We can align the tax depreciation schedule to operations records and compare available elections with expected income. For next year's capital purchases, involve facilities and the vendor early enough to know whether installation can actually finish before year-end."])
        ],
        sources=[("IRS Publication 946: How To Depreciate Property", "https://www.irs.gov/publications/p946")],
        related=[("Equipment leasing and Section 179", "/equipment-leasing-section-179/"), ("Business owner tax planning", "/business-owner-tax-planning/")],
    ),
    dict(
        slug="business-owner-large-accruals-before-signing-return",
        title="Large Accruals Before Signing a Business Return",
        question="What should I review before signing a business return with large accruals?",
        description="Profitable business owner with large year-end accruals? Review contracts, dates, payment records, and accounting method before signing the return.",
        audience="Business Owners",
        subtitle="A year-end accrual can move income or deductions between years. The owner should see the transaction support before approving the return.",
        sections=[
            ("Ask which transactions moved the result", ["A growing service firm reports strong cash collections but a much lower taxable profit after large year-end entries. Ask for a schedule of each material accrued revenue and expense item, with the customer or vendor, contract, invoice, amount, dates, and tax treatment. Compare the schedule to the general ledger and the prior-year return. An unexplained net accrual number is not enough to assess the filing position.", "Under an accrual method, income generally is included when the right to receive it is fixed and the amount can be determined with reasonable accuracy. Expense timing has separate requirements, including economic performance. A book entry can be appropriate for financial statements yet fall in a different tax year."]),
            ("Separate timing issues from corrections", ["Look at retainers, deferred customer billings, disputed receivables, bonuses, related-party charges, and work performed near the year-end cutoff. Trace a sample through signed contracts, delivery records, invoices, and subsequent payments. The tax result may differ by transaction; do not apply one generic rule to the whole accrual account.", "Also ask whether this is an established accounting method, a newly proposed treatment, or the correction of a posting mistake. Some method changes require a formal process and may affect multiple years. The return preparer should explain which category applies and how prior-year balances reconcile."]),
            ("Make the signing decision reviewable", ["Request a one-page bridge from book income to taxable income, a list of the largest timing items, and written answers to unresolved questions. AE can review the method and supporting workpapers before filing, then prioritize any adjustment or method-change analysis. Bring the current and prior returns, trial balances, contracts, A/R and A/P aging, and work-in-progress reports."])
        ],
        sources=[("IRS Publication 538: Accounting Periods and Methods", "https://www.irs.gov/publications/p538")],
        related=[("Construction retainage review", "/construction-retainage-tax-method-review/"), ("Business owner tax planning", "/business-owner-tax-planning/")],
    ),
    dict(
        slug="commercial-property-seller-repair-credit-tax-basis",
        title="Commercial Property Seller Repair Credit and Tax Basis",
        question="How does a seller repair credit affect my commercial property's tax basis?",
        description="Buying commercial real estate with a seller repair credit? Determine the actual purchase price, repair spending, and depreciable basis from closing records.",
        audience="Real Estate Investors",
        subtitle="A repair credit changes the cash needed at closing, but the tax basis calculation depends on the final agreement and what the buyer later spends.",
        sections=[
            ("Read the final settlement, not the listing price", ["An investor agrees to buy a warehouse for $3 million. Inspection finds roof damage, and the seller gives a $90,000 credit at closing. Before building the depreciation schedule, determine how the executed amendment and final settlement statement treat that credit. A price reduction generally reduces the buyer's cost basis. A reimbursement or other negotiated payment may raise different questions. The label on a preliminary worksheet should not decide the tax treatment.", "Reconcile the purchase agreement, amendments, escrow entries, loan funding, and seller's obligations. Allocate the resulting acquisition cost between land and depreciable property using defensible values; the roof and any future improvements should not simply be added to the building basis twice."]),
            ("Track the roof work separately", ["After closing, collect actual roofing invoices and determine the scope of work. A patch, a major replacement, and work that materially improves the property can receive different tax treatment. The seller's $90,000 estimate does not establish the amount or character of the buyer's eventual expenditure. If work is capitalized, document when the improvement is ready and available for its intended use.", "Also identify who was legally responsible for the repair and whether any escrow funds were restricted. Those documents can affect the analysis. Keep purchase accounting and post-closing capital projects as separate workstreams until the transactions are understood."]),
            ("Close with a basis schedule", ["AE can prepare a reconciliation from contract price to cash paid, assumed liabilities, qualifying closing costs, land allocation, building basis, and subsequent repair or improvement costs. Bring the signed purchase agreement, closing statement, inspection report, appraisals, escrow agreement, and invoices. Do this before ordering a cost segregation study or filing the first rental return."])
        ],
        sources=[("IRS Publication 551: Basis of Assets", "https://www.irs.gov/publications/p551"), ("IRS Publication 946: How To Depreciate Property", "https://www.irs.gov/publications/p946")],
        related=[("Real estate tax planning", "/real-estate-tax-planning/"), ("Cost segregation study", "/cost-segregation-study/")],
    ),
    dict(
        slug="short-term-rental-open-while-pool-unfinished-depreciation",
        title="STR Open While Pool Unfinished: Depreciation Dates",
        question="Can I start depreciating my short-term rental while the pool is unfinished?",
        description="STR taking guests before the pool is finished? Review separate placed-in-service dates for the rentable home, pool, furnishings, and site improvements.",
        audience="Real Estate Investors",
        subtitle="The rentable home and an unfinished pool may have different dates and basis schedules, depending on what is actually available to guests.",
        sections=[
            ("Establish when the home became available", ["An investor furnishes a vacation home, obtains required permits, publishes a listing, and accepts guests in September. The backyard pool is still under construction until November. Publication 946 generally treats property as placed in service when it is ready and available for its specific use. If the home really is available for rental in September, the unfinished pool does not automatically postpone the home's date. If construction makes the premises unsafe or unavailable, the facts point the other way.", "Save the dated listing, booking calendar, guest invoices, local permit, insurance coverage, inspection records, and photos showing what guests could use. A marketing screenshot without actual availability is a weaker file."]),
            ("Give each asset its own timeline", ["The pool, appliances, furniture, and land improvements are not one asset merely because they share a property address. Record acquisition cost, installation completion, and first availability for each material component. Do not place the pool in service based on the home's first reservation; document its inspection, filling, safety work, and when guests were allowed to use it.", "A cost segregation study can help classify eligible components, but it cannot create a date earlier than the evidence supports. The pool's classification and recovery period need a property-specific review, including how it is used and connected to the rental."]),
            ("Model the return before making elections", ["AE can reconcile the capital project ledger, rental start date, asset schedule, and guest use before calculating depreciation. Bring the closing statement, contractor invoices, property listing history, calendar, permits, and pool completion records. The tax model should also consider any personal use and the applicable passive activity rules rather than assuming a deduction offsets unrelated income."])
        ],
        sources=[("IRS Publication 946: How To Depreciate Property", "https://www.irs.gov/publications/p946"), ("IRS Publication 527: Residential Rental Property", "https://www.irs.gov/publications/p527")],
        related=[("STR year-end placed-in-service timeline", "/blog/str-placed-in-service-year-end-timeline/"), ("Short-term rental tax strategy", "/short-term-rental-tax-strategy/")],
    ),
]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def render(page: dict) -> str:
    slug, title, question, description = (page[k] for k in ("slug", "title", "question", "description"))
    url = f"{DOMAIN}/{slug}/"
    hub = "business-owner-tax-planning" if page["audience"] == "Business Owners" else "real-estate-tax-planning"
    meta = BASE[:BASE.index('<script type="application/ld+json">')]
    old_title = "1031 Exchange Into a New LLC: Same-Owner Tax Review"
    old_description = "Selling investment property and buying replacement property through a new LLC? Check federal taxpayer identity before signing the exchange documents."
    meta = meta.replace(old_title, esc(title)).replace(old_description, esc(description))
    meta = meta.replace("1031-exchange-replacement-property-new-llc-owner-review", slug)
    schema = {"@context": "https://schema.org", "@type": "Article", "headline": question,
              "description": description, "url": url, "datePublished": "2026-09-25",
              "dateModified": "2026-09-25", "articleSection": page["audience"],
              "author": {"@type": "Organization", "name": "AE Tax Advisors", "url": DOMAIN + "/"},
              "publisher": {"@type": "Organization", "name": "AE Tax Advisors", "logo": {"@type": "ImageObject", "url": DOMAIN + "/assets/ae-tax-logo.png"}},
              "mainEntityOfPage": {"@type": "WebPage", "@id": url},
              "citation": [u for _, u in page["sources"]]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"},
        {"@type": "ListItem", "position": 2, "name": page["audience"], "item": f"{DOMAIN}/{hub}/"},
        {"@type": "ListItem", "position": 3, "name": title, "item": url}]}
    meta += ''.join('<script type="application/ld+json">\n' + json.dumps(obj, indent=2) + '\n</script>\n' for obj in (schema, crumbs)) + "\n</head>\n"
    chrome = BASE[BASE.index("<body>"):BASE.index("    <main>")]
    main = f'''    <main>
    <section class="page-header"><div class="container narrow">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> &rsaquo; <a href="/{hub}/">{esc(page['audience'])}</a> &rsaquo; <span>{esc(title)}</span></nav>
      <h1>{esc(question)}</h1><p class="subtitle">{esc(page['subtitle'])}</p>
      <div class="cta-buttons"><a href="/discovery/" class="btn-cta btn-lg">Request a Tax Assessment</a></div>
    </div></section>
'''
    for heading, paragraphs in page["sections"]:
        main += f'    <section class="content-section fade-in-section"><div class="container narrow"><h2>{esc(heading)}</h2>\n'
        main += ''.join(f'      <p>{esc(p)}</p>\n' for p in paragraphs)
        main += '    </div></section>\n'
    for heading, links in (("Primary tax sources", page["sources"]), ("Related AE Tax guidance", page["related"])):
        main += f'    <section class="content-section fade-in-section"><div class="container narrow"><h2>{esc(heading)}</h2><ul class="related-links">\n'
        main += ''.join(f'      <li><a href="{esc(url)}">{esc(label)}</a></li>\n' for label, url in links)
        main += '    </ul></div></section>\n'
    main += '''    <section class="content-section fade-in-section" style="background:var(--light-bg);"><div class="container narrow center-text"><h2>Review Your Facts With AE</h2><p>Bring the transaction documents and dates to a discovery call. We can identify the tax questions, records, and next steps for your business or property.</p><div class="center-cta" style="margin-top:20px;"><a href="/discovery/" class="btn-cta btn-lg">Schedule Your Discovery Call</a></div></div></section>
    </main>
'''
    footer = BASE[BASE.index("<footer>"):]
    return meta + chrome + main + footer


def main() -> None:
    for page in PAGES:
        target = ROOT / page["slug"] / "index.html"
        if target.exists():
            raise RuntimeError(f"Refusing to overwrite {target}")
        target.parent.mkdir(parents=True)
        target.write_text(render(page), encoding="utf-8")
        print(target.relative_to(ROOT))


if __name__ == "__main__":
    main()
