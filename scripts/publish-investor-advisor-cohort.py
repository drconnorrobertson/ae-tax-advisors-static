#!/usr/bin/env python3
"""Publish the researched November investor-advisor cohort without legacy regeneration."""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import site_template as T

DATE = '2026-11-23'
COHORT = 'investor-advisors-20261123'
DATA = ROOT / 'content' / COHORT
HUB = '/compare/real-estate-business-tax-advisors/'
E = html.escape

def load(path):
    return json.loads((ROOT / path).read_text())

def write(path, value):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def link(url, label):
    return '<a href="' + E(url, quote=True) + '">' + E(label) + '</a>'

def para(text):
    return '<p>' + E(text) + '</p>'

# Facts are limited to the linked providers' own service descriptions. No inferred
# price, missing-capability assertion, customer rating or savings guarantee is used.
rows = [
    dict(slug='tax-strategy-365', name='Tax Strategy 365', source='https://taxstrategy365.com/services/',
         profile='Ryan Bakke and Tax Strategy 365 are relevant searches for investors comparing portfolio tax planning. The service page organizes its work around acquisition, ongoing ownership and exit decisions.',
         fit='Real estate portfolio planning across acquisitions, ongoing ownership and exits.',
         summary='Portfolio lifecycle planning, including entity choices, depreciation timing, participation documentation and sale planning.',
         keep='Keep Tax Strategy 365 on the shortlist when you want an investor-focused plan that connects a new purchase with existing properties and an eventual exit. Its public service page describes cost segregation, short-term rentals, real estate professional qualification and exchanges.',
         boundary='Have the firm identify which analysis, documentation, study work and filings it will actually perform for your portfolio.',
         scenario='An owner has an operating business, several rentals and a replacement-property purchase coming up. A useful proposal should address the existing depreciation schedules and timing of the next transaction before recommending another study.',
         decision='Compare the acquisition-to-exit work plan with AE’s coordinated business and rental planning scope. Ask who reconciles the exchange basis, checks whether losses can be used and supplies the final reporting instructions.',
         questions=['Will the proposal cover existing properties, the next acquisition and the planned exit in one projection?', 'Who verifies participation evidence and reconciles the study to the depreciation ledger?', 'Which studies, exchange-adviser services and returns require separate engagements?'],
         costs=[('Portfolio review', 'List each existing property and proposed transaction included in the engagement.'), ('Property analysis', 'Separate eligibility analysis, study preparation and depreciation implementation.'), ('Exit coordination', 'Confirm work with the qualified intermediary and return preparer, and any extra fee.')],
         peers=['the-cpa-realtor','landmark-cpa-group'], case='1031-replacement-rental-cost-seg-basis-review'),
    dict(slug='the-cpa-realtor', name='The CPA Realtor', source='https://www.thecparealtor.co/pricing',
         profile='The CPA Realtor publishes two first-year packages and separate business-return prices. That makes package scope, rather than a single advertised savings example, the useful starting point for comparison.',
         fit='Investors seeking a personal-return package with real estate planning and a defined year of support.',
         summary='Signature and Elite fixed-fee packages with personal filing, planning and 12 months of support; separate business-return pricing.',
         keep='Consider The CPA Realtor when personal return preparation and rental strategy belong in the same engagement. Its pricing page distinguishes a limited strategy-session allowance in Signature from broader access in Elite.',
         boundary='The provider states that bookkeeping, entity setup and cost segregation studies are usually separate. Confirm the exact entities, study work and support included in your proposal.',
         scenario='A W-2 household has an existing short-term rental and an S corporation. One proposal bundles personal filing with planning; another prices advisory and returns separately. Comparing only the planning line would hide a material scope difference.',
         decision='Price the personal return, S-corporation return, strategy sessions and any study under both proposals. Choose according to the actual work and access needed, rather than assuming AE’s advisory price and a filing package buy the same services.',
         questions=['Does Signature or Elite cover the decisions, meeting time and entities in our situation?', 'Which returns, bookkeeping tasks and property studies are priced separately?', 'What will renewal cost after the first-year review, and when does support end?'],
         costs=[('Signature', 'Published first-year range: $3,000 to $7,000. Verify the included personal return and planning scope.'), ('Elite', 'Published first-year range: $5,000 to $9,000. Verify access and support terms.'), ('Business returns', 'Published range: $1,500 to $2,500 per return, quoted after review.'), ('Outside work', 'Confirm bookkeeping, entity setup, studies and the returning-client quote separately.')],
         fee='The CPA Realtor publishes Signature at $3,000 to $7,000 and Elite at $5,000 to $9,000 for the first year. Business returns are listed separately at $1,500 to $2,500 per return.',
         fee_context='Both packages describe 12 months of support and include personal return preparation. Returning-client pricing can differ. These package ranges are not planning-only prices or a quote for every taxpayer.',
         filing_answer='Personal federal and state returns are described within the packages. Separately filed business returns have their own published range; confirm your entities and any study, bookkeeping or setup work.',
         peers=['tax-strategy-365','pocket-cpa'], case='catch-up-returns-rental-planning-sequence'),
    dict(slug='the-investors-accountant', name='The Investors Accountant', source='https://theinvestorsaccountant.com/',
         extra_sources=[('https://theinvestorsaccountant.com/service-pricing/','Service-pricing page; confirm current availability')],
         profile='The Investors Accountant is associated with Roger Herring and Investors Accounting. Its current homepage addresses real estate investors, business owners and high-income professionals. The business identity matters when checking older pricing references.',
         fit='Investors comparing proactive planning with an ongoing tax preparation relationship.',
         summary='Investor-focused tax strategy and accounting, with pricing discussed after the firm understands the client situation.',
         keep='Keep The Investors Accountant on the list if your priority is an investor-focused adviser with preparation and planning needs to discuss together. Its public website covers rental-property strategy, entity decisions and transaction planning.',
         boundary='The current homepage says pricing depends on the situation and is discussed on the call. Search results may retain older consultation or compliance program figures; obtain a current written proposal rather than treating those snippets as a live quote.',
         scenario='A rental owner has unfinished prior-year returns, partnership activity and a proposed property study. The first buying decision is whether one team can sequence the missing filings and property records before offering a forward-looking plan.',
         decision='Ask The Investors Accountant and AE to identify which years and entities are covered, what can begin before records are reconciled and who checks completion. Compare a full compliance-and-planning quote with the same AE scope.',
         questions=['Which prior years, entities and ongoing planning meetings are included in the current proposal?', 'Does any initial consultation fee reduce the cost of later work?', 'Who reconciles missing depreciation schedules and confirms filing acceptance?'],
         costs=[('Initial analysis', 'Confirm the current consultation or planning deliverable and whether later work is optional.'), ('Compliance', 'Identify each return, included time and any extra-time rate in the written quote.'), ('Ongoing planning', 'Price the meeting cadence, implementation support and renewal terms separately.')],
         peers=['the-cpa-realtor','tra-cpa'], case='catch-up-returns-rental-planning-sequence'),
    dict(slug='landmark-cpa-group', name='Landmark CPA Group', source='https://landmarkcpagroup.com/who-we-help/',
         profile='This guide concerns Ted Lanzaro’s Landmark CPA Group at landmarkcpagroup.com. It does not describe other firms using Landmark in their name.',
         fit='Real estate investors and entrepreneurial owners seeking tax strategy connected to a broader financial picture.',
         summary='Proactive planning for rental portfolios, operating businesses and owners integrating business income with real estate.',
         keep='Consider Landmark CPA Group when a portfolio and an operating business need to be evaluated together. Its who-we-help page explicitly addresses real estate investors and entrepreneurial owners, including people combining both.',
         boundary='Ask which financial-coordination and tax deliverables are provided by the CPA engagement and which require another adviser or agreement.',
         scenario='A business owner plans to direct operating profits into rentals while keeping working capital available for the business. The adviser must reconcile the household projection with the business cash forecast before selecting the next planning step.',
         decision='Compare Landmark’s proposed framework with AE’s task-by-task planning engagement. Ask both firms to show the baseline, cash commitment, implementation owner and follow-up date for each recommendation.',
         questions=['How will operating income, existing rentals and the next property purchase be modeled together?', 'Which financial or legal advisers participate, and who pays each of them?', 'What written priorities and implementation assignments will we receive?'],
         costs=[('Integrated review', 'Confirm which businesses, rental activities and household income streams are modeled.'), ('Coordination', 'Identify any separately engaged investment, legal or insurance professional.'), ('Follow-through', 'Specify who updates projections and checks implementation, and the fee for future years.')],
         peers=['tax-strategy-365','savage-tax-advisory'], case='trade-business-owner-rental-retirement-coordination'),
    dict(slug='madsen-and-company', name='Madsen and Company', source='https://www.madsencpa.com/tax-planning/',
         extra_sources=[('https://www.madsencpa.com/real-estate-tax-planning/','Real estate tax planning')],
         profile='Steve Madsen’s firm describes planning paths for S corporations, real estate investors and business owners. Buyers should identify which path and which ongoing services their proposal covers.',
         fit='S-corporation owners and rental investors comparing year-round planning with their accounting needs.',
         summary='Year-round business-owner tax planning, with separate service paths for S corporations and real estate.',
         keep='Keep Madsen and Company in consideration when payroll, distributions and rental decisions are connected. Its service page discusses S-corporation planning and directs real estate investors to a dedicated planning path.',
         boundary='A website discussion of compensation or deductions is not an engagement to operate payroll or implement every recommendation. Assign those responsibilities in writing.',
         scenario='An S-corporation owner also owns a rental and wants to adjust compensation and fund retirement without running short of business cash. A matched proposal must use the same payroll records, profit forecast and property assumptions.',
         decision='Evaluate the proposed compensation review, retirement coordination and rental-loss analysis together. AE’s scope can be compared against a complete Madsen proposal without assuming either firm includes payroll or annual filing in its advisory fee.',
         questions=['Who reviews compensation, runs payroll changes and verifies implementation?', 'Will the projection include rental limitations and retirement funding together?', 'Are bookkeeping, returns and scheduled projection updates included or separate?'],
         costs=[('Planning', 'Specify compensation review, projection frequency and the written action plan.'), ('Accounting and payroll', 'Price actual bookkeeping and payroll operations separately from advice.'), ('Return implementation', 'Identify business, personal and state returns and any additional charge.')],
         peers=['pocket-cpa','tarantino-cpa'], case='trade-business-owner-rental-retirement-coordination'),
    dict(slug='savage-tax-advisory', name='Savage Tax Advisory', source='https://savagetaxadvisory.com/faq/',
         extra_sources=[('https://savagetaxadvisory.com/','Advisory model and client fit')],
         profile='Alex Savage’s practice describes advisory for high earners and business owners with real estate. Its FAQ separates advisory pricing from preparation and explains the first-month roadmap.',
         fit='Owners wanting an ongoing advisory relationship connecting business, properties and retirement.',
         summary='Year-round advisory with a first-month written roadmap; preparation is separately billed for ongoing advisory clients.',
         keep='Consider Savage when recurring access and an evolving plan matter to you. Its FAQ describes two initial strategy calls and a written roadmap, followed by review through the year.',
         boundary='The FAQ says return preparation is available only to ongoing advisory clients and is billed separately. Confirm the quoted access level, future-year advisory fee and return complexity.',
         scenario='An owner with wages, business income and rentals wants a standing adviser through retirement funding and property decisions. A recurring relationship and a defined project can produce very different second-year costs even when both begin with a written plan.',
         decision='Compare the expected advisory access over two years, then add return preparation and other implementation. AE has no required standard annual planning renewal, but that does not buy unlimited future planning or replace a recurring service agreement.',
         questions=['What access and review cadence does the quoted annual advisory fee include?', 'How is the next year’s advisory price set and when can the engagement end?', 'What are the separately quoted preparation fees for our personal and business returns?'],
         costs=[('First-year advisory', 'Published range: $6,500 to $25,000, depending on complexity.'), ('Later-year advisory', 'The FAQ says fees are usually similar, with changes for situation or access level.'), ('Preparation', 'Published starting prices: $1,500 individual and $2,000 business; ongoing advisory clients only.')],
         fee='Savage Tax Advisory publishes first-year advisory fees of $6,500 to $25,000. Its FAQ lists separately billed return preparation starting at $1,500 for individuals and $2,000 for businesses.',
         fee_context='The FAQ says later-year advisory is usually similar, adjusted for changed circumstances or access. Preparation is available to ongoing advisory clients. Starting preparation prices and an advisory range do not establish your total.',
         filing_answer='The FAQ states that preparation is separately billed and offered only to ongoing advisory clients. Obtain a quote for each return and confirm whether amendments or study implementation are additional.',
         peers=['landmark-cpa-group','andrew-kabatchnick-cpa'], case='trade-business-owner-rental-retirement-coordination'),
    dict(slug='andrew-kabatchnick-cpa', name='Andrew Kabatchnick CPA', source='https://andrew-cpa.com/',
         profile='Andrew Kabatchnick’s official website identifies tax planning and wealth management in New Jersey. The homepage requires client-side rendering, so this guide intentionally limits the service comparison to that confirmed identity and asks for a current proposal.',
         fit='Buyers evaluating whether they need tax advice alongside a wealth-management relationship.',
         summary='Tax planning and wealth-management positioning; confirm the legal entities, current services and financial-advisory terms directly.',
         keep='Evaluate Andrew Kabatchnick CPA if the question is how tax planning will coordinate with investment decisions. Ask the provider to identify the professional and legal entity responsible for each service before comparing fees.',
         boundary='This review does not establish an assets-under-management requirement, investment minimum, registration status or bundled preparation service. Do not infer those terms from wealth-management wording alone.',
         scenario='A high-income household wants tax advice on investment gains while retaining its current portfolio manager. The key purchase question is whether tax planning can be engaged separately and how information will flow between advisers.',
         decision='Request a tax-only proposal and, if relevant, a separate investment-advisory proposal. Compare AE’s tax scope with the tax component. Evaluate any investment fee, custody arrangement or transfer requirement on its own terms.',
         questions=['Can we engage tax planning while retaining our existing portfolio manager?', 'Which entity supplies each service, and how is each professional compensated?', 'What filings, investment implementation and future reviews are included in the proposed agreement?'],
         costs=[('Tax scope', 'Request a written tax-planning fee and defined deliverables.'), ('Wealth relationship', 'If proposed, obtain the separate advisory fee schedule and any account minimum or transfer condition.'), ('Preparation and support', 'Confirm whether returns, implementation and future reviews require separate agreements.')],
         peers=['savage-tax-advisory','executive-tax-strategy'], case='trade-business-owner-rental-retirement-coordination'),
    dict(slug='tarantino-cpa', name='Tarantino CPA', source='https://tarantino-cpa.com/services',
         profile='This guide concerns Charles “CJ” Tarantino and Nicole Tarantino’s firm at tarantino-cpa.com. Its services page lists planning, preparation and accounting for real estate investors and high-income professionals.',
         fit='Investors and business owners comparing an accounting relationship with strategic planning.',
         summary='Strategic planning, tax projections, entity analysis, preparation, accounting and bookkeeping.',
         keep='Consider Tarantino CPA when you want to discuss planning and recurring accounting together. Its menu includes tax preparation and bookkeeping alongside advisory, rather than describing only a one-time strategy session.',
         boundary='Multiple services appearing on the same page does not establish that they share one fee. Request the price, responsible team and service calendar for each line of work.',
         scenario='An owner’s rental books are behind while a business is generating a larger profit. The choice of adviser depends partly on whether the proposal includes accounting cleanup before the projection and planning work.',
         decision='Compare the monthly accounting workload, planning milestones and return calendar with an AE proposal using the same starting records. A planning-only price should not be treated as the cost of replacing a full accounting team.',
         questions=['Will accounting cleanup happen before the projection, and who signs off on the balances?', 'How often are books reviewed and tax projections updated?', 'Are personal returns, entity returns and implementation charged separately?'],
         costs=[('Accounting', 'Price cleanup, recurring bookkeeping and financial reporting by entity.'), ('Advisory', 'Confirm projection frequency, meetings and the written implementation plan.'), ('Preparation', 'Separate personal, business and state filing charges and any amendment work.')],
         peers=['madsen-and-company','pocket-cpa'], case='catch-up-returns-rental-planning-sequence'),
    dict(slug='executive-tax-strategy', name='Executive Tax Strategy', source='https://executivetaxstrategy.com/',
         profile='Executive Tax Strategy markets proactive tax planning to operators, investors and high-income professionals. When evaluating a proposed strategy, the useful evidence is its written analysis and implementation scope, rather than a headline savings claim.',
         fit='High-income buyers comparing a proposed tax-planning engagement and its implementation dependencies.',
         summary='Tax strategy positioned toward business owners, investors and high earners; scope and fees require a current proposal.',
         keep='Keep Executive Tax Strategy on the list when its written proposal addresses your income mix, transaction and timeline. Ask the firm to show which decisions depend on another professional, a separate investment or additional documentation.',
         boundary='Marketing language about tax strategies does not establish IRS approval of a particular transaction, the buyer’s eligibility or a guaranteed benefit. Obtain the specific analysis for your facts.',
         scenario='An owner receives a proposal tied to a large year-end income event. Before signing, the owner needs a comparison of the baseline tax result, cash committed, legal work and filing obligations under each proposed approach.',
         decision='Ask Executive Tax Strategy and AE to state the assumptions, alternatives, implementation fees and risks of the same decision. Separate the adviser’s fee from any capital commitment or third-party product expense.',
         questions=['What is the baseline and what facts must be verified before recommending the strategy?', 'Does the plan require a separate investment, specialist or legal engagement?', 'Who implements each step, prepares the reporting and answers follow-up questions?'],
         costs=[('Advisory', 'Request the current planning fee and the written deliverables.'), ('Implementation', 'Itemize legal, specialist and return costs, and any required investment separately.'), ('Future obligations', 'Identify ongoing payments, compliance tasks, exit conditions and support fees.')],
         peers=['andrew-kabatchnick-cpa','kkos-lawyers'], case='trade-business-owner-rental-retirement-coordination'),
    dict(slug='tra-cpa', name='TRA CPA LLC', source='https://tracpallc.com/Tax-Advisory.html',
         extra_sources=[('https://tracpallc.com/Real-Estate-Accounting.html','Real estate accounting')],
         profile='TRA CPA LLC describes a remote practice serving business clients nationwide. Its advisory page addresses individuals, real estate investors, medical practices and home-care businesses.',
         fit='Remote business owners and investors comparing advisory with specialized accounting needs.',
         summary='Remote tax advisory addressing business and household goals, with a separate real estate accounting service page.',
         keep='Evaluate TRA CPA when your records and accounting needs require a remote working process. Ask how its proposed advisory relates to the bookkeeping, property accounting and returns you need completed.',
         boundary='Confirm who handles each industry-specific accounting task and state return. Nationwide positioning does not establish that every engagement covers every state or every service.',
         scenario='A medical-practice owner has a rental investment, several entities and records maintained by different bookkeepers. The proposed adviser must identify which balances can support a projection and what needs reconciliation first.',
         decision='Compare TRA CPA’s remote workflow with AE’s ownership and rental review. Use the same entity and state list, a secure document process and a written handoff between the accountant and the professional implementing the plan.',
         questions=['Which entities, states and industry accounting tasks are in the proposal?', 'How are financials reconciled before planning and who resolves missing records?', 'Who prepares the returns and checks implementation against the final projection?'],
         costs=[('Remote onboarding', 'Identify record conversion, cleanup and secure intake costs.'), ('Industry accounting', 'Price the practice or rental accounting work by entity and reporting frequency.'), ('Advisory and returns', 'Separate planning, state filings and implementation responsibilities.')],
         peers=['the-investors-accountant','tarantino-cpa'], case='catch-up-returns-rental-planning-sequence'),
    dict(slug='pocket-cpa', name='Pocket CPA', source='https://pocketcpas.com/tax-planning-services/',
         profile='Pocket CPA describes a planning-and-preparation model in which the CPA who builds the plan also prepares the returns. Its audience includes business owners, rental investors and high-income households.',
         fit='Buyers who want continuity between the tax plan and the returns that report it.',
         summary='Year-round planning and return preparation, including compensation, estimated payments, income timing and property decisions.',
         keep='Consider Pocket CPA when continuity between advice and preparation is a priority. Its planning page explicitly describes the same CPA building the plan and preparing the returns that reflect it.',
         boundary='That service description is not a quote for unlimited access, all entities or all prior years. Confirm the engagement calendar and what happens when additional work is discovered.',
         scenario='A self-employed owner with a rental wants to stop being surprised by quarterly payments. The adviser needs to reconcile business profit, household withholding and property assumptions, then update the projection when those inputs change.',
         decision='Compare the promised preparation continuity and projection cadence with AE’s separately scoped advisory and filing work. Clarify who recalculates payments and who checks that the return reflects completed recommendations.',
         questions=['Will the same CPA plan and prepare every return included in our engagement?', 'How often is the projection updated when profit, withholding or property plans change?', 'What access, bookkeeping and extra-year work is outside the quoted fee?'],
         costs=[('Planning cadence', 'Price the agreed projection updates and scheduled meetings.'), ('Preparation', 'List every personal, entity and state return and its responsible preparer.'), ('Changes in scope', 'Confirm charges for cleanup, amendments, new entities and additional support.')],
         peers=['madsen-and-company','the-cpa-realtor'], case='trade-business-owner-rental-retirement-coordination'),
    dict(slug='kkos-lawyers', name='KKOS Lawyers', source='https://kkoslawyers.com/services',
         extra_sources=[('https://kkoslawyers.com/pillar/tax-planning','Tax-planning services')],
         profile='KKOS Lawyers is a legal-services option, so the comparison with a tax advisory engagement is only partial. Its menu includes entity work, estate planning, tax consultations and self-directed retirement structures.',
         fit='Owners who need legal entity, estate or retirement-structure work alongside tax planning.',
         summary='Legal and tax-planning service menu covering entity setup, multi-entity planning, estate work and self-directed retirement.',
         keep='Keep KKOS Lawyers on the list when the actual deliverable is a legal document, entity restructuring or estate-planning work. The service menu is broader than tax advisory alone.',
         boundary='A tax adviser and a law firm may have complementary roles. Do not assume an AE advisory engagement replaces legal counsel, or that a KKOS consultation includes ongoing accounting and return preparation.',
         scenario='An owner wants to hold a rental in a new entity and update estate documents while the operating business funds retirement. Before choosing a provider, split the legal drafting from tax modeling, account setup and return reporting.',
         decision='Ask KKOS to scope the legal and consultation work and AE to scope any tax analysis and implementation coordination. You may need both kinds of professional; compare only overlapping work and identify gaps between the agreements.',
         questions=['Which legal documents, filings and consultations are included in this service?', 'Who handles accounting, tax modeling and federal or state return reporting?', 'Are ongoing entity maintenance, retirement administration and future amendments separate?'],
         costs=[('Legal deliverables', 'Identify documents, entity registrations, consultations and state charges.'), ('Tax coordination', 'Separate tax modeling and return implementation from legal drafting.'), ('Ongoing administration', 'Confirm annual entity, account, retirement-plan and amendment costs.')],
         peers=['executive-tax-strategy','landmark-cpa-group'], case='trade-business-owner-rental-retirement-coordination'),
]

providers = {}
for d in rows:
    n = d['name']
    d['sources'] = [(d['source'], 'Official services and fee evidence')] + d.get('extra_sources', [])
    d['alternative_intro'] = d['profile'] + ' Compare alternatives using the work you need completed, your income sources and the person responsible for implementation.'
    d['fee'] = d.get('fee', 'A current written quote is required for ' + n + '. This review did not establish a current universal advisory price from the official pages reviewed.')
    d['fee_context'] = d.get('fee_context', 'A missing public rate is not evidence of a high or low price. Give the firm your entity list, property schedule, required returns and timeline, and request an itemized proposal.')
    d['cost_rows'] = d.pop('costs')
    d['filing_answer'] = d.get('filing_answer', 'Confirm preparation, amendments and implementation in the proposal. A service menu alone does not establish which returns or tasks are included in the quoted advisory fee.')
    d['price_comparison'] = d['decision']
    d['vs_intro'] = d['profile'] + ' ' + d['summary']
    d['ae_question'] = 'Will AE’s written scope cover this decision, the implementation handoff and the support period, with all separately priced work identified?'
    providers[d['slug']] = d

pairs = [
    ['tax-strategy-365','the-cpa-realtor','tax-strategy-365-vs-the-cpa-realtor','A salaried investor is buying a second rental. Compare a portfolio-lifecycle planning proposal with a package that includes personal filing and a year of support. The property schedule, next purchase date and work already completed should be the same in both requests.','Who checks participation evidence, coordinates the study and reports the result, and which of those steps are included?'],
    ['landmark-cpa-group','tax-strategy-365','landmark-cpa-group-vs-tax-strategy-365','A business owner is building a rental portfolio while preparing for a property sale. Both firms describe investor planning; compare the proposed cash forecast, transaction sequence and coordination with the existing business advisers.','How will you connect operating income, acquisition timing and the proposed sale in one written plan?'],
    ['the-investors-accountant','the-cpa-realtor','the-investors-accountant-vs-the-cpa-realtor','An investor needs several returns completed as well as planning for the next rental. Obtain a current Investors Accountant quote and compare it with the applicable CPA Realtor package plus separately priced business returns. Historical search snippets are not current proposals.','Which years, entities and planning meetings are covered, and what happens if the records need reconstruction?'],
    ['madsen-and-company','pocket-cpa','madsen-and-company-vs-pocket-cpa','An S-corporation owner wants coordinated payroll, retirement and rental planning. Madsen describes separate business and real estate planning paths; Pocket CPA emphasizes continuity between planning and preparation. Compare the actual assigned work and the projection-update calendar.','Who updates the household projection after payroll or business profit changes, and who implements the final reporting?'],
    ['savage-tax-advisory','landmark-cpa-group','savage-tax-advisory-vs-landmark-cpa-group','An entrepreneur wants recurring advice on the operating business, rentals and retirement. Savage publishes an advisory range and separate preparation starting fees; Landmark requires a scope-specific proposal in this review. Match the access level and work over two years.','What changes between the first and second year, including price, access and responsibility for implementation?'],
    ['kkos-lawyers','executive-tax-strategy','kkos-lawyers-vs-executive-tax-strategy','A business owner is considering entity changes before a major income event. A law-firm service and a tax-planning engagement can overlap without replacing each other. Separate document drafting, tax modeling, investment commitments and return preparation before comparing cost.','Which professional supplies the legal documents, which supplies the tax analysis and who is responsible for the completed filings?'],
]

config = dict(date=DATE, pairs=pairs, hub_routes=[], marker='investor-advisors-20261123', published=['the-cpa-realtor','savage-tax-advisory'], new_comparisons=len(pairs), refreshed_pair_comparisons=0)
write('content/' + COHORT + '/sources.json', providers)
write('content/' + COHORT + '/cohort.json', config)

# Extend the ownership registry and price inventory together; preserve the original baseline.
manifest = load('content/provider-page-ownership-20261024.json')
owned = {d['slug']: d for d in manifest['providers']}
directory = load('compare/competitor-pricing/prices.json')
vendors = load('content/vendor-pricing-20261024.json')
pricing_file = ROOT / 'compare/competitor-pricing/index.html'
pricing_html = pricing_file.read_text()
for s,d in providers.items():
    owned[s] = dict(slug=s,brand=d['name'],alternative_url=T.SITE+'/compare/'+s+'-alternatives/',comparison_url=T.SITE+'/compare/'+s+'-vs-ae-tax/',pricing_url=T.SITE+'/compare/'+s+'-pricing/',review_url=T.SITE+'/compare/'+s+'-alternatives/#provider-review',review_owner='Provider service profile on dedicated alternatives page',comparison_action='distinct canonical comparison',official_source=d['source'],editorial_date=DATE)
    row = dict(slug=s,name=d['name'],path='/compare/'+s+'-pricing/',category='legal' if s=='kkos-lawyers' else 'strategy',source=d['source'],fee=d['fee'],qualification=d['fee_context'],reviewed=DATE,keywords=[d['name']+' '+k for k in ['pricing','cost','fees']],status='Current quote required',kind='quote')
    for records in (directory['providers'],vendors):
        if not any(x['slug']==s for x in records):
            records.append(row.copy())
    if 'href="/compare/'+s+'-pricing/"' not in pricing_html:
        placeholder='<tr><th scope="row">'+link('/compare/'+s+'-pricing/',d['name']+' pricing')+'</th><td>strategy</td><td>Current quote required</td><td>Review current scope</td></tr>'
        pricing_html=pricing_html.replace('</tbody>',placeholder+'</tbody>',1)
manifest['providers']=list(owned.values())
manifest.update(provider_count=len(owned),page_count=3*len(owned))
write('content/provider-page-ownership-20261024.json',manifest)
write('compare/competitor-pricing/prices.json',directory)
write('content/vendor-pricing-20261024.json',vendors)
pricing_file.write_text(pricing_html)
subprocess.run([sys.executable,str(ROOT/'scripts/refresh-provider-cohort.py'),COHORT],cwd=ROOT,check=True)
pricing_html=pricing_file.read_text()
pricing_html=re.sub(r'\b\d+ (?=Providers|providers|tax, accounting)',str(len(owned))+' ',pricing_html)
pricing_file.write_text(pricing_html)

cases = {
 'trade-business-owner-rental-retirement-coordination': ('A trade business owner coordinates payroll, retirement and rentals','This anonymized planning story describes a coordinated plan covering compensation, reimbursements, retirement and rental depreciation. It identifies recommendations and work in progress, rather than verified final filings or realized savings.'),
 'catch-up-returns-rental-planning-sequence': ('A rental owner sequences catch-up returns and property work','This anonymized engagement story explains why missing personal returns, partnership reporting and a property study need a common sequence. The source confirms engagement scope, not completed work or a realized tax benefit.'),
 '1031-replacement-rental-cost-seg-basis-review': ('A replacement rental needs an exchange-basis review','This educational composite explains the handoff between an exchange adviser, engineer and preparer. It is a planning illustration, not a report of completed client work, verified savings or investment results.'),
}
paths=load('content/'+COHORT+'/pages.json')
for s,d in providers.items():
    title,note=cases[d['case']]
    case_block=T.section('See how this buying decision appears in practice',para(note)+'<p>'+link('/case-studies/'+d['case']+'/',title)+'</p>'+para('Use the example to ask for an implementation sequence and evidence requirements in your own proposal. It does not establish how another firm serves its clients.'))
    for suffix in ('pricing','alternatives','vs-ae-tax'):
        f=ROOT/'compare'/f'{s}-{suffix}'/'index.html'
        text=f.read_text().replace(T.CTA_BLOCK,case_block+T.CTA_BLOCK,1)
        text=text.replace(' — ','; ').replace('—','; ')
        text=text.replace('</main>',T.related_section([(HUB,'Compare real estate and business-owner tax advisory options')])+'</main>',1)
        f.write_text(text)

title='Real Estate and Business Tax Advisors: Compare 12 Options'
desc='Compare 12 tax advisory options for business owners and real estate investors by planning scope, published fees, filing, legal work and implementation.'
trail=[('Home','/'),('Compare firms','/compare/'),('Real estate and business tax advisors',HUB)]
body=T.page_header(h1=title,subtitle=desc,trail=trail)
body+=T.section('Choose the work before choosing the firm',para('A business owner with rental property may need several kinds of help: a household projection, recurring accounting, personal and entity returns, a property study or legal documents. Buying one does not automatically buy the others. This shortlist helps you decide which firms to ask for a matched written proposal.')+para('AE Tax Advisors publishes this commercial guide and competes for advisory work. The options are not ordered by quality, popularity or independent customer scores. Official sources were reviewed November 23, 2026; confirm fees and availability directly.')+'<p>'+link('/compare/competitor-pricing/','Browse the full provider pricing directory')+' · '+link('/compare/tax-advisor-comparison-methodology/','How AE researches comparisons')+'</p>')
body+=T.section('Start with your buying situation','<ul><li>Buying, owning or selling rentals: compare the portfolio analysis and the handoff to the preparer.</li><li>Operating a business and owning real estate: ask for one projection that reconciles payroll, profit, retirement funding and rental assumptions.</li><li>Replacing an accounting team: include bookkeeping, cleanup and filing in both proposals.</li><li>Changing entities or estate documents: identify the attorney and legal deliverables separately.</li><li>Keeping your investment manager: confirm whether tax advice can be engaged on its own.</li></ul>')
for s,d in providers.items():
    guides=' · '.join(link('/compare/'+s+'-'+suffix+'/',label) for suffix,label in [('pricing','Pricing and cost'),('alternatives','Alternatives and service review'),('vs-ae-tax','Compare with AE')])
    body+=T.section(E(d['name']),para(d['profile'])+para('Evaluate it for: '+d['fit'])+para(d['fee'])+'<p>'+guides+'</p><p>'+link(d['source'],'Provider’s official website')+'</p>')
body+=T.section('Compare firms already on your shortlist','<ul>'+''.join('<li>'+link('/compare/'+s+'/',providers[l]['name']+' vs '+providers[r]['name'])+'</li>' for l,r,s,_,_ in pairs)+'</ul>')
body+=T.section('Use AE’s case studies to evaluate the proposed work',para('The examples below identify the work sequence and distinguish documented scope from completed results. Ask shortlisted providers how they would handle a similar decision using your actual records.')+'<ul>'+''.join('<li>'+link('/case-studies/'+s+'/',title)+': '+E(note)+'</li>' for s,(title,note) in cases.items())+'</ul>')
body+=T.section('What an AE proposal should make clear',para('AE’s standard advisory fee is $7,800 and complex advisory is $9,800. Returns, amendments, studies and additional services are separately scoped and priced. The standard engagement has no required recurring annual planning fee; that does not provide unlimited new planning in future years.')+para('Ask for a defined deliverable, support period, implementation assignments, client dependencies and a combined quote for the actual work. A discovery call helps determine fit before detailed analysis begins.')+'<p>'+link('/pricing/','Review AE fees and scope')+' · '+link('/discovery/','Discuss your business and rental planning')+'</p>')
schema=T.article_schema(title=title,description=desc,url=T.SITE+HUB,published=DATE,modified=DATE,section='Tax advisor comparisons',citations=[d['source'] for d in providers.values()]+[T.SITE+'/pricing/'])
items={'@context':'https://schema.org','@type':'ItemList','name':title,'itemListOrder':'https://schema.org/ItemListUnordered','numberOfItems':len(rows),'itemList':[{'@type':'ListItem','position':i+1,'name':d['name'],'url':T.SITE+'/compare/'+s+'-alternatives/'} for i,(s,d) in enumerate(providers.items())]}
f=ROOT/HUB.strip('/')/'index.html';f.parent.mkdir(parents=True,exist_ok=True)
f.write_text(T.build_page(title=title+' | AE Tax Advisors',description=desc,path=HUB,body=body,schemas=[schema,T.breadcrumb_schema(trail),items],published=DATE,modified=DATE,active_nav='/compare/'))
paths.append(HUB)

# Add short contextual discovery sections rather than another long link dump.
discovery={
 '/compare/':('More choices for business owners and rental investors',[(HUB,'Compare 12 real estate and business tax advisory options')]),
 '/compare/competitor-pricing/':('Match pricing to the work you need',[(HUB,'Real estate and business tax advisor shortlist')]),
 '/case-studies/':('Choosing a firm to carry out your plan',[(HUB,'Compare tax advisers by scope, fees and implementation')]),
}
for case in cases:
    associated=[(s,d) for s,d in providers.items() if d['case']==case]
    discovery['/case-studies/'+case+'/']=('Questions to ask when choosing an adviser',[(HUB,'Compare advisory options for this kind of decision')]+[('/compare/'+s+'-vs-ae-tax/',d['name']+' vs AE Tax Advisors') for s,d in associated[:3]])
for path,(heading,links) in discovery.items():
    f=ROOT/path.strip('/')/'index.html';text=f.read_text()
    marker='investor-advisor-discovery-20261123'
    text=re.sub('<!-- '+marker+':start -->.*?<!-- '+marker+':end -->','',text,flags=re.S)
    block='<!-- '+marker+':start -->'+T.section(heading,para('Compare a written plan, implementation responsibilities and the complete fee using the same facts.')+'<ul>'+''.join('<li>'+link(u,l)+'</li>' for u,l in links)+'</ul>')+'<!-- '+marker+':end -->'
    anchor=T.CTA_BLOCK if T.CTA_BLOCK in text else '</main>'
    f.write_text(text.replace(anchor,block+anchor,1))

# Register discovery and meaningful editorial dates without dating unrelated pages.
for sitemap in ('sitemap-comparisons.xml',):
    f=ROOT/sitemap;xml=f.read_text()
    for path in paths:
        if '<loc>'+T.SITE+path+'</loc>' not in xml:
            xml=xml.replace('</urlset>','<url><loc>'+T.SITE+path+'</loc><lastmod>'+DATE+'</lastmod></url>\n</urlset>')
    f.write_text(xml)
dates=load('content/reviewed-content-lastmod.json')
dates.update({path:DATE for path in paths+list(discovery)})
write('content/reviewed-content-lastmod.json',dates)
write('content/'+COHORT+'/pages.json',paths)
for path in paths:
    f=ROOT/path.strip('/')/'index.html'
    text=f.read_text().replace(' — ','; ').replace('—','; ')
    f.write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n')
print(json.dumps(dict(new_pages=len(paths),new_providers=len(providers),pair_comparisons=len(pairs),provider_inventory=len(owned),discovery_pages=len(discovery))))
