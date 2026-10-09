#!/usr/bin/env python3
import json
from pathlib import Path
from build_vendor_shopping_20261008 import build,p,inject,T,DATE,E,manifest
ROOT=Path(__file__).resolve().parent
GUIDES=json.loads((ROOT/'content/vendor-shopping-guides-20261008.json').read_text())
links=[]
for g in GUIDES:
 path='/compare/'+g['slug']+'/'
 if (ROOT/path.strip('/')/'index.html').exists() and '<!-- buyer-guide-20261008 -->' not in (ROOT/path.strip('/')/'index.html').read_text():
  raise RuntimeError('Existing owner needs overlap review: '+path)
 body='<!-- buyer-guide-20261008 -->'+T.section('The buying decision',p(g['answer']))
 for heading,text in g['sections']:body+=T.section(heading,p(text))
 body+=T.section('Apply this to your AE proposal',p('Ask AE to identify the entities, years, deliverables, implementation support, and filing work in your proposed engagement. Review current published fees and confirm exclusions in the agreement. General website content does not establish that a strategy applies to your circumstances.')+'<p><a href="/pricing/">AE pricing and scope</a> · <a href="/discovery/">Request a consultation</a></p>')
 body+=T.related_section([('/compare/tax-advisor-buying-guide/','Tax advisor buying guide'),('/compare/competitor-pricing/','Pricing for 100 providers'),('/workbooks/','Owner decision worksheets')])
 citations=[]
 if 'credentials' in g['slug']:
  citations=['https://www.irs.gov/tax-professionals/choosing-a-tax-professional'];body+=T.section('Credential verification resource','<p><a href="'+citations[0]+'">IRS: choosing a tax professional and checking credentials</a></p>')
 if 'document-checklist' in g['slug']:
  citations=['https://www.irs.gov/businesses/small-businesses-self-employed/recordkeeping'];body+=T.section('Recordkeeping resource','<p><a href="'+citations[0]+'">IRS recordkeeping guidance</a></p>')
 build(path,g['title'],g['answer'],body,g['keywords'],citations)
 links.append((path,g['title']))
# Established owners cover broad demand. Enhance their buying decisions rather than duplicating URLs.
OWNERS=[
('/how-much-does-a-tax-advisor-cost/','Tax advisor and tax strategist cost','Before comparing fees, identify whether you need analysis, recurring support, implementation, or filing. Ask for both first-year and ongoing totals with the same entities and tax years. A published starting fee may change after the provider reviews complexity.',['tax advisor cost','tax strategist cost','tax planning fees']),
('/real-estate-investor-cpa/','Choosing a real estate CPA','Ask who coordinates property accounting, owner returns, partnership K-1s, and depreciation records. Bring an entity chart and the next acquisition or sale deadline. Compare engagement scope by property and entity rather than just comparing the fee for a personal return.',['real estate CPA','CPA for real estate investors','rental property CPA']),
('/short-term-rental-tax-planning-basics/','Choosing a short-term rental tax advisor','Describe your rental use, ownership, participation records, services provided, and existing depreciation. Ask the advisor to evaluate your actual facts before estimating deductions. Confirm whether a property study, participation review, implementation, and tax preparation are separate services.',['short term rental tax advisor','Airbnb tax accountant','STR tax planning services']),
('/cost-segregation-study-cost-pricing/','Comparing cost segregation service providers','Request comparable quotes using the same property records. Compare methodology, input verification, report review, questions from your preparer, and included filing assistance. A lowest advertised study price does not establish the correct service for every property.',['cost segregation study cost','cost segregation quote','cost segregation companies']),
('/tax-planning-500k-1m-business-owners/','Hiring a business tax advisor','Identify the current entity structure, payroll, distributions, estimated payments, and pending business decisions. Ask for a written scope that connects owner planning to the operating companies and names the person responsible for follow-through.',['business tax advisor','tax strategist for entrepreneurs','tax advisor for business owners']),
('/individual-tax-planning-high-earners/','Selecting an advisor for high income','Tell the provider which income sources create complexity: wages, equity compensation, business ownership, rentals, or K-1s. Ask how the proposed plan addresses each source and which decisions require an outside professional. Compare tax services separately from investment management.',['high income tax planning services','high net worth tax advisor','tax advisor for W2 and rental income']),
('/physician-tax-planning/','Choosing a tax advisor for physicians','Clarify whether the proposal covers employed income, independent contractor work, practice ownership, property, and household filing. Confirm coordination with payroll and retirement plan specialists. A physician-specific website headline is less useful than a defined engagement for your income sources.',['tax planning for physicians','physician tax advisor']),
('/switching-cpas-mid-year-guide/','Questions before changing accountants','Confirm who owns every pending deadline before the handoff. Obtain complete returns, depreciation schedules, elections, books, and payment history. Ask the incoming professional to accept the scope in writing and identify any cleanup before the next filing.',['how to switch CPAs','switching accountants mid year','change tax advisor']),
('/exit-tax-planning-business-owners/','Selecting a business exit tax advisor','Before hiring, identify the transaction stage and the work needed before an LOI or binding agreement. Ask who reviews entity and deal structure, coordinates with legal counsel, and supports post-close reporting. Do not assume a general annual planning engagement includes transaction diligence.',['tax advisor before selling a business','business exit tax planning services']),
('/what-a-tax-advisory-engagement-includes/','Written deliverables and implementation','Ask for a list of reviewed records, assumptions, recommendations, action owners, and completion evidence. Confirm whether the engagement includes filing and meetings with other professionals or whether those are additional services.',['what does a tax planning engagement include','tax planning deliverables']),
('/proactive-tax-planning-vs-tax-preparation/','Compare planning and preparation proposals','Return preparation records and reports completed activity. Planning evaluates decisions and timing using the facts available. Some firms sell them together, while others separate them. Compare what each engagement actually delivers and how recommendations reach the return signer.',['tax planning vs tax preparation','tax strategist vs CPA']),
('/business-tax-second-opinion/','Buying a defined second opinion','Provide the original recommendation, assumptions, records, and deadlines. Ask the reviewer to identify what they can evaluate and whether they will provide a written conclusion. Confirm that a review fee includes neither implementation nor filing unless the agreement states otherwise.',['business tax second opinion','tax strategy review']),
('/cost-segregation-second-opinion/','Reviewing an existing study','Provide the report, supporting property records, depreciation schedules, and the questions raised by your preparer. Define whether the engagement is a report review, a corrected study, or filing assistance. Ask who owns any required follow-up.',['cost segregation second opinion']),
('/ae-tax-advisors-reviews/','Evaluating AE reviews and fit','Check the service discussed in each review and compare it with your proposed scope. Ask AE who owns your work, how communication is handled, and which deliverables are included. AE’s website is company-published; independent platform evidence should be read at its original source.',['AE Tax Advisors reviews','AE Tax Advisors complaints','is AE Tax Advisors legit']),
('/compare/best-tax-advisors-business-owners/','Compare vendors using a common buying checklist','Shortlist providers whose actual services match the business and owner decisions you face. Verify the assigned professionals, written deliverables, fee basis, implementation responsibilities, and filing scope. Best is a question of fit, not a universal ranking established by a vendor’s marketing.',['best tax advisors for business owners','best tax strategist']),
('/compare/diy-cost-segregation-vs-ae-tax/','Compare tools, review, and professional work','Describe which output you need and who will verify inputs and use the report on the return. Compare a software product with its actual support and review level. Avoid treating every DIY service as one provider with a single price or treating automation as proof that review is unnecessary.',['DIY vs professional cost segregation','cost segregation software vs engineering study'])
]
for path,heading,text,keywords in OWNERS:
 inject(path,T.section(heading,p(text)+'<p><a href="/compare/tax-advisor-buying-guide/">Use the tax advisor buying checklist</a> and <a href="/compare/competitor-pricing/">compare provider pricing and quote scope</a>.</p>'),'buyer-intent-20261008')
 links.insert(0,(path,heading))
body=T.section('Start with the decision you need help making',p('A business owner comparing an advisory proposal needs different evidence from a landlord buying a study or a founder purchasing bookkeeping and filing. Use the guides below to define the work, compare the complete fee, verify the assigned team, and plan implementation.')+p('AE publishes this guide as a tax provider. The linked comparisons disclose that commercial interest and distinguish verified fees from amounts that still require a quote.'))
body+=T.related_section(links,'Find the buying question that matches your situation')
body+=T.related_section([('/compare/competitor-pricing/','Compare pricing for 100 providers'),('/pricing/','AE Tax Advisors pricing'),('/compare/','Provider alternatives and comparisons'),('/discovery/','Discuss your engagement scope')],'Compare your shortlist')
build('/compare/tax-advisor-buying-guide/','Tax Advisor Buying Guide: Fees, Reviews, Proposals and Switching','Choose a tax advisor with a clear scope, verified team, complete fee comparison, and an implementation plan.',body,['how to choose a tax advisor','tax advisor buying guide','compare tax advisors'])
for path in ['/compare/','/pricing/']:
 inject(path,T.related_section([('/compare/competitor-pricing/','Provider pricing directory: 100 firms'),('/compare/tax-advisor-buying-guide/','Buyer guides: proposals, fees, reviews, and implementation')],'Research providers before hiring'),'buyer-navigation-20261008')
paths=[r['path'] for r in manifest]+['/compare/competitor-pricing/','/compare/tax-advisor-buying-guide/']+['/compare/'+g['slug']+'/' for g in GUIDES]+[x[0] for x in OWNERS]
xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>'+T.SITE+path+'</loc><lastmod>'+DATE+'</lastmod></url>\n' for path in paths)+'</urlset>\n'
(ROOT/'sitemap-vendor-shopping.xml').write_text(xml)
for filename in ['sitemap_index.xml','sitemap-index.xml']:
 f=ROOT/filename; text=f.read_text();entry='<sitemap><loc>'+T.SITE+'/sitemap-vendor-shopping.xml</loc><lastmod>'+DATE+'</lastmod></sitemap>\n'
 if '/sitemap-vendor-shopping.xml' not in text:text=text.replace('</sitemapindex>',entry+'</sitemapindex>')
 f.write_text(text)
coverage={'date':DATE,'competitorPricing':manifest,'newBuyerGuides':[{'path':'/compare/'+g['slug']+'/','keywords':g['keywords']} for g in GUIDES],'strengthenedOwners':[{'path':x[0],'keywords':x[3]} for x in OWNERS]}
(ROOT/'content/vendor-shopping-keyword-map-20261008.json').write_text(json.dumps(coverage,indent=2)+'\n')
print('Generated',len(GUIDES),'buyer guides; strengthened',len(OWNERS),'existing owners; sitemap URLs',len(paths))
