"""Publish reviewed existing-page corrections and 100 distinct owner decision briefs."""
from pathlib import Path
import re,json,html,csv,sys
ROOT=Path(__file__).resolve().parents[1]
DATE='2026-10-28'; SITE='https://www.aetaxadvisors.com'
def esc(s):return html.escape(s,quote=True)
def inline(s):
 s=esc(s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:'<a href="'+m[2]+'">'+m[1]+'</a>',s)
 s=re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',s)
 return s

def markdown(s):
 lines=s.strip().splitlines();out=[];i=0
 while i<len(lines):
  l=lines[i].strip()
  if not l:i+=1;continue
  if l.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    row=[x.strip() for x in lines[i].strip().strip('|').split('|')]
    if not all(re.fullmatch(r':?-+:?',x) for x in row):rows.append(row)
    i+=1
   out.append('<div class="ae-table-scroll" role="region" aria-label="Decision comparison" tabindex="0"><table class="blog-table"><thead><tr>'+''.join('<th scope="col">'+inline(x)+'</th>' for x in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(x)+'</td>' for x in row)+'</tr>' for row in rows[1:])+'</tbody></table></div>');continue
  m=re.match(r'^(#{1,6}) (.*)',l)
  if m:out.append('<h'+str(len(m[1]))+'>'+inline(m[2])+'</h'+str(len(m[1]))+'>');i+=1;continue
  if l.startswith('- '):
   items=[]
   while i<len(lines) and lines[i].strip().startswith('- '):items.append('<li>'+inline(lines[i].strip()[2:])+'</li>');i+=1
   out.append('<ul>'+''.join(items)+'</ul>');continue
  p=[l];i+=1
  while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','- ')):p.append(lines[i].strip());i+=1
  out.append('<p>'+inline(' '.join(p))+'</p>')
 return '\n'.join(out)

def metadata(s,title,desc,url,published=None):
 s=re.sub(r'<title>.*?</title>','<title>'+esc(title)+'</title>',s,flags=re.S)
 for k,v in {'description':desc,'og:title':title,'og:description':desc,'og:url':url,'twitter:title':title,'twitter:description':desc,'article:modified_time':DATE+'T12:00:00-04:00'}.items():
  s=re.sub(r'(<meta (?:name|property)="'+re.escape(k)+r'" content=")[^"]*("\s*/?>)',lambda m:m[1]+esc(v)+m[2],s)
 s=re.sub(r'(<link rel="canonical" href=")[^"]+',lambda m:m[1]+url,s)
 s=re.sub(r'(<link rel="alternate" hreflang="en" href=")[^"]+',lambda m:m[1]+url,s)
 if published:s=re.sub(r'(<meta property="article:published_time" content=")[^"]+',lambda m:m[1]+published,s)
 return s

def render(path,title,desc,body,published=DATE,sources=None):
 template=(ROOT/'ptet-election-by-state/index.html').read_text()
 pre=template[:template.index('<main')];post=template[template.index('</main>')+len('</main>'):]
 pre=re.sub(r'<script\b[^>]*type="application/ld\+json"[^>]*>.*?</script>','',pre,flags=re.S)
 url=SITE+path
 pre=metadata(pre,title,desc,url,published)
 ld=[{'@context':'https://schema.org','@type':'Article','headline':title,'description':desc,'url':url,'mainEntityOfPage':url,'datePublished':published[:10],'dateModified':DATE,'author':{'@type':'Organization','name':'AE Tax Advisors','url':SITE+'/'},'publisher':{'@type':'Organization','name':'AE Tax Advisors','url':SITE+'/'},'citation':sources or []}, {'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':SITE+'/'},{'@type':'ListItem','position':2,'name':title,'item':url}]}]
 pre=pre.replace('</head>','<script type="application/ld+json">'+json.dumps(ld).replace('</','<\\/')+'</script></head>')
 body=re.sub(r'<h1>.*?</h1>','',body,count=1,flags=re.S)
 return pre+'<main><section class="page-header"><div class="container narrow"><nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/blog/">Tax planning guides</a></nav><h1>'+esc(title)+'</h1><p>'+esc(desc)+'</p><p>By AE Tax Advisors Team · Updated October 28, 2026</p></div></section><section class="content-section"><div class="container narrow">'+body+'</div></section></main>'+post

def write(path,s):
 p=ROOT/path.strip('/')/'index.html';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)

def update_existing():
 pack=(ROOT/'content/owner-faqs-20261028/existing-page-updates.md').read_text()
 assets=pack.split('## Asset ')
 updated=[]
 for n,path in [(1,'/ptet-election-by-state/'),(2,'/amended-tax-returns/')]:
  txt=assets[n];title=re.search(r'\*\*SEO title:\*\* (.*)',txt)[1].strip();desc=re.search(r'\*\*Meta description:\*\* (.*)',txt)[1].strip()
  body=txt[txt.index('\n# '):].split('\n---')[0]
  heading=re.search(r'^# (.*)',body,re.M)[1]
  old=(ROOT/path.strip('/')/'index.html').read_text();pub=re.search(r'"datePublished"\s*:\s*"([^"]+)"',old)[1]
  s=render(path,title,desc,markdown(body),pub,re.findall(r'\]\((https://(?:www\.)?(?:irs.gov|law.cornell.edu|tax.ny.gov|ftb.ca.gov|nj.gov)[^)]+)\)',body))
  s=s.replace('<h1>'+esc(title)+'</h1>','<h1>'+esc(heading)+'</h1>')
  write(path,s);updated.append(path)
 module=assets[3]
 sub=module.split('### The owner is planning a QSBS stock sale')[1].split('### Short correction')[0]
 path='/c-corporation-strategy/c-corp-vs-s-corp/';p=ROOT/path.strip('/')/'index.html';s=p.read_text()
 s,n=re.subn(r'<h3>The Owner Plans a QSBS Exit</h3>.*?(?=<h3>)','<h3>The Owner Plans a QSBS Exit</h3>'+markdown(sub),s,flags=re.S);assert n==1
 row=markdown(module.split('### Replacement table row')[1].split('### The owner')[0])
 row=re.search(r'<tbody>(.*?)</tbody>',row,re.S)[1]
 s,n=re.subn(r'<tr>\s*<td>(?:QSBS Eligibility|QSBS)</td>.*?</tr>',lambda m:row,s,flags=re.S);assert n==1
 s=s.replace('the five-year holding period before a planned exit','the applicable holding period before a planned exit')
 title=re.search(r'\*\*Suggested SEO title:\*\* (.*)',module)[1].strip();desc=re.search(r'\*\*Meta description:\*\* (.*)',module)[1].strip()
 s=metadata(s,title,desc,SITE+path)
 def fixld(m):
  obj=json.loads(m[1])
  if obj.get('@type')=='Article':obj.update(description=desc,dateModified=DATE)
  return '<script type="application/ld+json">'+json.dumps(obj)+'</script>'
 s=re.sub(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',fixld,s,flags=re.S)
 p.write_text(s);updated.append(path)
 path='/business-owner-exit-strategy/';p=ROOT/path.strip('/')/'index.html';s=p.read_text()
 short=module.split('Replace its blanket QSBS limit paragraph with:')[1].split('\n---')[0].strip().strip('“”')
 s,n=re.subn(r'<h2>IRC Section 1202 QSBS Exclusion</h2>.*?(?=<h2>)','<h2>IRC Section 1202 QSBS Exclusion</h2>'+markdown(short),s,flags=re.S);assert n==1
 ans='QSBS qualification depends on acquisition and issuance dates, original issuance, business eligibility, holding period and other Section 1202 requirements. Newer stock has different rules. Review the records before estimating an exclusion.'
 s=re.sub(r'(<h3>What is IRC Section 1202 QSBS and does it apply to business owners\?</h3>)<p>.*?</p>',lambda m:m[1]+'<p>'+ans+'</p>',s,flags=re.S)
 def fixfaq(m):
  obj=json.loads(m[1])
  if obj.get('@type')=='FAQPage':
   for q in obj.get('mainEntity',[]):
    if 'What is IRC Section 1202' in q.get('name',''):q['acceptedAnswer']['text']=ans
  if obj.get('@type') in ['Article','BlogPosting','WebPage']:obj['dateModified']=DATE
  return '<script type="application/ld+json">'+json.dumps(obj)+'</script>'
 s=re.sub(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',fixfaq,s,flags=re.S)
 s=re.sub(r'(<meta property="article:modified_time" content=")[^"]+',lambda m:m[1]+DATE+'T12:00:00-04:00',s)
 p.write_text(s);updated.append(path)
 return updated


GROUPS={
 'owner-pay':dict(name='Owner compensation',service='/services/reasonable-compensation/',sources=['https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues','https://www.irs.gov/publications/p15'],context='Compensation review connects the work performed with the employer reporting it. Keep wage analysis separate from ownership rights and available cash. The payroll provider processes payments and forms; the tax advisor reviews their treatment. When the operating arrangement changes, update the record of duties and revisit the forecast instead of carrying forward a salary chosen under different facts.'),
 'owner-loans':dict(name='Shareholder loans and funding',service='/business-owner-small-business-tax/',sources=['https://www.irs.gov/instructions/i7203','https://www.irs.gov/publications/p550'],context='Shareholder funding has both a legal balance and a tax history. Advances, repayments and losses can change different parts of that history. Preserve the actual sequence of transactions, including money returned to the owner. Where a loan is involved, the person preparing the owner return needs the underlying workpapers rather than only the company balance sheet.'),
 'multiple-entities':dict(name='Multiple-business coordination',service='/business-owner-small-business-tax/',sources=['https://www.irs.gov/publications/p583','https://www.law.cornell.edu/uscode/text/26/482'],context='Common ownership does not eliminate the need to explain transactions between businesses. Start with the parties, the benefit provided and the actual cash movement. Matching records on both sides make a proposed treatment easier to evaluate. Separate questions about legal authority and contracts from the accounting and tax entries; an entry cannot supply an agreement that never existed.'),
 'business-purchases':dict(name='Buying a business',service='/retirement-exit-ma-tax-strategy/',sources=['https://www.irs.gov/instructions/i8594','https://www.irs.gov/publications/p544'],context='An acquisition handoff should connect the executed agreement, final price and opening books. Working-capital schedules, asset allocations and transition arrangements answer different questions. Keep the final version of each and identify who resolves discrepancies. If the contract changes after an initial model, update the workpapers before using them for depreciation, income recognition or a filed acquisition form.'),
 'selling-business':dict(name='Selling and winding down',service='/retirement-exit-ma-tax-strategy/',sources=['https://www.irs.gov/publications/p537','https://www.irs.gov/publications/p544'],context='A seller can have reporting obligations after the closing proceeds arrive. Keep operating income, sale consideration, interest and service payments identifiable. Update the transaction workpaper when the buyer pays, disputes or changes an amount. The signed documents and prior reporting should be read together before deciding whether a later event changes this year, a previous year or both.'),
 'retirement-plans':dict(name='Owner retirement commitments',service='/retirement-exit-ma-tax-strategy/',sources=['https://www.irs.gov/publications/p560','https://www.irs.gov/retirement-plans/one-participant-401k-plans'],context='Plan design, funding and income-tax deductions are connected but distinct. Give the administrator complete ownership, employee and payroll information. For a defined benefit plan, involve the actuary in funding changes. Record who confirms eligibility, who calculates contributions and who funds them, with actual completion evidence rather than assuming a recommendation was implemented.'),
 'owner-expenses':dict(name='Expenses and reimbursements',service='/business-owner-small-business-tax/',sources=['https://www.irs.gov/publications/p463','https://www.irs.gov/publications/p583'],context='Expense review begins with what was bought, who benefited and which taxpayer incurred the cost. Payment evidence supports the amount; business purpose and any special substantiation rules need their own support. Track refunds and reimbursements so one cost is not deducted twice. For a mixed personal and business item, retain the allocation method with the underlying records.'),
 'estimated-taxes':dict(name='Tax payments and owner cash',service='/business-owner-small-business-tax/',sources=['https://www.irs.gov/publications/p505','https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes'],context='A payment forecast needs the whole taxpayer picture, not only the operating company profit. Use actual payment dates, withholding and known household income. Keep the projected final liability separate from the installments used to manage underpayment exposure. Reconcile federal and state accounts independently, and update assumptions when a transaction or income event materially changes the year.'),
 'ownership-changes':dict(name='Changing ownership',service='/business-owner-small-business-tax/',sources=['https://www.irs.gov/publications/p541','https://www.irs.gov/instructions/i1120s'],context='Ownership changes need a common effective date across legal documents, capitalization records and tax workpapers. A negotiated company value is not automatically a tax-basis amount. Identify who transfers what and who receives cash, equity or other rights. Review entity-specific eligibility before implementing a transfer, particularly where a trust, another company or a new investor enters the ownership chain.'),
 'employees-benefits':dict(name='Employees and owner benefits',service='/business-owner-small-business-tax/',sources=['https://www.irs.gov/publications/p15b','https://www.irs.gov/publications/p15'],context='A benefit can be a legitimate business cost while still requiring wage reporting. Determine the recipient, ownership relationship and actual arrangement before deciding whether an exclusion applies. Coordinate payroll before year-end forms are prepared. If a payment has already been reported, ask which corrections are necessary rather than assuming a new expense code fixes the employer and employee records.')
}
LABELS={
'https://www.irs.gov/instructions/i7203':'IRS Form 7203 instructions: shareholder basis',
'https://www.irs.gov/publications/p538':'IRS Publication 538: accounting periods and methods',
'https://www.irs.gov/publications/p550':'IRS Publication 550: investment income and expenses',
'https://www.irs.gov/publications/p583':'IRS Publication 583: business records',
'https://www.irs.gov/publications/p463':'IRS Publication 463: travel, gifts and vehicles',
'https://www.irs.gov/publications/p537':'IRS Publication 537: installment sales',
'https://www.irs.gov/publications/p544':'IRS Publication 544: asset dispositions',
'https://www.irs.gov/publications/p560':'IRS Publication 560: small-business retirement plans',
'https://www.irs.gov/publications/p505':'IRS Publication 505: withholding and estimated tax',
'https://www.irs.gov/publications/p541':'IRS Publication 541: partnerships',
'https://www.irs.gov/publications/p15b':'IRS Publication 15-B: fringe benefits',
'https://www.irs.gov/publications/p15':'IRS Publication 15: employer tax guide',
'https://www.irs.gov/instructions/i8594':'IRS Form 8594 instructions: acquisition allocation',
'https://www.irs.gov/instructions/i1120s':'IRS Form 1120-S instructions',
'https://www.law.cornell.edu/uscode/text/26/482':'Section 482: related-party allocations',
'https://www.irs.gov/retirement-plans/one-participant-401k-plans':'IRS guidance: one-participant 401(k) plans',
'https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes':'IRS estimated-tax guidance',
'https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues':'IRS guidance: S-corporation compensation and insurance'
}
def load_briefs():
 rows=[];group=None
 for line in (ROOT/'content/owner-faqs-20261028/briefs.txt').read_text().splitlines():
  if line.startswith('['):group=line.strip('[]');continue
  if not line:continue
  bits=line.split('|');assert len(bits)==8,line
  row=dict(zip(['slug','title','answer','scenario','steps','records','trap','deliverable'],bits));row['group']=group;row['path']='/blog/'+row['slug']+'/'
  row['steps']=row['steps'].split(';');row['records']=row['records'].split(';');rows.append(row)
 assert len(rows)==100
 assert len(set(r['path'] for r in rows))==100
 return rows

FORKS=dict(line.split('|',1) for line in (ROOT/'content/owner-faqs-20261028/decision-forks.txt').read_text().splitlines() if line)

def faq_body(r,peers):
 g=GROUPS[r['group']]
 sources=list(g['sources'])
 if r['slug']=='owner-prepays-three-years-software':sources.append('https://www.irs.gov/publications/p538')
 if r['slug']=='partner-tax-distributions-different-state-rates':sources.append('https://www.irs.gov/publications/p541')
 def p(s):return '<p>'+esc(s)+'</p>'
 def h(s):return '<h2>'+esc(s)+'</h2>'
 def ul(xs,tag='ul'):return '<'+tag+'>'+''.join('<li>'+esc(x)+'.</li>' for x in xs)+'</'+tag+'>'
 s=p(r['answer'])+h('A business-owner scenario')+p(r['scenario'])+'<p><small>Illustrative scenario, not a client result.</small></p>'
 s+=h('Work through the transaction')+ul(r['steps'],'ol')
 s+=h('The mistake that changes the result')+p(r['trap'])
 s+=h('Records that resolve the question')+ul(r['records'])
 s+=h('The decision to document')+p(r['deliverable'])
 s+=h('Which fact changes the answer?')+p(FORKS[r['slug']])
 s+='<p><a href="'+g['service']+'">Explore '+esc(g['name'].lower())+' advisory</a> · <a href="/discovery/">Discuss your situation with AE Tax Advisors</a></p>'
 s+='<h2>Related owner questions</h2><ul>'+''.join('<li><a href="'+q['path']+'">'+esc(q['title'])+'</a></li>' for q in peers)+'</ul>'
 s+='<h2>Sources and scope</h2><ul>'+''.join('<li><a href="'+url+'">'+esc(LABELS[url])+'</a></li>' for url in sources)+'</ul>'
 s+='<p>General educational information prepared with AI assistance. No individual professional review is represented. Apply the relevant tax-year rules to the actual records. <a href="/editorial-policy/">Editorial policy</a> · <a href="/ai-disclosure/">AI disclosure</a>.</p>'
 return s

def expand():
 rows=load_briefs();manifest=[]
 seo_titles=(ROOT/'content/owner-faqs-20261028/seo-titles.txt').read_text().splitlines()
 assert len(seo_titles)==len(rows)
 assert all(len(t)<=60 for t in seo_titles),[(t,len(t)) for t in seo_titles if len(t)>60]
 holds=json.loads((ROOT/'discovery_review_holds.json').read_text());config=json.loads((ROOT/'vercel.json').read_text());redirects={x['source'].rstrip('/') for x in config.get('redirects',[])}
 for i,r in enumerate(rows):
  path=r['path'];p=ROOT/path.strip('/')/'index.html'
  assert path not in holds and path.rstrip('/') not in redirects,path
  if p.exists():assert 'owner-faq-batch:20261028' in p.read_text(),'Existing route: '+path
  peers=[x for x in rows if x['group']==r['group'] and x['path']!=path]
  peers=peers[i%9:i%9+2] if i%9<8 else peers[-2:]
  title=r['title']
  desc=r['answer'].split('. ')[0].rstrip('.')+'.'
  if len(desc)<70:desc=seo_titles[i]+'. Review the facts, records and next steps for your business.'
  if len(desc)>155:desc='A business-owner guide to '+r['slug'].replace('-',' ')+'. Review the facts, records and next decision.'
  if len(desc)>160:desc='Review '+r['slug'].replace('-',' ')+': a practical scenario, required records and next steps.'
  s=render(path,title,desc,faq_body(r,peers),sources=GROUPS[r['group']]['sources'])
  s=metadata(s,seo_titles[i],desc,SITE+path)
  s=s.replace('<main>','<!-- owner-faq-batch:20261028 --><main>',1)
  write(path,s)
  manifest.append(dict(path=path,title=title,seo_title=seo_titles[i],description=desc,group=r['group'],primary_keyword=r['slug'].replace('-',' '),sources=GROUPS[r['group']]['sources'],related=[x['path'] for x in peers]))
 # Existing hubs provide discovery; no extra landing pages are counted among the 100.
 def links_for(selected):
  s=''
  for key,g in GROUPS.items():
   bucket=[r for r in selected if r['group']==key]
   if bucket:s+='<h3>'+esc(g['name'])+'</h3><ul>'+''.join('<li><a href="'+r['path']+'">'+esc(r['title'])+'</a></li>' for r in bucket)+'</ul>'
  return s
 def block(s):return '<!-- owner-faqs-20261028:start --><section class="content-section"><div class="container narrow"><h2>Specific questions business owners ask</h2>'+s+'</div></section><!-- owner-faqs-20261028:end -->'
 discovery={
  'blog/index.html':rows,'sitemap/index.html':rows,
  'business-owner-small-business-tax/index.html':[r for i,r in enumerate(rows) if r['group'] not in ['business-purchases','selling-business','retirement-plans'] and i%10<2],
  'retirement-exit-ma-tax-strategy/index.html':[r for i,r in enumerate(rows) if r['group'] in ['business-purchases','selling-business','retirement-plans'] and i%10<2],
  'services/reasonable-compensation/index.html':[r for r in rows if r['group']=='owner-pay']}
 for f,selected in discovery.items():
  p=ROOT/f;s=p.read_text()
  if f=='sitemap/index.html':s=s.replace('1565 pages in total.','1665 pages in total.')
  s=re.sub(r'<!-- owner-faqs-20261028:start -->.*?<!-- owner-faqs-20261028:end -->','',s,flags=re.S)
  s=s.replace('</main>',block(links_for(selected))+'</main>',1);p.write_text(s)
 xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>'+SITE+r['path']+'</loc><lastmod>'+DATE+'</lastmod></url>\n' for r in rows)+'</urlset>\n'
 (ROOT/'sitemap-owner-faqs-20261028.xml').write_text(xml)
 for f in ['sitemap_index.xml','sitemap-index.xml']:
  p=ROOT/f;s=p.read_text();entry='<sitemap><loc>'+SITE+'/sitemap-owner-faqs-20261028.xml</loc><lastmod>'+DATE+'</lastmod></sitemap>'
  if 'sitemap-owner-faqs-20261028.xml' not in s:s=s.replace('</sitemapindex>',entry+'\n</sitemapindex>')
  p.write_text(s)
 # Register in the existing aggregate sitemap as well.
 p=ROOT/'sitemap.xml';s=p.read_text()
 for r in rows:
  if SITE+r['path'] not in s:s=s.replace('</urlset>','<url><loc>'+SITE+r['path']+'</loc><lastmod>'+DATE+'</lastmod></url>\n</urlset>')
 p.write_text(s)
 dest=ROOT/'content/owner-faqs-20261028'
 (dest/'manifest.json').write_text(json.dumps(dict(date=DATE,pages=manifest,discovery=list(discovery)),indent=2)+'\n')
 return manifest

if __name__=='__main__':
 updated=update_existing()
 added=expand()
 print('Updated',len(updated),'existing pages; rendered',len(added),'new business-owner FAQs.')
