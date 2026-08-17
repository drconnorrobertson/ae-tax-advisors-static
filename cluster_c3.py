#!/usr/bin/env python3
"""Cluster 3: Cost segregation.

The pillar already exists at /cost-segregation-study/ and already ranks, so it
is adopted rather than rewritten. This module adds the supporting posts the
cluster was missing and wires the hub into the existing pillar.
"""

from __future__ import annotations

from cluster_common import Cluster, Spoke

P = "cost-segregation-study"

OWNER_OCCUPIED = Spoke(
    slug="cost-segregation-owner-occupied-commercial",
    label="Cost seg for owner-occupied commercial buildings",
    title="Cost Segregation for Owner-Occupied Commercial Buildings",
    description=(
        "Why an owner-occupied building is the cleanest cost segregation case: the "
        "passive activity problem largely disappears and the deduction is usable."
    ),
    h1="Cost Segregation for Owner-Occupied Commercial Buildings",
    subtitle=(
        "When your business operates from a building you own, the deduction offsets "
        "the income you actually have."
    ),
    lead=(
        "Cost segregation on an owner-occupied commercial building is the strongest version "
        "of the strategy for a business owner, because it resolves the constraint that "
        "limits most studies. Rental losses are passive by default and generally cannot "
        "offset business income. When the building is used in the owner's own trade or "
        "business, the deduction lands against the income the owner actually has."
    ),
    keywords=[
        "cost segregation owner occupied building",
        "cost segregation commercial building business owner",
        "cost segregation self rental",
    ],
    body=[
        (
            "The Usability Problem Everywhere Else",
            "<p>A cost segregation study on a conventional rental property produces a large "
            "first-year deduction that many owners then cannot use. Rental activity is "
            "passive under Section 469, and passive losses generally offset only passive "
            "income. The loss is not lost, but it is suspended and carried forward until "
            "there is passive income to absorb it or the property is sold.</p>"
            "<p>For a business owner with $800,000 of operating profit and one rental "
            "property, a $400,000 suspended loss changes this year's tax bill by nothing. "
            "That is the outcome that makes owners feel a study was mis-sold, when in fact "
            "the study was fine and the usability question was never asked.</p>"
        ),
        (
            "Why Owner-Occupied Is Different",
            "<p>When the building is used in the owner's own trade or business, the analysis "
            "changes in the owner's favor. Property used in the business the owner materially "
            "participates in is not a passive rental activity, so the depreciation flows "
            "against active business income directly.</p>"
            "<p>Where the building is held in a separate entity that leases to the operating "
            "company, the self-rental rules under the Section 469 regulations apply. Their "
            "effect on income is often described as unfavorable, because net rental income "
            "from a self-rental is recharacterized as non-passive and cannot be sheltered by "
            "other passive losses. But the grouping election available under the regulations "
            "allows the rental and the operating business to be treated as a single activity "
            "where they constitute an appropriate economic unit, which is what lets the "
            "depreciation offset the operating income.</p>"
            "<p>This is a structural decision that should be made deliberately and documented "
            "when the entities are set up, not reconstructed after a study has been "
            "commissioned.</p>"
        ),
        (
            "What a Study Typically Finds",
            "<p>Commercial buildings generally reclassify 20 to 35 percent of depreciable "
            "basis out of the 39-year category, with the range driven by use. A medical or "
            "dental office with extensive specialized plumbing, electrical, and cabinetry "
            "sits at the top of the range. A plain warehouse shell sits at the bottom.</p>"
            "<p>Typical reclassifications include:</p>"
            "<ul>"
            "<li><strong>5-year property.</strong> Carpeting, decorative lighting, "
            "specialized electrical serving equipment, cabinetry and millwork, and process "
            "plumbing.</li>"
            "<li><strong>7-year property.</strong> Certain fixtures and equipment integral to "
            "the business function rather than the building.</li>"
            "<li><strong>15-year land improvements.</strong> Parking areas, site lighting, "
            "landscaping, fencing, and exterior signage.</li>"
            "</ul>"
            "<p>With 100 percent bonus depreciation permanent under the OBBBA for property "
            "acquired after January 19, 2025, every reclassified dollar in these categories "
            "becomes immediately deductible rather than spread across its recovery period.</p>"
        ),
        (
            "The Arithmetic on a Typical Building",
            "<p>Take a $1,800,000 purchase where $300,000 is allocable to land, leaving "
            "$1,500,000 of depreciable basis. Without a study, the annual deduction is "
            "roughly $38,000 of straight-line depreciation over 39 years.</p>"
            "<p>With a study reclassifying 25 percent of basis, $375,000 moves into "
            "short-lived categories and becomes immediately deductible. For an owner in the "
            "37 percent bracket whose business income the deduction can offset, that is "
            "roughly $139,000 of federal tax deferred into the first year, against a study "
            "cost driven by square footage.</p>"
            "<p>The deduction is acceleration rather than creation: basis claimed now is not "
            "available later, and depreciation recapture applies on sale. The value is in the "
            "time value of the money and in the ability to deploy it, which is why the "
            "strategy pairs naturally with an owner who has a use for capital now.</p>"
        ),
        (
            "Buildings Already Owned for Years",
            "<p>Owner-occupied buildings are frequently held for a long time before anyone "
            "raises a study, and owners assume the opportunity has passed. It has not. A "
            "Form 3115 accounting method change allows the cumulative difference between "
            "depreciation claimed and depreciation that should have been claimed to be taken "
            "in the current year, with no amended returns required.</p>"
            "<p>A building bought eight years ago and never studied can produce a very large "
            "catch-up deduction in the current year, because eight years of missed "
            "acceleration arrives at once.</p>"
        ),
        (
            "When It Still Does Not Make Sense",
            "<p>Several situations argue against a study even on an owner-occupied building: "
            "a sale planned within two to three years, where recapture arrives before the "
            "deferral has earned much; an owner with little current taxable income to "
            "shelter; a building with very low depreciable basis relative to study cost; and "
            "a property that is mostly land, where the depreciable base is thin to begin "
            "with.</p>"
        ),
    ],
    takeaways=[
        "Owner-occupied buildings avoid the passive loss problem that suspends most study deductions.",
        "Where a separate entity leases to the operating company, the grouping election is what makes it work.",
        "Commercial buildings typically reclassify 20 to 35 percent of basis, driven by use type.",
        "A building owned for years can still be caught up through Form 3115 without amending.",
        "A planned sale within two to three years usually argues against commissioning a study.",
    ],
    faqs=[
        (
            "Can I use cost segregation on the building my business operates from?",
            "<p>Yes, and it is generally the strongest case. Property used in a trade or "
            "business the owner materially participates in is not passive rental activity, so "
            "the accelerated depreciation offsets active business income rather than being "
            "suspended.</p>",
        ),
        (
            "What if I hold the building in a separate LLC that leases to my company?",
            "<p>That is a common and sound structure, but the self-rental rules apply. The "
            "grouping election under the Section 469 regulations allows the rental and the "
            "operating business to be treated as one activity where they form an appropriate "
            "economic unit, which is what allows the depreciation to offset operating income. "
            "The election should be documented deliberately.</p>",
        ),
        (
            "How much does a study cost?",
            "<p>We price cost segregation studies at $1 per square foot, subject to a $2,000 "
            "minimum. Pricing is quoted flat in writing before work begins rather than billed "
            "hourly.</p>",
        ),
        (
            "Does cost segregation create a permanent tax saving?",
            "<p>No. It accelerates deductions rather than creating them. Basis claimed now is "
            "not available in later years, and depreciation recapture applies on sale. The "
            "benefit is the time value of money, which is why it suits owners who have a "
            "productive use for capital now and no near-term sale planned.</p>",
        ),
    ],
)

ROI_BY_TYPE = Spoke(
    slug="cost-segregation-roi-by-property-type",
    label="Cost seg ROI by property type",
    title="Cost Segregation ROI by Property Type: A Comparison",
    description=(
        "Typical reclassification percentages and first-year deductions by property "
        "type, and why the same purchase price produces very different results."
    ),
    h1="Cost Segregation ROI by Property Type",
    subtitle=(
        "Two buildings at the same price can produce first-year deductions that "
        "differ by a factor of three. Use type is why."
    ),
    lead=(
        "Cost segregation return varies widely by property type because the percentage of a "
        "building's cost that sits in short-lived components depends on what the building "
        "does. A dental office dense with specialized plumbing, electrical, and cabinetry "
        "reclassifies far more than a warehouse shell of the same value, and the difference "
        "shows up directly in the first-year deduction."
    ),
    keywords=[
        "cost segregation by property type",
        "cost segregation reclassification percentage",
        "cost segregation roi comparison",
    ],
    body=[
        (
            "What Drives the Percentage",
            "<p>A study moves cost out of the 39-year or 27.5-year building category into "
            "5, 7, and 15-year categories. How much moves depends on three things: the "
            "density of specialized systems serving equipment rather than the structure, the "
            "amount of finish work such as cabinetry, decorative lighting, and floor "
            "coverings, and the extent of site improvements such as parking, lighting, and "
            "landscaping.</p>"
            "<p>A building that is mostly structure with minimal finish reclassifies little. "
            "A building dense with equipment-serving systems and finish work reclassifies a "
            "great deal.</p>"
        ),
        (
            "Typical Ranges by Property Type",
            "<p>These are the ranges we see in practice. Every building is studied on its own "
            "facts, and an actual engineering study can land outside these bands.</p>"
            "<div style=\"overflow-x:auto;\">"
            "<table>"
            "<thead><tr><th>Property type</th><th>Typical reclassified</th>"
            "<th>First-year deduction on $1.5M basis</th></tr></thead>"
            "<tbody>"
            "<tr><td>Dental / medical office</td><td>25% - 40%</td><td>$375,000 - $600,000</td></tr>"
            "<tr><td>Restaurant</td><td>25% - 40%</td><td>$375,000 - $600,000</td></tr>"
            "<tr><td>Short-term rental (furnished)</td><td>25% - 35%</td><td>$375,000 - $525,000</td></tr>"
            "<tr><td>Car wash</td><td>30% - 45%</td><td>$450,000 - $675,000</td></tr>"
            "<tr><td>Hotel / motel</td><td>22% - 35%</td><td>$330,000 - $525,000</td></tr>"
            "<tr><td>Retail strip center</td><td>20% - 30%</td><td>$300,000 - $450,000</td></tr>"
            "<tr><td>Self-storage</td><td>20% - 35%</td><td>$300,000 - $525,000</td></tr>"
            "<tr><td>Multifamily apartment</td><td>15% - 25%</td><td>$225,000 - $375,000</td></tr>"
            "<tr><td>General office building</td><td>15% - 25%</td><td>$225,000 - $375,000</td></tr>"
            "<tr><td>Warehouse / industrial shell</td><td>10% - 20%</td><td>$150,000 - $300,000</td></tr>"
            "</tbody></table></div>"
            "<p>The spread is the point. A car wash and a warehouse at identical purchase "
            "prices can differ by more than $400,000 in first-year deduction, because one is "
            "essentially equipment wrapped in a building and the other is a structure with a "
            "concrete floor.</p>"
        ),
        (
            "Why Car Washes and Restaurants Sit at the Top",
            "<p>Properties at the top of the range share a characteristic: a large share of "
            "the cost serves a process rather than the building. A car wash contains "
            "conveyors, water reclamation, specialized electrical, and dedicated plumbing, "
            "most of which is equipment by function. A restaurant carries hood systems, "
            "grease interceptors, specialized ventilation, and heavy finish work.</p>"
            "<p>Medical and dental offices behave similarly, with dedicated vacuum and air "
            "lines, lead shielding, specialized cabinetry, and electrical serving specific "
            "equipment positions.</p>"
        ),
        (
            "Why Warehouses Sit at the Bottom",
            "<p>An industrial shell is mostly structure: slab, frame, roof, and envelope, all "
            "of which remain 39-year property. What lifts a warehouse toward the upper end of "
            "its range is usually site work rather than the building, since parking, yard "
            "paving, site lighting, and fencing are 15-year land improvements and industrial "
            "sites often have a great deal of it.</p>"
        ),
        (
            "Short-Term Rentals Are a Special Case",
            "<p>Furnished short-term rentals sit higher in the range than their long-term "
            "equivalents, and for a reason worth understanding. A furnished property carries "
            "appliances, furniture, window treatments, and electronics that are personal "
            "property rather than building components, and those are 5-year property "
            "regardless of the structure they sit in.</p>"
            "<p>The result is that a short-term rental frequently reclassifies 25 to 35 "
            "percent where the same building operated as a long-term rental would reach 15 to "
            "25 percent. The furnishings alone can account for a meaningful share of the "
            "difference.</p>"
            "<p>This compounds with the passive activity treatment. A property where the "
            "average stay is seven days or less is not a rental activity under the Section "
            "469 regulations, so an owner who materially participates can use the loss "
            "against active income. A higher reclassification percentage and a usable "
            "deduction is why this combination produces the largest results we see for "
            "business owners without real estate professional status.</p>"
        ),
        (
            "Reading the Table Correctly",
            "<p>Two cautions. First, these percentages apply to depreciable basis, not "
            "purchase price. Land is not depreciable, and land can be a large share of the "
            "price in dense markets, so a $2,000,000 purchase might carry only $1,400,000 of "
            "depreciable basis.</p>"
            "<p>Second, the first-year deduction is not the tax saving. The saving is the "
            "deduction multiplied by the marginal rate, and only if the deduction is usable "
            "against income the owner actually has. For a passive rental held by an owner "
            "with no passive income, a $500,000 deduction can produce no current benefit "
            "at all.</p>"
        ),
    ],
    takeaways=[
        "Reclassification percentage is driven by use type, not by purchase price.",
        "Car washes, restaurants, and medical offices reclassify most; warehouse shells least.",
        "Percentages apply to depreciable basis, not purchase price; land is excluded.",
        "Site improvements are 15-year property and often lift otherwise plain buildings.",
        "The deduction is only worth its tax value if it is usable against income you have.",
    ],
    faqs=[
        (
            "Which property type gets the best cost segregation result?",
            "<p>Properties where much of the cost serves a process rather than the structure. "
            "Car washes, restaurants, and medical or dental offices typically reclassify 25 "
            "to 45 percent of depreciable basis, compared with 10 to 20 percent for a plain "
            "warehouse shell.</p>",
        ),
        (
            "Do apartment buildings benefit from cost segregation?",
            "<p>Yes, though typically at the lower end, around 15 to 25 percent, because "
            "residential construction has less specialized system density. Residential rental "
            "property also depreciates over 27.5 years rather than 39, so the baseline "
            "deduction without a study is already larger.</p>",
        ),
        (
            "How much of the purchase price is usually land?",
            "<p>It varies widely by market, commonly 15 to 30 percent, and considerably more "
            "in dense urban areas. Land is not depreciable and is excluded from the study "
            "basis, so the allocation matters and should be supported rather than assumed.</p>",
        ),
        (
            "Can I estimate my result before commissioning a study?",
            "<p>A preliminary estimate using property type, purchase price, land allocation, "
            "and placed-in-service date is usually enough to decide whether a full study is "
            "worthwhile. We provide that estimate before any engagement so the decision is "
            "made on numbers rather than on a range.</p>",
        ),
    ],
)

OBBBA = Spoke(
    slug="cost-segregation-bonus-depreciation-obbba-2026",
    label="Cost seg + bonus depreciation under OBBBA 2026",
    title="Cost Segregation and Bonus Depreciation Under the OBBBA in 2026",
    description=(
        "How permanent 100% bonus depreciation changes cost segregation economics, and "
        "the acquisition date rule that decides which percentage applies."
    ),
    h1="Cost Segregation + Bonus Depreciation Under OBBBA 2026",
    subtitle=(
        "The phase-down is gone. What matters now is the acquisition date, not the "
        "closing date."
    ),
    lead=(
        "The One Big Beautiful Bill Act ended the bonus depreciation phase-down and restored "
        "a permanent 100 percent first-year deduction for qualifying property acquired after "
        "January 19, 2025. For cost segregation this removes the deadline that drove studies "
        "for years, and replaces it with a single question that decides the percentage "
        "applied: when was the property acquired?"
    ),
    keywords=[
        "cost segregation bonus depreciation 2026",
        "obbba bonus depreciation cost segregation",
        "100 percent bonus depreciation 2026",
    ],
    body=[
        (
            "What Changed",
            "<p>Under the Tax Cuts and Jobs Act, bonus depreciation was scheduled to decline "
            "from 100 percent to 80 percent in 2023, 60 percent in 2024, 40 percent in 2025, "
            "20 percent in 2026, and zero thereafter. Every study was being run against a "
            "shrinking benefit and a closing window.</p>"
            "<p>The OBBBA removed that schedule. For qualifying property acquired after "
            "January 19, 2025 and placed in service thereafter, the rate is 100 percent and "
            "permanent. There is no expiration to plan around.</p>"
        ),
        (
            "Why This Changes Cost Segregation Economics",
            "<p>Cost segregation and bonus depreciation work together: the study identifies "
            "which portions of a building belong in 5, 7, and 15-year categories, and bonus "
            "depreciation determines how much of that reclassified amount is deductible "
            "immediately. At a 100 percent rate, every reclassified dollar is deductible in "
            "year one.</p>"
            "<p>Two practical effects follow. Studies on smaller properties now clear their "
            "cost more easily, because the first-year benefit is at full strength rather "
            "than a declining fraction. And the timing pressure is gone, which means a study "
            "can be scheduled when it fits the owner's tax position rather than rushed "
            "before a phase-down step.</p>"
        ),
        (
            "The Acquisition Date Rule",
            "<p>The date that governs is the acquisition date, not the placed-in-service "
            "date alone. Property acquired under a binding written contract entered into on "
            "or before January 19, 2025 generally remains under the old phase-down "
            "percentages even if it is placed in service in 2026.</p>"
            "<p>For an owner who signed a purchase contract in late 2024 and closed in 2025 "
            "or 2026, this distinction is worth a large fraction of the benefit. It is the "
            "first thing to establish on any study covering a property that changed hands "
            "near that date, and it turns on contract documents rather than on the closing "
            "statement.</p>"
        ),
        (
            "Properties Acquired Before the Cutoff",
            "<p>Older properties are not excluded from cost segregation. They are subject to "
            "the bonus percentage in effect when they were acquired, and the portion not "
            "eligible for bonus is still depreciated over its now-correct shorter recovery "
            "period rather than over 39 years.</p>"
            "<p>A study on a 2019 acquisition still produces a substantial catch-up through "
            "Form 3115, because the difference between what was claimed and what should have "
            "been claimed accumulates across every year since. The benefit is real, it is "
            "just composed differently.</p>"
        ),
        (
            "What Still Constrains the Deduction",
            "<p>Permanent 100 percent bonus does not solve usability. The passive activity "
            "rules under Section 469 are unchanged, so a large first-year deduction on a "
            "passive rental is still suspended unless the owner qualifies as a real estate "
            "professional, materially participates in a short-term rental, or the property is "
            "used in their own trade or business.</p>"
            "<p>The excess business loss limitation also continues to apply, capping how much "
            "net business loss can offset non-business income in a year, with the remainder "
            "carried forward. On very large studies this can spread the benefit across "
            "several years even where the passive question is resolved.</p>"
        ),
    ],
    takeaways=[
        "The OBBBA made 100 percent bonus depreciation permanent for property acquired after January 19, 2025.",
        "The acquisition date governs, not the closing date; a pre-cutoff binding contract keeps the old rates.",
        "Full-strength first-year benefit makes studies on smaller properties clear their cost more easily.",
        "Older properties still benefit through a Form 3115 catch-up of accumulated missed depreciation.",
        "Passive activity and excess business loss limits are unchanged and still govern usability.",
    ],
    faqs=[
        (
            "Is bonus depreciation still 100% in 2026?",
            "<p>Yes, for qualifying property acquired after January 19, 2025. The OBBBA ended "
            "the phase-down schedule and made the 100 percent rate permanent, so there is no "
            "scheduled expiration to plan around.</p>",
        ),
        (
            "What if I signed the purchase contract before January 19, 2025?",
            "<p>Property acquired under a binding written contract entered into on or before "
            "that date generally remains under the old phase-down percentages even if placed "
            "in service later. This is determined from the contract documents, and on a "
            "large study the difference is significant.</p>",
        ),
        (
            "Does permanent bonus depreciation mean there is no rush?",
            "<p>There is no statutory deadline, but there is still a timing question. The "
            "deduction is worth most in a year with high income to offset, and a Form 3115 "
            "catch-up on an older property grows with each year it is deferred only in the "
            "sense that the accumulated difference sits unclaimed. Scheduling should follow "
            "the owner's tax position.</p>",
        ),
        (
            "Can bonus depreciation create a loss I can use against other income?",
            "<p>Sometimes, subject to two limits. The passive activity rules generally "
            "prevent rental losses from offsetting business or wage income unless an "
            "exception applies, and the excess business loss limitation caps how much net "
            "business loss can offset non-business income in a single year.</p>",
        ),
    ],
)

SMALL_PROPS = Spoke(
    slug="cost-segregation-500k-2m-properties",
    label="Cost seg for $500K-$2M properties",
    title="Cost Segregation for $500K to $2M Properties: Does It Pay?",
    description=(
        "The economics of cost segregation on smaller properties, where the breakeven "
        "sits, and why the old million-dollar rule of thumb no longer holds."
    ),
    h1="Cost Segregation for $500K to $2M Properties",
    subtitle=(
        "The advice that studies only pay above several million dollars is out of "
        "date. Here is where the breakeven actually falls."
    ),
    lead=(
        "Cost segregation on properties between $500,000 and $2,000,000 is frequently "
        "dismissed on the basis that studies only pay at larger scale. That rule of thumb "
        "dates from a period of lower bonus depreciation percentages and higher study "
        "pricing. With 100 percent bonus permanent under the OBBBA and studies priced by "
        "square footage, the breakeven now sits well below $1,000,000 of depreciable basis "
        "for most property types."
    ),
    keywords=[
        "cost segregation small property",
        "cost segregation under 1 million",
        "is cost segregation worth it small building",
    ],
    body=[
        (
            "Where the Old Rule Came From",
            "<p>The guidance that studies need several million dollars of basis was "
            "reasonable when two things were true: study pricing was often a fixed engagement "
            "fee in the five figures regardless of building size, and bonus depreciation was "
            "phasing down, so only a fraction of the reclassified amount was immediately "
            "deductible.</p>"
            "<p>Both have changed. Square-footage pricing scales the cost to the building, "
            "and permanent 100 percent bonus means the full reclassified amount is deductible "
            "in year one. The arithmetic that produced the old rule no longer holds.</p>"
        ),
        (
            "The Breakeven Arithmetic",
            "<p>The test is straightforward. A study pays when the present value of the "
            "accelerated deduction exceeds its cost.</p>"
            "<p>Take a $900,000 purchase with $150,000 allocable to land, leaving $750,000 of "
            "depreciable basis. At a 22 percent reclassification, typical for a modest "
            "commercial property, $165,000 moves into short-lived categories and becomes "
            "immediately deductible under permanent bonus.</p>"
            "<p>For an owner in the 37 percent bracket who can use the deduction, that is "
            "roughly $61,000 of federal tax deferred into year one. Against a study priced at "
            "$1 per square foot, a 6,000 square foot building costs $6,000. The ratio is "
            "roughly ten to one, and it remains favorable well below this size.</p>"
        ),
        (
            "Where the $2,000 Minimum Binds",
            "<p>Because we price at $1 per square foot subject to a $2,000 minimum, small "
            "buildings pay the minimum rather than the per-foot rate. A 1,200 square foot "
            "property costs $2,000 rather than $1,200.</p>"
            "<p>Even then the arithmetic usually holds. A small property with $400,000 of "
            "depreciable basis reclassifying 20 percent produces $80,000 of immediate "
            "deduction, worth roughly $30,000 to an owner in the top bracket. Against a "
            "$2,000 minimum that is still strongly positive.</p>"
        ),
        (
            "What Actually Decides It at This Size",
            "<p>At $500,000 to $2,000,000, study cost is rarely the deciding factor. Three "
            "other questions matter more:</p>"
            "<p><strong>Can the deduction be used?</strong> A suspended passive loss produces "
            "no current benefit regardless of how cheap the study was. This is the single "
            "most important question and it should be answered first.</p>"
            "<p><strong>Is a sale planned?</strong> Depreciation recapture on sale reverses "
            "much of the benefit. A hold of five years or more generally supports a study; a "
            "sale within two to three years often does not.</p>"
            "<p><strong>What is the property type?</strong> A 10 percent reclassification on "
            "a warehouse produces a very different result from a 35 percent reclassification "
            "on a dental office at the same price.</p>"
        ),
        (
            "The Catch-Up on an Older Small Property",
            "<p>Smaller properties are disproportionately likely to have been held for years "
            "without a study, precisely because owners were told they were too small to "
            "bother with. That history is now an advantage.</p>"
            "<p>A Form 3115 accounting method change allows the cumulative difference between "
            "depreciation claimed and depreciation that should have been claimed to be taken "
            "in the current year, without amending any prior return. A $900,000 property "
            "bought six years ago and never studied delivers six years of missed acceleration "
            "in a single year, which is frequently a larger first-year number than a study on "
            "a property acquired this year would produce.</p>"
            "<p>The filing is made with the current year return, so the practical deadline is "
            "the return itself rather than year-end. This is one of the few valuable moves "
            "still fully available after December 31.</p>"
        ),
        (
            "The Case That Is Almost Always Worth It",
            "<p>One profile stands out at this size: a business owner who owns the building "
            "their company operates from. The passive activity problem largely falls away "
            "because the property is used in the trade or business, the deduction offsets "
            "operating income directly, and the hold period is usually long because the "
            "business is not moving.</p>"
            "<p>For that owner, a $700,000 building is very often worth studying, and the "
            "question is not whether but when, timed against the year with the most income to "
            "offset.</p>"
        ),
    ],
    takeaways=[
        "The several-million-dollar rule of thumb predates square-footage pricing and permanent bonus.",
        "Breakeven now sits well below $1,000,000 of depreciable basis for most property types.",
        "At this size, usability and hold period decide the outcome far more than study cost.",
        "A sale planned within two to three years usually argues against a study.",
        "An owner-occupied building at this size is almost always worth studying.",
    ],
    faqs=[
        (
            "Is cost segregation worth it on a $750,000 property?",
            "<p>Usually yes, if the deduction is usable and the hold period is reasonable. At "
            "roughly $600,000 of depreciable basis and a 20 to 25 percent reclassification, "
            "the immediate deduction is around $120,000 to $150,000, worth $44,000 to $55,000 "
            "to an owner in the top bracket against a study cost driven by square footage.</p>",
        ),
        (
            "What is the smallest property worth studying?",
            "<p>There is no hard floor, but below roughly $300,000 of depreciable basis the "
            "$2,000 minimum starts to matter and the answer depends heavily on property type "
            "and whether the deduction is usable. A preliminary estimate settles it quickly.</p>",
        ),
        (
            "Does a residential rental qualify?",
            "<p>Yes. Residential rental property depreciates over 27.5 years rather than 39, "
            "so the baseline deduction is already larger and the reclassification percentage "
            "is typically lower, often 15 to 25 percent. The passive activity question is "
            "usually the deciding factor rather than the study economics.</p>",
        ),
        (
            "How long does a study take?",
            "<p>Typically a few weeks from engagement to delivered report, including the site "
            "documentation and the engineering analysis. Studies on properties already placed "
            "in service in prior years also require the Form 3115 filed with the current year "
            "return to claim the catch-up.</p>",
        ),
    ],
)

CLUSTER = Cluster(
    key="cost-seg",
    slug=P,
    label="Cost Segregation",
    adopted_pillar=True,
    h1="Cost Segregation Study",
    spokes=[
        OWNER_OCCUPIED,
        ROI_BY_TYPE,
        OBBBA,
        Spoke(
            slug="cost-segregation-when-it-makes-sense",
            label="When cost segregation doesn't make sense",
            adopted=True,
        ),
        Spoke(
            slug="form-3115-cost-segregation-lookback",
            label="Cost seg for properties bought 3+ years ago (Form 3115)",
            adopted=True,
        ),
        SMALL_PROPS,
    ],
)
