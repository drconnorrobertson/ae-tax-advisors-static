#!/usr/bin/env python3
"""Check the reviewed existing gym article and its precise discovery addition."""
from pathlib import Path
import html,json,re,sys
repo=Path(__file__).resolve().parents[1]
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else repo
route='/blog/tax-strategy-for-gym-fitness-studio-owners/'
f=root/(route.strip('/')+'.html')
s=f.read_text()
def plain(v):return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',v))).strip()
def walk(v):
 if isinstance(v,dict):
  yield v
  for x in v.values():yield from walk(x)
 elif isinstance(v,list):
  for x in v:yield from walk(x)
objs=[o for raw in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S) for o in walk(json.loads(raw))]
assert re.findall(r'<link[^>]*rel="canonical"[^>]*href="([^"]+)"',s)==['https://www.aetaxadvisors.com'+route]
assert len(re.findall(r'<h1\b',s))==1
articles=[o for o in objs if o.get('@type') in ['BlogPosting','Article']]
assert len(articles)==1
assert articles[0]['datePublished'].startswith('2026-09-19')
assert articles[0]['dateModified'].startswith('2026-11-06')
assert '/pricing/' in s and '/discovery/' in s
visible=plain(re.sub(r'<script\b[^>]*>.*?</script>','',s,flags=re.S))
qs=[o for o in objs if o.get('@type')=='Question'];assert len(qs)==4
for q in qs:assert plain(q['name']) in visible and plain(q['acceptedAnswer']['text']) in visible
for phrase in ['permitted advance-payment','following tax year','controlled-group','internal structural framework','behavioral control','separately scoped','secure channel']:assert phrase in visible,phrase
assert '<loc>https://www.aetaxadvisors.com'+route+'</loc>' in (root/'sitemap-blog.xml').read_text()
assert route in {x['url'] for x in json.loads((repo/'scripts/blog-catalog.json').read_text())}
print('PASS existing gym canonical, preserved publication, reviewed modification, four FAQ pairs, sourced boundaries, conversion links and narrow discovery.')
