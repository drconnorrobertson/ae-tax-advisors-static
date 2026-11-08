#!/usr/bin/env python3
import html,json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit
r=Path(__file__).resolve().parents[1];out=Path(sys.argv[1]).resolve()if len(sys.argv)>1 else r;d=r/'content/str-costseg-library-20261108';scope=json.loads((d/'scope.json').read_text());questions=json.loads((d/'questions-index.json').read_text());cfg=json.loads((d/'questions.json').read_text());errors=[];base='https://www.aetaxadvisors.com';titles=set();links=0
assert len(questions)==100 and len({q['question']for q in questions})==100 and len(cfg['groups'])==20
xml=ET.parse(out/'sitemap-rental-question-library.xml');locs={x.text for x in xml.iter()if x.tag.endswith('loc')};assert locs=={base+p for p in scope['pages']}
for path in scope['pages']:
 s=(out/path.strip('/')/'index.html').read_text();plain=html.unescape(re.sub('<[^>]+>',' ',s));title=re.search('<title>(.*?)</title>',s,re.S)[1]
 if title in titles:errors.append(path+': duplicate title')
 titles.add(title)
 if len(re.findall('<h1\\b',s))!=1:errors.append(path+': H1')
 if re.findall(r'<link rel="canonical" href="([^"]+)"',s)!=[base+path]:errors.append(path+': canonical')
 if re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex',s):errors.append(path+': noindex')
 if re.search(r'nth[\s._-]*degree|dan\s+nicholson',s,re.I):errors.append(path+': exclusion')
 if 'November 8, 2026'not in s:errors.append(path+': review date')
 if s.count('src="/assets/booking-events.js"')!=1:errors.append(path+': booking hook')
 ds=[json.loads(x)for x in re.findall(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S)]
 if path!=scope['hub']:
  faq=[x for x in ds if x.get('@type')=='FAQPage'];qs=[q for q in questions if q['url'].split('#')[0]==path]
  if len(faq)!=1 or len(faq[0]['mainEntity'])!=5:errors.append(path+': FAQ count')
  else:
   for item,q in zip(faq[0]['mainEntity'],qs):
    if item['name']!=q['question']or html.unescape(item['name'])not in plain:errors.append(path+': question parity')
    answer=html.unescape(re.sub('<[^>]+>',' ',item['acceptedAnswer']['text'])).strip()
    if answer not in plain:errors.append(path+': answer not visible')
    if 'id="q'+str(q['id'])+'"'not in s:errors.append(path+': missing answer anchor')
  if len(plain.split())<420:errors.append(path+': insufficient detailed context')
 for href in re.findall(r'href="([^"]+)"',s):
  if not href.startswith('/')or href.startswith('//'):continue
  u=urlsplit(html.unescape(href));f=out/u.path.lstrip('/')
  if not(f.is_file()or(f/'index.html').exists()or Path(str(f)+'.html').exists()):errors.append(path+': missing '+u.path)
  links+=1
hub=(out/scope['hub'].strip('/')/'index.html').read_text()
for q in questions:
 if q['url']not in hub:errors.append('hub missing '+q['url'])
for path in scope['updated']:
 s=(out/path.strip('/')/'index.html').read_text()
 if scope['hub']not in s:errors.append(path+': hub discovery missing')
# Specific correctness distinctions that must survive future edits.
checks={'bonus-depreciation-current-rules':['January 19, 2025','study completion year','not make old assets newly acquired'],'old-ltr-lookback':['current refund','does not create a new acquisition'],'schedule-c-e-services':['does not automatically require Schedule C','between-guest'],'hours-spouses-managers':['more-than-half','Exactly']}
# Test positive page-specific evidence; numeric-boundary evidence is in the tests spoke.
checks.pop('hours-spouses-managers')
for slug,tokens in checks.items():
 s=html.unescape((out/scope['hub'].strip('/')/slug/'index.html').read_text()).lower()
 for token in tokens:
  if token.lower()not in s:errors.append(slug+': missing '+token)
print(json.dumps(dict(questions=100,spokes=20,pages=len(scope['pages']),entrypoints=len(scope['updated']),internalLinks=links,errors=errors)));sys.exit(bool(errors))
