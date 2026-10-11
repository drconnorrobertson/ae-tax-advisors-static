import json,re,unittest,xml.etree.ElementTree as ET
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
R=Path(__file__).resolve().parent
M=json.loads((R/'content/provider-comparisons-20261011/manifest.json').read_text())
class Parser(HTMLParser):
 def __init__(self,text):super().__init__();self.tags=[];self.feed(text)
 def handle_starttag(self,t,a):self.tags.append((t,dict(a)))
class ComparisonBatch(unittest.TestCase):
 def test_exact_count_unique_pair_and_broad_coverage(self):
  self.assertEqual(len(set(M['paths'])),500)
  pairs=[tuple(sorted(x['providers'])) for x in M['comparisons']]
  self.assertEqual(len(set(pairs)),496)
  self.assertEqual(len({s for pair in pairs for s in pair}),131)
  for s in ['tax-alchemy','prime-path-advisory','tax-hive','1800-accountant','collective','main-street-tax-advisor-network']:self.assertIn(s,M['provider_degrees'])
 def test_all_pages_metadata_links_and_disclosure(self):
  titles=set()
  for path in M['paths']:
   text=(R/path.strip('/')/'index.html').read_text();parser=Parser(text)
   self.assertEqual(sum(t=='h1' for t,a in parser.tags),1,path)
   self.assertIn('Published by AE Tax Advisors',text) if path not in M['paths'][-4:] else self.assertIn('published by AE Tax Advisors',text)
   canonical=[a['href'] for t,a in parser.tags if t=='link' and a.get('rel')=='canonical']
   self.assertEqual(canonical,['https://www.aetaxadvisors.com'+path])
   title=re.search('<title>(.*?)</title>',text).group(1);self.assertNotIn(title,titles);titles.add(title)
   self.assertNotRegex(text,r'(?i)<meta[^>]+content="[^"]*noindex')
   for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):
    data=json.loads(block);self.assertNotIn(data.get('@type'),['Review','AggregateRating'])
   for t,a in parser.tags:
    if t=='th':self.assertIn(a.get('scope'),['row','col'])
    if t=='a' and a.get('href','').startswith('/'):
     target=R/urlsplit(a['href']).path.lstrip('/')
     self.assertTrue(target.is_file() or (target/'index.html').is_file(),(path,a['href']))
 def test_sitemap_and_public_build(self):
  root=ET.parse(R/'sitemap-provider-comparisons-20261011.xml').getroot()
  urls=[e.text for e in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
  self.assertEqual(set(urls),{'https://www.aetaxadvisors.com'+u for u in M['paths']})
  for path in M['paths']:self.assertTrue((R/'public'/path.strip('/')/'index.html').is_file(),path)
  self.assertFalse((R/'public/content/provider-comparisons-20261011/profiles.json').exists())
  for filename in ['sitemap-index.xml','sitemap_index.xml']:self.assertIn('sitemap-provider-comparisons-20261011.xml',(R/filename).read_text())
if __name__=='__main__':unittest.main()
