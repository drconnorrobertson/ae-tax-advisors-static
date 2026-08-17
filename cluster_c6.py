#!/usr/bin/env python3
"""Cluster 6: Real estate tax strategy for business owners.

The site already ranks for most of these topics, so this cluster is mostly
adoption. The one genuinely uncovered angle, qualifying for REPS through a
spouse, is written new.
"""

from __future__ import annotations

from cluster_common import Cluster, Spoke

P = "real-estate-tax-strategy-business-owners"

REPS_SPOUSE = Spoke(
    slug="reps-qualification-through-spouse",
    label="REPS qualification through your spouse",
    title="REPS Qualification Through Your Spouse: How It Actually Works",
    description=(
        "Why a spouse can qualify for real estate professional status when a busy "
        "business owner cannot, and the documentation the position requires."
    ),
    h1="REPS Qualification Through Your Spouse",
    subtitle=(
        "The hours test is applied per spouse. The benefit lands on a joint return. "
        "That asymmetry is the entire strategy."
    ),
    lead=(
        "Real estate professional status under Section 469(c)(7) removes the automatic "
        "passive classification from rental activities, allowing rental losses to offset "
        "active business income. A business owner working full time in their own company "
        "essentially cannot meet the tests. A spouse who does not have a demanding "
        "non-real-estate job often can, and because the tests are applied to each spouse "
        "individually while the benefit lands on a jointly filed return, one qualifying "
        "spouse is enough."
    ),
    keywords=[
        "reps qualification spouse",
        "real estate professional status spouse",
        "spouse real estate professional business owner",
    ],
    body=[
        (
            "What REPS Requires",
            "<p>Two tests must both be met, and they are applied to each spouse "
            "individually:</p>"
            "<ul>"
            "<li><strong>More than half of all personal services</strong> performed in trades "
            "or businesses during the year must be in real property trades or businesses in "
            "which the taxpayer materially participates.</li>"
            "<li><strong>More than 750 hours</strong> of service during the year in those "
            "real property trades or businesses.</li>"
            "</ul>"
            "<p>Qualifying as a real estate professional is only the first step. Each rental "
            "activity must also satisfy material participation, which is why most taxpayers "
            "pursuing this also make the election to aggregate all rental interests into a "
            "single activity. Without aggregation, the material participation test has to be "
            "met property by property, which is far harder.</p>"
        ),
        (
            "Why a Busy Business Owner Cannot Qualify",
            "<p>The more-than-half test is the obstacle. An owner working 2,000 hours a year "
            "in their operating business would need more than 2,000 hours in real property "
            "trades or businesses to satisfy it, which is not credible for someone genuinely "
            "running a company.</p>"
            "<p>The 750-hour test alone is achievable for many owners. The more-than-half "
            "test is not, and both must be met. This is where taxpayers most often lose in "
            "court: they document 800 hours on rentals and overlook that their 2,200 hours in "
            "the operating business defeat the comparison.</p>"
        ),
        (
            "Why the Spouse Route Works",
            "<p>The tests are applied to each spouse separately, and the statute does not "
            "permit combining the spouses' hours to meet them. That sounds restrictive, and "
            "in this context it is the point: only one spouse needs to qualify.</p>"
            "<p>Once either spouse qualifies as a real estate professional, the rental "
            "activities lose their automatic passive character on the joint return. The "
            "resulting losses can then offset the other spouse's active business income, "
            "because a joint return combines both spouses' income and deductions.</p>"
            "<p>So a business owner working 2,200 hours in their company, married to a spouse "
            "who spends 900 hours managing the couple's rental portfolio and has no other "
            "substantial trade or business, can have rental losses offset the business income "
            "even though the owner personally could never qualify.</p>"
        ),
        (
            "Material Participation Still Has to Be Met",
            "<p>Qualifying as a real estate professional is necessary but not sufficient. The "
            "rental activities must also meet material participation, which is generally "
            "satisfied by more than 500 hours in the activity, by participation that is "
            "substantially all of the participation by anyone, or by one of the other "
            "regulatory tests.</p>"
            "<p>For a spouse already logging 750 or more hours to meet the REPS threshold, "
            "the 500-hour material participation test on an aggregated portfolio is usually "
            "met by the same work. Note that for material participation specifically, the "
            "regulations do allow a spouse's participation to be counted, which is a "
            "different rule from the REPS qualification tests and is a frequent source of "
            "confusion.</p>"
        ),
        (
            "The Documentation That Decides the Case",
            "<p>This position is examined regularly, and cases are won or lost on records "
            "rather than on the underlying facts.</p>"
            "<p>What holds up is a contemporaneous log with dates, hours, the specific "
            "activity performed, and the property involved, maintained during the year. What "
            "does not hold up is a summary reconstructed after a notice arrives, often from "
            "memory, frequently containing round numbers and implausible totals. Courts have "
            "repeatedly rejected reconstructed logs, and estimates like ten hours a week "
            "every week are treated as what they are.</p>"
            "<p>The log should also capture what the other spouse does, because the "
            "more-than-half test depends on the qualifying spouse's total service hours "
            "across all trades and businesses, not only the real estate hours.</p>"
            "<p>Time spent as an investor, such as reviewing financial statements or "
            "monitoring performance in a non-managerial capacity, does not count. Neither "
            "does travel in most circumstances. Hours must reflect actual operational work: "
            "tenant management, maintenance coordination, leasing, acquisitions, and "
            "oversight of contractors.</p>"
        ),
        (
            "Where the Strategy Falls Apart",
            "<p>Three recurring failures:</p>"
            "<p><strong>The spouse has another job.</strong> A spouse working 1,500 hours "
            "elsewhere needs more than 1,500 real estate hours to satisfy the more-than-half "
            "test. Part-time employment elsewhere does not necessarily defeat it, but it "
            "raises the bar and it has to be measured.</p>"
            "<p><strong>A property manager does the work.</strong> If a management company "
            "handles tenants, maintenance, and leasing, the spouse's remaining hours are "
            "often thin and largely investor-type activity. This is the most common "
            "structural problem, because the same portfolio that justifies the strategy is "
            "often the one large enough to warrant professional management.</p>"
            "<p><strong>Hours are not credible against the portfolio.</strong> Claiming 900 "
            "hours managing two single-family rentals invites the question of what occupied "
            "those hours. The claimed time has to be plausible for the properties held.</p>"
        ),
    ],
    takeaways=[
        "The REPS tests are applied per spouse, so only one spouse needs to qualify.",
        "The more-than-half test, not the 750-hour test, is what disqualifies busy business owners.",
        "Aggregating rental interests into one activity is usually necessary for material participation.",
        "Contemporaneous logs win these cases; reconstructed summaries routinely fail.",
        "A property manager doing the operational work is the most common structural obstacle.",
    ],
    faqs=[
        (
            "Can my spouse qualify for REPS so I can use rental losses?",
            "<p>Yes. The tests are applied to each spouse individually, and if either spouse "
            "qualifies, the rental activities lose their automatic passive character on a "
            "joint return. The losses can then offset the other spouse's active business "
            "income.</p>",
        ),
        (
            "Can we combine our hours to reach 750?",
            "<p>No. The 750-hour and more-than-half tests must be satisfied by one spouse "
            "individually. Material participation is different: for that test the regulations "
            "do permit a spouse's participation to be counted. Confusing the two rules is a "
            "common and expensive error.</p>",
        ),
        (
            "What if my spouse works part time somewhere else?",
            "<p>It raises the bar rather than disqualifying automatically. The more-than-half "
            "test compares real property service hours against all trade or business service "
            "hours, so a spouse working 1,000 hours elsewhere needs more than 1,000 real "
            "estate hours plus at least 750.</p>",
        ),
        (
            "Does using a property manager disqualify us?",
            "<p>Not automatically, but it makes the position much harder. If the manager "
            "handles tenants, maintenance, and leasing, the remaining owner hours are often "
            "thin and largely investor-type activity, which does not count. The hours claimed "
            "must reflect genuine operational work.</p>",
        ),
        (
            "What records do we need to keep?",
            "<p>A contemporaneous log kept during the year showing dates, hours, the specific "
            "activity, and the property. It should also capture the qualifying spouse's hours "
            "in any other trade or business, since the more-than-half test depends on the "
            "comparison. Logs reconstructed after an examination begins are routinely "
            "rejected.</p>",
        ),
    ],
)

CLUSTER = Cluster(
    key="real-estate",
    slug=P,
    label="Real Estate Tax Strategy",
    title="Real Estate Tax Strategy for Business Owners: The Complete Guide",
    description=(
        "How profitable business owners use real estate depreciation to offset business "
        "income, and the passive activity rules that decide whether it works."
    ),
    h1="Real Estate Tax Strategy for Business Owners",
    subtitle=(
        "The depreciation is easy to generate. Making it usable against your business "
        "income is the entire problem."
    ),
    lead=(
        "Real estate tax strategy for business owners is the use of property depreciation, "
        "particularly accelerated depreciation from cost segregation, to offset income from "
        "an operating business. Generating the deduction is straightforward. The difficulty "
        "is the passive activity rules under Section 469, which by default prevent rental "
        "losses from offsetting business income. Every strategy in this area is ultimately "
        "about getting through that constraint."
    ),
    keywords=[
        "real estate tax strategy business owners",
        "offset business income with real estate",
        "passive loss rules business owner",
        "real estate depreciation offset income",
    ],
    body=[
        (
            "The Constraint That Defines Everything",
            "<p>Rental activity is passive by default under Section 469, regardless of how "
            "involved the owner is. Passive losses can offset passive income, and generally "
            "nothing else. They are not lost when they cannot be used; they are suspended and "
            "carried forward until there is passive income to absorb them or the property is "
            "sold in a fully taxable transaction.</p>"
            "<p>This is why so many business owners feel that a cost segregation study "
            "underdelivered. The study did its job: it produced a $400,000 first-year "
            "deduction. The deduction then sat suspended, because the owner had $800,000 of "
            "active business income and no passive income for it to offset. The failure was "
            "not the study. It was that nobody asked, before commissioning it, whether the "
            "loss would be usable.</p>"
            "<p>There are four routes through, and every real estate strategy for a business "
            "owner is one of them.</p>"
        ),
        (
            "Route One: Property Used in Your Own Business",
            "<p>The cleanest route, and the most overlooked. Where the property is used in a "
            "trade or business the owner materially participates in, it is not a passive "
            "rental activity, and depreciation offsets active business income directly.</p>"
            "<p>For an owner whose company operates from a building they own, this makes cost "
            "segregation unusually attractive: the passive question largely falls away and "
            "the hold period is naturally long, because the business is not moving.</p>"
            "<p>Where the building sits in a separate entity leasing to the operating "
            "company, the self-rental rules apply and produce an unhelpful asymmetry: net "
            "rental income is recharacterized as non-passive while a net rental loss "
            "generally stays passive. The grouping election resolves this by treating the "
            "rental and the operating business as one activity where they form an appropriate "
            "economic unit. That election needs to be made deliberately and documented, not "
            "discovered afterward.</p>"
        ),
        (
            "Route Two: Short-Term Rentals",
            "<p>An activity where the average period of customer use is seven days or less is "
            "not a rental activity under the Section 469 regulations. That sounds like a "
            "technicality and it is a significant one: the property escapes the automatic "
            "passive classification, so the owner needs only to materially participate to "
            "treat the losses as non-passive.</p>"
            "<p>Material participation is generally met through more than 500 hours in the "
            "activity, or by being substantially all of the participation by anyone, which is "
            "often achievable for a self-managed property. Critically, real estate "
            "professional status is not required, which is what makes this route available to "
            "a business owner who could never satisfy the REPS tests.</p>"
            "<p>The average stay is computed across the year, so a property with mostly short "
            "bookings and a few monthly stays can fail the test. Using a full-service "
            "management company also undermines material participation, because the hours "
            "belong to the manager.</p>"
        ),
        (
            "Route Three: Real Estate Professional Status",
            "<p>REPS under Section 469(c)(7) removes the automatic passive classification "
            "from all rental activities. It requires more than half of all personal services "
            "in trades or businesses to be in real property trades or businesses, plus more "
            "than 750 hours in them.</p>"
            "<p>A business owner working full time in their own company essentially cannot "
            "meet the more-than-half test. The practical route is a spouse who qualifies: the "
            "tests are applied per spouse, so one qualifying spouse is enough, and the benefit "
            "lands on the joint return where it can offset the other spouse's business "
            "income.</p>"
            "<p>This position is examined regularly and turns on contemporaneous "
            "documentation rather than on the underlying facts. Reconstructed logs routinely "
            "fail.</p>"
        ),
        (
            "Route Four: Generating Passive Income",
            "<p>The least discussed and sometimes the most practical. Suspended passive "
            "losses can offset passive income from any source, so an owner sitting on a large "
            "suspended balance can acquire passive income producing investments and free the "
            "losses.</p>"
            "<p>This suits an owner who already has substantial suspended losses from prior "
            "studies. It is a way of recovering value that has already been created rather "
            "than a reason to buy property, and the investment has to make sense on its own "
            "terms first.</p>"
        ),
        (
            "What Cost Segregation Contributes",
            "<p>Cost segregation is the engine behind most of these strategies. A study "
            "separates a building's cost into components and reassigns them from the default "
            "27.5 or 39-year schedules to their correct 5, 7, and 15-year classifications. "
            "With 100 percent bonus depreciation permanent under the OBBBA for property "
            "acquired after January 19, 2025, every reclassified dollar becomes immediately "
            "deductible.</p>"
            "<p>Typical reclassification runs 20 to 35 percent of depreciable basis for "
            "commercial property and 15 to 25 percent for residential rental. Short-term "
            "rentals often sit at the higher end because furnishings and finishes are "
            "substantial relative to the structure.</p>"
            "<p>The deduction is acceleration rather than creation. Basis claimed now is not "
            "available later, and depreciation recapture applies on sale, which is why a "
            "planned sale within two to three years usually argues against a study.</p>"
        ),
        (
            "The Combination That Works Most Often",
            "<p>For a business owner with high active income and no realistic path to REPS, "
            "the most common effective structure is a self-managed short-term rental combined "
            "with a cost segregation study.</p>"
            "<p>The short-term rental classification removes the automatic passive character, "
            "self-management establishes material participation, and the study produces a "
            "large first-year deduction that is consequently non-passive and available "
            "against business income.</p>"
            "<p>The requirements are specific and all of them matter: the average stay must "
            "be seven days or less measured across the year, the owner must materially "
            "participate with contemporaneous records, and full-service management generally "
            "defeats the participation test. Each condition is where these positions fail on "
            "examination.</p>"
        ),
        (
            "The Limits That Still Apply",
            "<p>Even where the passive problem is solved, two limits remain.</p>"
            "<p>The <strong>excess business loss limitation</strong> caps how much net "
            "business loss can offset non-business income in a year, with the excess carried "
            "forward. On very large studies this can spread the benefit across several years "
            "even when everything else is correct.</p>"
            "<p><strong>Basis and at-risk rules</strong> limit deductions to the amount the "
            "owner has invested and is economically at risk for. This is where entity "
            "structure matters: partnership rules include a share of entity debt in basis, "
            "while S-corp shareholders receive no basis from entity borrowings. Holding "
            "leveraged real estate in an S-corp routinely suspends losses for lack of basis, "
            "which is a structural error rather than a tax one.</p>"
        ),
        (
            "Where the 1031 Exchange Fits",
            "<p>A like-kind exchange under Section 1031 defers gain on the sale of "
            "investment or business real property when the proceeds are reinvested in "
            "replacement property within the statutory timeframes: 45 days to identify "
            "replacement property and 180 days to close.</p>"
            "<p>For a business owner, the exchange serves a different purpose from the "
            "strategies above. Cost segregation accelerates deductions against current "
            "income; a 1031 exchange defers the tax that would otherwise arrive on a sale, "
            "including the depreciation recapture that a cost segregation study makes larger. "
            "The two are complements rather than alternatives, and they interact directly: an "
            "owner who has taken large accelerated depreciation has more recapture exposure on "
            "sale, which strengthens the case for exchanging rather than selling outright.</p>"
            "<p>The constraints are real. The property must be held for investment or "
            "productive use in a trade or business, so a personal residence does not qualify "
            "and a property held primarily for resale does not either. The timeframes are "
            "strict and are not extended for ordinary difficulties in finding replacement "
            "property. And the proceeds must not be constructively received by the seller, "
            "which is why a qualified intermediary is engaged before closing rather than "
            "after.</p>"
        ),
        (
            "Sequencing a Real Estate Strategy",
            "<p>The order in which these decisions are made determines how much of the "
            "benefit survives.</p>"
            "<p>First, establish which route through the passive rules is available, because "
            "it determines whether any deduction is worth generating. Second, settle the "
            "holding structure, since entity choice governs whether debt creates basis and "
            "whether the property can be moved later without triggering gain. Third, make and "
            "document any grouping or aggregation election, because these are difficult to "
            "change once made. Only then commission the cost segregation study, and time it "
            "against the year with the most income to offset.</p>"
            "<p>Owners commonly run this in reverse: they buy a property, have a study done "
            "because it was offered, and then discover the loss is suspended and the "
            "structure is wrong. Every element of that sequence is recoverable, but the "
            "recovery costs more than the planning would have.</p>"
        ),
        (
            "The Augusta Rule, Briefly",
            "<p>Section 280A(g) permits renting a personal residence for up to fourteen days "
            "a year without the rental income being taxable. A business owner with an entity "
            "can have the business rent their home for legitimate meetings, producing a "
            "deduction to the business and untaxed income personally.</p>"
            "<p>It is legitimate and it is modest in scale relative to the strategies above. "
            "It requires genuine business use, contemporaneous documentation of what actually "
            "occurred at each meeting, and a rate supported by comparable local venue "
            "pricing. Undocumented use of it does not survive examination.</p>"
            "<p>The practical value is in treating it as one small, clean item within a "
            "larger plan rather than as a strategy in its own right. Owners who build a plan "
            "around it are usually being sold something; owners who add it to a plan already "
            "containing structure, plan design, and depreciation are simply collecting a "
            "provision that applies to them.</p>"
        ),
    ],
    takeaways=[
        "Passive activity rules, not the size of the deduction, decide whether a study is worth commissioning.",
        "Property used in your own business is the cleanest route, and the grouping election makes it work.",
        "Short-term rentals with an average stay of seven days or less are not rental activities under Section 469.",
        "REPS is generally unreachable for a busy owner but reachable through a qualifying spouse.",
        "Self-managed short-term rental plus cost segregation is the most common effective combination.",
        "Excess business loss and basis limits still apply even after the passive problem is solved.",
    ],
    faqs=[
        (
            "Can I use real estate losses to offset my business income?",
            "<p>Only through one of four routes: the property is used in your own trade or "
            "business, it is a short-term rental averaging seven days or less per stay where "
            "you materially participate, you or your spouse qualify as a real estate "
            "professional, or you have passive income for the losses to offset. Otherwise the "
            "losses are suspended and carried forward.</p>",
        ),
        (
            "What is the short-term rental loophole?",
            "<p>An activity where the average period of customer use is seven days or less is "
            "not a rental activity under the Section 469 regulations, so it escapes automatic "
            "passive classification. The owner then needs only to materially participate, not "
            "to qualify as a real estate professional, for the losses to be non-passive.</p>",
        ),
        (
            "Do I need real estate professional status?",
            "<p>Not for the short-term rental route or for property used in your own business. "
            "REPS matters for conventional long-term rentals, and a business owner working "
            "full time in their company generally cannot meet the more-than-half test. A "
            "qualifying spouse is the usual route, since the tests are applied per spouse.</p>",
        ),
        (
            "How much depreciation does cost segregation produce?",
            "<p>Typically 20 to 35 percent of depreciable basis for commercial property and "
            "15 to 25 percent for residential rental, all immediately deductible under "
            "permanent 100 percent bonus depreciation. On $1,500,000 of basis that is roughly "
            "$300,000 to $450,000 in the first year.</p>",
        ),
        (
            "What if I already have suspended passive losses?",
            "<p>They carry forward indefinitely and are freed when you have passive income, "
            "when the activity's classification changes, or when the property is sold in a "
            "fully taxable transaction. Acquiring passive income producing investments is a "
            "legitimate way to use a large suspended balance.</p>",
        ),
        (
            "Does a property manager affect my ability to use losses?",
            "<p>Substantially, on the short-term rental route. Material participation requires "
            "your own hours, and a full-service manager handling bookings, cleaning, and "
            "maintenance means those hours belong to them. Self-management is usually "
            "necessary for that strategy to work.</p>",
        ),
        (
            "Should real estate be held in my S-corp?",
            "<p>Generally no. S-corp shareholders receive no basis from entity-level debt, "
            "which suspends the very losses the property is held to generate, and "
            "distributing appreciated property out of a corporation triggers gain as though "
            "it were sold. A partnership or disregarded LLC is nearly always the correct "
            "holding structure.</p>",
        ),
    ],
    spokes=[
        Spoke(
            slug="short-term-rental-tax-loophole-offset-w2-income",
            label="How business owners use STR to offset $500K+ income",
            adopted=True,
        ),
        Spoke(
            slug=(
                "the-business-owners-guide-to-section-469-passive-activity-loss-rules-"
                "and-material-participation"
            ),
            label="Material participation for busy business owners",
            adopted=True,
        ),
        REPS_SPOUSE,
        Spoke(
            slug="cost-segregation-airbnb",
            label="Cost seg + STR: the $100K+ tax play",
            adopted=True,
        ),
        Spoke(
            slug="augusta-rule-for-business-owners-when-it-works-and-how-to-do-it-safely",
            label="Augusta Rule for business owners with entities",
            adopted=True,
        ),
        Spoke(
            slug="the-business-owners-guide-to-section-1031-like-kind-exchanges-and-deferral-strategy",
            label="1031 exchange strategy for business owners",
            adopted=True,
        ),
    ],
)
