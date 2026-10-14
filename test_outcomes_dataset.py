"""Recursively validate outcomes Dataset definitions and references, offline."""
import json
import re
import unittest
from pathlib import Path
import build_case_study_outcomes_report as report

ROOT = Path(__file__).resolve().parent
PAGE = 'research/tax-planning-case-study-outcomes/index.html'
LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def nodes(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from nodes(child)


def datasets(document):
    return [node for block in LD.findall(document) for node in nodes(json.loads(block))
            if 'Dataset' in ([node.get('@type')] if isinstance(node.get('@type'), str)
                             else node.get('@type', []))]


class OutcomesDatasetTests(unittest.TestCase):
    def assert_valid_report(self, document):
        definitions = datasets(document)
        self.assertEqual(len(definitions), 1)
        dataset = definitions[0]
        self.assertEqual(dataset['@id'], report.DATASET_ID)
        self.assertTrue(dataset['name'])
        self.assertTrue(dataset['description'])
        self.assertEqual(dataset['creator']['name'], 'AE Tax Advisors')
        self.assertNotIn('license', dataset)
        blocks = [json.loads(block) for block in LD.findall(document)]
        article = next(node for block in blocks for node in nodes(block)
                       if node.get('@type') == 'Article')
        self.assertEqual(article['about'], [{'@id': dataset['@id']}])
        self.assertEqual({item['contentUrl'] for item in dataset['distribution']},
                         {report.T.SITE + report.JSON_PATH, report.T.SITE + report.CSV_PATH})

    def test_recursive_scanner_catches_original_nested_definition(self):
        fixture = [{'@type': 'Article', 'about': [{'@type': 'Dataset', 'name': 'Cohort'}]},
                   {'@type': 'Dataset', 'name': 'Cohort', 'description': 'Published outcomes',
                    'creator': {'@type': 'Organization', 'name': 'AE Tax Advisors'}}]
        definitions = datasets('<script type="application/ld+json">' + json.dumps(fixture) + '</script>')
        self.assertEqual(len(definitions), 2)
        self.assertEqual(sum(not node.get('description') for node in definitions), 1)
        self.assertEqual(sum(not node.get('creator') for node in definitions), 1)

    def test_nested_graph_and_type_arrays_are_scanned(self):
        fixture = {'@graph': [{'@type': 'Article', 'about': [{'@type': ['Thing', 'Dataset']}]}]}
        self.assertEqual(len(datasets('<script type="application/ld+json">' + json.dumps(fixture) + '</script>')), 1)

    def test_generator_and_committed_page(self):
        originals, rows, generated_count = report.cohort()
        self.assert_valid_report(report.report_html(originals, rows, generated_count))
        self.assert_valid_report((ROOT / PAGE).read_text())

    def test_staged_page(self):
        self.assert_valid_report((ROOT / 'public' / PAGE).read_text())



if __name__ == '__main__':
    unittest.main()
