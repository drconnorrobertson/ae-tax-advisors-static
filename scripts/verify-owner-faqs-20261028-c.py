"""Check routes, content, discovery, prior-batch preservation and publication metadata."""
from pathlib import Path
import json,re,html,sys,subprocess,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];out=ROOT/(sys.argv[1]if len(sys.argv)>1 else '.');SITE='https://www.aetaxadvisors.com';DATA=ROOT/'content/owner-faqs-20261028-c'
m=json.loads((DATA/'manifest.json').read_text());assert len(m['pages'])==100
previous=json.loads((ROOT/'content/owner-faqs-20261028/manifest.json').read_text())['pages'];previous+=json.loads((ROOT/'content/owner-faqs-20261028-b/manifest.json').read_text())['pages'];oldpaths={r['path']for r in previous}
assert not oldpaths&{r['path']for r in m['pages']}
urls=ET.fromstring((out/'sitemap-owner-faqs-20261028-c.xml').read_text());locs=[e.text for e in urls.iter()if e.tag.endswith('loc')];assert len(locs)==len(set(locs))==100
blog=(out/'blog/index.html').read_text();sitemap=(out/'sitemap/index.html').read_text();errors=[];titles=set();questions=set();counts=[]
for r in m['pages']:
 s=(out/r['path'].strip('/')/'index.html').read_text();main=re.search(r'<main[^>]*>(.*?)</main>',s,re.S)[1]
 def check(ok,msg):
  if not ok:errors.append(r['path']+': '+msg)
 h1s=re.findall(r'<h1[^>]*>(.*?)</h1>',s,re.S);ts=re.findall(r'<title>(.*?)</title>',s,re.S)
 check(len(h1s)==len(ts)==1,'single H1 and title')
 if h1s:check(html.unescape(h1s[0])==r['title'],'question matches')
 if ts:check(html.unescape(ts[0])==r['seo_title'],'SEO title matches');check(len(html.unescape(ts[0]))<=60,'title length')
 check(r['title']not in questions,'unique question');questions.add(r['title']);check(r['seo_title']not in titles,'unique title');titles.add(r['seo_title'])
 canonical=re.findall(r'<link[^>]*rel="canonical"[^>]*href="([^"]+)"',s);check(canonical==[SITE+r['path']],'self canonical')
 check(not re.search(r'<meta[^>]*name="robots"[^>]*content="[^"]*noindex',s,re.I),'indexable')
 desc=re.search(r'<meta name="description" content="([^"]+)"',s)[1];check(len(html.unescape(desc))<=160,'description length')
 check(SITE+r['path']in locs,'dedicated sitemap membership')
 check('href="'+r['path']+'"'in blog,'blog discovery');check('href="'+r['path']+'"'in sitemap,'HTML sitemap discovery')
 check('Illustrative example, not a client result.'in main,'hypothetical labels');check(html.escape(r['fork'],quote=True)in main,'bespoke decision fork')
 blocks=[]
 for b in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
  v=json.loads(b);blocks.extend(v if isinstance(v,list)else[v])
 art=[x for x in blocks if x.get('@type')=='Article'];check(len(art)==1,'single Article schema')
 if art:check(art[0]['url']==SITE+r['path']and art[0]['headline']==r['title'],'schema identity');check(art[0]['citation']==r['sources'],'schema sources')
 for href in re.findall(r'href="([^"]+)"',main):
  if href.startswith('/')and not href.startswith('//'):check((out/href.strip('/')/'index.html').exists(),'broken internal link '+href)
 words=len(html.unescape(re.sub('<[^>]+>',' ',main)).split());counts.append(words);check(words>=280,'substantive body')
for r in previous:
 s=(out/r['path'].strip('/')/'index.html').read_text();assert r['title']in html.unescape(s),r['path']
 if out==ROOT:
  f=r['path'].strip('/')+'/index.html';old=subprocess.check_output(['git','show','HEAD:'+f],cwd=ROOT,text=True);assert s==old,'Prior FAQ changed: '+f
for f in ['sitemap.xml','sitemap-index.xml','sitemap_index.xml']:
 ET.fromstring((out/f).read_text())
print('New FAQs:',100,'Previous FAQs preserved:',len(previous),'Main text words min/avg/max:',min(counts),round(sum(counts)/100),max(counts))
print('Errors:',len(errors))
for e in errors:print(e)
raise SystemExit(bool(errors))
