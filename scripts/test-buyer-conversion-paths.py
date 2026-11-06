#!/usr/bin/env python3
"""Check the seven buyer-conversion repairs in source or staged output.

Usage: python3 scripts/test-buyer-conversion-paths.py [--root public]
Optional --baseline DIR checks exact source price/date/link/client preservation
against before copies retained outside the repository. No generator is run.
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse,ast,collections,html,json,re
P=argparse.ArgumentParser();P.add_argument('--root',default='.');P.add_argument('--baseline');args=P.parse_args()
POLICY=Path(__file__).resolve().parents[1]; ROOT=(POLICY/args.root).resolve();built=ROOT!=POLICY
ROUTES=json.loads((POLICY/'content/buyer-conversion-paths-20261106/routes.json').read_text())
EXPECTED=['/','/cost-segregation-second-opinion/','/business-owner-tax-planning/','/compare/best-tax-advisors-buying-business-commercial-building/','/pricing/','/real-estate-tax-strategy-business-owners/','/compare/best-cost-segregation-companies-owner-occupied-commercial/']
assert ROUTES==EXPECTED and not (POLICY/'content/buyer-conversion-paths-20261106/pages.json').exists()
def rel(route):return route.strip('/')+'/index.html' if route!='/' else 'index.html'
def plain(s):return ' '.join(html.unescape(re.sub('<[^>]*>',' ',s)).split())
def schemas(s):return [json.loads(t) for t in re.findall(r'<script\b[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S)]
def dates(s):return re.findall(r'"(?:datePublished|dateModified)"\s*:\s*"[^"]+"|<meta property="article:(?:published|modified)_time"[^>]*>',s)
def prices(s):return re.findall(r'\$\d[\d,.]*(?:[KMB]|\+)?',s)
def section(s):return re.search(r'<section class="services-overview fade-in-section">.*?</section>',s,re.S)[0]
def card_check(s):
    b=section(s); assert '<h2>Tax Planning Services</h2>' in b
    cards=re.findall(r'<a href="([^"]+)" class="service-card">(.*?)</a>',b,re.S)
    assert len(cards)==3
    assert [u for u,_ in cards]==['/real-estate-tax-strategy-business-owners/','/cost-segregation-study/','/services/']
    labels=[]
    for target,body in cards:
        assert (ROOT/rel(target)).is_file()
        assert '<h3>' in body and '<p>' in body
        assert not re.search(r'<(?:a|button|input)\b|tabindex|aria-hidden|hidden|onclick',body)
        assert 'style="color:var(--primary);"' in body
        labels.append(plain(re.search(r'<h3>(.*?)</h3>',body,re.S)[1]))
    assert len(set(labels))==3
    assert not re.search(r'free assessment|guaranteed|refund|\$|%|savings',b,re.I)
    return b
pages={route:(ROOT/rel(route)).read_text() for route in ROUTES}
for route,s in pages.items():
    canonical_route=route
    if built and route=='/business-owner-tax-planning/':
        canonical_route='/business-owner-small-business-tax/'
        redirects=json.loads((POLICY/'vercel.json').read_text())['redirects']
        assert any(r['source']==route and r['destination']==canonical_route and r.get('permanent') is True for r in redirects)
    assert re.findall(r'<link rel="canonical" href="([^"]+)"',s)==['https://www.aetaxadvisors.com'+canonical_route]
    assert len(re.findall(r'<h1\b',s))==1
    assert schemas(s)
    if built:
        source=(POLICY/rel(route)).read_text()
        assert dates(s)==dates(source)
        assert prices(s)==prices(source)
    if args.baseline:
        before=(Path(args.baseline)/rel(route)).read_text()
        assert dates(s)==dates(before)
        assert prices(s)==prices(before)
        # No removal of links; only new service/source links in source edits.
        if not built:
            old=collections.Counter(re.findall(r'href="([^"]+)"',before))
            new=collections.Counter(re.findall(r'href="([^"]+)"',s))
            assert not old-new,(route,old-new)
        # Preserve existing case-study/result blocks verbatim.
        for block in re.findall(r'<a\b[^>]*class="result-card"[^>]*>.*?</a>',before,re.S):assert block in s
        for block in re.findall(r'<p>[^<]*(?:client|anonymized)[^<]*</p>',before,re.S|re.I):assert block in s
card_check(pages['/'])
# Shared CSS already provides native links, keyboard focus, no-JS readability,
# and responsive one-column cards. Check new copy contrast numerically.
css=(ROOT/'assets/style.css').read_text()
assert re.search(r'a:focus-visible,.*?outline:\s*3px solid #8D6D32',css,re.S)
assert re.search(r'\.fade-in-section\s*{\s*opacity:\s*1;',css)
assert '.card-grid-3, .card-grid-2, .blog-index-grid, .steps-grid { grid-template-columns: 1fr; }' in css
assert 'padding: 32px;' in css
colors={k:v for k,v in re.findall(r'--(primary|dark|medium|white):\s*(#[0-9A-Fa-f]{6})',css)}
def lum(x):
    c=[int(x[i:i+2],16)/255 for i in (1,3,5)]
    c=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in c]
    return sum(a*b for a,b in zip(c,[.2126,.7152,.0722]))
def contrast(a,b):
    x,y=sorted([lum(a),lum(b)]);return (y+.05)/(x+.05)
for key in ['primary','dark','medium']:assert contrast(colors[key],colors['white'])>=4.5
assert contrast('#8D6D32',colors['white'])>=3
print('PASS: three named native-link cards, valid destinations, no nested controls, no-JS/responsive/focus CSS, text and focus contrast.')
second=pages[ROUTES[1]];header=re.search(r'<section class="page-header">.*?</section>',second,re.S)[0]
expected='<a href="/cost-seg-discovery/" class="btn-cta btn-lg">Book a Cost Seg Discovery Call</a>' if built else '<a href="/discovery/" class="btn-cta btn-lg">Book a Discovery Call</a>'
assert expected in header and 'Free Tax Assessment' not in header
copy=json.loads((POLICY/'scripts/shared-discovery-cta.json').read_text())['new_paragraph']
assert 'study or advisory' in copy and 'agreed written scope' in copy
assert not re.search(r'complimentary|free|30.minute|paid advisory engagement',copy,re.I)
for route in ROUTES[2:4]:
    s=pages[route];assert plain(copy) in plain(s)
    assert 'what applies to you, what it is worth' not in plain(s)
    assert '<a href="/discovery/" class="btn-cta btn-lg">Book a Call</a>' in s
assert plain(copy) in plain((POLICY/'site_template.py').read_text())
pricing=pages['/pricing/']; visible=re.search(r'<section[^>]*id="faq"[^>]*>.*?</section>',pricing,re.S)[0]
faqs={q['name']:q['acceptedAnswer']['text'] for d in schemas(pricing) if d.get('@type')=='FAQPage' for q in d['mainEntity']}
contact=(POLICY/'contact/index.html').read_text()
source_ast=ast.parse((POLICY/'seo_topics.py').read_text())
faq_bank=next(ast.literal_eval(n.value) for n in source_ast.body if isinstance(n,ast.AnnAssign) and getattr(n.target,'id',None)=='FAQS')
firm=dict(faq_bank['firm'])
for q in ['How quickly can strategies be implemented?','How is tax planning different from tax preparation?']:
    a=faqs[q];assert a==firm[q] and a in contact and a in visible
for bad in ['full year of documentation','nearly every meaningful strategy','can only reflect decisions that were made months earlier']:
    assert bad not in pricing and bad not in str(faq_bank['firm'])
r=pages['/real-estate-tax-strategy-business-owners/'];heading='Tax Planning for Business Owners With Rental Properties'
assert '<h1>'+heading+'</h1>' in r
assert next(d for d in schemas(r) if d.get('@type')=='Article')['headline']==heading
assert json.loads((POLICY/'scripts/search-intent-config.json').read_text())['real-estate-tax-strategy-business-owners/index.html']['h1']==heading
assert 'existing portfolio' in r and 'acquisition, refinance or sale' in r
assert 'Tax Planning for Business Owners Buying Rental Property' not in r
comparison=pages[ROUTES[-1]]
for phrase in ['Direct business ownership and a related landlord are different','federal tax classification','does not automatically make a net rental loss nonpassive','appropriate economic unit','Grouping does not remove the other loss limits','Separate the engineering deliverable from tax implementation','separately scoped correction or method-change work']:
    assert phrase in comparison
for target in ['/cost-segregation-owner-occupied-commercial/','/cost-segregation-study-cost-pricing/']:
    assert 'href="'+target+'"' in comparison and (ROOT/rel(target)).is_file()
for u in ['https://www.irs.gov/publications/p925','https://www.irs.gov/publications/p946','https://www.law.cornell.edu/cfr/text/26/1.469-2','https://www.law.cornell.edu/cfr/text/26/1.469-4']:
    assert 'href="'+u+'"' in comparison
# Negative fixtures must be rejected rather than passing the happy path only.
for wrong in [pages['/'].replace('/services/" class="service-card"','/missing/" class="service-card"'),pages['/'].replace('<h3>Cost Segregation Review</h3>',''),pages['/'].replace('Review study feasibility','Guaranteed refund. Review study feasibility'),pages['/'].replace('style="color:var(--primary);"','style="color:var(--accent);"')]:
    try:card_check(wrong)
    except AssertionError:pass
    else:raise AssertionError('Invalid card fixture was accepted')
print('PASS:',len(ROUTES),'routes; booking scope, source/visible/schema FAQ consistency, portfolio H1/overlay, ownership/implementation distinctions, prices/dates and negative fixtures.', 'Staged' if built else 'Source')
