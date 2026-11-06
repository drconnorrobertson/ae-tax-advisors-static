#!/usr/bin/env python3
"""Focused, read-only checks for six reviewed QSBS guides.

Usage: python3 scripts/test-qsbs-buyer-accuracy.py [staged-public-directory]
Checks content, historical arithmetic, visible/schema FAQs, generator boundaries,
route eligibility and negative fixtures. Does not run any content generator.
"""
from pathlib import Path
from html.parser import HTMLParser
from decimal import Decimal as D
from urllib.parse import urlsplit,unquote
import ast,hashlib,html,importlib.util,json,re,subprocess,sys

REPO=Path(__file__).resolve().parents[1]
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else REPO
BASE='f2d5962a0b96bf7b9933bf1c764ed7778b6eea88'
DATA=json.loads((REPO/'content/qsbs-buyer-accuracy-20261106.json').read_text())
ROUTES=json.loads((REPO/'content/qsbs-buyer-accuracy-20261106/pages.json').read_text())
CHECKS=0
FAQ_COUNT=0
LINK_COUNT=0

def check(ok,message):
 global CHECKS
 CHECKS+=1
 assert ok,message

def plain(x):return ' '.join(html.unescape(re.sub('<[^>]*>','',x)).split())
def walk(o):
 if isinstance(o,dict):
  yield o
  for v in o.values():yield from walk(v)
 elif isinstance(o,list):
  for v in o:yield from walk(v)
def schemas(s):
 for raw in re.findall(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):yield from walk(json.loads(raw))
class Page(HTMLParser):
 def __init__(self,s):
  super().__init__();self.links=[];self.meta={};self.ids=[];self.canon=[];self.h1=0;self.stack=[];self.errors=[];self.feed(s)
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='a' and 'href' in d:self.links.append(d['href'])
  if t=='meta':self.meta[d.get('name',d.get('property',''))]=d.get('content','')
  if t=='link' and d.get('rel')=='canonical':self.canon.append(d['href'])
  if t=='h1':self.h1+=1
  if 'id' in d:self.ids.append(d['id'])
  if t not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:self.stack.append(t)
 def handle_endtag(self,t):
  if self.stack and self.stack[-1]==t:self.stack.pop()
  else:self.errors.append(t)

PATTERNS=[
 r'The maximum QSBS exclusion is the lesser of',
 r'QSBS exclusion would be the lesser of',
 r'If the final payment is received more than five years.*?entire gain qualifies',
 r'Converting an S corporation to a C corporation starts a new five-year clock',
 r'From the conversion date forward, stock is held as QSBS-eligible stock',
 r'married couple filing jointly each receives their own',
 r'each spouse can hold stock.*?claim separate limits',
 r'has been interpreted by the IRS to mean at least 80% of the time',
 r'Gross assets are measured as the greater of.*?adjusted basis.*?fair market value',
 r'more than 50% of assets must be used in an active business',
 r'Sale on June 1, 2026 satisfies the holding period',
 r'loss deduction is ordinary loss.*?if the investor is not a frequent investor',
 r'13\.61 million per person for 2026',
 r'These provisions are scheduled to expire on December 31, 2025',
 r'This approach avoids gift tax concerns entirely',
 r'QSBS that is inherited does not qualify for the Section 1202 exclusion',
 r'In practice three to five trusts.*?defensible structure',
]
def validate_content(s,label):
 text=plain(re.search(r'<main[^>]*>(.*?)</main>',s,re.S)[1])
 for pat in PATTERNS:check(not re.search(pat,text,re.I),f'{label}: obsolete claim {pat}')
 for word in ['July 4, 2025','$50 million','$75 million','$10 million','$15 million','greater of','more than five years','at least three years','at least four years','at least five years','original issuance','cap table','stock-sale versus asset-sale','Section 1202(e)','rental or leasing business']:
  check(word.lower() in text.lower(),f'{label}: missing {word}')
 for private in ['/workspace/','/tmp/','integration-12h','scratch notes','ranked findings','Search Console impressions']:
  check(private.lower() not in text.lower(),f'{label}: private data {private}')
 return text

redirects={r['source']:r['destination'] for r in json.loads((REPO/'vercel.json').read_text()).get('redirects',[])}
holds=json.loads((REPO/'discovery_review_holds.json').read_text())
check(len(ROUTES)==len(DATA['pages'])==6,'Six distinct routes')
check(len(set(ROUTES))==6,'No duplicate routes')
check(DATA['review_date']=='2026-11-06','Review date')
check(all(isinstance(x,str) and x.startswith('/') and x.endswith('/') for x in ROUTES),'Clean route-only public cohort')
PAGES={}
for record in DATA['pages']:
 path=record['path'];s=(ROOT/path).read_text();before=subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=REPO,text=True)
 p=Page(s);old=Page(before);route='/'+path.removesuffix('index.html')
 check(route in ROUTES and route not in redirects and route not in holds,path+': active route')
 check(p.canon==old.canon==[record['canonical']],path+': canonical unchanged')
 check(p.h1==1 and len(p.ids)==len(set(p.ids)),path+': heading and unique IDs')
 check(len(p.errors)<=len(old.errors) and len(p.stack)<=len(old.stack),path+': no new HTML balance problems')
 check(not any('noindex' in p.meta.get(k,'').lower() for k in ['robots','googlebot']),path+': indexable')
 check(p.meta['og:url']==old.meta['og:url']==record['canonical'],path+': og URL')
 check(re.findall(r'"datePublished"\s*:\s*"([^"]+)"',s)==record['publication_dates']==re.findall(r'"datePublished"\s*:\s*"([^"]+)"',before),path+': publication unchanged')
 for pub in re.findall(r'Published(?: on)? [^<|]+',before):check(pub in s,path+': visible publication unchanged')
 for key in ['article:published_time']:
  check(p.meta.get(key)==old.meta.get(key),path+': publication metadata')
 desc=p.meta['description']
 check(100<=len(desc)<=170 and desc.endswith('.'),path+': complete description')
 for key in ['og:description','twitter:description']:
  if key in p.meta:check(p.meta[key]==desc,path+': '+key)
 title=plain(re.search(r'<title>(.*?)</title>',s,re.S)[1])
 for key in ['og:title','twitter:title']:
  if key in p.meta:check(p.meta[key]==title,path+': '+key)
 if path!='qsbs-exclusion-section-1202/index.html':
  check(re.search(r'<h1[^>]*>.*?</h1>',s,re.S)[0]==re.search(r'<h1[^>]*>.*?</h1>',before,re.S)[0],path+': H1 unchanged')
 # Protect identity, navigation, actual pricing and case links. Staged builds may normalize footers.
 header=re.search(r'<header\b.*?</header>',s,re.S)[0];old_header=re.search(r'<header\b.*?</header>',before,re.S)[0]
 if ROOT==REPO:check(header==old_header,path+': header preserved')
 else:check(Page(header).links==Page(old_header).links,path+': staged navigation destinations preserved')
 for a in re.findall(r'<a[^>]+href="[^"]*(?:case-studies|pricing)[^"]*"[^>]*>.*?</a>',before,re.S):check(a in s,path+': pricing/case link retained')
 if ROOT==REPO:check(re.findall(r'<footer\b.*?</footer>',s,re.S)==re.findall(r'<footer\b.*?</footer>',before,re.S),path+': footer credentials preserved')
 for sec in re.findall(r'<section class="content-section related-reading">.*?</section>',before,re.S):
  if ROOT==REPO:check(sec in s,path+': related links retained')
 pairs={plain(q):plain(a) for q,a in re.findall(r'<h3[^>]*>(.*?)</h3>\s*<p[^>]*>(.*?)</p>',s,re.S)}
 for obj in schemas(s):
  if 'dateModified' in obj:check(obj['dateModified']=='2026-11-06',path+': dateModified')
  if obj.get('@type') in ('Article','BlogPosting') and 'description' in obj:check(obj['description']==desc,path+': article description')
  if obj.get('@type')=='FAQPage':
   for q in obj['mainEntity']:
    check(q['acceptedAnswer']['text']==pairs.get(q['name']),path+': exact FAQ parity '+q['name']);FAQ_COUNT+=1
 sources=re.search(r'<section[^>]+id="qsbs-official-sources".*?</section>',s,re.S)
 check(bool(sources),path+': source panel')
 for source in record['sources']:
  check(f'href="{source["url"]}"' in sources[0],path+': source link')
  check(urlsplit(source['url']).netloc in {'uscode.house.gov','www.irs.gov','www.ftb.ca.gov'},path+': official source')
 for href in p.links:
  u=urlsplit(href)
  if u.scheme or u.netloc or not u.path.startswith('/'):continue
  target=REPO/unquote(u.path).lstrip('/')
  check(target.is_file() or (target/'index.html').is_file() or u.path in redirects,path+': internal link '+href);LINK_COUNT+=1
 PAGES[path]=validate_content(s,path)
check(FAQ_COUNT==28,'Expected visible FAQ count preserved')

A=PAGES['the-business-owners-guide-to-section-1202-qualified-small-business-stock-qsbs/index.html']
B=PAGES['blog/qualified-small-business-stock-section-1202/index.html']
C=PAGES['qsbs-exclusion-section-1202/index.html']
E=PAGES['the-business-owners-guide-to-section-1202-qualified-small-business-stock-qsbs-exclusion/index.html']
# Arithmetic tied to visible numerical assertions, not just text existence.
def eligible(proceeds,basis,dollar=D('10000000'),percentage=D(1)):
 gain=proceeds-basis;excluded=min(gain,max(dollar,basis*10))*percentage
 return gain,excluded,gain-excluded
check(eligible(D(12000000),D(800000))==(D(11200000),D(10000000),D(1200000)),'Older-stock example 1 greater-of')
check('Excluded gain: $10 million. Taxable gain: $1.2 million.' in A,'Example 1 displayed')
check(eligible(D(25000000),D(1200000))==(D(23800000),D(12000000),D(11800000)),'Older-stock example 2 greater-of')
check('Excluded gain: $12 million. Taxable gain: $11.8 million.' in A,'Example 2 displayed')
check(D(40000000)-3*D(400000)==D(38800000),'Three-founder basis calculation')
check(D(38800000)-D(30000000)==D(8800000),'Three-founder taxable remainder')
check('total gain is $38.8 million' in A and 'total taxable gain is $8.8 million' in A,'Founder math displayed')
founder_basis=D(180000)*D('.6');trust_basis=D(180000)*D('.2')
founder_gain=D(96000000)*D('.6')-founder_basis;trust_gain=D(96000000)*D('.2')-trust_basis
check(founder_basis==108000 and trust_basis==36000,'2021 stock basis allocation')
check(founder_gain==57492000 and trust_gain==19164000,'2027 proceeds minus basis')
check(founder_gain-10000000==47492000 and 2*(trust_gain-10000000)==18328000,'2027 taxable allocation')
check(founder_gain+2*trust_gain-30000000==65820000,'2027 total taxable gain')
for n in ['$108,000','$36,000','$57,492,000','$19,164,000','$47,492,000','$18,328,000','$65,820,000']:
 check(n in B,'2021/2027 example displays '+n)
check(D(30000000)*D('.238')==D(7140000) and D(20000000)*D('.238')==D(4760000),'Trust savings illustration')
check('2021 acquisition date remains controlling' in B and '$10,000,000 dollar limit' in B,'Historical regime preserved')
check(D(18000000)*D('.238')==4284000 and D(3000000)*D('.238')==714000,'Future $18M example')
check('Future hypothetical, not a 2026 sale' in C and 'unindexed $15 million base' in C,'Future cap and dates stated')
check('June 1, 2026 is exactly five years' in E and 'June 2, 2026 sale can satisfy' in E,'Older-stock anniversary boundary')
check(D(5000000)*D('.238')==1190000,'$5M federal savings')
check('generally limited to $3,000 ($1,500 if married filing separately)' in E,'Capital-loss rule preserved')

# A separately reviewed sale cohort may update STRUCTURE in the same module.
# Require its exact approved definition and dedicated source/staged checks before
# excluding it; every other non-QSBS definition remains strictly preserved.
allow_sale_structure=(REPO/'content/sale-buyer-accuracy-20261106/pages.json').exists()
if allow_sale_structure:
 sale_routes=json.loads((REPO/'content/sale-buyer-accuracy-20261106/pages.json').read_text())
 check(sale_routes==['/the-business-owners-guide-to-installment-sales-and-deferred-gain-strategies/','/1031-exchange-planning/','/structuring-your-business-for-sale/','/business-exit-tax-planning-minimize-taxes-selling-company/'],'Exact reviewed sale cohort')
 def structure_signature(source):
  nodes=[n for n in ast.parse(source).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='STRUCTURE' for t in n.targets)]
  assert len(nodes)==1
  return hashlib.sha256(ast.dump(nodes[0],include_attributes=False).encode()).hexdigest()
 source=(REPO/'cluster_c8.py').read_text()
 expected_structure='9fb97321e4373c3d5714859760aa5e26809170632b0b053080c292010c1b3300'
 check(structure_signature(source)==expected_structure,'Reviewed sale STRUCTURE definition preserved')
 for old,new in [('Doing it years earlier does not','Doing it years earlier does'),('Section 751','Section 999')]:
  changed=source.replace(old,new)
  check(changed!=source and structure_signature(changed)!=expected_structure,'Changed sale definition must be rejected')
 subprocess.run([sys.executable,str(REPO/'scripts/test-sale-buyer-guides.py'),str(ROOT)],check=True)
# Generator scope: all remaining definitions/articles must remain identical.
def normalized_module(source,kind):
 tree=ast.parse(source)
 if kind=='cluster':
  tree.body=[n for n in tree.body if not(isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ({'QSBS','STRUCTURE'} if allow_sale_structure else {'QSBS'}) for t in n.targets))]
 else:
  arr=next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='ARTICLES' for t in n.targets))
  arr.elts=[n for n in arr.elts if not any(isinstance(k,ast.Constant) and k.value=='slug' and isinstance(v,ast.Constant) and v.value=='qualified-small-business-stock-section-1202' for k,v in zip(n.keys,n.values))]
 return ast.dump(tree,include_attributes=False)
for path,kind in [('cluster_c8.py','cluster'),('scripts/batch_entity.py','blog')]:
 before=subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=REPO,text=True)
 check(normalized_module(before,kind)==normalized_module((REPO/path).read_text(),kind),path+': unrelated definitions unchanged')
sys.path.insert(0,str(REPO));sys.path.insert(0,str(REPO/'scripts'))
import cluster_c8,batch_entity
q=cluster_c8.QSBS
s=(REPO/'qsbs-exclusion-section-1202/index.html').read_text()
check(q.lead in s and html.escape(q.title,quote=True) in s,'Cluster lead/title parity')
for title,body in q.body:check(body in s,'Cluster body parity '+title)
for question,answer in q.faqs:check(answer in s,'Cluster FAQ parity '+question)
for takeaway in q.takeaways:check(takeaway in s,'Cluster takeaway parity')
a=next(x for x in batch_entity.ARTICLES if x['slug']=='qualified-small-business-stock-section-1202')
s=(REPO/'blog/qualified-small-business-stock-section-1202/index.html').read_text()
for t in a['intro']:check(t in s,'Blog intro parity')
for title,paras in a['sections']:
 for t in paras:check(t in s,'Blog section parity '+title)
for question,answer in a['faqs']:check(answer in s,'Blog FAQ parity '+question)
# Negative fixtures restore each dangerous old claim and must fail the guard.
fixture=(REPO/DATA['pages'][0]['path']).read_text()
for old in [
 'The maximum QSBS exclusion is the lesser of $10 million or ten times basis.',
 'A married couple filing jointly each receives their own $10 million exclusion.',
 'Converting an S corporation to a C corporation starts a new five-year clock.',
 'Gross assets are measured as the greater of adjusted basis or fair market value.',
 'Sale on June 1, 2026 satisfies the holding period.',
 'A loss deduction is ordinary loss if the investor is not a frequent investor.',
 'More than 50% of assets must be used in an active business.',
 'If the final payment is received more than five years after issuance, the entire gain qualifies.',
 'This approach avoids gift tax concerns entirely.',
 'QSBS that is inherited does not qualify for the Section 1202 exclusion.',
]:
 corrupted=fixture.replace('</main>','<p>'+old+'</p></main>',1)
 try:validate_content(corrupted,'negative fixture')
 except AssertionError:pass
 else:raise AssertionError('Negative fixture escaped: '+old)
print(f'PASS: six QSBS guides; {FAQ_COUNT} FAQ pairs; {LINK_COUNT} internal links; {CHECKS} assertions; ten negative fixtures; two narrow generator scopes.')
