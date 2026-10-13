"""Focused ASCII wildcard/longest-rule regressions; no network requests.

Google semantics: https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec
stdlib robotparser does not support Google's wildcard matching.
"""
import ast
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def can_fetch(text, url):
    matches = []
    for line in text.splitlines():
        field, separator, rule = line.partition(':')
        if not separator or field.lower() not in ('allow', 'disallow'):
            continue
        rule = rule.split('#', 1)[0].strip()
        if not rule:
            continue
        pattern = '^' + re.escape(rule).replace(r'\*', '.*')
        if rule.endswith('$'):
            pattern = pattern[:-2] + '$'
        if re.search(pattern, url):
            matches.append((len(rule), field.lower() == 'allow'))
    return max(matches, default=(0, True))[1]


class RenderingRobotsTests(unittest.TestCase):
    def test_google_documented_precedence_examples(self):
        self.assertTrue(can_fetch('Allow: /folder\nDisallow: /folder', '/folder/page'))
        self.assertFalse(can_fetch('Allow: /page\nDisallow: /*.htm', '/page.htm'))
        self.assertFalse(can_fetch('Disallow: /*.php$', '/file.php'))
        self.assertTrue(can_fetch('Disallow: /*.php$', '/file.php?v=1'))

    def test_reproduces_original_homepage_conflict(self):
        rules = (ROOT / 'robots.txt').read_text()
        before = '\n'.join(line for line in rules.splitlines()
                           if not line.startswith('Allow: /assets/'))
        self.assertIn('/assets/footer.css?v=20261001', (ROOT / 'index.html').read_text())
        self.assertFalse(can_fetch(before, '/assets/footer.css?v=20261001'))
        self.assertTrue(can_fetch(rules, '/assets/footer.css?v=20261001'))

    def test_versioned_rendering_and_page_restrictions(self):
        rules = (ROOT / 'robots.txt').read_text()
        for url in ('/assets/footer.css?v=20261001',
                    '/assets/case-profile-filters.css?v=20261002',
                    '/assets/case-profile-filters.js?v=20261002',
                    '/assets/nested/widget.js?v=2', '/', '/recommendations/nth-degree/'):
            self.assertTrue(can_fetch(rules, url), url)
        for url in ('/?v=1', '/services/?v=1', '/assets/data.json?v=1',
                    '/research/source.csv?v=1', '/scripts/private.js?v=1',
                    '/assets/page.html?v=1', '/other/widget.js?v=1',
                    '/?utm_source=test', '/?fbclid=x', '/?gclid=x', '/?ref=x',
                    '/assets/footer.css?utm_source=test'):
            self.assertFalse(can_fetch(rules, url), url)

    def test_legacy_blocking_generators_keep_exceptions(self):
        for name in ('improve_owner_discovery.py', 'seo_service_schema.py'):
            tree = ast.parse((ROOT / name).read_text())
            templates = [node.value for node in ast.walk(tree)
                         if isinstance(node, ast.Constant) and isinstance(node.value, str)
                         and 'Disallow: /*?v=' in node.value]
            self.assertEqual(len(templates), 1, name)
            for rule in ('Allow: /assets/*.css?v=', 'Allow: /assets/*.js?v='):
                self.assertIn(rule, templates[0], name)

    def test_staged_robots_and_resources(self):
        self.assertEqual((ROOT / 'robots.txt').read_bytes(),
                         (ROOT / 'public/robots.txt').read_bytes())
        for name in ('footer.css', 'case-profile-filters.css', 'case-profile-filters.js'):
            self.assertTrue((ROOT / 'public/assets' / name).is_file(), name)
        for name in ('test_robots_rendering.py', 'seo_service_schema.py',
                     'improve_owner_discovery.py', 'scripts/build-public.cjs'):
            self.assertFalse((ROOT / 'public' / name).exists(), name)


if __name__ == '__main__':
    unittest.main()
