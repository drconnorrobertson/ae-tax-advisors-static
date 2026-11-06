"""Narrow, independently tested preservation contract for one retired placeholder.

This module never edits files. It permits only deletion of the exact retired
Related Reading item, only on the substantive installment guide, and only when
every other byte of that Related Reading section remains unchanged.
"""
import json
import re
from pathlib import Path

SITE = 'https://www.aetaxadvisors.com'
SOURCE = '/the-business-owners-guide-to-section-453-installment-sales-and-deferred-gain-recognition/'
DESTINATION = '/the-business-owners-guide-to-installment-sales-and-deferred-gain-strategies/'
SECTION731 = '/the-business-owners-guide-to-section-731-distributions-and-recognized-gain/'
SOURCE_FILE = SOURCE.strip('/') + '/index.html'
DESTINATION_FILE = DESTINATION.strip('/') + '/index.html'
SECTION731_FILE = SECTION731.strip('/') + '/index.html'
RETIRED_LABEL = 'The Business Owners Guide To Section 453 Installment Sales And Deferred Gain Recognition'
RETIRED_ITEM = f'            <li><a href="{SOURCE}">{RETIRED_LABEL}</a></li>\n'
RELATED = re.compile(r'<section class="content-section related-reading">.*?</section>', re.S)
FALLBACK_HTML = f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Installment Sale Guide Moved | AE Tax Advisors</title>
    <meta name="robots" content="noindex, follow">
    <link rel="canonical" href="{SITE}{DESTINATION}">
    <link rel="stylesheet" href="/assets/style.css">
</head>
<body>
    <main class="container" style="max-width:760px;margin:80px auto;padding:24px">
        <h1>Installment sale guide</h1>
        <p>This guide has moved. Read <a href="{DESTINATION}">The Business Owner's Guide to Installment Sales and Deferred Gain Strategies</a>.</p>
    </main>
</body>
</html>
'''


def remove_retired_related_item(value):
    sections = list(RELATED.finditer(value))
    if len(sections) != 1 or sections[0][0].count(RETIRED_ITEM) != 1:
        raise ValueError('Expected exactly one retired item in one Related Reading section')
    section = sections[0]
    return value[:section.start()] + section[0].replace(RETIRED_ITEM, '', 1) + value[section.end():]


def reconcile_sale_baseline(old, current, route):
    """Reconcile one proven Related Reading deletion; otherwise preserve strictly."""
    if route != DESTINATION:
        return old
    before, after = RELATED.findall(old), RELATED.findall(current)
    if len(before) == len(after) == 1 and before[0].count(RETIRED_ITEM) == 1:
        if before[0].replace(RETIRED_ITEM, '', 1) == after[0]:
            return remove_retired_related_item(old)
    return old


def redirect_errors(config, mapping):
    errors = []
    records = config.get('redirects', [])
    for route in (SOURCE, SOURCE.rstrip('/')):
        expected = {'source': route, 'destination': DESTINATION, 'permanent': True}
        if [r for r in records if r.get('source') == route] != [expected]:
            errors.append('missing or non-direct permanent redirect: ' + route)
    # The retained canonical must be terminal, not another redirect or loop.
    if any(r.get('source', '').rstrip('/') == DESTINATION.rstrip('/') for r in records):
        errors.append('destination redirect chain or loop')
    if mapping.get(SOURCE) != DESTINATION:
        errors.append('consolidation mapping missing or wrong')
    if SOURCE.rstrip('/') in mapping or any(k.rstrip('/') == DESTINATION.rstrip('/') for k in mapping):
        errors.append('duplicate source mapping or destination consolidation chain')
    return errors


def retirement_errors(root):
    """Replace the former audit-only assertion with this exact retirement contract."""
    root = Path(root)
    errors = redirect_errors(json.loads((root / 'vercel.json').read_text()),
                             json.loads((root / 'scripts/content-consolidation.json').read_text())['redirects'])
    if (root / SOURCE_FILE).read_text() != FALLBACK_HTML:
        errors.append('retired installment fallback differs from the exact approved fallback')
    return errors
