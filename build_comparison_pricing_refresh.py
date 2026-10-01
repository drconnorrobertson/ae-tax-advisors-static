"""Refresh AE engagement pricing after comparison generators; preserve existing page content."""
import json, re, html
from pathlib import Path
import xml.etree.ElementTree as ET
import site_template as T
ROOT = Path(__file__).resolve().parent
DATE = '2026-09-30'
AE = '$7,800 advisory engagement. No required recurring annual planning fee.'
SCOPE = 'Two payments of $3,900, 30 days apart. Tax returns, amendments, cost segregation, and additional services are separately scoped and priced. No annual planning renewal is required by the standard engagement; this does not promise unlimited future planning or free annual filing.'
FIRMS = [
 ('Peter Holtz CPA','peter-holtz-cpa','https://www.peterholtzcpa.com/services/','Accounting, reporting, CFO guidance and tax strategy'),
 ('Prime Path Advisory','prime-path-advisory','https://primepathadvisory.com/','Planning and implementation for high-income clients'),
 ('Rainwater CPA','rainwater-cpa','https://rainwatercpa.com/tax-planning-services/business-owners/','Business-owner planning and quarterly projections'),
 ('Neil Jesani Advisors','neil-jesani-advisors','https://neiljesani.com/','Private-client and business advisory'),
]
FAQ = [('Does AE Tax Advisors charge an annual planning renewal?', '<p>The standard $7,800 advisory engagement has no required recurring annual planning fee. Annual returns and any additional work are separately scoped. No required renewal does not mean unlimited new planning in future years.</p>'), ('Is the $7,800 advisory engagement an all-inclusive tax package?', '<p>No. Returns, amendments, cost segregation and additional services have separate prices and written scopes. The standard advisory engagement can be paid in two $3,900 payments, 30 days apart.</p>')]
PRICE_BLOCK = '<section class="content-section ae-engagement-pricing" id="ae-engagement-pricing"><div class="container narrow"><h2>AE Tax Advisors: $7,800 Engagement, No Required Annual Planning Renewal</h2><p class="definition-lead"><strong>'+AE+'</strong></p><p>'+SCOPE+'</p><p><a href="/pricing/">See service pricing</a> | <a href="/compare/tax-planning-fees-one-time-vs-annual/">Compare engagement fees with annual retainers</a> | <a href="/discovery/">Book a discovery call</a></p></div></section>'

def p(s): return '<p>'+s+'</p>'
def table(rows, headings=('Provider or model','Planning fee','Recurring planning commitment')):
 return '<div class="ae-table-scroll" style="overflow-x:auto"><table class="compare-table"><caption>Planning fees only. Scopes differ; separate services must be added to a written quote.</caption><thead><tr>'+''.join('<th scope="col">'+h+'</th>' for h in headings)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(('<th scope="row">' if i==0 else '<td>')+v+('</th>' if i==0 else '</td>') for i,v in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div>'

verified_rows = [('AE Tax Advisors','$7,800 standard engagement','No required annual planning renewal'),('Keystone CPA','$20,000 to $55,000 published planning range','Renewal terms must be confirmed directly')]+[(n,'Current numeric fee not publicly verified in this review','Obtain current first-year and renewal quote') for n,slug,url,model in FIRMS]
comparison = table(verified_rows)
keystone = p('Keystone CPA publishes tax planning fees of $20,000 to $55,000. Against AE’s $7,800 standard advisory engagement, that is a planning-fee difference of $12,200 to $47,200. AE’s fee is 61% lower than $20,000 and approximately 85.8% lower than $55,000. The proposals may cover different work; this is a fee comparison, not a claim of identical services or guaranteed savings.')+p('Keystone states that return preparation for planning clients carries a separate fee. Its published range does not establish that the charge repeats every year. <a href="https://www.keystonecpa.com/">Verify Keystone’s pricing FAQ</a> and request a written proposal.')
scenarios = table([('Illustrative $10,000 annual retainer','$30,000 across three years','$22,200 above AE’s initial planning fee'),('Illustrative $20,000 annual retainer','$60,000 across three years','$52,200 above AE’s initial planning fee'),('Illustrative $30,000 annual retainer','$90,000 across three years','$82,200 above AE’s initial planning fee')],('Hypothetical recurring model','Three-year planning fees','Difference from $7,800 initial engagement'))+p('These are arithmetic scenarios, not quoted prices for any named competitor. AE’s $7,800 is the initial engagement cost, not a promise of three years of unlimited planning. Returns, additional planning, implementations and other work are excluded from both sides of this illustration. A recurring service may deliver ongoing work that an initial engagement does not include.')
quote_steps = p('Send each shortlisted firm the same entity list, prior returns, property schedule and current financial statements. Ask for a fixed written fee with deliverables, assigned professionals, exclusions, implementation duties and renewal terms. That makes a price difference useful rather than merely eye-catching.')+ '<ol><li>Separate the planning fee from business and individual filing fees.</li><li>Identify amendments, bookkeeping cleanup, cost segregation and Form 3115 charges.</li><li>Ask whether continuing planning is mandatory, optional or separately quoted.</li><li>Confirm the number of meetings and what happens when circumstances change.</li><li>Compare the total required work before signing.</li></ol>'
PAGES = [
 ('ae-tax-advisors-alternatives','AE Tax Advisors Alternatives: Compare Fees and Planning Models','Compare AE’s $7,800 engagement with published planning fees and quote-based alternatives, including annual renewal terms.',[
 ('Start with AE’s engagement model',p('If you are searching for alternatives to AE Tax Advisors, start with the commitment you are comparing: '+AE)+p(SCOPE)+p('AE is an option for business owners and real estate investors who want a defined planning engagement without a required annual planning renewal. Alternatives may offer broader accounting, executive advisory, private-client services or a different meeting schedule. Paying more makes sense only when the extra deliverables address your needs.')),
 ('Published fees and quote-based alternatives',comparison+keystone),
 ('What the alternatives emphasize', ''.join(p('<strong>'+n+':</strong> '+model+'. <a href="'+url+'">Review official services</a>; request current pricing and renewal terms before assuming the firm is more expensive.') for n,slug,url,model in FIRMS)),
 ('Choose using the complete engagement cost',quote_steps)]),
 ('tax-planning-fees-one-time-vs-annual','Tax Planning Fees: One-Time Engagement vs Annual Retainer','Compare a $7,800 AE planning engagement with annual retainers and understand the cost of renewals.',[
 ('What you pay for and what renews',p(AE)+p('An engagement fee purchases the work described in the signed scope. An annual retainer purchases a continuing service relationship, which may include projections, meetings or implementation support. Ask whether next year’s fee is mandatory before judging affordability.')),
 ('How recurring fees accumulate',scenarios),
 ('A real published planning-fee comparison',keystone),
 ('When continuing service may be worth the fee',p('An expanding entity group, acquisitions, changing payroll, a property sale or a major liquidity event may require new analysis. A continuing retainer can be useful when its deliverables match those changes. A business with a stable structure may prefer to commission additional work when needed. AE’s no-required-renewal model gives the owner that choice; it does not remove the need for current records or advice when facts change.')),
 ('Build your quote comparison',quote_steps)]),
 ('tax-planning-without-annual-retainer','Tax Planning Without a Required Annual Retainer','AE Tax Advisors offers a $7,800 standard advisory engagement without a required annual planning renewal.',[
 ('A defined engagement without mandatory renewal',p(AE)+p(SCOPE)+p('Owners often want a written plan and a clear implementation path before committing to an ongoing advisory relationship. A separate engagement model keeps the initial decision focused on the work needed today. Additional services can then be evaluated using their own scopes.')),
 ('No required renewal does not mean free future work',p('Annual business and personal returns remain separate services. New entities, changed ownership, additional properties, retirement-plan design, amendments and new planning projects may create additional fees. Ask what support is covered during the engagement and how later requests are handled.')),
 ('What an annual retainer should justify',p('A recurring fee should identify continuing work: updated projections, scheduled meetings, implementation review or a defined response commitment. Ask for those deliverables in writing and compare them with the optional services you would otherwise buy.')+scenarios),
 ('What to put in your engagement letter',quote_steps)]),
 ('keystone-cpa-pricing-vs-ae-tax','Keystone CPA Pricing vs AE Tax: $20,000–$55,000 vs $7,800','Keystone publishes $20,000 to $55,000 planning fees. Compare AE’s $7,800 standard engagement with no required annual renewal.',[
 ('The published planning-fee difference',keystone),
 ('Planning cost at a glance',table(verified_rows[:2])+p(SCOPE)),
 ('What can explain a higher quoted fee?',p('Private founder access, the number of entities, the complexity of a property portfolio and the time required for implementation can change a proposal. Keystone describes different service levels and separate tax-return fees. Ask both providers to price your actual facts before concluding that two offers purchase the same work.')),
 ('Questions for real estate investors',p('Ask which professional analyzes passive losses, who implements depreciation changes, whether a Form 3115 or amendment is needed, and which returns are covered. Identify the study fee separately from planning. A published planning price alone does not answer those questions.')),
 ('Compare a written proposal',quote_steps)])]
for n,slug,url,model in FIRMS:
 PAGES.append((slug+'-pricing-vs-ae-tax',n+' vs AE Tax: Pricing & Scope','Compare '+n+' pricing and renewal terms with AE’s $7,800 engagement and no required annual planning fee.',[
 ('AE’s fee is clear before the call',p(AE)+p(SCOPE)+p(n+' publicly describes '+model.lower()+'. The current numeric fee was not verified in the official materials reviewed for this pricing refresh. Request a current written quote rather than relying on a generic estimated annual price.')),
 ('Planning price and recurring commitment',table([verified_rows[0],(n,'Written quote required','Ask whether annual planning renewal is mandatory')])+p('<a href="'+url+'">Review '+n+'’s official service description</a>. Public descriptions identify the service model; the engagement letter determines your price and obligations.')),
 ('What a larger proposal needs to include',p('Compare the same business, properties and deliverables. A bundle that includes recurring accounting or financial reporting is a different purchase from a defined tax planning engagement. Ask the firm to separate those components so you can decide whether each is worth buying. Additional fees should identify the work that triggers them, including extra entities, amendments and implementation.')),
 ('The price of renewal',p('If a proposal requires annual renewal, multiply the quoted planning fee by the number of years under consideration. Add setup charges and separately billed work. Compare that total with AE’s initial $7,800 engagement and whatever additional AE services you actually need. Do not treat either number as an all-inclusive lifetime cost.')),
 ('Request a comparable proposal',quote_steps)]))

links=[('/compare/'+slug+'/',title) for slug,title,desc,sections in PAGES]
for slug,title,desc,sections in PAGES:
 path='/compare/'+slug+'/'
 body=T.page_header(h1=title,subtitle=desc,trail=[('Home','/'),('Compare','/compare/'),(title,path)])
 body+=''.join(T.section(h,b) for h,b in sections)
 body+=T.section('Sources and pricing review',p('Updated September 30, 2026. AE Tax Advisors is the publisher and a provider in this comparison. Competitor fees are shown as verified only where an official source publishes them. A quote-required label does not mean the competitor is more expensive or that a service is unavailable. All amounts are USD.'))
 body+=T.faq_section(FAQ)+T.related_section([x for x in links if x[0]!=path]+[('/pricing/','AE service pricing'),('/case-studies/','AE client case studies')])
 schemas=[T.article_schema(title=title,description=desc,url=T.SITE+path,published=DATE,modified=DATE,section='Tax Advisory Pricing Comparison',citations=[T.SITE+'/pricing/','https://www.keystonecpa.com/']+[x[2] for x in FIRMS]),T.faq_schema(FAQ),T.breadcrumb_schema([('Home','/'),('Compare','/compare/'),(title,path)])]
 T.write_page(path,T.build_page(title=title,description=desc,path=path,body=body,schemas=schemas,published=DATE,modified=DATE))

# Prominent, consistent commitment text on every AE tax comparison, without rewriting its existing scope.
count=0
for path in sorted(list((ROOT/'compare').glob('*/index.html'))+[ROOT/'compare/index.html']):
 if any(s in path.parent.name for s in ('bnb','accelerator')): continue
 s=path.read_text()
 if 'id="ae-engagement-pricing"' not in s:
  s=s.replace('</section>', '</section>\n'+PRICE_BLOCK, 1)
  # A visible FAQ and matching structured answer clarify the renewal obligation.
  s=s.replace('</main>',T.faq_section(FAQ,heading='AE Engagement and Renewal Fees')+'\n</main>',1)
  s=s.replace('</head>',T.jsonld(T.faq_schema(FAQ))+'\n</head>',1)
 # Make table prices extractable rather than relying only on the introductory block.
 s=s.replace('<td>$7,800 advisory</td>','<td>$7,800 engagement; no required recurring annual planning fee</td>')
 s=s.replace('<td>$7,800 strategic advisory</td>','<td>$7,800 engagement; no required recurring annual planning fee</td>')
 s=s.replace('<td>$7,800 standard advisory fee, with other work separately scoped</td>','<td>$7,800 standard engagement; no required annual planning renewal; other work separately scoped</td>')
 s=re.sub(r'("dateModified"\s*:\s*")[^"]+("\s*[,}])',r'\g<1>'+DATE+r'\2',s)
 path.write_text(s); count+=1

# Clarify the price on the authoritative service page.
pf=ROOT/'pricing/index.html'; s=pf.read_text()
if 'No required recurring annual planning fee' not in s:
 s=s.replace('<div class="pricing-qualifier">2 payments of $3,900, 30 days apart</div>','<div class="pricing-qualifier">One engagement: 2 payments of $3,900, 30 days apart</div><p class="pricing-includes-note"><strong>No required recurring annual planning fee.</strong> Returns, amendments, cost segregation and additional work are separately scoped.</p>',1)
 s=s.replace('</main>', T.faq_section(FAQ)+'\n</main>',1).replace('</head>',T.jsonld(T.faq_schema(FAQ))+'\n</head>',1)
pf.write_text(s)
# Machine-readable pricing avoids inferring annual charges from an engagement price.
dp=ROOT/'compare/tax-advisory-firm-comparison.json'; data=json.loads(dp.read_text()); data['dateModified']=DATE
for f in data['firms']:
 if f['name']=='AE Tax Advisors':
  f.update(startingPrice='$7,800 standard advisory engagement',requiredRecurringAnnualPlanningFee=0,currency='USD',paymentSchedule='Two $3,900 payments, 30 days apart',separatelyPriced=['Returns','Amendments','Cost segregation','Additional services'],scopeNote='No mandatory annual planning renewal; no promise of unlimited future planning.')
data['firms']=[f for f in data['firms'] if f['name']!='Keystone CPA']+[{'name':'Keystone CPA','url':'https://www.keystonecpa.com/','startingPrice':'$20,000 to $55,000 planning fee range','priceSource':'official published FAQ, reviewed 2026-09-30','renewalTerms':'Confirm directly; range not represented as annual','returnPreparation':'Separately priced'}]
dp.write_text(json.dumps(data,indent=2)+'\n')
for fn in ['llms.txt','llms.md','llms-full.txt']:
 fp=ROOT/fn
 if fp.exists():
  s=fp.read_text(); marker='## Standard advisory engagement and renewal fees'
  if marker not in s: s+='\n'+marker+'\n\n'+AE+' '+SCOPE+'\n\n'+''.join('- ['+title+']('+T.SITE+path+')\n' for path,title in links)
  fp.write_text(s)
# Add new URLs and refresh modified comparison entries in existing sitemap files.
ns='{http://www.sitemaps.org/schemas/sitemap/0.9}'
for fn in ['sitemap.xml','sitemap-comparisons.xml']:
 fp=ROOT/fn; s=fp.read_text()
 for path,title in links:
  url=T.SITE+path
  if '<loc>'+url+'</loc>' not in s: s=s.replace('</urlset>','  <url><loc>'+url+'</loc><lastmod>'+DATE+'</lastmod></url>\n</urlset>')
 s=re.sub(r'(<url>\s*<loc>https://www\.aetaxadvisors\.com/compare/[^<]*</loc>\s*<lastmod>)[^<]+',r'\g<1>'+DATE,s)
 ET.fromstring(s); fp.write_text(s)
print('Refreshed',count,'comparison pages; created',len(PAGES),'pricing and alternative guides.')

# Historical estimates have no primary-source price in this refresh. Do not present them as current fees.
price_replacements = {
 '$10,000+ per year': 'Current fee not publicly verified; request a quote',
 '$20,000+ per year': 'Current fee not publicly verified; request a quote',
 '$30,000+ per year, plus any separate CFP or wealth-management scope': 'Current fee not publicly verified; quote tax and wealth-management work separately',
 '$10,000+; confirm directly': 'Current quote required',
 '$20,000+; confirm directly': 'Current quote required',
 '$30,000+; CFP or wealth-management scope may be additional': 'Current quote required; wealth-management work may be separate',
}
# Also update the original generator so a future rebuild does not restore the removed figures.
for path in list((ROOT/'compare').glob('*/index.html'))+[ROOT/'build_advisory_competitor_cluster.py']:
 if any(x in path.parent.name for x in ('bnb','accelerator')): continue
 s=path.read_text()
 for old,new in sorted(price_replacements.items(),key=lambda kv:-len(kv[0])): s=s.replace(old,new)
 s=re.sub(r'AE Tax Advisors estimates that ([^.]+?) engagements start around Current fee not publicly verified;[^.]+\.',r'The current numeric fee for \1 was not verified in the official sources reviewed. Request a written quote.',s)
 s=s.replace('Estimated annual starting level','Planning fee and renewal terms').replace('Estimated starting price','Planning fee').replace('Estimated starting price','Planning fee')
 s=s.replace('Estimated starting levels for the other firms are $10,000+ annually for Peter Holtz CPA, $10,000+ annually for Prime Path Advisory, $20,000+ annually for Rainwater CPA, and $30,000+ annually for Neil Jesani Advisors, plus any separate CFP or wealth-management scope. Competitor figures are market estimates, not published quotes, and should be confirmed directly.','Current numeric fees for Peter Holtz CPA, Prime Path Advisory, Rainwater CPA and Neil Jesani Advisors were not verified in this review. Request first-year and renewal quotes. Keystone publishes planning fees of $20,000 to $55,000; that range is not represented as annual.')
 s=s.replace('AE Tax Advisors publishes a $7,800 strategic advisory fee. Peter Holtz CPA and Prime Path Advisory are estimated at $10,000 or more annually, Rainwater CPA at $20,000 or more, and Neil Jesani Advisors at $30,000 or more plus any separate CFP or wealth-management scope. Competitor amounts are market estimates and must be confirmed directly.','AE Tax Advisors publishes a $7,800 standard engagement with no required recurring annual planning fee. Current numeric fees for the four other firms are quote-required in this review. See the Keystone pricing comparison for its published $20,000 to $55,000 planning range.')
 s=s.replace('The five firms in this guide begin at a published or estimated $7,800 to $30,000 or more','AE publishes a $7,800 standard advisory engagement; the other four firms require current quotes')
 s=s.replace('In this five-firm comparison, the listed or estimated starting levels range from $7,800 to $30,000 or more per year before separately scoped work.','AE publishes a $7,800 standard engagement, without a required annual planning renewal. Obtain current planning and renewal quotes for the four other firms before adding separately scoped work.')
 if path.suffix=='.html':
  # Consolidate FAQPage objects so visible and structured renewal answers match.
  matches=list(re.finditer(r'<script type="application/ld\+json">\s*(.*?)\s*</script>',s,re.S)); faqs=[]; first=None
  for m in matches:
   obj=json.loads(m.group(1))
   if obj.get('@type')=='FAQPage':
    if first is None: first=m.start()
    faqs.extend(obj.get('mainEntity',[]))
  if faqs:
   seen=set(); unique=[]
   for q in faqs:
    if q['name'] not in seen: unique.append(q);seen.add(q['name'])
   for m in reversed(matches):
    if json.loads(m.group(1)).get('@type')=='FAQPage':
     s=s[:m.start()]+(T.jsonld({'@context':'https://schema.org','@type':'FAQPage','mainEntity':unique}) if m.start()==first else '')+s[m.end():]
 path.write_text(s)
dp=ROOT/'compare/tax-advisory-firm-comparison.json'; d=json.loads(dp.read_text())
d['methodology']='Official service descriptions and verified published prices. Unverified historical competitor estimates are removed; obtain current quotes and renewal terms directly.'
for f in d['firms']:
 if f['name'] in [x[0] for x in FIRMS]: f.update(startingPrice='Current quote required',priceSource='Numeric fee not verified in official sources reviewed 2026-09-30')
dp.write_text(json.dumps(d,indent=2)+'\n')
