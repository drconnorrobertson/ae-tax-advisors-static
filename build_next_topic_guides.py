#!/usr/bin/env python3
"""Publish focused STR and cost segregation decision guides, with hub links."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

import seo_render

ROOT = Path(__file__).resolve().parent
seo_render.BASE = "https://www.aetaxadvisors.com"
DATE = "2026-09-22"

GUIDES = [
    dict(
        slug="str-spouse-cohost-material-participation-hours",
        title="Can Spouse and Co-Host Hours Count for STR Material Participation?",
        description="Learn whose hours count toward short-term rental material participation, how co-host work affects the 100-hour test, and what records to keep.",
        category="Short-Term Rentals",
        hub="str",
        lead="A short-term rental can fall outside the passive-activity definition of a rental when the average customer stay meets an exception. That alone does not make its loss nonpassive: the owner must still establish material participation in the activity.",
        body="""
<h2>Separate the customer-stay test from the participation test</h2>
<p>Under the passive-activity rules, an activity with average customer use of seven days or less is generally not treated as a rental activity. Certain activities with average use of 30 days or less and significant personal services may also qualify for an exception. Compute the average from actual rental periods; a listing's minimum-night setting is not the calculation. Only after identifying the activity and its classification should the owner analyze material participation.</p>
<p>There are seven material-participation tests. Two commonly discussed STR paths are participation exceeding 500 hours, or participation exceeding 100 hours and at least as much as any other individual. Those are annual tests of the taxpayer's participation in the activity, not thresholds per booking. Hours alone do not decide basis, at-risk, business-use, or other loss limitations.</p>
<h2>Spouse hours and co-host hours work differently</h2>
<p>The IRS counts a spouse's participation with the taxpayer's participation, even if the spouse owns no interest and the couple does not file jointly. Record each spouse's date, task, property, and time without double-counting work they did together. A co-host's work is not the owner's participation. For the 100-hour test, the comparison is to any other individual, including a property manager or co-host, so their hours can prevent an owner from satisfying that particular test.</p>
<p>Ask the manager for a task or time report rather than assuming that a percentage-of-revenue management fee proves a number of hours. Cleaners and maintenance vendors are also individuals whose work can be relevant to the comparison. Whether activities can be grouped is a separate factual and regulatory question; do not combine multiple properties merely because the same owner holds them or the same app lists them.</p>
<h2>What work should the log distinguish?</h2>
<p>Operating work can include guest communication, scheduling cleaners, direct maintenance, restocking, and active management. Investor work such as reviewing financial statements or monitoring performance in a nonmanagerial capacity generally does not count unless the owner is directly involved in day-to-day management or operations. Commuting, duplicated estimates, and reconstructed round numbers invite questions. Record start and end times, a concrete task, the property, and corroboration such as messages, invoices, calendars, or access logs.</p>
<h2>Illustrative annual comparison</h2>
<p>Assume one spouse performs 78 hours of guest and maintenance work and the other performs 64, for 142 combined hours. The co-host performs 150 hours and no other test applies. The owners may fail the 100-hour/more-than-anyone-else test because one individual worked more than their combined participation. If the co-host instead worked 95 hours and no other individual exceeded 142, the comparison could be satisfied, assuming all owner hours qualify and the activity is defined correctly. This example does not determine the return without the remaining limitations.</p>
<h2>Build evidence during the year</h2>
<p>Export booking history, task-management records, platform messages, cleaner schedules, maintenance invoices, and co-host statements quarterly. Reconcile the time log to these records. Keep a separate schedule of guest stays for the average-use test. A year-end spreadsheet reconstructed from memory is much weaker than contemporaneous records. IRS <a href="https://www.irs.gov/publications/p925">Publication 925</a> explains the stay exceptions, spouse participation, investor activities, and proof of participation.</p>
<p><a href="/assets/str-participation-log-template.csv" download>Download a blank STR participation log (CSV)</a>. Enter each person and task separately, with a source record such as a guest message, calendar event, invoice, or vendor report. The blank template is a recordkeeping aid; the tax treatment of an hour still depends on the actual work and activity facts.</p>
<p>For the overall planning sequence, see <a href="/short-term-rental-tax-strategy/">short-term rental tax strategy</a> and <a href="/blog/how-to-track-material-participation-hours-for-str/">how to track participation hours</a>. The latter covers the basic log; this guide focuses on the spouse and outside-manager comparison.</p>
""",
    ),
    dict(
        slug="str-personal-use-maintenance-days-tax",
        title="Do STR Maintenance Days Count as Personal Use?",
        description="Vacation-home rules can limit STR deductions. Learn when owner stays, family stays, and substantial maintenance days count as personal use.",
        category="Short-Term Rentals",
        hub="str",
        lead="An owner visit to a short-term rental can be a personal-use day, a repair-and-maintenance day, or a day with mixed facts. The label on a calendar does not decide the tax treatment.",
        body="""
<h2>First determine whether vacation-home rules apply</h2>
<p>A dwelling unit used personally and rented to others may be treated as a home if personal use exceeds the greater of 14 days or 10% of fair-rental days. When that happens, rental expense deductions can be limited. A separate rule applies when a home is rented for fewer than 15 days in the year. These rules should be analyzed before assuming that a passive-activity exception allows a loss to offset salary.</p>
<p>Fair-rental days and personal days are not the same as available nights. Empty nights listed on Airbnb are not days actually rented for the expense-allocation fraction described in IRS Publication 527. Guest stays at a substantial discount can be personal-use days. Use by family members or co-owners can count as personal use under the publication's rules even when the owner did not personally stay.</p>
<h2>Maintenance days have a specific exception</h2>
<p>A day spent working substantially full time repairing and maintaining the property is not counted as personal use, even if family members also use it for recreation that day. The actual work and main purpose of the trip matter. Publication 527 distinguishes repairs and maintenance from improving the property. Calling a bathroom remodel “maintenance” does not turn an improvement trip into exempt maintenance days.</p>
<p>The exclusion of a maintenance day from personal use does not automatically make it a day rented at a fair price. For the basic expense-allocation fraction, track actual rented days and personal days separately. Keep invoices, photographs, schedules, and receipts showing what was done. A vague note saying “worked on cabin” is difficult to evaluate when the family also used the cabin for a holiday.</p>
<h2>Illustrative calendar</h2>
<p>Assume a cottage is rented at fair value for 120 days. The owner vacations there 12 days, a sibling uses it free for 5 days, and the owner spends 4 days substantially full time repairing a deck. The 17 vacation and family days may be personal-use days; the 4 documented repair days are not personal-use days under the maintenance exception. Because 17 is greater than 14 and greater than 10% of 120, the cottage may be treated as a home for the limitation. Different facts could change the count, including whether the deck work was an improvement.</p>
<h2>Keep three separate records</h2>
<p>Use a guest-stay ledger for fair-rental days, an owner/family-use calendar for personal days, and a work log for maintenance visits. Record the participants, task, hours, and supporting invoice or photo. If a day has both fair-rental and personal use, Publication 527 gives special instructions for the home-use test; do not automatically put it in the same bucket for every calculation. A property used solely as a hotel-like establishment may also require a different threshold analysis, so establish the property's facts first.</p>
<p>See IRS <a href="https://www.irs.gov/publications/p527">Publication 527, chapter 5</a> for the personal-use, maintenance, and allocation rules. For adjacent STR questions, read <a href="/short-term-rental-tax-strategy/">the STR planning guide</a> and <a href="/blog/rental-property-partial-personal-use/">mixed personal and rental use</a>.</p>
""",
    ),
    dict(
        slug="cost-segregation-partial-disposition-renovation",
        title="Cost Segregation and Partial Dispositions During Renovation",
        description="Replacing a roof, HVAC system, or other component can leave old basis on the books. Learn when a partial-disposition election and cost study should be coordinated.",
        category="Cost Segregation",
        hub="costseg",
        lead="When an owner replaces a building component, the new component may be capitalized while the old component's unrecovered basis remains on the depreciation schedule. A partial-disposition analysis can address that overlap, but it requires evidence of what was retired and its adjusted basis.",
        body="""
<h2>Identify the retired component, not just the new invoice</h2>
<p>A renovation invoice shows the cost of the new roof, HVAC system, or interior work. It does not by itself establish the basis of the old component. The owner needs to determine whether a portion of a MACRS asset was actually disposed of, the original component's placed-in-service date, its unadjusted basis, depreciation taken, and adjusted basis at retirement. A building addition without removal of an old component is not automatically a partial disposition.</p>
<p>For qualifying elective partial dispositions, IRS Form 4797 instructions say the election is made on a timely filed return, including extensions, for the year of disposition. Some partial dispositions must be reported. A late decision can therefore be consequential; the tax team should flag component removals during project planning, not only when the return is due.</p>
<h2>Where the cost segregation study helps</h2>
<p>An existing engineering-based study may have identified the cost and classification of the old component. That can make the retirement basis more supportable. If there is no study, the preparer may need an appropriate method to estimate the historical cost of the removed portion and reconcile it to original building basis. The new improvement is then analyzed separately under the capitalization and depreciation rules. Avoid counting the removed component in both old and new schedules.</p>
<p>The IRS's <a href="https://www.irs.gov/pub/fatca/int_practice_units/examining-tp-electing-partial-disposition.pdf">partial-disposition practice unit</a> asks whether the taxpayer can substantiate ownership, actual disposition, placed-in-service date, adjusted basis, and a reduction of the remaining asset's basis. These are concrete workpaper requirements, not just an election label.</p>
<h2>Illustrative roof replacement</h2>
<p>Assume a landlord replaces an entire old roof with a $90,000 roof. The old roof's reconstructed original cost is $45,000, and $20,000 of depreciation was allowed or allowable on that component. A simplified adjusted basis of $25,000 may be evaluated for a partial-disposition loss if the facts and election requirements are satisfied. The $90,000 new roof is still analyzed as a capital improvement and depreciated under its proper class. This example omits transaction and accounting-method details; it is not an automatic $25,000 deduction.</p>
<h2>Build a before-and-after asset roll-forward</h2>
<p>Keep demolition records, photographs before and after, contractor scope, invoices identifying removed components, original acquisition or construction documents, the existing depreciation schedule, and the method used to estimate old cost. Reconcile old basis removed, accumulated depreciation removed, new capitalized cost, and remaining basis. If a study is commissioned after renovation, provide pre-project photos and plans; an inspection of the finished building alone may not show what was removed.</p>
<p>IRS <a href="https://www.irs.gov/publications/p544">Publication 544</a> and the <a href="https://www.irs.gov/instructions/i4797">Form 4797 instructions</a> discuss partial dispositions. See <a href="/cost-segregation-study/">the cost segregation guide</a> and <a href="/blog/what-repairs-vs-improvements-can-i-deduct-on-rental-property/">repairs versus improvements</a> for the surrounding decisions.</p>
""",
    ),
    dict(
        slug="cost-segregation-study-audit-ready-deliverables",
        title="What Should an Audit-Ready Cost Segregation Study Include?",
        description="Use the IRS cost segregation audit guide to evaluate methodology, asset schedules, site evidence, cost reconciliation, and tax implementation deliverables.",
        category="Cost Segregation",
        hub="costseg",
        lead="A cost segregation study should let a reviewer trace each reclassified asset from the property and cost records to a tax classification and depreciation schedule. A single percentage estimate is not the same as a documented study.",
        body="""
<h2>Start with the scope and the basis to be allocated</h2>
<p>The report should identify the taxpayer, property, acquisition or construction facts, placed-in-service date, and total depreciable basis. It should separate land, building, land improvements, and personal property. For an acquired property, the purchase agreement, closing statement, appraisal if available, and assumptions about the property's condition help support the allocation. For new construction, actual contractor and project cost records should be reconciled before estimating individual assets.</p>
<p>Compare the study total to the owner's fixed-asset ledger and tax return. If those totals do not match, the report should explain the difference. Land and loan costs cannot be silently included in depreciable building basis. For a prior-year property, the report should show how existing depreciation and any accounting-method change are handled rather than presenting only first-year deductions.</p>
<h2>Look for inspectable asset-level evidence</h2>
<p>The IRS <a href="https://www.irs.gov/pub/irs-pdf/p5653.pdf">2025 Cost Segregation Audit Technique Guide</a> describes a quality study as accurate and well documented. It discusses site visits, photographic evidence, construction drawings, contractor records, purchase documents, interviews, cost-estimate methodology, and asset schedules. The amount of evidence varies with the property and available records; the report should explain what was obtained and what had to be estimated.</p>
<p>An asset schedule should name recognizable assets, identify location and use where relevant, show cost and recovery period, and cite the classification basis. A line reading “specialty electrical: $250,000” without an asset description, drawings, or measurement leaves a reviewer unable to tell whether the wiring serves equipment or the building generally. Photographs and plans should map to the asset lines, not sit in an unindexed appendix.</p>
<h2>Reconcile direct and indirect costs</h2>
<p>Engineering estimates need to tie back to the purchase price or total project cost. A study may allocate indirect costs such as design, permits, or contractor overhead among assets using a supportable method. The report should say whether actual costs or estimates were used and why. If the engineer estimates a component at replacement cost, adjustments for age and condition may be needed for an acquired used property. An unexplained percentage of purchase price is weak evidence.</p>
<h2>Ask for implementation, not only a PDF</h2>
<p>The owner should receive a final asset schedule usable for Form 4562 and future dispositions, including class lives, placed-in-service dates, and cost totals. The tax preparer should document any Section 481(a) adjustment and Form 3115 analysis for a method change, as applicable. State conformity and loss-limitation questions belong in a separate tax review. The study's accelerated depreciation figure is not necessarily the owner's usable current-year deduction.</p>
<h2>A five-part acceptance check</h2>
<p>Before accepting a study, confirm: (1) property and basis tie to source documents; (2) site evidence and asset list are specific; (3) classification and cost methods are explained; (4) totals reconcile to prior depreciation schedules; and (5) the tax implementation and future-disposition records are delivered. Ask the preparer to resolve exceptions in writing. This is especially useful when comparing a low-fee desktop estimate with a more detailed study.</p>
<p><a href="/assets/cost-segregation-study-review-checklist.csv" download>Download the study review checklist (CSV)</a> to record the provider's answers and the evidence received. The checklist turns the IRS audit guide's quality concepts into a practical review; it does not replace the property's tax and engineering analysis.</p>
<p>For the broader decision, see <a href="/cost-segregation-study/">cost segregation studies</a> and <a href="/blog/how-to-evaluate-cost-segregation-study/">how to evaluate a study</a>. The IRS audit guide is an examiner resource; it is useful as a quality checklist, not a guarantee that any particular study will be accepted.</p>
""",
    ),
    dict(
        slug="1031-exchange-closing-costs-prorations-boot",
        title="Which 1031 Closing Costs Count as Exchange Expenses?",
        description="A 1031 settlement statement mixes exchange expenses with property tax, rent, security deposits, and loan charges. Learn how to classify each line before computing boot.",
        category="Real Estate Tax Planning",
        hub="realestate",
        lead="A 1031 exchange closing statement can contain dozens of debits and credits. Only qualifying exchange expenses receive the exchange-expense treatment; routine prorations and financing charges need separate analysis.",
        body="""
<h2>Do not use the net wire as the tax result</h2>
<p>When a property is sold through a qualified intermediary, sale proceeds often arrive net of commissions, taxes, loan payoff, rent prorations, and escrow charges. The net amount transferred to the intermediary does not tell you how much taxable boot exists. Start with both final settlement statements and the intermediary's ledger, then classify each line by what it bought or settled.</p>
<p>IRS Publication 544 says exchange expenses generally include closing costs paid on the disposition of relinquished property, such as brokerage commissions, attorney fees, and deed preparation fees. It also says exchange expenses can include closing costs paid on acquisition of replacement property. Publication 551 explains basis treatment on the replacement side. A charge's label is not enough; read the invoice and transaction documents.</p>
<h2>Separate exchange charges from operating items</h2>
<p>Property tax prorations, rent prorations, security deposits, and repairs are examples the IRS explicitly says are not exchange expenses. A security-deposit transfer reflects an obligation to tenants; a prepaid-rent adjustment reflects the right to rental income. These items may affect cash flows and reporting, but they should not be used as an undifferentiated reduction to exchange boot.</p>
<p>Loan origination fees, points, prepaid interest, and lender title charges relate to financing and need separate treatment. A mortgage payoff is debt repayment, not a selling expense. Title charges can include both acquisition and lender components, so request an itemized invoice. The question is not simply whether a cost appears on a closing statement; it is whether the cost is part of exchanging qualifying real property.</p>
<h2>Illustrative cash-boot computation</h2>
<p>Suppose an exchanger receives $20,000 of cash and pays $7,000 of qualifying exchange expenses. In a simplified case with sufficient realized gain, Publication 544's example approach can leave $13,000 as the cash amount considered for recognized gain. If the same $7,000 consisted of loan fees or tax prorations rather than exchange expenses, the calculation could differ. Debt relief and non-like-kind property must also be included in the full exchange worksheet.</p>
<h2>Build a line-by-line closing schedule</h2>
<p>Use columns for each settlement line, property side, payee, contract clause, supporting invoice, proposed tax category, and treatment in Form 8824 or another return schedule. Reconcile the total to the title company's statement and the intermediary's account. Highlight uncertain items for review before the replacement closing; a late correction can change the cash needed to complete the exchange.</p>
<p>Review <a href="/blog/1031-exchange-debt-relief-boot/">debt relief and boot</a> alongside this cost analysis. Primary references are IRS <a href="https://www.irs.gov/publications/p544">Publication 544</a> and <a href="https://www.irs.gov/publications/p551">Publication 551</a>. The <a href="/guides/rental-property-tax-questions/">rental tax hub</a> links the related acquisition and sale questions.</p>
""",
    ),
    dict(
        slug="late-s-corporation-election-relief-form-2553",
        title="What If an S Corporation Election Was Filed Late?",
        description="A late Form 2553 may qualify for IRS relief when the business intended S status and reported consistently. Learn the records, timing, and entity-classification issues.",
        category="Business Tax Planning",
        hub="business",
        lead="Missing the Form 2553 deadline does not always end an intended S election. IRS Revenue Procedure 2013-30 provides a relief process for qualifying late elections, but a business must document its intent and consistent tax reporting.",
        body="""
<h2>Confirm the intended effective date and entity type</h2>
<p>An eligible corporation generally files Form 2553 by the applicable election deadline for the desired effective year. An LLC taxed as a corporation may also need to address its federal entity classification. Before filing for relief, reconstruct the formation date, ownership history, first tax year, intended S effective date, Form 2553 preparation or mailing history, and the returns actually filed. A missed election is different from a valid election later terminated by an ineligible shareholder or other defect.</p>
<h2>Check the IRS relief conditions</h2>
<p>The IRS late-election relief page says Revenue Procedure 2013-30 generally applies when the entity failed to qualify solely because the election was not timely filed, the entity intended S status, and returns were reported consistently with that status. The ordinary timing window is generally within three years and 75 days of the intended effective date, with a narrow exception for certain corporations. An LLC with a related late corporate-classification election has additional conditions.</p>
<p>Do not promise relief based only on the calendar. Verify shareholder eligibility, required consents, the corporation's tax year, and every federal return for the affected period. If owners reported partnership or sole-proprietor income while the corporation filed no Form 1120-S, the consistency issue can be material. If the revenue procedure does not apply, the IRS says a private letter ruling may be the remaining path.</p>
<h2>Illustrative missed filing</h2>
<p>Assume a corporation intended S status beginning January 1, filed Form 1120-S and issued K-1s consistently, and later discovers that Form 2553 was never accepted. It may be able to request late-election relief if all substantive and procedural conditions are met. Compare that with an LLC that filed Schedule C for two years and now wants those years retroactively treated as S corporation years; the consistent-reporting requirement is a different problem. Neither example establishes eligibility without the complete return history.</p>
<h2>Prepare a reviewable relief package</h2>
<p>Collect the formation documents, ownership ledger, shareholder consents, filed Forms 1120-S, K-1s, shareholder returns, payroll filings, IRS notices, and proof of any earlier Form 2553 attempt. The Form 2553 instructions specify the notation “FILED PURSUANT TO REV. PROC. 2013-30” for late filings under that procedure and describe filing methods. Use current IRS instructions when preparing the actual submission and keep proof of delivery and IRS response.</p>
<p>Read the IRS <a href="https://www.irs.gov/businesses/small-businesses-self-employed/late-election-relief">late-election relief page</a>, <a href="https://www.irs.gov/instructions/i2553">Form 2553 instructions</a>, and <a href="https://www.irs.gov/irb/2013-36_IRB">Revenue Procedure 2013-30</a>. The <a href="/guides/business-tax-questions/">business tax hub</a> covers related S corporation owner questions.</p>
""",
    ),
]

CORRECTED_DEPRECIATION_GUIDE = dict(
    slug="str-39-year-recovery-period-nonresidential",
    title="Is a Short-Term Rental 27.5- or 39-Year Property?",
    description="A seven-day average stay does not automatically decide an STR building's depreciation period. Apply the separate residential-rental and transient-lodging rules.",
    category="Short-Term Rentals",
    hub="str",
    lead="The passive-activity seven-day rule and the building depreciation rule answer different questions. A short-term rental's average guest stay can affect passive classification without, by itself, proving a 39-year recovery period for the building.",
    body="""
<h2>Two rules that should not be merged</h2>
<p>For passive-activity purposes, IRS Publication 925 says an activity generally is not a rental activity if average customer use is seven days or less. That exception can make material participation relevant to whether the activity's loss is passive. It does not state the building's depreciation class. A property may also face basis, at-risk, and personal-use limits. Analyze those questions separately rather than treating one booking statistic as a universal tax status.</p>
<p>For depreciation, IRS Publication 946 says residential rental property is a building or structure for which 80% or more of gross rental income comes from dwelling units. Its definition of a dwelling unit excludes a unit in a hotel, motel, or other establishment where more than half the units are used on a transient basis. Residential rental buildings generally have a 27.5-year GDS recovery period; nonresidential real property generally has a 39-year period. The classification turns on the building and its use under this rule, not automatically on the seven-day passive-activity threshold.</p>
<h2>Compare clear cases with the harder STR case</h2>
<p>An apartment building leased to residents on annual terms is a straightforward residential rental example. A hotel with guest rooms predominantly used on a transient basis is a straightforward nonresidential example. A single vacation home rented through a platform can require a closer analysis of the dwelling-unit and transient-establishment language, actual guest use, services, and the property's facts. Avoid assuming that every Airbnb is a hotel or that every house is automatically residential rental property.</p>
<p>The source records should include annual gross rental income, booking lengths, floor plan and unit count, guest policies, services provided, and any mixed personal use. A change from long-term leasing to transient lodging can also call for a change-in-use depreciation analysis. Preserve the original placed-in-service date, basis schedule, and dates the property was used differently.</p>
<h2>How cost segregation fits</h2>
<p>Neither a 27.5-year residential rental building nor a 39-year nonresidential building is itself short-life property for bonus-depreciation purposes. A properly supported cost segregation study may identify separate assets with shorter recovery periods, such as certain tangible personal property and land improvements. The exact class depends on the asset's function and law, not a fixed percentage of the purchase price. The building's base recovery period affects the comparison, but a study can be useful under either classification.</p>
<p>Qualified improvement property is another distinct question. It generally concerns qualifying interior improvements to nonresidential real property after the building was first placed in service, subject to statutory exclusions. Calling an STR nonresidential does not automatically make every renovation QIP. A new roof, building enlargement, and separately classified personal property require their own analysis.</p>
<h2>Illustrative decision paths</h2>
<p>Suppose an owner has 40 bookings totaling 200 guest nights. The average period of customer use is five days for the passive-activity rental exception. The owner still needs a separate building-classification workpaper under Section 168 and Publication 946. If the property meets the residential rental definition, the building may use 27.5 years; if it is an excluded transient lodging establishment, the building may use 39 years. The five-day calculation alone does not settle that choice.</p>
<p>In a second example, a 20-room hotel operates 18 rooms for transient guests and two for longer stays. The transient-establishment exclusion is more directly implicated. The owner still has to identify land, building, and any separate depreciable assets. The examples show how an average-stay result and a building-life result can be documented without treating them as the same test.</p>
<h2>What the tax file should contain</h2>
<p>Write a short memo with the property's facts, the 80% gross-income computation, unit use, why the transient-establishment language does or does not apply, and the resulting building schedule. Separately calculate average customer use for passive-activity purposes and maintain an owner participation log if loss treatment depends on material participation. Keep a third file for any personal-use days. This separation makes a later study, amended return, or property sale easier to review.</p>
<p>Primary references: IRS <a href="https://www.irs.gov/publications/p946">Publication 946</a> for recovery periods and residential-rental classification, and <a href="https://www.irs.gov/publications/p925">Publication 925</a> for the passive-activity stay exception. See <a href="/short-term-rental-tax-strategy/">the STR planning guide</a> and <a href="/blog/cost-segregation-study-audit-ready-deliverables/">the cost segregation documentation guide</a> for related decisions.</p>
""",
)

PRACTICAL_FOLLOW_THROUGH = {
    "str-spouse-cohost-material-participation-hours": """
<h2>Review the log before relying on a loss</h2>
<p>At year-end, compare the owners' combined hours with each outside individual's hours under the intended material-participation test. If a cleaner works for several properties, ask for property-level invoices or schedules rather than allocating all their time to one address. Document who decided prices, accepted bookings, assigned work, and resolved guest issues; that helps distinguish direct management from investor oversight. Review the property's basis and debt schedule in the same meeting, because passing a participation test does not make a loss deductible when another limitation applies.</p>
""",
    "str-personal-use-maintenance-days-tax": """
<h2>Do not confuse owner work with guest-use classification</h2>
<p>A maintenance trip is not automatically a customer-use period for the passive-activity seven-day average. That average uses actual customer rental periods, while the vacation-home calculation examines personal use and days rented at fair value. Track the two tests in separate worksheets. Also record whether a visiting owner stays overnight, whether friends or family occupy the property, and whether guests are paying market rates. These details can change the personal-day count without changing the number of platform bookings.</p>
<p>For a mixed trip, retain a day-by-day itinerary rather than declaring the entire visit “business.” A contractor invoice may prove work occurred but not that the owner worked substantially full time on each claimed maintenance day. If the property was unavailable for guests while a major improvement was underway, keep the listing-pause and construction records as well. That period can affect expense allocation and capitalization independently of the personal-use question.</p>
""",
    "cost-segregation-partial-disposition-renovation": """
<h2>Coordinate three schedules</h2>
<p>The workpaper should show the old building or component, the disposed portion, and the new improvement as separate schedules. First reconcile the original asset to tax basis and depreciation allowed or allowable. Next identify how much of that asset was physically retired and calculate its remaining basis. Finally classify and place the new work in service. If the same project includes repairs, capital improvements, and removals, allocate costs by scope rather than applying one tax label to the whole invoice.</p>
<p>A cost segregation firm and tax preparer should agree on the scope before the contractor disposes of old materials. Photos, measurements, and demolition records are hard to recreate after the work is complete. If the owner acquired the property recently, purchase-price allocation records can inform the historical component cost; if the building is decades old, cost-estimation assumptions need more explanation. A partial-disposition election may not be beneficial in every case, so compare the supported tax result with the preparation effort and other loss limits.</p>
""",
    "cost-segregation-study-audit-ready-deliverables": """
<h2>Questions for the study provider</h2>
<p>Ask who inspected the property, what records were unavailable, how estimates were reconciled to total cost, and who signs the final conclusions. Request a sample asset schedule before engagement. Clarify whether the fee includes responses to preparer questions, revisions after ledger reconciliation, and support if the IRS asks about classifications. A provider's promise of a particular deduction percentage is less useful than a method that can explain the actual assets in the building.</p>
""",
    "1031-exchange-closing-costs-prorations-boot": """
<h2>Watch for personal property in the purchase contract</h2>
<p>A replacement rental may be sold with appliances, furniture, or equipment. Section 1031 generally applies to qualifying real property, not these separately identifiable non-real-property assets. Allocate the contract price on supportable facts and examine whether exchange funds paid for non-like-kind property. A cost segregation study obtained later does not automatically make all components of the exchange purchase qualifying real property at closing. The exchange and depreciation analyses should use a coherent acquisition allocation.</p>
<p>Rent and deposit adjustments also require an operating ledger after closing. A buyer who receives a tenant deposit owes a future refund or credit; the settlement statement should reconcile to the lease files. The seller should retain the final rent roll and proration schedule. This operational reconciliation helps the tax preparer keep exchange costs, rental income, tenant liabilities, and purchase basis in their correct buckets.</p>
<p>If the exchanger receives non-like-kind property or cash, qualifying exchange expenses may reduce the recognized-gain limit, but they do not erase realized gain or make a nonqualifying asset like-kind. Prepare the recognized-gain and replacement-basis calculations side by side. A closing attorney, intermediary, and tax preparer may each use “exchange cost” differently, so put the final tax classification in writing.</p>
""",
    "late-s-corporation-election-relief-form-2553": """
<h2>Distinguish an IRS processing problem from an eligibility problem</h2>
<p>A Form 2553 may have been mailed but not processed, filed with a missing signature, or filed after the deadline. The corrective path depends on what happened. An IRS acceptance letter, account transcript, copy of the signed election, and certified-mail receipt can narrow the issue. If a shareholder was not eligible for S status or the entity issued a second class of stock, late-filing relief alone may not cure the substantive defect.</p>
<p>Payroll history should be reviewed alongside the relief request. S status can affect owner compensation reporting, and retroactive relief may require reconciling wage, distribution, and shareholder-basis records. State S elections may have separate deadlines and do not necessarily follow federal relief. The business should plan for corrected returns or statements only after the federal effective date and affected-year treatment are established.</p>
<p>Make a dated timeline of every filing and IRS response. Note when each shareholder acquired stock and whether the shareholder signed the election. If an owner left before the late filing, the signature requirements may still include that person for the relevant period under the revenue procedure. Resolve missing consents before sending the package, and retain a copy of the complete submission.</p>
""",
}

PILLARS = {
    "str": ROOT / "short-term-rental-tax-strategy/index.html",
    "costseg": ROOT / "cost-segregation-study/index.html",
    "realestate": ROOT / "guides/rental-property-tax-questions/index.html",
    "business": ROOT / "guides/business-tax-questions/index.html",
}

PILLAR_URLS = {
    "str": "/short-term-rental-tax-strategy/",
    "costseg": "/cost-segregation-study/",
    "realestate": "/guides/rental-property-tax-questions/",
    "business": "/guides/business-tax-questions/",
}


def update_pillar(kind):
    path = PILLARS[kind]
    page = path.read_text()
    marker_a = f"<!-- next-topic-guides-{kind}:start -->"
    marker_b = f"<!-- next-topic-guides-{kind}:end -->"
    rows = "\n".join(
        f'<li><a href="/blog/{g["slug"]}/">{g["title"]}</a><br>{g["description"]}</li>'
        for g in GUIDES if g["hub"] == kind
    )
    block = (f'{marker_a}<section class="content-section related-reading"><div class="container narrow">'
             f'<h2>Practical decision guides</h2><ul class="related-articles">{rows}</ul>'
             f'</div></section>{marker_b}')
    if marker_a in page:
        page = re.sub(re.escape(marker_a) + r".*?" + re.escape(marker_b), block, page, flags=re.S)
    else:
        close = "</main>" if "</main>" in page else "    </main>"
        page = page.replace(close, block + "\n" + close, 1)
    path.write_text(page)


def update_sitemap(name):
    path = ROOT / name
    xml = path.read_text()
    for g in GUIDES:
        url = f'https://www.aetaxadvisors.com/blog/{g["slug"]}/'
        if url not in xml:
            xml = xml.replace('</urlset>', f'<url><loc>{url}</loc><lastmod>{DATE}</lastmod></url>\n</urlset>')
    ET.fromstring(xml)
    path.write_text(xml)


def main():
    for g in GUIDES + [CORRECTED_DEPRECIATION_GUIDE]:
        post = dict(g, h1=g["title"], breadcrumb=g["title"], date=DATE,
                    date_display="September 22, 2026",
                    cta_head="Need the facts reviewed?",
                    cta_text="We can review your records and the tax treatment of your property or study.",
                    related=[(PILLAR_URLS[g["hub"]], "Explore the main guide")])
        if g["slug"] in PRACTICAL_FOLLOW_THROUGH:
            post["body"] = g["body"] + PRACTICAL_FOLLOW_THROUGH[g["slug"]]
        seo_render.write_post(post, ROOT)
    for kind in PILLARS:
        update_pillar(kind)
    for name in ("sitemap.xml", "sitemap-blog.xml"):
        update_sitemap(name)
    print("Generated", len(GUIDES), "new guides and revised one STR guide")


if __name__ == "__main__":
    main()
