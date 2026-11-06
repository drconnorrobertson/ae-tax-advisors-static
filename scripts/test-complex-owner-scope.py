"""Focused source checks for the reviewed owner-scope cohort; no network or build."""
from pathlib import Path
import re,json,html,subprocess
R=Path(__file__).resolve().parents[1]
cohort=json.loads((R/'content/complex-owner-scope-20261106.json').read_text())
def txt(s):return html.unescape(re.sub('<[^>]+>','',s))
def walk(d):
 if isinstance(d,dict):
  yield d
  for v in d.values():yield from walk(v)
 elif isinstance(d,list):
  for v in d:yield from walk(v)
for item in cohort['pages']:
 path=item['path'].strip('/')+'/index.html';s=(R/path).read_text();old=subprocess.check_output(['git','show','f2d5962:'+path],cwd=R,text=True)
 assert len(re.findall('<h1[ >]',s))==1
 assert re.findall(r'<link[^>]*rel="canonical"[^>]*>',s)==re.findall(r'<link[^>]*rel="canonical"[^>]*>',old)
 assert not re.search(r'<meta[^>]*name="robots"[^>]*noindex',s)
 nodes=[d for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S) for d in walk(json.loads(block))]
 oldnodes=[d for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>',old,re.S) for d in walk(json.loads(block))]
 assert [d['datePublished'] for d in nodes if 'datePublished'in d]==[d['datePublished'] for d in oldnodes if 'datePublished'in d]
 assert all(d['dateModified'].startswith('2026-11-06') for d in nodes if 'dateModified'in d)
 for d in nodes:
  if d.get('@type')=='FAQPage':
   for q in d['mainEntity']:assert q['name'] in txt(s) and q['acceptedAnswer']['text'] in txt(s)
 for u in re.findall(r'href="(/[^"#?]*)',s):
  f=R/u.lstrip('/');assert f.exists() or Path(str(f).rstrip('/')+'.html').exists(),u
 # Preserve all preexisting case destinations and numerical service-price tokens.
 assert set(re.findall(r'href="(/case-studies/[^"]+)"',old))<=set(re.findall(r'href="(/case-studies/[^"]+)"',s))
 for price in ['$7,800','$9,800','$500,000']:
  if price in old:assert price in s
 assert not any(x in s.lower() for x in ['impressions','gsc_ae_raw','pos8.9'])
 print('PASS',path)
m=(R/'multi-state-real-estate-tax-planning/index.html').read_text()
assert m.count('>Coordinate the portfolio before the next filing season<')==1
cfg=json.loads((R/'scripts/search-intent-config.json').read_text());oldcfg=json.loads(subprocess.check_output(['git','show','f2d5962:scripts/search-intent-config.json'],cwd=R,text=True))
assert set(cfg)==set(oldcfg)
changed=[k for k in cfg if cfg[k]!=oldcfg[k]]
assert 'multi-state-real-estate-tax-planning/index.html' in changed
# Other integrated cohorts remove the same redundant H3; validate the exact
# transformation rather than requiring this batch to be deployed alone.
for key in changed:
 expected=dict(oldcfg[key])
 if key=='real-estate-tax-strategy-business-owners/index.html':
  assert 'h1' not in expected
  expected['h1']='Tax Planning for Business Owners With Rental Properties'
  assert cfg[key]==expected, 'Combined-owner config changed beyond its reviewed H1'
  continue
 duplicate='<h3>'+expected['heading']+'</h3>'
 assert expected['body'].count(duplicate)==1
 expected['body']=expected['body'].replace(duplicate,'')
 assert cfg[key]==expected,key+' changed beyond heading deduplication'
print('PASS config narrow keys, heading deduplication, exact combined-owner H1 and cohort preservation')
