"""Render the fourth 100-page release without changing earlier FAQ content."""
from pathlib import Path
import runpy,json,re,html
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/'content/owner-faqs-20261029-d';DATE='2026-10-29';SITE='https://www.aetaxadvisors.com'
shared=runpy.run_path(str(ROOT/'scripts/seo-expansion-20261028.py'));render=shared['render'];metadata=shared['metadata'];esc=shared['esc']
SOURCES={
'crosscredit':('https://www.irs.gov/irm/part5/irm_05-019-014r','IRS collection manual: cross-referencing trust-fund payments'),
'oicappeal':('https://www.irs.gov/taxtopics/tc204','IRS Topic 204: returned and rejected offers'),
'se':('https://www.irs.gov/instructions/i1040sse','IRS Schedule SE instructions: optional methods'),
'2210f':('https://www.irs.gov/instructions/i2210f','IRS Form 2210-F instructions: farmer estimated-tax rules'),
'ezrelief':('https://www.irs.gov/retirement-plans/penalty-relief-program-for-form-5500-ez-late-filers','IRS: penalty relief for eligible Form 5500-EZ late filers'),
'conditional':('https://www.law.cornell.edu/cfr/text/26/1.170A-1','Treasury regulation 1.170A-1: completed and conditional contributions'),
'6655':('https://www.law.cornell.edu/cfr/text/26/1.6655-2','Treasury regulation 1.6655-2: corporate annualized installments'),
'224':('https://www.law.cornell.edu/uscode/text/26/224','Section 224: qualified tip deduction'),
'1055':('https://www.law.cornell.edu/uscode/text/29/1055','ERISA Section 205: survivor annuities and spousal consent'),
'payee':('https://www.irs.gov/businesses/small-businesses-self-employed/understanding-employment-taxes','IRS: employer reporting and employment taxes'),
'15':('https://www.irs.gov/publications/p15','IRS Publication 15: employment taxes and tips'),
'531':('https://www.irs.gov/publications/p531','IRS Publication 531: tip reporting'),
'45b':('https://www.law.cornell.edu/uscode/text/26/45B','Section 45B: credit for employer taxes on tips'),
'8027':('https://www.irs.gov/instructions/i8027','IRS Form 8027 instructions: tip allocations'),
'8846':('https://www.irs.gov/pub/irs-pdf/f8846.pdf','IRS Form 8846 instructions: employer tip credit'),
'225':('https://www.irs.gov/publications/p225','IRS Publication 225: farmer tax guide'),
'2290':('https://www.irs.gov/instructions/i2290','IRS Form 2290 instructions: heavy highway vehicle use tax'),
'510':('https://www.irs.gov/publications/p510','IRS Publication 510: excise taxes'),
'720':('https://www.irs.gov/instructions/i720','IRS Form 720 instructions: excise reporting and adjustments'),
'4136':('https://www.irs.gov/instructions/i4136','IRS Form 4136 instructions: fuel-tax credits'),
'5500':('https://www.irs.gov/pub/irs-pdf/i5500ez.pdf','IRS Form 5500-EZ instructions: one-participant plans'),
'560':('https://www.irs.gov/publications/p560','IRS Publication 560: small-business retirement plans'),
'575':('https://www.irs.gov/publications/p575','IRS Publication 575: pension distributions and plan loans'),
'590':('https://www.irs.gov/publications/p590b','IRS Publication 590-B: IRA distributions and rollovers'),
'dol':('https://www.irs.gov/retirement-plans/retirement-plan-fiduciary-responsibilities','IRS: retirement-plan fiduciary responsibilities'),
'late':('https://www.irs.gov/retirement-plans/401k-plan-fix-it-guide-you-havent-timely-deposited-employee-elective-deferrals','IRS: correcting late employee deferrals'),
'988':('https://www.law.cornell.edu/uscode/text/26/988','Section 988: foreign-currency transactions'),
'hedge':('https://www.law.cornell.edu/cfr/text/26/1.1221-2','Treasury regulation 1.1221-2: tax hedging identification'),
'currency':('https://www.irs.gov/individuals/international-taxpayers/foreign-currency-and-currency-exchange-rates','IRS: functional currency and exchange rates'),
'blocked':('https://www.irs.gov/publications/p54','IRS Publication 54: blocked income and foreign-currency restrictions'),
'514':('https://www.irs.gov/publications/p514','IRS Publication 514: foreign-tax redeterminations'),
'170':('https://www.law.cornell.edu/uscode/text/26/170','Section 170: charitable deductions and limitations'),
'526':('https://www.irs.gov/publications/p526','IRS Publication 526: charitable contributions'),
'561':('https://www.irs.gov/publications/p561','IRS Publication 561: donated property and subsequent dispositions'),
'541':('https://www.irs.gov/publications/p541','IRS Publication 541: partnership charitable contributions'),
'disaster':('https://www.irs.gov/newsroom/tax-relief-in-disaster-situations','IRS: disaster-specific tax relief announcements'),
'547':('https://www.irs.gov/publications/p547','IRS Publication 547: casualty losses and disaster elections'),
'139':('https://www.law.cornell.edu/uscode/text/26/139','Section 139: qualified disaster-relief payments'),
'594':('https://www.irs.gov/pub/irs-pdf/p594.pdf','IRS Publication 594: collection process and rights'),
'433':('https://www.irs.gov/pub/irs-pdf/f433b.pdf','IRS Form 433-B: business collection financial statement'),
'656':('https://www.irs.gov/pub/irs-pdf/f656b.pdf','IRS Form 656 booklet: offer-in-compromise requirements'),
'interest':('https://www.irs.gov/payments/interest','IRS: interest on tax debts'),
'538':('https://www.irs.gov/publications/p538','IRS Publication 538: accounting periods and methods'),
'2220':('https://www.irs.gov/instructions/i2220','IRS Form 2220 instructions: corporate estimated-tax installments'),
'4466':('https://www.irs.gov/instructions/i4466','IRS Form 4466 instructions: quick refund of corporate estimates'),
'icdisc':('https://www.irs.gov/instructions/i1120icd','IRS Form 1120-IC-DISC instructions: qualification and reporting'),
'994':('https://www.law.cornell.edu/uscode/text/26/994','Section 994: IC-DISC commission pricing'),
'995':('https://www.law.cornell.edu/uscode/text/26/995','Section 995: IC-DISC distributions and tax-exempt shareholders'),
'991':('https://www.law.cornell.edu/uscode/text/26/991','Section 991: IC-DISC corporate treatment'),
'993':('https://www.law.cornell.edu/uscode/text/26/993','Section 993: qualified export receipts and property'),
'icreg':('https://www.law.cornell.edu/cfr/text/26/1.994-1','Treasury regulation 1.994-1: IC-DISC transaction pricing and payment')}
GROUPS={
'tips':('Tip reporting and employer credits',['15','531']),
'farm':('Farm-business tax decisions',['225']),
'excise':('Special business excise-tax situations',['510']),
'plans':('Retirement-plan administration',['560']),
'currency':('Business currency and cross-border accounting',['988','currency']),
'charity':('Business charitable contributions',['170','526']),
'disaster':('Business disaster relief and recovery',['disaster','547']),
'collections':('Tax collection notices and financial records',['594']),
'periods':('Tax years and corporate installments',['538']),
'exports':('IC-DISC qualification and export transactions',['icdisc','993'])}
EXTRA={
'trustfund-tax-paid-business-person-credit':['crosscredit'],
'business-oic-returned-versus-rejected-appeal':['oicappeal','656'],
'farmer-estimated-tax-gross-income-qualification':['2210f'],
'farm-optional-method-self-employment-loss':['se'],
'late-solo401k-5500ez-irs-penalty-program':['ezrelief','5500'],
'conditional-business-donation-refundable-project':['conditional'],
'corporate-estimated-tax-extraordinary-asset-sale':['2220','6655'],
'tip-deduction-employee-claim-employer-fica':['224','payee'],
'retirement-plan-beneficiary-spouse-consent':['1055'],
'restaurant-allocated-tips-w2-withholding':['8027'],
'large-food-establishment-form8027-multiple-sites':['8027'],
'tip-credit-beauty-business-expansion-2025':['45b','8846'],
'tip-credit-employer-payroll-deduction-coordination':['45b','8846'],
'heavy-truck-2290-first-use-midmonth':['2290'],
'heavy-truck-low-mileage-suspension-crossed':['2290'],
'heavy-truck-sold-schedule1-tax-credit':['2290'],
'heavy-truck-gross-weight-increase-amendment':['2290'],
'heavy-truck-form2290-ein-brand-new':['2290'],
'tanning-services-refund-excise-adjustment':['720'],
'fuel-tax-credit-offhighway-business-use':['4136'],
'fuel-credit-paid-tax-versus-dyed-diesel':['4136'],
'solo401k-250000-assets-all-owner-plans':['5500'],
'solo401k-final-return-below-asset-threshold':['5500'],
'late-employee-deferrals-business-cash-shortage':['late'],
'401k-loan-default-deemed-distribution-offset':['575'],
'retirement-required-distribution-cannot-rollover':['575'],
'five-percent-owner-still-working-rmd':['575'],
'simple-ira-two-year-rollover-restriction':['590'],
'retirement-plan-investment-fees-personal-payment':['dol'],
'foreign-currency-hedge-identification-timing':['hedge'],
'foreign-tax-credit-refund-redetermination':['514'],
'foreign-currency-restricted-withdrawals-reporting':['blocked'],
'charity-sells-donated-equipment-early-recapture':['561'],
'partnership-charity-owner-basis-limitation':['541'],
'qualified-disaster-payments-employees-wages':['139'],
'business-form433b-asset-values-book-basis':['433'],
'business-offer-compromise-payroll-compliance':['656'],
'business-irs-penalty-appeal-interest-separate':['interest'],
'corporate-estimated-tax-first-year-no-prior-tax':['2220'],
'corporate-estimated-tax-large-corporation-safeharbor':['2220'],
'corporate-estimated-tax-seasonal-income':['2220'],
'corporation-quick-refund-form4466':['4466'],
'icdisc-commission-methods-transaction-grouping':['994','icreg'],
'icdisc-commission-accrual-payment-timing':['icreg'],
'icdisc-shareholder-interest-charge-deferral':['995'],
'icdisc-retirement-account-owner-ubit':['995'],
'icdisc-existing-exporter-separate-corporation':['991']}

def load():
 answers={}
 for l in (DATA/'answers.tsv').read_text().splitlines():
  x=l.split('|');assert len(x)==8
  answers[x[0]]=dict(zip(['slug','answer','scenario','steps','records','trap','fork','decision'],x))
 rows=[]
 for l in (DATA/'questions.tsv').read_text().splitlines():
  group,slug,title,question=l.split('|');assert slug in answers
  r=dict(answers[slug],group=group,seo_title=title,title=question,path='/blog/'+slug+'/')
  r['steps']=r['steps'].split(';');r['records']=r['records'].split(';')
  r['source_keys']=list(dict.fromkeys(GROUPS[group][1]+EXTRA.get(slug,[])))
  r['sources']=[SOURCES[k][0]for k in r['source_keys']]
  r['description']=r['answer'].split('. ')[0].rstrip('.')+'.'
  if len(r['description'])>160:r['description']=r['description'][:156].rsplit(' ',1)[0]+'…'
  assert len(title)<=60 and len(r['description'])<=160
  rows.append(r)
 assert len(rows)==len(answers)==100 and len({r['path']for r in rows})==100
 return rows

def body(r,related):
 p=lambda x:'<p>'+esc(x)+'</p>'
 h=lambda x:'<h2>'+esc(x)+'</h2>'
 ul=lambda xs,tag='ul':'<'+tag+'>'+''.join('<li>'+esc(x.rstrip('.'))+'.</li>'for x in xs)+'</'+tag+'>'
 b=p(r['answer'])+h('A specific business-owner situation')+p(r['scenario'])+'<p><small>Illustrative example, not a client result.</small></p>'
 b+=h('What to establish before filing')+ul(r['steps'],'ol')+h('Which fact changes the answer?')+p(r['fork'])
 b+=h('A mistake to avoid')+p(r['trap'])+h('Records that support the decision')+ul(r['records'])+h('The decision to document')+p(r['decision'])
 b+=('<p>Tax collection disputes and debt settlement require a tax-resolution specialist. AE focuses on proactive planning, tax preparation, amendments and real estate tax strategy.</p>' if r['group']=='collections' else '')
 b+='<p><a href="/business-owner-small-business-tax/">Business-owner tax planning and preparation scope</a> · <a href="/discovery/">Discuss advisory scope with AE</a></p>'
 b+='<h2>Related questions</h2><ul>'+''.join('<li><a href="'+q['path']+'">'+esc(q['title'])+'</a></li>'for q in related)+'</ul>'
 b+='<h2>Sources and editorial context</h2><ul>'+''.join('<li><a href="'+SOURCES[k][0]+'">'+esc(SOURCES[k][1])+'</a></li>'for k in r['source_keys'])+'</ul>'
 b+='<p>General educational information prepared with AI assistance. No individual professional review is claimed. Apply the relevant tax-year rules to the actual records. <a href="/editorial-policy/">Editorial policy</a> · <a href="/ai-disclosure/">AI disclosure</a>.</p>'
 return b

def main():
 rows=load();holds=json.loads((ROOT/'discovery_review_holds.json').read_text());config=json.loads((ROOT/'vercel.json').read_text());redirects={x['source'].rstrip('/')for x in config.get('redirects',[])}
 for i,r in enumerate(rows):
  target=ROOT/r['path'].strip('/')/'index.html'
  assert r['path']not in holds and r['path'].rstrip('/')not in redirects,r['path']
  if target.exists():assert 'owner-faq-batch:20261029-d'in target.read_text(),'Existing route '+r['path']
  peers=[q for q in rows if q['group']==r['group']and q['path']!=r['path']];offset=i%8;related=peers[offset:offset+2]
  s=render(r['path'],r['title'],r['description'],body(r,related),published=DATE,sources=r['sources']);s=metadata(s,r['seo_title'],r['description'],SITE+r['path'])
  s=s.replace('2026-10-28',DATE).replace('Updated October 28, 2026','Updated October 29, 2026')
  s=s.replace('<main>','<!-- owner-faq-batch:20261029-d --><main>',1)
  target.parent.mkdir(parents=True,exist_ok=True);target.write_text(s)
  r['related']=[x['path']for x in related]
 # A separately marked section leaves all earlier links and articles intact.
 def links(selected):
  out=''
  for key,(name,_)in GROUPS.items():
   group=[r for r in selected if r['group']==key]
   if group:out+='<h3>'+esc(name)+'</h3><ul>'+''.join('<li><a href="'+r['path']+'">'+esc(r['title'])+'</a></li>'for r in group)+'</ul>'
  return out
 discovery={'blog/index.html':rows,'sitemap/index.html':rows,'business-owner-small-business-tax/index.html':[r for i,r in enumerate(rows)if i%10==0]}
 for file,selected in discovery.items():
  path=ROOT/file;s=path.read_text();s=re.sub(r'<!-- owner-faqs-20261029-d:start -->.*?<!-- owner-faqs-20261029-d:end -->','',s,flags=re.S)
  if file=='sitemap/index.html':s=s.replace('1865 pages in total.','1965 pages in total.')
  block='<!-- owner-faqs-20261029-d:start --><section class="content-section"><div class="container narrow"><h2>More specific business-owner questions</h2>'+links(selected)+'</div></section><!-- owner-faqs-20261029-d:end -->'
  assert '</main>'in s;s=s.replace('</main>',block+'</main>',1);path.write_text(s)
 xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>'+SITE+r['path']+'</loc><lastmod>'+DATE+'</lastmod></url>\n'for r in rows)+'</urlset>\n'
 (ROOT/'sitemap-owner-faqs-20261029-d.xml').write_text(xml)
 for f in ['sitemap-index.xml','sitemap_index.xml']:
  p=ROOT/f;s=p.read_text();entry='<sitemap><loc>'+SITE+'/sitemap-owner-faqs-20261029-d.xml</loc><lastmod>'+DATE+'</lastmod></sitemap>'
  if 'sitemap-owner-faqs-20261029-d.xml'not in s:s=s.replace('</sitemapindex>',entry+'\n</sitemapindex>')
  p.write_text(s)
 p=ROOT/'sitemap.xml';s=p.read_text()
 for r in rows:
  if SITE+r['path']not in s:s=s.replace('</urlset>','<url><loc>'+SITE+r['path']+'</loc><lastmod>'+DATE+'</lastmod></url>\n</urlset>')
 p.write_text(s)
 (DATA/'manifest.json').write_text(json.dumps({'date':DATE,'batch':'20261029-d','new_pages':100,'pages':rows,'discovery_pages':list(discovery)},indent=2)+'\n')
 print('Rendered 100 additional FAQs; preserved earlier 300 and existing page content.')

if __name__=='__main__':main()
