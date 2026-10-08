import hashlib,json,re,subprocess,unittest,xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlsplit
from pathlib import Path
from discovery_inventory import eligible,redirects,Metadata
ROOT=Path(__file__).resolve().parent;SITE='https://www.aetaxadvisors.com'
class Markup(HTMLParser):
 def __init__(self,s):super().__init__();self.h1=0;self.links=[];self.ids=[];self.feed(s)
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='h1':self.h1+=1
  if t=='a':self.links.append(a.get('href',''))
  if a.get('id'):self.ids.append(a['id'])
class Coverage(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.release=json.loads((ROOT/'_gen/competitor-coverage-20261008.json').read_text());cls.adjacent=json.loads((ROOT/'_gen/adjacent-audiences-20261008.json').read_text())
 def test_exact_brand_coverage_and_owner_reuse(self):
  rows=self.release['brands'];self.assertEqual(len(rows),100);self.assertEqual(len({r['slug'] for r in rows}),100)
  for field in ['alternative_url','comparison_url','review_url']:self.assertEqual(len({r[field] for r in rows}),100)
  authority=next(r for r in rows if r['slug']=='cost-segregation-authority');self.assertIn('/cost-seg-authority-vs-ae-tax/',authority['comparison_url']);self.assertFalse((ROOT/'compare/cost-segregation-authority-vs-ae-tax').exists())
  for r in rows:
   self.assertEqual(r['review_url'],r['alternative_url']+'#provider-review')
   text=(ROOT/r['alternative_url'].removeprefix(SITE).strip('/')/'index.html').read_text();self.assertEqual(Markup(text).ids.count('provider-review'),1,r['slug'])
 def test_metadata_links_and_discovery(self):
  changed=set(self.release['changed_paths']+self.adjacent['new_paths']+self.adjacent['updated_hubs']);mapping=redirects()
  for name in ['sitemap.xml','sitemap-comparisons.xml']:
   urls=[e.text for e in ET.parse(ROOT/name).findall('.//{*}loc')];self.assertEqual(len(urls),len(set(urls)),name)
   expected=[SITE+p for p in changed if name=='sitemap.xml' or p.startswith('/compare/')];self.assertTrue(set(expected)<=set(urls))
  titles={}
  for path in changed:
   f=ROOT/path.strip('/')/'index.html';text=f.read_text();p=Markup(text)
   self.assertTrue(eligible(f),path);self.assertEqual(p.h1,1,path)
   self.assertEqual(Metadata(text).canonical,SITE+path,path)
   for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):
    o=json.loads(raw);self.assertNotIn(o.get('@type'),['Review','AggregateRating'])
   for href in p.links:
    u=urlsplit(href)
    if not href.startswith('/') and u.netloc not in ['www.aetaxadvisors.com','aetaxadvisors.com']:continue
    target=ROOT/u.path.strip('/');self.assertTrue(target.is_file() or (target/'index.html').exists(),(path,href))
    if u.fragment and u.path.startswith('/compare/'):
     htmlfile=target if target.is_file() else target/'index.html'
     self.assertIn(u.fragment,Markup(htmlfile.read_text()).ids,(path,href))
   title=Metadata(text).title;self.assertNotIn(title,titles,(path,titles.get(title)));titles[title]=path
 def test_protected_files_unchanged(self):
  for n in ['index.html','assets/style.css','assets/site-ux.js','vercel.json','site_template.py']:
   self.assertEqual(subprocess.check_output(['git','show','HEAD:'+n],cwd=ROOT),(ROOT/n).read_bytes(),n)
if __name__=='__main__':unittest.main()
