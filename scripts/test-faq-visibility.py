#!/usr/bin/env python3
"""Verify the frozen, schema-only repair of 15 historical FAQPage entries.

Run after the complete release pipeline:
  python3 scripts/test-faq-visibility.py public
For direct before/after preservation checks, also supply --baseline-dir PATH.
Private original pages and build manifests stay outside this repository. The
hashes below pin every repaired source/staged byte, including normal release
transforms, and the two legitimate visible uses of the unchanged FAQ bank.
This script validates only; it never regenerates or writes site content.
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse
import ast
import copy
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
COHORT = 'content/faq-visibility-20261106/routes.json'
QUESTION = 'What are my options if I owe more than I can pay?'
ANSWER = ('Installment agreements, currently not collectible status, penalty '
          'abatement for reasonable cause or first-time abatement, and in '
          'appropriate cases an offer in compromise. Which applies depends '
          'on your financial position, and the analysis should happen before '
          'enforcement action begins.')
TARGET = {'@type': 'Question', 'name': QUESTION,
          'acceptedAnswer': {'@type': 'Answer', 'text': ANSWER}}
DEFERRED = '/tax-planning-for-high-net-worth-individuals-with-deferred-compensation-packages/'
SCRIPT = re.compile(r'<script\b[^>]*\btype=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script\s*>', re.I | re.S)
SPECS = {'/ae-tax-advisors-news-press-coverage/': {'source_sha256': '5238b48445b17a6a0ebe552bb1af08425be1b4ac828e6637a58fb253d90a89e1',
                                           'staged_sha256': '11df47b94cac04f954f2181315ce6d6a09c2392a788e1878515bd93b0ed7ce97',
                                           'retained_faq_sha256': '3d9f37b07a80d8f9831d4f244db7ea0438cf6c8ac8b79ba07563022f430d78c8'},
 '/bios/': {'source_sha256': 'ce1699b9102e35f9041ea102be4b27e289eeb5977bc93dd4c84f902f7d48ec73',
            'staged_sha256': '7a9f5a93e029f2c65ea61c8d357d2f0a586d9e8747943f1928ab2e4dacf3387d',
            'retained_faq_sha256': 'e77b45819214677cf5cddbe3ae0ec36ca0e2dc2c9829b261a9f29dd39c65f031'},
 '/blog/depreciation-recapture-planning/': {'source_sha256': '308db5a6b1e7afdad627bd46f55209d84f2b00c7a7de31004658dc3ca9c33f1f',
                                            'staged_sha256': '790510241eda258ceb37109aec6818166cd7faed33c57658a004585472ae467a',
                                            'retained_faq_sha256': '3d9f37b07a80d8f9831d4f244db7ea0438cf6c8ac8b79ba07563022f430d78c8'},
 '/blog/discovery-call-what-to-expect-ae-tax/': {'source_sha256': 'b9056cdd26f10c6e7b6b04a9708fdc78b89fdf30d6d22c5a2cd5f8b94f21b3ff',
                                                 'staged_sha256': 'cf7e327497980cdba04120c72d02907788afe8aa268e03beb3259de22ebb6e7d',
                                                 'retained_faq_sha256': 'e77b45819214677cf5cddbe3ae0ec36ca0e2dc2c9829b261a9f29dd39c65f031'},
 '/blog/when-to-fire-your-cpa-7-red-flags/': {'source_sha256': 'd8ba0fb06d7bfe77222fb5a4958023b2938bffb691122300d8ac89488b745117',
                                              'staged_sha256': '6638ff65f017bbdc23cea7da919bd986e26d0d99743c5e85857ddfd797805267',
                                              'retained_faq_sha256': 'e77b45819214677cf5cddbe3ae0ec36ca0e2dc2c9829b261a9f29dd39c65f031'},
 '/build-audit-proof-tax-documentation/': {'source_sha256': '9634f3fba537d713ad470dee110a588cddcda62a8e98757135634a475f869e2d',
                                           'staged_sha256': '38073d15638abe2aeee6df0018534d62f56d8f592097ae0cb5ffe68a7e3c078e',
                                           'retained_faq_sha256': '2fa40e2e709e9809e58835379065055497fcf2fb1b115482d00d3e138a8ee443'},
 '/build-bulletproof-audit-defense/': {'source_sha256': '4d3105151e25f720d8dd14361fd1925eacf033581bc03e9476a42f4a29fb468e',
                                       'staged_sha256': '5bf873e1b286bfba345a3579a096f29451d79c107cbf89b124c5e384226b8851',
                                       'retained_faq_sha256': 'c2d306671f4235421651080ea2e163ea939e15cda61ebae457add298f89fbe50'},
 '/hiring-first-employee-payroll/': {'source_sha256': 'b335b794b6ddd3dbcc4433789426b069d1dcd57680657238f374ae03e1a02240',
                                     'staged_sha256': '757ba8752076df7608040c56471c017c21dbd5104f3a0f9c14f666e0bd58e0d7',
                                     'retained_faq_sha256': '2fa40e2e709e9809e58835379065055497fcf2fb1b115482d00d3e138a8ee443'},
 '/hiring-first-employee-payroll-setup/': {'source_sha256': '7097c7a02681e5329998313bc60977e39f91cffc8e8c86bee5ece8f226d8cdb9',
                                           'staged_sha256': '5f5121e0c134b5e41971568cc941d5e65dfb4d3c9925a2ebfebd6bf479da58cd',
                                           'retained_faq_sha256': 'e77b45819214677cf5cddbe3ae0ec36ca0e2dc2c9829b261a9f29dd39c65f031'},
 '/how-it-works/': {'source_sha256': 'cff69ddfda5c89c35181962959ba0fd421e78bcaf75ef40f654ef01617a67104',
                    'staged_sha256': '2d6ec3f3c9852108f89b69e42bccebb5498462c9be8fede33cb528e55a2332e8',
                    'retained_faq_sha256': 'f22de1ae4813e54f8cebac380f16164551a40bc81f3bdf699ed56a3593a9fb65'},
 '/industries-clients/': {'source_sha256': '8790a21509212861ac5fd84b44e67f6e5398c64dcd4b9d4a99993e0d198914c7',
                          'staged_sha256': 'd524631934e8cb1b590eab616b08a64bfbb63887560de72c15a928cf569f2782',
                          'retained_faq_sha256': '3d9f37b07a80d8f9831d4f244db7ea0438cf6c8ac8b79ba07563022f430d78c8'},
 '/irs-letter-what-to-do/': {'source_sha256': '42e3aeb17e966dddf7f04808af16bd061811122535a75f3e69ac3bbc382c991f',
                             'staged_sha256': '55170f91d6bbb3ba10948b32139ee03239e4effeb85ad0611da2b854ae58d150',
                             'retained_faq_sha256': 'e77b45819214677cf5cddbe3ae0ec36ca0e2dc2c9829b261a9f29dd39c65f031'},
 '/tax-planning-for-high-net-worth-individuals-with-deferred-compensation-packages/': {'source_sha256': '89301efb1147aebba6952adde09614ce8a874787ed28e8cf0e748ade6eacdfd0',
                                                                                       'staged_sha256': '4b4d1cd83cfffbc73bc5fff4adec8ee12eff652770704a837b66702e2c94142b',
                                                                                       'retained_faq_sha256': 'f22de1ae4813e54f8cebac380f16164551a40bc81f3bdf699ed56a3593a9fb65'},
 '/testimonials/': {'source_sha256': 'd5aeff96aba5970d0f6eedb42ee88a092304ca7b517f078510d7864284d13c64',
                    'staged_sha256': '3af86d39edb4fcfc26dbdc37d402fa3bef3de3a7cf458499548c0cf0d993111d',
                    'retained_faq_sha256': '2fa40e2e709e9809e58835379065055497fcf2fb1b115482d00d3e138a8ee443'},
 '/why-high-net-worth-clients-choose-ae-tax-advisors/': {'source_sha256': '46e8d48be97b6c8ebf219ebc2e4be37145fe2f73f4cb7fde9d5fe33c009f7b8e',
                                                         'staged_sha256': '780fb709fa35e44fcec33d697af22a0a7409c673bb225f4cfa0fd2783552bf89',
                                                         'retained_faq_sha256': '3d9f37b07a80d8f9831d4f244db7ea0438cf6c8ac8b79ba07563022f430d78c8'}}
VALID_USES = {'/offer-in-compromise-irs/': {'source_sha256': 'c6edf6bb746a6cdd9f815d8675ffe2582cd9760e43fb3f97db99d0bd00182e57',
                               'staged_sha256': '8a78639a2666a28ecbbf4288ca34a3ad1db1d507a310fb941f66fbf3e55d3ebd'},
 '/blog/offer-in-compromise-myths-reality/': {'source_sha256': '9cd4c438a4a33227cb34cb906768726b0cd2ed16dc621e8a6a9ffe18a1ab8a81',
                                              'staged_sha256': 'fc89376514a3ded812f2908aef9dae862bf90458b66fe4211b614ecb0c4b2b9e'}}
AUDIT_BANK_SHA256 = 'ee4faa089cd89acf87caf012f13b9cfce832e8e58be1ed58658de6e886e97872'


def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value, str) else value).hexdigest()


def structural_sha(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False))


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.excluded = []
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ('head', 'script', 'style', 'template', 'svg'):
            self.excluded.append(tag)

    def handle_endtag(self, tag):
        if self.excluded and tag == self.excluded[-1]:
            self.excluded.pop()

    def handle_data(self, value):
        if not self.excluded:
            self.parts.append(value)


def visible(text):
    parser = VisibleText()
    parser.feed(text)
    return re.sub(r'\s+', ' ', ' '.join(parser.parts)).strip()


def schemas(text):
    return [json.loads(m[1]) for m in SCRIPT.finditer(text)]


def faq_nodes(value):
    if isinstance(value, dict):
        types = value.get('@type', [])
        if types == 'FAQPage' or isinstance(types, list) and 'FAQPage' in types:
            yield value
        for item in value.values():
            yield from faq_nodes(item)
    elif isinstance(value, list):
        for item in value:
            yield from faq_nodes(item)


def retained_items(text):
    nodes = list(faq_nodes(schemas(text)))
    assert len(nodes) == 1, 'Expected exactly one FAQPage'
    items = nodes[0]['mainEntity']
    assert len(items) == 3, 'Expected three retained questions'
    for item in items:
        assert item['@type'] == 'Question' and item['name'] != QUESTION
        assert item['acceptedAnswer']['@type'] == 'Answer'
        assert item['acceptedAnswer']['text'] != ANSWER
    return items


def remove_exact_orphan(text):
    """Test oracle: delete one exact JSON entry and its necessary comma only.

    Locate entries with JSONDecoder, never a brace-counting/string regex. The
    document and script are not serialized, so all retained bytes survive.
    Ambiguous, modified, duplicated or body-visible targets fail closed.
    """
    assert QUESTION not in visible(text), 'Question is already visible'
    assert ANSWER not in visible(text), 'Answer is already visible'
    blocks = list(SCRIPT.finditer(text))
    objects = [json.loads(m[1]) for m in blocks]
    candidates = [(i, obj) for i, obj in enumerate(objects)
                  if isinstance(obj, dict) and obj.get('@type') == 'FAQPage'
                  and any(x.get('name') == QUESTION for x in obj.get('mainEntity', []))]
    assert len(candidates) == 1, 'Missing or ambiguous target FAQPage'
    i, obj = candidates[0]
    targets = [n for n, item in enumerate(obj['mainEntity']) if item.get('name') == QUESTION]
    assert len(targets) == 1, 'Missing or duplicate target question'
    n = targets[0]
    assert obj['mainEntity'][n] == TARGET, 'Question/answer signature changed'
    assert len(obj['mainEntity']) > 1, 'Must retain the other questions'
    body = blocks[i][1]
    starts = list(re.finditer(r'"mainEntity"\s*:\s*\[', body))
    assert len(starts) == 1
    array_start = starts[0].end()
    pos, spans, commas = array_start, [], []
    decoder = json.JSONDecoder()
    while True:
        pos += len(body[pos:]) - len(body[pos:].lstrip())
        if body[pos] == ']':
            break
        item, end = decoder.raw_decode(body, pos)
        spans.append((pos, end, item))
        pos = end + len(body[end:]) - len(body[end:].lstrip())
        if body[pos] == ',':
            commas.append(pos)
            pos += 1
        else:
            assert body[pos] == ']'
            break
    assert [item for _, _, item in spans] == obj['mainEntity']
    assert len(commas) == len(spans) - 1
    if n < len(spans) - 1:
        start = array_start if n == 0 else commas[n - 1] + 1
        end = commas[n] + 1
    else:
        start, end = commas[n - 1], spans[n][1]
    repaired = body[:start] + body[end:]
    expected = copy.deepcopy(obj)
    del expected['mainEntity'][n]
    assert json.loads(repaired) == expected
    return text[:blocks[i].start(1)] + repaired + text[blocks[i].end(1):]


def validate_page(text, spec, layer, legitimate=False):
    parsed = schemas(text)  # Every JSON-LD block must remain parseable.
    if legitimate:
        matches = [item for node in faq_nodes(parsed) for item in node['mainEntity']
                   if item.get('name') == QUESTION]
        assert matches == [TARGET]
        body = visible(text)
        assert QUESTION in body and ANSWER in body
    else:
        assert QUESTION not in text and ANSWER not in text
        assert structural_sha(retained_items(text)) == spec['retained_faq_sha256']
    assert sha(text) == spec[layer + '_sha256'], 'Non-target bytes changed'


def audit_bank(text):
    tree = ast.parse(text)
    value = next(node.value for node in tree.body if isinstance(node, ast.AnnAssign)
                 and isinstance(node.target, ast.Name) and node.target.id == 'FAQS')
    return ast.literal_eval(value)['audit']


def rejected(action, label):
    try:
        action()
    except (AssertionError, ValueError, KeyError, StopIteration):
        return
    raise AssertionError('Accepted forbidden mutation: ' + label)


def negative_fixtures(root, output):
    harmless = {'@type': 'Question', 'name': 'A retained question?',
                'acceptedAnswer': {'@type': 'Answer', 'text': 'A retained answer.'}}
    def document(items):
        return ('<!doctype html><html><head><title>Fixture</title><script type="application/ld+json">'
                + json.dumps({'@context': 'https://schema.org', '@type': 'FAQPage',
                              'mainEntity': items}, indent=2)
                + '</script></head><body><p>Existing visible copy.</p></body></html>')
    # First, middle and last positions must retain every other object verbatim.
    for pos in range(3):
        items = [copy.deepcopy(harmless), copy.deepcopy(harmless)]
        items.insert(pos, TARGET)
        original = document(items)
        repaired = remove_exact_orphan(original)
        assert schemas(repaired)[0]['mainEntity'] == [harmless, harmless]
        assert visible(repaired) == visible(original)
    original = document([harmless, TARGET, harmless])
    bad = {
        'modified question': original.replace(QUESTION, QUESTION + ' Changed'),
        'modified answer': original.replace(ANSWER, 'Altered answer.'),
        'duplicate target': document([harmless, TARGET, TARGET]),
        'question becomes visible': original.replace('</body>', '<p>' + QUESTION + '</p></body>'),
        'answer becomes visible': original.replace('</body>', '<p>' + ANSWER + '</p></body>'),
        'wrong schema type': original.replace('"FAQPage"', '"WebPage"'),
    }
    for label, changed in bad.items():
        rejected(lambda: remove_exact_orphan(changed), label)
    count = len(bad)
    # Test the real source AND the fully normalized release output.
    for layer, base in [('source', root), ('staged', output)]:
        if base is None:
            continue
        route, spec = next(iter(SPECS.items()))
        text = (base / route.strip('/') / 'index.html').read_bytes().decode()
        item = retained_items(text)[0]
        cases = {
            'retained question': text.replace(item['name'], item['name'] + ' Changed', 1),
            'retained answer': text.replace(item['acceptedAnswer']['text'], 'Altered retained answer.', 1),
            'title': text.replace('<title>', '<title>Unreviewed ', 1),
            'body': text.replace('</body>', '<p>Unreviewed visible text.</p></body>', 1),
            'noindex': text.replace('</head>', '<meta name="robots" content="noindex"></head>', 1),
            'link': re.sub(r'href="[^"]+"', 'href="/unreviewed-target/"', text, count=1),
            'canonical': re.sub(r'(<link rel="canonical" href=")[^"]+', r'\1https://example.invalid/', text, count=1),
            'date': re.sub(r'"dateModified"\s*:\s*"[^"]+"', '"dateModified": "2099-01-01"', text, count=1),
            'other schema': text.replace('"https://schema.org"', '"https://example.invalid"', 1),
            'invalid JSON': text.replace('"FAQPage"', 'FAQPage', 1),
            'line ending': text.replace('\n', '\r\n', 1),
            'reinserted target': text.replace('</head>', '<script type="application/ld+json">' + json.dumps({'@type': 'FAQPage', 'mainEntity': [TARGET]}) + '</script></head>', 1),
        }
        # Preserve monetary text on an actual cohort page containing a fee.
        for fee_route, fee_spec in SPECS.items():
            fee_text = (base / fee_route.strip('/') / 'index.html').read_bytes().decode()
            if re.search(r'\$\d[\d,]*', fee_text):
                changed = re.sub(r'\$\d[\d,]*', '$999,999', fee_text, count=1)
                assert changed != fee_text
                rejected(lambda: validate_page(changed, fee_spec, layer), layer + ' price')
                count += 1
                break
        for label, changed in cases.items():
            assert changed != text, 'Fixture did not mutate ' + label
            rejected(lambda: validate_page(changed, spec, layer), layer + ' ' + label)
            count += 1
        for valid_route, valid_spec in VALID_USES.items():
            valid = (base / valid_route.strip('/') / 'index.html').read_bytes().decode()
            changed = valid.replace(ANSWER, 'Changed legitimate answer.', 1)
            assert changed != valid
            rejected(lambda: validate_page(changed, valid_spec, layer, True), 'legitimate visible use')
            count += 1
    bank_text = (root / 'seo_topics.py').read_bytes().decode()
    changed_bank = bank_text.replace(ANSWER, 'Changed bank answer.', 1)
    assert changed_bank != bank_text
    rejected(lambda: check_bank(changed_bank), 'valid audit bank changed')
    return count + 1


def check_bank(text):
    bank = audit_bank(text)
    assert (QUESTION, ANSWER) in bank
    assert structural_sha(bank) == AUDIT_BANK_SHA256


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', nargs='?', help='Fully built public directory')
    parser.add_argument('--baseline-dir', type=Path, help='Private source/public originals')
    args = parser.parse_args()
    output = Path(args.output).resolve() if args.output else None
    cohort = json.loads((ROOT / COHORT).read_bytes().decode())
    assert cohort == list(SPECS) and len(cohort) == len(set(cohort)) == 15
    assert all(isinstance(route, str) for route in cohort)
    assert not (ROOT / Path(COHORT).parent / 'pages.json').exists()
    check_bank((ROOT / 'seo_topics.py').read_bytes().decode())
    redirects = json.loads((ROOT / 'vercel.json').read_bytes().decode())['redirects']
    assert [r for r in redirects if r['source'] == DEFERRED] == [
        {'source': DEFERRED, 'destination': '/services/reasonable-compensation/', 'statusCode': 301}]
    assert DEFERRED not in json.loads((ROOT / 'discovery_review_holds.json').read_bytes().decode())
    assert DEFERRED not in json.loads((ROOT / 'content/reviewed-content-lastmod.json').read_bytes().decode())
    for layer, base in [('source', ROOT), ('staged', output)]:
        if base is None:
            continue
        for filename in base.glob('sitemap*.xml'):
            for loc in ET.parse(filename).iter():
                if loc.tag.endswith('loc') and loc.text:
                    assert loc.text.strip() != 'https://www.aetaxadvisors.com' + DEFERRED
        for route, spec in SPECS.items():
            rel = Path(route.strip('/')) / 'index.html'
            text = (base / rel).read_bytes().decode()
            validate_page(text, spec, layer)
            if args.baseline_dir:
                directory = 'baseline-source' if layer == 'source' else 'baseline-public'
                original = (args.baseline_dir / directory / rel).read_bytes().decode()
                assert remove_exact_orphan(original) == text, route + ': non-target bytes changed'
        for route, spec in VALID_USES.items():
            validate_page((base / route.strip('/') / 'index.html').read_bytes().decode(), spec, layer, True)
    count = negative_fixtures(ROOT, output)
    print('PASS: 15 exact source removals; 45 retained Q&A entries; all other bytes unchanged.')
    if output:
        print('PASS: exact staged-byte preservation after all current release normalizers.')
    print('PASS: valid audit bank and both visible uses, redirect, sitemap exclusion and technical-only cohort.')
    print(f'PASS: three removal-position fixtures and {count} negative mutation fixtures.')


if __name__ == '__main__':
    main()
