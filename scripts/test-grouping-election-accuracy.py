#!/usr/bin/env python3
"""One-route grouping review: claims, source/discovery parity and exact boundaries.

Optional --baseline is a private pre-edit snapshot directory. No private
snapshot or synthetic negative fixture is copied into the public build.
"""
import argparse
import html
import json
import re
import sys
from decimal import Decimal as D
from html.parser import HTMLParser
from pathlib import Path
from tax_review_build_normalization import normalize_baseline_html

REPO = Path(__file__).resolve().parents[1]
ROUTE = '/blog/grouping-elections-real-estate-irc-469/'
FILE = ROUTE.strip('/') + '/index.html'
SITE = 'https://www.aetaxadvisors.com'
DESCRIPTION = 'Review IRC 469 grouping, the REPS all-interests election, participation tests, suspended losses and sale tradeoffs before combining rental activities.'
OLD_DESCRIPTION = 'For real estate investors holding multiple properties, the difference between deducting hundreds of thousands in losses and watching them sit trapped.'
OWNER_QUESTION = 'Can I group a rental property with my operating business for tax purposes?'
SOURCE_URLS = [
 'https://www.irs.gov/publications/p925',
 'https://www.ecfr.gov/current/title-26/section-1.469-4',
 'https://www.ecfr.gov/current/title-26/section-1.469-9',
 'https://www.ecfr.gov/current/title-26/section-1.469-5T',
 'https://www.irs.gov/irb/2010-04_IRB#RP-2010-13',
 'https://www.irs.gov/irb/2011-24_IRB#RP-2011-34',
]
# Bound required facts to their own section so an unrelated FAQ cannot hide a
# broken body claim. The script mutates each token and requires rejection.
REQUIRED = {
 'Two Different Rules: Economic-Unit Grouping and the REPS Election': [
  'appropriate economic unit', 'common control', 'common ownership',
  'all-interests election', 'not permission to pick', 'publicly traded partnerships',
  'Rental activities generally remain passive', 'Classify each activity'],
 'Establish REPS Separately from Rental Material Participation': [
  'more than 750 hours', 'more than half of all personal services',
  'Exactly 750 hours is not enough', 'more than 5%',
  'one spouse must independently satisfy both', 'another applicable test'],
 'The Seven Material Participation Tests: Correct Thresholds': [
  'Test 1: More than 500 hours', 'Test 2:', 'substantially all',
  'Test 3: More than 100 hours', 'individual-by-individual comparison',
  'Test 4: More than 500 hours combined', 'eligible trade or business activity',
  'must not qualify under another', 'not a 750-hour test or a shortcut for rental activities',
  'Test 5:', 'five of the preceding ten', 'Test 6:', 'any three prior',
  'Test 7:', 'Regular, continuous and substantial', 'another person is paid to manage',
  'Limited partnership interests', 'Tests 1, 5 and 6', 'less-than-10%', 'section 1.469-9(f)'],
 'Hypothetical: Eight Rentals and 560 Hours': [
  'not a client result', '900 qualifying hours', 'not employee work',
  '900 + 100 + (8 × 70) = 1,560', '900 > 780', 'independently',
  'not substantially all participation', 'no qualifying prior-year participation history',
  'Tests 4 and 6 do not apply', '8 × 70 = 560',
  '900 brokerage hours cannot be imported', 'separate deduction limits'],
 'Can Rentals Be Grouped with an Operating Business?': [
  'appropriate economic unit', 'insubstantial', 'same proportionate rental ownership',
  'only the rental portion used in the business', 'qualifying taxpayer may not group',
  '1.469-9(e)(3)', "taxpayer's own rental real estate interests", "Managing other people's properties"],
 'Nonpassive Does Not Mean Fully Deductible': [
  'personal-use', 'basis', 'at-risk', 'before passive loss limits',
  'does not automatically release prior passive losses', '461(l)', 'after passive loss rules',
  'former passive activity', '$40,000', '$10,000', '$30,000 remains suspended'],
 'Hypothetical: Six Rentals, 520 Hours and a $180,000 Loss': [
  'not an actual reported outcome', '900 qualifying nonemployee brokerage hours',
  '100 + 90 + 90 + 80 + 80 + 80 = 520', '1,520', '900 > 760',
  'No brokerage hour', 'substantial paid-manager work', 'no qualifying participation history',
  'No property exceeds 100 hours', 'no other material participation test applies',
  'If the entire $180,000 current-year loss', 'after all relevant limits',
  '$180,000 × 40% = $72,000', 'not a guaranteed saving', 'already usable without the election',
  'Additional depreciation can remain deferred'],
 'Filing, Consistency and Selling One Property': [
  'original income tax return', 'declaring that the taxpayer qualifies', '469(c)(7)(A)',
  'not a substitute', 'late-election relief', 'amended return automatically cures',
  'future qualifying years', 'no effect in a nonqualifying year', 'material change',
  'break in REPS status alone does not qualify', 'Revenue Procedure 2010-13', 'addresses', 'EINs',
  'Selling one building generally is not a disposition of the entire activity',
  'unrelated party', 'substantially-all partial-disposition', 'reasonably certain allocation'],
 'Election-Review Checklist for Your Advisor': [
  'Inventory activities and ownership', 'Find prior filings', 'for each spouse separately',
  'Support the hours', 'not the only permitted evidence', 'Model both choices',
  'Agree on implementation', 'written scope and fees'],
}
STALE = [
 'aggregate participation in all significant participation activities exceeds 750 hours',
 'Every dollar of loss from those properties becomes fully deductible',
 'grouping election ensures every dollar',
 'the combined hours satisfy material participation for the entire group',
 'vague or after-the-fact documentation will not survive IRS scrutiny',
 'that grouping election saves $72,000 in taxes for a single year',
]

class Parser(HTMLParser):
 def __init__(self): super().__init__(); self.tags=[]; self.words=[]; self.skip=0
 def handle_starttag(self,t,a):
  self.tags.append((t,dict(a)))
  if t in ('script','style'): self.skip += 1
 def handle_endtag(self,t):
  if t in ('script','style'): self.skip -= 1
 def handle_data(self,s):
  if not self.skip: self.words.append(s)

def plain(s):
 p=Parser();p.feed(s);return ' '.join(' '.join(p.words).split())
def schemas(s):return [json.loads(x) for x in re.findall(r'<script\b[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S)]
def main(s):return re.search(r'<main\b[^>]*>.*?</main>',s,re.S)[0]
def body(s):return re.search(r'<section class="content-section fade-in-section"><div class="container narrow">(.*?)</div></section>',s,re.S)[1]
def sections(s):return {plain(h):plain(b) for h,b in re.findall(r'<h2[^>]*>(.*?)</h2>(.*?)(?=<h2\b|$)',body(s),re.S)}
def faq(s):
 block=re.search(r'<section[^>]* id="faq">(.*?)</section>',s,re.S)[1]
 pairs=[(plain(q),plain(a)) for q,a in re.findall(r'<h3[^>]*>(.*?)</h3>\s*<p>(.*?)</p>',block,re.S)]
 q,a=re.search(r'<!-- million-owner-answer:start -->.*?<h2[^>]*>(.*?)</h2><p>(.*?)</p>',s,re.S).groups()
 return pairs+[(plain(q),plain(a))]
def article(s):return next(d for d in schemas(s) if d.get('@type')=='BlogPosting')

def page_errors(s):
 errors=[]
 def check(ok,label):
  if not ok:errors.append(label)
 p=Parser();p.feed(s);v=plain(main(s));parts=sections(s)
 for h,tokens in REQUIRED.items():
  check(h in parts,'missing section: '+h)
  for token in tokens:check(token in parts.get(h,''),h+': missing '+token)
 for token in STALE:check(token.lower() not in html.unescape(s).lower(),'stale: '+token)
 for url in SOURCE_URLS:check(any(t=='a' and a.get('href')==url for t,a in p.tags),'source: '+url)
 check([a.get('href') for t,a in p.tags if t=='link' and a.get('rel')=='canonical']==[SITE+ROUTE],'canonical')
 check(len(re.findall(r'<h1\b',s))==1,'H1 count')
 check(not any('noindex' in a.get('content','') for t,a in p.tags if t=='meta' and a.get('name') in ['robots','googlebot']),'noindex')
 check('Reviewed November 6, 2026' in v,'review date')
 d=article(s);check(d['datePublished']=='2026-08-17','publication date');check(d['dateModified']=='2026-11-06','modified date')
 check(d['mainEntityOfPage']['dateModified']=='2026-11-06','WebPage modified date')
 check(d['headline']==plain(re.search(r'<h1[^>]*>(.*?)</h1>',s,re.S)[1]),'headline parity')
 check(d['description']==DESCRIPTION,'article description')
 for key in ['description','og:description','twitter:description']:
  check([a.get('content') for t,a in p.tags if t=='meta' and (a.get('name')==key or a.get('property')==key)]==[DESCRIPTION],'description parity: '+key)
 q=[d for d in schemas(s) if d.get('@type')=='FAQPage'];check(len(q)==1,'FAQ count')
 if q:
  pairs=[(plain(x['name']),plain(x['acceptedAnswer']['text'])) for x in q[0]['mainEntity']]
  check(pairs==faq(s),'exact visible/structured FAQ parity');check(len(pairs)==7,'FAQ item count')
 check(any(t=='a' and a.get('href')=='/discovery/' for t,a in p.tags),'discovery CTA')
 for token in ['/tmp/','baseline.html','scope.json','grouping-accuracy-audit','private pre-edit snapshot']:
  check(token not in s,'private artifact leak: '+token)
 return errors

def unowned_page(s):
 # Replace only the exact approved editorial regions/fields. Everything else,
 # including navigation, related-case captions, prices, publication and CTAs,
 # remains byte-for-byte comparable to the private pre-edit snapshot.
 s=re.sub(r'(<section class="content-section fade-in-section"><div class="container narrow">).*?(</div></section>)',r'\1<REVIEWED_BODY>\2',s,count=1,flags=re.S)
 s=re.sub(r'<section class="content-section fade-in-section" id="faq">.*?</section>','<REVIEWED_FAQ>',s,count=1,flags=re.S)
 s=re.sub(r'(<!-- million-owner-answer:start -->.*?</h2><p>).*?(</p>)',r'\1<REVIEWED_OWNER_ANSWER>\2',s,count=1,flags=re.S)
 for key in ['description','og:description','twitter:description']:
  s=re.sub(r'(<meta (?:name|property)="'+key+r'" content=")[^"]*',r'\1<REVIEWED_DESCRIPTION>',s)
 def schema(m):
  d=json.loads(m[1])
  if d.get('@type')=='FAQPage':return '<REVIEWED_FAQ_SCHEMA>'
  if d.get('@type')=='BlogPosting':
   d['description']='<REVIEWED_DESCRIPTION>';d['dateModified']='<REVIEWED_DATE>';d['mainEntityOfPage']['dateModified']='<REVIEWED_DATE>'
   return '<script type="application/ld+json">'+json.dumps(d,sort_keys=True)+'</script>'
  return m[0]
 return re.sub(r'<script type="application/ld\+json">\s*(.*?)</script>',schema,s,flags=re.S)

def source_errors(s):
 errors=[];owner=dict(faq(s))[OWNER_QUESTION]
 for f in ['scripts/blog-catalog.json','assets/blog-search-index.json']:
  rows=[x for x in json.loads((REPO/f).read_text()) if x['url']==ROUTE]
  if len(rows)!=1 or rows[0]['description']!=DESCRIPTION:errors.append(f+': description parity')
 rows=[x for x in json.loads((REPO/'owner_million_manifest.json').read_text()) if x['url']==ROUTE]
 if len(rows)!=1 or rows[0]['answer']!=owner:errors.append('owner answer source parity')
 d=json.loads((REPO/'content/discovery-reviewed-copy-20261106.json').read_text())[ROUTE]
 if d!={'title':'Grouping Elections for Real Estate Under IRC 469 | AE Tax Advisors','description':DESCRIPTION,'description_only':True}:errors.append('discovery copy scope')
 if json.loads((REPO/'content/reviewed-content-lastmod.json').read_text())[ROUTE]!='2026-11-06':errors.append('lastmod source')
 lines=[l for l in (REPO/'llms-full.txt').read_text().splitlines() if SITE+ROUTE in l]
 if len(lines)!=1 or not lines[0].endswith(': '+DESCRIPTION):errors.append('LLM discovery description')
 return errors

def preservation_errors(base,s):
 errors=[]
 if unowned_page((base/FILE).read_text())!=unowned_page(s):errors.append('unowned source page bytes changed')
 owner=dict(faq(s))[OWNER_QUESTION]
 for f,field,value in [('scripts/blog-catalog.json','description',DESCRIPTION),('assets/blog-search-index.json','description',DESCRIPTION),('owner_million_manifest.json','answer',owner)]:
  expected=json.loads((base/f).read_text());rows=[x for x in expected if x['url']==ROUTE];assert len(rows)==1;rows[0][field]=value
  if expected!=json.loads((REPO/f).read_text()):errors.append(f+': outside single allowed field')
 for f in ['content/reviewed-content-lastmod.json','content/discovery-reviewed-copy-20261106.json']:
  old=json.loads((base/f).read_text());new=json.loads((REPO/f).read_text());old.pop(ROUTE,None);new.pop(ROUTE,None)
  if old!=new:errors.append(f+': unrelated route changed')
 old=(base/'llms-full.txt').read_text();expected=''.join(l.replace(OLD_DESCRIPTION,DESCRIPTION) if SITE+ROUTE in l else l for l in old.splitlines(keepends=True))
 if (REPO/'llms-full.txt').read_text()!=expected:errors.append('LLM discovery outside one description')
 return errors

def math_checks():
 checks=[
  8*70==560,900+100+560==1560,900>750,900>D(1560)/2,560>500,
  sum([100,90,90,80,80,80])==520,900+100+520==1520,900>D(1520)/2,
  all(x<=100 for x in [100,90,90,80,80,80]),520>500,
  D(180000)*D('.40')==D(72000),D(40000)-D(10000)==D(30000),
  not (500>500),not (100>100),not (750>750),not (D('.10')<D('.10')),
 ]
 assert all(checks);return len(checks)

def main_cli():
 ap=argparse.ArgumentParser();ap.add_argument('root',nargs='?',default=str(REPO));ap.add_argument('--baseline');a=ap.parse_args();root=Path(a.root).resolve();s=(root/FILE).read_text();source=(REPO/FILE).read_text();errors=page_errors(s)+source_errors(source);negative=0
 # Each negative fixture must exercise the expected claim guard.
 for heading,tokens in REQUIRED.items():
  for token in tokens:
   target=next(m for m in re.finditer(r'<h2[^>]*>(.*?)</h2>(.*?)(?=<h2\b|$)',body(s),re.S) if plain(m[1])==heading)
   original=target[0];mutated=re.sub(r'<[^>]+>','',original)
   mutated=html.unescape(mutated).replace(token,'REMOVED_REQUIRED_CLAIM')
   assert mutated!=html.unescape(re.sub(r'<[^>]+>','',original)),(heading,token)
   bad=s.replace(original,'<h2>'+html.escape(heading)+'</h2><p>'+html.escape(mutated.split(heading,1)[1])+'</p>',1)
   assert page_errors(bad),(heading,token);negative+=1
 for token in STALE:
  assert page_errors(s.replace('</main>','<p>'+token+'</p></main>'));negative+=1
 for old,new in [('rel="canonical"','rel="alternate"'),('"datePublished": "2026-08-17"','"datePublished": "2000-01-01"'),('"dateModified": "2026-11-06"','"dateModified": "2000-01-01"')]:
  assert page_errors(s.replace(old,new));negative+=1
 for url in SOURCE_URLS:
  assert page_errors(s.replace('href="'+url+'"','href="https://example.com/missing"'));negative+=1
 for i in range(7):
  d=next(d for d in schemas(s) if d.get('@type')=='FAQPage');answer=d['mainEntity'][i]['acceptedAnswer']['text']
  assert page_errors(s.replace(json.dumps(answer,ensure_ascii=False),json.dumps('Unmatched '+answer,ensure_ascii=False),1));negative+=1
 if a.baseline:
  base=Path(a.baseline);errors+=preservation_errors(base,source)
  for old,new in [('href="/discovery/"','href="/missing/"'),('Long-Term Rental Cost Segregation Worked Example','Altered case result'),('Published on August 17, 2026','Published on November 6, 2026')]:
   assert old in source;assert preservation_errors(base,source.replace(old,new,1));negative+=1
  assert preservation_errors(base,source.replace('</footer>','<p>Unexpected public fee $999</p></footer>'));negative+=1
 if root!=REPO:
  expected=normalize_baseline_html(source,REPO,ROUTE)
  if main(expected)!=main(s):errors.append('staged main differs from exact allowed build transforms')
  if unowned_page(expected)!=unowned_page(s):
   # Staging adds speed-insights and may ensure shared UX in <head>. Compare
   # all original header/footer blocks explicitly, not broad stripped markup.
   for tag in ['header','footer']:
    pat=r'<'+tag+r'\b[^>]*>.*?</'+tag+'>'
    if re.findall(pat,expected,re.S)!=re.findall(pat,s,re.S):errors.append('staged '+tag+' differs from allowed transforms')
  assert main(expected)!=main(s.replace('</main>','<p>Unexpected public content</p></main>'));negative+=1
  if (root/'scripts/test-grouping-election-accuracy.py').exists():errors.append('test script published')
 xml='\n'.join(p.read_text() for p in root.glob('sitemap*.xml'))
 if '<loc>'+SITE+ROUTE+'</loc>' not in xml:errors.append('missing sitemap entry')
 if root!=REPO:
  entry=re.search(r'<url>\s*<loc>'+re.escape(SITE+ROUTE)+r'</loc>(.*?)</url>',xml,re.S)
  if not entry or '<lastmod>2026-11-06</lastmod>' not in entry[1]:errors.append('reviewed sitemap lastmod')
 if ROUTE in json.loads((REPO/'discovery_review_holds.json').read_text()):errors.append('route is held')
 if any(x.get('source') in [ROUTE,ROUTE.rstrip('/')] and x.get('destination') not in [ROUTE,ROUTE.rstrip('/')] for x in json.loads((REPO/'vercel.json').read_text()).get('redirects',[])):errors.append('redirect away')
 print(json.dumps({'root':str(root),'pages':1,'math_checks':math_checks(),'negative_fixtures':negative,'baseline_checks':bool(a.baseline),'errors':errors},indent=2));return bool(errors)
if __name__=='__main__':sys.exit(main_cli())
