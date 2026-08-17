#!/usr/bin/env python3
"""Cluster 4: Entity structuring for business owners."""

from __future__ import annotations

from cluster_common import Cluster, Spoke

P = "entity-structuring-business-owners"

THREE_WAY = Spoke(
    slug="llc-vs-s-corp-vs-c-corp-500k-business",
    label="LLC vs S-Corp vs C-Corp for $500K+ businesses",
    title="LLC vs S-Corp vs C-Corp for $500K+ Businesses: A Direct Comparison",
    description=(
        "How the three structures actually differ on tax treatment, payroll tax, "
        "retained earnings, and exit, for a business earning $500,000 or more."
    ),
    h1="LLC vs S-Corp vs C-Corp for $500K+ Businesses",
    subtitle=(
        "The comparison that matters is not which is best. It is which fits what "
        "you intend to do with the profit."
    ),
    lead=(
        "An LLC is a legal entity, while S-corp and C-corp are tax classifications, so the "
        "three are not strictly parallel choices. The practical question for a business "
        "earning $500,000 or more is how its profit should be taxed: as a pass-through "
        "without an S election, as a pass-through with one, or at the corporate level. The "
        "answer turns mostly on whether profit is distributed or retained."
    ),
    keywords=[
        "llc vs s corp vs c corp",
        "best entity structure 500k business",
        "business entity comparison high income",
    ],
    body=[
        (
            "Clearing Up the Categories",
            "<p>An LLC is formed under state law and provides liability protection. By "
            "default it is taxed as a sole proprietorship if it has one owner or a "
            "partnership if it has several. It can instead elect to be taxed as an S-corp or "
            "a C-corp without changing its legal form.</p>"
            "<p>So the real menu is the tax treatment: default pass-through, Subchapter S, or "
            "Subchapter C. A corporation formed under state law faces the same choice between "
            "S and C. Framing the decision as LLC versus S-corp obscures that the same LLC "
            "can be either.</p>"
        ),
        (
            "Default Pass-Through Taxation",
            "<p>Profit passes to the owners and is taxed on their personal returns whether or "
            "not distributed. For an actively involved owner, the entire share is generally "
            "subject to self-employment tax.</p>"
            "<p>At $500,000 of profit that exposure is the main drawback. The advantages are "
            "real, though: no payroll requirement, no reasonable compensation analysis, "
            "flexible allocations between owners that need not track ownership percentages, "
            "and basis that includes the entity's debt, which supports loss deductions. That "
            "last feature is why real estate is nearly always held this way.</p>"
        ),
        (
            "Subchapter S",
            "<p>Profit still passes through and is taxed personally, but only amounts paid as "
            "wages carry Social Security and Medicare tax. The rest is distributed free of "
            "those taxes.</p>"
            "<p>At $500,000 to $1,000,000 the saving is the Medicare component, roughly 3.8 "
            "percent, because the Social Security wage base is already cleared by wages. On "
            "$500,000 of distribution that is around $19,000 a year.</p>"
            "<p>The costs are a separate return, payroll infrastructure, a defensible "
            "reasonable compensation file, strictly pro-rata distributions, and shareholder "
            "eligibility restrictions. The disqualifying feature for many owners is that "
            "entity-level debt does not create basis.</p>"
        ),
        (
            "Subchapter C",
            "<p>The corporation is a separate taxpayer paying a 21 percent federal rate on "
            "its income. Profit distributed as dividends is taxed again to the shareholder, "
            "which is the double taxation that makes C-corps unattractive for owners who take "
            "their profit out.</p>"
            "<p>Where a C-corp becomes interesting is retained earnings. An owner reinvesting "
            "profit rather than distributing it pays 21 percent rather than a personal "
            "marginal rate above 37 percent. That gap funds growth from cheaper capital.</p>"
            "<p>Two further features matter. C-corps can deduct the full cost of health "
            "coverage and a broader range of fringe benefits for owner-employees than "
            "pass-throughs can. And qualified small business stock under Section 1202 can, "
            "where all the requirements are met including a five-year holding period, exclude "
            "a substantial amount of gain on an eventual sale. For a company being built to "
            "sell, that provision alone can outweigh years of double taxation.</p>"
        ),
        (
            "The Comparison That Actually Decides It",
            "<div style=\"overflow-x:auto;\">"
            "<table>"
            "<thead><tr><th></th><th>Default pass-through</th><th>S-corp</th><th>C-corp</th></tr></thead>"
            "<tbody>"
            "<tr><td>Entity-level tax</td><td>None</td><td>None</td><td>21%</td></tr>"
            "<tr><td>Payroll tax on profit</td><td>Full share</td><td>Wages only</td><td>Wages only</td></tr>"
            "<tr><td>Second tax on distribution</td><td>No</td><td>No</td><td>Yes, dividends</td></tr>"
            "<tr><td>Debt creates owner basis</td><td>Yes</td><td>No</td><td>Not applicable</td></tr>"
            "<tr><td>Allocations need not be pro rata</td><td>Yes</td><td>No</td><td>No</td></tr>"
            "<tr><td>Owner fringe benefits</td><td>Limited</td><td>Limited</td><td>Broad</td></tr>"
            "<tr><td>Section 1202 exclusion on sale</td><td>No</td><td>No</td><td>Possible</td></tr>"
            "<tr><td>Suits retained earnings</td><td>Poorly</td><td>Poorly</td><td>Well</td></tr>"
            "</tbody></table></div>"
        ),
        (
            "Choosing by Intent",
            "<p>The decision follows from what the profit is for.</p>"
            "<p><strong>Taking the profit out.</strong> An S election is usually correct for "
            "an owner-operated business at this level. The payroll tax saving is real and "
            "there is no second layer of tax.</p>"
            "<p><strong>Holding appreciating property.</strong> Default partnership treatment, "
            "because debt creates basis and property can be distributed without triggering "
            "gain.</p>"
            "<p><strong>Reinvesting to build enterprise value.</strong> A C-corp deserves "
            "serious analysis, particularly where Section 1202 might apply at exit.</p>"
            "<p><strong>Unequal owner economics.</strong> Partnership treatment, because "
            "S-corps require strictly pro-rata distributions.</p>"
            "<p>Many businesses at this level end up with more than one entity, because these "
            "intentions coexist: an S-corp operating company, a partnership holding the real "
            "estate, and occasionally a C-corp for a specific function.</p>"
        ),
    ],
    takeaways=[
        "An LLC can be taxed as a partnership, an S-corp, or a C-corp; the legal form is not the tax choice.",
        "S election suits owners distributing profit; the saving at this level is the Medicare component.",
        "Only partnership treatment gives owners basis from entity-level debt, which real estate needs.",
        "C-corps suit retained earnings at 21 percent and may open Section 1202 treatment at exit.",
        "Many businesses at this level need more than one entity because the intentions coexist.",
    ],
    faqs=[
        (
            "Which entity is best for a business making $500,000?",
            "<p>For an owner-operated business distributing its profit, an S election is "
            "usually correct. For a business retaining earnings to fund growth, a C-corp "
            "deserves analysis. For holding appreciating real estate, default partnership "
            "treatment is nearly always right. The intent for the profit decides it.</p>",
        ),
        (
            "Is the 21% corporate rate lower than my personal rate?",
            "<p>Yes, but only on retained income. Distributing the profit as a dividend adds a "
            "second tax that generally erases the advantage. The corporate rate helps when "
            "earnings stay in the business to fund growth.</p>",
        ),
        (
            "What is Section 1202 and does it apply to me?",
            "<p>Section 1202 allows exclusion of a substantial amount of gain on the sale of "
            "qualified small business stock, subject to requirements including C-corp status, "
            "an original issuance, a qualifying trade or business, gross asset limits, and a "
            "five-year holding period. It is relevant to companies being built for sale, and "
            "it requires planning from formation rather than at exit.</p>",
        ),
        (
            "Can I change entity type later?",
            "<p>Yes, though the routes differ in cost. Electing S status from a partnership "
            "is straightforward. Converting to a C-corp is generally possible. Converting a "
            "C-corp back to a pass-through can trigger built-in gains tax for five years. "
            "Moving appreciated property out of a corporation is usually the expensive "
            "direction, which is why property should not be placed there to begin with.</p>",
        ),
    ],
)

MGMT_CO = Spoke(
    slug="c-corp-management-company-strategy",
    label="When to add a C-Corp management company",
    title="When to Add a C-Corp Management Company",
    description=(
        "The narrow set of circumstances where a C-corp management company is "
        "legitimate, what it can actually accomplish, and how these get challenged."
    ),
    h1="When to Add a C-Corp Management Company",
    subtitle=(
        "It works for retained earnings and fringe benefits. It fails when the fee "
        "is set to move income rather than to pay for work."
    ),
    lead=(
        "A C-corp management company is a separate corporation that provides genuine "
        "services to an owner's operating business, such as administration, marketing, or "
        "management, and charges an arm's length fee for them. The legitimate purposes are "
        "taxing retained earnings at 21 percent rather than a personal marginal rate, and "
        "accessing fringe benefit deductions that pass-through entities cannot use. It fails "
        "when the fee is a mechanism for shifting income rather than payment for real work."
    ),
    keywords=[
        "c corp management company",
        "management fee related entity tax",
        "c corp management company strategy",
    ],
    body=[
        (
            "What the Structure Is",
            "<p>The operating business, typically an S-corp or partnership, pays a management "
            "fee to a C-corp owned by the same owner. The fee is deductible to the operating "
            "business and taxable to the C-corp at 21 percent. The C-corp performs actual "
            "services: bookkeeping, HR administration, marketing, purchasing, or executive "
            "management.</p>"
            "<p>Income moved into the C-corp is taxed at 21 percent rather than at the "
            "owner's personal rate. The gap is meaningful, but it only holds while the money "
            "stays there. Distributing it as a dividend adds the second tax and generally "
            "erases the benefit, so the structure is only coherent where the earnings are "
            "genuinely being retained.</p>"
        ),
        (
            "The Legitimate Reasons",
            "<p><strong>Retained earnings for growth.</strong> An owner accumulating capital "
            "inside the business to fund expansion pays 21 percent instead of a rate above 37 "
            "percent, leaving materially more to reinvest.</p>"
            "<p><strong>Fringe benefits.</strong> C-corps can deduct owner-employee health "
            "coverage, and provide certain benefits such as group term life within limits, on "
            "terms that pass-throughs cannot match. More than 2 percent S-corp shareholders "
            "face restrictions that do not apply to C-corp employees.</p>"
            "<p><strong>Genuinely separable functions.</strong> Where an owner runs several "
            "businesses that all need the same administrative infrastructure, centralizing it "
            "in one entity is ordinary commercial practice with an independent rationale.</p>"
            "<p><strong>Section 1202 positioning.</strong> Where the management company is "
            "itself being built into something saleable, C-corp status may open qualified "
            "small business stock treatment. This is narrow and requires planning from "
            "formation.</p>"
        ),
        (
            "How These Get Challenged",
            "<p>Management fee arrangements between related parties are a well-established "
            "audit target, and the IRS has broad authority to reallocate income among "
            "commonly controlled entities under Section 482 where the arrangement does not "
            "clearly reflect income.</p>"
            "<p>The challenges follow a pattern:</p>"
            "<ul>"
            "<li><strong>No identifiable services.</strong> The management company has no "
            "employees, no premises, and no evidence of work performed. The fee is a journal "
            "entry.</li>"
            "<li><strong>The fee is a residual.</strong> It equals whatever amount produces "
            "the desired taxable income at the operating company, often a suspiciously round "
            "figure that changes each year with profit.</li>"
            "<li><strong>No written agreement.</strong> Unrelated parties document a services "
            "arrangement before performing it. Related parties frequently do not, which is "
            "itself evidence the arrangement is not arm's length.</li>"
            "<li><strong>The fee is not actually paid.</strong> It accrues on the books and "
            "the cash never moves, or moves back immediately.</li>"
            "</ul>"
        ),
        (
            "What a Defensible Arrangement Contains",
            "<p>Documentation created before the services are performed:</p>"
            "<ul>"
            "<li>A written services agreement specifying scope, deliverables, and the basis "
            "for the fee, executed before the period it covers.</li>"
            "<li>Evidence of actual performance: employees or contractors, time records, work "
            "product, and correspondence.</li>"
            "<li>A fee derived from a defensible method, such as cost plus a reasonable "
            "markup, or benchmarked against what a third-party provider would charge for the "
            "same scope, with the derivation documented.</li>"
            "<li>Cash actually transferred on the agreed schedule.</li>"
            "<li>Separate books, bank accounts, and filings, with no commingling.</li>"
            "</ul>"
            "<p>The distinguishing feature of a defensible arrangement is that the fee is "
            "derived from the work. In a weak arrangement the fee is derived from the desired "
            "tax result and the work is described afterward.</p>"
        ),
        (
            "When It Is the Wrong Answer",
            "<p>The structure does not suit an owner who intends to take the money out, "
            "because the second layer of tax on distribution removes the benefit. It does not "
            "suit a business without genuinely separable functions, because there is nothing "
            "for the entity to actually do. And it adds a return, a payroll, and a compliance "
            "burden that has to be justified by more than a modest rate difference.</p>"
            "<p>Accumulating earnings without a documented business purpose also raises the "
            "accumulated earnings tax, a penalty regime aimed at corporations retaining "
            "income beyond their reasonable needs to avoid shareholder-level tax.</p>"
        ),
    ],
    takeaways=[
        "The 21 percent advantage only holds while earnings stay in the C-corp; dividends erase it.",
        "Legitimate uses are retained earnings, fringe benefits, and genuinely centralized functions.",
        "Section 482 lets the IRS reallocate income between commonly controlled entities.",
        "A defensible fee is derived from the work; a weak one is derived from the desired tax result.",
        "Retaining earnings without a documented business purpose invites the accumulated earnings tax.",
    ],
    faqs=[
        (
            "Is a C-corp management company legal?",
            "<p>Yes, when it provides genuine services at an arm's length fee. Centralizing "
            "administrative functions in a separate entity is ordinary commercial practice. "
            "What fails is an entity with no employees, no work product, and a fee set to "
            "produce a target taxable income.</p>",
        ),
        (
            "How is a reasonable management fee determined?",
            "<p>By a defensible method documented in advance, typically cost plus a reasonable "
            "markup, or benchmarking against what an unrelated provider would charge for the "
            "same scope. What matters is that the fee is derived from the services rather "
            "than from the desired tax outcome.</p>",
        ),
        (
            "What is the accumulated earnings tax?",
            "<p>A penalty tax on corporations that retain earnings beyond the reasonable needs "
            "of the business in order to avoid shareholder-level tax. Documented plans for the "
            "retained capital, such as an expansion or acquisition, are what establish the "
            "business need.</p>",
        ),
        (
            "Can I use this to pay for my health insurance?",
            "<p>A C-corp can generally deduct health coverage for owner-employees without the "
            "restrictions that apply to more than 2 percent S-corp shareholders. This is a "
            "real advantage, though on its own it rarely justifies the cost and compliance "
            "burden of an additional entity.</p>",
        ),
    ],
)

PTET = Spoke(
    slug="ptet-election-by-state",
    label="PTET elections by state",
    title="PTET Elections by State: What Business Owners Need to Know",
    description=(
        "How the pass-through entity tax election works around the SALT limitation, "
        "what it is worth, and the deadline mechanics that invalidate elections."
    ),
    h1="PTET Elections by State",
    subtitle=(
        "One of the highest-return items available to a profitable owner, and among "
        "the most frequently missed."
    ),
    lead=(
        "A pass-through entity tax election allows a partnership or S-corp to pay state "
        "income tax at the entity level, where it is fully deductible as a business expense, "
        "rather than passing the liability to owners whose federal deduction for state and "
        "local taxes is capped. Most states now offer one. For an owner in a high-tax state "
        "it converts a largely non-deductible personal expense into a fully deductible "
        "business one."
    ),
    keywords=[
        "ptet election by state",
        "pass through entity tax election",
        "salt cap workaround business owner",
    ],
    body=[
        (
            "The Problem It Solves",
            "<p>The federal deduction for state and local taxes on an individual return is "
            "capped. An owner paying substantial state income tax on pass-through business "
            "income loses most of the federal benefit of that payment.</p>"
            "<p>The PTET election moves the payment. The entity pays the state tax and "
            "deducts it as an ordinary business expense, which reduces the income flowing to "
            "the owner. Because it is an entity-level business expense rather than an "
            "individual itemized deduction, the individual cap does not reach it. The IRS "
            "confirmed this treatment in Notice 2020-75, which is what triggered most states "
            "to adopt these regimes.</p>"
        ),
        (
            "What It Is Worth",
            "<p>The benefit is the federal tax on the state tax that becomes deductible. For "
            "an owner with $700,000 of pass-through income in a state with a 6 percent income "
            "tax, roughly $42,000 of state tax shifts from largely non-deductible to fully "
            "deductible. At a 37 percent federal rate that is about $15,000 a year.</p>"
            "<p>In higher-tax states the figure is larger. An owner with $900,000 of income "
            "in a 9 percent state converts roughly $81,000 of state tax, worth around $30,000 "
            "federally. Relative to the effort of making an election, this is among the "
            "highest returns available.</p>"
        ),
        (
            "How the Regimes Differ",
            "<p>State rules vary enough that a general approach does not work. The dimensions "
            "that matter:</p>"
            "<ul>"
            "<li><strong>Annual versus binding elections.</strong> Some states require an "
            "election every year; others bind for multiple years once made.</li>"
            "<li><strong>Election timing.</strong> Some require the election during the tax "
            "year, others allow it with the return. Missing an in-year deadline forfeits the "
            "year entirely.</li>"
            "<li><strong>Estimated payment requirements.</strong> Several states require "
            "estimated payments during the year, and a missed payment can invalidate the "
            "election even where the election itself was timely filed.</li>"
            "<li><strong>Owner credit mechanics.</strong> Most states give owners a credit for "
            "the entity-level tax paid; a few use an exclusion instead, which affects the "
            "arithmetic.</li>"
            "<li><strong>Resident credit interaction.</strong> For owners with income in "
            "several states, whether the home state grants a credit for another state's PTET "
            "varies, and getting this wrong can produce double taxation.</li>"
            "</ul>"
        ),
        (
            "Where It Does Not Apply",
            "<p>States without a personal income tax have no PTET regime and nothing to "
            "elect, which includes Texas, Florida, Washington, Nevada, South Dakota, Wyoming, "
            "Alaska, and New Hampshire on ordinary income. A small number of income-tax states "
            "have still not enacted a regime.</p>"
            "<p>The election is also unavailable to sole proprietorships and single-member "
            "LLCs that have not elected entity treatment, because there is no pass-through "
            "entity to make it. For an owner in a high-tax state, that limitation is "
            "occasionally reason enough to reconsider the entity structure.</p>"
        ),
        (
            "Why It Gets Missed",
            "<p>Three reasons recur. It is a separate election rather than a line on the "
            "return, so it does not surface during preparation. Its deadlines frequently fall "
            "during the tax year, when a compliance-oriented relationship has no scheduled "
            "contact. And in multi-state situations the analysis requires modeling several "
            "states together, which is planning work rather than filing work.</p>"
            "<p>It is one of the most common findings in a three-year lookback, and prior "
            "years generally cannot be recovered, because the election had to be made "
            "contemporaneously. Each missed year is permanently gone, which is what makes it "
            "worth a calendar entry.</p>"
        ),
    ],
    takeaways=[
        "The PTET election moves state tax to the entity, where the individual SALT cap does not reach it.",
        "Worth roughly $15,000 a year on $700,000 of income in a 6 percent state.",
        "Deadlines and estimated payment rules vary by state and a miss can invalidate the election.",
        "Sole proprietorships and disregarded single-member LLCs have no entity to make the election.",
        "Missed years generally cannot be recovered later, so it belongs on a planning calendar.",
    ],
    faqs=[
        (
            "What is a PTET election?",
            "<p>An election allowing a partnership or S-corp to pay state income tax at the "
            "entity level, where it is deductible as a business expense, instead of passing "
            "the liability to owners subject to the federal cap on state and local tax "
            "deductions. The IRS blessed the approach in Notice 2020-75.</p>",
        ),
        (
            "How much does a PTET election save?",
            "<p>Roughly the federal rate applied to the state tax that becomes deductible. On "
            "$700,000 of income in a 6 percent state that is about $15,000 annually; in a 9 "
            "percent state on $900,000 of income it is closer to $30,000.</p>",
        ),
        (
            "Can I make the election for a prior year?",
            "<p>Generally no. Most states require the election to be made contemporaneously, "
            "and several require estimated payments during the tax year. A missed year is "
            "usually permanently lost, which is why the deadline belongs on a planning "
            "calendar rather than being addressed at filing.</p>",
        ),
        (
            "Does the election ever make things worse?",
            "<p>It can in specific situations, particularly for owners with income in several "
            "states where the home state does not grant a resident credit for another state's "
            "entity-level tax, which can produce double taxation. Multi-state owners should "
            "have the interaction modeled before electing.</p>",
        ),
    ],
)

HOLDCO = Spoke(
    slug="holding-company-vs-operating-company",
    label="Holding company vs operating company",
    title="Holding Company vs Operating Company: How to Split Them",
    description=(
        "Why profitable businesses separate assets from operations, how the split is "
        "structured for tax, and the mistakes that collapse the separation."
    ),
    h1="Holding Company vs Operating Company",
    subtitle=(
        "Separating what you own from what you do, without breaking the tax treatment "
        "of either."
    ),
    lead=(
        "A holding company owns assets such as real estate, equipment, or intellectual "
        "property, and leases or licenses them to an operating company that runs the "
        "business. The structure isolates valuable assets from operating liability and lets "
        "each entity be taxed in the way that suits what it holds. It only works if the "
        "entities are genuinely separate in practice, not merely on paper."
    ),
    keywords=[
        "holding company operating company structure",
        "holdco opco structure tax",
        "separate real estate from business entity",
    ],
    body=[
        (
            "Why the Split Exists",
            "<p>Three reasons, in roughly this order of importance for a business at this "
            "level.</p>"
            "<p><strong>Liability isolation.</strong> Operating businesses generate claims. "
            "Assets held in a separate entity that is not party to those operations are "
            "harder to reach.</p>"
            "<p><strong>Tax treatment that fits the asset.</strong> Real estate belongs in a "
            "partnership or disregarded entity, where debt creates basis and appreciated "
            "property can be distributed without triggering gain. An operating business often "
            "belongs in an S-corp. Holding both in one entity forces a single treatment onto "
            "assets with very different needs.</p>"
            "<p><strong>Exit flexibility.</strong> A buyer usually wants the operating "
            "business, not the building. Separating them lets the operating company be sold "
            "while the property is retained and leased to the buyer.</p>"
        ),
        (
            "The Standard Structure",
            "<p>Most commonly: an LLC taxed as a partnership or disregarded holds the real "
            "estate, and an LLC or corporation taxed as an S-corp runs the operations. The "
            "holding company leases to the operating company at a market rate under a written "
            "lease.</p>"
            "<p>Rent is deductible to the operating company and taxable to the holding "
            "company, where it is offset by depreciation, interest, and operating expenses. "
            "Where a cost segregation study has been done, that depreciation frequently "
            "exceeds the rent, producing a loss.</p>"
        ),
        (
            "The Self-Rental Trap and the Grouping Election",
            "<p>This is where the structure most often goes wrong. Under the Section 469 "
            "regulations, net rental income from property leased to a business the taxpayer "
            "materially participates in is recharacterized as non-passive, so it cannot be "
            "sheltered by other passive losses. Meanwhile a net rental loss from the same "
            "arrangement generally remains passive and is suspended.</p>"
            "<p>That asymmetry is unhelpful: income is non-passive, losses are passive. The "
            "remedy is the grouping election, which allows the rental and the operating "
            "business to be treated as a single activity where they constitute an appropriate "
            "economic unit. Grouped, the depreciation from the property offsets the operating "
            "income directly.</p>"
            "<p>The election must be documented, and once made it generally cannot be changed "
            "without IRS consent. It should be decided when the structure is created rather "
            "than discovered after a cost segregation study has produced a loss nobody can "
            "use.</p>"
        ),
        (
            "Setting the Rent",
            "<p>Rent between related entities has to be defensible. Set too high, it strips "
            "income from the operating company and can be challenged under Section 482. Set "
            "too low, it understates the holding company's income and may fail to support the "
            "separation.</p>"
            "<p>The workable approach is a market rate supported by comparable local lease "
            "data, documented at the time the lease is signed, with a written lease on "
            "ordinary commercial terms and rent actually paid on schedule. A rate that "
            "changes each year to produce a target result is the pattern that draws "
            "challenge.</p>"
        ),
        (
            "What Collapses the Separation",
            "<p>The structure fails when the entities are separate on paper only:</p>"
            "<ul>"
            "<li>No written lease, or a lease that was never followed.</li>"
            "<li>Rent that accrues but is never actually paid.</li>"
            "<li>Commingled bank accounts, or the operating company paying the holding "
            "company's expenses directly.</li>"
            "<li>No separate books, filings, or minutes.</li>"
            "<li>The holding company carrying no insurance and having no independent "
            "existence.</li>"
            "</ul>"
            "<p>These failures undermine both purposes at once. A court asked to disregard the "
            "separation for liability purposes looks at the same facts an examiner looks at "
            "for tax purposes.</p>"
        ),
    ],
    takeaways=[
        "Separation lets real estate sit in a partnership while operations sit in an S-corp.",
        "Self-rental rules make income non-passive but leave losses passive, which is the wrong way round.",
        "The grouping election is what allows property depreciation to offset operating income.",
        "Rent must be a documented market rate, not a figure adjusted to hit a target result.",
        "Paper-only separation fails for both liability and tax; the facts examined are the same.",
    ],
    faqs=[
        (
            "Should I put my building in a separate LLC from my business?",
            "<p>Usually yes. It isolates the asset from operating liability, allows the "
            "property to be held in a partnership or disregarded entity where debt creates "
            "basis, and preserves the option to sell the business while retaining the "
            "property. The lease and the grouping election need to be handled deliberately.</p>",
        ),
        (
            "What is the self-rental rule?",
            "<p>Under the Section 469 regulations, net rental income from property leased to a "
            "business you materially participate in is recharacterized as non-passive, while a "
            "net loss from the same arrangement generally stays passive. The grouping election "
            "resolves the asymmetry by treating the two as one activity.</p>",
        ),
        (
            "How do I set rent between my own entities?",
            "<p>At a market rate supported by comparable local lease data, documented when the "
            "lease is signed, under a written lease on ordinary commercial terms, with rent "
            "actually paid on schedule. Rates adjusted annually to produce a target taxable "
            "income are what draw scrutiny under Section 482.</p>",
        ),
        (
            "Can I move my building into a new LLC now?",
            "<p>Often yes, and the tax consequences depend on current ownership. Moving "
            "property out of an S-corp or C-corp generally triggers gain as though it were "
            "sold, which can be expensive. Moving it between disregarded entities with the "
            "same owner is usually straightforward. Mortgage due-on-sale clauses and title "
            "insurance also need checking before any transfer.</p>",
        ),
    ],
)

DECISION_TREE = Spoke(
    slug="entity-restructuring-decision-tree",
    label="The entity restructuring decision tree",
    title="The Entity Restructuring Decision Tree",
    description=(
        "A sequenced set of questions that leads a profitable business owner to the "
        "right entity structure, and the costs of moving between them."
    ),
    h1="The Entity Restructuring Decision Tree",
    subtitle=(
        "Six questions, asked in order, that determine the structure. The order is "
        "what makes it work."
    ),
    lead=(
        "Entity restructuring decisions are usually made one question at a time, which is why "
        "they so often produce a structure nobody would have designed deliberately. Asking "
        "them in sequence produces a defensible answer, because each question constrains the "
        "next: what the assets are, what happens to the profit, how the owners share it, and "
        "what the exit looks like."
    ),
    keywords=[
        "entity restructuring decision",
        "how to choose business entity structure",
        "change business entity type tax",
    ],
    body=[
        (
            "Question 1: What Does the Entity Hold?",
            "<p>Start with the assets, because they impose the hardest constraints.</p>"
            "<p><strong>Appreciating real estate</strong> belongs in a partnership or "
            "disregarded LLC. Entity debt creates owner basis, which supports loss "
            "deductions, and property can be distributed without triggering gain. This is not "
            "a close call, and it is the constraint most often violated.</p>"
            "<p><strong>Operating assets and goodwill</strong> are flexible and the later "
            "questions decide their treatment.</p>"
            "<p><strong>Mixed holdings</strong> are the signal to split. One entity holding "
            "both the building and the operations forces a single tax treatment onto assets "
            "with opposite needs.</p>"
        ),
        (
            "Question 2: Is the Profit Distributed or Retained?",
            "<p><strong>Distributed</strong> points to a pass-through. There is no second "
            "layer of tax, and for an owner-operated business an S election limits payroll "
            "tax to wages.</p>"
            "<p><strong>Retained for growth</strong> opens the C-corp question. Retained "
            "income taxed at 21 percent rather than a personal rate above 37 percent leaves "
            "materially more to reinvest, provided it genuinely stays in the business.</p>"
            "<p>The common error is choosing C-corp status for the rate while continuing to "
            "take the money out, which reintroduces the second tax and produces the worst of "
            "both.</p>"
        ),
        (
            "Question 3: Do the Owners Share Pro Rata?",
            "<p><strong>Yes, strictly by ownership</strong> keeps an S election available.</p>"
            "<p><strong>No</strong> rules it out. Preferred returns, waterfall tiers, and "
            "special allocations are second classes of stock and are incompatible with "
            "Subchapter S. This is the most common reason an S election turns out to have "
            "been invalid from the beginning, usually because the operating agreement was "
            "never conformed.</p>"
        ),
        (
            "Question 4: Who Are the Owners?",
            "<p>Subchapter S restricts ownership to U.S. individuals and certain trusts and "
            "estates, capped at 100 shareholders. A partnership, a corporation, or a "
            "nonresident alien as owner rules out the election.</p>"
            "<p>Planned outside investment is the forward-looking version of this question. "
            "An entity intending to raise from institutional investors should not be building "
            "toward an S election it will have to terminate.</p>"
        ),
        (
            "Question 5: How Involved Is the Owner?",
            "<p><strong>Materially involved</strong> means most profit is a return on labor, "
            "so payroll tax exposure is large and an S election is worth its cost.</p>"
            "<p><strong>Largely passive</strong> means most profit is a return on capital. A "
            "passive owner's share is generally not subject to self-employment tax anyway, so "
            "the election buys little while imposing pro-rata distribution constraints on "
            "everyone.</p>"
        ),
        (
            "Question 6: What Is the Exit?",
            "<p><strong>Sale of the business</strong> raises Section 1202, which can exclude a "
            "substantial amount of gain on qualified small business stock held five years, "
            "but requires C-corp status and planning from formation. Buyers also generally "
            "prefer asset purchases, which are taxed differently across structures.</p>"
            "<p><strong>Transfer to family</strong> raises valuation and gifting "
            "considerations, where entity structure affects available discounts.</p>"
            "<p><strong>Hold indefinitely</strong> makes the step-up in basis at death "
            "relevant, which favors holding appreciating assets in pass-throughs rather than "
            "corporations.</p>"
        ),
        (
            "What Restructuring Costs",
            "<p>Moving between structures is not symmetric, and the asymmetry should inform "
            "the original choice:</p>"
            "<ul>"
            "<li><strong>Partnership to S-corp.</strong> Generally straightforward. Conform "
            "the operating agreement, confirm eligibility, file Form 2553.</li>"
            "<li><strong>Pass-through to C-corp.</strong> Generally manageable, though it "
            "should be modeled against the second layer of tax before proceeding.</li>"
            "<li><strong>C-corp to pass-through.</strong> Built-in gains tax applies for five "
            "years on appreciation that existed at conversion.</li>"
            "<li><strong>Property out of a corporation.</strong> Triggers gain as though sold "
            "at fair market value. This is the expensive direction, and the reason property "
            "should not be placed in a corporation to begin with.</li>"
            "</ul>"
        ),
    ],
    takeaways=[
        "Start with what the entity holds; appreciating real estate belongs in a partnership.",
        "Distributed profit points to a pass-through; genuinely retained profit opens the C-corp question.",
        "Any allocation that is not strictly pro rata rules out an S election.",
        "A largely passive owner gains little from an S election while constraining everyone.",
        "Property out of a corporation triggers gain, so avoid putting it there in the first place.",
    ],
    faqs=[
        (
            "How often should entity structure be reviewed?",
            "<p>Whenever the answers to these questions change: a significant shift in profit, "
            "adding or removing an owner, acquiring real estate, a change in whether profit is "
            "distributed or retained, or a planned sale. For a stable business, every two to "
            "three years is reasonable.</p>",
        ),
        (
            "What is the most common structural mistake?",
            "<p>Holding appreciating real estate in an S-corp or C-corp. It suspends losses "
            "because entity debt does not create basis, and it makes the property expensive to "
            "remove later, since distributing it triggers gain as though it were sold.</p>",
        ),
        (
            "Can I undo an S election?",
            "<p>Yes, by revocation with the consent of shareholders holding more than half the "
            "shares, subject to timing rules. A five-year waiting period generally applies "
            "before re-electing, so revocation should be modeled rather than treated as "
            "reversible.</p>",
        ),
        (
            "Do I need multiple entities?",
            "<p>Often, at this profit level. A common structure is an S-corp operating "
            "company, a partnership or disregarded LLC holding the real estate, and "
            "occasionally a C-corp for a specific retained-earnings or fringe-benefit purpose. "
            "Each entity should have an identifiable reason to exist; entities added without "
            "one create cost and audit surface without benefit.</p>",
        ),
    ],
)

CLUSTER = Cluster(
    key="entity",
    slug=P,
    label="Entity Structuring",
    title="Entity Structuring for Business Owners: The Complete Guide",
    description=(
        "How profitable business owners structure entities for tax: choosing between "
        "pass-through and corporate treatment, separating assets, and multi-entity design."
    ),
    h1="Entity Structuring for Business Owners",
    subtitle=(
        "The structure decides what every other strategy can do. Getting it wrong "
        "constrains everything downstream."
    ),
    lead=(
        "Entity structuring is the design of the legal entities a business operates through "
        "and the tax classifications they elect. For a business earning $500,000 or more, "
        "the structure determines how much profit is exposed to payroll tax, whether "
        "depreciation losses are usable, what retirement plan capacity exists, and what the "
        "eventual sale is taxed at. It is the first decision because it constrains every "
        "decision after it."
    ),
    keywords=[
        "entity structuring business owners",
        "business entity structure tax strategy",
        "multi entity structure high income",
        "llc s corp c corp structure",
    ],
    body=[
        (
            "Why Structure Comes First",
            "<p>Entity structure is not one strategy among several. It is the container the "
            "others operate inside, and it sets their limits.</p>"
            "<p>The entity classification determines whether profit is exposed to "
            "self-employment tax in full or only on wages. The wage figure that follows "
            "determines retirement plan contribution capacity, because plan limits are driven "
            "by W-2 compensation. Whether debt creates owner basis determines whether "
            "depreciation losses are deductible or suspended. Whether the entity is a "
            "pass-through determines whether a state PTET election is even available.</p>"
            "<p>Every one of those is a structural consequence. An owner who optimizes "
            "retirement contributions or commissions a cost segregation study before settling "
            "the structure is optimizing inside constraints they have not chosen "
            "deliberately.</p>"
        ),
        (
            "The Three Tax Treatments",
            "<p>Setting aside legal form, there are three ways business profit is taxed.</p>"
            "<p><strong>Default pass-through.</strong> Profit flows to owners and is taxed "
            "personally. An active owner's full share is generally subject to self-employment "
            "tax. Owners get basis from entity debt, and allocations need not follow "
            "ownership percentages.</p>"
            "<p><strong>Subchapter S.</strong> Profit still flows through, but only wages "
            "carry Social Security and Medicare tax. The costs are a payroll requirement, a "
            "reasonable compensation analysis, strictly pro-rata distributions, shareholder "
            "eligibility limits, and no basis from entity debt.</p>"
            "<p><strong>Subchapter C.</strong> The corporation pays 21 percent on its income "
            "and distributions are taxed again to shareholders. This suits retained earnings "
            "and opens broader fringe benefit deductions and, in some cases, Section 1202 "
            "treatment at exit.</p>"
        ),
        (
            "The Real Estate Rule That Governs Everything",
            "<p>If one principle drives more structural decisions than any other, it is this: "
            "appreciating real estate does not belong in a corporation.</p>"
            "<p>Two reasons. Partnership rules include a partner's share of entity debt in "
            "basis, which is what allows the depreciation losses real estate generates to be "
            "deducted. S-corp shareholders receive no basis from entity borrowings, so those "
            "losses are frequently suspended. And distributing appreciated property out of a "
            "corporation triggers gain as though it had been sold, which means a structural "
            "mistake made at formation becomes expensive to correct years later.</p>"
            "<p>This is why the standard structure for a profitable business that owns its "
            "premises is two entities: a partnership or disregarded LLC holding the property, "
            "and a separate operating entity, usually an S-corp, running the business.</p>"
        ),
        (
            "Separating Assets From Operations",
            "<p>The holding company and operating company split serves three purposes at "
            "once: it isolates valuable assets from operating liability, it lets each entity "
            "be taxed appropriately for what it holds, and it preserves the ability to sell "
            "the business while retaining the property.</p>"
            "<p>The tax mechanics require care. Under the self-rental rules in the Section 469 "
            "regulations, net rental income from property leased to a business the owner "
            "materially participates in is recharacterized as non-passive, while a net rental "
            "loss from the same arrangement generally stays passive and is suspended. That "
            "asymmetry runs against the owner.</p>"
            "<p>The grouping election resolves it by treating the rental and the operating "
            "business as a single activity where they form an appropriate economic unit. "
            "Grouped, depreciation from the property offsets operating income directly. The "
            "election needs to be documented and is difficult to change later, so it belongs "
            "in the structural design rather than in a later scramble.</p>"
        ),
        (
            "When a Second or Third Entity Earns Its Place",
            "<p>Multi-entity structures are frequently oversold. Each additional entity adds "
            "a return, a set of books, a bank account, and audit surface. The test is whether "
            "it has an identifiable purpose beyond appearing sophisticated.</p>"
            "<p>Purposes that justify an entity:</p>"
            "<ul>"
            "<li>Holding real estate separately from operations, for liability and tax "
            "treatment.</li>"
            "<li>Isolating a genuinely distinct line of business with its own risk profile "
            "or ownership.</li>"
            "<li>A C-corp for earnings actually being retained, or for fringe benefits "
            "unavailable to pass-through owners.</li>"
            "<li>Centralizing administration where an owner runs several businesses that all "
            "need it.</li>"
            "<li>Holding equipment separately where it is leased across entities.</li>"
            "</ul>"
            "<p>Purposes that do not: creating deductions by moving money between entities "
            "the owner controls, or adding layers with no operational reality. Related-party "
            "arrangements without genuine substance are exactly what Section 482 exists to "
            "reallocate.</p>"
        ),
        (
            "The Operating Agreement Problem",
            "<p>The most common way a structure fails is not the choice of entity. It is that "
            "the governing document contradicts the tax election.</p>"
            "<p>A standard LLC operating agreement is drafted for partnership taxation, and "
            "very often contains special allocations, preferred returns, waterfall "
            "distribution tiers, or capital account provisions written under the Section "
            "704(b) rules. Each of those creates differing rights to distribution, which is a "
            "second class of stock and is incompatible with Subchapter S.</p>"
            "<p>An LLC that files an S election without conforming its agreement may have an "
            "invalid election from day one, typically discovered years later during diligence "
            "or examination. The agreement is amended to a straight pro-rata distribution "
            "provision before Form 2553 is filed, not afterward.</p>"
        ),
        (
            "State-Level Consequences",
            "<p>Federal classification is only part of the analysis. Some states impose "
            "entity-level taxes on S-corps, a few do not recognize the federal election, and "
            "franchise or gross receipts taxes may apply per entity, so each additional entity "
            "carries a recurring state cost.</p>"
            "<p>More significantly, the pass-through entity tax election is available only to "
            "actual pass-through entities. A sole proprietorship or a disregarded "
            "single-member LLC has nothing to make the election with. For an owner in a "
            "high-tax state, that alone can justify forming an entity that makes the election "
            "possible, because the annual benefit frequently exceeds the cost of the "
            "structure.</p>"
        ),
        (
            "Three Structures We See Regularly, and What Is Wrong With Them",
            "<p><strong>The single LLC holding everything.</strong> One entity owns the "
            "building, runs the operations, and holds the equipment. It is simple, and it "
            "forces one tax treatment onto assets with opposite requirements. If it has "
            "elected S status, the real estate is in the wrong place: losses are suspended "
            "for lack of basis, and the property cannot be moved out later without triggering "
            "gain. The fix is to separate the property, and the cost of that fix rises with "
            "every year of appreciation.</p>"
            "<p><strong>The S-corp with an unconformed operating agreement.</strong> The "
            "election was filed, payroll runs, distributions are made, and the operating "
            "agreement still contains the preferred return negotiated when a second owner "
            "joined. The election may have been invalid from the start. This surfaces during "
            "diligence, at the worst possible moment, and the remedy involves relief "
            "procedures rather than a simple amendment.</p>"
            "<p><strong>The entity stack with no purpose.</strong> Four or five entities, "
            "often assembled from a seminar, with management fees flowing between them and no "
            "documented services behind the fees. Each entity costs a return and a set of "
            "books, and the intercompany charges are exactly what Section 482 exists to "
            "reallocate. Complexity is not a strategy; the entities that survive review are "
            "the ones with an identifiable reason to exist.</p>"
        ),
        (
            "Sequencing a Restructure",
            "<p>Restructuring is done in an order that avoids creating tax on the way to "
            "saving it. Confirm what each entity holds and what it is worth, because moving "
            "appreciated assets is where the cost lives. Model the destination structure "
            "against the current one over several years rather than one. Conform governing "
            "documents before filing any election. Establish payroll and the compensation "
            "file before the first distribution under the new structure. Then file the "
            "elections, and document the grouping and PTET positions in the same pass.</p>"
            "<p>Entity changes generally take effect the following tax year, so a restructure "
            "decided in the third quarter is a decision for next year. That is not a reason "
            "to defer it. It is the reason to start it before year-end rather than during "
            "filing season, when the year it would have applied to has already closed.</p>"
        ),
        (
            "How Structure Determines the Exit",
            "<p>Structural decisions made now set the tax treatment of a sale years later, "
            "and they are difficult to reverse near the transaction.</p>"
            "<p>Section 1202 can exclude a substantial amount of gain on qualified small "
            "business stock, but requires C-corp status, original issuance, a qualifying trade "
            "or business, and a five-year holding period. It cannot be arranged shortly before "
            "a sale.</p>"
            "<p>Buyers generally prefer to purchase assets rather than equity, which is taxed "
            "differently depending on structure and can produce a second layer of tax in a "
            "C-corp. And where property is held separately from operations, the business can "
            "be sold while the real estate is retained and leased to the buyer, which is often "
            "the most valuable flexibility the split provides.</p>"
            "<p>For an owner intending to hold rather than sell, a different consideration "
            "applies. Assets held in a pass-through generally receive a step-up in basis at "
            "death, which can eliminate the built-in gain entirely for heirs. Assets locked "
            "inside a corporation do not receive the same treatment at the entity level, which "
            "is one more reason appreciating property is held outside a corporation.</p>"
        ),
    ],
    takeaways=[
        "Structure is the container every other strategy operates inside, so it is settled first.",
        "Appreciating real estate belongs in a partnership or disregarded LLC, never a corporation.",
        "The standard structure for an owner-occupied business is a property entity plus an operating entity.",
        "The grouping election is what makes property depreciation offset operating income.",
        "An operating agreement that was never conformed is the most common cause of invalid S elections.",
        "Section 1202 requires C-corp status and a five-year hold, so exit planning starts at formation.",
    ],
    faqs=[
        (
            "What is the best entity structure for a business making $500,000?",
            "<p>For an owner-operated business distributing its profit, an LLC or corporation "
            "taxed as an S-corp is usually correct. If the business owns its premises, the "
            "standard structure adds a separate partnership or disregarded LLC to hold the "
            "property. The right answer depends on whether profit is distributed or retained, "
            "how owners share it, and the intended exit.</p>",
        ),
        (
            "Should real estate be in the same entity as my business?",
            "<p>No. Appreciating property belongs in a partnership or disregarded LLC, where "
            "entity debt creates owner basis and property can be distributed without "
            "triggering gain. Holding it in the operating S-corp suspends losses and makes the "
            "property expensive to remove later.</p>",
        ),
        (
            "How many entities do I actually need?",
            "<p>As many as have an identifiable purpose, and no more. Two is common: an "
            "operating entity and a property-holding entity. A third is justified by a "
            "genuinely distinct business line, retained earnings in a C-corp, or centralized "
            "administration across several businesses. Entities added without a purpose "
            "create cost and audit surface.</p>",
        ),
        (
            "What is the grouping election and why does it matter?",
            "<p>It allows a rental activity and an operating business to be treated as a "
            "single activity where they form an appropriate economic unit. Without it, the "
            "self-rental rules make rental income non-passive while leaving rental losses "
            "passive and suspended. With it, depreciation from the property offsets operating "
            "income. It must be documented and is difficult to change later.</p>",
        ),
        (
            "Can my operating agreement invalidate my S election?",
            "<p>Yes, and it is the most common cause. Special allocations, preferred returns, "
            "or waterfall distribution tiers create differing rights to distribution, which is "
            "a second class of stock and is not permitted under Subchapter S. The agreement "
            "must be conformed to pro-rata distributions before Form 2553 is filed.</p>",
        ),
        (
            "Is a C-corp ever right for a $500K business?",
            "<p>Where earnings are genuinely being retained to fund growth, or where Section "
            "1202 treatment at exit is being planned for from the outset. It is generally "
            "wrong for an owner taking the profit out, because the dividend tax reintroduces "
            "the second layer the 21 percent rate was meant to avoid.</p>",
        ),
        (
            "Does entity structure affect my retirement plan?",
            "<p>Substantially. Contribution capacity is driven by W-2 compensation, so the "
            "entity classification and the wage figure it produces set the ceiling on what can "
            "be contributed. This is one of the main reasons structure is settled before plan "
            "design rather than alongside it.</p>",
        ),
        (
            "How much does restructuring cost?",
            "<p>The direction matters more than the fee. Moving from a partnership to an "
            "S-corp is generally straightforward. Converting a C-corp to a pass-through "
            "triggers built-in gains tax for five years, and moving appreciated property out "
            "of a corporation triggers gain as though sold. Our advisory engagement, which "
            "includes the structural analysis, is $7,800, with entity returns at $1,500 each.</p>",
        ),
    ],
    spokes=[
        THREE_WAY,
        MGMT_CO,
        Spoke(
            slug=(
                "eliminating-federal-income-tax-through-multi-entity-structuring-"
                "reimbursement-stacking-depreciation-and-credits"
            ),
            label="Multi-entity tax optimization",
            adopted=True,
        ),
        PTET,
        HOLDCO,
        DECISION_TREE,
    ],
)
