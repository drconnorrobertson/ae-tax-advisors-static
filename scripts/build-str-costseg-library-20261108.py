#!/usr/bin/env python3
"""Author the reviewed 100-question resource library; preserve truthful publication dates."""
import html,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT));import site_template as T
E=html.escape;D=ROOT/'content/str-costseg-library-20261108';cfg=json.loads((D/'questions.json').read_text());groups=cfg['groups'];DATE=cfg['reviewed'];HUB='/guides/str-tax-cost-segregation/';pages=[];updated=[]
S={k:(u,n) for k,u,n in [
 ('925','https://www.irs.gov/publications/p925','IRS Publication 925: passive activity, participation and at-risk rules'),('527','https://www.irs.gov/publications/p527','IRS Publication 527: rental use, reporting and depreciation'),('415','https://www.irs.gov/taxtopics/tc415','IRS Topic 415: vacation rental and personal use'),('414','https://www.irs.gov/taxtopics/tc414','IRS Topic 414: rental income, services and reporting'),('946','https://www.irs.gov/publications/p946','IRS Publication 946: depreciation, methods and elections'),('bonus','https://www.irs.gov/pub/irs-drop/n-26-11.pdf','IRS Notice 2026-11: additional first-year depreciation'),('4562','https://www.irs.gov/instructions/i4562','IRS Form 4562 instructions'),('3115','https://www.irs.gov/instructions/i3115','IRS Form 3115 instructions and filing procedures'),('procedures','https://www.irs.gov/forms-pubs/about-form-3115','IRS current Form 3115 guidance and automatic-change procedure references'),('atg','https://www.irs.gov/pub/irs-pdf/p5653.pdf','IRS Publication 5653: cost segregation audit technique guide (not binding law)'),('461','https://www.irs.gov/instructions/i461','IRS Form 461 instructions: excess business losses'),('544','https://www.irs.gov/publications/p544','IRS Publication 544: dispositions and recapture')]}
def p(s):return '<p>'+E(s)+'</p>'
def link(u,s):return '<a href="'+E(u,quote=True)+'">'+E(s)+'</a>'
def ul(xs):return '<ul>'+''.join('<li>'+E(x)+'</li>'for x in xs)+'</ul>'
def sec(h,s):return T.section(E(h),p(s))
def route(g):return HUB+g['slug']+'/'
def save(path,title,description,body,keys,faqs=None,extra=''):
 f=ROOT/path.strip('/')/'index.html';old=f.read_text()if f.exists()else'';m=re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})',old);published=m[1]if m else DATE
 trail=[('Home','/'),('STR and cost segregation questions',HUB)]
 if path!=HUB:trail.append((title,path))
 sources=[S[k]for k in dict.fromkeys(keys)]
 body+=T.section('Reviewed sources and scope',p('Reviewed November 8, 2026 by AE Tax Advisors. This is a federal planning resource; the facts, tax year, elections and state rules control the actual return. IRS publications explain rules but do not replace applicable law. The cost segregation audit guide is nonbinding examiner guidance and predates later bonus-depreciation changes.')+'<ul>'+''.join('<li>'+link(u,n)+'</li>'for u,n in sources)+'</ul>')
 body+=T.section('Bring the facts to a scoped review',p('A study estimates asset classifications; a tax review determines eligible and currently usable deductions. Ask who reconciles basis, prepares any Form 3115 or amended return, and implements the final schedules. No tax saving or investment outcome is guaranteed.')+'<p>'+link('/cost-segregation-study/','Cost segregation service and scope')+' · '+link('/cost-segregation-documents-checklist/','Documents checklist')+' · '+link('/pricing/','Advisory pricing')+'</p>')
 schema=[T.article_schema(title=title,description=description,url=T.SITE+path,published=published,modified=DATE,section='STR and rental depreciation questions',citations=[u for u,_ in sources]),T.breadcrumb_schema(trail)]
 if faqs:schema.append(T.faq_schema([(q,p(a))for q,a in faqs]))
 text=T.build_page(title=title+' | AE Tax Advisors',description=description,path=path,body=T.page_header(h1=E(title),subtitle=E(description),trail=trail)+body,schemas=schema,published=published,modified=DATE,active_nav='/resources/',extra_head='<script defer src="/assets/booking-events.js"></script>'+extra)
 f.parent.mkdir(parents=True,exist_ok=True);f.write_text(text+'\n');pages.append(path)
existing={
 'average-stay-tests':[('/short-term-rental-tax-loophole-2026/','STR qualification overview')],
 'material-participation-tests':[('/faq/str-material-participation-exactly-100-hours/','Exactly 100 hours: existing detailed answer')],
 'hours-spouses-managers':[('/faq/str-cleaner-more-hours-than-owner/','When a cleaner works more than the owner'),('/faq/str-spouse-hours-married-filing-separately/','Spouse hours and separate returns'),('/faq/str-property-research-material-participation-hours/','Property research and participation')],
 'personal-use-vacation-home':[('/faq/vacation-rental-personal-use-cost-segregation/','Vacation use and cost segregation')],
 'cost-segregation-components':[('/faq/condo-cost-segregation-zero-land-basis/','Condo land allocation')],
 'placed-in-service-timing':[('/faq/rental-depreciation-before-first-guest/','Depreciation before the first guest')],
 'form-3115-catchup':[('/faq/form-3115-tax-return-extension-duplicate-copy/','Extensions and the duplicate Form 3115 copy')],
 'amendments-method-errors':[('/amended-return-vs-form-3115/','Amendment versus method change'),('/faq/missed-rental-depreciation-one-year-vs-multiple/','One missed year versus multiple years')],
 'former-home-rental-basis':[('/faq/cash-out-refinance-cost-segregation-new-appraisal/','Refinance and appraisal basis')],
 'repairs-improvements-replacements':[('/faq/rental-renovation-before-placed-in-service-repair/','Renovation before rental readiness')],
 'selling-recapture-exchanges':[('/faq/cost-segregation-selling-rental-next-year/','Study shortly before a sale'),('/faq/rental-sale-suspended-passive-losses-full-interest/','Entire-interest sales and passive losses')]
}
qindex=[];qid=0
for i,g in enumerate(groups):
 body=sec('The decision this guide resolves',g['rule'])+sec('A practical fact pattern',g['scenario'])+T.section('Records to gather before deciding',ul(g['records']))
 for q,a in g['qa']:
  qid+=1;qindex.append(dict(id=qid,question=q,topic=g['title'],url=route(g)+'#q'+str(qid)))
 first=qid-4
 block=T.faq_section([(E(q),p(a))for q,a in g['qa']])
 ids=iter(range(first,qid+1));block=re.sub('class="faq-item"',lambda m:m[0]+' id="q'+str(next(ids))+'"',block);body+=block
 body+=sec('How to turn the answers into a return decision','Write down the property owner, affected tax year, the factual test being used and the evidence supporting it. Reconcile the amount on the study or workpaper with the return schedule, identify any limitation and assign the filing task to a named preparer. If a fact is missing, resolve it before treating the estimated deduction as usable.')
 related=[(HUB,'Search all 100 STR and cost segregation questions'),(route(groups[(i-1)%20]),'Previous topic: '+groups[(i-1)%20]['title']),(route(groups[(i+1)%20]),'Next topic: '+groups[(i+1)%20]['title'])]+existing.get(g['slug'],[])
 body+=T.related_section(related,'Continue the planning sequence')
 save(route(g),g['title'],'Answers to five connected questions about '+g['title'].split(':')[0].lower()+'. Review IRS sources, practical facts, records and filing responsibilities.',body,g['sources'],g['qa'])
body=sec('Start with the fact that changes your answer','Explore 100 researched questions across 20 focused guides. They cover short-term rental tax qualification, cost segregation, bonus depreciation and look-back work on existing LTRs and STRs. These are planning questions selected from recurring rule distinctions and existing AE question coverage; they are not a measured search-volume ranking.')
body+=T.section('Choose your starting point','<ol><li>'+link(route(groups[0]),'New STR: classify the activity before projecting W-2 offsets')+'</li><li>'+link(route(groups[10]),'Old LTR: reconstruct historical basis and depreciation')+'</li><li>'+link(route(groups[11]),'Existing STR: separate catch-up depreciation from loss usability')+'</li><li>'+link(route(groups[12]),'Report ready: determine the Form 3115 or correction route')+'</li><li>'+link(route(groups[18]),'Selling soon: model recapture and exit economics')+'</li></ol>')
body+=T.section('Three distinctions that prevent expensive mistakes',ul(['Seven-day average stays and material participation are separate tests; Schedule C and self-employment tax are separate questions too.','A new study does not reset old acquisition dates, original bonus rates, asset basis or passive-loss carryforwards.','A deduction is not tax savings, and a computed deduction is not necessarily usable this year.']))
body+=T.section('Browse 20 topic guides','<ol>'+''.join('<li>'+link(route(g),g['title'])+'</li>'for g in groups)+'</ol>')
controls='<label for="rental-question-search">Search the 100 rental tax questions</label><input id="rental-question-search" type="search" placeholder="Try old rental, 3115, spouse, seven days or bonus" aria-describedby="rental-question-count" style="display:block;width:100%;padding:14px;margin:12px 0"><p id="rental-question-count" role="status" aria-live="polite">100 questions</p>'
items=''.join('<li data-rental-question>'+link(q['url'],q['question'])+' <small>— '+E(q['topic'])+'</small></li>'for q in qindex)
body+=T.section('Find your question',controls+'<ol id="rental-question-list">'+items+'</ol><noscript><p>All questions and guide links remain available without JavaScript.</p></noscript>')
body+=T.related_section([('/short-term-rental-tax-loophole-2026/','STR loophole: qualification and limitations'),('/cost-segregation-study/','Cost segregation study services'),('/bonus-depreciation-rental-property/','Rental bonus depreciation guide'),('/amended-return-vs-form-3115/','Amendment versus Form 3115')])
save(HUB,'100 STR Tax and Cost Segregation Questions','Find answers to 100 STR tax, cost segregation and bonus depreciation questions, including look-back studies on old LTRs and STRs, Form 3115 and sale taxes.',body,['925','527','946','bonus','3115','544'],extra='<script defer src="/assets/rental-question-search.js"></script>')
(ROOT/'assets/rental-question-search.js').write_text("""'use strict';
(()=>{const input=document.getElementById('rental-question-search'),count=document.getElementById('rental-question-count'),rows=[...document.querySelectorAll('[data-rental-question]')];if(!input||!count)return;input.addEventListener('input',()=>{const terms=input.value.toLowerCase().trim().split(/\\s+/).filter(Boolean);let visible=0;rows.forEach(row=>{row.hidden=!terms.every(term=>row.textContent.toLowerCase().includes(term));if(!row.hidden)visible++;});count.textContent=visible+' of '+rows.length+' questions';});})();
""")
# Improve existing entry points without duplicating their primary answer or erasing dates.
entrypoints=['/blog/','/resources/','/short-term-rental-tax-loophole-2026/','/short-term-rental-tax-strategy/','/cost-segregation-study/','/bonus-depreciation-rental-property/','/amended-return-vs-form-3115/','/real-estate-tax-planning/','/cost-segregation-documents-checklist/','/faq/']
entrypoints+=list(dict.fromkeys(u for xs in existing.values()for u,_ in xs))
for path in entrypoints:
 f=ROOT/path.strip('/')/'index.html'
 if not f.exists():continue
 s=f.read_text();marker='rental-library-20261108';s=re.sub('<!-- '+marker+':start -->.*?<!-- '+marker+':end -->','',s,flags=re.S)
 block='<!-- '+marker+':start -->'+T.section('STR, older rentals and depreciation: find the next answer','<p>'+link(HUB,'Browse 100 STR tax and cost segregation questions')+' across qualification, participation, bonus timing, old-rental catch-up depreciation and sale taxes.</p><ul><li>'+link(route(groups[10]),'Cost segregation on an old LTR')+'</li><li>'+link(route(groups[11]),'Look-back study on an existing STR')+'</li><li>'+link(route(groups[12]),'Form 3115 and catch-up depreciation')+'</li><li>'+link(route(groups[18]),'Selling after cost segregation')+'</li></ul>')+'<!-- '+marker+':end -->'
 s=s.replace('</main>',block+'</main>',1);f.write_text(s);updated.append(path)
# Preserve library discovery through future deterministic blog archive renders.
f=ROOT/'scripts/blog_archive.py';s=f.read_text();needle="    companions = external_companion_block(landing.read_text()) if landing.exists() else ''"
if 'library_feature = 'not in s:s=s.replace(needle,needle+"\n    library_feature = ''\n    if landing.exists():\n        match = re.search(r'<!-- rental-library-20261108:start -->.*?<!-- rental-library-20261108:end -->', landing.read_text(), re.S)\n        library_feature = match[0] if match else ''")
s=s.replace('if page == 1 and companions:', 'if page == 1 and (companions or library_feature):').replace("match[0] + companions, body", "match[0] + companions + library_feature, body");f.write_text(s)
# Register resource sitemap in both sitemap indexes; do not add resource pages to the chronological blog.
xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>'+T.SITE+u+'</loc><lastmod>'+DATE+'</lastmod></url>\n'for u in pages)+'</urlset>\n';(ROOT/'sitemap-rental-question-library.xml').write_text(xml)
for name in ['sitemap-index.xml','sitemap_index.xml']:
 f=ROOT/name;s=f.read_text()
 if '/sitemap-rental-question-library.xml'not in s:s=s.replace('</sitemapindex>','<sitemap><loc>'+T.SITE+'/sitemap-rental-question-library.xml</loc></sitemap>\n</sitemapindex>')
 f.write_text(s)
f=ROOT/'content/reviewed-content-lastmod.json';dates=json.loads(f.read_text());dates.update({u:DATE for u in pages+updated});f.write_text(json.dumps(dates,indent=2)+'\n')
(D/'questions-index.json').write_text(json.dumps(qindex,indent=2)+'\n');(D/'scope.json').write_text(json.dumps(dict(hub=HUB,pages=pages,updated=updated,questions=100,spokes=20,published=DATE,gscMetricsAvailable=False,queryVolumeVerified=False),indent=2)+'\n')
print(json.dumps(dict(pages=len(pages),questions=len(qindex),existing_entrypoints=len(updated))))
