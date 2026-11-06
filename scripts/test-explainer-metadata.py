#!/usr/bin/env python3
"""Validate metadata-only repairs without importing or running the page generator."""
from pathlib import Path
import ast
import hashlib
import html
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ROUTES = json.loads((ROOT/'content/explainer-metadata-20261106/routes.json').read_text())
BASE = json.loads((ROOT/'scripts/fixtures/explainer-metadata-preservation.json').read_text())
MANIFEST = json.loads((ROOT/'scripts/owner-learning-manifest.json').read_text())
sys.path.insert(0, str(ROOT/'scripts'))
from tax_movement_lessons import SERIES


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def mask_descriptions(text):
    text, count = re.subn(
        r'(<meta (?:name|property)="(?:description|og:description|twitter:description)" content=")[^"]*(">)',
        r'\1__DESCRIPTION__\2', text)
    assert count == 3, count
    def replace_article(match):
        obj = json.loads(match[2])
        if obj.get('@type') not in ('Article', 'BlogPosting'):
            return match[0]
        body, count = re.subn(r'("description"\s*:\s*)"(?:[^"\\]|\\.)*"',
                             r'\1"__DESCRIPTION__"', match[2])
        assert count == 1, count
        return match[1] + body + match[3]
    return re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)',
                  replace_article, text, flags=re.S)


# Only compile the pure helper. The generator's main() has wide publishing scope.
generator = (ROOT/'scripts/build_owner_learning.py').read_text()
tree = ast.parse(generator)
node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'complete_description')
ns = {'re': re}
exec(compile(ast.Module(body=[node], type_ignores=[]), '<description-helper>', 'exec'), ns)
complete = ns['complete_description']
assert complete('A short sentence.') == 'A short sentence.'
assert complete('One sentence. A second sentence. A third sentence.') == 'One sentence. A second sentence.'
assert complete('  One  sentence. \n A second sentence.  ') == 'One sentence. A second sentence.'
assert complete('This sentence exceeds the target but must remain complete.', 12) == 'This sentence exceeds the target but must remain complete.'
assert complete('A complete sentence. A second sentence does not fit.', 25) == 'A complete sentence.'
assert complete('A sentence without final punctuation', 9) == 'A sentence without final punctuation'
assert complete('The U.S. tax rules apply. Another sentence is here.', 25) == 'The U.S. tax rules apply.'
assert complete('A 2.5% figure is illustrative. Another sentence is here.', 29) == 'A 2.5% figure is illustrative.'
assert complete('Sec. 179 requires review. Another sentence is here.', 24) == 'Sec. 179 requires review.'
assert complete('') == ''
assert generator.count("answer[:155]") == 1  # Unrelated legacy FAQ path is unchanged.
assert "if educational:\n              desc=reviewed.get(path, complete_description(answer))" in generator
assert "else:\n              # Existing FAQ workflow is outside this explainer-only repair.\n              desc=answer[:155].rsplit(' ',1)[0]+'.'" in generator
assert "content/explainer-metadata-20261106/routes.json" in generator

lessons = [lesson for *_, items in SERIES for lesson in items]
posts = [post for post in MANIFEST if post['educational']]
assert len(ROUTES) == len(posts) == len(lessons) == 100
assert len({row['path'] for row in ROUTES}) == 100
assert set(BASE) == {row['path'] for row in ROUTES}
selected = reviewed = 0
for row, post, (_, answer, _) in zip(ROUTES, posts, lessons):
    assert set(row) == {'path', 'title', 'description'}, row
    route = row['path']
    before = BASE[route]
    assert route == post['path']
    assert row['title'] == post['title'] == before['original_title']
    assert route.startswith('/blog/how-tax-moves-') and route.endswith('/')
    desc = row['description']
    assert desc == post['desc'] and digest(desc) == before['description_sha256']
    assert 90 <= len(desc) <= 170 and desc.endswith('.') and not desc.endswith('..'), route
    assert not re.search(r'\b(?:a|an|the|and|or|but|with|of|from|to|for|under|because|while|necessarily)\.$', desc, re.I), route
    assert digest(answer) == before['source_answer_sha256'], 'Source changed; review description: ' + route
    if desc == complete(answer):
        selected += 1
        assert answer.startswith(desc)
        assert len(answer) == len(desc) or answer[len(desc)] == ' '
    else:
        reviewed += 1  # Locked to the exact editorially reviewed complete summary above.
    text = (ROOT/route.strip('/')/'index.html').read_text()
    assert '<p>' + html.escape(answer) + '</p>' in text
    assert digest(mask_descriptions(text)) == before['metadata_masked_sha256'], route
    # Every body byte is preserved, including fees, case/example labels, H1, SVG
    # title/description accessibility markup, citations, links and dates.
    assert digest(text[text.index('<body'):]) == before['body_sha256'], route
    assert len(re.findall(r'<title>.*?</title>', text[:text.index('</head>')], re.S)) == 1
    assert re.findall(r'<meta (?:name|property)="(?:description|og:description|twitter:description)" content="([^"]*)">', text) == [html.escape(desc, quote=True)] * 3
    schemas = [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S)]
    articles = [x for x in schemas if x.get('@type') in ('Article', 'BlogPosting')]
    assert len(articles) == 1 and articles[0]['description'] == desc
    assert articles[0]['headline'] == row['title']
    assert articles[0]['url'] == 'https://www.aetaxadvisors.com' + route
    assert re.findall(r'<link rel="canonical" href="([^"]+)"', text) == [articles[0]['url']]
    assert articles[0]['datePublished'] == articles[0]['dateModified'] == '2026-10-06'
    assert re.search(r'<svg\b[^>]+role="img"[^>]*>', text)
    assert re.search(r'<title id="[^"]+-title">', text), route
assert (selected, reviewed) == (79, 21), (selected, reviewed)
# No unrelated FAQ, title, category, URL or manifest field may change.
for post in MANIFEST:
    if post['educational']:
        post['desc'] = '__DESCRIPTION__'
assert digest(json.dumps(MANIFEST, sort_keys=True)) == 'fdcf95e1a606ce0683c0a63b8d5a5663eebe09c5e9341e4721f64eb1c19cb5c8'
print('PASS: 100 existing routes; 400 synchronized description fields; 79 complete excerpts and 21 reviewed summaries.')
print('PASS: all non-description HTML bytes, bodies, titles (including SVG), dates, URLs, fees, cases and other manifest fields preserved.')
print('PASS: ten sentence-boundary regression cases; generator inspected but never run.')

# Optional staged-output checks complement the exact source-byte checks above.
# Common release navigation/footer/runtime transformations are tested separately.
def verify_staged(text, row):
    expected = row['description']
    assert re.findall(r'<meta (?:name|property)="(?:description|og:description|twitter:description)" content="([^"]*)">', text) == [html.escape(expected, quote=True)] * 3
    schemas = [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S)]
    articles = [x for x in schemas if x.get('@type') in ('Article', 'BlogPosting')]
    assert len(articles) == 1 and articles[0]['description'] == expected
    assert articles[0]['headline'] == row['title']
    assert articles[0]['datePublished'] == articles[0]['dateModified'] == '2026-10-06'
    assert re.findall(r'<link rel="canonical" href="([^"]+)"', text) == ['https://www.aetaxadvisors.com' + row['path']]
    assert re.search(r'<svg\b[^>]+role="img"[^>]*>', text)
    assert re.search(r'<title id="[^"]+-title">', text)
if len(sys.argv) > 1:
    output = Path(sys.argv[1]).resolve()
    for row in ROUTES:
        verify_staged((output/row['path'].strip('/')/'index.html').read_text(), row)
    first = ROUTES[0]
    staged = (output/first['path'].strip('/')/'index.html').read_text()
    for broken in [staged.replace(html.escape(first['description'], quote=True), 'Wrong metadata', 1),
                   staged.replace('"datePublished": "2026-10-06"', '"datePublished": "2020-01-01"'),
                   staged.replace('href="https://www.aetaxadvisors.com' + first['path'] + '"', 'href="https://example.invalid/"', 1)]:
        assert broken != staged
        try:
            verify_staged(broken, first)
        except AssertionError:
            pass
        else:
            raise AssertionError('Invalid staged metadata was accepted')
    print('PASS staged descriptions, schema, dates, canonical/SVG preservation and three negative fixtures.')
