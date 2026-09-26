"""Apply the 100-topic editorial release without regenerating unrelated pages.

Run after legacy content generators, before indexes and discovery files.
The manifest records substantive page work separately from navigation changes.
"""
from __future__ import annotations
import csv
import html
import io
import json
import re
from pathlib import Path
import site_template as T
from sprint_editorial import MODULES
from sprint_new_guides import EXTRA, CASE_EXTRA

ROOT = Path(__file__).resolve().parent
DATE = '2026-09-26'
START = '<!-- content-sprint-100:start -->'
END = '<!-- content-sprint-100:end -->'
HUB = '/guides/owner-tax-decisions/'
REPLACE = {1,9,13,21,23,29,39,43,67,83,84,85,87,88,89,*range(91,97)}
SOURCES = {
 'rental': ('https://www.irs.gov/publications/p527', 'IRS Publication 527: residential rental property'),
 'depreciation': ('https://www.irs.gov/publications/p946', 'IRS Publication 946: depreciation methods and eligibility'),
 'passive': ('https://www.irs.gov/publications/p925', 'IRS Publication 925: passive activity and at-risk rules'),
 'basis': ('https://www.irs.gov/publications/p551', 'IRS Publication 551: basis of assets'),
 'sale': ('https://www.irs.gov/publications/p544', 'IRS Publication 544: property dispositions and recapture'),
 'method': ('https://www.irs.gov/instructions/i3115', 'IRS Form 3115 instructions and current procedural references'),
 'amend': ('https://www.irs.gov/taxtopics/tc308', 'IRS Topic 308: amended returns'),
 'study': ('https://www.irs.gov/pub/irs-pdf/p5653.pdf', 'IRS cost segregation audit technique guide'),
 'payroll': ('https://www.irs.gov/publications/p15', 'IRS Publication 15: employer and reimbursement rules'),
 'home': ('https://www.irs.gov/publications/p587', 'IRS Publication 587: business use of a home'),
 'retirement': ('https://www.irs.gov/publications/p560', 'IRS Publication 560: small-business retirement plans'),
 'corporation': ('https://www.irs.gov/publications/p542', 'IRS Publication 542: corporations and distributions'),
 'scorp': ('https://www.irs.gov/businesses/small-businesses-self-employed/s-corporations', 'IRS: S corporations'),
 'compensation': ('https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues', 'IRS: S corporation compensation'),
 'qbi': ('https://www.irs.gov/newsroom/qualified-business-income-deduction', 'IRS: qualified business income deduction'),
 'newlaw': ('https://www.irs.gov/newsroom/working-families-tax-cuts', 'IRS: current legislation and effective-date guidance'),
}
GROUPS = [
 ('Cost segregation decisions','/cost-segregation-study/'),
 ('Residential property types','/cost-segregation-study/'),
 ('Short-term rental planning','/short-term-rental-tax-strategy/'),
 ('Long-term rental planning','/long-term-rental-tax-planning/'),
 ('Depreciation and return corrections','/amended-tax-returns/'),
 ('Property basis and sales','/real-estate-tax-planning/'),
 ('Business and rental ownership','/business-owner-tax-planning/'),
 ('Proactive business advisory','/business-owner-tax-planning/'),
 ('Buyer guides and comparisons','/compare/'),
 ('Worked examples and implementation','/case-studies/'),
]

def records():
    return [dict(id=int(n),path=p,title=t) for n,p,t in
            csv.reader((ROOT/'content_sprint_100.tsv').read_text().splitlines(),delimiter='\t')]

def references(n):
    if n<=20: keys=['study','depreciation','basis']
    elif n<=40: keys=['rental','passive']
    elif n<=50: keys=['depreciation','method','amend']
    elif n<=60: keys=['basis','depreciation','sale']
    elif n<=70: keys=['passive','corporation','scorp']
    elif n<=80: keys=['scorp','payroll']
    elif n<=90: keys=['study'] if n<=85 else ['scorp']
    else: keys=['depreciation','passive'] if n<=95 else ['scorp','payroll']
    overrides={7:['passive','depreciation'],37:['rental','basis'],46:['basis'],
      54:['depreciation','newlaw'],55:['depreciation'],74:['compensation'],
      75:['payroll'],76:['home','payroll'],77:['rental'],78:['retirement'],79:['qbi','newlaw']}
    return [SOURCES[k] for k in overrides.get(n,keys)]

def p(text): return '<p>'+html.escape(text)+'</p>'

def normalize_cta(text):
    def anchor(m):
        opening,label=m.group(1),m.group(2)
        href=re.search(r'href=["\']([^"\']+)',opening)
        if href and (href.group(1).rstrip('/') in ('/discovery','https://www.aetaxadvisors.com/discovery')
                     or 'widget/booking/FggCeBoxIuOuZZrTaVV1' in href.group(1)):
            return opening+'Book a Call</a>'
        return m.group(0)
    return re.sub(r'(<a\b[^>]*>)(.*?)</a>',anchor,text,flags=re.S|re.I)

def module(row,full=False):
    n=row['id'];m=MODULES[n]
    body=p(m['decision'])
    if full:
        for heading,text in EXTRA.get(n,[]): body+='<h3>'+html.escape(heading)+'</h3>'+p(text)
    body+='<h3>Illustrative decision</h3>'+p(m['example'])
    if n in CASE_EXTRA:
        heading,text=CASE_EXTRA[n]
        body+='<h3>'+heading+'</h3>'+p(text)
        body+='<h3>What this example does and does not establish</h3>'+p('The facts and numbers on this page are hypothetical teaching inputs. They are not a verified client result, a filed-return outcome or a prediction of typical savings. An actual engagement requires source records, applicable-year analysis and a final return reconciliation. No individual professional review is claimed. Cost segregation and other project work are separately scoped from advisory.')
    body+='<h3>Records and decisions to prepare</h3><ul>'+''.join('<li>'+html.escape(x)+'</li>' for x in m['checklist'])+'</ul>'
    sources=references(n)
    body+='<p class="post-meta">Decision guide updated September 26, 2026. AE Tax Advisors Team.</p>'
    body+='<p>Primary references for this decision:</p><ul>'+''.join(f'<li><a href="{u}">{html.escape(label)}</a></li>' for u,label in sources)+'</ul>'
    if n==83:
        body+='<h3>Official provider information</h3><ul>'+''.join(f'<li><a href="{u}">{label}</a></li>' for u,label in [('/cost-segregation-study/','AE Tax Advisors study scope'),('https://www.kbkg.com/cost-segregation','KBKG cost segregation'),('https://cssiservices.com/','CSSI services'),('https://www.recostseg.com/','R.E. Cost Seg')])+'</ul>'
    if n in (88,89):
        body+='<h3>Verify current scope directly</h3><ul>'+''.join(f'<li><a href="{u}">{label}</a></li>' for u,label in [('/pricing/','AE published pricing'),('https://www.peterholtzcpa.com/services/','Peter Holtz CPA services'),('https://primepathadvisory.com/terms','Prime Path Advisory service terms'),('https://neiljesani.com/services/','Neil Jesani Advisors services')])+'</ul>'
    group,hub=GROUPS[(n-1)//10]
    body+=p('Examples illustrate decisions, not guaranteed outcomes. Apply the rules for the relevant tax year and review the underlying facts before filing.')
    body+=f'<p><a href="{hub}">{html.escape(group)}</a> · <a href="{HUB}">Browse owner tax decisions</a> · <a href="/editorial-policy/">Editorial standards</a></p>'
    body+='<div class="cta-buttons"><a class="btn-cta" href="/discovery/">Book a Call</a></div>'
    return START+T.section(m['heading'],body)+END

def update_dates(text):
    def ld(m):
        data=json.loads(m.group(1))
        def walk(v):
            if isinstance(v,dict):
                if v.get('@type') in ['Article','BlogPosting','WebPage']: v['dateModified']=DATE
                for child in v.values():walk(child)
            elif isinstance(v,list):
                for child in v:walk(child)
        walk(data)
        return T.jsonld(data)
    text=re.sub(r'<script type="application/ld\+json">(.*?)</script>',ld,text,flags=re.S)
    return re.sub(r'(<meta property="article:modified_time" content=")[^"]+',r'\g<1>'+DATE+'T12:00:00-04:00',text)

def main():
    rows=records();manifest=[]
    prior_path=ROOT/'content_sprint_100_manifest.json'
    prior={r['id']:r for r in json.loads(prior_path.read_text())} if prior_path.exists() else {}
    assert len(rows)==100 and set(MODULES)==set(range(1,101))
    assert len({r['path'] for r in rows})==100
    for row in rows:
        n=row['id'];path=ROOT/row['path'].strip('/')/'index.html'
        existed=path.exists();old=path.read_text() if existed else ''
        is_new=prior.get(n,{}).get('action')=='new' or not existed
        full=is_new or n in REPLACE
        if full:
            assert n in EXTRA or n in CASE_EXTRA,(n,'Missing complete narrative')
            category=GROUPS[(n-1)//10][0]
            description='Review '+row['title'][0].lower()+row['title'][1:].rstrip('?')+'. Practical decisions, records and examples. Book a call with AE Tax Advisors.'
            if len(description)>175: description=row['title'].rstrip('?')+': decisions, supporting records and next steps with AE Tax Advisors.'
            published_match=re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})',old)
            published=published_match.group(1) if published_match else DATE
            trail=[('Home','/'),('Owner tax decisions',HUB),(row['title'],row['path'])]
            body=T.page_header(h1=html.escape(row['title']),subtitle='Practical guidance for business owners and residential rental investors.',trail=trail,cta='Book a Call')
            if n in CASE_EXTRA: body+=T.section('Hypothetical planning example',p('This page is an educational worked example. It does not represent a verified AE client outcome.'))
            body+=module(row,True)
            title=row['title'] if len(row['title'])>61 else row['title']+' | AE Tax'
            output=T.build_page(title=title,description=description,path=row['path'],body=body,
                schemas=[T.article_schema(title=row['title'],description=description,url=T.SITE+row['path'],published=published,modified=DATE,section=category,citations=[u for u,_ in references(n)]),T.breadcrumb_schema(trail)],published=published,modified=DATE)
        else:
            output=re.sub(re.escape(START)+'.*?'+re.escape(END),'',old,flags=re.S)
            assert '</main>' in output,(n,'Missing main boundary')
            output=output.replace('</main>',module(row)+'\n</main>',1)
            output=update_dates(output)
        output=normalize_cta(output).replace('—',', ').replace('&mdash;',', ')
        path.parent.mkdir(parents=True,exist_ok=True);path.write_text(output)
        added=T.strip_tags(module(row,full))
        manifest.append(dict(**row,action='new' if is_new else ('rewritten' if full else 'expanded'),
          editorial_words=len(added.split()),source_urls=[u for u,_ in references(n)],
          status='implemented',review_note='Hypothetical example replaces unsupported outcome claims' if n in CASE_EXTRA else 'Distinct decision, example and evidence checklist'))
    hub_body=T.page_header(h1='Tax Decisions for Business and Rental Owners',subtitle='Find practical guidance for the property, business or filing decision in front of you.',trail=[('Home','/'),('Owner tax decisions',HUB)],cta='Book a Call')
    hub_body+=T.section('Choose the decision you need to make',p('Explore cost segregation, rental operations, prior-year corrections, business planning and advisor selection. Each guide explains what records to prepare and what questions to resolve. Cost segregation is separately priced from advisory. Worked examples are hypothetical unless a page expressly identifies a documented result.'))
    for group_index,(group,hub) in enumerate(GROUPS):
        subset=rows[group_index*10:(group_index+1)*10]
        hub_body+=T.section(group,'<ul>'+''.join(f'<li><a href="{r["path"]}">{html.escape(r["title"])}</a></li>' for r in subset)+'</ul>')
    hub_output=T.build_page(title='Tax Decision Guides for Business & Rental Owners | AE Tax',description='Explore 100 practical tax decisions for business owners and rental investors: cost segregation, depreciation, corrections and advisor selection.',path=HUB,body=hub_body,schemas=[T.breadcrumb_schema([('Home','/'),('Owner tax decisions',HUB)])],published=DATE,modified=DATE)
    (ROOT/HUB.strip('/')).mkdir(parents=True,exist_ok=True)
    (ROOT/HUB.strip('/')/'index.html').write_text(normalize_cta(hub_output))
    # Add meaningful inbound links to both the collection and individual topics.
    for url in sorted({h for _,h in GROUPS}|{'/','/guides/'}):
        path=ROOT/url.strip('/')/'index.html'
        if not path.exists():continue
        text=path.read_text()
        text=re.sub(r'<!-- sprint-navigation:start -->.*?<!-- sprint-navigation:end -->','',text,flags=re.S)
        related=[(HUB,'Explore the owner tax decision library')]+[(r['path'],r['title']) for r in rows if GROUPS[(r['id']-1)//10][1]==url]
        block='<!-- sprint-navigation:start -->'+T.related_section(related,'Practical guides for your next decision')+'<!-- sprint-navigation:end -->'
        text=text.replace('</main>',block+'\n</main>',1)
        path.write_text(normalize_cta(text))
    # Keep cards and inbound labels consistent with the rewritten examples.
    cases={r['path']:r['title'] for r in rows if 91<=r['id']<=96}
    for page in ROOT.rglob('index.html'):
        if '.git' in page.parts: continue
        original=page.read_text(); text=original
        for url,title in cases.items():
            if url not in text: continue
            def card(m):
                value=m.group(0)
                if 'href="'+url+'"' not in value: return value
                value=re.sub(r'data-text="[^"]*"','data-text="'+html.escape(title,quote=True)+'"',value)
                value=re.sub(r'<p>.*?</p>',p('Hypothetical planning example: review eligibility, records and implementation. This is not a verified client outcome.'),value,flags=re.S)
                return value.replace('Read the Case Study','Read the Example')
            text=re.sub(r'<article\b[^>]*>.*?</article>',card,text,flags=re.S)
            pattern=r'(<a\b[^>]*href="'+re.escape(url)+r'"[^>]*>)(.*?)</a>'
            text=re.sub(pattern,lambda m:m.group(1)+(m.group(2) if re.sub('<[^>]+>','',m.group(2)).strip() in ('Read the Example','Read more','View example') else html.escape(title))+'</a>',text,flags=re.S)
        text=text.replace('Advisory relationship with cost seg included','Advisory relationship with cost segregation separately priced')
        if text!=original: page.write_text(text)
    from build_commercial_paths import main as restore_commercial_paths
    restore_commercial_paths()
    prior_path.write_text(json.dumps(manifest,indent=2)+'\n')
    buf=io.StringIO();writer=csv.DictWriter(buf,fieldnames=['id','title','url','action','status'],lineterminator='\n')
    writer.writeheader()
    for r in manifest:writer.writerow(dict(id=r['id'],title=r['title'],url=T.SITE+r['path'],action=r['action'],status=r['status']))
    (ROOT/'content_sprint_100_manifest.csv').write_text(buf.getvalue())
    print(json.dumps({a:sum(r['action']==a for r in manifest) for a in ('new','rewritten','expanded')}))
    print('Distinct editorial words:',sum(r['editorial_words'] for r in manifest))

if __name__=='__main__':main()
