#!/usr/bin/env python3
"""Apply the reviewed pricing dataset without rebuilding unrelated page content."""
import html,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATE='2026-10-24'
E=html.escape
DATA=ROOT/'content/vendor-pricing-20261024.json'
rows=json.loads(DATA.read_text())
coverage={r['slug']:r for r in json.loads((ROOT/'_gen/competitor-coverage-20261008.json').read_text())['brands']}
PLANNING=['https://www.anomalycpa.com/pricingcalculator','https://www.investorfriendlycpa.com/pricing-tax-planning','https://www.keystonecpa.com/']
BOOKS=['https://www.anomalycpa.com/pricingcalculator','https://kruzeconsulting.com/pricing/','https://www.graphitefinancial.com/pricing']
COSTSEG=['https://www.recostseg.com/','https://costsegez.com/','https://www.costsegregation.com/resources/cost-segregation-study-cost/']
HOURLY=['https://www.brighthilladvisors.com/pricing-and-fees/']
ESTIMATES={
 'planning':('$4,000–$20,000+ per planning engagement','A defined tax-planning project for a business owner or investor; filings, studies, legal work, and new projects are extra.','AE’s rounded budgeting band uses published planning tiers from Anomaly and Investor Friendly CPA and Keystone’s higher planning range. It is a comparable-service budget, not a measured average or this firm’s fee.',PLANNING),
 'books':('$400–$2,000+ per month; $4,800–$24,000+ over 12 months','Recurring small-business bookkeeping and tax coordination for one entity with usable records; cleanup, complex industries, payroll, returns, and CFO work may add cost.','AE’s rounded budgeting band uses Anomaly accounting from $400/month, Kruze bookkeeping at $650–$1,500/month, and Graphite accounting from $1,500/month. Scope and add-ons vary.',BOOKS),
 'costseg':('$2,500–$5,000+ per property study','A professionally reviewed or engineered study of a relatively straightforward property; complex commercial sites, travel, filings, and amendments are additional.','AE’s rounded budgeting band uses R.E. Cost Seg engineering from $2,320, CostSegEZ engineering from $2,500, and CostSegregation.com’s discussion of complex studies reaching $5,000 or more. Software-only products cost less.',COSTSEG),
 'software':('$395–$2,500+ per report or reviewed study','A qualifying small residential property using a software or professional-review workflow; comprehensive advisory and filing excluded.','AE’s budgeting band spans Cost Seg Atlas’s $395 report and My Cost Segregation professional review from $2,500. It does not assume identical methods or support.',['https://costseg.2911tech.com/pricing','https://www.mycostsegregation.com/pricing/']),
 'national':('$6,000–$45,000 illustrative project budget','A hypothetical 20–100 hour tax advisory project, using $300–$450/hour for budgeting; enterprise audits, transactions, international work, and ongoing compliance excluded.','Calculation: 20 × $300 = $6,000; 100 × $450 = $45,000. The rates are external published planning benchmarks from Bright Hill, not this national firm’s rates. Actual engagements may fall outside this scenario.',HOURLY),
 'legal':('$3,000–$14,000 illustrative tax-work budget','A hypothetical 10–40 hour tax/accounting advisory scope using $300–$350/hour; legal documents, court representation, government fees, and entity formation excluded.','Calculation: 10 × $300 = $3,000; 40 × $350 = $14,000, using Bright Hill’s published tax planning rates as an external benchmark. This is not a legal-services price or this provider’s hourly rate.',HOURLY),
 'wealth':('$3,950–$12,500 per year for a comparable flat-fee planning membership','Household financial planning membership benchmark; asset-based investment management fees and separate business tax work excluded.','AE uses Range’s published membership tiers as a comparison budget. This does not establish this provider’s fee schedule or imply it offers the same membership.',['https://www.range.com/pricing']),
}
def estimate_key(row):
 if row['slug'] in ('peter-holtz-cpa','rainwater-cpa','crescent-cpa-advisors'):return 'planning'
 c=row['category']
 if c in ('strategy','realestate','medical'):return 'planning'
 if c in ('national','costseg','software','wealth'):return c
 if c in ('legal','resolution'):return 'legal'
 return 'books'
for r in rows:
 if r.get('kind')!='published':
  key=estimate_key(r);fee,scope,basis,sources=ESTIMATES[key]
  r.update(kind='estimate',status='AE budget estimate — comparable service',fee=fee,qualification=scope,estimateBasis=basis,benchmarkSources=sources,estimateCategory=key)
 r['reviewed']=DATE
 if r['slug']=='tax-alchemy':r['additionalSources']=['https://taxalchemy.com/faqs/']
DATA.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')

def p(text):return '<p>'+E(text)+'</p>'
def section(heading,body,ident=''):
 return '<section class="content-section pricing-review"'+(' id="'+ident+'"' if ident else '')+'><div class="container narrow"><h2>'+E(heading)+'</h2>'+body+'</div></section>'
def anchors(urls):
 return ' · '.join('<a href="'+E(u,quote=True)+'" rel="noopener">'+E(re.sub(r'^https?://(www\.)?','',u).rstrip('/'))+'</a>' for u in dict.fromkeys(urls))
def card(r):
 published=r['kind']=='published'
 label=r['status'] if published else 'AE budget estimate for comparable work'
 b='<p class="pricing-evidence-label">'+E(label)+'</p><p class="pricing-fee">'+E(r['fee'])+'</p>'
 if not published:b+=p('A numeric fee for '+r['name']+' was not verified. The amount above is AE’s budgeting estimate for the scope below. It is not a published price or quote from '+r['name']+'.')
 b+=p(r['qualification'])
 if not published:b+=p(r['estimateBasis'])+'<p><strong>Estimate benchmarks:</strong> '+anchors(r['benchmarkSources'])+'</p>'
 b+='<p><strong>Provider source:</strong> '+anchors([r['source']]+r.get('additionalSources',[]))+'</p>'
 if r['slug']=='tax-alchemy':
  b+=p('Against AE’s $7,800 standard advisory fee, the homepage range is $24,200–$42,200 higher in initial fees. The FAQ’s wider range is $12,200–$142,200 higher. These are fee differences between differently scoped offers; confirm the same work in both proposals.')
 elif r['slug']=='keystone-cpa':
  b+=p('The published planning range is $12,200–$47,200 above AE’s $7,800 standard advisory fee. This arithmetic does not establish identical deliverables or an annual recurring charge.')
 b+=p('Reviewed October 24, 2026. USD. AE Tax Advisors publishes this commercial comparison and also offers tax services. Starting prices, examples, and estimates require confirmation for your facts.')
 b+='<p><a href="/compare/competitor-pricing/#estimate-methodology">How the prices and estimates were calculated</a> · <a href="/pricing/">AE’s pricing and separately scoped services</a></p>'
 return section(r['name']+': pricing and estimated cost',b,'competitor-price-review')
def metadata(text,sources):
 text=re.sub(r'(<meta property="article:modified_time" content=")[^"]+',r'\g<1>'+DATE+'T00:00:00-04:00',text)
 def schema(m):
  obj=json.loads(m[1])
  def walk(v):
   if isinstance(v,list):
    for item in v:walk(item)
   if isinstance(v,dict):
    if v.get('@type') in ('Article','WebPage','Dataset'):
     v['dateModified']=DATE
     if v.get('@type')=='Article':
      old=v.get('citation',[]);old=[old] if isinstance(old,str) else old
      v['citation']=list(dict.fromkeys(old+sources))
    for child in v.values():
     if isinstance(child,(dict,list)):walk(child)
  walk(obj)
  return '<script type="application/ld+json">\n'+json.dumps(obj,indent=2,ensure_ascii=False)+'\n</script>'
 text=re.sub(r'<script type="application/ld\+json">\s*(.*?)\s*</script>',schema,text,flags=re.S)
 if '/assets/competitor-pricing.css' not in text:text=text.replace('</head>','<link rel="stylesheet" href="/assets/competitor-pricing.css?v=20261024">\n</head>')
 return text
changed=set()
for r in rows:
 paths={r['path']}
 cov=coverage[r['slug']]
 paths.update(cov[key].replace('https://www.aetaxadvisors.com','') for key in ('alternative_url','comparison_url'))
 for url in paths:
  f=ROOT/url.strip('/')/'index.html'
  if not f.exists():continue
  text=f.read_text()
  if '<title>Page retired' in text:continue
  text=re.sub(r'<section\b[^>]*id="competitor-price-review"[^>]*>.*?</section>','',text,flags=re.S)
  # Replace the superseded price section on the dedicated guide; preserve scope and quote checklist.
  if url==r['path']:
   text=re.sub(r'<section\b[^>]*>\s*<div[^>]*>\s*<h2>What does .*? cost\?</h2>.*?</section>','',text,count=1,flags=re.S)
  if r['slug']=='tax-alchemy':text=re.sub(r'<!-- TAX-ALCHEMY-FEES-20261013 START -->.*?<!-- TAX-ALCHEMY-FEES-20261013 END -->','',text,flags=re.S)
  text=re.sub(r'(<section class="content-section\b)',lambda m:card(r)+m[1],text,count=1)
  text=text.replace('This overview does not publish an unverified numeric competitor fee.','The pricing review above distinguishes published fees from AE budget estimates for comparable work.')
  if r['kind']=='published':
   # Remove the old assertion that there is no verified numeric price in this overview.
   text=text.replace('This overview does not publish an unverified numeric competitor fee.','See the sourced pricing review above for published fees and their scope.')
   text=text.replace('A numeric fee was not verified in the official sources reviewed.','See the current sourced pricing review above.')
  text=metadata(text,[r['source']]+r.get('additionalSources',[])+r.get('benchmarkSources',[]))
  f.write_text(text);changed.add('/'+f.relative_to(ROOT).parent.as_posix()+'/')

published=sum(r['kind']=='published' for r in rows)
intro=section('Published prices, annual costs, and transparent estimates',
 p(f'{len(rows)} providers: {published} with sourced published prices and {len(rows)-published} with AE budget estimates for defined comparable work. Every row shows a numeric cost and its evidence type. Reviewed October 24, 2026. All amounts are USD.')+
 p('AE’s standard advisory engagement is $7,800, with no required annual planning renewal. Returns, amendments, studies, and additional services are separately priced. Compare the complete scope before choosing a provider.')+
 '<div class="pricing-highlights">'+
 '<article><h3>Tax Alchemy</h3><p class="pricing-fee">$32,000–$50,000</p><p>Homepage planning range; FAQ separately lists $20,000–$150,000.</p><a href="/compare/tax-alchemy-pricing/">Review both sources and scope</a></article>'+
 '<article><h3>Keystone CPA</h3><p class="pricing-fee">$20,000–$55,000</p><p>Published planning range; $12,200–$47,200 above AE’s initial advisory fee. Scopes differ.</p><a href="/compare/keystone-cpa-pricing-vs-ae-tax/">Compare planning fees</a></article>'+
 '<article><h3>Monthly fees add up</h3><p class="pricing-fee">$1,500/mo = $18,000/yr</p><p>Twelve monthly payments before setup, returns, cleanup, and other excluded work.</p><a href="#estimate-methodology">Check billing and assumptions</a></article></div>'+
 p('Published prices describe specific services, starting tiers, promotions, averages, or client examples. An AE estimate is a budget for comparable work, not a claim about what that named firm charges. Some providers cost less than AE or sell a different service.'))
table_rows=[]
for r in sorted(rows,key=lambda r:r['name']):
 text=r['name']+' '+r['category']+' '+r['fee']
 label=r['status'] if r['kind']=='published' else 'AE budget estimate (not a provider quote)'
 source_urls=[r['source']]+r.get('additionalSources',[]) if r['kind']=='published' else r['benchmarkSources']
 cov=coverage[r['slug']]
 research_links='<br><small><a href="'+cov['alternative_url'].replace('https://www.aetaxadvisors.com','')+'">Alternatives</a> · <a href="'+cov['comparison_url'].replace('https://www.aetaxadvisors.com','')+'">Compare with AE</a></small>'
 table_rows.append('<tr data-provider="'+E(text.lower(),quote=True)+'" data-kind="'+r['kind']+'" data-category="'+r['category']+'"><th scope="row"><a href="'+r['path']+'">'+E(r['name'])+' pricing</a>'+research_links+'</th><td>'+E(r['category'])+'</td><td>'+E(r['fee'])+'</td><td><strong>'+E(label)+'</strong><br>'+('<a href="'+E(source_urls[0],quote=True)+'" rel="noopener">Official price source</a>' if r['kind']=='published' else '<a href="'+r['path']+'#competitor-price-review">Scope and estimate basis</a>')+'</td></tr>')
filters='<div class="pricing-filters"><label>Search providers<input id="provider-search" type="search" placeholder="Name, service, or price"></label><label>Evidence<select id="provider-evidence"><option value="">All prices and estimates</option><option value="published">Published prices</option><option value="estimate">AE budget estimates</option></select></label><label>Service category<select id="provider-category"><option value="">All categories</option>'+''.join('<option value="'+c+'">'+c+'</option>' for c in sorted({r['category'] for r in rows}))+'</select></label></div>'
directory=section('Find a provider and compare the cost',filters+'<p id="provider-count" aria-live="polite">'+str(len(rows))+' providers</p><div class="pricing-table-scroll" role="region" aria-label="Provider pricing comparison" tabindex="0"><table><caption>Fees and budget estimates cover different services. Read each guide for billing terms, exclusions, and sources.</caption><thead><tr><th scope="col">Provider</th><th scope="col">Service</th><th scope="col">Price or estimated budget</th><th scope="col">Evidence</th></tr></thead><tbody id="provider-rows">'+''.join(table_rows)+'</tbody></table></div><script src="/assets/competitor-pricing.js" defer></script>')
method=section('How the prices and estimates were calculated',
 p('Published prices come from official provider pages reviewed on October 24, 2026. Starting prices are floors, not fixed quotes. Promotional prices may expire. Published examples and averages are identified separately. Revenue thresholds, projected tax savings, deposits, and marketing “values” are not substituted for engagement fees.')+
 p('For providers without a verified fee, AE supplies an estimate for a defined comparable scope. The estimate comes from peer fee schedules or an explicit hours-times-rate calculation. It is not an estimate based on a private quote from the named firm, not a statistical market average, and not evidence that the named firm is expensive. The actual proposal may be higher or lower.')+
 ''.join('<details><summary>'+E(key.title())+' estimate: '+E(v[0])+'</summary>'+p(v[1])+p(v[2])+'<p>'+anchors(v[3])+'</p></details>' for key,v in ESTIMATES.items())+
 p('Annualized amounts are twelve times a monthly fee and do not assert a required twelve-month contract. Add required bookkeeping, onboarding, returns, payroll, cleanup, studies, and implementation to compare the same first-year work. A one-time planning engagement and a recurring service relationship may include different deliverables.')+
 '<p><a href="/compare/tax-advisor-comparison-methodology/">Full comparison methodology</a> · <a href="/contact/">Submit a pricing correction with a source</a></p>', 'estimate-methodology')
f=ROOT/'compare/competitor-pricing/index.html';text=f.read_text()
# Preserve navigation, page header, and footer; replace directory content only.
start=text.index('<section class="content-section')
end=text.index('</main>',start)
text=text[:start]+intro+directory+method+text[end:]
text=re.sub(r'\b\d+ Providers\b',str(len(rows))+' Providers',text)
text=re.sub(r'Compare (?:official fee information and quote checklists|published fees and clearly labeled cost estimates) for \d+ tax, accounting, and cost segregation providers\.','Compare published fees and clearly labeled cost estimates for '+str(len(rows))+' tax, accounting, and cost segregation providers.',text)
text=metadata(text,[r['source'] for r in rows if r['kind']=='published'])
f.write_text(text);changed.add('/compare/competitor-pricing/')
mf=ROOT/'compare/tax-advisor-comparison-methodology/index.html';text=mf.read_text()
text=re.sub(r'<section\b[^>]*id="pricing-estimate-policy"[^>]*>.*?</section>','',text,flags=re.S)
text=text.replace('</main>',section('Pricing evidence and AE budget estimates',p('As of October 24, 2026, the competitor pricing directory distinguishes official published fees from AE estimates for comparable services. Each estimate states the work, billing period, source benchmarks, and assumptions. Estimates do not establish a named provider’s fees, renewal requirement, or relative price. Published examples, starting tiers, promotional offers, and annualized arithmetic are identified explicitly.')+'<p><a href="/compare/competitor-pricing/#estimate-methodology">Read the full estimation method and benchmarks</a>.</p>','pricing-estimate-policy')+'</main>')
text=text.replace('The competitor figures in this comparison cluster are market estimates available to AE Tax Advisors and must be confirmed directly with each firm.','The directory labels each figure as published pricing or an AE budget estimate for comparable work. Estimates have stated assumptions and do not establish the named firm’s actual fee. Confirm your scope and price directly.')
mf.write_text(metadata(text,[]));changed.add('/compare/tax-advisor-comparison-methodology/')
public_data={'reviewed':DATE,'currency':'USD','publisher':'AE Tax Advisors','estimateDisclosure':'AE estimates are budgets for defined comparable work, not named-provider fees or quotes.','providers':rows}
(ROOT/'compare/competitor-pricing/prices.json').write_text(json.dumps(public_data,indent=2,ensure_ascii=False)+'\n')
firm_file=ROOT/'compare/tax-advisory-firm-comparison.json'
firms=json.loads(firm_file.read_text());firms['dateModified']=DATE
firms['methodology']='Official published fees and explicitly labeled AE budget estimates for defined comparable services; estimates do not establish named-provider fees.'
firms['pricingDataUrl']='https://www.aetaxadvisors.com/compare/competitor-pricing/prices.json'
for firm in firms['firms']:
 match=next((r for r in rows if r['name']==firm['name'] or (r['slug']=='rainwater-cpa' and firm['name']=='Rainwater CPA')),None)
 if match and match['kind']=='estimate':
  firm['comparableServiceBudget']={'amount':match['fee'],'scope':match['qualification'],'basis':match['estimateBasis'],'sources':match['benchmarkSources'],'disclosure':'AE budget estimate, not this provider’s published fee or quote.'}
  firm['priceSource']='Provider quote required; comparable service budget reviewed '+DATE
 elif match:firm['priceSource']='Official published pricing reviewed '+DATE
firm_file.write_text(json.dumps(firms,indent=2,ensure_ascii=False)+'\n')
for f in ROOT.glob('sitemap*.xml'):
 text=f.read_text()
 def entry(m):
  x=m[0];loc=re.search(r'<loc>https://www\.aetaxadvisors\.com([^<]*)</loc>',x)
  if loc and loc[1] in changed:x=re.sub(r'<lastmod>[^<]+</lastmod>','<lastmod>'+DATE+'</lastmod>',x)
  return x
 updated=re.sub(r'<url>.*?</url>',entry,text,flags=re.S)
 if updated!=text:f.write_text(updated)
(ROOT/'content/pricing-refresh-20261024-manifest.json').write_text(json.dumps({'reviewed':DATE,'published':published,'estimates':len(rows)-published,'pages':sorted(changed)},indent=2)+'\n')
print('Updated',len(changed),'pages;',published,'published prices;',len(rows)-published,'explicit estimates')
