#!/usr/bin/env python3
"""Apply the screenshot keyword map to existing canonical pages; rerunnable."""
from pathlib import Path
import html,json,re
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'content/keyword-coverage-20261113.json').read_text())
esc=html.escape
for i,g in enumerate(data['groups']):
 p=ROOT/g['route'].strip('/')/'index.html';s=p.read_text()
 s=re.sub(r'<!-- keyword-coverage:start -->.*?<!-- keyword-coverage:end -->','',s,flags=re.S)
 block='<section class="content-section" id="planning-questions"><div class="container narrow"><h2>'+esc(g['title'])+': planning questions</h2><p>Updated November 13, 2026. Use these answers to prepare a review of your records with AE Tax Advisors.</p>'
 for j,a in enumerate(g['answers']):
  block+='<section id="planning-answer-'+str(j+1)+'"><h3>'+esc(a['question'])+'</h3><p>'+esc(a['answer'])+'</p></section>'
 block+='<h3>Records to bring to the planning call</h3><p>Bring the latest filed returns, ownership details and documents supporting the transaction or deduction. Identify deadlines and prior elections before implementing a change. <a href="/discovery/">Discuss your planning questions with AE Tax Advisors</a>.</p><h3>Source references</h3><ul>'
 for label,url in g['sources']:block+='<li><a href="'+esc(url)+'">'+esc(label)+'</a></li>'
 block+='</ul><p>Read the <a href="/editorial-policy/">editorial policy</a>. These educational answers do not establish eligibility for a particular return.</p><nav aria-label="Related tax planning guides"><h3>Coordinate the next decision</h3><ul>'
 related=[data['groups'][n] for n in [[4,6,7],[3,9,7],[9,3,1],[9,1,7],[6,5,8],[8,4,7],[4,8,0],[0,3,9],[5,4,6],[3,1,2]][i]]
 for other in related:block+='<li><a href="'+other['route']+'#planning-questions">'+esc(other['title'])+'</a></li>'
 block+='</ul></nav></div></section>'
 s=s.replace('</main>','<!-- keyword-coverage:start -->'+block+'<!-- keyword-coverage:end --></main>',1)
 # Extend the existing FAQ entity, keeping visible answers identical to JSON-LD.
 new=[{'@type':'Question','name':a['question'],'acceptedAnswer':{'@type':'Answer','text':a['answer']}} for a in g['answers']]
 found=[False]
 def update(m):
  obj=json.loads(m.group(2));before=json.dumps(obj,sort_keys=True)
  def visit(v):
   if isinstance(v,dict):
    if v.get('@type')=='FAQPage' and not found[0]:
     questions=v.setdefault('mainEntity',[]);names={a['name'] for a in new}
     v['mainEntity']=[q for q in questions if q.get('name') not in names]+new;found[0]=True
    else:
     for value in v.values():visit(value)
   elif isinstance(v,list):
    for value in v:visit(value)
  visit(obj)
  if json.dumps(obj,sort_keys=True)==before:return m.group(0)
  return m.group(1)+json.dumps(obj,ensure_ascii=False,indent=2).replace('<','\\u003c')+m.group(3)
 s=re.sub(r'(<script\b[^>]*type=[\"\']application/ld\+json[\"\'][^>]*>)(.*?)(</script>)',update,s,flags=re.S|re.I)
 if not found[0]:s=s.replace('</head>','<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':new}).replace('<','\\u003c')+'</script></head>',1)
 assert s.count('id="planning-questions"')==1
 p.write_text(s)
# Add the topic reading path to the existing homepage, using the deployed config.
p=ROOT/'scripts/seo-focus.json';cfg=json.loads(p.read_text());seen={x['href'] for x in cfg['links']}
for g in data['groups']:
 if g['route'] not in seen:cfg['links'].append({'href':g['route'],'label':g['title']})
p.write_text(json.dumps(cfg,indent=2)+'\n')
p=ROOT/'content/reviewed-content-lastmod.json';dates=json.loads(p.read_text())
for g in data['groups']:dates[g['route']]=data['date']
p.write_text(json.dumps(dates,indent=2)+'\n')
print('Expanded 10 existing pages with 50 direct answers and related reading links.')
