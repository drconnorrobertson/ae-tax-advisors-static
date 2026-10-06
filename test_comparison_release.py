import json,re,unittest
from html.parser import HTMLParser
from urllib.parse import urlsplit
from build_approved_comparison_pages import SLUGS
from discovery_inventory import ROOT,redirects
class Markup(HTMLParser):
 def __init__(self,text):
  super().__init__();self.tags=[];self.links=[];self.headings=0;self.feed(text)
 def handle_starttag(self,t,attrs):
  a=dict(attrs);self.tags.append((t,a))
  if t=='a':self.links.append(a.get('href',''))
  if t=='h1':self.headings+=1
class ComparisonRelease(unittest.TestCase):
 def test_all_nine_pages_render_and_link(self):
  for slug in SLUGS:
   text=(ROOT/'compare'/slug/'index.html').read_text();p=Markup(text)
   self.assertEqual(p.headings,1,slug)
   self.assertNotIn('**Action:**',text);self.assertNotIn('Title tag:',text)
   self.assertIn('href="/assets/style.css"',text)
   self.assertIn('href="/assets/footer.css?v=20261001"',text)
   self.assertIn('content="width=device-width, initial-scale=1.0"',text)
   self.assertIn('href="https://www.aetaxadvisors.com/compare/'+slug+'/"',text)
   for tag,a in p.tags:
    if tag=='th':self.assertIn(a.get('scope'),['row','col'])
   for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):json.loads(block)
   for href in p.links:
    if href.startswith('/'):
     path=urlsplit(href).path;target=ROOT/path.lstrip('/')
     self.assertTrue(target.is_file() or (target/'index.html').is_file(),(slug,href))
 def test_placeholder_routes_have_complete_destinations(self):
  mapping=redirects()
  for path in ['tax-advisor-for-attorneys','tax-advisor-for-dentists','tax-advisor-for-consultants','s-corp-for-tutoring-business','tax-strategy-for-car-wash-owners','tax-strategy-for-ecommerce','tax-strategy-for-restaurant-owners','tax-planning-for-freelancers','cost-segregation-for-auto-dealers']:
   dest=mapping['/'+path+'/'];text=(ROOT/dest.strip('/')/'index.html').read_text()
   self.assertGreater(len(text),5000);self.assertEqual(Markup(text).headings,1)
 def test_legacy_p4_redirects_to_updated_guide(self):
  self.assertEqual(redirects()['/compare/p4-tax-and-consulting-alternatives/'],'/compare/p4-tax-alternatives/')
 def test_sitemap_contains_updated_cluster(self):
  for name in ['sitemap.xml','sitemap-comparisons.xml']:
   text=(ROOT/name).read_text()
   for slug in SLUGS:self.assertIn('https://www.aetaxadvisors.com/compare/'+slug+'/',text)
   self.assertNotIn('/compare/p4-tax-and-consulting-alternatives/',text)
if __name__=='__main__':unittest.main()
