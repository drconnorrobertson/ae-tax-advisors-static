#!/usr/bin/env python3
"""Cluster 7: Tax planning vs tax preparation."""

from __future__ import annotations

from cluster_common import Cluster, Spoke

P = "tax-planning-vs-tax-preparation"

COMPLIANCE_SHOP = Spoke(
    slug="cpa-compliance-shop-vs-tax-strategist",
    label="Why your CPA is a compliance shop, not a strategist",
    title="Why Your CPA Is a Compliance Shop, Not a Strategist",
    description=(
        "The economics of a return preparation practice, and why they make proactive "
        "planning structurally difficult regardless of the CPA's ability."
    ),
    h1="Why Your CPA Is a Compliance Shop, Not a Strategist",
    subtitle=(
        "It is a business model problem, not a competence problem. The distinction "
        "matters for what you do about it."
    ),
    lead=(
        "Most CPA firms are built around return preparation, a business with specific "
        "economics: revenue concentrated in a three-month filing season, pricing per return, "
        "and capacity constrained by the same deadline for every client at once. Those "
        "economics make proactive planning structurally difficult, because planning has to "
        "happen in the quarters when the work is not being paid for and requires modeling "
        "that per-return pricing does not fund."
    ),
    keywords=[
        "cpa compliance vs strategy",
        "why cpa doesnt do tax planning",
        "tax strategist vs cpa",
    ],
    body=[
        (
            "The Economics of a Preparation Practice",
            "<p>A preparation firm earns most of its annual revenue between January and "
            "April. Staff are fully committed during those months, and the work is measured "
            "in returns completed. Pricing is per return, often anchored to what the client "
            "paid last year.</p>"
            "<p>The consequence is a capacity problem with no obvious solution. Planning work "
            "must occur in the third quarter, when the facts are still open, but it generates "
            "no revenue under a per-return model unless it is sold separately as a distinct "
            "service. Firms that have not built that service line have no mechanism to "
            "deliver planning, however capable the individual CPA is.</p>"
        ),
        (
            "Why This Is Not About Competence",
            "<p>The CPAs in these firms are generally very good at what they are engaged to "
            "do. Return preparation for a business with multiple entities, multi-state "
            "activity, and complex depreciation is demanding technical work, and doing it "
            "accurately under deadline pressure is a real skill.</p>"
            "<p>The gap is scope, not ability. A preparer receives the year's records after "
            "the year closed. By then the retirement plan was installed or it was not, the "
            "PTET election was made or missed, the equipment was placed in service or it was "
            "not. There is no version of preparation, however expert, that reopens those "
            "decisions.</p>"
            "<p>This matters because the fix is not finding a smarter CPA. It is engaging a "
            "different service, whether from the same firm or another.</p>"
        ),
        (
            "The Signals That Identify a Compliance Relationship",
            "<p>Reliable indicators, in rough order of significance:</p>"
            "<ul>"
            "<li><strong>The only substantive contact is in filing season.</strong> Planning "
            "requires a conversation before year-end, when something can still be done.</li>"
            "<li><strong>Estimates are set by prior-year safe harbor.</strong> Safe harbor is "
            "a penalty-avoidance mechanism, not a projection. Its use signals nobody modeled "
            "the current year.</li>"
            "<li><strong>Advice arrives as a comment on the return.</strong> A note about "
            "considering an S-corp next year, delivered in April, is an observation rather "
            "than analysis.</li>"
            "<li><strong>No written projections exist.</strong> Planning produces documents: "
            "multi-year projections, entity comparisons, plan design studies.</li>"
            "<li><strong>Prior years have never been reviewed.</strong> A three-year lookback "
            "is standard in a planning engagement and absent from a compliance one.</li>"
            "<li><strong>Fees are per return with no separate planning engagement.</strong> "
            "If planning is not priced, it is generally not scoped.</li>"
            "</ul>"
        ),
        (
            "What It Costs at $500K+ of Profit",
            "<p>At modest profit the gap is small, which is why this arrangement works fine "
            "for most taxpayers. Above roughly $500,000 the missing items become consistent "
            "and quantifiable: a retirement plan never designed, worth $150,000 or more in "
            "annual deductions; a PTET election never made, worth $15,000 to $30,000 a year; "
            "a cost segregation study never commissioned; an entity structure never revisited "
            "as the business grew; prior-year depreciation never caught up.</p>"
            "<p>None of these is exotic. Each is a well-established provision applied to facts "
            "that support it, and each falls outside what a preparation engagement is scoped "
            "to deliver.</p>"
        ),
        (
            "What to Do About It",
            "<p>Three workable options.</p>"
            "<p><strong>Ask the current firm directly</strong> whether they offer a separate "
            "planning engagement, what it includes, and what it costs. Some do and have never "
            "raised it because the client never asked.</p>"
            "<p><strong>Add a planning relationship alongside the existing preparer.</strong> "
            "This is common and works well when responsibilities are explicit: the planning "
            "firm produces the analysis and implementation steps, the preparer files the "
            "returns.</p>"
            "<p><strong>Consolidate with a firm that does both</strong>, accepting the "
            "transition cost, which is real in the first year while the new firm learns the "
            "history.</p>"
            "<p>What does not work is continuing to expect strategy from an engagement that "
            "was never scoped or priced to produce it, and concluding from its absence that "
            "no strategy exists.</p>"
        ),
    ],
    takeaways=[
        "Preparation revenue concentrates in filing season, when planning decisions have already defaulted.",
        "The gap is scope and timing, not the CPA's technical ability.",
        "Prior-year safe harbor estimates are a reliable signal that nobody modeled the current year.",
        "At $500K+ profit the missing items repeat every year the relationship continues.",
        "Adding a planning relationship alongside the existing preparer is usually the simplest fix.",
    ],
    faqs=[
        (
            "Is my CPA doing something wrong?",
            "<p>Generally no. They are delivering what the engagement was scoped and priced "
            "for, which is accurate and timely return preparation. Planning is a separate "
            "service with a different timeline. The problem is the mismatch between what was "
            "purchased and what was expected.</p>",
        ),
        (
            "How do I know if I am getting planning?",
            "<p>Look for a substantive conversation before year-end, written analysis "
            "comparing specific alternatives, and a set of decisions with deadlines attached. "
            "If the only deliverable is a completed return each spring, the relationship is "
            "compliance.</p>",
        ),
        (
            "Can I use two firms?",
            "<p>Yes, and many owners at this level do. The planning firm produces the strategy "
            "and implementation steps and the existing preparer files the returns. It works "
            "well when the division of responsibility is explicit and both parties see the "
            "same projections.</p>",
        ),
        (
            "Will my CPA be offended?",
            "<p>In our experience most preparers are comfortable with it, and some welcome it, "
            "because planning work sits outside what they are staffed to deliver. Framing it "
            "as adding a service rather than replacing a relationship usually resolves any "
            "friction.</p>",
        ),
    ],
)

HOW_MUCH_SAVES = Spoke(
    slug="how-much-proactive-tax-planning-saves",
    label="How much proactive tax planning actually saves",
    title="How Much Proactive Tax Planning Actually Saves",
    description=(
        "Realistic savings ranges by profit level and situation, what drives the "
        "variation, and how to evaluate whether an engagement is worth its fee."
    ),
    h1="How Much Proactive Tax Planning Actually Saves",
    subtitle=(
        "The honest answer is a range, and the range depends on facts that are "
        "knowable before you engage anyone."
    ),
    lead=(
        "Proactive tax planning savings depend on the strategies a specific situation "
        "supports, and the variation is wide. For a business owner at $500,000 to $1,000,000 "
        "of profit, annual savings of $40,000 to $80,000 are a realistic range where the "
        "situation supports retirement plan design, an entity change, and a state election. "
        "Where those are already in place or unavailable, the figure is far smaller, and any "
        "advisor quoting a number before reviewing the facts is guessing."
    ),
    keywords=[
        "how much does tax planning save",
        "tax planning roi business owner",
        "is tax planning worth it",
    ],
    body=[
        (
            "What Actually Drives the Number",
            "<p>Five factors explain most of the variation, and all are knowable before an "
            "engagement begins.</p>"
            "<p><strong>Profit level.</strong> Savings scale with income because most "
            "strategies produce deductions applied against a marginal rate. The same strategy "
            "is worth more at a higher rate.</p>"
            "<p><strong>Owner age.</strong> This drives retirement plan capacity more than "
            "any other input. A 55-year-old owner can often deduct two to three times what a "
            "35-year-old with identical profit can, because the defined benefit contribution "
            "is sized by the years remaining to fund the benefit.</p>"
            "<p><strong>Whether real estate is owned.</strong> Cost segregation only helps if "
            "there is property to study and the resulting loss is usable.</p>"
            "<p><strong>State.</strong> A PTET election in a 9 percent state is worth roughly "
            "three times what it is worth in a 3 percent state, and nothing at all in a state "
            "with no income tax.</p>"
            "<p><strong>What is already in place.</strong> An owner with a properly sized cash "
            "balance plan, a current S election, and a PTET election already made has far "
            "less available than one starting from nothing.</p>"
        ),
        (
            "Realistic Ranges",
            "<p>These reflect what we see, expressed as annual recurring savings for owners "
            "who had none of these strategies in place.</p>"
            "<div style=\"overflow-x:auto;\">"
            "<table>"
            "<thead><tr><th>Profile</th><th>Typical annual savings</th></tr></thead>"
            "<tbody>"
            "<tr><td>$300K profit, age 40, no real estate, low-tax state</td><td>$12,000 - $25,000</td></tr>"
            "<tr><td>$500K profit, age 45, no real estate, mid-tax state</td><td>$30,000 - $55,000</td></tr>"
            "<tr><td>$750K profit, age 52, owns building, mid-tax state</td><td>$60,000 - $110,000</td></tr>"
            "<tr><td>$1M profit, age 58, owns real estate, high-tax state</td><td>$90,000 - $170,000</td></tr>"
            "<tr><td>Any profile with strategies already in place</td><td>$0 - $20,000</td></tr>"
            "</tbody></table></div>"
            "<p>The last row matters and is rarely mentioned. An owner already well advised "
            "may find little available, and an honest assessment says so rather than "
            "manufacturing a strategy to justify a fee.</p>"
        ),
        (
            "The One-Time Recovery Most Owners Miss",
            "<p>Recurring savings are only part of it. A review of the last three years "
            "routinely surfaces recoverable amounts: depreciation never claimed, credits "
            "missed, a PTET election available and never made, an S election filed "
            "incorrectly, or a property never studied.</p>"
            "<p>Amended returns generally reach back three years, and a Form 3115 accounting "
            "method change allows missed depreciation to be caught up in the current year "
            "without amending anything. For a business at this profit level, the one-time "
            "recovery frequently exceeds the first year of forward savings, which is why the "
            "lookback belongs at the start of an engagement.</p>"
        ),
        (
            "Evaluating the Fee",
            "<p>The relevant question is not whether the fee is large. It is the ratio "
            "between the fee and the identified savings, and whether the savings are "
            "recurring.</p>"
            "<p>A $7,800 engagement identifying $60,000 in annual recurring savings returns "
            "roughly eight to one in year one and considerably more over time, because the "
            "structures persist while the fee does not repeat at the same level. A $7,800 "
            "engagement identifying $8,000 in savings is not worth doing, and a competent "
            "advisor should tell you that during the initial review rather than after "
            "invoicing.</p>"
            "<p>Beware fees quoted as a percentage of claimed savings. The incentive is to "
            "inflate the estimate, and the estimate is produced by the same party being paid "
            "on it.</p>"
        ),
        (
            "What Should Happen Before You Engage",
            "<p>A credible advisor should be able to give you a range before you commit, "
            "based on a short review of the last two returns, the entity structure, owner age "
            "and compensation, whether real estate is owned, the state, and what plans and "
            "elections already exist.</p>"
            "<p>That is enough to bracket the opportunity within a reasonable range. An "
            "advisor unwilling to look at the facts before quoting a benefit, or who quotes a "
            "specific large number in a first conversation, is describing a sales process "
            "rather than an analysis.</p>"
        ),
    ],
    takeaways=[
        "Owner age drives retirement plan capacity more than any other single input.",
        "An owner already well advised may have little available, and should be told so.",
        "A three-year lookback often recovers more one-time value than the first year of forward savings.",
        "Judge the fee on the ratio to recurring savings, not on its absolute size.",
        "Fees quoted as a percentage of claimed savings create an incentive to inflate the estimate.",
    ],
    faqs=[
        (
            "How much does tax planning save a business owner?",
            "<p>For an owner at $500,000 to $1,000,000 of profit with none of the main "
            "strategies in place, $40,000 to $80,000 annually is realistic, and more where "
            "real estate and a high-tax state are involved. For an owner already well advised, "
            "it may be very little.</p>",
        ),
        (
            "Is a $7,800 tax planning fee worth it?",
            "<p>It depends entirely on what the situation supports. Against $60,000 of annual "
            "recurring savings the ratio is strongly favorable and improves over time. Against "
            "$8,000 it is not worth doing, and that should be established during the initial "
            "review rather than after the engagement.</p>",
        ),
        (
            "How quickly do savings show up?",
            "<p>State elections and retirement contributions can affect the current year if "
            "handled before their deadlines. Entity changes generally take effect the "
            "following year. Prior-year recovery through amended returns or a Form 3115 "
            "catch-up can produce refunds within months of filing.</p>",
        ),
        (
            "Are the savings recurring or one-time?",
            "<p>Both. Retirement plan design, entity structure, and state elections recur "
            "every year the structures remain in place. Cost segregation and prior-year "
            "recovery are largely one-time, though cost segregation continues to affect the "
            "depreciation schedule in later years.</p>",
        ),
    ],
)

SIGNS = Spoke(
    slug="signs-your-cpa-is-underserving-you",
    label="Signs your CPA is underserving you",
    title="Signs Your CPA Is Underserving You: A Diagnostic",
    description=(
        "Specific, checkable indicators that a tax relationship is not delivering what "
        "a profitable business needs, and what each one means."
    ),
    h1="Signs Your CPA Is Underserving You",
    subtitle=(
        "Not opinions about service quality. Things you can check on your own return "
        "in twenty minutes."
    ),
    lead=(
        "Whether a tax relationship is serving a profitable business is checkable rather than "
        "a matter of impression. Most of the indicators appear on the returns you already "
        "have, and each points to a specific gap: an election never made, a plan never "
        "designed, a structure never revisited. This is a diagnostic rather than a complaint "
        "list."
    ),
    keywords=[
        "signs cpa underserving",
        "should i change cpa business owner",
        "is my cpa good enough",
    ],
    body=[
        (
            "Check the Return Itself",
            "<p><strong>Officer compensation is zero or token on a profitable 1120-S.</strong> "
            "This is an audit trigger sitting on the face of the return, and it means nobody "
            "produced a reasonable compensation analysis.</p>"
            "<p><strong>No PTET is reflected and you are in a state that offers it.</strong> "
            "Worth $15,000 to $30,000 a year at this income level, and missed years generally "
            "cannot be recovered.</p>"
            "<p><strong>The depreciation schedule shows only 27.5 or 39-year property.</strong> "
            "If you own a building and nothing has been reclassified into 5, 7, or 15-year "
            "categories, no cost segregation study was ever done or considered.</p>"
            "<p><strong>Retirement plan contributions are small or absent.</strong> A "
            "profitable owner with a $7,000 IRA contribution and no plan has the largest "
            "available deduction sitting unused.</p>"
            "<p><strong>Estimated payments match prior-year safe harbor exactly.</strong> Safe "
            "harbor avoids penalties; it does not reflect a projection. Exact matching means "
            "nobody modeled the current year.</p>"
        ),
        (
            "Check the Relationship",
            "<p><strong>The only substantive contact is between February and April.</strong> "
            "Planning decisions are made before year-end. A relationship that activates during "
            "filing season is structurally unable to deliver them.</p>"
            "<p><strong>You have never received a written projection.</strong> Planning "
            "produces documents: multi-year projections, entity comparisons, plan design "
            "studies. If nothing in writing has ever arrived, nothing was modeled.</p>"
            "<p><strong>Prior years have never been reviewed.</strong> A three-year lookback "
            "is standard when a planning engagement begins and absent from compliance "
            "relationships.</p>"
            "<p><strong>You learn about strategies from other business owners.</strong> If "
            "peers raise cash balance plans or cost segregation and your advisor has never "
            "mentioned them, that is a scope signal.</p>"
            "<p><strong>Questions get answered but nothing is ever proposed.</strong> A "
            "responsive advisor who only reacts is still not planning. Planning is proactive "
            "by definition.</p>"
        ),
        (
            "Check the Structure",
            "<p><strong>Your entity has not been reviewed since formation.</strong> A "
            "structure appropriate at $150,000 of profit is frequently wrong at $700,000.</p>"
            "<p><strong>You own real estate inside an S-corp or C-corp.</strong> A structural "
            "error that suspends losses and is expensive to unwind, because distributing "
            "appreciated property from a corporation triggers gain.</p>"
            "<p><strong>Your operating agreement has never been reviewed against your "
            "election.</strong> Special allocations or preferred returns are a second class of "
            "stock and can invalidate an S election from day one.</p>"
            "<p><strong>You have entities nobody can explain.</strong> Each entity costs a "
            "return and a set of books. Ones with no identifiable purpose are pure cost and "
            "added audit surface.</p>"
        ),
        (
            "Weigh What You Find",
            "<p>Not every item is equally serious.</p>"
            "<p><strong>Fix immediately:</strong> zero officer compensation on a profitable "
            "S-corp, real estate held in a corporation, an operating agreement conflicting "
            "with an S election. These are exposure, not just missed opportunity.</p>"
            "<p><strong>Address this year:</strong> a missing PTET election, an absent or "
            "undersized retirement plan, an unstudied building. Each is recurring money.</p>"
            "<p><strong>Raise at the next review:</strong> safe harbor estimates, the absence "
            "of written projections, an entity structure that has drifted. Real, and not "
            "urgent.</p>"
        ),
        (
            "What This Does Not Mean",
            "<p>Finding several of these is not evidence of incompetence. Most indicate that "
            "the engagement was scoped for compliance and delivered compliance. That is a "
            "legitimate service and it is what most clients need.</p>"
            "<p>The useful conclusion is not that your CPA is bad. It is that your business "
            "has outgrown the service level you are purchasing, and the fix is to add or "
            "change the service rather than to assume the strategies do not exist.</p>"
        ),
    ],
    takeaways=[
        "Most indicators are visible on returns you already have.",
        "Zero officer compensation on a profitable S-corp is exposure, not just a missed strategy.",
        "Estimates matching prior-year safe harbor exactly mean nobody modeled the current year.",
        "Real estate held inside a corporation is a structural error that gets costlier to unwind.",
        "Finding several of these usually means outgrown scope, not incompetence.",
    ],
    faqs=[
        (
            "What is the clearest sign of a problem?",
            "<p>Zero or token officer compensation on a profitable S-corp return. It is an "
            "audit trigger visible on the face of the return and it means no reasonable "
            "compensation analysis was performed. It is exposure rather than merely a missed "
            "opportunity.</p>",
        ),
        (
            "How do I check whether cost segregation was ever considered?",
            "<p>Look at the depreciation schedule attached to the return. If you own a "
            "building and every asset is on a 27.5 or 39-year life with nothing in 5, 7, or "
            "15-year categories, no study was done. A study produces distinctive shorter-lived "
            "asset classes.</p>",
        ),
        (
            "Should I change CPAs if I find several of these?",
            "<p>Not necessarily. Raise them directly first and ask whether the firm offers a "
            "separate planning engagement. Many owners add a planning relationship alongside "
            "their existing preparer rather than switching, which avoids losing institutional "
            "knowledge.</p>",
        ),
        (
            "Can prior-year mistakes be fixed?",
            "<p>Often. Amended returns generally reach back three years, and a Form 3115 "
            "accounting method change allows missed depreciation to be caught up in the "
            "current year without amending. Missed PTET elections are the main category that "
            "usually cannot be recovered.</p>",
        ),
    ],
)

ENGAGEMENT = Spoke(
    slug="what-a-tax-advisory-engagement-includes",
    label="What a $7,800 tax advisory engagement includes",
    title="What a $7,800 Tax Advisory Engagement Includes",
    description=(
        "The specific deliverables, timeline, and boundaries of a flat-fee tax advisory "
        "engagement, and what is priced separately."
    ),
    h1="What a $7,800 Tax Advisory Engagement Includes",
    subtitle="The deliverables, the sequence, and what sits outside the fee.",
    lead=(
        "A tax advisory engagement is a project rather than a recurring compliance service. "
        "Ours is $7,800, quoted flat in writing before work begins, and covers the analysis "
        "and implementation planning across entity structure, retirement plan design, "
        "depreciation strategy, state elections, and a three-year lookback for recoverable "
        "amounts. Return preparation and cost segregation studies are priced separately."
    ),
    keywords=[
        "tax advisory engagement cost",
        "what does tax planning include",
        "tax advisory engagement deliverables",
    ],
    body=[
        (
            "Phase One: Baseline and Lookback",
            "<p>The engagement opens with the last three years of business and personal "
            "returns read together, the current effective rate calculated rather than "
            "estimated, and the entity structure and its elections confirmed against the "
            "governing documents.</p>"
            "<p>The lookback runs in the same pass, identifying depreciation never claimed, "
            "credits missed, elections available and never made, and structural errors such "
            "as an S election filed without a conforming operating agreement. Recoverable "
            "amounts are quantified with the route to recover each: an amended return, or a "
            "Form 3115 catch-up in the current year.</p>"
            "<p>The deliverable is a written baseline with the recoverable amounts identified "
            "and a recommendation on which are worth pursuing.</p>"
        ),
        (
            "Phase Two: Structure and Plan Design",
            "<p>The analysis proper. Entity structure is modeled against alternatives over "
            "several years rather than one, because a structure that wins in the first year "
            "can lose over five. Where an S election is in place or recommended, a reasonable "
            "compensation analysis is produced with market data and the derivation "
            "documented.</p>"
            "<p>Retirement plan design is modeled against the employee census, comparing a "
            "solo 401(k) or safe harbor 401(k) alone against a cash balance plan layered on "
            "top, with the employee cost of each design quantified. Depreciation strategy is "
            "analyzed including whether any resulting loss will actually be usable under the "
            "passive activity rules, which determines whether a study is worth commissioning "
            "at all. State elections are reviewed, including multi-state apportionment where "
            "relevant.</p>"
            "<p>These are modeled together rather than in isolation, because compensation "
            "determines plan capacity, plan contributions change the Section 199A position, "
            "and depreciation changes it again.</p>"
        ),
        (
            "Phase Three: The Plan and Implementation Calendar",
            "<p>The output is a written tax plan setting out each recommended strategy, the "
            "quantified annual benefit, the cost of implementing it, and the steps required, "
            "with a calendar of deadlines: election dates, plan installation deadlines, and "
            "the dates estimated payments must change.</p>"
            "<p>Implementation support is included: coordinating with the actuary and "
            "third-party administrator on plan installation, preparing or reviewing the "
            "election filings, and providing the documentation templates for the compensation "
            "file, accountable plan, and grouping election where applicable.</p>"
        ),
        (
            "What Is Priced Separately",
            "<p>Stated plainly so the total is predictable:</p>"
            "<ul>"
            "<li><strong>Cost segregation studies:</strong> $1 per square foot, subject to a "
            "$2,000 minimum.</li>"
            "<li><strong>Entity tax returns:</strong> $1,500 each.</li>"
            "<li><strong>Personal tax returns:</strong> $1,000.</li>"
            "<li><strong>Amended returns:</strong> $2,500 each.</li>"
            "</ul>"
            "<p>Amended returns are separately priced because whether to file them is a "
            "decision that follows from the lookback rather than a given. The engagement "
            "identifies what is recoverable and what it is worth; you decide which to "
            "pursue.</p>"
        ),
        (
            "What the Engagement Does Not Do",
            "<p>Worth stating directly. It is not a return preparation engagement, though "
            "preparation is available separately. It is not investment advice or insurance "
            "placement, and we do not receive commissions on any product recommended, which "
            "is why the retirement plan analysis can be neutral about the provider.</p>"
            "<p>It does not include audit representation, though the documentation the "
            "engagement produces is what defends the positions taken. And it does not "
            "manufacture strategies where the facts do not support them. If the review "
            "identifies little available, we say so during the initial assessment, before an "
            "engagement letter is issued.</p>"
        ),
        (
            "Whether the Fee Is Justified",
            "<p>The test is the ratio to recurring savings. At $500,000 to $1,000,000 of "
            "profit with none of the main strategies in place, $40,000 to $80,000 in annual "
            "recurring savings is realistic, which returns five to ten times the fee in the "
            "first year and more thereafter, because the structures persist.</p>"
            "<p>Where an owner already has a properly sized plan, a current entity structure, "
            "and their state elections made, the available savings may be small. That is "
            "established in the initial assessment rather than after invoicing, and it is the "
            "reason the assessment happens before the engagement letter.</p>"
        ),
    ],
    takeaways=[
        "The fee is flat, quoted in writing before work begins, and covers analysis and implementation planning.",
        "The three-year lookback runs first and often recovers more than the first year of forward savings.",
        "Strategies are modeled together because each changes the inputs to the others.",
        "Cost segregation, return preparation, and amended returns are priced separately and stated up front.",
        "No commissions are received on recommended products, so the plan analysis stays neutral.",
    ],
    faqs=[
        (
            "What does a tax advisory engagement cost?",
            "<p>Ours is $7,800, quoted flat in writing before work begins, with split payment "
            "available. Cost segregation studies are $1 per square foot subject to a $2,000 "
            "minimum, entity returns are $1,500, personal returns are $1,000, and amended "
            "returns are $2,500 each.</p>",
        ),
        (
            "How long does the engagement take?",
            "<p>Typically several weeks from start to delivered plan, depending on how quickly "
            "documents arrive. Implementation extends beyond that, since plan installation and "
            "elections follow their own deadlines, which are set out in the calendar delivered "
            "with the plan.</p>",
        ),
        (
            "Do you prepare returns as well?",
            "<p>Yes, priced separately at $1,500 per entity return and $1,000 for a personal "
            "return. Many clients keep their existing preparer and use us only for planning, "
            "which works well when the division of responsibility is explicit.</p>",
        ),
        (
            "What if the review finds nothing worth doing?",
            "<p>We say so during the initial assessment, before an engagement letter is "
            "issued. An owner with a properly sized retirement plan, a current entity "
            "structure, and their state elections already made may have little available, and "
            "an engagement in that situation would not be worth its fee.</p>",
        ),
        (
            "Do you receive commissions on the products you recommend?",
            "<p>No. We are paid by the client, not by product providers, which is why the "
            "retirement plan analysis can be neutral about which provider or design is used. "
            "Fee arrangements that depend on product placement create an incentive we prefer "
            "not to have.</p>",
        ),
    ],
)

CLUSTER = Cluster(
    key="planning-vs-prep",
    slug=P,
    label="Tax Planning vs Tax Preparation",
    title="Tax Planning vs Tax Preparation: The Complete Guide",
    description=(
        "What separates proactive tax planning from return preparation, why the "
        "difference costs profitable business owners real money, and what to do about it."
    ),
    h1="Tax Planning vs Tax Preparation",
    subtitle=(
        "One reports what already happened. The other changes what happens. Most "
        "owners are buying the first and expecting the second."
    ),
    lead=(
        "Tax preparation is the accurate, timely reporting of transactions that have already "
        "occurred, and it is mandatory. Tax planning is the design of those transactions "
        "before they occur so the reported result is different, and it is optional. They run "
        "on opposite timelines, require different work, and are priced on different models, "
        "which is why a preparation engagement does not produce planning no matter how well "
        "it is performed."
    ),
    keywords=[
        "tax planning vs tax preparation",
        "difference between tax planning and preparation",
        "proactive tax planning business owner",
        "tax strategist vs tax preparer",
    ],
    body=[
        (
            "The Timeline Is the Whole Distinction",
            "<p>Preparation works on closed facts. The year ended, the transactions occurred, "
            "and the task is to report them correctly. The skills are accuracy, completeness, "
            "and defensibility, and a well-prepared return is genuinely valuable.</p>"
            "<p>Planning works on open facts. The decision has not been made, so it can still "
            "be shaped. Should this entity elect S status? Should this plan be installed "
            "before year-end? Should this building be studied before it is refinanced? Should "
            "the state election be made, and by which date?</p>"
            "<p>Once the year closes, every one of those questions has been answered by "
            "default. This is why the most capable preparer in the country cannot deliver "
            "planning in March. The facts are closed, and the work is to report them.</p>"
        ),
        (
            "What Each Engagement Is Scoped to Deliver",
            "<p>A <strong>preparation engagement</strong> delivers entity and personal "
            "returns, elections that attach to those returns, estimated payment vouchers "
            "usually based on prior-year safe harbor, and responses to notices. It is priced "
            "per return and its economics depend on efficient throughput in a compressed "
            "season.</p>"
            "<p>A <strong>planning engagement</strong> delivers a multi-year projection, an "
            "entity structure analysis, retirement plan design modeled against the employee "
            "census, a depreciation strategy tested for usability, a state election review, a "
            "prior-year lookback quantifying recoverable amounts, and a calendar of dated "
            "deadlines. It is priced as a project and performed outside filing season, "
            "because that is when the facts are still open.</p>"
            "<p>These are different products. Buying one and expecting the other is the "
            "single most common structural problem we see in a new client's situation.</p>"
        ),
        (
            "Why Good CPAs Still Deliver Only Compliance",
            "<p>This is an economics problem rather than a competence problem, and the "
            "distinction matters because it determines the fix.</p>"
            "<p>A preparation firm earns most of its revenue between January and April. Staff "
            "are fully committed in exactly the months they are being paid. Planning work has "
            "to happen in the third quarter, when the facts are open but no revenue attaches "
            "under a per-return model. A firm that has not built planning as a separate, "
            "separately priced service has no mechanism to deliver it, however capable its "
            "people are.</p>"
            "<p>The practical test is not what a firm advertises. It is whether a planning "
            "conversation happened before year-end, produced written analysis comparing "
            "specific alternatives, and ended with dated decisions. If the only substantive "
            "deliverable is a return each spring, the relationship is compliance regardless of "
            "how it was described.</p>"
        ),
        (
            "What Falls Through the Gap",
            "<p>The items that consistently fall outside a preparation scope are not exotic. "
            "They are well-established provisions that happen to require a decision before the "
            "year ends:</p>"
            "<ul>"
            "<li><strong>Retirement plan design.</strong> A cash balance plan layered on a "
            "401(k) can deduct $150,000 to $250,000 annually, and generally must be installed "
            "before the plan year ends. It requires an actuarial study, so a preparer has no "
            "natural moment to raise it.</li>"
            "<li><strong>The PTET election.</strong> Worth $15,000 to $30,000 a year at this "
            "income level. Its deadline usually falls during the tax year, and missed years "
            "generally cannot be recovered.</li>"
            "<li><strong>Cost segregation.</strong> Requires a study and, more importantly, an "
            "analysis of whether the resulting loss will be usable under the passive activity "
            "rules before it is commissioned.</li>"
            "<li><strong>Entity structure.</strong> Appropriate at $150,000 of profit is "
            "frequently wrong at $700,000, and changes take effect the following tax year.</li>"
            "<li><strong>Reasonable compensation analysis.</strong> A documented derivation "
            "produced before the year begins, rather than a figure carried forward because "
            "nobody revisited it.</li>"
            "<li><strong>Prior-year recovery.</strong> Amended returns and Form 3115 "
            "catch-ups for depreciation never claimed.</li>"
            "</ul>"
        ),
        (
            "What the Gap Costs",
            "<p>At modest profit the gap is small, which is why a compliance-only "
            "relationship works fine for most taxpayers. The arithmetic changes above roughly "
            "$500,000 of profit, because the same strategies produce deductions applied "
            "against a higher marginal rate and because more of them become available.</p>"
            "<p>For a business owner at $500,000 to $1,000,000 with none of the above in "
            "place, $40,000 to $80,000 in annual recurring savings is a realistic range, and "
            "more where real estate and a high-tax state are involved. That figure repeats "
            "every year the gap persists, which is what makes it consequential rather than "
            "merely unfortunate.</p>"
            "<p>The one-time recovery is separate and often larger in the first year. A "
            "three-year lookback routinely surfaces depreciation never claimed and elections "
            "never made, much of it recoverable through amended returns or a Form 3115 "
            "catch-up.</p>"
        ),
        (
            "Why Planning Has to Be Modeled as a System",
            "<p>The reason planning is a distinct discipline rather than a longer checklist "
            "is that the strategies interact.</p>"
            "<p>Entity structure determines the compensation figure. The compensation figure "
            "determines retirement plan capacity, because limits are driven by W-2 wages. "
            "Retirement contributions reduce taxable income, which changes where the owner "
            "sits relative to the Section 199A thresholds, which feeds back into what the "
            "compensation figure should have been. Depreciation reduces taxable income too, "
            "which can pull the owner below a threshold the plan was being sized to "
            "reach.</p>"
            "<p>Optimizing any one of these alone reliably produces a worse combined result "
            "than modeling them together. A checklist cannot capture that, which is why "
            "planning output is a model and a set of dated decisions rather than a list of "
            "tips.</p>"
        ),
        (
            "When Planning Should Happen",
            "<p>The calendar does more to determine the value of a planning engagement than "
            "almost anything else, because most of the decisions have dates attached.</p>"
            "<p>The third quarter is the natural window. Full-year profit can be projected "
            "with reasonable confidence from three quarters of actuals, and every deadline "
            "that matters is still open. A cash balance plan can be studied, designed, and "
            "installed before the plan year ends. State elections and their estimated payment "
            "requirements can still be met. Equipment can be identified and placed in service "
            "deliberately rather than in a December scramble. Entity changes can be decided "
            "for the following year with time to conform documents and establish payroll "
            "first.</p>"
            "<p>By late December the available set has narrowed to items that can be executed "
            "in days. By February the year has closed entirely, and the work that remains is "
            "reporting what happened plus whatever prior-year recovery is still open. That is "
            "worth doing, and it is a fraction of what the same analysis would have been "
            "worth six months earlier.</p>"
        ),
        (
            "You Need Both, and They Can Sit Anywhere",
            "<p>This is not an argument against compliance. A strategy reported incorrectly "
            "creates exposure rather than savings, and every structure described here has to "
            "survive as a filed position. Documentation is what defends it.</p>"
            "<p>The two functions can sit with one firm or two. Many owners keep an existing "
            "preparer for filing and add an advisory relationship for planning, which works "
            "well when the division of responsibility is explicit and both parties see the "
            "same projections. Others consolidate, accepting a real transition cost in the "
            "first year while the new firm learns the history.</p>"
            "<p>What does not work is assuming a compliance engagement includes planning it "
            "was never scoped or priced to deliver, and concluding from the absence of "
            "strategy that no strategy was available.</p>"
        ),
        (
            "The Three-Year Lookback",
            "<p>Planning is usually described as forward-looking, and the first substantial "
            "return in a new engagement is frequently backward-looking instead.</p>"
            "<p>A review of the last three years of business and personal returns routinely "
            "surfaces the same categories: depreciation never claimed because a building was "
            "never studied or assets were placed on the wrong recovery period, credits missed, "
            "a state election available and never made, an S election filed without a "
            "conforming operating agreement, and reasonable compensation figures carried "
            "forward for years without derivation.</p>"
            "<p>Much of this is recoverable. Amended returns generally reach back three years. "
            "A Form 3115 accounting method change allows missed depreciation to be claimed as "
            "a cumulative catch-up in the current year without amending anything, which is "
            "both cheaper and faster than amending. Missed state elections are the main "
            "category that generally cannot be recovered, because they had to be made "
            "contemporaneously.</p>"
            "<p>For a business at this profit level the lookback frequently recovers more in "
            "the first year than the forward plan saves, which is why it belongs at the "
            "beginning of an engagement rather than as an afterthought. It also serves a "
            "diagnostic purpose: what a firm missed for three consecutive years is a reliable "
            "indication of what the relationship is scoped to catch.</p>"
        ),
        (
            "How to Tell Which You Are Buying",
            "<p>Six checkable indicators, most visible on returns you already hold:</p>"
            "<ol>"
            "<li>Substantive contact happens only between February and April.</li>"
            "<li>Estimated payments match prior-year safe harbor exactly, meaning nobody "
            "projected the current year.</li>"
            "<li>No written projection or entity comparison has ever been delivered.</li>"
            "<li>Prior years have never been reviewed for recoverable amounts.</li>"
            "<li>Advice arrives as a comment on a completed return rather than as analysis "
            "before a decision.</li>"
            "<li>Fees are per return, with no separately priced planning engagement.</li>"
            "</ol>"
            "<p>Finding most of these does not mean your CPA is doing a poor job. It means the "
            "engagement was scoped for compliance and delivered compliance, and that the "
            "business has outgrown the service level being purchased.</p>"
            "<p>The constructive move is to raise it directly. Ask whether the firm offers a "
            "separate planning engagement, what it includes, and what it costs. Some firms do "
            "and have never mentioned it because no client asked. Some do not, and will say "
            "so, which is useful information rather than a confrontation. Either answer tells "
            "you what you need to know, and neither requires ending a relationship that is "
            "performing the compliance work perfectly well.</p>"
        ),
    ],
    takeaways=[
        "Preparation works on closed facts; planning works on facts that can still be changed.",
        "The gap is scope and timing, not the preparer's technical ability.",
        "Retirement plan design, PTET elections, and cost segregation are what consistently fall through.",
        "At $500K+ profit the gap costs $40,000 to $80,000 a year, repeating annually.",
        "Strategies interact, so planning output is a model and dated decisions, not a checklist.",
        "Both functions are necessary and can sit with one firm or two, provided the split is explicit.",
    ],
    faqs=[
        (
            "What is the difference between tax planning and tax preparation?",
            "<p>Preparation reports transactions that already occurred and is mandatory. "
            "Planning designs transactions before they occur so the reported outcome is "
            "different, and it is optional. They operate on opposite timelines and are priced "
            "on different models.</p>",
        ),
        (
            "Does my CPA already do tax planning?",
            "<p>The test is whether a substantive planning conversation happened before "
            "year-end, produced written analysis of specific alternatives, and ended with "
            "dated decisions. A return delivered each spring with a comment about next year is "
            "compliance with commentary attached.</p>",
        ),
        (
            "Why doesn't my CPA tell me about these strategies?",
            "<p>Usually because the engagement was scoped and priced for return preparation, "
            "and the strategies require decisions before deadlines that fall long before "
            "filing. It is a business model constraint rather than a competence issue, which "
            "is why the fix is a different service rather than a different preparer.</p>",
        ),
        (
            "How much does the gap actually cost?",
            "<p>At $500,000 to $1,000,000 of profit with none of the main strategies in place, "
            "$40,000 to $80,000 annually is realistic, and more with real estate in a high-tax "
            "state. A three-year lookback often recovers a larger one-time amount on top of "
            "that.</p>",
        ),
        (
            "Can I keep my CPA and add a tax strategist?",
            "<p>Yes, and it is common. The planning firm produces the strategy and "
            "implementation steps and the existing preparer files the returns. It works well "
            "when responsibilities are explicit and both parties work from the same "
            "projections.</p>",
        ),
        (
            "When should planning happen?",
            "<p>The third quarter is ideal, because most decisions require action before "
            "year-end and several need weeks of lead time. Retirement plan installation in "
            "particular requires an actuarial study, so a December start is usually too late "
            "for the current year.</p>",
        ),
        (
            "Is it too late to fix prior years?",
            "<p>Often not. Amended returns generally reach back three years, and a Form 3115 "
            "accounting method change allows missed depreciation to be caught up in the "
            "current year without amending prior returns. Missed state elections are the main "
            "category that usually cannot be recovered.</p>",
        ),
        (
            "What does a planning engagement cost?",
            "<p>Ours is $7,800, quoted flat in writing before work begins, with split payment "
            "available. Cost segregation studies are priced separately at $1 per square foot "
            "subject to a $2,000 minimum, entity returns are $1,500, personal returns are "
            "$1,000, and amended returns are $2,500 each.</p>",
        ),
    ],
    spokes=[
        COMPLIANCE_SHOP,
        Spoke(
            slug="the-3-year-tax-lookback-how-to-recover-thousands-in-missed-deductions",
            label="The 3-year tax lookback: what we find in every review",
            adopted=True,
        ),
        HOW_MUCH_SAVES,
        SIGNS,
        ENGAGEMENT,
    ],
)
