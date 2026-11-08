#!/usr/bin/env python3
"""Focused sale-year and post-year-end retirement review. No files are changed."""
import argparse,html,json,re,sys
from pathlib import Path
from html.parser import HTMLParser
from decimal import Decimal as D
from tax_review_build_normalization import normalize_baseline_html
R=Path(__file__).resolve().parents[1]
HOST='https://www.aetaxadvisors.com'
S='/blog/retirement-plan-before-business-sale/'
Y='/blog/can-i-set-up-a-retirement-plan-after-year-end/'
DATES={S:'2026-09-26',Y:'2026-07-31'}
DESC={S:'Review sale-year compensation, retirement contributions, employee costs, plan sponsorship and funding deadlines before selling your business.',Y:'Compare SEP, 401(k), SIMPLE IRA and cash balance plan deadlines, including retroactive adoption, first-year deferrals and separate funding rules.'}
SOURCES={'/blog/retirement-plan-before-business-sale/': ['https://www.irs.gov/publications/p560', 'https://www.irs.gov/retirement-plans/issue-snapshot-deductibility-of-employer-contributions-to-a-401k-plan-made-after-the-end-of-the-tax-year', 'https://www.irs.gov/retirement-plans/retirement-plan-faqs-regarding-contributions-s-corporation', 'https://www.irs.gov/retirement-plans/plan-participant-employee/sep-contribution-limits-including-grandfathered-sarseps', 'https://www.irs.gov/retirement-plans/retirement-plans-faqs-regarding-seps', 'https://www.ecfr.gov/current/title-26/section-1.430(j)-1', 'https://www.irs.gov/retirement-plans/terminating-a-retirement-plan', 'https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-employer-merges-with-another-company'], '/blog/can-i-set-up-a-retirement-plan-after-year-end/': ['https://www.irs.gov/publications/p560', 'https://www.irs.gov/retirement-plans/issue-snapshot-deductibility-of-employer-contributions-to-a-401k-plan-made-after-the-end-of-the-tax-year', 'https://uscode.house.gov/us/usc/t26/s401/', 'https://www.irs.gov/retirement-plans/plan-participant-employee/sep-contribution-limits-including-grandfathered-sarseps', 'https://www.irs.gov/retirement-plans/retirement-plans-faqs-regarding-seps', 'https://www.irs.gov/retirement-plans/retirement-plan-faqs-regarding-contributions-s-corporation', 'https://www.ecfr.gov/current/title-26/section-1.430(j)-1', 'https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/meeting-your-fiduciary-responsibilities', 'https://www.irs.gov/retirement-plans/retirement-plans-faqs-regarding-simple-ira-plans', 'https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-401k-and-profit-sharing-plan-contribution-limits']}
REQUIRED={S:{
'The direct answer':['eligible compensation separately from sale proceeds','who will sponsor the plan','before signing or closing','large closing payment does not create'],
'Reconcile sale cash with eligible compensation':['two schedules','Form W-2 compensation','not shareholder distributions','pass-through income','net earnings from self-employment','Capital gain' .lower(),'ordinary-income sale components are not automatically','actual service provider','Do not backdate payroll','controlled-group rules'],
'Decide who sponsors the plan after closing':['Equity sale','Asset sale','seller may retain the plan','partial termination','successor-plan restrictions','business-sale plan termination guide'],
'Model three separate contribution decisions':['Employee elective deferrals','wages already paid','prompt deposit rules','Employer contributions','valid extension','Defined benefit or cash balance funding','actuarial valuation','continuing funding','extended tax return also extends'],
'Hypothetical $5 million sale: cash is not the limit':['not a client result','sells S corporation stock for $5 million','$200,000 × 25% = $50,000','$72,000','2026','$100,000','$25,000','$75,000','not a $75,000 tax saving','later taxation'],
'Put the closing and plan deadlines on one calendar':['Before signing','Before final payroll and closing','March 15, 2027','September 15','April 15, 2027','October 15','valid extension','8½ months','Earlier quarterly installments','does not move this deadline','Short tax years'],
'Records and questions for the review':['plan documents and amendments','Forms 5500','participant census','owner contributions','required staff contributions','termination fees','written comparison','secure process','public inquiry'],
},Y:{
'SEP IRA: adoption and employer funding after year-end':['valid extension','eligible employees','lesser of','25% of eligible compensation or $72,000','2026','20% rate','self-employment tax','before the owner','not simply multiply gross profit','$50,000','$40,000','not promised tax savings'],
'Solo 401(k): employer contributions are not salary deferrals':['adopted after year-end','prior-year employer contributions','actually pay','return due date','valid extension','before compensation is paid','An S corporation cannot','prior-year wages','existing plan','election generally must be made by year-end','Deposit timing is separate','including extensions','ERISA-covered','as soon as','not permission to hold'],
'The narrow first-year sole-proprietor exception':['after December 29, 2022','entire interest','unincorporated business','only employee','first plan year only','Adopt the plan, make the election and pay','without extensions','April 15, 2027, not October 15','does not cover an S corporation, a partnership','another employee','later year','spouse','provider'],
'Cash balance plans: adoption and actuarial funding are different':['not subject to a universal December 31','extended return due date','does not extend minimum funding','single-employer','Section 430','8½ months','September 15, 2027','Earlier quarterly installments','October 15','does not extend September','both rules','enrolled actuary','deductible range','PBGC','not an automatic contribution'],
'SIMPLE IRA: a separate October 1 rule':['not previously maintained','January 1 and October 1','new employer formed after October 1','as soon as administratively feasible','previously maintained','effective January 1','not ordinarily'],
'A deadline calendar for 2026 contributions':['calendar-year deadlines','short-year rules','provider cutoff','does not extend the time to pay','During 2026','October 1, 2026','March 15, 2027','September 15, 2027','April 15, 2027','October 15, 2027','does not get that extension','earlier installments'],
'Check compensation, employees and cost before opening an account':['eligible W-2 compensation, not shareholder distributions','not automatically eligible compensation','$24,500','$72,000','100% of compensation','ceilings, not a promise','related-business aggregation','Roth requirements','owner and staff funding','Retroactive adoption is not blanket permission','secure process'],
}}
STALE=['The Solo 401(k) must be established by December 31','You cannot set up a Solo 401(k) in February','This is a firm deadline with no extension','employee deferral portion must be contributed by December 31','Defined Benefit Plan (Cash Balance Plan), Year-End Deadline','generally must be established by the last day of the tax year','up to $70,000 for 2026','almost always paired','roughly $72,000','well beyond $250,000']
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.words=[];self.tags=[];self.skip=0
 def handle_starttag(self,t,a):
  self.tags.append((t,dict(a)))
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip-=1
 def handle_data(self,d):
  if not self.skip:self.words.append(d)
def plain(s):p=Parser();p.feed(s);return ' '.join(' '.join(p.words).split())
def schemas(s):return [json.loads(d) for d in re.findall(r'<script type="application/ld\+json">\s*(.*?)</script>',s,re.S)]
def article(s):return next(d for d in schemas(s) if d.get('@type') in ['Article','BlogPosting'])
def main(s):return re.search(r'<main\b[^>]*>.*?</main>',s,re.S)[0]
def body(s,r):
 if r==S:return re.search(r'<section[^>]* id="retirement-sale-review"><div class="container narrow">(.*?)</div></section>',s,re.S)[1]
 return re.search(r'<!-- retirement-deadline-review:start -->(.*?)<!-- retirement-deadline-review:end -->',s,re.S)[1]
def sections(s,r):return {plain(h):plain(b) for h,b in re.findall(r'<h2[^>]*>(.*?)</h2>(.*?)(?=<h2\b|$)',body(s,r),re.S)}
def faq(s,r):
 b=re.search(r'<section[^>]* id="faq">(.*?)</section>',s,re.S)[1]
 pairs=[(plain(q),plain(a)) for q,a in re.findall(r'<h3[^>]*>(.*?)</h3>\s*<p>(.*?)</p>',b,re.S)]
 if r==Y:
  q,a=re.search(r'<!-- million-owner-answer:start -->.*?<h2[^>]*>(.*?)</h2><p>(.*?)</p>',s,re.S).groups();pairs.append((plain(q),plain(a)))
 return pairs

def page_errors(s,r):
 errors=[]
 def ck(ok,label):
  if not ok:errors.append(label)
 p=Parser();p.feed(s);parts=sections(s,r);doc=article(s)
 for heading,tokens in REQUIRED[r].items():
  ck(heading in parts,'missing section: '+heading)
  for token in tokens:ck(token in parts.get(heading,''),heading+': missing '+token)
 for token in STALE:ck(token.lower() not in html.unescape(s).lower(),'stale claim '+token)
 for key in ['description','og:description','twitter:description']:
  ck([a.get('content') for t,a in p.tags if t=='meta' and (a.get('name')==key or a.get('property')==key)]==[DESC[r]],'metadata '+key)
 ck(doc['description']==DESC[r],'Article description')
 ck(doc['datePublished']==DATES[r],'published date')
 ck(doc['dateModified']=='2026-11-06','modified date')
 ck(doc['mainEntityOfPage']['dateModified']=='2026-11-06','WebPage modified date')
 ck(doc['headline']==plain(re.search(r'<h1[^>]*>(.*?)</h1>',s,re.S)[1]),'headline parity')
 ck(len(re.findall(r'<h1\b',s))==1,'one H1')
 ck([a.get('href') for t,a in p.tags if t=='link' and a.get('rel')=='canonical']==[HOST+r],'canonical')
 ck(not any('noindex' in a.get('content','') for t,a in p.tags if t=='meta' and a.get('name') in ['robots','googlebot']),'indexability')
 ck('Reviewed November 6, 2026' in plain(main(s)),'visible review date')
 fq=[d for d in schemas(s) if d.get('@type')=='FAQPage'];ck(len(fq)==1,'one FAQ schema')
 if fq:
  pairs=[(plain(d['name']),plain(d['acceptedAnswer']['text'])) for d in fq[0]['mainEntity']]
  ck(pairs==faq(s,r),'exact visible FAQ parity');ck(len(pairs)==(4 if r==S else 6),'FAQ count')
 for u in doc.get('citation',[]):ck(any(t=='a' and a.get('href')==u for t,a in p.tags),'source link '+u)
 ck(len(doc.get('citation',[]))==(8 if r==S else 10),'source count')
 ck(doc.get('citation',[])==SOURCES[r],'exact official source set')
 ids=[a['id'] for t,a in p.tags if 'id' in a];ck(len(ids)==len(set(ids)),'duplicate IDs')
 for href in ['/discovery/','https://aetaxadvisors.taxdome.com/',Y if r==S else S]:ck(any(t=='a' and a.get('href')==href for t,a in p.tags),'required link '+href)
 if r==S:ck(any(t=='a' and a.get('href')=='/blog/owner-sells-business-plan-termination-timing/' for t,a in p.tags),'termination guide link')
 for token in ['/workspace/','baseline-12h','route-delta-12h','private report','REMOVED_REQUIRED']:
  ck(token not in s,'private data leak '+token)
 return errors

def unowned(s,r):
 if r==S:
  # Old five-section editorial region or new review+FAQ region. Closing CTA stays.
  start=s.index('    <section class="content-section fade-in-section">',s.index('<main>')) if 'id="retirement-sale-review"' not in s else s.index('<section class="content-section fade-in-section" id="retirement-sale-review">')
  end=s.index('    <section class="content-section fade-in-section" style="background:var(--light-bg);">',start)
  s=s[:start]+'<REVIEWED_BODY>\n'+s[end:]
 else:
  start=s.index('<!-- retirement-deadline-review:start -->') if '<!-- retirement-deadline-review:start -->' in s else s.index('        <p>One of the most common questions')
  end=s.index('        <hr style="margin: 3rem',start)
  s=s[:start]+'<REVIEWED_BODY>\n'+s[end:]
  s=re.sub(r'<section class="content-section fade-in-section" id="faq">.*?</section>','<REVIEWED_FAQ>',s,flags=re.S)
  s=re.sub(r'(<!-- million-owner-answer:start -->.*?</h2><p>).*?(</p>)',r'\1<REVIEWED_OWNER_ANSWER>\2',s,count=1,flags=re.S)
 for key in ['description','og:description','twitter:description']:
  s=re.sub(r'(<meta (?:name|property)="'+key+r'" content=")[^"]*',r'\1<REVIEWED_DESCRIPTION>',s)
 s=re.sub(r'(property="article:modified_time" content=")[^"]*',r'\1<REVIEWED_DATE>',s)
 def schema(m):
  d=json.loads(m[1])
  if d.get('@type')=='FAQPage':return ''
  if d.get('@type') in ['Article','BlogPosting']:
   d['description']='<REVIEWED_DESCRIPTION>';d['dateModified']='<REVIEWED_DATE>';d['mainEntityOfPage'].pop('dateModified',None);d.pop('citation',None)
   return '<script type="application/ld+json">'+json.dumps(d,sort_keys=True)+'</script>'
  return m[0]
 s=re.sub(r'<script type="application/ld\+json">\s*(.*?)</script>',schema,s,flags=re.S)
 # Inserting the sale FAQ adds one line before </head>; remove that exact blank.
 if r==S:s=s.replace('\n\n</head>','\n</head>')
 return s

def preservation(base,s,r):
 return [] if unowned((base/(r.strip('/')+'/index.html')).read_text(),r)==unowned(s,r) else ['unowned page bytes changed '+r]

def source_errors(base=None):
 e=[]
 for f,field in [('scripts/blog-catalog.json','description'),('assets/blog-search-index.json','description'),('owner_million_manifest.json','answer')]:
  new=json.loads((R/f).read_text());expected=json.loads((base/f).read_text()) if base else None
  for r in DATES:
   s=(R/(r.strip('/')+'/index.html')).read_text();value=DESC[r] if field=='description' else (sections(s,r)['The direct answer'].split(' A retirement plan can')[0] if r==S else faq(s,r)[-1][1])
   rows=[x for x in new if x['url']==r]
   if len(rows)!=1 or rows[0][field]!=value:e.append(f+': route value '+r)
   if base:next(x for x in expected if x['url']==r)[field]=value
  if base and new!=expected:e.append(f+': unrelated field/route changed')
 for f in ['content/reviewed-content-lastmod.json','content/discovery-reviewed-copy-20261106.json']:
  new=json.loads((R/f).read_text())
  for r in DATES:
   title=html.unescape(re.search(r'<title>(.*?)</title>',(R/(r.strip('/')+'/index.html')).read_text())[1])
   expected='2026-11-06' if 'lastmod' in f else {'title':title,'description':DESC[r],'description_only':True}
   if new.get(r)!=expected:e.append(f+': route value '+r)
  if base:
   old=json.loads((base/f).read_text())
   for r in DATES:old.pop(r,None);new.pop(r,None)
   if old!=new:e.append(f+': unrelated route changed')
 if base:
  old=(base/'llms-full.txt').read_text();catalog=json.loads((base/'scripts/blog-catalog.json').read_text())
  for r in DATES:
   desc=next(x['description'] for x in catalog if x['url']==r)
   old=''.join(l.replace(desc,DESC[r]) if HOST+r in l else l for l in old.splitlines(keepends=True))
  if old!=(R/'llms-full.txt').read_text():e.append('LLM discovery changed outside route description')
  if (base/'scripts/search-intent-config.json').read_bytes()!=(R/'scripts/search-intent-config.json').read_bytes():e.append('search intent global changed')
 return e

def math_checks():
 checks=[D(200000)*D('.25')==D(50000),D(100000)*D('.25')==D(25000),D(50000)+D(25000)==D(75000),D(50000)<D(72000),D('.25')/(1+D('.25'))==D('.20'),D(200000)*D('.20')==D(40000),D(40000)<D(72000),D(5000000)*D(0)==0]
 assert all(checks);return len(checks)

def cli():
 ap=argparse.ArgumentParser();ap.add_argument('root',nargs='?',default=str(R));ap.add_argument('--baseline');a=ap.parse_args();root=Path(a.root).resolve();base=Path(a.baseline) if a.baseline else None
 errors=source_errors(base);negative=0;links=0
 for r in DATES:
  file=r.strip('/')+'/index.html';s=(root/file).read_text();src=(R/file).read_text();errors+=page_errors(s,r)
  if base:
   errors+=preservation(base,src,r)
   for old,new in [('href="/discovery/"','href="/unexpected/"'),(DATES[r],'2000-01-01'),('</footer>','<p>New public fee: $999</p></footer>')]:
    assert old in src;assert preservation(base,src.replace(old,new,1),r);negative+=1
  if root!=R:
   expected=normalize_baseline_html(src,R,r)
   for tag in ['main','header','footer']:
    pat=r'<'+tag+r'\b[^>]*>.*?</'+tag+'>'
    if re.findall(pat,expected,re.S)!=re.findall(pat,s,re.S):errors.append('staged '+tag+' beyond exact build transforms '+r)
   assert main(expected)!=main(s.replace('</main>','<p>Unapproved result</p></main>'));negative+=1
  # Required claim guards are section-local, not satisfiable by an unrelated FAQ.
  for heading,tokens in REQUIRED[r].items():
   region=next(m[0] for m in re.finditer(r'<h2[^>]*>(.*?)</h2>(.*?)(?=<h2\b|$)',body(s,r),re.S) if plain(m[1])==heading)
   for token in tokens:
    changed=plain(region).replace(token,'REMOVED_REQUIRED')
    assert changed!=plain(region),(r,heading,token)
    bad=s.replace(region,'<h2>'+html.escape(heading)+'</h2><p>'+html.escape(changed[len(heading):])+'</p>',1)
    assert any(token in x for x in page_errors(bad,r)),(heading,token);negative+=1
  for token in STALE:
   assert any('stale claim' in x for x in page_errors(s.replace('</main>','<p>'+token+'</p></main>'),r));negative+=1
  for u in article(s)['citation']:
   assert any('source link' in x for x in page_errors(s.replace('href="'+u+'"','href="https://example.com/missing"'),r));negative+=1
  for q,a in faq(s,r):
   before=json.dumps(a,ensure_ascii=False);assert before in s
   assert 'exact visible FAQ parity' in page_errors(s.replace(before,json.dumps('Wrong '+a,ensure_ascii=False),1),r);negative+=1
  assert 'canonical' in page_errors(s.replace('rel="canonical"','rel="alternate"'),r);negative+=1
  p=Parser();p.feed(s)
  for t,attrs in p.tags:
   h=attrs.get('href','')
   if t=='a' and h.startswith('/') and not h.startswith('//'):
    target=h.split('#')[0].split('?')[0];target=root/((target.strip('/')+'/') if target.strip('/') else '')/'index.html' if not Path(target).suffix else root/target.lstrip('/')
    if not target.is_file():errors.append('missing internal link '+h)
    links+=1
  xml='\n'.join(p.read_text() for p in root.glob('sitemap*.xml'))
  entry=re.search(r'<url>\s*<loc>'+re.escape(HOST+r)+r'</loc>(.*?)</url>',xml,re.S)
  if not entry:errors.append('missing sitemap '+r)
  if root!=R and entry and '<lastmod>2026-11-06</lastmod>' not in entry[1]:errors.append('staged lastmod '+r)
  if r in json.loads((R/'discovery_review_holds.json').read_text()):errors.append('route held '+r)
  if any(d.get('source') in [r,r.rstrip('/')] and d.get('destination') not in [r,r.rstrip('/')] for d in json.loads((R/'vercel.json').read_text()).get('redirects',[])):errors.append('route redirected '+r)
 if root!=R and (root/'scripts/test-sale-year-retirement.py').exists():errors.append('test leaked to public')
 print(json.dumps({'root':str(root),'pages':2,'math_checks':math_checks(),'negative_fixtures':negative,'internal_links':links,'baseline_checks':bool(base),'errors':errors},indent=2));return bool(errors)
if __name__=='__main__':sys.exit(cli())
