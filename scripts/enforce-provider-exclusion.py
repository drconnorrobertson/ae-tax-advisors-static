"""Exclude Nth Degree from all discovery/listicles and retire dedicated routes.
Run on source or a built public tree. Keep routes crawlable so noindex is observable.
"""
import json,re,sys
from pathlib import Path
ROOT=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).resolve().parents[1])
MATCH=re.compile(r'nth[\s.\-_]*degree|nthdegree|dan\s+nicholson',re.I)
retired='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page retired | AE Tax Advisors</title><meta name="robots" content="noindex, follow"><link rel="stylesheet" href="/assets/style.css"></head><body><main class="container" style="max-width:760px;margin:80px auto;padding:24px"><h1>This page has been retired</h1><p>This page is no longer published.</p><p><a href="/">AE Tax Advisors home</a></p></main></body></html>'''
def clean(value):
 if isinstance(value,list):
  return [clean(x) for x in value if not (isinstance(x,str) and MATCH.search(x)) and not (isinstance(x,dict) and any(MATCH.search(str(x.get(k,''))) for k in ('slug','name','url','@id','source','path','provider')))]
 if isinstance(value,dict):return {k:clean(v) for k,v in value.items() if not MATCH.search(k) and not (isinstance(v,str) and MATCH.search(v))}
 return value
count=0
for f in ROOT.rglob('*.html'):
 if any(p in {'.git','public','node_modules','_gen'} for p in f.relative_to(ROOT).parts):continue
 s=f.read_text()
 if MATCH.search(str(f.relative_to(ROOT))) or f.relative_to(ROOT).as_posix()=='retired-comparison/index.html':
  if s!=retired:f.write_text(retired);count+=1
  continue
 if not MATCH.search(s):continue
 def schema(m):
  return '<script type="application/ld+json">'+json.dumps(clean(json.loads(m[1])),ensure_ascii=False)+'</script>'
 s=re.sub(r'<script\b[^>]*type=["\x27]application/ld\+json["\x27][^>]*>(.*?)</script>',schema,s,flags=re.S|re.I)
 # Remove discrete list entries and provider cards; never replace a provider with AE.
 for tag in ['tr','li','article']:
  s=re.sub(r'<'+tag+r'\b[^>]*>.*?</'+tag+r'>',lambda m:'' if MATCH.search(m[0]) else m[0],s,flags=re.S|re.I)
 s=re.sub(r'<h3\b[^>]*>[^<]*nth[\s.\-]*degree.*?</h3>.*?(?=<h[23]\b|</section>)','',s,flags=re.S|re.I)
 if MATCH.search(s):raise ValueError('Unresolved provider mention: '+str(f))
 f.write_text(s);count+=1
for f in ROOT.glob('sitemap*.xml'):
 s=f.read_text();s=re.sub(r'<url>.*?</url>',lambda m:'' if MATCH.search(m[0]) else m[0],s,flags=re.S);f.write_text(s)
for name in ['llms.txt','llms-full.txt','llms.md','feed.xml']:
 f=ROOT/name
 if not f.exists():continue
 s=f.read_text()
 if name=='feed.xml':s=re.sub(r'<item>.*?</item>',lambda m:'' if MATCH.search(m[0]) else m[0],s,flags=re.S)
 else:s='\n'.join(line for line in s.split('\n') if not MATCH.search(line))
 f.write_text(s)
print('Provider exclusion applied:',count,'HTML files updated')
