"""Render the third 100-page release without changing earlier FAQ content."""
from pathlib import Path
import runpy,json,re,html
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/'content/owner-faqs-20261028-c';DATE='2026-10-28';SITE='https://www.aetaxadvisors.com'
shared=runpy.run_path(str(ROOT/'scripts/seo-expansion-20261028.py'));render=shared['render'];metadata=shared['metadata'];esc=shared['esc']
SOURCES={
'761':('https://www.law.cornell.edu/uscode/text/26/761','Section 761: partnership definitions and exclusion'),
'761reg':('https://www.law.cornell.edu/cfr/text/26/1.761-2','Treasury regulation 1.761-2: exclusion from partnership provisions'),
'8985':('https://www.irs.gov/instructions/i8985','IRS Form 8985 instructions: pass-through partner reporting'),
'pcm':('https://www.law.cornell.edu/cfr/text/26/1.460-4','Treasury regulation 1.460-4: contract revenue and estimates'),
'producer':('https://www.law.cornell.edu/cfr/text/26/1.263A-2','Treasury regulation 1.263A-2: produced property'),
'de':('https://www.law.cornell.edu/cfr/text/26/301.7701-2','Treasury regulation 301.7701-2: disregarded entities and partner employment'),
'gp':('https://www.law.cornell.edu/cfr/text/26/1.707-1','Treasury regulation 1.707-1: guaranteed-payment reporting'),
'6221':('https://www.law.cornell.edu/uscode/text/26/6221','Section 6221: centralized audit rules and election out'),
'6223':('https://www.law.cornell.edu/uscode/text/26/6223','Section 6223: partnership representative authority'),
'6226':('https://www.law.cornell.edu/uscode/text/26/6226','Section 6226: partner-level audit adjustments'),
'currency':('https://www.irs.gov/individuals/international-taxpayers/foreign-currency-and-currency-exchange-rates','IRS: foreign currency and exchange rates'),
'contracts':('https://www.law.cornell.edu/uscode/text/26/460','Section 460: long-term contracts'),
'contractregs':('https://www.law.cornell.edu/cfr/text/26/1.460-1','Treasury regulation 1.460-1: contract classification and completion'),
'costregs':('https://www.law.cornell.edu/cfr/text/26/1.460-5','Treasury regulation 1.460-5: contract costs'),
'production':('https://www.law.cornell.edu/uscode/text/26/263A','Section 263A: inventory and production capitalization'),
'unicap':('https://www.law.cornell.edu/cfr/text/26/1.263A-1','Treasury regulation 1.263A-1: cost allocation'),
'partner':('https://www.irs.gov/publications/p541','IRS Publication 541: partnerships'),
'profits':('https://www.irs.gov/pub/irs-drop/rp-01-43.pdf','IRS Revenue Procedure 2001-43: unvested profits interests'),
'retirement':('https://www.irs.gov/publications/p560','IRS Publication 560: retirement plans for small business'),
'corp':('https://www.irs.gov/publications/p542','IRS Publication 542: corporations'),
'302':('https://www.law.cornell.edu/uscode/text/26/302','Section 302: stock redemptions'),
'foreign':('https://www.irs.gov/publications/p515','IRS Publication 515: foreign-person withholding'),
'creditforeign':('https://www.irs.gov/publications/p514','IRS Publication 514: foreign tax credits'),
'research':('https://www.irs.gov/instructions/i6765','IRS Form 6765 instructions: research credits and elections'),
'41':('https://www.law.cornell.edu/uscode/text/26/41','Section 41: research-credit requirements'),
'383':('https://www.law.cornell.edu/uscode/text/26/383','Section 383: credit limits after ownership changes'),
'payroll':('https://www.irs.gov/publications/p15','IRS Publication 15: employer tax guide'),
'sick':('https://www.irs.gov/publications/p15a','IRS Publication 15-A: supplemental payroll rules'),
'benefits':('https://www.irs.gov/publications/p15b','IRS Publication 15-B: employee fringe benefits'),
'jury':('https://www.irs.gov/publications/p525','IRS Publication 525: income and jury-duty fees'),
'state':('https://www.tax.ny.gov/pit/file/nonresident-faqs.htm','New York Tax Department: nonresident income and work sourcing'),
'274':('https://www.law.cornell.edu/uscode/text/26/274','Section 274: travel, conventions and entertainment limits'),
'463':('https://www.irs.gov/publications/p463','IRS Publication 463: travel, gifts and car expenses'),
'life':('https://www.law.cornell.edu/uscode/text/26/101','Section 101: life-insurance proceeds and exceptions'),
'8925':('https://www.irs.gov/pub/irs-pdf/f8925.pdf','IRS Form 8925 and instructions: employer-owned life insurance'),
'72':('https://www.law.cornell.edu/uscode/text/26/72','Section 72: policy distributions and contract investment'),
'connelly':('https://www.supremecourt.gov/opinions/23pdf/23-146_i42j.pdf','U.S. Supreme Court: Connelly v. United States'),
'estate':('https://www.irs.gov/publications/p559','IRS Publication 559: estates and income in respect of a decedent'),
'2703':('https://www.law.cornell.edu/uscode/text/26/2703','Section 2703: buy-sell agreements and valuation'),
'8822':('https://www.irs.gov/forms-pubs/about-form-8822-b','IRS Form 8822-B: business account changes'),
'name':('https://www.irs.gov/businesses/business-name-change','IRS: business name changes'),
'2848':('https://www.irs.gov/instructions/i2848','IRS Form 2848 instructions: power of attorney'),
'efile':('https://www.irs.gov/e-file-providers/electronic-communication-between-irs-and-transmitters-during-the-mef-e-file-process','IRS: electronic acknowledgments and rejected returns'),
'id':('https://www.irs.gov/newsroom/when-to-file-a-business-identity-theft-affidavit-with-the-irs','IRS: business identity theft'),
'penalty':('https://www.irs.gov/payments/penalties','IRS: penalties and relief'),
'extension':('https://www.irs.gov/forms-pubs/extension-of-time-to-file-your-tax-return','IRS: extensions of time to file'),
'records':('https://www.irs.gov/publications/p583','IRS Publication 583: business records')}
GROUPS={
'contracts':('Construction contract reporting',['contracts','contractregs','costregs','pcm']),
'production':('Manufacturing cost allocation',['production','unicap']),
'partners':('Working partners and partnership economics',['partner']),
'capital':('Corporate capital and shareholder payments',['corp']),
'foreign':('Cross-border vendors and owners',['foreign']),
'research':('Research-credit claim decisions',['research','41']),
'payroll':('Unusual payroll events',['payroll','sick','benefits']),
'travel':('Travel situations requiring a closer review',['463','274']),
'succession':('Insurance and owner succession',['life','estate']),
'admin':('Business tax-account administration',['records'])}
EXTRA={
'llc-partner-receives-w2-through-disregarded-entity':['de'],
'partner-guaranteed-payment-due-unpaid-yearend':['gp'],
'manufacturer-outsourced-production-tax-producer':['producer'],
'partnership-representative-binds-owners-consent':['6223'],
'partnership-audit-optout-disregarded-entity-partner':['6221'],
'joint-equipment-use-partnership-tax-exclusion':['761','761reg'],
'foreign-trip-currency-exchange-rate-receipts':['currency'],
'partner-retirement-contribution-guaranteed-payments':['retirement'],
'partnership-profits-interest-vesting-services':['profits'],
'corporate-redemption-spouse-retains-shares':['302'],
'foreign-tax-withheld-export-service-credit':['creditforeign'],
'rd-credit-acquired-company-carryforward':['383'],
'employee-jury-duty-fee-turnover-wages':['jury'],
'severance-paid-after-employee-leaves-state':['state'],
'buy-sell-redemption-company-life-insurance-value':['connelly'],
'business-policy-lapse-outstanding-loan':['72'],
'buyout-agreement-price-estate-value-difference':['2703'],
'employer-owned-life-insurance-consent-after-issue':['8925'],
'employer-life-insurance-form8925-no-death-benefit':['8925'],
'business-responsible-party-change-8822b':['8822'],
'business-name-change-same-ein-payroll':['name'],
'business-address-change-owner-personal-return':['8822'],
'irs-notice-old-address-response-deadline':['8822','penalty'],
'form2848-owner-versus-company-tax-authority':['2848'],
'irs-transcript-no-return-business-rejected-efile':['efile'],
'business-ein-identity-theft-duplicate-return':['id'],
'irs-business-penalty-notice-original-tax-paid':['penalty'],
'business-extension-confirmation-state-separate':['extension']}

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
  if target.exists():assert 'owner-faq-batch:20261028-c'in target.read_text(),'Existing route '+r['path']
  peers=[q for q in rows if q['group']==r['group']and q['path']!=r['path']];offset=i%8;related=peers[offset:offset+2]
  s=render(r['path'],r['title'],r['description'],body(r,related),sources=r['sources']);s=metadata(s,r['seo_title'],r['description'],SITE+r['path'])
  s=s.replace('<main>','<!-- owner-faq-batch:20261028-c --><main>',1)
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
  path=ROOT/file;s=path.read_text();s=re.sub(r'<!-- owner-faqs-20261028-c:start -->.*?<!-- owner-faqs-20261028-c:end -->','',s,flags=re.S)
  if file=='sitemap/index.html':s=s.replace('1765 pages in total.','1865 pages in total.')
  block='<!-- owner-faqs-20261028-c:start --><section class="content-section"><div class="container narrow"><h2>More specific business-owner questions</h2>'+links(selected)+'</div></section><!-- owner-faqs-20261028-c:end -->'
  assert '</main>'in s;s=s.replace('</main>',block+'</main>',1);path.write_text(s)
 xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>'+SITE+r['path']+'</loc><lastmod>'+DATE+'</lastmod></url>\n'for r in rows)+'</urlset>\n'
 (ROOT/'sitemap-owner-faqs-20261028-c.xml').write_text(xml)
 for f in ['sitemap-index.xml','sitemap_index.xml']:
  p=ROOT/f;s=p.read_text();entry='<sitemap><loc>'+SITE+'/sitemap-owner-faqs-20261028-c.xml</loc><lastmod>'+DATE+'</lastmod></sitemap>'
  if 'sitemap-owner-faqs-20261028-c.xml'not in s:s=s.replace('</sitemapindex>',entry+'\n</sitemapindex>')
  p.write_text(s)
 p=ROOT/'sitemap.xml';s=p.read_text()
 for r in rows:
  if SITE+r['path']not in s:s=s.replace('</urlset>','<url><loc>'+SITE+r['path']+'</loc><lastmod>'+DATE+'</lastmod></url>\n</urlset>')
 p.write_text(s)
 (DATA/'manifest.json').write_text(json.dumps({'date':DATE,'batch':'20261028-c','new_pages':100,'pages':rows,'discovery_pages':list(discovery)},indent=2)+'\n')
 print('Rendered 100 additional FAQs; preserved earlier 200 and existing page content.')

if __name__=='__main__':main()
