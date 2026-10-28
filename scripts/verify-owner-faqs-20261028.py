"""Verify the complete release surface, not only generator output."""
from pathlib import Path
import re,json,sys,html,xml.etree.ElementTree as ET
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1];out=ROOT/(sys.argv[1] if len(sys.argv)>1 else '.')
m=json.loads((ROOT/'content/owner-faqs-20261028/manifest.json').read_text());assert len(m['pages'])==100
alltitles=set();allh1=set();errors=[];wordcounts=[]
xml=(out/'sitemap-owner-faqs-20261028.xml').read_text();ET.fromstring(xml)
blog=(out/'blog/index.html').read_text()
for r in m['pages']:
 path=r['path'];p=out/path.strip('/')/'index.html';s=p.read_text();main=re.search(r'<main[^>]*>(.*?)</main>',s,re.S)[1]
 def check(ok,msg):
  if not ok:errors.append(path+': '+msg)
 check(len(re.findall(r'<h1\b',s))==1,'one H1')
 check(len(re.findall(r'<title>',s))==1,'one title')
 title=html.unescape(re.search(r'<title>(.*?)</title>',s,re.S)[1]);h1=html.unescape(re.search(r'<h1[^>]*>(.*?)</h1>',s,re.S)[1])
 check(title not in alltitles,'unique title');alltitles.add(title);check(h1 not in allh1,'unique question');allh1.add(h1)
 check(len(title)<=60,'title length')
 check('href="https://www.aetaxadvisors.com'+path+'"' in s,'canonical URL')
 check(len(re.findall(r'<link rel="canonical"',s))==1,'one canonical')
 check('noindex' not in re.sub(r'<script.*?</script>','',s,flags=re.S).lower(),'indexable')
 desc=html.unescape(re.search(r'<meta name="description" content="([^"]*)',s)[1]);check(40<=len(desc)<=160,'description length')
 check('https://www.aetaxadvisors.com'+path in xml,'XML sitemap membership');check('href="'+path+'"' in blog,'blog discovery')
 ld=[]
 for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
  obj=json.loads(block);ld.extend(obj if isinstance(obj,list) else [obj])
 articles=[x for x in ld if x.get('@type')=='Article'];check(len(articles)==1,'one Article schema')
 if articles:check(articles[0]['url']=='https://www.aetaxadvisors.com'+path,'schema URL');check(articles[0]['headline']==r['title'],'schema headline')
 check('Illustrative scenario, not a client result.' in main,'illustration labeling')
 check('Which fact changes the answer?' in main,'decision fork present')
 for href in re.findall(r'href="([^"]+)"',main):
  if href.startswith('/') and not href.startswith('//'):
   target=out/href.strip('/')/'index.html'
   check(target.exists(),'internal link target missing: '+href)
 words=len(html.unescape(re.sub('<[^>]+>',' ',main)).split());wordcounts.append(words);check(words>=280,'substantive page body')
for f in ['sitemap.xml','sitemap_index.xml','sitemap-index.xml']:
 ET.fromstring((out/f).read_text())
for path in ['/ptet-election-by-state/','/amended-tax-returns/','/c-corporation-strategy/c-corp-vs-s-corp/','/business-owner-exit-strategy/']:
 s=(out/path.strip('/')/'index.html').read_text()
 for b in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):json.loads(b)
 assert len(re.findall('<h1\\b',s))==1,path
assert '$40,400' in (out/'ptet-election-by-state/index.html').read_text()
assert 'through the end of 2025' in (out/'amended-tax-returns/index.html').read_text()
assert '$15 million' in (out/'c-corporation-strategy/c-corp-vs-s-corp/index.html').read_text()
print('New FAQs:',len(m['pages']),'Existing content pages:',4,'Words min/avg/max:',min(wordcounts),round(sum(wordcounts)/100),max(wordcounts))
print('Errors:',len(errors))
for e in errors:print(e)
raise SystemExit(bool(errors))
