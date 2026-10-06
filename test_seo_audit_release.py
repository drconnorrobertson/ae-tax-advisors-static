"""Release gates for content consistency, discovery decisions and staged routes."""
import html
import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
from discovery_inventory import ROOT, BASE, Metadata, inventory, redirects, review_holds
from build_seo_audit_release import PAGES

NS = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
PUBLIC = ROOT / 'public'

def clean(text):
    return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', '', text))).strip()

def nodes(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from nodes(child)

def resolves(route, base=PUBLIC):
    target = base / unquote(route).lstrip('/')
    return target.is_file() or (target / 'index.html').is_file()

class SEOReleaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {p['path'] for p in inventory()}
        cls.mapping = redirects()

    def test_review_decisions_do_not_promote_the_omitted_batch(self):
        self.assertEqual(len(review_holds()), 146)
        self.assertFalse(set(review_holds()) & self.pages)
        self.assertIn('/is-cost-segregation-worth-it/', self.pages)
        for old, dest in {
            '/tax-planning-for-law-firms/': '/attorney-tax-planning/',
            '/s-corp-for-online-business/': '/services/s-corp-election/',
            '/tax-advisor-florida/': '/florida/',
        }.items():
            self.assertEqual(self.mapping[old], dest)
            self.assertNotIn(dest, self.mapping)
            self.assertIn(dest, self.pages)
            self.assertNotIn(old, self.pages)
            self.assertTrue(resolves(dest))

    def test_main_inventory_is_complete_and_every_map_is_eligible(self):
        main = {x.text.removeprefix(BASE) for x in ET.parse(ROOT/'sitemap.xml').iter(NS+'loc')}
        self.assertEqual(main, self.pages)
        for file in ROOT.glob('sitemap*.xml'):
            tree = ET.parse(file)
            urls = [e.text for e in tree.iter(NS+'loc')]
            self.assertEqual(len(urls), len(set(urls)), file.name)
            for url in urls:
                self.assertTrue(url.startswith(BASE+'/'), (file.name, url))
                route = url.removeprefix(BASE)
                self.assertTrue(resolves(route), (file.name, route))
                if tree.getroot().tag == NS+'urlset':
                    self.assertIn(route, self.pages, (file.name, route))

    def test_rewritten_guides_have_consistent_visible_faqs_and_schema(self):
        for path, title, h1, description, prose, faqs, sources, published in PAGES:
            text = (PUBLIC/path.strip('/')/'index.html').read_text()
            self.assertEqual(Metadata(text).canonical, BASE+path)
            self.assertFalse(Metadata(text).noindex)
            self.assertEqual(len(re.findall('<h1\\b', text)), 1, path)
            main = re.search('<main[^>]*>(.*?)</main>', text, re.S).group(1)
            self.assertGreater(len(clean(main).split()), 600, path)
            graph = [json.loads(s) for s in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S)]
            questions = {n['name']: n['acceptedAnswer']['text'] for data in graph for n in nodes(data) if n.get('@type') == 'Question'}
            for q, answer in faqs:
                self.assertEqual(clean(questions[q]), clean(answer), path)
                self.assertIn(clean(answer), clean(main), (path, q))
            article = next(n for data in graph for n in nodes(data) if n.get('@type') == 'Article')
            self.assertEqual(article['datePublished'][:10], published)
            self.assertEqual(article['citation'], sources)

    def test_retained_targets_preserve_the_three_intents(self):
        attorney = (PUBLIC/'attorney-tax-planning/index.html').read_text()
        self.assertIn('Partnership income needs its own analysis', attorney)
        online = (PUBLIC/'services/s-corp-election/index.html').read_text()
        self.assertIn('S-corporation decisions for an online business', online)
        florida = (PUBLIC/'florida/index.html').read_text()
        self.assertIn('Tax advisory for Florida business and rental owners', florida)
        self.assertIn('6% state', florida)
        self.assertNotIn('Florida charges a 6% state Tourist Development Tax', florida)
        self.assertNotIn('Florida fully conforms', florida)

    def test_known_shared_false_answers_are_not_restored(self):
        prohibited = ['Can spouses combine hours to qualify?',
            'Once one spouse qualifies, spousal participation may then be combined',
            'For Test 4, you need more than 100 hours',
            'A property averaging seven days or less is typically nonresidential real property.',
            'when the activity\'s character changes.',
            'meaning a $7,500 study can generate $37,500 to $150,000']
        for file in PUBLIC.rglob('*.html'):
            text = file.read_text()
            # REPS-specific authored explanations may correctly describe qualification
            # followed by participation; the generic ambiguous FAQ is banned separately.
            for claim in prohibited[:1] + prohibited[2:]:
                self.assertNotIn(claim, text, str(file.relative_to(PUBLIC)))

    def test_jsonld_syntax_across_the_public_site(self):
        count = 0
        for file in PUBLIC.rglob('*.html'):
            for s in re.findall(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', file.read_text(), re.S):
                json.loads(s); count += 1
        self.assertGreater(count, 1500)

    def test_public_boundary_preserves_routes_and_excludes_sources(self):
        for route in ['/index.html', '/assets/style.css', '/assets/site-ux.js',
                      '/assets/ae-tax-logo.png', '/tools/property-review-prep/intake.js',
                      '/robots.txt', '/llms.txt', '/llms.md', '/.well-known/llms.txt',
                      '/feed.xml', '/compare/tax-advisory-firm-comparison.json',
                      '/research/tax-planning-case-study-outcomes.json',
                      '/research/tax-planning-case-study-outcomes.csv']:
            self.assertTrue(resolves(route), route)
        self.assertFalse(list(PUBLIC.rglob('*.py')))
        for route in ['/llm_build.py', '/vercel.json', '/scripts/build-public.cjs',
                      '/research/buyer_question_candidates.tsv', '/owner_million_manifest.json',
                      '/.git/config', '/_test-push/index.html']:
            self.assertFalse(resolves(route), route)

    def test_local_links_in_changed_guides_resolve_after_redirects(self):
        for route in [p[0] for p in PAGES] + ['/florida/', '/services/s-corp-election/']:
            text = (PUBLIC/route.strip('/')/'index.html').read_text()
            for link in re.findall(r'(?:href|src|poster)="([^"]+)"', text):
                url = urlsplit(urljoin(BASE+route, html.unescape(link)))
                if url.hostname not in ('aetaxadvisors.com', 'www.aetaxadvisors.com'):
                    continue
                target = self.mapping.get(url.path, url.path)
                self.assertTrue(resolves(target), (route, link))
                if url.fragment and target != url.path:
                    continue
                if url.fragment and target.endswith('/'):
                    destination = (PUBLIC/target.strip('/')/'index.html').read_text()
                    self.assertIn('id="'+url.fragment+'"', destination, (route, link))

if __name__ == '__main__':
    unittest.main()
