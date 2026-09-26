"""Release checks for crawler access and discovery-file eligibility."""
import json
import re
import unittest
import urllib.robotparser
import xml.etree.ElementTree as ET
from discovery_inventory import ROOT, BASE, Metadata, inventory, redirects

class DiscoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages={p['path'] for p in inventory()}

    def test_metadata_attribute_order_and_bot_noindex(self):
        meta=Metadata("<meta content='noindex,follow' name='googlebot'><link href='https://x/' rel='canonical'><title>A &amp; B</title>")
        self.assertTrue(meta.noindex);self.assertEqual(meta.canonical,'https://x/');self.assertEqual(meta.title,'A & B')

    def test_sitemaps_contain_only_canonical_eligible_pages(self):
        for name in ('sitemap.xml','sitemap-cost-segregation.xml','sitemap-owner-guides.xml'):
            urls=[x.text for x in ET.parse(ROOT/name).iter() if x.tag.endswith('loc')]
            self.assertEqual(len(urls),len(set(urls)),name)
            self.assertTrue(all(u.removeprefix(BASE) in self.pages for u in urls),name)

    def test_blog_cards_exclude_redirects_and_noindex(self):
        text=(ROOT/'blog/index.html').read_text()
        urls=re.findall(r'<h3><a href="([^"]+)"',text)
        self.assertGreater(len(urls),500)
        self.assertTrue(set(urls)<=self.pages)

    def test_optional_ai_indexes_use_eligible_targets(self):
        self.assertEqual((ROOT/'llms.txt').read_text(),(ROOT/'llms.md').read_text())
        self.assertEqual((ROOT/'llms.txt').read_text(),(ROOT/'.well-known/llms.txt').read_text())
        for name in ('llms.txt','llms-full.txt'):
            urls=re.findall(r'\]\('+re.escape(BASE)+r'([^\)]+)\)',(ROOT/name).read_text())
            self.assertTrue(all(u in self.pages or u.endswith(('.xml','.json')) for u in urls),name)

    def test_crawlers_can_see_public_content_and_staging_noindex(self):
        parser=urllib.robotparser.RobotFileParser();parser.parse((ROOT/'robots.txt').read_text().splitlines())
        for bot in ('Googlebot','Bingbot','OAI-SearchBot','ChatGPT-User','PerplexityBot','ClaudeBot','GPTBot'):
            self.assertTrue(parser.can_fetch(bot,BASE+'/cost-segregation-study/'),bot)
            self.assertTrue(parser.can_fetch(bot,BASE+'/blog-staging/'),bot)
            # stdlib robotparser does not implement Google's wildcard matching.
            # Check that there is no bot-specific group overriding the wildcard group.
            self.assertFalse(any(bot.lower() in [a.lower() for a in e.useragents] for e in parser.entries),bot)

    def test_consolidation_has_no_chain(self):
        mapping=redirects()
        for old in ('/tools/cost-seg-calculator/','/cost-segregation-savings-calculator/','/cost-seg-estimator/'):
            self.assertEqual(mapping[old],'/cost-segregation-calculator/')
            self.assertNotIn(mapping[old],mapping)

    def test_feed_urls_are_public_and_owner_relevant(self):
        items=ET.parse(ROOT/'feed.xml').findall('.//item')
        self.assertEqual(len(items),50)
        for item in items:self.assertIn(item.findtext('link').removeprefix(BASE),self.pages)

if __name__=='__main__':unittest.main()
