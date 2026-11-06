#!/usr/bin/env python3
"""Focused checks for four sale guides; negative fixtures remain in memory."""
import argparse, ast, hashlib, html, json, re, sys
from decimal import Decimal as D
from html.parser import HTMLParser
from pathlib import Path
from tax_review_build_normalization import normalize_baseline_html
from installment_consolidation_contract import reconcile_sale_baseline, retirement_errors
REPO=Path(__file__).resolve().parents[1]
ROUTES=json.loads((REPO/'scripts/sale-buyer-guide-routes-20261106.json').read_text())
FILES=[r.strip('/')+'/index.html' for r in ROUTES]
SITE='https://www.aetaxadvisors.com'
REQUIRED=[
 ['$120,000','$80,000','$480,000','60%','$275,000','$7,000,000','$1,500,000','$3,500,000','50%','$300,000','Section 453(e)','Section 453(g)','unrecaptured Section 1250','maximum 25%','can interact','collection risk','no debt','each principal payment is allocated','Separate asset-level basis','https://www.irs.gov/publications/p537'],
 ['$1,000,000','$180,000','$400,000','$1,400,000','$580,000','$820,000','land','both closing statements','depreciation schedule','not a safe harbor','maximum 25%','https://www.irs.gov/publications/p551','https://www.irs.gov/publications/p946'],
 ['Doing it years earlier does not','from the original acquisition','including a corporation','shareholder','built-in gains','https://www.irs.gov/publications/p542','https://www.irs.gov/publications/p544','not automatically tax-free','historically defective S election','Section 751','Section 743(b)','Land is not depreciable','acquisition date'],
 ['qualifying stock purchase','deemed sale','80%','12-month','all S corporation shareholders','Form 8883','Form 8023','Form 8594','$1,166,200','$1,950,298','$784,098','carry over','does not automatically step up','$7,800','$9,800','https://www.irs.gov/instructions/i8023','https://www.irs.gov/instructions/i8883']
]
STALE=[
 'reduce total tax burden by 15% to 25%', 'cash is taxable in year of sale as boot',
 'cash and other property received in the year of sale are treated as boot',
 'distinct and not integrated', '$150,000 annually for 7 years', '$1,220,000 of excess basis',
 'replacement cost exceeds the relinquished basis plus boot','Carryover basis is not eligible for bonus depreciation.',
 'Doing it years earlier, or holding the property in a separate entity from the start, avoids that outcome',
 'an asset sale can be treated as a stock sale', 'those taxes could be reduced to $800,000-$1,000,000',
 'You must file Form 8594', 'with better control', 'standard solution is a drop and swap',
 'which is unavailable on the sale of an operating business',
 'the five-year qualified small business stock holding period', 'The F reorganization gives the buyer a basis step-up and the seller one level of tax.',
 'Structure moves the effective rate on a sale by fifteen points or more',
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
def page_errors(i,s):
 errors=[]
 def check(ok,msg):
  if not ok:errors.append(FILES[i]+': '+msg)
 p=Parser();p.feed(s);main=re.search(r'<main\b[^>]*>(.*?)</main>',s,re.S);check(bool(main),'missing main');visible=plain(main[1]) if main else '';raw=html.unescape(s)
 check([a.get('href') for t,a in p.tags if t=='link' and a.get('rel')=='canonical']==[SITE+ROUTES[i]],'canonical')
 check(len(re.findall(r'<h1\b',s))==1,'H1 count')
 check(not any('noindex' in a.get('content','') for t,a in p.tags if t=='meta' and a.get('name') in ['robots','googlebot']),'noindex')
 for token in REQUIRED[i]:check(token in raw or token in visible,'missing '+token)
 for token in STALE:check(token.lower() not in raw.lower(),'stale '+token)
 check('November 6, 2026' in visible,'visible review date')
 h=plain(re.search(r'<h1\b[^>]*>(.*?)</h1>',s,re.S)[1]);a=[d for d in schemas(s) if d.get('@type') in ['Article','BlogPosting']];check(len(a)==1,'article count')
 if a:
  check(a[0].get('headline')==h,'headline parity');check(a[0].get('dateModified')=='2026-11-06','modified date')
  for key in ['description','og:description','twitter:description']:
   check([x.get('content') for t,x in p.tags if t=='meta' and (x.get('name')==key or x.get('property')==key)]==[a[0].get('description')],'description parity '+key)
 f=[d for d in schemas(s) if d.get('@type')=='FAQPage'];check(len(f)==1,'FAQ count')
 for item in schemas(s):
  if item.get('@type')=='WebPage' and 'dateModified' in item:check(item['dateModified']=='2026-11-06','WebPage modified date')
 for d in f:
  for q in d.get('mainEntity',[]):
   check(plain(q['name']) in visible,'FAQ question parity');check(plain(q['acceptedAnswer']['text']) in visible,'FAQ answer parity')
 check(any(t=='a' and x.get('href')=='/discovery/' for t,x in p.tags),'booking link')
 return errors

def outside_assignment(s,name):
 tree=ast.parse(s);node=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets));lines=s.splitlines(keepends=True);return ''.join(lines[:node.lineno-1])+''.join(lines[node.end_lineno:])
def source_entry(s):
 tree=ast.parse(s);return next(n for n in ast.walk(tree) if isinstance(n,ast.Dict) and any(isinstance(k,ast.Constant) and k.value=='slug' and isinstance(v,ast.Constant) and v.value=='1031-exchange-planning' for k,v in zip(n.keys,n.values)))
def without_entry(s):
 n=source_entry(s);lines=s.splitlines(keepends=True);start=sum(len(x) for x in lines[:n.lineno-1])+n.col_offset;end=sum(len(x) for x in lines[:n.end_lineno-1])+n.end_col_offset;return s[:start]+s[end:]
def source_errors(docs):
 errors=[];hub=(REPO/'scripts/batch_hubs.py').read_text();entry=source_entry(hub);values={k.value:v for k,v in zip(entry.keys,entry.values)}
 for h,ps in ast.literal_eval(values['sections']):
  if plain(h) not in plain(docs[1]):errors.append('source hub heading mismatch '+h)
  for p in ps:
   if plain(p) not in plain(docs[1]):errors.append('source hub paragraph mismatch '+h)
 for q,a in ast.literal_eval(values['faqs']):
  if plain(q) not in plain(docs[1]) or plain(a) not in plain(docs[1]):errors.append('source hub FAQ mismatch')
 src=(REPO/'cluster_c8.py').read_text();n=next(n for n in ast.parse(src).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='STRUCTURE' for t in n.targets));values={k.arg:k.value for k in n.value.keywords}
 for h,p in ast.literal_eval(values['body']):
  if plain(h) not in plain(docs[2]) or plain(p) not in plain(docs[2]):errors.append('source STRUCTURE mismatch '+h)
 for q,a in ast.literal_eval(values['faqs']):
  if plain(q) not in plain(docs[2]) or plain(a) not in plain(docs[2]):errors.append('source STRUCTURE FAQ mismatch')
 return errors

def preservation(i,old,new):
 old=reconcile_sale_baseline(old,new,ROUTES[i])
 errors=[]
 for tag in ['header','footer']:
  pat=r'<'+tag+r'\b[^>]*>.*?</'+tag+'>'
  if re.findall(pat,old,re.S)!=re.findall(pat,new,re.S):errors.append(FILES[i]+': '+tag+' preservation')
 for field in ['datePublished']:
  if [d[field] for d in schemas(old) if field in d]!=[d[field] for d in schemas(new) if field in d]:errors.append(FILES[i]+': '+field+' preservation')
 a,b=Parser(),Parser();a.feed(old);b.feed(new)
 for key in ['article:published_time']:
  if [x for t,x in a.tags if t=='meta' and x.get('property')==key]!=[x for t,x in b.tags if t=='meta' and x.get('property')==key]:errors.append(FILES[i]+': publication metadata preservation')
 internal=lambda p:sorted(x['href'] for t,x in p.tags if t=='a' and x.get('href','').startswith('/'))
 if internal(a)!=internal(b):errors.append(FILES[i]+': internal navigation preservation')
 pat=r'<div class=[\'"]post-cta[\'"]>.*?</div>'
 if re.findall(pat,old,re.S)!=re.findall(pat,new,re.S):errors.append(FILES[i]+': original CTA preservation')
 if i==3:
  # Entire existing premium CTA text is outside the authored article body.
  old_cta=old[old.index('Bring your advisor into the sale discussion early'):old.index('</main>')]
  new_cta=new[new.index('Bring your advisor into the sale discussion early'):new.index('</main>')]
  if old_cta!=new_cta:errors.append(FILES[i]+': premium CTA preservation')
 return errors

def math_checks():
 assert (D(1000000)-D(400000))/D(1000000)==D('.6')
 assert D(200000)*D('.6')==D(120000)
 assert D(800000)*D('.6')==D(480000)
 assert sum(D(1000000-100000*i)*D('.05') for i in range(10))==D(275000)
 assert D(4500000)-D(2500000)==D(2000000)
 assert D(2000000)+D(1500000)==D(3500000)
 assert (D(7000000)-D(3500000))/D(7000000)==D('.5')
 assert D(1500000)+D(1000000)*D('.5')+10*D(600000)*D('.5')==D(5000000)
 assert D(180000)+D(400000)==D(580000)
 assert D(1400000)-D(580000)==D(820000)
 assert D(4900000)*D('.238')==D(1166200)
 assert D(4900000)*D('.21')==D(1029000)
 assert (D(5000000)-D(1029000)-D(100000))*D('.238')==D(921298)
 assert D(1029000)+D(921298)==D(1950298)
 assert D(1950298)-D(1166200)==D(784098)
 return 15

def main():
 p=argparse.ArgumentParser();p.add_argument('root',nargs='?',default=str(REPO));p.add_argument('--baseline');a=p.parse_args();root=Path(a.root).resolve();docs=[(root/f).read_text() for f in FILES];errors=[]
 for i,s in enumerate(docs):errors+=page_errors(i,s)
 errors+=source_errors(docs);negative=0
 for stale in STALE:
  assert page_errors(0,docs[0].replace('</main>','<p>'+stale+'</p></main>'));negative+=1
 for i,token in [(0,'$120,000'),(0,'$275,000'),(0,'$300,000'),(1,'$580,000'),(1,'$400,000'),(2,'Doing it years earlier does not'),(3,'$1,950,298'),(3,'Form 8883'),(3,'$7,800'),(3,'$9,800')]:
  assert page_errors(i,docs[i].replace(token,'REMOVED'));negative+=1
 for i in range(4):
  for old,new in [('rel="canonical"','rel="alternate"'),('"dateModified": "2026-11-06"','"dateModified": "2020-01-01"'),('"acceptedAnswer": {','"acceptedAnswer": {')]:
   if old==new:continue
   assert page_errors(i,docs[i].replace(old,new));negative+=1
  a0=next(x for x in schemas(docs[i]) if x.get('@type')=='FAQPage')['mainEntity'][0]['acceptedAnswer']['text'];bad=docs[i].replace(json.dumps(a0,ensure_ascii=False),json.dumps('Unmatched answer '+a0,ensure_ascii=False),1)
  assert page_errors(i,bad);negative+=1
 if a.baseline:
  base=Path(a.baseline)
  for i,f in enumerate(FILES):
   old=(base/f).read_text();current=(REPO/f).read_text();errors+=preservation(i,old,current);bad=current.replace('href="/discovery/"','href="/removed/"',1);assert preservation(i,old,bad);negative+=1
  for f,strip in [('cluster_c8.py',lambda s:outside_assignment(s,'STRUCTURE')),('scripts/batch_hubs.py',without_entry)]:
   if strip((base/f).read_text())!=strip((REPO/f).read_text()):errors.append(f+': unrelated source bytes changed')
  placeholder='the-business-owners-guide-to-section-453-installment-sales-and-deferred-gain-recognition/index.html'
  if (REPO/placeholder).read_bytes()!=(base/placeholder).read_bytes():errors+=retirement_errors(REPO)
 if root!=REPO:
  for i,f in enumerate(FILES):
   expected=normalize_baseline_html((REPO/f).read_text(),REPO,ROUTES[i]);errors+=preservation(i,expected,docs[i])
   main=lambda x:re.search(r'<main\b[^>]*>.*?</main>',x,re.S)[0]
   if main(expected)!=main(docs[i]):errors.append(f+': staged main content preservation')
   assert main(expected)!=main(docs[i].replace('</main>','<p>Unexpected injected content</p></main>'));negative+=1
 xml='\n'.join(x.read_text() for x in root.glob('sitemap*.xml'))
 for route in ROUTES:
  if '<loc>'+SITE+route+'</loc>' not in xml:errors.append(route+': sitemap entry missing')
 print(json.dumps({'root':str(root),'pages':4,'math_checks':math_checks(),'negative_fixtures':negative,'source_parity':True,'baseline_checks':bool(a.baseline),'errors':errors},indent=2));return bool(errors)
if __name__=='__main__':sys.exit(main())
