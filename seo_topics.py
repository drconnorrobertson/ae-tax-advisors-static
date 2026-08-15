#!/usr/bin/env python3
"""Topic classification and topic-specific FAQ banks for the SEO pass.

Pages are matched to a topic by scoring their title, H1, and headings against
keyword sets. FAQs are only injected from the matched topic's bank, so the
questions relate to what the page actually covers.
"""

from __future__ import annotations

import re

# Topic key -> (weighted keywords, label)
TOPICS: dict[str, tuple[list[str], str]] = {
    "cost_seg": (["cost segregation", "cost seg", "depreciation study",
                  "reclassif", "component depreciation", "accelerated depreciation"],
                 "Cost Segregation"),
    "bonus_dep": (["bonus depreciation", "168(k)", "section 179", "macrs",
                   "depreciation schedule", "recovery period", "qualified improvement"],
                  "Depreciation"),
    "str": (["short-term rental", "short term rental", "airbnb", "vrbo", "str ",
             "vacation rental", "7-day", "seven-day"], "Short-Term Rentals"),
    "reps": (["real estate professional", "reps", "material participation",
              "passive activity", "passive loss", "469"], "Material Participation"),
    "rental": (["rental property", "long-term rental", "landlord", "schedule e",
                "rental income", "tenant", "multifamily", "apartment"],
               "Rental Property"),
    "exchange_1031": (["1031", "like-kind", "like kind", "qualified intermediary",
                       "boot", "deferred exchange"], "1031 Exchanges"),
    "scorp": (["s-corp", "s corp", "subchapter s", "reasonable compensation",
               "reasonable salary", "officer compensation", "form 2553",
               "self-employment tax", "payroll tax"], "S-Corp Planning"),
    "ccorp": (["c-corp", "c corp", "c corporation", "21%", "double taxation",
               "accumulated earnings", "qsbs", "1202"], "C-Corp Planning"),
    "entity": (["entity structur", "entity selection", "llc", "partnership",
                "holding company", "multi-entity", "restructur", "ptet",
                "pass-through entity tax", "salt cap"], "Entity Structuring"),
    "retirement": (["retirement plan", "solo 401", "401(k)", "cash balance",
                    "defined benefit", "sep ira", "simple ira", "profit sharing",
                    "backdoor roth", "mega backdoor"], "Retirement Planning"),
    "qbi": (["qbi", "199a", "qualified business income", "pass-through deduction"],
            "QBI Deduction"),
    "audit": (["audit", "irs representation", "examination", "notice", "cp2000",
               "appeals", "collection", "lien", "levy", "offer in compromise"],
              "IRS Representation"),
    "estate": (["estate", "trust", "wealth transfer", "gift tax", "step-up",
                "succession", "inheritance", "generation-skipping"],
               "Estate and Trust"),
    "exit": (["exit", "business sale", "m&a", "installment sale", "succession",
              "sell your business", "valuation", "earnout"], "Exit Planning"),
    "deductions": (["deduction", "write-off", "write off", "home office",
                    "accountable plan", "augusta rule", "280a", "mileage",
                    "meals", "vehicle"], "Business Deductions"),
    "bookkeeping": (["bookkeeping", "accounting", "financial statement",
                     "chart of accounts", "quickbooks", "clean up books",
                     "reconcil"], "Bookkeeping"),
    "credits": (["tax credit", "r&d credit", "research credit", "work opportunity",
                 "energy credit", "179d", "45l", "solar", "itc", "tip credit"],
                "Tax Credits"),
    "crypto": (["crypto", "bitcoin", "digital asset", "mining", "staking",
                "nft"], "Digital Assets"),
    "equipment": (["equipment", "section 179 deduction", "fleet", "vehicle depreciation",
                   "leasing", "machinery"], "Equipment and Section 179"),
    "multistate": (["multi-state", "multistate", "nexus", "state tax",
                    "domicile", "residency", "apportionment"], "Multi-State Tax"),
    "high_earner": (["high earner", "high-income", "w-2", "physician", "attorney",
                     "executive", "surgeon", "engineer", "amt", "net investment income"],
                    "High-Income Planning"),
    "compliance": (["tax return", "filing", "extension", "estimated tax",
                    "1099", "quarterly", "deadline", "penalty"], "Tax Compliance"),
    "firm": (["about", "our team", "why choose", "vs ", "versus", "review",
              "pricing", "consultation", "contact", "onboarding", "process"],
             "Working With Us"),
}

# Ordered so that more specific topics win ties.
PRIORITY = [
    "cost_seg", "str", "reps", "exchange_1031", "bonus_dep", "scorp", "ccorp",
    "retirement", "qbi", "credits", "crypto", "equipment", "estate", "exit",
    "audit", "multistate", "entity", "rental", "deductions", "bookkeeping",
    "high_earner", "compliance", "firm",
]


def classify(title: str, h1: str, headings: str, body: str) -> str:
    """Score a page against every topic and return the best match."""
    hay_strong = f" {title} {h1} ".lower()
    hay_mid = f" {headings} ".lower()
    hay_weak = f" {body[:4000]} ".lower()

    best, best_score = "firm", 0.0
    for key in PRIORITY:
        kws, _ = TOPICS[key]
        score = 0.0
        for kw in kws:
            if kw in hay_strong:
                score += 6.0
            if kw in hay_mid:
                score += 2.0
            score += min(hay_weak.count(kw), 4) * 0.6
        if score > best_score:
            best, best_score = key, score
    return best if best_score >= 3.0 else "firm"


# --------------------------------------------------------------- FAQ banks
# Each bank holds more entries than any page uses, and the generator picks a
# deterministic subset keyed on the page slug so neighbouring pages differ.

FAQS: dict[str, list[tuple[str, str]]] = {
"cost_seg": [
 ("What is a cost segregation study?",
  "A cost segregation study is an engineering-based analysis that separates a building's purchase or construction cost into its components and reassigns them from the default 27.5-year or 39-year recovery period to their correct 5-year, 7-year, and 15-year MACRS classifications. Because those shorter-life categories qualify for bonus depreciation, the reclassified amount is generally deductible in the first year."),
 ("How much of a property typically gets reclassified?",
  "It depends on the asset class. Office and warehouse properties commonly reclassify 15% to 25% of depreciable basis, multifamily 20% to 35%, restaurants and self-storage 30% to 40%, and hotels 30% to 45%. Furnished short-term rentals usually land between 25% and 35%."),
 ("Is a cost segregation study worth the cost?",
  "Generally yes once depreciable basis exceeds roughly $500,000, assuming you can actually use the deduction in the current year. The analysis that matters is not the size of the deduction but whether the passive activity loss rules, basis limits, and excess business loss limitation allow you to deduct it now."),
 ("Can I do a study on a property I bought years ago?",
  "Yes. A Form 3115 change in accounting method captures every missed deduction from the placed-in-service year in a single Section 481(a) adjustment claimed in the current year. No amended returns are needed and there is no three-year limitation."),
 ("What happens to the accelerated depreciation when I sell?",
  "Personal property is recaptured as ordinary income under Section 1245 to the extent of gain, and building depreciation is subject to unrecaptured Section 1250 gain taxed at up to 25%. A 1031 exchange defers it, and holding until death eliminates it through the basis step-up under Section 1014."),
 ("Do I need an engineering-based study or is an estimate enough?",
  "The IRS Cost Segregation Audit Techniques Guide identifies the detailed engineering approach as the most reliable method. Rule-of-thumb allocations without site work or construction document review are the first thing challenged on examination, particularly for specialty systems and site improvements."),
],
"bonus_dep": [
 ("Is bonus depreciation still 100% in 2026?",
  "Yes. The One Big Beautiful Bill Act restored the 100% first-year rate on a permanent basis for qualifying property acquired after January 19, 2025, removing the phase-down that would have cut the rate to 20% in 2026 and zero in 2027."),
 ("What property qualifies for bonus depreciation?",
  "Property with a MACRS recovery period of 20 years or less. That includes equipment and machinery, vehicles, furniture, qualified improvement property, and anything a cost segregation study reclassifies into 5-year, 7-year, or 15-year categories. Used property qualifies as well as new."),
 ("What is the difference between Section 179 and bonus depreciation?",
  "Section 179 is capped in dollar amount, phases out with total purchases, cannot create a loss, and is elected asset by asset. Bonus depreciation is uncapped, can create a loss, and is elected by class life. Section 179 also covers roofs, HVAC, fire protection, and security systems on nonresidential buildings, which bonus depreciation cannot reach."),
 ("Should I always take 100% bonus depreciation?",
  "No. Electing out can be better if you are in an unusually low bracket this year, if you plan to sell soon and want to avoid converting 25% unrecaptured Section 1250 gain into ordinary Section 1245 recapture, or if the deduction would reduce your Section 199A qualified business income deduction."),
 ("What are the 2026 MACRS recovery periods?",
  "Unchanged for 2026: 3, 5, 7, 10, 15, and 20 years for personal property and land improvements, 27.5 years for residential rental property, and 39 years for nonresidential real property. Short-term rentals with an average stay of seven days or less are generally 39-year property."),
 ("Do states follow federal bonus depreciation?",
  "Many do not. A number of states decouple entirely and require an addback with a separate state depreciation schedule, while conforming to Section 179 at some level. In those states the federal and state answers differ and both need to be modeled."),
],
"str": [
 ("How does the short-term rental tax strategy work?",
  "A property with an average period of customer use of seven days or less is not a rental activity under Treasury Regulation 1.469-1T(e)(3)(ii)(A). That removes the automatic passive classification of Section 469(c)(2), so if you materially participate the losses are non-passive and can offset W-2 and business income."),
 ("Do I need real estate professional status for a short-term rental?",
  "No. That is the central advantage of the short-term rental exception. Real estate professional status under Section 469(c)(7) requires more than 750 hours plus more than half of all personal services in real property trades or businesses. The short-term rental route requires only material participation."),
 ("How is the average period of customer use calculated?",
  "Total rental days divided by the number of separate bookings for the year. A property rented 200 days across 50 bookings averages 4 days and qualifies; the same 200 days across 20 bookings averages 10 days and does not. One long booking can push the annual average over the line."),
 ("Does using a property manager disqualify me?",
  "It often does in practice. The most commonly used material participation test requires more than 100 hours with no other individual participating more than you, and a full-service manager usually exceeds the owner's hours. Unbundling cleaning and maintenance while retaining guest communication and pricing generally preserves the test."),
 ("Is a short-term rental depreciated over 27.5 or 39 years?",
  "Generally 39 years. Residential rental property requires that 80% or more of gross rental income come from dwelling units, and a unit is not a dwelling unit if more than half its use is transient. A property averaging seven days or less is typically nonresidential real property."),
 ("Can I stay at my own short-term rental?",
  "Within limits. Personal use exceeding the greater of 14 days or 10% of rental days triggers the vacation home rules of Section 280A, which can cap deductions at rental income and eliminate the loss. Days spent substantially full time on repairs generally do not count as personal use."),
],
"reps": [
 ("What are the requirements for real estate professional status?",
  "Two tests must be met in the same year under IRC Section 469(c)(7): more than half of all personal services performed in all trades or businesses must be in real property trades or businesses in which you materially participate, and you must perform more than 750 hours in those businesses."),
 ("Can spouses combine hours to qualify?",
  "No. The qualification tests apply to each spouse individually and cannot be combined, even on a joint return. One spouse must satisfy both tests alone. Once one spouse qualifies, spousal participation may then be combined when testing material participation in the rental activities."),
 ("What are the seven material participation tests?",
  "Treasury Regulation 1.469-5T provides seven: more than 500 hours; substantially all participation; more than 100 hours with no one participating more; significant participation activities totaling more than 500 hours; material participation in five of the last ten years; a personal service activity with three prior years; and a facts-and-circumstances test."),
 ("Do I need an aggregation election?",
  "If you own more than one or two rentals, almost certainly. Without the election under Reg. 1.469-9(g), you must materially participate in each property separately, which is rarely achievable. The election groups all rental interests into a single activity so hours aggregate."),
 ("What documentation does the IRS accept for hours?",
  "The regulation allows any reasonable means, but contemporaneous dated logs with specific task descriptions, corroborated by emails, invoices, calendars, and receipts, are what survive. Reconstructed summaries prepared after an examination begins are consistently given little weight by the Tax Court."),
 ("What happens to suspended passive losses?",
  "They carry forward indefinitely and become deductible when the activity produces income, when other passive income is available, or when the activity's character changes. They are also released in full on a qualifying disposition of the entire interest."),
],
"rental": [
 ("Can rental losses offset my W-2 income?",
  "Not by default. Rental activities are passive per se under IRC Section 469(c)(2). The exceptions are qualifying as a real estate professional under Section 469(c)(7), using the short-term rental exception where average customer use is seven days or less with material participation, or the limited $25,000 allowance that phases out between $100,000 and $150,000 of modified AGI."),
 ("How is rental property depreciated?",
  "Residential rental property is depreciated straight line over 27.5 years using the mid-month convention. Nonresidential real property uses 39 years. A cost segregation study reassigns components into 5-year, 7-year, and 15-year classes that qualify for bonus depreciation."),
 ("What is depreciation recapture on a rental sale?",
  "Straight-line real property depreciation is recaptured as unrecaptured Section 1250 gain taxed at up to 25%. Accelerated depreciation on personal property identified in a cost segregation study is recaptured as ordinary income under Section 1245."),
 ("Should I hold rental property in an LLC or an S-Corp?",
  "An LLC taxed as a partnership or disregarded entity is almost always preferable. Rental income is not subject to self-employment tax, so an S election saves nothing, and distributing appreciated property out of an S-Corp triggers gain as though it had been sold."),
 ("Can I deduct travel to my rental property?",
  "Travel with a genuine business purpose such as inspection, maintenance, or tenant matters is deductible, but the IRS scrutinizes it closely and it does not count toward material participation hours. Records should show the business purpose, dates, and work performed."),
 ("What is the de minimis safe harbor for repairs?",
  "The tangible property regulations permit an annual election to expense items below a per-item threshold, generally $2,500 for taxpayers without an applicable financial statement. Combined with the routine maintenance safe harbor, this lets much of ordinary repair spending be deducted rather than capitalized."),
],
"exchange_1031": [
 ("What are the 1031 exchange deadlines?",
  "Two deadlines run from the closing of the relinquished property: 45 calendar days to identify replacement property in writing, and 180 calendar days to close on it. The 180-day period also cannot extend past the due date of your return including extensions, so filing an extension is often essential."),
 ("Can I touch the sale proceeds during an exchange?",
  "No. The proceeds must be held by a qualified intermediary from closing through acquisition of the replacement property. Receiving or controlling the funds at any point, even briefly, disqualifies the exchange entirely."),
 ("What property qualifies for a 1031 exchange?",
  "Real property held for investment or productive use in a trade or business. The definition is broad, so a rental house can be exchanged for a warehouse or raw land. Personal residences, property held primarily for sale such as flip inventory, and foreign real property do not qualify."),
 ("What is boot in a 1031 exchange?",
  "Any value received that is not like-kind property, including cash, debt relief, or non-qualifying property. Boot is taxable to the extent of gain, so replacement property should be of equal or greater value with equal or greater debt to achieve full deferral."),
 ("Does a 1031 exchange defer depreciation recapture?",
  "Yes. A properly structured exchange defers the entire gain including recapture into the replacement property. The deferred amount carries over in the replacement property's basis and is recognized on a later taxable sale, unless another exchange or a step-up at death intervenes."),
 ("Can I 1031 exchange a short-term rental?",
  "Yes, provided it is genuinely held for investment or business use rather than personal enjoyment. Significant personal use undermines the position, and the exchange must be structured before closing on the sale, not afterward."),
],
"scorp": [
 ("How much does an S-Corp election save?",
  "It saves 15.3% self-employment tax on profit characterized as distribution rather than wages, up to the Social Security wage base, and 2.9% to 3.8% above it. The election typically starts paying for itself once net profit exceeds roughly $60,000 to $80,000 per owner after compliance costs."),
 ("Is there a 60/40 rule for S-Corp salary?",
  "No. There is no safe harbor percentage in the Code, regulations, or IRS guidance. Reasonable compensation is a facts-and-circumstances determination measured against what comparable businesses pay for comparable services, using the nine factors summarized in IRS Fact Sheet FS-2008-25."),
 ("What happens if my S-Corp salary is too low?",
  "The IRS recharacterizes distributions as wages, producing back employment taxes for both halves, failure to deposit and failure to file penalties, accuracy-related penalties, and interest across all open years. Adjustments spanning three years frequently exceed six figures."),
 ("Does an S-Corp election reduce income tax?",
  "No. Profit is taxed at the same ordinary rates whether it flows through an LLC or an S-Corp. The election reduces employment tax only, which is a common point of confusion."),
 ("Can an LLC be taxed as an S-Corp?",
  "Yes. An LLC can elect S-Corp taxation by filing Form 2553 without converting to a corporation. The operating agreement, liability protection, and state law status are unaffected; only the federal tax characterization changes."),
 ("How does S-Corp salary interact with the QBI deduction?",
  "Above the Section 199A taxable income thresholds, the deduction for a non-service business is limited by W-2 wages. Reducing your salary to save payroll tax can therefore reduce the QBI deduction by more than the payroll tax saved, so both effects must be modeled together."),
],
"ccorp": [
 ("Does a C-Corp actually save tax?",
  "Only on income retained in the corporation. The flat 21% corporate rate beats a 37% individual rate on retained earnings, but distributing those earnings as qualified dividends adds a second layer that pushes the combined federal rate to roughly 39.8%."),
 ("What is the accumulated earnings tax?",
  "A 20% penalty tax under Section 531 on earnings accumulated beyond the reasonable needs of the business, with a credit of $250,000, or $150,000 for personal service corporations. It is defended with contemporaneous documentation of expansion plans and working capital requirements."),
 ("What is Section 1202 qualified small business stock?",
  "A provision allowing exclusion of a substantial portion of gain on the sale of qualifying C corporation stock held for the required period. The OBBBA expanded the regime with tiered exclusions beginning at three years and higher caps, making it the primary exit for growth-oriented C corporations."),
 ("Can I use a management company to shift income to a C-Corp?",
  "Yes, if the arrangement has substance. The corporation must actually provide services, the fee must be arm's length, and there must be a written agreement with supporting records. Section 482 permits the IRS to reallocate income between commonly controlled entities where pricing does not reflect economic reality."),
 ("Should real estate be held in a C-Corp?",
  "Almost never. Appreciated property distributed out of a C corporation triggers gain at both the corporate and shareholder level, with no equivalent of the partnership rules permitting tax-free property distributions."),
 ("What happens if I convert a C-Corp back to an S-Corp?",
  "The built-in gains tax of Section 1374 applies to gains that existed at conversion and are recognized within the following five-year period. This makes the C election harder to unwind than to make, which is why it should be modeled over a full holding period."),
],
"entity": [
 ("Which entity structure is right for my business?",
  "It depends on profit level, asset type, ownership, and exit plans. An LLC taxed as a partnership suits real estate and businesses needing special allocations; an S election suits profitable operating businesses above roughly $80,000 of profit per owner; a C corporation suits capital-intensive growth aiming at a Section 1202 exit."),
 ("What is a pass-through entity tax election?",
  "It allows a partnership or S corporation to pay state income tax at the entity level rather than passing it to owners. The entity-level tax is deductible federally and is not subject to the individual state and local tax cap, restoring a deduction that would otherwise be lost."),
 ("Should real estate be held in a separate entity from operations?",
  "Usually yes. It isolates liability, creates a clean platform for depreciation and cost segregation, and produces rent taxed once without payroll tax. The tradeoff is the self-rental rule of Reg. 1.469-2(f)(6), which is generally addressed with a grouping election under Reg. 1.469-4."),
 ("Are multiple entities always better?",
  "No. Separate entities are appropriate where they isolate genuinely different risks, hold different asset classes, or have different ownership. Entities that accumulate without a plan create duplicate filing fees, inconsistent intercompany charges, and compliance risk with no corresponding benefit."),
 ("What is a management company structure?",
  "One entity provides genuine management, administrative, or technology services to affiliated operating entities under a written agreement at arm's length rates. It can centralize administration, support benefit plans, and where a C corporation is used, capture rate arbitrage. It fails if the services are not real."),
 ("Can I change my entity structure later?",
  "Often, but not always cheaply. Converting an LLC to S-Corp taxation is straightforward, while unwinding a C corporation or removing appreciated real estate from one can be expensive. The cost of reversing a structure should be weighed before adopting it."),
],
"retirement": [
 ("How much can a business owner contribute to a retirement plan?",
  "A solo 401(k) permits employee deferrals plus employer contributions up to the annual additions limit, roughly $72,000 for 2026 plus catch-up. Adding a cash balance defined benefit plan can raise the total well beyond $250,000 for an owner in their fifties, because the contribution is actuarially derived from the benefit promised at retirement."),
 ("What is a cash balance plan?",
  "A defined benefit plan that expresses each participant's benefit as a hypothetical account balance credited annually with a pay credit and an interest credit. Because the plan limits the benefit rather than the contribution, the deductible amount rises sharply with the participant's age."),
 ("Can I have both a 401(k) and a cash balance plan?",
  "Yes, and they are almost always paired. Employee deferrals are unaffected, but employer profit sharing contributions are generally limited to 6% of covered compensation under the combined plan deduction limit of Section 404(a)(7) unless the defined benefit plan is PBGC-covered."),
 ("Do I have to cover my employees?",
  "Yes. Coverage and nondiscrimination rules apply, so a plan cannot cover only the owner. Cross-testing on a benefits basis allows the owner a much larger credit than staff, and typical staff cost runs 5% to 12% of covered payroll."),
 ("When must a retirement plan be established?",
  "Under the SECURE Act, most employer plans can be adopted as late as the due date of the employer's return including extensions for the first plan year, so a plan set up after year end can still produce a deduction for that year. Employee salary deferrals cannot be made retroactively."),
 ("What is a backdoor Roth contribution?",
  "A nondeductible traditional IRA contribution followed by a conversion to a Roth IRA, used by taxpayers above the Roth income limits. The pro-rata rule of Section 408(d)(2) aggregates all traditional IRA balances in computing the taxable portion, which is what makes the strategy work cleanly only when other pre-tax IRA balances are absent."),
],
"qbi": [
 ("What is the Section 199A qualified business income deduction?",
  "A deduction of up to 20% of qualified business income from a pass-through business, made permanent by the OBBBA. Below the taxable income thresholds it is simply 20% of QBI; above them it is limited by W-2 wages and the basis of qualified property."),
 ("What is a specified service trade or business?",
  "A business in health, law, accounting, actuarial science, performing arts, consulting, athletics, financial services, brokerage, or any business whose principal asset is the reputation or skill of its employees or owners. Above the taxable income thresholds, the QBI deduction for these businesses phases out entirely."),
 ("How do W-2 wages limit the QBI deduction?",
  "Above the thresholds, the deduction for a non-service business is limited to the greater of 50% of W-2 wages, or 25% of W-2 wages plus 2.5% of the unadjusted basis of qualified property. This is why minimizing an S-Corp salary can backfire."),
 ("Does rental real estate qualify for the QBI deduction?",
  "It can, where the activity rises to the level of a trade or business. Revenue Procedure 2019-38 provides a safe harbor requiring separate books, 250 hours of rental services annually, and contemporaneous records. Triple-net leases are generally excluded from the safe harbor."),
 ("Do large depreciation deductions reduce my QBI deduction?",
  "Yes. Depreciation reduces qualified business income, so a large first-year deduction can reduce the 20% deduction. For taxpayers inside the phase-in range the interaction is not intuitive and should be modeled before the depreciation elections are finalized."),
],
"audit": [
 ("What should I do if I receive an IRS notice?",
  "Read it carefully for the specific issue and the response deadline, and do not ignore it. Many notices are automated matching notices that can be resolved with documentation. Responding within the stated window preserves your appeal rights and prevents automatic assessment."),
 ("What triggers an IRS examination?",
  "Common triggers include large deductions relative to reported income, S-Corp officer compensation that appears low, real estate professional status claims, cryptocurrency reporting, and information return mismatches. Selection is also partly random through the National Research Program."),
 ("How long can the IRS go back?",
  "Generally three years from the filing date. That extends to six years where more than 25% of gross income was omitted, and there is no limit for a false or fraudulent return or a failure to file. Employment tax and certain international matters have their own rules."),
 ("Should I represent myself in an audit?",
  "It is rarely advisable beyond the simplest correspondence matters. Statements made during an examination cannot be retracted, and the scope of an audit frequently expands based on what the examiner learns. Representation by a CPA, enrolled agent, or attorney limits direct contact and keeps the scope defined."),
 ("What are my options if I owe more than I can pay?",
  "Installment agreements, currently not collectible status, penalty abatement for reasonable cause or first-time abatement, and in appropriate cases an offer in compromise. Which applies depends on your financial position, and the analysis should happen before enforcement action begins."),
],
"estate": [
 ("What is the step-up in basis at death?",
  "Under IRC Section 1014, most assets included in a decedent's estate receive a basis equal to fair market value at the date of death. This eliminates unrealized appreciation and, for real estate, wipes out accumulated depreciation recapture, which is why holding appreciated property until death is a core planning strategy."),
 ("How does estate planning interact with real estate depreciation?",
  "Accelerated depreciation creates recapture exposure on sale. Holding the property until death converts that exposure into a permanent benefit because the basis step-up eliminates the deferred gain, which is why exit planning and depreciation strategy are decided together."),
 ("What is the difference between a revocable and irrevocable trust?",
  "A revocable trust remains under the grantor's control, is included in the estate, and provides probate avoidance rather than tax reduction. An irrevocable trust generally removes assets from the estate for transfer tax purposes but gives up control and may have its own income tax consequences."),
 ("Should business interests be transferred during life or at death?",
  "It depends on expected appreciation and basis. Transferring an interest expected to appreciate substantially removes future growth from the estate, while holding an appreciated low-basis asset until death captures the step-up. The right answer usually blends both."),
],
"exit": [
 ("How is the sale of a business taxed?",
  "It depends on the structure. An asset sale allocates purchase price across asset classes with different rates, producing ordinary income on depreciation recapture and inventory and capital gain on goodwill. A stock sale is generally capital gain to the seller but is less attractive to buyers who lose the basis step-up."),
 ("What is an installment sale?",
  "A sale where payments are received over more than one tax year, allowing gain to be recognized as payments are received under Section 453. Depreciation recapture under Section 1245 is accelerated into the year of sale regardless of the payment schedule."),
 ("How early should exit planning begin?",
  "Three to five years before a sale. Entity structure, reasonable compensation history, clean financial statements, and Section 1202 holding periods all take years to position, and most of the value in exit planning is captured before a buyer is ever identified."),
 ("What is Section 1202 and how does it affect an exit?",
  "It permits exclusion of a substantial portion of gain on qualifying C corporation stock held for the required period. Because it depends on the entity type at issuance and on holding period, it must be planned years in advance and cannot be added at closing."),
],
"deductions": [
 ("What is an accountable plan?",
  "An arrangement under Treasury Regulation 1.62-2 through which a business reimburses employees, including owner-employees, for business expenses without the reimbursement being treated as taxable wages. It requires a business connection, substantiation within a reasonable period, and return of excess amounts."),
 ("How does the Augusta Rule work?",
  "IRC Section 280A(g) allows a taxpayer to rent a personal residence for 14 days or fewer per year without including the rental income in gross income. A business can deduct the rent if it is reasonable, documented with a rental agreement and a genuine business purpose, and supported by comparable rates."),
 ("Can I deduct a home office?",
  "Yes, where a portion of the home is used regularly and exclusively as the principal place of business or for meeting clients. For owner-employees of an S corporation, reimbursement through an accountable plan is generally preferable to claiming the deduction directly."),
 ("Are business meals deductible?",
  "Business meals with a clear business purpose are generally 50% deductible when not lavish and when the taxpayer or an employee is present. Entertainment remains nondeductible. Certain employee-related meals have different treatment, so the category matters."),
 ("What vehicle deductions are available?",
  "Either the standard mileage rate or actual expenses including depreciation. Passenger automobiles are subject to the Section 280F luxury auto caps, while vehicles above 6,000 pounds gross vehicle weight rating fall outside that definition and have separate rules. Contemporaneous mileage records are essential."),
],
"bookkeeping": [
 ("Why does bookkeeping quality affect tax planning?",
  "Every planning strategy depends on knowing profit accurately and in time to act. Entity elections, reasonable compensation, retirement contributions, and depreciation decisions all require reliable numbers before year end, not after, and reconstructed books eliminate most of the year's opportunities."),
 ("How often should books be reconciled?",
  "Monthly. Reconciling bank, credit card, and loan accounts monthly catches errors while source documents are still available and produces financial statements timely enough to support planning decisions during the year."),
 ("What records should a business keep and for how long?",
  "Generally at least three years from the filing date, and seven years is the safer practice. Records supporting asset basis, including purchase documents, improvements, and depreciation schedules, should be kept for the life of the asset plus the limitation period after disposition."),
 ("Should bookkeeping and tax strategy be handled by the same team?",
  "It removes a substantial amount of friction. When the people producing the numbers understand what the planning requires, the chart of accounts, fixed asset tracking, and payroll coding are set up to support the strategy rather than needing to be reworked at year end."),
],
"credits": [
 ("What is the R&D tax credit?",
  "A credit under Section 41 for qualified research expenses, available to more businesses than commonly assumed, including software development, process improvement, and product engineering. Qualified small businesses may apply a portion against payroll tax rather than income tax."),
 ("What is the FICA tip credit?",
  "A credit under Section 45B for employer Social Security and Medicare taxes paid on employee tips above the amount treated as wages for minimum wage purposes. For full-service restaurants it frequently amounts to tens of thousands of dollars annually and is routinely overlooked."),
 ("What is the Work Opportunity Tax Credit?",
  "A credit for hiring individuals from targeted groups. It requires Form 8850 certification submitted to the state workforce agency within 28 days of the employee's start date, which means it cannot be claimed retroactively."),
 ("Are energy efficiency incentives still available?",
  "Yes, in various forms including the Section 179D deduction for commercial building energy efficiency improvements and Section 45L for qualifying residential construction. Eligibility depends on efficiency standards and, in some cases, prevailing wage and apprenticeship requirements."),
],
"crypto": [
 ("How is cryptocurrency taxed?",
  "Digital assets are treated as property, so every sale, exchange, or use to purchase goods is a taxable disposition producing capital gain or loss. Holding period determines whether the gain is short or long term, and each disposition must be tracked with its own basis."),
 ("Is crypto mining a business?",
  "It can be. Mining conducted with continuity and a profit motive is generally a trade or business, with income recognized at the fair market value of coins when received and deductions available for equipment depreciation, electricity, and facilities. Casual mining is other income instead."),
 ("How is staking income taxed?",
  "Staking rewards are generally included in income at fair market value when the taxpayer gains dominion and control over them, establishing basis for a later disposition. The treatment continues to develop and positions should be documented."),
 ("What records are required for digital assets?",
  "Date and time of acquisition, cost basis, date and value at disposition, and the nature of each transaction, for every disposition. Exchange reporting is incomplete for transfers between wallets, so independent records are necessary to substantiate basis."),
],
"equipment": [
 ("Can I deduct equipment purchases in the first year?",
  "Generally yes. Bonus depreciation permits a 100% first-year deduction on property with a recovery period of 20 years or less, and Section 179 permits expensing up to an annual cap subject to a purchase phase-out and a taxable income limitation."),
 ("Is leasing or buying equipment better for taxes?",
  "It depends on the lease structure. A capital or finance lease is treated as a purchase, generating depreciation and interest deductions. A true operating lease produces deductible rent instead. The tax result follows the substance of the arrangement, not its label."),
 ("What is the mid-quarter convention?",
  "If more than 40% of the total basis of personal property placed in service during the year falls in the fourth quarter, the mid-quarter convention replaces the half-year convention for every asset placed in service that year, reducing first-year deductions on assets bought earlier."),
 ("What happens if business use of equipment drops?",
  "For Section 179 property, if business use falls to 50% or less before the end of the recovery period, the excess benefit is recaptured as ordinary income in that year. Bonus depreciation has no comparable business-use recapture rule during the holding period."),
],
"multistate": [
 ("When does my business create nexus in another state?",
  "Physical presence such as employees, inventory, or property generally creates nexus, and most states also apply economic nexus thresholds based on sales or transaction counts. Remote employees are one of the most common and least noticed triggers."),
 ("How is income apportioned among states?",
  "Most states now use a single sales factor, apportioning income based on the share of sales sourced to the state. Sourcing rules differ, particularly for services and intangibles, where states split between market-based sourcing and cost of performance."),
 ("What is the pass-through entity tax workaround?",
  "A majority of states with an income tax permit a pass-through entity to elect to pay state tax at the entity level. The entity-level tax is deductible federally and avoids the individual state and local tax cap, restoring a federal deduction for the owners."),
 ("How do I change my state of residency for tax purposes?",
  "By changing domicile in substance, not merely in form. States examine days present, location of the permanent home, family and business ties, licenses and registrations, and where the taxpayer's center of life sits. High-tax states audit departures aggressively."),
],
"high_earner": [
 ("What tax strategies are available to a high W-2 earner?",
  "W-2 income has few built-in levers, so plans generally create one: real estate that produces non-passive losses through the short-term rental exception, maximized retirement and after-tax plan contributions, charitable bunching through a donor advised fund, and where applicable a side business with its own planning capacity."),
 ("What is the net investment income tax?",
  "A 3.8% tax under Section 1411 on the lesser of net investment income or modified AGI above $200,000 single or $250,000 married filing jointly. Income from a trade or business in which the taxpayer materially participates is generally excluded, which is another reason material participation matters."),
 ("Why donate appreciated securities instead of cash?",
  "Contributing securities held more than one year allows a deduction at fair market value while permanently avoiding the capital gain a sale would trigger. Bunching several years of intended giving into one high-rate year through a donor advised fund increases the value further."),
 ("Can a high earner still use a Roth?",
  "Directly, no, above the income limits, but a nondeductible traditional IRA contribution followed by a Roth conversion accomplishes it. The pro-rata rule aggregates all traditional IRA balances, so the strategy works cleanly only when other pre-tax IRA balances are absent or have been rolled into a workplace plan."),
],
"compliance": [
 ("When are business tax returns due?",
  "Partnership and S corporation returns are generally due the fifteenth day of the third month after year end, and C corporation and individual returns the fifteenth day of the fourth month, with six-month extensions available. An extension extends the filing deadline, not the payment deadline."),
 ("Do I need to make estimated tax payments?",
  "Generally yes if you expect to owe $1,000 or more. Safe harbor is met by paying 90% of the current year's tax or 100% of the prior year's, rising to 110% for higher-income taxpayers, which avoids underpayment penalties regardless of how the year turns out."),
 ("Who needs to receive a Form 1099?",
  "Generally non-employee service providers paid $600 or more during the year who are not corporations, with exceptions including attorneys. Collecting a Form W-9 before the first payment is the practical way to avoid a scramble in January."),
 ("What happens if I file late?",
  "Failure to file penalties accrue at a substantially higher rate than failure to pay penalties, so filing on time matters even when you cannot pay in full. Pass-through entities face per-partner or per-shareholder monthly penalties that accumulate quickly."),
],
"firm": [
 ("What does a tax advisory engagement include?",
  "A prior year review to identify recoverable overpayments, a forward-looking plan quantifying each recommended strategy, implementation support including entity filings and plan documents, and ongoing coordination so decisions are made during the year rather than reconstructed afterward."),
 ("How is tax planning different from tax preparation?",
  "Preparation reports what already happened. Planning changes what happens, and nearly every meaningful strategy has a deadline that falls before year end. A return filed in April can only reflect decisions that were made months earlier."),
 ("Do you work with clients outside Montana?",
  "Yes. We work with clients nationwide from our office in Billings, Montana. Federal strategy is identical across states, and we coordinate state-specific issues including pass-through entity tax elections, nexus, and residency wherever clients operate."),
 ("How do you charge for advisory work?",
  "Advisory engagements are quoted as a fixed fee based on scope, with cost segregation studies and entity return work priced separately. Pricing is set before work begins so the value of a strategy can be weighed against its cost."),
 ("How quickly can strategies be implemented?",
  "It depends on the strategy. Entity elections, retirement plan adoption, and accountable plans can often be put in place quickly, while cost segregation studies typically take several weeks and material participation positions require a full year of documentation."),
],
}


STOPWORDS = {
    "the", "a", "an", "and", "or", "for", "of", "to", "in", "on", "with", "what",
    "how", "is", "are", "do", "does", "can", "your", "you", "my", "it", "that",
    "this", "tax", "taxes", "ae", "advisors", "guide", "2026", "2025",
}


def _tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", text.lower())
            if len(w) > 2 and w not in STOPWORDS}


def faqs_for(topic: str, slug: str, n: int = 4, context: str = "") -> list[tuple[str, str]]:
    """Pick FAQs for a page, most relevant first.

    Questions are ranked by word overlap with the page's title and headings so
    the page's own subject leads. Ties break on a slug-derived rotation, which
    keeps neighbouring pages in the same topic from showing identical lists.
    """
    bank = FAQS.get(topic) or FAQS["firm"]
    if len(bank) <= n and not context:
        return list(bank)

    ctx = _tokens(context) if context else set()
    rot = sum(ord(c) for c in slug) % max(len(bank), 1)

    scored = []
    for i, (q, a) in enumerate(bank):
        overlap = len(_tokens(q) & ctx)
        # Rotation offset keeps same-score questions from always ordering alike.
        tiebreak = -((i - rot) % len(bank))
        scored.append((overlap, tiebreak, i))
    scored.sort(reverse=True)
    return [bank[i] for _, _, i in scored[:n]]


DEFINITIONS: dict[str, str] = {
"cost_seg": "Cost segregation is an engineering-based tax study that separates a building's cost into its components and reassigns them from the default 27.5-year or 39-year depreciation schedule to their correct 5-year, 7-year, and 15-year classifications, so that the reclassified portion becomes immediately deductible under 100% bonus depreciation.",
"bonus_dep": "Bonus depreciation is a first-year deduction under IRC Section 168(k) that allows the full cost of qualifying property to be deducted immediately rather than over its recovery period. Under the One Big Beautiful Bill Act, the rate is 100% and permanent for property acquired after January 19, 2025.",
"str": "A short-term rental is a property with an average period of customer use of seven days or less, which under Treasury Regulation 1.469-1T(e)(3)(ii)(A) is not treated as a rental activity for passive loss purposes. That distinction allows an owner who materially participates to deduct losses against wages and business income.",
"reps": "Material participation is the standard under Treasury Regulation 1.469-5T that determines whether a taxpayer's involvement in an activity is regular, continuous, and substantial enough to make the activity non-passive, which in turn determines whether losses can offset wages and business income.",
"rental": "Rental property tax planning is the process of structuring ownership, depreciation, and participation so that a property's deductions are usable in the year they arise rather than suspended as passive losses under IRC Section 469.",
"exchange_1031": "A 1031 exchange is a transaction under IRC Section 1031 in which real property held for investment or business use is exchanged for other like-kind real property, deferring all capital gain and depreciation recapture provided the 45-day identification and 180-day closing deadlines are met and proceeds are held by a qualified intermediary.",
"scorp": "An S corporation is a federal tax election under Subchapter S in which a business pays its owner reasonable W-2 wages subject to payroll tax and distributes remaining profit free of self-employment tax, reducing employment tax without changing how the profit is taxed for income tax purposes.",
"ccorp": "A C corporation is a separate taxpayer subject to a flat 21% federal rate under IRC Section 11. Income retained in the corporation is taxed once at that rate, while distributions to shareholders as dividends add a second layer of tax, which is why the structure suits businesses that reinvest rather than distribute.",
"entity": "Entity structuring is the design of the legal and tax entities through which a business and its assets are held, determining employment tax exposure, loss usability, state tax treatment, liability isolation, and the tax cost of an eventual sale.",
"retirement": "Qualified retirement plans allow a business owner to deduct contributions today and defer tax until distribution. Defined contribution plans cap the annual contribution, while defined benefit and cash balance plans cap the benefit payable at retirement, which allows much larger deductions as the owner approaches retirement age.",
"qbi": "The qualified business income deduction under IRC Section 199A allows eligible taxpayers to deduct up to 20% of qualified business income from a pass-through business. Above the taxable income thresholds the deduction is limited by W-2 wages and qualified property, and it is unavailable to specified service businesses.",
"audit": "IRS representation is the practice of acting on a taxpayer's behalf in examinations, appeals, and collection matters under a power of attorney, controlling the scope of inquiry and the information provided while preserving procedural rights and deadlines.",
"estate": "Estate and wealth transfer planning determines how assets pass to the next generation and at what tax cost, coordinating the basis step-up under IRC Section 1014, transfer tax exposure, and the income tax consequences of holding versus selling appreciated assets.",
"exit": "Exit planning is the multi-year process of positioning a business for sale so that the transaction is taxed as favorably as possible, addressing entity structure, purchase price allocation, installment treatment, and qualified small business stock eligibility well before a buyer is identified.",
"deductions": "Business deductions are ordinary and necessary expenses of carrying on a trade or business under IRC Section 162, and their value depends less on identifying them than on documenting them properly and routing them through the correct structure, such as an accountable plan.",
"bookkeeping": "Bookkeeping is the ongoing recording and reconciliation of financial transactions that produces the timely, accurate numbers every tax planning decision depends on, since entity elections, compensation, retirement contributions, and depreciation choices must be made during the year rather than after it.",
"credits": "Tax credits reduce tax liability dollar for dollar rather than reducing taxable income, which makes them substantially more valuable than deductions of the same size, and many of them carry strict certification or filing deadlines that cannot be met retroactively.",
"crypto": "Digital assets are treated as property for federal tax purposes, so every sale, exchange, or use to acquire goods is a taxable disposition producing capital gain or loss measured against the asset's basis, and each disposition must be tracked independently.",
"equipment": "Equipment depreciation planning determines how quickly the cost of machinery, vehicles, and fixtures is deducted, using Section 179 expensing, 100% bonus depreciation, or the MACRS schedule, with the correct choice depending on loss usability, state conformity, and property type.",
"multistate": "Multi-state tax planning addresses where a business owes tax, covering nexus, apportionment, sourcing, and residency, and it has become substantially more complex as remote employees and economic nexus thresholds create filing obligations in states where a business has no physical location.",
"high_earner": "High-income tax planning for W-2 earners focuses on creating deduction capacity that salary income does not naturally provide, principally through real estate that generates non-passive losses, maximized retirement contributions, and structured charitable giving.",
"compliance": "Tax compliance is the accurate and timely filing of returns and information reports and the payment of estimated tax, and while it does not reduce tax by itself, failures in this area generate penalties that can exceed the value of the planning they undermine.",
"firm": "AE Tax Advisors is a strategic tax advisory firm in Billings, Montana, working with business owners, real estate investors, and high-income professionals nationwide on cost segregation, entity structuring, retirement plan design, and IRS-compliant tax reduction strategies.",
}

# Cross-link pools by topic. Every target is a real page on the site.
LINKS: dict[str, list[tuple[str, str]]] = {
"cost_seg": [
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works and What It Costs"),
 ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026 Under the OBBBA"),
 ("/form-3115-cost-segregation-lookback/", "Form 3115 Cost Segregation Lookback"),
 ("/cost-segregation-for-multifamily/", "Cost Segregation for Multifamily Properties"),
 ("/macrs-depreciation-schedule-2026/", "MACRS Depreciation Schedule 2026"),
 ("/case-studies/", "Case Studies: Real Tax Planning Results"),
],
"bonus_dep": [
 ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026 Under the OBBBA"),
 ("/section-179-vs-bonus-depreciation-2026/", "Section 179 vs Bonus Depreciation in 2026"),
 ("/macrs-depreciation-schedule-2026/", "MACRS Depreciation Schedule 2026"),
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
 ("/form-3115-cost-segregation-lookback/", "Form 3115 Cost Segregation Lookback"),
],
"str": [
 ("/short-term-rental-tax-loophole-2026/", "The Short-Term Rental Tax Loophole in 2026"),
 ("/material-participation-short-term-rental-7-day-rule/", "Material Participation and the STR 7-Day Rule"),
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
 ("/short-term-rental-tax-strategy/", "Short-Term Rental Tax Strategy"),
 ("/reps-real-estate-professional-status/", "Real Estate Professional Status: How to Qualify"),
],
"reps": [
 ("/reps-real-estate-professional-status/", "Real Estate Professional Status: How to Qualify"),
 ("/material-participation-short-term-rental-7-day-rule/", "Material Participation and the STR 7-Day Rule"),
 ("/short-term-rental-tax-loophole-2026/", "The Short-Term Rental Tax Loophole in 2026"),
 ("/real-estate-tax-planning/", "Real Estate Tax Planning"),
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
],
"rental": [
 ("/rental-property-tax-planning/", "Rental Property Tax Planning"),
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
 ("/reps-real-estate-professional-status/", "Real Estate Professional Status: How to Qualify"),
 ("/form-3115-cost-segregation-lookback/", "Form 3115 Cost Segregation Lookback"),
 ("/real-estate-tax-planning/", "Real Estate Tax Planning"),
],
"exchange_1031": [
 ("/1031-exchange-tax-coordination/", "1031 Exchange Tax Coordination"),
 ("/real-estate-tax-planning/", "Real Estate Tax Planning"),
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
 ("/reps-real-estate-professional-status/", "Real Estate Professional Status: How to Qualify"),
 ("/case-studies/", "Case Studies: Real Tax Planning Results"),
],
"scorp": [
 ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
 ("/reasonable-compensation-s-corp-irs/", "Reasonable Compensation for S-Corp Owners"),
 ("/business-owner-small-business-tax/", "Business Owner and Small Business Tax"),
 ("/cash-balance-plan-tax-deduction/", "Cash Balance Plan Tax Deduction"),
 ("/c-corp-income-shifting-strategy/", "C-Corp Income Shifting Strategy"),
],
"ccorp": [
 ("/c-corp-income-shifting-strategy/", "C-Corp Income Shifting Strategy"),
 ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
 ("/reasonable-compensation-s-corp-irs/", "Reasonable Compensation for S-Corp Owners"),
 ("/retirement-exit-ma-tax-strategy/", "Retirement, Exit and M&A Tax Strategy"),
 ("/cash-balance-plan-tax-deduction/", "Cash Balance Plan Tax Deduction"),
],
"entity": [
 ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
 ("/c-corp-income-shifting-strategy/", "C-Corp Income Shifting Strategy"),
 ("/multi-state-global-tax/", "Multi-State and Global Tax Planning"),
 ("/business-owner-small-business-tax/", "Business Owner and Small Business Tax"),
 ("/case-studies/", "Case Studies: Real Tax Planning Results"),
],
"retirement": [
 ("/cash-balance-plan-tax-deduction/", "Cash Balance Plan Tax Deduction"),
 ("/best-retirement-plan-business-owner-over-500k/", "Best Retirement Plan for Owners Over $500K"),
 ("/retirement-exit-ma-tax-strategy/", "Retirement, Exit and M&A Tax Strategy"),
 ("/reasonable-compensation-s-corp-irs/", "Reasonable Compensation for S-Corp Owners"),
 ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
],
"qbi": [
 ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
 ("/reasonable-compensation-s-corp-irs/", "Reasonable Compensation for S-Corp Owners"),
 ("/business-owner-small-business-tax/", "Business Owner and Small Business Tax"),
 ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026 Under the OBBBA"),
],
"audit": [
 ("/tax-compliance-irs-representation/", "Tax Compliance and IRS Representation"),
 ("/audit-defense-compliance/", "Audit Defense and Compliance"),
 ("/form-3115-cost-segregation-lookback/", "Form 3115 Cost Segregation Lookback"),
 ("/case-studies/", "Case Studies: Real Tax Planning Results"),
],
"estate": [
 ("/estate-trust-wealth-transfer/", "Estate, Trust and Wealth Transfer"),
 ("/retirement-exit-ma-tax-strategy/", "Retirement, Exit and M&A Tax Strategy"),
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
 ("/real-estate-tax-planning/", "Real Estate Tax Planning"),
],
"exit": [
 ("/retirement-exit-ma-tax-strategy/", "Retirement, Exit and M&A Tax Strategy"),
 ("/c-corp-income-shifting-strategy/", "C-Corp Income Shifting Strategy"),
 ("/estate-trust-wealth-transfer/", "Estate, Trust and Wealth Transfer"),
 ("/case-studies/", "Case Studies: Real Tax Planning Results"),
],
"deductions": [
 ("/accountable-plan/", "Accountable Plans Done Correctly"),
 ("/business-owner-small-business-tax/", "Business Owner and Small Business Tax"),
 ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
 ("/section-179-vs-bonus-depreciation-2026/", "Section 179 vs Bonus Depreciation in 2026"),
],
"bookkeeping": [
 ("/services/bookkeeping/", "Bookkeeping Services"),
 ("/business-owner-small-business-tax/", "Business Owner and Small Business Tax"),
 ("/reasonable-compensation-s-corp-irs/", "Reasonable Compensation for S-Corp Owners"),
 ("/case-studies/", "Case Studies: Real Tax Planning Results"),
],
"credits": [
 ("/cost-segregation-for-restaurant/", "Cost Segregation for Restaurants"),
 ("/business-owner-small-business-tax/", "Business Owner and Small Business Tax"),
 ("/section-179-vs-bonus-depreciation-2026/", "Section 179 vs Bonus Depreciation in 2026"),
 ("/case-studies/", "Case Studies: Real Tax Planning Results"),
],
"crypto": [
 ("/crypto-mining-tax-strategy/", "Crypto Mining Tax Strategy"),
 ("/business-owner-small-business-tax/", "Business Owner and Small Business Tax"),
 ("/section-179-vs-bonus-depreciation-2026/", "Section 179 vs Bonus Depreciation in 2026"),
 ("/case-studies/", "Case Studies: Real Tax Planning Results"),
],
"equipment": [
 ("/equipment-leasing-section-179/", "Equipment Leasing and Section 179"),
 ("/section-179-vs-bonus-depreciation-2026/", "Section 179 vs Bonus Depreciation in 2026"),
 ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026 Under the OBBBA"),
 ("/macrs-depreciation-schedule-2026/", "MACRS Depreciation Schedule 2026"),
],
"multistate": [
 ("/multi-state-global-tax/", "Multi-State and Global Tax Planning"),
 ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
 ("/business-owner-small-business-tax/", "Business Owner and Small Business Tax"),
 ("/case-studies/", "Case Studies: Real Tax Planning Results"),
],
"high_earner": [
 ("/individual-tax-planning-high-earners/", "Advanced Income and Entity Planning"),
 ("/short-term-rental-tax-loophole-2026/", "The Short-Term Rental Tax Loophole in 2026"),
 ("/cash-balance-plan-tax-deduction/", "Cash Balance Plan Tax Deduction"),
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
],
"compliance": [
 ("/tax-compliance-irs-representation/", "Tax Compliance and IRS Representation"),
 ("/business-owner-small-business-tax/", "Business Owner and Small Business Tax"),
 ("/services/bookkeeping/", "Bookkeeping Services"),
 ("/case-studies/", "Case Studies: Real Tax Planning Results"),
],
"firm": [
 ("/about/", "About AE Tax Advisors"),
 ("/pricing/", "Pricing and Engagement Options"),
 ("/case-studies/", "Case Studies: Real Tax Planning Results"),
 ("/services/", "Our Services"),
 ("/discovery/", "Request a Consultation"),
],
}


def links_for(topic: str, slug: str, self_path: str, n: int = 4) -> list[tuple[str, str]]:
    pool = [x for x in (LINKS.get(topic) or LINKS["firm"]) if x[0] != self_path]
    if len(pool) <= n:
        return pool
    start = sum(ord(c) for c in slug) % len(pool)
    return [pool[(start + k) % len(pool)] for k in range(n)]
