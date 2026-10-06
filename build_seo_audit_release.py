"""Maintained replacements for three existing owner guides; no new URL expansion.

Run this after legacy content generators, then rebuild discovery assets. This
module owns these pages so the checked sources, FAQs and body remain together.
"""
import re
import site_template as T

DATE = '2026-10-06'
P925 = 'https://www.irs.gov/publications/p925'
P946 = 'https://www.irs.gov/publications/p946'
COMP = 'https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues'
QBI = 'https://www.irs.gov/newsroom/qualified-business-income-deduction'
RETIRE = 'https://www.irs.gov/retirement-plans/choosing-a-retirement-plan-retirement-plan-options'
SCOPE = '''<p>The published standard advisory engagement is <strong>$7,800</strong>, paid in
two $3,900 installments, 30 days apart. It has no required recurring annual planning fee.
Tax returns, amendments, cost segregation and additional services are separately scoped
and priced. Support and audit-defense coverage depend on the period and terms in your
signed agreement; this is not unlimited future planning or free annual filing.
See <a href="/pricing/">current pricing and scope</a> before comparing proposals.</p>'''

MATERIAL_FAQS = [
('Can spouses combine hours for material participation?', '<p>Yes. A spouse\'s participation is included even without an ownership interest or a joint return. Keep each person\'s work identifiable and count a shared task once per person who actually performs it. This differs from real estate professional qualification: one spouse must independently satisfy both REPS thresholds.</p>'),
('Is exactly 100 hours enough for Test 3?', '<p>No. Test 3 requires more than 100 hours and participation at least equal to every other individual, including nonowners. Exactly 100 hours fails that test. Another applicable test may still establish material participation.</p>'),
('Do I have to keep a contemporaneous daily log?', '<p>No. Publication 925 allows any reasonable method that establishes the work and approximate hours, such as calendars or a narrative supported by records. A timely, detailed log is good practice because it makes corroboration easier; it is not the only permitted method.</p>'),
('Do a property manager\'s hours automatically disqualify me?', '<p>No. For Test 3, compare your qualifying participation with each individual\'s participation, including managers, cleaners and co-hosts. Company totals alone may not show that comparison. Other tests have different requirements; Test 7 restricts counting management work when another person is paid to manage or manages longer.</p>'),
('Does an average stay of seven days mean 39-year depreciation?', '<p>No. The passive-activity average-stay exception and the building\'s depreciation classification are separate analyses. Residential versus nonresidential classification depends on the property and its use, including the dwelling-unit and transient-use rules. A short booking pattern alone does not establish a recovery period.</p>'),
]

MATERIAL_BODY = '''
<p>For a short-term rental, a useful hour record identifies the activity, the person doing
the work, what they did and how long it took. Before claiming a nonpassive loss, establish
the activity's classification and an applicable material-participation test. A deduction
also remains subject to basis, at-risk and other limitations.</p>
<h2>Choose the participation test before choosing the log</h2>
<p>The seven tests in <a href="https://www.irs.gov/publications/p925">IRS Publication 925</a>
are alternatives, with additional restrictions for some taxpayers and activities. Three
commonly relevant tests are:</p>
<ul><li><strong>Test 1:</strong> more than 500 hours in the activity during the tax year.</li>
<li><strong>Test 2:</strong> substantially all participation by all individuals, including nonowners.
There is no separate 100-hour minimum in this test.</li>
<li><strong>Test 3:</strong> more than 100 hours, with participation at least equal to any other
individual's participation during the year. A tie can satisfy the comparison; exactly
100 hours cannot satisfy the threshold.</li></ul>
<p>Test 4 concerns significant-participation activities with combined participation above
500 hours. It is not the 100-hour/no-other-individual-more test. Tests 5 and 6 address
prior participation; Test 7 addresses regular, continuous and substantial participation
with specific limits on management work. Do not assume every test applies to every owner.</p>
<h2>What to record for each task</h2>
<p>Use a spreadsheet, calendar or other system that you can maintain. Record the property
or properly defined activity, date, participant, task, actual or reasonably supported time,
and a reference to evidence. Avoid a round-number total with no explanation of the work.</p>
<div class="table-wrap"><table><thead><tr><th>Date and activity</th><th>Person and task</th><th>Time</th><th>Supporting record</th></tr></thead>
<tbody><tr><td>Illustrative entry: June 12, Rental A</td><td>Owner: resolved a guest lock problem and coordinated replacement</td><td>35 minutes</td><td>Guest messages and vendor invoice</td></tr>
<tr><td>Illustrative entry: June 13, Rental A</td><td>Spouse: restocked and checked supplies</td><td>50 minutes</td><td>Receipt and checklist</td></tr></tbody></table></div>
<p>These entries illustrate a record format, not a client result or a conclusion that the
listed time qualifies. Document the actual work and avoid double-counting overlapping
tasks, automated messages or time another person performed.</p>
<h2>Separate operating work from investor time</h2>
<p>Guest support, maintenance, turnover work and operational vendor coordination may be
participation when the facts support it. Merely reviewing financial reports, preparing
investment analyses for your own use, or monitoring finances in a nonmanagerial capacity
does not count as participation. Work that owners do not normally perform can also be
excluded when it is done principally to avoid the passive-loss rules.</p>
<p>Do not count property research, education or an entire trip automatically. Identify
what you actually did, the activity it relates to and the applicable rules. Travel and
mixed-purpose time require their own factual analysis. The tax deductibility of an expense
does not by itself establish that the time counts for material participation.</p>
<h2>Spouses, cleaners and property managers</h2>
<p>Spousal participation counts for material participation even if you file separately or
the spouse has no ownership interest. Retain each spouse's entries so the combined total
can be supported. For REPS, one spouse independently satisfies the more-than-750-hours
and more-than-half-of-personal-services requirements; adding the spouses' hours cannot
establish those qualification thresholds.</p>
<p>For Test 3, request records that distinguish the work of individual managers, cleaners
and co-hosts. A cleaning company's total is not necessarily one person's total. A manager
does not automatically prevent material participation, but a manager's longer participation
can defeat Test 3. Keep genuine operating arrangements; changing labels or splitting
invoices does not change who performed the work.</p>
<h2>Review quarterly and before the return is filed</h2>
<ul><li>Reconcile entries against guest messages, invoices, calendars and booking records.</li>
<li>Check average customer use separately from participation and depreciation classification.</li>
<li>Compare individual outside-provider hours if relying on Test 3.</li>
<li>Confirm grouping, ownership, personal use and other loss limitations with the preparer.</li></ul>
<p>A contemporaneous log makes these checks easier. Publication 925 permits other reasonable
substantiation, so the goal is reliable evidence rather than a particular app. If the
evidence does not establish a test, assess passive treatment instead of inventing hours.</p>
<p>See the <a href="/guides/str-documentation-kit/">STR documentation kit</a>, the
<a href="/faq/str-material-participation-exactly-100-hours/">100-hour threshold answer</a>,
and the <a href="/faq/str-spouse-hours-married-filing-separately/">separate-return spouse answer</a>.
For depreciation classification, start with <a href="https://www.irs.gov/publications/p946">Publication 946</a>.</p>
'''

ATTORNEY_FAQS = [
('Should every law firm elect S-corporation status?', '<p>No. Compare eligible ownership, state professional-entity rules, reasonable wages, payroll costs, state treatment and the existing partnership arrangement. An S election may help some profitable owner-operated practices; it is not a universal result or a guaranteed savings amount.</p>'),
('Can law firm partners turn guaranteed payments into tax-free distributions?', '<p>No. Partnership allocations must reflect the agreement and applicable tax rules. Changing a label does not establish a self-employment-tax exemption. Review guaranteed payments, distributive shares, the partner\'s role and the governing rules with the return preparer.</p>'),
('Can a high-income attorney claim the QBI deduction?', '<p>Law is a specified service trade or business for QBI purposes. Eligibility and limits depend on taxable income, filing status and the rules for the return year. A law practice should not assume that all its profit produces a 20% deduction.</p>'),
('What does AE\'s advisory fee include?', '<p>The published standard advisory fee is $7,800, paid as two $3,900 installments 30 days apart, with no required recurring annual planning fee. Returns, amendments, studies and additional work are separately scoped and priced. Confirm deliverables and support coverage in the signed agreement.</p>'),
]
ATTORNEY_BODY = '''
<p>Law firm tax planning starts with how the practice earns and distributes income, not
with a promised savings range. A solo owner, an S-corporation shareholder and a partner
receiving a Schedule K-1 face different payroll, retirement and deduction questions.
AE works with profitable practice owners to coordinate those decisions before filing.</p>
<h2>Entity planning for a solo practice or growing firm</h2>
<p>Start with the current legal entity, tax election, ownership, state professional-entity
restrictions and expected profit after ordinary expenses. Compare the total cost of the
existing arrangement with alternatives, including payroll administration, reasonable
compensation and state taxes. The comparison should show assumptions and implementation
costs rather than treating every dollar of profit as avoidable employment tax.</p>
<p>An eligible S corporation must pay reasonable compensation to an owner who performs
services before making nonwage distributions. The
<a href="https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues">IRS compensation guidance</a>
explains why distributions can be reclassified as wages. See
<a href="/services/s-corp-election/">S-corporation election services</a> and
<a href="/reasonable-compensation/">owner salary documentation</a> for the next decisions.</p>
<h2>Partnership income needs its own analysis</h2>
<p>For a multi-partner firm, review the partnership agreement, ownership changes, guaranteed
payments, distributive shares and each partner's role. Guaranteed payments and allocations
have distinct rules, and active partners should not assume that changing the name of a
payment removes self-employment tax. Tax allocations must be supported by the governing
agreement and applicable economic-effect rules.</p>
<p>Bring the preparer into compensation and buy-in discussions before the documents are
signed. Changes can affect the firm's return and each partner's K-1, basis, cash-flow
planning and estimated payments. See the
<a href="https://www.irs.gov/publications/p541">IRS partnership guide</a> for the underlying framework.</p>
<h2>QBI: law is a specified service business</h2>
<p>The qualified business income deduction is not an automatic 20% deduction for every
law firm owner. Law is a specified service trade or business. Taxable income, filing
status, the applicable year's thresholds and other limits determine the result. Model
the deduction with the owner's full return instead of promising it from gross revenue.</p>
<p>The <a href="https://www.irs.gov/newsroom/qualified-business-income-deduction">IRS QBI overview</a>
and <a href="/qbi-deduction-guide/">AE's QBI guide</a> explain the questions to resolve.</p>
<h2>Retirement plans: evaluate staff and sustainable contributions</h2>
<p>A solo 401(k), profit-sharing arrangement or defined-benefit/cash-balance plan may fit
different stages of a practice. Employee eligibility, nondiscrimination testing,
actuarial funding, setup deadlines and ongoing costs matter. Large owner contributions
are not a substitute for evaluating required employee contributions and future obligations.</p>
<p>Review a multiyear funding range, not only the largest possible first-year deduction.
Retirement contributions generally defer income tax; they do not establish a permanent
tax saving of the same amount. Start with the
<a href="https://www.irs.gov/retirement-plans/choosing-a-retirement-plan-retirement-plan-options">IRS plan options</a>
and <a href="/retirement-planning-for-business-owners/">retirement planning for owners</a>.</p>
<h2>Records for a useful law firm planning review</h2>
<ul><li>Prior business and personal returns, K-1s, payroll summaries and current financials.</li>
<li>Formation documents, tax elections, partnership agreements and recent ownership changes.</li>
<li>Owner duties, hours, compensation records and employee census for retirement-plan review.</li>
<li>Estimated payments, state filing obligations and plans for a buy-in, sale or expansion.</li></ul>
<p>Use a secure engagement channel for client or firm records. The initial discovery call
can establish fit and scope without publishing confidential practice information.</p>
<h2>Pricing and the next step</h2>
''' + SCOPE + '''
<p>Ask for a written plan that distinguishes implementation actions, filing responsibilities,
deadlines and modeled outcomes. Deductions reduce taxable income; usable tax benefit
depends on rates, limitations, costs and the actual facts. A public example is not your forecast.</p>
'''

ROI_FAQS = [
('Is a depreciation deduction the same as tax savings?', '<p>No. A deduction reduces taxable income. Estimate the incremental deduction usable in the relevant year, apply the relevant tax rates, and account for limits, fees and future sale effects. A $50,000 deduction does not mean $50,000 of cash savings.</p>'),
('Is cost segregation always worth it above a property-value threshold?', '<p>No. Basis, qualifying components, deduction usability, study and filing costs, holding period and disposition consequences all affect value. Property price alone does not establish a positive return.</p>'),
('Does 100% bonus depreciation apply to every property in 2026?', '<p>No. Publication 946 describes the restored 100% allowance for certain qualified property acquired and placed in service after January 19, 2025. Acquisition dates, asset eligibility, related-party rules and elections matter. Land and an ordinary building shell do not become bonus-eligible merely because a study is performed.</p>'),
('What are AE\'s study and advisory prices?', '<p>Published standard study pricing is $1 per square foot with a $2,000 minimum. The standard $7,800 advisory engagement is separately priced, with two $3,900 payments 30 days apart and no required recurring annual planning fee. Confirm study deliverables, filing work and additional fees in the written scope.</p>'),
]
ROI_BODY = '''
<p>Cost segregation can move deductions into earlier years, but the useful comparison is
after-tax cash flow after fees and limitations. A study's deduction-to-fee ratio is not
its return on investment, and a property-value cutoff cannot establish that a study is worth it.</p>
<h2>Compare the incremental deduction with the current schedule</h2>
<p>Start with depreciable basis, excluding land, and the acquisition and placed-in-service
dates. Compare the supported asset classifications against the depreciation you would
otherwise claim. Use only the additional deduction in the scenario, rather than treating
all first-year depreciation as new savings.</p>
<p><a href="https://www.irs.gov/publications/p946">IRS Publication 946</a> describes the
restored 100% allowance for certain qualifying property acquired and placed in service
after January 19, 2025. The allowance depends on the assets and acquisition rules; a
study does not make land or an ordinary building shell eligible. Elections and state
conformity can change the comparison.</p>
<h2>Check whether the owner can use the deduction</h2>
<p>A deduction that is limited or suspended may produce a benefit in a later year rather
than current cash savings. Review entity basis, at-risk rules, passive-activity treatment,
personal use and other loss limitations with the preparer. Material participation alone
does not clear every limit. See <a href="https://www.irs.gov/publications/p925">Publication 925</a>
and <a href="/short-term-rental-tax-strategy/">the STR planning sequence</a>.</p>
<h2>A hypothetical calculation, with assumptions visible</h2>
<p>Assume a study supports an additional $50,000 federal deduction compared with the
existing schedule, the entire amount is usable in the same year, and the affected income
is taxed at a 30% federal marginal rate. The simplified first-year federal reduction is
$15,000. If the study and incremental filing work together cost $4,000, the simplified
first-year net benefit is $11,000.</p>
<p>This is an illustration, not a client result, a quote or a lifetime return calculation.
It ignores state treatment, rate interactions, financing, later deductions displaced and
sale consequences. If the entire deduction is suspended, the current-year federal
reduction in this example is zero; the potential later benefit needs a separate forecast.</p>
<h2>Model the holding period and sale</h2>
<p>Accelerating depreciation generally reduces future depreciation and adjusted basis.
A sale may bring depreciation-related gain and recapture, depending on the asset class,
sale proceeds and applicable rules. Compare planned and earlier-than-planned sale dates.
An exchange should not be assumed to defer every reclassified component.</p>
<p>For an older rental, reconcile depreciation already claimed and determine the correct
correction route. Form 3115 eligibility, timing and required filings are fact-specific;
neither an amendment nor an accounting-method change fits every situation. See
<a href="/form-3115-cost-segregation/">catch-up depreciation planning</a> and
<a href="https://www.irs.gov/instructions/i3115">the IRS Form 3115 instructions</a>.</p>
<h2>Compare total scope and fees</h2>
<p>Published standard AE study pricing is $1 per square foot, with a $2,000 minimum.
Confirm the property's measured area, complexity, report deliverables, correction work
and return preparation in the proposal. The study fee and advisory engagement are separate.</p>
''' + SCOPE + '''
<h2>When to pause before ordering a study</h2>
<ul><li>Basis or prior depreciation records are incomplete.</li>
<li>Most potential deductions would be suspended without a credible use timeline.</li>
<li>A near-term sale or personal-use change has not been modeled.</li>
<li>Incremental study and filing costs outweigh the forecast benefit.</li></ul>
<p>Use the <a href="/cost-segregation-calculator/">scenario calculator</a> to organize
assumptions, the <a href="/cost-segregation-calculator/#holding-period-form">holding-period tool</a> to
compare timing, and the <a href="/cost-segregation-documents-checklist/">document checklist</a>
to prepare a review. Calculator outputs still require property-specific confirmation.</p>
'''

PAGES = [
('/blog/how-to-track-material-participation-hours-for-str/', 'STR Material Participation Hours: Tests, Spouses & Records | AE Tax',
 'How to Track Material Participation Hours for an STR',
 'Track STR participation with individual-provider comparisons, spouse rules and supportable records. Distinguish Test 3, REPS and depreciation classification.',
 MATERIAL_BODY, MATERIAL_FAQS, [P925, P946], '2026-08-22'),
('/attorney-tax-planning/', 'Tax Planning for Law Firm Owners: Entity, QBI & Retirement | AE Tax',
 'Tax Planning for Law Firm Owners',
 'Law firm owner planning: entity elections, partnership income, QBI limits, retirement funding and the records needed to compare total costs and scope.',
 ATTORNEY_BODY, ATTORNEY_FAQS, [COMP, QBI, RETIRE, 'https://www.irs.gov/publications/p541'], '2026-05-05'),
('/is-cost-segregation-worth-it/', 'Is Cost Segregation Worth It? Usable Tax Benefit & Costs | AE Tax',
 'Is Cost Segregation Worth It? Compare Usable Tax Benefit and Costs',
 'Evaluate cost segregation using incremental usable deductions, tax rates, study and filing fees, holding period and sale effects. Includes a hypothetical example.',
 ROI_BODY, ROI_FAQS, [P946, P925, 'https://www.irs.gov/instructions/i3115'], '2026-10-03'),
]

ONLINE_BODY = '''<p>For an e-commerce store, digital product business or online service,
gross sales are not the amount available for owner wages and distributions. Reconcile
platform receipts, inventory or fulfillment costs, refunds, payment fees, advertising,
contractors and ordinary expenses before comparing an S election.</p>
<p>Document the owner's actual duties: product development, sales, operations and management
may require different compensation evidence. An online business does not have a special
percentage-of-profit salary exemption. Review eligible owners, payroll setup and
reasonable wages before distributions; a nonresident alien shareholder is not eligible.</p>
<p>Confirm the effective date and Form 2553 deadline before assuming the current year's
income can use the election. Digital sales and remote workers can also create state
filing or sales-tax obligations that an S election does not remove. Model income tax,
employment taxes, payroll costs and state obligations together rather than promising a
savings range from revenue alone.</p>
<p>Bring the prior return, year-to-date profit and loss, ownership records, existing
elections, payroll and the states where the business operates. See
<a href="/reasonable-compensation/">reasonable compensation documentation</a> and
<a href="/pricing/">published advisory and separately scoped filing fees</a>.</p>'''

FLORIDA_BODY = '''<p>Florida does not impose an individual income tax, but ownership
and residency still matter. A Florida corporation or corporate owner may have state
income/franchise tax obligations. Florida's corporate rules include federal bonus
depreciation additions and related subtractions; do not assume full federal conformity.
Check the <a href="https://floridarevenue.com/Forms_library/current/f1120n.pdf">current F-1120 instructions</a>
for the applicable property and filing year.</p>
<p>For generally six-month-or-shorter transient accommodations, Florida imposes 6% state
sales tax, plus applicable discretionary surtax and local transient-rental taxes.
Tourist development tax is a local option tax, not the name of the statewide 6% charge.
Check collection responsibilities, exemptions and the actual county rates using the
<a href="https://floridarevenue.com/Forms_library/current/brochure/gt800034.pdf">Florida accommodation-tax guide</a>.
A booking platform's involvement does not by itself settle every filing obligation.</p>
<h3>Tax advisory for Florida business and rental owners</h3>
<p>A study is one part of a broader plan. For a profitable Florida business owner, coordinate
entity classification, reasonable owner compensation, retirement funding, estimates and
the implementation of rental deductions. Florida location alone does not remove federal
loss limits or another state's resident/source-income rules.</p>
<p>A useful first review identifies the ownership entity, the owner's tax residency,
business and property locations, historical basis and depreciation, and the decisions
expected this year. See <a href="/business-owner-tax-planning/">business owner advisory</a>,
<a href="/multi-state-global-tax/">multistate planning</a> and
<a href="/pricing/">current fees and written engagement scope</a>.</p>'''

def insert_owned_section(path, marker, heading, prose):
    file = T.ROOT / path.strip('/') / 'index.html'
    text = file.read_text()
    block = '<!-- '+marker+' -->' + T.section(heading, prose) + '<!-- /'+marker+' -->'
    pattern = r'<!-- '+re.escape(marker)+r' -->.*?<!-- /'+re.escape(marker)+r' -->'
    if re.search(pattern, text, re.S):
        text = re.sub(pattern, lambda m: block, text, flags=re.S)
    else:
        text = text.replace('</main>', block+'\n</main>', 1)
    file.write_text(text)

def main():
    for path, title, h1, description, prose, faqs, sources, published in PAGES:
        trail = [('Home', '/'), ('Owner Guides', '/blog/'), (h1, path)]
        body = T.page_header(h1=h1, subtitle=description, trail=trail)
        body += T.section('Planning questions and records', prose) + T.faq_section(faqs)
        body += T.related_section([('/pricing/', 'Published fees and engagement scope'),
                                  ('/business-owner-tax-planning/', 'Business owner tax planning'),
                                  ('/short-term-rental-tax-strategy/', 'STR tax planning')])
        schemas = [T.article_schema(title=h1, description=description, url=T.SITE+path,
                    published=published, modified=DATE, citations=sources),
                   T.faq_schema(faqs), T.breadcrumb_schema(trail)]
        text = T.build_page(title=title, description=description, path=path,
                     body=body, schemas=schemas, published=published, modified=DATE)
        text = text.replace(DATE+'T00:00:00-06:00', DATE+'T00:00:00Z')
        T.write_page(path, '\n'.join(line.rstrip() for line in text.splitlines())+'\n')
        print(path)
    insert_owned_section('/services/s-corp-election/', 'online-business-election',
                         'S-corporation decisions for an online business', ONLINE_BODY)
    # Remove the contradictory legacy paragraph while preserving the state page's layout.
    file = T.ROOT / 'florida/index.html'
    text = file.read_text()
    text = re.sub(r'<p[^>]*>[^<]*Florida charges a 6% state Tourist Development Tax.*?</p>',
                  '', text, flags=re.S)
    file.write_text(text)
    insert_owned_section('/florida/', 'florida-tax-advisory',
                         'Florida income tax, lodging tax and advisory questions', FLORIDA_BODY)

if __name__ == '__main__':
    main()
