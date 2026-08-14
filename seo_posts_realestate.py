#!/usr/bin/env python3
"""Long-tail real estate and cost segregation cluster posts."""

POSTS = [
{
"slug": "seven-day-rule-short-term-rental",
"title": "The 7 Day Rule for Short Term Rentals: How the Average Stay Test Works",
"title_tag": "7 Day Rule for Short Term Rentals Explained | AE Tax Advisors",
"h1": "The 7 Day Rule for Short Term Rentals: How the Average Stay Test Works",
"breadcrumb": "The 7 Day Rule",
"category": "Real Estate Tax Strategy",
"description": "The 7 day rule under Treas. Reg. 1.469-1T(e)(3)(ii)(A) removes short term rentals from the passive rental category. How the average is calculated, what counts, and the mistakes that break it.",
"lead": "<strong>The 7 day rule says that if the average period of customer use of a rental property is 7 days or less, the activity is not treated as a rental activity for passive loss purposes under IRC Section 469.</strong> It comes from Treas. Reg. 1.469-1T(e)(3)(ii)(A). Clearing it does not by itself make your losses deductible. It moves the property out of the automatically passive rental bucket and into the ordinary trade or business rules, where material participation decides the outcome.",
"body": """
        <h2>Why the Rule Exists</h2>

        <p>IRC Section 469(c)(2) says that rental activity is passive per se. It does not matter how many hours you work. A landlord who spends 1,000 hours a year on a long term rental still has passive losses that cannot offset wages.</p>

        <p>But Congress recognized that some lodging operations look more like a hotel business than a landlord relationship. The regulations carve out six exceptions to the definition of rental activity, and the first one is the average period of customer use test. A property with an average stay of 7 days or less is running a service business, not collecting rent, so it is not a rental activity at all.</p>

        <h2>How the Average Is Calculated</h2>

        <p>The formula is total rental days divided by the number of separate rental periods during the tax year.</p>

        <table>
            <thead>
                <tr><th>Scenario</th><th>Rental days</th><th>Bookings</th><th>Average</th><th>Result</th></tr>
            </thead>
            <tbody>
                <tr><td>Mountain cabin, weekend heavy</td><td>190</td><td>62</td><td>3.06</td><td>Qualifies</td></tr>
                <tr><td>Beach house, weekly bookings</td><td>168</td><td>24</td><td>7.00</td><td>Qualifies (7 or less)</td></tr>
                <tr><td>Beach house, mixed with monthlies</td><td>210</td><td>26</td><td>8.08</td><td>Fails</td></tr>
                <tr><td>Corporate housing</td><td>300</td><td>10</td><td>30.00</td><td>Fails</td></tr>
            </tbody>
        </table>

        <p>Exactly 7.00 qualifies, because the regulation says 7 days <em>or less</em>. That said, sitting at 6.9 with no margin is a poor place to be. Most operators who rely on this treatment manage toward an average comfortably under 6.</p>

        <h3>What Counts in the Denominator</h3>

        <p>Each separate booking is one rental period. Vacant days between bookings are excluded from both the numerator and the denominator. Days you personally use the property are not rental days and do not enter the calculation, although personal use has its own consequences under Section 280A.</p>

        <p>The calculation is done <strong>per activity</strong>, not per booking. One long stay can be absorbed by many short ones. It is the annual average that governs, so a single 30 day booking in an otherwise weekend driven year is usually survivable. Several of them are not.</p>

        <h2>The Second Exception: The 30 Day Rule</h2>

        <p>There is a related carve out that gets overlooked. If the average period of customer use is <strong>30 days or less</strong> and <strong>significant personal services</strong> are provided in connection with making the property available, the activity is also excluded from rental treatment.</p>

        <p>Significant personal services means services performed by individuals, and the regulation specifically excludes services typically provided with long term rentals: repairs, maintenance, cleaning between tenants, trash collection, and utilities. It contemplates things closer to hotel service: daily housekeeping, concierge, meals, tours, on site staff.</p>

        <p>This exception is harder to satisfy and harder to document than the 7 day test, so it should be treated as a fallback rather than a plan. See <a href="/blog/mid-term-rental-tax-strategy-30-day/">mid term rental tax strategy</a>.</p>

        <h2>Clearing the 7 Day Rule Is Only Step One</h2>

        <p>This is where most people misunderstand the strategy. Passing the average stay test does not make your loss nonpassive. It only removes the automatic passive label. You still have to <strong>materially participate</strong> in the activity under Section 469(h) and Treas. Reg. 1.469-5T.</p>

        <p>There are seven material participation tests. The three that STR owners realistically use:</p>

        <table>
            <thead>
                <tr><th>Test</th><th>Requirement</th><th>Practical note</th></tr>
            </thead>
            <tbody>
                <tr><td>Test 1</td><td>More than 500 hours in the activity</td><td>Hard for a single property</td></tr>
                <tr><td>Test 2</td><td>Substantially all of the participation in the activity</td><td>Breaks if you use a full service property manager</td></tr>
                <tr><td>Test 3</td><td>More than 100 hours and more than any other individual</td><td>The one most STR owners rely on</td></tr>
            </tbody>
        </table>

        <p>Test 3 is the workhorse, and the trap inside it is the phrase "more than any other individual." That includes your cleaner, your co-host, your handyman, and your property manager. If your cleaning crew logs 140 hours and you log 120, you fail, even though you cleared 100. Full detail in <a href="/str-material-participation/">STR material participation</a> and <a href="/blog/material-participation-tests-str-owners-irc-469/">the material participation tests under IRC 469</a>.</p>

        <h2>What Breaks the 7 Day Rule</h2>

        <ul>
            <li><strong>Long winter bookings.</strong> A single 60 day off season stay can drag the annual average past 7.</li>
            <li><strong>Mid term and traveling professional guests.</strong> Attractive revenue, but each 30 day stay costs a lot of average.</li>
            <li><strong>Converting mid year.</strong> The average covers the full tax year, so months as a long term rental before conversion count.</li>
            <li><strong>Grouping with long term rentals.</strong> If activities are grouped together under Treas. Reg. 1.469-4, the average is computed for the combined activity. See <a href="/blog/grouping-elections-real-estate-irc-469/">grouping elections</a>.</li>
            <li><strong>Poor records.</strong> If you cannot produce a booking level report, you cannot prove the average.</li>
        </ul>

        <h2>Documentation You Need</h2>

        <p>The average stay calculation must be supportable on audit. Keep:</p>

        <ol>
            <li>A platform export from Airbnb, VRBO, or your PMS showing every reservation with check in and check out dates</li>
            <li>A reconciliation worksheet computing total rental days, booking count, and the resulting average</li>
            <li>Direct booking records for any reservations taken outside the platform</li>
            <li>A contemporaneous time log for material participation, with dates, hours, and a description of the work</li>
        </ol>

        <p>The time log is the item most often reconstructed after the fact, and courts have repeatedly rejected estimates prepared for an examination. Build it as you go.</p>

        <h2>What the Strategy Is Worth</h2>

        <p>Clearing the 7 day rule and material participation makes an STR loss nonpassive, which means it can offset W-2 wages and business income. Pair that with a <a href="/cost-segregation-airbnb/">cost segregation study</a> and <a href="/blog/bonus-depreciation-2026/">100 percent bonus depreciation</a>, and a first year loss on a $900,000 furnished property can run to $250,000 or more.</p>

        <p>For a physician or executive in the 37 percent bracket, that is roughly $92,000 of federal tax, plus state. This is the mechanism behind what people call the <a href="/str-tax-loophole/">short term rental loophole</a>, and it is a plainly written statutory and regulatory position, not a gray area, provided the facts are real and documented.</p>

        <h2>One Warning About Self Employment Tax</h2>

        <p>Failing to be a rental activity for Section 469 purposes does not automatically make the income subject to self employment tax. Rental real estate income is generally excluded from self employment income under Section 1402(a)(1) unless substantial services are provided to occupants. Short term rental income where you provide only cleaning between guests and basic amenities generally stays outside self employment tax. Add hotel style services and that changes. This is a separate analysis from the passive loss question and the two are frequently conflated.</p>
""",
"faqs": [
 ("What is the 7 day rule for short term rentals?",
  "Under Treas. Reg. 1.469-1T(e)(3)(ii)(A), if the average period of customer use of a property is 7 days or less, the activity is not treated as a rental activity for purposes of the passive activity loss rules in IRC Section 469. That removes the automatic passive classification that applies to rentals. The owner must still materially participate for the losses to be treated as nonpassive and deductible against wages or business income."),
 ("How do you calculate the average rental period?",
  "Divide total rental days for the tax year by the number of separate rental periods, meaning bookings. A property rented 190 days across 62 bookings has an average of 3.06 days and qualifies. A property rented 210 days across 26 bookings averages 8.08 days and does not. Vacant days and personal use days are excluded from the calculation."),
 ("Does the 7 day rule make my rental losses deductible?",
  "Not on its own. Passing the average stay test only removes the property from the per se passive rental category. You must then materially participate in the activity under IRC 469(h), most commonly through the test requiring more than 100 hours of participation and more hours than any other individual, including cleaners, co-hosts, and property managers. Without material participation, the loss remains passive."),
 ("Is exactly 7 days short enough?",
  "Yes. The regulation says 7 days or less, so an average of exactly 7.00 qualifies. In practice, operating with essentially no margin is risky, because a single recalculated or added booking can push the average above the threshold. Most owners relying on this treatment manage toward an average of 6 days or fewer."),
 ("What is the 30 day rule for short term rentals?",
  "A second exception in the same regulation applies when the average period of customer use is 30 days or less and significant personal services are provided in connection with making the property available. Significant personal services do not include repairs, maintenance, cleaning between tenants, trash collection, or utilities. It contemplates hotel style services such as daily housekeeping, concierge, or meals, which makes it substantially harder to satisfy than the 7 day test."),
 ("Does a long booking ruin the 7 day rule for the whole year?",
  "Not necessarily. The test is an annual average across all bookings, so one long stay can be offset by many short ones. A single 30 day booking in an otherwise weekend driven year is usually absorbed. Several long bookings, or a mid year conversion from a long term rental, will often push the average above 7 days."),
],
"related": [
 ("/str-tax-loophole/", "The STR Tax Loophole: Offsetting W-2 Income"),
 ("/str-material-participation/", "STR Material Participation Requirements"),
 ("/cost-segregation-airbnb/", "Cost Segregation for Airbnb and Short Term Rentals"),
 ("/str-vs-ltr-tax-treatment/", "Short Term vs Long Term Rental Tax Treatment"),
 ("/blog/material-participation-tests-str-owners-irc-469/", "Material Participation Tests Under IRC 469"),
 ("/blog/grouping-elections-real-estate-irc-469/", "Grouping Elections for Real Estate"),
 ("/blog/bonus-depreciation-2026/", "Bonus Depreciation in 2026"),
 ("/blog/mid-term-rental-tax-strategy-30-day/", "Mid Term Rental Tax Strategy"),
],
"cta_head": "Confirm Your STR Actually Clears the 7 Day Test",
"cta_text": "We review your booking data, average stay, and participation hours before the return is filed, not after.",
},

{
"slug": "cost-segregation-vs-1031-exchange",
"title": "Cost Segregation vs 1031 Exchange: Using Both Without Losing the Benefit",
"title_tag": "Cost Segregation vs 1031 Exchange: How They Interact | AE Tax Advisors",
"h1": "Cost Segregation vs 1031 Exchange: Using Both Without Losing the Benefit",
"breadcrumb": "Cost Segregation vs 1031",
"category": "Real Estate Tax Strategy",
"description": "Cost segregation accelerates deductions now. A 1031 exchange defers gain later. They work together, but carryover basis rules limit bonus depreciation on the replacement property.",
"lead": "<strong>Cost segregation and a 1031 exchange solve different problems: cost segregation accelerates depreciation deductions during ownership, while a 1031 exchange defers the tax on gain when you sell.</strong> They are compatible, and using both is common. The complication is that after an exchange, only the excess basis, meaning the new money you put into the replacement property, is eligible for bonus depreciation and a fresh accelerated schedule.",
"body": """
        <h2>The Two Strategies Side by Side</h2>

        <table>
            <thead>
                <tr><th></th><th>Cost segregation</th><th>1031 exchange</th></tr>
            </thead>
            <tbody>
                <tr><td>What it does</td><td>Reclassifies components into 5, 7, and 15 year lives</td><td>Defers gain by reinvesting in like kind property</td></tr>
                <tr><td>When it applies</td><td>During ownership</td><td>At disposition</td></tr>
                <tr><td>Benefit</td><td>Larger current deductions</td><td>No current tax on gain</td></tr>
                <tr><td>Cost</td><td>Study fee, larger recapture later</td><td>Strict timelines, qualified intermediary, lower basis carried forward</td></tr>
                <tr><td>Authority</td><td>IRC 167, 168, and the ATG</td><td>IRC 1031</td></tr>
            </tbody>
        </table>

        <h2>The Recapture Question People Worry About</h2>

        <p>The common fear is that cost segregation creates Section 1245 personal property, that personal property no longer qualifies for 1031 treatment after the 2017 tax act, and that the accelerated components therefore trigger recapture in an exchange.</p>

        <p>The 2017 law did limit Section 1031 to real property. But the 2020 final regulations under Treas. Reg. 1.1031(a)-3 define real property for exchange purposes on its own terms, covering land, inherently permanent structures, and structural components. Critically, the regulations state that property is analyzed under that definition regardless of whether it is treated as Section 1245 property for depreciation. A component depreciated over 5 years can still be real property for 1031 purposes if it meets the definition.</p>

        <p>That resolves much of the concern, but not all of it. Items that are genuinely personal property, such as furniture, appliances, and equipment in a furnished rental, are <strong>not</strong> real property under any definition. Those are excluded from the exchange and can produce recognized gain and Section 1245 recapture. On a furnished short term rental, that exposure can be meaningful and should be quantified before closing.</p>

        <h2>The Real Constraint: Carryover Basis</h2>

        <p>The bigger issue is not recapture, it is depreciation on the replacement property. Under Treas. Reg. 1.168(i)-6, the replacement property basis splits in two:</p>

        <ul>
            <li><strong>Exchanged basis.</strong> The adjusted basis carried over from the relinquished property. This continues depreciating on the <em>old</em> property's remaining schedule, using the old recovery period and method. It does not restart, and it is not eligible for bonus depreciation.</li>
            <li><strong>Excess basis.</strong> Any additional investment beyond the value of the relinquished property, typically new cash or new debt. This is treated as newly acquired property, gets a fresh recovery period, and <strong>is</strong> eligible for bonus depreciation.</li>
        </ul>

        <p>The practical consequence: if you trade a $2,000,000 property with $400,000 of remaining basis for a $3,000,000 replacement, only the $1,000,000 of excess basis can be cost segregated for a new bonus depreciation deduction. A study run on the full $3,000,000 misstates the benefit substantially.</p>

        <h3>An Illustration</h3>

        <table>
            <thead>
                <tr><th></th><th>Amount</th><th>Depreciation treatment</th></tr>
            </thead>
            <tbody>
                <tr><td>Replacement property price</td><td>$3,000,000</td><td></td></tr>
                <tr><td>Exchanged (carryover) basis</td><td>$400,000</td><td>Continues on old schedule, no bonus</td></tr>
                <tr><td>Excess basis</td><td>$1,000,000</td><td>New schedule, bonus eligible</td></tr>
                <tr><td>Land in excess basis</td><td>$200,000</td><td>Not depreciable</td></tr>
                <tr><td>Cost seg on $800,000 depreciable excess</td><td>~$240,000 short life</td><td>Deductible in year one</td></tr>
            </tbody>
        </table>

        <p>There is an election under Treas. Reg. 1.168(i)-6(i) to treat the entire replacement property basis as newly placed in service, but it comes at a price: you give up the carryover treatment and generally accelerate recognition. It is situational and should be modeled, not assumed.</p>

        <h2>When to Choose Cost Segregation Over an Exchange</h2>

        <ul>
            <li>You are keeping the property for the long haul and want deductions now</li>
            <li>You can clear the passive loss hurdle through <a href="/blog/seven-day-rule-short-term-rental/">the STR exception</a> or <a href="/real-estate-professional-status-reps-how-to-qualify/">real estate professional status</a></li>
            <li>The property has meaningful short life content, especially <a href="/blog/15-year-land-improvements-depreciation/">land improvements</a></li>
            <li>You have current year income that needs offsetting</li>
        </ul>

        <h2>When to Choose the Exchange</h2>

        <ul>
            <li>You are selling with a large embedded gain and want to keep the capital working</li>
            <li>Your basis is nearly exhausted after years of depreciation</li>
            <li>You are trading up in size or repositioning into a different market</li>
            <li>You intend to hold until death, where a step up in basis eliminates the deferred gain entirely</li>
        </ul>

        <h2>Using Both in Sequence</h2>

        <p>The strongest version of this is straightforward:</p>

        <ol>
            <li>Buy a property and run a cost segregation study to accelerate deductions during the hold</li>
            <li>Use the deductions against active income if participation rules allow</li>
            <li>Exchange into a larger property rather than selling outright, deferring the accumulated recapture</li>
            <li>Cost segregate the excess basis on the replacement property</li>
            <li>Repeat, and hold the final property until death for a basis step up</li>
        </ol>

        <p>Executed carefully, this defers the recapture created by acceleration indefinitely. The failure mode is running a study on the full replacement basis and claiming bonus depreciation that carryover basis rules do not permit, which is a correction waiting to happen. See <a href="/blog/1031-exchange-planning-timing-rules-mistakes/">1031 exchange timing rules and mistakes</a> and <a href="/blog/reverse-1031-exchange/">reverse exchanges</a>.</p>

        <h2>The Timeline You Cannot Miss</h2>

        <p>A forward exchange has two hard deadlines running from the closing of the relinquished property: <strong>45 days</strong> to identify replacement property in writing, and <strong>180 days</strong> to close, or the due date of the return including extensions, whichever is earlier. Neither is extendable except in declared disasters. Proceeds must be held by a qualified intermediary and never touched by you.</p>
""",
"faqs": [
 ("Can you do a cost segregation study on a 1031 exchange property?",
  "Yes, but with a limitation. Under Treas. Reg. 1.168(i)-6, the replacement property basis divides into exchanged basis carried over from the relinquished property, which continues on the old depreciation schedule and is not eligible for bonus depreciation, and excess basis representing new investment, which is treated as newly acquired and is bonus eligible. A cost segregation study on the replacement property should generally be applied to the excess basis."),
 ("Does cost segregation ruin a 1031 exchange?",
  "No. The 2020 final regulations under Treas. Reg. 1.1031(a)-3 define real property for exchange purposes independently of how an item is classified for depreciation, so components treated as Section 1245 property in a cost segregation study can still qualify as real property in an exchange. Genuinely personal property such as furniture, appliances, and equipment is excluded from the exchange and can produce recognized gain and Section 1245 recapture."),
 ("Which is better, cost segregation or a 1031 exchange?",
  "They address different moments. Cost segregation accelerates deductions while you own the property and is most valuable when you can currently use the loss. A 1031 exchange defers gain when you dispose of the property and is most valuable when you have a large embedded gain and intend to stay invested. Many investors use both in sequence: accelerate during the hold, exchange at disposition, then cost segregate the excess basis on the replacement."),
 ("What happens to depreciation recapture in a 1031 exchange?",
  "Recapture is generally deferred rather than eliminated. Accumulated depreciation carries over and continues to be tracked against the replacement property, and gain recognized in the exchange, including boot received, can trigger recapture currently. If the final property in a chain of exchanges is held until death, the basis step up under Section 1014 can eliminate the deferred gain and recapture entirely for the heirs."),
 ("How long do I have to complete a 1031 exchange?",
  "You have 45 calendar days from the closing of the relinquished property to identify replacement property in writing, and 180 calendar days from that same closing to complete the acquisition, or the due date of your return including extensions if that comes first. The deadlines are not extendable outside of IRS declared disaster relief, and sale proceeds must be held by a qualified intermediary throughout."),
],
"related": [
 ("/blog/reverse-1031-exchange/", "Reverse 1031 Exchange: How It Works"),
 ("/blog/1031-exchange-planning-timing-rules-mistakes/", "1031 Exchange Timing Rules and Mistakes"),
 ("/blog/depreciation-recapture-planning/", "Depreciation Recapture Planning"),
 ("/blog/section-1245-vs-1250-depreciation-recapture/", "Section 1245 vs 1250 Recapture"),
 ("/cost-segregation-studies-for-real-estate-investors/", "Cost Segregation Studies for Real Estate Investors"),
 ("/blog/bonus-depreciation-2026/", "Bonus Depreciation in 2026"),
 ("/blog/what-happens-to-depreciation-when-i-sell-after-cost-segregation/", "What Happens to Depreciation When You Sell"),
 ("/blog/1031-exchange-alternatives/", "Alternatives to a 1031 Exchange"),
],
"cta_head": "Planning an Exchange on a Property You Already Cost Segregated?",
"cta_text": "We model the carryover basis, the excluded personal property, and the recapture before you sign anything.",
},

{
"slug": "reverse-1031-exchange",
"title": "Reverse 1031 Exchange: Buying the Replacement Property First",
"title_tag": "Reverse 1031 Exchange Rules and Timeline | AE Tax Advisors",
"h1": "Reverse 1031 Exchange: Buying the Replacement Property First",
"breadcrumb": "Reverse 1031 Exchange",
"category": "Real Estate Tax Strategy",
"description": "A reverse 1031 exchange lets you acquire replacement property before selling. The Rev. Proc. 2000-37 safe harbor, the exchange accommodation titleholder, the 45 and 180 day clocks, and the financing problem.",
"lead": "<strong>A reverse 1031 exchange lets you acquire the replacement property before selling the property you are giving up.</strong> Because tax law does not allow you to own both ends of an exchange at once, an exchange accommodation titleholder takes title to one of the properties temporarily. The structure follows the safe harbor in Rev. Proc. 2000-37, and the same 45 and 180 day deadlines apply, just measured from a different starting point.",
"body": """
        <h2>Why Anyone Does This</h2>

        <p>In a competitive market, a forward exchange puts you in a bad position: you have sold, the clock is running, and you have 45 days to identify a replacement or you owe tax on the full gain. That pressure produces overpaying and bad acquisitions.</p>

        <p>A reverse exchange inverts the risk. You secure the property you want first, then sell on a normal timeline. The tradeoff is that reverse exchanges are more expensive, more complicated, and much harder to finance.</p>

        <h2>The Safe Harbor Structure</h2>

        <p>Rev. Proc. 2000-37 provides a safe harbor under which the IRS will not challenge the arrangement. The mechanics:</p>

        <ol>
            <li>You form a <strong>qualified exchange accommodation arrangement</strong> with an exchange accommodation titleholder, generally an affiliate of your qualified intermediary. The written agreement must be in place within <strong>5 business days</strong> of the EAT taking title.</li>
            <li>The EAT takes and holds legal title to one of the properties, called parking. Two variants exist:
                <ul>
                    <li><strong>Exchange last:</strong> the EAT parks the replacement property. Most common.</li>
                    <li><strong>Exchange first:</strong> the EAT parks the relinquished property. Used when the replacement property has debt or title issues that make parking impractical.</li>
                </ul>
            </li>
            <li>Within <strong>45 days</strong> of the EAT taking title, you identify in writing the property to be relinquished.</li>
            <li>Within <strong>180 days</strong> of the EAT taking title, the exchange must be completed and the parked property transferred to you.</li>
        </ol>

        <p>The 180 day limit is firm. Unlike a forward exchange, there is no version of this where the deadline stretches, and a reverse exchange that fails to close in time generally collapses into a taxable sale.</p>

        <h2>The Financing Problem</h2>

        <p>This is where most reverse exchanges die. The EAT holds title, so the lender is being asked to lend against property owned by a special purpose entity that is not the borrower, for a limited period, with an agreement to convey later. Many conventional lenders will not do it.</p>

        <p>Common workarounds:</p>

        <ul>
            <li>All cash acquisition, then refinance after the exchange completes</li>
            <li>A lender experienced with reverse exchanges who underwrites you and lends to the EAT with your guarantee</li>
            <li>Bridge or hard money financing for the parking period, refinanced after</li>
            <li>A loan from you to the EAT, which the safe harbor expressly permits</li>
        </ul>

        <p>Start the lender conversation before you go under contract. Discovering the financing will not work in week three of a 180 day window is a costly surprise.</p>

        <h2>What It Costs</h2>

        <table>
            <thead>
                <tr><th>Item</th><th>Typical range</th></tr>
            </thead>
            <tbody>
                <tr><td>EAT and reverse exchange fee</td><td>$5,000 to $15,000</td></tr>
                <tr><td>Entity formation and carrying costs</td><td>$1,000 to $3,000</td></tr>
                <tr><td>Additional legal work</td><td>$3,000 to $10,000</td></tr>
                <tr><td>Duplicate closing costs and title work</td><td>Varies with price</td></tr>
                <tr><td>Bridge financing, if used</td><td>Points plus interest for the parking period</td></tr>
            </tbody>
        </table>

        <p>Against a forward exchange at roughly $1,000 to $2,500, a reverse exchange is a meaningful expense. It is justified when the deferred gain is large and the replacement property is genuinely hard to replace.</p>

        <h2>Improvement Exchanges</h2>

        <p>The same parking structure supports a build to suit or improvement exchange, where the EAT holds title while construction is completed with exchange funds. The improvements must be in place before the property transfers to you at the end of 180 days, because you only get exchange credit for improvements actually completed within the window. Partially finished construction does not count toward the value requirement, which makes aggressive renovation timelines risky in this structure.</p>

        <h2>Depreciation on the Replacement Property</h2>

        <p>The carryover basis rules apply exactly as they do in a forward exchange. Exchanged basis continues on the relinquished property's schedule, and only excess basis is newly acquired property eligible for bonus depreciation. If you plan a <a href="/cost-segregation-studies-for-real-estate-investors/">cost segregation study</a> on the replacement, scope it to the excess basis. See <a href="/blog/cost-segregation-vs-1031-exchange/">cost segregation and 1031 exchanges</a>.</p>

        <h2>Rules That Trip People Up</h2>

        <ul>
            <li><strong>You cannot have owned the replacement property in the prior 180 days.</strong> The safe harbor is unavailable if you held it recently.</li>
            <li><strong>Related party acquisitions are restricted</strong> under Section 1031(f) and require care.</li>
            <li><strong>Both properties must be held for investment or productive use in a trade or business.</strong> A property you intend to flip does not qualify.</li>
            <li><strong>Only real property qualifies</strong> after the 2017 tax act. Personal property in the deal is outside the exchange.</li>
            <li><strong>Title company coordination matters.</strong> Not every title company has handled a parked property, and errors in the conveyance chain create real problems.</li>
        </ul>
""",
"faqs": [
 ("What is a reverse 1031 exchange?",
  "A reverse 1031 exchange is a like kind exchange in which the replacement property is acquired before the relinquished property is sold. Because a taxpayer cannot hold both properties simultaneously and still qualify, an exchange accommodation titleholder takes temporary title to one of the properties under the safe harbor in Rev. Proc. 2000-37. The taxpayer then has 45 days to identify the property to be sold and 180 days to complete the exchange."),
 ("How long do you have to complete a reverse 1031 exchange?",
  "The exchange accommodation titleholder can park the property for a maximum of 180 days. Within the first 45 days, you must identify in writing the property you will relinquish. The 180 day limit is strict and is not extended by filing an extension for your return, unlike some aspects of a forward exchange. Failing to close within the window generally results in a fully taxable sale."),
 ("How much does a reverse 1031 exchange cost?",
  "Reverse exchanges typically run $8,000 to $25,000 or more in accommodator fees, entity formation, legal work, and duplicate closing costs, compared with roughly $1,000 to $2,500 for a standard forward exchange. Bridge financing during the parking period adds further cost. The structure generally makes sense when the deferred gain is large and the replacement property would be difficult to secure on a forward timeline."),
 ("Can you finance a reverse 1031 exchange?",
  "It is possible but difficult, because title is held by the exchange accommodation titleholder rather than by you during the parking period. Many conventional lenders decline. Practical options include acquiring with cash and refinancing after the exchange completes, using a lender experienced with reverse exchanges who will lend to the EAT with your guarantee, using bridge financing, or lending to the EAT yourself, which the safe harbor permits."),
 ("What is the difference between exchange first and exchange last?",
  "In an exchange last structure, the accommodator parks the replacement property until you sell the relinquished property. This is the more common approach. In an exchange first structure, the accommodator parks the relinquished property while you take direct title to the replacement. Exchange first is generally used when existing debt, lender restrictions, or title issues make parking the replacement property impractical."),
],
"related": [
 ("/blog/cost-segregation-vs-1031-exchange/", "Cost Segregation vs 1031 Exchange"),
 ("/blog/1031-exchange-planning-timing-rules-mistakes/", "1031 Exchange Timing Rules and Mistakes"),
 ("/blog/1031-exchange-timeline-45-180-day-rules/", "The 45 and 180 Day Exchange Timeline"),
 ("/blog/1031-exchange-alternatives/", "Alternatives to a 1031 Exchange"),
 ("/blog/delaware-statutory-trust-dst-1031-exchange/", "Delaware Statutory Trusts and 1031 Exchanges"),
 ("/blog/depreciation-recapture-planning/", "Depreciation Recapture Planning"),
 ("/cost-segregation-studies-for-real-estate-investors/", "Cost Segregation Studies for Real Estate Investors"),
 ("/real-estate-investor-tax-planning/", "Tax Planning for Real Estate Investors"),
],
"cta_head": "Considering a Reverse Exchange?",
"cta_text": "We coordinate the accommodator, the lender, and the depreciation treatment so the structure holds together.",
},

{
"slug": "section-1245-vs-1250-depreciation-recapture",
"title": "Section 1245 vs Section 1250 Recapture: What You Actually Owe on Sale",
"title_tag": "Section 1245 vs 1250 Depreciation Recapture | AE Tax Advisors",
"h1": "Section 1245 vs Section 1250 Recapture: What You Actually Owe on Sale",
"breadcrumb": "1245 vs 1250 Recapture",
"category": "Depreciation",
"description": "Section 1245 recapture is taxed at ordinary rates. Unrecaptured Section 1250 gain is capped at 25 percent. How the split works after a cost segregation study and how to plan the exit.",
"lead": "<strong>Section 1245 recapture applies to personal property and is taxed at ordinary income rates, up to 37 percent. Unrecaptured Section 1250 gain applies to real property and is capped at 25 percent.</strong> When you sell a property that has been cost segregated, the gain splits across both categories plus long term capital gain, and the mix determines your actual tax bill. Understanding the split before you sell is the difference between a planned exit and an unpleasant surprise.",
"body": """
        <h2>The Three Buckets of Gain</h2>

        <p>Sell a depreciated building and the gain divides into three pieces, each taxed differently:</p>

        <table>
            <thead>
                <tr><th>Bucket</th><th>What it covers</th><th>Federal rate</th></tr>
            </thead>
            <tbody>
                <tr><td>Section 1245 recapture</td><td>Depreciation on personal property: appliances, carpeting, cabinetry, fixtures, equipment</td><td>Ordinary, up to 37%</td></tr>
                <tr><td>Unrecaptured Section 1250 gain</td><td>Straight line depreciation on the building and land improvements</td><td>Maximum 25%</td></tr>
                <tr><td>Section 1231 gain</td><td>Appreciation above original cost basis</td><td>0, 15, or 20% long term capital gain</td></tr>
            </tbody>
        </table>

        <p>Net investment income tax of 3.8 percent applies on top for most high income sellers, and state tax is separate.</p>

        <h2>Why Section 1250 Is Usually Gentler Than People Expect</h2>

        <p>Full Section 1250 recapture at ordinary rates only applies to depreciation taken in <em>excess</em> of straight line. Since 1986, real property under MACRS is required to use straight line, so there is essentially no excess depreciation on modern buildings and true 1250 recapture is almost always zero.</p>

        <p>What actually applies is <strong>unrecaptured Section 1250 gain</strong> under Section 1(h)(1)(E), which taxes the straight line depreciation you claimed at a maximum of 25 percent. It is technically a capital gain rate, just a higher one than the usual 15 or 20 percent.</p>

        <h2>How a Cost Segregation Study Changes the Mix</h2>

        <p>This is the tradeoff nobody explains clearly when selling a study. Reclassifying components into 5 year property produces a much larger deduction now, and moves that same depreciation from the 25 percent bucket into the ordinary income bucket on exit.</p>

        <p>A $2,000,000 property held five years, sold for $2,400,000:</p>

        <table>
            <thead>
                <tr><th></th><th>No study</th><th>With cost segregation</th></tr>
            </thead>
            <tbody>
                <tr><td>Depreciation claimed</td><td>$290,000</td><td>$780,000</td></tr>
                <tr><td>1245 recapture at 37%</td><td>$0</td><td>$300,000, tax $111,000</td></tr>
                <tr><td>Unrecaptured 1250 at 25%</td><td>$290,000, tax $72,500</td><td>$480,000, tax $120,000</td></tr>
                <tr><td>1231 gain at 20%</td><td>$400,000, tax $80,000</td><td>$400,000, tax $80,000</td></tr>
                <tr><td><strong>Tax at sale</strong></td><td><strong>$152,500</strong></td><td><strong>$311,000</strong></td></tr>
                <tr><td>Tax saved during hold at 37%</td><td>$107,300</td><td>$288,600</td></tr>
                <tr><td><strong>Net across the hold</strong></td><td><strong>-$45,200</strong></td><td><strong>-$22,400</strong></td></tr>
            </tbody>
        </table>

        <p>The study still wins, and that ignores five years of using the money. But the sale year tax is roughly double, and the seller who was not told this ahead of time is the one who ends up angry. Figures are illustrative; the mix depends on allocation, hold period, and rates.</p>

        <h2>Six Ways to Manage the Recapture</h2>

        <ol>
            <li><strong>Do not sell.</strong> A <a href="/blog/cost-segregation-vs-1031-exchange/">1031 exchange</a> defers the entire amount. Chain exchanges and hold until death, and the Section 1014 basis step up can eliminate it for your heirs.</li>
            <li><strong>Use a partial asset disposition.</strong> When you replace a roof or parking lot, elect to write off the remaining basis of the old component. That reduces the depreciation later subject to recapture. See <a href="/blog/partial-asset-disposition-overlooked-tax-strategy/">partial asset disposition</a>.</li>
            <li><strong>Time the sale into a low income year.</strong> 1245 recapture is taxed at ordinary rates, so it is highly bracket sensitive. Selling in a retirement or sabbatical year can move it several brackets.</li>
            <li><strong>Use an installment sale for the 1231 portion.</strong> Note that Section 1245 recapture is <em>not</em> eligible for installment treatment under Section 453(i) and is recognized entirely in the year of sale, even if you receive nothing that year. This surprises people badly.</li>
            <li><strong>Offset with suspended passive losses.</strong> A fully taxable disposition frees suspended losses under Section 469(g), which can absorb a large part of the gain. See <a href="/blog/passive-activity-loss-rules-investor-guide/">passive activity loss rules</a>.</li>
            <li><strong>Allocate the purchase price thoughtfully.</strong> The buyer wants basis in short life assets, you want gain in the 1231 bucket. It is a negotiated allocation reported by both parties on Form 8594, and it must be consistent.</li>
        </ol>

        <h2>Where This Shows Up on the Return</h2>

        <p>Sales of business and rental property are reported on Form 4797. Section 1245 recapture is computed in Part III and carries to Part II as ordinary income. Section 1231 gain flows to Schedule D. Unrecaptured Section 1250 gain is tracked on the Unrecaptured Section 1250 Gain Worksheet and taxed through the Schedule D tax computation. If a single sale is misreported as a simple capital gain, the error is usually visible in the absence of a Form 4797 entirely.</p>

        <h2>The Planning Point</h2>

        <p>Recapture is not a reason to avoid <a href="/cost-segregation-studies-for-real-estate-investors/">cost segregation</a>. Deferral has real value, and for most investors the present value math favors accelerating. But the exit needs to be modeled at the same time as the entry, not five years later when the property is already under contract. See <a href="/blog/what-happens-to-depreciation-when-i-sell-after-cost-segregation/">what happens to depreciation when you sell</a>.</p>
""",
"faqs": [
 ("What is the difference between Section 1245 and Section 1250 property?",
  "Section 1245 property is depreciable personal property, including appliances, carpeting, cabinetry, fixtures, machinery, and equipment. Section 1250 property is depreciable real property, meaning buildings and their structural components along with land improvements. The distinction matters at sale, because depreciation on 1245 property is recaptured at ordinary income rates while depreciation on 1250 property is generally taxed as unrecaptured Section 1250 gain at a maximum of 25 percent."),
 ("What is the tax rate on depreciation recapture?",
  "Section 1245 recapture is taxed at ordinary income rates, which can reach 37 percent federally. Unrecaptured Section 1250 gain is taxed at a maximum rate of 25 percent. Gain above your original cost basis is Section 1231 gain taxed at long term capital gain rates of 0, 15, or 20 percent. The 3.8 percent net investment income tax may apply on top, and state tax is separate."),
 ("Does cost segregation increase depreciation recapture?",
  "It changes the character of the recapture rather than creating more of it. By reclassifying components into 5, 7, and 15 year property, a study moves depreciation that would have been taxed at a maximum of 25 percent into the Section 1245 category taxed at ordinary rates. Total depreciation over the hold is similar, but more of it is recaptured at higher rates on sale. The accelerated deduction usually still wins on a present value basis, but the exit should be modeled up front."),
 ("Can you avoid depreciation recapture?",
  "You can defer it or eliminate it in certain ways. A 1031 exchange defers recapture into the replacement property. Holding until death gives heirs a stepped up basis under Section 1014, which eliminates the deferred gain and recapture. Suspended passive losses released on a fully taxable disposition can offset the gain. Timing a sale into a low income year reduces the rate on the ordinary portion. Simply selling in a normal year does not avoid it."),
 ("Is depreciation recapture eligible for installment sale treatment?",
  "No. Under Section 453(i), Section 1245 depreciation recapture must be recognized in full in the year of sale, regardless of how much cash you receive that year. Only the remaining Section 1231 gain can be spread across installment payments. Sellers who structure a seller financed sale without accounting for this can owe substantial tax in year one with very little cash collected."),
],
"related": [
 ("/blog/depreciation-recapture-planning/", "Depreciation Recapture Planning"),
 ("/blog/what-happens-to-depreciation-when-i-sell-after-cost-segregation/", "What Happens to Depreciation When You Sell"),
 ("/blog/cost-segregation-vs-1031-exchange/", "Cost Segregation vs 1031 Exchange"),
 ("/blog/partial-asset-disposition-overlooked-tax-strategy/", "Partial Asset Disposition"),
 ("/blog/5-year-property-depreciation/", "5 Year Property Depreciation"),
 ("/blog/15-year-land-improvements-depreciation/", "15 Year Land Improvements"),
 ("/cost-segregation-studies-for-real-estate-investors/", "Cost Segregation Studies for Real Estate Investors"),
 ("/the-business-owners-guide-to-installment-sales-and-deferred-gain-strategies/", "Installment Sales and Deferred Gain Strategies"),
],
"cta_head": "Know Your Recapture Number Before You List the Property",
"cta_text": "We compute the 1245, 1250, and 1231 split and show you the levers that actually move it.",
},
]
