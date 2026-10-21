"""Keep the existing Ambrose comparison discoverable through deployment."""
import json
import re
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
ROUTE = 'compare/the-ambrose-group-vs-ae-tax/'
URL = 'https://www.aetaxadvisors.com/' + ROUTE


class Tags(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class AmbroseDiscovery(unittest.TestCase):
    def check_release(self, root):
        text = (root / ROUTE / 'index.html').read_text()
        tags = Tags(text).tags
        self.assertEqual([a.get('href') for t, a in tags
                          if t == 'link' and a.get('rel') == 'canonical'], [URL])
        self.assertEqual([a.get('content') for t, a in tags
                          if t == 'meta' and a.get('property') == 'og:url'], [URL])
        self.assertFalse(any('noindex' in a.get('content', '').lower()
                             for t, a in tags if t == 'meta'
                             and a.get('name') in ('robots', 'googlebot')))
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
            json.loads(block)
        advertised = re.findall(r'^Sitemap:\s*(\S+)', (root / 'robots.txt').read_text(), re.M)
        pending = list(advertised)
        seen = set()
        occurrences = []
        while pending:
            sitemap = pending.pop()
            if sitemap in seen:
                continue
            seen.add(sitemap)
            tree = ET.parse(root / urlsplit(sitemap).path.lstrip('/'))
            locs = [e.text for e in tree.findall('.//{*}loc')]
            if tree.getroot().tag.endswith('sitemapindex'):
                pending.extend(locs)
            else:
                occurrences.extend(sitemap for loc in locs if loc == URL)
        self.assertEqual(occurrences, ['https://www.aetaxadvisors.com/sitemap-comparisons.xml'])

    def test_source(self):
        self.check_release(ROOT)

    def test_deployment_output(self):
        self.assertTrue((ROOT / 'public').is_dir(), 'Run the configured Vercel build first')
        self.check_release(ROOT / 'public')


if __name__ == '__main__':
    unittest.main()
