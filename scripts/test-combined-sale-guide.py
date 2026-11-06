#!/usr/bin/env python3
"""Read-only content, calculation, FAQ, discovery and preservation checks.

Run with optional public output, --registered, and --baseline-dir pointing to
the private audit directory. Does not run generators, register or build.
"""
from pathlib import Path
from html.parser import HTMLParser
from decimal import Decimal
from urllib.parse import urlsplit
import argparse
import copy
import hashlib
import html
import json
import re
import runpy
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ROUTE = '/blog/selling-business-and-building-1031-exchange/'
REL = ROUTE.strip('/') + '/index.html'
MANIFEST = 'content/combined-sale-guide-20261106/registration.json'
SITE = 'https://www.aetaxadvisors.com'
DATE = '2026-11-06'
SCRIPT = re.compile(r'<script\b[^>]*type=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script>', re.S | re.I)
SECTIONS = ['direct-answer','ownership','allocation','closing','depreciation','cash-example','alternatives','prepare','questions','sources']
REQUIRED = [
    'The full combined price does not automatically qualify for Section 1031.',
    'Property held primarily for sale does not qualify.',
    'A buyer receiving asset treatment does not by itself establish exchange eligibility for the seller.',
    'Form 8594 is required for the part to which the exchange rules do not apply.',
    'A separately sold building alone does not automatically trigger Form 8594.',
    'within 45 days',
    'earlier of 180 days after transfer or the due date of the exchanger’s return, including extensions',
    'actually or constructively',
    'Section 1031 real-property eligibility and depreciation recapture are separate tests.',
    'Some Section 1245 property can qualify as real property under the exchange regulations.',
    'neither automatically disqualifies the property nor guarantees that all gain can be deferred',
    'Hypothetical illustration, not a valuation, tax computation or client result.',
    'Do not treat the $1,300,000 as both a replacement-property funding source and money available to the owner.',
    'A corporation’s sale proceeds are not automatically the shareholder’s spendable cash',
    'These are scope questions, not a representation that every service is included in one advisory engagement.',
]
BANNED = [
    'all sale proceeds are tax-free', 'all section 1245 assets are ineligible',
    'every llc interest sale is excluded', 'the qi guarantees the exchange',
    'cost segregation erases recapture', 'choose any allocation you want',
    'we guarantee tax savings', 'tax-free owner cash',
]


def text(value):
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', value)).split())


def main_html(value):
    matches = re.findall(r'<main\b[^>]*>.*?</main>', value, re.S)
    assert len(matches) == 1
    return matches[0]


def schema_nodes(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from schema_nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from schema_nodes(child)


class Tags(HTMLParser):
    def __init__(self, value):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.feed(value)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


def validate_page(value, spec):
    body = main_html(value)
    visible = text(re.sub(r'<script\b.*?</script>|<style\b.*?</style>', '', body, flags=re.S))
    tags = Tags(value).tags
    assert len(re.findall(r'<h1\b', value)) == 1
    assert text(re.search(r'<h1\b[^>]*>(.*?)</h1>', body, re.S)[1]) == spec['catalog']['title']
    assert [a['href'] for t,a in tags if t == 'link' and a.get('rel') == 'canonical'] == [SITE + ROUTE]
    assert not any('noindex' in a.get('content','').lower() for t,a in tags if t == 'meta' and a.get('name','').lower() in ['robots','googlebot'])
    for key in ['description','og:description','twitter:description']:
        assert [a.get('content') for t,a in tags if t == 'meta' and (a.get('name') == key or a.get('property') == key)] == [spec['catalog']['description']]
    for key in ['article:published_time','article:modified_time']:
        assert [a.get('content') for t,a in tags if t == 'meta' and a.get('property') == key] == [DATE]
    seo = spec['reviewed_discovery_copy'][ROUTE]['title']
    assert text(re.search(r'<title>(.*?)</title>', value, re.S)[1]) == seo
    for key in ['og:title','twitter:title']:
        assert [a.get('content') for t,a in tags if t == 'meta' and (a.get('name') == key or a.get('property') == key)] == [seo]
    assert [a.get('content') for t,a in tags if t == 'meta' and a.get('property') == 'og:url'] == [SITE + ROUTE]
    ids = [a['id'] for _,a in tags if 'id' in a]
    assert len(ids) == len(set(ids))
    assert all(x in ids for x in SECTIONS)
    for _,a in tags:
        if a.get('href','').startswith('#'):
            assert a['href'][1:] in ids, a['href']
    for phrase in REQUIRED:
        assert phrase in visible, 'Missing qualification: ' + phrase
    for phrase in BANNED:
        assert phrase not in visible.lower(), 'Unsupported promise: ' + phrase
    assert not re.search(r'nth\s*degree|nthdegreecpas|dan\s+nicholson',value,re.I)
    assert not any(x in value for x in ['SOC 2 Compliant','Licensed CPAs','IRS Enrolled Agents','As Featured In 45 Publications'])
    assert '<time datetime="'+DATE+'">November 6, 2026</time>' in body
    assert body.count('href="/discovery/"') >= 2
    assert '<a href="/pricing/">Published pricing and engagement scope</a>' in body
    assert '$7,800' not in body and '$9,800' not in body
    for source in spec['primary_sources']:
        assert 'href="'+source['url']+'"' in body
    nodes = list(schema_nodes([json.loads(m[1]) for m in SCRIPT.finditer(value)]))
    articles = [x for x in nodes if x.get('@type') in ['Article','BlogPosting']]
    assert len(articles) == 1
    article = articles[0]
    for key in ['datePublished','dateModified']:
        assert article[key] == DATE
    assert article['headline'] == spec['catalog']['title']
    assert article['description'] == spec['catalog']['description']
    assert article['url'] == article['mainEntityOfPage'] == SITE + ROUTE
    assert article['citation'] == [x['url'] for x in spec['primary_sources']]
    faqs = [x for x in nodes if x.get('@type') == 'FAQPage']
    assert len(faqs) == 1 and len(faqs[0]['mainEntity']) == 5
    visible_faqs = re.findall(r'<div class="faq-item"><h3>(.*?)</h3><p>(.*?)</p></div>',body,re.S)
    assert [(text(q),text(a)) for q,a in visible_faqs] == [(q['name'],q['acceptedAnswer']['text']) for q in faqs[0]['mainEntity']]
    cash = next(t for t in re.findall(r'<table\b.*?</table>',body,re.S) if '<caption>Illustrative closing funds, before tax analysis</caption>' in t)
    rows = re.findall(r'<tr>(.*?)</tr>',cash,re.S)[1:]
    amounts = [text(re.findall(r'<td>(.*?)</td>',row,re.S)[0]) for row in rows]
    assert amounts == ['$3,000,000','$2,000,000','$5,000,000','($600,000)','($100,000)','$1,300,000']
    assert Decimal(3000000) + Decimal(2000000) == Decimal(5000000)
    assert Decimal(2000000) - Decimal(600000) - Decimal(100000) == Decimal(1300000)
    for table in re.findall(r'<table\b.*?</table>',body,re.S):
        assert '<caption>' in table and 'scope="col"' in table and 'scope="row"' in table


def rejection(fn, label):
    try:
        fn()
    except (AssertionError, ValueError, KeyError, StopIteration):
        return
    raise AssertionError('Accepted forbidden mutation: ' + label)


def negative_fixtures(value, spec):
    count = 0
    for phrase in REQUIRED:
        assert html.escape(phrase) in value or phrase in value, phrase
        bad = value.replace(html.escape(phrase), 'Qualification removed', 1) if html.escape(phrase) in value else value.replace(phrase,'Qualification removed',1)
        rejection(lambda: validate_page(bad,spec),'missing '+phrase)
        count += 1
    for phrase in BANNED:
        bad = value.replace('</main>','<p>'+phrase+'</p></main>',1)
        rejection(lambda: validate_page(bad,spec),phrase)
        count += 1
    cases = {
        'changed math cell': value.replace('<td>$1,300,000</td>','<td>$1,400,000</td>',1),
        'wrong canonical': value.replace('rel="canonical"','rel="alternate"',1),
        'noindex': value.replace('content="index, follow','content="noindex, follow',1),
        'publication promotion': value.replace('"datePublished": "2026-11-06"','"datePublished": "2026-12-01"',1),
        'missing section': value.replace('id="closing"','id="closing-removed"',1),
        'wrong description': value.replace('name="description" content="','name="description" content="Changed ',1),
        'unsupported credential': value.replace('</main>','<p>SOC 2 Compliant</p></main>',1),
        'changed FAQ answer': value.replace('"acceptedAnswer": {"@type": "Answer", "text": "','"acceptedAnswer": {"@type": "Answer", "text": "Unmatched ',1),
        'missing visible FAQ': re.sub(r'<div class="faq-item">.*?</div>','',value,count=1,flags=re.S),
    }
    for label,bad in cases.items():
        assert bad != value,label
        rejection(lambda: validate_page(bad,spec),label)
        count += 1
    return count


def check_links(value, root):
    redirects = {x['source']:x['destination'] for x in json.loads((ROOT/'vercel.json').read_text()).get('redirects',[]) if not re.search(r'[:*()]',x['source'])}
    for tag,attrs in Tags(value).tags:
        href=attrs.get('href','')
        if tag != 'a' or not href.startswith('/') or href.startswith('//'):
            continue
        path=urlsplit(href).path
        seen=set()
        while path in redirects:
            assert path not in seen
            seen.add(path)
            target=urlsplit(redirects[path])
            if target.netloc and target.netloc != 'www.aetaxadvisors.com':
                path='';break
            path=target.path
        if path:
            assert any(p.is_file() for p in [root/path.strip('/')/'index.html',root/path.strip('/'),root/(path.strip('/')+'.html')]),href


def expected_inbound(original, item):
    assert original.count(item['anchor']) == 1
    addition = item['addition']
    replacement = item['anchor']+'\n'+addition if item['position']=='after' else addition+'\n'+item['anchor']
    return original.replace(item['anchor'],replacement,1)


def check_registration(spec, output):
    entries=json.loads((ROOT/'scripts/blog-catalog.json').read_text())
    assert [x for x in entries if x['url']==ROUTE]==[spec['catalog']]
    assert json.loads((ROOT/'content/reviewed-content-lastmod.json').read_text())[ROUTE]==DATE
    assert json.loads((ROOT/'content/discovery-reviewed-copy-20261106.json').read_text())[ROUTE]==spec['reviewed_discovery_copy'][ROUTE]
    assert json.loads((ROOT/'content/seo-refresh-20261106/pages.json').read_text()).count(ROUTE)==1
    for root in [ROOT]+([output] if output else []):
        for entry in spec['xml_sitemaps']:
            rows=[x for x in ET.parse(root/entry['file']).getroot() if x.findtext('{*}loc')==SITE+ROUTE]
            assert len(rows)==1 and rows[0].findtext('{*}lastmod')==DATE
        for path in ['llms.txt','llms.md','.well-known/llms.txt','llms-full.txt']:
            assert (root/path).read_text().count(SITE+ROUTE)==1,path
        assert (root/'sitemap/index.html').read_text().count('href="'+ROUTE+'"')==1
        index=json.loads((root/'assets/blog-search-index.json').read_text())
        assert [x for x in index if x['url']==ROUTE]==[spec['catalog']]
        assert 'href="'+ROUTE+'"' in (root/'blog/index.html').read_text()


def registration_fixtures():
    register=runpy.run_path(str(ROOT/'scripts/register-combined-sale-guide.py'))
    spec,missing=register['plans']()
    paths=['scripts/blog-catalog.json','content/reviewed-content-lastmod.json','content/discovery-reviewed-copy-20261106.json','content/seo-refresh-20261106/pages.json','sitemap.xml','sitemap-blog.xml','sitemap/index.html','llms.txt','llms.md','.well-known/llms.txt','llms-full.txt',MANIFEST]
    with tempfile.TemporaryDirectory(prefix='combined-sale-registration-') as temp:
        temp=Path(temp)
        for rel in paths:
            p=temp/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/rel).read_bytes())
        _,plan=register['plans'](temp)
        for rel,value in plan.items():(temp/rel).write_text(value)
        assert register['plans'](temp)[1]=={},'Registration not idempotent'
        # Unrelated additions from another writer survive each route-specific operation.
        path=temp/'content/reviewed-content-lastmod.json';data=json.loads(path.read_text());data['/concurrent-owner-guide/']='2026-11-06';del data[ROUTE];path.write_text(json.dumps(data))
        plan=register['plans'](temp)[1]
        assert json.loads(plan['content/reviewed-content-lastmod.json'])['/concurrent-owner-guide/']=='2026-11-06'
        data[ROUTE]='2099-01-01';path.write_text(json.dumps(data))
        rejection(lambda:register['plans'](temp),'conflicting date overwrite')
        data[ROUTE]=DATE;path.write_text(json.dumps(data))
        path=temp/'scripts/blog-catalog.json';data=json.loads(path.read_text());next(x for x in data if x['url']==ROUTE)['title']='Unapproved competing title';path.write_text(json.dumps(data))
        rejection(lambda:register['plans'](temp),'conflicting catalog overwrite')
    return 4


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output',nargs='?',type=Path)
    parser.add_argument('--baseline-dir',type=Path)
    parser.add_argument('--registered',action='store_true')
    args=parser.parse_args()
    output=args.output.resolve() if args.output else None
    spec=json.loads((ROOT/MANIFEST).read_text())
    assert spec['route']==ROUTE and spec['publication_date']==DATE
    source=(ROOT/REL).read_text()
    validate_page(source,spec);check_links(source,ROOT)
    negatives=negative_fixtures(source,spec)
    if output:
        staged=(output/REL).read_text();validate_page(staged,spec);check_links(staged,output)
        # This new page uses no transformed internal aliases or generated main content.
        assert main_html(staged)==main_html(source),'Unexpected staged article-body change'
        negatives+=negative_fixtures(staged,spec)
    for item in spec['inbound_links']:
        current=(ROOT/item['file']).read_text()
        assert current.count(item['addition'])==1
        if args.baseline_dir:
            for layer,base in [('source',ROOT),('public',output)]:
                if base is None:continue
                old=(args.baseline_dir/f'baseline-{layer}'/item['file']).read_text()
                assert expected_inbound(old,item)==(base/item['file']).read_text(),'Non-link bytes changed: '+item['file']
    if args.registered:check_registration(spec,output)
    fixtures=registration_fixtures()
    print(json.dumps({'pages_authored':1,'matching_faqs':5,'inbound_additions':3,'arithmetic_checks':2,'negative_fixtures':negatives,'registration_fixtures':fixtures,'source_and_staged':bool(output),'baseline_byte_preservation':bool(args.baseline_dir),'registered':args.registered,'errors':[]},indent=2))


if __name__=='__main__':main()
