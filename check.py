import json,re,sys,collections,gzip
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'dist';fail=[];pages=list(OUT.rglob('*.html'));titles=collections.Counter();indexable=set()
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.hrefs=[];self.h1=0;self.canon=[];self.title=False;self.titletext='';self.schemas=[];self.schema=False;self.schematext='';self.noindex=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='a' and a.get('href'):self.hrefs.append(a['href'])
  if tag=='h1':self.h1+=1
  if tag=='link' and a.get('rel')=='canonical':self.canon.append(a.get('href'))
  if tag=='title':self.title=True
  if tag=='meta' and a.get('name')=='robots' and 'noindex' in a.get('content',''):self.noindex=True
  if tag=='script' and a.get('type')=='application/ld+json':self.schema=True;self.schematext=''
 def handle_endtag(self,tag):
  if tag=='title':self.title=False
  if tag=='script' and self.schema:self.schemas.append(self.schematext);self.schema=False
 def handle_data(self,data):
  if self.title:self.titletext+=data
  if self.schema:self.schematext+=data
for p in pages:
 txt=p.read_text();a=Parser();a.feed(txt);titles[a.titletext]+=1
 if a.h1!=1:fail.append(f'{p.relative_to(OUT)}: H1 count {a.h1}')
 if len(a.canon)!=1:fail.append(f'{p}: canonical count {len(a.canon)}')
 if not a.noindex and a.canon:indexable.add(a.canon[0])
 if '\u2014' in txt:fail.append(f'{p}: em dash')
 for raw in a.schemas:
  try:json.loads(raw)
  except:fail.append(f'{p}: broken JSON-LD')
 for href in a.hrefs:
  if not href.startswith('/') or href.startswith('//'):continue
  target=unquote(urlparse(href).path).lstrip('/');t=OUT/target
  if not (t.is_file() or (t/'index.html').is_file()):fail.append(f'{p.relative_to(OUT)}: broken link {href}')
dups=[(t,n) for t,n in titles.items() if n>1 and not t.startswith('Page Not Found')]
if dups:fail.append('Duplicate page titles: '+str(dups[:5]))
sitemap=[]
for p in OUT.glob('sitemap-*.xml'):
 tree=ET.parse(p);sitemap.extend(n.text for n in tree.iter() if n.tag.endswith('loc'))
if set(sitemap)!=indexable:fail.append(f'Sitemap mismatch: {len(set(sitemap)^indexable)}')
firms=json.loads((OUT/'firms.json').read_text());ae=firms[0]
if ae['slug']!='ae-tax-advisors':fail.append('AE is not first')
if len(set(f['slug'] for f in firms))!=len(firms):fail.append('Duplicate firm slug')
if len(firms)<1001:fail.append('Fewer than 1000 external firms')
def load_data(name):
 p=ROOT/'data'/name
 return json.loads(p.read_text() if p.exists() else gzip.decompress(Path(str(p)+'.gz').read_bytes()))
guides=load_data('guides.json')
aeurls=load_data('ae-existing-urls.json')
aeslugs={urlparse(u).path.strip('/') for u in aeurls}
collision=[g['slug'] for g in guides if g['slug'] in aeslugs]
if collision:fail.append('AE slug collision: '+str(collision))
print(json.dumps({'html_pages':len(pages),'firm_listings':len(firms),'buyer_guides':len(guides),'indexable_urls':len(indexable),'broken_links_or_other_failures':len(fail),'ae_slug_collisions':collision},indent=2))
for item in fail[:20]:print(item)
sys.exit(bool(fail))
