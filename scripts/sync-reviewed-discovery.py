#!/usr/bin/env python3
"""Author-time copy sync. Changes existing labels only; never adds/removes routes.
The reviewed-copy manifest is deliberately explicit, not an inventory generator.
Run regression tests against a saved pre-edit snapshot before integrating.
"""
from pathlib import Path
import json,re,html
ROOT=Path(__file__).resolve().parents[1]
COPY=json.loads((ROOT/'content/discovery-reviewed-copy-20261106.json').read_text())
def sync_markdown(s):
 def replace(m):
  route=m['route'];d=COPY.get(route)
  if not d:return m[0]
  suffix=': '+d['description'] if m['description'] is not None else ''
  label=m['title'] if d.get('description_only') else d['title']
  return m['prefix']+'['+label+']('+m['url']+')'+suffix
 return re.sub(r'(?P<prefix>^- )\[(?P<title>[^\]\n]*)\]\((?P<url>https://www\.aetaxadvisors\.com(?P<route>/[^)\s]*))\)(?P<description>: [^\n]*)?',replace,s,flags=re.M)
def sync_labels(s):
 def replace(m):
  d=COPY.get(m[2])
  if not d or d.get('description_only'):return m[0]
  return m[1]+html.escape(d['title'])+m[4]
 return re.sub(r'(<a\b[^>]*href="(/[^"]+)"[^>]*>)([^<]*)(</a>)',replace,s)
def apply():
 for f in ['llms-full.txt','llms.txt','llms.md','.well-known/llms.txt']:
  p=ROOT/f;p.write_text(sync_markdown(p.read_text()))
 p=ROOT/'sitemap/index.html';p.write_text(sync_labels(p.read_text()))
 p=ROOT/'resources/index.html';s=p.read_text()
 s=s.replace('IRS-compliant engineering studies that accelerate depreciation into Year 1.','Engineering-based studies of supported asset classifications, with deduction timing and owner eligibility reviewed separately.')
 s=s.replace('>Amended-return self-assessment</a>','>Business tax return review readiness checklist</a>')
 for old,new in json.loads((ROOT/'content/discovery-reviewed-resources-copy-20261106.json').read_text()).items():
  s=s.replace(old,new)
 p.write_text(s)
 p=ROOT/'form-3115-cost-segregation-lookback/index.html';s=p.read_text();desc=COPY['/form-3115-cost-segregation-lookback/']['description']
 for key in ['description','og:description','twitter:description']:
  s=re.sub(r'(<meta (?:name|property)="'+key+r'" content=")[^"]*',lambda m:m[1]+html.escape(desc,quote=True),s)
 # Only the matching Article description, not FAQ or body.
 s=s.replace('"description": "A missed cost segregation study is not a lost opportunity. Form 3115 and the Section 481(a) adjustment recover the entire catch-up in one year."','"description": '+json.dumps(desc))
 p.write_text(s)
 p=ROOT/'compare/tax-advisory-firm-comparison.json';s=p.read_text();d=json.loads(s)
 firm=next(x for x in d['firms'] if x['name']=='Prime Path Advisory')
 for k,v in {
 'serviceModel':'Advertises an internal tax team and an outside attorney and financial-adviser network. Tax preparation is offered; confirm included work, the assigned professionals and preparer handoff in the engagement.',
 'clientFocus':'Advertised positioning includes people making $1M+; confirm fit for the owner, entities, investments and planning needs rather than treating that positioning as a universal eligibility rule.'
 }.items():
  old=json.dumps(firm[k],ensure_ascii=False);new=json.dumps(v,ensure_ascii=False)
  assert s.count(old)==1
  s=s.replace(old,new)
 p.write_text(s)
if __name__=='__main__':apply()
