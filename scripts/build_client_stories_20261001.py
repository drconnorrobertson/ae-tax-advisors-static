#!/usr/bin/env python3
"""Build anonymized planning stories and the reviews landing page from vetted public copy."""
import sys, re, json, html
from pathlib import Path
from collections import Counter
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import site_template as T
from client_stories_20261001 import STORIES
DATE='2026-10-01'
ROOT=T.ROOT
REFS={
 'passive':('IRS: Passive Activity and At-Risk Rules','https://www.irs.gov/publications/p925'),
 'compensation':('IRS: S Corporation Compensation and Medical Insurance','https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues'),
 'retirement':('IRS: Choosing a Retirement Plan','https://www.irs.gov/retirement-plans/choosing-a-retirement-plan-plan-options'),
 'payments':('IRS: Estimated Taxes','https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes'),
 'depreciation':('IRS: How to Depreciate Property','https://www.irs.gov/publications/p946'),
}
def p(s):return '<p>'+T.esc(s)+'</p>'
def path(s):return '/case-studies/'+s['slug']+'/'
def card(s):
 return f'''<article class="cs-card" data-cat="{s['cat']}" data-text="{T.esc((s['title']+' '+s['context']).lower())}"><span class="cs-tag">{s['cat']} · Anonymized planning story</span><h3><a href="{path(s)}">{s['title']}</a></h3>{p(s['value'])}<p><strong>Documented:</strong> {s['kind']}. <strong>Next step:</strong> {T.esc(s['next'].split('. ')[0])}.</p><a class="btn-secondary" href="{path(s)}">Read the planning story</a></article>'''
DISCLOSURE='Based on anonymized engagement records or planning documents. Names, locations, entity names and exact financial figures are omitted. Proposed strategies and additional opportunities are identified separately from completed work. This is an editorial planning story, not a client quotation or a promise of savings.'
for s in STORIES:
 trail=[('Home','/'),('Case Studies','/case-studies/'),(s['title'],path(s))]
 body=T.page_header(h1=s['title'],subtitle=s['value'],trail=trail,cta='Discuss Your Planning Opportunities')
 body+=T.section('The Starting Point',p(s['context']))
 body+=T.section('The Documented AE Work',p(s['work'])+'<ul>'+''.join('<li>'+T.esc(x)+'</li>' for x in s['moves'])+'</ul>')
 body+=T.section('Where the Work Stands',p(s['status']))
 body+=T.section('The Next Opportunity to Evaluate',p(s['next'])+'<h3>What to Gather Before Taking That Step</h3>'+p(s['proof']))
 body+=T.section('Why This Approach Matters',p(s['value']))
 body+=T.section('About This Story',p(DISCLOSURE)+p('Source basis: '+s['kind']+'. Published October 1, 2026. Private client records are retained internally and are not linked publicly.'))
 name,url=REFS[s['ref']]
 body+=T.related_section([(url,name),('/case-studies/','More AE planning stories'),('/ae-tax-advisors-reviews/','AE Tax Advisors reviews and client planning stories'),('/discovery/','Discuss your own tax planning')])
 desc=s['value']+' An anonymized AE Tax Advisors planning story with documented scope and a separate next opportunity.'
 schemas=[T.article_schema(title=s['title'],description=desc,url=T.SITE+path(s),published=DATE,modified=DATE,section='Anonymized Client Planning Stories',citations=[url]),T.breadcrumb_schema(trail)]
 T.write_page(path(s),T.build_page(title=s['title']+' | AE Tax Advisors',description=desc,path=path(s),body=body,schemas=schemas,published=DATE,modified=DATE,active_nav='/case-studies/'))
# Keep the original case-study library and its filters; prepend the new stories.
f=ROOT/'case-studies/index.html';s=f.read_text().replace('See all 36 features','See all 45 features')
missing=[x for x in STORIES if ('href="'+path(x)+'"') not in s]
if missing:
 s=s.replace('<div class="cs-grid" id="cs-grid">','<div class="cs-grid" id="cs-grid">\n'+''.join(card(x) for x in missing),1)
 def extend(m):
  d=json.loads(m.group(1))
  def visit(o):
   if isinstance(o,dict):
    if o.get('@type')=='ItemList' and isinstance(o.get('itemListElement'),list):
     old=o['itemListElement'];new=[{'@type':'ListItem','position':i+1,'name':x['title'],'url':T.SITE+path(x)} for i,x in enumerate(missing)]
     for i,item in enumerate(old,start=len(new)+1):item['position']=i
     o['itemListElement']=new+old;o['numberOfItems']=len(new+old)
    else:
     for v in o.values():visit(v)
   elif isinstance(o,list):
    for v in o:visit(v)
  visit(d)
  return '<script type="application/ld+json">\n'+json.dumps(d,indent=2)+'\n</script>'
 s=re.sub(r'<script type="application/ld\+json">\s*(.*?)\s*</script>',extend,s,flags=re.S)
counts=Counter(x['cat'] for x in STORIES)
total=75+len(STORIES)
s=re.sub(r'All \(\d+\)',f'All ({total})',s)
s=re.sub(r'Real Estate Investors \(\d+\)',f"Real Estate Investors ({33+counts['Real Estate Investors']})",s)
s=re.sub(r'Business Owners \(\d+\)',f"Business Owners ({38+counts['Business Owners']})",s)
s=re.sub(r'\d+ case studies',f'{total} case studies',s)
s=re.sub(r'\d+ tax planning case studies and anonymized planning stories',f'{total} tax planning case studies and anonymized planning stories',s)
s=re.sub(r'New: \d+ anonymized planning stories',f'New: {len(STORIES)} anonymized planning stories',s)
f.write_text(s)
# Replace unverified testimonials and rating claims with source-backed editorial stories.
reviews='/ae-tax-advisors-reviews/'
faqs=[
 ('Are these client reviews or planning stories?','The stories on this page are AE’s editorial summaries of anonymized planning documents and engagement records. They are not quotations, star ratings or independent customer reviews.'),
 ('What kinds of clients does AE Tax Advisors work with?','The records reviewed include business owners, professional practices, rental investors, partnership owners and households seeking coordinated tax planning. The written engagement determines which advisory, study and filing services are included.'),
 ('Do the stories include completed tax savings?','Each story states what the reviewed source documents establish. Proposed plans, contracted work and additional opportunities are not presented as completed savings. No aggregate savings figure is claimed for this group.'),
 ('What should I expect before starting?','Expect to provide prior returns, entity documents and relevant financial records. Confirm the scope, fees, implementation responsibilities and delivery schedule in writing. Returns, amendments and property studies may have separate fees.'),
 ('Can I ask AE to review my own situation?','Yes. A discovery call is a starting point for discussing your current structure, prior returns and planning goals. Recommendations depend on your actual records and circumstances.'),
]
trail=[('Home','/'),('AE Tax Advisors Reviews',reviews)]
body=T.page_header(h1='AE Tax Advisors Reviews & Client Planning Stories',subtitle='See how AE approaches the business, property and household decisions behind a tax plan.',trail=trail,cta='Discuss Your Tax Planning')
body+='    <section class="content-section fade-in-section">\n        <div class="container narrow">\n            <h2>Read AE Tax Advisors Reviews and Explore the Work</h2>\n<p>If you are looking for AE Tax Advisors reviews, start with third-party feedback, then compare the work described in our case studies with your own needs. This is AE’s official website; the planning stories below are written by AE and are distinct from independent customer reviews.</p><p><a href="https://www.bbb.org/us/mt/billings/profile/tax-consultant/ae-tax-advisors-1296-1000196769" rel="noopener">View AE Tax Advisors’ BBB business profile and available customer feedback</a>. Review the current profile directly for ratings, dates and any customer feedback; a business profile is not itself a customer endorsement.</p><nav aria-label="Reviews page sections"><a href="#featured-planning-stories">Featured case studies</a> · <a href="#planning-story-library">All 28 planning stories</a> · <a href="#evaluate-ae">Evaluate the engagement</a> · <a href="/pricing/">Fees and scope</a></nav>\n        </div>\n    </section>    <section id="featured-planning-stories" class="content-section fade-in-section">\n        <div class="container narrow">\n            <h2>Featured AE Tax Advisors Case Studies</h2>\n<p>These six anonymized stories show the planning question, documented work and what still needs confirmation. Read the complete story before treating a proposed plan as an implemented result.</p><div class="story-grid"><article class="cs-card"><span class="cs-tag">Tax plan</span><h3><a href="/case-studies/restaurant-owner-entity-retirement-roadmap/">A Restaurant Owner Connects Entity Planning, Payroll and Retirement</a></h3><p>A coordinated plan helps an expanding business choose an order of operations: structure, payroll, benefits and then capital spending.</p><p><strong>Evidence boundary:</strong> The source documents a proposed tax plan. It does not establish that the restructuring was completed or that projected savings were realized.</p></article><article class="cs-card"><span class="cs-tag">Tax plan</span><h3><a href="/case-studies/dental-practice-business-rental-tax-roadmap/">A Dental Practice Owner Coordinates Business and Rental Planning</a></h3><p>Coordinating the practice and rentals helps prioritize the next decision by usable benefit rather than deduction size.</p><p><strong>Evidence boundary:</strong> The available document is a tax plan with projections. This summary does not report completed elections or verified savings.</p></article><article class="cs-card"><span class="cs-tag">Tax plan</span><h3><a href="/case-studies/rental-investor-loss-classification-review/">A Rental Investor Reviews Loss Classification Before Accelerating Depreciation</a></h3><p>The key planning question is where a deduction can be used, not simply how large a depreciation report can be.</p><p><strong>Evidence boundary:</strong> The source describes proposed strategies. It does not verify that suspended losses were released, a study was completed or a refund was received.</p></article><article class="cs-card"><span class="cs-tag">Completed document review</span><h3><a href="/case-studies/investor-passive-loss-carryforward-review/">An Investor Receives a Clearer View of Passive Loss Carryforwards</a></h3><p>A careful review can be useful even when it rules out an assumed refund. It gives the investor a clearer record of what remains to be checked.</p><p><strong>Evidence boundary:</strong> A document review is recorded. It did not establish a specific amendment or refund from the available records, and it requested original supporting documents before further action.</p></article><article class="cs-card"><span class="cs-tag">Engagement scope</span><h3><a href="/case-studies/rental-conversion-study-and-return-planning/">A Property Owner Coordinates Rental Conversion, Cost Segregation and Filing</a></h3><p>Reviewing conversion facts early helps keep the study and the return aligned on the same starting assumptions.</p><p><strong>Evidence boundary:</strong> The source confirms contracted work, not a completed depreciation study or filed tax benefit.</p></article><article class="cs-card"><span class="cs-tag">Engagement scope</span><h3><a href="/case-studies/mixed-use-rental-property-study-coordination/">A Property Owner Separates Rental and Personal Use Before Study Work</a></h3><p>A shared allocation record can make multiple property projects easier to coordinate without overstating the rental deduction.</p><p><strong>Evidence boundary:</strong> The reviewed source documents contracted scope. It does not establish completed studies, filed amendments or realized refunds.</p></article></div>\n        </div>\n    </section>'
body+=T.section('A Closer Look at the Work Behind the Plan',p('A strong tax advisory relationship starts with understanding how your income, entities and investments fit together. AE Tax Advisors brings those pieces into one planning conversation, with a focus on practical decisions that can be evaluated before the next return is filed.')+p(f'This collection draws on a review of the 50 most recent clients by first signed engagement date in the available AE client tracker. The {len(STORIES)} stories below highlight distinct planning situations, supported by engagement records and available tax-planning documents.')+p('The stories are written by AE and anonymized for privacy. They are editorial summaries of the work, rather than client quotations or independent reviews. Each one explains the documented plan or scope and a separate next opportunity.'))
body+=T.section('What AE’s Planning Approach Looks Like', '<div class="story-values">'+''.join('<div><h3>'+h+'</h3>'+p(t)+'</div>' for h,t in [
 ('Connect the Full Picture','Business profits, wages, property income and retirement decisions can affect the same household return. Reviewing them together gives the plan a clearer starting point.'),
 ('Give Every Move a Place','An entity change, study or amendment needs supporting records and an implementation sequence. A written roadmap helps define what comes first and what still needs confirmation.'),
 ('Look for the Next Useful Step','A plan should make the next decision easier. These stories include a concrete opportunity to evaluate, with the information needed to assess it.')])+'</div>')
body+=T.section(f'Explore {len(STORIES)} Anonymized Client Planning Stories','<div class="story-grid">'+''.join(card(x) for x in STORIES)+'</div>')
body+=T.section('What to Expect When Working With AE',p('Start with the records that explain your situation: prior personal and business returns, entity documents, bookkeeping, payroll and property information where relevant. AE can use that starting point to define the planning questions and identify the next workstream.')+p('A written scope should identify who handles implementation, what is included and when additional work is needed. More complex situations may involve coordination with legal counsel, a plan administrator, a study team or the return preparer.')+'<h3>A Few Practical Fit Considerations</h3>'+p('An advisory engagement is a better fit when you want coordinated planning and can supply the supporting records. If your needs are limited to a simple return, confirm whether a preparation-only engagement is more appropriate. Review separate study or filing fees and agreed timelines before starting.'))
body+=T.section('Media Coverage of AE Tax Advisors',p('Read AE’s published media coverage to learn more about the firm’s planning focus and client work. Media articles provide background about the firm and are distinct from customer reviews.')+'<p><a href="/press/">Explore all 45 press articles</a> · <a href="/compare/tax-planning-firms/">Compare AE with other tax planning firms</a> · <a href="/pricing/">Review AE’s scope and pricing</a></p>')
body+=T.faq_section(faqs)
body+='    <section id="evaluate-ae" class="content-section fade-in-section">\n        <div class="container narrow">\n            <h2>How to Evaluate AE Tax Advisors Before Hiring</h2>\n<ul><li><strong>Reviews:</strong> Look for the review date, service used and specific experience. Compare feedback from more than one source.</li><li><strong>People:</strong> <a href="/bios/">Meet the advisory team</a> and verify the credentials of the professional assigned to you.</li><li><strong>Scope:</strong> Ask who delivers the plan, who implements it and who prepares the returns. Get exclusions and deadlines in writing.</li><li><strong>Fees:</strong> Compare total advisory, study, filing and amendment costs using <a href="/pricing/">AE’s published pricing</a> and your written proposal.</li><li><strong>Evidence:</strong> Distinguish a deduction from tax savings, tax deferral and a projected benefit. Ask which facts still need confirmation.</li><li><strong>Support:</strong> Confirm communication expectations and any separately scoped IRS representation.</li></ul><p><a href="/tools/tax-advisor-engagement-scorecard/">Use the advisor engagement scorecard</a> · <a href="/contact/">Ask a question or share feedback</a> · <a href="/compare/best-tax-advisors-short-term-rental-owners/">Choosing a short-term rental tax company</a></p>\n        </div>\n    </section>'
body+=T.section('Bring Your Own Planning Questions',p('If your business, property portfolio or income has outgrown the way your taxes are currently handled, start with a conversation about the records and decisions that matter most.')+'<p><a class="btn-cta" href="/discovery/">Request a Discovery Call</a></p>')
body=body.replace('<h2>Explore 28 Anonymized Client Planning Stories</h2>', '<h2 id="planning-story-library">Explore 28 Anonymized Client Planning Stories</h2>')
style='<style>.story-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}.story-grid .cs-card{border:1px solid #ddd;border-radius:12px;padding:24px;background:#fff}.story-grid h3{font-size:22px;line-height:1.35}.story-grid .cs-tag{font-size:12px;letter-spacing:.4px;color:#665126}.story-grid .btn-secondary{margin-top:12px}.story-values{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}.story-grid p{font-size:15px}@media(max-width:760px){.story-grid,.story-values{grid-template-columns:1fr}}</style>'
desc='Read AE Tax Advisors reviews information, explore 28 anonymized planning stories, and compare advisory scope, fees and next steps before booking a call.'
schema={'@context':'https://schema.org','@type':'CollectionPage','name':'AE Tax Advisors Reviews & Case Studies | Official Site','url':T.SITE+reviews,'description':desc,'dateModified':DATE,'publisher':{'@type':'Organization','name':T.BRAND},'mainEntity':{'@type':'ItemList','numberOfItems':len(STORIES),'itemListElement':[{'@type':'ListItem','position':i+1,'name':x['title'],'url':T.SITE+path(x)} for i,x in enumerate(STORIES)]}}
T.write_page(reviews,T.build_page(title='AE Tax Advisors Reviews & Case Studies | Official Site',description=desc,path=reviews,body=body,schemas=[schema,T.breadcrumb_schema(trail),T.faq_schema(faqs)],published=DATE,modified=DATE,extra_head=style))
# Update existing sitemap partitions without touching unrelated URLs.
for fn in ['sitemap.xml','sitemap-case-studies.xml','sitemap-pages.xml']:
 f=ROOT/fn
 if not f.exists():continue
 s=f.read_text()
 for x in STORIES:
  url=T.SITE+path(x)
  if url not in s and fn!='sitemap-pages.xml':s=s.replace('</urlset>',f'  <url><loc>{url}</loc><lastmod>{DATE}</lastmod></url>\n</urlset>')
 for route in ['/case-studies/',reviews]:
  s=re.sub(r'(<loc>'+re.escape(T.SITE+route)+r'</loc>\s*<lastmod>)[^<]+',lambda m:m.group(1)+DATE,s)
 f.write_text(s)
(ROOT/'scripts/client_stories_manifest_20261001.json').write_text(json.dumps({'date':DATE,'reviewed_clients':50,'stories':len(STORIES),'paths':[path(x) for x in STORIES]+[reviews,'/case-studies/']},indent=2)+'\n')
print(f'Built {len(STORIES)} stories; expanded reviews page and case-study index; updated sitemaps.')

# Reapply public profile tags after rebuilding the library.
import runpy
runpy.run_path(str(ROOT / "scripts/build_case_profile_filters.py"))

# Preserve the expanded buyer evidence on the regenerated reviews page.
from expand_buyer_guides_20261001 import enhance, GUIDES
enhance(next(g for g in GUIDES if g["key"] == "ae-reviews"))
