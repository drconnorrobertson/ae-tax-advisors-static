#!/usr/bin/env python3
"""Five-page retirement accuracy, source ownership, arithmetic and preservation checks.

Optional --baseline points to a private pre-edit snapshot; no private data ships.
Mutated negative fixtures stay in memory and never enter public output.
"""
import argparse, ast, html, json, re, sys
from decimal import Decimal as D
from html.parser import HTMLParser
from pathlib import Path
from tax_review_build_normalization import normalize_baseline_html
REPO=Path(__file__).resolve().parents[1]
ROUTES=json.loads((REPO/'scripts/retirement-buyer-guide-routes-20261106.json').read_text())
FILES=[r.strip('/')+'/index.html' for r in ROUTES]
SITE='https://www.aetaxadvisors.com'
REQUIRED=[
 ['$24,500','$72,000','$8,000','$11,250','20%','$40,000','$64,500','$47,500','$62,000','$150,000 vested','$50,000','$30,000','preceding 12 months','at least quarterly','principal-residence','not new retirement contributions','generally adds the taxable amount to income','Ordinary rental income','personally guarantee','unextended individual return deadline','Form 5500-EZ','https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-loans'],
 ['$49,500','$25,000','$288,000','$72,000','written agreement','Roth SEP',"employer deduction is evaluated separately",'prior-year wages','Other employer-plan deferrals','controlled groups','Form 5305-SEP','same non-catch-up limit','retroactive S-corporation payroll deferrals','unextended individual return deadline','https://www.irs.gov/publications/p560'],
 ['$250,500','$18,000','$200,000','$300,000','not a client result','not a universal contribution or deduction cap','excess enters','8.5 months','September 15','Quarterly installments','October 15','does not erase','80%','assumed inputs','https://www.irs.gov/pub/irs-drop/n-07-28.pdf'],
 ['$300,500','$292,500','$268,000','$108,225','$8,000 Roth','up to 20%, not 23%','QBI','not an independent-audit threshold','participant-count','8.5 months','September 15','October 15','Quarterly installments','never covered more than 25 active participants','Schedule SB','retain Schedule SB','$2,000 to $5,000','$1,500 to $3,000','$74,000','not a binding fee quote','https://www.irs.gov/instructions/i8995'],
 ['$290,000','$72,000','$307,000','$26,200','$128,940','11.72','2.93','$2,500 to $6,000','$5,000','hypothetical arithmetic illustrations','not client outcomes','not a statutory safe harbor','never had more than 25 active participants','substantial owners','controlled groups','affiliated service groups','8.5 months','excess enters','https://www.pbgc.gov/employers-practitioners/legal-resources/insurance-coverage']
]
STALE=[
 'can borrow up to $75,000 to fund', 'deductions taken in conversion years',
 '25% of your net Schedule C profit reduced', 'Employee deferrals in 2024 are capped at $23,500',
 'Form 5500-N (a streamlined', 'can file the simplified Form 5500-N',
 'At identical compensation, the solo 401(k) contributes more.',
 'so at any given compensation level it reaches a higher total',
 'No plan document to maintain', 'a solo 401(k) generally cannot',
 'Missing it forfeits the entire year', 'mid-December is generally too late',
 'Full DC limit plus catch-up', 'frequently directs 80 to 90 percent',
 'Every dollar contributed reduces taxable income dollar-for-dollar',
 'QBI deduction increase to 23%', 'claiming the 23% QBI deduction',
 'Plans with more than $250,000 in assets require an independent audit',
 'must be adopted before the end of the plan year',
 'the employer deduction for the defined contribution plan is limited to 6%',
 'professional service employers with 25 or fewer participants are generally exempt',
 'These costs are trivial', 'number routinely lands between $150,000 and $300,000 annually, fully deductible',
]
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.tags=[];self.words=[];self.skip=0
 def handle_starttag(self,t,a):
  self.tags.append((t,dict(a)))
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip-=1
 def handle_data(self,s):
  if not self.skip:self.words.append(s)
def plain(s):
 p=Parser();p.feed(s);return ' '.join(' '.join(p.words).split())
def schemas(s):return [json.loads(x) for x in re.findall(r'<script\b[^>]*type=[\'"]application/ld\+json[\'"][^>]*>(.*?)</script>',s,re.S)]
def mainhtml(s):return re.search(r'<main\b[^>]*>.*?</main>',s,re.S)[0]
def faq_pairs(s):
 main=re.sub(r'<div class="compact-booking-cta"[^>]*>.*?</div>','',mainhtml(s),flags=re.S);out=[(plain(q),plain(a)) for q,a in re.findall(r'<h3\b[^>]*>(.*?)</h3>\s*<p[^>]*>(.*?)</p>',main,re.S)]
 extra=re.search(r'<!-- million-owner-answer:start -->.*?<h2[^>]*>(.*?)</h2><p>(.*?)</p>',main,re.S)
 if extra:out.append((plain(extra[1]),plain(extra[2])))
 return out

def page_errors(i,s):
 errors=[]
 def check(ok,msg):
  if not ok:errors.append(FILES[i]+': '+msg)
 p=Parser();p.feed(s);v=plain(mainhtml(s));raw=html.unescape(s)
 check([a.get('href') for t,a in p.tags if t=='link' and a.get('rel')=='canonical']==[SITE+ROUTES[i]],'canonical')
 check(len(re.findall(r'<h1\b',s))==1,'H1 count')
 check(not any('noindex' in a.get('content','') for t,a in p.tags if t=='meta' and a.get('name') in ['robots','googlebot']),'noindex')
 for token in REQUIRED[i]:check(token in raw or token in v,'missing '+token)
 for token in STALE:check(token.lower() not in raw.lower(),'stale '+token)
 check('Reviewed November 6, 2026' in v,'review date')
 a=[d for d in schemas(s) if d.get('@type') in ['Article','BlogPosting']];check(len(a)==1,'article count')
 if a:
  check(a[0].get('headline')==plain(re.search(r'<h1[^>]*>(.*?)</h1>',s,re.S)[1]),'headline parity')
  check(a[0].get('dateModified')=='2026-11-06','modified date')
  for key in ['description','og:description','twitter:description']:
   check([x.get('content') for t,x in p.tags if t=='meta' and (x.get('name')==key or x.get('property')==key)]==[a[0].get('description')],'description parity '+key)
 f=[d for d in schemas(s) if d.get('@type')=='FAQPage'];check(len(f)==1,'FAQ count')
 if f:
  pairs=[(plain(q['name']),plain(q['acceptedAnswer']['text'])) for q in f[0]['mainEntity']]
  check(pairs==faq_pairs(s),'exact FAQ question/answer parity')
 check(any(t=='a' and x.get('href')=='/discovery/' for t,x in p.tags),'booking link')
 return errors

def assignment(s,name):return next(n for n in ast.parse(s).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets))
def dbnode(s):return next(n for n in ast.walk(ast.parse(s)) if isinstance(n,ast.Dict) and any(isinstance(k,ast.Constant) and k.value=='slug' and isinstance(v,ast.Constant) and v.value=='defined-benefit-plan-high-income-business-owners' for k,v in zip(n.keys,n.values)))
def span(s,n):
 lines=s.splitlines(keepends=True);return sum(map(len,lines[:n.lineno-1]))+n.col_offset,sum(map(len,lines[:n.end_lineno-1]))+n.end_col_offset
def strip_owned_fields(s,file):
 spans=[]
 if file=='cluster_c5.py':
  for name in ['SOLO_VS_SEP','STACKING']:
   n=assignment(s,name)
   for k in n.value.keywords:
    if k.arg in ['description','subtitle','lead','body','takeaways','faqs']:spans.append(span(s,k.value))
 else:
  n=dbnode(s)
  for k,v in zip(n.keys,n.values):
   if k.value in ['meta_desc','intro','sections','faqs','cta_body']:spans.append(span(s,v))
 for a,b in sorted(spans,reverse=True):s=s[:a]+'<OWNED_VALUE>'+s[b:]
 return s

def source_errors(docs):
 errors=[];src=(REPO/'cluster_c5.py').read_text()
 for i,name in [(1,'SOLO_VS_SEP'),(2,'STACKING')]:
  v={k.arg:ast.literal_eval(k.value) for k in assignment(src,name).value.keywords};main=plain(mainhtml(docs[i]))
  for x in [v['subtitle'],v['lead']]+v['takeaways']+[a for pair in v['body']+v['faqs'] for a in pair]:
   if plain(x) not in main:errors.append(name+': source/body mismatch '+plain(x)[:90])
  if next(d for d in schemas(docs[i]) if d.get('@type')=='Article')['description']!=v['description']:errors.append(name+': source description mismatch')
 src=(REPO/'scripts/batch_str.py').read_text();v={k.value:ast.literal_eval(x) for k,x in zip(dbnode(src).keys,dbnode(src).values) if not isinstance(x,ast.Name)};main=plain(mainhtml(docs[4]))
 for x in v['intro']+[p for h,ps in v['sections'] for p in [h]+ps]+[x for q,a in v['faqs'] for x in [q,a]]:
  if plain(x) not in main:errors.append('batch_str DB source/body mismatch '+plain(x)[:90])
 if next(d for d in schemas(docs[4]) if d.get('@type')=='BlogPosting')['description']!=v['meta_desc']:errors.append('DB source description mismatch')
 return errors

def preservation(i,old,new):
 errors=[]
 for tag in ['header','footer']:
  pat=r'<'+tag+r'\b[^>]*>.*?</'+tag+'>'
  if re.findall(pat,old,re.S)!=re.findall(pat,new,re.S):errors.append(FILES[i]+': '+tag+' changed')
 for key in ['datePublished']:
  if [d[key] for d in schemas(old) if key in d]!=[d[key] for d in schemas(new) if key in d]:errors.append(FILES[i]+': publication date changed')
 a,b=Parser(),Parser();a.feed(old);b.feed(new)
 published=lambda p:[x for t,x in p.tags if t=='meta' and x.get('property')=='article:published_time']
 if published(a)!=published(b):errors.append(FILES[i]+': publication metadata changed')
 internal=lambda p:sorted(x['href'] for t,x in p.tags if t=='a' and x.get('href','').startswith('/'))
 if internal(a)!=internal(b):errors.append(FILES[i]+': internal navigation changed')
 anchors=lambda s:re.findall(r'<a\b(?=[^>]*class="[^"]*\bbtn-cta\b)[^>]*>.*?</a>',s,re.S)
 if anchors(old)!=anchors(new):errors.append(FILES[i]+': CTA anchors changed')
 for pat,label in [(r'<div class="post-cta">.*?</div>','post CTA'),(r'<!-- million-owner-answer:start -->.*?<!-- million-owner-answer:end -->','appended owner question')]:
  if re.findall(pat,old,re.S)!=re.findall(pat,new,re.S):errors.append(FILES[i]+': '+label+' changed')
 for marker in ['Related Reading','More in This Series','Start With the Pillar Guide']:
  def segment(s):
   m=re.search(r'<h2[^>]*>'+marker+r'</h2>\s*<ul[^>]*>.*?</ul>',s,re.S);return m[0] if m else ''
  if segment(old)!=segment(new):errors.append(FILES[i]+': related reading changed')
 return errors

def math_checks():
 count=0
 def eq(a,b):
  nonlocal count
  assert a==b,(a,b);count+=1
 eq(D('.25')/(1+D('.25')),D('.20'));eq(D(200000)*D('.20'),D(40000));eq(D(40000)+D(24500),D(64500));eq(min(D(50000),D(150000)*D('.5')),D(50000));eq(D(50000)-(D(20000)-D(0)),D(30000));eq(D(150000)*D('.25')+D(24500),D(62000));eq(D(72000)-D(24500),D(47500));eq(D(100000)*D('.25'),D(25000));eq(D(25000)+D(24500),D(49500));eq(D(288000)*D('.25'),D(72000));eq(D(300000)*D('.06'),D(18000));eq(D(24500)+D(8000)+D(18000)+D(200000),D(250500));eq(D(200000)/D(250000),D('.8'));eq(D(24500)+D(8000)+D(18000)+D(250000),D(300500));eq(D(300500)-D(8000),D(292500));eq(D(250000)+D(18000),D(268000));eq(D(292500)*D('.37'),D(108225));eq(D(200000)*D('.37'),D(74000));eq(D(70000)+D(237000),D(307000));eq(D(9800)+D(16400),D(26200));eq(D(307000)*D('.42'),D(128940));eq(round(D(307000)/D(26200),2),D('11.72'));eq(round(D(580000)/D(198000),2),D('2.93'))
 return count

def main():
 p=argparse.ArgumentParser();p.add_argument('root',nargs='?',default=str(REPO));p.add_argument('--baseline');a=p.parse_args();root=Path(a.root).resolve();docs=[(root/f).read_text() for f in FILES];errors=[];negative=0
 for i,s in enumerate(docs):errors+=page_errors(i,s)
 errors+=source_errors(docs)
 for i in range(5):
  for token in REQUIRED[i]:assert page_errors(i,docs[i].replace(token,'REMOVED_REQUIRED_CLAIM'));negative+=1
  for old,new in [('rel="canonical"','rel="alternate"'),('"dateModified": "2026-11-06"','"dateModified": "2000-01-01"')]:assert page_errors(i,docs[i].replace(old,new));negative+=1
  answer=next(d for d in schemas(docs[i]) if d.get('@type')=='FAQPage')['mainEntity'][0]['acceptedAnswer']['text'];assert page_errors(i,docs[i].replace(json.dumps(answer,ensure_ascii=False),json.dumps('Unmatched answer '+answer,ensure_ascii=False),1));negative+=1
 for token in STALE:assert page_errors(0,docs[0].replace('</main>','<p>'+token+'</p></main>'));negative+=1
 if a.baseline:
  base=Path(a.baseline)
  for i,f in enumerate(FILES):
   old=(base/f).read_text();current=(REPO/f).read_text();errors+=preservation(i,old,current)
   assert preservation(i,old,current.replace('href="/discovery/"','href="/missing/"',1));negative+=1
   assert preservation(i,old,current.replace('</footer>','<p>Unexpected change</p></footer>'));negative+=1
  for file in ['cluster_c5.py','scripts/batch_str.py']:
   old=(base/file).read_text();new=(REPO/file).read_text()
   if strip_owned_fields(old,file)!=strip_owned_fields(new,file):errors.append(file+': unrelated source bytes changed')
   assert strip_owned_fields(old,file)!=strip_owned_fields(new+'\n# unauthorized edit\n',file);negative+=1
  if (base/'owner_million_manifest.json').read_bytes()!=(REPO/'owner_million_manifest.json').read_bytes():errors.append('owner_million_manifest.json: unowned source changed')
  old_catalog=json.loads((base/'scripts/blog-catalog.json').read_text());new_catalog=json.loads((REPO/'scripts/blog-catalog.json').read_text())
  expected_catalog=json.loads(json.dumps(old_catalog))
  descriptions={
   '/blog/cash-balance-plans-business-owners-2026/':'Model 2026 cash balance and 401(k) contributions, staff costs, funding deadlines, deduction limits and administration before committing business cash.',
   '/blog/defined-benefit-plan-high-income-business-owners/':'Evaluate a defined benefit plan with 2026 limits, actuarial funding, employee costs, PBGC coverage and combined 401(k) deduction rules before adopting.'}
  for route,description in descriptions.items():
   rows=[row for row in expected_catalog if row['url']==route];assert len(rows)==1
   rows[0]['description']=description
  # The integration may synchronize only the two reviewed descriptions. All
  # row membership/order, titles, categories, dates and other fields stay exact.
  if new_catalog not in (old_catalog,expected_catalog):errors.append('scripts/blog-catalog.json: changed beyond two reviewed descriptions')
  for key,value in [('title','Unreviewed title'),('date','2000-01-01'),('category','Unreviewed category'),('url','/unexpected/')]:
   bad=json.loads(json.dumps(expected_catalog));bad[0][key]=value
   assert bad not in (old_catalog,expected_catalog);negative+=1
  bad=json.loads(json.dumps(expected_catalog));bad.append(dict(bad[0]));assert bad not in (old_catalog,expected_catalog);negative+=1
 if root!=REPO:
  for i,f in enumerate(FILES):
   expected=normalize_baseline_html((REPO/f).read_text(),REPO,ROUTES[i]);errors+=preservation(i,expected,docs[i])
   if mainhtml(expected)!=mainhtml(docs[i]):errors.append(f+': staged main differs from exact allowed build transforms')
   assert mainhtml(expected)!=mainhtml(docs[i].replace('</main>','<p>Unexpected public content</p></main>'));negative+=1
 xml='\n'.join(x.read_text() for x in root.glob('sitemap*.xml'))
 holds=json.loads((REPO/'discovery_review_holds.json').read_text())
 redirects=json.loads((REPO/'vercel.json').read_text()).get('redirects',[])
 for route in ROUTES:
  if '<loc>'+SITE+route+'</loc>' not in xml:errors.append(route+': sitemap entry missing')
  if route in holds:errors.append(route+': route is held')
  if any(x.get('source') in [route,route.rstrip('/')] and x.get('destination') not in [route,route.rstrip('/')] for x in redirects):errors.append(route+': redirect away')
 print(json.dumps({'root':str(root),'pages':5,'math_checks':math_checks(),'negative_fixtures':negative,'source_parity':not any('source' in e for e in errors),'baseline_checks':bool(a.baseline),'errors':errors},indent=2));return bool(errors)
if __name__=='__main__':sys.exit(main())
