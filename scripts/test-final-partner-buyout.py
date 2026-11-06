#!/usr/bin/env python3
"""Focused final-owner buyout content, FAQ, basis-math and preservation checks.

Run: python3 scripts/test-final-partner-buyout.py --check-discovery
Checks existing source and staged pages. No content is generated or modified.
Negative fixtures prove guards reject known regressions. This is not a full
production build, individual tax review or search-rich-result certification.
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse, hashlib, html, json, re

ROOT = Path(__file__).resolve().parents[1]
ROUTE = '/blog/buying-out-dental-medical-practice-partner-tax-review/'
URL = 'https://www.aetaxadvisors.com' + ROUTE
TITLE = 'Practice Partner Buyout Tax Review | AE Tax Advisors'
H1 = 'Buying Out a Practice Partner: Tax Review Before Agreement'
DESC = 'Buying out a dental or medical practice partner? Compare direct purchase, redemption and a final-owner LLC buyout, including basis and final-return records.'
DATE = '2026-11-06'
SOURCES = [
    'https://www.irs.gov/pub/irs-irbs/irb99-06.pdf',
    'https://www.irs.gov/publications/p541',
    'https://www.irs.gov/businesses/small-businesses-self-employed/single-member-limited-liability-companies',
    'https://www.irs.gov/businesses/partnerships/faqs-for-internal-revenue-code-irc-sec-754-election-and-revocation',
    'https://www.irs.gov/instructions/i1065',
]
GUIDES = ['/the-business-owners-guide-to-section-743b-basis-adjustments-after-partner-transfer/', '/blog/partnership-cash-redemption-734b-depreciation/']
CASE = '/case-studies/dental-practice-business-rental-tax-roadmap/'
PRESERVED = ['Start with the decision', 'Identify the payer and tax classification', 'Separate the purchase price from other payments', 'Model the practice after the partner leaves', 'Create a closing and first-year handoff', 'Discuss the advisory scope']
PINS = {'source': {'Start with the decision': 'f11f3d187070ab4fce098ffc94b3f09027dadeaceb94c902e5d34803f4ab2e13', 'Identify the payer and tax classification': '843a33416b4899d827c243425d51bb7382baf64279ab08137f59de8cdab794d2', 'Separate the purchase price from other payments': 'c907cd531ae686ed49d94336c561dcfebadaa5995257962e03bf016c0fc1d796', 'Model the practice after the partner leaves': 'bd1f0a384688211efb1bd0fa18d584fef6a45fe4439138bc5270fa4b4988dbf8', 'Create a closing and first-year handoff': '211730b4ef65c2fb7d1e1db0e9a91103da207c5bde93e402effcbcc503155c2c', 'Discuss the advisory scope': '1b0fd938f878c770f719c59792cab7ddfe52f1a664e337a5223c97a1359bf392', 'header': '8eef47e32c2b9958f8515c905cc0944c78e549be301de5ac5f50ca2f6a26c7ca', 'footer': '812fdf80aaf4cc9d1dbab287d113cd6e705111053c13a4f8cd60489c818d202e'}, 'staged': {'Start with the decision': 'f11f3d187070ab4fce098ffc94b3f09027dadeaceb94c902e5d34803f4ab2e13', 'Identify the payer and tax classification': '843a33416b4899d827c243425d51bb7382baf64279ab08137f59de8cdab794d2', 'Separate the purchase price from other payments': 'c907cd531ae686ed49d94336c561dcfebadaa5995257962e03bf016c0fc1d796', 'Model the practice after the partner leaves': 'bd1f0a384688211efb1bd0fa18d584fef6a45fe4439138bc5270fa4b4988dbf8', 'Create a closing and first-year handoff': '211730b4ef65c2fb7d1e1db0e9a91103da207c5bde93e402effcbcc503155c2c', 'Discuss the advisory scope': '1b0fd938f878c770f719c59792cab7ddfe52f1a664e337a5223c97a1359bf392', 'header': '02195cba0bcd18d300b8369806b546cf36fb14e329dfcdd84f6d29f02d67bdd5', 'footer': 'e12a6d280bfceb5cd471df4d3d1ed23708118dd03d366f66c3dd6951dd060408'}}


def digest(s):
    return hashlib.sha256(s.encode()).hexdigest()


def text(s):
    return ' '.join(html.unescape(re.sub('<[^>]*>', ' ', s)).split())


def section(s, heading):
    match = re.search(r'<section\b[^>]*><div class="container narrow"><h2>' + re.escape(heading) + r'</h2>[\s\S]*?</div></section>', s)
    assert match, 'Missing section: ' + heading
    return match.group()


class Tags(HTMLParser):
    def __init__(self, s):
        super().__init__(); self.tags = []; self.ids = []; self.feed(s)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs); self.tags.append((tag, a))
        if 'id' in a: self.ids.append(a['id'])


def check(s, variant, root):
    tags = Tags(s)
    assert len(tags.ids) == len(set(tags.ids)), 'Duplicate IDs'
    assert s.count('<main>') == s.count('</main>') == 1, 'Main structure'
    assert len(re.findall(r'<section\b', s)) == s.count('</section>'), 'Section structure'
    assert re.findall('<title>(.*?)</title>', s) == [TITLE], 'Title drift'
    assert re.findall('<h1>(.*?)</h1>', s) == [H1], 'H1 drift'
    canonical = [a['href'] for t,a in tags.tags if t == 'link' and a.get('rel') == 'canonical']
    assert canonical == [URL], 'Canonical drift'
    meta = {a.get('name', a.get('property')): a.get('content') for t,a in tags.tags if t == 'meta'}
    for key in ['description', 'og:description', 'twitter:description']: assert meta[key] == DESC, 'Description parity: ' + key
    assert meta['article:published_time'] == '2026-10-24T12:00:00-04:00', 'Publication timestamp drift'
    assert meta['article:modified_time'].startswith(DATE), 'Modified date'
    assert 'noindex' not in meta['robots'], 'Accidental noindex'
    assert '<p class="subtitle">' + DESC + '</p>' in s, 'Visible description parity'
    assert 'Updated November 6, 2026' in s, 'Visible modified date'
    docs = [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)]
    assert len(docs) == 1 and isinstance(docs[0], list), 'Schema shape'
    docs = docs[0]
    assert [x['@type'] for x in docs] == ['Article','BreadcrumbList','FAQPage'], 'Schema types'
    article = docs[0]
    assert article['datePublished'] == '2026-10-24', 'Schema publication date drift'
    assert article['dateModified'] == DATE and article['description'] == DESC, 'Article metadata parity'
    assert article['url'] == article['mainEntityOfPage'] == URL, 'Article URL'
    for url in SOURCES:
        assert url in article['citation'] and 'href="' + url + '"' in s, 'Missing visible/schema official source: ' + url
    faq = section(s, 'Questions owners ask')
    visible = [(text(q),text(a)) for q,a in re.findall('<h3>(.*?)</h3><p>(.*?)</p>',faq,re.S)]
    structured = [(x['name'],x['acceptedAnswer']['text']) for x in docs[2]['mainEntity']]
    assert len(visible) == 5 and visible == structured, 'FAQ visible/schema mismatch'
    assert len(set(q for q,a in visible)) == 5, 'Duplicate FAQ'
    body = text(re.search('<main>(.*?)</main>',s,re.S).group(1))
    for required in [
        'Direct purchase with a continuing partnership:', 'when at least two tax owners remain',
        'Redemption paid by the partnership:', 'Section 734(b)', 'mandatory-adjustment rule',
        'Direct purchase leaving one owner:', 'A corporation or an LLC taxed as a corporation does not follow',
        'Revenue Ruling 99-6, Situation 1 (printed pages 6–7)', 'The seller reports a sale of a partnership interest.',
        'deemed to distribute its assets in liquidation to both members',
        'Section 731', 'basis under Section 732(b)', 'adjusted outside basis',
        'distribution basis, not an automatic fair-market-value reset', 'cost basis under Section 1012',
        'The partnership’s holding period generally carries over', 'This portion has a new holding period.',
        'not a routine Section 743(b) adjustment inside a continuing partnership',
        'A Section 754 election is not what creates the purchased portion’s cost basis',
        'no debt and no unrealized receivables or substantially appreciated inventory for Section 751(b)',
        'cash-method patient receivables, equipment recapture, inventory, loan balances and guarantees',
        'Review Section 751 ordinary-income treatment for the seller',
        'do not assume the seller’s entire gain is capital gain',
        'Nor does a new cost basis establish an immediate equipment or bonus-depreciation deduction',
        'asset class, acquisition facts, related-party rules, placed-in-service timing',
        'hypothetical basis reconciliation, not a valuation, deduction or client savings result',
        'final Form 1065 and final Schedules K-1', 'short-period return and its filing or extension deadline',
        'Form 8308 reporting where applicable', 'An individual operating a practice generally uses Schedule C',
        'uses its own name and EIN', 'whether an EIN change is actually required',
        'A capital-account balance alone is not outside basis',
    ]: assert required in body, 'Missing tax boundary: ' + required
    m=re.search(r'Total opening asset basis is \$([\d,]+) \(\$([\d,]+) \+ \$([\d,]+)\), not \$([\d,]+)',body)
    assert m, 'Basis example missing'
    total,old,purchased,false_reset=[int(n.replace(',','')) for n in m.groups()]
    assert (old,purchased,total,false_reset)==(40000,100000,140000,200000), 'Basis example amounts'
    assert total==old+purchased and total!=false_reset, 'Basis arithmetic'
    assert {x.rstrip(',') for x in re.findall(r'\$[\d,]+',body)} == {'$40,000','$100,000','$140,000','$200,000','$7,800','$9,800'}, 'Unreviewed dollar amount'
    for heading in PRESERVED:
        assert digest(section(s,heading)) == PINS[variant][heading], 'Protected section changed: ' + heading
    for tag in ['header','footer']:
        chunk=re.search('<'+tag+r'\b[^>]*>[\s\S]*?</'+tag+'>',s).group()
        assert digest(chunk)==PINS[variant][tag], 'Protected navigation/footer changed'
    for route in GUIDES+[CASE]: assert 'href="'+route+'"' in s, 'Missing retained/related guide'
    for t,a in tags.tags:
        href=a.get('href','')
        if t=='a' and href.startswith('/') and not href.startswith('//'):
            dest=root/href.split('#')[0].lstrip('/')
            assert dest.is_file() or (dest/'index.html').is_file() or Path(str(dest)+'.html').is_file(), 'Broken internal link: ' + href
    assert not re.search(r'nth[\s._-]*degree|nthdegree|dan\s+nicholson',s,re.I), 'Excluded provider'
    assert 'ttlc.intuit.com' not in s, 'Qualitative source is not tax authority'


def discovery(root):
    for rel in ['scripts/blog-catalog.json','assets/blog-search-index.json','public/assets/blog-search-index.json']:
        records=[x for x in json.loads((root/rel).read_text()) if x['url']==ROUTE]
        assert len(records)==1 and records[0]['description']==DESC, 'Catalog description: ' + rel
        assert records[0]['date']=='2026-10-24' and records[0]['title']==H1, 'Catalog publication/title drift'
    for rel in ['blog/page/12/index.html','public/blog/page/12/index.html']:
        s=(root/rel).read_text();assert ROUTE in s and DESC in s, 'Archive copy: ' + rel
    for rel in ['sitemap.xml','public/sitemap.xml']:
        matches=[x for x in re.findall('<url>[\\s\\S]*?</url>',(root/rel).read_text()) if '<loc>'+URL+'</loc>' in x]
        assert len(matches)==1 and '<lastmod>'+DATE+'</lastmod>' in matches[0], 'Route sitemap date: ' + rel
    assert json.loads((root/'content/reviewed-content-lastmod.json').read_text())[ROUTE]==DATE, 'Reviewed date record'
    assert json.loads((root/'content/discovery-reviewed-copy-20261106.json').read_text())[ROUTE]=={'title':TITLE,'description':DESC}, 'Reviewed discovery record'


def main():
    p=argparse.ArgumentParser();p.add_argument('--check-discovery',action='store_true');p.add_argument('--site-root',type=Path,default=ROOT);args=p.parse_args();root=args.site_root.resolve()
    pages={k:(root/(('public/' if k=='staged' else '')+ROUTE.strip('/')+'/index.html')).read_text() for k in ['source','staged']}
    for variant,s in pages.items():check(s,variant,root/('public' if variant=='staged' else ''))
    assert re.search('<main>(.*?)</main>',pages['source'],re.S).group()==re.search('<main>(.*?)</main>',pages['staged'],re.S).group(), 'Source/staged main mismatch'
    mutations=[
        ('basis_math','$140,000 ($40,000 + $100,000)','$200,000 ($40,000 + $100,000)'),
        ('basis_law','basis under Section 732(b)','basis under Section 1012'),
        ('full_reset','distribution basis, not an automatic fair-market-value reset','an automatic fair-market-value reset'),
        ('hot_asset_caveat','no debt and no unrealized receivables or substantially appreciated inventory for Section 751(b)','all practice assets are simple capital assets'),
        ('bonus_guarantee','Nor does a new cost basis establish an immediate equipment or bonus-depreciation deduction','A new cost basis establishes an immediate bonus-depreciation deduction'),
        ('final_return','final Form 1065 and final Schedules K-1','no Form 1065 or K-1 is needed'),
        ('faq_schema','"name": "Is a practice buyout payment always deductible?"','"name": "Is everything deductible?"'),
        ('fee','$7,800','$7,900'),
        ('case_status','does not establish completed implementation or realized tax savings','establishes completed implementation and realized tax savings'),
        ('publication','"datePublished": "2026-10-24"','"datePublished": "2026-11-06"'),
        ('corporate_boundary','A corporation or an LLC taxed as a corporation does not follow','A corporation or an LLC taxed as a corporation follows'),
        ('broken_link',GUIDES[0],'/nonexistent-final-owner-guide/'),
    ]
    for name,old,new in mutations:
        assert old in pages['source'],'Invalid negative fixture: '+name
        try:check(pages['source'].replace(old,new), 'source', root)
        except AssertionError:pass
        else:raise AssertionError('Negative guard failed: '+name)
    if args.check_discovery:discovery(root)
    print(json.dumps({'pages_checked':2,'visible_and_structured_faqs_each':5,'basis_math':'40000 + 100000 = 140000, not 200000','protected_sections_per_variant':len(PRESERVED)+2,'negative_mutations_rejected':len(mutations),'discovery_checked':args.check_discovery,'errors':[]},indent=2))

if __name__=='__main__':main()
