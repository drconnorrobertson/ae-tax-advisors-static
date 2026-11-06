#!/usr/bin/env python3
"""Scoped rental-page source/staged, FAQ, math and preservation regression checks.

Use --root public for staged HTML. Optional --baseline points to pre-edit HTML.
Negative fixtures are in memory; no reports or private notes enter public output.
"""
import argparse,html,json,re,sys
from decimal import Decimal as D
from html.parser import HTMLParser
from pathlib import Path
from tax_review_build_normalization import normalize_baseline_html
REPO=Path(__file__).resolve().parents[1]
ROUTE='/rental-property-tax-planning/'
FILE=ROUTE.strip('/')+'/index.html'
URL='https://www.aetaxadvisors.com'+ROUTE
TITLE='Rental Property Tax Planning for Business Owners | AE Tax'
DESC='Plan rental losses, REPS eligibility, cost segregation and 1031 exchanges alongside business income. Know which deductions you can use and which records matter.'
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.tags=[];self.words=[];self.skip=0
 def handle_starttag(self,t,a):
  self.tags.append((t,dict(a)))
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip-=1
 def handle_data(self,x):
  if not self.skip:self.words.append(x)
def plain(s):
 p=Parser();p.feed(s);return ' '.join(' '.join(p.words).split())
def schemas(s):return [json.loads(v) for v in re.findall(r'<script\b[^>]*type=[\'"]application/ld\+json[\'"][^>]*>(.*?)</script>',s,re.S)]
def section(s,id):return re.search(r'<section\b[^>]*id="'+re.escape(id)+r'"[^>]*>.*?</section>',s,re.S)[0]
def pairs(s):return [(plain(q),plain(a)) for q,a in re.findall(r'<div class="faq-item">\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>',s,re.S)]
def math_errors(s):
 text=plain(s);errs=[]
 results=[(D(25000)-(D(130000)-D(100000))/2,D(10000)),(D(500000)-D(100000),D(400000)),(D(80000)/D(400000),D('.20')),(D(80000)/D(500000),D('.16')),(D(80000)*D('.32'),D(25600)),(D(30000)-D(12000),D(18000))]
 if any(a!=b for a,b in results):errs.append('arithmetic invariants')
 for x in ['$25,000 minus half of the $30,000 excess','$30,000 of supported allocated basis and $12,000 of accumulated depreciation','$18,000','$500,000 acquisition cost, with $100,000 allocated to land and $400,000 to depreciable assets','$80,000 of eligible short-lived assets','20% of the $400,000 depreciable basis and 16% of the total purchase price','$80,000 multiplied by 32% is $25,600','not the incremental benefit over regular depreciation','Suspended losses may produce no current-year reduction','assumed inputs, not typical results']:
  if x not in text:errs.append('math context '+x)
 return errs
REQUIRED={
'passive-activity-loss-rules':['Basis:','At risk:','Passive activity:','Excess business loss:','Section 461(l)','Personal use','14 days or 10%','Married-filing-separately','at least 10%','entire interest','unrelated person','does not automatically free prior-year'],
'real-estate-professional-status':['more than 750','more than half','one spouse must independently','spouses cannot combine','more than 5%','Investor research','no other individual participating more','basis, at-risk, personal-use, Section 461(l)','prior returns'],
'cost-segregation':['acquired and placed in service after January 19, 2025','ADS property is generally ineligible','No fixed percentage','not automatically an amended-return','depreciation already taken'],
'1031-exchanges':['45 days','earlier of 180 days','including extensions','Actual or constructive receipt','before the sale closes','unrestricted right','partially taxable exchange','carryover basis','U.S. real estate is not like-kind to foreign'],
'grouping-elections':['does not provide a universal','1.469-11(b)(3)(iv)','disclosure'],
'niit':['lesser of','trade-or-business','more than 500 hours','five of the preceding ten','$125,000'],
'record-keeping':['no general seven-year rule','worthless securities or bad-debt','personal-use','carryover-basis'],
'owner-planning-fit':['Reviewed November 6, 2026','written engagement','secure client portal','not a public booking form'],
'results-context':['reported outcomes, not forecasts','refund also reflects payments and credits']}
STALE=['allows unlimited deductions','There is no income limitation.','35% or more of a property','25% to 40%','near zero when applied correctly','Most landlords overpay their taxes by $10,000 to $50,000','fresh start election under Rev. Proc. 2010-13','savings typically exceed the cost by a factor of 10']
def errors(s):
 e=[];p=Parser();p.feed(s);v=plain(s)
 def check(ok,msg):
  if not ok:e.append(msg)
 check([a.get('href') for t,a in p.tags if t=='link' and a.get('rel')=='canonical']==[URL],'canonical')
 check(len(re.findall(r'<h1\b',s))==1,'H1 count')
 check(not any('noindex' in a.get('content','').lower() for t,a in p.tags if t=='meta' and a.get('name') in ['robots','googlebot']),'noindex')
 check(re.search(r'<title>(.*?)</title>',s,re.S)[1]==TITLE,'title')
 for key in ['description','og:description','twitter:description']:
  check([a.get('content') for t,a in p.tags if t=='meta' and (a.get('name')==key or a.get('property')==key)]==[DESC],'metadata '+key)
 for id,tokens in REQUIRED.items():
  try:txt=plain(section(s,id)).lower()
  except TypeError:e.append('missing section '+id);continue
  for token in tokens:check(token.lower() in txt,'missing '+id+': '+token)
 for token in STALE:check(token.lower() not in html.unescape(s).lower(),'stale '+token)
 try:ds=schemas(s)
 except Exception as ex:return e+['JSON-LD parse: '+str(ex)]
 fs=[d for d in ds if d.get('@type')=='FAQPage'];check(len(fs)==1,'FAQ count')
 if fs:
  sp=[(plain(x['name']),plain(x['acceptedAnswer']['text'])) for x in fs[0]['mainEntity']]
  check(len(sp)==12,'12 FAQ count');check(sp==pairs(s),'exact FAQ question/answer parity')
 art=[d for d in ds if d.get('@type')=='Article'];check(len(art)==1,'Article count')
 if art:
  check(art[0]['datePublished']=='2026-01-06','original publication')
  check(art[0]['dateModified']=='2026-11-06','modification date')
  check(art[0]['description']==DESC,'Article description')
  check(art[0]['headline']==plain(re.search(r'<h1[^>]*>(.*?)</h1>',s,re.S)[1]),'Article headline')
 for source in json.loads((REPO/'content/rental-planning-accuracy-20261106/sources.json').read_text())['sources']:
  # Publication 527 is source-supported, with evidence retained in sources, not forced into repetitive FAQ links.
  if 'p527' not in source['url']:check(source['url'] in s,'source link '+source['url'])
 check(any(t=='a' and a.get('href')=='/discovery/' for t,a in p.tags),'discovery CTA')
 return e+math_errors(s)
def preservation(old,new):
 e=[]
 for tag in ['header','footer']:
  pat=r'<'+tag+r'\b[^>]*>.*?</'+tag+'>'
  if re.findall(pat,old,re.S)!=re.findall(pat,new,re.S):e.append('preservation '+tag)
 if section(old,'client-results')!=section(new,'client-results'):e.append('reported actual results changed')
 if pairs(old)[10]!=pairs(new)[10]:e.append('pricing FAQ changed')
 os=schemas(old);ns=schemas(new)
 if [x for x in os if x.get('@type')=='Service']!=[x for x in ns if x.get('@type')=='Service']:e.append('Service scope/offers changed')
 for key in ['datePublished']:
  if [x[key] for x in os if key in x]!=[x[key] for x in ns if key in x]:e.append('publication changed')
 # All displayed prices in the advisory/service block must retain their amounts and units.
 for token in ['$7,800 annual advisory engagement','$2,500 per year','$1,500','$1,000']:
  if token not in plain(section(new,'why-ae-tax')):e.append('price removed '+token)
 return e

def main():
 a=argparse.ArgumentParser();a.add_argument('--root',default=str(REPO));a.add_argument('--baseline');a.add_argument('--negative-fixtures',action='store_true');args=a.parse_args();root=Path(args.root).resolve();s=(root/FILE).read_text();e=errors(s)
 baseline=Path(args.baseline).read_text() if args.baseline else None
 if baseline and root!=REPO:baseline=normalize_baseline_html(baseline,REPO,ROUTE)
 if baseline:e+=preservation(baseline,s)
 # Resolve all newly introduced local URLs. Historical unrelated links remain out of scope.
 for u in ['/discovery/','/1031-exchange-planning/','/str-vs-ltr-tax-treatment/','/blog/excess-business-loss-limitation-461l-2026/','/form-3115-cost-segregation/']:
  if not (root/u.strip('/')/'index.html').exists():e.append('new link missing '+u)
 delta=json.loads((REPO/'content/rental-planning-accuracy-20261106/metadata-discovery-delta.json').read_text())
 for item in delta['discovery_replacements']:
  text=(root/item['path']).read_text()
  for replacement in item['replacements']:
   if replacement['new'] not in text or replacement['old'] in text:e.append('discovery copy '+item['path'])
 if root!=REPO:
  source=(REPO/FILE).read_text()
  for sid in list(REQUIRED)+['depreciation','repairs-vs-improvements','self-rental-rules','client-results','why-ae-tax']:
   if plain(section(source,sid))!=plain(section(s,sid)):e.append('source/staged section drift '+sid)
  if pairs(source)!=pairs(s):e.append('source/staged FAQ drift')
  entries=[]
  for f in root.glob('sitemap*.xml'):
   for entry in re.findall(r'<url>.*?</url>',f.read_text(),re.S):
    if '<loc>'+URL+'</loc>' in entry:entries.append(entry)
  if not entries or any('<lastmod>2026-11-06</lastmod>' not in x for x in entries):e.append('sitemap membership/lastmod')
 checkpages=json.loads((REPO/'content/rental-planning-accuracy-20261106/pages.json').read_text())
 if checkpages!=[ROUTE]:e.append('plain pages array')
 neg=[]
 if args.negative_fixtures:
  fixes=[('unlimited body','A rental deduction and a current-year tax saving are different things.','REPS allows unlimited deductions.'),('bonus denominator','20% of the $400,000 depreciable basis','20% of the $500,000 purchase price'),('tax versus deduction','$25,600 of illustrative','$80,000 of illustrative'),('date cut-off','acquired and placed in service after January 19, 2025','eligible in every tax year'),('basis loss limit','<strong>Basis:</strong>','<strong>Investment:</strong>'),('at-risk limit','<strong>At risk:</strong>','<strong>Loan:</strong>'),('EBL limit','<strong>Excess business loss:</strong>','<strong>Other:</strong>'),('personal use','14 days or 10%','14 days'),('REPS spouse','one spouse must independently','spouses together may'),('employee threshold','more than 5% of the employer','any share of the employer'),('receipt','<strong>Actual or constructive receipt:</strong>','<strong>Proceeds:</strong>'),('exchange deadline','earlier of 180 days after transfer or the federal return due date, including extensions','180 days'),('NIIT trade business','trade-or-business conditions','status'),('NIIT lesser of','lesser of net investment income or MAGI','net investment income and MAGI'),('records','no general seven-year rule','a general seven-year rule'),('classification caveat','No fixed percentage','A fixed percentage'),('title',TITLE,'Generic Rental Tax Advice'),('publication','"datePublished": "2026-01-06"','"datePublished": "2026-11-06"'),('noindex','</head>','<meta name="robots" content="noindex"></head>'),('schema-only answer','"text": "Under the general depreciation system','"text": "Hidden extra answer. Under the general depreciation system'),('json syntax','"@type": "FAQPage",','"@type": "FAQPage" BROKEN,')]
  for label,old,new in fixes:
   assert old in s,label
   mutant=s.replace(old,new,1)
   if not errors(mutant):e.append('negative fixture escaped '+label)
   else:neg.append(label)
  if baseline:
   for label,old,new in [('actual results','$187,000','$188,000'),('pricing','<strong>$7,800</strong>','<strong>$7,900</strong>'),('header','<header>','<header data-mutated="true">'),('footer','<footer','<footer data-mutated="true"'),('Service offer','"price": "7800"','"price": "7900"')]:
    assert old in s,label
    if not preservation(baseline,s.replace(old,new,1)):e.append('negative fixture escaped '+label)
    else:neg.append(label)
 print(json.dumps({'root':str(root),'ok':not e,'errors':e,'FAQ_pairs':len(pairs(s)),'math_checks':6,'negative_fixtures_rejected':len(neg),'negative_fixture_names':neg},indent=2))
 sys.exit(bool(e))
if __name__=='__main__':main()
