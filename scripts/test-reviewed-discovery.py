#!/usr/bin/env python3
"""Focused fixtures plus optional pre-edit snapshot regression.
Usage: python scripts/test-reviewed-discovery.py [snapshot.json]
Snapshot maps only the eight targeted file paths to their original UTF-8 text.
"""
from pathlib import Path
import importlib.util,json,re,sys
p=Path(__file__).with_name('sync-reviewed-discovery.py')
spec=importlib.util.spec_from_file_location('sync',p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def urls(s):return re.findall(r'https://www\.aetaxadvisors\.com/[^\s)"<>]+',s)
def hrefs(s):return re.findall(r'href=["\']([^"\']+)',s)
fixture='- [Old](https://www.aetaxadvisors.com/form-3115-cost-segregation-lookback/): stale\n- [Untouched](https://www.aetaxadvisors.com/unreviewed/): unchanged\n'
out=mod.sync_markdown(fixture)
assert '): stale' not in out and out.endswith('- [Untouched](https://www.aetaxadvisors.com/unreviewed/): unchanged\n')
assert urls(out)==urls(fixture) and mod.sync_markdown(out)==out
assert mod.sync_markdown('no routes here')=='no routes here'
fixture='<a href="/form-3115-cost-segregation-lookback/">Old</a><a href="/held-not-in-list/">Keep</a>'
out=mod.sync_labels(fixture)
assert hrefs(out)==hrefs(fixture) and '>Keep</a>' in out and mod.sync_labels(out)==out
files=['form-3115-cost-segregation-lookback/index.html','compare/tax-advisory-firm-comparison.json','llms-full.txt','llms.txt','llms.md','.well-known/llms.txt','sitemap/index.html','resources/index.html']
before={f:(mod.ROOT/f).read_text() for f in files};mod.apply()
assert before=={f:(mod.ROOT/f).read_text() for f in files},'helper must be idempotent and preserve reviewed article'
if len(sys.argv)>1:
 old=json.loads(Path(sys.argv[1]).read_text())
 for f in ['llms-full.txt','llms.txt','llms.md','.well-known/llms.txt']:
  assert urls(old[f])==urls(before[f]),f+' membership/order'
  assert before[f]==mod.sync_markdown(old[f]),f+' unrelated content changed'
 for f in ['sitemap/index.html','resources/index.html']:
  assert hrefs(old[f])==hrefs(before[f]),f+' membership/order'
 assert before['sitemap/index.html']==mod.sync_labels(old['sitemap/index.html'])
 a=json.loads(old[files[1]]);b=json.loads(before[files[1]])
 for d in [a,b]:
  firm=next(x for x in d['firms'] if x['name']=='Prime Path Advisory')
  del firm['serviceModel'];del firm['clientFocus']
 assert a==b,'only two Prime Path fields may change, including dates/prices/budgets'
 f=files[0]
 assert re.findall(r'"datePublished":\s*"[^"]+"',old[f])==re.findall(r'"datePublished":\s*"[^"]+"',before[f])
 assert re.findall(r'<link rel="canonical"[^>]*>',old[f])==re.findall(r'<link rel="canonical"[^>]*>',before[f])
 for f in files:
  print(f,'changed',old[f]!=before[f])
s=before[files[0]]
assert len(re.findall('<h1[ >]',s))==1
docs=[json.loads(x) for x in re.findall(r'<script type="application/ld\+json">\s*(.*?)</script>',s,re.S)]
faq=next(d for d in docs if d.get('@type')=='FAQPage')
assert len(faq['mainEntity'])==5
for q in faq['mainEntity']:assert q['name'] in s and q['acceptedAnswer']['text'] in s
for phrase in ['no statute of limitations cap','recover the entire catch-up in one year','late partial disposition election is itself an automatic']:assert phrase not in s
assert 'article:modified_time" content="2026-11-06' in s
assert all(x.startswith('2026-11-06') for x in re.findall(r'"dateModified":\s*"([^"]+)"',s))
print('PASS fixtures, idempotence, membership/hold non-addition, publication, price and FAQ checks')
s=before['resources/index.html']
docs=[json.loads(x) for x in re.findall(r'<script type="application/ld\+json">\s*(.*?)</script>',s,re.S)]
faq=next(d for d in docs if d.get('@type')=='FAQPage')
assert len(faq['mainEntity'])==4
for q in faq['mainEntity']:assert q['name'] in s and q['acceptedAnswer']['text'] in s
for old,new in json.loads((mod.ROOT/'content/discovery-reviewed-resources-copy-20261106.json').read_text()).items():
 assert old not in s and s.count(new)==2
for f in ['llms-full.txt','llms.txt','llms.md','.well-known/llms.txt']:
 for line in before[f].splitlines():
  if any(route in line for route in ['/blog/form-3115-missed-depreciation/','/blog/lookback-cost-segregation-existing-property/','/blog/what-is-form-3115-and-how-does-it-relate-to-cost-segregation/']):
   assert 'No amended returns needed' not in line and 'entire catch-up' not in line and 'in one year' not in line
print('PASS resources FAQ parity and related catch-up discovery summaries')

# Metadata-only cohorts update descriptions without changing existing link labels.
key='/metadata-only-fixture/'
mod.COPY[key]={'title':'Unused replacement label','description':'A complete reviewed description.','description_only':True}
assert mod.sync_markdown('- [Keep exact label](https://www.aetaxadvisors.com/metadata-only-fixture/): Old snippet\n')=='- [Keep exact label](https://www.aetaxadvisors.com/metadata-only-fixture/): A complete reviewed description.\n'
assert mod.sync_labels('<a href="/metadata-only-fixture/">Keep exact label</a>')=='<a href="/metadata-only-fixture/">Keep exact label</a>'
del mod.COPY[key]
print('PASS metadata-only description updates preserve discovery labels.')
