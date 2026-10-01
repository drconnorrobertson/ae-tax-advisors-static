"""Publish distinct owner guides on Section 461(l), preserving the site chrome."""
import re
import site_template as T

DATE = '2026-09-30'
MAIN = '/blog/excess-business-loss-limitation-461l-2026/'
SOURCES = [
 ('https://www.irs.gov/instructions/i461', 'IRS Instructions for Form 461 (2025): definition, employee-income exclusion and ordering rules'),
 ('https://www.irs.gov/pub/irs-drop/rp-25-32.pdf', 'IRS Revenue Procedure 2025-32, section 4.31: 2026 thresholds'),
 ('https://www.irs.gov/publications/p925', 'IRS Publication 925: passive activity and at-risk rules'),
 ('https://www.irs.gov/instructions/i172', 'IRS Instructions for Form 172: NOL calculations and carryforwards'),
 ('https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis', 'IRS: S corporation shareholder loss limitations'),
]
POSTS = [
dict(path=MAIN, title='How Does the Excess Business Loss Limitation Work in 2026?', category='Business Deductions',
description='Understand Section 461(l), the 2025 and 2026 loss limits, Form 461, W-2 income and NOL carryforwards with worked business-owner examples.',
lead='The excess business loss rule limits how much a noncorporate taxpayer can deduct when aggregate business deductions exceed aggregate business income and gains. The excess is deferred as a net operating loss carryforward. For 2026, the threshold is $256,000 for non-joint returns and $512,000 for joint returns.',
body='''<h2>A business loss and an excess business loss are different</h2>
<p>A business can report a legitimate tax loss without producing an excess business loss on its owner’s return. Section 461(l) asks a second question: after combining the owner’s qualifying business activity, how much of the net loss exceeds the annual threshold? It applies to noncorporate taxpayers, including individual owners of sole proprietorships, partnerships and S corporations. A C corporation is outside this particular rule.</p>
<p>This is a limit on the current deduction, not a tax rate or a cap on the amount a business can lose. It also does not give each LLC its own allowance. On a joint return, both spouses’ qualifying business items enter one calculation.</p>
<h2>Use the threshold for the correct tax year</h2>
<div style="overflow-x:auto"><table><caption>Federal excess business loss thresholds</caption><thead><tr><th scope="col">Tax year</th><th scope="col">Non-joint returns</th><th scope="col">Joint returns</th></tr></thead><tbody><tr><th scope="row">2025</th><td>$313,000</td><td>$626,000</td></tr><tr><th scope="row">2026</th><td>$256,000</td><td>$512,000</td></tr></tbody></table></div>
<p>The 2025 legislation made the limitation permanent and changed the inflation-adjustment framework used for 2026. Do not carry the 2025 amount into a 2026 projection. A return filed in 2026 for tax year 2025 still uses the 2025 rules. Revenue Procedure 2025-32, section 4.31, supplies the 2026 amounts.</p>
<h2>The simplified calculation</h2>
<p><strong>Excess business loss = the greater of zero or qualifying business deductions minus qualifying business income and gains minus the applicable threshold.</strong> This summary assumes the earlier loss limitations have already been applied. Form 461 contains adjustments that a simple profit-and-loss statement does not capture.</p>
<p>Employee compensation, including W-2 wages, is excluded from the business-income side of this calculation. NOL and Section 199A deductions are also excluded when figuring business deductions. Capital asset losses are excluded, and business capital gains enter under a specific statutory limit. Portfolio income does not become business income simply because it appears on the same return.</p>
<h2>Example: a joint filer with two businesses</h2>
<p>Assume a married couple filing jointly in 2026 has a $900,000 allowable loss from Business A and $200,000 of qualifying net income from Business B. Their aggregate net business loss is $700,000. Subtracting the $512,000 threshold produces a $188,000 excess business loss. The Section 461(l) adjustment leaves a $512,000 net business loss for the current return, subject to the rest of the return calculation.</p>
<p>If Business B instead produces $500,000 of qualifying net income, the aggregate loss becomes $400,000. That is below the joint threshold, so this example has no excess business loss. The rule aggregates income as well as losses. Neither result is a promise of a specific refund.</p>
<h2>Apply the other limitations first</h2>
<p>For pass-through owners, review basis, then the at-risk rules, then passive activity restrictions, and then Section 461(l). A loss suspended for insufficient basis or under the passive activity rules is not automatically an NOL. Track each limitation separately so a future release goes through the remaining rules correctly.</p>
<h2>What happens to the deferred amount?</h2>
<p>The disallowed excess is treated as an NOL carryforward for subsequent years. Modern NOL carryforwards generally face an 80% limitation based on specially computed taxable income. The excess-business-loss threshold and the NOL limit are separate tests applied at different stages.</p>
<h2>What to review before year-end</h2>
<p>Prepare one schedule covering every qualifying business, both spouses if filing jointly, projected depreciation and losses released from earlier years. Reconcile it to basis schedules, participation records and prior carryforwards. Then compare current tax, future NOL use and cash needs. A large deduction can be valid while its immediate tax benefit is much smaller than the headline amount.</p>''',
faqs=[('Is the limit per business?', '<p>No. It applies to aggregate qualifying business items at the taxpayer level, including both spouses on a joint return.</p>'), ('Is the deferred deduction lost forever?', '<p>The excess becomes an NOL carryforward. Its future use depends on the NOL rules and the taxpayer’s later income.</p>'), ('Does a profitable business avoid the rule?', '<p>Its income enters the aggregate calculation, but the owner can still have an excess loss if other qualifying businesses produce larger losses.</p>')]),
dict(path='/blog/excess-business-loss-w2-income/',title='Can Excess Business Losses Offset W-2 Income?',category='High-Income Planning',
description='See why W-2 wages do not increase the Section 461(l) allowance and how a large business loss can leave a high-income employee with taxable income.',
lead='An otherwise allowable business loss can reduce W-2 income, but Section 461(l) can defer part of that loss. Your wages do not increase the business-income amount used to calculate the excess business loss.',
body='''<h2>Wages do not expand the loss allowance</h2>
<p>A common planning error is treating a $1 million salary as $1 million of business income for Form 461. The law excludes income from providing services as an employee. This remains true when the employee also owns the company paying the wages. Genuine pass-through business income has a different role in the calculation.</p>
<p>The distinction matters for physicians, executives and other employees buying businesses or rental properties with large depreciation deductions. The wage total tells you the income you would like to offset. It does not tell you the amount of business loss you can use this year.</p>
<h2>Example: $1 million of wages and an $800,000 loss</h2>
<p>Assume a joint return for 2026 has $1 million in W-2 wages, an $800,000 qualifying net business loss, no other business income, and no earlier restriction on that loss. The excess is $800,000 minus $512,000, or $288,000. The current net business loss after the excess-loss adjustment is $512,000.</p>
<p>Combining only these two items leaves $488,000 before other adjustments and deductions. It does not leave $200,000. The $288,000 difference is carried forward under the NOL rules. This is an illustration of income arithmetic, not a completed taxable-income or tax-liability calculation.</p>
<h2>What changes for a non-joint filer?</h2>
<p>With the same assumptions and a non-joint 2026 return, the threshold is $256,000. The excess would be $544,000 and the current net business loss would be $256,000. Using a joint threshold in a single-filer model would materially overstate the current deduction.</p>
<h2>Business income can change the outcome</h2>
<p>Now give the joint filers $300,000 of qualifying net pass-through income in addition to their wages and the $800,000 loss. The aggregate net business loss becomes $500,000, below the $512,000 threshold. The example has no Section 461(l) deferral. The salary still does not count toward the business-income calculation.</p>
<p>Do not use this arithmetic as a reason to relabel compensation. Payroll classification and reasonable compensation must remain correct. A model should distinguish W-2 compensation, pass-through profit, portfolio income and distributions using the actual legal and tax treatment of each item.</p>
<h2>Rental losses need another review before reaching this test</h2>
<p>A rental loss must first be deductible under the relevant passive activity and other restrictions. Buying an Airbnb, obtaining a cost segregation report or spending time at a property does not by itself establish a current wage offset. Read the <a href="/blog/excess-business-loss-short-term-rental/">short-term rental guide</a> for that sequence.</p>
<h2>Ask for a projection showing the adjustment</h2>
<p>A useful projection shows the loss before limits, the loss allowed after each limit, the excess-loss addback and the carryforward. If an estimate merely multiplies the full depreciation deduction by your highest marginal tax rate, request the complete owner-return calculation before relying on it for a purchase decision.</p>''',
faqs=[('Do my spouse’s wages count as business income?', '<p>No. Employee wages remain excluded even when both spouses file jointly.</p>'),('Can a carryforward reduce wages in a later year?', '<p>An NOL deduction can generally reduce later taxable income that includes wages, subject to the NOL calculation and applicable limits. It is not restricted to the original business’s future profit.</p>')]),
dict(path='/blog/excess-business-loss-short-term-rental/',title='Excess Business Loss Limits for Short-Term Rental Owners',category='Short-Term Rentals',
description='Learn why a nonpassive short-term rental loss can still be limited by Section 461(l), with a 2026 example and a rental-record checklist.',
lead='A short-term rental loss that passes the passive activity rules can still be limited by the excess business loss rule. Nonpassive treatment opens one gate; it does not guarantee that the full depreciation deduction offsets wages this year.',
body='''<h2>Establish the rental’s actual tax treatment</h2>
<p>For the passive activity rules, an activity with an average period of customer use of seven days or less is generally outside the rental-activity definition. The owner still needs to evaluate material participation. Other exceptions have their own requirements. A property’s listing category or nightly price does not establish the result.</p>
<p>Longer-term rentals follow a different passive-activity analysis. Real estate professional status alone is also insufficient without the necessary material participation analysis. Section 461(l) asks a separate question about trade or business items; do not assume every Schedule E item qualifies automatically.</p>
<h2>Trace the deduction through the return</h2>
<p>First establish a supportable depreciation deduction, including basis and placed-in-service facts. Then apply applicable basis and at-risk restrictions, followed by the passive activity rules. Only losses allowed through those steps enter the excess business loss analysis where attributable to a trade or business.</p>
<p>Keep the passive-loss worksheet separate from the excess-loss worksheet. A suspended passive loss and an NOL carryforward may both represent future deductions, but they are not interchangeable. They have different release conditions and reporting requirements.</p>
<h2>Example: a nonpassive rental loss larger than the threshold</h2>
<p>Assume joint filers in 2026 have $900,000 of W-2 income and a $700,000 short-term rental tax loss. For this example, the rental is a trade or business, the owners satisfy the relevant participation requirements, all earlier limitations allow the loss, and there is no other business income.</p>
<p>The excess is $700,000 minus $512,000, or $188,000. The current net business loss is $512,000 after the adjustment. Combining the wages and allowed business loss leaves $388,000 before other adjustments and deductions. Nonpassive treatment did not permit the full $700,000 wage offset.</p>
<h2>What if the owners also have operating-business profit?</h2>
<p>With $250,000 of qualifying operating-business net income, the same $700,000 rental loss produces a $450,000 aggregate net business loss. That falls below the 2026 joint threshold. This simplified example has no excess-loss deferral. Aggregating the owner’s full business picture can therefore change the result substantially.</p>
<h2>Records to collect before projecting savings</h2>
<ul><li>Booking records supporting average customer-use periods.</li><li>Participation records identifying the work performed and who performed it.</li><li>Closing documents, land allocation, improvement records and depreciation schedules.</li><li>Loan and ownership records supporting basis and amounts at risk.</li><li>Prior passive losses and NOL workpapers, plus all other business income.</li></ul>
<p>Personal-use days and vacation-home restrictions also need review. The numerical examples here assume those rules do not restrict the deduction. Do not use a projected tax loss as a substitute for a rental’s operating cash-flow analysis.</p>
<h2>Model the tax benefit separately from the study deduction</h2>
<p>A cost segregation study addresses asset classification and depreciation. The owner’s return determines when that deduction becomes usable. Have the advisor present current-year use, suspended amounts and expected carryforward use alongside the study estimate. See the <a href="/blog/excess-business-loss-cost-segregation/">cost segregation and excess-loss guide</a> for the timing comparison.</p>''',
faqs=[('Does material participation eliminate Section 461(l)?','<p>No. Material participation addresses passive activity treatment. The excess business loss limit is a separate owner-level test.</p>'),('Does every short-term rental loss offset wages?', '<p>No. The facts must support the deduction and the activity’s tax treatment, and each applicable loss limitation must be applied.</p>')]),
dict(path='/blog/excess-business-loss-cost-segregation/',title='Cost Segregation and Excess Business Loss: How Much Can You Use?',category='Cost Segregation',
description='Compare a cost segregation deduction with the loss actually usable in 2026, including business income, Section 461(l) and carryforward timing.',
lead='A cost segregation study may accelerate depreciation without delivering an equally large current-year tax benefit. Section 461(l) can defer an otherwise allowable net business loss after the other loss limitations have been applied.',
body='''<h2>The study amount is only the starting point</h2>
<p>A depreciation estimate is an asset-level calculation. Tax savings require an owner-level calculation. Between those two numbers sit rental operations, other income, ownership allocations, basis, amounts at risk, passive restrictions and the excess business loss test. The most useful report states each assumption rather than presenting one deduction as a guaranteed refund.</p>
<h2>Example: $1.1 million of depreciation is not a $1.1 million net loss</h2>
<p>Assume a joint-filing owner has a rental trade or business with $200,000 of net income before depreciation and $1.1 million of allowable depreciation. The rental tax loss is $900,000. Assume all earlier loss limits are satisfied and there is no other business income in 2026.</p>
<p>The $900,000 loss exceeds the $512,000 joint threshold by $388,000. Section 461(l) defers that excess. A proposal that applies a marginal tax rate to the full $1.1 million ignores both the $200,000 of operating income absorbed by depreciation and the $388,000 excess-loss adjustment.</p>
<h2>Add the owner’s other business activity</h2>
<p>If the same owner also has $500,000 of qualifying operating-business net income, the aggregate business loss is $400,000. The example then has no excess business loss. If the $500,000 instead consists entirely of W-2 wages, it does not reduce the $900,000 net business loss used for this test.</p>
<p>A multi-property investor needs a consolidated schedule, not an independent savings claim for every property. Multiple depreciation studies can compete for the same current-year allowance. New LLCs do not create new Section 461(l) thresholds.</p>
<h2>Compare deduction timing across several years</h2>
<p>Where available, compare accelerated depreciation with applicable election alternatives and future income forecasts. For each scenario, show current tax, future tax, the carryforward balance and after-tax cash. A deferred deduction can remain valuable, but its timing should be visible before fees and purchases are committed.</p>
<p>Do not assume you can elect any arbitrary depreciation amount. Bonus depreciation elections and other depreciation choices have their own scope, deadlines and consistency rules. The advisor must identify the actual permitted election, affected asset classes and consequences before including it in a plan.</p>
<h2>Keep financing separate from tax use</h2>
<p>Borrowing can help pay for property, but cash borrowed is not business profit that expands the excess-loss calculation. Basis and at-risk treatment of debt also require their own review. A funded purchase and a currently deductible loss are separate conclusions.</p>
<h2>Questions to ask before commissioning a study</h2>
<ul><li>What is the property’s net tax result after ordinary operations and depreciation?</li><li>Which earlier limitations might suspend the loss?</li><li>How much other qualifying business income is on the owner’s return?</li><li>What is the excess-loss adjustment for the correct filing status and year?</li><li>When is the deferred deduction expected to be used?</li></ul>
<p>AE Tax Advisors can evaluate the study estimate within the owner’s broader return. Bring the proposed deduction, operating forecast and prior carryforward workpapers to a <a href="/discovery/">discovery call</a>.</p>''',
faqs=[('Does cost segregation bypass the loss limit?', '<p>No. Accelerating depreciation does not override owner-level loss restrictions.</p>'),('Does a separate LLC provide a separate allowance?', '<p>No. The excess business loss calculation aggregates qualifying business items at the taxpayer level.</p>')]),
dict(path='/blog/excess-business-loss-s-corporation-partnership/',title='Excess Business Loss Rules for S Corporations and Partnerships',category='S-Corp Planning',
description='Trace S corporation and partnership K-1 losses through basis, at-risk, passive activity and Section 461(l), with multi-entity owner examples.',
lead='An S corporation or partnership reports the owner’s allocated items, but the excess business loss limitation is determined at the owner level. Receiving a K-1 with a loss does not establish that the entire loss is deductible this year.',
body='''<h2>Four limitations, in the right order</h2>
<p>The IRS identifies four shareholder loss limitations for S corporations: stock and debt basis, at-risk restrictions, passive activity limits and excess business losses. Review them in that order. Partnership owners also need their applicable outside-basis analysis before proceeding through the remaining restrictions.</p>
<p>Each worksheet answers a different question. Basis measures tax investment under the applicable entity rules. The at-risk rules measure qualifying economic exposure. Passive restrictions address the owner’s activity and permitted offsets. Section 461(l) then evaluates aggregate business losses against the owner’s annual threshold.</p>
<h2>Example: the K-1 loss exceeds available basis</h2>
<p>Assume a non-joint filer receives an S corporation K-1 reporting a $600,000 ordinary business loss for 2026. The shareholder’s properly computed basis permits only $350,000. Assume the at-risk and passive rules allow that $350,000, and the shareholder has no other qualifying business items.</p>
<p>The $250,000 blocked by basis remains a basis-suspended loss. Of the $350,000 reaching Section 461(l), $94,000 exceeds the $256,000 threshold. That $94,000 is the excess business loss treated as an NOL carryforward. The illustration leaves a $256,000 current net business loss and two distinct deferred balances.</p>
<p>Calling the entire $344,000 deferred amount an NOL would be incorrect. The $250,000 basis suspension needs its own tracking and future basis analysis. When a suspended deduction later becomes allowable, review the other applicable limitations for that later year.</p>
<h2>Example: profitable and loss-making pass-throughs</h2>
<p>Assume joint filers in 2026 have a $700,000 allowable partnership business loss and $250,000 of qualifying S corporation net income. The aggregate business loss is $450,000, below the $512,000 threshold. If the $250,000 were employee wages instead, it would not enter that business-income calculation, and the excess would be $188,000.</p>
<h2>Distributions are not the same as business income</h2>
<p>A bank transfer to an owner does not independently establish the business-income amount for Form 461. Review the entity’s tax results and the nature of separately stated items. Distributions have their own basis and tax consequences; they should not be added again merely because the owner received cash.</p>
<p>Similarly, an owner contribution may change basis without creating operating profit. For S corporations, a guarantee of corporate debt does not automatically create shareholder debt basis. Review actual transactions and the governing basis rules before assuming a loss is available.</p>
<h2>Build one owner-level reconciliation</h2>
<p>Collect every K-1, basis schedule, at-risk calculation and passive-loss workpaper. Show the portion of each loss that reaches Form 461, then aggregate eligible business items across the return. Preserve both spouses’ information on joint returns and identify nonbusiness items separately.</p>
<p>The finished file should reconcile the current deduction and each deferred balance to the next year’s opening workpapers. Changing preparers or forming a new entity does not erase those distinctions. See the <a href="/blog/excess-business-loss-nol-carryforward/">carryforward guide</a> for the next stage.</p>''',
faqs=[('Does an S corporation apply its own $256,000 limit?', '<p>No. The owner applies the applicable threshold after aggregating qualifying business items.</p>'),('Is every K-1 loss an NOL?', '<p>No. Basis, at-risk and passive suspensions have separate treatment. Only the excess loss reaching Section 461(l) is treated as an NOL carryforward under that rule.</p>')]),
dict(path='/blog/excess-business-loss-nol-carryforward/',title='What Happens to an Excess Business Loss Carryforward?',category='Tax Compliance',
description='Follow a Section 461(l) excess loss into an NOL carryforward, understand the 80% limitation and keep it separate from passive and basis suspensions.',
lead='A disallowed excess business loss is treated as a net operating loss carryforward for later years. Its future use follows the NOL rules, which generally limit modern NOL deductions to 80% of specially computed taxable income.',
body='''<h2>The loss changes its reporting path</h2>
<p>Section 461(l) disallows the excess business deduction in the loss year and treats that excess as an NOL carryforward. In the carryforward year, the taxpayer applies Section 172 rather than simply deducting the entire balance against the original activity. The deduction can generally affect taxable income that includes wages or other income.</p>
<p>An excess business loss is not the same as an overall current-year NOL. The rest of the return can affect the separate NOL computation. Maintain the Form 461 adjustment and the complete NOL workpaper rather than equating a negative Schedule C or Schedule E amount with the final carryforward.</p>
<h2>Example: creating the carryforward</h2>
<p>Assume joint filers have a $900,000 allowable aggregate business loss in 2026 and no business income offset. The $512,000 threshold leaves a $388,000 excess business loss. That amount becomes an NOL carryforward. The current-return treatment of the remaining loss still depends on the complete tax calculation.</p>
<h2>Example: the 80% limitation in the next year</h2>
<p>Assume the next year’s taxable income, computed for the NOL limitation before the NOL and relevant deductions, is $300,000. Assume the only available NOL is the $388,000 carryforward, with no pre-2018 losses or special exceptions. The 80% ceiling is $240,000.</p>
<p>The example permits a $240,000 NOL deduction, leaves $60,000 after that deduction in this simplified calculation, and carries $148,000 forward again. A carryforward larger than the year’s income did not eliminate all income. At $500,000 of income measured on the same basis, the $400,000 ceiling would instead allow use of the full $388,000 balance.</p>
<h2>Do not apply the excess-loss threshold twice</h2>
<p>The NOL deduction is excluded when computing the new year’s excess business loss. A new current-year business loss may produce a separate Form 461 adjustment, while an older NOL is evaluated under the NOL rules. The two workpapers must reconcile, but an old NOL is not simply another current-year business expense.</p>
<h2>Carryforward and carryback are different</h2>
<p>Modern nonfarm NOLs generally carry forward indefinitely rather than back to earlier years. Farming losses have special carryback rules. The excess business loss itself is treated as a carryforward, so do not assume a new excess loss creates an automatic refund of tax paid two years ago.</p>
<h2>Keep separate schedules for different deferred losses</h2>
<ul><li>NOL carryforwards: track origin year, opening balance, use and closing balance.</li><li>Passive losses: track the activity and the conditions that permit use.</li><li>Basis-suspended losses: track the entity and the relevant basis changes.</li><li>At-risk suspensions: track changes in qualifying amounts at risk.</li></ul>
<p>For example, a $100,000 passive loss cannot simply be added to a $388,000 NOL balance and deducted under the 80% rule. First identify why each loss was deferred. The eventual release of one category can require a fresh review under later limitations.</p>
<h2>Preserve the workpapers when changing preparers</h2>
<p>Transfer the filed returns, Forms 461, NOL computations, utilization statements, depreciation schedules and separate suspended-loss records. A single number entered into tax software is not sufficient support for a multi-year carryforward. Reconcile any amendments through the affected later years before accepting the opening balance.</p>''',
faqs=[('Will the carryforward wipe out next year’s tax?', '<p>Not necessarily. The available balance, the 80% limitation and the complete tax calculation determine its use.</p>'),('Does the NOL have to offset the original business?', '<p>Generally no. An NOL deduction is applied to the taxpayer’s return under Section 172, subject to its limitations.</p>')]),
]

def main():
    for p in POSTS:
        published = '2026-09-17' if p['path'] == MAIN else DATE
        trail = [('Home','/'),('Blog','/blog/'),(p['title'],p['path'])]
        body = T.page_header(h1=p['title'], subtitle='Loss limitations for business owners and real estate investors.', trail=trail)
        body += T.section('The short answer', T.definition(p['lead']) + f'<p>By AE Tax Advisors Team. Published <time datetime="{published}">{published}</time>. Updated <time datetime="{DATE}">September 30, 2026</time>.</p>' + p['body'])
        body += T.faq_section(p['faqs'])
        body += T.section('Primary sources and scope','<ul>'+''.join(f'<li><a href="{u}">{label}</a></li>' for u,label in SOURCES)+'</ul><p>Sources checked September 30, 2026. The 2025 Form 461 instructions explain the framework; Revenue Procedure 2025-32 supplies the 2026 threshold. Examples are hypothetical federal income tax illustrations. They omit other deductions, credits, state taxes and special facts unless stated. <a href="/editorial-policy/">Read our editorial policy</a>.</p>')
        body += T.related_section([(q['path'],q['title']) for q in POSTS if q != p]+[('/business-owner-tax-planning/','Business owner tax planning'),('/short-term-rental-tax-strategy/','Short-term rental tax strategy'),('/cost-segregation-study/','Cost segregation services')])
        schemas=[T.article_schema(title=p['title'],description=p['description'],url=T.SITE+p['path'],published=published,modified=DATE,section=p['category'],citations=[x[0] for x in SOURCES]),T.breadcrumb_schema(trail),T.faq_schema(p['faqs'])]
        T.write_page(p['path'],T.build_page(title=p['title']+' | AE Tax Advisors',description=p['description'],path=p['path'],body=body,schemas=schemas,published=published,modified=DATE))
        print(p['path'])

if __name__ == '__main__':
    main()
