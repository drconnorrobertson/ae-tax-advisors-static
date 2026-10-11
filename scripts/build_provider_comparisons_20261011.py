"""Build 496 distinct provider pairs and four browsing guides from sourced profiles."""
import html,itertools,json,re,sys
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import site_template as T
DATE='2026-10-11'; E=html.escape
DATA=ROOT/'content/provider-comparisons-20261011'
profiles=json.loads((DATA/'profiles.json').read_text())
by={p['slug']:p for p in profiles}
demand=json.loads((DATA/'demand.json').read_text())
HUB='/compare/provider-comparison-library/'
paths=[];manifest=[]
def p(t):return '<p>'+E(t)+'</p>'
def ul(items):return '<ul>'+''.join('<li>'+E(x)+'</li>' for x in items)+'</ul>'
def section(h,b):return T.section(E(h),b)
def link(url,label):return '<a href="'+E(url,quote=True)+'">'+E(label)+'</a>'
def table(rows,headers):
 return '<div style="overflow-x:auto"><table><thead><tr>'+''.join('<th scope="col">'+E(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr><th scope="row">'+E(r[0])+'</th>'+''.join('<td>'+E(x)+'</td>' for x in r[1:])+'</tr>' for r in rows)+'</tbody></table></div>'
def pairpath(a,b):return '/compare/'+a['slug']+'-vs-'+b['slug']+'/'
def group(f):
 c=f['category']
 if c in ('study','costseg','software'):return 'property'
 if c in ('realestate',):return 'realestate'
 if c in ('national','legal','resolution'):return 'specialist'
 if c in ('wealth','network'):return 'wealth'
 return 'owner'
def score(a,b):
 same=group(a)==group(b)
 # Match a specialist or study to relevant peers; do not create arbitrary study/payroll pairs.
 return (10000 if same else 0)+demand.get(a['slug'],0)+demand.get(b['slug'],0)
candidates=[]
for a,b in itertools.combinations(sorted(profiles,key=lambda f:f['slug']),2):
 if group(a)!=group(b):continue
 path=pairpath(a,b)
 if (ROOT/path.strip('/')/'index.html').exists():continue
 candidates.append((score(a,b),a,b))
candidates.sort(key=lambda z:(-z[0],z[1]['slug'],z[2]['slug']))
selected={};degree=Counter()
# Breadth first: each provider gets at least three relevant comparisons before filling by demand.
for _ in range(3):
 for f in sorted(profiles,key=lambda x:(-demand.get(x['slug'],0),x['slug'])):
  for _,a,b in candidates:
   key=(a['slug'],b['slug'])
   if f['slug'] in key and key not in selected:
    selected[key]=(a,b);degree.update(key);break
for _,a,b in candidates:
 if len(selected)>=496:break
 key=(a['slug'],b['slug'])
 if key not in selected:selected[key]=(a,b);degree.update(key)
assert len(selected)==496,len(selected)
assert len(degree)==len(profiles),(len(degree),len(profiles))
def save(path,title,desc,body,sources):
 assert not (ROOT/path.strip('/')/'index.html').exists(),path
 trail=[('Home','/'),('Compare','/compare/'),('Provider comparison library',HUB),(title,path)]
 schemas=[T.article_schema(title=title,description=desc,url=T.SITE+path,published=DATE,modified=DATE,section='Tax Provider Comparisons',citations=sources),T.breadcrumb_schema(trail)]
 header=T.page_header(h1=E(title),subtitle=E(desc),trail=[(E(n),u) for n,u in trail])
 T.write_page(path,T.build_page(title=title,description=desc,path=path,body=header+body,schemas=schemas,published=DATE,modified=DATE,active_nav='/compare/'))
 paths.append(path)
def profile_block(f):
 body=p(f['summary'])+p('Relevant buyer: '+f['fit'])+p('Evaluation example: '+f['scenario'])
 body+=p(f['decision'])
 if f.get('note'):body+=p(f['note'])
 if f.get('documents'):body+=p('Organize these records: '+f['documents'])
 if f.get('deliverable'):body+=p('A useful requested deliverable is '+f['deliverable']+'.')
 body+='<p>'+link(f['source'],f['name']+' official service information')+'. Profile research date: '+f['reviewed']+'.</p>'
 return section(f['name']+': service model and buyer fit',body)
for a,b in selected.values():
 path=pairpath(a,b);title=a['name']+' vs '+b['name']+': Tax Services Compared'
 desc='Compare '+a['name']+' and '+b['name']+' on service focus, buyer fit, proposal questions and implementation. Published by AE Tax Advisors.'
 body=section('Start with the decision your advisor must help you make',p('These are two providers to investigate for '+{'property':'property-related tax work','realestate':'real estate and owner tax coordination','specialist':'a specialist tax or broader business assignment','wealth':'tax planning within a wider advisor relationship','owner':'business owner and high-income tax help'}[group(a)]+'. The comparison below uses their public descriptions and separate buyer scenarios. It does not establish that both providers offer every service you need.')+p('Published by AE Tax Advisors, a competing provider. This is a source-based service comparison, not an independent ranking, customer review or endorsement.'))
 body+=section('At a glance: what to put in the two proposals',table([('Public service description',a['summary'],b['summary']),('Buyer situation to investigate',a['fit'],b['fit']),('Question to resolve before signing',a['question'],b['question']),('Planning and implementation',a['decision'],b['decision'])],['Decision',a['name'],b['name']]))
 body+=profile_block(a)+profile_block(b)
 body+=section('How these two options change your shortlist',p('Investigate '+a['name']+' first when your immediate assignment matches this situation: '+a['scenario'])+p('Investigate '+b['name']+' first when this is the closer description: '+b['scenario'])+p('If both situations apply, ask whether one lead professional can coordinate the work or whether separate engagements are needed. A stated specialty is a reason to investigate fit, not proof that the other provider lacks that capability.'))
 body+=section('Two questions that make the comparison concrete',p('For '+a['name']+': '+a['question'])+p('For '+b['name']+': '+b['question'])+p('Ask both teams to return a written scope identifying the assigned professional, the information needed, the result you will receive and the completion date. Compare answers against your actual entities and income sources, rather than counting the number of services on a website.'))
 body+=section('Compare fees on the same assignment',p('This comparison does not assert a current numeric fee for either provider. Request a dated proposal from each. Separate the initial review, recurring accounting, written planning, implementation, business returns, personal returns, state filings and any specialist work. An advertised starting price, consultation fee or subscription is not the complete price for every business.')+p('Put both proposals on the same time horizon. Include first-year onboarding or cleanup, outside-professional costs, required renewals and cancellation terms. Request an explanation of whether a projected benefit is a permanent tax reduction, a timing benefit or simply a deduction. No provider’s fee or service model guarantees savings.'))
 body+=section('Where AE belongs in the comparison',p('AE Tax Advisors is another option for business owners, real estate investors and high-income professionals seeking a defined tax advisory engagement. The standard published advisory price is $7,800, payable in two $3,900 installments 30 days apart. Tax returns, amendments, property studies and additional work are separately scoped and priced. The standard engagement does not require an annual planning renewal; confirm the actual duration and deliverables in your agreement.')+p('Ask AE the same two issue-specific questions above. A broader national practice, an investment relationship, a legal assignment, a directory referral or a specialist engineering study may contain work outside AE’s advisory scope. Retain any specialist your facts require.')+'<p>'+link('/pricing/','Check current AE pricing')+' · '+link('/how-it-works/','Review the advisory process')+' · '+link('/discovery/','Book a Call')+'</p>')
 related=[(x,y) for x,y in selected.values() if (a['slug'] in (x['slug'],y['slug']) or b['slug'] in (x['slug'],y['slug'])) and pairpath(x,y)!=path][:6]
 body+=section('Continue your shortlist','<ul>'+''.join('<li>'+link(pairpath(x,y),x['name']+' vs '+y['name'])+'</li>' for x,y in related)+'<li>'+link(HUB,'Browse all providers and comparisons')+'</li><li>'+link('/compare/','AE comparisons and provider alternatives')+'</li></ul>')
 body+=section('Sources and research limits','<p>'+link(a['source'],a['name']+' official source')+' (profile reviewed '+a['reviewed']+'); '+link(b['source'],b['name']+' official source')+' (profile reviewed '+b['reviewed']+'); '+link('/pricing/','AE pricing')+'.</p>'+p('Service descriptions summarize public marketing information and are not an audit of capabilities or client outcomes. Confirm current services, credentials, availability and contract terms directly. Illustrative buyer situations are not client results. Details not established here should be verified, not treated as missing services.'))
 save(path,title,desc,body,[a['source'],b['source'],T.SITE+'/pricing/'])
 manifest.append({'path':path,'providers':[a['slug'],b['slug']],'demand_priority_score':demand.get(a['slug'],0)+demand.get(b['slug'],0)})
hubs=[(HUB,'Tax Provider Comparison Library',profiles),('/compare/business-owner-provider-shortlists/','Business Owner Tax Provider Shortlists',[f for f in profiles if group(f) in ('owner','specialist')]),('/compare/high-income-provider-shortlists/','High-Income Tax Advisor Shortlists',[f for f in profiles if group(f) in ('owner','wealth','realestate')]),('/compare/real-estate-study-provider-shortlists/','Real Estate Tax and Study Provider Shortlists',[f for f in profiles if group(f) in ('realestate','property')])]
for path,title,subset in hubs:
 desc='Browse sourced provider comparisons, service models and shortlist questions from AE Tax Advisors.'
 body=section('Choose a provider around the actual assignment',p('Compare '+str(len(subset))+' providers using their published service descriptions and the pair-by-pair guides below. This library is published by AE Tax Advisors, a competing provider; it is not an independent ranking. Listings are alphabetical and do not rank quality or promise a tax result.')+p('Start by identifying whether you need owner-level planning, monthly accounting, return preparation, wealth coordination, legal advice or a property study. Search a provider name below, then compare its service model with the other relevant options.'))
 body+='<section class="content-section"><div class="container narrow"><label for="provider-filter">Find a provider</label><input id="provider-filter" type="search" placeholder="Search provider names or services" style="width:100%;padding:12px;margin:12px 0"><p id="provider-count" role="status">'+str(len(subset))+' providers</p></div></section>'
 for f in sorted(subset,key=lambda x:x['name'].lower()):
  comparisons=[(a,b) for a,b in selected.values() if f['slug'] in (a['slug'],b['slug'])]
  content=p(f['summary'])+p('Shortlist question: '+f['question'])+'<p>'+link(f['source'],'Official provider source')+'</p><ul>'+''.join('<li>'+link(pairpath(a,b),a['name']+' vs '+b['name'])+'</li>' for a,b in comparisons)+'</ul>'
  body+='<div data-provider="'+E((f['name']+' '+f['summary']).lower(),quote=True)+'">'+section(f['name'],content)+'</div>'
 body+='''<script>document.getElementById('provider-filter').addEventListener('input',function(){let n=0;document.querySelectorAll('[data-provider]').forEach(el=>{el.hidden=!el.dataset.provider.includes(this.value.toLowerCase().trim());if(!el.hidden)n++;});document.getElementById('provider-count').textContent=n+' providers';});</script>'''
 body+=section('Explore another shortlist','<ul>'+''.join('<li>'+link(u,t)+'</li>' for u,t,_ in hubs if u!=path)+'<li>'+link('/compare/','AE comparisons and alternatives')+'</li><li>'+link('/discovery/','Book a Call')+'</li></ul>')
 save(path,title,desc,body,list(dict.fromkeys(f['source'] for f in subset)))
assert len(paths)==500
for filename in ['compare/index.html','compare/tax-planning-firms/index.html']:
 q=ROOT/filename;x=q.read_text();marker='provider-library-20261011'
 assert marker not in x
 block='<section class="content-section" id="'+marker+'"><div class="container narrow"><h2>Compare more tax providers</h2><p>Browse '+str(len(profiles))+' providers and 496 firm-to-firm comparisons by service model, buyer fit and implementation questions.</p><p>'+link(HUB,'Open the tax provider comparison library')+'</p></div></section>'
 assert '</main>' in x;q.write_text(x.replace('</main>',block+'</main>'))
xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>'+T.SITE+u+'</loc><lastmod>'+DATE+'</lastmod></url>\n' for u in paths)+'</urlset>\n'
(ROOT/'sitemap-provider-comparisons-20261011.xml').write_text(xml)
for filename in ['sitemap-index.xml','sitemap_index.xml']:
 q=ROOT/filename;x=q.read_text();assert '</sitemapindex>' in x
 x=x.replace('</sitemapindex>','<sitemap><loc>'+T.SITE+'/sitemap-provider-comparisons-20261011.xml</loc><lastmod>'+DATE+'</lastmod></sitemap>\n</sitemapindex>');q.write_text(x)
(DATA/'manifest.json').write_text(json.dumps({'date':DATE,'provider_count':len(profiles),'comparison_count':len(manifest),'page_count':len(paths),'paths':paths,'comparisons':manifest,'provider_degrees':dict(degree)},indent=2))
print(json.dumps({'new_pages':len(paths),'unique_providers':len(profiles),'comparisons':len(manifest),'minimum_comparisons_per_provider':min(degree.values())}))
