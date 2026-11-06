#!/usr/bin/env python3
"""Cluster 5: Retirement plan tax strategy for business owners."""

from __future__ import annotations

from cluster_common import Cluster, Spoke

P = "retirement-plan-tax-strategy-business-owners"

SOLO_VS_SEP = Spoke(
    slug="solo-401k-vs-sep-ira-business-owners",
    label="Solo 401(k) vs SEP IRA for profitable businesses",
    title="Solo 401(k) vs SEP IRA for Profitable Businesses",
    description=(
        'Compare 2026 solo 401(k) and SEP IRA limits, earned-income calculations, Roth options, employee costs, and prior-year setup and funding deadlines.'
    ),
    h1="Solo 401(k) vs SEP IRA for Profitable Businesses",
    subtitle=(
        'A solo 401(k) can reach the shared contribution ceiling with less compensation. Compare timing, employee costs, Roth options, and administration before choosing.'
    ),
    lead=(
        'A SEP IRA accepts employer retirement contributions; a solo 401(k) adds employee elective deferrals. The solo 401(k) can allow more at moderate compensation, but both can reach the same $72,000 non-catch-up ceiling in 2026. The best choice depends on eligible earnings, deferrals already made at another job, employees, deadlines, and administrative cost.'
    ),
    keywords=[
        "solo 401k vs sep ira",
        "best retirement plan self employed business owner",
        "sep ira solo 401k comparison",
    ],
    body=[('The Structural Difference',
  '<p>For 2026, the elective deferral limit is $24,500 and the defined contribution annual additions limit '
  'is $72,000, excluding permitted catch-up contributions. The ordinary age-50-or-older catch-up is $8,000; '
  'participants attaining ages 60 through 63 may use $11,250 instead, if permitted. Catch-up contributions '
  'for participants whose prior-year wages from the sponsoring employer exceeded $150,000 generally must be '
  'Roth in 2026. That wage test is not household income or net self-employment earnings, and Roth '
  'contributions are not current deductions.</p><p>Employer contributions are generally limited to 25% of '
  'eligible W-2 compensation. For a self-employed owner, a stated 25% rate generally becomes 20% of adjusted '
  'net earnings after the deductible part of self-employment tax; use the Publication 560 worksheets rather '
  'than multiplying Schedule C profit by 25%. Contributions also cannot exceed the applicable compensation '
  'limits.</p><p>For a 2026 owner under 50 with $100,000 of eligible W-2 pay, no other deferrals and no '
  'employees, a 25% employer contribution is $25,000. A SEP can receive $25,000; a solo 401(k) can receive '
  'that plus $24,500 of employee deferrals, totaling $49,500. At $288,000 of eligible pay, a 25% SEP '
  'contribution reaches $72,000, matching the solo 401(k) non-catch-up ceiling. These are contribution '
  'illustrations, not a recommendation to change reasonable compensation.</p><p>The employee deferral limit '
  'follows the individual across applicable employer plans. Deferrals already made at a day job reduce the '
  'remaining solo 401(k) deferral room. Annual additions are generally aggregated for plans of the same or '
  'related employers; genuinely unrelated employers may have separate limits. Review controlled groups and '
  'affiliated service groups before assuming separate businesses create separate capacity.</p>'),
 ('Where the Solo 401(k) Wins',
  '<p><strong>Contribution room at moderate compensation.</strong> Employee deferrals can fill a gap that '
  'percentage-limited employer contributions cannot, provided the owner has eligible earnings and unused '
  'deferral room.</p><p><strong>Roth flexibility.</strong> A plan may allow designated Roth deferrals and '
  'in-plan Roth conversions. SECURE 2.0 also permits Roth SEP contributions where the arrangement and '
  'provider support them, so Roth treatment is not exclusive to a 401(k). Roth employee deferrals do not '
  "reduce the participant's current taxable income. Employer Roth SEP contributions are generally included "
  "in the participant's income when deposited, while the employer deduction is evaluated separately under "
  'the SEP deduction rules.</p><p><strong>Loan provisions.</strong> A solo 401(k) may permit participant '
  'loans within statutory and plan limits; SEP IRAs do not permit participant loans.</p><p><strong>Cash '
  'balance coordination.</strong> A 401(k) can be paired with a defined benefit plan, subject to census '
  'testing and combined deduction calculations. A SEP is not automatically barred from another plan, but the '
  'IRS model Form 5305-SEP cannot be used when maintaining another qualified plan, apart from its stated '
  'exception. Obtain a compatible document and design review.</p><p><strong>Backdoor Roth planning.</strong> '
  'Pre-tax traditional SEP IRA balances enter the IRA pro-rata calculation, along with traditional and '
  'SIMPLE IRAs. Qualified-plan balances do not. A rollover of eligible pre-tax SEP assets into a 401(k) that '
  'accepts them may help, but review basis, year-end balances, and rollover eligibility first.</p>'),
 ('Where the SEP IRA Still Wins',
  '<p><strong>Simple administration.</strong> A SEP still needs a written agreement, required employee '
  'disclosures, and an IRA for each eligible participant. It generally has no annual Form 5500 filing. A '
  'solo 401(k) requires a qualified plan document and may trigger Form 5500-EZ filing when total '
  'one-participant plan assets exceed $250,000 at year-end; a final return is generally required on '
  'termination regardless of assets.</p><p><strong>Prior-year employer funding.</strong> A SEP can generally '
  'be established and funded by the extended employer return deadline. A solo 401(k) can also be adopted '
  'after year-end for eligible employer contributions; missing December 31 does not automatically make a SEP '
  'the only option.</p><p>Most qualified employer plans may be adopted by the employer tax-return due date, '
  'including extensions, and treated as adopted for the prior tax year. Adoption, employee deferral '
  'elections, deposit deadlines, and employer contribution deductibility are separate tests. Salary '
  'deferrals generally require a timely election before compensation becomes available; adopting a plan '
  'later does not authorize retroactive S-corporation payroll deferrals. A narrow first-year exception '
  'permits an individual who owns the entire unincorporated business and is its only employee to adopt a new '
  '401(k) and make first-year elective deferrals by the unextended individual return '
  'deadline.</p><p><strong>Variable income.</strong> SEP employer contributions can be discretionary, '
  'including zero for a year. Discretionary profit sharing can also be available in a 401(k); neither label '
  'removes promised safe harbor or other required contributions.</p>'),
 ('The Employee Problem Applies to Both',
  '<p>A SEP generally requires the same contribution percentage for every eligible participant under the '
  'plan formula, which can make owner contributions costly when staff qualify. A 401(k) covering employees '
  'has coverage, nondiscrimination and reporting requirements; safe harbor designs address some testing but '
  'do not remove every obligation.</p><p>A solo 401(k) generally covers only an owner, or owner and spouse, '
  'without eligible common-law employees. Review employee service, including applicable long-term part-time '
  'rules, and all controlled or affiliated businesses before using an owner-only plan. Ordinary rental '
  'receipts and S-corporation distributions do not themselves create eligible retirement-plan '
  'compensation.</p>'),
 ('How to Choose',
  '<p>Bring projected eligible W-2 pay or adjusted self-employment earnings, employee census, all related '
  'businesses, outside-plan deferrals, existing IRA balances, and the tax year you want to fund. Compare '
  'total owner savings, required staff contributions, administration, Roth treatment, and cash needed by '
  'each deadline.</p><p>A solo 401(k) often fits an eligible owner seeking maximum contributions at moderate '
  'compensation or a compatible cash balance design. A SEP may fit an owner prioritizing simpler '
  'administration who does not need loans or employee deferrals. At sufficient compensation both can reach '
  'the same non-catch-up limit. Confirm provider support and obtain the written calculation before adopting '
  'or rolling funds.</p>')],
    takeaways=['Both plans can reach the $72,000 non-catch-up ceiling in 2026; a solo 401(k) can reach it with less '
 'compensation.',
 'Other employer-plan deferrals reduce the individual deferral room available to a solo 401(k).',
 'Both plans require written arrangements; a SEP generally avoids annual Form 5500 filing.',
 'After-year-end employer adoption is possible; deferral elections and funding have separate deadlines.',
 'Roth SEP contributions may be available, and employee or related-business coverage can change the answer.'],
    faqs=[('Which allows a larger contribution, a solo 401(k) or a SEP IRA?',
  '<p>At moderate compensation, a solo 401(k) may permit more because it adds unused employee deferral room '
  'to employer contributions. Both can reach the $72,000 non-catch-up annual additions limit for 2026 at '
  'sufficient eligible compensation. Outside-plan deferrals and related-employer limits must be '
  'coordinated.</p>'),
 ('Can I set up a retirement plan after the year ends?',
  '<p>Most qualified employer plans may be adopted by the employer tax-return due date, including '
  'extensions, and treated as adopted for the prior tax year. Adoption, employee deferral elections, deposit '
  'deadlines, and employer contribution deductibility are separate tests. Salary deferrals generally require '
  'a timely election before compensation becomes available; adopting a plan later does not authorize '
  'retroactive S-corporation payroll deferrals. A narrow first-year exception permits an individual who owns '
  'the entire unincorporated business and is its only employee to adopt a new 401(k) and make first-year '
  'elective deferrals by the unextended individual return deadline.</p>'),
 ('Does a SEP IRA interfere with a backdoor Roth?',
  '<p>Pre-tax SEP IRA balances count in the pro-rata calculation for traditional IRA conversions, along with '
  'traditional and SIMPLE IRA balances. A solo 401(k) balance does not. Any rollover into a 401(k) must be '
  'eligible and accepted by the plan, with IRA basis reviewed separately.</p>'),
 ('Can I have both a SEP and a solo 401(k)?',
  '<p>It may be possible with compatible plan documents, but plans of the same or related employer share '
  'applicable annual additions limits. IRS model Form 5305-SEP generally cannot be used while maintaining '
  'another qualified plan. A second account does not double the deduction.</p>')],
)

STACKING = Spoke(
    slug="stacking-retirement-plans-maximum-deduction",
    label="Stacking retirement plans for maximum deduction",
    title="Stacking Retirement Plans for Maximum Deduction",
    description=(
        'Model a 401(k) plus cash balance plan using 2026 limits, employee costs, PBGC coverage, combined deduction rules, and separate adoption and funding deadlines.'
    ),
    h1="Stacking Retirement Plans for Maximum Deduction",
    subtitle=(
        'A 401(k) and cash balance plan can build larger retirement savings, but contribution limits, deductible amounts, staff costs, and funding deadlines must all fit.'
    ),
    lead=(
        'Stacking retirement plans means operating a defined contribution plan, usually a 401(k), alongside a defined benefit or cash balance plan. Their benefit and contribution limits differ, but that does not make the maximum amounts automatically deductible together. An actuarial study and tax projection must establish a sustainable owner benefit, required employee funding, and the allowed deduction.'
    ),
    keywords=[
        "stacking retirement plans business owner",
        "combine 401k cash balance plan",
        "maximum retirement deduction business owner",
    ],
    body=[('Why Two Plans Beat One',
  '<p>For 2026, the elective deferral limit is $24,500 and the defined contribution annual additions limit '
  'is $72,000, excluding permitted catch-up contributions. The ordinary age-50-or-older catch-up is $8,000; '
  'participants attaining ages 60 through 63 may use $11,250 instead, if permitted. Catch-up contributions '
  'for participants whose prior-year wages from the sponsoring employer exceeded $150,000 generally must be '
  'Roth in 2026. That wage test is not household income or net self-employment earnings, and Roth '
  'contributions are not current deductions.</p><p>A defined benefit plan instead funds a promised '
  'retirement benefit. The 2026 Section 415(b) annual-benefit dollar limit is $290,000, subject to '
  'compensation, age, participation, and payment-form adjustments. That is not an annual contribution '
  'allowance. An enrolled actuary calculates minimum required funding and the maximum deductible '
  'contribution using the plan formula, assets, compensation history, and applicable '
  'assumptions.</p><p>Older owners may have fewer years to fund a benefit, which can support larger annual '
  'contributions. Age alone does not establish a permitted deduction.</p>'),
 ('What the Numbers Look Like',
  '<p>Illustrative 2026 arithmetic only: assume a 55-year-old sole proprietor has $300,000 of plan-eligible '
  'compensation after the required self-employment adjustments, no eligible employees across related '
  'businesses, no other deferrals, and no prior-year wages from this sponsor triggering Roth catch-up. '
  'Assume an actuary separately validates a $200,000 cash balance contribution as both required or permitted '
  'funding and deductible, and verifies the combined design.</p><div '
  'style="overflow-x:auto;"><table><thead><tr><th>Component</th><th>Illustrative '
  'amount</th><th>Condition</th></tr></thead><tbody><tr><td>401(k) elective '
  'deferral</td><td>$24,500</td><td>Unused individual deferral room</td></tr><tr><td>Age-55 '
  'catch-up</td><td>$8,000</td><td>Plan permits catch-up; assumed pre-tax '
  'eligibility</td></tr><tr><td>Employer defined contribution</td><td>$18,000</td><td>6% of $300,000 '
  'eligible compensation</td></tr><tr><td>Cash balance contribution</td><td>$200,000</td><td>Assumed '
  'actuarial result, not an age-based entitlement</td></tr><tr><td>Total '
  'contribution</td><td>$250,500</td><td>Subject to all funding and deduction '
  'tests</td></tr></tbody></table></div><p>This is not a client result or a funding quote. It deliberately '
  'does not assume the full $72,000 defined contribution limit can be stacked automatically. Actual '
  'self-employed compensation and deduction calculations are interdependent and require the Publication 560 '
  'worksheets and actuarial review. Current tax savings also depend on QBI, tax brackets, Roth treatment and '
  'state law.</p>'),
 ('The Rules Governing the Combination',
  '<p>The 6% figure is not a universal contribution or deduction cap. Under Section 404(a)(7), employer '
  'defined contribution amounts up to 6% of covered compensation are excluded from the combined deduction '
  'calculation; when employer contributions exceed 6%, the excess enters the applicable combined test. '
  'Employee elective deferrals are excluded. A PBGC-covered defined benefit plan is excluded from this '
  'combined limit, but separate plan limits still apply. Have the actuary and tax preparer calculate both '
  'the minimum funding and maximum deductible contribution.</p><p><strong>Coverage and '
  'nondiscrimination.</strong> Review controlled groups and affiliated service groups under Section 414, '
  'employee service, compensation and ownership before treating a business as owner-only. Where aggregation '
  'is permitted for testing, both plans still must satisfy the applicable coverage, minimum participation '
  'and nondiscrimination rules.</p><p><strong>Funding and permanence.</strong> A defined benefit plan is '
  'intended as an ongoing retirement program. A weak year does not eliminate minimum funding, and an early '
  'termination needs a legitimate facts-and-circumstances review. There is no three-year or five-year legal '
  'safe harbor.</p>'),
 ('The Employee Cost',
  '<p>With employees, model total employer cash outlay, the benefits allocated to owners and staff, and '
  'administration costs. Cross-tested designs can be useful when owners are older than staff, but no '
  'standard owner allocation percentage is guaranteed.</p><p>For arithmetic only, $200,000 allocated to '
  'owners and $50,000 to staff means owners receive 80% of $250,000 total contributions. That percentage '
  'describes assumed inputs, not proof that a census will pass testing or that the contributions are '
  'deductible. Two businesses with equal profit can have very different results.</p>'),
 ('Deadlines That Cannot Be Missed',
  '<p>Most qualified employer plans may be adopted by the employer tax-return due date, including '
  'extensions, and treated as adopted for the prior tax year. Adoption, employee deferral elections, deposit '
  'deadlines, and employer contribution deductibility are separate tests. Salary deferrals generally require '
  'a timely election before compensation becomes available; adopting a plan later does not authorize '
  'retroactive S-corporation payroll deferrals. A narrow first-year exception permits an individual who owns '
  'the entire unincorporated business and is its only employee to adopt a new 401(k) and make first-year '
  'elective deferrals by the unextended individual return deadline.</p><p>Defined benefit minimum funding is '
  'generally due 8.5 months after the plan year ends, normally September 15 for a calendar-year plan. '
  'Quarterly installments may apply. An October 15 extended individual tax-return deadline does not postpone '
  'that funding deadline. Contributions paid by the applicable extended employer return deadline may be '
  'deductible for the prior tax year when properly designated and within Section 404 limits; the funding and '
  'deduction calculations must both be satisfied.</p><p>Starting early leaves time for actuarial design, '
  'participant notices, elections, investment arrangements and cash planning. A December or post-year-end '
  'inquiry is not automatically too late, but the administrator must verify every deadline before promising '
  'a prior-year deduction.</p>'),
 ('Whether the Deferral Is Worth It',
  '<p>Pre-tax contributions generally defer rather than eliminate income tax. Compare current deductions, '
  'any reduction in the QBI deduction, later ordinary-income distributions, investment risk, required staff '
  'benefits and ongoing administration. Roth contributions do not produce current deductions.</p><p>A freeze '
  'may stop future accruals prospectively but does not erase already earned benefits, existing funding '
  'shortfalls, annual actuarial work or reporting. A termination can require additional funding, participant '
  'notices and PBGC procedures where covered. Size the plan for a poor year and review a business sale '
  'before committing capital.</p>')],
    takeaways=['Separate plan limits do not guarantee that both maximum contributions are deductible together.',
 'The $290,000 limit in 2026 is a defined benefit annual-benefit ceiling, not a contribution limit.',
 'Employee costs require a complete census, related-employer review and actuarial testing.',
 'Adoption, employee deferral elections, minimum funding and tax-deduction deadlines are different.',
 'The 6% rule is an exclusion within the combined deduction calculation, not a universal cap.'],
    faqs=[('How much can a business owner deduct with stacked retirement plans?',
  '<p>The amount depends on eligible compensation, age, benefit formula, plan assets, employee census, other '
  'plans and the Section 404 deduction calculations. The $250,500 illustration on this page assumes a '
  'separately validated $200,000 cash balance contribution; it is not a quoted entitlement or client '
  'result.</p>'),
 ('Can I have a 401(k) and a cash balance plan at the same time?',
  '<p>The 6% figure is not a universal contribution or deduction cap. Under Section 404(a)(7), employer '
  'defined contribution amounts up to 6% of covered compensation are excluded from the combined deduction '
  'calculation; when employer contributions exceed 6%, the excess enters the applicable combined test. '
  'Employee elective deferrals are excluded. A PBGC-covered defined benefit plan is excluded from this '
  'combined limit, but separate plan limits still apply. Have the actuary and tax preparer calculate both '
  'the minimum funding and maximum deductible contribution.</p>'),
 ('What happens if I have a bad year and cannot fund the plan?',
  '<p>Minimum required funding can remain due despite a weak year. Prospective amendments or a freeze do not '
  'erase earned benefits or funding shortfalls. Ask the actuary about funding, notice and termination '
  'options before the deadline; underfunding can cause excise taxes.</p>'),
 ('How much do these plans cost to administer?',
  '<p>A cash balance plan needs ongoing actuarial work, a written plan and applicable annual returns, '
  'typically several thousand dollars a year. These recurring costs, employee benefits and any PBGC premiums '
  'should be modeled against the projected deduction. Owner-only Form 5500-EZ filing exceptions do not '
  'remove the actuarial funding obligation.</p>')],
)

MEGA_ROTH = Spoke(
    slug="mega-backdoor-roth-business-owners",
    label="Mega backdoor Roth for business owners",
    title="Mega Backdoor Roth for Business Owners: What It Requires",
    description=(
        "How after-tax 401(k) contributions convert to Roth, the plan features "
        "required, and why business owners are better positioned than employees."
    ),
    h1="Mega Backdoor Roth for Business Owners",
    subtitle=(
        "It requires specific plan provisions. As the owner, you control the plan "
        "document that grants them."
    ),
    lead=(
        "A mega backdoor Roth uses after-tax contributions to a 401(k) plan, converted to "
        "Roth either inside the plan or by rollover, to move far more into Roth treatment "
        "than the direct Roth IRA limits permit. It is distinct from the ordinary backdoor "
        "Roth, which works through nondeductible IRA contributions and much smaller amounts. "
        "It requires plan provisions many plans do not have, which is exactly where a "
        "business owner has the advantage."
    ),
    keywords=[
        "mega backdoor roth business owner",
        "after tax 401k conversion roth",
        "mega backdoor roth solo 401k",
    ],
    body=[
        (
            "The Three Contribution Types",
            "<p>A 401(k) can accept three kinds of contribution, and the distinction is the "
            "whole mechanism.</p>"
            "<p><strong>Elective deferrals</strong>, traditional or Roth, subject to the "
            "annual deferral limit.</p>"
            "<p><strong>Employer contributions</strong>, deductible to the business.</p>"
            "<p><strong>After-tax contributions</strong>, which are neither. These are made "
            "with already-taxed dollars and are limited only by the overall annual additions "
            "limit less the other two categories. They are the raw material of the strategy: "
            "the gap between total deferrals plus employer contributions and the overall "
            "limit is the space available.</p>"
        ),
        (
            "How the Conversion Works",
            "<p>After-tax contributions sitting in the plan grow tax-deferred, and their "
            "earnings are taxable on distribution. Converting them to Roth changes that, so "
            "all future growth is tax-free.</p>"
            "<p>Two routes exist. An <strong>in-plan Roth conversion</strong> moves the "
            "after-tax balance to a Roth source inside the same plan. An <strong>in-service "
            "distribution</strong> rolls the after-tax amount to a Roth IRA outside the "
            "plan.</p>"
            "<p>Timing matters. Only the earnings on after-tax contributions are taxable at "
            "conversion, since the contributions were already taxed. Converting promptly, "
            "before meaningful earnings accrue, makes the conversion close to tax-free. "
            "Leaving after-tax money to grow for years and then converting creates a taxable "
            "event on all of that growth.</p>"
        ),
        (
            "The Plan Provisions Required",
            "<p>The strategy is not available unless the plan document permits it. Three "
            "features are needed:</p>"
            "<ul>"
            "<li>The plan must accept after-tax contributions, which is separate from "
            "accepting Roth deferrals and is a distinct provision.</li>"
            "<li>The plan must permit in-plan Roth conversions, or in-service distributions "
            "of after-tax amounts.</li>"
            "<li>The recordkeeper must track after-tax contributions and their earnings "
            "separately, since the conversion arithmetic depends on the split.</li>"
            "</ul>"
            "<p>Many corporate plans lack at least one of these, which is why employees often "
            "cannot use the strategy. A business owner adopting a solo 401(k) selects a plan "
            "document and a provider, and can simply choose ones that include all three. That "
            "control is the owner's structural advantage.</p>"
        ),
        (
            "Where Testing Gets in the Way",
            "<p>For a plan covering only the owner and a spouse, nondiscrimination testing is "
            "generally not a constraint.</p>"
            "<p>With employees, after-tax contributions are subject to the actual contribution "
            "percentage test, which compares contribution rates for highly compensated "
            "employees against everyone else. If staff make little or no after-tax "
            "contribution, and few do, the owner's permitted amount is sharply limited and "
            "excess amounts must be refunded. Safe harbor designs that solve deferral testing "
            "do not automatically solve this test.</p>"
            "<p>This is the practical reason the strategy suits owner-only plans far better "
            "than plans with staff.</p>"
        ),
        (
            "Whether Roth Is the Right Choice",
            "<p>Roth treatment forgoes a current deduction for tax-free growth, which is the "
            "opposite trade from the deduction-focused strategies most profitable owners "
            "pursue. It makes sense where the owner expects meaningful future tax on the "
            "balance, values tax-free growth over decades, or wants to avoid required minimum "
            "distributions on Roth amounts.</p>"
            "<p>It makes less sense for an owner whose priority is reducing current taxable "
            "income, particularly one near a Section 199A threshold where a deduction does "
            "double duty. For many owners the correct answer is both: maximize the deductible "
            "contributions first, then use remaining annual additions capacity for after-tax "
            "amounts converted to Roth.</p>"
        ),
    ],
    takeaways=[
        "After-tax contributions fill the gap between deferrals plus employer contributions and the overall limit.",
        "Convert promptly, since only the earnings on after-tax amounts are taxable at conversion.",
        "The plan document must permit after-tax contributions and in-plan conversions or in-service distributions.",
        "With employees, the actual contribution percentage test sharply limits the strategy.",
        "For many owners the right sequence is deductible contributions first, then after-tax to Roth.",
    ],
    faqs=[
        (
            "What is the difference between a backdoor and a mega backdoor Roth?",
            "<p>A backdoor Roth uses a nondeductible IRA contribution converted to Roth, "
            "limited to the annual IRA contribution amount. A mega backdoor Roth uses "
            "after-tax 401(k) contributions converted to Roth, which can be many times "
            "larger because it is bounded by the overall annual additions limit rather than "
            "the IRA limit.</p>",
        ),
        (
            "Does my solo 401(k) allow after-tax contributions?",
            "<p>Only if the plan document provides for them, and many standard low-cost solo "
            "401(k) documents do not. The provision is separate from accepting Roth deferrals. "
            "Owners pursuing this generally need a plan document and provider selected for "
            "these features specifically.</p>",
        ),
        (
            "Is the conversion taxable?",
            "<p>Only the earnings on the after-tax contributions are taxable, because the "
            "contributions themselves were made with taxed dollars. Converting soon after "
            "contributing, before significant earnings accrue, keeps the taxable amount "
            "minimal.</p>",
        ),
        (
            "Can I do this if I have employees?",
            "<p>It is much harder. After-tax contributions are subject to the actual "
            "contribution percentage test, and if employees make little after-tax "
            "contribution the owner's permitted amount is sharply limited with excess amounts "
            "refunded. The strategy is best suited to owner-only plans.</p>",
        ),
    ],
)

SCORP_DESIGN = Spoke(
    slug="retirement-plan-design-s-corp-owners",
    label="Retirement plan design for S-Corp owners",
    title="Retirement Plan Design for S-Corp Owners",
    description=(
        "Why S-corp retirement capacity is driven by W-2 wages rather than profit, and "
        "how that changes the reasonable compensation decision."
    ),
    h1="Retirement Plan Design for S-Corp Owners",
    subtitle=(
        "Distributions do not count. Only W-2 wages create contribution capacity, "
        "which links plan design directly to the compensation figure."
    ),
    lead=(
        "For an S-corp owner, retirement plan contribution capacity is calculated on W-2 "
        "wages, not on total profit. Distributions, however large, create no capacity. This "
        "single rule links plan design directly to the reasonable compensation decision, and "
        "it means an owner who minimizes wages to reduce payroll tax may be capping the "
        "largest deduction available to them."
    ),
    keywords=[
        "s corp retirement plan design",
        "s corp owner 401k contribution wages",
        "retirement plan s corporation owner",
    ],
    body=[
        (
            "Why Wages Are the Only Input",
            "<p>Retirement plan limits are defined in terms of compensation, and for an "
            "S-corp shareholder-employee, compensation means W-2 wages. Pass-through income "
            "reported on the K-1 is not compensation for this purpose.</p>"
            "<p>The consequence is direct. An owner with $700,000 of profit taking $80,000 in "
            "wages has plan capacity calculated on $80,000, not $700,000. The employer "
            "contribution, expressed as a percentage of compensation, is computed on the "
            "smaller figure, and a cash balance plan's actuarial sizing works from it too.</p>"
            "<p>This differs from a sole proprietorship or partnership, where net "
            "self-employment earnings serve as the compensation base, so the entire profit "
            "contributes to capacity. It is one of the few respects in which the S election "
            "works against the owner.</p>"
        ),
        (
            "The Tension With Payroll Tax Minimization",
            "<p>The two goals pull in opposite directions. Minimizing wages reduces payroll "
            "tax. Maximizing wages increases retirement capacity and, above the Section 199A "
            "thresholds, raises the W-2 wage limitation that caps the qualified business "
            "income deduction.</p>"
            "<p>The arithmetic frequently favors higher wages at this profit level. Additional "
            "wages cost the Medicare component, roughly 3.8 percent including the additional "
            "tax, since the Social Security base is already cleared. Those same wages create "
            "retirement capacity generating a deduction at a marginal rate above 37 percent, "
            "and may lift the Section 199A cap.</p>"
            "<p>Paying 3.8 percent to enable a deduction worth 37 percent or more is usually "
            "a good trade, and it is the opposite of the advice owners commonly receive.</p>"
        ),
        (
            "Sizing Wages to the Plan",
            "<p>The workable sequence:</p>"
            "<ol>"
            "<li>Establish the reasonable compensation floor from role, hours, and market "
            "data. This is the minimum, and it is not optional.</li>"
            "<li>Determine the target plan contribution, including any cash balance "
            "component, from the actuarial study.</li>"
            "<li>Calculate the wage level required to support that contribution.</li>"
            "<li>Take the higher of the compensation floor and the wage the plan requires.</li>"
            "<li>Test the result against the Section 199A limitation, since the same wage "
            "figure feeds that calculation.</li>"
            "</ol>"
            "<p>Where the plan requires a wage above the reasonable compensation floor, that "
            "is entirely permissible. Reasonable compensation is a minimum, not a ceiling. "
            "Paying more than the floor is never the compliance risk; paying less is.</p>"
        ),
        (
            "The Cash Balance Layer",
            "<p>A cash balance plan layered on a solo 401(k) is where S-corp owners find the "
            "largest deductions, and wage sizing matters even more here. The actuarial "
            "calculation works from compensation, so an owner targeting a $180,000 cash "
            "balance contribution needs a wage level that supports it.</p>"
            "<p>This often means paying wages well above what a pure payroll tax analysis "
            "would suggest. The additional Medicare cost on the incremental wages is small "
            "against a six-figure deduction, and the trade is usually clearly favorable once "
            "modeled.</p>"
        ),
        (
            "Spouse Compensation",
            "<p>Where a spouse genuinely works in the business, paying them a reasonable wage "
            "creates separate plan capacity for them, effectively doubling the household's "
            "contribution room. It also adds W-2 wages that count toward the Section 199A "
            "limitation.</p>"
            "<p>The requirement is that the work is real and the wage reflects it. Wages paid "
            "for no genuine services are disallowed, and they undermine the compensation "
            "position for the owner as well, which is a disproportionate cost for a modest "
            "benefit.</p>"
        ),
    ],
    takeaways=[
        "S-corp plan capacity is calculated on W-2 wages; distributions create none.",
        "Minimizing wages for payroll tax can cap the largest deduction available to the owner.",
        "Paying 3.8 percent Medicare to enable a deduction worth 37 percent is usually a good trade.",
        "Reasonable compensation is a floor, not a ceiling; paying above it is not a compliance risk.",
        "A genuinely employed spouse creates separate plan capacity and adds Section 199A wages.",
    ],
    faqs=[
        (
            "Can S-corp distributions count toward retirement contributions?",
            "<p>No. Only W-2 wages count as compensation for retirement plan purposes. "
            "Distributions, regardless of size, create no contribution capacity, which is why "
            "an S-corp owner's plan design is tied directly to the wage decision.</p>",
        ),
        (
            "Should I raise my salary to contribute more to retirement?",
            "<p>Often yes at this profit level. Additional wages cost roughly 3.8 percent in "
            "Medicare tax once the Social Security base is cleared, while creating capacity "
            "for deductions at a marginal rate above 37 percent, and potentially raising the "
            "Section 199A wage limitation. The combination usually favors the higher wage.</p>",
        ),
        (
            "Is paying myself more than reasonable compensation a problem?",
            "<p>No. Reasonable compensation is a minimum designed to prevent understating "
            "wages. Paying above it is permitted. The compliance risk runs entirely in the "
            "other direction.</p>",
        ),
        (
            "Can I pay my spouse to increase our contributions?",
            "<p>Yes, where the spouse performs genuine services and the wage reflects them. "
            "This creates separate plan capacity and adds W-2 wages for the Section 199A "
            "limitation. Wages for work not actually performed are disallowed and weaken the "
            "compensation position for the whole entity.</p>",
        ),
    ],
)

CLUSTER = Cluster(
    key="retirement",
    slug=P,
    label="Retirement Plan Tax Strategy",
    title="Retirement Plan Tax Strategy for Business Owners: The Complete Guide",
    description=(
        "How profitable business owners use plan design to deduct $150,000 to $250,000 "
        "a year, and how the choice of plan interacts with entity structure."
    ),
    h1="Retirement Plan Tax Strategy for Business Owners",
    subtitle=(
        "The largest deduction most profitable owners will ever access, and the one "
        "most often left on the table."
    ),
    lead=(
        "Retirement plan tax strategy for business owners is the design of qualified plans "
        "to maximize deductible contributions rather than simply to save for retirement. For "
        "a business earning $500,000 or more, a properly designed combination of a defined "
        "contribution plan and a defined benefit or cash balance plan routinely supports "
        "$150,000 to $250,000 in annual deductions, which is larger than any other strategy "
        "available from ordinary operations."
    ),
    keywords=[
        "retirement plan tax strategy business owner",
        "cash balance plan business owner deduction",
        "business owner retirement plan design",
        "maximum retirement deduction high income",
    ],
    body=[
        (
            "Why This Is the Largest Lever",
            "<p>Most tax strategies available to a profitable business owner produce "
            "deductions measured in tens of thousands. Retirement plan design produces "
            "deductions measured in hundreds of thousands, and it does so without acquiring "
            "an asset, changing entity structure, or taking a position that depends on facts "
            "an examiner might see differently.</p>"
            "<p>It is also the most consistently underused, for a structural reason. Plan "
            "design requires an actuarial study, a plan document, and a decision before a "
            "deadline that falls long before the return is filed. A return preparation "
            "engagement has no natural point at which to raise it, so in a compliance-only "
            "relationship it usually never comes up.</p>"
        ),
        (
            "The Plan Types That Matter",
            "<p><strong>Solo 401(k).</strong> For an owner with no employees other than a "
            "spouse. Combines an employee deferral with an employer contribution, permits "
            "Roth treatment, and serves as the base layer for stacking.</p>"
            "<p><strong>SEP IRA.</strong> Employer contributions only, simple to administer, "
            "and importantly can be established after year-end. Its drawback is that SEP "
            "balances interfere with backdoor Roth conversions through the pro-rata rule.</p>"
            "<p><strong>Safe harbor 401(k).</strong> Where there are employees. A required "
            "employer contribution buys a pass on the deferral nondiscrimination testing that "
            "otherwise limits owner contributions.</p>"
            "<p><strong>Cash balance plan.</strong> A defined benefit plan expressed as "
            "hypothetical account balances. This is where the large numbers come from, "
            "because contributions are sized actuarially rather than by a fixed dollar "
            "limit.</p>"
            "<p><strong>Traditional defined benefit plan.</strong> Similar in effect, "
            "expressed as a monthly retirement benefit, and can support even larger "
            "contributions for an older owner.</p>"
            "<p>The choice between a cash balance plan and a traditional defined benefit plan "
            "is mostly one of presentation and volatility. Cash balance plans state the "
            "benefit as an account balance, which owners and employees find easier to "
            "understand, and their interest crediting rate can be set to reduce the swings in "
            "required contributions that a traditional plan can produce when investment "
            "returns miss the assumption. For most owners at this profit level the cash "
            "balance design is the practical default, with the traditional plan reserved for "
            "cases where an older owner wants the largest possible contribution and can "
            "tolerate more year-to-year variability in it.</p>"
        ),
        (
            "The Stacking Structure",
            "<p>Defined contribution and defined benefit plans are governed by separate "
            "limits, which is what allows them to be combined.</p>"
            "<p>A defined contribution plan is capped by an annual additions limit expressed "
            "as a dollar figure. A defined benefit plan is limited instead by the benefit it "
            "is designed to pay at retirement; the contribution is whatever an actuary "
            "determines is needed to fund that benefit. An owner closer to retirement has "
            "fewer years to fund the same benefit, so the required annual contribution is "
            "much larger.</p>"
            "<p>This is why age is an asset in plan design. A 55-year-old owner and a "
            "35-year-old owner with identical profit have very different deduction capacity, "
            "and the difference runs to six figures.</p>"
        ),
        (
            "Entity Structure Sets the Ceiling",
            "<p>Contribution capacity is calculated on compensation, and what counts as "
            "compensation depends on entity structure.</p>"
            "<p>For an S-corp shareholder-employee, compensation means W-2 wages. "
            "Distributions create no capacity at all. An owner with $700,000 of profit taking "
            "$80,000 in wages has capacity computed on $80,000.</p>"
            "<p>For a sole proprietorship or partnership, net self-employment earnings serve "
            "as the base, so the full profit contributes.</p>"
            "<p>This produces a tension specific to S-corps. Minimizing wages reduces payroll "
            "tax but caps retirement capacity. At this profit level the arithmetic usually "
            "favors higher wages: the incremental cost is the Medicare component, roughly 3.8 "
            "percent once the Social Security base is cleared, while the capacity created "
            "produces deductions at a marginal rate above 37 percent. Paying 3.8 percent to "
            "unlock a 37 percent deduction is a trade worth making, and it is the opposite of "
            "the advice owners usually receive.</p>"
        ),
        (
            "What Employees Cost",
            "<p>With staff, the question shifts from what the owner can contribute to what "
            "share of total contributions reaches the owner.</p>"
            "<p>Plans covering employees must satisfy coverage and nondiscrimination "
            "requirements. A well-designed combination frequently still directs 80 to 90 "
            "percent of contributions to the owner, using cross-tested or new comparability "
            "designs that rely on older participants having fewer years to accumulate "
            "benefits.</p>"
            "<p>The employee cost is real, deductible, and often lower than owners expect. It "
            "cannot be estimated from profit alone; it requires a census-based study, and two "
            "businesses with identical profit and different workforce demographics can reach "
            "very different conclusions.</p>"
        ),
        (
            "The Deadlines",
            "<p>Deadlines vary by plan type and are the most common way this deduction is "
            "lost:</p>"
            "<ul>"
            "<li>A new defined benefit or cash balance plan generally must be established "
            "before the plan year ends. Missing this forfeits the year entirely.</li>"
            "<li>Solo 401(k) rules differ between the employee deferral and the employer "
            "contribution, with the employer portion generally fundable up to the extended "
            "filing deadline.</li>"
            "<li>A SEP IRA can generally be established and funded up to the extended filing "
            "deadline, which is its main advantage.</li>"
            "</ul>"
            "<p>Because a cash balance plan needs an actuarial study, a document, and a trust "
            "account, the practical lead time is weeks. An owner raising this in December is "
            "usually too late; raising it in the third quarter is what makes it available.</p>"
        ),
        (
            "How This Interacts With Section 199A",
            "<p>Retirement contributions do more than generate their own deduction. They "
            "reduce taxable income, which changes where the owner sits relative to the "
            "Section 199A thresholds.</p>"
            "<p>For a specified service business owner, health, law, accounting, consulting "
            "and similar fields, the qualified business income deduction phases out entirely "
            "above the threshold range. A large retirement contribution can pull taxable "
            "income back into the phase-out range and restore a deduction that no amount of "
            "wage adjustment could reach.</p>"
            "<p>This makes the contribution worth considerably more than its face value, and "
            "it is a clear illustration of why these strategies are modeled together rather "
            "than evaluated one at a time.</p>"
        ),
        (
            "A Worked Example",
            "<p>Consider an owner aged 53 running an S-corp with $900,000 of profit and four "
            "employees averaging 38 years old.</p>"
            "<p>Under a compliance-only relationship, the typical position is a solo 401(k) "
            "or a modest SEP, a wage set as low as anyone felt comfortable defending, and a "
            "contribution somewhere in the low tens of thousands.</p>"
            "<p>Designed deliberately, the picture changes. The wage is set at the level the "
            "plan requires rather than the minimum defensible figure, which costs roughly 3.8 "
            "percent in Medicare tax on the increment. A safe harbor 401(k) handles the "
            "deferral testing and provides the required employee contribution. A cash balance "
            "plan is layered on top, cross-tested so that the bulk of the contribution is "
            "directed to the owner given the age gap between the owner and the staff.</p>"
            "<p>The combined owner deduction lands in the low-to-mid $200,000 range, with an "
            "employee cost that is real, deductible, and typically a modest fraction of the "
            "total. Against a marginal rate above 37 percent federal plus state, the annual "
            "tax effect is well into six figures. The difference between the two outcomes is "
            "not a different tax law. It is that someone modeled the census and set the wage "
            "to the plan rather than to the payroll tax line.</p>"
        ),
        (
            "Where This Fits in the Overall Plan",
            "<p>Plan design does not sit on its own. It sits third in a sequence, and its "
            "position is not arbitrary.</p>"
            "<p>Entity structure comes first, because the classification determines whether "
            "capacity is computed on W-2 wages or on self-employment earnings. Compensation "
            "comes second, because the wage figure sets the ceiling on what any plan can "
            "absorb. Plan design comes third, working within those constraints. Depreciation "
            "and state elections come after, and they matter here because they also reduce "
            "taxable income and can change whether a contribution is still needed to reach a "
            "Section 199A threshold.</p>"
            "<p>Running these in the wrong order is the most common way the deduction gets "
            "undersized. An owner who fixed their wage in January for payroll tax reasons has "
            "already capped the plan before anyone looked at what the plan could have "
            "absorbed.</p>"
        ),
        (
            "The Commitment This Represents",
            "<p>These plans are not free options. Defined benefit contributions are a funding "
            "obligation rather than a discretionary choice, so a poor year still requires the "
            "contribution, and underfunding carries excise tax exposure. Plans are also "
            "expected to be maintained for a meaningful period; establishing and terminating "
            "one after two years to capture deductions invites challenge.</p>"
            "<p>The practical implication is to size the benefit formula to a contribution "
            "the business can sustain through a bad year, not just a good one. A conservative "
            "formula with room to make additional discretionary contributions is generally "
            "better than an aggressive one that becomes a liability when profit falls.</p>"
            "<p>The deferral case also depends on rates. A deduction taken at 37 percent "
            "federal plus state against distributions later taken at a lower rate is a real "
            "gain, as is decades of compounding on untaxed amounts. For an owner who expects "
            "the same bracket in retirement, or who needs the capital working in the business, "
            "the case is weaker and should be modeled rather than assumed.</p>"
        ),
    ],
    takeaways=[
        "Plan design produces the largest deduction available to most profitable owners.",
        "Defined contribution and defined benefit plans have separate limits and stack together.",
        "Contribution capacity rises sharply with owner age, because there are fewer years to fund.",
        "For S-corp owners, only W-2 wages create capacity, which argues for higher wages than payroll tax alone suggests.",
        "New cash balance plans generally must be established before the plan year ends.",
        "Contributions can restore a Section 199A deduction for service businesses above the phase-out.",
    ],
    faqs=[
        (
            "How much can a business owner deduct through retirement plans?",
            "<p>With a solo 401(k) and a cash balance plan combined, commonly $150,000 to "
            "$250,000 annually for an owner in their forties or fifties, and more for an "
            "owner in their sixties. The defined benefit component is sized actuarially by "
            "age, compensation, and the benefit targeted rather than by a fixed limit.</p>",
        ),
        (
            "What is a cash balance plan?",
            "<p>A defined benefit plan that expresses each participant's benefit as a "
            "hypothetical account balance. Contributions are determined by an actuary based "
            "on what must be funded to provide the stated benefit at retirement, which is why "
            "they can far exceed defined contribution limits, particularly for older "
            "owners.</p>",
        ),
        (
            "Do I need employees to be covered?",
            "<p>If you have eligible employees, yes, and the plan must satisfy coverage and "
            "nondiscrimination requirements. Cross-tested designs frequently still direct 80 "
            "to 90 percent of total contributions to the owner. The employee cost requires a "
            "census-based study and cannot be estimated from profit alone.</p>",
        ),
        (
            "When do I need to set up the plan?",
            "<p>A new defined benefit or cash balance plan generally must be established "
            "before the plan year ends, and the practical lead time is weeks because of the "
            "actuarial study and plan document. A SEP IRA can generally be established up to "
            "the extended filing deadline, which makes it the fallback when the year has "
            "already closed.</p>",
        ),
        (
            "Should S-corp owners raise their salary to contribute more?",
            "<p>Often yes at this profit level. Additional wages cost roughly 3.8 percent in "
            "Medicare tax once the Social Security wage base is cleared, while creating "
            "capacity for deductions at a marginal rate above 37 percent and potentially "
            "raising the Section 199A wage limitation.</p>",
        ),
        (
            "What if I have a bad year and cannot fund the plan?",
            "<p>Defined benefit contributions are a funding obligation, and underfunding "
            "carries excise tax exposure. Plans can be frozen or amended prospectively, and "
            "the benefit formula can be set conservatively from the outset. Sizing the plan "
            "to a sustainable contribution is part of the design work.</p>",
        ),
        (
            "Is deferring tax actually worth it?",
            "<p>It is when the deduction comes off at a high marginal rate and distributions "
            "occur later at a lower one, and when decades of compounding run on amounts never "
            "taxed. It is weaker for an owner expecting the same bracket in retirement or who "
            "needs the capital in the business, which is why it should be modeled.</p>",
        ),
        (
            "How much do these plans cost to run?",
            "<p>A cash balance plan requires annual actuarial certification, a plan document, "
            "and Form 5500 filing, typically several thousand dollars annually. Against a "
            "deduction of $150,000 or more the ratio is strongly favorable, but the cost "
            "recurs and belongs in the model.</p>",
        ),
    ],
    spokes=[
        Spoke(
            slug="cash-balance-plan-tax-deduction",
            label="Cash Balance Plan for business owners",
            adopted=True,
        ),
        SOLO_VS_SEP,
        STACKING,
        Spoke(
            slug="defined-benefit-plans-tax-shelter-high-income-business-owners",
            label="Defined benefit plans for business owners over 50",
            adopted=True,
        ),
        MEGA_ROTH,
        SCORP_DESIGN,
    ],
)
