#!/usr/bin/env python3
"""Replace unsupported legacy comparisons and align search snippets with visible scope."""
import html,json,re,runpy,sys,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
import site_template as T
E=html.escape;SITE=T.SITE;DATE='2026-10-24'
rows=json.loads((ROOT/'content/provider-page-ownership-20261024.json').read_text())['providers']
prices={r['slug']:r for r in json.loads((ROOT/'content/vendor-pricing-20261024.json').read_text())}
profiles={line.split('|')[0]:dict(zip(('category','focus','audience','scenario','instruction','question'),line.split('|')[1:])) for line in (ROOT/'content/seo-campaign-20261007/competitors.tsv').read_text().splitlines()}
facts=json.loads((ROOT/'content/comparison-source-corrections-20261024.json').read_text())
def p(s):return '<p>'+E(s)+'</p>'
def a(url,label):return '<a href="'+E(url,quote=True)+'">'+E(label)+'</a>'
def file(url):return ROOT/url.removeprefix(SITE).strip('/')/'index.html'
def table(headers,items):return '<div class="pricing-table-scroll" role="region" aria-label="Engagement comparison" tabindex="0"><table><thead><tr>'+''.join('<th scope="col">'+E(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr><th scope="row">'+E(label)+'</th><td>'+left+'</td><td>'+right+'</td></tr>' for label,left,right in items)+'</tbody></table></div>'
rebuilt=[]
for r in rows:
 s=r['slug']
 if s not in facts:continue
 d=facts[s];profile=profiles[s];name=r['brand'];url=r['comparison_url'];path=url.removeprefix(SITE)
 old=file(url).read_text();m=re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})',old);published=m[1] if m else DATE
 title=name+' vs AE Tax Advisors: Pricing and Services'
 desc='Compare '+name+' and AE Tax Advisors using official services, published fees or labeled estimates, implementation duties, and complete project cost.'
 trail=[('Home','/'),('Compare','/compare/'),(name+' vs AE Tax Advisors',path)]
 body=T.page_header(h1=E(title),subtitle=E(desc),trail=trail)
 body+=T.section('What '+E(name)+' publishes',p(d['offering'])+'<p>'+a(d['source'],'Read the official '+name+' source')+'. The service description establishes the public offering; the signed agreement establishes your scope.</p>')
 body+=T.section('Compare responsibilities alongside the fee',table(('Workstream',name,'AE Tax Advisors'),[
  ('Service model',E(d['offering']),'A defined owner or investor advisory engagement; studies, returns, amendments, and other work separately scoped.'),
  ('Implementation',E(d['implementation']),'Ask for the recommendation, assigned professional, deadline, and evidence of completion for each contracted task.'),
  ('Pricing evidence',a(r['pricing_url'].removeprefix(SITE),'See published fees or the explicitly labeled AE budgeting estimate'),'Standard advisory $7,800; complex advisory $9,800. Additional services have separate prices.'),
  ('Future commitments','Confirm the service period, required companions, optional work, and any renewal fee.','No required annual planning renewal under the standard advisory engagement; new work can require a new scope.'),
  ('The decision to resolve',E(profile['question']),E('Request an AE proposal answering the same question: '+profile['question']))]))
 body+=T.section('Which proposal fits this situation?',p(profile['scenario'])+p(d['decision'])+p(profile['instruction']))
 if profile['category'] in ('costseg','software'):
  body+=T.section('Separate the study from advisory and filing',p('AE’s published standalone study rate is $1 per square foot with a $2,000 minimum. At that rate, a 1,500-square-foot study has a $2,000 base price; a 3,000-square-foot study has a $3,000 base price. These are arithmetic examples before separately scoped advisory, filing, amendments, or other work.')+'<p>'+a('/pricing/','Check AE’s current study and service prices')+'. Add the corresponding work to the other proposal before comparing totals.</p>')
 body+=T.section('A practical request for both firms','<blockquote>'+p('Please price this engagement for the same entities, properties, records, and tax years. '+profile['question']+' Identify the work product, responsible professional, implementation tasks, filing responsibility, support period, first-year fee, exclusions, and any continuing commitment.')+'</blockquote>')
 body+=T.section('Official sources and review',p('Reviewed October 24, 2026. AE is the publisher and a competing provider. This is a review of public service information, not an independent ranking or firsthand test. Delivery times, advertised tax savings, and guarantees are not substituted for a written scope or a verified client outcome.')+'<p>'+a(d['source'],name+' official service source')+' · '+a(r['official_source'],'Provider source in the directory')+' · '+a('/pricing/','AE service pricing')+' · '+a('/compare/tax-advisor-comparison-methodology/','Comparison methodology')+'</p>')
 body+=T.related_section([(r['pricing_url'].removeprefix(SITE),name+' pricing'),(r['alternative_url'].removeprefix(SITE),name+' alternatives'),('/compare/competitor-pricing/','Compare all 100 providers')])
 schemas=[T.article_schema(title=title,description=desc,url=url,published=published,modified=DATE,section='Tax provider comparison',citations=[d['source'],r['official_source'],SITE+'/pricing/']),T.breadcrumb_schema(trail)]
 doc=T.build_page(title=title+' | AE Tax Advisors',description=desc,path=path,body=body,schemas=schemas,published=published,modified=DATE,active_nav='/compare/',extra_head='<link rel="stylesheet" href="/assets/competitor-pricing.css?v=20261024">')
 file(url).write_text('\n'.join(line.rstrip() for line in doc.splitlines())+'\n');rebuilt.append(path)

# Restore the shared current price cards and all reciprocal links after targeted rebuilds.
runpy.run_path(str(ROOT/'scripts/complete-provider-triplets.py'),run_name='__main__')
metadata=[]
for r in rows:
 name=r['brand'];fee=prices[r['slug']]
 for key in ('pricing_url','alternative_url','comparison_url'):
  f=file(r[key]);text=f.read_text()
  if key=='pricing_url':
   title=name+(' Pricing: Published Fees and Scope' if fee['kind']=='published' else ' Pricing: Cost Estimates and Scope')
   desc=('Review '+name+' pricing, published fees, billing terms, and exclusions using official sources. Compare the complete service scope with AE.' if fee['kind']=='published' else 'Review '+name+' pricing with a clearly labeled AE budget estimate, official service sources, and questions about the complete first-year cost.')
  elif key=='alternative_url':
   title=name+' Alternatives: Fees and Service Fit'
   desc='Compare alternatives to '+name+' by services, pricing, client fit, and implementation responsibility. Use official sources and matching written proposals.'
  else:
   title=name+' vs AE Tax Advisors: Pricing and Services'
   desc='Compare '+name+' and AE Tax Advisors on pricing, service scope, and implementation. Published fees and AE budget estimates are clearly distinguished.'
  page_title=title+' | AE Tax Advisors'
  text=re.sub(r'<title>.*?</title>','<title>'+E(page_title)+'</title>',text,count=1,flags=re.S)
  text=re.sub(r'<h1\b[^>]*>.*?</h1>','<h1>'+E(title)+'</h1>',text,count=1,flags=re.S)
  def meta(m):
   raw=m[0]
   if re.search(r'(?:name|property)="(?:description|og:description|twitter:description)"',raw):return re.sub(r'content="[^"]*"','content="'+E(desc,quote=True)+'"',raw)
   if re.search(r'(?:name|property)="(?:og:title|twitter:title)"',raw):return re.sub(r'content="[^"]*"','content="'+E(page_title,quote=True)+'"',raw)
   return raw
  text=re.sub(r'<meta\b[^>]*>',meta,text)
  def schema(m):
   obj=json.loads(m[1])
   def walk(v):
    if isinstance(v,list):
     for x in v:walk(x)
    elif isinstance(v,dict):
     if v.get('@type') in ('Article','BlogPosting','WebPage'):
      if 'headline'in v:v['headline']=title
      if 'name'in v and v.get('@type')=='WebPage':v['name']=title
      if 'description'in v:v['description']=desc
      v['dateModified']=DATE
     for x in v.values():
      if isinstance(x,(dict,list)):walk(x)
   walk(obj);return T.jsonld(obj)
  text=re.sub(r'<script type="application/ld\+json">\s*(.*?)\s*</script>',schema,text,flags=re.S)
  text=re.sub(r'<!-- provider-guide-nav:start -->.*?<!-- provider-guide-nav:end -->','',text,flags=re.S)
  nav='<nav class="provider-guide-nav container narrow" aria-label="'+E(name,quote=True)+' guides">'+''.join('<a href="'+r[k].removeprefix(SITE)+'"'+(' aria-current="page"' if k==key else '')+'>'+label+'</a>' for k,label in [('pricing_url','Pricing and fees'),('alternative_url','Alternatives'),('comparison_url','Compare with AE')])+'</nav>'
  text=re.sub(r'(<section class="content-section\b)',lambda m:'<!-- provider-guide-nav:start -->'+nav+'<!-- provider-guide-nav:end -->'+m[1],text,count=1)
  f.write_text(text);metadata.append(r[key].removeprefix(SITE))

# Existing links elsewhere should show the corrected page identity rather than old assertions.
changed_labels={}
for path in rebuilt:
 r=next(r for r in rows if r['comparison_url']==SITE+path)
 changed_labels[path]=r['brand']+' vs AE Tax Advisors: Pricing and Services'
for f in (ROOT/'compare').glob('*/index.html'):
 text=f.read_text();old=text
 for path,label in changed_labels.items():
  pattern=r'(<a\b[^>]*href="(?:'+re.escape(SITE)+r')?'+re.escape(path)+r'"[^>]*>)([^<]*)(</a>)'
  text=re.sub(pattern,lambda m:m[1]+E(label)+m[3],text)
 if text!=old:f.write_text(text)

manifest={'reviewed':DATE,'corrected_comparisons':rebuilt,'search_metadata_pages':metadata,'corrections':{s:d['correction'] for s,d in facts.items()}}
(ROOT/'content/comparison-quality-release-20261024.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'corrected_comparisons':len(rebuilt),'search_metadata_pages':len(metadata)}))
