#!/usr/bin/env python3
"""Cluster 2: High income tax strategy for $500K-$1M business owners."""

from __future__ import annotations

from cluster_common import Cluster, Spoke

P = "high-income-tax-strategy"

PLANNING_500K = Spoke(
    slug="tax-planning-500k-1m-business-owners",
    label="Tax planning for $500K-$1M business owners",
    title="Tax Planning for $500K to $1M Business Owners: What Actually Applies",
    description=(
        "The strategies that matter at $500,000 to $1,000,000 of business profit, and "
        "the ones that get sold to this income band but do not survive scrutiny."
    ),
    h1="Tax Planning for $500K to $1M Business Owners",
    subtitle=(
        "This income band has its own playbook. It is not the small business "
        "checklist, and it is not the ultra-high-net-worth toolkit either."
    ),
    lead=(
        "Tax planning at $500,000 to $1,000,000 of business profit occupies a specific "
        "band: high enough that the owner is past the phase-outs and deep into the top "
        "marginal brackets, but not so high that the private-placement and family-office "
        "structures marketed to much larger balance sheets are appropriate. The strategies "
        "that work here are entity structure, retirement plan design, depreciation timing, "
        "and state-level elections, applied in that order."
    ),
    keywords=[
        "tax planning 500k business owner",
        "high income business owner tax strategy",
        "tax strategy 1 million profit",
    ],
    body=[
        (
            "Why This Band Is Different",
            "<p>Below roughly $250,000 of profit, most of the available planning is "
            "mechanical: elect S status when it clears the cost, fund a retirement plan, "
            "keep clean books. The dollar amounts do not justify complexity.</p>"
            "<p>Above roughly $5,000,000, a different toolkit opens: private placement "
            "insurance, complex trust structures, opportunity zone funds sized to matter, "
            "and dedicated family office infrastructure. Those structures carry fixed costs "
            "that only amortize at scale.</p>"
            "<p>The $500,000 to $1,000,000 band sits between them, and it is the most "
            "commonly misserved. Owners here are routinely handed the small business "
            "checklist by a compliance-oriented CPA, or sold structures that were designed "
            "for balance sheets ten times larger. Neither fits.</p>"
        ),
        (
            "What Actually Applies, In Order",
            "<p>Four categories account for the overwhelming majority of legitimate savings "
            "at this level, and they should be worked in sequence because each affects the "
            "next.</p>"
            "<p><strong>1. Entity structure.</strong> Whether profit is exposed to "
            "self-employment tax, whether a second entity should hold equipment or real "
            "estate, and whether a C-corp has a role for retained earnings. Structure "
            "decisions constrain everything downstream, so they come first.</p>"
            "<p><strong>2. Retirement plan design.</strong> This is the single largest "
            "deduction available to most owners in this band. A solo 401(k) alone reaches a "
            "meaningful figure; paired with a cash balance plan, an owner in their fifties "
            "can often deduct $150,000 to $250,000 a year. Nothing else on this list "
            "produces a deduction of that size from ordinary operations.</p>"
            "<p><strong>3. Depreciation timing.</strong> With 100 percent bonus depreciation "
            "permanent under the OBBBA for property acquired after January 19, 2025, "
            "equipment purchases and cost segregation studies on owned real estate convert "
            "into immediate deductions rather than deductions spread over decades.</p>"
            "<p><strong>4. State-level elections.</strong> The pass-through entity tax "
            "election, available in most states, moves state income tax to the entity where "
            "it is federally deductible. For an owner in a high-tax state this is often the "
            "highest-return item on the list relative to the effort it takes.</p>"
        ),
        (
            "The Retirement Plan Is Usually the Largest Single Move",
            "<p>Owners in this band consistently underuse retirement plans, generally "
            "because they are thinking of the contribution limits that apply to employees "
            "rather than the limits available to an owner who controls the plan design.</p>"
            "<p>A solo 401(k) combines an employee deferral with an employer contribution "
            "based on compensation. A defined benefit or cash balance plan layered on top is "
            "sized actuarially by the benefit it must fund at retirement, which means an "
            "older owner with fewer years to fund it can contribute dramatically more. That "
            "age sensitivity is why two owners with identical profit can have very different "
            "deduction capacity.</p>"
            "<p>The constraint is employees. A plan covering a staff has nondiscrimination "
            "requirements, and the cost of the contributions owed to employees has to be "
            "modeled against the owner's benefit. That modeling is the work, and it is "
            "exactly what does not happen in a compliance-only relationship.</p>"
        ),
        (
            "What Gets Sold to This Band and Should Not Be Bought",
            "<p>The $500,000 to $1,000,000 owner is a target market for arrangements that "
            "range from aggressive to listed transactions. Recurring examples:</p>"
            "<ul>"
            "<li><strong>Syndicated conservation easements.</strong> Listed transactions, "
            "aggressively litigated, with penalty exposure that survives the deduction being "
            "disallowed.</li>"
            "<li><strong>Micro-captive insurance arrangements.</strong> Legitimate captives "
            "exist and serve real risk-management purposes. The promoted versions sold "
            "primarily as deductions have been repeatedly disallowed and carry disclosure "
            "obligations.</li>"
            "<li><strong>Cash-value life insurance sold as a tax strategy.</strong> The "
            "product may be sound; the tax case for it at this income level frequently is "
            "not, and the commission structure rarely gets disclosed alongside the "
            "projection.</li>"
            "<li><strong>Offshore structures.</strong> For a domestic operating business "
            "with domestic customers, these create reporting obligations and exposure "
            "without a defensible benefit.</li>"
            "</ul>"
            "<p>A useful filter: if the arrangement's primary economic purpose is the "
            "deduction itself, and it would make no sense without the tax benefit, it "
            "deserves a much higher standard of proof than it is usually given.</p>"
        ),
        (
            "The Effective Rate Worth Targeting",
            "<p>Owners at this level frequently arrive with a combined federal and state "
            "effective rate in the low-to-mid thirties. With entity structure, a properly "
            "sized retirement plan, depreciation timing, and a PTET election working "
            "together, the mid-twenties is a realistic target for many operating "
            "businesses, and the low twenties is achievable where real estate is part of the "
            "picture.</p>"
            "<p>What makes that credible is that no single item produces it. It is four or "
            "five moves of moderate size, sequenced so they do not undercut each other, "
            "which is a fundamentally different exercise from hunting for one large "
            "deduction.</p>"
        ),
    ],
    takeaways=[
        "This income band needs its own playbook, not the small business checklist or the family office toolkit.",
        "Work the order: entity structure, retirement plan design, depreciation timing, then state elections.",
        "A cash balance plan layered on a solo 401(k) is usually the largest single deduction available.",
        "Treat any arrangement whose main economic purpose is its own deduction with heavy skepticism.",
        "A mid-twenties effective rate is realistic, but it comes from several moves, not one.",
    ],
    faqs=[
        (
            "What is a realistic effective tax rate at $500K to $1M of profit?",
            "<p>Most owners arrive in the low-to-mid thirties combined federal and state. "
            "With entity structure, a properly sized retirement plan, depreciation timing, "
            "and a state PTET election working together, the mid-twenties is realistic for "
            "an operating business, and the low twenties is reachable where real estate is "
            "involved.</p>",
        ),
        (
            "What is the biggest single deduction available at this income level?",
            "<p>For most owners it is retirement plan design, specifically a cash balance or "
            "defined benefit plan layered on top of a solo 401(k). Depending on age and "
            "compensation this can reach $150,000 to $250,000 annually, which is larger than "
            "anything else generated from ordinary operations.</p>",
        ),
        (
            "Is a C-corp worth considering at this profit level?",
            "<p>Only where earnings are genuinely being retained to fund growth rather than "
            "distributed. The 21 percent corporate rate applies to retained income, but "
            "distributing it later triggers a second layer of tax. A C-corp used as a "
            "management company alongside a pass-through can make sense; a full conversion "
            "usually does not.</p>",
        ),
        (
            "How much should tax planning cost at this level?",
            "<p>A full advisory engagement at this profit level is typically a flat fee in "
            "the several-thousand-dollar range, quoted before work begins. Our advisory "
            "engagement is $7,800. The relevant test is the ratio: an engagement that "
            "identifies $60,000 of annual savings against a $7,800 fee is a different "
            "proposition from an hourly compliance relationship that identifies none.</p>",
        ),
    ],
)

BELOW_20 = Spoke(
    slug="cut-effective-tax-rate-below-20-percent",
    label="How business owners cut their effective rate below 20%",
    title="How Business Owners Cut Their Effective Tax Rate Below 20%",
    description=(
        "The specific combination of entity structure, retirement plans, depreciation, "
        "and state elections that moves a profitable business owner under a 20% rate."
    ),
    h1="How Business Owners Cut Their Effective Rate Below 20%",
    subtitle=(
        "It is never one deduction. It is four or five moves that stack without "
        "undercutting each other."
    ),
    lead=(
        "An effective tax rate is total tax divided by total income, which is always lower "
        "than the marginal rate on the last dollar earned. Moving a profitable business "
        "owner below 20 percent combined generally requires four things working together: "
        "an entity structure that limits payroll tax, a retirement plan sized to the owner's "
        "age, depreciation deployed against real property, and a state pass-through entity "
        "tax election."
    ),
    keywords=[
        "lower effective tax rate business owner",
        "effective tax rate below 20 percent",
        "reduce effective tax rate high income",
    ],
    body=[
        (
            "Effective Rate Versus Marginal Rate",
            "<p>These get conflated constantly and the difference matters for goal-setting. "
            "The marginal rate is what applies to the next dollar. The effective rate is "
            "total tax divided by total income, and it is always lower because the earlier "
            "dollars were taxed in lower brackets.</p>"
            "<p>An owner in the 37 percent bracket is not paying 37 percent of their income. "
            "Before any planning, their federal effective rate might be 28 percent, with "
            "state and payroll tax on top. Planning works on the effective rate, and quoting "
            "a marginal rate as though it were the actual burden produces both bad targets "
            "and bad decisions.</p>"
        ),
        (
            "Move One: Structure Out the Payroll Tax",
            "<p>For an owner-operated business, an S election limits Social Security and "
            "Medicare tax to the wages paid rather than the entire profit. At this income "
            "level, with the Social Security wage base already cleared, the saving is the "
            "Medicare component, roughly 3.8 percent including the additional tax, on the "
            "profit taken as distribution.</p>"
            "<p>On $500,000 of distribution that is around $19,000. Against $800,000 of "
            "total income it moves the effective rate by roughly two and a half points. Real, "
            "but on its own nowhere near the target.</p>"
        ),
        (
            "Move Two: Size the Retirement Plan to the Owner's Age",
            "<p>This is the heaviest lever. A solo 401(k) alone is useful. A cash balance "
            "plan stacked on top is sized actuarially by what must be funded by retirement, "
            "so the contribution capacity rises sharply with age.</p>"
            "<p>An owner at 52 can frequently deduct $150,000 to $250,000 across the "
            "combined structure. Against $800,000 of income, a $200,000 deduction moves the "
            "effective rate by six to eight points by itself. Nothing else available from "
            "ordinary operations comes close.</p>"
            "<p>The money is deferred rather than eliminated, and it is taxed on "
            "distribution. That still wins where the deduction comes off at 37 percent and "
            "distributions later occur in a lower bracket, and it wins on the compounding of "
            "amounts that were never taxed in the first place.</p>"
        ),
        (
            "Move Three: Put Depreciation Against Real Property",
            "<p>With 100 percent bonus depreciation permanent under the OBBBA for property "
            "acquired after January 19, 2025, a cost segregation study on a building the "
            "owner already holds converts what would have been decades of straight-line "
            "depreciation into an immediate deduction.</p>"
            "<p>On a $1,500,000 commercial building, a study typically reclassifies 20 to 30 "
            "percent of basis into shorter-lived categories, producing a first-year "
            "deduction in the $300,000 to $450,000 range. The critical constraint is whether "
            "the loss can be used: passive activity rules generally prevent rental losses "
            "from offsetting business income unless the owner qualifies as a real estate "
            "professional, materially participates in a short-term rental, or the property "
            "is used in the owner's own trade or business.</p>"
            "<p>That constraint is where most of the value is won or lost, and it is why "
            "this move has to be planned rather than discovered in March.</p>"
        ),
        (
            "Move Four: Elect the State Pass-Through Entity Tax",
            "<p>Most states now permit a pass-through entity to pay state income tax at the "
            "entity level, where it is deductible federally, rather than at the individual "
            "level where the state and local tax deduction is limited.</p>"
            "<p>For an owner in a state with a 5 to 9 percent income tax, this converts a "
            "largely non-deductible expense into a fully deductible one. On $700,000 of "
            "income in a 6 percent state, that is $42,000 of state tax becoming deductible, "
            "worth roughly $15,000 federally. It requires an election, usually annually, and "
            "it is among the most frequently missed items on returns we review.</p>"
        ),
        (
            "How It Stacks",
            "<p>Take an owner with $850,000 of profit, age 52, in a 6 percent state, who "
            "owns their commercial building.</p>"
            "<ul>"
            "<li>S-corp structure: roughly $19,000 of payroll tax avoided.</li>"
            "<li>Solo 401(k) plus cash balance plan: roughly $200,000 deducted.</li>"
            "<li>Cost segregation on the owner-occupied building: a first-year deduction "
            "usable against business income because the property is used in the trade or "
            "business.</li>"
            "<li>PTET election: state tax made federally deductible.</li>"
            "</ul>"
            "<p>Each move is ordinary. None is aggressive. Sequenced together they take a "
            "low-thirties effective rate into the high teens or low twenties, and the result "
            "comes from stacking rather than from any single item.</p>"
        ),
    ],
    takeaways=[
        "Effective rate and marginal rate are different numbers; plan against the effective rate.",
        "Retirement plan design is the heaviest single lever, and its capacity rises with the owner's age.",
        "Cost segregation only helps if the resulting loss is actually usable against the income you have.",
        "The PTET election is among the most commonly missed items on high income returns.",
        "Sub-20 percent comes from four moderate moves stacking, never from one large deduction.",
    ],
    faqs=[
        (
            "Is a sub-20% effective rate realistic for a business owner?",
            "<p>For an operating business owner with real estate in the picture and a "
            "properly sized retirement plan, yes. For a service business owner with no "
            "property and no retirement plan capacity, the mid-twenties is a more realistic "
            "floor. The answer depends heavily on age, state, and whether depreciation has "
            "anything to attach to.</p>",
        ),
        (
            "Does deferring tax through a retirement plan really help?",
            "<p>It helps when the deduction comes off at a high marginal rate and "
            "distributions later occur at a lower one, and it helps through compounding on "
            "amounts that were never taxed. It helps less if the owner expects to be in the "
            "same bracket in retirement, which is why plan design should be modeled rather "
            "than assumed.</p>",
        ),
        (
            "Why can't I use my rental losses against my business income?",
            "<p>Rental activity is passive by default under Section 469, and passive losses "
            "generally offset only passive income. The common exceptions are qualifying as a "
            "real estate professional, materially participating in a short-term rental where "
            "the average stay is seven days or less, or holding property used in your own "
            "trade or business.</p>",
        ),
        (
            "How long does it take to move an effective rate?",
            "<p>State elections and retirement plan contributions can affect the current "
            "year if handled before the relevant deadlines. Entity changes usually take "
            "effect the following tax year. Cost segregation can reach back to prior years "
            "through a Form 3115 catch-up without amending returns.</p>",
        ),
    ],
)

PLAYBOOK = Spoke(
    slug="500k-business-owner-tax-playbook",
    label="The $500K business owner tax playbook",
    title="The $500K Business Owner Tax Playbook: A Year-One Sequence",
    description=(
        "A concrete twelve-month sequence for a business owner crossing $500,000 in "
        "profit, from entity review through year-end execution."
    ),
    h1="The $500K Business Owner Tax Playbook",
    subtitle="What to do, in what order, across the first full year of real planning.",
    lead=(
        "Crossing $500,000 in profit changes which tax strategies are worth their "
        "complexity. This playbook sets out the sequence we work with new clients at this "
        "level: structure first, because it constrains everything else; then retirement "
        "plan design, because it is the largest deduction; then depreciation and state "
        "elections, because they depend on the first two being settled."
    ),
    keywords=[
        "500k business owner tax playbook",
        "tax strategy checklist business owner",
        "business owner tax planning sequence",
    ],
    body=[
        (
            "Phase One: Establish the Baseline (Weeks 1-3)",
            "<p>No decision gets made before the current position is measured. That means "
            "the last three years of business and personal returns read together, the "
            "current effective rate calculated rather than estimated, the entity structure "
            "and its elections confirmed, and existing retirement plans and their unused "
            "capacity documented.</p>"
            "<p>The three-year lookback is not a formality. It is where prior-year errors "
            "surface: missed depreciation, unclaimed credits, an S election that was never "
            "properly filed, a PTET election available and never made. Recoverable amounts "
            "frequently exceed the first year of forward planning, and they are recoverable "
            "through amended returns or a Form 3115 catch-up.</p>"
        ),
        (
            "Phase Two: Settle the Structure (Weeks 3-6)",
            "<p>Structure comes before everything because it determines the inputs to "
            "everything. The questions to close:</p>"
            "<ul>"
            "<li>Is the operating entity taxed correctly for its profit level and owner "
            "involvement?</li>"
            "<li>If an S-corp, is there a documented reasonable compensation file, or a "
            "number nobody can derive?</li>"
            "<li>Should real estate or equipment sit in a separate entity?</li>"
            "<li>Is there a role for a C-corp management company for retained earnings and "
            "fringe benefits?</li>"
            "<li>Does the operating agreement conflict with the tax election in place?</li>"
            "</ul>"
            "<p>Entity changes generally take effect the following tax year, so decisions "
            "made here are being made for next year, not this one. That is precisely why "
            "they come first.</p>"
        ),
        (
            "Phase Three: Design the Retirement Plan (Weeks 6-10)",
            "<p>This is the largest deduction most owners at this level will ever access, "
            "and it has a hard installation deadline, so it gets its own phase.</p>"
            "<p>The work is an actuarial study modeling the owner's age, compensation, and "
            "employee census against several plan designs; the required employee "
            "contributions under each; a comparison of solo 401(k) alone against a paired "
            "cash balance plan; and confirmation of installation deadlines, which differ by "
            "plan type and can fall before year-end.</p>"
            "<p>Missing the installation deadline forfeits the entire year's deduction. It "
            "is the single most expensive deadline on this list.</p>"
        ),
        (
            "Phase Four: Deploy Depreciation (Weeks 10-16)",
            "<p>With the structure settled and the plan installed, depreciation gets placed "
            "where it can actually be used:</p>"
            "<ul>"
            "<li>A cost segregation study on any owned commercial or rental property, "
            "including property acquired in earlier years, which can be caught up through "
            "Form 3115 without amending.</li>"
            "<li>Equipment and vehicle purchases timed against 100 percent bonus "
            "depreciation, permanent under the OBBBA for property acquired after January 19, "
            "2025.</li>"
            "<li>A usability analysis before anything is commissioned: if passive activity "
            "rules will suspend the loss, the deduction has been bought and cannot be "
            "spent.</li>"
            "</ul>"
        ),
        (
            "What Each Phase Should Produce in Writing",
            "<p>A useful check on whether the sequence is actually being followed is whether "
            "each phase leaves a document behind. Planning that produces only conversations "
            "tends to evaporate when the year gets busy.</p>"
            "<ul>"
            "<li><strong>Phase one:</strong> a written baseline with the current effective "
            "rate, and a schedule of recoverable prior-year amounts with the route to recover "
            "each.</li>"
            "<li><strong>Phase two:</strong> an entity comparison modeled over several years, "
            "and a reasonable compensation analysis with its market data and derivation.</li>"
            "<li><strong>Phase three:</strong> an actuarial study comparing plan designs, with "
            "the employee cost of each quantified.</li>"
            "<li><strong>Phase four:</strong> a depreciation analysis that states explicitly "
            "whether the loss will be usable, before any study is commissioned.</li>"
            "<li><strong>Phase five:</strong> a dated calendar of elections, deadlines, and "
            "revised estimated payments.</li>"
            "</ul>"
            "<p>If a phase produced no document, it is worth asking whether it was actually "
            "performed or merely discussed.</p>"
        ),
        (
            "Phase Five: State Elections and Year-End (Weeks 16-52)",
            "<p>The remainder of the year is election deadlines and execution. The PTET "
            "election where the state offers one, with attention to its specific deadline "
            "and estimated payment requirements. Multi-state apportionment if the business "
            "operates across lines. An accountable plan adopted and actually used. Quarterly "
            "estimates recalculated against the new position rather than last year's safe "
            "harbor.</p>"
            "<p>Then a year-end review in November, early enough that anything requiring "
            "action still has runway. A December review is a report, not a plan.</p>"
        ),
    ],
    takeaways=[
        "Measure the baseline before deciding anything; the three-year lookback often funds the engagement.",
        "Structure decisions come first because they set the inputs for every later move.",
        "Retirement plan installation deadlines are unforgiving and can fall before year-end.",
        "Confirm a depreciation loss will be usable before commissioning the study that creates it.",
        "Run the year-end review in November; a December review is a report, not a plan.",
    ],
    faqs=[
        (
            "How long before tax planning shows results?",
            "<p>State elections and retirement contributions can affect the current year if "
            "handled before their deadlines. Entity changes usually take effect the "
            "following year. Prior-year recovery through amended returns or a Form 3115 "
            "catch-up can produce refunds within months of filing.</p>",
        ),
        (
            "What if I am mid-year when I start?",
            "<p>Most of the sequence still applies. Retirement plan installation and state "
            "elections often remain available depending on the deadline, and the three-year "
            "lookback is unaffected by where you are in the year. Entity changes shift to "
            "the following year, which they usually would have anyway.</p>",
        ),
        (
            "Do I need to change CPAs to do this?",
            "<p>Not necessarily. Planning and compliance are different functions and can sit "
            "with different firms. Many owners keep an existing preparer for filing and add "
            "an advisory relationship for the planning work. What does not work is assuming "
            "a compliance engagement includes planning it was never scoped to deliver.</p>",
        ),
        (
            "What does this engagement cost?",
            "<p>Our advisory engagement is $7,800, quoted flat before work begins, with cost "
            "segregation studies priced separately at $1 per square foot subject to a $2,000 "
            "minimum. Amended returns are $2,500 each. Fees are quoted in writing rather "
            "than billed hourly.</p>",
        ),
    ],
)

NOT_RECOMMENDED = Spoke(
    slug="tax-strategies-most-cpas-dont-recommend",
    label="Tax strategies most CPAs don't recommend",
    title="Tax Strategies Most CPAs Don't Recommend (And Why)",
    description=(
        "Legitimate strategies that rarely surface in a compliance relationship, the "
        "structural reasons they get skipped, and which ones deserve the skepticism."
    ),
    h1="Tax Strategies Most CPAs Don't Recommend",
    subtitle=(
        "Some are skipped because the engagement was never scoped for them. Others "
        "are skipped for good reason."
    ),
    lead=(
        "Most CPAs are engaged to prepare returns, not to design tax positions. A return "
        "preparation engagement is scoped to report last year accurately and on time, which "
        "is a backward-looking exercise. Several entirely legitimate strategies require a "
        "decision to be made before the year ends, so they fall outside that scope by "
        "construction rather than by judgment."
    ),
    keywords=[
        "tax strategies cpas dont recommend",
        "advanced tax strategies business owners",
        "tax planning vs preparation strategies",
    ],
    body=[
        (
            "The Structural Reason, Not a Conspiracy",
            "<p>This is not about competence or willingness. It is about scope and timing. A "
            "preparer receives the year's records after the year has closed and reports what "
            "happened. By then, the retirement plan was either installed or it was not, the "
            "PTET election was either made or missed, the equipment was either placed in "
            "service or it was not.</p>"
            "<p>Compounding this, most preparers are paid per return and are capacity-bound "
            "between January and April. Planning work requires modeling in the third quarter, "
            "which is a different service with a different economic model. Firms that do not "
            "sell that service do not staff for it.</p>"
        ),
        (
            "Legitimate and Routinely Missed",
            "<p><strong>Cash balance plans.</strong> The largest deduction available to most "
            "profitable owners, and the one least often raised, because it requires an "
            "actuary, a plan document, and a decision before an installation deadline. A "
            "preparer has no natural moment to introduce it.</p>"
            "<p><strong>Form 3115 depreciation catch-up.</strong> Missed depreciation from "
            "prior years can be claimed in the current year through an accounting method "
            "change, with no amended returns required. It is a well-established procedure "
            "that goes unused because nobody reviewed the fixed asset schedule against what "
            "should have been claimed.</p>"
            "<p><strong>The PTET election.</strong> Available in most states, worth real "
            "money to anyone in a high-tax state, and frequently missed because it is a "
            "separate election with its own deadline and estimated payment rules.</p>"
            "<p><strong>Cost segregation on modest properties.</strong> Widely assumed to be "
            "worthwhile only above several million dollars of basis. At current study "
            "pricing the economics work well below that, particularly with 100 percent bonus "
            "depreciation permanent.</p>"
            "<p><strong>Accountable plans.</strong> A short written policy that converts "
            "otherwise non-deductible owner expenses into deductible reimbursements. Cheap, "
            "durable, and routinely absent.</p>"
            "<p><strong>The Augusta rule.</strong> Section 280A(g) permits renting a personal "
            "residence to the business for up to fourteen days a year without the rental "
            "income being taxable. It requires genuine business use, documented meetings, and "
            "a defensible market rate, which is why it is skipped, but it is legitimate when "
            "done properly.</p>"
        ),
        (
            "Skipped for Good Reason",
            "<p>Not everything absent from your return is an oversight. Several arrangements "
            "marketed to profitable owners deserve exactly the skepticism they get:</p>"
            "<ul>"
            "<li><strong>Syndicated conservation easements.</strong> Listed transactions with "
            "sustained IRS enforcement and penalty exposure that outlives the disallowed "
            "deduction.</li>"
            "<li><strong>Promoted micro-captives.</strong> A genuine captive insuring genuine "
            "risk is legitimate. A captive sold primarily as a deduction has repeatedly "
            "failed in court and carries disclosure obligations.</li>"
            "<li><strong>Aggressive management fee arrangements.</strong> Fees between "
            "related entities must reflect real services at arm's length rates. Fees set to "
            "move income rather than to pay for work do not survive examination.</li>"
            "<li><strong>Charitable remainder structures sold as tax plays.</strong> Sound "
            "for genuine charitable intent, poor economics when the deduction is the "
            "motive.</li>"
            "</ul>"
        ),
        (
            "How to Tell the Difference",
            "<p>Four questions separate the two lists reliably:</p>"
            "<ol>"
            "<li>Would this arrangement make economic sense if the tax benefit disappeared? "
            "A cash balance plan still funds a retirement. A syndicated easement does not "
            "survive the question.</li>"
            "<li>Is it a specific, identifiable provision, or a structure assembled to "
            "produce a result the code does not directly provide?</li>"
            "<li>Is it a listed or reportable transaction? That status is published, and it "
            "is a definitive answer.</li>"
            "<li>Who is paid, and how? A strategy sold by the party earning a commission on "
            "the product deserves independent review before it is implemented.</li>"
            "</ol>"
        ),
    ],
    takeaways=[
        "Strategies get missed because return preparation is scoped backward, not because of incompetence.",
        "Cash balance plans, Form 3115 catch-ups, and PTET elections are the most commonly missed legitimate moves.",
        "Listed transactions such as syndicated easements are skipped for sound reasons.",
        "If an arrangement makes no economic sense without its deduction, hold it to a much higher standard.",
        "Always ask who is being paid and how before implementing a strategy that was sold to you.",
    ],
    faqs=[
        (
            "Why didn't my CPA tell me about a cash balance plan?",
            "<p>Most commonly because the engagement was scoped to prepare returns, and the "
            "plan requires an actuarial study and installation before a deadline that falls "
            "long before filing. It is a planning service rather than a compliance one, and "
            "firms that do not sell planning do not staff for it.</p>",
        ),
        (
            "Is the Augusta rule legitimate?",
            "<p>Yes. Section 280A(g) allows a personal residence to be rented for up to "
            "fourteen days a year without the rental income being taxable. It requires "
            "genuine business use, contemporaneous documentation of what occurred, and a "
            "market rate supported by comparable local rates. Undocumented use of it does not "
            "survive examination.</p>",
        ),
        (
            "Should I be worried about aggressive strategies on my return?",
            "<p>Worth reviewing, particularly anything involving conservation easements, "
            "captive insurance, or offshore entities. Reportable and listed transaction "
            "status is published by the IRS, and disclosure obligations attach independently "
            "of whether the deduction survives.</p>",
        ),
        (
            "Can I claim missed depreciation from prior years?",
            "<p>Generally yes, through a Form 3115 accounting method change, which allows the "
            "cumulative catch-up to be claimed in the current year without amending prior "
            "returns. This is a common route to recovering value from a cost segregation "
            "study on a property acquired several years ago.</p>",
        ),
    ],
)

YEAR_END = Spoke(
    slug="year-end-tax-moves-profitable-businesses",
    label="Year-end tax moves for profitable businesses",
    title="Year-End Tax Moves for Profitable Businesses: The November Checklist",
    description=(
        "The year-end moves that still work in Q4 for a business with real profit, "
        "ordered by deadline, and the ones that had to happen earlier."
    ),
    h1="Year-End Tax Moves for Profitable Businesses",
    subtitle=(
        "Some moves close on December 31. Several close earlier. Running this in "
        "November is what makes it a plan."
    ),
    lead=(
        "Year-end tax planning for a profitable business is the process of taking actions "
        "before the tax year closes that change what the return will report. It is "
        "constrained by the calendar: some items remain available through December 31, "
        "several close earlier, and a few required action in the first half of the year. "
        "Running the review in November rather than December is what separates a plan from "
        "a report."
    ),
    keywords=[
        "year end tax planning business",
        "year end tax moves profitable business",
        "q4 tax planning business owner",
    ],
    body=[
        (
            "Start in November, Not December",
            "<p>Several of the highest-value year-end items need lead time that a late "
            "December review does not leave. An actuarial study for a cash balance plan takes "
            "weeks. Equipment must be placed in service, not merely ordered. A cost "
            "segregation study needs a site visit and a report. A PTET election may require "
            "an estimated payment by a specific date.</p>"
            "<p>By late December the list of available moves has narrowed to the few that "
            "can be executed in days. Most of the value has already closed.</p>"
        ),
        (
            "Moves With Deadlines Before December 31",
            "<p><strong>Retirement plan installation.</strong> A new defined benefit or cash "
            "balance plan generally must be established before the end of the plan year to "
            "generate a deduction for that year. Missing this forfeits the largest single "
            "deduction on the list, with no remedy.</p>"
            "<p><strong>PTET elections and payments.</strong> State rules vary widely, and "
            "several require an election and an estimated payment during the tax year rather "
            "than at filing. A missed payment date can invalidate the election entirely.</p>"
            "<p><strong>Placing property in service.</strong> Bonus depreciation requires "
            "the asset to be placed in service, meaning ready and available for its intended "
            "use, not merely purchased or delivered. Equipment sitting in a crate on December "
            "31 does not qualify.</p>"
        ),
        (
            "Moves Available Through December 31",
            "<p><strong>Equipment and vehicle purchases.</strong> With 100 percent bonus "
            "depreciation permanent under the OBBBA for property acquired after January 19, "
            "2025, qualifying purchases placed in service before year-end are fully "
            "deductible. Vehicles have their own weight and use rules that need checking "
            "before relying on the deduction.</p>"
            "<p><strong>Timing income and expenses.</strong> A cash-basis business can "
            "defer December invoicing into January or prepay deductible expenses before "
            "year-end. Useful at the margin, and worth checking against next year's expected "
            "position rather than applied reflexively.</p>"
            "<p><strong>Bonuses and reasonable compensation true-ups.</strong> Where the "
            "compensation figure has drifted from the documented analysis, year-end is when "
            "it gets corrected.</p>"
            "<p><strong>Charitable contributions.</strong> Including appreciated securities, "
            "which avoid the capital gain while generally deducting at fair market value, and "
            "donor advised funds where the deduction is wanted this year but the grants are "
            "not yet decided.</p>"
            "<p><strong>Harvesting capital losses.</strong> Against realized gains, watching "
            "the wash sale rules on repurchase.</p>"
        ),
        (
            "Moves Still Available After Year-End",
            "<p>A short list survives into the following year and is worth knowing so it is "
            "not rushed in December:</p>"
            "<ul>"
            "<li>Solo 401(k) employer contributions, generally fundable up to the extended "
            "filing deadline.</li>"
            "<li>SEP IRA contributions, on a similar timeline.</li>"
            "<li>Form 3115 depreciation catch-ups, which can be filed with the current year "
            "return to recover prior-year amounts.</li>"
            "<li>A cost segregation study on a property already placed in service, whose "
            "benefit can be caught up rather than lost.</li>"
            "</ul>"
        ),
        (
            "The Review Itself",
            "<p>A useful November review projects full-year profit against the last "
            "quarter's actuals, recalculates the effective rate on that projection, confirms "
            "every election deadline still open, reconciles the retirement plan funded to "
            "date against its capacity, and tests whether any depreciation being contemplated "
            "will actually be usable given passive activity constraints.</p>"
            "<p>It ends with a dated list of actions and deadlines, not a summary. The output "
            "of a planning review is decisions with dates attached.</p>"
        ),
    ],
    takeaways=[
        "Run the review in November; by late December most high-value moves have already closed.",
        "New defined benefit and cash balance plans generally must be installed before year-end.",
        "Property must be placed in service, not merely purchased, to earn bonus depreciation.",
        "Solo 401(k) employer contributions and Form 3115 catch-ups survive past December 31.",
        "The output of a real review is dated decisions, not a summary of the year.",
    ],
    faqs=[
        (
            "When is the deadline to set up a retirement plan for this tax year?",
            "<p>It depends on the plan. A new defined benefit or cash balance plan generally "
            "must be established before the plan year ends. Solo 401(k) rules differ between "
            "the employee deferral and the employer contribution, with the employer portion "
            "generally fundable up to the extended filing deadline. Confirm the specific "
            "deadline for your plan type well before December.</p>",
        ),
        (
            "Does buying equipment in December still work?",
            "<p>Only if it is placed in service by December 31, meaning ready and available "
            "for its intended use. Ordering, paying for, or taking delivery of equipment is "
            "not sufficient. Equipment still in its packaging on December 31 does not "
            "qualify for that year.</p>",
        ),
        (
            "Is deferring income into next year worth doing?",
            "<p>Sometimes, and it should be checked rather than assumed. Deferring helps if "
            "next year's rate will be lower or equal. If the business is growing into a "
            "higher bracket, deferral moves income into a worse year. It is a timing decision "
            "that requires a projection, not a default.</p>",
        ),
        (
            "What if I have already missed the year-end deadlines?",
            "<p>Several routes remain: employer retirement contributions up to the extended "
            "deadline, Form 3115 catch-ups for missed depreciation, and cost segregation on "
            "property already in service. Prior-year errors can also be recovered through "
            "amended returns, which is where a three-year lookback often pays for itself.</p>",
        ),
    ],
)

COMPLIANCE_VS_STRATEGY = Spoke(
    slug="tax-compliance-vs-tax-strategy",
    label="The difference between tax compliance and tax strategy",
    title="Tax Compliance vs Tax Strategy: What Separates Them",
    description=(
        "Compliance reports what happened. Strategy changes what happens. Why the two "
        "are different engagements and what each is actually scoped to deliver."
    ),
    h1="Tax Compliance vs Tax Strategy",
    subtitle=(
        "One is backward-looking and mandatory. The other is forward-looking and "
        "optional. Most owners are buying the first and expecting the second."
    ),
    lead=(
        "Tax compliance is the accurate, timely reporting of transactions that have already "
        "occurred. Tax strategy is the design of those transactions before they occur so "
        "that the reported result is different. They run on opposite timelines, require "
        "different skills, and are priced on different models, which is why a compliance "
        "engagement does not produce strategy no matter how well it is performed."
    ),
    keywords=[
        "tax compliance vs tax strategy",
        "tax planning vs tax preparation difference",
        "what is tax strategy business owner",
    ],
    body=[
        (
            "The Timeline Is the Whole Difference",
            "<p>Compliance operates on closed facts. The year has ended, the transactions "
            "occurred, and the work is to report them correctly. Skill here means accuracy, "
            "completeness, and defensibility. A well-prepared return is genuinely valuable "
            "and it is not optional.</p>"
            "<p>Strategy operates on open facts. The decision has not been made, so it can "
            "still be shaped. Should this entity elect S status? Should this plan be "
            "installed before year-end? Should this building be studied before it is "
            "refinanced? Once the year closes, every one of those questions has been answered "
            "by default.</p>"
            "<p>This is why the best preparer in the country cannot deliver strategy in "
            "March. The facts are closed. The work is to report them.</p>"
        ),
        (
            "What Each Engagement Is Scoped To Deliver",
            "<p><strong>A compliance engagement</strong> delivers the entity and personal "
            "returns, required elections attached to those returns, estimated payment "
            "vouchers usually based on prior-year safe harbor, and responses to notices. It "
            "is priced per return, and its economics depend on efficient throughput during a "
            "compressed filing season.</p>"
            "<p><strong>A strategy engagement</strong> delivers a multi-year projection, an "
            "entity structure analysis, retirement plan design modeled against the employee "
            "census, a depreciation plan tested for usability, a state election review, a "
            "prior-year lookback for recoverable amounts, and a calendar of dated deadlines. "
            "It is priced as a project and performed outside filing season, because that is "
            "when the facts are still open.</p>"
        ),
        (
            "Why One Firm Doing Both Often Still Delivers Only One",
            "<p>Many firms offer both, and many clients still receive only compliance. The "
            "reason is capacity, not intent. A firm whose revenue is concentrated in returns "
            "filed between January and April is fully committed during exactly the months it "
            "is being paid, and planning work has to happen in the quarters when the same "
            "staff are least busy but the revenue is not attached.</p>"
            "<p>The practical test is not what a firm offers. It is whether a planning "
            "conversation happened in the third quarter, produced written analysis, and ended "
            "with dated decisions. If the only substantive contact is a return delivered in "
            "the spring, the relationship is compliance regardless of how it was described.</p>"
        ),
        (
            "What Compliance-Only Costs at $500K+",
            "<p>At modest profit the gap is small. At $500,000 to $1,000,000 the recurring "
            "items that fall outside a compliance scope are consistent and quantifiable: a "
            "retirement plan never designed, a PTET election never made, a cost segregation "
            "study never commissioned, an entity structure never revisited as the business "
            "grew, and prior-year depreciation never caught up.</p>"
            "<p>Individually each is five figures. Together they are the difference between "
            "an effective rate in the low thirties and one in the mid twenties, repeated "
            "every year the relationship continues.</p>"
        ),
        (
            "You Need Both",
            "<p>This is not an argument against compliance. A strategy that is not reported "
            "correctly creates exposure rather than savings, and every structure described "
            "here ultimately has to survive as a filed position.</p>"
            "<p>The two functions can sit with one firm or with two. Many owners keep an "
            "existing preparer for filing and add an advisory relationship for planning, and "
            "that works well when the division of labor is explicit. What does not work is "
            "assuming that a compliance engagement includes planning it was never scoped or "
            "priced to deliver.</p>"
        ),
    ],
    takeaways=[
        "Compliance works on closed facts; strategy works on facts that can still be changed.",
        "A preparer cannot deliver strategy in March because the decisions have already defaulted.",
        "The test of a real planning relationship is a Q3 conversation ending in dated decisions.",
        "At $500K+ profit, the items outside a compliance scope repeat every year they are missed.",
        "Both functions are necessary; the failure is expecting one engagement to deliver both.",
    ],
    faqs=[
        (
            "Is tax planning the same as tax preparation?",
            "<p>No. Preparation reports transactions that already occurred and is mandatory. "
            "Planning designs transactions before they occur to change the reported outcome, "
            "and it is optional. They operate on opposite timelines and are priced on "
            "different models.</p>",
        ),
        (
            "Does my CPA already do tax planning?",
            "<p>Some do. The test is whether a substantive planning conversation happened "
            "before year-end, produced written analysis of specific alternatives, and ended "
            "with dated decisions. A return delivered in the spring with a note about next "
            "year is compliance with commentary attached.</p>",
        ),
        (
            "Can I keep my current CPA and add a tax strategist?",
            "<p>Yes, and it is common. The planning firm produces the strategy and the "
            "implementation steps; the existing preparer files the returns. It works well "
            "when responsibilities are explicit and both parties see the same projections.</p>",
        ),
        (
            "How is a strategy engagement priced?",
            "<p>As a project rather than per return. Our advisory engagement is $7,800, "
            "quoted flat in writing before work begins, with cost segregation studies at $1 "
            "per square foot subject to a $2,000 minimum and amended returns at $2,500 each. "
            "Flat pricing exists so the analysis is not constrained by an hourly meter.</p>",
        ),
    ],
)

CLUSTER = Cluster(
    key="high-income",
    slug=P,
    label="High Income Tax Strategy",
    title="High Income Tax Strategy for Business Owners: The Complete Guide",
    description=(
        "The tax strategies that actually apply at $500,000 to $1,000,000 of business "
        "profit, in the order they should be worked, and what they are worth."
    ),
    h1="High Income Tax Strategy for Business Owners",
    subtitle=(
        "What applies at $500,000 to $1,000,000 of profit, what it is worth, and why "
        "the sequence matters more than any single strategy."
    ),
    lead=(
        "High income tax strategy for business owners is the coordinated use of entity "
        "structure, retirement plan design, depreciation timing, and state-level elections "
        "to reduce the effective tax rate on business profit. At $500,000 to $1,000,000 of "
        "profit, no single strategy produces a transformative result. Four or five moves of "
        "moderate size, sequenced so they do not undercut one another, routinely move an "
        "effective rate from the low thirties into the mid twenties."
    ),
    keywords=[
        "high income tax strategy",
        "business owner tax strategy 500k",
        "reduce taxes high income business owner",
        "tax planning high earners business",
    ],
    body=[
        (
            "The Problem With How This Income Level Gets Served",
            "<p>A business owner clearing $500,000 in profit sits in an awkward band. They "
            "have moved well past the point where the standard small business checklist has "
            "anything left to offer, and they are nowhere near the scale where the structures "
            "marketed to family offices make economic sense.</p>"
            "<p>The result is a persistent mismatch. The owner's CPA, engaged to prepare "
            "returns, delivers accurate compliance and little else, because that is what the "
            "engagement was scoped for. Meanwhile the owner is a target market for promoted "
            "arrangements sold on the strength of the deduction rather than the economics. "
            "Neither is planning.</p>"
            "<p>What actually works at this level is unglamorous and well-established: get "
            "the entity right, size the retirement plan properly, put depreciation where it "
            "can be used, and take the state elections available. The difficulty is not that "
            "these are exotic. It is that they interact, and getting the sequence wrong "
            "forfeits much of the benefit.</p>"
        ),
        (
            "Why Sequence Determines the Result",
            "<p>These strategies are not independent, and treating them as a list to be "
            "picked from is the most common planning error at this income level.</p>"
            "<p>Entity structure determines the compensation figure. The compensation figure "
            "determines retirement plan capacity, because contribution limits are driven by "
            "W-2 wages. Retirement contributions reduce taxable income, which changes where "
            "the owner sits relative to the Section 199A thresholds, which feeds back into "
            "what the compensation figure should have been. Depreciation reduces taxable "
            "income too, which can pull the owner below a threshold that the retirement plan "
            "was being sized to reach.</p>"
            "<p>Optimizing any one of these in isolation reliably produces a worse combined "
            "result than modeling them together. This is the central reason planning at this "
            "level is a modeling exercise rather than a checklist.</p>"
        ),
        (
            "Entity Structure: The Foundation",
            "<p>The first question is whether profit is being exposed to payroll tax "
            "unnecessarily. For an owner-operated business, an S election limits Social "
            "Security and Medicare tax to wages paid rather than total profit.</p>"
            "<p>The saving is smaller than commonly advertised at this income level, because "
            "an owner here has already cleared the Social Security wage base through wages "
            "alone. What remains is the Medicare component, roughly 3.8 percent including the "
            "Additional Medicare Tax, on profit taken as distribution. On $500,000 of "
            "distribution that is around $19,000 annually. Meaningful, and only the "
            "beginning.</p>"
            "<p>Beyond the operating entity, the structural questions worth closing are "
            "whether real estate or equipment belongs in a separate entity, whether a C-corp "
            "management company has a role where earnings are being retained, and whether "
            "the operating agreement is consistent with the tax election in place. That last "
            "one invalidates more S elections than any other single issue.</p>"
        ),
        (
            "Retirement Plan Design: The Largest Lever",
            "<p>For most owners in this band, retirement plan design produces the single "
            "largest deduction available from ordinary operations, and it is the most "
            "consistently underused.</p>"
            "<p>A solo 401(k) combines an employee deferral with an employer contribution "
            "tied to compensation. Layering a cash balance or defined benefit plan on top "
            "changes the scale entirely, because those plans are sized actuarially by the "
            "benefit that must be funded by retirement age. An owner in their fifties with "
            "fewer years remaining to fund the benefit can contribute far more than a "
            "younger owner with identical profit. Combined deductions of $150,000 to $250,000 "
            "are routine at this profit level.</p>"
            "<p>The binding constraint is employees. A plan covering staff carries "
            "nondiscrimination requirements, and the contributions owed to employees have to "
            "be modeled against the owner's benefit. That modeling determines whether the "
            "structure works, and it is precisely the analysis a compliance engagement is "
            "not scoped to perform.</p>"
        ),
        (
            "Depreciation: Powerful, and Only If Usable",
            "<p>Under the OBBBA, 100 percent bonus depreciation is permanent for qualifying "
            "property acquired after January 19, 2025. For an owner holding real property, a "
            "cost segregation study reclassifies portions of the building into 5, 7, and "
            "15-year categories, all of which become immediately deductible. On a $1,500,000 "
            "building a study typically produces a first-year deduction in the $300,000 to "
            "$450,000 range.</p>"
            "<p>The question that decides whether this is worth anything is usability. Rental "
            "activity is passive by default under Section 469, and passive losses generally "
            "cannot offset business income. The routes through are qualifying as a real "
            "estate professional, materially participating in a short-term rental where the "
            "average stay is seven days or less, or holding property used in the owner's own "
            "trade or business.</p>"
            "<p>An owner-occupied commercial building is the cleanest case, because the "
            "property is used in the trade or business and the passive question largely "
            "falls away. Commissioning a study before confirming usability is how owners buy "
            "a deduction they cannot spend.</p>"
        ),
        (
            "State Elections: The Highest Return on Effort",
            "<p>Most states now allow a pass-through entity to pay state income tax at the "
            "entity level, where it is federally deductible, rather than at the individual "
            "level where the state and local tax deduction is limited.</p>"
            "<p>For an owner in a state with a 5 to 9 percent income tax, this converts a "
            "largely non-deductible expense into a fully deductible one. On $700,000 of "
            "income in a 6 percent state, $42,000 of state tax becomes deductible, worth "
            "roughly $15,000 federally, for the effort of making an election.</p>"
            "<p>Rules vary substantially. Some states require the election annually, some "
            "require estimated payments during the tax year, and a missed payment date can "
            "invalidate the election. It remains one of the most frequently missed items on "
            "the returns we review.</p>"
        ),
        (
            "Where the Section 199A Deduction Fits",
            "<p>The qualified business income deduction is worth up to 20 percent of "
            "qualified business income, and at this profit level it is rarely automatic. "
            "Owners here are above the taxable income thresholds, which means the deduction "
            "is capped by a formula based on W-2 wages paid and the basis of qualified "
            "property held.</p>"
            "<p>Two consequences follow. First, a business paying no W-2 wages has a "
            "limitation of zero and receives no deduction regardless of profitability, which "
            "makes the compensation decision a deduction decision as well as a payroll tax "
            "decision. Second, for a specified service business, meaning health, law, "
            "accounting, consulting, financial services and similar fields, the deduction "
            "phases out entirely above the threshold range, and no amount of wage adjustment "
            "restores it.</p>"
            "<p>For service business owners this reframes the work. The lever is no longer "
            "tuning the wage line but reducing taxable income enough to re-enter the "
            "phase-out range, which is usually done through retirement plan contributions or "
            "depreciation. It is one of the clearest illustrations of why these strategies "
            "have to be modeled together: the retirement plan is not only a deduction in its "
            "own right, it can restore a separate deduction worth tens of thousands more.</p>"
        ),
        (
            "What This Looks Like Combined",
            "<p>Consider an owner with $850,000 of profit, age 52, in a state with a 6 "
            "percent income tax, who owns the building the business operates from.</p>"
            "<p>The S election removes roughly $19,000 of payroll tax. A solo 401(k) paired "
            "with a cash balance plan deducts roughly $200,000. A cost segregation study on "
            "the owner-occupied building produces a large first-year deduction that is "
            "usable because the property is used in the trade or business. The PTET election "
            "makes the state tax federally deductible.</p>"
            "<p>None of these is aggressive. Each is a well-established provision applied to "
            "facts that support it. Together they move a low-thirties effective rate into the "
            "high teens or low twenties. The result comes from the stack, and from ordering "
            "the stack correctly.</p>"
        ),
        (
            "What This Is Not",
            "<p>None of this involves offshore entities, listed transactions, or "
            "arrangements whose economic purpose is the deduction itself. Owners at this "
            "income level are actively marketed syndicated conservation easements, promoted "
            "micro-captive insurance, and structures whose primary output is a tax benefit.</p>"
            "<p>The filter worth applying: would this arrangement make economic sense if the "
            "tax benefit disappeared? A retirement plan still funds a retirement. A cost "
            "segregation study still describes a building accurately. A syndicated easement "
            "does not survive the question, which is why it carries penalty exposure that "
            "outlives the disallowed deduction.</p>"
            "<p>A second filter is worth applying alongside it: who is being paid, and how? "
            "A strategy presented by the party earning a commission on the product that "
            "implements it deserves independent review before it is put in place. That is not "
            "a judgment about anyone's integrity. It is simply that the incentive to "
            "recommend and the duty to evaluate should not sit with the same party.</p>"
        ),
        (
            "The Prior-Year Recovery Most Owners Miss",
            "<p>Forward planning is only half of it. A review of the last three years "
            "routinely surfaces recoverable amounts: depreciation never claimed, a PTET "
            "election available and never made, credits missed, an S election filed "
            "incorrectly, or a property never studied.</p>"
            "<p>Much of this is recoverable. Amended returns reach back three years, and a "
            "Form 3115 accounting method change allows missed depreciation to be caught up in "
            "the current year without amending anything. For a business at this profit level "
            "the lookback frequently recovers more in the first year than the forward plan "
            "saves, which is why it belongs at the front of the engagement rather than at the "
            "end.</p>"
        ),
    ],
    takeaways=[
        "No single strategy is transformative at this level; four or five moderate moves stacked are.",
        "Sequence matters because entity structure sets compensation, which sets retirement capacity.",
        "The S-corp saving here is the Medicare component, not 15.3 percent of profit.",
        "Retirement plan design is the largest deduction available from ordinary operations.",
        "Confirm a depreciation loss is usable under Section 469 before commissioning the study.",
        "A three-year lookback often recovers more in year one than the forward plan saves.",
    ],
    faqs=[
        (
            "What is the most effective tax strategy for a business owner making $500K?",
            "<p>For most owners it is retirement plan design, specifically a cash balance or "
            "defined benefit plan layered on a solo 401(k), which can produce deductions of "
            "$150,000 to $250,000 depending on age and compensation. No other strategy "
            "available from ordinary operations produces a deduction of that size.</p>",
        ),
        (
            "How much can a business owner realistically save with tax planning?",
            "<p>At $500,000 to $1,000,000 of profit, moving an effective rate from the low "
            "thirties to the mid twenties is a realistic target, which is roughly $50,000 to "
            "$80,000 annually depending on state and structure. The result comes from several "
            "moves stacking rather than from one large deduction.</p>",
        ),
        (
            "Should I set up an S-corp if I make $500,000?",
            "<p>Usually yes for an owner-operated business, though the saving is the Medicare "
            "component rather than the full 15.3 percent, since the Social Security wage base "
            "is already cleared at that income. It is generally not appropriate for a real "
            "estate holding entity, where the lack of basis from entity debt suspends losses.</p>",
        ),
        (
            "What is the pass-through entity tax election worth?",
            "<p>It converts state income tax from a largely non-deductible individual expense "
            "into a fully deductible entity expense. On $700,000 of income in a 6 percent "
            "state that is roughly $15,000 of federal benefit annually, for the effort of "
            "making an election within its deadline.</p>",
        ),
        (
            "Can I use real estate depreciation against my business income?",
            "<p>Only in specific circumstances. Rental activity is passive by default under "
            "Section 469. The routes through are qualifying as a real estate professional, "
            "materially participating in a short-term rental averaging seven days or less per "
            "stay, or holding property used in your own trade or business, which is the "
            "cleanest case.</p>",
        ),
        (
            "Is it too late to fix prior years?",
            "<p>Usually not. Amended returns generally reach back three years, and a Form "
            "3115 accounting method change allows missed depreciation to be caught up in the "
            "current year without amending prior returns. A three-year lookback frequently "
            "recovers more than the first year of forward planning saves.</p>",
        ),
        (
            "How is this different from what my current CPA does?",
            "<p>Most CPAs are engaged to prepare returns, which is backward-looking work on "
            "facts that have already closed. Planning requires decisions before year-end and "
            "is a separate engagement with a different timeline. Many owners keep their "
            "preparer for filing and add an advisory relationship for the planning work.</p>",
        ),
        (
            "What does high income tax planning cost?",
            "<p>Our advisory engagement is $7,800, quoted flat in writing before work begins. "
            "Cost segregation studies are priced separately at $1 per square foot subject to a "
            "$2,000 minimum, entity returns are $1,500, personal returns are $1,000, and "
            "amended returns are $2,500 each.</p>",
        ),
    ],
    spokes=[
        PLANNING_500K,
        BELOW_20,
        PLAYBOOK,
        NOT_RECOMMENDED,
        YEAR_END,
        Spoke(
            slug="cpa-costing-you-money",
            label="Why your CPA is costing you $50K+ per year",
            adopted=True,
        ),
        COMPLIANCE_VS_STRATEGY,
    ],
)
