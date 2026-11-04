"""Validate the retained 100-page content refresh in source and release output."""
import html,json,re,subprocess,sys
from pathlib import Path
from urllib.parse import urlsplit
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'content/long-tail-refresh-20261104'
class Page(HTMLParser):
 def __init__(self,s):
  super().__init__();self.tags=[];self.text=[];self.feed(s)
 def handle_starttag(self,tag,attrs):self.tags.append((tag,dict(attrs)))
 def handle_data(self,s):self.text.append(s)
 def count(self,tag):return sum(t==tag for t,_ in self.tags)
 def attr(self,tag,key,value,out):return next(a[out] for t,a in self.tags if t==tag and a.get(key)==value)
 def content(self):return ' '.join(' '.join(self.text).split())
def block(s,tag):return re.search('<'+tag+r'\b[^>]*>.*?</'+tag+'>',s,re.S)[0]
def text(s):return Page(s).content()
def verify():
 m=json.loads((DATA/'manifest.json').read_text());assert len(m['pages'])==100
 links=0;words=oldwords=0;all_titles=[]
 for r in m['pages']:
  file=r['path'].strip('/')+'/index.html';s=(ROOT/file).read_text()
  old=subprocess.check_output(['git','show','ba9cb31dc:'+file],text=True,cwd=ROOT)
  assert block(s,'header')==block(old,'header'),file+' header'
  assert block(s,'footer')==block(old,'footer'),file+' footer'
  for tree in (ROOT,ROOT/'public'):
   f=tree/file;h=f.read_text();d=Page(h);main=block(h,'main');v=text(main)
   assert d.count('h1')==1,file+' H1'
   assert d.attr('link','rel','canonical','href')=='https://www.aetaxadvisors.com'+r['path'],file+' canonical'
   assert 'noindex' not in d.attr('meta','name','robots','content'),file+' indexability'
   assert len(d.attr('meta','name','description','content'))<=185,file+' description'
   assert 'id="worked-example"' in main and 'id="preparation-checklist"' in main
   assert '\u2014' not in v,file+' em dash'
   assert 'Put the answer into your own tax file' not in v
   assert 'Another situation to compare' in v
   assert 'long-tail-refresh:20261104:start' in main
   title=text(block(h,'title'));assert len(title)<95
   objects=[json.loads(x) for x in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',h,re.S)]
   faq=next(x for x in objects if x.get('@type')=='FAQPage')
   assert len(faq['mainEntity'])==1
   for q in faq['mainEntity']:assert q['name'] in v and q['acceptedAnswer']['text'] in v,file+' FAQ parity'
   article=next(x for x in objects if x.get('@type') in ('Article','BlogPosting'))
   assert article['dateModified']=='2026-11-04'
   assert article['datePublished']=='2026-10-06'
   assert article['citation']==r['sources']
   if tree.name=='public':
    hrefs=[a['href'] for t,a in Page(main).tags if t=='a' and 'href' in a]
    assert all(p in hrefs for p in r['related']),file+' related'
    for href in hrefs:
     u=urlsplit(href)
     if u.netloc and u.netloc!='www.aetaxadvisors.com':continue
     if not u.path or u.path=='/':continue
     dest=tree/u.path.lstrip('/')
     if u.path.endswith('/'):dest=dest/'index.html'
     assert dest.exists(),(file,href)
     links+=1
  words+=len(text(block(s,'main')).split());oldwords+=len(text(block(old,'main')).split());all_titles.append(title)
 assert len(set(all_titles))==100
 for tree in (ROOT,ROOT/'public'):
  sitemap=(tree/'sitemap-blog.xml').read_text()
  for r in m['pages']:
   loc='https://www.aetaxadvisors.com'+r['path']
   row=next(x for x in re.findall('<url>.*?</url>',sitemap,re.S) if '<loc>'+loc+'</loc>' in x)
   assert '<lastmod>2026-11-04</lastmod>' in row
 result=dict(pages_verified=100,new_main_words=words,previous_main_words=oldwords,internal_article_links_checked=links,unique_titles=100,faq_schema_parity='passed',canonical_and_indexability='passed',publication_dates_preserved=True,headers_and_footers_preserved=True,sitemap_lastmod='passed',broken_internal_links=0)
 (DATA/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':verify()
