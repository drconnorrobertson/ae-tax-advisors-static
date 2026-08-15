#!/usr/bin/env python3
"""Long-tail keyword posts, batch B: participation, REPS, and specialty cost seg."""

POSTS = [

# ---------------------------------------------------------------- 6
{
"slug": "material-participation-short-term-rental-7-day-rule",
"h1": "Material Participation and the Short-Term Rental 7-Day Rule",
"title": "Material Participation: STR 7-Day Rule",
"description": "The 7-day rule takes a short-term rental outside the passive rental category, but only material participation makes the loss deductible against wages. Here are the seven tests and how to document them.",
"subtitle": "The seven-day rule and material participation are two separate hurdles. Clearing one without the other leaves the loss suspended.",
"keywords": ["material participation short term rental", "7 day rule", "STR material participation", "1.469-1T(e)(3)(ii)"],
"definition": "The short-term rental 7-day rule is the exception in Treasury Regulation 1.469-1T(e)(3)(ii)(A) under which a rental property with an average period of customer use of seven days or less is not treated as a rental activity for passive activity loss purposes. Because it is not a rental activity, the per se passive rule of IRC Section 469(c)(2) does not apply, and the owner needs only to materially participate under one of the seven tests in Treasury Regulation 1.469-5T for the losses to be non-passive and deductible against wages and other ordinary income.",
"sections": [
 ("Two Separate Hurdles, Not One", [
  "Almost every misunderstanding in this area comes from collapsing two distinct requirements into one. They are independent, and you must clear both.",
  "<strong>Hurdle one: escape rental classification.</strong> IRC Section 469(c)(2) makes rental activities passive regardless of participation. Treasury Regulation 1.469-1T(e)(3)(ii) lists six exceptions that remove an activity from the definition of rental activity, and the first is an average period of customer use of seven days or less.",
  "<strong>Hurdle two: materially participate.</strong> Escaping rental classification only means the activity is treated like any other trade or business. Trade or business activities are still passive unless you materially participate under Treasury Regulation 1.469-5T.",
  "Clearing hurdle one alone gets you nothing. The activity is simply a non-rental passive activity, and the loss remains suspended. Clearing hurdle two without hurdle one gets you nothing either, because a rental activity stays passive under Section 469(c)(2) even with material participation, unless you qualify as a real estate professional.",
 ]),
 ("How the Average Period of Customer Use Is Calculated", [
  "The average is computed by dividing total rental days by the number of rental periods for the year, not by counting how many bookings were short.",
  "If a property is rented for 200 total days across 50 separate bookings, the average period of customer use is 4.0 days and the exception applies. If the same 200 days come from 20 bookings, the average is 10 days and it does not.",
  "This is measured per property, per year, unless activities are grouped. A single long winter booking can pull the annual average above seven days and destroy the treatment for the entire year, which is why owners relying on this exception need to monitor the running average rather than checking it in January.",
  "A second exception in the same regulation covers average periods of thirty days or less where the owner provides significant personal services, and a third covers extraordinary personal services with no time limit. Those are narrower and rarely the cleanest path, but they exist for properties that cannot hold a seven-day average.",
 ]),
 ("The Seven Material Participation Tests", [
  "Treasury Regulation 1.469-5T(a) provides seven tests. Meeting any one is sufficient.",
  "<strong>Test 1:</strong> More than 500 hours in the activity during the year.",
  "<strong>Test 2:</strong> Your participation constitutes substantially all of the participation of all individuals in the activity, including non-owners.",
  "<strong>Test 3:</strong> More than 100 hours, and no other individual participates more than you. This is the workhorse test for short-term rentals.",
  "<strong>Test 4:</strong> The activity is a significant participation activity, more than 100 hours, and your combined significant participation activities exceed 500 hours.",
  "<strong>Test 5:</strong> You materially participated in the activity for any five of the preceding ten tax years.",
  "<strong>Test 6:</strong> The activity is a personal service activity in which you materially participated for any three preceding years.",
  "<strong>Test 7:</strong> Based on all facts and circumstances, you participated on a regular, continuous, and substantial basis. This test requires more than 100 hours and is the least reliable to rely on.",
  "For a typical owner-operated short-term rental, Test 3 is the realistic target. The critical word is <em>individual</em>, not <em>owner</em>. If you use a property manager who spends more hours than you do, you fail Test 3 even if you spend 300 hours yourself. That single fact defeats more STR positions than any other.",
 ]),
 ("What Counts as Participation and What Does Not", [
  "Qualifying work generally includes guest communication and booking management, cleaning and turnover when you do it yourself, maintenance and repairs, supply purchasing and restocking, listing creation and pricing management, coordinating and supervising contractors, bookkeeping for the activity, and property inspections.",
  "Work that does not count includes investor activities such as reviewing financial statements or analyzing the investment, unless you are also involved in day-to-day management; travel time to and from the property, which the IRS has consistently challenged; and work of a type not customarily done by owners if a principal purpose was to avoid the passive loss rules.",
  "Spousal hours count. Participation by a spouse is attributed to the taxpayer under Section 469(h)(5) even if the spouse has no ownership interest and the couple files separately. For couples where one spouse has a demanding W-2 job, running the hours through the other spouse is a legitimate and common approach.",
 ]),
 ("Documentation That Survives Examination", [
  "The regulation permits proof by any reasonable means and does not require contemporaneous daily logs. In practice, the Tax Court has rejected reconstructed summaries repeatedly, and the IRS treats a log created after the fact as weak evidence.",
  "A defensible record has a date, the time spent, a specific description of the task, and corroboration. Corroboration is what separates a credible log from a spreadsheet of round numbers: booking platform message timestamps, cleaning and supply receipts, contractor invoices and text threads, calendar entries, bank and card records, and photographs with metadata.",
  "Two patterns draw scrutiny. Round numbers, where every entry is exactly two or four hours, and totals that land just above a threshold, such as 101 or 501 hours. Real logs are irregular.",
  "Keep the log for the year the loss is claimed and for every year the position depends on, since Test 5 can pull earlier years into the analysis.",
 ]),
 ("Grouping Elections and When They Help", [
  "Under Treasury Regulation 1.469-4, activities that constitute an appropriate economic unit may be grouped and tested together for material participation.",
  "For an owner with several short-term rentals, grouping means hours are aggregated across properties, which makes the 500-hour test achievable when no single property would reach it. The tradeoff is that a grouped activity is treated as one activity for disposition purposes, so suspended losses are not freed until substantially all of the group is sold.",
  "Grouping is generally made by filing a written statement with the return for the first year, and once made it is binding unless the original grouping was clearly inappropriate or facts change materially.",
  "Note that short-term rentals excluded from rental treatment by the seven-day rule are business activities, and grouping them with genuine rental activities creates problems. These groupings should be structured deliberately, not assumed.",
 ]),
 ("Common Failures We See", [
  "Using a full-service property manager and still claiming Test 3. The manager's hours almost always exceed the owner's.",
  "Averaging above seven days because of one long booking, discovered only at filing time.",
  "Counting travel time to reach the property, which is routinely disallowed.",
  "Reconstructing a log in March for the prior year, with round numbers and no corroboration.",
  "Assuming the STR exception makes the owner a real estate professional. It does not; they are separate provisions with separate consequences.",
  "Buying the property in late December and expecting to reach 100 hours before year end while also being outparticipated by cleaners and contractors during the rehab.",
 ]),
],
"faqs": [
 ("What is the 7-day rule for short-term rentals?",
  "<p>Under Treasury Regulation 1.469-1T(e)(3)(ii)(A), a property whose average period of customer use is seven days or less is not a rental activity for passive loss purposes. That removes the automatic passive classification of Section 469(c)(2), but the owner must still materially participate for losses to be non-passive.</p>"),
 ("How many hours do I need for material participation in a short-term rental?",
  "<p>There is no single number. The most commonly used test is Test 3: more than 100 hours, provided no other individual participates more than you. Test 1 is a flat 500 hours with no comparison to others. If you use a property manager who works more hours than you, Test 3 fails regardless of your own total.</p>"),
 ("Does using a property manager disqualify me?",
  "<p>Not automatically, but it usually defeats the 100-hour test because the manager's hours exceed yours. You would then need to meet the 500-hour test on your own, or restructure the arrangement so you handle guest communication, pricing, maintenance coordination, and turnovers directly.</p>"),
 ("Do my spouse's hours count toward material participation?",
  "<p>Yes. IRC Section 469(h)(5) attributes a spouse's participation to the taxpayer even if the spouse holds no ownership interest and even if you file separately. This is frequently how couples with one demanding W-2 career meet the tests.</p>"),
 ("Is the 7-day rule the same as real estate professional status?",
  "<p>No. They are separate provisions. The seven-day rule removes an activity from rental treatment so that only material participation is needed. Real estate professional status under Section 469(c)(7) applies to genuine rental activities and requires more than 750 hours in real property trades or businesses plus more than half of all personal services.</p>"),
],
"related": [
 ("/short-term-rental-tax-loophole-2026/", "The Short-Term Rental Tax Loophole in 2026"),
 ("/reps-real-estate-professional-status/", "Real Estate Professional Status: How to Qualify"),
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works and What It Costs"),
 ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026 Under the OBBBA"),
 ("/str-vs-ltr-tax-treatment/", "STR vs LTR Tax Treatment Compared"),
],
"takeaways": [
 "The seven-day rule and material participation are two separate requirements and both must be met.",
 "Average period of customer use is total rental days divided by number of bookings, not a count of short stays.",
 "Test 3, more than 100 hours with no individual participating more, is the realistic target and the reason property managers are so often fatal.",
 "Spousal hours are attributed to the taxpayer, which is the most useful planning fact in this area.",
 "Contemporaneous, corroborated, irregular logs survive examination; reconstructed round-number summaries do not.",
]},

# ---------------------------------------------------------------- 7
{
"slug": "reps-real-estate-professional-status",
"h1": "REPS: Real Estate Professional Status and How to Actually Qualify",
"title": "REPS: Real Estate Professional Status",
"description": "Real estate professional status under IRC 469(c)(7) makes rental losses non-passive. Here are the two statutory tests, the aggregation election, what counts toward 750 hours, and how the position is defended.",
"subtitle": "REPS is the most valuable and most frequently disallowed position in real estate taxation. The rules are strict, mechanical, and unforgiving of poor records.",
"keywords": ["real estate professional status", "REPS", "750 hours", "IRC 469(c)(7)", "aggregation election"],
"definition": "Real estate professional status (REPS) is a tax classification under IRC Section 469(c)(7) that removes the automatic passive treatment of rental real estate. A taxpayer qualifies by satisfying two tests in the same year: more than half of all personal services performed in all trades or businesses must be performed in real property trades or businesses in which the taxpayer materially participates, and the taxpayer must perform more than 750 hours of service in those real property trades or businesses. Qualifying makes rental activities in which the taxpayer also materially participates non-passive, so losses may offset wages, business income, and portfolio income.",
"sections": [
 ("The Two Tests, and Why the First One Is the Hard One", [
  "Both tests must be met in the same tax year, and neither can be averaged across years.",
  "<strong>The more-than-half test.</strong> More than 50% of the personal services you perform in all trades or businesses during the year must be in real property trades or businesses in which you materially participate. This is a relative test, and it is where most high-earning taxpayers fail.",
  "<strong>The 750-hour test.</strong> You must perform more than 750 hours of services in real property trades or businesses in which you materially participate. This is an absolute floor.",
  "The interaction is what defeats people. A physician working 1,800 hours in a medical practice would need more than 1,800 hours in real property trades or businesses to satisfy the more-than-half test, not 751. The 750-hour figure is a minimum, not the target, and for anyone with a substantial W-2 job the real target is far higher.",
  "This is why REPS in a married couple is so often assigned to the non-W-2 spouse. Critically, the two tests are applied to each spouse individually and cannot be combined, even on a joint return. One spouse must satisfy both tests alone. Only after one spouse qualifies do the material participation rules allow spousal hours to be combined at the activity level.",
 ]),
 ("What Counts as a Real Property Trade or Business", [
  "Section 469(c)(7)(C) defines these as any real property development, redevelopment, construction, reconstruction, acquisition, conversion, rental, operation, management, leasing, or brokerage trade or business.",
  "That is broad, and it captures general contractors, developers, real estate agents and brokers, property managers, and landlords who operate their portfolios directly.",
  "It does not capture activities that merely relate to real estate. Mortgage brokering, real estate lending, appraisal, title work, and passive investment in real estate partnerships are generally outside the definition. Neither does work as an employee count, unless you own more than 5% of the employer, which is a specific statutory carve-out in Section 469(c)(7)(D)(ii).",
  "That 5% rule matters for real estate agents who work as W-2 employees of a brokerage they do not own. Their hours may not count at all.",
 ]),
 ("The Aggregation Election Under Reg. 1.469-9(g)", [
  "Qualifying as a real estate professional does not by itself make your rental losses deductible. It only removes the per se passive rule. You must then materially participate in each rental activity separately.",
  "For an investor with eight properties, testing each one separately is usually impossible. The solution is the election under Treasury Regulation 1.469-9(g) to treat all interests in rental real estate as a single activity. Hours across all properties are then aggregated for the material participation test.",
  "The election is made by attaching a statement to an original return declaring that the taxpayer is a qualifying taxpayer and is making the election under Section 469(c)(7)(A). It is binding for all future years in which the taxpayer qualifies, and it may only be revoked when a material change in facts and circumstances occurs.",
  "Revenue Procedure 2011-34 provides late election relief for taxpayers who failed to file the statement but otherwise behaved consistently with having made it. This relief has saved a large number of positions, and it is worth checking before conceding an examination.",
  "There is a cost. Because the grouped rentals are one activity, suspended losses are not released on the sale of a single property. They are released when substantially all of the grouped activity is disposed of.",
 ]),
 ("Hours That Count and Hours That Do Not", [
  "Counted: acquisition due diligence and property tours, negotiating purchases and financing, arranging and supervising repairs and improvements, tenant screening, showings, and lease negotiation, rent collection and enforcement, bookkeeping and record maintenance for the properties, insurance and vendor management, and direct maintenance work.",
  "Not counted: investor-type activities such as reviewing financial statements, studying reports, and analyzing finances, unless performed as part of day-to-day management under Reg. 1.469-5T(f)(2)(ii); education and seminars; time spent searching for properties you never acquire, which courts have treated inconsistently and which is safest to segregate; and travel time, which the IRS regularly challenges.",
  "The distinction between manager and investor is the most litigated issue in this area. Someone who owns eight properties, uses a management company for all of them, and spends their hours reviewing statements is an investor, not a real estate professional, no matter how many hours they log.",
 ]),
 ("How These Cases Are Actually Lost", [
  "The Tax Court record is consistent and instructive. Positions fail for a small number of recurring reasons.",
  "<strong>No contemporaneous log.</strong> Reconstructed calendars prepared for an examination are given little weight. This is the single most common cause of loss.",
  "<strong>Implausible totals.</strong> Logs showing hours that exceed what the properties could plausibly require, or that conflict with the taxpayer's W-2 work schedule, are rejected outright.",
  "<strong>Failing the more-than-half test.</strong> A taxpayer with a full-time job who logs 800 rental hours meets the 750-hour test and fails the relative test, and the whole position collapses.",
  "<strong>No aggregation election.</strong> The taxpayer qualifies as a real estate professional but cannot show material participation in each individual property, and never made the grouping election.",
  "<strong>Property manager participation.</strong> Third-party management hours exceeding the owner's undermine material participation even after REPS is established.",
 ]),
 ("Building a Position That Holds", [
  "Decide which spouse will qualify before the year begins, and structure the work accordingly. This is a planning decision, not a filing decision.",
  "Track hours daily in a dated log with task descriptions, and keep the corroborating records that make it credible: emails, invoices, calendars, receipts, and platform timestamps.",
  "File the aggregation election with the first return in which you qualify. If you should have filed it earlier, evaluate relief under Rev. Proc. 2011-34.",
  "Reduce reliance on third-party property managers, or restructure so that you retain the functions that generate hours: tenant relations, vendor supervision, and maintenance decisions.",
  "Model what REPS is actually worth before organizing your year around it. It is most valuable in a year with large depreciation deductions, typically from a cost segregation study or a Form 3115 catch-up. Without significant losses to release, REPS may not justify the operational changes required.",
 ]),
],
"faqs": [
 ("What are the requirements for real estate professional status?",
  "<p>Two tests must be met in the same year under IRC Section 469(c)(7): more than half of all personal services you perform in all trades or businesses must be in real property trades or businesses in which you materially participate, and you must perform more than 750 hours in those businesses. Both are required, and the first is usually the harder one.</p>"),
 ("Can my spouse and I combine hours to reach 750?",
  "<p>No. The two qualification tests are applied to each spouse individually and cannot be combined, even on a joint return. One spouse must satisfy both tests alone. Once one spouse qualifies, spousal participation may then be combined for testing material participation in the rental activities themselves.</p>"),
 ("Do I need to make an aggregation election?",
  "<p>If you own more than one or two rentals, almost certainly. Without the election under Reg. 1.469-9(g), you must materially participate in each property separately, which is rarely achievable. The election groups all rental interests into a single activity so hours aggregate.</p>"),
 ("Does time as a W-2 employee of a real estate company count?",
  "<p>Only if you own more than 5% of the employer. Section 469(c)(7)(D)(ii) excludes services performed as an employee unless the taxpayer holds more than a 5% interest, which affects agents and managers employed by brokerages they do not own.</p>"),
 ("What proof does the IRS accept for hours?",
  "<p>The regulation allows any reasonable means, but in practice contemporaneous dated logs with specific task descriptions, corroborated by emails, invoices, calendars, and receipts, are what survive. Reconstructed summaries prepared after an examination begins are consistently given little weight by the Tax Court.</p>"),
],
"related": [
 ("/material-participation-short-term-rental-7-day-rule/", "Material Participation and the STR 7-Day Rule"),
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works and What It Costs"),
 ("/form-3115-cost-segregation-lookback/", "Form 3115 Cost Segregation Lookback"),
 ("/cost-segregation-for-multifamily/", "Cost Segregation for Multifamily Properties"),
 ("/real-estate-tax-planning/", "Real Estate Tax Planning (Pillar Guide)"),
],
"takeaways": [
 "The more-than-half test, not the 750-hour test, is what defeats most high earners.",
 "The qualification tests apply per spouse and cannot be combined, which is why one spouse usually carries the position.",
 "Without the Reg. 1.469-9(g) aggregation election, multi-property owners rarely establish material participation.",
 "Investor-type activities such as reviewing statements do not count; manager-type activities do.",
 "REPS is worth organizing a year around only when there are large deductions waiting to be released.",
]},

# ---------------------------------------------------------------- 8
{
"slug": "short-term-rental-tax-loophole-2026",
"h1": "The Short-Term Rental Tax Loophole in 2026: How It Works and Who It Fits",
"title": "Short-Term Rental Tax Loophole 2026",
"description": "The STR loophole lets short-term rental losses offset W-2 and business income without real estate professional status. Here is the 2026 mechanics, the qualification steps, and where it goes wrong.",
"subtitle": "It is not a loophole so much as a specific regulatory exception, and it is the most accessible way for a high W-2 earner to convert real estate depreciation into current-year tax savings.",
"keywords": ["short term rental tax loophole 2026", "STR loophole", "offset W2 income", "Airbnb tax strategy"],
"definition": "The short-term rental tax loophole is the combination of two rules: the exception in Treasury Regulation 1.469-1T(e)(3)(ii)(A), under which a property with an average period of customer use of seven days or less is not a rental activity for passive loss purposes, and 100% bonus depreciation on components identified by a cost segregation study. Together they allow a taxpayer who materially participates to deduct a large first-year loss against W-2 wages, business income, and portfolio income, without qualifying as a real estate professional.",
"sections": [
 ("Why It Exists and Why It Is Not Aggressive", [
  "The label 'loophole' overstates it. Congress made rental activities per se passive in 1986 because they were being used as tax shelters. The regulations then carved out activities that look more like operating businesses than passive investments, and a property rented in three-day increments with continuous turnover, cleaning, guest service, and pricing management is closer to a hotel than to a triple-net lease.",
  "The exception has been in the regulations since 1988. It is not a gap, it is a deliberate line, and the IRS applies it as written. What has changed is that 100% bonus depreciation makes the deduction on the other side of that line very large.",
  "That said, the IRS knows this strategy well and examines it. The positions that fail almost never fail on the law. They fail on the facts: average stay, hours, and documentation.",
 ]),
 ("The Four Conditions", [
  "<strong>1. Average period of customer use of seven days or less.</strong> Total rental days divided by number of bookings, computed annually per property. One long booking can pull the average over the line for the entire year.",
  "<strong>2. Material participation.</strong> One of the seven tests in Reg. 1.469-5T. For most owners this is Test 3: more than 100 hours with no other individual participating more, or Test 1 at more than 500 hours outright.",
  "<strong>3. A loss to deduct.</strong> Ordinary operations rarely produce one. The loss comes from a cost segregation study reclassifying 25% to 35% of basis into 5-, 7-, and 15-year property, all of it bonus-eligible at 100%.",
  "<strong>4. Basis, at-risk, and excess business loss capacity.</strong> The loss must clear Section 704(d) or stock and debt basis, the at-risk rules of Section 465, and the excess business loss limitation of Section 461(l), which the OBBBA made permanent.",
 ]),
 ("A Full Worked Example", [
  "A married couple with $650,000 of combined W-2 income buys a $1,400,000 mountain cabin in November 2026 and operates it on Airbnb with a three-night minimum.",
  "The appraisal supports a $280,000 land allocation, leaving $1,120,000 of depreciable basis. Because the average stay is under seven days, the property is nonresidential 39-year property.",
  "A cost segregation study reclassifies $358,000, roughly 32%, into 5-, 7-, and 15-year categories: appliances, furnishings, flooring, cabinetry, window treatments, decorative lighting, the deck and hot tub surround, landscaping, the driveway, and site lighting. All of it is bonus-eligible.",
  "First-year depreciation is $358,000 in bonus plus about $8,100 of straight line on the remaining $762,000 under the mid-month convention, roughly $366,100 total.",
  "The property generated $22,000 of revenue in its partial first year against $19,000 of operating expenses, so the net loss is approximately $363,100.",
  "One spouse documents 118 hours of guest communication, listing setup, furnishing and design decisions, supply runs, and contractor supervision, with no individual participating more, satisfying Test 3.",
  "The $363,100 loss is non-passive and offsets W-2 income. At a 35% marginal federal rate the first-year federal saving is approximately $127,000, before state effects and before applying the Section 461(l) limitation, which for a married couple sits well above this amount.",
 ]),
 ("The Recapture Question Nobody Asks Early Enough", [
  "This is a timing strategy unless you plan the exit. Accelerated depreciation on 5- and 7-year property is recaptured as ordinary income under Section 1245 on sale. Land improvements and building depreciation are subject to unrecaptured Section 1250 gain at up to 25%.",
  "If you deduct $358,000 at a 35% rate and later recapture it at 37%, you have borrowed money from the IRS at a negative spread. The strategy only produces a permanent benefit through one of three exits: a 1031 exchange deferring the gain into a replacement property, holding until death for the Section 1014 basis step-up, or a later sale in a materially lower-rate year.",
  "Note that a 1031 exchange of a short-term rental works, but converting the property to personal use before sale creates problems, and the exchange must be planned before closing rather than after.",
  "We model the full hold period before recommending the study. A client who intends to sell in three years often should not do this.",
 ]),
 ("Where It Goes Wrong", [
  "<strong>The property manager problem.</strong> A full-service manager almost always logs more hours than the owner, which defeats Test 3. Co-hosting arrangements need to be structured so the owner retains the functions that generate hours.",
  "<strong>Average stay drift.</strong> Accepting a 30-day booking in the off season to fill the calendar can push the annual average above seven days and eliminate the treatment for that entire year.",
  "<strong>Buying too late in the year.</strong> A December purchase leaves almost no time to accumulate 100 hours while contractors and cleaners are accumulating theirs.",
  "<strong>Personal use.</strong> Significant personal use triggers the vacation home rules of Section 280A, which can limit deductions to rental income and disable the loss entirely. The threshold is more than 14 days or 10% of rental days, whichever is greater.",
  "<strong>No documentation.</strong> The law is not the vulnerability. The log is.",
 ]),
 ("Who This Actually Fits", [
  "It fits high W-2 earners with $300,000 or more of income, enough liquidity for a meaningful down payment, willingness to operate the property hands-on for at least the first year, and a hold horizon long enough to make the exit planning work.",
  "It does not fit someone who wants a passive investment, someone who intends to hand the property to a full-service manager on day one, or someone buying primarily for appreciation with a short hold.",
  "It also does not fit anyone unwilling to keep records. The strategy is legally sound and factually demanding, and those are not the same thing.",
 ]),
],
"faqs": [
 ("Is the short-term rental tax loophole legal?",
  "<p>Yes. It relies on an exception that has been in Treasury Regulation 1.469-1T(e)(3)(ii)(A) since 1988, combined with bonus depreciation under Section 168(k). It is a deliberate regulatory line rather than a gap. Positions that fail almost always fail on facts such as average stay, hours, and documentation, not on the underlying law.</p>"),
 ("Do I need real estate professional status to use it?",
  "<p>No, and that is the point. Because a property with an average stay of seven days or less is not a rental activity, the per se passive rule does not apply and only material participation is required. REPS is a separate and much harder qualification.</p>"),
 ("How much can I deduct in the first year?",
  "<p>It depends on basis and the study results, but a cost segregation study on a short-term rental typically reclassifies 25% to 35% of depreciable basis, all bonus-eligible at 100%. On a $1.4 million property with $1.12 million of depreciable basis, a first-year deduction in the $360,000 range is a realistic outcome.</p>"),
 ("What happens if I sell the property later?",
  "<p>Accelerated depreciation on personal property is recaptured as ordinary income under Section 1245, and building depreciation is subject to unrecaptured Section 1250 gain at up to 25%. Without a 1031 exchange, a step-up at death, or a sale in a lower-rate year, the strategy is a deferral rather than a permanent saving.</p>"),
 ("Can I stay at the property myself?",
  "<p>Only within limits. Personal use exceeding the greater of 14 days or 10% of rental days triggers the vacation home rules of Section 280A, which can cap deductions at rental income and eliminate the loss. Days spent substantially full time on repairs and maintenance generally do not count as personal use.</p>"),
],
"related": [
 ("/material-participation-short-term-rental-7-day-rule/", "Material Participation and the STR 7-Day Rule"),
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works and What It Costs"),
 ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026 Under the OBBBA"),
 ("/reps-real-estate-professional-status/", "Real Estate Professional Status: How to Qualify"),
 ("/short-term-rental-tax-strategy/", "Short-Term Rental Tax Strategy Services"),
],
"takeaways": [
 "The strategy is a regulatory exception, not a gap, and it turns on facts rather than legal interpretation.",
 "Four conditions must all hold: seven-day average, material participation, an actual loss, and basis capacity.",
 "The loss comes from cost segregation plus 100% bonus depreciation, not from operations.",
 "Without a 1031 exchange or a step-up at death, recapture converts the benefit into a deferral.",
 "A full-service property manager and a late-December closing are the two most common ways the position fails.",
]},

# ---------------------------------------------------------------- 9
{
"slug": "cost-segregation-for-self-storage",
"h1": "Cost Segregation for Self-Storage Facilities",
"title": "Cost Segregation for Self-Storage 2026",
"description": "Self-storage facilities reclassify unusually well, often 25% to 40% of basis, because so much of the asset is site work and non-structural partitioning. Here is what qualifies and what returns look like.",
"subtitle": "Few asset classes convert as favorably as self-storage. The economics come from paving, fencing, gates, security systems, and partition walls that are not part of the building structure.",
"keywords": ["cost segregation self storage", "self storage depreciation", "storage facility tax"],
"definition": "Cost segregation for self-storage is an engineering study that reallocates a storage facility's purchase or construction cost from the default 39-year nonresidential recovery period into 5-year, 7-year, and 15-year MACRS classes. Self-storage typically reclassifies 25% to 40% of depreciable basis, one of the highest ratios of any commercial asset class, because a large share of the investment is in land improvements and non-structural components rather than in the building shell.",
"sections": [
 ("Why Self-Storage Reclassifies Better Than Almost Anything", [
  "A self-storage facility is mostly site work and light construction. On a typical drive-up facility, the building shell is a pre-engineered metal structure that is inexpensive relative to the land development around it.",
  "The site carries enormous 15-year value: asphalt or concrete drive aisles, which on a storage property can exceed the building footprint, perimeter fencing, security gates and access control, exterior lighting, drainage and retention, landscaping, and signage.",
  "Inside, the partition walls between units are typically demountable metal panel systems that are not structural and qualify as personal property rather than building components. On a facility with hundreds of units, that partitioning is a substantial dollar amount.",
  "Add climate control equipment serving specific unit groups, individual unit door assemblies, security cameras and alarm systems, kiosks and office fixtures, and the short-life total climbs quickly.",
 ]),
 ("Component Breakdown", [
  "<strong>5-year property:</strong> security and surveillance systems, access control and gate operators, kiosks and point-of-sale equipment, office furniture and fixtures, decorative and task lighting, moving and rental equipment, and specialty electrical serving specific equipment.",
  "<strong>7-year property:</strong> demountable partition systems where facts support it, office furnishings, and certain specialty equipment.",
  "<strong>15-year land improvements:</strong> paving, drive aisles and striping, curbing and sidewalks, perimeter fencing and gates, exterior site lighting, storm drainage and retention basins, landscaping and irrigation, and site signage. This is usually the largest reclassified bucket in a storage study.",
  "<strong>39-year property:</strong> the building shell, roof, foundation, exterior walls, and base building mechanical, electrical, and plumbing systems.",
  "The partition wall analysis is where studies differ most. Whether a partition is personal property turns on how it is attached, whether it is designed to be moved, and whether removing it damages the structure. An engineer who has done storage facilities knows how to document this; a generic desktop study usually does not attempt it.",
 ]),
 ("Illustrative Returns", [
  "<div class=\"ae-table-scroll\" style=\"overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%\"><table><thead><tr><th>Facility</th><th>Purchase price</th><th>Depreciable basis</th><th>Reclassified</th><th>Year 1 deduction</th></tr></thead><tbody>"
  "<tr><td>Single-story drive-up, 320 units</td><td>$2,800,000</td><td>$2,100,000</td><td>34% / $714,000</td><td>~$749,000</td></tr>"
  "<tr><td>Mixed climate-controlled, 550 units</td><td>$6,500,000</td><td>$5,200,000</td><td>31% / $1,612,000</td><td>~$1,704,000</td></tr>"
  "<tr><td>Multi-story climate-controlled, 900 units</td><td>$14,000,000</td><td>$11,200,000</td><td>27% / $3,024,000</td><td>~$3,234,000</td></tr>"
  "<tr><td>Three-facility portfolio</td><td>$21,000,000</td><td>$16,300,000</td><td>32% / $5,216,000</td><td>~$5,500,000</td></tr>"
  "</tbody></table></div>",
  "Multi-story climate-controlled facilities reclassify at a lower percentage than drive-up facilities because more of the cost sits in the structure and less in site work, but the absolute dollars are larger.",
  "Land allocation on storage properties is often higher than on other commercial assets because facilities sit on large parcels, which makes a supportable appraisal-based allocation especially important.",
 ]),
 ("Operating Considerations That Affect the Study", [
  "Self-storage is generally an active trade or business rather than a passive rental, particularly where the operator provides services such as tenant insurance, retail sales, truck rentals, and on-site management. That classification matters because it affects whether losses are passive.",
  "Where the owner materially participates in the storage business, losses are non-passive without needing the rental exceptions that short-term rentals rely on. Where the facility is leased to a third-party operator under a triple-net structure, the owner's position looks much more passive.",
  "Facilities frequently expand in phases. Each phase is a separate placed-in-service event with its own study opportunity, and phased construction is one of the better arguments for engaging an engineering firm on an ongoing basis rather than once.",
  "Many storage owners hold through partnerships or REIT-adjacent structures. In a partnership, the deduction flows on K-1 subject to each partner's basis, at-risk, and passive limits.",
 ]),
 ("Timing and the Lookback Option", [
  "The best time is the year of acquisition or completion of construction. The second best is immediately following an expansion or major upgrade, such as adding climate control or replacing the access control system, which also creates partial disposition opportunities for the retired components.",
  "For facilities held for several years without a study, a Form 3115 change in accounting method recovers the entire cumulative difference as a Section 481(a) adjustment deducted in the current year, without amending prior returns. Storage owners who bought between 2018 and 2022 tend to see very large catch-ups because the recomputation applies the 100% bonus rate in effect then.",
  "Do not order a study in the year you intend to sell. The method change generally is not available in the disposition year, and recapture would consume the benefit.",
 ]),
 ("What a Study Costs and How to Judge the Return", [
  "Engineering-based studies on self-storage generally run $6,000 to $15,000 depending on facility size, unit count, and whether construction documents are available. Portfolio pricing is common, since a firm that has already modeled one facility for an owner can work faster on the next.",
  "The right way to evaluate that cost is against the present value of the accelerated deduction, not against its face amount. A $10,000 study that produces a $714,000 first-year deduction at a 35% marginal rate delivers roughly $250,000 of current-year tax reduction, but the true economic benefit is the time value of accelerating deductions you would eventually have received anyway, plus the option value of deploying that cash now.",
  "Two things move the return materially. First, whether you can actually use the loss this year, which depends on material participation and the excess business loss limitation. Second, your expected hold period, since a short hold means recapture arrives before the deferral has earned much.",
  "Be skeptical of low-cost desktop studies that produce a percentage allocation without a site visit or construction document review. The IRS Cost Segregation Audit Techniques Guide describes the detailed engineering approach as the most reliable method, and a study without engineering support is the first thing challenged on examination. On storage properties specifically, the partition wall and site improvement allocations that drive most of the value are exactly the allocations a desktop study cannot defend.",
 ]),
 ("Recapture and Exit", [
  "5- and 7-year property is recaptured as ordinary income under Section 1245 on sale. The 15-year land improvements and the building generate unrecaptured Section 1250 gain taxed at up to 25%.",
  "Because land improvements are such a large share of a storage reclassification, and because they fall under Section 1250 rather than 1245, the blended recapture rate on a storage exit is often more favorable than on an asset class weighted toward 5-year personal property.",
  "Storage assets trade actively, and 1031 exchanges into larger facilities are common. Chaining exchanges and holding until death remains the cleanest way to convert the acceleration into a permanent benefit.",
 ]),
],
"faqs": [
 ("How much does a self-storage cost segregation study typically reclassify?",
  "<p>Commonly 25% to 40% of depreciable basis, among the highest of any commercial asset class. Single-story drive-up facilities sit at the high end because so much of the investment is paving, fencing, gates, and site lighting rather than building structure.</p>"),
 ("Are storage unit partition walls personal property?",
  "<p>Often yes, where they are demountable metal panel systems that are not structural and can be relocated without damaging the building. The determination turns on the method of attachment, whether the system is designed to be moved, and the damage caused by removal, so it requires engineering documentation rather than assumption.</p>"),
 ("Is self-storage income passive?",
  "<p>Not necessarily. Where the owner provides substantial services and materially participates, self-storage is generally an active trade or business rather than a rental activity, so losses are non-passive without relying on the rental exceptions. A facility leased to a third-party operator under a triple-net structure looks far more passive.</p>"),
 ("Can I do a study on a facility I bought five years ago?",
  "<p>Yes. A Form 3115 change in accounting method captures every missed deduction from the placed-in-service year in a single Section 481(a) adjustment deducted in the current year, with no amended returns and no three-year limitation.</p>"),
 ("What happens on sale?",
  "<p>5- and 7-year property is recaptured as ordinary income under Section 1245, while land improvements and the building produce unrecaptured Section 1250 gain at up to 25%. Because storage reclassifications are weighted toward 15-year land improvements, the blended recapture is often gentler than in other asset classes.</p>"),
],
"related": [
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works and What It Costs"),
 ("/cost-segregation-for-multifamily/", "Cost Segregation for Multifamily Properties"),
 ("/cost-segregation-for-hotel-motel/", "Cost Segregation for Hotels and Motels"),
 ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026 Under the OBBBA"),
 ("/form-3115-cost-segregation-lookback/", "Form 3115 Cost Segregation Lookback"),
],
"takeaways": [
 "Self-storage reclassifies 25% to 40% of basis, among the best of any commercial asset class.",
 "Site work, paving, fencing, gates, and lighting usually form the largest reclassified bucket.",
 "Demountable partition systems can qualify as personal property, but only with engineering documentation.",
 "Owner-operated storage is typically an active business, so losses avoid the rental passive trap entirely.",
 "The 15-year weighting means a gentler blended recapture rate on exit than personal-property-heavy assets.",
]},

# ---------------------------------------------------------------- 10
{
"slug": "cost-segregation-for-hotel-motel",
"h1": "Cost Segregation for Hotels and Motels",
"title": "Cost Segregation for Hotels and Motels",
"description": "Hotels carry more short-life property than any other commercial asset class, often 30% to 45% of basis. Here is how FF&E, guest room finishes, and site work reclassify, plus renovation and PIP planning.",
"subtitle": "Between guest room furnishings, food and beverage equipment, decorative finishes, and extensive site work, hospitality assets produce the largest reclassification percentages we see.",
"keywords": ["cost segregation hotel", "motel depreciation", "hospitality cost segregation", "hotel FF&E"],
"definition": "Cost segregation for hotels and motels is an engineering analysis that separates a hospitality property's cost into components and reassigns them from the 39-year nonresidential recovery period to 5-year, 7-year, and 15-year MACRS classes. Hotels typically reclassify 30% to 45% of depreciable basis, the highest range of any major commercial asset class, because furniture, fixtures and equipment, guest room finishes, food and beverage operations, and extensive site improvements make up such a large share of the total investment.",
"sections": [
 ("Why Hospitality Produces the Largest Reclassifications", [
  "A hotel is an operating business housed in a building, and the operating assets are everywhere. Every guest room contains beds, case goods, seating, lamps, televisions, artwork, window treatments, carpeting or luxury vinyl, and bathroom fixtures and accessories. Multiply by room count and the personal property total is substantial before you leave the guest floors.",
  "Public areas add more: lobby furnishings, decorative lighting, millwork, signage, business center and fitness equipment, and pool furniture.",
  "Food and beverage operations contribute heavily, since commercial kitchen equipment, walk-in coolers, bar equipment, dining furniture, and the specialty plumbing and electrical serving them are 5- and 7-year property.",
  "Site work follows the pattern of other commercial assets: parking, drive courts and porte cocheres, sidewalks, landscaping and irrigation, site lighting, pools and pool decking, and signage.",
  "Together these routinely push reclassification into the 30% to 45% range, and full-service resorts can exceed that.",
 ]),
 ("Component Detail", [
  "<strong>5-year property:</strong> guest room furniture and case goods, mattresses and bedding systems, televisions and audiovisual, decorative and accent lighting, window treatments, carpeting and resilient flooring, artwork and decor, kitchen and bar equipment, laundry equipment, fitness equipment, point-of-sale and property management systems, telephone and data cabling serving equipment, and specialty electrical and plumbing serving specific equipment.",
  "<strong>7-year property:</strong> office furniture, certain specialty fixtures, and equipment without an assigned class life.",
  "<strong>15-year land improvements:</strong> paving and parking, sidewalks and curbing, porte cochere paving, landscaping and irrigation, site lighting, fencing, retaining walls, pools and decking, drainage, and exterior signage.",
  "<strong>39-year property:</strong> structural frame, foundation, roof, exterior envelope, elevators, and base building mechanical, electrical, plumbing, and life safety systems.",
  "The most valuable engineering judgment in a hotel study concerns building systems that serve specific operating functions. Kitchen exhaust and make-up air, walk-in refrigeration, and dedicated electrical to laundry or kitchen equipment can often be separated from base building systems, and those allocations are worth substantial dollars.",
 ]),
 ("Illustrative Returns", [
  "<div class=\"ae-table-scroll\" style=\"overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%\"><table><thead><tr><th>Property type</th><th>Purchase price</th><th>Depreciable basis</th><th>Reclassified</th><th>Year 1 deduction</th></tr></thead><tbody>"
  "<tr><td>Limited-service, 62 rooms</td><td>$5,200,000</td><td>$4,200,000</td><td>33% / $1,386,000</td><td>~$1,458,000</td></tr>"
  "<tr><td>Select-service, 110 rooms</td><td>$12,500,000</td><td>$10,300,000</td><td>36% / $3,708,000</td><td>~$3,877,000</td></tr>"
  "<tr><td>Boutique with F&amp;B, 48 rooms</td><td>$9,800,000</td><td>$7,900,000</td><td>41% / $3,239,000</td><td>~$3,359,000</td></tr>"
  "<tr><td>Full-service resort, 240 rooms</td><td>$46,000,000</td><td>$37,000,000</td><td>38% / $14,060,000</td><td>~$14,650,000</td></tr>"
  "</tbody></table></div>",
  "Boutique properties with significant food and beverage operations reclassify at the highest percentages because the personal property density per room is greatest. Limited-service properties with no restaurant sit at the lower end of the hospitality range but still above most other asset classes.",
 ]),
 ("Renovations, PIPs, and Partial Dispositions", [
  "Hospitality is unusual in that major renovation is contractual. Franchise agreements impose property improvement plans on a cycle, typically every six to eight years, requiring guest room refreshes, lobby renovations, and system replacements.",
  "Each PIP is a cost segregation opportunity on the new spend, and a partial disposition opportunity on what comes out. When you replace 110 rooms of case goods, carpet, and soft goods, the removed components frequently still carry undepreciated basis on the fixed asset schedule.",
  "A partial disposition election under the tangible property regulations writes off that remaining basis, and it also stops you from depreciating assets that no longer exist. On a full guest room renovation, the disposition deduction alone can be a seven-figure item on a larger property.",
  "The repair regulations matter here too. Some PIP spend qualifies as a deductible repair rather than a capitalized improvement under the betterment, adaptation, and restoration framework of Reg. 1.263(a)-3. Sorting the PIP budget into repairs, short-life property, and structure before the work begins is worth far more than analyzing it afterward.",
 ]),
 ("Passive Loss Treatment for Hotel Owners", [
  "Hotels are not rental activities. The regulation excludes activities where the average period of customer use is seven days or less, and it also excludes activities where average use is thirty days or less and significant personal services are provided. A hotel clears both.",
  "That means hotel losses are governed by ordinary trade or business rules, and the question is simply whether the owner materially participates under Reg. 1.469-5T. An owner-operator generally does. A passive investor in a hotel partnership generally does not.",
  "For owner-operators, this makes hospitality cost segregation unusually clean: there is no need to engineer around the rental passive rules, and large first-year deductions offset business income directly, subject to basis, at-risk, and the excess business loss limitation of Section 461(l).",
  "Where the real property is held in a separate entity and leased to an operating company, the self-rental rules of Reg. 1.469-2(f)(6) become relevant and the structure needs review.",
 ]),
 ("Franchise Agreements, Management Contracts, and Who Owns What", [
  "Hospitality ownership is layered in a way that affects who gets the deduction. A single property commonly involves a property owner, an operating lessee, a management company, and a franchisor, and the depreciation follows tax ownership of each asset rather than the brand on the sign.",
  "Where the property is held in one entity and leased to an operating entity, the owner depreciates the building and the components that transferred with it, while the operator depreciates the FF&E it purchases directly. A study should be scoped to the correct taxpayer, and the purchase price allocation at acquisition should be documented so both entities are working from consistent numbers.",
  "The self-rental rules of Reg. 1.469-2(f)(6) apply to owner-operator structures, recharacterizing net rental income from a self-rental as non-passive while leaving net rental losses passive. Where the same taxpayers control both entities and they form an appropriate economic unit, a grouping election under Reg. 1.469-4 generally resolves the asymmetry.",
  "Franchise fees themselves are not part of the cost segregation analysis. Initial franchise fees are typically amortized over 15 years as a Section 197 intangible, and ongoing royalties are deductible as paid. They are worth separating from the depreciable basis at acquisition so they are not inadvertently swept into the building.",
 ]),
 ("Exit Planning", [
  "Hotels carry a high proportion of 5-year personal property, which means Section 1245 ordinary income recapture is a larger share of the eventual gain than in most asset classes.",
  "This makes exit planning more important, not less. The common paths are a 1031 exchange into a replacement property, an installment sale to spread gain, though Section 1245 recapture is accelerated into the year of sale regardless, or holding until death for the basis step-up.",
  "There is also a practical point specific to hospitality: because FF&E is replaced on a cycle, much of the original 5-year property is fully depreciated and disposed of long before the real estate is sold, so the recapture exposure at exit is often smaller than the original study suggests.",
 ]),
],
"faqs": [
 ("How much do hotels reclassify in a cost segregation study?",
  "<p>Typically 30% to 45% of depreciable basis, the highest range of any major commercial asset class. Boutique and full-service properties with food and beverage operations sit at the top of that range because personal property density per room is highest.</p>"),
 ("Is hotel income passive for tax purposes?",
  "<p>No. A hotel is not a rental activity under the passive loss regulations, because the average period of customer use is seven days or less and significant personal services are provided. Losses turn on ordinary material participation rules, and an owner-operator generally materially participates.</p>"),
 ("Should I do a study when completing a property improvement plan?",
  "<p>Yes, and you should also evaluate partial dispositions at the same time. A PIP adds substantial short-life property while removing components that still carry undepreciated basis. Claiming the disposition deduction and sorting repair from capital spend before the work begins is worth more than analyzing it after.</p>"),
 ("Does a motel reclassify as well as a full-service hotel?",
  "<p>Somewhat less, but still very well. A limited-service motel lacks food and beverage equipment and elaborate public spaces, so it typically lands around 30% to 33% rather than 40%, which is still above most office, industrial, and retail properties.</p>"),
 ("What is the recapture exposure on a hotel sale?",
  "<p>Higher than most asset classes, because a large share of the reclassification is 5-year personal property recaptured as ordinary income under Section 1245. In practice, much of that FF&E is replaced and disposed of during the hold period, so the exposure remaining at sale is often smaller than the original study implies.</p>"),
],
"related": [
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works and What It Costs"),
 ("/cost-segregation-for-restaurant/", "Cost Segregation for Restaurants"),
 ("/cost-segregation-for-self-storage/", "Cost Segregation for Self-Storage Facilities"),
 ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026 Under the OBBBA"),
 ("/form-3115-cost-segregation-lookback/", "Form 3115 Cost Segregation Lookback"),
],
"takeaways": [
 "Hotels reclassify 30% to 45% of basis, the highest of any major commercial asset class.",
 "Guest room FF&E, food and beverage equipment, and site work drive the result.",
 "Hotels are not rental activities, so owner-operators avoid the passive loss problem entirely.",
 "Every property improvement plan is both a new study opportunity and a partial disposition opportunity.",
 "Section 1245 recapture exposure is higher here, but FF&E replacement cycles reduce it before sale.",
]},

]
