#!/usr/bin/env python3
"""Maintain the October 6 brand-comparison cluster without rewriting other pages."""
import html
import json
import re
import site_template as T

DATE = '2026-10-06'
HUB = '/compare/p4-tax-delerme-cpa-gelt/'
FIRMS = [
    dict(slug='p4-tax', name='P4 Tax & Consulting', short='P4 Tax',
         url='https://p4taxes.com/',
         overview='P4 Tax & Consulting publishes tax planning, entity structuring and compliance for real estate investors, tech founders and business owners. Its website emphasizes direct access to Chris Pantoja, CPA, and nationwide service from Austin.',
         fit='direct CPA access and a focus on founder equity, exits or real estate operations are central to your decision',
         scenario='You own an operating company and several rental entities, and a property sale is approaching. Before comparing fees, ask each firm to map the ownership records, return responsibilities and transaction deadlines. A consultation should identify what can be decided now and what needs supporting records.',
         questions=[('Direct advisor access', 'Who will conduct planning meetings and review recommendations when the lead CPA is unavailable?'),
                    ('Founder or property transaction', 'Which transaction documents need review before signing, and who coordinates with counsel?'),
                    ('K-1 handoff', 'What is the delivery schedule, and who reconciles partner information with the owner return?')]),
    dict(slug='delerme-cpa', name='Delerme CPA', short='Delerme CPA',
         url='https://www.delermecpa.com/tax-planning-services.htm',
         overview='Delerme CPA publishes proactive business and individual tax planning, multistate planning and tax-reduction coaching. Its broader Atlanta practice also lists accounting, outsourced CFO, international and cryptocurrency services.',
         fit='you want planning alongside accounting or CFO support, or need to evaluate its international or Puerto Rico offering',
         scenario='You run a profitable company, need better monthly financial reporting, and are considering a major change in where you live or operate. Separate the accounting work from the planning project, then identify any jurisdiction-specific work that requires its own specialist and proposal.',
         questions=[('Accounting and planning', 'Which monthly reports feed the tax projection, and who resolves discrepancies?'),
                    ('International scope', 'Which jurisdictions, entities and returns are included, and which require additional specialists?'),
                    ('Puerto Rico work', 'Is relocation-related work relevant to my actual goals, and is it a separate engagement?')]),
]

def p(text): return '<p>' + text + '</p>'
def li(items): return '<ul class="takeaway-list">' + ''.join('<li>'+s+'</li>' for s in items) + '</ul>'
def link(url, label): return f'<a href="{html.escape(url, quote=True)}">{html.escape(label)}</a>'
def table(headers, rows):
    return '<div class="ae-table-scroll" style="overflow-x:auto"><table class="compare-table"><caption>Decision framework reviewed October 6, 2026. Confirm actual deliverables in each proposal.</caption><thead><tr>' + ''.join('<th scope="col">'+h+'</th>' for h in headers) + '</tr></thead><tbody>' + ''.join('<tr><th scope="row">'+row[0]+'</th>'+''.join('<td>'+c+'</td>' for c in row[1:])+'</tr>' for row in rows) + '</tbody></table></div>'

def disclosure(f):
    return p('Published by AE Tax Advisors, a competing provider. This page is not affiliated with or endorsed by '+f['name']+'. Official materials were reviewed on October 6, 2026. Public descriptions do not establish the scope of a particular engagement. An unverified service or price should be confirmed directly.')

def ae_pitch():
    return p('AE focuses on business owners and real estate investors. Consider AE when you want business, property and household decisions discussed together, with a clear plan for who completes each action. '+link('/pricing/', 'Review AE scope and pricing')+'.')

def price_note():
    return p('AE standard advisory: $7,800, paid in two installments; no required annual planning renewal. Returns, amendments, studies and additional work are separate. '+link('/pricing/', 'See current terms')+'.')

def evaluation(f):
    return table(['Decision', 'Question for '+f['short'], 'Question for AE'], [(name, question, 'Request the same deliverable, responsible professional and deadline in writing.') for name, question in f['questions']])

def common_faqs(f, alternative=False):
    return [
      ('Is AE Tax Advisors a '+f['short']+' alternative?', '<p>Yes, it is an option to evaluate for a business or property planning engagement. Compare the records reviewed, written deliverables and implementation assignments against your actual needs.</p>'),
      ('Which firm is better for me?', '<p>Start with your next decision. Request a proposal for that decision from each firm, then compare the assigned advisor, required records, deadlines and complete project cost. This page does not rank firms by client outcomes.</p>'),
      ('Can I compare a planning fee with a filing fee?', '<p>Use separate columns for planning, preparation, implementation and future support. A filing-only fee and a planning engagement purchase different deliverables.</p>'),
      ('How do I avoid paying for overlapping work?', '<p>List the tasks already covered by your current provider. Ask the new firm to identify the additional work and agree a handoff before you approve the proposal.</p>'),
    ]

def write(path, title, desc, sections, faqs, citations, published=DATE):
    trail=[('Home','/'),('Compare','/compare/'),(title,path)]
    body=T.page_header(h1=title,subtitle=desc,trail=trail)+'\n'+ '\n'.join(T.section(h,b) for h,b in sections)
    if faqs: body += T.faq_section(faqs)
    body += T.related_section([(HUB,'Compare P4 Tax, Delerme CPA, Gelt and AE'),('/tools/tax-advisor-engagement-scorecard/','Compare written engagements'),('/pricing/','AE fees and scope')])
    schemas=[T.article_schema(title=title,description=desc,url=T.SITE+path,published=published,modified=DATE,section='Tax advisor comparisons',citations=citations),T.breadcrumb_schema(trail)]
    if faqs: schemas.append(T.faq_schema(faqs))
    T.write_page(path,T.build_page(title=title+' | AE Tax Advisors',description=desc,path=path,body=body,schemas=schemas,published=published,modified=DATE))

def build_firm(f):
    compare='/compare/'+f['slug']+'-vs-ae-tax/'
    alternative='/compare/'+f['slug']+'-alternatives/'
    source=p(link(f['url'], f['name']+' official services'))
    write(compare, f['short']+' vs AE Tax Advisors: Scope, Fees and Fit',
      'Compare '+f['short']+' with AE Tax Advisors on client fit, advisor access, implementation responsibilities and complete project cost.',
      [('The decision to make',p('Both firms advertise planning. The useful distinction is the engagement you can buy for the decision in front of you. Consider '+f['short']+' when '+f['fit']+'.')+ae_pitch()+disclosure(f)),
       ('What '+f['short']+' publishes',p(f['overview'])+source),
       ('Compare the work before the fee',evaluation(f)+price_note()+p('A current comparable '+f['short']+' fee was not verified in the reviewed materials. Ask for a written quote; do not infer that it is more expensive or less expensive than AE.')),
       ('A practical comparison scenario',p(f['scenario'])+p('Send both firms the same brief: the decision, target date, entities involved, current advisor and available documents. Ask for a sample deliverable with client details removed.')),
       ('Where AE belongs on your shortlist',p('Bring AE a coordinated planning question: what needs review, what needs a decision and who needs to implement it. Ask for assumptions, an action schedule and separately priced work. Compare those answers against '+f['short']+' using the same criteria.')),
       ('Before you switch',li(['Agree who completes open returns and responds to outstanding notices.','Confirm access to depreciation schedules, basis records and prior elections.','Define the start and end of support and any later engagement.'])+p(link(alternative,'Explore '+f['short']+' alternatives')))], common_faqs(f),[f['url'],T.SITE+'/pricing/'])
    write(alternative,f['short']+' Alternatives for Business Owners and Investors',
      'Considering '+f['short']+' alternatives? Build a shortlist around your tax planning, accounting, property or transaction needs.',
      [('Choose the alternative by the job',p('A useful alternative should solve the reason you are looking. Start with the work you need and the working relationship you prefer. Switching providers is only one option; a clearly scoped specialist engagement may also address the gap.')+disclosure(f)),
       ('Four approaches to compare',table(['Approach','Use it when','Confirm before signing'],[
          ('AE Tax Advisors','Business and property decisions need a coordinated planning conversation.','Written deliverables, implementation assignments and additional fees.'),
          ('P4 Tax & Consulting','Direct CPA access and founder or real estate focus are priorities.','Assigned advisor and transaction scope.'),
          ('Delerme CPA','Accounting, CFO support or international work should be evaluated alongside planning.','Separate workstreams and jurisdictions covered.'),
          ('Gelt','A platform-based workflow is important to how you manage the engagement.','Strategy scope alongside compliance and human review.')])+p('These are fit considerations, not a ranking or a claim that any firm lacks other capabilities. '+link(HUB,'See the sourced four-firm guide')+'.')),
       ('Define your reason for looking',li(['Communication: agree the meeting schedule and escalation process.','Implementation: identify who completes elections, documents and filings.','Complexity: list every entity, property and state to be reviewed.','Cost: compare the total project and later support, including third-party work.'])),
       ('Give the shortlist one concrete assignment',p(f['scenario'])+p('Ask each candidate for its proposed sequence of work. A useful answer explains the missing records, the decision owner and the deadline. Compare how each firm handles uncertainty before comparing projected savings.')),
       ('How to evaluate AE',ae_pitch()+p('Request a scope tied to the assignment above. If you only need a return prepared, ask for a preparation proposal. If multiple decisions interact, ask how the planning work will connect them. '+link(compare,'Read the '+f['short']+' vs AE comparison')+'.'))],common_faqs(f,True),[T.SITE+HUB,f['url']])

def hub():
    rows=[('AE Tax Advisors','Business and property planning','Start with records, deliverables and implementation assignments.'),
          ('P4 Tax & Consulting','Direct CPA relationship; founders and property owners','Confirm lead-advisor access and transaction scope.'),
          ('Delerme CPA','Planning alongside accounting and broader services','Separate accounting, jurisdiction-specific work and planning.'),
          ('Gelt','Tax strategy and compliance through a platform','Identify strategy work outside the filing package.')]
    links=[]
    for slug,name in [('p4-tax','P4 Tax'),('delerme-cpa','Delerme CPA'),('gelt','Gelt')]:
        links.append(link('/compare/'+slug+'-vs-ae-tax/',name+' vs AE')+' · '+link('/compare/'+slug+'-alternatives/',name+' alternatives'))
    write(HUB,'P4 Tax, Delerme CPA, Gelt and AE Tax Advisors Compared',
      'Compare four tax advisory options by client fit, service model, planning scope and implementation. Explore individual comparisons and alternatives.',
      [('Start with the decision you need to make',p('A business owner with rentals needs a different scope from a founder preparing a transaction or an owner seeking monthly financial reporting. Use this guide to choose whom to interview, then request proposals for the same assignment. Published by AE Tax Advisors, a competing provider; this is an editorial comparison, not an independent ranking.')),
       ('Compare the published models',table(['Firm','Published emphasis','Buyer question'],rows)),
       ('Why put AE on the shortlist?',p('If you need several business and property decisions connected, ask AE to explain the sequence of review and implementation. The proposal should show how the records support the recommendations and where separate work is required. An attractive estimate becomes useful when you can see the assumptions, fees and actions behind it.')),
       ('Compare complete project cost',price_note()+p('Gelt lists business filing and quarterly estimates from $2,500 per entity/year and business strategy plans from $8,000. It states strategy is excluded from compliance pricing. These are starting prices, not a combined quote. '+link('https://www.joingelt.com/','Verify Gelt pricing')+'.')+p('No comparable P4 or Delerme fee was verified. Ask each firm to price the same entities, tax years and workstreams. Different package names do not establish equivalent coverage.')),
       ('A proposal checklist',li(['Name the decision and the date it needs to be resolved.','List the entities, properties, jurisdictions and tax years.','Identify who reviews recommendations and who completes each action.','Separate planning, preparation, study, legal and administrator fees.','Confirm support dates and terms for additional future work.'])),
       ('Individual comparisons and alternatives',li(links)),
       ('Sources and research limits',li([link('https://p4taxes.com/','P4 official website'),link('https://www.delermecpa.com/tax-planning-services.htm','Delerme planning'),link('https://www.delermecpa.com/','Delerme broader services'),link('https://www.joingelt.com/','Gelt services and pricing'),link('/pricing/','AE pricing')])+p('Reviewed October 6, 2026. Delerme’s taxsavings subdomain currently redirects to a Puerto Rico page; that campaign does not describe its entire practice. No comparative savings, satisfaction ranking or superiority claim is established by this review.'))],[],['https://p4taxes.com/','https://www.delermecpa.com/','https://www.joingelt.com/',T.SITE+'/pricing/'])

def enrich_gelt():
    marker='brand-comparison-update'
    for slug in ['gelt-vs-ae-tax','gelt-alternatives']:
        path=T.ROOT/'compare'/slug/'index.html'
        text=path.read_text()
        section='<section class="content-section" id="'+marker+'"><div class="container narrow"><h2>Compare Gelt with P4 Tax, Delerme CPA and AE</h2>'+p('When evaluating a platform-based engagement, ask who approves projections, who owns implementation tasks and how completed work is recorded. Use the same assignment and entity list for each proposal. '+link(HUB,'Review the four-firm comparison')+'.')+'<p>Updated October 6, 2026. Published by AE Tax Advisors, a competing provider.</p></div></section>'
        text=re.sub(r'<section class="content-section" id="'+marker+r'">.*?</section>','',text,flags=re.S)
        text=text.replace('</main>',section+'</main>')
        # Correct the existing alternatives page's inaccurate independent label.
        text=text.replace('This independent comparison uses','This AE-authored comparison uses')
        text=re.sub(r'("dateModified":\s*")[^"]+',r'\g<1>'+DATE,text)
        text=re.sub(r'(<meta property="article:modified_time" content=")[^"]+',r'\g<1>'+DATE+'T00:00:00-04:00',text)
        path.write_text(text)

def update_index():
    path=T.ROOT/'compare/index.html'
    text=path.read_text()
    marker='p4-delerme-gelt-cluster'
    block='<section class="content-section" id="'+marker+'"><div class="container narrow"><h2>P4 Tax, Delerme CPA and Gelt comparisons</h2>'+p('Compare client fit, project scope and responsibilities across the brands you are considering.')+li([link(HUB,'P4 Tax, Delerme CPA, Gelt and AE comparison guide')]+[link('/compare/'+f['slug']+'-vs-ae-tax/',f['short']+' vs AE')+' · '+link('/compare/'+f['slug']+'-alternatives/',f['short']+' alternatives') for f in FIRMS])+ '</div></section>'
    text=re.sub(r'<section class="content-section" id="'+marker+r'">.*?</section>','',text,flags=re.S)
    text=text.replace('</main>',block+'</main>')
    text=re.sub(r'("dateModified":\s*")[^"]+',r'\g<1>'+DATE,text)
    path.write_text(text)

def update_sitemap():
    # Preserve unrelated inventory and lastmod values from the committed map.
    path=T.ROOT/'sitemap.xml'
    text=path.read_text()
    paths=[HUB,'/compare/','/compare/gelt-vs-ae-tax/','/compare/gelt-alternatives/']
    paths += ['/compare/'+f['slug']+suffix+'/' for f in FIRMS for suffix in ['-vs-ae-tax','-alternatives']]
    for route in paths:
        url=T.SITE+route
        pattern=r'<url>\s*<loc>'+re.escape(url)+r'</loc>.*?</url>'
        match=re.search(pattern,text,re.S)
        if match:
            old=match.group(0)
            new=re.sub(r'<lastmod>[^<]*</lastmod>','<lastmod>'+DATE+'</lastmod>',old)
            if '<lastmod>' not in old: new=new.replace('</loc>','</loc><lastmod>'+DATE+'</lastmod>',1)
            text=text[:match.start()]+new+text[match.end():]
        else:
            text=text.replace('</urlset>','<url><loc>'+url+'</loc><lastmod>'+DATE+'</lastmod></url></urlset>')
    path.write_text(text)

if __name__=='__main__':
    for firm in FIRMS: build_firm(firm)
    hub()
    enrich_gelt()
    update_index()
    update_sitemap()
    print('Built five pages; updated two Gelt pages and the comparison index.')
