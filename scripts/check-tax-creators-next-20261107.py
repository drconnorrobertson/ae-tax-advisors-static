#!/usr/bin/env python3
"""Validate name intent, review disclosure, graph links, structured data and preservation."""
import html,json,re,sys,xml.etree.ElementTree as ET,subprocess
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin,urlsplit
repo=Path(__file__).resolve().parents[1];root=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else repo;data=repo/'content/tax-creators-next-20261107';people=json.loads((data/'people.json').read_text())['people'];paths=json.loads((data/'pages.json').read_text());base='https://www.aetaxadvisors.com';errors=[];links=0;titles=set();urls={x.text for f in root.glob('sitemap*.xml')for x in ET.parse(f).findall('.//{*}loc')};redirects={x['source']:x['destination']for x in json.loads((repo/'vercel.json').read_text())['redirects']if not re.search(r'[:*()]',x['source'])}
class P(HTMLParser):
 def __init__(self,s):super().__init__();self.tags=[];self.feed(s)
 def handle_starttag(self,t,a):self.tags.append((t,dict(a)))
def plain(s):return ' '.join(html.unescape(re.sub('<[^>]*>',' ',s)).split())
for path in paths:
 s=(root/path.strip('/')/'index.html').read_text();p=P(s);v=plain(s)
 if len([t for t,a in p.tags if t=='h1'])!=1:errors.append(path+': H1')
 if [a.get('href')for t,a in p.tags if t=='link'and a.get('rel')=='canonical']!=[base+path]:errors.append(path+': canonical')
 if base+path not in urls:errors.append(path+': sitemap')
 if any('noindex'in a.get('content','').lower()for t,a in p.tags if t=='meta'and a.get('name')=='robots'):errors.append(path+': noindex')
 if s.count('src="/assets/booking-events.js"')!=1:errors.append(path+': booking hook')
 title=re.search('<title>(.*?)</title>',s,re.S)[1]
 if title in titles:errors.append(path+': duplicate title')
 titles.add(title)
 if re.search(r'nth[\s._-]*degree|dan\s+nicholson',s,re.I):errors.append(path+': exclusion')
 if 'competing'in v.lower()or 'competes'in v.lower():pass
 else:errors.append(path+': commercial disclosure')
 for t,a in p.tags:
  if t!='a':continue
  u=urlsplit(urljoin(base+path,a.get('href','')))
  if u.hostname not in ['www.aetaxadvisors.com','aetaxadvisors.com']:continue
  target=u.path;seen=set()
  while target in redirects:
   if target in seen:errors.append(path+': redirect loop');break
   seen.add(target);target=redirects[target]
  f=root/target.lstrip('/')
  if not(f.is_file()or(f/'index.html').is_file()or Path(str(f)+'.html').is_file()):errors.append(path+': missing '+target)
  links+=1
 ds=[json.loads(x)for x in re.findall(r'<script[^>]+type=[\'"]application/ld\+json[\'"][^>]*>(.*?)</script>',s,re.S)]
 if any(x.get('@type')in ['Review','AggregateRating']for x in ds):errors.append(path+': unsupported rating schema')
 faq=[x for x in ds if x.get('@type')=='FAQPage']
 if faq:
  schema=[(plain(x['name']),plain(x['acceptedAnswer']['text']))for x in faq[0]['mainEntity']];visible=[(plain(q),plain(a))for q,a in re.findall(r'<div class="faq-item">\s*<h3>(.*?)</h3>\s*(.*?)\s*</div>',s,re.S)]
  if path in ['/compare/jasmine-dilucci-alternatives/','/compare/jasmine-dilucci-vs-ae-tax/']:
   if not all(pair in visible for pair in schema):errors.append(path+': schema answer not visible')
  elif schema!=visible:errors.append(path+': FAQ parity')
 if path.endswith('-reviews/'):
  for token in ['not a firsthand','competing','original platform','Sources']:
   if token.lower()not in v.lower():errors.append(path+': review '+token)
for x in people:
 for k in ['alternative','comparison','review']:
  s=(root/x[k].strip('/')/'index.html').read_text()
  if x['name']not in html.unescape(s):errors.append(x[k]+': name')
  if not all(u in s for u,label in x['sources']):errors.append(x[k]+': primary source')
# Preserve prior core and creator guides outside the three expressly refreshed lists.
import hashlib
for path,digest in json.loads((data/'preservation.json').read_text()).items():
 if hashlib.sha256((repo/path.strip('/')/'index.html').read_bytes()).hexdigest()!=digest:errors.append(path+': preserved source changed')
hub=(root/'compare/tax-influencer-alternatives/index.html').read_text()
expected_creators=len({x['slug'] for source in repo.glob('content/tax-creators*/people.json') for x in json.loads(source.read_text())['people']})
if hub.count('data-firm-card')!=expected_creators:errors.append('directory: creator inventory count')
for x in people:
 if not all(x[k] in hub for k in ['alternative','comparison','review']):errors.append(x['slug']+': directory links')
for path in [by for by in paths if 'sharon-winsmith' in by]:
 text=plain((root/path.strip('/')/'index.html').read_text())
 if not all(token in text for token in ['$1,500','$2,500','$10,000','educational']):errors.append(path+': consultation fee and scope')
print(json.dumps(dict(people=len(people),pages=len(paths),internal_links_checked=links,preserved_guides=len(json.loads((data/'preservation.json').read_text())),errors=errors)));sys.exit(bool(errors))
