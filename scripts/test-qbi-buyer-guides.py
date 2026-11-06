#!/usr/bin/env python3
"""Read-only QBI guide, source ownership, preservation, and arithmetic checks.
Negative fixtures are in memory only. Baselines and audits are not public content.
"""
import argparse,ast,hashlib,html,json,re,sys
from decimal import Decimal as D
from pathlib import Path
from html.parser import HTMLParser
SITE='https://www.aetaxadvisors.com'
PAGES=[
 's-corp-qbi-deduction-maximization/index.html',
 'the-business-owners-guide-to-section-199a-qualified-business-income-qbi-deduction/index.html',
 'qbi-deduction-a-practical-guide-for-business-owners/index.html',
]
STALE=[
 '/workspace/','internal audit only','$182,100','$364,200','$400,200','projected to increase to $195,000',
 'A business paying no wages has a cap of zero','zero wages means a zero cap',
 'Every dollar of officer wage saves income tax','Officer wages cut payroll tax',
 'That crossing point is the mathematical target',
 'any business whose principal asset is the reputation or skill of its owners',
 'any business whose principal asset is the reputation or skill of its employees or owners',
 'those operations may qualify for their own QBI treatment even when the service business does not',
 'where the arrangement is principally a device',
 'Maximum QBI deduction available: $600,000',
 'W-2 wages paid to others (only the owner',
 'depreciable life exceeding one year','remaining useful life exceeding one year',
 '20% of W-2 wages plus 2.5%',
 'Let me recalculate','New limitation = 25% of $200,000 + 2.5% of $2,800,000',
 'cost segregation studies increase qualified property basis',
 'saving $50,000-$300,000 annually','generate $30,000 to $75,000',
 'generating net tax savings of approximately $4,700',
 'plus self-employment tax','Equipment acquired in January generates QBI benefit for only 11 months',
 'Strategic December acquisition provides incremental timing advantage',
 'Aggregation is irrevocable for subsequent tax years without IRS consent',
 'unless the real estate investor claims real estate professional status',
 'allocate income to higher-wage partners','consider converting their business structure to a C-corporation',
 'Our team ensures your business structure',
]
COMMON=[
 '$403,500','$553,500','$201,775','$276,775','$201,750','$276,750',
 'taxable income before the QBI deduction','phase-in','50%','25%','2.5%',
 '50% or more common ownership','endorsements',"licensing an individual's identity",'paid appearances',
 'at least two','majority of the tax year including its last day','same date','none of the aggregated businesses can be an SSTB',
 'later of 10 years','last day of the last full year','year-end','unadjusted basis immediately after acquisition',
 'employee','employer retirement contribution','not also deducted a second time',
 '$400','$1,000','material participation','qualified dividends','November 6, 2026',
]
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.tags=[];self.words=[];self.skip=0
 def handle_starttag(self,t,a):
  self.tags.append((t,dict(a)))
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip-=1
 def handle_data(self,s):
  if not self.skip:self.words.append(s)
def text(s):
 p=Parser();p.feed(s);return ' '.join(html.unescape(' '.join(p.words)).split())
def schemas(s):return [json.loads(x) for x in re.findall(r'<script\b[^>]*type=[\'"]application/ld\+json[\'"][^>]*>(.*?)</script>',s,re.S)]
def block(s,tag):return re.search(r'<'+tag+r'\b[^>]*>.*?</'+tag+'>',s,re.S)[0]
def digest(s):return hashlib.sha256(s.encode()).hexdigest()
def check_page(path,s,expected,staged=False):
 errors=[]
 def check(ok,msg):
  if not ok:errors.append(path+': '+msg)
 par=Parser();par.feed(s);raw=html.unescape(s);main=block(s,'main');visible=text(main)
 meta=lambda key:[a.get('content') for t,a in par.tags if t=='meta' and (a.get('name')==key or a.get('property')==key)]
 route='/'+path[:-10]
 check([a.get('href') for t,a in par.tags if t=='link' and a.get('rel')=='canonical']==[SITE+route],'canonical changed')
 check(len(re.findall(r'<h1\b',s))==1,'one H1 required')
 check(not any('noindex' in a.get('content','') for t,a in par.tags if t=='meta' and a.get('name','').lower() in ['robots','googlebot']),'unexpected noindex')
 check(text(re.search(r'<title>(.*?)</title>',s,re.S)[1])==expected['title'],'title changed')
 for key in ['description','og:description','twitter:description']:check(meta(key)==[expected['description']],'metadata mismatch: '+key)
 for token in STALE:check(token.lower() not in raw.lower(),'stale tax claim: '+token)
 for token in COMMON:check(token.lower() in visible.lower(),'missing rule: '+token)
 for url in ['https://www.irs.gov/pub/irs-drop/rp-25-32.pdf','https://www.ecfr.gov/current/title-26/section-1.199A-5','https://www.ecfr.gov/current/title-26/section-1.199A-4','https://www.ecfr.gov/current/title-26/section-1.199A-2']:
  check(url in main,'primary source missing: '+url)
 check('instructions are currently labeled 2025' in visible,'instructions-year caveat missing')
 if path==PAGES[0]:
  for token in ['W = 2P/7','$700,000','$200,000','$100,000','$75,000','$90,000','deduction-only','not the total-tax optimum','$50,000, not zero','required reasonable compensation']:
   check(token in visible,'S-corp calculation missing: '+token)
 else:
  for token in ['Real estate professional status is not required','three of the five years','at least four years','C corporation does not qualify automatically','$2,000,000, not $2,800,000','limitation remains $100,000']:
   check(token.lower() in visible.lower(),'rental/UBIA rule missing: '+token)
 if path==PAGES[1]:
  for token in ['$400,000, not $600,000','$300,000','no deduction increase in this symmetric example','corporate income is outside Section 199A','constructive-receipt','$10,000, before the overall cap']:
   check(token.lower() in visible.lower(),'overview calculation missing: '+token)
 if path==PAGES[2]:
  for token in ['$7,400','$7,900 worse','$10,000, not an automatic percentage','$40,000 increase','not also subject to self-employment tax','partner generally is not an employee']:
   check(token.lower() in visible.lower(),'practical calculation missing: '+token)
 ds=schemas(s);articles=[d for d in ds if d.get('@type') in ['Article','BlogPosting']]
 check([d.get('datePublished') for d in articles]==expected['publication_dates'],'publication dates changed')
 for d in articles:
  check(d.get('dateModified')=='2026-11-06','modified date missing')
  check(d.get('description')==expected['description'],'article description differs')
  check(d.get('headline')==text(re.search(r'<h1\b[^>]*>(.*?)</h1>',s,re.S)[1]),'headline differs from H1')
 faqs=[d for d in ds if d.get('@type')=='FAQPage'];check(len(faqs)==1,'one FAQ schema required')
 if faqs:
  pairs=[(x['name'],x['acceptedAnswer']['text']) for x in faqs[0]['mainEntity']]
  check(pairs==[tuple(x) for x in expected['faqs']],'FAQ data mismatch')
  for q,a in pairs:
   check(text(q) in visible,'FAQ question not visible: '+q)
   check(text(a) in visible,'FAQ answer not visible: '+q)
 for tag,h in expected['staged_preserved_sha256' if staged else 'preserved_sha256'].items():check(digest(block(s,tag))==h,tag+' changed')
 for label,item in expected.get('preserved_blocks',{}).items():
  found=re.search(item['pattern'],s,re.S)
  check(bool(found) and digest(found[0])==item['staged_sha256' if staged else 'sha256'],label+' changed, including case-result text or CTA')
 links=re.findall(r'<a\b[^>]*href="(/[^\"]*)"',s)
 check(sorted(links)==sorted(expected['staged_internal_links' if staged else 'internal_links']),'internal links changed, including case and CTA links')
 return errors

def mathematical_checks():
 """Independently check published examples and 2026 endpoint behavior."""
 count=0
 def eq(a,b):
  nonlocal count
  assert a==b,(a,b);count+=1
 def component(q,w,u):return min(D('.2')*D(q),max(D('.5')*D(w),D('.25')*D(w)+D('.025')*D(u)))
 def phase(q,w,u,taxable,threshold,width,sstb=False):
  ratio=max(D(0),min(D(1),(D(taxable)-D(threshold))/D(width)))
  percentage=1-ratio if sstb else D(1)
  q,w,u=(D(x)*percentage for x in (q,w,u))
  tentative=D('.2')*q
  limit=max(D('.5')*w,D('.25')*w+D('.025')*u)
  return tentative-max(D(0),tentative-limit)*ratio
 for threshold,width in [(403500,150000),(201775,75000),(201750,75000)]:
  eq(phase(100000,0,0,threshold-1,threshold,width),D(20000))
  eq(phase(100000,0,0,threshold,threshold,width),D(20000))
  eq(phase(100000,0,0,D(threshold)+D(width)/2,threshold,width),D(10000))
  eq(phase(100000,0,0,threshold+width,threshold,width),D(0))
  eq(phase(100000,100000,0,threshold+width-1,threshold,width,sstb=True)>0,True)
  eq(phase(100000,100000,0,threshold+width,threshold,width,sstb=True),D(0))
  eq(phase(100000,0,0,D(threshold)+D(width)/2,threshold,width,sstb=True),D(5000))
 eq(component(2000000,1200000,0),D(400000));eq(component(2000000,400000,8000000),D(300000));eq(component(400000,0,2000000),D(50000))
 eq(max(D('.5')*200000,D('.25')*200000+D('.025')*(1200000+800000)),D(100000))
 eq(D(1200000)+D(800000),D(2000000))
 for wage,expected in [(150000,75000),(200000,100000),(250000,90000)]:eq(component(700000-wage,wage,0),D(expected))
 eq(D(700000)*2/7,D(200000));eq(D(20000)*D('.37'),D(7400));eq(D(7400)-D(15300),D(-7900))
 eq(component(300000,200000,0)-component(400000,100000,0),D(10000))
 eq(component(500000,200000,0)-(component(300000,200000,0)+component(200000,0,0)),D(40000))
 eq(component(1200000,450000,3000000),3*component(400000,150000,1000000))
 # Regular overall cap removes net capital gain and qualified dividends.
 eq(min(D(20000),D('.2')*(D(100000)-D(20000)-D(5000))),D(15000))
 # Active-business floor is separate from the ordinary formula, applies at >= $1,000.
 minimum=lambda ordinary,active_qbi:max(D(ordinary),D(400)) if D(active_qbi)>=1000 else D(ordinary)
 eq(minimum(200,999),D(200));eq(minimum(200,1000),D(400));eq(minimum(500,1000),D(500))
 return count

def ownership_checks(root,baseline):
 errors=[]
 if not (root/'cluster_c1.py').exists():return errors
 def drop_qbi(tree):
  tree.body=[n for n in tree.body if not(isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='QBI_MAX' for t in n.targets))];return ast.dump(tree)
 if drop_qbi(ast.parse((root/'cluster_c1.py').read_text()))!=drop_qbi(ast.parse((baseline/'cluster_c1.py').read_text())):errors.append('cluster_c1.py: non-QBI AST changed')
 # Stronger byte preservation of everything before and after the assignment.
 def split_qbi(p):
  s=p.read_text();lines=s.splitlines(keepends=True);n=next(n for n in ast.parse(s).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='QBI_MAX' for t in n.targets));return ''.join(lines[:n.lineno-1]),''.join(lines[n.end_lineno:])
 if split_qbi(root/'cluster_c1.py')!=split_qbi(baseline/'cluster_c1.py'):errors.append('cluster_c1.py: non-QBI bytes changed')
 def non_qbi(p):
  s=p.read_text();a=s.index('"qbi": [');b=s.index('\n"audit": [',a);return s[:a],s[b:]
 if non_qbi(root/'seo_topics.py')!=non_qbi(baseline/'seo_topics.py'):errors.append('seo_topics.py: non-QBI bytes changed')
 faq_tree=ast.parse((root/'seo_topics.py').read_text())
 banks=[n for n in ast.walk(faq_tree) if isinstance(n,ast.Dict) and any(isinstance(k,ast.Constant) and k.value=='qbi' and isinstance(v,ast.List) for k,v in zip(n.keys,n.values))]
 bank=next(ast.literal_eval(v) for n in banks for k,v in zip(n.keys,n.values) if isinstance(k,ast.Constant) and k.value=='qbi')
 overview_faq=next(d for d in schemas((root/PAGES[1]).read_text()) if d.get('@type')=='FAQPage')
 if bank[:4]!=[(q['name'],q['acceptedAnswer']['text']) for q in overview_faq['mainEntity']]:errors.append('seo_topics.py: QBI FAQ/page parity changed')
 # QBI_MAX-owned copy matches visible page and FAQ.
 module=ast.parse((root/'cluster_c1.py').read_text());n=next(n for n in module.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='QBI_MAX' for t in n.targets));data={kw.arg:ast.literal_eval(kw.value) for kw in n.value.keywords}
 s=(root/PAGES[0]).read_text();v=text(block(s,'main'))
 for k in ['h1','subtitle','lead']:
  if text(data[k]) not in v:errors.append('QBI_MAX source/page mismatch: '+k)
 for h,b in data['body']+data['faqs']:
  if text(h) not in v or text(b) not in v:errors.append('QBI_MAX source/page mismatch: '+h)
 return errors

def fixtures(docs,expected,staged=False):
 count=0;path=PAGES[0];good=docs[path]
 def rejected(path,s,label):
  nonlocal count
  assert check_page(path,s,expected[path],staged),label;count+=1
 for stale in STALE:rejected(path,good.replace('</main>','<p>'+stale+'</p></main>'),stale)
 for old,new in [('rel="canonical"','rel="alternate"'),('$201,775','$201,750'),('50% or more common ownership','more than 50% common ownership'),('later of 10 years','earlier of 10 years'),('"datePublished": "2026-08-17"','"datePublished": "2026-11-06"'),('"dateModified": "2026-11-06"','"dateModified": "2025-01-01"'),('"text": "Deductible wages','"text": "UNMATCHED FAQ Deductible wages')]:
  assert old in good,old;rejected(path,good.replace(old,new),old)
 for path,old,new in [(PAGES[1],'limitation remains $100,000','limitation remains $120,000'),(PAGES[2],'$7,900 worse','$7,900 better'),(PAGES[2],'$40,000 increase','$50,000 increase')]:
  assert old in docs[path],old
  rejected(path,docs[path].replace(old,new),old)
 for path in PAGES[1:]:
  assert '$28K' in docs[path]
  rejected(path,docs[path].replace('$28K','$29K'),'reported case-result amount')
 for path in PAGES:
  s=docs[path];case=next((x for x in expected[path]['internal_links'] if 'business-owner-saves' in x),'/case-studies/')
  assert case in s;rejected(path,s.replace(case,'/removed-case/'),'case link')
  rejected(path,s.replace('href="/discovery/"','href="/wrong-destination/"'),'CTA')
 return count

def main():
 ap=argparse.ArgumentParser();ap.add_argument('root',nargs='?',default='.');ap.add_argument('--baseline');ap.add_argument('--data-root');a=ap.parse_args();root=Path(a.root).resolve();data_root=Path(a.data_root).resolve() if a.data_root else Path(__file__).resolve().parents[1]
 expected=json.loads((data_root/'content/qbi-buyer-accuracy-20261106.json').read_text())['pages']
 docs={p:(root/p).read_text() for p in PAGES};staged=root.name=='public';errors=[]
 if staged:
  # Predict only documented release transforms from source that independently
  # passes preservation checks. Never learn allowed changes from public output.
  from tax_review_build_normalization import normalize_baseline_html
  for path,item in expected.items():
   source=(data_root/path).read_text()
   errors+=check_page(path,source,item,False)
   predicted=normalize_baseline_html(source,data_root,'/'+path[:-10])
   item['staged_preserved_sha256']={tag:digest(block(predicted,tag)) for tag in item['preserved_sha256']}
   item['staged_internal_links']=re.findall(r'<a\b[^>]*href="(/[^\"]*)"',predicted)
   for label,protected in item.get('preserved_blocks',{}).items():
    protected['staged_sha256']=digest(re.search(protected['pattern'],predicted,re.S)[0])
 errors += [e for p,s in docs.items() for e in check_page(p,s,expected[p],staged)]
 negatives=fixtures(docs,expected,staged);math=mathematical_checks()
 if a.baseline:
  baseline=Path(a.baseline);errors+=ownership_checks(root,baseline)
  for p in PAGES:
   old=(baseline/p).read_text();s=docs[p]
   for pattern in [r'<meta\s+property="article:published_time"[^>]*>',r'<div class="post-cta">.*?</div>',r'<div class="cta-buttons">.*?</div>']:
    if re.findall(pattern,old,re.S)!=re.findall(pattern,s,re.S):errors.append(p+': preserved publication or CTA block changed')
 xml='\n'.join(p.read_text() for p in root.glob('sitemap*.xml'))
 for p in PAGES:
  if '<loc>'+SITE+'/'+p[:-10]+'</loc>' not in xml:errors.append(p+': sitemap entry missing')
 print(json.dumps({'root':str(root),'pages':len(docs),'negative_fixtures':negatives,'mathematical_boundary_checks':math,'baseline_checked':bool(a.baseline),'errors':errors},indent=2));return bool(errors)
if __name__=='__main__':sys.exit(main())
