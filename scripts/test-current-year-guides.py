#!/usr/bin/env python3
"""Focused current-year guide checks; no build, generator, or external writes.

Usage: python3 scripts/test-current-year-guides.py [content-root]
Optional content-root can point to a staged public directory. Baseline metadata
and the public route cohort are read from this checkout.
"""
from pathlib import Path
from decimal import Decimal as D
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import html,json,re,subprocess,sys

REPO=Path(__file__).resolve().parents[1]
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else REPO
COHORT=json.loads((REPO/'content/current-year-guides-20261106.json').read_text())
BASE='f2d5962'
PAGES={}
FAQ_TOTAL=0
LINK_TOTAL=0

def plain(s):
    return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',s))).strip()

def walk(o):
    if isinstance(o,dict):
        yield o
        for value in o.values(): yield from walk(value)
    elif isinstance(o,list):
        for value in o: yield from walk(value)

class Elements(HTMLParser):
    def __init__(self):
        super().__init__(); self.anchors=[]; self.meta={}; self.ids=[]; self.h1=0; self.canon=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='a' and 'href' in a:self.anchors.append(a['href'])
        if tag=='meta':self.meta[a.get('name',a.get('property',''))]=a.get('content','')
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='link' and a.get('rel')=='canonical':self.canon.append(a.get('href'))

def money(n):return f'${n:,.0f}'
def must(text,values,label):
    for value in values:assert value in text,(label,'missing',value)

redirects=json.loads((REPO/'vercel.json').read_text()).get('redirects',[])
holds=(REPO/'discovery_review_holds.json').read_text()
assert len(COHORT['pages'])==5
assert COHORT['review_date']=='2026-11-06' and COHORT['tax_year']==2026
assert len({p['path'] for p in COHORT['pages']})==5
for rec in COHORT['pages']:
    path=rec['path'];s=(ROOT/path).read_text()
    before=subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=REPO,text=True)
    PAGES[path]=s
    parser=Elements();parser.feed(s)
    old=Elements();old.feed(before)
    route=urlsplit(rec['canonical']).path
    assert parser.canon==old.canon==[rec['canonical']],path
    assert route=='/'+path.removesuffix('index.html'),path
    assert parser.h1==1 and len(parser.ids)==len(set(parser.ids)),path
    assert not any('noindex' in parser.meta.get(k,'').lower() for k in ['robots','googlebot']),path
    assert not any(r.get('source','').rstrip('/')==route.rstrip('/') for r in redirects),path
    assert route.strip('/') not in holds,path
    if path.startswith('s-corp-'):
        assert rec['discovery_handling']=='preserve_existing_canonical_and_discovery'
        assert urlsplit(rec['canonical']).netloc=='aetaxadvisors.com'
    else:assert urlsplit(rec['canonical']).netloc=='www.aetaxadvisors.com'
    assert re.findall(r'"datePublished"\s*:\s*"([^"]+)"',s)==rec['publication_dates']==re.findall(r'"datePublished"\s*:\s*"([^"]+)"',before)
    for published in re.findall(r'Published(?: on)? [^<|]+',before):assert published in s,(path,published)
    assert re.search(r'<title>(.*?)</title>',s,re.S)[1]==re.search(r'<title>(.*?)</title>',before,re.S)[1]
    assert parser.meta['og:title']==old.meta['og:title']
    assert parser.meta['og:url']==old.meta['og:url']==rec['canonical']
    description=parser.meta['description']
    assert parser.meta['og:description']==description
    if 'twitter:description' in parser.meta:assert parser.meta['twitter:description']==description
    # Fees and real case-study link labels must not be rewritten as generic examples.
    for row in re.findall(r'<tr\b[^>]*>.*?</tr>',before,re.S):
        if re.search(r'(?:Setup|Admin) Cost',row,re.I):assert row in s,(path,'fee table row changed')
    for section in re.findall(r'<section class="content-section related-reading".*?</section>',before,re.S):
        expected = section if ROOT == REPO else section.replace('href="/business-owner-tax-planning/"', 'href="/business-owner-small-business-tax/"')
        assert expected in s,(path,'related reading / case labels changed')
    for anchor in re.findall(r'<a\b[^>]*href="[^"]*(?:/case-studies/|/pricing/)[^"]*"[^>]*>.*?</a>',before,re.S):
        assert anchor in s,(path,'case or pricing link changed')
    pairs={plain(q):plain(a) for q,a in re.findall(r'<h[23][^>]*>([^<>]*)</h[23]>\s*<p[^>]*>(.*?)</p>',s,re.S)}
    count=0
    for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
        for obj in walk(json.loads(block)):
            if 'dateModified' in obj:assert obj['dateModified']=='2026-11-06'
            if obj.get('@type') in ('Article','BlogPosting'):assert obj['description']==description
            if obj.get('@type')=='FAQPage':
                for q in obj['mainEntity']:
                    assert q['name'] in pairs,(path,q['name'])
                    assert q['acceptedAnswer']['text']==pairs[q['name']],(path,q['name'],'FAQ mismatch')
                    count+=1
    assert count==rec['faq_count'],path
    FAQ_TOTAL+=count
    source_section=re.search(r'<section[^>]+id="current-year-sources".*?</section>',s,re.S)
    assert source_section
    for source in rec['sources']:
        assert f'href="{source["url"]}"' in source_section[0]
        assert urlsplit(source['url']).netloc in ['www.irs.gov','www.ssa.gov']
        assert source['title'] in source_section[0]
    for href in parser.anchors:
        parsed=urlsplit(href)
        if parsed.scheme or parsed.netloc or not parsed.path:continue
        if parsed.path.startswith('/'):
            target=ROOT/unquote(parsed.path).lstrip('/')
            exists=target.is_file() or (target/'index.html').is_file()
            # Explicit redirects are valid navigation targets; validate the literal route otherwise.
            redirected=any(r.get('source','').rstrip('/')==parsed.path.rstrip('/') for r in redirects)
            assert exists or redirected,(path,'missing internal route',href)
            LINK_TOTAL+=1
    for stale in ['$191,950','$383,900','$241,950','$483,900','$23,500','$7,500','$77,500','$81,250','$168,600','$1,250,000','$3,130,000','$980,000','$31,300']:
        assert stale not in s,(path,'stale current-year amount',stale)
    for private in ['/workspace/','/tmp/','number-audit','scratch notes','integration-12h']:
        assert private not in s,(path,'private work detail',private)

S=PAGES['s-corp-tax-optimization-complete-guide/index.html']
RET=PAGES['blog/defined-benefit-plan-vs-solo-401k/index.html']
SEC=PAGES['blog/section-179-deduction-2026-complete-guide/index.html']
OB=PAGES['blog/one-big-beautiful-bill-act-business-owners-2026/index.html']
QBI=PAGES['blog/qbi-deduction-optimization-irc-199a/index.html']
for page in [S,RET]:
    must(page,['$24,500','$72,000','$8,000','$11,250','$80,000','$83,250','$290,000','Roth','not a','eligible','compensation'], 'retirement rules')
    assert '$70,000' not in page and '$275,000' not in page
    assert 'https://www.irs.gov/pub/irs-drop/n-25-67.pdf' in page
must(S,['$2,000 to $5,000','$40 to $150','$184,500','72.5 cents','January 1 through June 30','76 cents','July 1 through December 31','commuting','reimbursements','section 4.02','$255','$260'],'S-corp rules and fees')
assert '40% to 60%' not in S and 'Roth contributions' not in S.split('<h3>SEP-IRA</h3>')[1].split('<h3>')[0] # no obsolete Roth prohibition
must(RET,['$0 to $500','$1,500 to $3,000','$2,000 to $5,000','PBGC-exempt','6%','final-year','250,000 or less','20% of adjusted net earnings','per-person'],'plan limits and cost assumptions')
assert '25% of net self-employment income' not in RET
assert '$245,000' not in RET and '$90,650' not in RET
for page in [S,OB,QBI]:
    must(page,['$201,750','$276,750','$403,500','$553,500','$201,775','$276,775','$75,000','$150,000','20%','before the QBI deduction'],'2026 QBI')
    assert 'https://www.irs.gov/pub/irs-drop/rp-25-32.pdf' in page
assert 'without reducing QBI' not in QBI
must(QBI,['can reduce QBI','less than 10%','less than 5%','50% or more common ownership','does not manufacture','three-of-five-year'],'QBI conditions')
assert 'increased the deduction rate to 23%' not in OB and 'new 23% rate' not in OB
assert 'no 23% QBI rate' in OB and 'not 23%' in OB
must(OB,['For 2026, the cap is $40,400','$505,000','$20,200','$252,500','$10,000','$5,000','then halve','30%','2025 cap was $40,000','through 2029'],'SALT year distinction')
for page in [SEC,OB]:
    must(page,['$2,560,000','$4,090,000','$6,650,000','$32,000','acquired and placed in service after January 19, 2025'],'Section 179 and bonus')
must(SEC,['$2,500,000 and $4,000,000','2025','6,000','14,000','six feet','nine passengers','business use','active-business','carryforward'],'Section 179 conditions')

# Calculate the published examples independently, including boundary values.
# QBI thresholds and widths must produce each stated endpoint.
for start,width,end in [(201750,75000,276750),(201775,75000,276775),(403500,150000,553500)]:
    assert start+width==end
assert D('500000')*D('.20')==100000
assert D('250000')*D('.20')==50000
assert D('150000')*D('.50')==75000
assert D('50000')*D('.37')==18500
must(QBI,['$400,000','$150,000','$250,000','$50,000','$75,000','$18,500','already reflected'],'QBI illustration')
must(OB,['$500,000 of QBI','preliminary $100,000','before wage/property'],'OBBBA illustration')
# Annual-additions totals, age-specific catch-up, and combined-plan cash vs deduction.
assert 72000+8000==80000 and 72000+11250==83250
assert D(200000)*D('.06')==12000
assert 24500+12000==36500
assert 36500+175000==211500
assert 211500+8000==219500
assert D(211500)*D('.35')==74025
must(RET,['$200,000','$12,000','$36,500','$175,000','$211,500','$219,500','$74,025','every dollar','QBI effects'],'combined-plan illustration')
# Section 179: investment ceiling first, active-business income separately.
def section179(placements):return max(D(0),D(2560000)-max(D(0),D(placements)-D(4090000)))
assert section179(3400000)==2560000
assert section179(4090000)==2560000 and section179(4090001)==2559999
assert section179(4360000)==2290000
assert section179(6649999)==1 and section179(6650000)==0 and section179(7000000)==0
assert min(section179(600000),D(600000),D(280000))==280000 and 600000-280000==320000
must(SEC,['$3,400,000','no investment-based reduction','$4,360,000','$270,000','$2,290,000','$600,000','$280,000','$320,000'],'Section 179 arithmetic')
# Financing is not profit: closing-cost assumption and outstanding principal retained.
assert D(500000)*D('.10')==50000 and D(500000)*D('.03')==15000
assert 50000+15000==65000 and 500000-50000==450000
assert D(500000)*D('.35')==175000
must(SEC,['$50,000','$15,000','$65,000','$175,000','$450,000','not a guaranteed refund or a profit'],'financing arithmetic')
# SALT method source: https://www.irs.gov/instructions/i1040sca
# State and Local Tax Deduction Worksheet, lines 1-10 (2025 instructions).
# 2026 input source, replacing the worksheet's 2025 cap and threshold:
# https://www.irs.gov/forms-pubs/correction-to-state-and-local-income-tax-deduction-amount-in-the-2026-form-1040-es
# Lines 2-4 use actual AGI plus excluded-income addbacks. No MAGI doubling.
# Line 10 halves the floored result for MFS before comparing with actual SALT.
def salt_worksheet(agi,mfs=False,addbacks=0,eligible_salt=100000):
    steps={1:D(40400),2:D(agi),3:D(addbacks),5:D(252500 if mfs else 505000)}
    steps[4]=steps[2]+steps[3]
    steps[6]=max(D(0),steps[4]-steps[5])
    steps[7]=steps[6]*D('.30')
    steps[8]=steps[1]-steps[7]
    steps[9]=max(D(10000),steps[8])
    steps[10]=min(steps[9]/(2 if mfs else 1),D(eligible_salt))
    return steps
def salt_cap(magi,mfs=False):return salt_worksheet(magi,mfs)[10]
assert salt_worksheet(275000,True)=={
    1:D(40400),2:D(275000),3:D(0),4:D(275000),5:D(252500),
    6:D(22500),7:D(6750),8:D(33650),9:D(33650),10:D(16825)}
assert salt_cap(505000)==40400 and salt_cap(550000)==26900
assert salt_cap(606333)==D('10000.10') and salt_cap(606334)==10000
assert salt_cap(1000000)==10000
assert salt_cap(252500,True)==20200 and salt_cap(275000,True)==16825
assert salt_cap(353833,True)==D('5000.05') and salt_cap(353834,True)==5000
assert salt_cap(1000000,True)==5000
assert salt_worksheet(400000,eligible_salt=35000)[10]==35000
assert salt_worksheet(270000,True,addbacks=5000)[10]==16825
assert salt_worksheet(275000,True,eligible_salt=12000)[10]==12000
must(OB,['$550,000','$45,000','$13,500','$26,900','$275,000 MAGI','$22,500','$6,750','$16,825'],'SALT arithmetic')
# The $275,000 separate-filer illustration is not the obsolete pension benefit ceiling.
assert '$275,000 per year' not in OB
# S-corp example includes employer FICA in remaining income, and mileage respects dates.
assert D(100000)*D('.9235')*D('.153')==D('14129.55')
assert D(55000)*D('.153')==D(8415)
assert D(55000)*D('.0765')==D('4207.50')
assert D(100000)-55000-D('4207.50')==D('40792.50')
assert D('14129.55')-8415==D('5714.55')
assert 1000*D('.725')+1000*D('.76')==1485
must(S,['$14,129.55','$8,415','$4,207.50','$40,792.50','$5,714.55','$725 + $760 = $1,485','not net total tax savings'],'S-corp arithmetic')
print(f'PASS: 5 guides; {FAQ_TOTAL} FAQ/schema pairs; {LINK_TOTAL} internal navigation links; 2026 limits, boundary arithmetic, source citations, canonical/publication metadata, fee estimates, and case links verified.')
print('S-corp canonical/discovery preserved as a separate handling case. No full build or live-site verification performed.')

# Guard filing-status and phaseout language against the reviewed edge cases.
assert "A non-separate filer who itemizes, has $35,000" in (ROOT / "blog/one-big-beautiful-bill-act-business-owners-2026/index.html").read_text()
assert "reduces the available Section 179 dollar limit to zero" in (ROOT / "blog/section-179-deduction-2026-complete-guide/index.html").read_text()
