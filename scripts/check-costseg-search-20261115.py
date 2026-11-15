#!/usr/bin/env python3
"""Validate the complete cost-seg directory and its existing provider routes."""
import json,re,sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse,unquote
REPO=Path(__file__).resolve().parents[1]
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else REPO
DATA=json.loads((REPO/'content/costseg-search-optimization-20261115.json').read_text())
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.links=[];self.ids=[];self.canonical=None;self.description=None;self.h1=0;self.nav=0;self.main=False;self.main_links=[];self.robots='';self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='main':self.main=True
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='nav' and 'provider-guide-nav' in a.get('class',''):self.nav+=1
  if tag=='a':
   self.links.append(a.get('href',''))
   if self.main:self.main_links.append(a.get('href',''))
  if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href')
  if tag=='meta' and a.get('name')=='description':self.description=a.get('content')
  if tag=='meta' and a.get('name')=='robots':self.robots=a.get('content','')
 def handle_endtag(self,tag):
  if tag=='main':self.main=False

def read(route):
 f=ROOT/route.strip('/')/'index.html'
 assert f.is_file(),route
 text=f.read_text();return text,Page(text)
errors=[];routes=set();descriptions=set();directory_route='/compare/'
directory,hub=read(directory_route)
for row in DATA['providers']:
 slug=row['slug'];fragment='costseg-'+slug
 assert fragment in hub.ids,('directory fragment',slug)
 for key in ['alternative_url','pricing_url','comparison_url']:
  if not row[key]:continue
  route=urlparse(row[key]).path;routes.add(route);text,p=read(route)
  assert p.h1==1 and p.canonical==row[key] and 'noindex' not in p.robots,(route,'identity')
  assert p.nav==1,(route,'navigation')
  assert '/assets/competitor-pricing.css' in text,(route,'nav stylesheet')
  assert '/compare/#'+fragment in p.main_links,(route,'directory handoff')
  assert '/cost-seg-discovery/' in p.main_links,(route,'study call destination')
  assert len(p.ids)==len(set(p.ids)),(route,'duplicate IDs')
  assert row['official_source'] in p.links,(route,'own website source')
  for peer_key in ['alternative_url','pricing_url','comparison_url']:
   if row[peer_key]:assert urlparse(row[peer_key]).path in p.main_links or row[peer_key] in p.main_links,(route,'triplet link')
  for raw in re.findall(r'<script\b[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',text,re.S):json.loads(raw)
  if key=='alternative_url':
   assert 'class="costseg-decision"' in text and row['original_intro'] in text,(route,'researched introduction preserved')
   assert 60<=len(p.description)<=200,(route,'description length')
   assert p.description not in descriptions,(route,'duplicate snippet')
   descriptions.add(p.description)
   assert row['question'].replace('&','&amp;') in text,(route,'specific decision question')
  for href in p.main_links:
   u=urlparse(href)
   if u.netloc not in ('','www.aetaxadvisors.com','aetaxadvisors.com') or not u.path.startswith('/'):continue
   target=ROOT/u.path.strip('/')/'index.html'
   # Existing flat routes are allowed by Vercel cleanUrls.
   if not target.is_file() and not (ROOT/(u.path.strip('/')+'.html')).is_file():errors.append((route,href))
for route in ['/compare/','/compare/best-cost-segregation-companies/']:
 text,p=read(route)
 assert len(p.ids)==len(set(p.ids)),(route,'duplicate IDs')
 assert text.count('id="cost-segregation-providers"')==1,(route,'directory count')
 schema=json.loads(re.search(r'<script type="application/ld\+json" id="costseg-directory-schema">(.*?)</script>',text,re.S)[1])
 assert schema['numberOfItems']==len(schema['itemListElement'])==46
 for row in DATA['providers']:
  for key in ['alternative_url','pricing_url','comparison_url']:
   if row[key]:assert urlparse(row[key]).path in p.main_links,(route,row['slug'],key)
assert not errors,errors
print(json.dumps({'providers':len(DATA['providers']),'existing_provider_pages':len(routes),'directory_hubs':2,'unique_alternatives_snippets':len(descriptions),'errors':errors},indent=2))
