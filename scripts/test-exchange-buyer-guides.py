#!/usr/bin/env python3
"""Read-only source/public checks for the five reviewed 1031 buyer guides.
Negative fixtures are in-memory and never enter public output.
"""
import argparse,ast,hashlib,html,json,re,sys
from pathlib import Path
from html.parser import HTMLParser
SITE='https://www.aetaxadvisors.com'
PAGES={
 'the-business-owners-guide-to-section-1031-like-kind-exchanges-and-tax-deferral/index.html':'2024-10-30T00:00:00-04:00',
 'the-business-owners-guide-to-section-1031-like-kind-exchanges-and-deferral-strategy/index.html':'2025-06-24T00:00:00-04:00',
 '1031-exchange-explained-defer-capital-gains/index.html':'2025-07-03T00:00:00-04:00',
 'blog/common-1031-exchange-mistakes/index.html':'2026-04-08',
 'blog/1031-exchange-planning-timing/index.html':'2026-07-17',
}
STALE=[
 'foreign real property do not qualify', 'equal or greater debt to achieve full deferral',
 'no extensions for any reason', 'strict deadlines with no extensions',
 'identification deadline is July 15', 'ordinary income rates (up to 25%)',
 'net boot received: $200,000', '37% rate on $2 million gain',
 'replacement property should have higher value than relinquished property, avoiding boot recognition',
 'This tax cannot be deferred through 1031 mechanism', 'approximately $56,000 in federal tax at 28 percent',
 'Using a qualified intermediary is mandatory and non-negotiable',
 'Without a QI, the exchanger takes constructive receipt',
 'If your closing attorney also serves as your QI, the exchange is invalid',
 'recaptured at a 25% federal rate', 'equal or greater value while also assuming equal or greater debt',
 'The qualified intermediary (QI) is the linchpin of every 1031 exchange',
 'The Tax Cuts and Jobs Act clarified that real property is like-kind regardless of location',
 'Strategic geographic replacement property selection creates permanent tax savings',
 'A properly structured exchange defers the entire gain including recapture',
 'third-party facilitator licensed and bonded',
 'a "reverse exchange" (Treas. Reg. 1.1031(k)-1(c)(4))',
]
PROTECTED={'the-business-owners-guide-to-section-1031-like-kind-exchanges-and-deferral-strategy/index.html': {'Case Study: Multi-Property Portfolio 1031 Exchange': '9ae02bd08060a01728342d35213d13ae171664094e34f5fe229539142d4c12e8'}, '1031-exchange-explained-defer-capital-gains/index.html': {'Real Application Example': '401a480013ebfc593361ccab17a1f38eddfaede2eb80206dcb599e828d49e48d'}}
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.tags=[];self.words=[];self.skip=0
 def handle_starttag(self,t,a):
  self.tags.append((t,dict(a)))
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip-=1
 def handle_data(self,s):
  if not self.skip:self.words.append(s)
def text(s):
 p=Parser();p.feed(s);return ' '.join(' '.join(p.words).split())
def schemas(s):return [json.loads(x) for x in re.findall(r'<script\b[^>]*type=[\'"]application/ld\+json[\'"][^>]*>(.*?)</script>',s,re.S)]
def protected(s,heading):
 return re.search(r'<h2>'+re.escape(heading)+r'</h2>\s*<p>.*?</p>',s,re.S)[0]
def check_page(path,s):
 errors=[]
 def check(ok,msg):
  if not ok:errors.append(path+': '+msg)
 p=Parser();p.feed(s);plain=text(s);raw=html.unescape(s);route='/'+path[:-10]
 main=re.search(r'<main\b[^>]*>(.*?)</main>',s,re.S);check(bool(main),'main missing');visible=text(main[1]) if main else ''
 check([a.get('href') for t,a in p.tags if t=='link' and a.get('rel')=='canonical']==[SITE+route],'canonical changed')
 check(len(re.findall(r'<h1\b',s))==1,'expected one H1')
 check(not any('noindex' in a.get('content','') for t,a in p.tags if t=='meta' and a.get('name','').lower() in ['robots','googlebot']),'unexpected noindex')
 for stale in STALE:check(stale.lower() not in raw.lower(),'stale claim: '+stale)
 for token in ['earlier of 180','including extensions','IRS relief','foreign-to-foreign','additional cash','cash retained','recapture','25%','November 6, 2026']:
  check(token.lower() in plain.lower(),'missing rule: '+token)
 check('https://www.irs.gov/instructions/i8824' in s and 'https://www.irs.gov/publications/p544' in s,'missing primary sources')
 check('routine financial, title-insurance, escrow, or trust services' in plain,'QI exception missing')
 check('not mandatory' in plain or 'not required for every' in plain or 'not a requirement for every' in plain or 'not the only possible' in plain or 'not automatically constructive receipt' in plain,'QI safe-harbor distinction missing')
 if path in [list(PAGES)[0],list(PAGES)[1],list(PAGES)[4]]:
  for token in ['EAT','QEAA','5 business days','180 days','Revenue Procedure 2004-51']:
   check(token in visible,'reverse safe-harbor detail missing: '+token)
 if path in [list(PAGES)[2],list(PAGES)[3],list(PAGES)[4]]:
  check(('cash-out' in visible or 'cashes out' in visible) and ('two-year' in visible or 'two years' in visible),'related-party cash-out or holding rule missing')
 if path in [list(PAGES)[1],list(PAGES)[2],list(PAGES)[4]]:
  check('July 16' in visible and 'November 28' in visible,'June 1 arithmetic missing')
 if path==list(PAGES)[1]:
  for token in ['$500 to $1,500','$2,000 to $4,000','1% to 3%','$1.6 million','Replacement basis is $400,000']:
   check(token in visible,'fee or basis illustration lost: '+token)
 if path==list(PAGES)[0]:check('no net debt-relief boot' in visible,'cash-replaces-debt illustration missing')
 if path==list(PAGES)[2]:check('FTB 3840' in visible and 'California-source deferred gain' in visible,'state-source warning missing')
 for link in ['/discovery/','/case-studies/']:
  check(any(t=='a' and a.get('href')==link for t,a in p.tags),'conversion/case link missing: '+link)
 for heading,digest in PROTECTED.get(path,{}).items():
  try:actual=hashlib.sha256(protected(s,heading).encode()).hexdigest()
  except (AttributeError,IndexError):actual=None
  check(actual==digest,'protected reported outcome changed: '+heading)
 ds=schemas(s)
 for item in [d for d in ds if d.get('@type') in ['Article','BlogPosting']]:
  check(item.get('dateModified')=='2026-11-06','article modified date not aligned')
  check(item.get('description')==next(a.get('content') for t,a in p.tags if t=='meta' and a.get('name')=='description'),'article description not aligned')
 articles=[d for d in ds if d.get('@type')=='BlogPosting'];check(len(articles)==1,'expected one article schema')
 if articles:
  a=articles[0];check(a.get('datePublished')==PAGES[path],'publication changed');check(a.get('dateModified')=='2026-11-06','modified date missing')
  h=re.search(r'<h1\b[^>]*>(.*?)</h1>',s,re.S)
  check(bool(h) and a.get('headline')==text(h[1]),'schema headline differs from visible H1')
  for key in ['description','og:description','twitter:description']:
   check([attrs.get('content') for t,attrs in p.tags if t=='meta' and (attrs.get('name')==key or attrs.get('property')==key)]==[a.get('description')],'description mismatch: '+key)
 for faq in [d for d in ds if d.get('@type')=='FAQPage']:
  for q in faq.get('mainEntity',[]):
   check(text(q['name']) in visible,'FAQ question not visible')
   check(text(q['acceptedAnswer']['text']) in visible,'FAQ answer not visible')
 return errors

def fixtures(docs):
 path=list(PAGES)[0];good=docs[path];n=0
 for stale in STALE:
  assert check_page(path,good.replace('</main>','<p>'+stale+'</p></main>')),stale;n+=1
 for old,new in [('rel="canonical"','rel="alternate"'),('2024-10-30T00:00:00-04:00','2026-11-06'),('"text": "Boot includes cash','"text": "Unmatched FAQ. Boot includes cash')]:
  assert old in good;assert check_page(path,good.replace(old,new)),old;n+=1
 for path,items in PROTECTED.items():
  for heading in items:
   block=protected(docs[path],heading)
   assert check_page(path,docs[path].replace(block,block.replace('$','$1',1))),heading;n+=1
 return n

def main():
 p=argparse.ArgumentParser();p.add_argument('root',nargs='?',default='.');p.add_argument('--baseline');args=p.parse_args();root=Path(args.root).resolve()
 docs={name:(root/name).read_text() for name in PAGES};errors=[e for name,s in docs.items() for e in check_page(name,s)]
 n=fixtures(docs)
 xml='\n'.join(p.read_text() for p in root.glob('sitemap*.xml'))
 if xml:
  for name in PAGES:
   if '<loc>'+SITE+'/'+name[:-10]+'</loc>' not in xml:errors.append(name+': sitemap entry missing')
 if args.baseline:
  base=Path(args.baseline)
  for i,(name,s) in enumerate(docs.items(),1):
   old=(base/f'{i}.html').read_text()
   for tag in ['header','footer']:
    pattern=r'<'+tag+r'\b[^>]*>.*?</'+tag+'>'
    if re.findall(pattern,old,re.S)!=re.findall(pattern,s,re.S):errors.append(name+': '+tag+' changed')
   old_pub=[d.get('datePublished') for d in schemas(old) if 'datePublished' in d];new_pub=[d.get('datePublished') for d in schemas(s) if 'datePublished' in d]
   if old_pub!=new_pub:errors.append(name+': schema publication dates changed')
   before=Parser();before.feed(old);after=Parser();after.feed(s)
   old_meta=[a for t,a in before.tags if t=='meta' and a.get('property')=='article:published_time'];new_meta=[a for t,a in after.tags if t=='meta' and a.get('property')=='article:published_time']
   if old_meta!=new_meta:errors.append(name+': publication metadata changed')
   old_links=[a['href'] for t,a in before.tags if t=='a' and a.get('href','').startswith('/')]
   new_links=[a['href'] for t,a in after.tags if t=='a' and a.get('href','').startswith('/')]
   if sorted(old_links)!=sorted(new_links):errors.append(name+': internal links changed')
  old=(base/'seo_topics.py').read_text();new=(root/'seo_topics.py').read_text()
  old_tree=ast.parse(old);new_tree=ast.parse(new)
  def strings(tree):return [n for n in ast.walk(tree) if isinstance(n,ast.Constant) and isinstance(n.value,str)]
  a,b=strings(old_tree),strings(new_tree);changes=[(x,y) for x,y in zip(a,b) if x.value!=y.value]
  if len(a)!=len(b) or len(changes)!=4:errors.append('seo_topics.py: expected only four string changes')
  for x,y in changes:x.value=y.value
  if ast.dump(old_tree)!=ast.dump(new_tree):errors.append('seo_topics.py: unrelated AST changes')
 print(json.dumps({'root':str(root),'pages':len(docs),'negative_fixtures':n,'baseline_checks':bool(args.baseline),'errors':errors},indent=2));return bool(errors)
if __name__=='__main__':sys.exit(main())
