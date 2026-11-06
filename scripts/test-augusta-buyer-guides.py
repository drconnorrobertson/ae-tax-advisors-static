#!/usr/bin/env python3
"""Read-only regression checks for the three corrected Augusta Rule guides.

Run against source and staged public output. --check-discovery additionally checks
llms-full.txt after the integration's separately owned discovery sync is applied.
Negative fixtures are in memory only and cannot enter the public build.
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse, html, json, re, sys

SITE = 'https://www.aetaxadvisors.com'
PAGES = {
 'augusta-rule-business-owners/index.html': '2024-10-19T00:00:00-04:00',
 'augusta-rule-for-business-owners-when-it-works-and-how-to-do-it-safely/index.html': '2024-11-22T00:00:00-04:00',
 'blog/augusta-rule-real-estate-investors-irc-280a/index.html': '2026-08-20',
}
STALE_SUMMARY = 'The Augusta Rule, named after Augusta National Golf Club, allows you to deduct property rental expenses without reporting the rental income under IRC 280A(g).'
FORBIDDEN = [
 r'you still deduct expenses allocable', r'You can still deduct rental expenses',
 r'deduct the full rental period', r'created a \$15,000 deduction with zero income',
 r'personal use does not exceed 14', r'limit personal use to 14',
 r'avoid personal use exceeding 14', r'Spend at least 14 days',
 r'residence for at least 14 days', r'File Schedule E for the property \(even though',
 r'personal expenses \(not deductible\)', r'No Form 1099\.',
 r'no offsetting limitation on your personal deductions',
 r'personal use rules do not restrict your deductions',
 r'37% federal bracket plus 3\.8%', r'\$7,344',
 r'entity side remains a straightforward business deduction',
 r'IRS scrutiny is high', r'IRS is increasingly scrutinizing',
 r'deduct all rental expenses under normal rules',
]

class Content(HTMLParser):
 def __init__(self):
  super().__init__(); self.tags=[]; self.text=[]; self.skip=0
 def handle_starttag(self,tag,attrs):
  self.tags.append((tag,dict(attrs)))
  if tag in ['script','style']: self.skip += 1
 def handle_endtag(self,tag):
  if tag in ['script','style']: self.skip -= 1
 def handle_data(self,data):
  if not self.skip: self.text.append(data)

def plain(value):
 p=Content(); p.feed(value); return ' '.join(' '.join(p.text).split())

def schemas(document):
 return [json.loads(m) for m in re.findall(r'<script\b[^>]*type=[\'"]application/ld\+json[\'"][^>]*>(.*?)</script>', document, re.S)]

def validate_page(path,document):
 errors=[]
 def check(ok,message):
  if not ok: errors.append(f'{path}: {message}')
 route='/' + path[:-len('index.html')]
 parsed=Content(); parsed.feed(document)
 text=plain(document)
 main=re.search(r'<main\b[^>]*>(.*?)</main>',document,re.S)
 check(main is not None,'missing main')
 main_text=plain(main[1]) if main else ''
 canonical=[a.get('href') for t,a in parsed.tags if t=='link' and a.get('rel')=='canonical']
 check(canonical==[SITE+route],'canonical changed or duplicated')
 check(len(re.findall(r'<h1\b',document))==1,'expected one H1')
 check(not any('noindex' in a.get('content','').lower() for t,a in parsed.tags if t=='meta' and a.get('name','').lower() in ['robots','googlebot']),'page is noindex')
 for expression in FORBIDDEN:
  check(not re.search(expression,html.unescape(document),re.I),'stale claim: '+expression)
 check(STALE_SUMMARY not in document,'stale summary')
 check(re.search(r'(more than|exceed[s]?) the greater of 14 (?:personal-use )?days or 10%',main_text,re.I),'missing strict residence test')
 check('fewer than 15' in main_text,'missing annual rental limit')
 check(re.search(r'(all renters|all actual rental days|all rental dates)',main_text,re.I),'missing aggregate rental-day check')
 check('Section 162' in main_text and 'ordinary and necessary' in main_text,'missing independent business expense test')
 check('unrelated guests' in main_text,'missing unrelated-renter distinction')
 check('sole propriet' in main_text.lower() and 'disregarded' in main_text,'missing own-business payer warning')
 check('Section 274' in main_text,'missing entertainment limitation')
 check('Schedule E' in main_text and 'information-return' in main_text,'missing distinct reporting analysis')
 check('personal itemized deductions' in main_text or 'ordinary itemized-deduction rules and limits' in main_text,'missing ordinary personal deduction limits')
 check('https://uscode.house.gov/us/usc/119-118/t26/s280A/' in document and 'https://www.irs.gov/taxtopics/tc415' in document,'primary sources missing')
 check('November 6, 2026' in main_text,'visible review date missing')
 data=schemas(document)
 articles=[d for d in data if d.get('@type')=='BlogPosting']
 check(len(articles)==1,'expected one BlogPosting')
 if articles:
  article=articles[0]
  check(article['datePublished']==PAGES[path],'publication date changed')
  check(article['dateModified']=='2026-11-06','review date not aligned')
  heading=re.search(r'<h1\b[^>]*>(.*?)</h1>',document,re.S)
  check(heading is not None and article.get('headline')==plain(heading[1]),'Article headline differs from visible H1')
  for key in ['description','og:description','twitter:description']:
   values=[a.get('content') for t,a in parsed.tags if t=='meta' and (a.get('name')==key or a.get('property')==key)]
   check(values==[article['description']],key+' mismatches Article description')
 for faq in [d for d in data if d.get('@type')=='FAQPage']:
  check(bool(faq.get('mainEntity')),'empty FAQ')
  for question in faq.get('mainEntity',[]):
   if not isinstance(question,dict): check(False,'FAQ contains a non-Question entry'); continue
   check(question.get('@type')=='Question','FAQ entry lacks Question type')
   check(plain(question.get('name','')) in main_text,'FAQ question missing from visible page')
   check(plain(question.get('acceptedAnswer',{}).get('text','')) in main_text,'FAQ answer differs from visible page')
 if path==list(PAGES)[0]:
  for token in ['$5,000','$70,000','$15,000','30 days','Support the business rental, not just the day count','Decision guide updated September 26, 2026.']:
   check(token in main_text,'illustration or later decision section changed: '+token)
 if path==list(PAGES)[1]:
  check('<title>Augusta Rule Documentation and Rental-Day Checklist | AE Tax Advisors</title>' in document,'complete buyer title missing')
  for token in ['$5,000','$50,000','$3,000','$500','$300','$1,500 to $3,500','$1,800 to $2,300']:
   check(token in main_text,'illustrative price or cost removed: '+token)
 if path==list(PAGES)[2]:
  for token in ['$1,500','$18,000','$6,660','$3,600','$14,400','$5,328','37%','20%','NIIT','nonpassive','QBI']:
   check(token in main_text,'tax illustration missing: '+token)
  check(18000*.37==6660 and (18000-18000*.2)*.37==5328,'tax illustration arithmetic')
 for link in ['/discovery/','/pricing/','/case-studies/','/business-owner-tax-planning/']:
  # Business-owner link is not present on the third source baseline.
  if path==list(PAGES)[2] and link=='/business-owner-tax-planning/': continue
  alternatives=[link]
  if link=='/business-owner-tax-planning/': alternatives.append('/business-owner-small-business-tax/')
  check(any(f'href="{candidate}"' in document or f"href='{candidate}'" in document for candidate in alternatives),'required existing conversion link missing: '+link)
 return errors

def validate_discovery(base,documents):
 p=base/'llms-full.txt'
 if not p.exists(): return ['llms-full.txt: missing discovery output']
 text=p.read_text(); errors=[]
 if STALE_SUMMARY in text: errors.append('llms-full.txt: stale Augusta rental-expense summary remains')
 for path,document in documents.items():
  url=SITE+'/'+path[:-len('index.html')]
  entries=[line for line in text.splitlines() if f']({url})' in line]
  if not entries: errors.append(f'llms-full.txt: missing {url}'); continue
  desc=next(d['description'] for d in schemas(document) if d.get('@type')=='BlogPosting')
  if any(desc not in entry for entry in entries): errors.append(f'llms-full.txt: description not synchronized for {url}')
 return errors

def negative_fixtures(documents):
 path=list(PAGES)[0]; good=documents[path]; tested=0
 for bad in ['You can still deduct rental expenses.','No Form 1099.','personal use does not exceed 14 days.','At the 37% federal bracket plus 3.8% NIIT, savings are $7,344.','File Schedule E for the property (even though you exclude the income).','personal expenses (not deductible).']:
  assert validate_page(path,good.replace('</main>',f'<p>{bad}</p></main>')),bad
  tested+=1
 for replacement in [good.replace('2024-10-19T00:00:00-04:00','2026-11-06'),good.replace('rel="canonical"','rel="alternate"'),good.replace('"acceptedAnswer": {','"acceptedAnswer": {"bad": true,',1).replace('"text": "IRC Section 280A(g)','"text": "Unmatched FAQ. IRC Section 280A(g)',1),good.replace('more than the greater of 14 days or 10%','at least 14 days',1).replace('exceed the greater of 14 days or 10%','at least 14 days')]:
  assert validate_page(path,replacement),'negative fixture not detected'; tested+=1
 return tested

def main():
 parser=argparse.ArgumentParser(); parser.add_argument('root',nargs='?',default='.'); parser.add_argument('--check-discovery',action='store_true'); args=parser.parse_args()
 base=Path(args.root).resolve(); documents={p:(base/p).read_text() for p in PAGES}
 errors=[e for p,d in documents.items() for e in validate_page(p,d)]
 if args.check_discovery: errors+=validate_discovery(base,documents)
 fixtures=negative_fixtures(documents)
 # Within a full build every corrected route remains discoverable without redirects.
 sitemaps=list(base.glob('sitemap*.xml'))
 if sitemaps:
  xml='\n'.join(p.read_text() for p in sitemaps)
  for p in PAGES:
   url=SITE+'/'+p[:-len('index.html')]
   if f'<loc>{url}</loc>' not in xml: errors.append(f'{p}: missing sitemap entry')
 config_path=base/'vercel.json'
 if not config_path.exists(): config_path=base.parent/'vercel.json'
 if config_path.exists():
  redirects=json.loads(config_path.read_text()).get('redirects',[])
  targets={'/'+p[:-len('index.html')] for p in PAGES}
  for r in redirects:
   if r.get('source') in targets: errors.append(f'{r["source"]}: corrected route redirects')
 print(json.dumps({'root':str(base),'pages':len(documents),'negative_fixtures':fixtures,'discovery_checked':args.check_discovery,'errors':errors},indent=2))
 return bool(errors)
if __name__=='__main__': sys.exit(main())
