#!/usr/bin/env python3
"""Focused read-only source/staged content, metadata, FAQ, math and preservation checks."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
from decimal import Decimal as D
import hashlib,html,json,re,sys
REPO=Path(__file__).resolve().parents[1]
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else REPO
DATA=json.loads((REPO/'content/owner-exit-guides-20261106.json').read_text())
CONTEXT='source' if ROOT==REPO else 'public'
COUNT=0
DOMAIN='https://www.aetaxadvisors.com'
def check(ok,m):
 global COUNT
 COUNT+=1
 assert ok,m
def plain(x):return ' '.join(html.unescape(re.sub('<[^>]*>',' ',x)).split())
def walk(o):
 if isinstance(o,dict):
  yield o
  for v in o.values():yield from walk(v)
 elif isinstance(o,list):
  for v in o:yield from walk(v)
def docs(s):return [x for raw in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S) for x in walk(json.loads(raw))]
class Page(HTMLParser):
 def __init__(self,s):
  super().__init__();self.links=[];self.ids=[];self.meta={};self.canon=[];self.stack=[];self.errors=[];self.h1=0;self.feed(s)
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='a' and 'href' in d:self.links.append(d['href'])
  if t=='meta':self.meta[d.get('name',d.get('property',''))]=d.get('content','')
  if t=='link' and d.get('rel')=='canonical':self.canon.append(d['href'])
  if t=='h1':self.h1+=1
  if 'id' in d:self.ids.append(d['id'])
  if t not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:self.stack.append(t)
 def handle_endtag(self,t):
  if self.stack and self.stack[-1]==t:self.stack.pop()
  else:self.errors.append(t)
REDIR=json.loads((REPO/'scripts/content-consolidation.json').read_text()).get('redirects',{})
REDIR.update({x['source']:x['destination'] for x in json.loads((REPO/'vercel.json').read_text()).get('redirects',[]) if ':' not in x['source']})
HOLDS=json.loads((REPO/'discovery_review_holds.json').read_text())
def resolve(p):
 seen=set()
 while p in REDIR:
  assert p not in seen;seen.add(p);p=REDIR[p]
 return p
BAD=[
 'Accelerating depreciation on retained properties under IRC Section 168(k) can generate losses that offset ordinary income recognized from the business sale',
 'Allocations to goodwill (Class VII) receive capital gain treatment',
 'taxes that were entirely avoidable with a three-year head start',
 'For married couples who each hold qualifying stock, the combined exclusion can reach $20 million',
 'Every month of delay narrows the available strategies and increases the tax cost of your exit',
 'The sale automatically makes rent subject to NIIT',
 'You automatically lose QBI after selling the tenant business',
 'A cost segregation study automatically releases prior passive losses',
 'A 1031 exchange releases all suspended passive losses',
]
def claims_ok(text):return not any(x in text for x in BAD)
SEARCH=json.loads((ROOT/'assets/blog-search-index.json').read_text())
PAGES={}
for e in DATA['routes']:
 route=e['route'];s=(ROOT/route.strip('/')/'index.html').read_text();p=Page(s);dd=docs(s)
 check(not p.errors and not p.stack,route+' balanced HTML: '+str(p.errors))
 check(p.h1==1,route+' one H1');check(len(p.ids)==len(set(p.ids)),route+' unique IDs')
 check(p.canon==[DOMAIN+route],route+' self canonical');check('noindex' not in p.meta.get('robots',''),route+' indexable')
 a=[x for x in dd if x.get('@type') in ['Article','BlogPosting']];check(len(a)==1,route+' one article');a=a[0]
 check(a['datePublished']==e['datePublished'],route+' original publication')
 check(a['dateModified']==DATA['reviewed'] and 'November 6, 2026' in s,route+' visible/schema update')
 check(a['headline']==plain(re.search(r'<h1[^>]*>(.*?)</h1>',s,re.S)[1]),route+' headline parity')
 check(a['url']==DOMAIN+route,route+' schema URL')
 check(plain(re.search(r'<title>(.*?)</title>',s,re.S)[1])==p.meta['og:title']==p.meta['twitter:title']==e['title'],route+' titles')
 check(p.meta['description']==p.meta['og:description']==p.meta['twitter:description']==a['description']==e['description'],route+' descriptions')
 check(100<=len(e['description'])<=170 and e['description'].endswith('.'),route+' complete description')
 faq=[x for x in dd if x.get('@type')=='FAQPage'];check(len(faq)==1,route+' one FAQ schema')
 expected=[(x['name'],x['acceptedAnswer']['text']) for x in faq[0]['mainEntity']]
 visible=[(plain(q),plain(ans)) for q,ans in re.findall(r'<div class="faq-item">\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>\s*</div>',s,re.S)]
 check(expected==visible and len(expected)>=4,route+' exact visible FAQ/schema parity')
 check(route not in REDIR and route not in HOLDS,route+' active route')
 row=[x for x in SEARCH if x['url']==route];check(len(row)==1 and row[0]['description']==e['description'],route+' search description')
 check(row[0]['date']==e['datePublished'],route+' search publication date')
 cards=[c for pth in (ROOT/'blog/page').glob('*/index.html') for c in re.findall(r'<article class="blog-card">.*?</article>',pth.read_text(),re.S) if 'href="'+route+'"' in c]
 check(len(cards)==1 and plain(re.search(r'<p>(.*?)</p>',cards[0],re.S)[1])==e['description'],route+' archive description')
 check('datetime="'+e['datePublished']+'"' in cards[0],route+' archive publication date')
 for source in e['sources']:check(source in p.links,route+' cited source '+source)
 main=re.search(r'<main[^>]*>(.*?)</main>',s,re.S)[1]
 for href in Page(main).links:
  u=urlsplit(href)
  if (u.netloc and u.netloc!='www.aetaxadvisors.com') or not u.path.startswith('/'):continue
  dest=resolve(u.path);check(dest not in HOLDS,route+' link not held '+dest)
  f=ROOT/dest.lstrip('/');f=f/'index.html' if dest.endswith('/') else f
  check(f.is_file(),route+' internal link exists '+dest)
  if u.fragment:check(u.fragment in Page(f.read_text()).ids,route+' fragment exists '+href)
 for name,pattern in [('header',r'<header\b[^>]*>.*?</header>'),('footer',r'<footer\b[^>]*>.*?</footer>'),('related',r'<section class="content-section related-reading">.*?</section>')]:
  if name in e['preservation'][CONTEXT]:check(hashlib.sha256(re.search(pattern,s,re.S)[0].encode()).hexdigest()==e['preservation'][CONTEXT][name],route+' preserved '+name)
 check(claims_ok(plain(s)),route+' obsolete/unsafe claims absent')
 for term in ['client-service issue','Search Console','keyword volume','/tmp/','/workspace/','scratch notes','GSC observations']:
  check(term.lower() not in s.lower(),route+' no private text '+term)
 check('/discovery/' in p.links and '/case-studies/' in p.links,route+' discovery and case nav retained')
 PAGES[route]=(s,plain(main))
keep,kt=PAGES['/blog/selling-business-keeping-building-tax-planning/']
loss,lt=PAGES['/blog/rental-losses-offset-business-income/']
time,tt=PAGES['/blog/tax-planning-timeline-before-selling-business/']
for x in ['Section 469','Section 1411','Section 199A','sale-year projection','first-full-post-sale-year projection','common control','triple-net','historical-participation','Owner and bookkeeper','Tax advisor and return preparer','Deal counsel and property manager']:
 check(x in kt,'Retained-building '+x)
inbound='<p>If the buyer also wants the property, compare <a href="/blog/selling-business-and-building-1031-exchange/">selling the business and building together, including a possible exchange of qualifying real estate</a>, before choosing the retained-building route.</p>'
check(keep.count(inbound)==1,'Approved incoming combined-sale paragraph preserved exactly once')
for x in ['Strategic Tax Advisory: $7,800. Complex Tax Advisory: $9,800. Returns, amendments, cost segregation and additional work are separately scoped.','Read a business-sale cash-reserve planning example','This example is illustrative and is not a client result.']:
 check(x in kt,'Retained-building fee/case/example preserved '+x)
for x in ['Identify actual sale income','Classify each activity','Separate loss vintages','Apply loss limits','Recompute the return','at-risk','Section 461(l)','Former-passive-activity','fully taxable','Exchange the rental','Owner-return preparer','Form 3115','$400,000','$70,000','$330,000']:
 check(x in lt,'Loss workpaper '+x)
check(D('400000')-D('70000')==D('330000'),'Original conditional illustration arithmetic')
check(D('70000')+D('30000')-D('20000')==D('80000'),'Sale-year passive-pool arithmetic')
check('not a client result or a complete tax calculation' in lt,'Loss example conditional status')
for x in ['on or before July 4, 2025','after July 4, 2025','September 27, 2010','more than five years','50%','75%','100%','$10 million','$15 million','$50 million','$75 million','10 times','after the ceiling','married-return rules','Depreciation recapture','Section 1245','Section 1231','Section 338(h)(10)','Form 8023','60-day','more than six months','not automatically','not a client result']:
 check(x in tt,'Timeline boundary '+x)
check('Business Owner Saves $28K Optimizing QBI Deduction Before Phase-Out' in tt,'Actual related-case label preserved verbatim')
check((D('8000000')-D('1000000'))/D('8000000')==D('.875'),'Installment 87.5% gross profit')
check(D('1600000')*D('.875')==D('1400000') and D('1600000')-D('1400000')==D('200000'),'Installment gain/basis')
check(D('10000000')*D('.238')==D('2380000'),'Hypothetical 23.8% arithmetic')
check('not merely a $10 million sale price' in tt and 'NIIT applying to all that gain' in tt,'Rate illustration assumptions')
# Mutations must fail the regression detector.
for bad in BAD:check(not claims_ok(tt+' '+bad),'Negative unsafe-claim fixture')
check(claims_ok(tt),'Clean control fixture')
print(json.dumps({'result':'PASS','checks':COUNT,'routes':len(PAGES),'faqs':sum(len([x for x in docs(s) if x.get('@type')=='Question']) for s,_ in PAGES.values()),'negative_fixtures':len(BAD),'root':str(ROOT)},indent=2))
