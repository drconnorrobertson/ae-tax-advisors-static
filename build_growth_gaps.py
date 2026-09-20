#!/usr/bin/env python3
"""Build high-intent AE Tax service and decision pages.

These pages fill commercial search gaps around cost segregation, amended
business returns, and year-round advisory. Each topic has a distinct intent so
the pages support, rather than compete with, the site's primary service pages.
"""

from site_template import (
    article_schema,
    breadcrumb_schema,
    build_page,
    definition,
    faq_schema,
    faq_section,
    page_header,
    related_section,
    section,
    takeaways,
    write_page,
)

DATE = "2026-09-20"


PAGES = [
    {
        "slug": "cost-segregation-study-cost-pricing",
        "title": "Cost Segregation Study Cost and Pricing: What Business Owners Should Compare",
        "meta": "Understand cost segregation study pricing, what affects the fee, what a defensible study should include, and how to evaluate value before ordering a report.",
        "subtitle": "The cheapest report is not always the lowest-cost decision. Compare scope, engineering support, tax coordination, and usable deductions before comparing fees.",
        "definition": "Cost segregation study pricing depends on property type, size, records, improvement history, and the level of engineering and tax analysis required. A useful proposal should define the property and tax years covered, the deliverables, who prepares and reviews the work, how the study coordinates with the return, and what support is available if the classifications are questioned.",
        "sections": [
            ("What Drives the Price of a Cost Segregation Study", [
                "A single-family rental with a clean closing statement is a different engagement from a renovated hotel, manufacturing plant, medical building, or multi-property portfolio. Complexity rises when the property has multiple additions, incomplete fixed-asset records, tenant improvements, partial dispositions, or prior depreciation that must be reconciled.",
                "The number of assets is only part of the workload. A defensible study connects construction details and available documentation to tax recovery periods. That may require plans, invoices, photographs, appraisals, settlement records, and interviews about improvements. A provider quoting from purchase price alone may be estimating the tax result before understanding the building.",
            ]),
            ("What a Complete Proposal Should Include", [
                "The proposal should state whether the work is a full study, a lookback study, an update, or a limited analysis. It should identify the federal tax year, each property, the expected report format, the depreciation schedules delivered, and whether prior improvements or partial asset dispositions are included.",
                "Ask who will perform the engineering analysis, who will review the tax treatment, and who will coordinate Form 3115 or return implementation. A report that never reaches the depreciation schedule does not create a tax result. AE Tax Advisors treats the engineering report, tax modeling, and return position as connected workstreams, with final treatment dependent on the taxpayer's facts and preparer's review.",
            ]),
            ("How to Measure Value Instead of Chasing a Percentage", [
                "A projected reclassification percentage is not a guaranteed tax saving. The usable benefit depends on depreciable basis, placed-in-service date, bonus-depreciation rules, passive-loss limitations, basis and at-risk limits, state conformity, and the owner's tax rate. A large paper deduction can be temporarily unusable if the loss is suspended.",
                "Compare proposals using after-limit, after-state, after-fee value. A strong analysis shows the deduction with and without the study, identifies the rules that could delay use, and explains recapture and holding-period considerations. That is more decision-useful than a headline deduction alone.",
            ]),
            ("Questions to Ask Before You Sign", [
                "Confirm whether the fee changes if records are incomplete, whether a site visit or equivalent documentation review is included, and whether the provider will answer the tax preparer's implementation questions. Ask how land value, indirect costs, renovation costs, and disposed components are handled.",
                "Also ask what happens if the property is sold soon, converted to personal use, or held in an entity with limited basis. Cost segregation is a timing strategy, so exit assumptions belong in the analysis before the report is commissioned.",
            ]),
        ],
        "faqs": [
            ("Is cost segregation pricing based only on purchase price?", "No. Purchase price affects potential value, but fee and scope also depend on property type, records, renovations, asset count, prior depreciation, and whether a Form 3115 lookback is required."),
            ("Should I choose the provider with the highest projected reclassification?", "Not by itself. A projection should be supported by facts, and the deduction must survive passive-loss, basis, at-risk, state, and recapture analysis. Compare defensibility and usable tax value."),
            ("Does the study fee include filing Form 3115?", "Sometimes, but not always. The proposal should expressly state whether tax-return implementation, Form 3115 preparation, state adjustments, and preparer coordination are included."),
        ],
        "related": [("/cost-segregation-study/", "Cost Segregation Study Services"), ("/cost-segregation-calculator/", "Cost Segregation Calculator"), ("/form-3115-cost-segregation/", "Form 3115 Catch-Up Depreciation")],
    },
    {
        "slug": "cost-segregation-study-timeline-process",
        "title": "Cost Segregation Study Timeline: From Property Records to Tax Return",
        "meta": "See each step in the cost segregation process, the documents that prevent delays, and how the final report reaches Form 4562 or Form 3115.",
        "subtitle": "A study is complete only when the engineering analysis, depreciation schedule, tax elections, and return implementation agree.",
        "definition": "A cost segregation timeline normally has five phases: eligibility and tax modeling, document collection, engineering analysis, quality review, and tax-return implementation. Timing varies with property complexity and record quality, so owners should start before the filing deadline rather than treating the report as a last-minute attachment.",
        "sections": [
            ("Phase 1: Eligibility and Tax Modeling", ["The first step is not measuring the building. It is deciding whether accelerated depreciation is likely to be usable. The review should cover ownership, depreciable basis, placed-in-service date, current depreciation, entity basis, passive-activity status, expected holding period, and state treatment.", "This screen can prevent an owner from paying for a study that produces only suspended losses or an unattractive recapture profile. It also determines whether the project is a current-year study or a lookback requiring an accounting-method change."]),
            ("Phase 2: Documents and Property History", ["The strongest files include the closing statement, appraisal, inspection, existing depreciation schedule, improvement ledger, construction drawings when available, contractor invoices, and photographs. Renovated properties also need a timeline showing what was replaced and when each improvement was placed in service.", "Missing plans do not automatically end the project, but the provider needs reliable substitutes. Prompt answers about renovations and prior use prevent assumptions from becoming rework later."]),
            ("Phase 3: Engineering and Classification", ["The analyst identifies building systems and site improvements, develops cost support, and assigns tax recovery periods based on function and applicable authority. The work should distinguish structural building components from qualifying personal property and land improvements.", "For acquired buildings, cost estimates may be needed because the closing statement does not price every component. The methodology and source support belong in the report, not only in an internal worksheet."]),
            ("Phase 4: Tax Review and Implementation", ["The final asset schedule should reconcile to depreciable basis. The tax team then evaluates bonus depreciation, Section 179 where applicable, state adjustments, passive-loss treatment, and the correct return forms.", "For a lookback, Form 3115 and the Section 481(a) adjustment must tie to the study and the existing depreciation schedule. For a current-year acquisition, the new asset classes flow to Form 4562 and the entity or individual return."],),
            ("How to Prevent Filing-Deadline Delays", ["Start with a document checklist, name one person responsible for questions, and provide the prior depreciation schedule at the beginning. Tell the provider about additions, casualty losses, dispositions, personal use, and ownership changes before analysis begins.", "If the return deadline is close, discuss whether an extension is more appropriate than rushing an incomplete file. An extension is procedural; an unsupported classification can create a substantive problem."],),
        ],
        "faqs": [("How long does a cost segregation study take?", "Timing depends on property complexity, records, and provider capacity. A clean property may move quickly, while a renovated commercial asset or portfolio requires more document and review time."), ("Can a study be completed after the return is filed?", "Yes. Depending on the facts, missed depreciation may be addressed through Form 3115 in a later year rather than amending every prior year."), ("What causes the most delays?", "Missing depreciation schedules, unclear placed-in-service dates, undocumented renovations, incomplete closing records, and late answers to engineering questions are common causes.")],
        "related": [("/cost-segregation-documents-checklist/", "Cost Segregation Document Checklist"), ("/cost-segregation-study/", "Cost Segregation Study Services"), ("/form-3115-cost-segregation-lookback/", "Form 3115 Lookback Guide")],
    },
    {
        "slug": "cost-segregation-documents-checklist",
        "title": "Cost Segregation Documents Checklist for Rental and Commercial Property",
        "meta": "Use this cost segregation document checklist to gather closing, appraisal, improvement, depreciation, and property records before a study begins.",
        "subtitle": "Better records produce faster analysis, fewer assumptions, and a cleaner handoff to the tax return.",
        "definition": "The core cost segregation file consists of proof of basis, proof of placed-in-service date, an existing depreciation schedule, property details, and support for improvements. The exact list changes by property, but every study must reconcile the classified assets to the taxpayer's books and return.",
        "sections": [
            ("Acquisition and Basis Records", ["Provide the closing disclosure or settlement statement, purchase agreement, appraisal, allocation schedules, and documentation of acquisition costs. The appraisal can help separate land from building, but the tax allocation should be reviewed rather than copied automatically.", "If multiple parcels, buildings, furniture packages, or business assets were acquired together, include the allocation used on the books. Related-party transactions and contributions to an entity require additional basis history."]),
            ("Placed-in-Service and Use Records", ["Document when the property was ready and available for its intended use. For a rental, this may include the listing date, certificate of occupancy, first booking, lease, or management records. Closing date and placed-in-service date are not always the same.", "Identify personal-use periods, conversions from personal to rental use, and changes between short-term, long-term, and commercial use. These facts can affect recovery period and loss treatment."],),
            ("Construction and Improvement Support", ["Provide contractor invoices, draw schedules, architectural plans, specifications, change orders, permits, and photographs when available. A simple ledger that labels everything 'renovation' is not enough to distinguish repairs, improvements, building systems, and disposed components.", "For older work, bank records, insurance files, inspection reports, listing photos, and interviews may help reconstruct the scope. The report should disclose estimation methods and assumptions."],),
            ("Tax and Accounting Records", ["Include the current fixed-asset ledger, depreciation schedules for every year held, prior returns affecting the asset, and any Form 3115 previously filed. If ownership changed, provide contribution, distribution, sale, or inheritance records.", "The depreciation schedule is essential in a lookback. It shows what was already claimed and prevents a catch-up calculation from duplicating deductions."],),
            ("A Clean Handoff to the Tax Preparer", ["The final package should include the report, asset-level schedule, basis reconciliation, current-year depreciation, and any proposed Section 481(a) adjustment. State differences and elections should be identified separately.", "Keep the source documents with the report. The study explains the conclusion; the source file shows how the conclusion connects to the actual property."],),
        ],
        "faqs": [("Do I need original blueprints?", "No. Blueprints are helpful but not always available. Appraisals, inspections, photographs, invoices, and reliable cost-estimation methods may support the analysis."), ("Why does the provider need my depreciation schedule?", "It establishes what basis and depreciation were already reported, which is necessary to reconcile a new study and calculate any catch-up adjustment."), ("Can bank statements replace improvement invoices?", "They may help establish payment, but they often do not describe the asset or work well enough by themselves. Combine them with contracts, photos, permits, or other records.")],
        "related": [("/cost-segregation-study-timeline-process/", "Cost Segregation Timeline"), ("/cost-segregation-study/", "Cost Segregation Study Services"), ("/build-audit-proof-tax-documentation/", "Build Audit-Proof Documentation")],
    },
    {
        "slug": "cost-segregation-second-opinion",
        "title": "Cost Segregation Second Opinion: Review a Study Before Filing",
        "meta": "Get a cost segregation second opinion when classifications, land value, bonus depreciation, Form 3115, or tax-return implementation do not reconcile.",
        "subtitle": "A second opinion should test the report against the property, the depreciation schedule, and the tax return, not merely offer a different deduction estimate.",
        "definition": "A cost segregation second opinion is an independent review of an existing study and its planned tax treatment. It is useful when the asset classes do not reconcile to basis, assumptions are unclear, prior depreciation is missing, projected deductions appear unusually aggressive, or the tax preparer cannot implement the report as delivered.",
        "sections": [
            ("When a Review Is Worth Doing", ["Warning signs include unexplained land allocations, round-number classifications, missing methodology, duplicated improvements, negative basis, a Section 481(a) adjustment that does not tie to prior depreciation, or a report that assumes all accelerated depreciation is currently usable.", "A review can also be valuable before a large amended return, before filing Form 3115, or when a new preparer inherits a study they did not commission."],),
            ("What the Reviewer Should Reconcile", ["The classified assets must add to depreciable basis after land and other exclusions. The report's placed-in-service dates should match the facts, and the tax lives should flow to an asset schedule that the return can use.", "For lookbacks, allowed-or-allowable depreciation, depreciation actually claimed, and the proposed catch-up must reconcile. State depreciation and passive-loss treatment should not be inferred from a federal engineering schedule."],),
            ("Aggressive Is Not the Same as Defensible", ["Cost segregation applies tax classifications to real components. A higher reclassification percentage can be correct for one property and wrong for another. The question is whether the facts and authorities support the treatment.", "A good review separates computational errors, documentation gaps, reasonable judgment calls, and positions that should be changed. That gives the owner and preparer a usable action list instead of a vague risk label."],),
            ("Possible Outcomes", ["The original report may be ready to file, may need a schedule correction, may require added documentation, or may need a more substantial revision. Sometimes the engineering is sound but the tax implementation needs work; sometimes the reverse is true.", "The review should end with a basis reconciliation, identified issues, recommended changes, and clear responsibility for updating the report, depreciation schedule, Form 3115, and return."],),
        ],
        "faqs": [("Does a second opinion replace the original study?", "Not necessarily. It may validate the study, identify limited corrections, or recommend a replacement only when the original work cannot be supported."), ("Can a report be corrected before filing?", "Yes. Correcting classifications, basis, dates, or schedules before filing is generally simpler than fixing a return after the fact."), ("Should the tax preparer participate?", "Yes. The preparer should understand the conclusions and confirm how the revised schedules will be reported.")],
        "related": [("/cost-segregation-audit-defense/", "Cost Segregation Audit Defense"), ("/cost-segregation-study-cost-pricing/", "Cost Segregation Pricing"), ("/form-3115-cost-segregation/", "Form 3115 for Cost Segregation")],
    },
    {
        "slug": "cost-segregation-cpa-coordination",
        "title": "Cost Segregation and CPA Coordination: Getting the Study Onto the Return",
        "meta": "Learn how property owners, cost segregation analysts, and tax preparers coordinate basis, Form 3115, depreciation, state adjustments, and passive losses.",
        "subtitle": "The report, depreciation schedule, and return must tell the same story.",
        "definition": "Cost segregation coordination is the process of reconciling the engineering report to the taxpayer's books and tax return. It covers basis, placed-in-service dates, depreciation methods, Form 3115 when required, bonus elections, state conformity, and the limitations that determine whether the deduction is currently usable.",
        "sections": [
            ("Three Different Jobs, One Tax Position", ["The engineering team identifies and costs property components. The tax advisor models the consequences and elections. The return preparer reports the final classes, forms, adjustments, and disclosures. A project fails when one role assumes another completed the handoff.", "The owner should know who is responsible for every deliverable. 'Study completed' does not answer whether the asset ledger was updated or whether Form 3115 was prepared."],),
            ("The Reconciliation Package", ["At minimum, the preparer needs total basis, land allocation, asset classes, recovery periods, methods, conventions, placed-in-service dates, current depreciation, and prior depreciation for a lookback. The sum should tie to the fixed-asset ledger.", "If renovations or partial dispositions are included, those adjustments should be labeled so the preparer can avoid duplicate assets and depreciation."],),
            ("Tax Decisions the Engineering Report Does Not Make", ["An engineering report does not establish real-estate-professional status, material participation, basis availability, at-risk amount, Section 461(l) treatment, or whether a state conforms to federal bonus depreciation. Those are return-level questions.", "The advisor should also model the expected holding period and recapture. A technically correct acceleration schedule may still be a poor economic choice for an imminent sale."],),
            ("Questions for the Pre-Filing Review", ["Confirm that every new class appears on the depreciation schedule, the catch-up matches Form 3115, state addbacks are handled, and suspended losses are tracked. Verify names, EINs, property addresses, ownership percentages, and tax years.", "Keep the final signed return, depreciation schedule, Form 3115, study, and source documents together. Future preparers need the full chain, not only the PDF report."],),
        ],
        "faqs": [("Can my existing CPA use a third-party study?", "Yes. The CPA should receive a complete asset schedule and enough support to evaluate and implement the treatment."), ("Who prepares Form 3115?", "The engagement should specify responsibility. Some study providers include it, while others deliver only the engineering report and schedules."), ("Does cost segregation automatically make rental losses nonpassive?", "No. Passive-loss characterization depends on the activity and the taxpayer's participation, not on the study.")],
        "related": [("/cost-segregation-study/", "Cost Segregation Study Services"), ("/form-3115-cost-segregation-lookback/", "Form 3115 Lookback"), ("/passive-activity-loss-rules-real-estate/", "Passive Activity Loss Rules")],
    },
    {
        "slug": "cost-segregation-before-selling-property",
        "title": "Should You Do Cost Segregation Before Selling a Property?",
        "meta": "Evaluate cost segregation before a sale by comparing catch-up depreciation, suspended losses, Section 1245 recapture, holding period, and current tax rates.",
        "subtitle": "A late study can still create value, but the answer depends on timing, recapture, loss usability, and the structure of the sale.",
        "definition": "Cost segregation before a sale may recover depreciation that should have been claimed in prior years, often through Form 3115. The strategy must be modeled with depreciation recapture, passive-loss release, transaction timing, and current-year tax rates because accelerating a deduction shortly before disposition can also accelerate ordinary-income recapture.",
        "sections": [
            ("Why a Late Study Can Still Matter", ["Tax depreciation generally follows an allowed-or-allowable concept. Failing to claim the correct amount does not necessarily preserve basis forever. A lookback study may correct the method and claim a catch-up before the asset leaves the taxpayer's hands.", "That can be valuable when the deduction offsets high-rate ordinary income or when released passive losses create room to use the adjustment."],),
            ("The Recapture Tradeoff", ["Assets reclassified into shorter lives may generate Section 1245 ordinary-income recapture on sale to the extent of gain and prior depreciation. The benefit of an ordinary deduction followed quickly by ordinary recapture may be small unless rates, timing, state treatment, or loss interactions create value.", "The model should compare the no-study sale, the study with catch-up, and any sale allocation effects. Do not compare only the current deduction."],),
            ("Passive Losses and Complete Dispositions", ["A fully taxable disposition of an entire passive activity can release suspended passive losses, subject to the transaction facts. That can make the sale year different from prior years and may change how much of a catch-up is usable.", "Entity ownership, related-party sales, installment treatment, and partial dispositions can complicate the analysis. The advisor should review the actual transaction rather than assume every sale releases every loss."],),
            ("A Pre-Sale Decision Checklist", ["Estimate closing date and sales price, identify asset allocations, gather the depreciation schedule, quantify suspended losses, and model federal and state outcomes. Confirm whether the accounting-method change can be filed for the intended year.", "If the sale is imminent, coordinate the study provider, return preparer, and transaction advisor before documents are finalized. Purchase-price allocations signed at closing can affect both sides."],),
        ],
        "faqs": [("Can I file Form 3115 in the year I sell?", "Potentially, depending on the facts and procedural requirements. The filing and sale timeline should be reviewed before the return is prepared."), ("Does cost segregation always increase recapture?", "Reclassification can change the amount and character of recapture. The net result depends on gain, asset allocations, prior depreciation, and the holding period."), ("What if I have suspended passive losses?", "A qualifying disposition may release some suspended losses, which can materially change the model. Confirm the activity and transaction details with the preparer.")],
        "related": [("/form-3115-cost-segregation/", "Form 3115 Catch-Up"), ("/blog/depreciation-recapture-planning/", "Depreciation Recapture Planning"), ("/cost-segregation-study/", "Cost Segregation Study Services")],
    },
    {
        "slug": "cost-segregation-without-bonus-depreciation",
        "title": "Does Cost Segregation Work Without Bonus Depreciation?",
        "meta": "Cost segregation can still accelerate deductions without bonus depreciation. See how shorter MACRS lives, land improvements, QIP, and cash-flow timing create value.",
        "subtitle": "Bonus depreciation amplifies cost segregation, but it is not what makes the classifications valid or useful.",
        "definition": "Cost segregation works without bonus depreciation because it moves eligible components from 27.5-year or 39-year building depreciation into shorter 5-year, 7-year, or 15-year recovery periods. Even when first-year bonus is unavailable or elected out, the shorter schedules generally accelerate deductions and can identify separately disposed assets.",
        "sections": [
            ("Classification Comes Before the Election", ["A cost segregation study determines what the property is for tax purposes. Bonus depreciation is a separate rule applied after class life is assigned. A five-year asset remains five-year property even if the taxpayer elects out of bonus.", "That distinction matters for annual depreciation, disposition, repairs, and future elections. The study is an asset-accounting tool, not only a first-year deduction tool."],),
            ("When Bonus May Be Unavailable", ["Bonus depreciation may be unavailable for certain property, related-party acquisitions, listed property that fails business-use requirements, or property required to use the alternative depreciation system. State law may also decouple from the federal rule.", "The exact result depends on the placed-in-service year and elections. The advisor should model federal and state schedules separately."],),
            ("Why Shorter Lives Still Create Cash-Flow Value", ["A deduction received earlier can fund operations, debt reduction, or additional investment. The present value depends on marginal rates and the number of years accelerated, not solely on whether the entire amount is deducted immediately.", "For investors expecting higher future rates or a near-term sale, full bonus may not be optimal. Regular MACRS on shorter classes can create a smoother deduction pattern."],),
            ("Other Benefits of Asset-Level Records", ["Separating components makes it easier to identify assets removed during renovations and evaluate partial dispositions. It also gives future preparers a clearer basis trail than a single building line.", "The study can support repair-versus-capitalization analysis and help distinguish land improvements, personal property, qualified improvement property, and structural components."],),
        ],
        "faqs": [("Is a study useless if my state disallows bonus depreciation?", "No. The state may still recognize shorter recovery periods even when it requires a federal bonus addback, and federal benefits may remain available."), ("Can I elect out of bonus depreciation?", "Taxpayers may make elections by property class under applicable rules. The decision should consider rates, losses, QBI, state treatment, and expected sale timing."), ("Does cost segregation create new deductions?", "It generally changes timing and classification of depreciation. The economic value comes from receiving supported deductions earlier and maintaining better asset records.")],
        "related": [("/bonus-depreciation-rental-property/", "Bonus Depreciation for Rental Property"), ("/macrs-depreciation-schedule-2026/", "MACRS Depreciation Schedules"), ("/cost-segregation-study/", "Cost Segregation Study Services")],
    },
    {
        "slug": "amended-business-tax-return-services",
        "title": "Amended Business Tax Return Services for S Corporations, Partnerships, and C Corporations",
        "meta": "Correct prior business returns after bookkeeping errors, missed deductions, basis problems, entity reporting issues, or new tax documents are discovered.",
        "subtitle": "A business amendment should begin with corrected books and a year-to-year reconciliation, not with changing isolated lines on a return.",
        "definition": "An amended business tax return corrects a previously filed entity return when the underlying income, deductions, allocations, elections, or disclosures were wrong or incomplete. The work may involve Form 1120-S, Form 1065, Form 1120, related state returns, shareholder or partner basis, and corrected Schedules K-1.",
        "sections": [
            ("When a Business Return May Need Correction", ["Common triggers include incomplete books, duplicated income, personal expenses recorded as business costs, missed fixed assets, omitted payroll or contractor reporting, incorrect owner allocations, and tax documents received after filing.", "A strategic review may also find accountable-plan reimbursements, home-office treatment, retirement contributions, depreciation, or entity issues that were not reflected correctly. Not every missed opportunity can be retroactively created, so eligibility and documentation must be tested year by year."],),
            ("Correct the Books Before Correcting the Return", ["The amended return should tie to a final adjusted trial balance, profit and loss statement, balance sheet, and fixed-asset ledger. If the books remain wrong, the amendment becomes a one-off patch that creates a new difference for the next year.", "Reconcile opening and ending equity, loans, distributions, capital accounts, retained earnings, payroll, and depreciation. The correction should roll forward into the current books so future returns start from the amended position."],),
            ("Owner-Level Consequences", ["An entity amendment often changes Schedules K-1 and therefore the owners' individual or trust returns. It may also change stock or debt basis, partnership capital, passive-loss limitations, QBI, self-employment income, state-source income, and estimated-tax carryovers.", "The engagement should identify every affected return before filing. Correcting the entity without addressing the owners can leave the filing set inconsistent."],),
            ("A Controlled Amendment Process", ["AE Tax Advisors begins with the original returns, source documents, and corrected books. The team prepares a change schedule showing the original amount, corrected amount, reason, tax impact, and supporting evidence.", "After client and preparer review, the entity amendment, corrected K-1s, owner amendments, and applicable state filings are sequenced. Fees and recommendations depend on scope, complexity, and expected value."],),
        ],
        "faqs": [("Can an amended business return change my personal return?", "Yes. Changes to a K-1, wages, basis, or pass-through deductions can require owner-level amendments."), ("Should I amend before the bookkeeping cleanup is final?", "Usually no. Final corrected books and reconciliations should support the amended figures."), ("Can every missed tax strategy be added retroactively?", "No. Some deductions require timely elections, contemporaneous records, payroll, plan adoption, or actual payment. Each item must be tested under its own rules.")],
        "related": [("/amended-tax-returns/", "Amended Tax Returns"), ("/3-year-tax-lookback-cleanup/", "Three-Year Tax Lookback"), ("/amend-tax-return-after-bookkeeping-cleanup/", "Amending After Bookkeeping Cleanup")],
    },
    {
        "slug": "amend-s-corporation-tax-return",
        "title": "How to Amend an S Corporation Tax Return and Correct Shareholder Basis",
        "meta": "Learn what must be reconciled when amending Form 1120-S, including books, payroll, distributions, shareholder basis, K-1s, QBI, and state returns.",
        "subtitle": "An S corporation amendment can change both the entity filing and every shareholder return connected to it.",
        "definition": "An S corporation generally amends its federal return by filing a corrected Form 1120-S with the required amendment indication and explanation, along with corrected schedules and K-1s. The exact filing method and affected owner returns depend on the year, software, changes, and IRS procedures then in effect.",
        "sections": [
            ("Start With the Corporate Books", ["Reconcile gross receipts, expenses, payroll, officer compensation, fixed assets, loans, distributions, and equity. The ending balance sheet should roll into the next year's beginning balances.", "If the amendment changes retained earnings but the current books were never adjusted, later returns can repeat the original error. Post the final tax adjustments back to the accounting file."],),
            ("Shareholder Basis and Distribution Risk", ["Loss deductions and tax-free distributions depend on shareholder stock and debt basis. An amendment that changes income, loss, contributions, repayments, or distributions can change basis for multiple years.", "A distribution exceeding basis may create gain, while a previously suspended loss may become deductible or may need to be restored. Basis schedules should be rebuilt through every affected year rather than estimated from the latest K-1."],),
            ("Payroll, Reasonable Compensation, and Reimbursements", ["Do not convert distributions to wages on paper without evaluating payroll filings and payment history. Corrections can affect Forms 941, W-2, state payroll, penalties, and the shareholder's individual return.", "Accountable-plan reimbursements require a valid plan process, business connection, substantiation, and return of excess advances. A bookkeeping reclassification alone does not cure missing facts."],),
            ("Corrected K-1s and Owner Returns", ["Each affected shareholder receives a corrected Schedule K-1. The owner may need to amend federal and state individual returns, QBI calculations, passive-loss schedules, net investment income tax, and estimated-tax carryovers.", "Sequence matters when several years are involved. Finish the earliest year first so basis and carryovers flow correctly into later amendments."],),
        ],
        "faqs": [("Does an amended 1120-S require corrected K-1s?", "If shareholder items change, corrected K-1s are generally part of the amendment and may require owner-level action."), ("Can I add officer wages through an amended return?", "Wage corrections may require payroll filings and actual payment analysis, not only an income-tax amendment."), ("How far back should shareholder basis be rebuilt?", "Far enough to support the opening basis for the first affected year, which may require records from formation or acquisition.")],
        "related": [("/amended-business-tax-return-services/", "Amended Business Returns"), ("/blog/shareholder-basis-tracking-s-corp-essentials/", "S Corporation Shareholder Basis"), ("/reasonable-compensation-s-corp-irs/", "Reasonable Compensation")],
    },
    {
        "slug": "amend-partnership-tax-return",
        "title": "How to Correct a Partnership Tax Return, K-1s, and Partner Capital",
        "meta": "Understand partnership return corrections, amended returns versus administrative adjustment requests, corrected K-1s, capital accounts, basis, and allocations.",
        "subtitle": "Partnership corrections are procedural as well as computational. The correct path depends on the partnership and filing year.",
        "definition": "Correcting a partnership return may involve an amended Form 1065 or an administrative adjustment request under the centralized partnership audit regime. The correct procedure depends on the partnership's status, elections, year, and IRS rules, and it can affect how changes reach the partners.",
        "sections": [
            ("Determine the Correct Procedure First", ["Partnerships subject to the centralized audit regime generally cannot assume that a traditional amended return and corrected K-1s are available. Eligibility to elect out, the number and type of partners, and the reviewed year matter.", "Choose the procedural path before calculating owner refunds. An administrative adjustment may be taken into account differently from a direct amendment."],),
            ("Reconcile Capital and Tax Basis", ["Tax-basis capital on Schedule K-1 is not the same as outside basis. The partnership maintains capital information, while each partner must consider contributions, distributions, allocated liabilities, income, loss, and transfers to determine outside basis.", "Corrections to debt allocations, guaranteed payments, contributions, or distributions can affect loss deductibility and gain recognition across several years."],),
            ("Revisit Allocations and the Agreement", ["Special allocations must be supported by the partnership agreement and applicable tax rules. A bookkeeping percentage that differs from the legal allocation can create both tax and governance issues.", "Review ownership changes, admission and redemption dates, Section 704(c) layers, and Section 754 elections where relevant. Do not rewrite allocations solely to reach a preferred tax result."],),
            ("Partner-Level Follow-Through", ["The correction can affect individual, corporate, trust, or tax-exempt partners differently. State composite returns, withholding, credits, passive losses, self-employment tax, and QBI may all change.", "Prepare a partner impact schedule before filing so each owner understands the amount, year, documents, and next action."],),
        ],
        "faqs": [("Can every partnership file an amended Form 1065?", "No. Partnerships subject to the centralized audit regime may need an administrative adjustment request unless an exception applies."), ("Is K-1 capital the same as partner basis?", "No. Outside basis includes partner-specific items such as allocated liabilities and must be maintained separately."), ("Can allocations be changed after year end?", "Allocation changes must be consistent with the agreement and tax law. A retroactive bookkeeping change alone may not be respected.")],
        "related": [("/amended-business-tax-return-services/", "Amended Business Returns"), ("/blog/partnership-debt-basis-recourse-nonrecourse/", "Partnership Debt Basis"), ("/advanced-tax-planning-services/", "Advanced Tax Planning")],
    },
    {
        "slug": "amend-c-corporation-tax-return",
        "title": "How to Amend a C Corporation Tax Return and Reconcile Retained Earnings",
        "meta": "Correct Form 1120 after revenue, expense, fixed-asset, shareholder-loan, credit, NOL, or retained-earnings errors are found.",
        "subtitle": "A C corporation amendment should reconcile tax changes to the balance sheet, retained earnings, shareholder accounts, and future-year carryovers.",
        "definition": "A C corporation generally corrects a previously filed federal income-tax return using Form 1120-X, with supporting schedules and explanations. Related state returns, net operating losses, credits, estimated-tax applications, and shareholder transactions may also need correction.",
        "sections": [
            ("Build the Corrected Tax Workpapers", ["Start with an adjusted trial balance and a line-by-line comparison to the filed return. Reconcile revenue, cost of goods sold, compensation, benefits, fixed assets, interest, taxes, and other deductions.", "The explanation should identify the factual reason for each change and point to support. A net change without the underlying schedule is difficult to review and difficult to carry forward."],),
            ("Retained Earnings and Balance-Sheet Continuity", ["Tax adjustments can change retained earnings and other balance-sheet accounts. Those changes must flow into the next year's opening balances and Schedule L.", "Differences between book income and taxable income also affect Schedule M-1 or M-3. Correcting tax without correcting the books can leave an unexplained permanent difference."],),
            ("Shareholder Loans, Compensation, and Distributions", ["Review whether payments recorded as loans have notes, repayment terms, interest, and actual repayment behavior. A label in QuickBooks does not determine tax treatment.", "Corrections involving officer compensation, dividends, redemptions, or fringe benefits may affect payroll, information reporting, and shareholder returns. Coordinate all affected filings."],),
            ("Carryovers and Future Returns", ["An amendment may change NOLs, general business credits, charitable-contribution carryovers, capital losses, depreciation, and estimated-tax applications. Update the carryover workpapers and every open later year.", "When a correction creates an overpayment, confirm the available refund or credit procedure and limitation period before assuming the amount is recoverable."],),
        ],
        "faqs": [("What form is used to amend a C corporation return?", "Form 1120-X is generally used for federal C corporation income-tax corrections, with schedules explaining each adjustment."), ("Does an amended 1120 affect the shareholder's return?", "It can when compensation, dividends, redemptions, loans, or benefits change."), ("Should retained earnings change?", "Often yes when book or tax items change. The corrected balance sheet must roll forward consistently.")],
        "related": [("/amended-business-tax-return-services/", "Amended Business Returns"), ("/c-corporation-strategy/advanced-c-corporation-tax-planning/", "C Corporation Tax Planning"), ("/blog/c-corporation-shareholder-loan-tax-rules/", "C Corporation Shareholder Loans")],
    },
    {
        "slug": "amend-tax-return-after-bookkeeping-cleanup",
        "title": "Amending a Tax Return After Bookkeeping Cleanup: A Business Owner's Process",
        "meta": "Learn how corrected books flow into amended entity and owner returns, including reconciliations, fixed assets, equity, basis, K-1s, and state filings.",
        "subtitle": "Clean books are the evidence and operating record behind a defensible amendment.",
        "definition": "A bookkeeping-driven amendment begins when corrected financial records reveal that the filed return does not match the business's actual transactions. The process should produce final financial statements, a tax change schedule, updated basis and depreciation records, and a consistent filing set for the entity and owners.",
        "sections": [
            ("Freeze the Period and Preserve the Original", ["Keep a copy of the books exactly as they existed when the original return was prepared. Make corrections in a controlled copy or through dated adjusting entries with descriptions and support.", "This creates an audit trail and allows the team to explain why the filed numbers changed. Overwriting historical transactions without a change log makes review harder."],),
            ("Reconcile the Core Accounts", ["Tie bank and credit-card accounts, payroll, merchant processors, loans, owner contributions and distributions, accounts receivable, accounts payable, inventory, and fixed assets. Investigate suspense and uncategorized accounts rather than moving them to a generic expense.", "Reconcile the balance sheet as carefully as the profit and loss statement. Basis, equity, debt, and depreciation errors often live there."],),
            ("Separate Corrections From New Planning", ["Some cleanup items correct facts that existed in the filed year. Other ideas are future planning that required timely action, a written plan, payment, payroll, or contemporaneous substantiation.", "Label each proposed item as a factual correction, accounting-method issue, election issue, documentation issue, or future strategy. This prevents a valid cleanup project from becoming an unsupported retroactive wish list."],),
            ("Create the Amendment Map", ["For each adjustment, show the book entry, tax-return line, federal impact, state impact, owner impact, evidence, and next-year rollforward. Then determine which entity returns, K-1s, individual returns, payroll forms, and state filings are affected.", "File in chronological order when basis or carryovers connect the years. Update current books and tax workpapers after the filings are accepted."],),
        ],
        "faqs": [("Can I amend based on a new profit and loss statement alone?", "A P&L is a starting point. The return should also reconcile balance-sheet, fixed-asset, equity, and owner-level effects."), ("Can bookkeeping cleanup add deductions I never documented?", "Not automatically. Deductions still require legal eligibility and appropriate substantiation."), ("Should I change the current books after amending?", "Yes. The final corrections and tax adjustments should roll forward so later periods begin with accurate balances.")],
        "related": [("/amended-business-tax-return-services/", "Amended Business Return Services"), ("/3-year-tax-lookback-cleanup/", "Three-Year Lookback"), ("/build-audit-proof-recordkeeping-system/", "Audit-Proof Recordkeeping")],
    },
    {
        "slug": "business-tax-return-lookback-review",
        "title": "Business Tax Return Lookback Review: What to Check Before Amending",
        "meta": "Review up to three prior filing years for bookkeeping errors, missed deductions, basis problems, depreciation, entity issues, and amendment opportunities.",
        "subtitle": "A lookback should quantify recoverable value, filing cost, documentation quality, and future corrections before recommending amendments.",
        "definition": "A business tax return lookback is a structured review of prior returns, financial statements, books, and owner records to identify errors, missed opportunities, and carryover problems. It is an assessment first; amendments are recommended only when the legal and economic case is supported.",
        "sections": [
            ("The Documents to Review Together", ["The review should compare entity and owner returns with profit and loss statements, balance sheets, general ledgers, payroll reports, fixed-asset schedules, loan statements, formation documents, and prior-year workpapers.", "Looking at the return alone can reveal inconsistencies, but it cannot prove whether the books or the return are correct."],),
            ("High-Value Review Areas", ["Review depreciation and placed-in-service dates, owner basis, distributions, loans, payroll, accountable-plan reimbursements, home-office treatment, retirement plans, state filings, QBI, passive losses, credits, and entity elections.", "For real estate, include land allocation, cost segregation, Form 3115, material participation, and disposition history. For operating businesses, focus on revenue completeness, cost classification, compensation, benefits, and multi-entity transactions."],),
            ("Score Each Finding Before Filing", ["Classify findings by expected tax impact, documentation strength, procedural availability, filing deadline, professional fees, and effect on future years. Some corrections reduce tax, some increase it, and some mainly repair basis or carryovers.", "A credible review includes unfavorable findings too. The goal is an accurate and optimized filing position, not a predetermined refund."],),
            ("Deliverables From a Useful Lookback", ["The owner should receive a findings schedule, estimated federal and state impact, missing-document list, recommended amendments, future-year corrections, and items that are not supportable.", "The plan should identify which professionals own bookkeeping, payroll, entity, engineering, and tax-return tasks, with an order of operations."],),
        ],
        "faqs": [("Does a lookback guarantee a refund?", "No. It may find savings, additional tax, basis corrections, carryover changes, or no amendment worth filing."), ("Why review the owner return too?", "Pass-through income, K-1s, basis, passive losses, QBI, and credits often change the owner return."), ("Is three years always the deadline?", "No. Refund and assessment periods vary by filing, payment, issue, and jurisdiction. Confirm the applicable statute for each return.")],
        "related": [("/3-year-tax-lookback-cleanup/", "Three-Year Tax Lookback"), ("/amended-tax-returns/", "Amended Tax Returns"), ("/amended-business-tax-return-services/", "Amended Business Returns")],
    },
    {
        "slug": "amended-return-vs-form-3115",
        "title": "Amended Return vs. Form 3115: How to Correct Prior-Year Tax Treatment",
        "meta": "Compare amended returns and Form 3115 for depreciation, accounting-method, timing, and factual errors. Learn why the correction route depends on the issue.",
        "subtitle": "The correct filing depends on whether you are fixing a return error or changing an accounting method.",
        "definition": "An amended return corrects a previously filed return for that year. Form 3115 requests or reports a change in accounting method and can include a Section 481(a) adjustment that brings prior cumulative differences into the current year. The two procedures are not interchangeable.",
        "sections": [
            ("When an Amended Return Is the Natural Starting Point", ["Amendments commonly address omitted income, incorrect deductions, wrong filing status, corrected tax documents, or factual errors specific to a year. Entity changes can also require corrected K-1s and owner amendments.", "The applicable limitation period, filing method, state procedure, and effect on later years must be reviewed."],),
            ("When Form 3115 Enters the Analysis", ["Form 3115 applies to accounting-method changes, including many depreciation-method corrections after an impermissible method has been adopted. A negative Section 481(a) adjustment may catch up previously missed deductions in the year of change.", "The procedural rules are detailed. Eligibility, designated change number, automatic-change requirements, filing copies, and timing should be confirmed for the year filed."],),
            ("Why Depreciation Corrections Are Often Misclassified", ["Buying an asset but omitting it from one return may be a different issue from consistently depreciating a building under an impermissible method for several years. The number of years and pattern of treatment matter.", "A cost segregation lookback frequently uses Form 3115 because the taxpayer is changing the method or recovery treatment of existing assets, but not every asset error belongs there."],),
            ("A Decision Framework", ["Identify the original facts, the treatment used, how many returns used it, the correct treatment, cumulative difference, affected entities, and procedural deadline. Then determine whether the issue is an error, election, method change, or late filing.", "Document the conclusion. The return should show not only the preferred tax result but why the chosen correction procedure applies."],),
        ],
        "faqs": [("Can Form 3115 replace every amended return?", "No. It applies to qualifying accounting-method changes, not every factual or computational error."), ("Can Form 3115 recover missed depreciation?", "It can in many method-change situations through a Section 481(a) adjustment, subject to the applicable procedures."), ("Do states follow the federal adjustment?", "State conformity varies. Review the state treatment and any separate filing requirement.")],
        "related": [("/form-3115-cost-segregation/", "Form 3115 Cost Segregation"), ("/amended-tax-returns/", "Amended Tax Returns"), ("/business-tax-return-lookback-review/", "Business Return Lookback Review")],
    },
    {
        "slug": "business-tax-advisor-vs-cpa",
        "title": "Business Tax Advisor vs. CPA: What a Growing Company Actually Needs",
        "meta": "Compare tax preparation, proactive tax advisory, bookkeeping, controllership, and legal work so business owners know which professional should own each decision.",
        "subtitle": "A credential describes professional authority. An advisory engagement describes the work, cadence, and responsibility your company receives.",
        "definition": "A CPA may provide tax preparation, assurance, accounting, consulting, or advisory services, while a business tax advisor focuses on planning decisions and implementation across the year. The roles can overlap, but owners should evaluate scope, experience, review process, and accountability rather than assume a title guarantees a particular service model.",
        "sections": [
            ("Tax Preparation and Tax Advisory Solve Different Problems", ["Preparation reports what already happened. Advisory models choices before deadlines: entity structure, compensation, retirement plans, depreciation, transactions, estimated taxes, and documentation systems.", "A firm can do both, but the engagement should say who monitors implementation and when reviews occur. An annual return meeting is not automatically year-round planning."],),
            ("The Four Roles Around a Growing Business", ["Bookkeeping records transactions, controllership closes and reconciles the books, tax preparation files returns, and advisory evaluates decisions. Legal counsel handles contracts, governance, and legal opinions. No single professional should silently be assumed to own all five.", "AE Tax Advisors coordinates tax planning and filing work within its engagement scope and works with the client's accounting and legal professionals when a decision crosses disciplines."],),
            ("Questions That Reveal the Service Model", ["Ask how often the advisor reviews actual results, who maintains the planning calendar, how recommendations are documented, whether federal and state effects are modeled, and who verifies implementation.", "Ask what is excluded. Payroll filings, legal drafting, valuation, bookkeeping cleanup, engineering studies, and investment advice may be separate services or require another specialist."],),
            ("When to Upgrade From Return-Only Service", ["Businesses with changing profit, multiple entities, real estate, owner payroll, significant equipment, multi-state activity, a planned sale, or recurring surprises at filing time usually need more than annual compliance.", "The economic test is whether decisions are material enough that earlier modeling can improve cash flow, reduce error, or prevent a missed deadline. Complexity matters as much as revenue."],),
        ],
        "faqs": [("Is every CPA a tax advisor?", "No. CPAs work in many specialties, and tax engagements vary. Confirm the actual planning scope and cadence."), ("Can a tax advisor prepare returns?", "Some firms provide both advisory and preparation through appropriately qualified professionals; others coordinate with the client's preparer."), ("Do I still need a bookkeeper?", "Usually. Reliable advisory depends on timely, reconciled books, and bookkeeping is a distinct ongoing function.")],
        "related": [("/best-tax-advisor-for-business-owners/", "Best Tax Advisor for Business Owners"), ("/year-round-business-tax-planning/", "Year-Round Business Tax Planning"), ("/proactive-tax-planning-vs-tax-preparation/", "Planning vs. Preparation")],
    },
    {
        "slug": "year-round-business-tax-planning",
        "title": "Year-Round Business Tax Planning for Companies With $250K to $5M in Profit",
        "meta": "A quarterly tax planning system for profitable businesses covering forecasts, entity structure, owner pay, retirement, depreciation, estimated taxes, and year-end execution.",
        "subtitle": "The best planning window is while the owner can still change facts, execute documents, make payments, and preserve evidence.",
        "definition": "Year-round business tax planning is a recurring process that combines current financials, a full-year forecast, owner goals, entity and payroll data, and an implementation calendar. It turns tax planning from a filing-season reaction into a set of documented decisions made before deadlines.",
        "sections": [
            ("Quarter 1: Close the Prior Year and Set the Baseline", ["Finalize books, resolve prior-year open items, update basis and fixed assets, and review the completed return for carryovers and recurring issues. Build a current-year forecast by entity and owner.", "Set estimated-tax assumptions and identify decisions with long lead times, such as retirement plans, entity changes, or acquisitions."],),
            ("Quarter 2: Test Structure and Cash Flow", ["Compare actual results with forecast. Review owner compensation, distributions, intercompany activity, state exposure, retirement contributions, and capital spending.", "If profit is moving materially, update estimates and planning capacity. Do not wait until December to discover that the original forecast was wrong."],),
            ("Quarter 3: Choose and Start Implementation", ["Model the strategies that require documents, payroll, financing, appraisals, engineering, or third-party administration. Assign owners and deadlines.", "This is often the last comfortable window for cost segregation, retirement-plan design, entity cleanup, accountable-plan systems, and transaction planning."],),
            ("Quarter 4: Execute, Verify, and Preserve Evidence", ["Confirm payments, payroll, elections, contributions, placed-in-service dates, reimbursements, minutes, and supporting records. Run a final projection before the books close.", "Create the tax-preparation package while the facts are fresh. A strategy is not complete until the books and return workpapers reflect it."],),
            ("What Changes as Profit Approaches $5 Million", ["Higher profit increases the cost of weak forecasting and may add multi-entity, state, retirement, transaction, credit, and cash-management complexity. It also increases the value of coordination between tax, legal, investment, and operating teams.", "AE Tax Advisors is designed for profitable owner-led businesses that need proactive modeling and implementation discipline, with scope tailored to the actual entities and issues."],),
        ],
        "faqs": [("How often should a profitable business review taxes?", "Quarterly is a practical minimum for many growing businesses, with additional reviews around major transactions or large forecast changes."), ("What financials are needed?", "Current reconciled profit and loss, balance sheet, payroll, fixed assets, debt, owner activity, and a credible year-end forecast."), ("Does planning replace tax preparation?", "No. Planning informs decisions; preparation reports the completed facts and elections on the returns.")],
        "related": [("/tax-advisor-for-businesses-under-5-million-profit/", "Tax Advisor for Businesses Under $5M Profit"), ("/best-tax-advisor-for-business-owners/", "Best Tax Advisor for Business Owners"), ("/business-tax-advisor-vs-cpa/", "Tax Advisor vs. CPA")],
    },
    {
        "slug": "tax-advisor-for-businesses-under-5-million-profit",
        "title": "Tax Advisor for Businesses With $250,000 to $5 Million in Annual Profit",
        "meta": "Proactive tax advisory for profitable owner-led businesses needing entity, compensation, retirement, depreciation, multi-state, and transaction planning.",
        "subtitle": "At this profit range, the tax return is the output. The real work is coordinating decisions before the year closes.",
        "definition": "Businesses earning roughly $250,000 to $5 million in annual profit often need a tax advisory system beyond annual compliance. The right scope usually combines forecasting, entity and owner-pay review, estimated taxes, retirement and benefit planning, depreciation, transaction support, and implementation follow-through.",
        "sections": [
            ("Why This Profit Range Needs a Different Service Model", ["The business is large enough that compensation, entity structure, timing, retirement plans, equipment, real estate, and state footprint can materially affect tax. It is also often still owner-led, so personal cash needs and business decisions are tightly connected.", "A generic checklist is not enough. Recommendations should be ranked by net benefit, implementation effort, risk, cash cost, and fit with the owner's operating plan."],),
            ("The Core Advisory Work", ["A complete engagement begins with clean financials and a full-year forecast. It then reviews entity structure, owner wages and distributions, basis, QBI, benefits, retirement, depreciation, credits, multi-state obligations, and estimated taxes.", "For real-estate owners, add passive-loss modeling, cost segregation, Form 3115, material participation, and disposition planning. For acquisitive businesses, add purchase allocations, debt, integration, and exit assumptions."],),
            ("What AE Tax Advisors Does Not Pretend to Replace", ["Tax planning does not replace legal advice, investment advice, daily bookkeeping, payroll processing, engineering, valuation, or benefits administration. Those functions may be coordinated, but their professional boundaries should remain clear.", "The engagement should state who owns each implementation item and what evidence must be retained. Clarity is part of the value."],),
            ("How to Evaluate the Return on Advisory", ["Measure avoided surprises, improved decision timing, supported deductions, reduced penalties, cash-flow visibility, corrected carryovers, and implementation completion. Do not measure quality only by the largest projected tax saving.", "A recommendation that requires spending a dollar to save thirty cents may still be good if the purchase is needed, but it is not free money. AE Tax Advisors compares tax outcomes with business economics."],),
            ("When the Fit Is Strongest", ["The strongest fit is a profitable owner who wants proactive quarterly decisions, has reliable records or will improve them, and is willing to execute documented recommendations. Multiple entities, real estate, a large prior-year issue, a planned sale, or rapid growth make coordination more valuable.", "The discovery process should confirm scope and expected value before either side commits."],),
        ],
        "faqs": [("Is there a minimum profit level for proactive advisory?", "Complexity and opportunity matter, but businesses above roughly $250,000 of profit often have enough recurring decisions to justify a structured review."), ("Can AE Tax Advisors work with my existing bookkeeper or attorney?", "Yes. Clear coordination with existing professionals is often the best model."), ("Do you help businesses above $5 million?", "Potentially, depending on complexity and scope. This page focuses on the owner-led market where the service model is most consistent.")],
        "related": [("/year-round-business-tax-planning/", "Year-Round Tax Planning"), ("/advanced-tax-planning-services/", "Advanced Tax Planning Services"), ("/discovery/", "Request a Consultation")],
    },
    {
        "slug": "business-tax-second-opinion",
        "title": "Business Tax Second Opinion: Review Your Entity, Return, and Tax Plan",
        "meta": "Get an independent business tax second opinion on prior returns, entity structure, owner compensation, basis, depreciation, and proposed tax strategies.",
        "subtitle": "A second opinion should identify what is correct, what is missing, what is unsupported, and what action is worth taking.",
        "definition": "A business tax second opinion is an independent review of a filed return or proposed tax plan using the underlying books, entity records, owner facts, and supporting documents. It is most useful before a major amendment, entity change, transaction, or expensive strategy implementation.",
        "sections": [
            ("What to Bring", ["Provide the relevant federal and state returns, depreciation schedules, K-1s, profit and loss statements, balance sheets, payroll, ownership records, and the written plan or concern. Include prior-year information when basis and carryovers matter.", "A reviewer cannot validate a position from a summary slide alone. The source records determine whether the recommendation fits the actual taxpayer."],),
            ("What the Review Should Test", ["The review should test arithmetic, return-to-books reconciliation, basis, compensation, entity classification, elections, depreciation, state treatment, passive losses, and implementation requirements.", "For a proposed strategy, test cash cost, legal steps, deadlines, audit support, exit consequences, and whether the benefit is permanent or only deferred."],),
            ("A Useful Findings Report", ["Findings should be grouped into confirmed, needs support, should be corrected, future planning, and not recommended. Quantify tax impact where the data supports it and identify missing facts where it does not.", "The report should not manufacture disagreement. Valid work should be recognized so the owner knows what can remain unchanged."],),
            ("When a Second Opinion Is Especially Valuable", ["Consider one before filing a large refund claim, changing entity type, adopting an unusual structure, buying or selling a business, claiming a large depreciation adjustment, or replacing a long-term preparer.", "It is also useful when the owner receives conflicting advice and needs the assumptions placed side by side."],),
        ],
        "faqs": [("Will a second opinion automatically recommend amendments?", "No. It may validate the current treatment, identify future changes, or conclude that an amendment is not worth the cost."), ("Can you review only one issue?", "Yes. A targeted scope can focus on depreciation, basis, entity structure, or another defined question."), ("Should my current CPA see the findings?", "Usually. Coordinating corrections with the current preparer can reduce duplication and preserve continuity.")],
        "related": [("/business-tax-return-lookback-review/", "Business Return Lookback"), ("/best-tax-advisor-for-business-owners/", "Tax Advisor for Business Owners"), ("/discovery/", "Request a Consultation")],
    },
    {
        "slug": "proactive-tax-planning-vs-tax-preparation",
        "title": "Proactive Tax Planning vs. Tax Preparation for Business Owners",
        "meta": "Understand the difference between filing tax returns and making year-round decisions about entities, payroll, retirement, depreciation, estimates, and transactions.",
        "subtitle": "Preparation reports completed facts. Planning changes decisions while the owner still has time to act.",
        "definition": "Tax preparation calculates and reports a completed period under applicable filing rules. Proactive tax planning uses forecasts and current facts to evaluate decisions before deadlines. A business often needs both, but the workpapers, timing, meetings, and deliverables are different.",
        "sections": [
            ("What Preparation Does Well", ["Preparation reconciles tax documents, applies the law to completed transactions, calculates liability, files forms, and preserves elections and carryovers. Strong compliance work is foundational.", "A preparer may identify issues during filing, but many choices are no longer available once the year has closed, payroll has not been run, or a document was not executed."],),
            ("What Planning Adds", ["Planning uses current books and forecasts to model entity structure, owner pay, retirement plans, depreciation, capital spending, estimated taxes, benefits, transactions, and state exposure.", "The output should be an implementation plan with owners, deadlines, cash requirements, documents, and verification. Ideas without execution are not a planning system."],),
            ("Examples of Timing-Sensitive Decisions", ["Payroll, retirement-plan adoption and funding, placed-in-service dates, accountable-plan reimbursements, charitable structures, entity elections, and transaction documents can have timing requirements.", "Even when a filing can be amended later, the facts required for the position may not be capable of retroactive creation."],),
            ("How the Two Teams Should Coordinate", ["The planning file should flow into the books and tax-preparation workpapers. The preparer should see the forecast assumptions, completed steps, elections, contracts, and supporting schedules.", "After filing, the team should compare the final return with the plan, update carryovers, and record lessons for the next cycle."],),
        ],
        "faqs": [("Can my tax preparer also be my advisor?", "Yes, if the engagement includes proactive reviews, modeling, implementation, and follow-through rather than only annual filing."), ("When should planning start?", "Early in the year is ideal, with updates as profit and transactions change. Major decisions should be reviewed before they are executed."), ("Can planning eliminate all taxes?", "No. The objective is an accurate, defensible, economically sensible result, not a promise of zero tax.")],
        "related": [("/year-round-business-tax-planning/", "Year-Round Business Tax Planning"), ("/business-tax-advisor-vs-cpa/", "Business Tax Advisor vs. CPA"), ("/tax-advisor-for-businesses-under-5-million-profit/", "Tax Advisor for Businesses Under $5M")],
    },
]


def render(page):
    path = f"/{page['slug']}/"
    faqs = [(q, f"<p>{a}</p>") for q, a in page["faqs"]]
    body = [
        page_header(h1=page["title"], subtitle=page["subtitle"], trail=[("Home", "/"), (page["title"], path)]),
        takeaways([
            page["definition"],
            "Recommendations depend on the taxpayer's facts, records, elections, state rules, and filing deadlines.",
            "AE Tax Advisors defines implementation responsibilities before recommending a filing or strategy.",
        ]),
        section("The Short Answer", definition(page["definition"])),
    ]
    for heading, paragraphs in page["sections"]:
        body.append(section(heading, "\n".join(f"            <p>{p}</p>" for p in paragraphs)))
    body.extend([faq_section(faqs), related_section(page["related"], "Related AE Tax Resources")])
    schemas = [
        article_schema(title=page["title"], description=page["meta"], url=f"https://www.aetaxadvisors.com{path}", published=DATE, modified=DATE, keywords=[page["slug"].replace("-", " "), "AE Tax Advisors"]),
        faq_schema(faqs),
        breadcrumb_schema([("Home", "/"), (page["title"], path)]),
    ]
    return build_page(title=page["title"], description=page["meta"], path=path, body="\n".join(body), schemas=schemas, published=DATE, modified=DATE, active_nav="/services/")


def main():
    for page in PAGES:
        out = write_page(page["slug"], render(page))
        print(out)
    print(f"Built {len(PAGES)} growth-gap pages")


if __name__ == "__main__":
    main()
