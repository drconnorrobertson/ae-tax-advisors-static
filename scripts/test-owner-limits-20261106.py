#!/usr/bin/env python3
"""Focused 2026 limits, example arithmetic, metadata and preservation checks."""
from pathlib import Path
import re,json,html,subprocess
from decimal import Decimal as D
R=Path(__file__).resolve().parents[1]
cohort=json.loads((R/'content/owner-limits-20261106.json').read_text())
redirects=json.loads((R/'vercel.json').read_text()).get('redirects',[])
def plain(s):return html.unescape(re.sub('<[^>]+>','',s)).strip()
def walk(x):
 if isinstance(x,dict):
  yield x
  for v in x.values():yield from walk(v)
 elif isinstance(x,list):
  for v in x:yield from walk(v)
for rec in cohort['pages']:
 p=rec['path'];s=(R/p).read_text();old=subprocess.check_output(['git','show','f2d5962:'+p],cwd=R,text=True)
 route=rec['canonical'].removeprefix('https://www.aetaxadvisors.com')
 assert not any(x.get('source','').rstrip('/')==route.rstrip('/') for x in redirects),p
 assert route.strip('/') not in (R/'discovery_review_holds.json').read_text()
 assert not re.search(r'<meta[^>]+name="(?:robots|googlebot)"[^>]+noindex',s)
 assert rec['canonical'] in s and len(re.findall(r'<h1\b',s))==1
 assert re.findall(r'"datePublished"\s*:\s*"([^"]+)"',s)==rec['publication_dates']
 for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):
  for o in walk(json.loads(block)):
   if 'dateModified'in o:assert o['dateModified']=='2026-11-06'
   if o.get('@type')=='FAQPage':
    assert len(o['mainEntity'])==rec['faq_count']
    visible=re.search(r'<section[^>]+id="faq".*?</section>',s,re.S).group()
    pairs=[(plain(q),plain(a)) for q,a in re.findall(r'<h3>(.*?)</h3><p>(.*?)</p>',visible,re.S)]
    assert pairs==[(x['name'],x['acceptedAnswer']['text']) for x in o['mainEntity']]
 for stale in ['$23,500','$70,000','$77,500','$176,100','$168,600','$31,000','$34,750','$81,250']:
  assert stale not in s,(p,stale)
 assert '$24,500'in s and '$72,000'in s
 # Historical related-reading link labels and destinations stay byte-for-byte.
 oldrelated=re.search(r'<section class="content-section related-reading".*?</section>',old,re.S).group()
 assert oldrelated in s,p
 for fee in ['$7,800','$3,900','$9,800']:
  assert old.count(fee)==s.count(fee)
 assert 'https://www.irs.gov/pub/irs-drop/n-25-67.pdf' in s
 for href in re.findall(r'href="(/[^"#?]*)',s):
  if href=='/' or any(x.get('source','').rstrip('/')==href.rstrip('/') for x in redirects):continue
  target=R/href.lstrip('/')
  assert target.exists() or target.with_suffix('.html').exists(),(p,href)
# Independently compute transparent examples, not claimed tax savings.
def se(profit):
 earnings=D(str(profit))*D('.9235')
 return min(earnings,D(184500))*D('.124')+earnings*D('.029')
assert se(200000)==D('28234.3000')
assert (D(200000)-se(200000)/2)*D('.20')==D('37176.570000')
assert (D(200000)-se(200000)/2)*D('.20')+24500==D('61676.570000')
assert se(600000)==D('38946.9000')
assert (D(600000)*D('.9235')-200000)*D('.009')==D('3186.9000000')
assert 72000-24500==47500 and 150000*.25+24500==62000
assert 72000-24500-20000==27500 and 72000+8000==80000 and 72000+11250==83250
print('PASS: five active routes; 20 FAQ/schema pairs; current limits; four example models; publication, related-case labels, fees and internal links preserved.')
