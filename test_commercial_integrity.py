import json,re,unittest
from schema_hygiene import scrub
from discovery_inventory import ROOT,eligible,redirects
class CommercialIntegrity(unittest.TestCase):
 def test_corrupted_breadcrumbs_are_detected_and_repaired(self):
  node={'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':'https://example.com/'},'https://social.example.com/']}
  findings=[];self.assertFalse(scrub(node,False,findings));self.assertTrue(findings);self.assertEqual(len(node['itemListElement']),2)
  self.assertTrue(scrub(node,True,[]));self.assertEqual(len(node['itemListElement']),1)
  findings=[];self.assertFalse(scrub(node,False,findings));self.assertFalse(findings)
 def test_all_commercial_paths_resolve_directly(self):
  mapping=redirects()
  for group in json.loads((ROOT/'commercial_intents.json').read_text()):
   for target in (group['destination'],group['secondary']):
    self.assertNotIn(target,mapping)
    self.assertTrue(eligible(ROOT/target.strip('/')/'index.html'))
   for slug in group['support']:
    text=(ROOT/slug/'index.html').read_text()
    self.assertEqual(text.count('<!-- commercial-owner-path -->'),1,slug)
    self.assertIn('href="'+group['destination']+'"',text)
 def test_pricing_consolidation(self):
  self.assertEqual(redirects()['/cost-segregation-pricing/'],'/cost-segregation-study-cost-pricing/')
  text=(ROOT/'cost-segregation-study-cost-pricing/index.html').read_text()
  self.assertIn('$2,000 minimum',text);self.assertIn('$1 per square foot',text)
  self.assertNotIn('cost-segregation-pricing/',(ROOT/'sitemap.xml').read_text())
if __name__=='__main__':unittest.main()
