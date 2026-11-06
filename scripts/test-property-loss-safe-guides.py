#!/usr/bin/env python3
"""Validate reviewed rental-loss guides in source or a staged public directory.
No network calls, generators, external writes, or publication.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from fractions import Fraction
from decimal import Decimal
import re,json,html,hashlib,sys
REPO=Path(__file__).resolve().parents[1]
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else REPO
COHORT=json.loads((REPO/'content/property-loss-safe-guides-20261106.json').read_text())
PRESERVE={'real-estate-professional-status-reps/index.html': {'header': '8eef47e32c2b9958f8515c905cc0944c78e549be301de5ac5f50ca2f6a26c7ca', 'footer': 'aa83db1e1b87b94920072d063c0e85c35bd986e34cd2be9a0b8f86c2e245e138', 'related_reading': 'd359fd8537d1d89b17d8645fa7f4d5bbc87d121ba15ff10e3706f1e8bbf3b6ae', 'reported_examples': ['b0bcefa376c086f06ef973a648a1498c2f584f6d64893340c80dd845c2a3c2e6'], 'title': 'Real Estate Professional Status REPS | AE Tax Advisors', 'published': ['2024-11-25T00:00:00-04:00'], 'article_published': ['2024-11-25T00:00:00-04:00'], 'cta_tail': None, 'anchors': ['<a href="/case-studies/" class="nav-link">Case Studies</a>', '<a href="/pricing/" class="nav-link">Pricing</a>', '<a href="/discovery/" class="btn-cta nav-cta">Request a Consultation</a>', '<a href="/case-studies/physician-reps-qualification-cost-seg-combo/">Physician Real Estate Professional Status Qualification and Cost Segregation Combo</a>', '<a href="/case-studies/real-estate-agent-investment-portfolio/">Business Owner With Rental Properties Worked Example</a>', '<a href="/case-studies/professional-athlete-entity-setup-real-estate-offset/">Professional Athlete Entity Structure and Real Estate Income Offset Strategy</a>', '<a href="tel:+16316145762">(631) 614-5762</a>', '<a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a>', '<a href="/case-studies/">Case Studies</a>', '<a href="/pricing/">Pricing</a>', '<a href="/discovery/">Request a Consultation</a>', '<a href="/discovery/" class="btn-cta">Get Your Free Tax Assessment</a>']}, 'the-business-owners-guide-to-passive-loss-rules-and-real-estate-professional-status-reps/index.html': {'header': '8eef47e32c2b9958f8515c905cc0944c78e549be301de5ac5f50ca2f6a26c7ca', 'footer': 'aa83db1e1b87b94920072d063c0e85c35bd986e34cd2be9a0b8f86c2e245e138', 'related_reading': 'e9789184967aa81aabe7e8121590868511eac0f5f61060166c6d98bb1b0b45c5', 'reported_examples': [], 'title': 'The Business Owners Guide To Passive Loss (2026) | AE Tax Advisors', 'published': ['2025-06-28T00:00:00-04:00'], 'article_published': ['2025-06-28T00:00:00-04:00'], 'cta_tail': 'd067a05c4fe2eabe0d55e2877ccb25f91789e77205d42a1a9ca80f05ce43131f', 'anchors': ['<a href="/case-studies/" class="nav-link">Case Studies</a>', '<a href="/pricing/" class="nav-link">Pricing</a>', '<a href="/discovery/" class="btn-cta nav-cta">Request a Consultation</a>', '<a href="/discovery/" class="btn-cta">Schedule Your REPS Status Review</a>', '<a href="/discovery/" class="btn-cta">Schedule Your Free Tax Assessment</a>', '<a href="/case-studies/physician-reps-qualification-cost-seg-combo/">Physician Real Estate Professional Status Qualification and Cost Segregation Combo</a>', '<a href="tel:+16316145762">(631) 614-5762</a>', '<a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a>', '<a href="/case-studies/">Case Studies</a>', '<a href="/pricing/">Pricing</a>', '<a href="/discovery/">Request a Consultation</a>', '<a href="/discovery/" class="btn-cta">Get Your Free Tax Assessment</a>']}, 'material-participation-real-estate-documentation/index.html': {'header': '8eef47e32c2b9958f8515c905cc0944c78e549be301de5ac5f50ca2f6a26c7ca', 'footer': 'aa83db1e1b87b94920072d063c0e85c35bd986e34cd2be9a0b8f86c2e245e138', 'related_reading': 'e525589a42956c0cbaf8ce98e883ff78e33b54ce863eb66711bb47a009caa17e', 'reported_examples': [], 'title': 'Material Participation Real Estate | AE Tax Advisors', 'published': ['2024-08-13T00:00:00-04:00'], 'article_published': ['2024-08-13T00:00:00-04:00'], 'cta_tail': None, 'anchors': ['<a href="/case-studies/" class="nav-link">Case Studies</a>', '<a href="/pricing/" class="nav-link">Pricing</a>', '<a href="/discovery/" class="btn-cta nav-cta">Request a Consultation</a>', '<a href="tel:+16316145762">(631) 614-5762</a>', '<a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a>', '<a href="/case-studies/">Case Studies</a>', '<a href="/pricing/">Pricing</a>', '<a href="/discovery/">Request a Consultation</a>', '<a href="/discovery/" class="btn-cta">Get Your Free Tax Assessment</a>']}, 'short-term-rental-tax-loophole-offset-w2-income/index.html': {'header': '8eef47e32c2b9958f8515c905cc0944c78e549be301de5ac5f50ca2f6a26c7ca', 'footer': 'aa83db1e1b87b94920072d063c0e85c35bd986e34cd2be9a0b8f86c2e245e138', 'reported_examples': ['9c15e3425378086d2563117e0957fc817f6d0d211ba4c544a0a3c0e76848d81e'], 'title': 'Short Term Rental Tax Strategy for Business Owners (2026)', 'published': ['2024-08-24T00:00:00-04:00'], 'article_published': ['2024-08-24T00:00:00-04:00'], 'cta_tail': '9faa3d486eab2ebf0321cfe4950133e21f06e95e2a2b545c6dcb0fc9fe11472e', 'anchors': ['<a href="/case-studies/" class="nav-link">Case Studies</a>', '<a href="/pricing/" class="nav-link">Pricing</a>', '<a href="/discovery/" class="btn-cta nav-cta">Request a Consultation</a>', '<a href="/discovery/" class="btn-cta">Schedule Free Consultation</a>', '<a href="tel:+16316145762">(631) 614-5762</a>', '<a href="/how-much-does-a-tax-advisor-cost/">How Much Does a Tax Advisor Cost</a>', '<a href="/discovery/">Book a Call</a>', '<a href="tel:+16316145762">(631) 614-5762</a>', '<a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a>', '<a href="/case-studies/">Case Studies</a>', '<a href="/pricing/">Pricing</a>', '<a href="/discovery/">Request a Consultation</a>', '<a href="/discovery/" class="btn-cta">Get Your Free Tax Assessment</a>']}, 'short-term-rental-tax-planning-the-core-concepts-most-hosts-miss/index.html': {'header': '8eef47e32c2b9958f8515c905cc0944c78e549be301de5ac5f50ca2f6a26c7ca', 'footer': 'aa83db1e1b87b94920072d063c0e85c35bd986e34cd2be9a0b8f86c2e245e138', 'related_reading': '360b58226bab7572671254070e48117da6bc31fc610f810f82672fc1dedebb40', 'reported_examples': ['c0eb834d7c9b73015e3e0f8dacdb9802b0f9ad37dc5105294503c84bca200f28'], 'title': 'Short Term Rental Tax Planning The Core (2026) | AE Tax Advisors', 'published': ['2025-05-08T00:00:00-04:00'], 'article_published': ['2025-05-08T00:00:00-04:00'], 'cta_tail': None, 'anchors': ['<a href="/case-studies/" class="nav-link">Case Studies</a>', '<a href="/pricing/" class="nav-link">Pricing</a>', '<a href="/discovery/" class="btn-cta nav-cta">Request a Consultation</a>', '<a href="tel:+16316145762">(631) 614-5762</a>', '<a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a>', '<a href="/case-studies/">Case Studies</a>', '<a href="/pricing/">Pricing</a>', '<a href="/discovery/">Request a Consultation</a>', '<a href="/discovery/" class="btn-cta">Get Your Free Tax Assessment</a>']}}

def plain(s):return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',s))).strip()
def digest(s):return hashlib.sha256(s.encode()).hexdigest()
def need(s,words,label):
    for word in words:assert word in s,(label,'missing',word)
def objects(o):
    if isinstance(o,dict):
        yield o
        for v in o.values():yield from objects(v)
    elif isinstance(o,list):
        for v in o:yield from objects(v)
class Page(HTMLParser):
    def __init__(self):super().__init__();self.meta={};self.links=[];self.ids=[];self.h1=0;self.canonical=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='meta':self.meta[a.get('name',a.get('property',''))]=a.get('content','')
        if tag=='a':self.links.append(a.get('href',''))
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a.get('href'))

REPS='real-estate-professional-status-reps/index.html'
LONG='the-business-owners-guide-to-passive-loss-rules-and-real-estate-professional-status-reps/index.html'
DOC='material-participation-real-estate-documentation/index.html'
STR='short-term-rental-tax-loophole-offset-w2-income/index.html'
CORE='short-term-rental-tax-planning-the-core-concepts-most-hosts-miss/index.html'

# Validate operative prose separately from preserved historical-outcome paragraphs.
def semantic(s,path):
    body=re.search(r'<div class="post-content">(.*?)\n        </div>\n    </article>',s,re.S)[1]
    body=re.sub(r'<h2>(?:Real Application Example|Real Example:[^<]+)</h2>\s*<p>.*?</p>','',body,flags=re.S)
    t=plain(body)
    need(t,['material participation','basis','at-risk','Section 461(l)','personal'],path)
    for wrong in ['deduct unlimited losses','losses automatically deduct','without material participation requirement','REPS requires a grouping election','no one participates less','averaging across three years','Active participation in STR operations creates self-employment tax','over 60 percent of examined']:
        assert wrong not in t,(path,'reintroduced unsupported rule',wrong)
    if path in [REPS,LONG,CORE]:
        need(t,['more than 750 hours','exceed half','Exactly 750 hours or exactly half does not qualify','independently meet both REPS qualification tests','cannot combine their hours','1.469-9(g)'],path)
    if path in [REPS,LONG,DOC]:need(t,['Employment hours still count in total personal services','real property numerator','more-than-5% owner','Investor work','day-to-day','reasonable method','daily time reports are not mandatory'],path)
    if path in [REPS,LONG]:
        need(t,['optional','original return','material change in facts and circumstances','current net income','unrelated person','$25,000','$100,000','$150,000','modified adjusted gross income'],path)
    if path==REPS:
        need(t,['Exactly 750 hours across four properties would fail','does not create an unlimited write-off','does not automatically release prior suspended passive losses','$1.5 million','after excluding land','approximately $54,545'],path)
    elif path==LONG:
        need(t,['Cash distributions are not the measure of passive income','$200,000 of suspended passive losses','$40,000 of current net income','remaining $160,000','fully taxable disposition of the entire interest','basis increase allowed to the recipient'],path)
    elif path==DOC:
        need(t,['Test 1: More than 500 hours','Test 2: Substantially all participation','Test 3: More than 100 hours and no individual participates more','Test 4: Significant participation activities','Test 5: Five of the preceding ten years','Test 6: Personal service activity in three prior years','Test 7: Facts and circumstances','rental activities are not significant participation activities','Exactly 500 hours does not satisfy','Equality is permitted; exactly 100 hours fails','another person is compensated for managing','no such test exists','150 hours, equality is sufficient','151 hours, Test 3 fails'],path)
    elif path==STR:
        need(t,['seven days or less','30 days or less and significant personal services','tax year','210 customer-use days across 30','211 days across 30','about 7.03 days','not a three-year average','greater of 14 days or 10%','fewer than 15 days','disallows rental expense deductions','materially participate','not required','Self-Employment Tax','primarily for the occupant','taxable income before an otherwise allowable $120,000','If $800,000 instead represents business revenue'],path)
    elif path==CORE:
        need(t,['seven days or less','30 days or less with significant personal services','material participation still determines','appropriate economic unit','interests in rental real estate','not automatically included','lesser of net investment income','$200,000 for single','$250,000 for married','$125,000 for married filing separately','$50,000 and the tax is $1,900','Section 162','does not establish that exclusion','noncorporate lessor rules'],path)

redirects=json.loads((REPO/'vercel.json').read_text()).get('redirects',[])
holds=json.loads((REPO/'discovery_review_holds.json').read_text())

def validate(s,rec,links=True):
    path=rec['path'];old=PRESERVE[path];p=Page();p.feed(s)
    assert p.canonical==[rec['canonical']],(path,'canonical')
    assert urlsplit(rec['canonical']).path=='/'+path.removesuffix('index.html')
    assert urlsplit(rec['canonical']).netloc=='www.aetaxadvisors.com'
    assert p.h1==1 and len(p.ids)==len(set(p.ids)),(path,'headings/IDs')
    assert not any('noindex' in p.meta.get(k,'').lower() for k in ['robots','googlebot'])
    assert urlsplit(rec['canonical']).path not in holds
    assert not any(r.get('source','').rstrip('/')==urlsplit(rec['canonical']).path.rstrip('/') for r in redirects)
    assert re.search('<title>(.*?)</title>',s,re.S)[1]==old['title']
    assert re.findall(r'"datePublished"\s*:\s*"([^"]+)"',s)==old['published']
    assert re.findall(r'<meta property="article:published_time" content="([^"]+)"',s)==old['article_published']
    assert p.meta['description']==p.meta['og:description']==p.meta['twitter:description']==rec['description']
    assert p.meta['og:url']==rec['canonical']
    # Source must preserve exact navigation and footer. Production has separately reviewed footer normalization.
    if ROOT==REPO:
        for key,pattern in [('header',r'<header\b.*?</header>'),('footer',r'<footer\b.*?</footer>'),('related_reading',r'<section class="content-section related-reading".*?</section>')]:
            if key in old:assert digest(re.search(pattern,s,re.S)[0])==old[key],(path,key)
    examples=re.findall(r'<h2>(?:Real Application Example|Real Example:[^<]+)</h2>\s*<p>.*?</p>',s,re.S)
    assert [digest(x) for x in examples]==old['reported_examples'],(path,'reported outcome altered')
    # Reported examples are preserved as historical assertions, not verified outcomes.
    # Preserve reported-example content and its surrounding presentation.
    assert 'example-qualification-note' not in s,(path,'unexpected example commentary')
    for a in old['anchors']:
        expected=a
        if ROOT!=REPO and 'nav-cta' in a:expected=re.sub(r'>[^<]+</a>', '>Book a Call</a>', a)
        assert expected in s,(path,'pricing, contact, case, or CTA changed',expected)
    pairs={plain(q):plain(a) for q,a in re.findall(r'<div class="faq-item">\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>',s,re.S)}
    assert len(pairs)==rec['faq_count']==4
    count=0
    for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
        for o in objects(json.loads(block)):
            if 'dateModified' in o:assert o['dateModified']=='2026-11-06'
            if o.get('@type') in ['Article','BlogPosting']:assert o['description']==rec['description']
            if o.get('@type')=='FAQPage':
                for q in o['mainEntity']:
                    assert pairs.get(q['name'])==q['acceptedAnswer']['text'],(path,'FAQ/schema parity',q['name']);count+=1
    assert count==4
    source=re.search(r'<section id="property-loss-sources".*?</section>',s,re.S)[0]
    for src in rec['sources']:
        assert 'href="'+src['url']+'"' in source and html.escape(src['title']) in source
        assert urlsplit(src['url']).netloc in ['www.irs.gov','www.ecfr.gov']
    for internal in ['/workspace/','/tmp/','baseline-manifest','private handoff','scratch notes','integration-12h']:
        assert internal not in s,(path,'private audit leaked')
    if links:
        for href in p.links:
            u=urlsplit(href)
            if u.scheme or u.netloc or not u.path.startswith('/'):continue
            target=ROOT/unquote(u.path).lstrip('/')
            assert target.is_file() or (target/'index.html').is_file() or any(r.get('source','').rstrip('/')==u.path.rstrip('/') for r in redirects),(path,'missing route',href)
    semantic(s,path)
    return count

# Independent threshold functions; these are test oracles, not production calculators.
def reps(hours,other):return hours>750 and hours>other
def test3(hours,individual_hours):return hours>100 and all(hours>=v for v in individual_hours)
def test1(hours):return hours>500
def str7(days,periods):return Fraction(days,periods)<=7
def residence(personal,fairdays):return personal>max(Fraction(14),Fraction(fairdays,10))
def former_passive(carry,income):
    usable=min(carry,max(0,income));return usable,carry-usable
def niit(nii,magi,threshold):return min(max(Decimal(0),nii),max(Decimal(0),magi-threshold))*Decimal('.038')

assert not reps(750,749) and not reps(751,751) and reps(751,750)
assert not reps(965,2200) and reps(1200,800)
assert round(float(Fraction(965,3165))*100,1)==30.5
# Neither spouse's qualification failure is repaired by pooling their hours.
assert not reps(400,0) and not reps(400,0) and reps(800,0)
assert not test1(500) and test1(501)
assert not test3(100,[99]) and test3(150,[120,150]) and not test3(150,[151])
assert str7(210,30) and not str7(211,30)
assert round(float(Fraction(211,30)),2)==7.03
assert not residence(14,100) and residence(15,100)
assert not residence(20,200) and residence(21,200)
assert former_passive(200000,40000)==(40000,160000)
assert former_passive(200000,-500000)==(0,200000)
assert niit(Decimal(200000),Decimal(250000),Decimal(200000))==Decimal(1900)
assert niit(Decimal(200000),Decimal(200000),Decimal(200000))==0
assert round(Decimal(1500000)/Decimal('27.5'))==54545
assert 800000-120000==680000

assert len(COHORT['pages'])==5 and len({r['path'] for r in COHORT['pages']})==5
assert COHORT['review_date']=='2026-11-06'
pages={};faq=0
for rec in COHORT['pages']:
    s=(ROOT/rec['path']).read_text();pages[rec['path']]=s;faq+=validate(s,rec)
# Mutations must be rejected. They cover law, math, preservation, schema, and sources.
mutations=[
(REPS,'more than 750 hours','at least 750 hours'),
(REPS,'$29,600 federal tax','$30,000 federal tax'),
(REPS,'<h2>Real Application Example</h2>','<p class="example-qualification-note">Unexpected example commentary.</p><h2>Real Application Example</h2>'),
(LONG,'remaining $160,000','remaining $200,000'),
(DOC,'Equality is permitted; exactly 100 hours fails','Equality fails; exactly 100 hours passes'),
(DOC,'rental activities are not significant participation activities','rental activities are significant participation activities'),
(STR,'about 7.03 days','exactly seven days'),
(STR,'Section 461(l)','Section 999'),
(CORE,'$50,000 and the tax is $1,900','$200,000 and the tax is $7,600'),
(CORE,'not automatically included','always automatically included'),
(STR,'https://www.irs.gov/publications/p925','https://example.com/unsupported'),
]
recmap={r['path']:r for r in COHORT['pages']}
failed=0
for path,old,new in mutations:
    assert old in pages[path],(path,'invalid negative fixture',old)
    altered=pages[path].replace(old,new)
    try:validate(altered,recmap[path],False)
    except (AssertionError,TypeError,KeyError):failed+=1
    else:raise AssertionError(('negative fixture escaped',path,old))
# Schema-only corruption must fail while visible answer stays unchanged.
s=pages[DOC];s=s.replace('"text": "The alternatives are more than 500 hours;', '"text": "The alternatives are at least 500 hours;',1)
assert s!=pages[DOC]
try:validate(s,recmap[DOC],False)
except AssertionError:failed+=1
else:raise AssertionError('schema-only mutation escaped')
print(f'PASS: 5 property-loss guides; {faq} synchronized FAQs; independent threshold/math checks; {failed} rejected negative fixtures; preservation, sources, metadata, and links. Reported-example content and presentation are preserved.')
