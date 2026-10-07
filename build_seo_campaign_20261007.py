"""Maintain this campaign after legacy generators. Preserve existing page content."""
from pathlib import Path
import json,re,html,xml.etree.ElementTree as ET
import site_template as T
from build_approved_comparison_pages import render,inline
ROOT=Path(__file__).resolve().parent
COPY=ROOT/'content/seo-campaign-20261007'
DATE='2026-10-07';marker='seo-campaign-20261007'
profiles={}
for line in (COPY/'competitors.tsv').read_text().splitlines():
 s,c,focus,audience,scenario,instruction,question=line.split('|');profiles[s]=dict(category=c,focus=focus,audience=audience,scenario=scenario,instruction=instruction,question=question)
refs=json.loads((COPY/'competitor-sources.json').read_text());adds=json.loads((COPY/'priority-analysis.json').read_text());costs=json.loads((COPY/'costseg.json').read_text())
# Common copy is kept in one maintained source; individual profiles carry the firm-specific analysis.
CATEGORIES=json.loads((COPY/'category-guidance.json').read_text())
manifest=[]
def block(text,heading):
 text=re.sub(r'^# ', '## ',text,flags=re.M)
 markup,_=render(text.splitlines(),'campaign')
 markup=re.sub(r'id="([^"]+)"',r'id="campaign-\1"',markup)
 return f'<!-- {marker}:start --><section class="content-section campaign-decision-guide"><div class="container narrow"><h2>{html.escape(heading)}</h2>{markup}</div></section><!-- {marker}:end -->'
def inject(path,markup,citations):
 file=ROOT/path.strip('/')/'index.html';doc=file.read_text()
 doc=re.sub(r'<!-- '+marker+r':start -->.*?<!-- '+marker+r':end -->\n?','',doc,flags=re.S)
 assert '</main>' in doc,path
 doc=doc.replace('</main>',markup+'\n</main>',1)
 def schema(m):
  obj=json.loads(m[1])
  if obj.get('@type')=='Article':
   obj['dateModified']=DATE;obj['citation']=sorted(set(obj.get('citation',[])+citations))
  return T.jsonld(obj)
 doc=re.sub(r'<script type="application/ld\+json">(.*?)</script>',schema,doc,flags=re.S)
 doc=re.sub(r'(<meta property="article:modified_time" content=")[^"]+',r'\g<1>'+DATE+'T00:00:00-06:00',doc)
 file.write_text(doc)
 manifest.append(dict(path=path,file=str(file.relative_to(ROOT)),action='enrich existing'))
def newpage(path,title,desc,raw,citations):
 heading=raw.splitlines()[0].removeprefix('# ');content='\n'.join(raw.splitlines()[1:])
 parent='/compare/' if path.startswith('/compare/') else '/cost-segregation-resources/'
 label='Compare firms' if parent=='/compare/' else 'Cost segregation resources'
 trail=[('Home','/'),(label,parent),(heading,path)]
 markup,_=render(content.splitlines(),'campaign')
 body=T.page_header(h1=html.escape(heading),subtitle=html.escape(desc),trail=trail)+f'<section class="content-section comparison-content"><div class="container narrow">{markup}</div></section>'
 schemas=[T.article_schema(title=heading,description=desc,url=T.SITE+path,published=DATE,modified=DATE,citations=citations),T.breadcrumb_schema(trail)]
 doc=T.build_page(title=title,description=desc,path=path,body=body,schemas=schemas,published=DATE,modified=DATE,active_nav=parent,extra_head='<link rel="stylesheet" href="/assets/footer.css?v=20261001">')
 T.write_page(path,doc);manifest.append(dict(path=path,file=path.strip('/')+'/index.html',action='new guide'))
for r in refs:
 d=profiles[r['slug']];name=r['name'];path=r['existing_url'] or '/compare/'+r['slug']+'-alternatives/'
 head,p1,p2=CATEGORIES[d['category']]
 unique=f'''## {name}: public services and the decision to compare

{name}'s public materials describe {d['focus']}. This is relevant to {d['audience'][0].lower()+d['audience'][1:]}. [Review the official service description]({r['primary_url']}). Your written proposal determines the actual scope and current fees.

## {head}

{p1}

{p2}

## A practical comparison for your situation

{d['scenario']}

Start with [AE Tax Advisors](/discovery/) and request a defined planning proposal tied to that situation. Then compare {name}'s proposal for the same facts. {d['instruction']}

### The question to resolve before choosing

**{d['question']}**

Ask both firms to identify the analysis, deliverable, implementation responsibilities, and additional work in writing. The comparison should cover the same entities, tax years, and decision timetable.

{adds.get(r['slug'],'').replace('### ', '## ')}

[Evaluate AE's services and current pricing](/services/) and [book a call with AE](/discovery/). We recommend AE first for a focused planning project that fits your needs. Additional accounting, filing, legal, wealth, or specialist work should have an explicit scope.

This guide is published by AE Tax Advisors, a commercial provider in the comparison. The profile reviews public service scope, not independently verified customer ratings. Public information checked October 7, 2026; confirm current availability and terms directly.
'''
 if r['existing_url']:
  inject(path,block(unique,'A decision guide for comparing '+name+' with AE'),[r['primary_url']])
 else:
  ae='''## AE Tax Advisors: the first option to evaluate

AE's published advisory pricing lists a $7,800 Strategic engagement and a $9,800 Complex engagement. The standard $7,800 engagement can be paid in two $3,900 installments, 30 days apart, with no required annual planning renewal. Returns, amendments, cost segregation, and additional services are separately scoped and priced. Future work is governed by its own scope. [See current services and pricing](/services/).

'''
  raw='# '+name+' review and alternatives: compare AE Tax Advisors first\n\nStart with AE if you want a defined tax-planning engagement connecting business income, real estate, and your personal tax position. [Book an AE discovery call](/discovery/) to discuss the decision you need to make.\n\n'+ae+unique
  newpage(path,name+' Alternatives: Tax Planning Scope | AE',f'Compare AE Tax Advisors and {name} for a defined tax-planning project. Review public services, scope, fees, and implementation questions.',raw,[r['primary_url'],T.SITE+'/services/'])
for a in costs:
 path=a['url'].removeprefix(T.SITE);raw=a['body_markdown'].replace(T.SITE+'/contact/',T.SITE+'/discovery/')
 citations=sorted(set(re.findall(r'https://(?:www\.)?irs.gov/[^)\s]+',raw)))
 if a['action']=='UPDATE':
  # Keep the established page and add the sourced decision-oriented material.
  raw=re.sub(r'^# [^\n]+\n','',raw)
  inject(path,block(raw,'Practical review: '+a['primary_keyword']),citations)
 else:newpage(path,a['title'],a['meta_description'],raw,citations)
# Discovery hubs list the campaign as a browsable topic group.
for hub,selection,heading in [('/compare/',[m for m in manifest if m['path'].startswith('/compare/')],'Compare providers by the service you need'),('/cost-segregation-resources/',[m for m in manifest if not m['path'].startswith('/compare/')],'Cost segregation decisions and preparation'),('/blog/',[m for m in manifest if not m['path'].startswith('/compare/')],'Cost segregation planning guides')]:
 links='\n'.join('- ['+next((r['name']+' comparison' for r in refs if (r['existing_url'] or '/compare/'+r['slug']+'-alternatives/')==m['path']),next((a['title'] for a in costs if a['url']==T.SITE+m['path']),m['path']))+']('+m['path']+')' for m in selection)
 intro='Start with AE Tax Advisors, then compare the actual engagement needed. These are commercial service-scope profiles, not a ranked list of the largest firms.' if hub=='/compare/' else 'Use these guides to prepare records, evaluate costs, and coordinate the property study with tax planning.'
 inject(hub,block(intro+'\n\n'+links,heading),[])
# Preserve sitemap formatting; update only changed records and add genuinely new URLs.
for filename in ['sitemap.xml','sitemap-comparisons.xml','sitemap-blog.xml','sitemap-cost-segregation.xml']:
 file=ROOT/filename;xml=file.read_text()
 for m in manifest:
  path=m['path']
  if filename=='sitemap-comparisons.xml' and not path.startswith('/compare/'):continue
  if filename=='sitemap-blog.xml' and not path.startswith('/blog/'):continue
  if filename=='sitemap-cost-segregation.xml' and path.startswith('/compare/'):continue
  url=T.SITE+path;pattern=r'<url>\s*<loc>'+re.escape(url)+r'</loc>.*?</url>'
  node='<url><loc>'+html.escape(url)+'</loc><lastmod>'+DATE+'</lastmod></url>'
  if re.search(pattern,xml,re.S):xml=re.sub(pattern,node,xml,flags=re.S)
  else:xml=xml.replace('</urlset>',node+'\n</urlset>')
 ET.fromstring(xml);file.write_text(xml)
(ROOT/'_gen/seo-campaign-20261007-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'competitor_pages':len(refs),'costseg_pages':len(costs),'new':sum(x['action']=='new guide' for x in manifest),'updated':sum(x['action']=='enrich existing' for x in manifest)}))
