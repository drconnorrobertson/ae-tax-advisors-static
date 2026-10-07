"""Checks the reviewed batch and produces a production-verifiable manifest."""
import json, re, subprocess, sys
from pathlib import Path
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET
sys.path.insert(0,'/Users/connorrobertson/Documents/Codex/2026-10-06/go-l/work/python-deps')
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent
SITE='https://www.aetaxadvisors.com'
ledger=json.loads((ROOT/'_gen/ae-buyer-content-scores.json').read_text())
selected={x['url'] for x in json.loads((ROOT/'_gen/ae-buyer-value-batch.json').read_text())} if '--value-batch' in sys.argv else None
if selected: ledger['articles']=[a for a in ledger['articles'] if a['url'] in selected]
manifest=[]
maps=[{x.text for x in ET.parse(ROOT/n).findall('.//{*}loc')} for n in ['sitemap.xml','sitemap-blog.xml']]
redirects={r['source'] for r in json.loads((ROOT/'vercel.json').read_text())['redirects']}
titles=set()
for a in ledger['articles']:
 path=urlsplit(a['url']).path; f=ROOT/path.strip('/')/'index.html';s=BeautifulSoup(f.read_text(),'html.parser'); main=s.find('main');assert main
 assert len(s.find_all('h1'))==1 and len(s.find_all('title'))==1
 assert s.title.text not in titles;titles.add(s.title.text)
 assert s.find('link',rel='canonical')['href']==a['url']
 assert 'noindex' not in s.find('meta',attrs={'name':'robots'})['content']
 assert path not in redirects and all(a['url'] in m for m in maps)
 for link in s.find_all('a',href=True):
  href=link['href'];parts=urlsplit(href)
  if parts.netloc==urlsplit(SITE).netloc or (not parts.netloc and href.startswith('/')):
   pth=parts.path;target=ROOT/pth.strip('/')
   assert pth not in redirects,(path,pth)
   assert target.is_file() or (target/'index.html').is_file(),(path,pth)
 scripts=[json.loads(x.text) for x in s.find_all('script',attrs={'type':'application/ld+json'})]
 article=next(x for x in scripts if x.get('@type')=='Article');assert article['dateModified']=='2026-10-07'
 assert article['author']['@id']==SITE+'/#organization'
 faq=next(x for x in scripts if x.get('@type')=='FAQPage');text=main.get_text(' ',strip=True)
 for q in faq['mainEntity']:
  assert q['name'] in text and q['acceptedAnswer']['text'] in text
 assert a['total']>=85 and a['scores']['buyerRelevance']>=27 and a['scores']['serviceFit']>=17
 assert len(text.split())>=750
 assert not re.search(r'\$20,000.\$150,000|average first.year savings|savings.*consistently exceed',text,re.I)
 manifest.append({'url':a['url'],'title':s.title.text,'h1':s.h1.text,'mainText':text,'published':article['datePublished'],'modified':article['dateModified'],'editorialScore':a['total'],'words':len(text.split())})
# Changes must be confined to the reviewed batch and its discovery metadata.
changed=subprocess.check_output(['git','diff','--name-only'],cwd=ROOT,text=True).splitlines()
allowed={'blog/index.html','sitemap.xml','sitemap-blog.xml'}|{urlsplit(x['url']).path.strip('/')+'/index.html' for x in ledger['articles']}
assert set(changed)-{'_gen/ae-buyer-content-scores.json','validate_buyer_quality.py'}==allowed,changed
for name in ['index.html','vercel.json','assets/style.css','assets/site-ux.js']:
 old=subprocess.check_output(['git','show','HEAD:'+name],cwd=ROOT)
 assert (ROOT/name).read_bytes()==old,name
(ROOT/('_gen/ae-buyer-value-manifest.json' if selected else '_gen/ae-buyer-batch-manifest.json')).write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'articles':len(manifest),'words':[x['words'] for x in manifest],'scores':[x['editorialScore'] for x in manifest],'allChecksPassed':True}))
