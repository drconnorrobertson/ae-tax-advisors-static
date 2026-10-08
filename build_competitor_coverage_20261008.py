"""Complete 100-brand coverage with one canonical owner for each intent.

Run after build_seo_campaign_20261007.py. Review intent is integrated with the
established source-based alternatives profiles rather than spun into copies.
"""
import csv,html,json,re,subprocess,xml.etree.ElementTree as ET
from pathlib import Path
import site_template as T
from discovery_inventory import eligible,redirects
ROOT=Path(__file__).resolve().parent
DATE='2026-10-08'
MARK='competitor-coverage-20261008'
REFS=json.loads((ROOT/'content/seo-campaign-20261007/competitor-sources.json').read_text())
NOTES=json.loads((ROOT/'content/competitor-comparison-notes-20261008.json').read_text())
PROFILES={}
for line in (ROOT/'content/seo-campaign-20261007/competitors.tsv').read_text().splitlines():
 s,c,focus,audience,scenario,instruction,question=line.split('|')
 PROFILES[s]=dict(category=c,focus=focus,audience=audience,scenario=scenario,instruction=instruction,question=question)
ALIASES={'cost-segregation-authority':'cost-seg-authority'}
REVIEWED_EXISTING={'cost-segregation-guys','maven-cost-segregation'}
E=html.escape
def paragraph(s):return '<p>'+E(s)+'</p>'
def link(path,label):return '<a href="'+E(path,quote=True)+'">'+E(label)+'</a>'
def file(path):return ROOT/path.strip('/')/'index.html'
def owners(r):
 s=r['slug'];alt=r['existing_url'] or '/compare/'+s+'-alternatives/'
 candidates=['/compare/'+s+'-vs-ae-tax/','/compare/ae-tax-vs-'+s+'/']
 if s in ALIASES:candidates.insert(0,'/compare/'+ALIASES[s]+'-vs-ae-tax/')
 candidates=[p for p in candidates if file(p).exists() and eligible(file(p))]
 if len(candidates)>1:raise ValueError('Competing canonical owners for '+s+': '+str(candidates))
 return alt,candidates[0] if candidates else '/compare/'+s+'-vs-ae-tax/'
def strip_block(doc):return re.sub(r'<!-- '+MARK+r':start -->.*?<!-- '+MARK+r':end -->\n?','',doc,flags=re.S)
def patch(path,markup):
 doc=strip_block(file(path).read_text())
 doc=doc.replace('</main>','<!-- '+MARK+':start -->'+markup+'<!-- '+MARK+':end -->\n</main>',1)
 def update(m):
  obj=json.loads(m[1])
  if obj.get('@type')=='Article':obj['dateModified']=DATE
  return T.jsonld(obj)
 doc=re.sub(r'<script type="application/ld\+json">(.*?)</script>',update,doc,flags=re.S)
 doc=re.sub(r'(<meta property="article:modified_time" content=")[^"]+',r'\g<1>'+DATE+'T00:00:00-06:00',doc)
 file(path).write_text(doc)
def related(r,alt,vs):
 return T.section('Research '+E(r['name'])+' before deciding','<ul><li>'+link(alt+'#provider-review',r['name']+' service review')+'</li><li>'+link(alt,r['name']+' alternatives')+'</li><li>'+link(vs,r['name']+' versus AE Tax Advisors')+'</li></ul>')
def new_comparison(r,alt,path):
 published=DATE
 if file(path).exists():
  old=re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})',file(path).read_text())
  if old:published=old[1]
 s=r['slug'];d=PROFILES[s];name=r['name'];title=name+' vs AE Tax Advisors: Scope & Fit'
 desc='Compare '+name+' and AE Tax Advisors on the work you need, proposal scope, implementation responsibilities, and complete engagement cost.'
 trail=[('Home','/'),('Compare firms','/compare/'),(name+' vs AE',path)]
 body=T.page_header(h1=E(title),subtitle=E(desc),trail=trail)
 body+=T.section('Choose by the work you need',paragraph(NOTES[s]))
 body+=T.section('The provider offering to evaluate',paragraph(name+' is considered here for '+d['focus']+'.')+'<p>'+link(r['primary_url'],'Read '+name+' official service materials')+'.</p>')
 body+=T.section('The decision your proposal should answer',paragraph(d['scenario'])+'<h3>'+E(d['question'])+'</h3>'+paragraph(d['instruction']))
 rows=[('Starting scope',name+': '+d['focus'],'Business and property owner advisory, separately scoped'),('Decision to resolve',d['question'],'Request a project answering: '+d['question']),('Implementation boundary',d['instruction'],'Assign implementation for the '+name+' comparison question above.'),('Engagement cost','Request an itemized '+name+' quote.','Strategic $7,800; Complex $9,800; additional services separate.')]
 table='<div class="ae-table-scroll"><table class="compare-table"><caption>Service-scope comparison; written proposals control actual deliverables.</caption><thead><tr><th scope="col">Decision</th><th scope="col">'+E(name)+'</th><th scope="col">AE Tax Advisors</th></tr></thead><tbody>'
 for label,left,right in rows:table+='<tr><th scope="row">'+E(label)+'</th><td>'+E(left)+'</td><td>'+E(right)+'</td></tr>'
 body+=T.section('Compare the same assignment',table+'</tbody></table></div>')
 body+=T.section('Cost and source checks','<p>'+link('/pricing/','AE fee schedule')+' · '+link(r['primary_url'],name+' current offering')+'. Compare total costs for '+E(name)+' and AE against the assignment above, including optional reporting work.</p><p>October 8, 2026 editorial analysis; October 7 provider research supplemented by current public-source checks. Published by competing provider AE Tax Advisors. No customer scores or firsthand testing. '+link('/compare/tax-advisor-comparison-methodology/','Research methodology')+'.</p>')
 body+=related(r,alt,path)+T.CTA_BLOCK
 schemas=[T.article_schema(title=title,description=desc,url=T.SITE+path,published=published,modified=DATE,section='Tax advisor comparisons',citations=[r['primary_url'],T.SITE+'/pricing/']),T.breadcrumb_schema(trail)]
 doc=T.build_page(title=title+' | AE',description=desc,path=path,body=body,schemas=schemas,published=published,modified=DATE,active_nav='/compare/',extra_head='<link rel="stylesheet" href="/assets/footer.css?v=20261001">')
 T.write_page(path,'\n'.join(line.rstrip() for line in doc.splitlines())+'\n')
def main():
 assert len(REFS)==100 and len({x['slug'] for x in REFS})==100
 assert len({x['primary_url'] for x in REFS})==100
 manifest=[];changed=set();new=[]
 original=set(subprocess.check_output(['git','ls-files'],cwd=ROOT,text=True).splitlines())
 # These two held owners were reviewed against current official materials;
 # rewrite unsupported old claims before clearing their discovery holds.
 holds_path=ROOT/'discovery_review_holds.json';holds=json.loads(holds_path.read_text())
 for r in REFS:
  if r['slug'] in REVIEWED_EXISTING:
   alt=r['existing_url'] or '/compare/'+r['slug']+'-alternatives/'
   vs='/compare/'+r['slug']+'-vs-ae-tax/'
   new_comparison(r,alt,vs);holds.pop(vs,None)
 holds_path.write_text(json.dumps(holds,indent=2)+'\n')
 from discovery_inventory import review_holds
 review_holds.cache_clear()
 for r in REFS:
  alt,vs=owners(r)
  assert eligible(file(alt)),alt
  exists=str(file(vs).relative_to(ROOT)) in original
  if not exists:new_comparison(r,alt,vs);new.append(vs)
  doc=strip_block(file(alt).read_text())
  # Existing campaign already supplies each brand's substantive public-scope
  # review. Give that same answer an explicit review anchor, not a copy URL.
  pattern=r'(<section class="content-section campaign-decision-guide")([^>]*><div class="container narrow"><h2>)(.*?)(</h2>)'
  if re.search(pattern,doc,re.S):
   doc=re.sub(pattern,lambda m:m[1]+' id="provider-review"'+m[2]+E(r['name']+' review: service scope and buyer fit')+m[4],doc,count=1,flags=re.S)
  else:
   assert 'comparison-content' in doc,alt
   doc=doc.replace('<section class="content-section comparison-content">','<section class="content-section comparison-content" id="provider-review">',1)
  # Repeated runs preserve one stable review anchor.
  doc=doc.replace('id="provider-review" id="provider-review"','id="provider-review"')
  file(alt).write_text(doc)
  review_note=paragraph('This '+r['name']+' review evaluates public service descriptions and the engagement questions below. It does not verify customer experiences or independently substantiate advertised savings. Ask '+r['name']+' for a written proposal addressing: '+PROFILES[r['slug']]['question'])
  if r['slug']=='fox-and-company-cpas':review_note+=paragraph('Fox & Company’s official homepage lists a seasonal closure to new clients from September 1 through mid-May and offers a waitlist. Confirm acceptance directly before relying on onboarding for an upcoming deadline.')
  patch(alt,T.section('How to use this service review',review_note)+related(r,alt,vs))
  if exists:patch(vs,related(r,alt,vs))
  changed.update([alt,vs])
  manifest.append(dict(slug=r['slug'],brand=r['name'],alternative_url=T.SITE+alt,comparison_url=T.SITE+vs,review_url=T.SITE+alt+'#provider-review',review_owner='integrated source-based review on existing alternatives page',comparison_action='reused canonical owner' if exists else 'new comparison',official_source=r['primary_url'],editorial_date=DATE))
 # Bracket Partners is a real-estate incentive firm, not Bracket Tax Co.
 path=next(x['alternative_url'].removeprefix(T.SITE) for x in manifest if x['slug']=='bracket-partners')
 doc=file(path).read_text()
 doc=doc.replace('tax planning and advisory services. This is relevant to owners comparing a planning-focused advisory relationship.','tax-credit, incentive, cost segregation, and real estate development advisory services. This is relevant to developers and property owners evaluating specialist project work.')
 file(path).write_text(doc)
 rows=''.join('<tr><th scope="row">'+E(r['brand'])+'</th><td>'+link(r['alternative_url'].removeprefix(T.SITE),'Alternatives')+'</td><td>'+link(r['comparison_url'].removeprefix(T.SITE),'AE comparison')+'</td><td>'+link(r['review_url'].removeprefix(T.SITE),'Service review')+'</td></tr>' for r in manifest)
 hub=T.section('100 provider research paths','<p>Each provider has an alternatives guide, an AE comparison, and a source-based service review. Reviews share the established alternatives page when they answer the same research intent. These are AE-published commercial analyses, not customer ratings or an independent ranking.</p><div class="ae-table-scroll"><table class="compare-table"><caption>Provider directory: alternatives, direct comparisons, and public-service reviews.</caption><thead><tr><th scope="col">Provider</th><th scope="col">Alternatives</th><th scope="col">Compare AE</th><th scope="col">Review</th></tr></thead><tbody>'+rows+'</tbody></table></div>')
 patch('/compare/',hub);changed.add('/compare/')
 for filename in ['sitemap.xml','sitemap-comparisons.xml']:
  p=ROOT/filename;xml=p.read_text()
  for path in sorted(changed):
   url=T.SITE+path;node='<url><loc>'+E(url)+'</loc><lastmod>'+DATE+'</lastmod></url>';pattern=r'<url>\s*<loc>'+re.escape(url)+r'</loc>.*?</url>'
   if re.search(pattern,xml,re.S):xml=re.sub(pattern,node,xml,flags=re.S)
   else:xml=xml.replace('</urlset>',node+'\n</urlset>')
  ET.fromstring(xml);p.write_text(xml)
 out=ROOT/'_gen/competitor-coverage-20261008.json';out.write_text(json.dumps(dict(brands=manifest,new_comparisons=new,changed_paths=sorted(changed),review_policy='Reuse established alternatives owners for overlapping service-review intent; no duplicate review URLs.'),indent=2)+'\n')
 with (ROOT/'_gen/competitor-coverage-20261008.csv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(manifest[0]),lineterminator="\n");w.writeheader();w.writerows(manifest)
 print(json.dumps({'brands':len(manifest),'new_comparisons':len(new),'changed_pages':len(changed),'integrated_reviews':len(manifest)}))
if __name__=='__main__':main()
