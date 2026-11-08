"""Prevent reviewed factual errors and unsupported template claims from returning."""
from pathlib import Path
from html.parser import HTMLParser
import json
import re
import sys


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.noindex = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('name') == 'robots':
            self.noindex |= 'noindex' in attrs.get('content', '').lower()


root = Path(sys.argv[1] if len(sys.argv) > 1 else 'public')
redirects = json.loads((Path(__file__).parent / 'content-consolidation.json').read_text())['redirects']
patterns = {
    'Unsupported typical annual savings': r'proper tax planning typically saves',
    'Unsupported deduction uplift': r'capture 30[–-]50% more in total deductions',
    'Blanket compliance promise': r'All strategies recommended by AE Tax Advisors are fully compliant',
    'Retirement contributions do not generally reduce FICA': r'Maximizing retirement plan contributions reduces W-2 income and the corresponding FICA taxes',
    'Outdated 2026 Section 179 ceiling': r'(?:Section 179[^<\n]{0,100}\$1,250,000[^<\n]{0,45}(?:for|in) 2026|Section 179[^<\n]{0,80}2026[^<\n]{0,80}\$1,250,000)',
}
errors = []
checked = 0
for file in root.rglob('*.html'):
    route = '/' + str(file.relative_to(root)).removesuffix('index.html')
    if route in redirects:
        continue
    source = file.read_text()
    page = Page()
    page.feed(source)
    if page.noindex:
        continue
    checked += 1
    for label, pattern in patterns.items():
        if re.search(pattern, source, re.I):
            errors.append({'file': str(file.relative_to(root)), 'issue': label})
print(json.dumps({'pages': checked, 'reviewedClaimErrors': errors}, indent=2))
sys.exit(bool(errors))
