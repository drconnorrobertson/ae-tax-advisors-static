import json,re,unittest,subprocess
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent;SITE='https://www.aetaxadvisors.com'
class Document(HTMLParser):
 def __init__(self,text):
  super().__init__();self.tags=[];self.hrefs=[];self.h1s=0;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);self.tags.append((tag,a))
  if tag=='a':self.hrefs.append(a.get('href',''))
  if tag=='h1':self.h1s+=1
class Release(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.manifest=json.loads((ROOT/'_gen/seo-campaign-20261007-manifest.json').read_text());cls.redirects={x['source'] for x in json.loads((ROOT/'vercel.json').read_text())['redirects']}
 def test_counts(self):
  self.assertEqual(len([x for x in self.manifest if x['path'].startswith('/compare/') and x['path']!='/compare/']),100);self.assertEqual(sum(x['action']=='new guide' for x in self.manifest),12)
 def test_markup_schema_links(self):
  for x in self.manifest:
   text=(ROOT/x['file']).read_text();p=Document(text);self.assertEqual(p.h1s,1,x['path'])
   self.assertEqual([a['href'] for tag,a in p.tags if tag=='link' and a.get('rel')=='canonical'],[SITE+x['path']],x['path']);self.assertNotIn(x['path'],self.redirects)
   for tag,a in p.tags:
    if tag=='meta' and a.get('name') in ['robots','googlebot']:self.assertNotIn('noindex',a.get('content',''),x['path'])
   for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):
    obj=json.loads(raw)
    if obj.get('@type')=='Article':self.assertEqual(obj['dateModified'],'2026-10-07')
   section=re.search(r'<!-- seo-campaign-20261007:start -->(.*?)<!-- seo-campaign-20261007:end -->',text,re.S);markup=section[1] if section else re.search(r'<main[^>]*>(.*?)</main>',text,re.S)[1]
   for href in Document(markup).hrefs:
    parts=urlsplit(href)
    if href.startswith('/') or parts.netloc in ['www.aetaxadvisors.com','aetaxadvisors.com']:
     path=parts.path;target=ROOT/path.strip('/');self.assertTrue(target.is_file() or (target/'index.html').exists(),(x['path'],href));self.assertNotIn(path,self.redirects,(x['path'],href))
   if x['path'].startswith('/compare/') and x['path']!='/compare/':
    for phrase in ['official service description','published by AE Tax Advisors','book a call with AE']:self.assertIn(phrase,markup)
 def test_discovery(self):
  maps={n:{e.text for e in ET.parse(ROOT/n).findall('.//{*}loc')} for n in ['sitemap.xml','sitemap-comparisons.xml','sitemap-blog.xml','sitemap-cost-segregation.xml']}
  for x in self.manifest:
   self.assertIn(SITE+x['path'],maps['sitemap.xml']);category='sitemap-comparisons.xml' if x['path'].startswith('/compare/') else 'sitemap-blog.xml' if x['path'].startswith('/blog/') else 'sitemap-cost-segregation.xml';self.assertIn(SITE+x['path'],maps[category])
 def test_preserved_content_and_brand(self):
  main=lambda t:re.search(r'<main[^>]*>(.*?)</main>',t,re.S)[1].strip()
  for x in self.manifest:
   if x['action']!='enrich existing':continue
   previous=subprocess.check_output(['git','show','HEAD:'+x['file']],cwd=ROOT,text=True);current=(ROOT/x['file']).read_text();clean=re.sub(r'<!-- seo-campaign-20261007:start -->.*?<!-- seo-campaign-20261007:end -->','',main(current),flags=re.S).strip();self.assertEqual(main(previous),clean,x['path'])
  for n in ['index.html','assets/style.css','assets/site-ux.js','vercel.json','site_template.py']:self.assertEqual(subprocess.check_output(['git','show','HEAD:'+n],cwd=ROOT),(ROOT/n).read_bytes(),n)
if __name__=='__main__':unittest.main()
