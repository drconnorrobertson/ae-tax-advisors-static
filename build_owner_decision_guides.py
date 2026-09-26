"""Distinct owner decision guides: no location swaps or templated tax claims."""
import json
import re
from pathlib import Path
import site_template as T

DATE = '2026-09-26'
POSTS = [
dict(slug='cost-segregation-related-party-property-purchase',
 title='Cost Segregation on a Related-Party Purchase',
 description='Buying a building from family or another entity you own? Separate cost segregation from bonus eligibility before projecting a first-year deduction.',
 category='Cost Segregation', hub='/cost-segregation-study/',
 lead='A related-party property purchase can still require an asset classification analysis, but a cost segregation report does not establish eligibility for bonus depreciation. Review the seller relationship and the buyer’s basis before applying an accelerated deduction to the report.',
 source='https://www.irs.gov/irb/2019-41_IRB', source_name='IRS final bonus depreciation regulations, used-property acquisition requirements',
 body='''
<h2>Why the seller matters before the engineer starts</h2>
<p>A business owner may buy a warehouse from a family member, purchase a building held by another company in the ownership group, or move property between entities. Each can look like a new acquisition in the bookkeeping system. The tax result depends on the legal transaction, ownership attribution, consideration, and basis rules. A new closing statement or LLC name is not enough to establish a qualifying purchase.</p>
<p>The used-property bonus rules include restrictions involving prior use by the taxpayer, related parties, and certain carryover-basis acquisitions. The related-party analysis refers to statutory relationships, including attribution; it is broader than asking whether two companies have identical names. A study can identify shorter-lived assets while the acquisition still fails a bonus requirement. See the IRS regulations linked below for the underlying framework.</p>
<h2>Build a transaction map</h2>
<p>Prepare a one-page diagram showing the seller, purchaser, entity tax classifications, owners, and ownership percentages immediately before and after closing. List family relationships separately. Include trusts, partnerships, and corporations rather than stopping at the person signing the deed. Ask the tax preparer to identify whether the transaction is a taxable asset purchase, contribution, distribution, interest purchase, or transfer disregarded for federal tax purposes.</p>
<p>Next, reconcile the cash paid, debt assumed, and consideration allocated to land, building, and separately purchased assets. Retain the agreement and supporting valuation. A purchase of an interest in a property-owning partnership is a different analysis from a purchase of the property itself; do not automatically apply the buyer’s interest price to a new building depreciation schedule.</p>
<h2>Illustrative planning comparison</h2>
<p>Assume an owner budgets $1.4 million for a building transaction and a preliminary study identifies $180,000 of components for shorter recovery periods. One projection treats the entire $180,000 as immediately deductible. A second projection flags the seller relationship and leaves bonus eligibility unresolved. Both projections use the same engineering estimate, but only the second identifies the missing tax decision. The owner should not reduce an estimated payment based on the first projection until the acquisition requirements and loss limitations are resolved.</p>
<p>This is a hypothetical review problem, not a promised deduction. If bonus is unavailable, the classification work may still affect regular depreciation. Model that alternative with the correct methods and conventions instead of treating the study as either a complete write-off or worthless.</p>
<h2>Questions to resolve before signing a study proposal</h2>
<ul><li>Who is the seller for federal tax purposes, including disregarded entities?</li><li>Does an ownership or family relationship trigger a restriction?</li><li>Was the property previously used by this taxpayer?</li><li>Is the new basis a purchase basis, carryover basis, or partner-specific adjustment?</li><li>Which assets and tax years are included in the engagement?</li><li>Who will confirm bonus eligibility and implement the depreciation schedule?</li></ul>
<h2>Keep two conclusions separate</h2>
<p>Ask for an asset-classification conclusion and a tax-eligibility conclusion. The former should explain the components and costs; the latter should address the acquisition and taxpayer facts. Save both with the return workpapers. If the related-party question is still open, label the cash-flow model accordingly and avoid presenting a provisional estimate as spendable tax savings.</p>
<p>For the general study workflow, use <a href="/cost-segregation-study/">cost segregation services</a>. For an existing report, use the <a href="/blog/cost-segregation-report-basis-reconciliation/">report reconciliation checklist</a>. These address different decisions from the seller-relationship review.</p>'''),
dict(slug='elect-out-bonus-depreciation-asset-class',
 title='Electing Out of Bonus Depreciation by Asset Class',
 description='Business and property owners should model bonus depreciation elections by asset class, including other purchases, future income and state differences.',
 category='Business Owner Tax', hub='/business-owner-tax-planning/',
 lead='Electing out of bonus depreciation is generally a decision for a class of property placed in service during a tax year, not a choice made separately for each asset. Business owners and real estate owners should review the full asset list before deciding that a smaller current deduction is better.',
 source='https://www.irs.gov/instructions/i4562', source_name='IRS Form 4562 instructions: electing out of the special depreciation allowance',
 body='''
<h2>Start with a list of assets, not a target deduction</h2>
<p>A projection may suggest that a business owner needs only part of a large depreciation deduction this year. That does not mean the owner can simply choose a desired percentage of otherwise applicable bonus depreciation. The Form 4562 instructions explain the election out by class of property and the statement accompanying a timely filed return, including extensions. Revoking the election generally requires IRS consent. Confirm the rules applicable to the filing year before making the election.</p>
<p>Create a list by taxpayer, placed-in-service year, asset description, recovery period, and basis. Include equipment purchases outside the cost segregation project. A five-year asset in a property study and five-year equipment elsewhere in the same taxpayer’s business can belong in the same election review. Keep separate taxpayers separate; an owner’s personal preference does not replace an entity-level filing decision.</p>
<h2>Compare at least three planning outputs</h2>
<p>Ask for a current-year federal projection, a multi-year depreciation schedule, and a state reconciliation. Keep the federal tax benefit separate from any state benefit. Show deductions that are currently usable and those carried forward under an applicable limitation. Include planned purchases and an expected sale year in the assumptions rather than assuming that next year’s income will match this year’s.</p>
<p>A larger deduction may free cash now. A smaller deduction may retain deductions for later years. Neither outcome is automatically better. The useful comparison is the timing and usability of the deductions against the owner’s expected income and cash needs, with the assumptions visible. A projection that reports only the largest first-year number cannot answer that question.</p>
<h2>A class-level example</h2>
<p>Consider a company with $70,000 of five-year components identified in a building study and $30,000 of other five-year equipment placed in service in the same year. The company should evaluate the relevant class as a whole rather than asking to turn off bonus only for the building components. If its advisor models an election out, the workpapers should identify both purchases and the regular depreciation treatment that would follow.</p>
<p>The $100,000 total is hypothetical basis for the example. It is not a prediction of a deductible amount or a statement that every item qualifies for bonus. Classification, acquisition requirements, elections, and limitations still need to be resolved. Separately list any assets for which eligibility is uncertain.</p>
<h2>Record the decision before filing</h2>
<ul><li>Export the fixed-asset list and identify each affected class.</li><li>Retain a version of the projection with bonus and a version reflecting the proposed election.</li><li>List assumptions about future profits, property sales, and state treatment.</li><li>Record who approved the filing choice and who prepares the election statement.</li><li>Check that the return and depreciation software reflect the same choice.</li></ul>
<h2>Coordinate with partners and future preparers</h2>
<p>If a partnership or S corporation owns the assets, circulate a clear explanation of the entity’s decision to the owners who need it for their projections. Keep the election statement with permanent tax records so a future preparer does not treat the absence of bonus as an error. When the decision changes after filing, request a procedural review before amending; the original election is a tax position with its own correction rules.</p>
<p>Use the <a href="/cost-segregation-calculator/">cost segregation calculator</a> for an explicitly limited scenario and <a href="/business-owner-tax-planning/">business owner tax planning</a> for a projection covering the rest of the return.</p>'''),
dict(slug='cost-segregation-report-basis-reconciliation',
 title='Cost Segregation Report: Basis Reconciliation Checklist',
 description='Check a completed cost segregation report against land, building basis, prior depreciation and separately purchased assets before implementing it.',
 category='Cost Segregation', hub='/cost-segregation-study/',
 lead='Before a cost segregation report reaches the tax return, its asset totals should reconcile to the property’s supported depreciable basis. A report-to-return reconciliation helps detect duplicated furniture, omitted improvements, incorrect land treatment and an unsupported catch-up adjustment.',
 source='https://www.irs.gov/pub/irs-pdf/p5653.pdf', source_name='IRS Publication 5653: Cost Segregation Audit Technique Guide',
 body='''
<h2>Three files should tell one numerical story</h2>
<p>Place the closing and improvement records, the cost segregation report, and the tax depreciation schedule side by side. Identify the taxpayer, property address, scope, and tax year on each. A report for the acquisition alone may exclude later renovations; a revised report may include them. Resolve that scope before comparing totals. Otherwise a difference can be mistaken for an error or, worse, a duplicate cost can appear reasonable.</p>
<p>The IRS audit technique guide describes elements of a quality study, including methodology, supporting documentation, and reconciliation of costs. It is examiner guidance, not a binding legal determination or IRS approval of a provider. Use it as a review reference while the preparer evaluates the actual tax treatment.</p>
<h2>Work through this hypothetical reconciliation</h2>
<p>Suppose the supported acquisition cost is $1,100,000, of which $220,000 is land. There are $80,000 of additional capitalized improvements included in the study scope. The expected total basis covered by the depreciation analysis is $960,000. If the report lists $160,000 of shorter-lived assets and $800,000 of remaining building basis, it ties mathematically. That tie alone does not validate the classifications or establish the amount currently deductible.</p>
<p>Now suppose the owner separately purchased $25,000 of furniture and the preparer already put it on another asset schedule. If the report’s $960,000 includes that same furniture without an appropriate adjustment, the return could duplicate basis. Ask which invoices are included in each subtotal and assign each invoice to one schedule. Do not fix a discrepancy by changing the land allocation merely to make totals agree.</p>
<h2>Review the asset-level handoff</h2>
<ul><li>Reconcile acquisition costs, capitalized costs, and excluded land.</li><li>Match property identifiers and entity ownership to the return.</li><li>List the report’s asset classes, methods, conventions, and service dates.</li><li>Flag furniture and equipment already depreciated separately.</li><li>Separate additions from replaced or disposed components.</li><li>Identify federal and state schedules that need different treatment.</li><li>Retain a bridge from the old schedule to the proposed new schedule.</li></ul>
<p><a href="/assets/cost-segregation-reconciliation-checklist.csv" download>Download the report reconciliation checklist</a>. It is a blank review aid, not a depreciation calculation or tax election. Assign an owner and an evidence reference to every unresolved line.</p>
<h2>Lookback reports need another bridge</h2>
<p>For property reported in earlier years, request a schedule explaining prior deductions and the proposed correction. Ask the preparer to identify the procedural route and reconcile the proposed adjustment to the historical returns. Do not subtract an informal estimate of past depreciation from a headline report total. The <a href="/form-3115-cost-segregation/">Form 3115 guide</a> explains the separate accounting-method question.</p>
<h2>Close the review with a written exception list</h2>
<p>For each difference, write the amount, explanation, supporting file, responsible person, and resolution. A report can be complete while implementation questions remain open. Keep unresolved items visible instead of treating delivery of a PDF as completion of the return work. The final file should show what was accepted, what changed, and which version was implemented.</p>
<p>This checklist reviews a delivered report. The <a href="/cost-segregation-documents-checklist/">pre-study document checklist</a> covers what to collect before the work begins. Keeping those two stages distinct reduces back-and-forth between the property owner, analyst, and return preparer.</p>'''),
dict(slug='business-equipment-delivered-not-operational-year-end',
 title='Equipment Delivered in December but Not Operational',
 description='A deposit or December delivery does not settle depreciation timing. Business owners should document installation, readiness and actual equipment use.',
 category='Business Owner Tax', hub='/business-owner-tax-planning/',
 lead='Equipment generally starts depreciating when it is ready and available for its intended business use. A December payment or delivery does not by itself establish that the equipment was placed in service before year-end.',
 source='https://www.irs.gov/publications/p946', source_name='IRS Publication 946: when property is placed in service',
 body='''
<h2>Separate five dates in the purchase file</h2>
<p>Record the order date, payment date, delivery date, installation completion date, and date the asset became ready for its specific business use. These dates can differ by weeks. A medical practice may receive a machine before room work is complete. A manufacturer may take delivery while waiting for electrical service. A contractor may own a truck that still needs the equipment required for its assigned work.</p>
<p>IRS Publication 946 distinguishes delivery from readiness and availability. It also explains that actual first use can occur after an asset is ready and available. Do not automatically substitute the first customer invoice for the service date, and do not assume that a boxed machine in a warehouse is operational merely because the purchase was financed.</p>
<h2>Illustrative equipment timeline</h2>
<p>A fabrication business orders a machine on November 15, pays a deposit on December 1, and receives it on December 21. Installation finishes January 6, followed by completion of the work needed to make it operational on January 8. These facts point to reviewing January as the service period rather than treating the December delivery receipt as conclusive. The analysis should describe what remained unfinished at year-end.</p>
<p>Change the facts: installation and commissioning are complete on December 27, the machine is available for production, and the owner waits until January 3 to run the next customer order. The first job date alone would not establish January as the service date. The distinction is readiness for the specific use, supported by records. These are hypothetical timelines, not a conclusion about any particular purchase.</p>
<h2>Build an evidence packet while events are happening</h2>
<ul><li>Purchase order and contract, including required installation work.</li><li>Delivery receipt identifying the actual equipment.</li><li>Installer completion report and commissioning records.</li><li>Dated photographs and operational test records.</li><li>Required permits or approvals relevant to intended use.</li><li>A short description of any unfinished work on December 31.</li><li>The asset ledger entry and the service date used by the preparer.</li></ul>
<p><a href="/assets/equipment-placed-in-service-checklist.csv" download>Download the equipment readiness checklist</a>. Use one line per asset, with references to the underlying evidence. A checklist does not replace the facts; it makes missing evidence easier to identify.</p>
<h2>Update the cash forecast before reducing payments</h2>
<p>If installation slips into the next year, send the new schedule to the advisor preparing the tax projection. Keep a version of the forecast without the anticipated deduction so the owner can plan the cash required if the asset is delayed. Ask the vendor for a realistic completion schedule, not a tax conclusion.</p>
<p>Depreciation timing is only one step. Eligibility for bonus depreciation or Section 179 and the amount usable on the owner’s return require separate review. Use <a href="/blog/elect-out-bonus-depreciation-asset-class/">the bonus election guide</a> to understand how other equipment in the same class can affect that decision.</p>
<h2>Give the preparer a factual memo</h2>
<p>Write a brief memo stating what the equipment does, where it is located, what was complete at year-end, what remained, and which records support those statements. Keep it with the depreciation schedule. This is more useful than a vendor email promising a write-off or a bookkeeping entry dated December 31. Review readiness early enough that a changed installation date does not become a surprise when the return is prepared.</p>'''),
dict(slug='rental-partnership-refinance-distribution-basis',
 title='Rental Partnership Refinance: Distribution and Basis',
 description='Before a rental partnership distributes refinance proceeds, reconcile each partner’s outside basis, liability share and cash distribution.',
 category='Real Estate Tax', hub='/real-estate-tax-planning/',
 lead='Refinancing proceeds received by a rental partnership and cash distributed to a partner are separate tax events to analyze. A partner should review outside basis and liability changes before assuming that a cash-out distribution is entirely tax-free.',
 source='https://www.irs.gov/publications/p541', source_name='IRS Publication 541: partnership distributions and partner liabilities',
 body='''
<h2>The property’s equity is not the partner’s tax basis</h2>
<p>A lender may value a property well above its original cost. That valuation explains lending capacity; it does not directly establish a partner’s outside basis. Likewise, the capital account shown on a K-1 does not by itself complete the outside-basis calculation. Start with a partner-level schedule, then reconcile contributions, allocated income and loss, distributions, and the relevant liability adjustments.</p>
<p>IRS Publication 541 explains that money distributed beyond a partner’s adjusted basis can produce gain. It also describes how increases and decreases in a partner’s share of partnership liabilities affect the calculation. A decrease can be treated as a money distribution. The liability allocation therefore belongs in the same review as the wire sent to the partner, with the applicable ordering and transaction rules considered.</p>
<h2>Prepare a before-and-after closing schedule</h2>
<p>For each partner, list the beginning basis supported by prior workpapers, current-year activity, old debt share, new debt share, actual cash distributed, and other cash-equivalent changes. Identify lender fees and reserves separately from distributable proceeds. A closing statement reports the partnership’s transaction; it normally does not tell each partner the personal tax result.</p>
<p>Document changes in guarantees and economic responsibility for the debt. Do not divide every loan equally just because ownership percentages are equal. Ask the preparer to explain the allocation used. Keep that explanation with the debt documents so next year’s preparer can trace the opening liability share.</p>
<h2>A simplified illustration</h2>
<p>Assume a partner has $60,000 of adjusted outside basis immediately before a $90,000 cash distribution, after all relevant adjustments have already been made. In this deliberately simplified scenario, the $30,000 excess requires gain analysis. The amount borrowed by the partnership does not eliminate that comparison.</p>
<p>If a different, properly supported liability adjustment changes the partner’s basis before the distribution, the result can change. That is why a projection should not start with the phrase “loan proceeds are not income” and stop there. This illustration omits special distribution, disguised-sale, and other transaction rules; it demonstrates the reconciliation needed before a conclusion can be reached.</p>
<h2>What owners should request before authorizing the wire</h2>
<ul><li>An outside-basis schedule for each receiving partner.</li><li>A reconciliation of old and new partnership debt.</li><li>A proposed distribution schedule identifying every recipient.</li><li>An explanation of any changed guarantee or liability allocation.</li><li>A projection of owner-level tax and cash needs if gain arises.</li><li>A clear list of assumptions still awaiting documents.</li></ul>
<h2>Resolve missing history instead of guessing</h2>
<p>If the partnership changed preparers or acquired properties over several years, obtain prior K-1s, contribution records, distribution ledgers, and debt schedules. Identify which historical numbers are supported and which are reconstructed. A current appraisal cannot replace missing tax-basis history. Before paying out nearly all available cash, reserve time to resolve material uncertainties.</p>
<p>This guide focuses on a partnership’s distribution to its owners. For the broader property transaction, see <a href="/blog/cash-out-refinance-tax-treatment-rental-property/">cash-out refinance tax treatment</a>. For coordinated ownership and property planning, see <a href="/real-estate-tax-planning/">real estate tax planning</a>.</p>'''),
dict(slug='business-equipment-trade-in-depreciation-recapture',
 title='Equipment Trade-In: Basis and Depreciation Recapture',
 description='Trading in business equipment can create a taxable disposition. Separate the old asset’s gain from the new asset’s cost before forecasting deductions.',
 category='Business Owner Tax', hub='/business-owner-tax-planning/',
 lead='A business equipment trade-in needs two calculations: the disposition of the old asset and the basis of the replacement. The cash paid to the dealer alone does not show either the taxable gain or the new depreciation deduction.',
 source='https://www.irs.gov/publications/p544', source_name='IRS Publication 544: exchanges and depreciation recapture',
 body='''
<h2>A net invoice can hide two transactions</h2>
<p>A dealer may quote one net amount after allowing a credit for the old machine. For tax planning, request a document showing the replacement’s price, the trade-in allowance, additional cash, financing, and fees separately. Retain the old asset’s original cost and depreciation history. A zero book value in the bookkeeping system should be reconciled to the tax schedule before it is used in a gain calculation.</p>
<p>Section 1031 like-kind exchange treatment is generally limited to qualifying real property; business equipment does not qualify simply because the replacement performs the same function. Prior depreciation can cause some or all of a gain to be treated as ordinary income under the applicable recapture rules. Publication 544 explains these disposition rules. The new asset is then evaluated under its own basis and depreciation requirements.</p>
<h2>A hypothetical trade-in worksheet</h2>
<p>Suppose a machine originally cost $100,000, its adjusted tax basis is $10,000, and the dealer allows $35,000 for it against a $120,000 replacement. Ignoring fees and other adjustments, the old asset has a $25,000 gain to analyze. If the applicable Section 1245 conditions are met and prior depreciation is sufficient, that gain can be ordinary recapture income. The $85,000 net cash difference does not mean that the business has only an $85,000 replacement asset.</p>
<p>The new machine’s basis and deduction should be computed separately. Whether a current deduction offsets the disposition income depends on timing, eligibility, and the taxpayer’s other facts. Do not promise that the trade-in gain disappears because a new machine was ordered.</p>
<h2>Check whether the two sides fall in different tax years</h2>
<p>If the dealer takes the old asset in December but the replacement is not ready for business use until January, the owner needs a projection that considers the timing mismatch. Preserve the disposal date and the replacement’s readiness records. The <a href="/blog/business-equipment-delivered-not-operational-year-end/">equipment placed-in-service guide</a> explains the evidence to collect for that second date.</p>
<p>For a financed replacement, separately track the loan balance and the asset. Principal payments are not a substitute for an asset-level depreciation schedule. Have the bookkeeper and preparer agree on how the invoice is entered so the old machine does not remain on the ledger after disposal.</p>
<h2>Use a two-column handoff</h2>
<ul><li>Old asset: description, serial number, cost, depreciation, adjusted basis, disposal date, and trade-in proceeds.</li><li>New asset: description, full acquisition cost, separately identified fees, financing, delivery, and placed-in-service evidence.</li><li>Reconciliation: dealer contract, cash settlement, debt entries, and asset ledger changes.</li><li>Tax projection: disposition gain, character, replacement deduction, and any timing difference.</li></ul>
<h2>Review the trade before negotiating around a deduction</h2>
<p>Compare keeping, selling, and trading the equipment using operating needs and after-tax cash flow. Include downtime, financing costs, maintenance, and expected resale value. A larger deduction does not make an unnecessary purchase profitable. Ask the advisor to identify the assumptions that would materially change the tax comparison before committing to the trade.</p>
<p>For the broader depreciation decision, see <a href="/equipment-leasing-section-179/">business equipment tax planning</a> and <a href="/blog/elect-out-bonus-depreciation-asset-class/">bonus depreciation elections by class</a>.</p>''')
]

def main():
    for post in POSTS:
        path = '/blog/' + post['slug'] + '/'
        sources = [post['source']]
        body = T.page_header(h1=post['title'], subtitle='Practical decisions for business owners and real estate owners.', trail=[('Home','/'),('Blog','/blog/'),(post['title'],path)])
        body += T.section('The decision', T.definition(T.esc(post['lead'])) + f'<p>Published <time datetime="{DATE}">September 26, 2026</time> · AE Tax Advisors Team</p>' + post['body'])
        body += T.section('Source and scope', f'<p><a href="{post["source"]}">{post["source_name"]}</a>. Source checked September 26, 2026. Examples are hypothetical. This guide is general education, not a conclusion about your return. <a href="/editorial-policy/">Read our editorial policy</a>.</p>')
        body += T.related_section([(post['hub'],'Explore related tax planning'),('/blog/','More owner tax guides')])
        schema = T.article_schema(title=post['title'],description=post['description'],url=T.SITE+path,published=DATE,modified=DATE,section=post['category'],citations=sources)
        output = T.build_page(title=post['title']+' | AE Tax', description=post['description'],path=path,body=body,schemas=[schema,T.breadcrumb_schema([('Home','/'),('Blog','/blog/'),(post['title'],path)])],published=DATE,modified=DATE)
        target = T.ROOT / path.strip('/') / 'index.html'
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(output)
        print(path)
    for hub in sorted({p['hub'] for p in POSTS}):
        path = T.ROOT / hub.strip('/') / 'index.html'
        text = path.read_text()
        block = '<!-- owner-decisions:start -->' + T.related_section([('/blog/'+p['slug']+'/',p['title']) for p in POSTS if p['hub']==hub], 'Owner decisions and working checklists') + '<!-- owner-decisions:end -->'
        text = re.sub(r'<!-- owner-decisions:start -->.*?<!-- owner-decisions:end -->','',text,flags=re.S)
        path.write_text(text.replace('</main>',block+'\n</main>'))
    assets = T.ROOT/'assets'
    (assets/'cost-segregation-reconciliation-checklist.csv').write_text('Review item,Evidence reference,Amount if applicable,Responsible person,Status,Resolution\n'+'\n'.join(x+',,,,,' for x in ['Property and taxpayer identity','Acquisition cost','Land excluded','Included improvements','Separately depreciated equipment','Report total versus basis','Prior depreciation bridge','Disposed components','Federal and state schedules','Return implementation approval'])+'\n')
    (assets/'equipment-placed-in-service-checklist.csv').write_text('Asset,Intended business use,Order date,Delivery date,Installation complete,Ready and available date,Evidence reference,Unfinished work at year-end,Reviewer\n')

if __name__ == '__main__':
    main()
