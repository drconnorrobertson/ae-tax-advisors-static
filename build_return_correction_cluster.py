#!/usr/bin/env python3
"""Build the amended-return and depreciation-correction topic cluster.

The cluster is intentionally fact-pattern driven. Each page owns a different
filing decision, form, or downstream consequence. The build refuses duplicate
titles, thin copy, weak sourcing, or pages without a direct booking path.
"""

from __future__ import annotations

import html
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
HUB = "/amended-business-tax-return-services/"


PAGES = [
    {
        "slug": "amend-s-corporation-return",
        "title": "Amend an S Corporation Return | AE Tax Advisors",
        "h1": "How to Amend an S Corporation Tax Return",
        "description": "Correct Form 1120-S, amended K-1s, shareholder returns, and related state filings with a coordinated S corporation amendment process.",
        "section": "Business Return Amendments",
        "lead": "An S corporation correction starts with the entity return, not an isolated replacement K-1. The corporation generally files a complete corrected Form 1120-S, checks the amended-return box, explains each change, and delivers amended K-1 or K-3 information to every affected shareholder.",
        "takeaways": [
            "Rebuild the entity return from the corrected books before changing any shareholder form.",
            "Trace each corrected item through Schedule K, the affected K-1s, shareholder basis, and state filings.",
            "A depreciation-method issue may require Form 3115 instead of, or in addition to, an amended return analysis.",
        ],
        "sections": [
            ("Start with the reason for the correction", """
<p>Separate a clerical error from a tax-method or election problem. A duplicated expense, omitted bank account, ownership allocation error, or corrected information return can change the filed numbers. A change in depreciation method, inventory treatment, or another accounting method can follow a different procedure. The remedy depends on what was wrong, when it began, and whether the same treatment appeared on more than one return.</p>
<p>Build a correction schedule that identifies the original line, corrected line, dollar change, explanation, and source document. Reconcile that schedule to the revised trial balance and fixed-asset ledger. This prevents a common failure: correcting ordinary income while leaving Schedule L, Schedule M-1, Schedule M-2, AAA, or shareholder basis inconsistent.</p>"""),
            ("Coordinate every amended K-1", """
<p>If the amendment changes income, deductions, credits, or other shareholder information, the corporation generally files amended Schedules K-1 or K-3 with the amended 1120-S and gives copies to the shareholders. Each affected owner then evaluates their Form 1040, state returns, estimated taxes, basis schedules, passive-loss limitations, and any downstream entity that received the K-1.</p>
<p>Do not treat a corrected K-1 as a standalone spreadsheet. Confirm the shareholder ownership dates, allocation percentages, distributions, loans, and basis before issuing it. If ownership changed during the year, determine whether the default per-share, per-day allocation or a permitted closing-of-the-books election was used. The corrected corporate return and shareholder workpapers should tell the same story.</p>"""),
            ("Illustrative amendment workflow", """
<p>Assume an S corporation discovers that $80,000 of equipment was posted to repairs even though it should have been capitalized and depreciated. The preparer first establishes the placed-in-service date and correct recovery treatment. The revised depreciation changes ordinary income, Schedule K, each shareholder's K-1, retained tax accounts, and possibly state taxable income. If the treatment was repeated across years, the team must also decide whether this remains an amendable error or has become an accounting-method change.</p>
<p>The file should contain the corrected ledger, asset invoice, depreciation comparison, line-by-line amendment statement, updated K-1s, shareholder basis impact, and state-filing analysis. That package is more defensible than simply attaching a new depreciation report.</p>"""),
            ("Documents to assemble before filing", """
<ul><li>Originally filed federal and state returns, including all K-1s and elections</li><li>Corrected trial balance and general ledger</li><li>Payroll returns and officer-compensation detail when wages change</li><li>Shareholder stock and debt basis schedules</li><li>Fixed-asset and depreciation schedules</li><li>Ownership ledger, distributions, and shareholder-loan records</li><li>A written explanation and tax-effect bridge for every corrected line</li></ul>
<p>AE Tax Advisors can review the full chain before the corporation files. <a href="/discovery/">Book a call to discuss an S corporation amendment</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/instructions/i1120s", "IRS Instructions for Form 1120-S"),
            ("https://www.irs.gov/businesses/corporations/amended-and-superseding-corporate-returns", "IRS amended and superseding corporate returns"),
        ],
        "related": ["corrected-k1-after-amended-1120s", "superseding-vs-amended-business-return", "business-tax-return-second-opinion"],
    },
    {
        "slug": "corrected-k1-after-amended-1120s",
        "title": "Corrected K-1 After an Amended 1120-S | AE Tax",
        "h1": "Corrected K-1 After an Amended Form 1120-S",
        "description": "Learn how an amended S corporation return flows through corrected K-1s, shareholder basis, personal returns, state filings, and later tax years.",
        "section": "Business Return Amendments",
        "lead": "A corrected S corporation K-1 is an output of the amended entity return. It can change a shareholder's federal and state returns, stock or debt basis, passive-loss carryforwards, qualified business income calculations, and later-year reporting even when the current cash distribution did not change.",
        "takeaways": [
            "Correct the 1120-S and the affected K-1s from one reconciled set of books.",
            "Measure both current-year tax and carryforward changes for every shareholder.",
            "Notify owners with a plain-language schedule showing what changed and what they must do next.",
        ],
        "sections": [
            ("Why a K-1 correction reaches beyond one box", """
<p>A change to ordinary business income can affect taxable income, QBI, basis, and loss utilization. A separately stated capital gain, charitable contribution, rental item, credit, or Section 179 amount can produce a different result. The amended K-1 should preserve the character and supplemental disclosures of each item, not merely adjust Box 1 until the total matches.</p>
<p>Compare the original and corrected K-1 line by line. Then roll the difference into the shareholder's basis schedule and any Form 6198, Form 8582, QBI, net investment income, or state workpapers. A zero current-year tax change does not mean the correction is immaterial if it changes a suspended loss or the basis available for a later distribution or stock sale.</p>"""),
            ("Determine which shareholder returns are affected", """
<p>An amended K-1 normally requires the shareholder to evaluate the corresponding individual, trust, estate, or entity return. If the shareholder is another pass-through entity, the correction can continue through an additional tier. Map the ownership chain before filing so each recipient receives the right information and the amendment sequence is logical.</p>
<p>State consequences do not always mirror the federal change. The shareholder may have filed in the corporation's operating states, resident state, or both. Some jurisdictions require notice of a federal change within a separate period. Others need a full amended return, a federal-change report, or revised composite or pass-through entity tax filing.</p>"""),
            ("Example: a loss changes but the refund does not", """
<p>Suppose a two-owner S corporation corrects a $60,000 deduction. Each 50% shareholder receives a K-1 with $30,000 less ordinary income. One owner has enough basis and can use the loss difference immediately. The other owner lacks basis, so the amount remains suspended. The corporate correction is identical, but the shareholder results differ.</p>
<p>The second owner may receive no immediate refund, yet the basis and suspended-loss records must still be corrected. If those records are ignored, a future distribution or business sale can be reported incorrectly. The amendment file should therefore track tax paid, refund requested, basis movement, and carryforwards separately.</p>"""),
            ("A clean shareholder communication package", """
<ul><li>Original and corrected K-1 with differences highlighted</li><li>Reason for the change and the affected tax year</li><li>Revised basis and carryforward schedules when available</li><li>List of federal and state returns that may need review</li><li>Deadline, refund-statute, and payment considerations</li><li>Contact information for entity-level questions</li></ul>
<p>Need the entity and owner returns reviewed together? <a href="/discovery/">Book a call with AE Tax Advisors</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/instructions/i1120s", "IRS Instructions for Form 1120-S"),
            ("https://www.irs.gov/instructions/i1120ssk", "IRS Shareholder Instructions for Schedule K-1"),
        ],
        "related": ["amend-s-corporation-return", "amended-business-return-state-filings", "passive-loss-carryforward-correction"],
    },
    {
        "slug": "partnership-aar-vs-amended-return",
        "title": "Partnership AAR vs. Amended Return | AE Tax",
        "h1": "Partnership AAR vs. Amended Form 1065",
        "description": "Determine whether a partnership correction requires an amended Form 1065 or a BBA administrative adjustment request and how partners are affected.",
        "section": "Business Return Amendments",
        "lead": "A partnership cannot assume that every correction uses a conventional amended Form 1065. A partnership subject to the centralized partnership audit regime generally corrects partnership-related items through an administrative adjustment request, while an eligible partnership that validly elected out may follow amended-return procedures.",
        "takeaways": [
            "Verify the partnership's BBA status for the reviewed year before choosing a form.",
            "An AAR can create an imputed underpayment or push-out reporting rather than amended K-1s.",
            "The partnership representative for the reviewed year controls key AAR actions.",
        ],
        "sections": [
            ("Read the originally filed return first", """
<p>Start with Schedule B, the partnership-representative designation, any election out of the BBA regime, and the ownership roster for the year being corrected. Eligibility and a timely election matter. The partners' current identities do not replace the reviewed-year facts, and a new managing member is not automatically the person authorized to act for that year.</p>
<p>Next classify the error. An omitted deduction, allocation change, corrected sale, basis item, credit, or depreciation adjustment can affect the partnership and partners differently. If the issue involves an accounting method, Form 3115 rules may overlay the partnership-correction procedure. Avoid choosing an AAR solely because the software offers it.</p>"""),
            ("How an AAR changes the economics", """
<p>A BBA AAR can result in an imputed underpayment paid at the partnership level or, when permitted and elected, adjustments pushed out to reviewed-year partners. Forms 8082, 8985, and 8986 can become part of the package. These mechanics differ from issuing a familiar amended K-1, and they can change who bears the cash cost when ownership has changed.</p>
<p>Model the result before filing. Compare partnership-level payment, push-out effects, interest, state conformity, partner liquidity, and the partnership agreement's tax-allocation provisions. A technically valid correction can still create an avoidable dispute if current owners pay tax attributable to former partners.</p>"""),
            ("Example: a missed deduction in a sold partnership interest", """
<p>Assume a partnership finds a $200,000 reviewed-year deduction after one partner has sold its interest. A non-BBA amendment might flow revised information to the reviewed-year partners. A BBA partnership may instead compute an AAR adjustment and decide between partnership-level treatment and an available push-out process. The current cap table alone does not answer who receives or funds the adjustment.</p>
<p>The workpaper should show BBA status, reviewed-year ownership, the corrected return lines, imputed-underpayment computation if applicable, push-out alternative, state consequences, and the economic allocation under the partnership agreement.</p>"""),
            ("Documents required for an AAR decision", """
<ul><li>Original Form 1065, Schedule B, and partnership-representative designation</li><li>Election-out statement, if one was made</li><li>Reviewed-year and current ownership schedules</li><li>Partnership agreement and transfer documents</li><li>Corrected trial balance and allocation workpapers</li><li>State returns and composite or PTE tax filings</li></ul>
<p>Partnership corrections are procedural and economic projects. <a href="/discovery/">Book a call before filing an AAR or amended Form 1065</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/businesses/partnerships/file-an-administrative-adjustment-request-for-a-bba-partnership", "IRS guidance for BBA partnership AARs"),
            ("https://www.irs.gov/instructions/i1065", "IRS Instructions for Form 1065"),
            ("https://www.irs.gov/instructions/i1065x", "IRS Instructions for Form 1065-X"),
        ],
        "related": ["superseding-vs-amended-business-return", "amended-business-return-state-filings", "business-tax-return-second-opinion"],
    },
    {
        "slug": "amended-c-corporation-return",
        "title": "Amended C Corporation Return | AE Tax Advisors",
        "h1": "How to Amend a C Corporation Tax Return",
        "description": "Correct Form 1120 with Form 1120-X, reconcile tax attributes and payments, and coordinate federal changes with state corporate income tax filings.",
        "section": "Business Return Amendments",
        "lead": "A C corporation generally uses Form 1120-X to correct a previously filed corporate income tax return. The amendment must reconcile the originally reported amounts, corrected amounts, tax payments, credits, carrybacks or carryforwards, and any state effects.",
        "takeaways": [
            "Tie Form 1120-X to a corrected full return and a line-by-line explanation.",
            "Recalculate NOLs, credits, estimated payments, and later-year attributes before requesting a refund.",
            "Review state reporting deadlines separately from the federal refund statute.",
        ],
        "sections": [
            ("Rebuild the corporate tax computation", """
<p>Do not begin with the refund line. Correct the general ledger and tax workpapers, then recompute taxable income, special deductions, credits, tax, payments, and attributes. An error in depreciation or inventory can affect several years through carryovers. A correction to a dividend, capital transaction, or foreign item can require specialized schedules beyond Form 1120-X.</p>
<p>Prepare an original-to-corrected bridge for every changed line. Reconcile that bridge to the revised Form 1120, Schedule M-1 or M-3, Schedule L when affected, fixed-asset ledger, and tax attribute rollforwards. If the correction changes book entries after financial statements were issued, coordinate with the financial-reporting team rather than forcing the tax return to match an unrevised ledger.</p>"""),
            ("Distinguish a claim from an accounting-method change", """
<p>Some errors can be corrected on an amended return. A recurring treatment may constitute a method of accounting that requires consent and Form 3115. The same distinction appears in depreciation, revenue recognition, inventory, capitalization, and prepaid-expense issues. Identify the first year the treatment occurred and whether it was used consistently before selecting Form 1120-X.</p>
<p>If the corporation is still within the original filing period, including extensions, a superseding return may be available instead. That return replaces the original for many purposes and follows different timing logic. Record the filing date, extended due date, and e-file availability before choosing the route.</p>"""),
            ("Example: correcting a capitalized software project", """
<p>Suppose a corporation deducted $300,000 of software-development costs and later determines that part of the project required capitalization under the applicable rules. The correction changes current deductions, tax depreciation or amortization, deferred tax records, and later-year schedules. If the same treatment continued across multiple returns, the method-change analysis becomes central.</p>
<p>The amendment package should include project invoices, placed-in-service evidence, the legal analysis, corrected asset schedule, current and future deduction comparison, amended state computation, and an explanation of why Form 1120-X or Form 3115 is the appropriate procedure.</p>"""),
            ("Corporate amendment file", """
<ul><li>Originally filed return and proof of filing</li><li>Corrected return and Form 1120-X reconciliation</li><li>Tax payment, deposit, and credit transcript support</li><li>NOL, credit, charitable contribution, and capital-loss rollforwards</li><li>State apportionment and amended-return schedules</li><li>Board or officer approval for material refund claims</li></ul>
<p><a href="/discovery/">Book a call for a coordinated C corporation return review</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/forms-pubs/about-form-1120-x", "IRS Form 1120-X"),
            ("https://www.irs.gov/businesses/corporations/amended-and-superseding-corporate-returns", "IRS amended and superseding corporate returns"),
        ],
        "related": ["superseding-vs-amended-business-return", "amended-business-return-state-filings", "business-tax-return-second-opinion"],
    },
    {
        "slug": "superseding-vs-amended-business-return",
        "title": "Superseding vs. Amended Business Return | AE Tax",
        "h1": "Superseding Return vs. Amended Business Return",
        "description": "Compare superseding and amended business returns, including timing, e-file treatment, elections, K-1 effects, and state filing consequences.",
        "section": "Business Return Amendments",
        "lead": "A superseding return is generally filed after the original return but before the filing period, including extensions, expires. An amended return is filed after that period. The timing distinction can affect elections, processing, partner or shareholder reporting, and how the filing is labeled.",
        "takeaways": [
            "Confirm the original due date, valid extension, and actual filing date.",
            "Do not label a late correction as superseding merely because it is the second return.",
            "Coordinate corrected K-1s, elections, and state returns with the chosen federal procedure.",
        ],
        "sections": [
            ("Timing controls the classification", """
<p>A business can discover an error days after filing. If the valid filing period remains open, a superseding return may replace the original return for many purposes. Once that period expires, the filing is generally an amended return. The calendar must account for the entity type, fiscal year, weekends or holidays, and a valid extension rather than an assumed six-month window.</p>
<p>Gather the e-file acknowledgments, extension acceptance, signed original return, and proposed correction. Software labels do not establish legal timing. A return transmitted before the deadline but rejected afterward can raise additional procedural questions that should be documented.</p>"""),
            ("Why elections require special review", """
<p>Some elections must be made on a timely original return, including a timely superseding return where permitted. Others have regulatory or revenue-procedure relief. An amended return may not recreate every election opportunity. Identify each election statement affected by the correction instead of assuming that changing a number also changes the election.</p>
<p>For pass-through entities, the superseding return may generate replacement K-1s before owners file. If shareholders or partners already filed, even a technically superseding entity return creates practical amendment work downstream. Keep a recipient log showing who received which version and when.</p>"""),
            ("Example: correction before the extended deadline", """
<p>An S corporation files in August under a valid extension and discovers omitted revenue in early September. If the extended filing period has not expired, the team evaluates a superseding 1120-S. It still must correct the complete return, explain the changes through the required e-file data, and issue corrected shareholder information. If the same error is found after the extended deadline, the amended-return procedure applies instead.</p>
<p>The key evidence is the calendar and filing record. Preserve the extension, original acknowledgment, superseding or amended acknowledgment, and notices to owners. Do not rely on file names such as “final-final-return.”</p>"""),
            ("Pre-filing decision checklist", """
<ul><li>Entity type and tax year</li><li>Original statutory and extended due dates</li><li>Proof of a valid extension</li><li>Original filing and acceptance date</li><li>Elections affected by the correction</li><li>K-1 or K-3 recipients who already filed</li><li>Federal and state electronic-filing availability</li></ul>
<p><a href="/discovery/">Book a call before the correction window closes</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/businesses/corporations/amended-and-superseding-corporate-returns", "IRS amended and superseding corporate returns"),
            ("https://www.irs.gov/instructions/i1120s", "IRS Instructions for Form 1120-S"),
        ],
        "related": ["amend-s-corporation-return", "amended-c-corporation-return", "partnership-aar-vs-amended-return"],
    },
    {
        "slug": "amended-business-return-state-filings",
        "title": "State Filings After a Business Amendment | AE Tax",
        "h1": "State Filings After an Amended Business Return",
        "description": "Trace a federal business-return correction through state income, franchise, composite, withholding, PTE tax, and owner filings.",
        "section": "Business Return Amendments",
        "lead": "A federal business amendment can trigger more than one state filing. The entity may need amended income or franchise returns, while owners may need resident and nonresident amendments, corrected withholding, composite returns, or pass-through entity tax adjustments.",
        "takeaways": [
            "Build a jurisdiction matrix before filing the federal correction.",
            "Track federal-change notification periods separately from ordinary refund deadlines.",
            "Reconcile entity payments, owner credits, composite filings, and PTE tax elections together.",
        ],
        "sections": [
            ("Map where the corrected item was reported", """
<p>Start with the federal return, every state entity return, apportionment schedules, owner K-1 equivalents, withholding forms, composite returns, and PTE tax filings. A federal ordinary-income change may be apportioned differently by state. A depreciation correction may encounter state decoupling from federal bonus depreciation. A gain may be sourced to a particular jurisdiction rather than follow the entity's general apportionment percentage.</p>
<p>Create one row per jurisdiction showing the original amount, federal change, state modification, revised state base, tax or refund, owner effect, form required, and deadline. This prevents the federal refund from being treated as the complete project.</p>
<p>Include local income or gross-receipts filings when the business operates in a city with its own return. A federal correction may change a local base even when the state amendment is small. Confirm whether the locality follows federal taxable income, state apportioned income, payroll, or receipts.</p>"""),
            ("Watch for owner-level mismatches", """
<p>An S corporation or partnership amendment may change state-source income and the credit available on an owner's resident return. If the entity corrects nonresident withholding or composite tax, the owner must use the matching revised amount. A PTE tax payment can affect both the entity deduction and the owner's state credit, sometimes in different years.</p>
<p>Send corrected state schedules with the federal K-1 package. Owners need to know which state forms changed, whether payment is due, and whether an amendment should wait for the entity filing to process. Multi-tier partnerships require an additional pass-through map.</p>"""),
            ("Example: federal depreciation with state decoupling", """
<p>Assume an entity increases federal depreciation through a correction, but one operating state does not conform to the same bonus-depreciation treatment. The federal ordinary-income decrease does not flow dollar for dollar into that state. The entity must update the state's depreciation adjustment, apportionment, K-1 equivalent, and potentially the owner's resident-state credit.</p>
<p>A strong file retains the federal fixed-asset schedule, state depreciation schedule, conformity authority for the tax year, revised state returns, owner notices, and proof of payments or refunds.</p>"""),
            ("State amendment control sheet", """
<ul><li>Jurisdiction and return type</li><li>Federal-change report or full amended return</li><li>Original and revised apportionment</li><li>Bonus-depreciation or other conformity adjustment</li><li>Composite, withholding, and PTE tax changes</li><li>Owner returns and resident-credit effects</li><li>Notice deadline and filing status</li></ul>
<p><a href="/discovery/">Book a multistate amendment review</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/instructions/i1120s", "IRS Form 1120-S instructions on state effects"),
            ("https://www.irs.gov/instructions/i1065", "IRS Instructions for Form 1065"),
        ],
        "related": ["corrected-k1-after-amended-1120s", "partnership-aar-vs-amended-return", "business-tax-return-second-opinion"],
    },
    {
        "slug": "business-tax-return-second-opinion",
        "title": "Business Tax Return Second Opinion | AE Tax",
        "h1": "Business Tax Return Second-Opinion Review",
        "description": "Review prior Forms 1120-S, 1065, or 1120 for missed deductions, depreciation errors, basis problems, and amendment opportunities.",
        "section": "Business Return Review",
        "lead": "A second-opinion review should not begin with a promise of a refund. It should reconcile the return to the books, trace material tax positions to source records, identify procedural options, and quantify both favorable and unfavorable corrections before recommending an amendment.",
        "takeaways": [
            "Review entity, owner, depreciation, and state reporting as one system.",
            "Separate planning opportunities from errors that can still be corrected.",
            "Do not amend until the team has modeled future-year and audit consequences.",
        ],
        "sections": [
            ("What the review should test", """
<p>For an S corporation, examine officer wages, shareholder distributions, stock and debt basis, health insurance, accountable-plan reimbursements, retirement contributions, and K-1 allocations. For a partnership, examine capital accounts, liabilities, special allocations, Section 754 history, guaranteed payments, and BBA status. For a C corporation, examine NOLs, credits, compensation, dividends, capital transactions, and retained tax attributes.</p>
<p>Across all entity types, reconcile gross receipts, payroll, information returns, fixed assets, depreciation, loans, owner transactions, and state filings. Compare tax-basis workpapers to the filed balance sheet. An issue list without a reconciliation can misidentify bookkeeping differences as tax errors.</p>"""),
            ("Classify every finding before valuing it", """
<p>Label each item as correct as filed, documentation improvement, prospective planning, amendable error, accounting-method issue, uncertain position, or closed-year matter. This prevents a common sales problem: describing a future strategy as money recoverable from a prior return.</p>
<p>For each correction candidate, quantify federal tax, state tax, interest, penalties, professional fees, carryforward effects, owner consequences, and audit exposure. A $20,000 additional deduction is not a $20,000 benefit. Conversely, a correction with no immediate refund may restore basis or losses that matter later.</p>
<p>Rank findings by certainty and value. A fully documented fixed-asset omission is different from an aggressive position that depends on disputed facts. The review should make that distinction visible so the owner can approve corrections without assuming every item carries the same confidence or filing risk.</p>"""),
            ("Illustrative three-year review", """
<p>Suppose a real-estate operating company has an S corporation return, two rental partnerships, and the owner's individual return. The review finds an omitted reimbursement plan, inconsistent rental depreciation, a partner-liability allocation error, and an unused state PTE credit. These findings require different actions: prospective documentation, depreciation-procedure analysis, partnership correction, and owner-level state amendment.</p>
<p>The final deliverable should show facts, authority, amount, affected returns, correction path, deadline, risk, and recommended action for each item. The client can then approve a coherent filing plan instead of a stack of isolated amended returns.</p>"""),
            ("Records for an efficient review", """
<ul><li>Three years of federal and state entity and owner returns</li><li>Year-end and current general ledgers</li><li>Depreciation schedules and cost segregation reports</li><li>Payroll, retirement-plan, and owner-compensation records</li><li>Debt agreements, basis schedules, and ownership changes</li><li>IRS and state notices or account transcripts</li></ul>
<p><a href="/discovery/">Book a business-return second-opinion call</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/businesses/corporations/amended-and-superseding-corporate-returns", "IRS amended corporate return guidance"),
            ("https://www.irs.gov/forms-pubs/about-form-3115", "IRS Form 3115"),
        ],
        "related": ["amend-s-corporation-return", "partnership-aar-vs-amended-return", "depreciation-schedule-review"],
    },
    {
        "slug": "form-3115-vs-amended-return-cost-segregation",
        "title": "Form 3115 vs. Amended Return for Cost Seg | AE Tax",
        "h1": "Form 3115 vs. an Amended Return for Cost Segregation",
        "description": "Determine whether prior-year cost segregation belongs on Form 3115, an amended return, or a timely superseding return based on depreciation history.",
        "section": "Cost Segregation Corrections",
        "lead": "The correct filing route depends on depreciation history, not simply the age of the property. If the taxpayer has adopted a depreciation method, a cost segregation lookback commonly proceeds through Form 3115 and a Section 481(a) adjustment. Certain first-year, mathematical, posting, or otherwise amendable errors can follow a different route.",
        "takeaways": [
            "Count filed returns and identify the depreciation method actually used.",
            "Separate a cost-segregation method change from a math, basis, or placed-in-service error.",
            "Do not file Form 3115 until the study reconciles to the return's existing asset basis.",
        ],
        "sections": [
            ("The decision begins with depreciation history", """
<p>Collect every depreciation schedule from the placed-in-service year through the proposed year of change. Confirm the owner, activity, tax form, depreciable basis, land allocation, recovery periods, convention, bonus treatment, and dispositions. A cost segregation report cannot be dropped onto the current return if its starting basis differs from the filed schedules.</p>
<p>IRS depreciation guidance distinguishes corrections allowed on an amended return from changes in accounting method. Generally, using the same impermissible depreciation method on two or more consecutively filed returns establishes a method. A change from that method ordinarily requires consent through Form 3115. Exceptions and current revenue procedures must be checked for the filing year.</p>"""),
            ("When an amended or superseding return may matter", """
<p>A mathematical or posting error can be amendable. Depreciation for a property where the taxpayer has not yet adopted a method may also be eligible for amendment under the applicable rules. If the original filing period remains open, a timely superseding return may offer another path. These are procedural categories, not interchangeable labels.</p>
<p>Basis errors require separate analysis. A cost segregation study classifies components within supported depreciable basis; it does not validate an incorrect purchase-price, land, closing-cost, or improvement basis. Correct the transaction ledger before deciding how to implement the classification change.</p>"""),
            ("Example: first return versus established method", """
<p>Property A was placed in service last year and only one return has been filed. The owner now obtains a study. Depending on the facts and deadlines, an amended or superseding return may remain available because a method may not yet have been adopted. Property B has been depreciated as one building asset on three returns. A lookback study for Property B generally points toward a method change and a cumulative Section 481(a) adjustment.</p>
<p>The example does not create an automatic two-return rule for every fact pattern. Late elections, bonus depreciation, prior dispositions, entity changes, and impermissible basis can alter the procedure. Document why the selected correction method applies.</p>"""),
            ("Implementation file", """
<ul><li>Placed-in-service documentation and original closing records</li><li>Every filed depreciation schedule</li><li>Cost segregation report and basis reconciliation</li><li>Old-versus-new depreciation by asset and year</li><li>Section 481(a) calculation where applicable</li><li>Form 3115 method-change citation and filing instructions</li><li>State depreciation adjustment analysis</li></ul>
<p><a href="/discovery/">Book a call to review the right filing path</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/publications/p946", "IRS Publication 946"),
            ("https://www.irs.gov/forms-pubs/about-form-3115", "IRS Form 3115"),
            ("https://www.irs.gov/instructions/i3115", "IRS Instructions for Form 3115"),
        ],
        "related": ["catch-up-depreciation-section-481a", "missed-depreciation-rental-property", "cost-segregation-after-extension-deadline"],
    },
    {
        "slug": "catch-up-depreciation-section-481a",
        "title": "Section 481(a) Catch-Up Depreciation | AE Tax",
        "h1": "Section 481(a) Catch-Up Depreciation Explained",
        "description": "See how a Section 481(a) adjustment measures prior depreciation differences, enters the year of change, and interacts with loss limitations.",
        "section": "Cost Segregation Corrections",
        "lead": "A Section 481(a) adjustment generally measures the cumulative difference between the old and new accounting methods as of the beginning of the year of change. For a favorable depreciation change, the adjustment can bring previously missed deductions into the current return without reopening each prior year.",
        "takeaways": [
            "Reconcile cumulative depreciation asset by asset, not with a single percentage estimate.",
            "The adjustment changes taxable income, but basis, at-risk, and passive-loss rules still control usability.",
            "The study, Form 3115, depreciation schedule, and return must use the same numbers.",
        ],
        "sections": [
            ("Build the adjustment from filed history", """
<p>Start with depreciation allowed or allowable under the taxpayer's old method through the end of the prior year. Compare it with cumulative depreciation under the proposed permissible method for the same period. Account for assets placed in service at different dates, prior bonus or Section 179 deductions, improvements, dispositions, and business-use changes.</p>
<p>A favorable adjustment is often described as catch-up depreciation, but it is not a new property basis. It synchronizes the cumulative depreciation under the new method. The post-change schedule must continue from the corrected accumulated depreciation so the taxpayer does not claim the same amount again.</p>"""),
            ("Illustrative calculation", """
<p>Assume the filed schedules show $120,000 of cumulative depreciation through the prior year. A reconciled cost segregation study and corrected schedule show that $205,000 would have been allowable under the new method for the same period. The simplified favorable Section 481(a) adjustment is $85,000. Current-year depreciation is then computed separately under the new schedule.</p>
<p>The $85,000 is a deduction, not an $85,000 refund. If the property activity is passive, or the owner lacks basis or amount at risk, some or all of the loss may be suspended. State depreciation conformity can also produce a different state adjustment.</p>"""),
            ("Common reconciliation failures", """
<p>Problems arise when the study uses purchase price while the return used a different depreciable basis, ignores later renovations, includes land, or reclassifies an asset that was already separately depreciated. Another failure is calculating catch-up through the current year and then also claiming full current-year depreciation, creating a duplicate deduction.</p>
<p>Use a bridge that begins with tax basis, subtracts land, identifies prior separately stated assets, adds or removes supported improvements and dispositions, and ties exactly to the study total. Then reconcile cumulative depreciation and current-year depreciation in separate columns.</p>"""),
            ("Review package", """
<ul><li>Old and new asset ledgers</li><li>Annual depreciation comparison from placed-in-service date</li><li>Basis reconciliation to closing and improvement records</li><li>Form 3115 and designated-change support</li><li>Federal and state Section 481(a) calculations</li><li>Loss-limitation and carryforward schedules</li></ul>
<p><a href="/discovery/">Book a Section 481(a) calculation review</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/forms-pubs/about-form-3115", "IRS Form 3115"),
            ("https://www.irs.gov/instructions/i3115", "IRS Instructions for Form 3115"),
            ("https://www.irs.gov/publications/p946", "IRS Publication 946"),
        ],
        "related": ["form-3115-vs-amended-return-cost-segregation", "depreciation-schedule-review", "passive-loss-carryforward-correction"],
    },
    {
        "slug": "missed-depreciation-rental-property",
        "title": "Missed Depreciation on Rental Property | AE Tax",
        "h1": "How to Correct Missed Rental Property Depreciation",
        "description": "Correct depreciation that was omitted from a rental return by identifying basis, placed-in-service date, filed history, and the proper filing method.",
        "section": "Rental Return Corrections",
        "lead": "Missed rental depreciation should not be fixed by adding an arbitrary current-year expense. The owner must reconstruct the property's depreciable basis and placed-in-service date, determine what was allowed or allowable, and then select the correct amended-return or accounting-method procedure.",
        "takeaways": [
            "Reconstruct land, building, improvements, furnishings, and prior dispositions separately.",
            "Depreciation can affect basis on sale even when the owner failed to claim it.",
            "The correction method depends on how many returns were filed and what treatment they used.",
        ],
        "sections": [
            ("Rebuild the property timeline", """
<p>Document acquisition, conversion from personal use if applicable, ready-and-available date, first rental date, improvements, periods of personal use, casualty events, and sale or exchange. Depreciation begins when the property is placed in service, not necessarily when the first tenant pays rent. For a converted residence, the depreciation basis can differ from the basis used to calculate gain on a later sale.</p>
<p>Separate land from depreciable improvements. Identify appliances, furniture, land improvements, and later capital projects. Reconcile purchase and improvement basis to settlement statements, invoices, and the filed Schedule E or entity return.</p>"""),
            ("Choose the correction route", """
<p>If depreciation was omitted or incorrectly computed on one return and no method was adopted, an amended return may be available under the applicable rules. If the same impermissible treatment appeared on two or more consecutive returns, changing to the permissible method generally requires Form 3115. Mathematical and posting errors have their own treatment.</p>
<p>Do not assume that an open three-year refund period alone determines the route. The depreciation-method rules and the refund statute answer different questions. A Form 3115 catch-up can reach cumulative prior depreciation through a current-year adjustment when its requirements are met.</p>"""),
            ("Example: a duplex omitted for three years", """
<p>An owner bought a duplex for $600,000, allocated $120,000 to land, placed it in service three years ago, and never added the building to the depreciation schedule. Before correcting the return, the preparer verifies the $480,000 improvement basis, closing costs, improvements, personal use, and all filed returns. Because the omission continued across multiple returns, the analysis generally moves toward an accounting-method correction rather than simply amending the most recent year.</p>
<p>The catch-up amount must be computed from the permissible schedule through the beginning of the correction year. Current-year depreciation remains separate, and passive-loss limitations determine how much affects current taxable income.</p>"""),
            ("Records to preserve", """
<ul><li>Closing statement, deed, and land allocation</li><li>Placed-in-service and rental-listing evidence</li><li>Improvement and furnishing invoices</li><li>Every filed depreciation schedule and Schedule E</li><li>Old-versus-correct depreciation computation</li><li>Form 3115 or amended-return analysis</li></ul>
<p><a href="/discovery/">Book a rental depreciation review</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/publications/p527", "IRS Publication 527"),
            ("https://www.irs.gov/publications/p946", "IRS Publication 946"),
            ("https://www.irs.gov/forms-pubs/about-form-3115", "IRS Form 3115"),
        ],
        "related": ["form-3115-vs-amended-return-cost-segregation", "wrong-rental-depreciation-basis", "amend-schedule-e-rental-property"],
    },
    {
        "slug": "wrong-rental-depreciation-basis",
        "title": "Wrong Rental Depreciation Basis | AE Tax Advisors",
        "h1": "Correcting the Wrong Rental Property Depreciation Basis",
        "description": "Fix rental depreciation based on an incorrect purchase allocation, converted-home value, closing costs, improvements, or land amount.",
        "section": "Rental Return Corrections",
        "lead": "An incorrect depreciation basis is not automatically the same problem as an incorrect depreciation method. Before choosing an amendment or Form 3115, determine why basis is wrong: purchase allocation, land, converted-property value, omitted closing costs, unsupported improvements, casualty adjustments, or duplicated assets.",
        "takeaways": [
            "Reconstruct total property basis before applying a cost segregation classification.",
            "Converted personal residences can use a special basis rule for depreciation.",
            "A basis correction can affect depreciation, gain or loss, recapture, and state reporting.",
        ],
        "sections": [
            ("Identify the source of the wrong number", """
<p>Compare the settlement statement, purchase agreement, appraisal, tax assessment, improvement invoices, and filed asset schedule. Determine whether the return incorrectly included land, omitted eligible acquisition costs, duplicated a separately listed appliance, or used loan proceeds as basis. For a property converted from personal to rental use, compare adjusted basis and fair market value at conversion under the applicable loss and depreciation rules.</p>
<p>Do not use a new appraisal merely to target a preferred deduction. The allocation method should be supportable for the acquisition date or conversion date and consistent with the actual transaction. Document why the selected land and building values are more reliable than alternatives.</p>"""),
            ("Separate basis from classification", """
<p>Cost segregation divides supported depreciable cost among recovery classes. It does not create additional purchase price or cure missing transaction records. First establish the amount available to allocate. Then reconcile the engineering or detailed study to that tax basis.</p>
<p>If the old return used a permissible depreciation method on the wrong basis, the correction analysis may differ from a change between depreciation methods. Examine the nature and duration of the error, current procedural guidance, and whether amended returns remain available. Avoid choosing Form 3115 merely because the issue appears on a depreciation schedule.</p>"""),
            ("Example: former home converted to a rental", """
<p>An owner bought a home for $500,000, later converted it to rental use when its fair market value was $430,000, and used the original purchase price as depreciation basis without separating land. The correction requires evidence of adjusted basis, fair market value at conversion, land allocation, improvements, and the actual placed-in-service date. The basis used for depreciation may not equal the amount used to compute gain on a later sale.</p>
<p>Once the correct depreciation basis is established, calculate the annual and cumulative differences, determine the filing procedure, and update the eventual sale schedule. This avoids fixing depreciation while leaving future gain calculations wrong.</p>"""),
            ("Basis reconstruction file", """
<ul><li>Purchase and conversion-date records</li><li>Appraisal or other valuation support</li><li>Land and building allocation method</li><li>Capital improvement and casualty history</li><li>Prior depreciation and disposition schedules</li><li>Correction-method memorandum</li></ul>
<p><a href="/discovery/">Book a basis and depreciation review</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/publications/p527", "IRS Publication 527"),
            ("https://www.irs.gov/publications/p551", "IRS Publication 551"),
            ("https://www.irs.gov/publications/p946", "IRS Publication 946"),
        ],
        "related": ["missed-depreciation-rental-property", "converted-home-rental-depreciation-basis", "depreciation-schedule-review"],
    },
    {
        "slug": "cost-segregation-after-extension-deadline",
        "title": "Cost Segregation After the Tax Deadline | AE Tax",
        "h1": "Cost Segregation After the Extension Deadline",
        "description": "Understand what happens when a cost segregation study or Form 3115 is not ready by the return deadline and how to plan the next filing year.",
        "section": "Cost Segregation Corrections",
        "lead": "A late cost segregation report does not authorize attaching an incomplete or backdated Form 3115 to a filed return. The next step depends on whether the property is in its first return year, whether a depreciation method has been adopted, and which method-change procedure applies for the next tax year.",
        "takeaways": [
            "Preserve the actual completion and filing dates for the study and Form 3115.",
            "Do not confuse an amended-return window with permission to make a late method change.",
            "Model the next year of change, including the updated Section 481(a) calculation.",
        ],
        "sections": [
            ("Establish what was filed by the deadline", """
<p>Collect the accepted return, extension, depreciation schedule, drafts, engagement letters, and the date the cost segregation report became final. Determine whether Form 3115 was properly completed and filed under the applicable procedure or whether the taxpayer only intended to file it. Intent and a preliminary estimate do not substitute for a filed method-change application.</p>
<p>If the property was placed in service in the return year, assess whether a timely election or depreciation choice was missed. If the property was already under an established method, evaluate a change in the next available year. These are different problems and should not be blended into a generic “late cost seg” answer.</p>"""),
            ("Recalculate the next-year catch-up", """
<p>When the method change moves to the following year, the Section 481(a) calculation generally needs another year of depreciation history. Update old-method depreciation through the year before the new year of change, then compare it with the proposed method through the same date. Do not reuse the earlier draft adjustment without reconciliation.</p>
<p>Also update passive-loss, basis, at-risk, and state schedules. A later catch-up can land in a year with different income, ownership, or activity status. Model whether the deduction is usable before presenting the gross adjustment as tax savings.</p>"""),
            ("Example: study completed after an S-corp deadline", """
<p>An S corporation files its extended return on time, then receives the final study several weeks later. The property has been depreciated under the same method for several years. The team should not simply amend the filed return and attach a Form 3115 dated later. It evaluates the current method-change rules for the next tax year, recalculates the cumulative adjustment, and coordinates any required duplicate filing or statement procedures.</p>
<p>If the property was instead first placed in service on the just-filed return, the amendment analysis can be different because method adoption and election timing must be examined. The file should explain the distinction.</p>"""),
            ("Deadline recovery checklist", """
<ul><li>Accepted return and extension proof</li><li>Final study delivery date</li><li>Filed depreciation method and number of returns</li><li>Any elections made or missed</li><li>Updated Section 481(a) schedule</li><li>Next-year designated-change procedure</li><li>State conformity and filing effects</li></ul>
<p><a href="/discovery/">Book a late cost-segregation implementation review</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/forms-pubs/about-form-3115", "IRS Form 3115"),
            ("https://www.irs.gov/instructions/i3115", "IRS Instructions for Form 3115"),
            ("https://www.irs.gov/publications/p946", "IRS Publication 946"),
        ],
        "related": ["form-3115-vs-amended-return-cost-segregation", "catch-up-depreciation-section-481a", "missed-depreciation-rental-property"],
    },
    {
        "slug": "amend-schedule-e-rental-property",
        "title": "Amend Schedule E for Rental Property | AE Tax",
        "h1": "When to Amend Schedule E for a Rental Property",
        "description": "Correct rental income, expenses, ownership, personal use, depreciation, or passive-loss reporting on Schedule E without creating new inconsistencies.",
        "section": "Rental Return Corrections",
        "lead": "A Schedule E correction can change rental income, expenses, depreciation, passive-loss carryforwards, qualified business income reporting, net investment income tax, and eventual gain or loss. The correction should be rebuilt from property records rather than entered as one net adjustment.",
        "takeaways": [
            "Correct each property and expense category separately.",
            "A depreciation-method issue may require Form 3115 rather than repeated amended returns.",
            "Update Form 8582 and all carryforward schedules even when no immediate refund results.",
        ],
        "sections": [
            ("Classify the Schedule E error", """
<p>Common issues include omitted rent, duplicated platform statements, security deposits treated as income, repairs capitalized or deducted incorrectly, personal-use allocation errors, mortgage-interest mismatches, missing management fees, and depreciation omissions. Ownership through a partnership or S corporation usually does not belong on the individual's Schedule E as though the individual directly owned the property.</p>
<p>Reconcile rental activity to bank deposits, property-manager statements, Forms 1099, leases, escrow statements, and the general ledger. For short-term rentals, determine whether substantial services or the average customer-use period changes where and how the activity is reported.</p>
<p>Keep refundable tenant deposits separate from rent until the facts cause them to become income. Reconcile advance rent by the taxpayer's accounting method. Platform payouts should be bridged from gross guest charges through fees, refunds, and taxes rather than reported from net bank deposits alone.</p>"""),
            ("Recompute the passive-loss schedule", """
<p>A corrected property result feeds Form 8582 when the activity is passive. The amendment can change losses allowed, suspended, or released. Prior-year changes may also alter the opening carryforward used on later returns. Rebuild the activity rollforward through the current year rather than correcting one isolated form.</p>
<p>Basis and at-risk limits can apply before the passive-loss rules. For a direct rental, debt and investment records matter. For a pass-through rental, the entity's K-1 and basis schedule control. Keep each limitation in the correct order.</p>"""),
            ("Example: repair reclassified as an improvement", """
<p>A landlord deducted a $45,000 renovation as repairs. Review later shows that part replaced a major building component and should have been capitalized, while another portion was routine maintenance. The amendment needs an invoice-level allocation, corrected depreciation, revised Schedule E expense, updated Form 8582, and a plan for later sale basis. A single $45,000 reversal would be too coarse.</p>
<p>If the same capitalization treatment continued across several years, the team also evaluates whether the correction is an accounting-method change. The nature and duration of the error determine the procedure.</p>"""),
            ("Rental amendment workpaper", """
<ul><li>Property-by-property income reconciliation</li><li>Invoice classification and personal-use allocation</li><li>Mortgage, tax, insurance, and management statements</li><li>Corrected depreciation schedules</li><li>Basis, at-risk, and passive-loss rollforwards</li><li>Federal and state amendment analysis</li></ul>
<p><a href="/discovery/">Book a Schedule E review</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/publications/p527", "IRS Publication 527"),
            ("https://www.irs.gov/publications/p925", "IRS Publication 925"),
            ("https://www.irs.gov/forms-pubs/about-schedule-e-form-1040", "IRS Schedule E"),
        ],
        "related": ["missed-depreciation-rental-property", "passive-loss-carryforward-correction", "depreciation-schedule-review"],
    },
    {
        "slug": "passive-loss-carryforward-correction",
        "title": "Correct a Passive Loss Carryforward | AE Tax",
        "h1": "How to Correct a Rental Passive-Loss Carryforward",
        "description": "Reconstruct an incorrect rental passive-loss carryforward by tracing basis, at-risk limits, Form 8582, grouping, income, and dispositions.",
        "section": "Rental Return Corrections",
        "lead": "A passive-loss carryforward is the result of a multi-year limitation calculation, not a free-standing number. Correcting it requires rebuilding each activity from the year the discrepancy began and distinguishing basis, at-risk, and passive-activity suspensions.",
        "takeaways": [
            "Trace losses in limitation order rather than combining every suspended amount.",
            "Preserve activity groupings and ownership changes across all years.",
            "A disposition releases passive losses only when the applicable requirements are met.",
        ],
        "sections": [
            ("Find the first year that does not reconcile", """
<p>Collect Forms 8582, Schedules E, K-1s, basis schedules, at-risk forms, and activity grouping statements for every relevant year. Roll the beginning carryforward plus current passive income and loss to the ending carryforward. If the number breaks, investigate that year before changing the latest return.</p>
<p>Keep losses separated by activity unless a valid grouping applies. A rental owned directly is not automatically grouped with a partnership interest or operating business. Ownership transfers, conversions between short- and long-term use, and changes in material participation can alter the analysis without erasing prior records.</p>
<p>Compare the federal rollforward with every state carryforward. States may apply different loss rules or begin with a federal amount that was later modified. A federal correction should not overwrite a state balance without a year-by-year reconciliation and an explanation of any conformity difference.</p>"""),
            ("Separate three different limitations", """
<p>Basis generally limits pass-through losses before the at-risk and passive-activity rules. The at-risk rules can suspend amounts even when tax basis exists. Form 8582 then measures passive loss use. A spreadsheet that labels all three categories “PAL” can release deductions at the wrong time.</p>
<p>For direct rental property, confirm debt, contributions, refinancings, and distributions where relevant. For an entity interest, use the entity-specific basis and debt allocation records. Correcting one limitation may change the amount reaching the next.</p>"""),
            ("Example: carryforward omitted after a software migration", """
<p>An investor changes preparers, and $70,000 of prior suspended rental losses does not migrate into the new software. The current return shows no carryforward. Before adding $70,000, the reviewer reconciles prior-year activity, checks basis and at-risk status, verifies no taxable disposition occurred, and confirms that the activity was not grouped with another property.</p>
<p>If the omission affected a filed return, the correction plan considers that year's amendment, any later years that used the wrong opening balance, state carryforwards, and whether the loss changes current tax or remains suspended.</p>"""),
            ("Carryforward reconstruction package", """
<ul><li>Year-by-year activity rollforward</li><li>Basis and at-risk schedules kept separate</li><li>Form 8582 worksheets and grouping elections</li><li>Ownership and disposition records</li><li>Federal and state amendment map</li><li>Correct opening balances for the next return</li></ul>
<p><a href="/discovery/">Book a passive-loss reconstruction review</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/publications/p925", "IRS Publication 925"),
            ("https://www.irs.gov/forms-pubs/about-form-8582", "IRS Form 8582"),
            ("https://www.irs.gov/instructions/i8582", "IRS Instructions for Form 8582"),
        ],
        "related": ["amend-schedule-e-rental-property", "corrected-k1-after-amended-1120s", "missed-depreciation-rental-property"],
    },
    {
        "slug": "depreciation-schedule-review",
        "title": "Depreciation Schedule Review | AE Tax Advisors",
        "h1": "Depreciation Schedule Review for Business and Rental Returns",
        "description": "Audit a depreciation schedule for basis, land, recovery period, convention, bonus treatment, dispositions, and Form 3115 opportunities.",
        "section": "Depreciation Review",
        "lead": "A depreciation review reconciles the tax asset ledger to actual purchases, improvements, disposals, prior returns, and the general ledger. It should identify both missed deductions and overstated deductions before recommending a cost segregation study, amendment, or accounting-method change.",
        "takeaways": [
            "Tie every material asset to acquisition and placed-in-service evidence.",
            "Test basis, class life, convention, method, bonus, business use, and disposition status separately.",
            "Quantify future and sale consequences, not only the current deduction difference.",
        ],
        "sections": [
            ("Reconcile completeness and ownership", """
<p>Compare the depreciation schedule with the fixed-asset general ledger, closing statements, capital-expenditure accounts, property tax records, insurance schedules, and disposal proceeds. Identify assets that appear in the books but not the return, assets depreciated twice, and assets that were sold or abandoned but remain on the schedule.</p>
<p>Confirm which taxpayer owns each asset. A building held by a partnership should not appear on a shareholder's direct Schedule E. Tenant improvements, leased equipment, and property transferred between related entities require contract and ownership review.</p>
<p>Review construction-in-progress and deposits separately. Paying an invoice does not always place an asset in service, and an asset can be ready for use before the final vendor payment clears. The schedule should capture the operational date supported by the facts rather than defaulting to the check date.</p>"""),
            ("Test the tax attributes", """
<p>For each asset, verify depreciable basis, land allocation, placed-in-service date, recovery period, method, convention, bonus percentage, Section 179 treatment, listed-property limits, and business-use percentage. Review whether qualified improvement property or land improvements were classified correctly. A cost segregation report should tie to this ledger rather than create a parallel one.</p>
<p>Then test accumulated depreciation and remaining basis. Compare prior returns with the schedule to catch migrations where software imported original cost but lost bonus depreciation or prior dispositions.</p>"""),
            ("Classify the remedy", """
<p>A current-year bookkeeping fix may be enough for an asset that was never placed in service. A mathematical or posting error may be amendable. A repeated impermissible depreciation method may require Form 3115. A missed election may have its own relief procedure. The review should assign a procedural category and authority to every material finding.</p>
<p>Also model limitations. Accelerated depreciation from a rental can remain suspended under basis, at-risk, or passive-loss rules. A large catch-up adjustment may not create current cash savings, but the corrected schedule can still matter for later income and disposition reporting.</p>"""),
            ("Deliverable and booking", """
<ul><li>Reconciled old and proposed asset ledgers</li><li>Issue log with source document and tax authority</li><li>Current, future, and disposition tax effects</li><li>Amendment, Form 3115, or prospective correction recommendation</li><li>State conformity analysis</li><li>Implementation checklist for the return preparer</li></ul>
<p><a href="/discovery/">Book a depreciation schedule and return review</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/publications/p946", "IRS Publication 946"),
            ("https://www.irs.gov/forms-pubs/about-form-4562", "IRS Form 4562"),
            ("https://www.irs.gov/forms-pubs/about-form-3115", "IRS Form 3115"),
        ],
        "related": ["business-tax-return-second-opinion", "form-3115-vs-amended-return-cost-segregation", "wrong-rental-depreciation-basis"],
    },
    {
        "slug": "converted-home-rental-depreciation-basis",
        "title": "Converted Home Rental Depreciation Basis | AE Tax",
        "h1": "Depreciation Basis When a Home Becomes a Rental",
        "description": "Calculate and correct depreciation basis when a former personal residence becomes a rental, including value, land, improvements, and sale effects.",
        "section": "Rental Return Corrections",
        "lead": "When a former personal residence becomes a rental, depreciation generally begins when it is ready and available for rent. The depreciation basis can be limited by fair market value at conversion and must exclude land, while the basis used for a later gain or loss calculation can follow different rules.",
        "takeaways": [
            "Document adjusted basis and fair market value at the conversion date.",
            "Allocate land after applying the correct conversion-basis rule.",
            "Maintain separate depreciation and eventual sale-basis workpapers.",
        ],
        "sections": [
            ("Establish the conversion date", """
<p>The key date is when the property becomes ready and available for rent, not simply when the owner moves out or signs with a property manager. Preserve listings, photographs, permits, utility records, repair completion, and the first lease. A property undergoing a major renovation may not yet be in service even if the owner intends to rent it.</p>
<p>Divide expenses between personal and rental periods. Pre-conversion personal expenses do not become rental deductions because the property later produces income. Capital improvements can adjust basis, while ordinary repairs after the property enters service follow their own analysis.</p>"""),
            ("Compute the depreciation starting point", """
<p>For converted property, federal rules generally compare adjusted basis and fair market value at conversion for depreciation and loss purposes. After determining the applicable amount, allocate a supportable portion to nondepreciable land. Improvements made after conversion are separately capitalized and placed in service when ready for use.</p>
<p>Use a contemporaneous appraisal or other support for conversion-date value. A current online estimate created years later is weaker evidence. Reconcile original purchase price, acquisition costs, improvements, casualty adjustments, and any prior credits affecting basis.</p>
<p>If only part of the home becomes a rental, document the square footage and shared areas used for the allocation. A basement unit, accessory dwelling unit, or seasonal rental period may require both space and time allocations. The appraisal should identify the portion valued rather than assume the whole residence entered service.</p>"""),
            ("Example: value declined before conversion", """
<p>An owner purchased a home for $550,000, made $30,000 of capital improvements, and converted it when fair market value was $500,000. If adjusted basis before conversion exceeds fair market value, the lower value can limit the depreciation starting point. A land allocation is then applied to the relevant amount, not automatically to the original purchase price.</p>
<p>If the filed return instead depreciated the original cost without regard to conversion value or land, reconstruct the schedule and determine whether an amended return or accounting-method correction applies. Preserve a separate gain/loss basis schedule for the eventual sale.</p>"""),
            ("Conversion file", """
<ul><li>Original closing statement and improvement records</li><li>Conversion-date valuation</li><li>Evidence of ready-and-available status</li><li>Land allocation support</li><li>Filed and corrected depreciation schedules</li><li>Personal-use and rental-use calendar</li></ul>
<p><a href="/discovery/">Book a converted-rental basis review</a>.</p>"""),
        ],
        "sources": [
            ("https://www.irs.gov/publications/p527", "IRS Publication 527"),
            ("https://www.irs.gov/publications/p551", "IRS Publication 551"),
            ("https://www.irs.gov/publications/p946", "IRS Publication 946"),
        ],
        "related": ["wrong-rental-depreciation-basis", "missed-depreciation-rental-property", "amend-schedule-e-rental-property"],
    },
]

# These concepts already have established, indexable AE URLs.  Keep those URLs
# authoritative instead of publishing near-duplicates that would split links,
# relevance, and crawl signals.
SKIP_SLUGS = {
    "amend-s-corporation-return",
    "amended-c-corporation-return",
    "business-tax-return-second-opinion",
    "form-3115-vs-amended-return-cost-segregation",
    "depreciation-schedule-review",
    "converted-home-rental-depreciation-basis",
    "missed-depreciation-rental-property",
}
PAGES = [page for page in PAGES if page["slug"] not in SKIP_SLUGS]

EXISTING_GUIDES = {
    "amend-s-corporation-return": ("/amend-s-corporation-tax-return/", "How to amend an S corporation tax return"),
    "amended-c-corporation-return": ("/amend-c-corporation-tax-return/", "How to amend a C corporation tax return"),
    "business-tax-return-second-opinion": ("/business-tax-second-opinion/", "Business tax second-opinion review"),
    "form-3115-vs-amended-return-cost-segregation": ("/amended-return-vs-form-3115/", "Amended return versus Form 3115"),
    "depreciation-schedule-review": ("/depreciation-and-fixed-asset-review-for-rental-properties/", "Rental depreciation and fixed-asset review"),
    "converted-home-rental-depreciation-basis": ("/blog/rental-property-converted-home-basis/", "Basis when a home becomes a rental"),
    "missed-depreciation-rental-property": ("/blog/form-3115-missed-depreciation/", "Claim missed depreciation with Form 3115"),
}


def source_block(sources: list[tuple[str, str]]) -> str:
    links = "".join(f'<li><a href="{url}">{label}</a></li>' for url, label in sources)
    return section(
        "Primary sources and editorial review",
        f"""<p>This guide was prepared under the <a href="/editorial-policy/">AE Tax Advisors editorial policy</a>. Tax procedures can change, and the correct filing method depends on the return year and facts. Review the current forms and instructions before filing.</p><ul>{links}</ul>""",
    )


def render_page(page: dict) -> str:
    path = f'/{page["slug"]}/'
    content = [
        page_header(
            h1=page["h1"],
            subtitle=page["description"],
            trail=[("Home", "/"), ("Amended Business Returns", HUB), (page["h1"], path)],
            cta="Book a Return Review Call",
        ),
        section("The short answer", definition(page["lead"])),
        takeaways(page["takeaways"]),
    ]
    content.extend(section(head, body) for head, body in page["sections"])
    content.append(source_block(page["sources"]))
    related = [(HUB, "Amended business returns and depreciation corrections")]
    by_slug = {p["slug"]: p for p in PAGES}
    for slug in page["related"]:
        if slug in by_slug:
            related.append((f'/{slug}/', by_slug[slug]["h1"]))
        elif slug in EXISTING_GUIDES:
            related.append(EXISTING_GUIDES[slug])
    related.extend([
        ("/resources/amendment-self-assessment/", "Amendment self-assessment"),
        ("/blog/how-far-back-can-i-amend-a-tax-return/", "How far back a return can be amended"),
    ])
    content.append(related_section(related))
    schemas = [
        article_schema(
            title=page["h1"], description=page["description"], url=f"{SITE}{path}",
            published=DATE, modified=DATE, section=page["section"],
            keywords=[page["h1"], "amended business return", "tax return correction"],
            citations=[url for url, _ in page["sources"]],
        ),
        breadcrumb_schema([("Home", "/"), ("Amended Business Returns", HUB), (page["h1"], path)]),
    ]
    return build_page(
        title=page["title"], description=page["description"], path=path,
        body="\n".join(content), schemas=schemas, published=DATE, modified=DATE,
        active_nav="/services/",
    )


def render_hub() -> str:
    cards = []
    groups = [
        ("Business return corrections", "Business Return Amendments"),
        ("Cost segregation and method changes", "Cost Segregation Corrections"),
        ("Rental return corrections", "Rental Return Corrections"),
        ("Review before filing", "Business Return Review"),
        ("Depreciation controls", "Depreciation Review"),
    ]
    for heading, category in groups:
        matching = [p for p in PAGES if p["section"] == category]
        if not matching:
            continue
        items = "".join(
            f'<li><a href="/{p["slug"]}/"><strong>{p["h1"]}</strong></a><br>{p["description"]}</li>'
            for p in matching
        )
        cards.append(section(heading, f"<ul class=\"related-links\">{items}</ul>"))
    intro = page_header(
        h1="Amended Business Returns and Depreciation Corrections",
        subtitle="A practical decision center for correcting Forms 1120-S, 1065, 1120, K-1s, rental depreciation, and cost segregation implementation.",
        trail=[("Home", "/"), ("Amended Business Returns", HUB)],
        cta="Book a Return Review Call",
    )
    body = [intro, section("Choose the filing problem, not just the form", """
<p>A correction can be a conventional amendment, a superseding return, a BBA partnership administrative adjustment request, or an accounting-method change. The right path depends on the entity, filing date, depreciation history, ownership, and error. This hub separates those workflows so a business owner can identify the records, affected returns, and professional review required before filing.</p>
<p>AE Tax Advisors reviews the entity return, owner reporting, fixed assets, and state consequences together. Every guide below is built around a distinct procedure or fact pattern rather than a keyword variation.</p>"""),
        takeaways([
            "Correct the source books and schedules before changing a tax form.",
            "Trace entity changes through K-1s, owner returns, carryforwards, and states.",
            "Use Form 3115 only when the accounting-method rules support it.",
            "Quantify unfavorable corrections and future effects as well as refunds.",
        ])]
    body.extend(cards)
    body.append(source_block([
        ("https://www.irs.gov/businesses/corporations/amended-and-superseding-corporate-returns", "IRS amended corporate return guidance"),
        ("https://www.irs.gov/businesses/partnerships/file-an-administrative-adjustment-request-for-a-bba-partnership", "IRS partnership AAR guidance"),
        ("https://www.irs.gov/forms-pubs/about-form-3115", "IRS Form 3115"),
    ]))
    schemas = [
        {
            "@context": "https://schema.org", "@type": "CollectionPage",
            "name": "Amended Business Returns and Depreciation Corrections",
            "description": "AE Tax Advisors guides for business-return amendments, K-1 corrections, rental depreciation, and Form 3115.",
            "url": f"{SITE}{HUB}",
            "publisher": {"@type": "Organization", "name": "AE Tax Advisors", "url": f"{SITE}/"},
        },
        breadcrumb_schema([("Home", "/"), ("Amended Business Returns", HUB)]),
    ]
    return build_page(
        title="Amended Business Returns | AE Tax Advisors",
        description="Review amended business returns, corrected K-1s, partnership AARs, rental depreciation errors, and Form 3115 implementation.",
        path=HUB, body="\n".join(body), schemas=schemas,
        published=DATE, modified=DATE, active_nav="/services/",
    )


def visible_words(markup: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", html.unescape(re.sub(r"<[^>]+>", " ", markup))))


def validate(rendered: dict[str, str]) -> None:
    titles = [p["title"] for p in PAGES]
    descriptions = [p["description"] for p in PAGES]
    if len(titles) != len(set(titles)) or len(descriptions) != len(set(descriptions)):
        raise ValueError("duplicate title or meta description in return-correction cluster")
    for page in PAGES:
        text = rendered[page["slug"]]
        main = re.search(r"<main[^>]*>(.*?)</main>", text, re.S).group(1)
        if visible_words(main) < 600:
            raise ValueError(f'{page["slug"]}: fewer than 600 main-content words')
        if text.count('/discovery/') < 2:
            raise ValueError(f'{page["slug"]}: missing direct booking paths')
        if len(page["sources"]) < 2:
            raise ValueError(f'{page["slug"]}: insufficient primary sources')
    # A high token-set overlap catches pages that differ mainly by swapped nouns.
    token_sets = {}
    stop = set("the and for with from that this into your return tax business amended guide".split())
    for page in PAGES:
        main = re.search(r"<main[^>]*>(.*?)</main>", rendered[page["slug"]], re.S).group(1)
        words = set(re.findall(r"[a-z]{4,}", re.sub(r"<[^>]+>", " ", main.lower()))) - stop
        token_sets[page["slug"]] = words
    for i, left in enumerate(PAGES):
        for right in PAGES[i + 1:]:
            a, b = token_sets[left["slug"]], token_sets[right["slug"]]
            overlap = len(a & b) / max(1, len(a | b))
            if overlap > 0.58:
                raise ValueError(f'excessive topical overlap {overlap:.2f}: {left["slug"]} / {right["slug"]}')


def inject_hub_link(path: Path, marker: str) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    if marker in text:
        text = text.replace('/amended-business-tax-returns/', HUB)
        path.write_text(text, encoding="utf-8")
        return
    block = f'''<!-- {marker} --><section class="content-section fade-in-section"><div class="container narrow"><h2>Business Return Corrections</h2><p>Use the <a href="{HUB}">amended business return and depreciation correction center</a> to compare amended returns, corrected K-1s, partnership AARs, and Form 3115 procedures. For a return-specific review, <a href="/discovery/">book a call with AE Tax Advisors</a>.</p></div></section>'''
    text = text.replace("</main>", block + "\n</main>", 1)
    path.write_text(text, encoding="utf-8")


def inject_existing_hub() -> None:
    """Turn the established service URL into the cluster's navigation hub."""
    path = ROOT / HUB.strip("/") / "index.html"
    text = path.read_text(encoding="utf-8")
    marker = "<!-- correction-decision-center:start -->"
    end = "<!-- correction-decision-center:end -->"
    items = "".join(
        f'<li><a href="/{page["slug"]}/"><strong>{page["h1"]}</strong></a> — {page["description"]}</li>'
        for page in PAGES
    )
    established = "".join(
        f'<li><a href="{href}">{label}</a></li>'
        for href, label in EXISTING_GUIDES.values()
    )
    block = f'''{marker}<section class="content-section fade-in-section"><div class="container narrow"><h2>Business Return Correction Decision Center</h2><p>Choose the filing problem that matches the facts. These guides separate entity amendments, partnership AARs, corrected K-1s, accounting-method changes, rental depreciation errors, and state follow-up so each URL answers a distinct decision.</p><h3>Filing-specific long-tail guides</h3><ul class="related-links">{items}</ul><h3>Established correction guides</h3><ul class="related-links">{established}</ul><p><a href="/discovery/" class="btn-cta">Book a Return Review Call</a></p></div></section>{end}'''
    if marker in text:
        text = re.sub(re.escape(marker) + r".*?" + re.escape(end), block, text, flags=re.S)
    else:
        text = text.replace("</main>", block + "\n</main>", 1)
    path.write_text(text, encoding="utf-8")


WINNER_LINKS = {
    "blog/how-long-does-an-amended-tax-return-take-to-process/index.html": [
        (HUB, "Amended business return decision center"),
        ("/amend-s-corporation-tax-return/", "How to amend an S corporation return"),
        ("/partnership-aar-vs-amended-return/", "Partnership AAR versus amended Form 1065"),
    ],
    "blog/how-far-back-can-i-amend-a-tax-return/index.html": [
        (HUB, "Amended business return decision center"),
        ("/superseding-vs-amended-business-return/", "Superseding versus amended business returns"),
        ("/business-tax-second-opinion/", "Business return second-opinion review"),
    ],
    "form-3115-cost-segregation/index.html": [
        ("/amended-return-vs-form-3115/", "Form 3115 versus an amended return"),
        ("/catch-up-depreciation-section-481a/", "Section 481(a) catch-up depreciation"),
        ("/cost-segregation-after-extension-deadline/", "Cost segregation after the filing deadline"),
    ],
    "form-3115-cost-segregation-lookback/index.html": [
        ("/amended-return-vs-form-3115/", "Choose Form 3115 or an amended return"),
        ("/depreciation-and-fixed-asset-review-for-rental-properties/", "Depreciation schedule review"),
        ("/blog/form-3115-missed-depreciation/", "Correct missed rental depreciation"),
    ],
    "blog/macrs-depreciation-schedule-explained/index.html": [
        ("/depreciation-and-fixed-asset-review-for-rental-properties/", "Review a depreciation schedule for errors"),
        ("/wrong-rental-depreciation-basis/", "Correct an incorrect rental depreciation basis"),
        ("/catch-up-depreciation-section-481a/", "Understand Section 481(a) catch-up depreciation"),
    ],
    "blog/what-is-real-estate-professional-status-and-how-do-i-qualify/index.html": [
        ("/passive-loss-carryforward-correction/", "Correct a passive-loss carryforward"),
        ("/amend-schedule-e-rental-property/", "Correct Schedule E rental reporting"),
        ("/blog/form-3115-missed-depreciation/", "Correct missed rental depreciation"),
    ],
    "blog/can-i-use-cost-segregation-to-offset-w2-income/index.html": [
        ("/passive-loss-carryforward-correction/", "Reconstruct passive losses before using them"),
        ("/amended-return-vs-form-3115/", "Implement prior-year cost segregation correctly"),
        ("/depreciation-and-fixed-asset-review-for-rental-properties/", "Review the depreciation schedule"),
    ],
    "cost-segregation-calculator/index.html": [
        ("/depreciation-and-fixed-asset-review-for-rental-properties/", "Validate the tax inputs behind an estimate"),
        ("/amended-return-vs-form-3115/", "Choose the filing method for a prior-year property"),
        ("/catch-up-depreciation-section-481a/", "Calculate catch-up depreciation"),
    ],
    "amend-s-corporation-tax-return/index.html": [
        ("/corrected-k1-after-amended-1120s/", "Corrected K-1 after an amended Form 1120-S"),
        ("/superseding-vs-amended-business-return/", "Superseding versus amended business returns"),
        ("/amended-business-return-state-filings/", "State filings after a federal amendment"),
    ],
    "amend-c-corporation-tax-return/index.html": [
        ("/superseding-vs-amended-business-return/", "Superseding versus amended business returns"),
        ("/amended-business-return-state-filings/", "State filings after a federal amendment"),
        ("/business-tax-second-opinion/", "Review the correction before filing"),
    ],
    "amended-return-vs-form-3115/index.html": [
        ("/catch-up-depreciation-section-481a/", "Section 481(a) catch-up depreciation"),
        ("/cost-segregation-after-extension-deadline/", "Cost segregation after the extension deadline"),
        ("/wrong-rental-depreciation-basis/", "Correct the wrong rental depreciation basis"),
    ],
    "business-tax-second-opinion/index.html": [
        (HUB, "Business return correction decision center"),
        ("/partnership-aar-vs-amended-return/", "Partnership AAR versus an amended return"),
        ("/amended-business-return-state-filings/", "Review state amendment exposure"),
    ],
    "depreciation-and-fixed-asset-review-for-rental-properties/index.html": [
        ("/wrong-rental-depreciation-basis/", "Correct the wrong rental depreciation basis"),
        ("/catch-up-depreciation-section-481a/", "Section 481(a) catch-up depreciation"),
        ("/passive-loss-carryforward-correction/", "Correct passive-loss carryforwards"),
    ],
    "blog/rental-property-converted-home-basis/index.html": [
        ("/wrong-rental-depreciation-basis/", "Correct the wrong rental depreciation basis"),
        ("/amend-schedule-e-rental-property/", "Correct Schedule E rental reporting"),
        ("/passive-loss-carryforward-correction/", "Correct passive-loss carryforwards"),
    ],
    "blog/form-3115-missed-depreciation/index.html": [
        ("/catch-up-depreciation-section-481a/", "Understand the Section 481(a) adjustment"),
        ("/amended-return-vs-form-3115/", "Compare Form 3115 with an amended return"),
        ("/cost-segregation-after-extension-deadline/", "Implement a late cost-segregation study"),
    ],
}


def inject_winner_links() -> None:
    for rel, links in WINNER_LINKS.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        marker = "<!-- data-driven-correction-links:start -->"
        end = "<!-- data-driven-correction-links:end -->"
        items = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in links)
        block = f'''{marker}<section class="content-section fade-in-section"><div class="container narrow"><h2>Correcting a Filed Return or Depreciation Schedule</h2><p>Use these filing-specific guides when the return is already filed or the depreciation history is incomplete.</p><ul class="related-links">{items}</ul><p><a href="/discovery/" class="btn-cta">Book a Return Review Call</a></p></div></section>{end}'''
        if marker in text:
            text = re.sub(re.escape(marker) + r".*?" + re.escape(end), block, text, flags=re.S)
        else:
            text = text.replace("</main>", block + "\n</main>", 1)
        path.write_text(text, encoding="utf-8")


def main() -> None:
    rendered = {p["slug"]: render_page(p) for p in PAGES}
    validate(rendered)
    for page in PAGES:
        write_page(f'/{page["slug"]}/', rendered[page["slug"]])
    inject_existing_hub()
    inject_hub_link(ROOT / "tax-compliance-irs-representation" / "index.html", "return-correction-cluster")
    inject_hub_link(ROOT / "guides" / "business-tax-questions" / "index.html", "return-correction-cluster")
    inject_hub_link(ROOT / "resources" / "index.html", "return-correction-cluster")
    inject_winner_links()
    print(f"Generated {len(PAGES)} distinct correction guides and enhanced the established cluster hub")


if __name__ == "__main__":
    main()
