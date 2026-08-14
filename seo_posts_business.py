#!/usr/bin/env python3
"""Long-tail business ownership and tax planning cluster posts."""

POSTS = [
{
"slug": "ptet-pass-through-entity-tax-election",
"title": "PTET: The Pass Through Entity Tax Election That Works Around the SALT Cap",
"title_tag": "PTET Election and the SALT Cap Workaround | AE Tax Advisors",
"h1": "PTET: The Pass Through Entity Tax Election That Works Around the SALT Cap",
"breadcrumb": "PTET Election",
"category": "Business Owner Tax",
"description": "The pass through entity tax election converts nondeductible personal state tax into a deductible business expense. How PTET works, who benefits, and the traps in electing.",
"lead": "<strong>A pass through entity tax election lets an S corporation or partnership pay state income tax at the entity level, where it is fully deductible as a business expense, instead of passing it to owners where the SALT cap limits the deduction.</strong> The IRS blessed the approach in Notice 2020-75. More than 35 states now offer some version, and for a profitable pass through owner it is often the single largest federal deduction available with no change to operations.",
"body": """
        <h2>The Problem PTET Solves</h2>

        <p>The 2017 tax act capped the state and local tax deduction on individual returns at $10,000. The One Big Beautiful Bill Act raised the cap to $40,000 beginning in 2025, with a phasedown for taxpayers above roughly $500,000 of modified AGI that pushes high earners back toward the $10,000 floor, and a scheduled reversion later in the decade.</p>

        <p>For a business owner in a state with a 6 to 10 percent income tax, state tax on business income can be tens or hundreds of thousands of dollars. Under the cap, most of it is simply not deductible.</p>

        <p>PTET changes where the tax is paid. There is no SALT cap on business deductions, so state income tax paid by the entity reduces the federal income that flows through on the K-1.</p>

        <h2>How It Works in Practice</h2>

        <ol>
            <li>The entity elects into the state's PTET regime, generally annually and often with an early deadline.</li>
            <li>The entity pays state income tax on the owners' distributive shares of income.</li>
            <li>That payment is deducted on the federal return as an ordinary and necessary business expense, reducing federal taxable income flowing to owners.</li>
            <li>Owners claim a state credit or income exclusion so the income is not taxed twice at the state level.</li>
        </ol>

        <h3>The Math on a Real Example</h3>

        <table>
            <thead>
                <tr><th></th><th>Without PTET</th><th>With PTET</th></tr>
            </thead>
            <tbody>
                <tr><td>S corp income</td><td>$1,000,000</td><td>$1,000,000</td></tr>
                <tr><td>State tax at 7%</td><td>$70,000 paid personally</td><td>$70,000 paid by entity</td></tr>
                <tr><td>Federal K-1 income</td><td>$1,000,000</td><td>$930,000</td></tr>
                <tr><td>Federal SALT deduction</td><td>Capped, largely lost</td><td>n/a, already deducted</td></tr>
                <tr><td>Federal tax at 37%</td><td>$370,000</td><td>$344,100</td></tr>
                <tr><td><strong>Federal savings</strong></td><td></td><td><strong>$25,900</strong></td></tr>
            </tbody>
        </table>

        <p>The savings equal the state tax multiplied by the federal marginal rate. Simple, and it repeats every year.</p>

        <h2>Who Benefits Most</h2>

        <ul>
            <li>Owners of S corporations and partnerships with meaningful profit</li>
            <li>Taxpayers in states with high income tax rates</li>
            <li>High earners already past the SALT cap phasedown</li>
            <li>Owners who itemize, and even many who do not, since the deduction is above the line at the entity</li>
        </ul>

        <p>Who does not benefit: single member LLCs and sole proprietors filing on Schedule C, since there is no entity to make the election. That is one more reason entity choice matters. See <a href="/s-corp-vs-llc-tax-savings/">S corp vs LLC</a> and <a href="/blog/when-to-convert-llc-to-s-corp/">when to convert an LLC to an S corp</a>.</p>

        <h2>The Traps</h2>

        <p><strong>Deadlines are unforgiving.</strong> Many states require the election, or a first estimated payment, before the tax year ends or very early in the year. Miss it and you wait a full year. This is the most common way the benefit is lost.</p>

        <p><strong>Cash timing matters.</strong> The deduction generally lands when the entity actually pays. A cash basis entity that elects but does not pay by December 31 may not deduct until the following year.</p>

        <p><strong>Resident credits vary.</strong> If you live in one state and the entity pays PTET in another, your home state may or may not give you credit for the entity level tax. In some pairings this creates genuine double taxation. Multi state owners need the analysis before electing. See <a href="/multi-state-global-tax/">multi state tax planning</a>.</p>

        <p><strong>It is not always all or nothing.</strong> Some states let individual owners opt in or out, others bind every owner. In a partnership with mixed residency or tax exempt partners, an election that helps one partner can hurt another.</p>

        <p><strong>Basis and distributions.</strong> PTET paid by the entity reduces the cash available to distribute and affects owner basis. For S corps, watch the interaction with <a href="/blog/shareholder-basis-tracking-s-corp-essentials/">shareholder basis</a>.</p>

        <p><strong>It reduces QBI.</strong> The entity level deduction lowers qualified business income, which can slightly reduce a Section 199A deduction. The net is still strongly positive, but the modeling should account for it. See our <a href="/qbi-deduction-guide/">QBI guide</a>.</p>

        <h2>PTET and Reasonable Compensation</h2>

        <p>PTET generally applies to the pass through income, not to W-2 wages an S corp owner pays themselves. Since <a href="/reasonable-compensation-s-corp-payroll/">reasonable compensation</a> must still be paid, salary dollars stay outside the PTET benefit. This slightly changes the usual salary versus distribution calculus: distributions now carry an additional federal benefit through PTET, which argues for keeping compensation at a defensible level rather than an inflated one.</p>

        <h2>What to Do Before Year End</h2>

        <ol>
            <li>Confirm your state has a PTET regime and identify the election deadline</li>
            <li>Project entity taxable income for the year</li>
            <li>Make the election and fund the payment before December 31 if the state requires payment for the deduction</li>
            <li>Coordinate owner level estimated payments downward to avoid overpaying twice</li>
            <li>Verify resident state credit treatment for any nonresident owners</li>
        </ol>

        <p>PTET is one of the highest return, lowest complexity items in business owner planning. It requires no restructuring, no new entity, and no change in how the business operates. It just requires someone to file the election on time.</p>
""",
"faqs": [
 ("What is a PTET election?",
  "A pass through entity tax election allows an S corporation or partnership to pay state income tax at the entity level rather than passing the liability to owners individually. Because business level state taxes are not subject to the individual SALT deduction cap, the payment is fully deductible on the federal return, reducing the income reported on each owner's K-1. Owners then receive a state credit or exclusion so the income is not taxed twice by the state."),
 ("Is the PTET workaround allowed by the IRS?",
  "Yes. In Notice 2020-75, the IRS confirmed that state and local income taxes imposed on and paid by a partnership or S corporation are deductible by the entity in computing its nonseparately stated income, and are not subject to the individual SALT limitation. More than 35 states have since enacted pass through entity tax regimes in reliance on that guidance."),
 ("How much does a PTET election save?",
  "The federal savings roughly equal the state tax paid multiplied by the owner's federal marginal rate. An entity paying $70,000 of state tax for an owner in the 37 percent bracket saves about $25,900 of federal tax per year. The exact benefit depends on state rate, entity income, the owner's bracket, and any reduction in the Section 199A qualified business income deduction."),
 ("Who cannot use a PTET election?",
  "Sole proprietors filing on Schedule C and single member LLCs treated as disregarded entities generally cannot, because there is no partnership or S corporation to make the election. C corporations do not need it, since they already deduct state tax at the entity level. Owners in states without a pass through entity tax regime also have no election available."),
 ("When is the deadline to make a PTET election?",
  "Deadlines vary significantly by state. Many require the election or a first estimated payment before the close of the tax year, and some require it as early as the first quarter. Because the deduction typically requires the entity to actually pay the tax within the year, missing the payment date can cost the full year's benefit. Confirm your specific state's deadline well before December."),
 ("Does PTET affect my QBI deduction?",
  "Yes, modestly. The entity level state tax deduction reduces qualified business income, which reduces the Section 199A deduction calculated on that income. The federal savings from the PTET deduction generally far exceed the small reduction in the QBI deduction, but the two effects should be modeled together rather than viewed in isolation."),
],
"related": [
 ("/salt-deduction-cap-workarounds-high-income-taxpayers/", "SALT Deduction Cap Workarounds"),
 ("/qbi-deduction-guide/", "The QBI Deduction Guide"),
 ("/reasonable-compensation-s-corp-payroll/", "Reasonable Compensation for S Corp Owners"),
 ("/s-corp-vs-llc-tax-savings/", "S Corp vs LLC Tax Savings"),
 ("/multi-state-global-tax/", "Multi State and Global Tax Planning"),
 ("/business-owner-tax-planning/", "Business Owner Tax Planning"),
 ("/blog/shareholder-basis-tracking-s-corp-essentials/", "Shareholder Basis Tracking Essentials"),
 ("/blog/when-to-convert-llc-to-s-corp/", "When to Convert an LLC to an S Corp"),
],
"cta_head": "Did Your Entity Make the PTET Election This Year?",
"cta_text": "We check the deadline, project the payment, and coordinate your personal estimates so nothing is paid twice.",
},

{
"slug": "section-179-vehicle-6000-pound-gvwr",
"title": "The 6,000 Pound Vehicle Rule: Section 179 and Bonus Depreciation on SUVs and Trucks",
"title_tag": "6,000 lb Vehicle Tax Deduction Rules (Section 179) | AE Tax Advisors",
"h1": "The 6,000 Pound Vehicle Rule: Section 179 and Bonus Depreciation on SUVs and Trucks",
"breadcrumb": "6,000 Pound Vehicle Rule",
"category": "Business Owner Tax",
"description": "Vehicles over 6,000 pounds GVWR escape the luxury auto depreciation caps. The Section 179 SUV limit, the bed length exception, business use requirements, and the recapture risk.",
"lead": "<strong>A vehicle with a gross vehicle weight rating above 6,000 pounds is not subject to the luxury auto depreciation limits in IRC Section 280F, which is why heavy SUVs and trucks can generate first year deductions that ordinary cars cannot.</strong> Heavy SUVs are still capped for Section 179 purposes at an inflation adjusted limit around $31,300, but bonus depreciation can cover the remaining basis. Pickups with a bed of at least six feet avoid the SUV cap entirely.",
"body": """
        <h2>Why 6,000 Pounds Is the Line</h2>

        <p>Section 280F imposes annual depreciation caps on passenger automobiles to prevent luxury car write offs. Those caps are severe: a few thousand dollars a year, stretching the deduction on an expensive car over many years.</p>

        <p>The statute excludes from the definition of passenger automobile any vehicle with a <strong>gross vehicle weight rating over 6,000 pounds</strong>. GVWR is the manufacturer's maximum loaded weight, not curb weight, and it is printed on the driver's door jamb sticker. Many mid and full size SUVs and nearly all full size pickups clear it.</p>

        <h2>The Three Tiers</h2>

        <table>
            <thead>
                <tr><th>Vehicle type</th><th>Section 179 limit</th><th>Bonus depreciation</th></tr>
            </thead>
            <tbody>
                <tr><td>Passenger auto, 6,000 lb GVWR or less</td><td>Subject to 280F caps</td><td>Subject to 280F caps</td></tr>
                <tr><td>SUV over 6,000 lb GVWR</td><td>Capped near $31,300, indexed</td><td>100% of remaining basis</td></tr>
                <tr><td>Pickup over 6,000 lb with 6 ft bed, or cargo van</td><td>Full Section 179, up to the general cap</td><td>100% of remaining basis</td></tr>
            </tbody>
        </table>

        <p>The SUV cap in Section 179(b)(5) applies to vehicles between 6,000 and 14,000 pounds GVWR. The exceptions that escape it:</p>

        <ul>
            <li>A cargo area of at least six feet that is not readily accessible from the passenger compartment, which is the standard pickup exception</li>
            <li>A vehicle with seating for more than nine passengers behind the driver, such as a shuttle van</li>
            <li>A vehicle with no seating behind the driver and no body section extending more than 30 inches ahead of the windshield, meaning a true cargo van</li>
        </ul>

        <h3>What a Full Deduction Looks Like</h3>

        <p>An $85,000 SUV with 8,000 pound GVWR, used 100 percent for business and placed in service in 2026:</p>

        <table>
            <thead>
                <tr><th>Step</th><th>Amount</th></tr>
            </thead>
            <tbody>
                <tr><td>Section 179 on heavy SUV</td><td>~$31,300</td></tr>
                <tr><td>100% bonus depreciation on remainder</td><td>~$53,700</td></tr>
                <tr><td><strong>Total year one deduction</strong></td><td><strong>$85,000</strong></td></tr>
                <tr><td>Value at 37% federal</td><td>~$31,450</td></tr>
            </tbody>
        </table>

        <p>With <a href="/blog/bonus-depreciation-2026/">100 percent bonus depreciation permanent</a>, the SUV cap has become far less consequential. Bonus picks up whatever Section 179 leaves behind.</p>

        <h2>The Business Use Requirement Is Where People Get Hurt</h2>

        <p>Vehicles are <strong>listed property</strong> under Section 280F(d)(4). Two rules follow:</p>

        <ol>
            <li><strong>Business use must exceed 50 percent</strong> to claim Section 179 or accelerated depreciation. At 50 percent or less, you are forced onto straight line ADS.</li>
            <li><strong>The deduction is proportional.</strong> Use the vehicle 70 percent for business and you deduct 70 percent of the cost, not all of it.</li>
        </ol>

        <p>If business use later drops to 50 percent or below, <strong>recapture</strong> applies. You must recompute depreciation as if you had used straight line ADS from the start and report the excess as ordinary income in the year the use dropped. Buying a heavy SUV in a high income year and then using it mostly personally afterward is how a large deduction turns into a large add back.</p>

        <h2>Substantiation: The Part Everyone Skips</h2>

        <p>Section 274(d) requires that listed property deductions be substantiated by adequate records. Estimates and after the fact reconstructions are routinely disallowed. You need a contemporaneous log capturing:</p>

        <ul>
            <li>Date of each business trip</li>
            <li>Mileage for the trip</li>
            <li>Destination</li>
            <li>Business purpose</li>
            <li>Total annual mileage, to compute the business percentage</li>
        </ul>

        <p>A mileage tracking app satisfies this and takes almost no effort. A shoebox of gas receipts does not. See <a href="/vehicle-deductions-mileage-logs/">vehicle deductions and mileage logs</a>.</p>

        <h2>Actual Expense Versus Standard Mileage</h2>

        <p>Section 179 and bonus depreciation are only available under the <strong>actual expense method</strong>. If you use the standard mileage rate, depreciation is already baked into the rate and no separate deduction is allowed.</p>

        <p>You also cannot switch freely. If you use actual expenses with accelerated depreciation in year one, you are locked into actual expenses for that vehicle for as long as you own it. For an expensive heavy vehicle driven modestly, actual expenses usually wins. For a cheaper vehicle driven a lot of miles, standard mileage often wins. Run both before the first return is filed.</p>

        <h2>S Corp and Partnership Owners: Ownership Matters</h2>

        <p>If the vehicle is titled to you personally but used for the business, the cleanest treatment is usually reimbursement through an <a href="/accountable-plan/">accountable plan</a> at the standard mileage rate, which is deductible to the business and tax free to you. Titling the vehicle in the entity allows the entity to depreciate it, but then personal use becomes a taxable fringe benefit that must be valued and added to your W-2. Neither approach is automatically better, and mixing them incorrectly is a common exam finding. See <a href="/blog/home-office-deduction-s-corp-owners/">how S corp owners handle mixed use assets</a>.</p>

        <h2>A Note on How This Gets Marketed</h2>

        <p>The heavy vehicle deduction is real and it is in the statute. It is also promoted online in ways that ignore the business use requirement, the substantiation rules, and the recapture exposure. The deduction is worth having when you genuinely need the vehicle for the business. It is not a reason to buy a vehicle you would not otherwise buy, since you are spending a full dollar to save roughly forty cents.</p>
""",
"faqs": [
 ("What is the 6,000 pound vehicle tax deduction rule?",
  "Vehicles with a gross vehicle weight rating over 6,000 pounds are excluded from the definition of a passenger automobile under IRC Section 280F, so they are not subject to the annual luxury auto depreciation caps. This allows much larger first year deductions through Section 179 and bonus depreciation. GVWR is the manufacturer's maximum loaded weight and appears on the driver's door jamb sticker, not the vehicle's curb weight."),
 ("How much can you deduct for an SUV over 6,000 pounds?",
  "Section 179 expensing on a heavy SUV between 6,000 and 14,000 pounds GVWR is capped at an inflation adjusted amount around $31,300. However, 100 percent bonus depreciation can cover the remaining basis, so a business owner using the vehicle entirely for business can often deduct the full cost in year one. The deduction is reduced proportionally by any personal use."),
 ("Do pickup trucks avoid the Section 179 SUV limit?",
  "Yes, if the truck has a cargo bed of at least six feet that is not readily accessible from the passenger compartment. That exception in Section 179(b)(5) removes the SUV cap, allowing full Section 179 expensing up to the general annual limit. Vehicles seating more than nine passengers behind the driver and true cargo vans also qualify for the exception."),
 ("What happens if business use of my vehicle drops below 50 percent?",
  "Recapture applies. You must recompute depreciation as if the straight line Alternative Depreciation System had been used from the year the vehicle was placed in service, and report the excess previously claimed as ordinary income in the year business use fell to 50 percent or less. This can create a significant add back years after the original deduction."),
 ("Can I take Section 179 on a vehicle if I use the standard mileage rate?",
  "No. Section 179 and bonus depreciation are only available under the actual expense method. The standard mileage rate already includes a depreciation component, so no separate depreciation deduction is permitted. Choosing accelerated depreciation in the first year generally locks you into the actual expense method for that vehicle for as long as you own it."),
 ("Should my business or I personally own the vehicle?",
  "It depends. Personal ownership with reimbursement through an accountable plan at the standard mileage rate is simple, deductible to the business, and tax free to you. Entity ownership allows the business to depreciate the vehicle but makes personal use a taxable fringe benefit that must be valued and included on your W-2. The right answer turns on vehicle cost, business use percentage, and how much administrative work you are willing to carry."),
],
"related": [
 ("/vehicle-deductions-mileage-logs/", "Vehicle Deductions and Mileage Logs"),
 ("/the-smart-way-to-handle-business-vehicle-deductions/", "The Smart Way to Handle Business Vehicle Deductions"),
 ("/blog/section-179-vs-bonus-depreciation-difference/", "Section 179 vs Bonus Depreciation"),
 ("/blog/bonus-depreciation-2026/", "Bonus Depreciation in 2026"),
 ("/accountable-plan/", "Accountable Plans for Business Owners"),
 ("/blog/macrs-depreciation-schedule-explained/", "MACRS Depreciation Schedules Explained"),
 ("/business-owner-tax-planning/", "Business Owner Tax Planning"),
 ("/blog/can-i-write-off-a-boat-or-airplane-for-business/", "Writing Off a Boat or Airplane"),
],
"cta_head": "Buying a Vehicle Through the Business This Year?",
"cta_text": "We size the deduction, check the GVWR and bed length rules, and set up substantiation that survives an exam.",
},

{
"slug": "oil-and-gas-working-interest-tax-deduction",
"title": "Oil and Gas Working Interests: The Active Loss Exception Most Investors Miss",
"title_tag": "Oil and Gas Working Interest Tax Deduction (IDC) | AE Tax Advisors",
"h1": "Oil and Gas Working Interests: The Active Loss Exception Most Investors Miss",
"breadcrumb": "Oil and Gas Working Interests",
"category": "Tax Planning",
"description": "A working interest in oil and gas is exempt from the passive activity rules under IRC 469(c)(3), and intangible drilling costs are largely deductible in year one. The rules, the risks, and who this fits.",
"lead": "<strong>A working interest in an oil and gas property is statutorily excluded from the passive activity loss rules under IRC Section 469(c)(3), which means losses can offset W-2 wages and business income without any material participation test.</strong> Combined with the current deduction available for intangible drilling costs, this is one of very few ways a high income taxpayer can generate a large active deduction without changing how they spend their time. It also carries unlimited liability and genuine investment risk.",
"body": """
        <h2>The Provision That Makes This Work</h2>

        <p>Section 469(c)(3) provides that the passive activity rules do not apply to a working interest in an oil or gas property, provided the taxpayer's liability is <strong>not limited</strong>. No hours requirement, no material participation test, no 500 hour log.</p>

        <p>This is the opposite of how most tax favored real estate works. With <a href="/str-tax-loophole/">short term rentals</a> or <a href="/real-estate-professional-status-reps-how-to-qualify/">real estate professional status</a>, you buy the deduction with documented time. With a working interest, you buy it with liability exposure.</p>

        <p>The catch is in the phrase "liability is not limited." Hold the interest through a general partnership interest or directly, and the exception applies. Hold it through a limited partnership interest, an LLC membership interest, or any structure that caps your liability, and you lose the exception and the losses become passive.</p>

        <h2>Working Interest Versus Royalty Interest</h2>

        <table>
            <thead>
                <tr><th></th><th>Working interest</th><th>Royalty interest</th></tr>
            </thead>
            <tbody>
                <tr><td>Pays drilling and operating costs</td><td>Yes</td><td>No</td></tr>
                <tr><td>Liability exposure</td><td>Unlimited, if structured for the exception</td><td>None</td></tr>
                <tr><td>Section 469 treatment</td><td>Excluded from passive rules</td><td>Portfolio income</td></tr>
                <tr><td>Deducts intangible drilling costs</td><td>Yes</td><td>No</td></tr>
                <tr><td>Subject to self employment tax</td><td>Generally yes</td><td>No</td></tr>
            </tbody>
        </table>

        <p>Only the working interest gets the deduction treatment. A royalty interest is a passive income stream with no drilling deductions attached.</p>

        <h2>Intangible Drilling Costs</h2>

        <p>Intangible drilling and development costs, or IDC, are the non salvageable expenditures of drilling a well: labor, fuel, chemicals, drilling fluids, site preparation, and rig rental. They typically represent 60 to 80 percent of the cost of a well.</p>

        <p>Under Section 263(c) and the regulations, an operator may elect to deduct IDC currently rather than capitalize it. Tangible costs, meaning casing, pumps, wellhead equipment, and tanks, are capitalized and depreciated, generally as 7 year property eligible for <a href="/blog/bonus-depreciation-2026/">bonus depreciation</a>.</p>

        <p>The result is that a large share of an investment can be deducted in the year it is spent.</p>

        <table>
            <thead>
                <tr><th>Item</th><th>Amount</th><th>Treatment</th></tr>
            </thead>
            <tbody>
                <tr><td>Total investment</td><td>$500,000</td><td></td></tr>
                <tr><td>Intangible drilling costs</td><td>$375,000</td><td>Deducted currently</td></tr>
                <tr><td>Tangible equipment</td><td>$125,000</td><td>7 year property, bonus eligible</td></tr>
                <tr><td><strong>Potential year one deduction</strong></td><td><strong>$500,000</strong></td><td></td></tr>
                <tr><td>Value at 37% federal</td><td>~$185,000</td><td></td></tr>
            </tbody>
        </table>

        <p>Timing matters. IDC is generally deductible when paid for a cash basis taxpayer, but prepaying at year end for a well that will not spud for months runs into the economic performance rules of Section 461(h), which include a limited 90 day exception for drilling. Aggressive December prepayments are a recurring exam issue.</p>

        <h2>Depletion in Later Years</h2>

        <p>Once a well produces, the owner deducts depletion. Percentage depletion under Section 613A allows 15 percent of gross income from the property for independent producers within statutory limits, and it can continue even after basis reaches zero. Cost depletion recovers actual basis over the reserves produced. You generally take the larger of the two.</p>

        <h2>The Alternative Minimum Tax Interaction</h2>

        <p>Excess IDC is an AMT preference item, though independent producers get relief and an exception applies where excess IDC does not exceed 40 percent of alternative minimum taxable income. AMT is far less common after the 2017 changes and the OBBBA exemption adjustments, but for a taxpayer taking a very large IDC deduction against otherwise ordinary income, it should still be checked rather than assumed away.</p>

        <h2>Self Employment Tax</h2>

        <p>Because the working interest is treated as a trade or business and the liability is unlimited, net income from it is generally subject to self employment tax. In loss years this is irrelevant. In profitable years it is a real cost that the original modeling often ignores.</p>

        <h2>Who This Actually Fits</h2>

        <ul>
            <li>Taxpayers with $500,000 or more of active income and a large current year tax liability</li>
            <li>Investors who can afford to lose the entire investment without changing their financial plan</li>
            <li>People who have already used the more conventional tools: retirement plans, <a href="/defined-benefit-plans-tax-shelter-high-income-business-owners/">defined benefit plans</a>, entity optimization, <a href="/cost-segregation-studies-for-real-estate-investors/">cost segregation</a></li>
            <li>Those willing to underwrite the operator carefully, not just the tax outcome</li>
        </ul>

        <h2>What to Watch For</h2>

        <p>This is an area with real economics and also real promoter activity. Before investing:</p>

        <ol>
            <li><strong>Underwrite the geology and the operator, not the tax deduction.</strong> A 100 percent deduction on a worthless well is a 100 percent loss with a partial rebate.</li>
            <li><strong>Read the structure carefully.</strong> If the offering limits your liability, the Section 469(c)(3) exception does not apply and the losses are passive. Some programs convert a general partner interest to a limited interest after the drilling phase, which is intentional and should be understood.</li>
            <li><strong>Watch the IDC percentage claimed.</strong> Very high IDC allocations relative to total cost invite scrutiny.</li>
            <li><strong>Confirm at risk basis</strong> under Section 465. Nonrecourse financing does not create deductible losses.</li>
            <li><strong>Be skeptical of anything sold primarily on the tax benefit.</strong> That framing correlates strongly with poor investment outcomes.</li>
        </ol>

        <p>Used well, a working interest is a legitimate and powerful planning tool. Used as a way to avoid tax on an otherwise unexamined basis, it is an expensive way to lose money.</p>
""",
"faqs": [
 ("Are oil and gas working interest losses passive?",
  "No, provided your liability is not limited. IRC Section 469(c)(3) specifically excludes a working interest in an oil or gas property from the passive activity loss rules when the taxpayer's form of ownership does not limit liability. That means losses can offset wages, business income, and other active income without meeting any material participation test. Holding the interest through a limited partnership or an LLC that caps liability forfeits the exception."),
 ("What are intangible drilling costs?",
  "Intangible drilling costs are the non salvageable expenses of drilling and preparing a well, including labor, fuel, chemicals, drilling fluids, site preparation, and rig rental. They generally represent 60 to 80 percent of total well cost. Under IRC Section 263(c), a taxpayer may elect to deduct these costs currently instead of capitalizing them, which is what produces the large first year deduction associated with oil and gas investments."),
 ("How much of an oil and gas investment is deductible in year one?",
  "Frequently a large majority of it. Intangible drilling costs, typically 60 to 80 percent of the investment, can be deducted currently, and the remaining tangible equipment is generally 7 year property eligible for bonus depreciation. Depending on timing and structure, a substantial portion of the investment can be deducted in the first year, though economic performance rules limit how far in advance you can prepay and deduct."),
 ("Is oil and gas working interest income subject to self employment tax?",
  "Generally yes. A working interest held with unlimited liability is treated as a trade or business, so net income is subject to self employment tax. This is a cost that often gets overlooked in projections that focus only on the first year deduction. Royalty interests, by contrast, are not subject to self employment tax."),
 ("What is the difference between a working interest and a royalty interest?",
  "A working interest holder pays a share of drilling and operating costs, bears liability, and is entitled to deduct intangible drilling costs and claim the Section 469(c)(3) passive activity exception. A royalty interest holder receives a share of production revenue without paying costs, has no liability, and receives portfolio income with no drilling deductions. Only working interests produce the large first year deductions."),
],
"related": [
 ("/defined-benefit-plans-tax-shelter-high-income-business-owners/", "Defined Benefit Plans for High Income Owners"),
 ("/blog/passive-activity-loss-rules-investor-guide/", "Passive Activity Loss Rules for Investors"),
 ("/str-tax-loophole/", "The STR Tax Loophole"),
 ("/cost-segregation-studies-for-real-estate-investors/", "Cost Segregation Studies for Real Estate Investors"),
 ("/energy-tax-credits-high-net-worth-investors-clean-energy/", "Energy Tax Credits for High Net Worth Investors"),
 ("/the-business-owners-guide-to-the-at-risk-rules-and-loss-limitation-planning/", "At Risk Rules and Loss Limitation Planning"),
 ("/how-to-lower-taxes-on-high-income-for-high-net-worth-individuals/", "How to Lower Taxes on High Income"),
 ("/blog/bonus-depreciation-2026/", "Bonus Depreciation in 2026"),
],
"cta_head": "Evaluating an Oil and Gas Program?",
"cta_text": "We review the structure, the liability terms, and the at risk basis before you fund, not after the K-1 arrives.",
},

{
"slug": "conservation-easement-tax-deduction-rules",
"title": "Conservation Easement Deductions: What Is Legitimate and What the IRS Attacks",
"title_tag": "Conservation Easement Tax Deduction Rules and Risks | AE Tax Advisors",
"h1": "Conservation Easement Deductions: What Is Legitimate and What the IRS Attacks",
"breadcrumb": "Conservation Easements",
"category": "Tax Planning",
"description": "A qualified conservation contribution under IRC 170(h) is a legitimate deduction. Syndicated easements are listed transactions with a statutory 2.5x basis disallowance. How to tell them apart.",
"lead": "<strong>A conservation easement donation is a legitimate charitable deduction under IRC Section 170(h) when a landowner permanently restricts development on their own property and donates that restriction to a qualified organization.</strong> A syndicated conservation easement, where investors buy into a partnership that donates an inflated easement and passes back a deduction several times their investment, is a different thing entirely. It is a listed transaction, subject to a statutory disallowance rule, and the IRS has prevailed in the overwhelming majority of litigated cases.",
"body": """
        <h2>The Legitimate Version</h2>

        <p>Section 170(h) allows a deduction for a qualified conservation contribution, which requires three elements:</p>

        <ol>
            <li><strong>A qualified real property interest,</strong> typically a perpetual restriction on the use of the land</li>
            <li><strong>A qualified organization,</strong> generally a land trust or government unit with the commitment and resources to enforce the restriction</li>
            <li><strong>A conservation purpose,</strong> meaning public recreation or education, protection of a natural habitat, preservation of open space with public benefit, or preservation of a historically important structure</li>
        </ol>

        <p>A farmer who permanently gives up development rights on land that will stay a farm, and takes a deduction reflecting the honest difference in value, is doing exactly what Congress intended. Deduction limits are favorable: generally 50 percent of AGI with a 15 year carryforward, and 100 percent of AGI for qualified farmers and ranchers.</p>

        <h2>The Version That Draws Enforcement</h2>

        <p>In a syndicated deal, a promoter assembles investors into a partnership that acquires land, obtains an appraisal asserting a very high value based on a hypothetical development that was never going to happen, donates an easement, and allocates a charitable deduction often four to nine times what each investor contributed.</p>

        <p>The IRS designated these as listed transactions in Notice 2017-10, placed them on the annual Dirty Dozen list repeatedly, and has litigated aggressively. Courts have overwhelmingly sided with the government, frequently on both valuation and technical defects in the easement deed itself.</p>

        <h2>The Statutory Rule That Ended Most of These</h2>

        <p>The SECURE 2.0 Act of 2022 added Section 170(h)(7), which <strong>disallows a partnership level conservation easement deduction that exceeds 2.5 times the sum of the partners' adjusted bases</strong> in the partnership. The rule applies to contributions made after December 29, 2022.</p>

        <p>This removed the economics from the syndicated model. A deal promising a 4.5 to 1 deduction cannot deliver it. Narrow exceptions exist for family partnerships, property held three years or more, and certified historic structures, and those exceptions are where remaining promoter activity has migrated.</p>

        <h2>Penalty Exposure</h2>

        <table>
            <thead>
                <tr><th>Penalty</th><th>Amount</th><th>When it applies</th></tr>
            </thead>
            <tbody>
                <tr><td>Accuracy related, substantial valuation misstatement</td><td>20% of underpayment</td><td>Claimed value 150% or more of correct value</td></tr>
                <tr><td>Gross valuation misstatement</td><td>40% of underpayment</td><td>Claimed value 200% or more of correct value</td></tr>
                <tr><td>Reportable transaction understatement</td><td>20% or 30%</td><td>Listed transaction not properly disclosed</td></tr>
                <tr><td>Failure to disclose on Form 8886</td><td>Up to $100,000 individual</td><td>Participation in a listed transaction</td></tr>
            </tbody>
        </table>

        <p>Add interest running from the original due date, plus the professional cost of a multi year examination and possible Tax Court litigation. The reasonable cause defense based on reliance on an appraisal has been rejected repeatedly where the appraisal was procured by the promoter.</p>

        <h2>Substantiation Requirements That Fail Deals on Technicalities</h2>

        <p>Many easement cases are lost without ever reaching valuation, because the paperwork was defective:</p>

        <ul>
            <li><strong>Qualified appraisal</strong> by a qualified appraiser, meeting every element of the regulations</li>
            <li><strong>Form 8283</strong> Section B, signed by both appraiser and donee</li>
            <li><strong>Contemporaneous written acknowledgment</strong> from the donee, obtained before the return is filed</li>
            <li><strong>Cost basis disclosure</strong> on Form 8283, an omission courts have treated as fatal</li>
            <li><strong>A perpetuity compliant deed,</strong> particularly the extinguishment clause governing what the donee receives if the easement is ever terminated. Improper proceeds formulas have sunk many otherwise defensible donations.</li>
            <li><strong>Baseline documentation</strong> establishing the property's condition at the time of donation</li>
            <li><strong>Form 8886</strong> if the transaction is listed or substantially similar</li>
        </ul>

        <h2>How to Tell the Two Apart</h2>

        <table>
            <thead>
                <tr><th>Legitimate donation</th><th>Warning signs</th></tr>
            </thead>
            <tbody>
                <tr><td>You already owned the land, often for years</td><td>Land acquired shortly before donation</td></tr>
                <tr><td>Deduction roughly matches real value given up</td><td>Deduction is a multiple of your cash investment</td></tr>
                <tr><td>You chose the appraiser</td><td>Promoter supplied the appraiser</td></tr>
                <tr><td>Conservation is the actual objective</td><td>Marketed by projected tax savings ratio</td></tr>
                <tr><td>Established land trust with stewardship funding</td><td>Land trust formed or funded by the promoter</td></tr>
                <tr><td>Valuation based on realistic highest and best use</td><td>Valuation assumes development that was never feasible</td></tr>
            </tbody>
        </table>

        <h2>If You Already Participated</h2>

        <p>Do not simply wait. Options include filing Form 8886 disclosure if it was not filed, amending to remove the deduction to limit penalty exposure, and getting independent representation rather than relying on counsel selected by the promoter, whose interests diverge from yours once an examination begins. See <a href="/blog/voluntary-correction-vs-waiting-for-audit/">voluntary correction versus waiting for an audit</a> and <a href="/irs-audit-defense/">IRS audit defense</a>.</p>

        <h2>Better Tools for the Same Objective</h2>

        <p>If the goal is a large deduction against high income, there are strategies with far better risk adjusted outcomes:</p>

        <ul>
            <li><a href="/cost-segregation-studies-for-real-estate-investors/">Cost segregation</a> paired with <a href="/blog/bonus-depreciation-2026/">bonus depreciation</a></li>
            <li><a href="/defined-benefit-plans-tax-shelter-high-income-business-owners/">Defined benefit and cash balance plans</a></li>
            <li>Donor advised funds and appreciated securities gifts</li>
            <li><a href="/blog/ptet-pass-through-entity-tax-election/">PTET elections</a> for pass through owners</li>
            <li>Charitable remainder trusts where philanthropy is genuinely intended</li>
        </ul>

        <p>None of these promise a four to one deduction, because nothing legitimate does.</p>
""",
"faqs": [
 ("Are conservation easement tax deductions legal?",
  "Yes. A qualified conservation contribution under IRC Section 170(h) is a legitimate charitable deduction when a landowner donates a perpetual restriction on their property to a qualified organization for a recognized conservation purpose. What draws IRS enforcement is the syndicated version, where investors buy into a partnership that claims a deduction several times their contribution based on an inflated appraisal."),
 ("What is a syndicated conservation easement?",
  "A syndicated conservation easement is a promoted arrangement in which investors purchase interests in a partnership that acquires land, obtains an appraisal asserting a high value based on hypothetical development, donates an easement, and allocates charitable deductions often four to nine times each investor's contribution. The IRS designated these as listed transactions in Notice 2017-10, and courts have ruled for the government in the large majority of litigated cases."),
 ("What is the 2.5 times basis rule for conservation easements?",
  "Section 170(h)(7), added by the SECURE 2.0 Act of 2022, disallows a partnership level conservation easement deduction to the extent it exceeds 2.5 times the sum of the partners' adjusted bases in the partnership. It applies to contributions made after December 29, 2022 and effectively eliminated the economics of most syndicated deals. Limited exceptions exist for certain family partnerships, property held three years or more, and certified historic structures."),
 ("What are the penalties for an improper conservation easement deduction?",
  "Penalties can reach 20 percent of the underpayment for a substantial valuation misstatement, 40 percent for a gross valuation misstatement where claimed value is 200 percent or more of correct value, and 20 or 30 percent for a reportable transaction understatement. Failure to file Form 8886 disclosing participation in a listed transaction carries penalties up to $100,000 for individuals. Interest accrues from the original return due date."),
 ("How much can I deduct for a conservation easement?",
  "For a qualified conservation contribution, the deduction is generally limited to 50 percent of adjusted gross income with a 15 year carryforward, and 100 percent of AGI for qualified farmers and ranchers. The deduction amount equals the decline in the property's fair market value caused by the easement, established by a qualified appraisal, not by any multiple of what you invested."),
],
"related": [
 ("/irs-audit-defense/", "IRS Audit Defense"),
 ("/blog/voluntary-correction-vs-waiting-for-audit/", "Voluntary Correction vs Waiting for an Audit"),
 ("/cost-segregation-studies-for-real-estate-investors/", "Cost Segregation Studies for Real Estate Investors"),
 ("/defined-benefit-plans-tax-shelter-high-income-business-owners/", "Defined Benefit Plans for High Income Owners"),
 ("/blog/ptet-pass-through-entity-tax-election/", "The PTET Election"),
 ("/tax-planning-for-high-net-worth-individuals-using-advanced-charitable-strategies/", "Advanced Charitable Strategies"),
 ("/how-do-i-avoid-an-irs-audit/", "How to Avoid an IRS Audit"),
 ("/how-to-lower-taxes-on-high-income-for-high-net-worth-individuals/", "How to Lower Taxes on High Income"),
],
"cta_head": "Been Pitched a Deduction That Sounds Too Good?",
"cta_text": "We will tell you plainly whether it holds up, and show you what a defensible version of the same savings looks like.",
},
]
