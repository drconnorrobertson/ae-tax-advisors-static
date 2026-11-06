#!/usr/bin/env python3
"""Guard eight schema-only buyer-page repairs, without generating site content.

Run after the full release: python3 scripts/test-buyer-faq-markup.py public
Add --baseline-dir PATH to prove the exact allowed source/staged deletions
against private baseline-source and baseline-public files. Baselines and audit
reports stay outside the repository. Whole-file pins include normal release
transforms, every displayed byte, fee/cadence, date, URL, and unrelated schema.
This is a content-parity guard, not a tax, pricing, or rich-result certification.
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse
import copy
import hashlib
import html
import json
import re
import unicodedata
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
COHORT = 'content/buyer-faq-markup-20261106/routes.json'
COMPARISON = '/compare/your-current-cpa-vs-ae-tax/'
HOTEL = '/cost-segregation-hotels/'
QUESTION = 'How long does the onboarding process take?'
FRAGMENT = ' Implementation begins immediately after.'
ANSWER = ('Most new clients are fully onboarded within two to three weeks. '
          'The process includes a discovery call, document collection of the '
          'last three years of returns and entity documents, the three-year '
          'lookback analysis, and delivery of a written tax plan with dollar '
          'estimates for each strategy.')
SCRIPT = re.compile(r'<script\b[^>]*\btype=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script\s*>', re.I | re.S)
SPECS = {'/tax-advisory-cost-roi/': {'removed_faq_sha256': '3c0c54c49e67bb89da70430a9b9399b8bc4488290756c978c0753877dc32d8e9',
                             'source_base_sha256': '9f1167b6e9477d9b70938ce7e660dae2c9c4ffa3731066853d424690c7c26426',
                             'source_sha256': 'f98706a88c09d6994e2ce936d3001c5e26c055cdc537320fee522d3872c2b7db',
                             'staged_base_sha256': '72799e97dd0114d4c8a27929014127b0b25674b159d2c1b61810cb9c549c1842',
                             'staged_sha256': '1f0598e71dbc213fec839c45c8ee91201fdbca7339e5590262f40d0e309d7ab9'},
 '/services/s-corp-election/': {'removed_faq_sha256': '3a6e531998e1cde30622dbadd995c0df96cc88d08713ae45bed7d3da7f3921c8',
                                'source_base_sha256': 'd3b06c684de7b788e422bbb1d34efa170fe85c64397d079ef31f508b9caa52a3',
                                'source_sha256': 'd7481d3520e9275ccdf7854a05ff8a0aa9ff6acacf0f8cfd997ca71d227d00d3',
                                'staged_base_sha256': 'fdd3cbeff9fcbba5f2eefe6b2c97362050f4b1c2bed81110dd9abbe0dc540cdb',
                                'staged_sha256': '709c406bbd11ace7424fdefcf2ce3b969ce3d4c116154ae73278ee8bb06fd2db'},
 '/for/ecommerce-sellers/': {'removed_faq_sha256': 'f6526b1fb568314fe8db72c36a094296d49f29802722d3473a49460bc93c55fd',
                             'source_base_sha256': '81e9f0f5019f9d5f8691b1c96ebb0597943d1ad60b2579383c20e05b4d3f3f0a',
                             'source_sha256': '70f2723060d00b4dcbc575899561b89ec4cc02b7d8fc1e0e7aa63f1d4d003c43',
                             'staged_base_sha256': 'e268b2762f6a40a8ccbab9d95289b91feb1ff22341ccb1d485ba516b2f862762',
                             'staged_sha256': '67b9b8718e353246734a5e04bc43e083e14370a167bbdba91f7783edbc9b2b73'},
 '/for/physicians-dentists/': {'removed_faq_sha256': 'de6cf9b8ea712c5e4a951fd1573c2509b6a50d6c87070900f076fc28ff00c6ff',
                               'source_base_sha256': '4efa5909e38b9acc5168e4f11d91b967c61afa9c3dad6533c7876eeb69d5e3ea',
                               'source_sha256': '9bb1f8835a37063b58d1231486f6d632a48f266f4c54ea593ac19b02d09bcd4d',
                               'staged_base_sha256': '82851bffbbe27cc8634124fb3ffec6f55a3a40c749cb7fe966a4acf1ce36e544',
                               'staged_sha256': 'c1d3ccb0cfbd234e429e12d9486d233a82bc90dabdf65d41e25fb47371804db2'},
 '/for/restaurant-owners/': {'removed_faq_sha256': '9dad9d81dc53e4a2f00aafa29fe7cb217879d6a4e40cad8b6422b5e410a4aa21',
                             'source_base_sha256': 'd064809221c87e951410494d2e7454ca91be9f684a0e793465ea79669cfcf017',
                             'source_sha256': '5a50a97f7b142d244213dbf26ad3d28fe48955a0b5477b7bb45164eb91151304',
                             'staged_base_sha256': '32a346ea7bc070eb74190d6a77864c3d069e52196ed438636da290ca352dc1b8',
                             'staged_sha256': '128880842572852e0939e4dc9a5408c4b0e52d175ec1f7ec3c5337543257f818'},
 '/resources/tax-deadline-calendar/': {'removed_faq_sha256': '59789507901a195bf17ae5bdcc7a00481fcdb6132da49f2b395e02fe5dfabbc7',
                                       'source_base_sha256': '8f1462bf3755905e7774ae66e39984415c556b86c77864d67d8a8c7d4754ab7f',
                                       'source_sha256': 'deaf36ef0d3b839834e07200ad3d63da7c4b53ef2ecc79ad7fa55274505c0fb8',
                                       'staged_base_sha256': '2e2e9290aaeeba5f7eaa1efd6361553afa399f025318bf2824a0217f0d90371b',
                                       'staged_sha256': '1c21acd8295da3cf80a296bc6400d01827cc5bd17ea4239c793dc8ffab965900'},
 '/cost-segregation-hotels/': {'removed_faq_sha256': '09de1d2c657627de0f88c1bcbdbfd59c23deb571d84aba606517adfee368a1f0',
                               'source_base_sha256': '17e2825b14d827a5f6a75ee8c06243bf9573568068211c5a8bc19d1ffa978884',
                               'source_sha256': 'bc5ee7409d67c9b1ce64b09b9101b6811168edcb177d3a84b5664f9b5164f08c',
                               'staged_base_sha256': '1dc3e4bf260b0ae9320fa88d120f9e9c2c998a26d2fdd6314eef25c5bd8013a9',
                               'staged_sha256': '21d03a40d27b95dabf5e353e9d0b3eeac4a2666f91e2696b42a6828d9549af80'},
 '/compare/your-current-cpa-vs-ae-tax/': {'source_base_sha256': '9ef57d4ede1cbcf90a255c3c1ffb6c89e9c62c4c426ba345610560065c6ff602',
                                          'source_sha256': '340ea52e84a788e2092eed85fb80b77ac1584ae4ad01022153ba3d06d770c73a',
                                          'staged_base_sha256': '19dbc746b287791145340f49d81b14ec7210ec890d68b58d3e7a2f2fbe1a9682',
                                          'staged_sha256': 'ce96356e630b6342055ec622e101b855b38ad6a5312e85e4fae6680c4efba144',
                                          'retained_faq_sha256': '19c8d622c7030a25dc7bed0219d48f697dfd2840b1042f1a7901b1fea6149c9f'}}
CONTROLS = {'/services/cost-segregation-hotels/': {'faq_sha256': '61c549abab6ebd591e2e716d6832bd147e1d62b865ed158334e548dac83dd888'},
 '/offer-in-compromise-irs/': {'faq_sha256': 'cd39354dbdd9a27f5a010a83f99ea4a0882065f5e2e8b5162204bcc663893874'},
 '/blog/offer-in-compromise-myths-reality/': {'faq_sha256': '9665ff5a2ef6a6de7a5235cc146b22a5d462955f2d7636f318bc2c6f5a2c5107'}}


def sha(value):
    return hashlib.sha256(value.encode() if isinstance(value, str) else value).hexdigest()


def structural_sha(value):
    return sha(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')))


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.excluded, self.parts = [], []

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


def normalize(text):
    for _ in range(3):
        text = html.unescape(text)
    text = unicodedata.normalize('NFKC', text).casefold()
    return ' '.join(re.sub(r'[^\w\s]', ' ', text).split())


def schemas(text):
    return [json.loads(m[1]) for m in SCRIPT.finditer(text)]


def faq_nodes(value):
    if isinstance(value, dict):
        types = value.get('@type', [])
        if types == 'FAQPage' or isinstance(types, list) and 'FAQPage' in types:
            yield value
        for child in value.values():
            yield from faq_nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from faq_nodes(child)


def remove_exact_faq(text, signature):
    """Oracle: remove one reviewed FAQ object, never serialize retained JSON.

    Standalone FAQ scripts are deleted as a whole. A top-level JSON array uses
    JSONDecoder boundaries and drops only the object plus one required comma.
    Other layouts, altered signatures, multiple FAQ objects, and a question
    already present in the body fail closed instead of guessing.
    """
    blocks = list(SCRIPT.finditer(text))
    objects = [json.loads(m[1]) for m in blocks]
    nodes = list(faq_nodes(objects))
    assert len(nodes) == 1, 'Missing or multiple FAQPage objects'
    target = nodes[0]
    assert structural_sha(target) == signature, 'Reviewed FAQ object changed'
    assert target['mainEntity'], 'Empty FAQ object'
    body = normalize(visible(text))
    for item in target['mainEntity']:
        assert normalize(item['name']) not in body, 'FAQ question is already displayed'
    candidates = [i for i, obj in enumerate(objects) if list(faq_nodes(obj))]
    assert len(candidates) == 1
    i = candidates[0]
    block, obj = blocks[i], objects[i]
    if isinstance(obj, dict):
        assert obj == target, 'Unsupported nested FAQ layout'
        # Include the removed script's own indentation, not a new blank line
        # containing trailing whitespace. No adjacent non-whitespace moves.
        start = text.rfind('\n', 0, block.start()) + 1
        if text[start:block.start()].strip():
            start = block.start()
        return text[:start] + text[block.end():]
    assert isinstance(obj, list) and len(obj) > 1
    n = [j for j, value in enumerate(obj) if value == target]
    assert len(n) == 1
    n = n[0]
    raw = block[1]
    start = len(raw) - len(raw.lstrip())
    assert raw[start] == '['
    array_start = pos = start + 1
    spans, commas = [], []
    decoder = json.JSONDecoder()
    while True:
        pos += len(raw[pos:]) - len(raw[pos:].lstrip())
        if raw[pos] == ']':
            break
        value, end = decoder.raw_decode(raw, pos)
        spans.append((pos, end, value))
        pos = end + len(raw[end:]) - len(raw[end:].lstrip())
        if raw[pos] == ',':
            commas.append(pos)
            pos += 1
        else:
            assert raw[pos] == ']'
            break
    assert [value for _, _, value in spans] == obj
    assert len(commas) == len(spans) - 1
    if n < len(spans) - 1:
        start = array_start if n == 0 else commas[n - 1] + 1
        end = commas[n] + 1
    else:
        start, end = commas[n - 1], spans[n][1]
    repaired = raw[:start] + raw[end:]
    expected = copy.deepcopy(obj)
    del expected[n]
    assert json.loads(repaired) == expected
    return text[:block.start(1)] + repaired + text[block.end(1):]


def remove_exact_commitment(text):
    nodes = list(faq_nodes(schemas(text)))
    assert len(nodes) == 1
    matches = [item for item in nodes[0]['mainEntity'] if item['name'] == QUESTION]
    assert len(matches) == 1
    assert matches[0]['acceptedAnswer']['text'] == ANSWER + FRAGMENT
    body = visible(text)
    assert QUESTION in body and ANSWER in body and FRAGMENT.strip() not in body
    assert text.count(FRAGMENT) == 1
    pos = text.index(FRAGMENT)
    assert any(m.start(1) <= pos < m.end(1) for m in SCRIPT.finditer(text))
    return text[:pos] + text[pos + len(FRAGMENT):]


def repair(text, route, spec):
    return (remove_exact_commitment(text) if route == COMPARISON
            else remove_exact_faq(text, spec['removed_faq_sha256']))


def validate_page(text, route, spec, layer):
    nodes = list(faq_nodes(schemas(text)))
    if route == COMPARISON:
        assert len(nodes) == 1
        assert structural_sha(nodes) == spec['retained_faq_sha256']
        matches = [item for item in nodes[0]['mainEntity'] if item['name'] == QUESTION]
        assert len(matches) == 1 and matches[0]['acceptedAnswer']['text'] == ANSWER
        assert QUESTION in visible(text) and ANSWER in visible(text)
        assert FRAGMENT.strip() not in text
        # Equivalent existing wording is intentionally retained, not rewritten.
        assert any(item['name'] == 'What is cost segregation and why does it matter?'
                   for item in nodes[0]['mainEntity'])
        assert 'What is cost segregation and why should I care?' in visible(text)
    else:
        assert not nodes, 'Unsupported FAQPage was regenerated'
    assert sha(text) == spec[layer + '_sha256'], 'Non-target page bytes changed'


def rejected(action, label):
    try:
        action()
    except (AssertionError, ValueError, KeyError, StopIteration):
        return
    raise AssertionError('Accepted forbidden mutation: ' + label)


def fixtures(output):
    target = {'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': 'Undisplayed question?',
         'acceptedAnswer': {'@type': 'Answer', 'text': 'Undisplayed answer.'}}]}
    other = {'@type': 'Article', 'headline': 'Preserve {braces}, commas and quotes: "x".'}
    def document(obj):
        return ('<html><head><title>Fixture</title><script type="application/ld+json">'
                + json.dumps(obj, indent=2) + '</script></head><body>Visible prose.</body></html>')
    signature = structural_sha(target)
    for pos in range(3):
        array = [copy.deepcopy(other), copy.deepcopy(other)]
        array.insert(pos, target)
        original = document(array)
        result = remove_exact_faq(original, signature)
        assert schemas(result) == [[other, other]]
        assert visible(original) == visible(result)
    assert schemas(remove_exact_faq(document(target), signature)) == []
    original = document([other, target])
    cases = {
        'modified FAQ question': original.replace('Undisplayed question?', 'Changed question?'),
        'modified FAQ answer': original.replace('Undisplayed answer.', 'Changed answer.'),
        'duplicate FAQ': document([target, target]),
        'visible question': original.replace('Visible prose.', 'Undisplayed question?'),
        'visible entity variant': original.replace('Visible prose.', 'UNDISPLAYED&#32;question?'),
        'nested FAQ': document({'@graph': [other, target]}),
        'wrong schema type': original.replace('FAQPage', 'WebPage'),
    }
    for label, changed in cases.items():
        rejected(lambda: remove_exact_faq(changed, signature), label)
    count = len(cases)
    for layer, base in [('source', ROOT), ('staged', output)]:
        if base is None:
            continue
        route = '/tax-advisory-cost-roi/'
        spec = SPECS[route]
        text = (base / route.strip('/') / 'index.html').read_bytes().decode()
        changes = {
            'visible body': text.replace('</body>', '<p>Unapproved content.</p></body>'),
            'title': text.replace('<title>', '<title>Changed ', 1),
            'canonical': re.sub(r'(<link rel="canonical" href=")[^"]+', r'\1https://example.invalid/', text, count=1),
            'link': re.sub(r'href="[^"]+"', 'href="/changed/"', text, count=1),
            'noindex': text.replace('</head>', '<meta name="robots" content="noindex"></head>'),
            'price': text.replace('$7,800', '$9,999', 1),
            'annual cadence': text.replace('annual fee', 'monthly fee', 1),
            'split-pay cadence': text.replace('at the midpoint', '30 days later', 1),
            'review date': re.sub(r'"dateModified"\s*:\s*"[^"]+"', '"dateModified": "2099-01-01"', text, count=1),
            'other schema': text.replace('"BreadcrumbList"', '"WebPage"', 1),
            'invalid JSON': text.replace('"BreadcrumbList"', 'BreadcrumbList', 1),
            'line ending': text.replace('\n', '\r\n', 1),
            'FAQ regeneration': text.replace('</head>', '<script type="application/ld+json">' + json.dumps(target) + '</script></head>'),
        }
        for label, changed in changes.items():
            assert changed != text, 'Non-mutating fixture: ' + label
            rejected(lambda: validate_page(changed, route, spec, layer), layer + ' ' + label)
        count += len(changes)
        route, spec = COMPARISON, SPECS[COMPARISON]
        text = (base / route.strip('/') / 'index.html').read_bytes().decode()
        for label, changed in {
            'returned commitment': text.replace(ANSWER, ANSWER + FRAGMENT, 1),
            'changed equivalent question': text.replace('why does it matter?', 'why should I care?', 1),
            'removed retained FAQ': text.replace('"FAQPage"', '"WebPage"', 1),
        }.items():
            assert changed != text
            rejected(lambda: validate_page(changed, route, spec, layer), label)
            count += 1
        hotel = (base / HOTEL.strip('/') / 'index.html').read_bytes().decode()
        changed = hotel.replace('href="https://www.aetaxadvisors.com/services/cost-segregation-hotels/"',
                                'href="https://www.aetaxadvisors.com/cost-segregation-hotels/"', 1)
        assert changed != hotel
        rejected(lambda: validate_page(changed, HOTEL, SPECS[HOTEL], layer), 'hotel promotion')
        count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', nargs='?', help='Fully built public directory')
    parser.add_argument('--baseline-dir', type=Path)
    args = parser.parse_args()
    output = Path(args.output).resolve() if args.output else None
    routes = json.loads((ROOT / COHORT).read_bytes())
    assert routes == list(SPECS) and len(routes) == len(set(routes)) == 8
    assert not (ROOT / Path(COHORT).parent / 'pages.json').exists(), 'Technical cohort must not promote review dates'
    for layer, base in [('source', ROOT), ('staged', output)]:
        if base is None:
            continue
        for route, spec in SPECS.items():
            rel = Path(route.strip('/')) / 'index.html'
            text = (base / rel).read_bytes().decode()
            validate_page(text, route, spec, layer)
            if args.baseline_dir:
                directory = 'baseline-source' if layer == 'source' else 'baseline-public'
                original = (args.baseline_dir / directory / rel).read_bytes().decode()
                assert sha(original) == spec[layer + '_base_sha256']
                assert repair(original, route, spec) == text, 'Non-target bytes changed: ' + route
                assert original[original.index('<body'): ] == text[text.index('<body'): ]
        for route, spec in CONTROLS.items():
            text = (base / route.strip('/') / 'index.html').read_bytes().decode()
            assert structural_sha(list(faq_nodes(schemas(text)))) == spec['faq_sha256']
        for file in base.glob('sitemap*.xml'):
            assert all(node.text != 'https://www.aetaxadvisors.com' + HOTEL
                       for node in ET.parse(file).iter() if node.tag.endswith('loc'))
    count = fixtures(output)
    print('PASS: seven exact FAQPage removals (22 Q&A pairs) and one exact schema-only sentence deletion.')
    print('PASS: source' + (' and staged' if output else '') + ' byte pins, retained FAQs, equivalent wording, hotel exclusion and technical-only cohort.')
    print(f'PASS: standalone/first/middle/last removal fixtures and {count} negative mutation fixtures.')


if __name__ == '__main__':
    main()
