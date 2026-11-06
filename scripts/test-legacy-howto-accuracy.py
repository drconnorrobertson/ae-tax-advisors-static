#!/usr/bin/env python3
"""Focused preservation and visible/schema checks; no build or remote operations."""
from pathlib import Path
import json,re,subprocess,html
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'content/seo-refresh-20261106/legacy-howto-accuracy.json').read_text())
def objects(v):
 if isinstance(v,dict):
  yield v
  for x in v.values():yield from objects(x)
 elif isinstance(v,list):
  for x in v:yield from objects(x)
def docs(s):return [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">\s*(.*?)</script>',s,re.S)]
def text(s):return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',s))).strip()
for rec in manifest:
 f=rec['path'];s=(ROOT/f).read_text()
 old=subprocess.check_output(['git','show','HEAD:'+f],cwd=ROOT,text=True)
 a=list(objects(docs(old)));b=list(objects(docs(s)))
 assert [x['datePublished'] for x in a if 'datePublished' in x]==[x['datePublished'] for x in b if 'datePublished' in x],f
 assert re.findall(r'<link rel="canonical"[^>]*>',old)==re.findall(r'<link rel="canonical"[^>]*>',s),f
 assert f=='cost-segregation-car-wash/index.html' or [v.rstrip('.,') for v in re.findall(r'\$[0-9][0-9,.]*(?:\+)?',old)]==[v.rstrip('.,') for v in re.findall(r'\$[0-9][0-9,.]*(?:\+)?',s)],f+' dollar amounts changed'
 assert sum(x.get('@type')=='HowTo' for x in a)==sum(x.get('@type')=='HowTo' for x in b),f+' HowTo removed'
 assert all(x['dateModified']=='2026-11-06' for x in b if 'dateModified' in x)
 assert 'article:modified_time" content="2026-11-06' in s
 visible=text(re.sub(r'<script\b[^>]*>.*?</script>','',s,flags=re.S))
 for x in b:
  if x.get('@type')=='Question':
   assert text(x['name']) in visible,(f,x['name'])
   assert text(x['acceptedAnswer']['text']) in visible,(f,x['name'],'answer parity')
  if x.get('@type')=='HowToStep':assert text(x['text']) in visible,(f,'HowTo parity')
 for claim in ['captures every missed deduction','often a late partial disposition election','Only one is easy to defend','A 1031 exchange defers it','Deducting at 35% and recapturing at 37% is a bad trade']:
  assert claim not in s,(f,claim)
 # Provider-facing and pricing FAQ answers outside technical correction scope are unchanged.
 oldq={x['name']:x['acceptedAnswer']['text'] for x in a if x.get('@type')=='Question'}
 newq={x['name']:x['acceptedAnswer']['text'] for x in b if x.get('@type')=='Question'}
 if f.startswith('compare/'):
  for q,v in oldq.items():
   if q!='Does a cheaper cost segregation study mean a worse outcome?':assert newq[q]==v,(f,q)
 assert len(re.findall('<h1[ >]',s))==1
 print('PASS',f)
print('PASS cohort; pricing, publication, canonical, HowTo retention and visible/schema parity')

for rec in manifest:
 s=(ROOT/rec['path']).read_text()
 assert 'duplicate Ogden copy' not in s
 assert 'A partial disposition election writes off the remaining basis.' not in s
 if not rec['path'].startswith('compare/') and rec['path']!='cost-segregation-car-wash/index.html':
  assert s.count('Determine correction procedure and file correctly')==2
  assert 'not a verified industry benchmark' in s
  assert s.count('not a universal threshold')==2
  assert 'Generally yes once depreciable basis' not in s
  assert 'typically reclassify' not in s
s=(ROOT/'cost-segregation-for-medical-office/index.html').read_text()
assert 'everything placed in service that year' not in s
assert 'Exclude nonresidential real property' in s
print('PASS follow-up disposition, destination, ranges, threshold and mid-quarter checks')

routes=[]
for rec in manifest:
 s=(ROOT/rec['path']).read_text()
 canonical=re.search(r'<link rel="canonical" href="([^"]+)"',s)[1]
 assert canonical=='https://www.aetaxadvisors.com'+rec['releaseRoute']
 if rec['includeInDiscovery']:routes.append(rec['releaseRoute'])
assert len(routes)==len(set(routes))==8
assert '/cost-segregation-for-car-wash/' not in routes
s=(ROOT/'cost-segregation-car-wash/index.html').read_text()
assert '$735,000 to $840,000' in s
assert 'Based on studies performed across tunnel' in s
assert 'Our engineering-based cost segregation studies routinely reclassify 30-45%' in s
print('PASS canonical release cohort: 9 files, 8 canonical routes; historical study claims retained')
