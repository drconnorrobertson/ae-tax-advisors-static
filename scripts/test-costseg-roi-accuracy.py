#!/usr/bin/env python3
"""Focused source/staged guide checks with exact preservation and negative fixtures.
Run from any directory. --root public verifies release output; no files are written.
"""
import argparse,hashlib,html,json,re,sys
from decimal import Decimal as D
from html.parser import HTMLParser
from pathlib import Path
from tax_review_build_normalization import normalize_baseline_html
REPO=Path(__file__).resolve().parents[1]
DATA=REPO/'content/costseg-roi-accuracy-20261106'
ROUTE='/resources/cost-seg-roi-guide/'
FILE=ROUTE.strip('/')+'/index.html'
URL='https://www.aetaxadvisors.com'+ROUTE
DELTA=json.loads((DATA/'metadata-discovery-delta.json').read_text())
PRES=json.loads((DATA/'preservation.json').read_text())
TITLE=DELTA['metadata']['title'];DESC=DELTA['metadata']['description'];H1=DELTA['metadata']['h1']
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
def sha(s):return hashlib.sha256(s.encode()).hexdigest()
def section(s,id):
 m=re.search(r'<section\b[^>]*id="'+re.escape(id)+r'"[^>]*>.*?</section>',s,re.S)
 return m[0] if m else ''
def schemas(s):
 out=[]
 for b in re.findall(r'<script\b[^>]*type=[\'"]application/ld\+json[\'"][^>]*>(.*?)</script>',s,re.S):
  d=json.loads(b);out.extend(d if isinstance(d,list) else [d])
 return out
def pairs(s):return [(plain(q),plain(a)) for q,a in re.findall(r'<h3>(.*?)</h3>\s*<p>(.*?)</p>',section(s,'costseg-faq'),re.S)]
def stage_expected(s):
 s=normalize_baseline_html(s,REPO,ROUTE)
 # Existing cost-seg-routing.cjs rewrites these exact non-navigation CTA tags.
 # This explicit list does not exempt arbitrary link/text changes.
 for old in [
  '<a href="/discovery/" class="btn-cta">Discuss Your Property\'s Study Fit</a>',
  '<a href="/discovery/" class="btn-cta">Request a Consultation</a>',
  '<a href="/discovery/" class="btn-cta">Discuss Your Property and Study Scope</a>',
  '<a href="/discovery/">Request a Consultation</a>',
  '<a href="/discovery/" class="btn-cta">Get Your Free Tax Assessment</a>']:
  new=re.sub(r'>[^<]*</a>$','>Book a Cost Seg Discovery Call</a>',old.replace('href="/discovery/"','href="/cost-seg-discovery/"'))
  s=s.replace(old,new)
 return s
REQUIRED={
'consultation-prep':['public booking form','secure client portal'],
'study-basics':["asset's function, use and supporting facts",'structural components','depreciable basis, excluding land'],
'property-facts':['No property category guarantees','no universal purchase-price cutoff','An Airbnb listing or a short average stay alone does not establish a 39-year recovery period','27.5 years','39 years','ADS','separate from the Section 469'],
'roi-model':['$500,000 of depreciable basis after excluding land','$100,000 assigned to eligible components','assumed 20% of depreciable basis','not a typical reclassification percentage','constant 37% federal marginal rate','No state benefit is assumed','no-study deduction on those same components would be $2,500','not a MACRS rate','$3,000 fee is an example, not an AE quote','before implementation costs and any tax treatment of fees','fully suspended','may instead be $0','reduced depreciation in future years','discount rate','expected sale','Section 1245 or Section 1250','not net economic ROI'],
'deduction-usability':['deduction, not a dollar-for-dollar tax credit','Basis and at risk:','Passive activity:','Excess business loss:','Section 461(l)','Personal use:','State treatment:','suspended carryforward'],
'bonus-depreciation':['acquired and placed in service after January 19, 2025','written binding contracts','self-construction','ADS is generally ineligible','does not reset those dates','not the general acquisition','annual deductions are not generally equal'],
'form-3115':['may qualify','qualifying accounting-method change','negative Section 481(a)','generally taken in the year of change','not an automatic benefit','amended return or another correction route','duplicate-copy','subsequent modifications'],
'study-timing':['ready and available for use','permitted correction route','short holding period'],
'study-fees':['$45,000','15:1 gross tax-effect-to-study-fee ratio','not a net or lifetime return','separately priced'],
'audit-support':['IRS can still examine','challenge particular classifications or costs','not approval of a particular report','audit-support scope, exclusions'],
'buyer-checklist':['Closing statement','land allocation support','Depreciation schedules','suspended-loss schedules','Written deliverables:','Responsibilities:']}
STALE=['IRS-approved methodology','fully defensible','does not increase audit risk','follows those standards exactly','is not a red flag','every dollar reclassified','STR properties use a 39-year','immediate, dollar-for-dollar tax savings','Most cost segregation studies deliver','Typical Reclassification %','Typical ROI on Study Fee','Enter your email to receive','Email capture form placeholder','highest-returning investments','ROI overwhelmingly positive','the only way to know your exact']
def errors(s,staged=False):
 e=[];p=Parser();p.feed(s);v=plain(s)
 def ck(ok,msg):
  if not ok:e.append(msg)
 ck(len(re.findall(r'<h1\b',s))==1,'one H1')
 ck(plain(re.search(r'<h1\b[^>]*>(.*?)</h1>',s,re.S)[1])==H1,'H1 text')
 ck(plain(re.search(r'<title>(.*?)</title>',s,re.S)[1])==TITLE,'title')
 ck([a.get('href') for t,a in p.tags if t=='link' and a.get('rel')=='canonical']==[URL],'canonical')
 ck(not any(t=='meta' and a.get('name') in ['robots','googlebot'] and 'noindex' in a.get('content','').lower() for t,a in p.tags),'noindex')
 for key,val in [('description',DESC),('og:description',DESC),('og:title',TITLE),('og:url',URL)]:
  ck([a.get('content') for t,a in p.tags if t=='meta' and (a.get('name')==key or a.get('property')==key)]==[val],'metadata '+key)
 for id,tokens in REQUIRED.items():
  text=plain(section(s,id))
  for token in tokens:ck(token in text,'missing '+id+': '+token)
 for token in STALE:ck(token.lower() not in html.unescape(s).lower(),'stale '+token)
 for token in ['private substantiation','unsubstantiated experience','unsupported experience','verification pending']:
  ck(token not in v.lower(),'private flag public '+token)
 try:ds=schemas(s)
 except Exception as ex:return e+['JSON-LD parse '+str(ex)]
 fs=[d for d in ds if d.get('@type')=='FAQPage'];ck(len(fs)==1,'FAQ count')
 if fs:
  sp=[(plain(x['name']),plain(x['acceptedAnswer']['text'])) for x in fs[0]['mainEntity']]
  ck(len(sp)==6,'six FAQ pairs');ck(sp==pairs(s),'exact visible/schema FAQ parity')
 art=[d for d in ds if d.get('@type')=='Article'];ck(len(art)==1,'Article count')
 if art:
  for key,val in [('datePublished','2026-09-18'),('dateModified','2026-11-06'),('headline',H1),('description',DESC),('mainEntityOfPage',URL)]:ck(art[0].get(key)==val,'Article '+key)
 for item in json.loads((DATA/'sources.json').read_text())['sources']:ck(item['url'] in s,'missing citation '+item['url'])
 # Numeric output must agree with the page's explicit assumptions.
 rows=re.findall(r'<tr>.*?<td\b[^>]*>(.*?)</td>\s*</tr>',re.search(r'<table id="roi-example".*?</table>',s,re.S)[0],re.S)
 equations=[(D(100000),'×',D('.37'),D(37000)),(D(100000),'−',D(2500),D(97500)),(D(97500),'×',D('.37'),D(36075)),(D(36075),'−',D(3000),D(33075))]
 ck(len(rows)==4,'four arithmetic rows')
 for row,(a,op,b,c) in zip(rows,equations):
  text=plain(row);nums=re.findall(r'\$?([0-9][0-9,]*)(%)?',text)
  vals=[D(n.replace(',',''))/(100 if pc else 1) for n,pc in nums]
  ck(vals==[a,b,c] and op in text,'arithmetic row '+text)
  ck((a*b if op=='×' else a-b)==c,'arithmetic invariant')
 ck(D(100000)/D(500000)==D('.20'),'basis ratio invariant');ck(D(45000)/D(3000)==D(15),'fee ratio invariant')
 ck(PRES['fee_text'] in s,'exact advertised fees')
 ck(PRES['experience_paragraph'] in s,'exact $150,000 experience paragraph')
 ck(PRES['volume_sentence'] in s,'exact hundreds-of-studies sentence')
 for tag in ['header','footer']:
  m=re.search(r'<'+tag+r'\b.*?</'+tag+'>',s,re.S)
  ck(m and sha(m[0])==PRES[tag+('_staged_sha256' if staged else '_source_sha256')],'exact '+tag+' preservation')
 # The replacement card has one existing consultation link and no collection UI.
 card=section(s,'consultation-prep');c=Parser();c.feed(card)
 ck([a.get('href') for t,a in c.tags if t=='a']==['/cost-seg-discovery/' if staged else '/discovery/'],'consultation card destination')
 ck(not any(t in ['form','input','iframe'] for t,a in c.tags),'no new collection UI')
 return e

def main():
 a=argparse.ArgumentParser();a.add_argument('--root',default=str(REPO));a.add_argument('--baseline');a.add_argument('--negative-fixtures',action='store_true');args=a.parse_args();root=Path(args.root).resolve();staged=root!=REPO;s=(root/FILE).read_text();e=errors(s,staged)
 if args.baseline:
  base=Path(args.baseline).read_text()
  if sha(base)!=PRES['source_sha256']:e.append('baseline hash mismatch')
  norm=stage_expected(base) if staged else base
  for tag in ['header','footer']:
   if re.search(r'<'+tag+r'\b.*?</'+tag+'>',norm,re.S)[0]!=re.search(r'<'+tag+r'\b.*?</'+tag+'>',s,re.S)[0]:e.append('baseline exact '+tag)
 for u in ['/discovery/','/cost-seg-discovery/','/form-3115-cost-segregation/','/str-vs-ltr-tax-treatment/']:
  if not (root/u.strip('/')/'index.html').exists():e.append('missing local link '+u)
 for item in DELTA['discovery_replacements']:
  text=(root/item['path']).read_text()
  for replacement in item['replacements']:
   if replacement['new'] not in text or replacement['old'] in text:e.append('discovery '+item['path'])
 if json.loads((DATA/'pages.json').read_text())!=[ROUTE]:e.append('one-route pages manifest')
 if staged:
  expected=stage_expected((REPO/FILE).read_text())
  for sid in list(REQUIRED)+['costseg-faq']:
   if section(s,sid)!=section(expected,sid):e.append('exact source/staged section drift '+sid)
  urls=[]
  for f in root.glob('sitemap*.xml'):
   urls.extend(x for x in re.findall(r'<url>.*?</url>',f.read_text(),re.S) if '<loc>'+URL+'</loc>' in x)
  if not urls or any('<lastmod>2026-11-06</lastmod>' not in x for x in urls):e.append('reviewed sitemap membership/lastmod')
  if (root/'content/costseg-roi-accuracy-20261106').exists() or (root/'scripts/test-costseg-roi-accuracy.py').exists():e.append('private artifacts staged')
 rejected=[]
 if args.negative_fixtures:
  mutations=[('basis denominator','$500,000 of depreciable basis after excluding land','$500,000 purchase price including land'),('classification percentage','not a typical reclassification percentage','a typical reclassification percentage'),('no-study baseline','no-study deduction on those same components would be $2,500','no-study deduction would be $0'),('gross arithmetic','$100,000 × 37% = $37,000','$100,000 × 37% = $38,000'),('incremental arithmetic','$100,000 − $2,500 = $97,500','$100,000 − $2,500 = $100,000'),('incremental tax','$97,500 × 37% = $36,075','$97,500 × 37% = $37,000'),('after fee','$36,075 − $3,000 = $33,075','$36,075 − $3,000 = $36,075'),('state assumption','No state benefit is assumed','All states conform'),('suspended deduction','may instead be $0','will always be positive'),('sale limits','Section 1245 or Section 1250','tax-free sale'),('STR classification','An Airbnb listing or a short average stay alone does not establish a 39-year recovery period','All short-term rentals use 39 years'),('bonus date','acquired and placed in service after January 19, 2025','placed in service after July 4, 2025'),('Form3115 qualification','This is not an automatic benefit for every old property.','This is an automatic benefit for every old property.'),('basis limit','<strong>Basis and at risk:</strong>','<strong>Other:</strong>'),('audit promise','IRS can still examine','IRS cannot examine'),('phantom PDF','Start with the checklist below','Enter your email to receive'),('fee range','$2,500 to $7,500','$2,500 to $8,000'),('larger fee range','$7,500 to $15,000 or more','$7,500 to $14,000 or more'),('AE unit price','approximately $1 per square foot','approximately $2 per square foot'),('experience','$150,000','$151,000'),('study volume','has completed hundreds of cost segregation studies','has completed thousands of cost segregation studies'),('header','<header>','<header data-mutated="true">'),('footer','<footer class="ae-site-footer">','<footer class="ae-site-footer" data-mutated="true">'),('publication','"datePublished": "2026-09-18"','"datePublished": "2026-11-06"'),('hidden FAQ promise','"text": "There is no guaranteed','"text": "Guaranteed 10:1 returns. There is no guaranteed'),('broken schema','"@type": "FAQPage",','"@type": "FAQPage" BROKEN,'),('title',html.escape(TITLE),'Generic tax article'),('noindex','</head>','<meta name="robots" content="noindex"></head>')]
  destination='/cost-seg-discovery/' if staged else '/discovery/'
  mutations += [('new collection form','<h2>Turn This Guide into a Property Review</h2>','<h2>Turn This Guide into a Property Review</h2><form><input name="email"></form>'),('new collection destination','<p><a href="'+destination+'" class="btn-cta">','<p><a href="https://unapproved.example/collect" class="btn-cta">')]
  for label,old,new in mutations:
   if old not in s:e.append('invalid negative fixture '+label);continue
   if not errors(s.replace(old,new,1),staged):e.append('negative fixture escaped '+label)
   else:rejected.append(label)
 print(json.dumps({'root':str(root),'ok':not e,'errors':e,'FAQ_pairs':len(pairs(s)),'arithmetic_checks':6,'negative_fixtures_rejected':len(rejected),'negative_fixture_names':rejected},indent=2));sys.exit(bool(e))
if __name__=='__main__':main()
