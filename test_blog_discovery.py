"""Check that shared site chrome cannot pollute article discovery categories."""
import unittest
from build_blog_index import collect
class BlogDiscoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.posts = {p['slug']:p for p in collect()}
    def test_distinct_editorial_topics(self):
        expected = {
            'business-family-travel-deduction-rules': 'Business Deductions',
            'estimated-tax-safe-harbor-high-income-owner': 'Tax Compliance',
            'cost-segregation-quote-checklist': 'Cost Segregation',
        }
        for slug, category in expected.items():
            self.assertEqual(self.posts[slug]['category'],category,slug)
    def test_intake_topics_do_not_become_cost_segregation(self):
        for slug in ['business-business-loan-proceeds-tax','software-development-costs-section-174a-2026']:
            self.assertNotEqual(self.posts[slug]['category'],'Cost Segregation',slug)
if __name__ == '__main__':unittest.main()
