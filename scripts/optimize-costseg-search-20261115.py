#!/usr/bin/env python3
"""Apply the reviewed cost-seg navigation/snippet pass to existing source pages.

No provider facts or source-review dates are refreshed by this script. The
manifest records the exact existing introductions to protect researched copy.
Uses the standard library; production stages committed HTML, not this generator.
"""
from pathlib import Path
import json, re, html
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'content/costseg-search-optimization-20261115.json').read_text())
SITE='https://www.aetaxadvisors.com'
DATE=DATA['date']
E=html.escape
providers=DATA['providers']
changed=set()

def link(path,label): return '<a href="'+E(path,quote=True)+'">'+E(label)+'</a>'
def path(url): return urlparse(url).path

def update_metadata(doc,description,title=None):
 if title: doc=re.sub(r'<title>.*?</title>','<title>'+E(title)+'</title>',doc,count=1,flags=re.S)
 for key,value in [('description',description),('og:description',description),('twitter:description',description),('og:title',title),('twitter:title',title)]:
  if value is not None:
   doc=re.sub(r'(<meta\s+(?:name|property)="'+re.escape(key)+r'"\s+content=")[^"]*("\s*/?>)',lambda m:m[1]+E(value,quote=True)+m[2],doc,count=1)
 return doc

def save(route,doc):
 f=ROOT/route.strip('/')/'index.html'
 if f.read_text()!=doc: f.write_text(doc);changed.add(route)

def block_replace(doc,marker,block):
 pattern=r'<!-- '+re.escape(marker)+r':start -->.*?<!-- '+re.escape(marker)+r':end -->'
 tagged='<!-- '+marker+':start -->'+block+'<!-- '+marker+':end -->'
 if re.search(pattern,doc,re.S):return re.sub(pattern,lambda _:tagged,doc,flags=re.S)
 return doc.replace('</main>',tagged+'\n</main>',1)

for row in providers:
 name=row['name'];slug=row['slug'];alt=path(row['alternative_url'])
 routes=[(kind,path(row[key])) for kind,key in [('alternative','alternative_url'),('pricing','pricing_url'),('comparison','comparison_url')] if row[key]]
 for kind,route in routes:
  f=ROOT/route.strip('/')/'index.html';doc=f.read_text()
  # Keep the top-of-page triplet navigation; add it where legacy pages lack it.
  nav='<nav class="provider-guide-nav container narrow" aria-label="'+E(name,quote=True)+' comparison guides">'
  for target,key,label in [('alternative','alternative_url','Alternatives'),('pricing','pricing_url','Pricing and fees'),('comparison','comparison_url','Compare with AE')]:
   if row[key]:nav+='<a href="'+path(row[key])+'"'+(' aria-current="page"' if kind==target else '')+'>'+label+'</a>'
  if not row['pricing_url']:nav+=link('/cost-segregation-study-cost-pricing/','AE study pricing')
  nav+=link('/compare/#costseg-'+slug,'All study providers')+'</nav>'
  if 'class="provider-guide-nav ' in doc:
   doc=re.sub(r'<nav class="provider-guide-nav\b.*?</nav>',lambda _:nav,doc,count=1,flags=re.S)
  else:
   main=re.search(r'(<main\b[^>]*>)(.*?)(</main>)',doc,re.S);body=main[2]
   # The first section is the page header, not the shared site navigation.
   idx=body.index('</section>')+len('</section>')
   doc=doc[:main.start(2)]+body[:idx]+nav+body[idx:]+doc[main.end(2):]
  main=re.search(r'(<main\b[^>]*>)(.*?)(</main>)',doc,re.S)
  body=main[2].replace('href="/discovery/"','href="/cost-seg-discovery/"')
  shared=json.loads((ROOT/'scripts/shared-discovery-cta.json').read_text())
  old=r'\s+'.join(re.escape(word) for word in shared['old_paragraph'].split())
  body=re.sub(r'(<p>)'+old+r'(</p>)',lambda m:m[1]+shared['new_paragraph']+m[2],body)
  body=body.replace('>Book a Call<','>Book a Cost Seg Discovery Call<').replace('>Discuss Your Property<','>Discuss Your Cost Seg Study<')
  doc=doc[:main.start(2)]+body+doc[main.end(2):]
  if kind=='alternative':
   decision='<p class="costseg-decision"><strong>Start with '+E(row['focus'])+'.</strong> '+E(row['question'])+'</p>'
   if 'class="costseg-decision"' in doc:doc=re.sub(r'<p class="costseg-decision">.*?</p>',lambda _:decision,doc,count=1,flags=re.S)
   else:
    assert row['original_intro'] in doc,slug
    doc=doc.replace(row['original_intro'],decision+row['original_intro'],1)
   desc=f"Compare {name} alternatives for {row['focus']}. Review study fees, report support and CPA handoff."
   if len(desc)>180:desc=f"Compare {name} alternatives for {row['focus']}. Review fees and CPA handoff."
   # Preserve established high-ranking titles. Improve only bare legacy labels.
   title=name+' Alternatives: Study Scope & Fees | AE Tax Advisors' if row['title']==name+' Alternatives | AE Tax Advisors' else None
   doc=update_metadata(doc,desc,title)
   def schema_edit(m):
    obj=json.loads(m[1])
    if obj.get('@type')=='Article':
     obj['description']=desc;obj['dateModified']=DATE
     obj['about']={'@type':'Organization','name':name,'url':row['official_source']}
    if title and obj.get('@type')=='Article':obj['headline']=title.removesuffix(' | AE Tax Advisors')
    return '<script type="application/ld+json">\n'+json.dumps(obj,indent=2,ensure_ascii=False)+'\n</script>'
   doc=re.sub(r'<script type="application/ld\+json">(.*?)</script>',schema_edit,doc,flags=re.S)
   doc=re.sub(r'(<meta property="article:modified_time" content=")[^"]*',r'\g<1>'+DATE+'T00:00:00-06:00',doc,count=1)
   # Nine older pages put advisory ahead of a standalone-study explanation.
   if not row['pricing_url']:
    offer='<aside class="costseg-study-scope container narrow" aria-label="AE standalone study scope"><h2>Compare a standalone study with a standalone study</h2><p>AE publishes cost segregation studies at <strong>$1 per square foot, with a $2,000 minimum per study</strong>. Advisory and return work are separately scoped; the $7,800 advisory engagement below is a different service.</p><p>'+link('/pricing/#service-pricing','Review AE service pricing')+' · '+link('/cost-seg-discovery/','Discuss your property study')+'</p></aside>'
    if 'class="costseg-study-scope ' not in doc:doc=doc.replace(nav,nav+offer,1)
   # A compact direct path from every alternatives page to the full directory.
   directory='<p class="costseg-directory-path container narrow">'+link('/compare/#costseg-'+slug,'Browse study providers and their pricing guides')+' · '+link('/compare/best-cost-segregation-companies/','How to compare cost segregation companies')+'</p>'
   if 'class="costseg-directory-path ' not in doc:doc=doc.replace('</main>',directory+'</main>',1)
  if '/assets/competitor-pricing.css' not in doc:doc=doc.replace('</head>','<link rel="stylesheet" href="/assets/competitor-pricing.css?v=20261115">\n</head>',1)
  else:doc=re.sub(r'(/assets/competitor-pricing\.css)(?:\?v=[^"\s]+)?',r'\g<1>?v=20261115',doc)
  save(route,doc)

# Identity and proposal terms verified on the provider's own website, 2026-11-15.
route='/compare/cost-seg-america-alternatives/'
doc=(ROOT/route.strip('/')/'index.html').read_text()
identity='<section class="section" id="cost-seg-america-identity"><div class="container narrow"><h2>Cost Seg America: identify the firm and compare the report</h2><p>This guide concerns '+link('https://www.costsegamerica.com/','Cost Seg America, Inc.')+'. Its website describes component-level engineering and a report package with fixed-asset and depreciation schedules. Compare the written investigation scope, documentation and audit-response terms with each alternative’s proposal. Provider description checked November 15, 2026; AE has not independently verified service delivery or advertised outcomes.</p><p>For this shortlist, start with AE Tax Advisors, '+link('/compare/segpro-solutions-alternatives/','SegPro Solutions')+' and '+link('/compare/modern-cfo-alternatives/','Modern CFO')+'. Ask all three for the same property and report deliverables. If you meant the separately named Remote Cost Seg, use the '+link('/compare/remote-cost-seg-alternatives/','Remote Cost Seg alternatives guide')+'.</p></div></section>'
# Put the unique identity section before the generic proposal checklist.
if 'id="cost-seg-america-identity"' not in doc:
 marker=re.search(r'<section\b[^>]*>\s*<div[^>]*>\s*<h2>Ask for a proposal you can compare</h2>',doc)
 assert marker
 doc=doc[:marker.start()]+identity+doc[marker.start():]
save(route,doc)

# Repair the legacy Bedford list: linked article titles were presented as firms.
route='/compare/bedford-cost-segregation-alternatives/'
doc=(ROOT/route.strip('/')/'index.html').read_text()
pattern=r'(<h2>Bedford Cost Segregation alternatives to compare</h2>).*?(?=</div>\s*</section>)'
shortlist='<p>Compare proposals for the same commercial property. These are research paths, not a quality ranking:</p><ul><li>'+link('/cost-segregation-study/','AE Tax Advisors standalone study scope')+'</li><li>'+link('/compare/madison-specs-alternatives/','Madison SPECS study options')+'</li><li>'+link('/compare/engineered-tax-services-alternatives/','Engineered Tax Services study options')+'</li><li>'+link('/compare/capstan-tax-strategies-alternatives/','Capstan Tax Strategies study options')+'</li></ul><p>Read each provider’s official sources and obtain a current property-specific quote. Compare inspection, engineering records, component schedules, report support and separately scoped filing work.</p>'
doc,n=re.subn(pattern,lambda m:m[1]+shortlist,doc,count=1,flags=re.S);assert n==1
save(route,doc)

# Consolidate seven repetitive cost-seg cohort blocks into one complete directory.
for route in ['/compare/','/compare/best-cost-segregation-companies/']:
 doc=(ROOT/route.strip('/')/'index.html').read_text()
 pattern=r'<!-- (costseg-[a-z0-9-]+):start -->.*?<!-- \1:end -->'
 blocks=re.findall(pattern,doc,re.S)
 pair_links={}
 for m in re.finditer(pattern,doc,re.S):
  for href,label in re.findall(r'<a href="([^"]+)">(.*?)</a>',m[0],re.S):
   if '-vs-' in href:pair_links[href]=html.unescape(re.sub('<[^>]+>','',label))
 # Retain the original marked blocks (and all pair links) so cohort rerenders
 # remain reversible. Only their repeated explanatory paragraphs are reduced.
 for m in list(re.finditer(pattern,doc,re.S))[::-1]:
  pairs=[(h,l) for h,l in re.findall(r'<a href="([^"]+)">(.*?)</a>',m[0],re.S) if '-vs-' in h]
  compact='<!-- '+m[1]+':start --><details class="costseg-pair-links container narrow"><summary>More provider-to-provider comparisons</summary><ul>'+''.join('<li><a href="'+h+'">'+l+'</a></li>' for h,l in pairs)+'</ul></details><!-- '+m[1]+':end -->'
  doc=doc[:m.start()]+compact+doc[m.end():]
 rows=[];ordered=sorted(providers,key=lambda x:x['name'].casefold())
 for row in ordered:
  choices=[link(path(row['alternative_url']),'Alternatives')]
  if row['pricing_url']:choices.append(link(path(row['pricing_url']),'Pricing'))
  if row['comparison_url']:choices.append(link(path(row['comparison_url']),'Compare with AE'))
  rows.append('<tr id="costseg-'+row['slug']+'"><th scope="row">'+E(row['name'])+'</th><td>'+E(row['focus'].capitalize())+'</td><td>'+ ' · '.join(choices)+'</td></tr>')
 directory='<section id="cost-segregation-providers" class="section costseg-provider-directory"><div class="container narrow"><h2>Find a cost segregation provider comparison</h2><p>Browse '+str(len(providers))+' provider names covered in AE’s comparison library, including alternative brand names. Choose an alternatives guide to build a shortlist, a pricing guide to evaluate fees, or a direct AE comparison to examine scope. This alphabetical directory is not an independent ranking; AE publishes it and also supplies studies.</p><p>'+link('/cost-segregation-study-cost-pricing/','AE standalone study pricing')+' · '+link('/cost-seg-discovery/','Discuss a study proposal')+'</p><div class="costseg-directory-scroll" role="region" aria-label="Cost segregation provider guides" tabindex="0"><table><caption>Compare property fit, report scope and complete fees. Availability and contract terms require a current proposal.</caption><thead><tr><th scope="col">Provider</th><th scope="col">Comparison focus</th><th scope="col">Read the guides</th></tr></thead><tbody>'+''.join(rows)+'</tbody></table></div></div></section>'
 doc=block_replace(doc,'costseg-search-directory-20261115',directory)
 schema={'@context':'https://schema.org','@type':'ItemList','name':'Cost segregation provider comparison guides','itemListOrder':'https://schema.org/ItemListOrderAscending','numberOfItems':len(ordered),'itemListElement':[{'@type':'ListItem','position':i+1,'item':{'@type':'WebPage','name':row['name']+' alternatives','url':row['alternative_url']}} for i,row in enumerate(ordered)]}
 schema_tag='<script type="application/ld+json" id="costseg-directory-schema">'+json.dumps(schema,ensure_ascii=False)+'</script>'
 if 'id="costseg-directory-schema"' in doc:doc=re.sub(r'<script type="application/ld\+json" id="costseg-directory-schema">.*?</script>',lambda _:schema_tag,doc,flags=re.S)
 else:doc=doc.replace('</head>',schema_tag+'\n</head>',1)
 if '/assets/competitor-pricing.css' not in doc:doc=doc.replace('</head>','<link rel="stylesheet" href="/assets/competitor-pricing.css?v=20261115">\n</head>',1)
 # Make the new directory visible without traversing the full older library.
 jump='<p class="container narrow costseg-directory-jump">'+link('#cost-segregation-providers','Jump to all 46 cost segregation provider guides')+'</p>'
 if 'class="container narrow costseg-directory-jump"' not in doc:
  main=re.search(r'<main\b[^>]*>',doc);start=doc.index('</section>',main.end())+len('</section>');doc=doc[:start]+jump+doc[start:]
 save(route,doc)

reviewed=ROOT/'content/reviewed-content-lastmod.json';dates=json.loads(reviewed.read_text())
for row in providers:dates[path(row['alternative_url'])]=DATE
for route in ['/compare/','/compare/best-cost-segregation-companies/']:dates[route]=DATE
reviewed.write_text(json.dumps(dates,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'providers':len(providers),'changed_pages':len(changed),'routes':sorted(changed)},indent=2))
