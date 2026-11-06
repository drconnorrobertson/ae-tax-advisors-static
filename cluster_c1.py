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
    slug='s-corp-qbi-deduction-maximization',
    label='S-Corp QBI deduction maximization',
    title='S-Corp QBI Deduction: Wages, UBIA and 2026 Limits',
    description=('Compare S-corp wages, QBI, qualified-property UBIA, SSTB rules and 2026 phase-in limits before '
     'changing compensation or retirement contributions.'),
    h1='S-Corp QBI Deduction Maximization',
    subtitle=('Model reasonable compensation, retirement contributions, qualified property, and the 2026 QBI '
     'limits together before changing payroll.'),
    lead=("An S-corp QBI review starts with reasonable compensation and the owner's taxable income, not a "
     'target salary ratio. Wages can reduce qualified business income while supporting a wage limit '
     'that applies only as income rises. Qualified-property UBIA, service-business restrictions, '
     'retirement contributions, and the overall taxable-income cap can change the answer.'),
    keywords=['s corp qbi deduction', 'section 199a s corp wages', 'qbi w2 wage limitation'],
    body=[('The 2026 Thresholds and Phase-In Rules',
      '<p>Use <strong>taxable income before the QBI deduction</strong>, not revenue, gross profit, or '
      'QBI alone. For tax years beginning in 2026, the threshold and end of the phase-in range '
      'are:</p><ul><li><strong>Married filing jointly:</strong> $403,500 to $553,500, a $150,000 '
      'range.</li><li><strong>Married filing separately:</strong> $201,775 to $276,775, a $75,000 '
      'range.</li><li><strong>All other returns, including single and head of household:</strong> '
      '$201,750 to $276,750, a $75,000 range.</li></ul><p>At or below the threshold, the W-2 wage/UBIA '
      'limit and SSTB restriction do not apply. Within the range, the wage/property limit phases in '
      'and only an applicable percentage of SSTB QBI, wages, and UBIA is counted. At the upper '
      'endpoint, the non-SSTB wage/property limit is fully effective and the SSTB applicable '
      'percentage is zero. The overall taxable-income limitation still matters. These are the 2026 '
      'amounts in <a href="https://www.irs.gov/pub/irs-drop/rp-25-32.pdf">Revenue Procedure 2025-32, '
      'section 4.26</a>.</p><p>For a non-SSTB above the phase-in range, the business component '
      'generally is the <strong>lesser of 20% of QBI or the greater of 50% of properly allocable W-2 '
      'wages and 25% of those wages plus 2.5% of UBIA of qualified property</strong>. UBIA means '
      'unadjusted basis immediately after acquisition. After business loss netting and any qualified '
      'REIT/PTP component, the regular deduction is generally capped at 20% of the amount remaining '
      'after subtracting net capital gain, including qualified dividends, from taxable income before '
      'the QBI deduction. A deduction reduces taxable income; it is not a dollar-for-dollar tax '
      'credit.</p><p>Beginning in 2026, Section 199A(i) separately provides a $400 minimum deduction '
      'for an applicable taxpayer with at least $1,000 of aggregate QBI from active qualified trades '
      'or businesses. Active means material participation under Section 469. This limited floor does '
      'not make an excluded SSTB a qualified business or remove other eligibility requirements. The '
      'examples here address the regular calculation, not that minimum.</p>'),
     ('Why Two-Sevenths Is Not a Salary Recommendation',
      '<p>Reasonable compensation for services is a legal constraint, not a number chosen to fit a '
      'deduction. Shareholder wages are taxable compensation, while pass-through profit is generally '
      'taxable whether or not cash is distributed. Increasing salary shifts income between those '
      'categories and adds relevant employment-tax costs; it does not automatically save income '
      "tax.</p><p>In a deliberately simplified non-SSTB model, let P be profit before the owner's "
      'wages and W be those wages. Assume no other wages, payroll deductions, UBIA, phase-in, losses, '
      'retirement contributions, or taxable-income constraint. The regular business component is the '
      'lesser of 20% × (P − W) and 50% × W. The lines cross at W = 2P/7.</p><p>For P = $700,000, W = '
      '$200,000 leaves $500,000 of QBI and both tests at $100,000. At W = $150,000, the component is '
      '$75,000; at W = $250,000, it is $90,000. This is a deduction-only illustration, not the '
      'total-tax optimum. Employee wages, employer payroll tax, Social Security wage limits, Medicare, '
      'benefits, and actual compensation requirements change the result.</p>'),
     ('Zero Wages Do Not Always Mean Zero Capacity',
      '<p>Assume a qualifying non-SSTB owner is above the phase-in range, has $400,000 of QBI, no '
      'allocable W-2 wages, and $2,000,000 of eligible UBIA. The wage/property limit is $50,000, not '
      'zero. The tentative business component is the lesser of $80,000 and $50,000: $50,000, before '
      'the overall cap and other adjustments. This does not permit an S-corp shareholder who performs '
      'services to skip required reasonable compensation.</p><p>Qualified property is depreciable '
      'tangible property held by and available for use in the business at year-end, used at some point '
      'during the year to produce QBI, and still within its Section 199A depreciable period. Land does '
      'not qualify. That period ends on the <strong>later of 10 years after first placed in service or '
      'the last day of the last full year of the applicable recovery period</strong>, determined '
      'without ADS. It is not a test of whether more than one year of useful life remains.</p><p>UBIA '
      'is generally measured before depreciation, including bonus depreciation and Section 179, '
      'subject to the detailed acquisition and allocation rules. Ordinary calendar-year UBIA is not '
      'prorated by purchase month: eligible equipment placed in service in January or December and '
      'held at year-end can count for that tax year. Buying equipment without placing it in service is '
      'not enough, and short-year, transfer, and anti-abuse rules can alter the analysis. See <a '
      'href="https://www.ecfr.gov/current/title-26/section-1.199A-2">Treasury Regulation '
      '1.199A-2</a>.</p>'),
     ('Specified Service Businesses and Related Rentals',
      '<p>SSTBs include defined services in health, law, accounting, actuarial science, performing '
      'arts, consulting, athletics, financial services, and securities brokerage, plus specified '
      'investing, trading, and dealing activities. Engineering and architecture are excluded from the '
      'listed service fields. Real estate brokerage and direct real-property management are not '
      'automatically SSTBs under the securities-brokerage or investment-management '
      'categories.</p><p>The separate <strong>reputation or skill</strong> category is narrow: income '
      "from endorsements, licensing an individual's identity, or paid appearances. A business does not "
      'become an SSTB merely because its owner is skilled or well known. Apply the actual definitions '
      'and any de minimis rules in <a '
      'href="https://www.ecfr.gov/current/title-26/section-1.199A-5">Treasury Regulation '
      '1.199A-5</a>.</p><p>A separate rental or management company is not a workaround for the SSTB '
      'limits. Under Treasury Regulation 1.199A-5(c)(2), where there is <strong>50% or more common '
      'ownership</strong>, including applicable direct, indirect, and related-party attribution, the '
      'portion of a business providing property or services to the commonly owned SSTB is treated as a '
      'separate SSTB with respect to the related parties. Real contracts, fair-market rent, and '
      'genuine services do not switch off this rule.</p><p>For example, a commonly owned building '
      "company leasing the entire building to the owners' law practice falls under the rule. If part "
      'is leased to unrelated tenants, analyze that unrelated portion separately. Rental qualification '
      'and the Section 469 self-rental rule are separate questions; neither overrides the Section 199A '
      'related-SSTB restriction.</p>'),
     ('When Aggregation Can Combine Wages and Property',
      '<p>Aggregation under <a href="https://www.ecfr.gov/current/title-26/section-1.199A-4">Treasury '
      'Regulation 1.199A-4</a> is optional and requires more than owning several entities. The same '
      'person or group must own at least 50% of each business, directly or by the applicable '
      'attribution rules, for a majority of the tax year including its last day. Items must be '
      'reported for tax years ending on the same date, and none of the aggregated businesses can be an '
      'SSTB. At least two of these three operational links must exist:</p><ul><li>The businesses '
      'provide the same or customarily offered-together products or services.</li><li>They share '
      'facilities or significant centralized business elements, such as personnel, accounting, or '
      'purchasing.</li><li>They operate in coordination with, or reliance on, one '
      'another.</li></ul><p>Document the qualifying facts and annual disclosures, including Schedule B '
      '(Form 8995-A) when required. Continue an aggregation consistently in later years while it '
      'qualifies. Changes in facts can require a new analysis, and a newly created or acquired '
      'qualifying business may be added. It is not freely reversible, but it is not an unconditional '
      'forever election requiring IRS consent for every factual change.</p>'),
     ('How Retirement Contributions Affect Both Tests',
      "<p>Distinguish an S-corp employee's elective salary deferral from an employer contribution. A "
      "traditional employee 401(k) deferral generally lowers the employee's federal taxable wages but "
      'is part of gross salary already deducted by the S-corp, not a second business deduction. It '
      'generally remains within the Section 199A W-2 wage definition under the permitted calculation '
      'methods. A Roth elective deferral does not lower current federal taxable income.</p><p>An '
      'S-corp employer retirement contribution generally reduces pass-through profit and QBI. It is '
      'not also deducted a second time by the shareholder on the individual return. Deductible '
      'self-employed retirement contributions, health insurance, and the deductible part of '
      'self-employment tax attributable to a sole proprietorship or partnership can reduce that '
      "owner's QBI. Lower taxable income may improve phase-in treatment even when QBI falls, so "
      'compare the complete return, plan limits, staff costs, and cash commitments.</p>'),
     ('What to Bring to a QBI and Salary Review',
      '<p>Bring the current profit-and-loss statement, prior return and QBI loss carryforwards, '
      'ownership chart, payroll and W-2 records, reasonable-compensation support, asset register with '
      'placed-in-service dates and UBIA, and retirement-plan documents. Compare the regular deduction, '
      'federal and state taxes, payroll costs, and after-tax cash across defensible scenarios. Confirm '
      'the actual scope and cost of any advisory work before proceeding.</p>'),
     ('Sources and Review Date',
      '<p>Reviewed November 6, 2026. Primary references: <a '
      'href="https://www.law.cornell.edu/uscode/text/26/199A">IRC Section 199A</a>, <a '
      'href="https://www.irs.gov/pub/irs-drop/rp-25-32.pdf">Revenue Procedure 2025-32 (2026 '
      'thresholds)</a>, <a href="https://www.ecfr.gov/current/title-26/section-1.199A-5">SSTB '
      'regulations</a>, <a href="https://www.ecfr.gov/current/title-26/section-1.199A-4">aggregation '
      'regulations</a>, <a href="https://www.ecfr.gov/current/title-26/section-1.199A-2">wage and UBIA '
      'regulations</a>, <a href="https://www.irs.gov/pub/irs-drop/rp-19-38.pdf">rental safe '
      'harbor</a>, <a href="https://www.irs.gov/instructions/i8995a">Form 8995-A instructions</a>. The '
      'linked Form 8995-A instructions are currently labeled 2025; their filing-year dollar amounts '
      'and phase-in widths must not be reused as 2026 figures. Examples are hypothetical federal '
      'illustrations, not reported client outcomes or promised savings.</p>')],
    takeaways=['Use 2026 taxable income before the QBI deduction to locate the phase-in range.',
     'Zero wages can still leave capacity from 2.5% of eligible UBIA; reasonable compensation remains '
     'required.',
     'Two-sevenths is a simplified deduction crossing point, not a total-tax salary target.',
     'The related-SSTB rule applies at 50% or more common ownership even with genuine contracts.',
     'Model employee deferrals and employer retirement contributions separately, without a double '
     'deduction.'],
    faqs=[('Do S-corp wages increase or decrease the QBI deduction?',
      '<p>Deductible wages reduce business profit and QBI; shareholder wages are not QBI to the '
      'recipient. Properly allocable W-2 wages may also support the wage limit when it applies. The '
      'overall result depends on the phase-in range, qualified-property UBIA, SSTB status, and the '
      'taxable-income cap.</p>'),
     ('What is the optimal wage level for QBI purposes?',
      '<p>Two-sevenths of pre-wage profit is only the crossing point in a simplified model with no '
      'other wages, payroll expense, UBIA, phase-in, or other deductions, and a fully applicable 50% '
      'wage limit. It maximizes that simplified QBI component, not total tax savings. Reasonable '
      'compensation and the full return control.</p>'),
     ('Can an S-corp owner in a service business still claim QBI?',
      '<p>An SSTB can produce eligible QBI at or below the taxable-income threshold. Within the '
      'phase-in range only an applicable percentage of its QBI, wages, and UBIA is considered, and the '
      'SSTB percentage is zero at the upper endpoint. A commonly owned rental or management entity '
      'does not automatically escape these rules.</p>'),
     ('Does paying wages to a spouse help the wage limitation?',
      '<p>Reasonable wages for genuine services may count if properly allocable and timely reported. '
      'They also reduce QBI and can create payroll taxes and retirement-plan obligations. A spouse '
      'does not need to own the business to be an employee. Count only qualifying wages, without '
      'duplication across businesses.</p>'),
     ('Should the deduction change how compensation is set?',
      '<p>Compare defensible compensation scenarios after documenting duties, hours, and market pay. '
      'QBI can inform the comparison, but it cannot replace reasonable compensation, justify '
      'unsupported wages, or establish that a larger deduction leaves the owner with more cash.</p>')],
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
        "Social Security and Medicare tax, and distributions, which do not. Wages and "
        "allocated business income generally enter the owner's income-tax calculation; "
        "cash distributions have separate basis and distribution rules. "
        "Employment-tax savings depend on paying "
        "reasonable compensation for the services the owner performs; income-tax effects, "
        "including Section 199A, must also be modeled."
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
            "<p>Business profit generally remains subject to the owner's individual "
            "income-tax rates. However, compensation and the Section 199A qualified "
            "business income deduction can change the income-tax result, even though "
            "Section 199A is also available to other eligible pass-through businesses.</p>"
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
        "An S-corp election can reduce employment taxes; income-tax effects must also be modeled.",
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
