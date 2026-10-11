"""Permanent redirect forms stay out of source and staged discovery."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import discovery_inventory as discovery
import generate_sitemap as sitemap

class RedirectDiscoveryTests(unittest.TestCase):
    def test_supported_permanent_forms_and_temporary_exclusions(self):
        rules = [
            {'source': '/permanent/', 'destination': '/canonical/', 'permanent': True},
            {'source': '/301/', 'destination': '/canonical/', 'statusCode': 301},
            {'source': '/308/', 'destination': '/canonical/', 'statusCode': 308},
            {'source': '/temporary/', 'destination': '/canonical/', 'permanent': False},
            {'source': '/302/', 'destination': '/canonical/', 'statusCode': 302},
            {'source': '/307/', 'destination': '/canonical/', 'statusCode': 307},
            {'source': '/pattern/:path*', 'destination': '/canonical/', 'permanent': True},
        ]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'vercel.json').write_text(json.dumps({'redirects': rules}))
            with patch.object(discovery, 'ROOT', root), patch.object(sitemap, 'Path', lambda name: root / name):
                expected = {'/permanent/', '/301/', '/308/'}
                self.assertEqual(sitemap.redirected_paths(), expected)
                self.assertEqual(discovery.redirects(), dict.fromkeys(expected, '/canonical/'))

    def test_source_and_staged_maps_exclude_flagship_redirects(self):
        import xml.etree.ElementTree as ET
        ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
        rules = json.loads((discovery.ROOT / 'vercel.json').read_text())['redirects']
        rules = [r for r in rules if r.get('permanent') is True and ':' not in r['source']
                 and r['destination'].startswith('/')]
        self.assertEqual(len(rules), 7)
        for base in (discovery.ROOT, discovery.ROOT / 'public'):
            urls = {e.text for e in ET.parse(base / 'sitemap.xml').iter(ns + 'loc')}
            for rule in rules:
                self.assertNotIn(discovery.BASE + rule['source'], urls)
                self.assertIn(discovery.BASE + rule['destination'], urls)
            for name in ('llms.txt', 'llms.md', 'llms-full.txt', '.well-known/llms.txt'):
                text = (base / name).read_text()
                for rule in rules:
                    self.assertNotIn(discovery.BASE + rule['source'] + ')', text)

if __name__ == '__main__':
    unittest.main()
