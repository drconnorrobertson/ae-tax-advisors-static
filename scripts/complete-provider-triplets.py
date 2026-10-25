#!/usr/bin/env python3
"""Maintain 100 distinct pricing/alternatives/comparison page sets from primary sources."""
import csv,html,json,re,runpy,sys,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
import site_template as T
E=html.escape;DATE='2026-10-24';SITE=T.SITE
EXCLUDED=re.compile(r'nth[\s._-]*degree|nthdegree|dan\s+nicholson',re.I)
def dump(f,d):f.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def clean(value):
 if isinstance(value,list):
  return [clean(x) for x in value if not (isinstance(x,str) and EXCLUDED.search(x)) and not (isinstance(x,dict) and any(EXCLUDED.search(str(x.get(k,''))) for k in ('slug','name','brand','url','@id','source','path','provider')))]
 if isinstance(value,dict):
  return {k:clean(v) for k,v in value.items() if not EXCLUDED.search(k) and not (isinstance(v,str) and EXCLUDED.search(v))}
 return value
# Remove excluded records from generator inputs, historical research manifests, and exports.
# Redirect definitions and exclusion guards intentionally remain to keep removed URLs retired.
for folder in ('content','_gen'):
 for f in (ROOT/folder).rglob('*.json'):
  old=json.loads(f.read_text());new=clean(old)
  if old!=new:dump(f,new)
 for ext in ('*.csv','*.tsv','*.md'):
  for f in (ROOT/folder).rglob(ext):
   old=f.read_text();new='\n'.join(line for line in old.splitlines() if not EXCLUDED.search(line))+'\n'
   if EXCLUDED.search(old):f.write_text(new)
f=ROOT/'small_business_firms.json';dump(f,clean(json.loads(f.read_text())))
prices=json.loads((ROOT/'content/vendor-pricing-20261024.json').read_text())
if not any(r['slug']=='tax-hive' for r in prices):
 prices.append(dict(slug='tax-hive',name='Tax Hive',path='/compare/tax-hive-pricing/',category='strategy',source='https://taxhive.com/pricing/',fee='Advertised services start at $399; a customized tax plan requires a proposal.',qualification='The pricing page does not identify the billing period or the full scope attached to $399. Do not treat it as an annual, monthly, or complete-plan fee. Confirm the initial plan, filing, bookkeeping, implementation, and renewal charges.',reviewed=DATE,keywords=['Tax Hive pricing','Tax Hive cost','Tax Hive fees'],status='Published starting amount — billing period unspecified',kind='published',additionalSources=['https://taxhive.com/services/strategic-tax-planning/']))
dump(ROOT/'content/vendor-pricing-20261024.json',prices)
refs=json.loads((ROOT/'content/seo-campaign-20261007/competitor-sources.json').read_text())
old_coverage=json.loads((ROOT/'_gen/competitor-coverage-20261008.json').read_text())
old_map={r['slug']:r for r in old_coverage['brands']}
CURRENT_SOURCES={'tax-alchemy':'https://taxalchemy.com/','wcg-cpas':'https://wcginc.com/tax-center/business-advisory-services/','xendoo':'https://xendoo.com/xendoo-pricing/','fondo':'https://fondo.com/taxpass','little-fish-accounting':'https://www.littlefishaccounting.com/taxes','costsegrx':'https://www.costsegrx.com/'}
for r in refs:
 r['existing_url']='/compare/'+r['slug']+'-alternatives/'
 r['primary_url']=CURRENT_SOURCES.get(r['slug'],r['primary_url'])
if not any(r['slug']=='tax-hive' for r in refs):refs.append(dict(slug='tax-hive',name='Tax Hive',existing_url='/compare/tax-hive-alternatives/',primary_url='https://taxhive.com/services/strategic-tax-planning/'))
dump(ROOT/'content/seo-campaign-20261007/competitor-sources.json',refs)
profile_file=ROOT/'content/seo-campaign-20261007/competitors.tsv'
profile_lines=profile_file.read_text().splitlines()
if not any(s.startswith('tax-hive|') for s in profile_lines):profile_lines.append('tax-hive|strategy|business tax planning, return preparation, bookkeeping, and entity services|Business owners comparing a customized plan with ongoing support|You need to connect a tax plan with the person responsible for carrying out each recommendation and filing the returns.|Separate the initial plan, implementation support, filings, bookkeeping, and annual plan updates in the proposal.|What does the $399 starting amount buy, and what is the complete first-year price?')
profile_file.write_text('\n'.join(profile_lines)+'\n')
profiles={line.split('|')[0]:dict(zip(('category','focus','audience','scenario','instruction','question'),line.split('|')[1:])) for line in profile_lines}
notes=json.loads((ROOT/'content/competitor-comparison-notes-20261008.json').read_text())
def file(url):return ROOT/url.removeprefix(SITE).strip('/')/'index.html'
def p(s):return '<p>'+E(s)+'</p>'
def a(url,label):return '<a href="'+E(url,quote=True)+'">'+E(label)+'</a>'
def table(headers,rows):return '<div class="pricing-table-scroll" tabindex="0" role="region" aria-label="Provider options"><table><thead><tr>'+''.join('<th scope="col">'+E(h)+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+cell+'</td>' for cell in row)+'</tr>' for row in rows)+'</tbody></table></div>'
def write(url,title,desc,body,citations):
 trail=[('Home','/'),('Compare','/compare/'),(title,url)]
 body=T.page_header(h1=E(title),subtitle=E(desc),trail=trail)+body
 schemas=[T.article_schema(title=title,description=desc,url=SITE+url,published=DATE,modified=DATE,section='Provider research',citations=citations),T.breadcrumb_schema(trail)]
 doc=T.build_page(title=title+' | AE Tax Advisors',description=desc,path=url,body=body,schemas=schemas,published=DATE,modified=DATE,active_nav='/compare/',extra_head='<link rel="stylesheet" href="/assets/competitor-pricing.css?v=20261024">')
 T.write_page(url,'\n'.join(line.rstrip() for line in doc.splitlines())+'\n')
PEERS={
 'strategy':['gelt','anomaly-cpa','investor-friendly-cpa'],
 'realestate':['hall-cpa','investor-friendly-cpa','keystone-cpa'],
 'costseg':['re-cost-seg','maven-cost-segregation','kbkg'],
 'software':['cost-seg-smart','costsegregation-com','my-cost-segregation'],
 'books':['xendoo','acuity','decimal'],
 'startup':['pilot','kruze-consulting','fondo'],
 'practice':['heard','wellness-fi','tldr-accounting'],
 'medical':['cerebral-tax-advisors','1099-tax-doctor','duncan-carter-tax-advisory'],
 'fitness':['fitness-cpa','jetro-associates','incite-tax'],
 'digital':['tax-hack-accounting','bottom-line-cpa','fusion-cpa'],
 'creative':['blumer-cpas','little-fish-accounting','acuity'],
 'inventory':['accountfully','xendoo','acuity'],
 'regulated':['greengrowth-cpas','fusion-cpa','aprio'],
 'filing':['taxhub','vincere-tax','wcg-cpas'],
 'solopreneur':['collective','wcg-cpas','vincere-tax'],
 'wealth':['range','creative-planning','neil-jesani-advisors'],
 'national':['aprio','bdo','rsm'],
 'legal':['anderson-advisors','jasmine-dilucci','wcg-cpas'],
 'resolution':['jasmine-dilucci','firm1040','anderson-advisors'],
 'business':['wcg-cpas','fusion-cpa','anomaly-cpa'],
}
refmap={r['slug']:r for r in refs};pricemap={r['slug']:r for r in prices}
assert len(refs)==len(prices)==100
manifest=[];created=[]
for ref in refs:
 s=ref['slug'];name=ref['name'];profile=profiles[s]
 old=old_map.get(s,{})
 alt='/compare/'+s+'-alternatives/'
 vs=old.get('comparison_url',SITE+'/compare/'+s+'-vs-ae-tax/').removeprefix(SITE)
 price=pricemap[s]['path']
 manifest.append(dict(slug=s,brand=name,alternative_url=SITE+alt,comparison_url=SITE+vs,pricing_url=SITE+price,review_url=SITE+alt+'#provider-review',review_owner='Provider service profile on dedicated alternatives page',comparison_action='distinct canonical comparison',official_source=ref['primary_url'],editorial_date=DATE))
 if not file(alt).exists() or s in ('tax-hive','proactive-tax-advisors'):
  peers=[x for x in PEERS.get(profile['category'],PEERS['business']) if x!=s][:2]
  title=name+' Alternatives: Compare Services, Fees and Fit'
  desc='Evaluate alternatives to '+name+' using official service information, pricing scope, and the work your business needs.'
  body=T.section('What '+E(name)+' publishes',p(name+' describes '+profile['focus']+'.')+'<p>'+a(ref['primary_url'],'Read '+name+'’s own service information')+'. Provider claims are drawn from its website; a service menu does not establish what your engagement includes.</p>').replace('<section ', '<section id="provider-review" ',1)
  body+=T.section('Why you may be considering an alternative',p(profile['scenario'])+p(profile['instruction'])+'<h3>'+E(profile['question'])+'</h3>')
  if s in notes:body+=T.section('The scope that matters for this decision',p(notes[s]))
  options=[('AE Tax Advisors','A defined owner or real-estate tax planning engagement. Standard advisory $7,800; complex advisory $9,800; implementation, returns, studies, and other services separately scoped.','/pricing/','AE service pricing')]
  options += [(refmap[x]['name'],profiles[x]['focus']+'. Confirm the actual proposal and continuing obligations.',refmap[x]['primary_url'],'Official service information') for x in peers]
  body+=T.section('Alternatives to put on your shortlist',p('These options address different scopes. AE is the publisher and one of the providers. Select the work you need before comparing the complete fee; this is not an independent ranking.')+table(('Option','Scope to evaluate','Primary source'),[(E(n),E(scope),a(url,label)) for n,scope,url,label in options]))
  body+=T.section('Compare the cost before switching','<p>'+a(price,'Review '+name+' pricing, published fees, and any clearly labeled AE budget estimate')+'. Ask each alternative to price the same entities, records, returns, planning period, and implementation tasks. A lower filing price or a broader accounting subscription buys different work.</p>')
  body+=T.section('Make the handover concrete',p('Before ending an existing engagement, confirm which tax years and deadlines the replacement accepts. Obtain reconciled books, prior returns, depreciation schedules, entity records, and outstanding notices through the firms’ secure processes. Assign responsibility for work in progress and check any cancellation or renewal dates.')+p(profile['instruction']))
  body+=T.section('Questions for each shortlisted provider','<ul>'+''.join('<li>'+E(q)+'</li>' for q in [profile['question'],'Which named professional owns the deliverable and each implementation step?','Which filings, bookkeeping, specialist work, and future updates are separately priced?','What is the total required first-year cost and what, if anything, renews?'])+'</ul>')
  body+=T.section('Sources and review date',p('Reviewed October 24, 2026 using official provider websites. This is AE’s commercial analysis, not firsthand customer testing. Public claims and savings examples are not independently verified outcomes.')+'<p>'+a(ref['primary_url'],name+' official website')+' · '+a('/compare/tax-advisor-comparison-methodology/','Research methodology')+'</p>')
  body+=T.related_section([(price,name+' pricing'),(vs,name+' vs AE Tax Advisors'),('/compare/','Compare all 100 providers')])+T.CTA_BLOCK
  write(alt,title,desc,body,[ref['primary_url']]+[refmap[x]['primary_url'] for x in peers]+[SITE+'/pricing/']);created.append(alt)
 if s=='tax-hive':
  title='Tax Hive vs AE Tax Advisors: Services, Pricing and Implementation'
  desc='Compare Tax Hive and AE Tax Advisors using their own service and pricing pages, with clear scope and implementation questions.'
  body=T.section('The two engagements to compare',p('Tax Hive’s website describes a customized business plan and offers return, bookkeeping, and entity services. AE offers a defined advisory engagement, with other work separately scoped. Compare the proposals for the same business and tax years.')+'<p>'+a(ref['primary_url'],'Tax Hive’s official planning page')+' · '+a('/pricing/','AE’s published scope and fees')+'</p>')
  body+=T.section('Put responsibilities beside the price',table(('Decision','Tax Hive proposal','AE proposal'),[(E('Plan and implementation'),E('Confirm the written plan, assigned adviser, and implementation support.'),E('Confirm the written advisory deliverables and separately scoped implementation.')),(E('Starting fee'),E('Official page advertises services from $399 without stating billing period or complete scope.'),E('$7,800 standard or $9,800 complex advisory; other services separately priced.')),(E('Future work'),E('The website recommends updating plans annually; request the renewal fee and terms.'),E('No required annual planning renewal in the standard engagement; future work may be separately scoped.'))]))
  body+=T.section('Use your business facts',p(profile['scenario'])+p(profile['instruction']))
  body+=T.section('Source review',p('Reviewed October 24, 2026. AE is the commercial publisher and a provider in this comparison. Marketing promises are not verified tax outcomes.')+'<p>'+a(ref['primary_url'],'Tax Hive service source')+' · '+a('https://taxhive.com/pricing/','Tax Hive pricing source')+'</p>')
  body+=T.related_section([(alt,'Tax Hive alternatives'),(price,'Tax Hive pricing'),('/compare/','Provider directory')])+T.CTA_BLOCK
  write(vs,title,desc,body,[ref['primary_url'],'https://taxhive.com/pricing/',SITE+'/pricing/'])
  write(price,'Tax Hive Pricing: Published Starting Fee and Scope','Review Tax Hive’s $399 advertised starting amount and confirm billing, scope, implementation, and annual update fees.',T.section('Confirm the complete engagement',p('Request a written proposal identifying the tax plan, support period, preparation, bookkeeping, entity services, implementation tasks, and renewal terms. The advertised starting amount does not establish a complete-plan price.'))+T.related_section([(alt,'Tax Hive alternatives'),(vs,'Tax Hive vs AE Tax Advisors')]),['https://taxhive.com/pricing/',ref['primary_url']])

# All three pages carry their own primary-source link and reciprocal research links.
for row in manifest:
 name=row['brand'];s=row['slug'];profile=profiles[s]
 body='<nav aria-label="'+E(name,quote=True)+' research pages"><ul>'+''.join('<li>'+a(row[k].removeprefix(SITE),label)+'</li>' for k,label in [('pricing_url',name+' pricing'),('alternative_url',name+' alternatives'),('comparison_url',name+' vs AE Tax Advisors')])+'</ul></nav><p><strong>Primary provider source:</strong> '+a(row['official_source'],name+'’s own website')+'.</p>'
 markup=T.section('Research '+E(name)+': prices, alternatives and comparison',body)
 for key in ('pricing_url','alternative_url','comparison_url'):
  f=file(row[key]);doc=f.read_text()
  doc=re.sub(r'<!-- provider-triplet:start -->.*?<!-- provider-triplet:end -->','',doc,flags=re.S)
  doc=doc.replace('</main>','<!-- provider-triplet:start -->'+markup+'<!-- provider-triplet:end --></main>',1)
  # Correct old navigation that mislabeled the comparison URL as an alternatives page.
  if old_map.get(s,{}).get('alternative_url')==row['comparison_url']:
   comparison=row['comparison_url'].removeprefix(SITE)
   pattern=r'<a\b([^>]*href=")'+re.escape(comparison)+r'("[^>]*)>([^<]*alternatives[^<]*)</a>'
   doc=re.sub(pattern,lambda m:'<a'+m[1]+row['alternative_url'].removeprefix(SITE)+m[2]+'>'+m[3]+'</a>',doc,flags=re.I)
  if key=='alternative_url' and 'id="provider-review"' not in doc:
   doc=re.sub(r'<section\b(?![^>]*\bid=)([^>]*\bclass="content-section[^\"]*"[^>]*)>',lambda m:'<section id="provider-review"'+m[1]+'>',doc,count=1)
  f.write_text(doc)
holds_file=ROOT/'discovery_review_holds.json';holds=json.loads(holds_file.read_text())
for path in ('/compare/tax-hive-alternatives/','/compare/tax-hive-vs-ae-tax/','/compare/proactive-tax-advisors-alternatives/'):holds.pop(path,None)
dump(holds_file,holds)
coverage=dict(brands=manifest,new_comparisons=[],changed_paths=sorted({r[k].removeprefix(SITE) for r in manifest for k in ('pricing_url','alternative_url','comparison_url')}|{'/compare/'}),review_policy='One dedicated pricing, alternatives and AE comparison page per provider. Official provider sources only for provider claims.')
dump(ROOT/'_gen/competitor-coverage-20261008.json',coverage)
dump(ROOT/'content/provider-page-ownership-20261024.json',dict(reviewed=DATE,provider_count=100,page_count=300,providers=manifest,new_alternatives=created))
with (ROOT/'_gen/competitor-coverage-20261008.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(manifest[0]),lineterminator='\n');w.writeheader();w.writerows(manifest)
hubrows=[(E(r['brand']),a(r['pricing_url'].removeprefix(SITE),'Pricing'),a(r['alternative_url'].removeprefix(SITE),'Alternatives'),a(r['comparison_url'].removeprefix(SITE),'Compare with AE'),a(r['official_source'],'Official website')) for r in sorted(manifest,key=lambda r:r['brand'])]
hub=T.section('100 providers: pricing, alternatives and comparisons',p('Each company has three separate guides, using its own website for provider information. Published fees and AE estimates are labeled in the pricing guides. AE publishes this commercial directory and also offers tax services.')+table(('Provider','Pricing','Alternatives','Comparison','Primary source'),hubrows))
f=ROOT/'compare/index.html';doc=f.read_text()
doc=re.sub(r'<!-- provider-ownership:start -->.*?<!-- provider-ownership:end -->','',doc,flags=re.S)
doc=re.sub(r'<!-- competitor-coverage-20261008:start -->.*?<!-- competitor-coverage-20261008:end -->','',doc,flags=re.S)
doc=doc.replace('</main>','<!-- provider-ownership:start -->'+hub+'<!-- provider-ownership:end --></main>')
if '/assets/competitor-pricing.css' not in doc:doc=doc.replace('</head>','<link rel="stylesheet" href="/assets/competitor-pricing.css?v=20261024"></head>')
f.write_text(doc)
# Latest price renderer applies current fee cards and directory count to the complete set.
runpy.run_path(str(ROOT/'scripts/refresh-competitor-pricing.py'),run_name='__main__')
for filename in ('sitemap.xml','sitemap-comparisons.xml','sitemap-vendor-shopping.xml'):
 f=ROOT/filename;xml=f.read_text()
 for url in sorted({r[k] for r in manifest for k in ('pricing_url','alternative_url','comparison_url')}):
  node='<url><loc>'+E(url)+'</loc><lastmod>'+DATE+'</lastmod></url>'
  pattern=r'<url>\s*<loc>'+re.escape(url)+r'</loc>.*?</url>'
  if re.search(pattern,xml,re.S):xml=re.sub(pattern,node,xml,flags=re.S)
  else:xml=xml.replace('</urlset>',node+'\n</urlset>')
 ET.fromstring(xml);f.write_text(xml)
print(json.dumps({'providers':100,'distinct_pages':300,'new_alternatives':len(created),'official_sources':100}))
