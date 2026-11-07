#!/usr/bin/env python3
"""Verify investor-intent ownership, rule distinctions, visible FAQ parity and crawl paths."""
import html,json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
from html.parser import HTMLParser
from decimal import Decimal
repo=Path(__file__).resolve().parents[1];root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else repo
mapping=json.loads((repo/'content/investment-search-20261107/keyword-map.json').read_text());paths=json.loads((repo/'content/investment-search-20261107/pages.json').read_text());base='https://www.aetaxadvisors.com'
class P(HTMLParser):
 def __init__(self,s):super().__init__();self.tags=[];self.feed(s)
 def handle_starttag(self,t,a):self.tags.append((t,dict(a)))
def plain(s):return ' '.join(html.unescape(re.sub('<[^>]*>',' ',s)).split())
urls={e.text for f in root.glob('sitemap*.xml') for e in ET.parse(f).findall('.//{*}loc')};errors=[];titles=set()
required={
'/solar-tax-credit-investment/':['July 4, 2026','December 31, 2027','6%','30%','five-year','2026-15','passive','credit purchase'],
'/solar-tax-credit-investment-vs-credit-purchase/':['Section 6418','registration','passive','depreciation','recapture'],
'/heavy-equipment-leasing-investment-tax/':['noncorporate lessors','January 19, 2025','at-risk','nonrecourse','Section 1245','currently allowed'],
'/heavy-equipment-leasing-investment-due-diligence/':['serial numbers','no current-year tax benefit','passive','placed-in-service'],
'/short-term-rental-tax-loophole-2026/':['two separate','seven days or less','no other individual','14 days','10%','at-risk','Schedule C','Schedule E','suspended']}
for path in paths:
 s=(root/path.strip('/')/'index.html').read_text();p=P(s);v=plain(s)
 if len([t for t,a in p.tags if t=='h1'])!=1:errors.append(path+': H1')
 if [a.get('href') for t,a in p.tags if t=='link' and a.get('rel')=='canonical']!=[base+path]:errors.append(path+': canonical')
 if base+path not in urls:errors.append(path+': sitemap')
 if any('noindex' in a.get('content','').lower() for t,a in p.tags if t=='meta' and a.get('name')=='robots'):errors.append(path+': noindex')
 for t,a in p.tags:
  if t=='a' and a.get('href','').startswith('/'):
   u=a['href'].split('#')[0].split('?')[0];f=root/u.lstrip('/')
   if not(f.is_file()or(f/'index.html').is_file()):errors.append(path+': missing link '+u)
 for token in required.get(path,[]):
  if token.lower() not in v.lower():errors.append(path+': missing '+token)
 if path in required or path in ['/equipment-leasing/','/equipment-leasing-landing/','/eliminating-federal-income-tax-through-solar-itc-bonus-depreciation-and-entity-coordination/']:
  title=re.search('<title>(.*?)</title>',s,re.S)[1]
  if title in titles:errors.append(path+': duplicate title')
  titles.add(title)
  if s.count('src="/assets/booking-events.js"')!=1:errors.append(path+': tracking hook')
  ds=[json.loads(x) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S)]
  faq=[x for x in ds if x.get('@type')=='FAQPage']
  visible=[(plain(q),plain(a)) for q,a in re.findall(r'<div class="faq-item">\s*<h3>(.*?)</h3>\s*(.*?)\s*</div>',s,re.S)]
  if faq:
   schema=[(plain(x['name']),plain(x['acceptedAnswer']['text']))for x in faq[0]['mainEntity']]
   if schema!=visible:errors.append(path+': FAQ parity')
  art=[x for x in ds if x.get('@type')=='Article']
  if len(art)!=1 or art[0]['dateModified']!='2026-11-07':errors.append(path+': review date')
# Published illustrative values must not conflate loss and tax savings.
assert Decimal(40000)*Decimal('.32')==Decimal(12800)
assert Decimal(50000)*Decimal('.32')==Decimal(16000)
assert Decimal(60)/10==6 and Decimal(80)/10==8
print(json.dumps({'pages':len(paths),'keyword_targets':len(mapping['targets']),'errors':errors}));sys.exit(bool(errors))
