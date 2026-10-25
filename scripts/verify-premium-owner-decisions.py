"""Verify the owner decision release in source, build output, or on the live site."""
import json,re,sys,urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
M=json.loads((ROOT/'content/premium-owner-decisions-20261024/manifest.json').read_text())
SITE='https://www.aetaxadvisors.com'
class Page(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.h1=0;self.canonical=[];self.links=[];self.main=0;self.mainends=0;self.inmain=False;self.words=[];self.jsons=[];self.injson=False;self.script='';self.title=False;self.titles=[]
 def handle_starttag(self,t,attrs):
  d=dict(attrs)
  if t=='h1':self.h1+=1
  if t=='main':self.main+=1;self.inmain=True
  if t=='link' and d.get('rel')=='canonical':self.canonical.append(d.get('href'))
  if t=='a' and self.inmain:self.links.append(d.get('href',''))
  if t=='script' and d.get('type')=='application/ld+json':self.injson=True;self.script=''
  if t=='title':self.title=True
 def handle_endtag(self,t):
  if t=='main':self.inmain=False;self.mainends+=1
  if t=='script' and self.injson:self.jsons.append(json.loads(self.script));self.injson=False
  if t=='title':self.title=False
 def handle_data(self,s):
  if self.inmain:self.words.extend(s.split())
  if self.injson:self.script+=s
  if self.title:self.titles.append(s)
def check():
 live='--live' in sys.argv;out=ROOT/('public' if 'public' in sys.argv else '.')
 cfg=json.loads((ROOT/'vercel.json').read_text());redirects={r['source'] for r in cfg.get('redirects',[])};holds=json.loads((ROOT/'discovery_review_holds.json').read_text())
 sitemap=(out/'sitemap.xml').read_text()
 results=[]
 for row in M['pages']:
  path=row['path'];assert path not in redirects,path;assert path not in holds,path
  if live:
   with urllib.request.urlopen(SITE+path,timeout=40) as r:
    assert r.status==200,(path,r.status);assert urlsplit(r.url).path==path,(path,r.url);s=r.read().decode()
  else:s=(out/path.strip('/')/'index.html').read_text()
  p=Page();p.feed(s)
  assert p.h1==p.main==p.mainends==1,(path,p.h1,p.main,p.mainends)
  assert p.canonical==[SITE+path],(path,p.canonical)
  assert row['title'] in ' '.join(p.words),path
  assert 500<=len(p.words)<=1400,(path,len(p.words))
  assert '<p><h3' not in s,path
  assert not re.search(r'<meta[^>]+content="[^"]*noindex',s),path
  assert SITE+path in sitemap,path
  assert '/pricing/' in p.links and any(x in p.links for x in ['/discovery/','/cost-seg-discovery/']),path
  assert '$7,800' in s and '$9,800' in s,path
  assert len(p.jsons)>0,path
  for href in p.links:
   if href.startswith('/'):
    clean=urlsplit(href).path
    assert (out/clean.strip('/')/'index.html').exists() or (out/clean.lstrip('/')).exists(),(path,href)
  results.append({'path':path,'words':len(p.words),'canonical':p.canonical[0]})
 for f in M['discovery_pages']:
  s=(out/f).read_text();assert '<!-- owner-decisions:start -->' in s,f
  assert any(p['path'] in s for p in M['pages']),f
 print(json.dumps({'mode':'live' if live else str(out),'pages':results,'discovery_pages':len(M['discovery_pages']),'errors':[]},indent=2))
if __name__=='__main__':check()
