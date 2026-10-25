#!/usr/bin/env python3
"""Verify every allowed provider owns three indexable pages with primary sources."""
import json,re,sys,xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
REPO=Path(__file__).resolve().parents[1]
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else REPO
SITE='https://www.aetaxadvisors.com'
EXCLUDED=re.compile(r'nth[\s._-]*degree|nthdegree|dan\s+nicholson',re.I)
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.h1=0;self.links=[];self.canonical='';self.indexable=True;self.redirect=False;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if tag=='a':self.links.append(a.get('href',''))
  if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href')
  if tag=='meta' and a.get('name') in ('robots','googlebot') and 'noindex' in a.get('content',''):self.indexable=False
  if tag=='meta' and a.get('http-equiv','').lower()=='refresh':self.redirect=True
manifest=json.loads((REPO/'content/provider-page-ownership-20261024.json').read_text())
providers=manifest['providers'];errors=[];urls=set();titles={}
assert len(providers)==100
assert len({r['slug'] for r in providers})==100
assert not EXCLUDED.search(json.dumps(manifest))
for folder in ('content','_gen'):
 for f in (REPO/folder).rglob('*'):
  if f.is_file() and f.suffix in ('.json','.csv','.tsv','.md'):
   assert not EXCLUDED.search(f.read_text()),'Excluded provider in generator data: '+str(f)
redirects={r['source'] for r in json.loads((REPO/'vercel.json').read_text()).get('redirects',[])}
sitemap=set(e.text for e in ET.parse(ROOT/'sitemap-comparisons.xml').findall('.//{*}loc'))
for r in providers:
 triple=[r[k] for k in ('pricing_url','alternative_url','comparison_url')]
 assert len(set(triple))==3,r['slug']
 for url in triple:
  path=url.removeprefix(SITE);f=ROOT/path.strip('/')/'index.html'
  if not f.exists():errors.append(url+': missing');continue
  text=f.read_text();p=Page(text)
  if url in urls:errors.append(url+': shared page')
  urls.add(url)
  if p.h1!=1 or p.canonical!=url or not p.indexable or p.redirect or path in redirects:errors.append(url+': invalid canonical/indexability/heading')
  if EXCLUDED.search(text):errors.append(url+': excluded content')
  if r['official_source'] not in p.links:errors.append(url+': missing own website source')
  if url==r['alternative_url'] and text.count('id="provider-review"')!=1:errors.append(url+': missing or duplicate review anchor')
  for peer in triple:
   if peer not in p.links and peer.removeprefix(SITE) not in p.links:errors.append(url+': missing reciprocal link '+peer)
  if url not in sitemap:errors.append(url+': missing sitemap')
  for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):json.loads(raw)
  title=re.search(r'<title>(.*?)</title>',text,re.S)[1]
  if title in titles:errors.append(url+': duplicate title with '+titles[title])
  titles[title]=url
assert len(urls)==300
price_data=json.loads((ROOT/'compare/competitor-pricing/prices.json').read_text())
assert len(price_data['providers'])==100
assert {r['slug'] for r in price_data['providers']}=={r['slug'] for r in providers}
assert not EXCLUDED.search(json.dumps(price_data))
assert not errors,'\n'.join(errors)
print('PASS: 100 providers, 300 distinct self-canonical indexable pages, official sources, reciprocal links, unique titles, JSON-LD, sitemaps, and exclusion policy.')
