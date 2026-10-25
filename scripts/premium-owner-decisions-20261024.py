"""Render eight distinct owner decision guides and their discovery links."""
import html,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATE='2026-10-24'
SITE='https://www.aetaxadvisors.com'
def a(path,label):return f'<a href="{path}">{label}</a>'
def ul(items):return '<ul>'+''.join('<li>'+x+'</li>' for x in items)+'</ul>'
def table(head,rows):return '<div class="ae-table-scroll" role="region" aria-label="Decision comparison" tabindex="0"><table class="blog-table"><thead><tr>'+''.join('<th scope="col">'+x+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>'
SOURCES={
'sale':('https://www.irs.gov/businesses/small-businesses-self-employed/sale-of-a-business','IRS: sale of a business'),
'assets':('https://www.irs.gov/instructions/i8594','IRS: Form 8594 allocation instructions'),
'disposition':('https://www.irs.gov/publications/p544','IRS Publication 544: sales and dispositions'),
'installment':('https://www.irs.gov/publications/p537','IRS Publication 537: installment sales'),
'passive':('https://www.irs.gov/publications/p925','IRS Publication 925: passive activity and at-risk rules'),
'partnership':('https://www.irs.gov/publications/p541','IRS Publication 541: partnerships'),
'depreciation':('https://www.irs.gov/publications/p946','IRS Publication 946: depreciation'),
'groups':('https://www.irs.gov/irm/part7/irm_07-011-007','IRS Internal Revenue Manual: related employers and multiple employer plans'),
'db':('https://www.irs.gov/newsroom/choosing-a-defined-benefit-plan','IRS: choosing a defined benefit plan'),
'scorp':('https://www.irs.gov/businesses/small-businesses-self-employed/s-corporations','IRS: S corporation requirements'),
'professional':('https://www.irs.gov/newsroom/selecting-a-tax-professional-as-a-small-business-taxpayer','IRS: selecting a tax professional'),
'quality':('https://www.irs.gov/pub/irs-pdf/p5653.pdf','IRS cost segregation audit technique guide (examination guidance, not law)')}
PAGES=[]
def page(path,title,meta,desc,keyword,intro,sections,faqs,service,case,sources,new=True):
 PAGES.append(dict(path=path,title=title,meta=meta,description=desc,primary_keyword=keyword,intro=intro,sections=sections,faqs=faqs,service=service,case=case,sources=sources,new=new))
page('/blog/selling-business-keeping-building-tax-planning/',
'Selling Your Business but Keeping the Building: Tax Planning',
'Selling a Business, Keeping the Building | AE Tax',
'Selling your business while retaining its building? Compare ownership, lease cash flow, sale proceeds and tax responsibilities before agreeing to terms.',
'selling business keeping building tax planning',
['Selling your business while keeping the building creates two connected decisions: how to sell the operating business and how to operate the property after closing. A purchase offer that looks attractive can produce a different outcome once you include debt, taxes, tenant obligations and future repairs.',
'This guide is for established owners whose company occupies a building they own, directly or through another entity. Start the review while sale and lease terms are still negotiable. Ask for a combined after-tax cash forecast, supported by separate records for the business sale and retained property.'],[
('Confirm whether the building is already separate',[
'Begin with the deed, entity returns and ownership chart. A building in a separate property entity is a different starting point from a building owned inside the company being sold. Retaining a corporate asset may require a transaction of its own; moving appreciated property out before closing can itself create tax. A new LLC does not automatically make that transfer tax-free.',
'List the legal seller of the business, the owner of the building, any minority owners, lender guarantees and proposed tenant. Have deal counsel and the tax advisor compare the proposed structure before anyone promises that the property can simply be excluded.']),
('Model the business sale and the lease together',[
'For a covered asset sale, the purchase-price allocation affects reporting. A stock or ownership-interest transaction needs its own analysis. Keep equipment, improvements and retained building assets clearly identified so that the sale schedule and future depreciation records do not assign the same item to both parties.',
table(['Decision','What to compare'],[['Lease rent and increases','After-tax rent, vacancy exposure, tenant credit and market support'],['Repairs and improvements','Which party pays, approval rights and expected capital reserves'],['Debt and guarantees','Payoff requirements, refinancing and lender consent'],['Sale consideration','Cash at closing, withheld amounts, seller financing and advisory costs']]),
'Use the proposed lease in the cash forecast. Gross rent is not spendable income: debt payments, property expenses, reserves and taxes all matter. Request a downside case if the buyer closes a location or asks to assign the lease.']),
('Revisit the property tax analysis after closing',[
'The property may move from serving your operating company to being leased to an unrelated buyer. Review prior passive-activity groupings, suspended losses and the post-sale activity rather than assuming last year’s treatment continues. The sale does not automatically release every property-related loss.',
'Keep the historical depreciation schedule and supporting asset detail. A later property sale will require its own basis and disposition analysis. Separating the property today also means keeping reliable rental books after the operating business has changed hands.']),
('Illustrative decision: practice sale with retained premises',[
'A hypothetical practice owner receives an offer for the operating business and a proposed long-term lease for the office. The owner initially compares only the purchase price. A useful review also models mortgage service, future roof costs, the buyer’s lease guarantees and the tax reserve on sale proceeds.',
'The work product is a set of comparable scenarios and open issues for counsel, not a promise that keeping the property is always better. The owner may reasonably choose a lower headline offer if the overall cash flow, risk and contractual terms fit better. This example is illustrative and is not a client result.']),
('Prepare a transaction handoff',[
ul(['Draft offer and purchase agreement, plus the proposed lease.','Ownership chart, deed, debt documents and guarantees.','Business and property returns, current financials and depreciation schedules.','A list of retained assets, transaction costs and expected closing dates.','Named responsibility for allocation review, estimated taxes, lease review and final returns.']),
'Agree on a review date before signing revisions that affect the structure. If the sale is already under contract, provide the full agreement so the team can distinguish available choices from terms that are fixed.'])],
[('Does keeping the building avoid tax on the business sale?','No. The operating business sale needs its own tax analysis. Retained property, lease income and any transfer needed to separate the building have separate consequences.'),('Can I take the building out of my corporation before selling?','A distribution or transfer of appreciated property may create tax. Review ownership, basis, debt and the transaction documents before moving it.')],
('/retirement-exit-ma-tax-strategy/','Business exit advisory'),('/case-studies/business-sale-earnout-tax-cash-reserve/','a business-sale cash-reserve planning example'),['sale','assets','disposition','passive'])
page('/blog/tax-planning-before-signing-letter-of-intent/',
'Tax Planning Before Signing a Business Sale Letter of Intent',
'Business Sale Tax Planning Before an LOI | AE Tax',
'Before signing a business sale LOI, compare deal structure, allocation, cash proceeds and review responsibilities with your tax advisor and deal counsel.',
'tax planning before signing letter of intent',
['Tax planning before signing a letter of intent starts with turning the proposed deal into an after-tax comparison. An LOI may settle important commercial expectations before the detailed purchase agreement exists. The legal effect of its provisions belongs with deal counsel; tax review should happen alongside that discussion.',
'The goal is a short decision memo: the alternatives still available, the assumptions behind each model, and the terms that require further diligence. There is no universal rule that all planning remains possible until signing or that every option disappears once an LOI is signed.'],[
('Separate deal value from cash you can use',[
'List the headline price, debt payoff, working-capital adjustment, fees, escrow, retained equity and contingent payments. Then estimate taxes using the actual seller, basis and proposed structure. Avoid applying one capital-gains percentage to the entire purchase price.',
'Ask which amounts arrive at closing and which depend on future events. A seller note or earnout is not equivalent to cash, and installment treatment does not defer every type of income. Keep the financing and tax assumptions separate so one does not conceal the other.']),
('Identify the structure before negotiating allocations',[
'An asset sale, a stock sale and a partnership-interest sale can produce different results for seller and buyer. If a deemed asset transaction or another election is proposed, identify who must consent and who calculates the consequences.',
'For a covered asset acquisition, the allocation connects the negotiated price with the assets reported by each party. Have the tax team review proposed equipment, inventory and intangible allocations before they become an unexplained exhibit in the final agreement.']),
('Use the LOI as a review agenda',[
table(['LOI item','Question to resolve'],[['Assets or ownership interests','Exactly what is being sold and by which entity?'],['Retained building','What lease or property transaction will be required?'],['Earnout or continued employment','Which payments depend on services or performance?'],['Rollover equity','What is retained, at what value, and with which tax assumptions?'],['Timing and diligence','Who supplies the model and when can terms still change?']]),
'An LOI is not a substitute for the final documents. Ask counsel to identify binding provisions and keep an explicit list of commercial terms that remain open. Reconcile the model whenever proposed terms change.']),
('Do not rely on a last-minute planning checklist',[
'Ownership changes, charitable planning and other pre-sale steps can depend on facts and timing beyond the date printed on a document. If any are being considered, bring them to the appropriate tax and legal specialists early. Avoid assuming that an unsigned purchase agreement alone establishes the outcome.',
'A practical team also considers what happens if the transaction fails. Evaluate costs, administration, control and business purpose before implementing a change solely for the projected sale.']),
('Illustrative comparison and required records',[
'A hypothetical owner compares an all-cash asset offer with an ownership-interest offer containing rollover equity and an earnout. The useful result is not a single “best tax rate.” It is a side-by-side model of timing, estimated taxes, uncertainty and accessible proceeds. This is a planning illustration, not a completed transaction.',
ul(['Current LOI and prior revisions, ownership history and entity elections.','Recent returns, basis records, depreciation schedules and debt balances.','Proposed allocation, employment or consulting terms and rollover documents.','A written list of model assumptions, responsible reviewers and decision dates.']),
'Use '+a('/workbooks/business-sale/business-sale-letter-of-intent-review/','the LOI review workbook')+' to organize questions. Detailed agreements and financial records should move through the agreed secure channel.'])],
[('Is it too late to seek tax advice after signing an LOI?','Not necessarily. Provide the signed LOI and transaction status. Counsel and your tax advisor can identify the terms still open and the decisions requiring immediate review.'),('Does an earnout postpone all taxes until payment?','No. Treatment depends on the arrangement and the income involved. Some amounts may be compensation or otherwise require different timing; depreciation recapture can also limit deferral.')],
('/retirement-exit-ma-tax-strategy/','Pre-sale and exit advisory'),('/case-studies/business-sale-earnout-tax-cash-reserve/','a sale and earnout cash-reserve planning example'),['sale','assets','installment'])
page('/blog/cash-balance-plan-multiple-businesses-controlled-group/',
'Can One of My Businesses Have a Cash Balance Plan?',
'Cash Balance Plans Across Multiple Businesses | AE Tax',
'Own several businesses? Review related employers, employee coverage and funding before adding a cash balance plan to one company.',
'cash balance plan multiple businesses',
['A cash balance plan for one of several owned businesses requires a review of the businesses together before the plan is designed. Separate payroll accounts, tax returns or LLCs do not by themselves establish that employees can be tested separately.',
'This issue matters when an owner has a profitable professional practice, a separate service company, a spouse’s business or a recent acquisition. The question is which employers and employees must be considered, then whether the proposed retirement design fits the group’s funding and operating needs.'],[
('Build an ownership and service map first',[
'Controlled-group, common-control and affiliated-service-group rules can cause related employers to be treated as one employer for relevant retirement-plan requirements. The analysis can involve ownership attribution and service relationships. Affiliated-service-group issues can arise even where the obvious ownership percentages do not tell the whole story.',
'Provide direct and indirect ownership, relevant family relationships, management arrangements and services performed between entities. Ask the retirement specialist to document which rules apply. Do not use a generic ownership threshold or a spouse’s separate incorporation as the entire analysis.']),
('Employee coverage is different from choosing a plan sponsor',[
'Identifying the company that signs the plan documents does not settle which employees enter the coverage and nondiscrimination analysis. Related businesses may need to be included in testing, even if one entity is intended to fund the plan. That does not mean every employee must receive the same contribution or that every business must adopt identical documents.',
'Have the third-party administrator and actuary evaluate the actual design, employee census, existing plans and applicable requirements. A tax projection made before this work can overstate the owner’s benefit or omit employee costs.']),
('Compare the full funding commitment',[
'A cash balance arrangement is a defined benefit plan. The actuary’s annual work and funding requirements matter alongside the tax deduction. Model owner and employee funding, administration, cash reserves and expected business variability.',
table(['Forecast input','Why the owner needs it'],[['Employee census across related businesses','Supports coverage, testing and cost estimates'],['Existing retirement arrangements','Identifies coordination and operational questions'],['Business profit and compensation forecast','Tests available cash and planning assumptions'],['Acquisition or staffing changes','Can change the employee population and plan economics']]),
'Compare the proposed design with retaining or adjusting existing plans. A larger deduction is not necessarily the best use of cash during expansion or a partner buyout.']),
('Illustrative situation: practice plus management business',[
'A hypothetical dentist owns a practice with staff and a separate management company. The owner asks whether a cash balance plan in the management company can cover only the owner. Before calculating a contribution, the team reviews ownership, services between entities, employee eligibility and the existing practice plan.',
'The outcome could be a workable combined design, a different design or a decision to defer adoption. The entity name alone provides no answer. This example illustrates the review process and does not establish eligibility or a contribution amount.']),
('Agree on specialist roles before adoption',[
ul(['Owner and bookkeeper: complete ownership records and employee census.','Tax advisor: connect funding scenarios with business and household projections.','Administrator and actuary: evaluate plan design, testing, funding and administration.','Benefits counsel where needed: resolve legal questions about related employers or documentation.']),
'Get the analysis before signing plan documents or moving employees between entities. Revisit it when ownership, staffing, service arrangements or acquisitions change. For the broader decision, use '+a('/cash-balance-plan-tax-deduction/','the cash balance plan guide')+'.'])],
[('Do separate EINs mean my businesses can ignore each other?','No. Related-employer rules depend on the facts and applicable requirements, not only the number of EINs.'),('Must every employee receive the same cash balance contribution?','Not necessarily. Coverage, nondiscrimination and other requirements must be evaluated using the actual employee population and proposed design.')],
('/business-owner-small-business-tax/','Multi-entity business advisory'),('/case-studies/retirement-plan-owner-with-employees-cash-flow/','a retirement-funding planning example'),['groups','db'])
page('/blog/buying-out-dental-medical-practice-partner-tax-review/',
'Buying Out a Practice Partner: Tax Review Before Agreement',
'Practice Partner Buyout Tax Review | AE Tax Advisors',
'Buying out a dental or medical practice partner? Compare who pays, transaction form, basis, debt and post-buyout cash before signing.',
'practice partner buyout tax planning',
['A practice partner buyout needs a tax review of who is buying, what is being acquired and how the payment will be funded. A partner selling an interest directly to another owner is different from the practice redeeming that interest. A business taxed as a partnership also differs from a corporation, even when both owners call themselves partners.',
'For established dental and medical practices, the buyout often interacts with equipment debt, a jointly owned building, retirement plans and the departing owner’s remaining work. Resolve those connections while the agreement is being negotiated.'],[
('Identify the payer and tax classification',[
'Collect the governing agreement, ownership ledger and recent returns. Determine whether the buyer is the continuing owner, the operating entity or another acquisition entity. Then identify whether the transaction is an interest purchase, redemption or asset acquisition.',
'For a partnership, a direct interest sale and payments liquidating a retiring partner’s interest follow different rules. Receivables, goodwill, liabilities and the terms of the agreement can affect character and basis. Corporate redemptions need a separate analysis; partnership rules do not apply simply because the owners use the word “partner.”']),
('Separate the purchase price from other payments',[
table(['Payment or obligation','Review question'],[['Ownership purchase price','Who pays it and what basis results?'],['Unpaid compensation or ongoing services','How is work before and after departure documented?'],['Seller note and interest','What are payment dates, guarantees and tax timing?'],['Building interest or lease','Does the property remain jointly owned or change hands?'],['Existing loans','Which liabilities and guarantees change after the buyout?']]),
'A total price without this breakdown can hide a funding gap or inconsistent reporting. Ask each party’s advisors to reconcile the intended treatment before the closing schedules are finalized.']),
('Do not assume the buyer gets a new equipment deduction',[
'Buying an ownership interest does not automatically reset the operating entity’s asset basis. A partnership acquisition may require analysis of an available Section 754 election and a transferee-specific adjustment; that is a different assignment from recording a new equipment purchase.',
'Retain prior depreciation and basis schedules. The buyer needs a reliable opening position, while the seller needs records supporting the disposition. The same balance-sheet capital number should not be assumed to answer every tax-basis question.']),
('Model the practice after the partner leaves',[
'A hypothetical two-owner practice borrows to buy out one owner. The continuing owner expects the same profit with one fewer owner distribution. The forecast should also account for reduced clinical production, replacement staffing, debt service and transition costs.',
'Compare available cash after the buyout with owner compensation, retirement funding and operating reserves. The transaction can be affordable on an earnings statement and still strain monthly cash. This example illustrates planning questions rather than a client outcome.']),
('Create a closing and first-year handoff',[
ul(['Agree on transaction structure and required independent legal or valuation work.','Reconcile ownership, basis, liabilities and historical fixed assets.','Assign final or continuing K-1, corporate and owner reporting.','Review payroll, retirement plans and property arrangements affected by the departure.','Schedule a post-closing review against the final agreement and loan documents.']),
'Arrange secure delivery of agreements and returns. A first conversation can begin with the entity type, ownership percentages, proposed payer, approximate price and target date.'])],
[('Is a practice buyout payment always deductible?','No. Treatment depends on the transaction and payment component. A purchase of ownership, redemption payment, service payment and interest can have different consequences.'),('Does buying my partner’s share create a new basis in all practice assets?','Not automatically. The entity’s tax classification and transaction structure determine whether an asset-basis adjustment is available and how it is recorded.')],
('/physician-tax-planning/','Practice-owner advisory'),('/case-studies/dental-practice-business-rental-tax-roadmap/','a documented practice planning roadmap'),['partnership','sale','disposition'])
page('/blog/buying-second-medical-dental-practice-tax-planning/',
'Buying a Second Practice: Coordinate Entities, Staff and Cash',
'Buying a Second Practice: Tax Planning | AE Tax Advisors',
'Before buying a second medical or dental practice, coordinate acquisition structure, retirement plans, owner income and opening tax records.',
'buying a second practice tax planning',
['Buying a second medical or dental practice adds a new transaction to an existing tax and operating system. The right question is how the acquisition fits ownership, staff, debt, owner income and records across both locations.',
'This guide is for practice owners evaluating another operating practice, not simply opening an additional bank account. Start with the proposed purchase agreement and a combined cash forecast, then decide which entity and specialist questions must be resolved before closing.'],[
('Compare the acquisition structure with the existing practice',[
'Identify whether the offer buys assets, stock or another ownership interest. Confirm the legal buyer, financing borrower and ownership percentages. A separate entity may serve a business purpose, but it can also add returns, payroll administration, accounting and intercompany documentation.',
'Professional-practice ownership and licensing requirements vary by state and require appropriate counsel. Federal tax treatment is a separate review. If S corporation treatment is considered, allowable shareholders and the one-class-of-stock requirement must be addressed rather than assuming any existing company can own the new practice.']),
('Reconcile the price and opening records',[
'For a covered asset purchase, the allocation should connect with acquired equipment, other assets and goodwill. If the purchase includes a building, separate the real estate review from the operating practice schedule. Confirm the opening records with the buyer’s preparer before depreciation is entered.',
'An ownership-interest acquisition needs a different basis analysis. Do not reuse an asset-purchase spreadsheet simply because the same lender financed a previous location. Record transaction expenses separately for review instead of treating every closing payment as an immediate deduction.']),
('Review employees and retirement plans across the businesses',[
'Collect the acquired practice’s employee census, plan documents and benefit obligations before relying on a projected owner retirement deduction. Related-employer, coverage and transaction rules can affect the plan analysis. A separate company does not automatically isolate staff from the existing retirement arrangement.',
'Ask the administrator and benefits specialists to identify continuation, transition and testing questions with actual dates. Use '+a('/blog/cash-balance-plan-multiple-businesses-controlled-group/','the multiple-business cash balance guide')+' to prepare the ownership and service map.']),
('Model operating cash before increasing commitments',[
table(['Combined forecast','Decision it supports'],[['Collections and staffing','Whether acquisition assumptions leave enough operating cash'],['Debt service and integration costs','Whether the owner can fund the transition'],['Owner compensation and distributions','How owner cash flows change across entities'],['Retirement and taxes','Which commitments fit alongside the acquisition'],['Property and equipment needs','Which additional projects can wait']]),
'A hypothetical owner acquires a second practice with different payroll software and a retiring seller. The first priority may be reliable combined financials and a collections transition, rather than another entity election. That sequence helps the team model the tax questions using credible operating assumptions. The example is illustrative.']),
('Name the owners of the first-year work',[
ul(['Deal counsel: professional ownership, agreements and legal structure.','Bookkeeper: separate opening balances and consistent reporting across locations.','Tax advisor and preparer: acquisition treatment, owner projections and required returns.','Payroll and retirement specialists: employee transition and plan review.','Practice owner: provide records, approve decisions and track deadlines.']),
'Before closing, request a checklist linking every major recommendation to a responsible person and completion evidence. Schedule a review once the opening books and final purchase schedules are available.'])],
[('Should the second practice always have a separate LLC?','No universal structure fits every acquisition. Review legal ownership rules, liability, financing, partners, tax treatment and administration with the relevant professionals.'),('Can I put a cash balance plan in just the acquired company?','That needs a related-employer and plan-design review. Separate entities do not automatically permit separate treatment of employees.')],
('/physician-tax-planning/','Medical and dental practice advisory'),('/case-studies/dental-practice-business-rental-tax-roadmap/','a documented practice-owner planning roadmap'),['assets','scorp','groups'])
page('/blog/cost-segregation-portfolio-prioritization/',
'Which Rental Property Should You Study First?',
'Prioritize Cost Segregation Across a Portfolio | AE Tax',
'Prioritize cost segregation across your rental portfolio using records, usable deductions, hold periods and total implementation costs.',
'cost segregation portfolio prioritization',
['Prioritizing cost segregation across a rental portfolio starts with the owner’s tax position and the records for each building. The largest purchase price is not automatically the best first study, and the largest projected deduction is not automatically the largest current benefit.',
'Build a property-by-property decision sheet, then connect it to the taxpayers and activities reporting the results. The first assignment may be completing missing basis records or implementing an existing report rather than ordering another study.'],[
('Create a portfolio inventory that reaches the return',[
ul(['Property, ownership entity and taxpayer reporting the income.','Acquisition and placed-in-service dates, use and improvement history.','Purchase allocation, supported land amount and current adjusted basis.','Existing depreciation schedules, prior studies and correction work.','Participation records, activity-level losses and known limitations.','Expected holding period, planned sale and estimated study plus filing costs.']),
'One consolidated spreadsheet is an organizational tool. It does not combine legal entities, make grouping elections or establish that one activity’s losses can offset another activity’s income. Keep those questions explicit.']),
('Rank readiness and usable benefit separately',[
'A cost segregation study addresses asset classification. Whether and when resulting deductions reduce the owner’s taxes requires separate analysis of basis, at-risk, passive-activity and other applicable limits. Review the federal and relevant state treatment using the acquisition and tax-year facts.',
table(['Portfolio situation','Likely first assignment'],[['Existing study never reported','Reconcile the report with returns and determine implementation'],['Large property with uncertain land allocation','Resolve basis and supporting records'],['Property expected to sell soon','Compare accelerated deductions with disposition costs and timing'],['Strong records but suspended losses','Model when additional deductions could be usable'],['Multiple properties with usable benefit','Compare total costs and sequence the work']]),
'A percentage-based estimate can screen an opportunity, but it is not a completed engineering report or a return-level tax conclusion. Ask what evidence would change the proposed ranking.']),
('Use a consistent comparison instead of a savings leaderboard',[
'Compare each property against its existing no-study depreciation schedule. Show the incremental deduction, expected year of use, study fee, implementation cost and effect on later deductions and sale assumptions. Keep tax savings, tax deferral and deduction amounts in separate columns.',
'A near-term sale can change the economics even when a current deduction is usable. Request an alternative if the holding period shortens. Use '+a('/rental-property-sale-tax-calculator/','the property-sale discussion calculator')+' to organize questions after the underlying basis and treatment have been reviewed.']),
('Illustrative sequence for an established portfolio',[
'A hypothetical owner has six rentals. One already has a report awaiting filing, one is being sold, two have complete acquisition records and two lack improvement invoices. Ordering six new studies would ignore the different assignments.',
'A staged scope could first reconcile the existing report, model the planned disposition and review the two ready properties. Record collection can continue for the remaining buildings. The final order depends on the return-level model; this illustration does not predict a tax result.']),
('Define the study and preparer handoff',[
'Request a report tied to the property’s supported basis, with methodology and asset detail that the preparer can evaluate. The IRS cost segregation audit technique guide describes examination considerations; it is not an IRS approval of a provider or a substitute for applicable law.',
'Assign the person preparing any correction or election, updating depreciation, tracking carryovers and reviewing the return. Confirm deliverables and separate fees before starting the next building. Review the priority list when income, ownership, operating use or the planned sale date changes.'])],
[('Should I study every rental in the same year?','Not automatically. Compare records, deduction usability, holding periods and full implementation costs before sequencing the portfolio.'),('Does a larger cost segregation deduction always create more current savings?','No. Loss limits, other tax interactions and state treatment may affect when and how much benefit is available.')],
('/real-estate-tax-strategy-business-owners/','Business and rental portfolio advisory'),('/case-studies/multi-business-owner-property-planning-roadmap/','a documented business-and-property planning roadmap'),['passive','depreciation','disposition','quality'],False)
page('/compare/keep-cpa-hire-tax-strategist/',
'Can You Keep Your CPA and Hire a Tax Strategist?',
'Keep Your CPA and Hire a Tax Strategist | AE Tax',
'Keep your CPA while hiring a tax strategist: define records, modeling, implementation, return review and responsibility before engaging another advisor.',
'keep CPA hire tax strategist',
['You can discuss keeping your CPA while hiring a tax strategist when the division of work is clear and both professionals agree to the arrangement. Established owners often need transaction modeling or coordination across businesses and rentals while an existing preparer continues annual filing.',
'The practical issue is who reviews the facts, develops recommendations, carries them out and reports the result. Put those responsibilities into the proposed engagement before paying for an additional planning relationship.'],[
('Agree on a responsibility map',[
table(['Workstream','Assignment to confirm'],[['Current books and records','Who reconciles accounts and confirms the source data?'],['Planning and alternatives','Who models scenarios and states assumptions?'],['Technical review','Who checks eligibility and supporting authority?'],['Implementation','Who handles payroll changes, elections and specialist coordination?'],['Return preparation','Who evaluates and reports the final position?'],['Follow-up','Who checks completion and updates projections?']]),
'The return preparer needs sufficient support to evaluate a position. A recommendation deck alone may omit calculations, taxpayer details or documentation needed for filing. Agree on the actual handoff documents and review dates.']),
('Set a review process for multiple entities',[
'Identify the businesses, property entities, owner returns, states and tax years in scope. Separate preparers may otherwise work from different versions of income, depreciation or ownership records. Use one list of open items and identify who approves the final assumptions.',
'Keep intercompany payments and household-level questions visible. A change in one entity may affect another filing or the owner’s projected payments. Ask the planner to identify those dependencies rather than assuming every preparer will infer them.']),
('Resolve a disagreement before implementation',[
'If the professionals disagree, ask each to state the disputed facts, relevant authority and missing records. Distinguish a technical disagreement from a timing or scope problem. A recommendation delivered too late may be difficult to implement even where its underlying analysis is sound.',
'For unresolved specialist issues, discuss an independent review and its cost. Do not treat the largest projected deduction as proof that a position is correct. Record the final conclusion and the professional responsible for reporting it.']),
('Illustrative handoff for an acquisition',[
'A hypothetical owner retains the existing CPA for annual returns and hires an advisor to compare buying a second practice through different structures. The advisor prepares a decision memo and calculations; counsel evaluates legal documents; the CPA reviews opening records and reporting before closing.',
'The owner tracks the required approvals and supplies the records. Each professional confirms their own fee and scope. This arrangement illustrates coordination rather than a promise that every preparer will accept another advisor’s proposal.']),
('Questions before engaging AE',[
ul(['Can we agree on coordination with my existing CPA before the engagement begins?','Which entities, years, written deliverables and review meetings are included?','Who prepares any return, election, amendment or accounting-method change?','What happens if the preparer needs additional technical support?','What is the total cost, including other professionals and implementation?']),
'Arrange consent and secure document sharing with the team. Begin with an overview of the current accountant’s work and the decision you need help with; do not send returns through a general inquiry form. The IRS recommends checking credentials and discussing fees when choosing a tax professional.'])],
[('Do I have to replace my CPA to hire AE?','Discuss the coordination arrangement and scope with AE and your current CPA. The engagement should explicitly assign review, implementation and filing responsibilities.'),('Who is responsible for a recommendation appearing on my return?','Agree on the planner’s support and the preparer’s evaluation and reporting responsibilities. Hiring several professionals does not remove the taxpayer’s responsibility to review the return.')],
('/business-owner-small-business-tax/','Business-owner advisory'),('/case-studies/multi-business-household-filing-map/','a documented multi-business filing-map case'),['professional'],False)
page('/what-a-tax-advisory-engagement-includes/',
'What Should a $7,800–$9,800 Tax Advisory Engagement Include?',
'Tax Advisory Deliverables and Fees | AE Tax Advisors',
'Compare a $7,800–$9,800 tax advisory engagement by records reviewed, written deliverables, implementation responsibilities and separately priced work.',
'what tax advisory engagement includes',
['A tax advisory engagement should turn a defined business or investment question into documented analysis and an actionable plan. For a profitable owner, value depends on the quality of the decisions and follow-through, not the number of strategies mentioned in a presentation.',
'AE publishes Strategic Tax Advisory at $7,800 and Complex Tax Advisory at $9,800. The signed agreement determines the deliverables and support period. Use the questions below to compare proposals for the same entities, decisions and implementation work.'],[
('Start with the decision and the records',[
'A useful scope identifies the taxpayer, entities, properties, states and years being reviewed. It also states the owner’s decision: an acquisition, retirement commitment, ownership change, property sale or another matter requiring coordinated analysis.',
'Request a record list and a process for missing information. Prior returns, ownership records, current financials and supporting schedules can affect whether a model is reliable. A recommendation based on incomplete records should identify its unresolved assumptions instead of presenting them as settled facts.']),
('Ask for written alternatives and a clear baseline',[
table(['Deliverable to specify','What the owner should be able to understand'],[['Current-position review','What is happening today and which facts remain uncertain'],['Scenario comparison','How available alternatives differ in cash, taxes, costs and risk'],['Written recommendations','Why a proposed action fits the documented facts'],['Implementation schedule','Who performs each task and when'],['Completion evidence','What confirms an election, funding, filing or other action occurred']]),
'Any savings model should distinguish deductions from tax savings, and permanent savings from changes in timing. Ask whether calculations include administrative costs, future consequences and assumptions about income or disposition. A headline projection does not establish realized benefits.']),
('Separate planning from implementation and filing',[
'Identify who prepares legal documents, performs valuation or engineering work, processes payroll and files returns. Discuss which work AE performs, which is separately scoped and which requires another professional. Coordination should include the person responsible for resolving an incomplete handoff.',
'If you retain an existing CPA, agree on when the preparer receives the calculations and what support is available. Use '+a('/compare/keep-cpa-hire-tax-strategist/','the CPA and strategist coordination guide')+' to define that arrangement.']),
('Compare the full price and support period',[
'AE’s standard $7,800 advisory engagement can be paid in two $3,900 payments, 30 days apart, with no required recurring annual planning fee. Returns, amendments, cost segregation and additional work are separately scoped. Complex advisory is published at $9,800; confirm the applicable scope and payment terms in the proposal.',
'No required annual planning renewal does not promise unlimited future planning. Confirm the start and end dates, meeting schedule, communication process and terms for additional work. Any audit support or representation should specify the issues, years, exclusions and responsible professional.',
'For a transaction involving several entities, ask for the complete project budget. Advisory, return work, plan administration, legal services and independent specialist costs may each have separate fees.']),
('Illustrative comparison: two proposals for the same owner',[
'A hypothetical owner has two operating businesses, rental property and a pending acquisition. One proposal offers a strategy presentation. Another includes an agreed record review, written alternatives, responsibility assignments and a coordinated handoff. Compare the work each actually promises before comparing the fees.',
'Neither a higher price nor a larger projected saving proves better advice. A review may support keeping the current structure, collecting better records or postponing a transaction. These can be useful conclusions even when the review does not produce a new deduction. The example is illustrative, not a client outcome.']),
('Bring a decision summary to the first conversation',[
ul(['Income sources and approximate annual business profit.','Entity and property ownership, with states involved.','The transaction or planning decision and target date.','What current advisors handle and where coordination is missing.','The deliverables you need to make or implement the decision.']),
'Compare proposals using '+a('/tools/tax-advisor-engagement-scorecard/','the engagement scorecard')+' and '+a('/pricing/','current published pricing')+'. Confirm the proposed scope before supplying detailed records through the agreed secure process.'])],
[('Does the advisory fee include tax returns and studies?','Returns, amendments, cost segregation and additional work are separately scoped and priced. Ask for the complete project cost for your situation.'),('Does paying $7,800 or $9,800 guarantee savings?','No. Results depend on facts, eligibility, records and implementation. Proposed benefits are estimates, and the review may support retaining the current approach.')],
('/business-owner-small-business-tax/','Business-owner advisory'),('/case-studies/multi-business-household-filing-map/','a documented engagement-scope and filing-map case'),['professional'],False)

TEMPLATE=(ROOT/'buying-dental-practice-and-building-tax-allocation/index.html').read_text()
pre=TEMPLATE[:TEMPLATE.index('<main>')]
post=TEMPLATE[TEMPLATE.index('</main>')+len('</main>'):]
# New article metadata replaces the template's article and FAQ claims.
pre=re.sub(r'<script\b[^>]*type="application/ld\+json"[^>]*>.*?</script>','',pre,flags=re.S)
FEES='<p><strong>Strategic Tax Advisory: $7,800. Complex Tax Advisory: $9,800.</strong> Returns, amendments, cost segregation and additional work are separately scoped. Confirm the entities, written deliverables, implementation responsibilities and support period in your agreement.</p>'
def section(title,paras):return '<section class="content-section"><div class="container narrow"><h2>'+title+'</h2>'+''.join(x if x.startswith(('<ul','<div','<table','<p','<h3')) else '<p>'+x+'</p>' for x in paras)+'</div></section>'
def render(p):
 url=SITE+p['path']; head=pre
 head=re.sub(r'<title>.*?</title>','<title>'+html.escape(p['meta'])+'</title>',head,flags=re.S)
 head=re.sub(r'(<link rel="canonical" href=")[^"]+("\s*/?>)',lambda m:m[1]+url+m[2],head)
 values={'description':p['description'],'og:title':p['meta'],'og:description':p['description'],'og:url':url,'twitter:title':p['meta'],'twitter:description':p['description'],'article:published_time':DATE+'T12:00:00-04:00','article:modified_time':DATE+'T12:00:00-04:00'}
 for k,v in values.items():head=re.sub(r'(<meta (?:name|property)="'+re.escape(k)+r'" content=")[^"]*("\s*/?>)',lambda m:m[1]+html.escape(v,quote=True)+m[2],head)
 original=ROOT/p['path'].strip('/')/'index.html'
 published=DATE
 if not p['new']:
  prev=original.read_text();m=re.search(r'"datePublished"\s*:\s*"([^"]+)"',prev)
  if m:published=m[1][:10]
 head=re.sub(r'(<meta property="article:published_time" content=")[^"]+',lambda m:m[1]+published+'T12:00:00-04:00',head)
 ld={'@context':'https://schema.org','@type':'Article','headline':p['title'],'description':p['description'],'url':url,'mainEntityOfPage':url,'datePublished':published,'dateModified':DATE,'author':{'@type':'Organization','name':'AE Tax Advisors','url':SITE+'/'},'publisher':{'@type':'Organization','name':'AE Tax Advisors','url':SITE+'/'},'citation':[SOURCES[k][0] for k in p['sources']]}
 crumbs={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':SITE+'/'},{'@type':'ListItem','position':2,'name':'Owner decision guides','item':SITE+'/blog/'},{'@type':'ListItem','position':3,'name':p['title'],'item':url}]}
 head=head.replace('</head>','<script type="application/ld+json">'+json.dumps([ld,crumbs],ensure_ascii=False).replace('</','<\\/')+'</script></head>')
 body='<main><section class="page-header"><div class="container narrow"><nav class="breadcrumb" aria-label="Breadcrumb">'+a('/','Home')+' &rsaquo; '+a('/blog/','Owner decision guides')+'</nav><h1>'+html.escape(p['title'])+'</h1><p class="subtitle">'+html.escape(p['description'])+'</p><p>By AE Tax Advisors Team · Updated October 24, 2026</p></div></section>'
 body+=section('Start with the decision',p['intro'])
 for title,paras in p['sections']:body+=section(title,paras)
 body+=section('Questions owners ask',[('<h3>'+html.escape(q)+'</h3><p>'+html.escape(ans)+'</p>') for q,ans in p['faqs']])
 body+=section('Discuss the advisory scope',[FEES,'<p>'+a(*p['service'])+' · '+a('/pricing/','Fees and engagement scope')+'</p>','<p>Read '+a(*p['case'])+'. Check the case facts and status: a planning recommendation or engagement scope does not establish completed implementation or realized tax savings.</p>','<p>'+a('/discovery/','Discuss your decision and advisory fit')+'</p>'])
 body+=section('Sources and editorial context',[ul([a(*SOURCES[k]) for k in p['sources']]),'<p>General educational information prepared with AI assistance; no individual professional review or client result is represented. Sources provide background, not approval of a transaction. Conclusions require the applicable rules and your records. '+a('/editorial-policy/','Editorial policy')+' · '+a('/ai-disclosure/','AI disclosure')+'</p>'])
 body+='</main>'
 return (head+body+post).replace('</section>', '</section>\n').replace('</p>', '</p>\n').replace('</h2>', '</h2>\n')

if __name__=='__main__':
 manifest=[]
 for p in PAGES:
  out=ROOT/p['path'].strip('/')/'index.html'
  if p['new'] and out.exists() and 'owner-decision-batch:20261024' not in out.read_text():raise ValueError('New route already exists: '+p['path'])
  out.parent.mkdir(parents=True,exist_ok=True)
  out.write_text(render(p).replace('<main>','<!-- owner-decision-batch:20261024 --><main>',1))
  manifest.append({k:p[k] for k in ['path','title','primary_keyword','new','sources']})
 # Links belong on existing service pages and relevant subject guides.
 destinations={
 'retirement-exit-ma-tax-strategy/index.html':[0,1],
 'business-owner-small-business-tax/index.html':[0,1,2,6,7],
 'physician-tax-planning/index.html':[2,3,4],
 'real-estate-tax-strategy-business-owners/index.html':[0,5],
 'buying-dental-practice-and-building-tax-allocation/index.html':[3,4],
 'cash-balance-plan-tax-deduction/index.html':[2],
 'blog/index.html':list(range(8)),
 'sitemap/index.html':list(range(8)),
 'workbooks/business-sale/business-sale-letter-of-intent-review/index.html':[1]}
 for f,ids in destinations.items():
  file=ROOT/f;s=file.read_text();s=re.sub(r'<!-- owner-decisions:start -->.*?<!-- owner-decisions:end -->','',s,flags=re.S)
  block='<!-- owner-decisions:start -->'+section('Planning for your next ownership decision',[ul([a(PAGES[i]['path'],PAGES[i]['title']) for i in ids])])+'<!-- owner-decisions:end -->'
  if f=='blog/index.html':
   pos=s.index('</section>',s.index('<main'))+len('</section>');s=s[:pos]+block+s[pos:]
  else:
   assert '</main>' in s,f;s=s.replace('</main>',block+'</main>',1)
  file.write_text(s)
 # Preserve the existing main sitemap and register each new canonical route once.
 file=ROOT/'sitemap.xml';s=file.read_text()
 for p in PAGES:
  url=SITE+p['path'];pat=r'<url>\s*<loc>'+re.escape(url)+r'</loc>.*?</url>'
  entry='<url><loc>'+url+'</loc><lastmod>'+DATE+'</lastmod></url>'
  if re.search(pat,s,re.S):s=re.sub(pat,lambda m:entry,s,flags=re.S)
  else:s=s.replace('</urlset>',entry+'\n</urlset>')
 file.write_text(s)
 out=ROOT/'content/premium-owner-decisions-20261024'
 (out/'manifest.json').write_text(json.dumps({'date':DATE,'pages':manifest,'discovery_pages':list(destinations),'sources':SOURCES},indent=2,ensure_ascii=False)+'\n')
 print('Rendered',len(PAGES),'guides: 5 new, 3 expanded; linked from',len(destinations),'existing destinations.')
