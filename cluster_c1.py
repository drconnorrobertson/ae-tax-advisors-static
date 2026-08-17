#!/usr/bin/env python3
"""Cluster 1: S-Corp tax strategy.

Pillar plus supporting posts. Topics the site already ranks for are adopted
rather than rewritten; see cluster_common for why.
"""

from __future__ import annotations

from cluster_common import Cluster, Spoke

P = "s-corp-tax-strategy"

# ---------------------------------------------------------------------------
# New supporting posts
# ---------------------------------------------------------------------------

AUDIT_TRIGGERS = Spoke(
    slug="s-corp-officer-compensation-audit-triggers",
    label="S-Corp officer compensation audit triggers",
    title="S-Corp Officer Compensation Audit Triggers: What the IRS Looks For",
    description=(
        "The specific patterns that make the IRS reclassify S-corp distributions as "
        "wages, and how profitable businesses document compensation to survive review."
    ),
    h1="S-Corp Officer Compensation Audit Triggers",
    subtitle=(
        "Reclassification is the most common S-corp adjustment the IRS makes. "
        "These are the patterns that draw it and the file that defeats it."
    ),
    lead=(
        "An S-corp officer compensation audit trigger is a reporting pattern that suggests "
        "a shareholder-employee took profit as distributions instead of wages to avoid "
        "payroll tax. The IRS does not need a new statute to adjust it: under IRC Section "
        "3121(d) and a long line of cases beginning with Revenue Ruling 74-44, it can "
        "recharacterize distributions as wages and assess the payroll tax, interest, and "
        "penalties that should have been paid."
    ),
    keywords=[
        "s corp officer compensation audit",
        "s corp reasonable compensation audit trigger",
        "irs reclassify distributions as wages",
    ],
    body=[
        (
            "Why This Adjustment Is So Common",
            "<p>Reclassifying distributions as wages is close to an ideal audit for the "
            "IRS. The adjustment is mechanical, the authority is settled, and the facts "
            "are usually sitting on the face of the return. The examiner does not have to "
            "value anything exotic. They compare the officer compensation line on the "
            "1120-S against the ordinary business income being distributed, and if the "
            "ratio looks wrong, the file opens.</p>"
            "<p>The consequences compound. A reclassification does not just add payroll "
            "tax. It changes the W-2, which changes the personal return, which can change "
            "the Section 199A deduction, which can change the state return. One adjustment "
            "at the entity level cascades through several years of filings.</p>"
        ),
        (
            "Trigger One: Zero or Token Officer Compensation",
            "<p>The single loudest signal is an 1120-S reporting meaningful ordinary "
            "business income with zero on the officer compensation line. There is no "
            "credible fact pattern where a shareholder who materially runs a profitable "
            "business performs no services. Courts have consistently refused to accept "
            "that framing.</p>"
            "<p>Token compensation is the same problem with a smaller number attached. A "
            "shareholder taking $30,000 in salary out of an $800,000 profit is asserting "
            "that their labor is worth less than four percent of what the business "
            "produced. That is a position that has to be defended with facts, and in most "
            "practices it cannot be.</p>"
        ),
        (
            "Trigger Two: Distributions That Track Payroll Timing",
            "<p>Examiners look at the rhythm of the money, not only the totals. When "
            "distributions land on a regular biweekly or monthly cadence in consistent "
            "amounts, they function as a paycheck regardless of what the ledger calls "
            "them. Genuine distributions are periodic and tied to available cash and "
            "capital needs; they do not usually arrive every other Friday.</p>"
        ),
        (
            "Trigger Three: The Ratio Falls Outside Practice Norms",
            "<p>There is no statutory safe-harbor percentage, and any advisor quoting a "
            "flat rule such as a 60/40 split as though it were law is describing a "
            "convention, not authority. That said, examiners do work from comparables. A "
            "compensation figure far below what the same role commands in the open market "
            "for a business of that size invites the question of how it was derived.</p>"
            "<p>The useful discipline is to reason from the role rather than the ratio. "
            "What would it cost to hire someone to do what the shareholder actually does, "
            "at the hours the shareholder actually works, in that market?</p>"
        ),
        (
            "Trigger Four: Loans to Shareholder That Never Repay",
            "<p>A shareholder loan account that grows every year and is never serviced is "
            "treated as what it is. Without a note, a stated rate, and an actual repayment "
            "history, the balance is recharacterized as compensation or distribution. This "
            "is a common way profitable businesses accidentally create the exact exposure "
            "they were trying to avoid.</p>"
        ),
        (
            "Trigger Five: The Compensation Number Has No Derivation",
            "<p>The most damaging fact at examination is not a low number. It is a number "
            "with no explanation behind it. When the only answer to how compensation was "
            "set is that the prior accountant chose it, the taxpayer has no position to "
            "argue and the examiner's figure becomes the default.</p>"
        ),
        (
            "The File That Actually Defends the Position",
            "<p>A defensible compensation figure is documented before the year begins, not "
            "reconstructed after a notice arrives. At minimum the file should contain:</p>"
            "<ul>"
            "<li>A written description of the shareholder's actual duties, separated into "
            "the roles being performed, such as operations, sales, and management.</li>"
            "<li>Third-party market data for those roles in that geography, from a "
            "compensation survey or a documented industry source, with the date pulled.</li>"
            "<li>An estimate of hours devoted to the business, and to each role.</li>"
            "<li>An explicit allocation between the return on labor and the return on "
            "invested capital, since only the labor component is wages.</li>"
            "<li>Board or member minutes adopting the figure for the coming year.</li>"
            "<li>Payroll records showing the figure was actually paid and reported.</li>"
            "</ul>"
            "<p>The point of the file is not that it produces a high number. It is that it "
            "produces a derived number. A derived number that an examiner disagrees with is "
            "a negotiation. An undocumented number is a concession.</p>"
        ),
        (
            "What Happens If the IRS Wins",
            "<p>On reclassification, the reclassified amount becomes wages subject to "
            "Social Security and Medicare tax at the combined employer and employee rate, "
            "plus the Additional Medicare Tax where the income threshold is crossed. On top "
            "of the tax come failure-to-deposit penalties, failure-to-file penalties on the "
            "corrected employment tax returns, and interest running from the original due "
            "dates. Because employment tax returns are filed quarterly, a multi-year "
            "adjustment generates a long series of penalty computations.</p>"
        ),
    ],
    takeaways=[
        "Zero or token officer compensation on a profitable 1120-S is the loudest trigger there is.",
        "Distributions paid on a payroll-like cadence read as wages regardless of labeling.",
        "No statutory safe-harbor percentage exists; reason from the role, not from a ratio.",
        "An undocumented compensation figure is not a weak position, it is no position.",
        "Build the compensation file before the year starts, not after a notice arrives.",
    ],
    faqs=[
        (
            "Is there a safe percentage split between salary and distributions?",
            "<p>No. No statute, regulation, or ruling establishes a percentage safe harbor. "
            "Conventions such as 60/40 circulate widely but have no authority behind them. "
            "The standard is reasonable compensation for services actually rendered, which "
            "is a facts-and-circumstances test derived from the role, the hours, and the "
            "market rate.</p>",
        ),
        (
            "How far back can the IRS reclassify compensation?",
            "<p>The general assessment period is three years from the filing of the return. "
            "That extends to six years for a substantial omission of income and is unlimited "
            "where no return was filed or fraud is present. Because employment tax filings "
            "are quarterly, an adjustment across open years typically touches twelve or more "
            "separate returns.</p>",
        ),
        (
            "Does paying a high salary eliminate the risk?",
            "<p>It eliminates the reclassification risk but usually overshoots the point of "
            "the election. Compensation above a defensible level converts income that would "
            "have escaped Social Security and Medicare tax into wages that do not, which is "
            "the cost the S-corp structure exists to manage. The goal is the defensible "
            "figure, not the highest one.</p>",
        ),
        (
            "Do shareholder loans really get reclassified?",
            "<p>Routinely, when they lack the features of a real loan. A promissory note, a "
            "stated interest rate at or above the applicable federal rate, a repayment "
            "schedule, and an actual history of repayment are what distinguish a loan from a "
            "disguised distribution. A balance that only ever grows is not a loan.</p>",
        ),
        (
            "What if a prior accountant set the number and we cannot justify it?",
            "<p>That is a fixable position, but it is fixed prospectively. Establish a "
            "documented, derived figure for the coming year and consider whether prior open "
            "years should be corrected voluntarily. Correcting on your own terms is "
            "materially cheaper than being corrected on examination.</p>",
        ),
    ],
)

MULTI_MEMBER_LLC = Spoke(
    slug="multi-member-llc-taxed-as-s-corp",
    label="Multi-member LLC taxed as an S-corp",
    title="Multi-Member LLC Taxed as an S-Corp: When It Works and When It Breaks",
    description=(
        "How a multi-member LLC elects S-corp treatment, the eligibility traps that "
        "invalidate the election, and when partnership taxation is the better answer."
    ),
    h1="Multi-Member LLC Taxed as an S-Corp",
    subtitle=(
        "The election can cut payroll tax across several owners at once. It also "
        "imposes rules a partnership never had to follow."
    ),
    lead=(
        "A multi-member LLC taxed as an S-corp is a limited liability company that keeps "
        "its state-law LLC form but elects, on Form 2553, to be taxed under Subchapter S "
        "instead of as a partnership. The appeal is that only amounts paid as wages carry "
        "payroll tax, while a partnership generally exposes an active member's full "
        "distributive share to self-employment tax. The cost is that the LLC must then "
        "satisfy S-corp eligibility rules that partnerships are free to ignore."
    ),
    keywords=[
        "multi member llc taxed as s corp",
        "llc s corp election multiple owners",
        "partnership vs s corp llc",
    ],
    body=[
        (
            "What the Election Actually Changes",
            "<p>Nothing changes at the state level. The entity remains an LLC, the "
            "operating agreement still governs, and liability protection is unaffected. "
            "What changes is the federal tax classification and, with it, how each owner's "
            "share of profit is exposed to payroll tax.</p>"
            "<p>In a partnership, a general or actively participating member's distributive "
            "share is generally subject to self-employment tax in full. Under Subchapter S, "
            "the entity pays each owner-operator a reasonable wage that carries Social "
            "Security and Medicare tax, and the remaining profit passes through as a "
            "distribution that does not. With several active owners, that difference "
            "multiplies across all of them.</p>"
        ),
        (
            "The Eligibility Rules That Break the Election",
            "<p>Subchapter S is a narrow regime. An LLC that elects into it has to satisfy "
            "every one of these, continuously:</p>"
            "<ul>"
            "<li><strong>One class of stock.</strong> All ownership interests must confer "
            "identical rights to distribution and liquidation proceeds.</li>"
            "<li><strong>Eligible owners only.</strong> Individuals who are U.S. citizens or "
            "residents, plus certain estates and qualifying trusts. Partnerships, "
            "corporations, and nonresident alien individuals are not permitted.</li>"
            "<li><strong>No more than 100 shareholders</strong>, with family attribution "
            "rules allowing certain relatives to be counted as one.</li>"
            "</ul>"
            "<p>The one-class-of-stock rule is where most multi-member LLCs fail, and they "
            "usually fail on a document they forgot they signed.</p>"
        ),
        (
            "The Operating Agreement Problem",
            "<p>A standard LLC operating agreement is written for partnership taxation. It "
            "very often contains special allocations, preferred returns, waterfall "
            "distribution tiers, or capital account maintenance provisions drafted under "
            "the Section 704(b) rules. Every one of those creates rights to distribution "
            "that differ between members, and each is a second class of stock.</p>"
            "<p>An LLC that elects S status without conforming its operating agreement can "
            "have an invalid election from the first day, which is typically discovered "
            "years later during diligence or examination. The remedy is to amend the "
            "agreement to a straight pro-rata distribution provision before filing Form "
            "2553, not after.</p>"
        ),
        (
            "Where the Election Pays Off",
            "<p>The structure works best with a specific profile: several owners who all "
            "work in the business, similar economic arrangements between them, profit "
            "meaningfully above what the owners would be paid as employees, and no outside "
            "investor requiring preferred economics.</p>"
            "<p>A three-owner professional services firm with equal thirds and equal "
            "involvement is close to the ideal case. Each owner takes a documented "
            "reasonable wage, the residual profit is distributed pro rata, and the payroll "
            "tax saved is realized three times over rather than once.</p>"
        ),
        (
            "Where Partnership Taxation Wins",
            "<p>Several common arrangements are simply better off staying a partnership:</p>"
            "<ul>"
            "<li><strong>Unequal contribution and effort.</strong> Partnerships can allocate "
            "profit disproportionately to reflect who brought capital and who brought labor. "
            "S-corps cannot; everything is strictly pro rata to ownership.</li>"
            "<li><strong>Real estate holding entities.</strong> Partnerships allow debt to be "
            "included in a partner's basis, which supports loss deductions. S-corp "
            "shareholders get no basis from entity-level debt they have not personally lent. "
            "This difference alone disqualifies most property-holding LLCs.</li>"
            "<li><strong>Passive or investor members.</strong> A member who does not work in "
            "the business already avoids self-employment tax on their share, so the "
            "election buys them nothing while imposing constraints on everyone.</li>"
            "<li><strong>Planned outside investment.</strong> Anything requiring preferred "
            "returns or an entity investor is incompatible with Subchapter S.</li>"
            "</ul>"
        ),
        (
            "Making the Election Correctly",
            "<p>The election is made on Form 2553, signed by every owner. To apply to a "
            "given tax year, it is generally due within two months and fifteen days after "
            "the start of that year, or at any point in the preceding year. Late elections "
            "can often be repaired under Revenue Procedure 2013-30 where there was "
            "reasonable cause and the entity has otherwise behaved consistently with S "
            "status.</p>"
            "<p>The correct sequence matters: conform the operating agreement, confirm every "
            "owner is an eligible shareholder, establish payroll before the first "
            "distribution, then file the election.</p>"
        ),
    ],
    takeaways=[
        "The election changes federal tax treatment only; LLC status and liability protection are untouched.",
        "Special allocations and preferred returns are a second class of stock and void the election.",
        "Amend the operating agreement to pro-rata distributions before filing Form 2553.",
        "Entity-level debt does not create S-corp basis, which rules out most real estate LLCs.",
        "The structure suits several equally involved owners, not passive or unequal ones.",
    ],
    faqs=[
        (
            "Can a multi-member LLC elect S-corp status?",
            "<p>Yes, by filing Form 2553 signed by all owners, provided the LLC meets the "
            "Subchapter S eligibility rules: one class of stock, no more than 100 "
            "shareholders, and only eligible owners, meaning U.S. individuals and certain "
            "trusts and estates.</p>",
        ),
        (
            "Does a preferred return void the S election?",
            "<p>Generally yes. A preferred return gives one member a different right to "
            "distribution than another, which is a second class of stock and is not "
            "permitted. The operating agreement must be conformed to pro-rata distributions "
            "before the election is filed.</p>",
        ),
        (
            "Should a real estate LLC elect S-corp status?",
            "<p>Usually not. Partnership rules allow entity-level debt to be included in a "
            "partner's basis, which supports the loss deductions real estate generates. "
            "S-corp shareholders receive no basis from entity debt, so losses are often "
            "suspended. Property held in an S-corp is also difficult to distribute without "
            "triggering gain.</p>",
        ),
        (
            "Can members be paid differently under an S election?",
            "<p>Wages can differ, because wages compensate services actually performed. "
            "Distributions cannot; they must be strictly proportionate to ownership. Using "
            "wages to reflect genuinely different roles is legitimate. Using them to "
            "recreate a special allocation is not.</p>",
        ),
        (
            "What happens if the election was invalid from the start?",
            "<p>The entity is treated as having been a partnership or corporation for the "
            "affected years, which can unwind reported payroll and distribution treatment. "
            "The IRS has relief procedures for inadvertent terminations under Section "
            "1362(f), but relief requires prompt correction once discovered.</p>",
        ),
    ],
)

QBI_MAX = Spoke(
    slug="s-corp-qbi-deduction-maximization",
    label="S-Corp QBI deduction maximization",
    title="S-Corp QBI Deduction Maximization: Tuning Wages Against Section 199A",
    description=(
        "Officer wages cut payroll tax but also cut QBI. How profitable S-corps find "
        "the compensation level that optimizes both at once under Section 199A."
    ),
    h1="S-Corp QBI Deduction Maximization",
    subtitle=(
        "Every dollar of officer wage saves income tax and costs QBI. Above the "
        "income thresholds, wages start creating the deduction instead."
    ),
    lead=(
        "S-corp QBI maximization is the process of setting officer compensation at the "
        "level that produces the largest combined benefit from the Section 199A qualified "
        "business income deduction and the payroll tax structure. It matters because wages "
        "cut both ways: they reduce the qualified business income the deduction is computed "
        "on, but above the income thresholds they are also what unlocks the deduction "
        "through the W-2 wage limitation."
    ),
    keywords=[
        "s corp qbi deduction",
        "section 199a s corp wages",
        "qbi w2 wage limitation",
    ],
    body=[
        (
            "The Two Regimes of Section 199A",
            "<p>Section 199A behaves as two different rules depending on where taxable "
            "income falls relative to the annual thresholds, which are indexed each year.</p>"
            "<p><strong>Below the threshold</strong>, the deduction is simply 20 percent of "
            "qualified business income, with no wage test at all. Officer wages are pure "
            "cost in this range: every dollar moved from distribution to wage reduces QBI by "
            "a dollar, cutting the deduction by twenty cents, and adds payroll tax on top.</p>"
            "<p><strong>Above the threshold</strong>, the deduction is capped at the greater "
            "of 50 percent of the business's W-2 wages, or 25 percent of W-2 wages plus 2.5 "
            "percent of the unadjusted basis of qualified property. Here wages are what "
            "creates deduction capacity. A business paying no wages has a cap of zero and "
            "gets no deduction at all, regardless of how profitable it is.</p>"
        ),
        (
            "Why the Optimum Is a Curve, Not a Rule",
            "<p>Above the threshold the two effects run in opposite directions. Raising "
            "wages lifts the wage cap, which can increase the allowable deduction. It also "
            "lowers QBI, which lowers the twenty percent figure the cap is being applied to. "
            "The benefit rises, peaks, and then falls.</p>"
            "<p>Under the 50-percent-of-wages test, the two lines cross when W-2 wages reach "
            "roughly two-sevenths of the business's pre-wage profit. Below that point the "
            "wage cap is binding and additional wages help. Above it, the cap is no longer "
            "the constraint and additional wages only shrink QBI while adding payroll tax. "
            "That crossing point is the mathematical target, and the reasonable compensation "
            "requirement is the floor it has to respect.</p>"
        ),
        (
            "The Specified Service Business Problem",
            "<p>A specified service trade or business, which includes health, law, "
            "accounting, consulting, financial services, athletics, performing arts, and any "
            "business whose principal asset is the reputation or skill of its owners, is "
            "treated differently. Once taxable income passes the threshold, the SSTB "
            "deduction phases out over a defined range and then disappears entirely.</p>"
            "<p>For an SSTB owner fully above the phase-out, no amount of wage tuning "
            "restores the deduction, and the optimization question changes completely. The "
            "lever becomes reducing taxable income below the phase-out range through "
            "retirement plan contributions, depreciation, or entity separation, rather than "
            "adjusting the wage line.</p>"
        ),
        (
            "Aggregation and Separating the Non-Service Business",
            "<p>Where a practice has genuinely distinct non-service operations, such as a "
            "real estate holding entity leasing premises to the practice or an administrative "
            "services company, those operations may qualify for their own QBI treatment even "
            "when the service business does not.</p>"
            "<p>This is legitimate when the separated business is real: it has its own "
            "economics, its own contracts, and terms that would hold up between unrelated "
            "parties. It is not legitimate when it exists only to relabel service income. "
            "The regulations contain specific anti-abuse rules aimed at exactly that, "
            "including rules that treat income from a related party as tainted where the "
            "arrangement is principally a device.</p>"
        ),
        (
            "How the Retirement Plan Interacts",
            "<p>Retirement plan contributions reduce taxable income, which can pull an owner "
            "back below the threshold or the SSTB phase-out. This is often the highest-value "
            "move available to a service business owner, because it can restore a deduction "
            "that wage tuning alone cannot reach.</p>"
            "<p>The interaction runs both ways and has to be modeled together. Employer "
            "contributions reduce QBI at the entity level, while the deduction on the "
            "personal return reduces taxable income used for the threshold test. Modeling "
            "the compensation figure, the plan design, and the deduction in isolation "
            "reliably produces the wrong answer.</p>"
        ),
        (
            "The Order of Operations That Works",
            "<p>The sequence matters more than any single input:</p>"
            "<ol>"
            "<li>Determine the reasonable compensation floor from the role and market data. "
            "This is not negotiable and it constrains everything downstream.</li>"
            "<li>Project taxable income and locate it against the current thresholds, "
            "including the SSTB phase-out range if applicable.</li>"
            "<li>If below the threshold, keep wages at the documented floor.</li>"
            "<li>If above and not an SSTB, solve for the wage level where the W-2 cap stops "
            "binding, then take the higher of that figure and the floor.</li>"
            "<li>If above and an SSTB, shift the work to reducing taxable income rather than "
            "tuning wages.</li>"
            "<li>Re-run the model with retirement plan contributions included, since they "
            "move the threshold test.</li>"
            "</ol>"
        ),
    ],
    takeaways=[
        "Below the income thresholds there is no wage test, so wages only reduce the QBI deduction.",
        "Above the thresholds, W-2 wages create the deduction capacity; zero wages means a zero cap.",
        "Under the 50-percent test the optimum sits near wages equal to two-sevenths of pre-wage profit.",
        "Reasonable compensation is a floor on the optimization, never something the math overrides.",
        "For SSTB owners above the phase-out, reducing taxable income beats tuning the wage line.",
    ],
    faqs=[
        (
            "Do S-corp wages increase or decrease the QBI deduction?",
            "<p>Both, depending on income level. Wages always reduce qualified business "
            "income dollar for dollar. Above the taxable income thresholds they also raise "
            "the W-2 wage limitation, which can increase the allowable deduction by more "
            "than the QBI reduction costs. Below the thresholds no wage test applies, so the "
            "effect is purely negative.</p>",
        ),
        (
            "What is the optimal wage level for QBI purposes?",
            "<p>Where the 50-percent-of-W-2-wages test governs, the benefit peaks near wages "
            "equal to two-sevenths of pre-wage profit. That figure is only a target, not a "
            "conclusion: the documented reasonable compensation amount is a floor, and if it "
            "sits above the calculated optimum, it controls.</p>",
        ),
        (
            "Can an S-corp owner in a service business still claim QBI?",
            "<p>Yes, if taxable income stays below the specified service business phase-out "
            "range. Within the range the deduction is reduced proportionally, and above it "
            "the deduction is unavailable for the service income. Reducing taxable income "
            "with retirement contributions or depreciation is the usual route back.</p>",
        ),
        (
            "Does paying wages to a spouse help the wage limitation?",
            "<p>It can, since all W-2 wages of the business count toward the limitation, not "
            "only the owner's. The wages must be for services actually performed and set at "
            "a reasonable rate. Wages paid for no genuine work are disallowed and undermine "
            "the compensation position for every other owner.</p>",
        ),
        (
            "Should the deduction change how compensation is set?",
            "<p>It should inform the figure within the defensible range, not replace the "
            "analysis that produces it. Reasonable compensation is determined by the role, "
            "the hours, and the market. Section 199A can justify choosing the upper end of a "
            "defensible range, but it cannot justify a figure outside it.</p>",
        ),
    ],
)

# ---------------------------------------------------------------------------
# Pillar
# ---------------------------------------------------------------------------

CLUSTER = Cluster(
    key="s-corp",
    slug=P,
    label="S-Corp Tax Strategy",
    title="S-Corp Tax Strategy for $500K+ Business Owners: The Complete Guide",
    description=(
        "How profitable business owners use the S-corp election to cut payroll tax, "
        "what reasonable compensation actually requires, and where the savings stop."
    ),
    h1="S-Corp Tax Strategy for Business Owners",
    subtitle=(
        "What the election is worth at $500,000 to $1,000,000 of profit, what "
        "constrains it, and the situations where it is the wrong structure."
    ),
    lead=(
        "S-corp tax strategy is the use of an S corporation election to divide a business "
        "owner's profit into two streams that are taxed differently: wages, which carry "
        "Social Security and Medicare tax, and distributions, which do not. Both streams "
        "remain subject to ordinary income tax. The saving is confined to payroll tax, and "
        "it is bounded by the requirement that the owner first pay themselves reasonable "
        "compensation for the services they actually perform."
    ),
    keywords=[
        "s corp tax strategy",
        "s corp tax savings 500k",
        "s corporation reasonable compensation",
        "s corp vs llc high income",
    ],
    body=[
        (
            "What the S-Corp Election Actually Does",
            "<p>An S-corp is a tax election, not a type of company. An LLC or a corporation "
            "elects to be taxed under Subchapter S, and the entity itself generally pays no "
            "federal income tax. Profit passes through to the owners and is taxed on their "
            "personal returns whether or not it is distributed.</p>"
            "<p>The mechanism that matters is narrower than most owners assume. In a sole "
            "proprietorship or a partnership, an active owner's entire share of profit is "
            "generally exposed to self-employment tax. Under Subchapter S, only what the "
            "owner is paid as wages carries Social Security and Medicare tax. Profit taken "
            "as a distribution is exempt from those taxes.</p>"
            "<p>Income tax does not change. A dollar of profit is taxed at the owner's "
            "marginal rate either way. Anyone describing an S-corp election as a way to "
            "reduce income tax is describing something else, usually the Section 199A "
            "deduction, which is available to pass-through businesses regardless of whether "
            "they elect S status.</p>"
        ),
        (
            "The Math at $500,000 to $1,000,000 of Profit",
            "<p>Self-employment tax has two components with very different behavior. The "
            "Social Security component, 12.4 percent combining both halves, applies only up "
            "to an annual wage base. The Medicare component, 2.9 percent, applies to every "
            "dollar with no ceiling, and an Additional Medicare Tax of 0.9 percent applies "
            "above $200,000 for single filers and $250,000 for joint filers.</p>"
            "<p>This shape is what determines the value of the election at high profit "
            "levels, and it is where most owners misjudge it. An owner earning $800,000 in "
            "profit has already cleared the Social Security wage base with their wages "
            "alone. The election is not saving them 15.3 percent on $800,000. It is saving "
            "the Medicare component on the profit taken as distribution rather than wage.</p>"
            "<p>That is still substantial. On $500,000 of distribution, avoiding the 2.9 "
            "percent Medicare tax and the 0.9 percent additional tax is worth roughly "
            "$19,000 a year. It is simply a different and smaller number than the one "
            "usually quoted, and knowing which number applies is the difference between a "
            "plan and a sales pitch.</p>"
        ),
        (
            "Reasonable Compensation Is the Binding Constraint",
            "<p>The entire structure rests on one requirement: a shareholder who works in "
            "the business must be paid reasonable compensation for those services before "
            "taking distributions. This is not a formality. It is the most frequently "
            "litigated issue in Subchapter S and the most common adjustment on examination.</p>"
            "<p>There is no percentage safe harbor. Figures such as a 60/40 split are "
            "industry convention with no authority behind them. The standard is what the "
            "services are worth, determined from the specific roles performed, the hours "
            "worked, the market rate for those roles in that geography, and the portion of "
            "profit attributable to labor rather than to invested capital.</p>"
            "<p>Two owners with identical profit can defensibly report very different "
            "compensation. An owner working sixty hours a week running every function of the "
            "business supports a high figure. An owner who has hired a general manager and "
            "works ten hours a week supports a much lower one. What neither supports is a "
            "number with no derivation behind it.</p>"
        ),
        (
            "How Section 199A Changes the Calculation",
            "<p>The qualified business income deduction interacts with compensation in a way "
            "that reverses direction at the income thresholds. Below them, the deduction is "
            "20 percent of qualified business income with no wage test, so every dollar of "
            "wage reduces the deduction. Above them, the deduction is capped by a formula "
            "based on W-2 wages, so wages become what creates deduction capacity.</p>"
            "<p>At $500,000 to $1,000,000 of profit, owners are firmly in the second regime, "
            "which means the payroll tax analysis and the deduction analysis have to be "
            "solved together. Optimizing compensation for payroll tax alone routinely "
            "forfeits more in lost deduction than it saves.</p>"
        ),
        (
            "State Taxes and the PTET Election",
            "<p>Federal analysis is only part of the picture. Some states impose entity-level "
            "taxes on S-corps, and a few do not recognize the federal election at all, which "
            "changes the arithmetic materially.</p>"
            "<p>More importantly, most states now offer a pass-through entity tax election, "
            "which allows the business to pay state income tax at the entity level and deduct "
            "it federally, working around the individual limitation on state and local tax "
            "deductions. For an owner in a high-tax state, the PTET election is frequently "
            "worth more than the payroll tax saving that motivated the S election in the "
            "first place. It is routinely missed.</p>"
        ),
        (
            "The Real Costs of the Structure",
            "<p>An S-corp is not free, and the recurring cost has to clear before the "
            "structure makes sense:</p>"
            "<ul>"
            "<li>A separate entity return, Form 1120-S, with K-1s for every owner.</li>"
            "<li>Payroll processing, quarterly employment tax filings, and annual W-2s.</li>"
            "<li>A defensible reasonable compensation analysis, refreshed as the role "
            "changes.</li>"
            "<li>Corporate formalities and clean separation of business and personal funds.</li>"
            "<li>Basis tracking, which becomes critical the moment losses or large "
            "distributions occur.</li>"
            "</ul>"
            "<p>At $500,000 of profit these costs are immaterial against the saving. Below "
            "roughly $60,000 of profit they frequently exceed it.</p>"
        ),
        (
            "When the S-Corp Is the Wrong Answer",
            "<p>Several situations argue against the election even at high profit:</p>"
            "<ul>"
            "<li><strong>Real estate holding entities.</strong> S-corp shareholders get no "
            "basis from entity-level debt, which suspends the losses real estate is held to "
            "generate. Appreciated property also cannot be distributed out without "
            "triggering gain. Partnership treatment is almost always correct here.</li>"
            "<li><strong>Owners with unequal economics.</strong> Distributions must be "
            "strictly pro rata. Any arrangement requiring a preferred return or a special "
            "allocation is incompatible with Subchapter S.</li>"
            "<li><strong>Planned outside investment.</strong> Entity and nonresident "
            "investors are ineligible shareholders and terminate the election.</li>"
            "<li><strong>Owners retaining large earnings.</strong> Where profit is being "
            "retained to fund growth rather than distributed, a C-corp structure may tax "
            "that retained income at a lower rate.</li>"
            "<li><strong>Minimal owner involvement.</strong> If the owner performs few "
            "services, most profit is a return on capital and the payroll tax exposure the "
            "election solves was never large.</li>"
            "</ul>"
        ),
        (
            "Basis: The Tracking That Prevents a Surprise Tax Bill",
            "<p>Stock basis is the running measure of what an owner has invested in the "
            "S-corp plus the income already taxed to them, less what has been distributed "
            "and deducted. It is unglamorous and it is the source of some of the most "
            "expensive surprises in Subchapter S.</p>"
            "<p>Two rules do the damage. Distributions in excess of basis are taxable as "
            "capital gain, so an owner can face a tax bill on cash they thought was a "
            "return of their own money. And losses are deductible only to the extent of "
            "basis, so an owner with a genuine economic loss may find it suspended and "
            "carried forward instead of offsetting income in the year it occurred.</p>"
            "<p>The trap specific to S-corps is that entity-level debt does not create "
            "shareholder basis. A partner in a partnership generally gets basis from the "
            "partnership's borrowings; an S-corp shareholder does not, unless they lend the "
            "money to the company personally. Owners who move from a partnership to an S "
            "election frequently carry the old assumption across and discover the difference "
            "only when a loss year arrives. Basis has to be tracked from the first day, "
            "because reconstructing it years later is expensive and often incomplete.</p>"
        ),
        (
            "The Pieces That Compound: Accountable Plans and Retirement",
            "<p>Two additions convert a merely correct S-corp into an efficient one.</p>"
            "<p>An <strong>accountable plan</strong> is a written arrangement under which "
            "the company reimburses an owner-employee for business expenses they pay "
            "personally, including the business-use portion of a home office, mileage, and "
            "equipment. Reimbursements under a compliant plan are deductible to the company "
            "and untaxed to the owner. Without the plan, those same expenses are generally "
            "not deductible on the personal return at all, so the plan converts a lost "
            "deduction into a real one for the cost of drafting a policy and keeping "
            "receipts.</p>"
            "<p>A <strong>retirement plan</strong> is where the compensation figure starts "
            "working twice. Plan contribution capacity is driven by W-2 wages, so the "
            "reasonable compensation figure that carries payroll tax also determines how "
            "much can be moved into a deductible plan. For an owner at this profit level, a "
            "solo 401(k) paired with a cash balance plan can absorb a large multiple of what "
            "the payroll tax analysis alone would suggest is optimal, and it changes the "
            "Section 199A position at the same time. This is the clearest case of why the "
            "structure has to be modeled as one system.</p>"
        ),
        (
            "Election Timing and Getting It Right",
            "<p>Form 2553 is generally due within two months and fifteen days of the "
            "beginning of the tax year the election is to take effect, or any time during "
            "the preceding year. Missing the deadline is common and usually repairable: "
            "Revenue Procedure 2013-30 provides relief where there was reasonable cause and "
            "the entity has otherwise filed consistently with S status.</p>"
            "<p>The sequence that avoids problems is: confirm shareholder eligibility, "
            "conform the operating agreement to a single class of interest, complete the "
            "reasonable compensation analysis, establish payroll, then file the election. "
            "Reversing those steps is what produces invalid elections discovered years later.</p>"
        ),
        (
            "What Implementation Looks Like",
            "<p>A properly implemented S-corp for a business at this profit level has a "
            "documented compensation file assembled before the year begins, payroll running "
            "on a real schedule, distributions that are demonstrably not a paycheck in "
            "disguise, an accountable plan for reimbursing owner expenses, a retirement plan "
            "sized against the compensation figure, and basis tracked from the first day "
            "rather than reconstructed later.</p>"
            "<p>Each piece supports the others. The compensation figure drives the retirement "
            "plan capacity. The retirement plan changes the Section 199A position. The "
            "Section 199A position influences where in the defensible range compensation "
            "should sit. This is why the structure is worth modeling as one system rather "
            "than assembling piece by piece.</p>"
        ),
    ],
    takeaways=[
        "An S-corp election saves payroll tax only; it does not change income tax rates.",
        "Above the Social Security wage base the saving is the Medicare component, not 15.3 percent.",
        "Reasonable compensation is the binding constraint and has no percentage safe harbor.",
        "Above the Section 199A thresholds, wages create deduction capacity rather than destroying it.",
        "A state PTET election is often worth more than the payroll tax saving itself.",
        "Real estate, unequal owner economics, and outside investors all argue against the election.",
    ],
    faqs=[
        (
            "How much does an S-corp election save at $500,000 of profit?",
            "<p>Less than the commonly quoted 15.3 percent, because an owner at that level "
            "has already cleared the Social Security wage base through wages alone. The "
            "saving is the 2.9 percent Medicare tax plus the 0.9 percent Additional Medicare "
            "Tax on profit taken as distribution rather than wage. On $500,000 of "
            "distribution that is roughly $19,000 a year, before considering the Section "
            "199A and state effects that often matter more.</p>",
        ),
        (
            "What is reasonable compensation for an S-corp owner?",
            "<p>The amount an unrelated party would have to be paid to perform the same "
            "services. It is determined from the specific roles the owner performs, the "
            "hours worked, market rate data for those roles in that geography, and the split "
            "between return on labor and return on invested capital. No percentage safe "
            "harbor exists in any statute, regulation, or ruling.</p>",
        ),
        (
            "Is an S-corp better than an LLC for a business making $500,000?",
            "<p>An LLC and an S-corp are not alternatives; an LLC is a legal entity and an "
            "S-corp is a tax election that an LLC can make. The real question is whether an "
            "LLC should be taxed as a sole proprietorship, a partnership, or an S-corp. At "
            "$500,000 of profit from an operating business with an active owner, the S "
            "election is usually favorable. For a real estate holding entity it usually is "
            "not.</p>",
        ),
        (
            "Can an S-corp own rental property?",
            "<p>It can, but it rarely should. Shareholders receive no basis from entity-level "
            "debt, which suspends the depreciation losses rental property is held to "
            "generate. Distributing appreciated property out of an S-corp also triggers gain "
            "as though it were sold. A partnership or a disregarded LLC is nearly always the "
            "better holding structure.</p>",
        ),
        (
            "What happens if the IRS says compensation was too low?",
            "<p>Distributions are recharacterized as wages, and Social Security and Medicare "
            "tax is assessed on the reclassified amount along with failure-to-deposit and "
            "failure-to-file penalties and interest running from the original due dates. "
            "Because employment tax returns are quarterly, an adjustment across open years "
            "typically touches a dozen or more filings.</p>",
        ),
        (
            "Do I need payroll if I am the only employee?",
            "<p>Yes. A shareholder performing services for the business is an employee for "
            "employment tax purposes, and the compensation must be paid as wages reported on "
            "a W-2. Distributions without payroll are the single most common S-corp "
            "compliance failure and the easiest for the IRS to identify from the return "
            "itself.</p>",
        ),
        (
            "When should an S-corp election be revoked?",
            "<p>Common triggers include a shift toward retaining rather than distributing "
            "earnings, a plan to raise outside investment from entity or nonresident "
            "investors, a need for allocations that are not strictly pro rata, or the "
            "acquisition of appreciating real estate. Revocation has its own timing rules "
            "and a five-year waiting period before re-electing, so it should be modeled "
            "before it is filed.</p>",
        ),
        (
            "Does an S-corp reduce the Section 199A deduction?",
            "<p>Wages reduce qualified business income, but above the taxable income "
            "thresholds they also raise the W-2 wage limitation that caps the deduction. For "
            "a business at $500,000 to $1,000,000 of profit, wages generally create "
            "deduction capacity rather than destroying it, which is why compensation and the "
            "deduction have to be modeled together.</p>",
        ),
    ],
    spokes=[
        Spoke(
            slug="reasonable-compensation-s-corp-irs",
            label="S-Corp reasonable compensation analysis",
            adopted=True,
        ),
        Spoke(
            slug="s-corp-vs-llc-tax-comparison-2026",
            label="S-Corp vs LLC for $500K+ businesses",
            adopted=True,
        ),
        Spoke(
            slug="s-corp-tax-savings-calculator",
            label="S-Corp payroll tax savings calculator",
            adopted=True,
        ),
        Spoke(
            slug="s-corp-election-timing-late-relief",
            label="When to elect S-Corp status",
            adopted=True,
        ),
        AUDIT_TRIGGERS,
        Spoke(
            slug="the-ultimate-guide-to-s-corporation-salary-optimization",
            label="S-Corp distributions vs salary optimization",
            adopted=True,
        ),
        QBI_MAX,
        MULTI_MEMBER_LLC,
    ],
)
