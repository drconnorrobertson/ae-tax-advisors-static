"""Refresh an explicitly reviewed set of comparison pages; never create pair pages."""
from pathlib import Path
from urllib.parse import urlsplit
import html,json,re
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'content/comparison-quality-20261108'
data=json.loads((DATA/'notes.json').read_text());DATE=data['reviewed'];E=html.escape
providers=data['providers'];routes=[]
assert not re.search(r'dan\s*nicholson|nth[\s-]*degree',json.dumps(data),re.I)
def sec(h,b):return '<section class="content-section"><div class="container narrow"><h2>'+E(h)+'</h2>'+b+'</div></section>'
def p(t):return '<p>'+E(t)+'</p>'
def a(url,label):return '<a href="'+E(url,quote=True)+'">'+E(label)+'</a>'
config_file=ROOT/'scripts/search-intent-config.json';config=json.loads(config_file.read_text())
lastmod_file=ROOT/'content/reviewed-content-lastmod.json';lastmod=json.loads(lastmod_file.read_text())
for item in data['pairs']:
 left,right=providers[item['a']],providers[item['b']]
 route='/compare/'+item['a']+'-vs-'+item['b']+'/'
 path=ROOT/route.strip('/')/'index.html'
 assert path.is_file(), 'Do not manufacture an additional pair URL: '+route
 s=path.read_text();canonical='https://www.aetaxadvisors.com'+route
 assert 'href="'+canonical+'"' in s and 'content="noindex' not in s
 title=left['name']+' vs '+right['name']+': Services & Scope'
 desc='Compare '+left['name']+' and '+right['name']+'. '+item['decision']+' Review public services, scope questions and implementation responsibilities.'
 # Keep the main distinction visible when the combined brand names are long.
 if len(desc)>200:desc='Compare '+left['name']+' and '+right['name']+' on services, scope and implementation. '+item['decision']
 h1=left['name']+' vs '+right['name']
 intro='<section class="page-header"><div class="container narrow"><nav aria-label="Breadcrumb">'+a('/','Home')+' / '+a('/compare/','Compare tax providers')+'</nav><h1>'+E(h1)+'</h1><p class="subtitle">'+E(item['decision'])+'</p></div></section>'
 body=sec('The decision behind this comparison',p(item['scenario'])+p('Published by AE Tax Advisors, a competing provider. This illustrative buying scenario is not a customer review or rating.'))
 table='<div class="table-wrap"><table><caption>'+E(left['name']+' and '+right['name']+': current public service scope')+'</caption><thead><tr><th scope="col">Compare</th><th scope="col">'+E(left['name'])+'</th><th scope="col">'+E(right['name'])+'</th></tr></thead><tbody>'
 for label,lv,rv in [('Public offering',left['summary'],right['summary']),('Ask in the proposal',item['questionA'],item['questionB'])]:table+='<tr><th scope="row">'+E(label)+'</th><td>'+E(lv)+'</td><td>'+E(rv)+'</td></tr>'
 table+='</tbody></table></div>'
 body+=sec('Services and the questions that distinguish them',table+'<p>Sources: '+a(left['source'],left['name']+' official service information')+'; '+a(right['source'],right['name']+' official service information')+'. Public descriptions checked November 8, 2026. A listed offering is not proof that every package includes it.</p>')
 body+=sec('Before choosing',p('Get written answers to the two questions above. Compare named professionals, deliverables, deadlines and total fees for the same assignment. Confirm any exclusions or renewal requirements directly.'))
 body+=sec('Compare a focused AE engagement','<p>If you also want an AE proposal, compare its agreed scope using our '+a('/pricing/','published pricing')+' and '+a('/how-it-works/','advisory process')+'. '+a('/discovery/','Discuss your situation')+'.</p>')
 related=[]
 for slug,provider in [(item['a'],left),(item['b'],right)]:
  candidate='/compare/'+slug+'-alternatives/'
  if (ROOT/candidate.strip('/')/'index.html').exists():related.append('<li>'+a(candidate,provider['name']+' alternatives')+'</li>')
 body+=sec('Continue your comparison','<ul>'+''.join(related)+'<li>'+a('/compare/provider-comparison-library/','Browse the provider comparison library')+'</li><li>'+a('/compare/','Compare AE and other tax providers')+'</li></ul>')
 s=re.sub(r'<main\b[^>]*>[\s\S]*?</main>',lambda _:'<main id="main-content" tabindex="-1">'+intro+body+'</main>',s,count=1)
 s=re.sub(r'<title>[\s\S]*?</title>',lambda _:'<title>'+E(title)+'</title>',s,count=1)
 for key,val in [('description',desc),('og:title',title),('og:description',desc),('twitter:title',title),('twitter:description',desc),('article:modified_time',DATE+'T00:00:00-05:00')]:
  s=re.sub(r'(<meta\s+(?:name|property)="'+re.escape(key)+r'"\s+content=")[^"]*("\s*/?>)',lambda m:m[1]+E(val,quote=True)+m[2],s)
 def schema(m):
  obj=json.loads(m[1])
  if obj.get('@type') not in ['Article','BlogPosting','BreadcrumbList']:
   return ''
  if obj.get('@type') in ['Article','BlogPosting']:
   obj.update(headline=h1,description=desc,dateModified=DATE,citation=[left['source'],right['source'],'https://www.aetaxadvisors.com/pricing/'])
  if obj.get('@type')=='BreadcrumbList' and obj.get('itemListElement'):
   obj['itemListElement'][-1].update(name=h1,item=canonical)
  return '<script type="application/ld+json">'+json.dumps(obj,indent=2)+'</script>'
 s=re.sub(r'<script type="application/ld\+json">([\s\S]*?)</script>',schema,s)
 path.write_text('\n'.join(line.rstrip() for line in s.splitlines())+'\n');routes.append(route);lastmod[route]=DATE
 config[route.strip('/')+'/index.html']={'title':title,'description':desc,'h1':h1}
config_file.write_text(json.dumps(config,indent=2)+'\n');lastmod_file.write_text(json.dumps(lastmod,indent=2)+'\n');(DATA/'routes.json').write_text(json.dumps(routes,indent=2)+'\n')
print('Updated',len(routes),'existing comparisons with source-specific decisions; no additional pairs created.')
