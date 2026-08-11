"""Batch: state-level cost segregation and depreciation conformity guides."""

from blog_gen import write_all

C = "Real Estate Investor Tax"
D = "2026-08-11"

CAVEAT = ("State conformity provisions are amended frequently and the "
          "mechanics below should be confirmed against the current year "
          "instructions before filing.")

ARTICLES = [
{
"slug": "cost-segregation-california-state-tax-rules",
"title": "Cost Segregation in California: Why the State Deduction Looks Nothing Like the Federal One",
"meta_title": "Cost Segregation in California: State Tax Rules (2026) | AE Tax Advisors",
"meta_desc": "California does not conform to bonus depreciation and caps Section 179 near $25,000. What a cost segregation study actually produces on a CA return.",
"category": C, "date": D,
"intro": [
"California investors run cost segregation studies, see an enormous federal deduction, and then discover their California return barely moved. The study was not wrong. California simply does not follow the federal rules that make the deduction large.",
"With a top individual rate of 13.3%, the state side is not a rounding error. Understanding what California allows changes how the study should be modeled and, in some cases, whether it should be run at all.",
],
"sections": [
("California Does Not Conform to Bonus Depreciation", [
"California has not conformed to federal bonus depreciation under IRC Sec. 168(k) at any point since the provision was enacted. There is no addback and recovery mechanism, no partial conformity, and no phase-in.",
"For state purposes, the reclassified components identified in a cost segregation study depreciate over their MACRS recovery periods on a California schedule. Five-year property depreciates over five years. Fifteen-year land improvements depreciate over fifteen.",
"That is still substantially faster than 27.5 or 39 years, so the study does produce a California benefit. It simply arrives over years rather than all at once.",
"The practical effect is that every California investor running a study maintains two depreciation schedules for the life of the property, with a growing difference between federal and state basis that must be tracked through to disposition.",
]),
("Section 179 Is Capped Far Below Federal", [
"California limits the Sec. 179 deduction to $25,000 with a phase-out beginning at $200,000 of qualifying property placed in service. The federal limit for 2025 is $2,500,000 with a $4,000,000 phase-out threshold.",
"For a business owner placing $600,000 of equipment in service, the federal deduction is the full amount and the California deduction is zero, since the phase-out has fully eliminated it.",
"California also does not conform to the federal qualified real property provisions in IRC Sec. 179(f), so roofs, HVAC, fire protection, and security systems on nonresidential buildings cannot be expensed at the state level.",
]),
("Passive Loss Rules Track Federal, With a Twist", [
"California generally conforms to the passive activity loss rules of IRC Sec. 469, including real estate professional status and the $25,000 special allowance.",
"But because California depreciation is smaller, the California passive loss is smaller. An investor with a $340,000 federal loss from a study may have a $58,000 California loss in the same year, with the balance arriving over the following fourteen years.",
"California also requires separate tracking of suspended passive losses for state purposes, since the amounts differ. Investors who assume the federal suspended loss carryforward applies to California are wrong, and the discrepancy compounds annually.",
]),
("The LLC Fee Nobody Budgets For", [
"California imposes an $800 minimum annual franchise tax on every LLC doing business in the state, plus a gross receipts fee that begins at $900 for total California income of $250,000 and rises to $11,790 above $5,000,000.",
"An investor with six California rental LLCs pays $4,800 in minimum tax alone before any income tax, and the gross receipts fee is assessed on gross rents, not net income. A property with negative cash flow still owes it.",
"This is a genuine argument for consolidating California properties into fewer LLCs, weighed against the asset protection cost of doing so. The fee is per entity, not per property.",
"An out-of-state LLC owning California property is doing business in California and owes the same amounts. Forming in Wyoming or Nevada does not avoid this.",
]),
("Nonresident Owners", [
"California-source rental income is taxable to nonresidents. Withholding is generally required on payments to nonresident owners, and a California nonresident return is required.",
"California also applies a throwback concept to certain trusts and has an unusually aggressive residency audit program. Investors who move out of California while retaining California rental property should expect the state to examine the facts of the move, and should document it thoroughly.",
]),
("Worked Example: What the Study Actually Produces", [
"A California investor acquires a $2,300,000 apartment building. Land is allocated at $520,000, leaving $1,780,000 depreciable. A study reclassifies 25%, identifying $267,000 of five-year property and $178,000 of 15-year land improvements.",
"Federally, all $445,000 is bonus eligible and deductible in year one, plus $48,545 of structural depreciation, for roughly $493,545.",
"For California, no bonus applies. Five-year property produces roughly $53,400 in year one under MACRS, 15-year property produces roughly $8,900, and the structure produces $48,545. California depreciation is roughly $110,845.",
"The first-year difference is $382,700. At a 13.3% California rate, the state benefit deferred is roughly $50,900, recovered over the following fourteen years rather than lost.",
"The study is still clearly worth running. California accelerates from 27.5 years to five and fifteen, which is meaningful. The error is modeling the state benefit as though it mirrors the federal one.",
]),
("Planning Implications", [
"Model both schedules before commissioning the study, not after. The federal number sells the study. The combined number determines whether it fits your situation.",
"Track federal and California basis separately from day one. At disposition, California gain will differ from federal gain, sometimes substantially, and reconstructing fourteen years of divergent schedules retroactively is expensive.",
"Consider entity count deliberately given the franchise tax and gross receipts fee.",
"For investors contemplating a move out of California, understand that California property continues to generate California-source income and California filing obligations regardless of residency.",
CAVEAT,
]),
],
"faqs": [
("Does California allow bonus depreciation?",
 "No. California has never conformed to federal bonus depreciation under IRC Sec. 168(k). Reclassified components from a cost segregation study depreciate over their MACRS recovery periods on the California schedule, which is still far faster than 27.5 or 39 years."),
("What is California's Section 179 limit?",
 "$25,000 with a phase-out beginning at $200,000 of qualifying property, against a federal limit of $2,500,000 for 2025. For most businesses placing meaningful equipment in service, the California deduction is fully phased out."),
("Is a cost segregation study still worth it in California?",
 "Usually yes. The state benefit arrives over five and fifteen years rather than immediately, but accelerating from 27.5 or 39 years is still substantial. The mistake is modeling the state benefit as though it matched the federal one."),
("Do I owe the LLC fee on a property losing money?",
 "Yes. The $800 minimum franchise tax applies regardless of profitability, and the gross receipts fee is assessed on gross California income, not net. A property with negative cash flow still owes both."),
("Can I avoid California tax with a Wyoming LLC?",
 "No. An out-of-state LLC owning California property is doing business in California and owes the same franchise tax, gross receipts fee, and income tax on California-source income. The formation state affects liability protection, not California taxation."),
],
"related": [
("/california/", "California cost segregation and tax planning"),
("/blog/cost-segregation-pennsylvania-state-tax-rules/", "Cost segregation in Pennsylvania"),
("/blog/passive-activity-loss-rules-for-real-estate-investors/", "Passive activity loss rules"),
],
"cta_head": "Model Both Schedules Before You Commission the Study",
"cta_body": "We run California and federal projections side by side so you know what the study is actually worth in your situation. Send us the property detail.",
},

{
"slug": "cost-segregation-new-jersey-state-tax-rules",
"title": "Cost Segregation in New Jersey: Decoupling, Category Income, and the Loss Trap",
"meta_title": "Cost Segregation in New Jersey: State Tax Rules (2026) | AE Tax Advisors",
"meta_desc": "New Jersey decouples from bonus depreciation and does not let rental losses offset wages. What a cost segregation study really does on an NJ-1040.",
"category": C, "date": D,
"intro": [
"New Jersey is one of the least forgiving states for real estate depreciation strategy, and it fails investors in two independent ways. It decouples from bonus depreciation, and its gross income tax uses a category system that prevents rental losses from offsetting wages at all.",
"The second issue is the larger one and it is unique enough that investors moving from other states are frequently caught by it.",
],
"sections": [
("The Category Income System", [
"New Jersey's gross income tax does not compute a single taxable income figure the way federal law does. Income is reported in separate categories, and losses in one category generally cannot offset income in another.",
"Wages are one category. Net profits from business are another. Net gains or income from rents, royalties, patents, and copyrights are another.",
"A net loss in the rental category cannot reduce wage income. It cannot reduce business income. Within the rental category, losses from one property offset income from another, and a net category loss is generally not deductible against other categories and does not carry forward.",
"This is the fact that matters most. A New Jersey investor who runs a cost segregation study producing a large rental loss gets no New Jersey benefit from the loss portion at all, regardless of real estate professional status, regardless of material participation, and regardless of what the federal return shows.",
"Real estate professional status is a federal concept under IRC Sec. 469. It does not change the New Jersey category structure.",
]),
("Decoupling From Bonus Depreciation", [
"New Jersey decouples from federal bonus depreciation. For state purposes, depreciation is computed under MACRS without the Sec. 168(k) allowance.",
"For the corporation business tax, New Jersey requires an addback of federal bonus depreciation and a recomputation. For gross income tax purposes, the state's treatment of depreciation on rental activity similarly does not follow the federal accelerated provisions.",
"The combined effect with the category rules is that a New Jersey investor sees the smaller state depreciation number, and then cannot use even that smaller number against other income if it creates a category loss.",
]),
("What Still Works in New Jersey", [
"A cost segregation study remains valuable where the investor has rental income to shelter. Accelerated depreciation reducing rental category income to zero is fully effective. It is only the excess loss that is wasted at the state level.",
"For an investor with a portfolio generating $180,000 of net rental income, a study that shelters that income entirely produces the full state benefit. For an investor with one property and no other rental income, the state benefit is limited to that property's income.",
"This argues for portfolio-level thinking. An investor acquiring a new property with a large study should consider the timing against the rest of the portfolio's income rather than against wages.",
]),
("The Federal Side Is Unchanged", [
"None of this affects the federal return. Bonus depreciation applies in full, IRC Sec. 469 governs normally, and real estate professional status works as it does everywhere.",
"For a high-income New Jersey household, the federal benefit is usually the dominant number anyway. A 37% federal rate against a New Jersey top rate of 10.75% means roughly three quarters of the value is federal.",
"The error is assuming the New Jersey return will follow, and budgeting cash flow accordingly.",
]),
("Disposition Consequences", [
"Because New Jersey depreciation differs from federal, New Jersey basis differs from federal basis. At sale, New Jersey gain will generally be lower than federal gain, since less depreciation was claimed.",
"New Jersey does not have a preferential capital gain rate. Gain is taxed as ordinary income at rates up to 10.75%.",
"New Jersey also imposes an estimated gross income tax payment requirement on nonresidents selling New Jersey real property, commonly called the exit tax, though it is a withholding mechanism rather than a separate tax. The payment is credited against the actual liability on the return.",
]),
("Worked Example: New Jersey Investor", [
"An investor earns $460,000 in wages and owns four New Jersey rentals generating $71,000 of net rental income before depreciation.",
"They acquire a fifth property for $960,000 and run a cost segregation study. Land is $185,000, leaving $775,000 depreciable. The study reclassifies 24%, identifying $186,000 of bonus eligible components.",
"Federally, first-year depreciation across the new property is approximately $207,000. Combined with the existing portfolio, the federal rental result is a loss of roughly $148,000. The investor's spouse qualifies as a real estate professional with the aggregation election, so the loss is non-passive and offsets wages, saving roughly $55,000 federally.",
"For New Jersey, depreciation is computed without bonus. The new property produces roughly $47,000 of state depreciation. Rental category income drops from $71,000 to approximately $24,000.",
"New Jersey benefit is the tax on $47,000 of sheltered rental income at roughly 9%, or about $4,200. No portion of the federal loss reaches New Jersey wages.",
"The study is still clearly worthwhile. The federal benefit dominates. But an investor who budgeted for a proportional state refund would be $10,000 short.",
CAVEAT,
]),
],
"faqs": [
("Can New Jersey rental losses offset my wages?",
 "No. New Jersey's gross income tax uses a category system where losses in the rental category generally cannot offset wage income or business income. This applies regardless of real estate professional status, which is a federal concept under IRC Sec. 469."),
("Does New Jersey allow bonus depreciation?",
 "No. New Jersey decouples from federal bonus depreciation under IRC Sec. 168(k), requiring depreciation to be computed under MACRS without the additional first-year allowance."),
("Is cost segregation worth it for a New Jersey investor?",
 "Yes, for two reasons. The federal benefit is unaffected and typically dominates, and the state benefit is real to the extent the accelerated depreciation shelters existing rental category income rather than creating an unusable loss."),
("Does real estate professional status help in New Jersey?",
 "Not for the category income problem. REPS under IRC Sec. 469 changes the federal passive classification. New Jersey's restriction on offsetting rental losses against wages is structural and unrelated to the federal passive rules."),
("What is the New Jersey exit tax on a property sale?",
 "It is a withholding requirement on nonresidents selling New Jersey real property, not a separate tax. The estimated payment is credited against the actual liability computed on the New Jersey return, and any excess is refunded."),
],
"related": [
("/new-jersey/", "New Jersey cost segregation and tax planning"),
("/blog/cost-segregation-pennsylvania-state-tax-rules/", "Cost segregation in Pennsylvania"),
("/blog/real-estate-professional-status-qualification-guide/", "Real estate professional status"),
],
"cta_head": "Budget the State Result Separately",
"cta_body": "New Jersey investors routinely overestimate the state refund by five figures. We model both returns before the study is commissioned.",
},

{
"slug": "cost-segregation-new-york-state-tax-rules",
"title": "Cost Segregation in New York: Bonus Depreciation Addbacks and City Tax",
"meta_title": "Cost Segregation in New York: State Tax Rules (2026) | AE Tax Advisors",
"meta_desc": "New York decouples from federal bonus depreciation, requiring an addback and separate schedule. What a study produces on an NY return plus NYC tax.",
"category": C, "date": D,
"intro": [
"New York investors face a two-layer problem. The state decouples from federal bonus depreciation, and New York City imposes its own taxes on top for city residents and for unincorporated businesses operating in the city.",
"The study still works. But the state and city math diverges from the federal math immediately, and it stays divergent for the entire hold period.",
],
"sections": [
("New York Decouples From Bonus Depreciation", [
"New York requires an addback of the federal bonus depreciation deduction under IRC Sec. 168(k) and a recomputation of depreciation as though the provision did not exist. A narrow exception has historically applied to certain property placed in service in designated zones.",
"For state purposes, reclassified components from a cost segregation study depreciate over their normal MACRS recovery periods. Five-year property over five years, 15-year land improvements over fifteen.",
"The reclassification is still worth a great deal at the state level, because moving basis from a 27.5-year or 39-year schedule to five and fifteen years accelerates recovery substantially even without bonus.",
"The consequence is a permanent divergence between federal and New York depreciation schedules and, eventually, between federal and New York basis. Both must be tracked separately.",
]),
("New York City Adds Another Layer", [
"New York City residents pay a city personal income tax on top of state tax, pushing combined marginal rates well above 14% at high incomes.",
"Separately, the city imposes the unincorporated business tax on the income of partnerships and sole proprietorships carrying on a trade or business in the city. Real estate activity is generally excluded from UBT where the taxpayer holds property solely for its own account, which covers most passive rental ownership, but the exclusion has limits and does not extend to dealer activity or to entities providing services.",
"City corporate taxes apply to corporations. The classification of the ownership entity therefore has consequences beyond the state level for New York City property.",
]),
("Passive Loss Rules Follow Federal", [
"New York generally starts from federal adjusted gross income and applies modifications, which means the federal passive activity determination under IRC Sec. 469 carries into the state computation.",
"An investor who qualifies as a real estate professional and generates a non-passive federal loss carries that treatment into New York, subject to the depreciation modification. This is a meaningful advantage over states like New Jersey and Pennsylvania that restrict loss usage structurally.",
"The New York loss will simply be smaller, because the bonus depreciation was added back.",
]),
("Nonresident Owners and Property Transfers", [
"New York taxes nonresidents on New York source income, including rental income from New York property, and requires a nonresident return.",
"New York also imposes real estate transfer taxes at both the state and, for city property, the city level. New York City's real property transfer tax and the state's mansion tax and additional base tax apply to acquisitions and dispositions at rates that make transaction structuring consequential.",
"Transfers of controlling interests in entities holding New York real property can trigger transfer tax as well, which catches investors who assume an entity-level transfer avoids it.",
]),
("Worked Example: Brooklyn Multifamily", [
"An investor acquires a Brooklyn multifamily property for $4,200,000. Land is allocated at $1,100,000, leaving $3,100,000 depreciable. A study reclassifies 22%, identifying $409,200 of five-year property and $272,800 of 15-year land improvements.",
"Federally, the full $682,000 is bonus eligible in year one, plus $87,927 of structural depreciation, for approximately $769,927.",
"For New York, bonus is added back. Five-year property produces roughly $81,840 in year one under MACRS, 15-year property roughly $13,640, and structure $87,927, for approximately $183,407.",
"The first-year difference is $586,520. At a combined New York State and New York City marginal rate near 14.8%, that is roughly $86,800 of state and city benefit deferred rather than lost, recovered across the following fourteen years.",
"Against a straight-line-only alternative, the study still accelerates roughly $95,480 of state depreciation into year one, worth about $14,100 in the first year alone, with the advantage compounding annually.",
CAVEAT,
]),
("Planning Points", [
"Track New York and federal basis separately from acquisition. The divergence begins immediately and is expensive to reconstruct at disposition.",
"For New York City property, confirm the entity classification against the unincorporated business tax rules before acquisition rather than after.",
"Model transfer tax on both acquisition and the anticipated exit, including the controlling interest rules, since the combined transfer tax burden on New York City property is high enough to affect hold period decisions.",
"Where the household includes a spouse who can qualify for real estate professional status, the federal treatment carries into New York, which makes the New York position materially better than New Jersey or Pennsylvania.",
]),
],
"faqs": [
("Does New York allow bonus depreciation?",
 "Generally no. New York requires an addback of the federal bonus depreciation deduction under IRC Sec. 168(k) and a recomputation without it, with a narrow historical exception for certain designated zone property."),
("Is cost segregation worth it in New York?",
 "Yes. Even without bonus depreciation, reclassifying basis from a 27.5-year or 39-year schedule to five and fifteen years accelerates state recovery substantially, and the federal benefit is unaffected."),
("Do New York rental losses offset wages?",
 "Subject to the depreciation modification, yes, where the federal treatment allows it. New York starts from federal adjusted gross income, so a non-passive federal loss under real estate professional status carries into the state computation. This is more favorable than New Jersey or Pennsylvania."),
("Does New York City tax rental income separately?",
 "City residents pay city personal income tax on top of state tax. The unincorporated business tax applies to partnerships and sole proprietorships doing business in the city, though holding property solely for one's own account is generally excluded."),
("Does transferring an LLC interest avoid New York transfer tax?",
 "Often not. Transfers of controlling interests in entities holding New York real property can trigger transfer tax at the state and city level. This catches investors who assume an entity-level transfer is outside the transfer tax rules."),
],
"related": [
("/new-york/", "New York cost segregation and tax planning"),
("/blog/cost-segregation-multifamily-apartment-buildings/", "Cost segregation for multifamily"),
("/blog/entity-structuring-rental-property-portfolios/", "Entity structuring for rental portfolios"),
],
"cta_head": "Two Schedules, Three Tax Layers",
"cta_body": "New York property requires federal, state, and city modeling together. Send us the acquisition detail and entity structure and we will run all three.",
},

{
"slug": "cost-segregation-north-carolina-state-tax-rules",
"title": "Cost Segregation in North Carolina: The 85 Percent Addback and Five Year Recovery",
"meta_title": "Cost Segregation in North Carolina: State Tax Rules (2026) | AE Tax Advisors",
"meta_desc": "North Carolina requires an 85 percent bonus depreciation addback recovered over five years. How that changes cost segregation timing on an NC return.",
"category": C, "date": D,
"intro": [
"North Carolina uses an addback and recovery model rather than outright decoupling, which puts it in a middle tier among states. You do not get the full federal deduction in year one, but you do not lose it either. You get 15% of it now and the rest across the following five years.",
"With a flat individual income tax rate, the modeling is unusually clean compared to graduated-rate states.",
],
"sections": [
("How the Addback Works", [
"North Carolina requires taxpayers to add back 85% of the federal bonus depreciation deduction claimed under IRC Sec. 168(k). The remaining 15% flows through to the state return in the year claimed.",
"The added-back amount is then deducted in equal installments over the following five taxable years, at 20% of the addback per year.",
"The mechanism is a timing difference rather than a permanent one. Over six years, the full federal bonus deduction is recognized for North Carolina purposes. Nothing is lost.",
"North Carolina applies a parallel addback and recovery mechanism to Sec. 179 amounts exceeding the state's own limitation, which has historically been set below the federal amount.",
]),
("What This Means for a Study", [
"A cost segregation study producing $500,000 of federal bonus depreciation produces $75,000 of North Carolina deduction in year one, with $85,000 deducted in each of the following five years.",
"Compared to states that decouple entirely, this is favorable. The full benefit arrives, just spread.",
"Compared to full conformity states, the first-year state result is muted, which matters for investors modeling cash flow around a large first-year refund.",
"The five-year recovery also creates a useful planning feature. An investor with rising income over the next several years receives the deduction in higher-rate years, though with a flat state rate the timing is neutral for state purposes.",
]),
("The Flat Rate Simplifies Modeling", [
"North Carolina applies a flat individual income tax rate that has been scheduled to decline under enacted legislation. Because the rate is flat, there is no bracket management to perform at the state level.",
"That flatness matters for the addback recovery. A deduction received five years from now is worth the same rate as one received today, subject to whatever rate is then in effect. Where scheduled rate reductions are in force, a deferred deduction is actually worth slightly less, which argues modestly against deferral strategies at the state level.",
]),
("Passive Loss Treatment", [
"North Carolina begins from federal adjusted gross income with modifications, so the federal passive activity determination under IRC Sec. 469 carries through.",
"An investor qualifying as a real estate professional with the aggregation election generates a non-passive federal loss, and that treatment carries into the North Carolina computation, subject to the bonus depreciation addback.",
"This makes North Carolina considerably more favorable than category-income states, because the loss can offset wage income at the state level once the addback adjustment is applied.",
]),
("Nonresident Owners", [
"North Carolina taxes nonresidents on income from North Carolina sources, including rental income from North Carolina property. A nonresident return is required.",
"Pass-through entities with nonresident owners generally must withhold on the nonresidents' share of North Carolina income, which creates a credit claimed on the nonresident return.",
"North Carolina also offers a pass-through entity tax election, allowing the entity to pay state tax at the entity level. For owners subject to the federal state and local tax deduction limitation, this can convert a non-deductible personal state tax payment into a deductible entity-level expense. Investors with meaningful North Carolina income should model this.",
]),
("Worked Example: Charlotte Rental Portfolio", [
"An investor acquires a Charlotte multifamily property for $3,400,000. Land is allocated at $610,000, leaving $2,790,000 depreciable. A study reclassifies 25%, identifying $697,500 of bonus eligible components.",
"Federal first-year depreciation is approximately $697,500 of bonus plus $76,036 of structural depreciation, for $773,536.",
"For North Carolina, 85% of the $697,500 bonus amount, or $592,875, is added back. Year one North Carolina depreciation is $104,625 of allowed bonus plus $76,036 of structure, for $180,661.",
"In each of the following five years, North Carolina allows an additional $118,575 of the added-back amount, on top of ongoing MACRS depreciation on the remaining basis.",
"By year six, cumulative North Carolina depreciation equals cumulative federal depreciation. The study's full value is realized at the state level, just later.",
CAVEAT,
]),
("Planning Points", [
"Track the addback recovery schedule explicitly. It runs for five years after each year in which bonus depreciation is claimed, so an investor running studies in consecutive years has overlapping recovery schedules that are easy to lose track of.",
"Model the pass-through entity tax election, particularly for investors whose personal state and local tax deduction is capped federally.",
"Because the state benefit is deferred rather than denied, North Carolina does not change the decision to run a study. It changes only the cash flow timing, which should be reflected in the projection.",
]),
],
"faqs": [
("Does North Carolina allow bonus depreciation?",
 "Partially. North Carolina requires an addback of 85% of the federal bonus depreciation deduction, with 15% allowed currently. The added-back amount is then deducted in equal installments over the following five years, so nothing is permanently lost."),
("Is cost segregation still worth it in North Carolina?",
 "Yes. The federal benefit is unaffected, and the state benefit arrives in full over six years rather than being denied. Only the cash flow timing changes, which should be reflected in the projection rather than treated as a reason to skip the study."),
("Can North Carolina rental losses offset wages?",
 "Subject to the addback, yes, where the federal treatment allows it. North Carolina begins from federal adjusted gross income, so a non-passive loss under real estate professional status carries into the state computation."),
("Should I make the pass-through entity tax election?",
 "Often yes for investors whose federal state and local tax deduction is capped. The election lets the entity pay North Carolina tax at the entity level, converting a limited personal deduction into a deductible entity-level expense. Model it against your full picture."),
("How do I track the addback recovery?",
 "Maintain a schedule by year of origination. Each year in which you claim bonus depreciation starts its own five-year recovery, so consecutive studies produce overlapping schedules that are easy to lose track of and expensive to reconstruct."),
],
"related": [
("/north-carolina/", "North Carolina cost segregation and tax planning"),
("/blog/cost-segregation-multifamily-apartment-buildings/", "Cost segregation for multifamily"),
("/blog/bonus-depreciation-obbba-permanent-100-percent/", "Permanent 100% bonus depreciation"),
],
"cta_head": "The Deduction Arrives, Just on a Schedule",
"cta_body": "We build the six-year North Carolina recovery projection alongside the federal one so the cash flow model is accurate. Send us the property detail.",
},

{
"slug": "cost-segregation-texas-and-florida-no-income-tax-states",
"title": "Cost Segregation in Texas and Florida: What No State Income Tax Actually Changes",
"meta_title": "Cost Segregation in Texas and Florida (2026 Guide) | AE Tax Advisors",
"meta_desc": "No state income tax means the federal deduction is the whole story, but franchise tax, property tax, and residency planning still matter for investors.",
"category": C, "date": D,
"intro": [
"Texas and Florida impose no individual income tax, which makes cost segregation modeling refreshingly simple. There is no addback, no separate state depreciation schedule, no divergent basis, and no state passive loss analysis.",
"What the federal return shows is what you get. That simplicity is real, but it also means three other things carry more weight than investors expect.",
],
"sections": [
("The Federal Deduction Is the Entire Deduction", [
"In states like California or New York, an investor tracks two depreciation schedules for the life of the property and reconciles two different bases at disposition. In Texas and Florida, there is one schedule.",
"That removes a genuine ongoing compliance cost. It also removes the modeling complexity that causes so many investors in decoupled states to overestimate their benefit.",
"For an investor comparing markets, this is a real if modest advantage. A study producing $600,000 of federal deduction in Texas produces $600,000 of usable deduction. The same study in New Jersey produces $600,000 federally and a much smaller, differently structured state result.",
]),
("Texas Franchise Tax", [
"Texas imposes a franchise tax, often called the margin tax, on entities doing business in the state. There is a no-tax-due threshold that exempts entities below a revenue level, and many small real estate holding entities fall below it.",
"Above the threshold, the tax is computed on taxable margin, generally the lesser of 70% of total revenue, total revenue less cost of goods sold, or total revenue less compensation, with a separate calculation available for entities below a revenue ceiling.",
"For real estate entities, the cost of goods sold subtraction is generally unavailable for rental activity, which pushes most rental entities to the compensation subtraction or the 70% method.",
"The rate is low, but the tax applies to margin rather than net income, so an entity with a large depreciation deduction and negative taxable income can still owe franchise tax. Depreciation does not reduce the margin tax base the way it reduces income tax.",
"Passive entities meeting specific statutory requirements may be exempt. The requirements are technical and turn on the composition of income, so entity structuring for Texas property should account for this rather than assume exemption.",
]),
("Florida Corporate Income Tax and Entity Choice", [
"Florida imposes no individual income tax but does impose a corporate income tax on entities taxed as corporations. Partnerships and disregarded entities are generally not subject to it, which is one reason Florida real estate is rarely held in corporate form.",
"Florida decouples from federal bonus depreciation for corporate income tax purposes, requiring an addback with recovery over subsequent years. This is irrelevant to an individual investor holding through an LLC taxed as a partnership or disregarded entity, and highly relevant to anyone holding through a C corporation.",
"The practical guidance is straightforward. Hold Florida real estate in a pass-through structure and the corporate rules never apply.",
]),
("Property Tax Carries More Weight", [
"Both states fund heavily through property tax, and rates in many Texas jurisdictions exceed 2% of assessed value. On a $4,000,000 property that is $80,000 annually, which is larger than the state income tax an investor would have paid in most states.",
"Texas has no cap on annual assessment increases for non-homestead property, so commercial and rental assessments can rise sharply after an acquisition. The purchase price itself frequently triggers reassessment.",
"Florida's Save Our Homes cap applies to homestead property, not to rental or commercial property, which is subject to a separate and higher assessment growth cap.",
"Protesting assessments is a routine and worthwhile exercise in both states, and it is a larger annual line item than most state income tax planning would be.",
]),
("Residency Planning Is the Larger Opportunity", [
"For an investor currently residing in a high-tax state, the more consequential planning question is not how the study performs in Texas or Florida but whether the investor should become a resident.",
"A move from California or New York to Florida or Texas eliminates state tax on all income, not just rental income. For a household with $1,200,000 of income, that is $130,000 or more annually.",
"High-tax states audit these moves aggressively. Establishing residency requires more than a lease and a driver's license. Domicile turns on where you actually live, where your family is, where your possessions are, where your professional and social connections are, and where you spend your days.",
"Day counting matters and is verifiable through cell phone records, credit card activity, and travel documentation. Investors making this move should assume the departure state will examine it and should document accordingly from the start.",
"Property in the former state continues to generate source income and filing obligations there regardless of residency.",
]),
("Worked Example: Texas Acquisition", [
"An investor acquires a Houston self-storage facility for $6,800,000. Land is allocated at $1,200,000, leaving $5,600,000 depreciable. A study reclassifies 32%, identifying $1,792,000 of bonus eligible components.",
"Federal first-year depreciation is $1,792,000 of bonus plus $97,641 of structural depreciation, for approximately $1,889,641. There is no state adjustment. The full amount is the deduction.",
"The property is held in a Texas LLC taxed as a partnership. The entity's total revenue is $840,000, above the no-tax-due threshold, so franchise tax applies on taxable margin. Depreciation does not reduce the margin base, so the franchise tax is owed regardless of the large income tax deduction.",
"Property tax at roughly 2.3% of assessed value runs approximately $156,000 annually and is a deductible operating expense.",
"The modeling is clean. One depreciation schedule, one basis, no reconciliation, and a franchise tax and property tax analysis that operates independently of the income tax result.",
CAVEAT,
]),
],
"faqs": [
("Do Texas and Florida allow bonus depreciation?",
 "The question does not arise for individual investors, since neither state imposes an individual income tax. The federal deduction is the entire deduction. Florida's corporate income tax does require a bonus depreciation addback, which is why Florida real estate is rarely held in corporate form."),
("Does depreciation reduce the Texas franchise tax?",
 "No. The Texas franchise tax is computed on taxable margin rather than net income, so a large depreciation deduction does not reduce the base. An entity with negative taxable income for federal purposes can still owe franchise tax."),
("Is a cost segregation study more valuable in a no-income-tax state?",
 "The federal benefit is identical everywhere. What changes is that there is no offsetting state complexity, no divergent basis to track, and no risk of overestimating a state benefit that does not materialize. The simplicity is real but the deduction itself is the same."),
("Should I move to Texas or Florida for tax reasons?",
 "For a high-income household it can be worth six figures annually, well beyond any rental strategy. But high-tax states audit these moves aggressively. Domicile turns on where you actually live, and day counting is verifiable. Document the move thoroughly from the beginning."),
("Do I still owe tax in my old state if I keep property there?",
 "Yes. Property in another state generates source income there and requires a nonresident return regardless of where you live. Moving changes the tax on your other income, not on income sourced to the state you left."),
],
"related": [
("/texas/", "Texas cost segregation and tax planning"),
("/florida/", "Florida cost segregation and tax planning"),
("/blog/cost-segregation-self-storage-facilities/", "Cost segregation for self storage"),
],
"cta_head": "Simple Modeling, Different Levers",
"cta_body": "In no-income-tax states the planning shifts to entity structure, franchise tax, and residency. Bring your property list and current state of residence.",
},

{
"slug": "cost-segregation-massachusetts-state-tax-rules",
"title": "Cost Segregation in Massachusetts: Decoupling and the Millionaires Tax",
"meta_title": "Cost Segregation in Massachusetts: State Tax Rules (2026) | AE Tax Advisors",
"meta_desc": "Massachusetts decouples from bonus depreciation and adds a 4 percent surtax above $1 million. How a study performs on a Massachusetts return in 2026.",
"category": C, "date": D,
"intro": [
"Massachusetts decouples from federal bonus depreciation, so a cost segregation study produces a much smaller first-year state deduction than the federal return suggests.",
"The state also imposes a 4% surtax on taxable income above roughly $1,000,000, indexed annually. That surtax interacts with large one-time deductions in a way that makes timing genuinely valuable rather than merely convenient.",
],
"sections": [
("Massachusetts Does Not Follow Bonus Depreciation", [
"Massachusetts has decoupled from the federal bonus depreciation allowance under IRC Sec. 168(k). Depreciation for state purposes is computed under MACRS without the additional first-year allowance.",
"Reclassified components still depreciate over their shorter recovery periods, so a study accelerates state depreciation meaningfully relative to a 27.5-year or 39-year schedule. It simply does not produce a single large first-year state deduction.",
"Massachusetts and federal basis therefore diverge from the first year and must be tracked separately through disposition.",
]),
("The Surtax Changes the Timing Calculus", [
"Massachusetts imposes a surtax of 4% on the portion of annual taxable income exceeding a threshold near $1,000,000, indexed for inflation, on top of the base individual rate.",
"This creates a genuine bracket to manage, which is unusual in a flat-rate state. Income above the threshold faces a materially higher combined rate.",
"The surtax is computed on annual taxable income, so a one-time spike, such as a property sale or a business exit, can push a household above the threshold for a single year. Deductions that reduce income in that specific year are worth more than deductions in ordinary years.",
"For an investor anticipating a large gain, running a cost segregation study on another property in the same year to shelter income below the threshold is a legitimate and valuable timing strategy. Because the study can be run as a look-back with Form 3115 on property already owned, the deduction can be placed in the year it is needed rather than the year of acquisition.",
]),
("Capital Gains Treatment", [
"Massachusetts taxes long-term capital gains at the base individual rate, with certain short-term gains taxed at a higher rate. The surtax applies on top where total taxable income exceeds the threshold.",
"A property sale generating $1,800,000 of gain will push most households well past the surtax threshold. The combined state rate on the excess is meaningfully higher than on ordinary years, which strengthens the case for either installment structuring under IRC Sec. 453 or a 1031 exchange under IRC Sec. 1031.",
"Because Massachusetts depreciation is lower than federal depreciation, Massachusetts basis is higher and Massachusetts gain is lower. This partially offsets the surtax exposure and should be computed rather than assumed.",
]),
("Passive Loss Rules", [
"Massachusetts generally follows the federal passive activity determination, so real estate professional status and the aggregation election carry into the state computation.",
"The state loss will be smaller because of the depreciation modification, but the character of the loss follows federal treatment. This is more favorable than category-income states.",
]),
("Worked Example: Timing Around the Surtax", [
"An investor sells a Boston-area property in the current year, generating $2,300,000 of Massachusetts taxable gain. Household income including the gain is approximately $2,650,000, placing roughly $1,650,000 above the surtax threshold.",
"The 4% surtax on that excess is approximately $66,000 on top of base tax.",
"The investor also owns two rental properties acquired in 2022 and 2023 that have never been studied. Look-back cost segregation studies filed with Form 3115 produce a combined Sec. 481(a) adjustment of approximately $486,000 federally.",
"For Massachusetts, the adjustment is smaller because bonus depreciation is added back, but the reclassification to five-year and 15-year schedules still produces a catch-up of roughly $214,000 for state purposes.",
"That $214,000 reduces income subject to the surtax, saving approximately $8,560 in surtax alone plus base tax on the same amount.",
"Federally, the $486,000 deduction against a 37% rate is worth roughly $180,000.",
"The key point is that the deduction was placed in the year it was worth the most. Had the studies been run in 2022 and 2023 when the properties were acquired, the deductions would have landed in ordinary years and the surtax exposure in the sale year would have been unmitigated.",
CAVEAT,
]),
("Planning Points", [
"Track Massachusetts and federal basis separately from acquisition. The divergence is permanent and reconstructing it at sale is expensive.",
"Treat the surtax threshold as a planning target. Deductions are worth 4% more when they land in a year that crosses it.",
"Use look-back studies deliberately. The ability to place a large deduction in a chosen year through Form 3115 is the most useful timing tool available to a Massachusetts investor.",
"For anticipated large gains, model installment sale treatment under IRC Sec. 453 against a 1031 exchange, since spreading gain across years can keep each year below the surtax threshold.",
]),
],
"faqs": [
("Does Massachusetts allow bonus depreciation?",
 "No. Massachusetts has decoupled from the federal bonus depreciation allowance under IRC Sec. 168(k). State depreciation is computed under MACRS without the additional first-year allowance, so federal and Massachusetts basis diverge immediately."),
("What is the Massachusetts millionaires tax?",
 "A 4% surtax on the portion of annual taxable income above a threshold near $1,000,000, indexed for inflation, applied on top of the base individual rate. Because it is computed annually, one-time income spikes such as property sales are heavily exposed to it."),
("Can I time a cost segregation study to reduce the surtax?",
 "Yes, and this is the most useful timing tool available. A look-back study filed with Form 3115 on a property you already own places the catch-up deduction in the current year, which lets you offset a gain year rather than an ordinary year."),
("Is cost segregation worth it in Massachusetts?",
 "Yes. The federal benefit is unaffected, and even without bonus depreciation the state benefit from reclassifying to five-year and 15-year schedules is substantial relative to 27.5 or 39 years."),
("Does Massachusetts follow federal passive loss rules?",
 "Generally yes. Real estate professional status and the aggregation election carry into the Massachusetts computation, so the character of the loss follows federal treatment. Only the amount differs, because of the depreciation modification."),
],
"related": [
("/massachusetts/", "Massachusetts cost segregation and tax planning"),
("/blog/form-3115-cost-segregation-catch-up/", "Form 3115 catch-up depreciation"),
("/blog/seller-financing-tax-treatment-installment-sales/", "Installment sales and gain spreading"),
],
"cta_head": "Place the Deduction in the Year That Needs It",
"cta_body": "Massachusetts rewards deliberate timing more than most states. Bring your properties, your prior studies, and any anticipated sale.",
},
]

if __name__ == "__main__":
    write_all(ARTICLES)
