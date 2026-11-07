#!/usr/bin/env python3
"""Add intent-specific decision support and a crawlable hundred-firm navigation hub."""
import html,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));import site_template as T
E=html.escape;DATE='2026-11-07';BASE=T.SITE
manifest=json.loads((ROOT/'content/provider-page-ownership-20261024.json').read_text());baseline=set(manifest['baseline_provider_slugs']);providers=[x for x in manifest['providers'] if x['slug'] in baseline];assert len(providers)==100
profiles={line.split('|')[0]:dict(zip(('category','focus','audience','scenario','instruction','question'),line.split('|')[1:])) for line in (ROOT/'content/seo-campaign-20261007/competitors.tsv').read_text().splitlines()}
assert baseline<=profiles.keys()
def p(s):return '<p>'+E(s)+'</p>'
def link(u,s):return '<a href="'+E(u,quote=True)+'">'+E(s)+'</a>'
def route(x,k):return x[k+'_url'].removeprefix(BASE)
changed=[]
for x in providers:
 profile=dict(profiles[x['slug']]);profile['question']=('What does the starting amount buy, and what is the complete first-year price?' if x['slug']=='tax-hive' else profile['question']);name=x['brand'];category=profile['category'];peers=sorted([y for y in providers if y['slug']!=x['slug'] and profiles[y['slug']]['category']==category],key=lambda y:y['brand'])[:2]
 if len(peers)<2:peers+=sorted([y for y in providers if y['slug']!=x['slug'] and y not in peers],key=lambda y:y['brand'])[:2-len(peers)]
 for intent in ['alternative','pricing','comparison']:
  path=route(x,intent);file=ROOT/path.strip('/')/'index.html';text=file.read_text();marker='hundred-firm-decision-'+intent
  text=re.sub('<!-- '+marker+':start -->.*?<!-- '+marker+':end -->','',text,flags=re.S)
  if intent=='alternative':
   heading='How to compare '+name+' alternatives'
   body=p('Start with the decision you need help making: '+profile['scenario'])+p(profile['instruction'])
   body+='<p>'+link(route(x,'pricing'),'Review '+name+' pricing evidence')+' · '+link(route(x,'comparison'),'Compare '+name+' with AE Tax Advisors')+'</p>'
   body+=p('Related providers in this directory to investigate for a matching engagement; this is not an independent ranking or a claim that their services are identical.')+'<ul>'+''.join('<li>'+link(route(y,'alternative'),y['brand']+' alternatives and scope')+'</li>' for y in peers)+'</ul>'
  elif intent=='pricing':
   heading='Build a comparable '+name+' fee proposal'
   body=p(profile['scenario'])+p(profile['instruction'])+p('Ask for a written total covering the work you actually need, separately identifying advice, implementation, filings, specialist projects and ongoing support. Keep published provider fees separate from AE’s labeled budget estimates. Use the dated evidence below and confirm the current quote directly.')
   body+='<p>'+link(route(x,'alternative'),'Compare alternatives to '+name)+' · '+link(route(x,'comparison'),name+' vs AE Tax Advisors')+'</p>'
  else:
   heading='The decision to resolve before choosing '+name+' or AE'
   body=p(profile['scenario'])+'<blockquote>'+p(profile['question'])+'</blockquote>'+p(profile['instruction'])+p('Ask both firms to put the answer, responsible professional, deliverables and deadline into the proposal. This checklist does not assert that either provider omits a service; the signed scope establishes who completes the work.')
   body+='<p>'+link(route(x,'pricing'),name+' fee evidence and quote questions')+' · '+link(route(x,'alternative'),'Other '+name+' alternatives')+'</p>'
  body+='<p>'+link('/compare/tax-firm-alternatives/','Compare the full 100-firm directory by your needs')+'</p>'
  block='<!-- '+marker+':start -->'+T.section(E(heading),body)+'<!-- '+marker+':end -->'
  # Keep the established lead and early calls to action; add decision support before the final main CTA.
  pos=text.find(T.CTA_BLOCK)
  if pos<0:pos=text.find('</main>')
  assert pos>=0,path
  text=text[:pos]+block+text[pos:]
  def update(m):
   obj=json.loads(m[1]);types=obj.get('@type',[]);types=[types] if isinstance(types,str) else types
   if 'Article' in types:obj['dateModified']=DATE
   return '<script type="application/ld+json">'+json.dumps(obj,ensure_ascii=False)+'</script>'
  text=re.sub(r'<script type="application/ld\+json">(.*?)</script>',update,text,flags=re.S)
  file.write_text(text);changed.append(path)
# One useful searchable hub, with all provider links available to crawlers without JavaScript.
path='/compare/tax-firm-alternatives/';title='Compare 100 Tax, Accounting and Property Study Firms';desc='Find alternatives, pricing evidence and AE comparisons for 100 tax, accounting and cost segregation providers. Match your needs to the scope before choosing.'
intro=p('Search the firms already covered in AE’s original hundred-provider directory. Each has separate alternatives, pricing and AE comparison guides. AE publishes this commercial directory and competes for tax services; the alphabetical list is not an independent ranking.')+p('Choose the work first: an ongoing accounting relationship, a defined planning engagement, a filed return or a property study. Use the linked provider sources to confirm current services, fees and availability. An estimate is not a guaranteed saving or a provider quote.')
controls='<label for="firm-search">Find a firm or describe your needs</label><input id="firm-search" type="search" placeholder="Search a name, rental, startup, medical…" aria-describedby="firm-count" style="width:100%;padding:14px;margin:12px 0"><p id="firm-count" role="status">100 providers</p>'
cards=[]
for x in sorted(providers,key=lambda x:x['brand'].lower()):
 q=dict(profiles[x['slug']]);q['question']=('What does the starting amount buy, and what is the complete first-year price?' if x['slug']=='tax-hive' else q['question']);needs=q['audience'];links=' · '.join(link(route(x,k),label) for k,label in [('alternative','Alternatives'),('pricing','Pricing'),('comparison','Compare with AE')])
 cards.append('<article data-firm-card><h3>'+E(x['brand'])+'</h3>'+p('A buying situation to evaluate: '+needs)+p('Ask: '+q['question'])+'<p>'+links+'</p><p>'+link(x['official_source'],'Provider’s own website')+'</p></article>')
body=T.page_header(h1=title,subtitle=desc,trail=[('Home','/'),('Compare firms','/compare/'),(title,path)])+T.section('Choose by the work you need',intro)+T.section('Find a firm',controls+''.join(cards))+T.section('Compare proposals on the same basis',p('Give each firm the same entity list, income sources, records, property facts and deadline. Ask what is included, who implements the work, who files affected returns and what future support costs. A lower starting fee or a preliminary tax-savings estimate alone does not establish a better fit.'))+T.related_section([('/compare/competitor-pricing/','Full pricing directory'),('/compare/tax-advisor-comparison-methodology/','Comparison methodology'),('/pricing/','AE fees and scope')])
items=[{'@type':'ListItem','position':i+1,'name':x['brand'],'url':x['alternative_url']} for i,x in enumerate(sorted(providers,key=lambda x:x['brand'].lower()))]
schemas=[T.article_schema(title=title,description=desc,url=BASE+path,published=DATE,modified=DATE,section='Tax firm comparisons',citations=[x['official_source'] for x in providers]),{'@context':'https://schema.org','@type':'ItemList','itemListOrder':'https://schema.org/ItemListOrderAscending','numberOfItems':100,'itemListElement':items}]
doc=T.build_page(title=title+' | AE Tax Advisors',description=desc,path=path,body=body,schemas=schemas,published=DATE,modified=DATE,active_nav='/compare/',extra_head='<script defer src="/assets/firm-comparison-search.js"></script>')
f=ROOT/path.strip('/')/'index.html';f.parent.mkdir(exist_ok=True);f.write_text(doc)
(ROOT/'assets/firm-comparison-search.js').write_text("""'use strict';
(()=>{const input=document.getElementById('firm-search'),count=document.getElementById('firm-count'),cards=Array.from(document.querySelectorAll('[data-firm-card]'));if(!input||!count)return;input.addEventListener('input',()=>{const query=input.value.trim().toLocaleLowerCase();let visible=0;for(const card of cards){const show=card.textContent.toLocaleLowerCase().includes(query);card.hidden=!show;if(show)visible++;}count.textContent=visible+' of '+cards.length+' providers';});})();
""")
# Link the hub from the established comparison landing page.
f=ROOT/'compare/index.html';text=f.read_text();mark='hundred-firm-search-hub';text=re.sub('<!-- '+mark+':start -->.*?<!-- '+mark+':end -->','',text,flags=re.S);block='<!-- '+mark+':start -->'+T.section('Find a firm and compare the right engagement','<p>'+link(path,'Search the original 100 tax firms and study providers')+' for alternatives, fee evidence and AE comparisons.</p>')+'<!-- '+mark+':end -->';f.write_text(text.replace('</main>',block+'</main>',1))
changed.append(path);xmlfile=ROOT/'sitemap-comparisons.xml';xml=xmlfile.read_text()
if '<loc>'+BASE+path+'</loc>' not in xml:xml=xml.replace('</urlset>','<url><loc>'+BASE+path+'</loc><lastmod>'+DATE+'</lastmod></url>\n</urlset>')
xmlfile.write_text(xml);f=ROOT/'content/reviewed-content-lastmod.json';dates=json.loads(f.read_text());dates.update({p:DATE for p in changed});f.write_text(json.dumps(dates,indent=2)+'\n')
data=ROOT/'content/hundred-firm-discovery-20261107';data.mkdir(exist_ok=True);(data/'pages.json').write_text(json.dumps(changed,indent=2)+'\n');(data/'scope.json').write_text(json.dumps({'providers':100,'core_pages':300,'new_search_hub':path,'excluded_policy':'Existing provider-exclusion guard remains mandatory. No excluded provider is present in this manifest.','basis':'Existing provider profiles supply buyer scenarios and questions. No new provider service or fee verification date is claimed by this decision-support addition.'},indent=2)+'\n')
# The user expressly requested improving the original hundred after this cohort started.
f=ROOT/'content/costseg-more-20261107/preservation.json';preserve=json.loads(f.read_text());allowed=set(changed);preserve={p:h for p,h in preserve.items() if p not in allowed};f.write_text(json.dumps(preserve,indent=2)+'\n')
print(json.dumps({'providers':100,'updated_core_pages':300,'new_hubs':1,'prior_non_target_pages_preserved':len(preserve)}))
