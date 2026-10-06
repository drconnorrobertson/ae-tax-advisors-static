"""Publish authored FAQ articles and illustrated lessons using the existing site design."""
import sys, re, json, html, collections, xml.etree.ElementTree as ET
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import site_template as T
from owner_faq_articles import GROUPS,CONTEXT
from tax_movement_lessons import SERIES
ROOT=T.ROOT;DATE='2026-10-06';HUB='/tax-movement-explained/'
def slug(s):return re.sub('[^a-z0-9]+','-',s.lower()).strip('-')
def p(s):return '<p>'+html.escape(s)+'</p>'
def add_section(body,title,text):return body+T.section(title,p(text))

# Four-node drawings describe the actual mechanism, not a generic tax-saving arrow.
# A dashed connector is information or a review; a solid connector is cash.
FLOWS={
'corporation':[
 ('Taxable corporate profit','Corporate tax calculation','After-tax company cash','Owner payment reviewed'),
 ('After-tax company cash','Dividend to shareholder','Shareholder dividend income','Personal tax calculation'),
 ('Corporate profit','Company tax calculation','Cash retained in company','Business reserve plan'),
 ('Company pays wages','Owner payroll reporting','Company wage deduction review','Combined tax comparison'),
 ('Owner invests cash','Corporation receives capital','Equity and stock basis','Business uses funding'),
 ('Company purchases equipment','Asset placed in service','Depreciation eligibility','Corporate tax deduction'),
 ('Corporation advances cash','Shareholder owes repayment','Principal and interest records','Loan classification review'),
 ('Company retains cash','Defined business needs','Accumulation review','Corporate tax analysis'),
 ('C corporation loss','Corporate loss rules','Company return','No annual owner pass-through'),
 ('C corporation history','S election eligibility','Transition tax review','Future pass-through reporting'),
],
'pass-through':[
 ('S corporation profit','Schedule K-1 allocation','Owner income reporting','Personal tax calculation'),
 ('Working shareholder','Supported wages / payroll','Separate distribution','Stock basis review'),
 ('Opening stock basis','Income increases basis','Other adjustments','Ending stock basis'),
 ('Proposed cash distribution','Available stock basis','Excess distribution review','Possible owner gain'),
 ('K-1 loss','Basis and at-risk review','Passive and other limits','Allowed / suspended loss'),
 ('Owner funds corporation','Equity or direct loan','Company pays business cost','Expense and basis review'),
 ('Company pays premiums','Shareholder W-2 treatment','Owner deduction eligibility','Personal return'),
 ('One owner lends cash','Direct company obligation','Lending owner debt basis','Owner-specific loss review'),
 ('S corporation cash','Shareholder distribution','Owner estimated payment','Personal tax credit'),
 ('Company repays owner loan','Adjusted loan basis','Taxable repayment review','Owner reporting'),
],
'partnership':[
 ('Partnership result','Partner K-1 allocations','Each partner return','Tax and limitation review'),
 ('Partnership operating profit','Tax allocation','Separate cash distribution','Partner basis review'),
 ('Partner provides services','Guaranteed payment','Deduction / capitalization','Partner income reporting'),
 ('Partner contributes assets','Partnership receives capital','Inside / outside basis','Ownership records'),
 ('Partnership liabilities','Allocation to partner','Outside basis adjustment','Separate at-risk review'),
 ('Partnership loss','Partner outside basis','At-risk and passive limits','Allowed / suspended loss'),
 ('Partnership cash reserve','Tax distribution to partner','Partner pays estimated tax','Partner payment credit'),
 ('Property operating result','Partner K-1 share','Individual participation test','Partner-specific loss use'),
 ('Partner pays business cost','Evidence and agreement','Partnership reimbursement','Correct reporting review'),
 ('Buyer purchases interest','Buyer outside basis','Inside basis review','Election / adjustment analysis'),
],
'payroll':[
 ('Gross wages','Employee withholding','Net employee pay','Government tax deposits'),
 ('Gross payroll cost','Employee withholding','Employer tax expense','Company cash requirement'),
 ('Payroll withholding','Employer holds tax funds','Required tax deposit','Payroll return reporting'),
 ('Owner services','Supported payroll wages','Employment tax reporting','Separate owner distribution'),
 ('Approved cash bonus','Supplemental wage withholding','Employee net bonus','Final owner tax return'),
 ('Gross compensation','Elected plan deferral','Retirement plan deposit','Remaining net pay'),
 ('Actual worker relationship','Classification review','Payroll or contractor path','Correct tax reporting'),
 ('Employee-paid expense','Accountable plan review','Reimbursement or wages','Company reporting'),
 ('Spouse performs services','Entity-specific payroll rules','Documented wage payment','Employee reporting'),
 ('Payroll registers','Quarterly Form 941','Annual W-2 reporting','Deposit reconciliation'),
],
'two-entities':[
 ('Service company work','Supported fee invoice','Operating company payment','Income / expense reporting'),
 ('Controlled transaction','Evidence of actual service','Supported arm\'s-length price','Both entity returns'),
 ('Operating business cash','Supported building rent','Property entity receipts','Self-rental / tax review'),
 ('Employer pays staff','Actual shared services','Supported cost allocation','Receiving company review'),
 ('Documented IP rights','Operating company use','Supported royalty payment','Recipient income reporting'),
 ('Entity A advances cash','Entity B records debt','Principal repayment','Separate interest review'),
 ('Parent contributes capital','Subsidiary receives funds','Investment / equity records','No automatic fee deduction'),
 ('Entity A pays vendor','Entity B actual obligation','Intercompany reconciliation','One supported deduction'),
 ('Owner has two LLCs','Federal classification review','Cash transfers recorded','Correct taxpayer reporting'),
 ('Payer entity payment','Recipient entity income','Owner cash extraction','Combined tax calculation'),
],
'property':[
 ('Tenant gross rent','Property expense records','Depreciation and limits','Owner rental reporting'),
 ('Mortgage cash payment','Principal reduces debt','Interest expense review','Rental tax computation'),
 ('Rental property basis','Depreciation computation','Noncash tax deduction','Rental loss limits'),
 ('Personal home converted','Rental availability date','Conversion basis review','Depreciation schedule'),
 ('Owner pays improvement','New capital asset record','Service date / recovery','Rental depreciation'),
 ('Refundable tenant deposit','Landlord deposit liability','Returned / applied amount','Rent income review'),
 ('Rental and personal days','Expense allocation','Vacation-home limits','Owner rental return'),
 ('STR operating result','Activity classification','Participation and limits','Owner deduction review'),
 ('Guest gross receipts','Manager fees and costs','Owner net cash remittance','Gross income reconciliation'),
 ('Property sale price','Adjusted basis comparison','Tax gain calculation','Separate net cash calculation'),
],
'retirement':[
 ('Employer cash funding','Plan contribution','Eligibility and limit review','Employer deduction'),
 ('Eligible gross wages','Pretax elective deferral','Plan account deposit','Current wage tax treatment'),
 ('Current taxable wages','Roth elective deferral','Plan account deposit','Qualified withdrawal rules'),
 ('Employee census','Actuarial calculation','Company plan funding','Ongoing funding obligations'),
 ('Owner-only business','Eligible employee added','Plan coverage review','Employer and employee funding'),
 ('Reasonable owner wages','Eligible compensation','Plan contribution calculation','Actual employer funding'),
 ('Employer SEP funding','Participant allocation','Eligibility / limits','Employer deduction'),
 ('Ownership in two companies','Related-employer review','Combined employee picture','Plan design decision'),
 ('Company cash reserve','Plan contribution','Reduced cash for operations','Tax benefit comparison'),
 ('Contribution error','Administrator correction','Payroll / plan reconciliation','Corrected tax reporting'),
],
'deductions':[
 ('Employee business expense','Receipts and substantiation','Company reimbursement','Expense / wage treatment'),
 ('Owner pays company bill','Evidence of company purpose','Supported repayment / funding','One tax expense record'),
 ('Vehicle total use','Business / personal split','Eligible expense method','Supported deduction'),
 ('Meal payment','Business purpose evidence','Applicable deduction limits','Company tax treatment'),
 ('Company travel advance','Employee substantiates costs','Excess cash returned','Reimbursement classification'),
 ('Cash purchase','Eligible asset in service','Recovery method / election','Tax deduction schedule'),
 ('Loan cash payment','Principal reduces debt','Interest expense review','Business tax computation'),
 ('Business expense correction','Entity income changes','Owner allocations / basis','Personal return review'),
 ('Business use of home','Eligibility and allocation','Supported reimbursement','Company / owner reporting'),
 ('One actual business cost','Shared reimbursement ledger','One approved payment','No duplicate deduction'),
],
'loans':[
 ('Owner advances cash','Business loan payable','Owner loan receivable','Terms / repayments tracked'),
 ('Owner provides funding','Equity or debt decision','Investment / obligation record','Basis and payment rules'),
 ('Loan supports prior loss','Debt basis reduced','Company repays principal','Taxable repayment review'),
 ('Bank lends to company','Owner guarantee','No automatic debt basis','Actual payment review'),
 ('Company loan payment','Principal portion','Interest portion','Owner income reporting'),
 ('Company bank balance','Borrowing / profit / funding','Separate owner basis schedule','Distribution review'),
 ('Genuine owner cash investment','Stock basis increase','Proposed distribution','Ordering and gain review'),
 ('Entity B repays principal','B liability reduced','A receivable reduced','Separate interest review'),
 ('Company pays personal bill','Actual owner benefit','Wage / distribution / loan','Correct tax classification'),
 ('Opening loan balance','Advances and repayments','Interest and tax basis','Reconciled return records'),
],
'payments':[
 ('Owner tax liability','Payroll withholding','Estimated payments','Return payment reconciliation'),
 ('Company cash reserve','Classified owner transfer','Owner estimated tax','Personal payment credit'),
 ('Current-year tax projection','Safe-harbor calculation','Timely payment credits','Remaining balance due'),
 ('Uneven period income','Annualized tax calculation','Required installments','Payment / penalty review'),
 ('Rental sale tax result','Updated household projection','Payment need calculation','Owner tax payment'),
 ('Original payment deadline','Estimated balance payment','Extended filing timeline','Final reconciliation'),
 ('Prior-year overpayment','Carryforward election','Current-year credit','Remaining payment need'),
 ('Quarterly books','Tax adjustments','Household projection','Payment and cash plan'),
 ('Spouse payroll withholding','Joint household income','Combined payment credits','Joint tax reconciliation'),
 ('Final individual liability','Owner cash funding','IRS balance payment','No operating deduction'),
]}

def drawing(kind,n,title,example):
    labels=FLOWS[kind][n]; uid=kind+'-'+str(n)
    positions=[(210,40),(20,205),(400,205),(210,370)]
    # Standard review flow travels through a diamond; payroll / partnership fan out.
    fan=kind in ('payroll','partnership','payments') and n in (0,1,6,8)
    edges=[(0,1),(0,2),(1,3),(2,3)] if fan else [(0,1),(1,2),(2,3)]
    cash_indices={('corporation',1):{0},('corporation',4):{0},('corporation',6):{0},('pass-through',8):{0,1},('pass-through',9):set(),('two-entities',5):{0,1},('two-entities',6):{0},('property',5):{0,1},('loans',0):{0},('loans',7):{0},('payments',1):{0,1}}
    cash=cash_indices.get((kind,n),set())
    desc='; '.join(labels)+'. Solid arrows mark cash where explicitly identified. Dashed arrows show information or review, not deductible payments.'
    svg=f'<figure class="tax-figure"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 500" role="img" aria-labelledby="{uid}-title {uid}-desc"><title id="{uid}-title">{html.escape(title)}</title><desc id="{uid}-desc">{html.escape(desc)}</desc><defs><marker id="{uid}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#b39457"/></marker></defs>'
    for i,(a,b) in enumerate(edges):
      x1,y1=positions[a];x2,y2=positions[b]
      if y1==y2:
        x1+=220;y1+=40;y2+=40
      else:x1+=110;y1+=80;x2+=110
      svg+=f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#b39457" stroke-width="3" fill="none" marker-end="url(#{uid}-arrow)"'+(' stroke-dasharray="7 5"' if i not in cash else '')+'/>'
    for i,(x,y) in enumerate(positions):
      svg+=f'<rect x="{x}" y="{y}" width="220" height="80" rx="10" fill="#1b2a4a"/>'
      words=labels[i].split(); lines=[];line=''
      for w in words:
        if len(line+' '+w)>25:lines.append(line);line=w
        else:line=(line+' '+w).strip()
      lines.append(line)
      for j,line in enumerate(lines):svg+=f'<text x="{x+110}" y="{y+34+j*21}" text-anchor="middle" fill="#ffffff" font-size="16" font-family="Inter,Arial,sans-serif">{html.escape(line)}</text>'
    svg+='</svg><figcaption>'+html.escape(example)+' Solid arrows: cash. Dashed arrows: information, classification or review.</figcaption></figure>'
    svg+='<ol class="tax-flow-text">'+''.join('<li>'+html.escape(l)+'</li>' for l in labels)+'</ol>'
    return svg

STYLE='<style>.tax-figure{margin:24px 0;border:1px solid #e1e5ec;border-radius:12px;padding:16px;background:#f8f9fc}.tax-figure svg{display:block;width:100%;height:auto;max-width:680px;margin:auto}.tax-figure figcaption{font-size:.95rem;line-height:1.65;margin-top:12px}.tax-flow-text{padding-left:24px}.tax-flow-text li{margin:8px 0}@media(max-width:500px){.tax-figure{padding:8px;margin-left:-12px;margin-right:-12px}}</style>'

LESSON_NAMES={
'corporation':['C corporation income tax before an owner takes cash','a C corporation dividend and its second tax layer','retaining earnings in a C corporation','owner payroll as a C corporation expense','a C corporation capital contribution','equipment purchases inside a C corporation','a corporate loan to a shareholder','a C corporation business reserve','a C corporation loss at the company level','the transition from C corporation to S taxation'],
'pass-through':['S corporation profit on an owner return','S corporation payroll versus distributions','an S corporation stock basis increase','an S corporation distribution above basis','S corporation loss limitation review','shareholder funding for business expenses','S corporation health insurance reimbursement','debt basis when only one shareholder lends','an S corporation tax distribution','an S corporation shareholder loan repayment'],
'partnership':['partnership income from Form 1065 to the partner','partnership profit allocation versus cash distribution','a guaranteed payment to a partner','a partner capital contribution','partnership debt in outside basis','partnership losses on the partner return','a partnership tax distribution','participation in a rental partnership','reimbursing a partner business expense','buying a partnership interest rather than its property'],
'payroll':['the split from gross wages to net pay','the employer share of payroll taxes','remitting payroll withholding to the IRS','payroll for a sole S corporation shareholder','a bonus payment through payroll','an employee 401(k) payroll deferral','employee versus contractor payment classification','employee reimbursement versus additional wages','paying a spouse through business payroll','reconciling Form 941 and W-2 totals'],
'two-entities':['a real management fee between two entities','related-party pricing in a two-entity arrangement','separating property ownership from operations','shared payroll cost allocation between entities','a royalty between commonly owned companies','a loan between commonly owned entities','a parent capital contribution to a subsidiary','paying a vendor from the wrong entity account','a transfer between two commonly owned LLCs','owner cash extraction in a two-entity plan'],
'property':['rental income reporting from tenant to owner','a rental mortgage principal and interest split','noncash depreciation against rental income','depreciation after home-to-rental conversion','a rental improvement on the asset schedule','rental security deposit accounting','vacation rental personal-use allocation','a short-term rental loss on the household return','property manager fees and net remittances','rental sale gain versus net closing cash'],
'retirement':['an employer retirement plan contribution','a pretax employee salary deferral','a Roth 401(k) payroll deferral','a cash balance plan funding obligation','retirement coverage after hiring employees','S corporation salary for retirement contributions','a SEP employer contribution','retirement coverage across two companies','retirement funding alongside business expansion','a retirement contribution correction with payroll'],
'deductions':['an accountable plan reimbursement','an owner-paid expense for the correct entity','mixed-use vehicle expense allocation','the business meal deduction review','travel advances and expense reconciliation','depreciation versus immediate expensing','business interest versus principal repayment','an expense correction across business and personal returns','home office eligibility before reimbursement','preventing duplicate owner reimbursements'],
'loans':['an owner loan on the business balance sheet','owner equity funding versus a business loan','repayment of a loan with reduced debt basis','a shareholder guarantee versus a direct loan','shareholder loan interest reporting','stock basis versus company bank cash','a stock contribution before a distribution','intercompany loan principal repayment','classification of company-paid personal bills','a loan schedule in the business return'],
'payments':['estimated tax versus payroll withholding','a tax reserve followed by an owner payment','a tax safe harbor versus final liability','annualized income for estimated installments','a rental sale in a new payment projection','tax payments during a filing extension','a prior-year overpayment applied forward','quarterly books in an owner tax projection','spouse withholding for joint business income','paying an individual final tax balance'],
}

def sources(category,url):
    urls=[url]
    if category in ['Retirement Planning','S-Corp Planning']:urls.append('https://www.irs.gov/retirement-plans/retirement-plan-faqs-regarding-contributions-s-corporation')
    if category=='S-Corp Planning':urls.append('https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues')
    if category=='Business Deductions':urls+=['https://www.irs.gov/publications/p334','https://www.irs.gov/publications/p946','https://www.irs.gov/publications/p587']
    if category in ['Rental Property','Material Participation','Cost Segregation']:urls+=['https://www.irs.gov/publications/p925','https://www.irs.gov/publications/p946','https://www.irs.gov/publications/p527']
    if category=='Entity Structuring':urls+=['https://www.irs.gov/publications/p541','https://www.irs.gov/publications/p542','https://www.irs.gov/publications/p925']
    if category=='Tax Return Mistakes':urls+=['https://www.irs.gov/forms-pubs/about-form-3115','https://www.irs.gov/publications/p946']
    if category=='Tax Compliance':urls+=['https://www.irs.gov/publications/p505','https://www.irs.gov/publications/p15','https://www.irs.gov/businesses/small-businesses-self-employed/independent-contractor-self-employed-or-employee']
    return list(dict.fromkeys(urls))

def main():
    posts=[]
    assert sum(len(g[3]) for g in GROUPS)==100
    assert sum(len(g[3]) for g in SERIES)==100
    existingtitles={re.sub('<[^>]*>','',m[1]).strip().lower() for f in (ROOT/'blog').glob('*/index.html') if (m:=re.search(r'<h1[^>]*>(.*?)</h1>',f.read_text(),re.S)) and not f.parent.name.startswith(('owner-faq-','how-tax-moves-'))}
    for educational,groups in [(False,GROUPS),(True,SERIES)]:
      for category,source,mechanism,items in groups:
        for i,(question,answer,example) in enumerate(items):
          if educational:question='How does '+LESSON_NAMES[mechanism][i]+' work?'
          assert question.lower() not in existingtitles,question
          ident=('how-tax-moves-' if educational else 'owner-faq-')+slug(question)
          path='/blog/'+ident+'/'
          desc=answer[:155].rsplit(' ',1)[0]+'.'
          url=T.SITE+path
          body=T.page_header(h1=html.escape(question),subtitle='Illustrated tax movement lesson for business and real estate owners.' if educational else 'A practical tax FAQ for business and real estate owners.',trail=[('Home','/'),('Blog','/blog/'),(question,path)])
          body+=T.section('The direct answer',p(answer))
          if educational:body+=T.section('Follow the movement',drawing(mechanism,i,question,example))
          else:body+=T.section('A practical example',p('Illustrative example, not a client result: '+example))
          if not educational:
            heading,context,records=CONTEXT[category]
          else:
            heading='What the drawing does and does not show'
            context='The boxes identify the parties, records or decisions involved in this specific question. A connector showing tax reporting does not mean cash was paid. A cash transfer does not establish a deduction. The transaction must be classified before the return is prepared, and the recipient side must be included in the analysis. Review the actual tax year, legal ownership and any related-party or loss limitation rules before implementing the arrangement.'
            records='Entity classifications, ownership records, transaction documents, payment evidence, books and the relevant filed returns.'
          body+=T.section(heading,p(context))
          body+=T.section('Put the answer into your own tax file',p('Start by identifying the taxpayer, the tax year and the actual transaction. Then connect the transaction to the original documents before choosing a return line or moving money between accounts. A payment description can be useful evidence, but it cannot replace the underlying facts.')+p('The records to review for this topic are: '+records)+p('For the example above, write down the decision that needs to be made, the missing information and the person responsible for supplying it. Keep the business, payroll, property and personal return teams aligned when more than one set of records is affected.'))
          faqs=[(question,answer),('What should I verify before applying this answer?', 'Verify the taxpayer, tax year, ownership, actual payments and supporting records. '+records)]
          body+=T.faq_section(faqs,'Questions to resolve before implementation')
          urls=sources(category,source)
          body+=T.section('Primary sources', '<ul>'+''.join(f'<li><a href="{u}" target="_blank" rel="noopener">'+html.escape(('IRS '+u.split('/')[-1].replace('-',' ').upper()) if '/p' in u and u.split('/')[-1][1:].isdigit() else 'IRS guidance: '+u.split('/')[-1].replace('-',' '))+'</a></li>' for u in urls)+'</ul>'+p('Sources checked October 6, 2026. Use the guidance and form instructions for the relevant tax year. This article provides general education; facts and state rules can change the treatment.'))
          # Cross-links include two sibling lessons, a case and the conversion route.
          other=[('How does '+LESSON_NAMES[mechanism][j]+' work?') if educational else items[j][0] for j in [(i+1)%10,(i+2)%10]]
          links=[('/blog/'+('how-tax-moves-' if educational else 'owner-faq-')+slug(q)+'/',q) for q in other]
          casekey={'C-Corp Planning':'compensation','S-Corp Planning':'compensation','Tax Compliance':'review','Entity Structuring':'review','Business Deductions':'reimbursements','Retirement Planning':'retirement','Rental Property':'assets','Material Participation':'rentals','Cost Segregation':'assets','1031 Exchanges':'sale','Tax Return Mistakes':'review'}[category]
          persona='real-estate-agent-with-rentals' if category in ['Rental Property','Material Participation','Cost Segregation','1031 Exchanges'] else 'general-contractor'
          links += [('/case-studies/planning-'+persona+'-'+casekey+'/','Related illustrative owner planning example'),(HUB,'Explore the illustrated How Tax Moves series'),('/discovery/','Discuss your business and property planning')]
          body+=T.related_section(links)
          article=T.article_schema(title=question,description=desc,url=url,published=DATE,modified=DATE,section=category,citations=urls);article['@type']='BlogPosting';article['isPartOf']={'@type':'Blog','@id':T.SITE+'/blog/'};article['inLanguage']='en-US'
          if educational:article['isPartOf']={'@type':'CollectionPage','@id':T.SITE+HUB}
          schemas=[article,T.faq_schema(faqs),T.breadcrumb_schema([('Home','/'),('Blog','/blog/'),(question,path)])]
          page=T.build_page(title=question+' | AE Tax Advisors',description=desc,path=path,body=body,schemas=schemas,published=DATE,modified=DATE,active_nav='/blog/',extra_head=STYLE if educational else '')
          T.write_page(path,page);posts.append(dict(title=question,desc=desc,path=path,category=category,educational=educational))
    assert len({p['path'] for p in posts})==200
    hubbody=T.page_header(h1='How Tax Moves: 100 Illustrated Lessons',subtitle='Follow wages, cash transfers, deductions and tax reporting through corporations, partnerships, payroll and property activities.',trail=[('Home','/'),('How Tax Moves',HUB)])
    hubbody+=T.section('Read the arrows before moving the money',p('Solid arrows represent cash where explicitly identified. Dashed arrows represent tax information, classification or review. Each lesson explains the mechanism and its limits. A payment to another entity does not automatically reduce the combined tax bill.'))
    for cat in dict.fromkeys(p['category'] for p in posts if p['educational']):
      group=[p for p in posts if p['educational'] and p['category']==cat]
      hubbody+=T.section(cat,'<ul>'+''.join(f'<li><a href="{p["path"]}">{html.escape(p["title"])}</a></li>' for p in group)+'</ul>')
    T.write_page(HUB,T.build_page(title='How Tax Moves: 100 Illustrated Tax Lessons | AE Tax Advisors',description='100 illustrated lessons explain C corporations, S corporations, partnerships, payroll, two-entity transactions, property and tax payments.',path=HUB,body=hubbody,schemas=[{'@context':'https://schema.org','@type':'CollectionPage','name':'How Tax Moves','url':T.SITE+HUB,'mainEntity':{'@type':'ItemList','numberOfItems':100,'itemListElement':[{'@type':'ListItem','position':i+1,'name':p['title'],'url':T.SITE+p['path']} for i,p in enumerate([p for p in posts if p['educational']])]}}],published=DATE,modified=DATE,active_nav='/blog/',og_type='website'))
    indexpath=ROOT/'blog/index.html';index=indexpath.read_text()
    # Replace this batch on rerun without touching existing editorial cards.
    index=re.sub(r'<!-- owner-learning:start -->.*?<!-- owner-learning:end -->','',index,flags=re.S)
    cards=[]
    for post in posts:
      cards.append(f'<article class="blog-card" data-cat="{post["category"]}" data-text="{T.esc((post["title"]+" "+post["desc"]+" "+post["category"]).lower())}"><div class="blog-body"><div class="blog-meta"><span class="blog-cat">{post["category"]}</span><time class="blog-date" datetime="{DATE}">October 6, 2026</time></div><h3><a href="{post["path"]}">{html.escape(post["title"])}</a></h3><p>{html.escape(post["desc"])}</p><a href="{post["path"]}" class="blog-readmore">Read article</a></div></article>')
    index=index.replace('<div class="blog-grid" id="blog-grid">','<div class="blog-grid" id="blog-grid">\n<!-- owner-learning:start -->'+''.join(cards)+'<!-- owner-learning:end -->',1)
    total=index.count('class="blog-card"')
    counts=collections.Counter(re.findall(r'class="blog-card" data-cat="([^"]+)"',index))
    index=re.sub(r'(<button class="blog-chip" data-cat="([^"]+)"[^>]*>).*?</button>',lambda m:m[1]+('All' if m[2]=='all' else m[2])+f' ({total if m[2]=="all" else counts[m[2]]})</button>',index)
    index=re.sub(r'\b629 articles\b',str(total)+' articles',index)
    index=re.sub(r'(<p class="blog-count"[^>]*>).*?</p>',lambda m:m[1]+str(total)+' articles</p>',index)
    def blog_schema(m):
      d=json.loads(m[1])
      if d.get('@type')=='Blog':
        old=[e for e in d.get('blogPost',[]) if not any(x in e.get('url','') for x in ['/owner-faq-','/how-tax-moves-'])]
        d['blogPost']=[{'@type':'BlogPosting','headline':p['title'],'url':T.SITE+p['path'],'datePublished':DATE} for p in posts]+old;d['dateModified']=DATE
      return '<script type="application/ld+json">'+json.dumps(d)+'</script>'
    index=re.sub(r'<script type="application/ld\+json">(.*?)</script>',blog_schema,index,flags=re.S)
    index=index.replace('<div class="blog-grid" id="blog-grid">',f'<p><a href="{HUB}">Explore 100 illustrated How Tax Moves lessons</a></p>\n<div class="blog-grid" id="blog-grid">',1) if HUB not in index else index
    indexpath.write_text(index)
    # Advertised primary sitemap plus specialized blog and case-study discovery.
    ns='http://www.sitemaps.org/schemas/sitemap/0.9'; ET.register_namespace('',ns)
    for filename,newpaths in [('sitemap.xml',[p['path'] for p in posts]+[HUB]+['/'+str(p.parent)+'/' for p in (ROOT/'case-studies').glob('planning-*/index.html')]),('sitemap-blog.xml',[p['path'] for p in posts])]:
      doc=ET.parse(ROOT/filename);root=doc.getroot();seen={e.text for e in root.findall('{'+ns+'}url/{'+ns+'}loc')}
      for path in newpaths:
        path=path.replace(str(ROOT)+'/','') if str(ROOT) in path else path
        path='/'+path.strip('/')+'/'
        url=T.SITE+path
        if url not in seen:
          e=ET.SubElement(root,'{'+ns+'}url');ET.SubElement(e,'{'+ns+'}loc').text=url;ET.SubElement(e,'{'+ns+'}lastmod').text=DATE;seen.add(url)
      doc.write(ROOT/filename,encoding='utf-8',xml_declaration=True)
    feed=ET.parse(ROOT/'feed.xml');channel=feed.getroot().find('channel');old={e.findtext('link') for e in channel.findall('item')}
    for post in reversed(posts):
      if T.SITE+post['path'] in old:continue
      item=ET.Element('item');ET.SubElement(item,'title').text=post['title'];ET.SubElement(item,'link').text=T.SITE+post['path'];ET.SubElement(item,'description').text=post['desc'];ET.SubElement(item,'pubDate').text='Tue, 06 Oct 2026 00:00:00 +0000';ET.SubElement(item,'guid',{'isPermaLink':'true'}).text=T.SITE+post['path'];channel.insert(4,item)
    feed.write(ROOT/'feed.xml',encoding='utf-8',xml_declaration=True)
    (ROOT/'scripts/owner-learning-manifest.json').write_text(json.dumps(posts,indent=2))
    print('Created 100 FAQ articles, 100 illustrated lessons and a series hub. Blog cards:',total)

if __name__=='__main__':main()
