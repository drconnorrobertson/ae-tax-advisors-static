#!/usr/bin/env python3
"""Build a sourced, decision-specific comparison pair for 25 additional brands.

Dataset facts are deliberately brief; scenarios and evaluation criteria are AE's
editorial analysis. Preserve all unrelated comparison pages and sitemap entries.
"""
import html
import json
import re
from pathlib import Path
import site_template as T

DATE = '2026-10-06'
HUB = '/compare/small-business-tax-firms/'
FIRMS = json.loads((T.ROOT / 'small_business_firms.json').read_text())
BY_SLUG = {f['slug']: f for f in FIRMS}

def e(s): return html.escape(s, quote=True)
def p(s): return '<p>' + s + '</p>'
def link(url, label): return '<a href="'+e(url)+'">'+e(label)+'</a>'
def ul(items): return '<ul class="takeaway-list">'+''.join('<li>'+s+'</li>' for s in items)+'</ul>'
def route(f, alt=False): return '/compare/'+f['slug']+('-alternatives/' if alt else '-vs-ae-tax/')
def table(rows):
    return '<div style="overflow-x:auto"><table class="compare-table"><caption>Proposal comparison: requirements to confirm with both firms</caption><thead><tr><th scope="col">Workstream</th><th scope="col">What to request</th><th scope="col">Evidence to compare</th></tr></thead><tbody>'+''.join('<tr><th scope="row">'+e(a)+'</th><td>'+e(b)+'</td><td>'+e(c)+'</td></tr>' for a,b,c in rows)+'</tbody></table></div>'

def disclosure(f):
    return p('Published by AE Tax Advisors, a competing provider; no affiliation or endorsement by '+e(f['name'])+' is implied. Reviewed October 6, 2026. Service descriptions below come from public materials. Scenarios and buyer-fit judgments are our editorial analysis, not client testimonials or verified comparative outcomes.')

def sources(f):
    extra=[link('https://www.bill.com/webinars/tax-prep','BILL webinar: Accountfully acquisition context')] if f['slug']=='accountfully' else []
    return ul([link(f['source'], f['name']+' official service information'),link(f['marketing'],'Observed public marketing resource')]+extra+[link('/pricing/','AE scope and current pricing')])+p('Observed marketing: '+e(f['signal'])+'. Public visibility does not establish advertising spend, search volume, market share or service quality. Confirm current availability, personnel, licensing where relevant, fees and deliverables directly.')

def ae(f):
    return p('Consider AE when the assignment is to connect business, property and household tax decisions. For this situation, ask AE to propose '+e(f['deliverable'])+'. Evaluate the assigned reviewer, assumptions, action dates and separately scoped implementation work. '+link('/pricing/','Review current AE scope and fees')+' before treating a planning proposal as a quote for preparation, bookkeeping or another specialist service.')

def write(path,title,desc,sections,faqs,citations):
    trail=[('Home','/'),('Compare','/compare/'),('Small-business tax firms',HUB)]
    if path != HUB: trail.append((title,path))
    body=T.page_header(h1=title,subtitle=desc,trail=trail)
    body+=''.join(T.section(h,b) for h,b in sections)
    if faqs: body+=T.faq_section(faqs)
    body+=T.related_section([(HUB,'Browse all 25 firms'),('/tools/tax-advisor-engagement-scorecard/','Compare written proposals'),('/pricing/','AE scope and fees')])
    schemas=[T.article_schema(title=title,description=desc,url=T.SITE+path,published=DATE,modified=DATE,section='Small-business tax advisor comparisons',citations=citations),T.breadcrumb_schema(trail)]
    if faqs: schemas.append(T.faq_schema(faqs))
    short_title=title.split(':',1)[0]
    T.write_page(path,T.build_page(title=short_title,description=desc,path=path,body=body,schemas=schemas,published=DATE,modified=DATE))

def build_pair(f):
    name=f['name']
    questions=ul([e(q) for q in f['questions']])
    records=ul([e(s) for s in f['records']])
    comparison_faqs=[
        ('When should I compare '+name+' with AE?',p('Use both proposals to evaluate '+e(f['focus'])+'. A published service category is a starting point; ask each firm for a written assignment based on your records and decision date.')),
        ('What should I request in the proposal?',p('For the illustrative situation above, request '+e(f['deliverable'])+'. Confirm the professional responsible for each output and what remains with you or another provider.')),
        ('Does this comparison establish which firm saves more tax?',p('No. No matched client outcomes or comparative savings were verified. Evaluate assumptions, supporting evidence and complete costs before relying on a projected result.')),
    ]
    write(route(f),name+' vs AE Tax Advisors: '+f['focus'].capitalize(),
          'Compare '+name+' and AE on '+f['focus']+', required records, implementation responsibilities and total engagement cost.',[
        ('The buying decision',p('This comparison is for an owner evaluating '+e(f['focus'])+'. '+name+' belongs on the shortlist when its published service model addresses that assignment. AE belongs on the shortlist when owner-level business and property decisions need coordinated tax review. The right proposal may involve one firm or a defined collaboration.')+disclosure(f)),
        ('What '+name+' publishes',p(e(f['services']))+p(link(f['source'],'Read the official service description')+'. Do not interpret a service omitted from this summary as a capability the provider lacks.')),
        ('A specific owner scenario',p(e(f['scenario']))+p('Illustrative scenario, not a reported client result. Send the same background and target decision date to both firms so you can compare proposed work on equal terms.')),
        ('The issue to resolve before choosing',p(e(f['risk']))+questions),
        ('Compare deliverables and complete cost',table([
            ('Decision review',f['deliverable'],'A sample output, assumptions and review date.'),
            ('Supporting records',', '.join(f['records']),'Who reconciles missing or conflicting information.'),
            ('Implementation','Named owner for each agreed action.','Completion evidence and unresolved-item tracking.'),
            ('Fees and support','Planning, preparation, recurring support and specialist work priced separately.','First-year total, later obligations and support end dates.')])+p('No matched current quote was obtained from these two providers. A monthly service price and an advisory-project fee can purchase different work. Ask both firms to price the same entities, tax years and outputs; include cleanup, payroll, extra states and third-party work where applicable.')),
        ('How to evaluate AE for this assignment',ae(f)),
        ('Prepare for the first conversation',records+p('Identify which records your current provider already holds and obtain permission for any direct exchange. Agree who completes open returns and handles notices before changing advisors. '+link(route(f,True),'Explore '+name+' alternatives')+' if a different service model would address your reason for looking.')),
        ('Sources and research limits',sources(f))],comparison_faqs,[f['source'],f['marketing'],T.SITE+'/pricing/'])

    shortlist=[]
    for slug in f['peers']:
        peer=BY_SLUG[slug]
        shortlist.append('<h3>'+link(route(peer),peer['name'])+'</h3>'+p('Interview this provider if your priority is '+e(peer['focus'])+'. Ask how that assignment would fit alongside the work you already receive. '+link(route(peer,True),'Read its alternatives guide')+'.'))
    alternative_faqs=[
        ('Why look for '+name+' alternatives?',p('A reason to compare is '+e(f['switch'])+'. This is a possible buyer need, not a claim that '+e(name)+' cannot address it. First ask the current provider whether a revised scope would solve the issue.')),
        ('Do I need to move all my accounting?',p(e(f['alternative']))),
        ('How should I compare the shortlist?',p('Send each candidate the assignment and records listed here. Compare its proposed output, responsible reviewer, dependencies, full fee and transition plan. The shortlist is organized by potential fit and is not a ranking.')),
    ]
    write(route(f,True),name+' Alternatives: '+f['switch'].capitalize(),
          'Explore '+name+' alternatives for '+f['switch']+'. Compare a scope adjustment, specialist engagement and relevant providers.',[
        ('Start with the reason for looking',p('This guide addresses '+e(f['switch'])+'. A useful alternative changes the work or relationship in a way that solves that need. First describe what is missing from the current arrangement and ask whether it can be supplied through a revised scope.')+disclosure(f)),
        ('Three ways to change the arrangement',
         '<h3>Adjust the current scope</h3>'+p('Request a written addition that states the new deliverable, fee and completion date. This can preserve continuity when existing preparation or bookkeeping is dependable. Do not assume the new assignment is covered merely because advisory appears in a service description.')+
         '<h3>Add a defined specialist engagement</h3>'+p(e(f['alternative']))+
         '<h3>Replace the recurring relationship</h3>'+p('A full replacement makes more sense when the operating workflow itself needs to change. Before signing, require a transition calendar covering records, software access, open filings and recurring payment obligations. Keep the outgoing and incoming responsibilities explicit.')),
        ('A relevant provider shortlist',p('The options below are interview candidates, not ranked recommendations. They have different service emphases; the same firm may be suitable for more than one kind of assignment.')+'<h3>'+link('/discovery/','AE Tax Advisors')+'</h3>'+ae(f)+''.join(shortlist)),
        ('The assignment to send each candidate',p(e(f['scenario']))+p('Ask for '+e(f['deliverable'])+'. Explain what is already handled by your bookkeeper, preparer, payroll team or another specialist. A candidate should identify dependencies before promising a completion date.')),
        ('Records and questions for the shortlist',records+questions),
        ('Evaluate the response before switching',p(e(f['risk']))+p('Compare whether the proposal answers your actual reason for looking. Ask what happens if records arrive late, a recommendation changes or implementation cannot be completed before the decision date. Obtain a full first-year cost and the terms for later work, then choose the arrangement with clear responsibility for the outputs you need. '+link(route(f),'Read the direct '+name+' vs AE comparison')+'.')),
        ('Sources and research limits',sources(f))],alternative_faqs,[f['source'],f['marketing']]+[BY_SLUG[s]['source'] for s in f['peers']])

def build_hub():
    sections=[('Choose a firm around your next business decision',p('These 25 additional brands publish small-business tax services or tax-inclusive accounting support. Some are CPA practices; others are service platforms or broader accounting providers. Each pair below addresses a distinct owner situation and links the official materials reviewed. Published by AE Tax Advisors, a competing provider; this is an editorial buying guide, not an independent ranking.')),
              ('Why these brands were selected',p('We observed public marketing through podcasts, webinars, calculators, guides, industry pages and consultation offers. That establishes visible marketing activity, not paid-ad intensity or search demand. We excluded brands already covered in this comparison collection and distinguished similarly named businesses. The research date is October 6, 2026.'))]
    for group in dict.fromkeys(f['group'] for f in FIRMS):
        body=''
        for f in FIRMS:
            if f['group']!=group: continue
            body+='<h3>'+e(f['name'])+'</h3>'+p('Decision focus: '+e(f['focus'])+'.')+p('Observed marketing: '+link(f['marketing'],f['signal'])+'.')+p(link(route(f),f['name']+' vs AE')+' · '+link(route(f,True),f['name']+' alternatives'))
        sections.append((group,body))
    sections.extend([('When to put AE on the shortlist',p('Consider AE for a coordinated business, property and household tax-planning assignment. Bring a decision date, entity list and available records. Request a scope that identifies the output, reviewer and implementation responsibilities, then compare it against the same assignment from the other firms. '+link('/pricing/','Review AE scope and pricing')+' or '+link('/discovery/','book a call')+'.')),
                     ('How to use the comparison pairs',p('The direct comparisons explain the published service model and a practical owner scenario. Alternatives guides consider three routes: amend an existing scope, add a specialist or replace the recurring provider. Relevant peer links help you build a focused shortlist. No comparative client savings, satisfaction scores or guaranteed rankings are asserted.'))])
    write(HUB,'25 Small-Business Tax Firms: Comparisons and Alternatives','Explore 25 additional tax and accounting providers, with 50 decision-specific AE comparisons and alternatives guides for business owners.',sections,[],[f['source'] for f in FIRMS])

def update_navigation():
    path=T.ROOT/'compare/index.html'
    text=path.read_text()
    marker='small-business-25-cluster'
    text=re.sub(r'<section class="content-section" id="'+marker+r'">.*?</section>','',text,flags=re.S)
    block='<section class="content-section" id="'+marker+'"><div class="container narrow"><h2>25 more small-business tax firms</h2>'+p('Explore 50 new comparisons and alternatives guides organized around owner decisions, from first hires to related entities and business exits.')+p(link(HUB,'Browse the 25-firm guide'))+ul([link(route(f),f['name']+' vs AE')+' · '+link(route(f,True),'Alternatives') for f in FIRMS])+'</div></section>'
    text=text.replace('</main>',block+'</main>')
    text=re.sub(r'("dateModified":\s*")[^"]+',r'\g<1>'+DATE,text)
    path.write_text(text)

def update_sitemaps():
    paths=[HUB,'/compare/']+[route(f,a) for f in FIRMS for a in [False,True]]
    for filename in ['sitemap.xml','sitemap-comparisons.xml']:
        path=T.ROOT/filename
        text=path.read_text()
        for route_path in paths:
            url=T.SITE+route_path
            match=re.search(r'<url>\s*<loc>'+re.escape(url)+r'</loc>.*?</url>',text,re.S)
            if match:
                old=match.group(0)
                new=re.sub(r'<lastmod>[^<]*</lastmod>','<lastmod>'+DATE+'</lastmod>',old)
                if '<lastmod>' not in old: new=new.replace('</loc>','</loc><lastmod>'+DATE+'</lastmod>',1)
                text=text[:match.start()]+new+text[match.end():]
            else:
                text=text.replace('</urlset>','  <url><loc>'+url+'</loc><lastmod>'+DATE+'</lastmod></url>\n</urlset>')
        path.write_text(text)

if __name__=='__main__':
    assert len(FIRMS)==len(BY_SLUG)==25
    for f in FIRMS: build_pair(f)
    build_hub()
    update_navigation()
    update_sitemaps()
    print('Built 50 comparison/alternatives pages and a 25-firm hub; updated index and two sitemaps.')
