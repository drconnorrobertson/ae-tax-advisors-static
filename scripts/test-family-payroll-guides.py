#!/usr/bin/env python3
"""Focused source/staged family-payroll checks. Never runs generators or writes output.

The cohort contains public content and preservation hashes only. Negative fixtures
remain in memory. Run: python3 scripts/test-family-payroll-guides.py [public]
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from decimal import Decimal as D
import argparse,hashlib,html,json,re,sys
REPO=Path(__file__).resolve().parents[1]
COHORT=json.loads((REPO/'content/family-payroll-accuracy-20261106.json').read_text())
SITE='https://www.aetaxadvisors.com'
PATTERNS={'footer':r'<footer\b.*?</footer>','header':r'<header\b.*?</header>','related_reading':r'<section class="content-section related-reading">.*?</section>','cta':r'<div class="post-cta">.*?</div>','h1':r'<h1\b.*?</h1>'}
FORBIDDEN=[r'without incurring any payroll tax obligations',r'Under IRC Section 3121\(c\)',r'payroll tax obligations exist for all family employees except',r'except for qualifying children under 18',r'\$1,250',r'\$23,500',r'\$11,875',r'\$35,375',r'saving \$15,300 in SE tax',r'saving \$13,000 in taxes',r'creates \$24,000 tax liability instead of \$37,000',r'with the spouse.s portion taxed at the spouse.s bracket',r'Family employment avoids kiddie tax entirely',r'building retirement savings tax-free',r'It saves 15\.3% self-employment tax',r'FUTA exemption ends at (?:age )?18',r'FICA exemption (?:continues|ends).*?21',r'No Form W-4 is needed',r'corporate child wages are exempt',r'new management company automatically',r'internal review only',r'/workspace/']
PRESERVED_SCORP='An S election can reduce employment taxes on business profit remaining after reasonable compensation. Income-tax results can also change, including through the Section 199A qualified business income deduction, so compare the combined tax effect rather than assuming income tax is unchanged.'
class Text(HTMLParser):
 def __init__(self): super().__init__();self.skip=0;self.parts=[];self.tags=[]
 def handle_starttag(self,t,a):
  self.tags.append((t,dict(a)))
  if t in ('script','style'):self.skip+=1
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip-=1
  self.parts.append(' ')
 def handle_data(self,d):
  if not self.skip:self.parts.append(d)
def plain(v):
 p=Text();p.feed(v);return ' '.join(' '.join(p.parts).split())
def schemas(v):return [json.loads(x) for x in re.findall(r'<script\b[^>]*type=[\'"]application/ld\+json[\'"][^>]*>(.*?)</script>',v,re.S)]
def validate(path,s,root):
 errors=[]
 def check(ok,why):
  if not ok:errors.append(path+': '+why)
 item=COHORT['pages'][path];stage='staged_' if root.name=='public' else '';route='/'+path[:-len('index.html')];parsed=Text();parsed.feed(s);t=plain(s)
 check(len(re.findall(r'<h1\b',s))==1,'one H1 required')
 canonical=[a.get('href') for tag,a in parsed.tags if tag=='link' and a.get('rel')=='canonical'];check(canonical==[SITE+route],'self canonical changed')
 check(not any('noindex' in a.get('content','').lower() for tag,a in parsed.tags if tag=='meta' and a.get('name','').lower() in ('robots','googlebot')),'noindex')
 title=re.search(r'<title>(.*?)</title>',s,re.S);check(title and html.unescape(title[1])==item['title'],'title mismatch')
 for name,value in [('description',item['description']),('og:description',item['description']),('twitter:description',item['description']),('og:title',item['title']),('twitter:title',item['title'])]:
  check([html.unescape(a.get('content','')) for tag,a in parsed.tags if tag=='meta' and (a.get('name')==name or a.get('property')==name)]==[value],name+' mismatch')
 for key,pattern in PATTERNS.items():
  block=re.search(pattern,s,re.S);check(block is not None and hashlib.sha256(block[0].encode()).hexdigest()==item[stage+'preserved_sha256'][key],key+' changed, including reported outcomes/offer/navigation')
 for expr in FORBIDDEN:check(not re.search(expr,html.unescape(s),re.I|re.S),'stale or unsafe claim '+expr)
 for needed in ['November 6, 2026','actual','reasonable','FUTA','Social Security','Medicare','withholding','joint','disregarded','EIN','retirement','child-labor','state','secure document channel']:
  check(needed.lower() in t.lower(),'missing '+needed)
 for url in ['https://www.irs.gov/publications/p15','https://www.irs.gov/businesses/small-businesses-self-employed/family-employees','https://www.ecfr.gov/current/title-26/section-31.3121(b)(3)-1','https://www.ecfr.gov/current/title-26/section-31.3306(c)(5)-1']:
  check(url in html.unescape(s),'primary source missing '+url)
 for expr in [r'(?:before|until|at|age) (?:age )?18',r'(?:before|until|at|age) (?:age )?21',r'corporat',r'every partner is a parent',r'actual (?:employer|services|work)',r'income.tax withholding']:
  check(re.search(expr,t,re.I),'boundary missing '+expr)
 try: data=schemas(s)
 except Exception as e:return errors+['invalid JSON-LD '+str(e)]
 a=[x for x in data if x.get('@type')=='BlogPosting'];check(len(a)==1,'one article schema required')
 if a:
  check(a[0].get('datePublished')==item['datePublished'],'publication date changed')
  check(a[0].get('dateModified')=='2026-11-06','review date missing')
  check(a[0].get('description')==item['description'],'article description mismatch')
  check(a[0].get('mainEntityOfPage',{}).get('@id')==SITE+route,'article URL mismatch')
 f=[x for x in data if x.get('@type')=='FAQPage'];check(len(f)==1,'one FAQ schema required')
 schema_faq=[(x.get('name'),x.get('acceptedAnswer',{}).get('text')) for x in f[0].get('mainEntity',[])] if f else []
 section=re.search(r'<section[^>]+id="faq".*?</section>',s,re.S)
 visible=[(plain(q),plain(a)) for q,a in re.findall(r'<h3>(.*?)</h3>\s*<p>(.*?)</p>',section[0] if section else '',re.S)]
 expected=[tuple(x) for x in item['faqs']];check(schema_faq==expected==visible,'FAQ parity or content mismatch')
 links=set(a.get('href','') for tag,a in parsed.tags if tag=='a')
 check(set(item[stage+'original_internal_links'])<=links,'existing internal link removed')
 for link in links:
  if not link.startswith('/') or link.startswith('//'):continue
  target=unquote(urlsplit(link).path).strip('/');candidate=root/target
  check(candidate.is_file() or (candidate/'index.html').is_file(),'missing internal link '+link)
 if 'complete-guide' in path:
  for n in ['$12,450','$12,500','$37,000','$24,500','6%','5.4%','$7,000','18 through 20','parent','Form W-4']:
   check(n in t,'implementation detail missing '+n)
 if 'ultimate-guide' in path:
  for n in ['$7,650','$15,300','$7,500','$2,700','$16,100','$1,350','$450','SEP','not an automatic net tax saving','do not build credits']:
   check(n in t,'planning detail missing '+n)
 if 'use-family' in path:
  for n in ['$18,000','$200,000','9%','3-10%','capitalization','related-party','combined','not a finding','do not establish $6,300']:
   check(n.lower() in t.lower(),'management detail missing '+n)
 if 'hidden-tax' in path:
  for n in ['$15,050','$7,500','$2,700','50%','25%','2.5%','not a dollar-for-dollar',PRESERVED_SCORP]:
   check(n in t,'preserved correction or family detail missing '+n)
 return errors

def main():
 ap=argparse.ArgumentParser();ap.add_argument('root',nargs='?',default=str(REPO));args=ap.parse_args();root=Path(args.root).resolve()
 assert len(COHORT['pages'])==4 and COHORT['review_date']=='2026-11-06'
 assert json.loads((REPO/'content/family-payroll-accuracy-20261106/pages.json').read_text())==['/'+p[:-len('index.html')] for p in COHORT['pages']]
 documents={p:(root/p).read_text() for p in COHORT['pages']}
 errors=[e for p,s in documents.items() for e in validate(p,s,root)]
 if errors:print('\n'.join(errors));return 1
 # Independent numeric boundaries, not extracted values asserted against themselves.
 dep=lambda wages:min(D('16100'),max(D('1350'),D(wages)+D('450')))
 assert dep('0')==1350 and dep('12000')==12450 and dep('14600')==15050 and dep('20000')==16100
 assert D('50000')*D('.25')+D('24500')==37000
 assert D('100000')*D('.0765')==7650 and D('7650')*2==15300
 assert D('200000')*D('.09')==18000 and D('200000')*D('.5')==100000
 checks=0
 for p,s in documents.items():
  mutations=[('missing review',s.replace('November 6, 2026','October 6, 2026')),('duplicate H1',s.replace('</main>','<h1>Another</h1></main>')),('wrong canonical',s.replace('rel="canonical" href="'+SITE,'rel="canonical" href="https://example.invalid')),('outcome tamper',s.replace('Saves $39K','Saves $40K').replace('Saves $83K','Saves $84K')),('CTA tamper',s.replace('class="post-cta"','class="changed-cta"')),('wrong publication',s.replace(COHORT['pages'][p]['datePublished'],'2026-11-06')),('bad FAQ',s.replace('"@type": "FAQPage"','"@type": "Thing"'))]
  for label,mutation in mutations:
   assert mutation!=s,(p,label)
   assert validate(p,mutation,root),(p,label,'not rejected');checks+=1
  for bad in ['FUTA exemption ends at 18.','No Form W-4 is needed.','A new management company automatically exempts wages.','Passive income above $1,250 is taxed at parental rates.']:
   assert validate(p,s.replace('</main>',pwrap(bad)+'</main>'),root),(p,bad);checks+=1
 print(f'PASS: 4 source/staged guides, 16 matching FAQs, employer/age/withholding/2026 math boundaries, preserved offers/outcomes/navigation/dates, internal links, {checks} rejected negative fixtures.')
 return 0

def pwrap(s):return '<p>'+s+'</p>'
if __name__=='__main__':sys.exit(main())
