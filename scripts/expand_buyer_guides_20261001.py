"""Add distinct buyer evidence and comparison worksheets to established URLs.

Run after other page generators. Blocks are replaced by markers on subsequent runs.
No client outcomes or customer quotations are generated here.
"""
from pathlib import Path
import sys,re,json,csv,io
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(Path(__file__).parent))
import site_template as T
from client_stories_20261001 import STORIES
BASE=T.SITE
PASSIVE=('IRS Publication 925: Passive Activity and At-Risk Rules','https://www.irs.gov/publications/p925')
DEPRECIATION=('IRS Publication 946: How To Depreciate Property','https://www.irs.gov/publications/p946')
COMP=('IRS: S Corporation Compensation','https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues')
METHOD=('IRS Instructions for Form 3115','https://www.irs.gov/instructions/i3115')
GUIDES=[
dict(key='str-advisor',path='/compare/best-tax-advisors-short-term-rental-owners/',title='Best Short Term Rental Tax Company & Advisors | AE Tax',h1='Best Short Term Rental Tax Company and Airbnb Tax Accountant',desc='Choose an Airbnb tax accountant or STR tax advisor by comparing participation review, cost segregation, filing support, fees and documented planning work.',
 lead='The best Airbnb tax accountant for an owner-operated vacation rental may offer a different scope from the right STR tax advisor for a managed portfolio. Start with the property’s operating facts, the household’s income and the work you need delivered. Ask who connects that information to the filed return.',
 heading='Match the STR engagement to your operating model',
 rows=[('First Airbnb purchase','Who reviews the closing file, furnishing budget and rental-readiness records before a study is ordered?'),('Self-managed vacation rental','Who reviews actual guest stays, personal use and each person’s work records?'),('Property-manager arrangement','Who evaluates the management agreement and the owner’s documented participation?'),('Multiple STRs','Who maintains property-level schedules and coordinates entity and household reporting?'),('Local compliance','Does the proposal include lodging-tax registration and marketplace remittance reconciliation, or only income-tax services?')],
 example='Hypothetical comparison: a first-time Airbnb buyer needs a closing-to-filing calendar; an owner with several seasons of operations needs a review of depreciation, loss carryforwards and management records. Compare the deliverables for the actual stage, rather than choosing solely by a projected deduction.',
 stories=[5,12,15],resources=[('/guides/str-documentation-kit/','STR documentation kit'),('/short-term-rental-tax-strategy/','AE short-term rental tax planning')],sources=[PASSIVE,DEPRECIATION],
 faqs=[('What should the best Airbnb tax accountant review before quoting?','The property’s ownership, rental stage, stay history, personal use, management arrangements, prior depreciation and required returns. Ask whether the quote includes planning, a study, preparation and local lodging-tax work.'),('Should I hire an STR tax advisor before purchasing?','A pre-purchase discussion can identify the required records, provisional assumptions and implementation schedule. A purchase estimate cannot establish final loss treatment; operating facts still need review.')]),
dict(key='str-study',path='/compare/best-cost-segregation-companies-short-term-rentals/',title='Best STR & Airbnb Cost Segregation Companies | AE Tax',h1='Best Cost Segregation Companies for Short-Term Rentals and Airbnb',desc='Compare STR and Airbnb cost segregation companies by study scope, furnishing reconciliation, pricing, preparer handoff and support after delivery.',
 lead='The best cost segregation company for a short-term rental should explain what is inside the study, which records support the classifications and how the report reaches your tax preparer. For a furnished Airbnb, ask how separately purchased furniture and improvements are reconciled so the same cost is not counted twice.',
 heading='Compare a furnished STR study from records to return',
 rows=[('Basis and land','How are acquisition costs, land allocation and prior depreciation reconciled?'),('Furniture and improvements','Which furnishings are separately owned or purchased, and which assets are included in the building acquisition?'),('Study method','What property records, inspection information and component calculations support the report?'),('Return handoff','Who maps the report into the depreciation schedule and evaluates an existing-property method change?'),('After delivery','What correction, explanation and separately scoped examination support is available?')],
 example='Hypothetical comparison: two studies show similar accelerated deductions. One quote covers only the report; the other separately itemizes report preparation, schedule reconciliation and preparer coordination. Compare those deliverables and the total fee rather than assuming the headline study price covers filing.',
 stories=[12,15,19],resources=[('/cost-segregation-study-cost-pricing/','AE cost segregation study pricing'),('/compare/best-cost-segregation-companies-tax-filing-support/','Compare study providers with filing support')],sources=[DEPRECIATION],
 faqs=[('How do I compare cost segregation companies for an Airbnb?','Use the same closing records, furnishing invoices, improvement history and prior depreciation schedules. Ask for study boundaries, method, sample deliverables, pricing and the responsibility for incorporating the report into the return.'),('Does a cost segregation study guarantee an STR tax saving?','No. A study addresses asset classification and depreciation. Actual tax consequences also depend on loss limitations, property use, the household return, state treatment, fees and later disposition.')]),
dict(key='business-rentals',path='/compare/best-tax-advisors-business-owners-buying-rental-property/',title='Best Tax Advisors for Business Owners With Rentals | AE Tax',h1='Best Tax Advisors for Business Owners With Rental Properties',desc='Compare tax advisors for business owners with rentals: coordinated projections, entity review, depreciation, retirement planning and implementation scope.',
 lead='The best tax advisor for a business owner with rental properties should connect the operating business and the property portfolio in one household projection. That means reviewing payroll, pass-through income, financing, retirement funding and the usability of rental deductions before recommending an acquisition or a new entity.',
 heading='Compare business and rental planning in one engagement',
 rows=[('Business forecast','Who updates operating profit, owner pay and distributions before modeling a property purchase?'),('Acquisition decision','Who separates investment economics from a provisional depreciation benefit?'),('Ownership and financing','Who coordinates proposed ownership with the lender, legal counsel and reporting requirements?'),('Cash and retirement','Who evaluates retirement funding alongside reserves, debt service and property spending?'),('Return coordination','Who connects business K-1s, rental schedules and estimated payments on the household return?')],
 example='Hypothetical comparison: a profitable contractor wants to buy a rental while also funding a retirement plan. A useful engagement models the cash required for both decisions and identifies which deductions may be usable. A property-only study cannot answer that complete planning question.',
 stories=[7,8,17],resources=[('/business-owner-small-business-tax/','Business owner tax advisory'),('/s-corp-and-real-estate-coordination-for-active-businesses/','S-corp and real estate coordination')],sources=[PASSIVE],
 faqs=[('Can one tax advisor coordinate my business and rental properties?','Ask for a written scope connecting business reporting, owner income, rental records and the household projection. Confirm whether entity restructuring, studies, returns and legal work are included or separately engaged.'),('Should I buy a rental just to reduce business taxes?','Evaluate cash flow, financing, operating responsibilities and exit plans before relying on a tax projection. The advisor should explain which assumptions are provisional and which loss limitations require further review.')]),
dict(key='s-corp-owner',path='/compare/best-tax-advisors-s-corp-owners-rental-property/',title='Best S-Corp Tax Advisors for Owners With Rentals | AE Tax',h1='Best S-Corp Tax Advisors for Owners With Rental Property',desc='Compare S-corp tax advisors by owner compensation, payroll, retirement, basis records and coordination with rental properties and household returns.',
 lead='The best S-corp tax advisor should turn entity planning into a workable payroll, bookkeeping and filing process. For owners with rental property, the advisor also needs to connect the business return with property income and the household’s tax position. An election alone does not complete that work.',
 heading='Ask for the S-corp operating plan, not just an election',
 rows=[('Owner compensation','Who documents duties and reviews compensation before distributions are finalized?'),('Payroll and benefits','Who coordinates the payroll provider, owner benefits and year-end reporting?'),('Retirement funding','Who reviews employee coverage, ownership relationships and cash available for contributions?'),('Basis and distributions','Who maintains the records used to evaluate shareholder distributions and losses?'),('Rental ownership','Who compares proposed property ownership with financing, distribution and eventual sale consequences?')],
 example='Hypothetical comparison: a newly elected S-corp owner and a longstanding owner with several entities need different projects. The first may need payroll and reimbursement setup; the second may need a year-by-year basis and distribution reconciliation. Ask for a proposal that identifies the actual starting point.',
 stories=[4,1,23],resources=[('/s-corp-tax-strategy/','S-corp tax strategy'),('/s-corp-tax-savings-calculator/','S-corp planning calculator')],sources=[COMP,PASSIVE],
 faqs=[('What should I ask when choosing an S-corp tax advisor?','Ask who reviews owner compensation, payroll, benefits, retirement coverage, shareholder basis and distributions. Confirm the implementation calendar and which services are separately billed.'),('Does an S-corp election make rental losses usable?','The election does not by itself establish the treatment of a separate rental activity. Ownership, participation and applicable loss limits still require review; ask for a coordinated analysis before restructuring property ownership.')]),
dict(key='rental-portfolio',path='/compare/best-cpas-multiple-rental-properties/',title='Best CPA for Multiple Rental Properties | AE Tax',h1='Best CPA for Multiple Rental Properties: Compare Portfolio Support',desc='Choose a CPA for multiple rental properties by comparing property records, entity returns, K-1s, loss carryforwards, study coordination and transition fees.',
 lead='The best CPA for multiple rental properties should be able to trace each property from ownership and books to depreciation, entity reporting and the owners’ returns. A mixed portfolio needs a reporting map: which taxpayer owns each asset, which return reports it and which limitations need separate worksheets.',
 heading='Use a portfolio handoff matrix to compare CPAs',
 rows=[('Property-to-entity map','Which owner, entity and return correspond to each property?'),('Depreciation register','Who reconciles acquisition costs, land, improvements, studies and prior deductions?'),('Partnership reporting','Who reviews contributions, distributions, debt allocations and K-1 delivery?'),('Carryforwards','Who traces basis, at-risk and passive-loss limitations year by year?'),('Provider transition','What onboarding fee covers prior records, software migration and unresolved adjustments?')],
 example='Hypothetical comparison: an investor owns one property personally and another through a partnership. A portfolio-wide report may still be insufficient without the entity-to-owner handoff and separate loss worksheets. Request a property-level responsibility map before comparing preparation fees.',
 stories=[11,19,20],resources=[('/rental-property-tax-planning/','Rental property tax planning'),('/compare/best-cost-segregation-companies-rental-portfolios/','Portfolio cost segregation comparisons')],sources=[PASSIVE,DEPRECIATION],
 faqs=[('What records does a CPA need for multiple rental properties?','Provide a property and ownership inventory, prior entity and personal returns, K-1s, depreciation schedules, financing records, improvement invoices and loss carryforward worksheets. Identify missing records before agreeing to the transition scope.'),('Can a single portfolio study replace owner-level tax review?','No. Study work and owner-level tax reporting serve different purposes. The engagement should identify who evaluates each taxpayer’s basis, at-risk position and passive activity limitations.')]),
dict(key='physician-rentals',path='/compare/best-tax-advisors-physicians-rental-property/',title='Best Tax Advisors for Physicians With Rentals | AE Tax',h1='Best Tax Advisors for Physicians With Rental Properties',desc='Compare physician tax advisors for practice income, W-2 wages, rental properties, spouse participation, retirement funding and coordinated household planning.',
 lead='The best tax advisor for a physician with rental properties should distinguish employed medical work from practice ownership and review the household’s actual property activities. A physician’s professional income alone does not establish how rental losses are treated. Compare the records reviewed and the professional responsible for the complete household projection.',
 heading='Compare the medical practice and property workstreams',
 rows=[('Employment or ownership','Who separates W-2 wages, practice ownership and other professional income?'),('Spouse participation','Who reviews each person’s work records and the relevant activity-specific requirements?'),('Rental operations','Who reviews management agreements, actual stays and personal use before modeling loss treatment?'),('Retirement and liquidity','Who coordinates available workplace plans, practice plans and property cash needs?'),('Professional coordination','Who assigns legal, payroll, study and filing responsibilities in the written engagement?')],
 example='Hypothetical comparison: an employed physician with a managed rental and a practice owner whose household operates property directly may need different analyses. Request a proposal based on each person’s records rather than a generic promise that real estate will offset medical income.',
 stories=[3,2,6],resources=[('/physician-tax-planning/','Physician tax planning'),('/compare/physician-business-real-estate-tax-advisors/','Practice and real estate advisor comparison')],sources=[PASSIVE],
 faqs=[('What makes a physician tax advisor a good fit for rental investing?','The advisor should connect professional income, practice structure where applicable, property records and the household return. Confirm who reviews spouse participation, retirement funding and separate study or filing work.'),('Do these planning stories prove a physician will save the same amount?','No. The linked stories document particular plans or engagement scopes and identify unresolved steps. They are not independent reviews or promises of the same tax outcome for another household.')]),
dict(key='study-filing',path='/compare/best-cost-segregation-companies-tax-filing-support/',title='Cost Segregation Companies With Tax Filing Support | AE Tax',h1='Best Cost Segregation Companies With Tax Preparation and Filing Support',desc='Compare cost segregation companies with tax filing support: study delivery, depreciation schedules, Form 3115 review, return preparation and separate fees.',
 lead='A cost segregation company with tax preparation support can help connect the report to the return, but the phrase “filing support” needs a precise definition. Ask whether it means answering your preparer’s questions, preparing schedules, evaluating a method change or actually signing and filing the tax return.',
 heading='Define the handoff from study to filed return',
 rows=[('Study delivery','Which taxpayer and property basis does the final report address?'),('Schedule integration','Who reconciles the report with prior depreciation and separately purchased assets?'),('Method-change review','Who evaluates whether Form 3115 or another correction procedure is appropriate?'),('Entity and owner returns','Who prepares each return, signs it and delivers the relevant schedules or K-1s?'),('After filing','Who preserves the supporting records and handles separately scoped follow-up or examination work?')],
 example='Hypothetical comparison: Provider A gives a study to your existing CPA; Provider B offers a study and separately priced preparation. Either can be workable if responsibilities are clear. Compare the exact handoff, deadlines and combined fee before assuming that integrated marketing means an all-inclusive service.',
 stories=[12,15,21],resources=[('/form-3115-cost-segregation-lookback/','Form 3115 and existing-property review'),('/cost-segregation-study-cost-pricing/','Study scope and pricing')],sources=[DEPRECIATION,METHOD],
 faqs=[('Does filing support mean the provider prepares my tax return?','Not necessarily. It may mean preparer coordination or schedule assistance. Ask whether actual entity and personal return preparation is included, who signs the returns and what separate fees apply.'),('Can I use a study company and my existing CPA?','Yes, if the scope and handoff are coordinated. Confirm who reconciles basis and prior depreciation, evaluates correction procedures and incorporates the final report into the appropriate returns.')]),
dict(key='missed-depreciation',path='/compare/best-tax-advisors-form-3115-catch-up-depreciation/',title='Tax Advisors for Missed Depreciation & Form 3115 | AE Tax',h1='Best Tax Advisors for Missed Depreciation and Form 3115',desc='Compare advisors for missed depreciation and Form 3115 by prior-year review, correction procedure, study coordination, return integration and records.',
 lead='A tax advisor for missed depreciation should review the actual filed-return history before quoting a catch-up deduction or refund. Form 3115 is a method-change procedure, not a universal fix for every omitted asset or incorrect return. Compare the diagnostic review, proposed correction route and filing responsibilities.',
 heading='Compare the diagnostic work before the correction quote',
 rows=[('Filed-return history','Who confirms what was filed, which assets were used and how depreciation was reported?'),('Asset and basis records','Who reconciles closing costs, land, conversion dates, improvements and prior deductions?'),('Procedure selection','Who explains the applicable method-change or amendment route and filing requirements?'),('Adjustment calculation','Who documents the starting schedules and the effect of the proposed correction?'),('Owner-level effect','Who reviews carryforwards and applicable limitations before treating a deduction as an immediate tax benefit?')],
 example='Hypothetical comparison: one owner has an existing depreciation method requiring review; another has an omitted asset on a draft that was never filed. Those records do not support the same correction project. Ask the advisor to identify the filed-return facts and procedure before buying a form service.',
 stories=[10,24,12],resources=[('/form-3115-cost-segregation-lookback/','Existing-property depreciation review'),('/amended-tax-returns/','Amended return services')],sources=[METHOD,DEPRECIATION,PASSIVE],
 faqs=[('Does every missed depreciation issue require Form 3115?','No. The appropriate correction depends on the facts, filed-return history and applicable procedures. Ask the professional to explain why the proposed method-change or amendment route applies.'),('What should I gather before hiring a Form 3115 advisor?','Gather filed returns and acceptance evidence, complete depreciation schedules, closing documents, asset invoices, conversion and placed-in-service records, prior studies and loss carryforward worksheets.')]),
dict(key='planning-fees',path='/compare/tax-planning-fees-one-time-vs-annual/',title='Tax Planning Firm Fees: One-Time vs Annual | AE Tax',h1='Tax Planning Firm Fees: One-Time Engagement vs Annual Retainer',desc='Compare tax planning firm pricing using first-year and ongoing fees, implementation scope, return costs, renewals and documented deliverables.',
 lead='Tax planning firm pricing is easiest to compare when every quote uses the same deliverables and time period. A one-time advisory engagement and an annual retainer can buy different work. Separate the initial plan from implementation, future updates, return preparation and studies before comparing totals.',
 heading='Build a complete first-year and continuing-service comparison',
 rows=[('Initial advisory','What analysis and written deliverables are included in the quoted planning fee?'),('Implementation','Which elections, payroll changes, administrator coordination and legal work cost extra?'),('Studies and filings','Are property studies, entity returns, household returns and amendments separately billed?'),('Future support','What follow-up is included, for how long, and when is new work separately scoped?'),('Renewal and exit','Is renewal required, what changes at renewal, and what records are delivered when the engagement ends?')],
 example='Hypothetical quote comparison: a $5,000 plan plus $3,000 of separately required work costs $8,000 in the first year. A $7,000 package covering those same tasks costs $7,000. Compare included tasks and required future fees before deciding from the headline price. These numbers are examples, not competitor prices.',
 stories=[27,17,18],resources=[('/pricing/','AE service prices and exclusions'),('/tools/tax-advisor-engagement-scorecard/','Advisor engagement scorecard')],sources=[],
 faqs=[('Is a one-time tax planning fee always cheaper than a retainer?','No. Compare the same deliverables and time period, including implementation, studies, preparation and future updates. A lower initial fee can cover less work; recurring fees may fund services you actually need.'),('How should I compare tax advisory return on cost?','Ask for the baseline, assumptions, implementation costs and timing. Separate deductions, deferred tax and permanent savings. A projected benefit should not be presented as a completed result, and the investment should still fit your cash flow.')]),
dict(key='ae-cost',path='/pricing/',title='AE Tax Advisors Cost, Fees & Service Pricing',h1=None,desc='Review AE Tax Advisors costs for advisory, cost segregation, returns and amendments. Compare included services, separate fees and written engagement scope.',
 lead='If you are comparing AE Tax Advisors cost with another firm, begin with the written scope. The standard $7,800 advisory engagement is paid in two $3,900 installments 30 days apart, with no required annual planning renewal. Returns, amendments, cost segregation and additional services are separately scoped and priced; the engagement is not unlimited lifetime planning.',
 heading='Is AE Tax Advisors worth the cost for your situation?',
 rows=[('Coordinated decisions','Do you need business, property and household analysis together, or only a straightforward return?'),('Documents available','Can you supply the returns, books, ownership records and property information needed for the work?'),('Actionable deliverables','Does the proposal identify a written plan, implementation assignments and deadlines?'),('Complete project cost','Have you added required study, preparation, amendment, legal and administrator fees?'),('Economic benefit','Are baseline, cash requirements and uncertain assumptions clear before you act?')],
 example='A useful value assessment begins with the complexity of the decisions and the deliverables you need. If the issue is limited to preparation, ask whether a preparation-only scope is suitable. If several decisions interact, compare a coordinated advisory proposal with the total cost of having those workstreams handled separately.',
 stories=[27,4,19],resources=[('/ae-tax-advisors-reviews/','AE Tax Advisors reviews and case studies'),('/compare/tax-planning-fees-one-time-vs-annual/','One-time fees and annual retainers')],sources=[],
 faqs=[('What does AE Tax Advisors cost for a complete project?','The total depends on the written engagement and required services. The standard advisory engagement is $7,800; returns, amendments, cost segregation and additional work have separate scope and prices. Ask for a combined quote for your actual project.'),('Does paying for advisory guarantee tax savings?','No. Value depends on the decisions, facts, records and implementation. Proposed benefits are estimates; review the baseline, limitations, fees and cash commitments before relying on a projection.')]),
dict(key='ae-reviews',path='/ae-tax-advisors-reviews/',title='AE Tax Advisors Reviews & Case Studies | Official Site',h1=None,desc='Read AE Tax Advisors reviews information, explore 28 anonymized planning stories, and compare advisory scope, fees and next steps before booking a call.',
 lead='AE Tax Advisors reviews are most useful when you connect the feedback to the service purchased. Compare independent customer experiences with the scope you need, then use the anonymized planning stories to understand the questions AE has documented. These editorial stories do not establish a customer rating or a typical savings result.',
 heading='Review the evidence behind a tax advisory claim',
 rows=[('Customer feedback','Is there a review source, date and description of the actual engagement?'),('Planning story','Does the page explain the documented starting point and work?'),('Status','Does the record show a proposal, contracted scope, completed review or filed outcome?'),('Financial result','Is the number a deduction, tax deferral, estimate or reconciled saving?'),('Fit and cost','Does the same type of work appear in your written proposal, with fees and exclusions?')],
 example='A client’s positive communication experience and a technical planning story answer different questions. Use reviews to assess the experience described; use documented work to assess process and relevance. Before hiring, verify the responsible professional and obtain the complete scope and cost in writing.',
 stories=[],resources=[('/bios/','Meet the AE advisory team'),('/pricing/','AE Tax Advisors cost and scope')],sources=[],
 faqs=[('Where can I evaluate AE Tax Advisors reviews and costs together?','Use the third-party profile linked on this page for available customer feedback, read the anonymized planning stories and review the pricing page. Confirm your complete scope and total cost in a written engagement.'),('Are AE’s planning stories independent customer reviews?','No. AE writes these anonymized summaries from planning or engagement records. Each identifies what the available source establishes; they are distinct from customer quotations, ratings and independently verified outcomes.')]),
]

def block(g):
 body=T.section('Choose the Right Scope for Your Situation','<p>'+T.esc(g['lead'])+'</p>')
 rows=''.join('<tr><th scope="row">'+T.esc(a)+'</th><td>'+T.esc(b)+'</td></tr>' for a,b in g['rows'])
 body+=T.section(g['heading'],'<div class="buyer-table-wrap"><table class="buyer-evidence-table"><caption>Questions to compare before hiring</caption><thead><tr><th scope="col">Decision</th><th scope="col">Ask the provider</th></tr></thead><tbody>'+rows+'</tbody></table></div><h3>A Practical Comparison</h3><p>'+T.esc(g['example'])+'</p>')
 if g['stories']:
  cards=''
  for index in g['stories']:
   s=STORIES[index];cards+='<article class="buyer-story"><span>'+T.esc(s['kind'])+'</span><h3><a href="/case-studies/'+s['slug']+'/">'+T.esc(s['title'])+'</a></h3><p>'+T.esc(s['value'])+'</p><p>'+T.esc(s['status'])+'</p></article>'
  body+=T.section('Relevant Documented AE Planning Stories','<p>These anonymized editorial summaries show the documented work and its status. They are not client quotations or promises of a future outcome.</p><div class="buyer-story-grid">'+cards+'</div>')
 download='/downloads/'+g['key']+'-provider-comparison.csv'
 body+=T.section('Take These Questions to Your Discovery Call','<p>Download the comparison worksheet, send the same questions to each firm and record the answer in writing. Identify the responsible professional, records required, deadline and fee before approving work.</p><p><a class="btn-secondary" href="'+download+'" download>Download the comparison worksheet (CSV)</a></p><ul>'+''.join('<li><a href="'+a+'">'+T.esc(b)+'</a></li>' for a,b in g['resources'])+'</ul><p><a href="/discovery/">Discuss your records and scope with AE</a></p>')
 body+=T.faq_section([(q,'<p>'+T.esc(a)+'</p>') for q,a in g['faqs']],heading='Questions About This Engagement')
 if g['sources']:
  body+=T.section('Technical Background for the Questions','<p>These sources explain why the underlying records matter. The applicable procedure and treatment must be evaluated for the relevant tax year and facts.</p><ul>'+''.join('<li><a href="'+u+'">'+T.esc(t)+'</a></li>' for t,u in g['sources'])+'</ul>')
 if g['path'].startswith('/compare/'):
  body+='<p class="buyer-publisher-note">AE Tax Advisors publishes this guide and offers services discussed here. “Best” refers to engagement fit; this page does not establish an independent award or measured superiority.</p>'
 buf=io.StringIO();w=csv.writer(buf);w.writerow(['Decision','Question','Provider name','Written response','Responsible professional','Records needed','Delivery date','Included or separate fee','Unresolved facts'])
 for a,b in g['rows']:w.writerow([a,b,'','','','','','',''])
 (ROOT/download.lstrip('/')).write_text(buf.getvalue())
 return '<!-- buyer-evidence-'+g['key']+' -->\n'+body+'\n<!-- /buyer-evidence-'+g['key']+' -->'

STYLE='''<style id="buyer-evidence-style">.buyer-table-wrap{overflow-x:auto}.buyer-evidence-table{width:100%;border-collapse:collapse;line-height:1.6}.buyer-evidence-table caption{text-align:left;margin-bottom:12px}.buyer-evidence-table th,.buyer-evidence-table td{text-align:left;vertical-align:top;padding:14px;border-bottom:1px solid #ddd}.buyer-evidence-table th:first-child{width:28%}.buyer-story-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}.buyer-story{padding:22px;border:1px solid #ded7c9;border-radius:12px;background:#fff}.buyer-story h3{font-size:21px;line-height:1.4}.buyer-story span{font-size:13px;color:#665126}.buyer-publisher-note{max-width:840px;margin:24px auto;padding:0 24px;font-size:14px}@media(max-width:760px){.buyer-story-grid{grid-template-columns:1fr}.buyer-evidence-table th,.buyer-evidence-table td{padding:10px;overflow-wrap:anywhere}}</style>'''

def enhance(g):
 p=ROOT/g['path'].strip('/')/'index.html';s=p.read_text();body=block(g)
 marker=r'<!-- buyer-evidence-'+g['key']+r' -->.*?<!-- /buyer-evidence-'+g['key']+r' -->'
 if re.search(marker,s,re.S):s=re.sub(marker,lambda m:body,s,flags=re.S)
 else:
  main=s.index('<main');match=re.search(r'<section class="content-section',s[main:]);pos=main+match.start();s=s[:pos]+body+'\n'+s[pos:]
 s=re.sub('<title>.*?</title>','<title>'+T.esc(g['title'])+'</title>',s,count=1)
 for key,value in [('description',g['desc']),('og:description',g['desc']),('twitter:description',g['desc']),('og:title',g['title']),('twitter:title',g['title'])]:
  s=re.sub(r'(<meta (?:name|property)="'+key+r'" content=")[^"]*(")',lambda m:m[1]+T.esc(value)+m[2],s)
 if g['h1']:s=re.sub(r'<h1>.*?</h1>','<h1>'+T.esc(g['h1'])+'</h1>',s,count=1)
 s=re.sub(r'(<meta property="article:modified_time" content=")[^"]+',lambda m:m[1]+'2026-10-01T00:00:00-04:00',s)
 if 'id="buyer-evidence-style"' not in s:s=s.replace('</head>',STYLE+'\n</head>')
 # Keep one FAQPage and preserve existing unique fee and service questions.
 pattern=r'<script type="application/ld\+json">\s*(.*?)\s*</script>'
 matches=list(re.finditer(pattern,s,re.S));faqs=[]
 for m in matches:
  d=json.loads(m[1])
  if d.get('@type')=='FAQPage':faqs.extend(d.get('mainEntity',[]))
 for q,a in g['faqs']:faqs.append({'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}})
 seen=set();faqs=[q for q in faqs if not(q['name'] in seen or seen.add(q['name']))]
 for m in reversed(matches):
  d=json.loads(m[1]);typ=d.get('@type')
  if typ=='FAQPage':replacement=''
  else:
   if typ in ('Article','CollectionPage','WebPage'):
    d['description']=g['desc'];d['dateModified']='2026-10-01'
    if 'headline' in d:d['headline']=g['title']
    if 'name' in d:d['name']=g['title']
   replacement=T.jsonld(d)
  s=s[:m.start()]+replacement+s[m.end():]
 s=s.replace('</head>',T.jsonld({'@context':'https://schema.org','@type':'FAQPage','mainEntity':faqs})+'\n</head>')
 p.write_text(s)

def linking():
 groups={
 'short-term-rental-tax-strategy':[0,1,6],
 'cost-segregation-study':[1,6,7],
 'business-owner-small-business-tax':[2,3,8],
 's-corp-tax-strategy':[3,2,8],
 'rental-property-tax-planning':[4,2,7],
 'physician-tax-planning':[5,2,8],
 'form-3115-cost-segregation-lookback':[7,6,1],
 'compare':[0,1,2,3,4,5,6,7,8,9,10],
 }
 for path,indexes in groups.items():
  p=ROOT/path/'index.html';s=p.read_text();body='<!-- buyer-guide-paths -->'+T.section('Compare the Advisor and Scope for Your Next Decision','<ul>'+''.join('<li><a href="'+GUIDES[i]['path']+'">'+T.esc(GUIDES[i]['title'].replace(' | AE Tax',''))+'</a></li>' for i in indexes)+'</ul>')+'<!-- /buyer-guide-paths -->'
  if '<!-- buyer-guide-paths -->' in s:s=re.sub(r'<!-- buyer-guide-paths -->.*?<!-- /buyer-guide-paths -->',lambda m:body,s,flags=re.S)
  else:s=s.replace('</main>',body+'\n</main>',1)
  p.write_text(s)

def main():
 for g in GUIDES:enhance(g)
 linking()
 manifest={'updated':'2026-10-01','guides':[{'path':g['path'],'keyword':g['h1'] or g['title'],'worksheet':'/downloads/'+g['key']+'-provider-comparison.csv'} for g in GUIDES]}
 (ROOT/'scripts/buyer_guide_manifest_20261001.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print('Enhanced',len(GUIDES),'existing buyer pages; added',len(GUIDES),'comparison worksheets and eight contextual-link sections.')
if __name__=='__main__':main()
