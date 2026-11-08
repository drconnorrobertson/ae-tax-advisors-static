#!/usr/bin/env python3
"""Reconcile observed Search Console URLs against staged output; never change indexability."""
from pathlib import Path
from urllib.parse import urlparse
from collections import Counter
import json,re,csv,sys
root=Path(__file__).resolve().parents[1];out=root/'public';data=Path(sys.argv[1]) if len(sys.argv)>1 else root/'research/gsc-20261108'
cfg=json.loads((root/'vercel.json').read_text());red={r['source']:r['destination'] for r in cfg['redirects'] if not re.search('[:*()]',r['source'])}
rows=[]
for cat in ['discovered','crawled','404','noindex','alternate','duplicate','redirect']:
 d=json.loads((data/(cat+'.json')).read_text());urls=[r['URL'] for r in d['rows']] if isinstance(d,dict) else d
 for url in urls:
  u=urlparse(url);route=u.path;f=out/route.lstrip('/');f=f if f.is_file() else f/'index.html';t=f.read_text(errors='replace') if f.exists() and f.suffix=='.html' else ''
  can=(re.search(r'<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"',t) or [None,None])[1];no=bool(re.search(r'<meta\b[^>]*name="robots"[^>]*content="[^"]*noindex',t))
  dest=red.get(route) or (route+'/' if not route.endswith('/') and (out/(route.lstrip('/')+'/index.html')).exists() else None)
  kind='configured-redirect' if dest else 'non-html-resource' if f.is_file() and f.suffix!='.html' else 'intentional-noindex' if no else 'canonical-variant' if can and can!=url else 'eligible-html' if t else 'historical-missing'
  rows.append(dict(category=cat,url=url,currentDisposition=kind,canonical=can,redirect=dest))
summary={cat:dict(Counter(r['currentDisposition'] for r in rows if r['category']==cat)) for cat in sorted(set(r['category'] for r in rows))}
(data/'triage.json').write_text(json.dumps({'observed':'2026-11-08','reportLastUpdated':'2026-10-22','summary':summary,'rows':rows},indent=2)+'\n')
with (data/'triage.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(json.dumps(summary,indent=2))
