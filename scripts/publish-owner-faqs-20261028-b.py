"""Render the second 100-page release without changing earlier FAQ content."""
from pathlib import Path
import runpy,json,re,html
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/'content/owner-faqs-20261028-b';DATE='2026-10-28';SITE='https://www.aetaxadvisors.com'
shared=runpy.run_path(str(ROOT/'scripts/seo-expansion-20261028.py'));render=shared['render'];metadata=shared['metadata'];esc=shared['esc']
SOURCES={
'1099':('https://www.irs.gov/businesses/what-to-do-with-form-1099-k','IRS: what to do with Form 1099-K'),
'small':('https://www.irs.gov/publications/p334','IRS Publication 334: small-business tax guide'),
'method':('https://www.irs.gov/publications/p538','IRS Publication 538: accounting methods'),
'basis':('https://www.irs.gov/publications/p551','IRS Publication 551: basis of assets'),
'dep':('https://www.irs.gov/publications/p946','IRS Publication 946: depreciation'),
'debt':('https://www.irs.gov/publications/p4681','IRS Publication 4681: canceled debts and repossessions'),
'loss':('https://www.irs.gov/publications/p547','IRS Publication 547: casualties and thefts'),
'income':('https://www.irs.gov/publications/p525','IRS Publication 525: income and recoveries'),
'start':('https://www.law.cornell.edu/uscode/text/26/195','Section 195: startup expenditures'),
'intangible':('https://www.law.cornell.edu/uscode/text/26/197','Section 197: acquired intangibles'),
'capital':('https://www.law.cornell.edu/uscode/text/26/263','Section 263: capital expenditures'),
'corp':('https://www.irs.gov/publications/p542','IRS Publication 542: corporations'),
'close':('https://www.irs.gov/businesses/small-businesses-self-employed/closing-a-business','IRS: closing a business'),
'records':('https://www.irs.gov/publications/p583','IRS Publication 583: keeping business records'),
'foreign':('https://www.irs.gov/publications/p515','IRS Publication 515: foreign-payee withholding'),
'4562':('https://www.irs.gov/instructions/i4562','IRS Form 4562 instructions: depreciation and amortization'),
'sale':('https://www.irs.gov/publications/p544','IRS Publication 544: sales and dispositions'),
'scorp':('https://www.irs.gov/instructions/i1120s','IRS Form 1120-S instructions'),
'partner':('https://www.irs.gov/publications/p541','IRS Publication 541: partnerships'),
'payroll':('https://www.irs.gov/publications/p15','IRS Publication 15: employer tax guide'),
'research':('https://www.irs.gov/newsroom/working-families-tax-cuts','IRS: current tax-law changes, including research costs'),
'amend':('https://www.irs.gov/filing/file-an-amended-return','IRS: amended-return guidance')}
GROUPS={
'processors':('Merchant accounts and settlements',['1099','small']),
'stock':('Inventory and supplier arrangements',['small','method']),
'contracts':('Customer contracts and noncash receipts',['small','method']),
'borrowing':('Business financing and debt changes',['debt','method']),
'claims':('Insurance, disputes and recoveries',['loss','income']),
'preopening':('Before the business opens',['start','records']),
'rights':('Intellectual property and software rights',['intangible','4562']),
'locations':('Leases and location commitments',['method','4562']),
'closeout':('After operations stop',['close','corp']),
'records':('Book-to-return corrections',['records','amend'])}
EXTRA={
'supplier-tooling-charge-mold-stays-factory':['capital','basis'],
'bulk-spare-parts-equipment-inventory':['dep'],
'demo-inventory-converted-business-use':['dep'],
'scorp-debt-forgiven-after-owner-sells-shares':['scorp'],
'refinance-old-business-debt-fees-unamortized':['capital'],
'merchant-cash-advance-daily-repayments':['capital'],
'equipment-repossessed-remaining-debt-waived':['sale'],
'cofounder-leaves-before-business-opens':['partner'],
'new-product-research-existing-business':['research'],
'foreign-licensor-us-business-royalty-withholding':['foreign'],
'purchase-source-code-versus-development-work':['research'],
'business-sells-domain-keeps-operating-company':['sale'],
'creator-licenses-course-business-revenue':['capital'],
'equipment-sale-leaseback-business-records':['sale'],
'commercial-lease-personal-guaranty-paid-owner':['debt'],
'partnership-final-cash-debt-still-outstanding':['partner'],
'unclaimed-payroll-checks-business-closes':['payroll'],
'same-invoice-expense-and-capitalized-asset':['dep'],
'cash-to-accrual-management-books-tax-method':['method'],
'fiscal-year-business-calendar-year-payroll-reconciliation':['payroll','method']}

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
  r['description']=title+'. A specific owner scenario, the facts that change the answer, and the records needed for a tax review.'
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
 b+='<p><a href="/business-owner-small-business-tax/">Business-owner tax planning and coordination</a> · <a href="/discovery/">Discuss your business and advisory needs</a></p>'
 b+='<h2>Related questions</h2><ul>'+''.join('<li><a href="'+q['path']+'">'+esc(q['title'])+'</a></li>'for q in related)+'</ul>'
 b+='<h2>Sources and editorial context</h2><ul>'+''.join('<li><a href="'+SOURCES[k][0]+'">'+esc(SOURCES[k][1])+'</a></li>'for k in r['source_keys'])+'</ul>'
 b+='<p>General educational information prepared with AI assistance. No individual professional review is claimed. Apply the relevant tax-year rules to the actual records. <a href="/editorial-policy/">Editorial policy</a> · <a href="/ai-disclosure/">AI disclosure</a>.</p>'
 return b

def main():
 rows=load();holds=json.loads((ROOT/'discovery_review_holds.json').read_text());config=json.loads((ROOT/'vercel.json').read_text());redirects={x['source'].rstrip('/')for x in config.get('redirects',[])}
 for i,r in enumerate(rows):
  target=ROOT/r['path'].strip('/')/'index.html'
  assert r['path']not in holds and r['path'].rstrip('/')not in redirects,r['path']
  if target.exists():assert 'owner-faq-batch:20261028-b'in target.read_text(),'Existing route '+r['path']
  peers=[q for q in rows if q['group']==r['group']and q['path']!=r['path']];offset=i%8;related=peers[offset:offset+2]
  s=render(r['path'],r['title'],r['description'],body(r,related),sources=r['sources']);s=metadata(s,r['seo_title'],r['description'],SITE+r['path'])
  s=s.replace('<main>','<!-- owner-faq-batch:20261028-b --><main>',1)
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
  path=ROOT/file;s=path.read_text();s=re.sub(r'<!-- owner-faqs-20261028-b:start -->.*?<!-- owner-faqs-20261028-b:end -->','',s,flags=re.S)
  if file=='sitemap/index.html':s=s.replace('1665 pages in total.','1765 pages in total.')
  block='<!-- owner-faqs-20261028-b:start --><section class="content-section"><div class="container narrow"><h2>More specific business-owner questions</h2>'+links(selected)+'</div></section><!-- owner-faqs-20261028-b:end -->'
  assert '</main>'in s;s=s.replace('</main>',block+'</main>',1);path.write_text(s)
 xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>'+SITE+r['path']+'</loc><lastmod>'+DATE+'</lastmod></url>\n'for r in rows)+'</urlset>\n'
 (ROOT/'sitemap-owner-faqs-20261028-b.xml').write_text(xml)
 for f in ['sitemap-index.xml','sitemap_index.xml']:
  p=ROOT/f;s=p.read_text();entry='<sitemap><loc>'+SITE+'/sitemap-owner-faqs-20261028-b.xml</loc><lastmod>'+DATE+'</lastmod></sitemap>'
  if 'sitemap-owner-faqs-20261028-b.xml'not in s:s=s.replace('</sitemapindex>',entry+'\n</sitemapindex>')
  p.write_text(s)
 p=ROOT/'sitemap.xml';s=p.read_text()
 for r in rows:
  if SITE+r['path']not in s:s=s.replace('</urlset>','<url><loc>'+SITE+r['path']+'</loc><lastmod>'+DATE+'</lastmod></url>\n</urlset>')
 p.write_text(s)
 (DATA/'manifest.json').write_text(json.dumps({'date':DATE,'batch':'20261028-b','new_pages':100,'pages':rows,'discovery_pages':list(discovery)},indent=2)+'\n')
 print('Rendered 100 additional FAQs; preserved earlier 100 and existing page content.')

if __name__=='__main__':main()
