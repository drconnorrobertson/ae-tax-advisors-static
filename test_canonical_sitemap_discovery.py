"""Canonical-host corrections must retain advertised discovery after the build."""
from collections import defaultdict
import re
import unittest
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

from discovery_inventory import BASE, ROOT, Metadata, eligible

RESTORED = (
    '/business-owner-tax-calculator/',
    '/cost-segregation-complete-guide-2026/',
    '/crypto-tax-business-owners/',
    '/estate-planning-tax-strategies-business-owners/',
    '/how-much-does-tax-advisor-save-roi/',
    '/how-to-fire-your-cpa/',
    '/irs-audit-defense-business-owners/',
    '/qsbs-section-1202-business-owners/',
    '/rd-tax-credit-small-business/',
    '/tax-mistakes-cost-business-owners-50k/',
    '/tax-planning-checklist-by-quarter/',
)
AMBROSE = '/compare/the-ambrose-group-vs-ae-tax/'


def advertised_locations(root):
    """Follow both robots declarations and nested indexes; count unique maps once."""
    pending = re.findall(r'^Sitemap:\s*(\S+)', (root / 'robots.txt').read_text(), re.M)
    if not pending:
        raise AssertionError('No advertised sitemaps')
    seen, locations = set(), defaultdict(list)
    while pending:
        url = pending.pop()
        if url in seen:
            continue
        seen.add(url)
        if not url.startswith(BASE + '/'):
            raise AssertionError('Unexpected sitemap host: ' + url)
        tree = ET.parse(root / urlsplit(url).path.lstrip('/'))
        locs = [e.text for e in tree.findall('.//{*}loc')]
        if tree.getroot().tag.endswith('sitemapindex'):
            pending.extend(locs)
        else:
            for loc in locs:
                locations[loc].append(url)
    return locations


class CanonicalSitemapDiscovery(unittest.TestCase):
    def check_surface(self, root):
        locations = advertised_locations(root)
        main = [e.text for e in ET.parse(root / 'sitemap.xml').findall('.//{*}loc')]
        for route in RESTORED:
            with self.subTest(surface=str(root), route=route):
                source = ROOT / route.strip('/') / 'index.html'
                self.assertTrue(eligible(source), 'Do not promote held, redirected or noindex pages')
                page = root / route.strip('/') / 'index.html'
                meta = Metadata(page.read_text())
                self.assertEqual(meta.canonical, BASE + route)
                self.assertFalse(meta.noindex)
                self.assertEqual(main.count(BASE + route), 1)
                self.assertEqual(locations[BASE + route], [BASE + '/sitemap.xml'])
        # This comparison has an explicit single-topic-map policy, not a main-map requirement.
        self.assertNotIn(BASE + AMBROSE, main)
        self.assertEqual(locations[BASE + AMBROSE], [BASE + '/sitemap-comparisons.xml'])

    def test_source_advertised_discovery(self):
        self.check_surface(ROOT)

    def test_release_advertised_discovery(self):
        self.assertTrue((ROOT / 'public').is_dir(), 'Run the configured release build first')
        self.check_surface(ROOT / 'public')


if __name__ == '__main__':
    unittest.main()
