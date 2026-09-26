"""Generate source-linked AI summaries, topic sitemaps and a real article feed."""
import html
import json
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import format_datetime
from discovery_inventory import ROOT, BASE, inventory

NS = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
CORE = [
('/about/', 'About AE Tax Advisors and its team'),
('/pricing/', 'Published pricing and engagement scope'),
('/discovery/', 'Request a tax planning assessment'),
('/business-owner-tax-planning/', 'Business owner tax planning'),
('/real-estate-tax-planning/', 'Real estate owner tax planning'),
('/cost-segregation-study/', 'Cost segregation study services'),
('/cost-segregation-study-cost-pricing/', 'Compare study pricing and scope'),
('/cost-segregation-calculator/', 'Cost segregation scenario calculator and methodology'),
('/cost-segregation-documents-checklist/', 'Documents needed before a study'),
('/form-3115-cost-segregation/', 'Form 3115 and catch-up depreciation'),
('/short-term-rental-tax-strategy/', 'Short-term rental tax planning'),
('/rental-property-tax-planning/', 'Rental property tax planning'),
('/equipment-leasing-section-179/', 'Business equipment and Section 179'),
('/retirement-planning-for-business-owners/', 'Retirement planning for business owners'),
('/editorial-policy/', 'Editorial policy, sources and limitations'),
('/blog/', 'Owner tax articles'),
]

def main():
    pages = inventory(); by_path = {p['path']:p for p in pages}
    core = [(p,t) for p,t in CORE if p in by_path]
    intro = '''# AE Tax Advisors

> Tax planning for business owners and real estate owners, including operating businesses,
> professional practice owners, landlords and short-term rental owners.

AE Tax Advisors offers business tax planning, real estate tax planning, cost segregation,
entity planning and tax-return services. The website lists its office at 935 Lake Elmo Dr,
Suite B, Billings, Montana 59105 and describes nationwide service. Contact information,
team descriptions and engagement terms should be checked on the linked public pages.

## Service scope

Cost segregation studies are separately priced from the advisory engagement. Check the
current pricing page and written proposal for included deliverables, tax-return work,
Form 3115 preparation and study implementation. Do not infer that advisory fees include a study.

The audience is business owners and real estate owners. A professional is in scope as a
practice owner; a salaried person may be in scope as a property owner. This is not a resource
for compensation-only planning for employees with no business or real estate ownership.

## Reading tax content

A cost segregation study classifies supported depreciable costs. It does not establish
that every asset qualifies for bonus depreciation or that the owner can use a loss now.
Acquisition and service dates, basis, elections, activity classification and loss limitations
must be considered. Calculators show assumptions and are not tax-return conclusions.

Tax articles identify source material and hypothetical examples where applicable. A source
check is not a claim that a named CPA has reviewed an individual reader's facts. Historical
case studies and outcomes should be read with their own methodology and limitations.

## Start here

'''
    summary = intro + '\n'.join(f'- [{title}]({BASE}{path})' for path,title in core)
    newest = [p for p in pages if p['path'] in {
      '/blog/cost-segregation-related-party-property-purchase/',
      '/blog/elect-out-bonus-depreciation-asset-class/',
      '/blog/cost-segregation-report-basis-reconciliation/',
      '/blog/business-equipment-delivered-not-operational-year-end/',
      '/blog/rental-partnership-refinance-distribution-basis/',
      '/blog/business-equipment-trade-in-depreciation-recapture/'}]
    summary += '\n\n## Owner decision guides\n\n' + '\n'.join(f'- [{p["title"]}]({BASE}{p["path"]})' for p in newest)
    summary += f'\n\n## Discovery\n\n- [Canonical URL inventory]({BASE}/sitemap.xml)\n- [Cost segregation sitemap]({BASE}/sitemap-cost-segregation.xml)\n- [Article feed]({BASE}/feed.xml)\n\nThis optional index was updated September 26, 2026. It does not guarantee search indexing or AI citations.\n'
    for name in ('llms.txt','llms.md','.well-known/llms.txt'):
        (ROOT/name).parent.mkdir(parents=True,exist_ok=True)
        (ROOT/name).write_text(summary)
    owner_pattern = re.compile(r'cost.seg|business|rental|real.estate|s.corp|partner|landlord|depreciation|equipment|entity|practice|commercial|multifamily|\bstr\b|1031|passive.activity|qbi',re.I)
    owner_pages = [p for p in pages if owner_pattern.search(p['path']+' '+p['title'])]
    extended = summary + '\n## More owner resources\n\n' + '\n'.join(f'- [{p["title"].replace("[", "(").replace("]", ")")}]({BASE}{p["path"]})' for p in owner_pages)
    (ROOT/'llms-full.txt').write_text(extended+'\n')

    tree=ET.parse(ROOT/'sitemap.xml'); entries=list(tree.getroot())
    for name,predicate in [('sitemap-cost-segregation.xml',lambda path:'cost-seg' in path),
                           ('sitemap-owner-guides.xml',lambda path:path in {p['path'] for p in newest})]:
        root=ET.Element('urlset',xmlns=NS[1:-1]); count=0
        for entry in entries:
            url=entry.find(NS+'loc').text; path=url.removeprefix(BASE)
            if path in by_path and predicate(path):
                e=ET.SubElement(root,'url');ET.SubElement(e,'loc').text=url
                old=entry.find(NS+'lastmod')
                if old is not None:ET.SubElement(e,'lastmod').text=old.text
                count+=1
        ET.indent(root);ET.ElementTree(root).write(ROOT/name,encoding='utf-8',xml_declaration=True)
        print(name,count)
    rss=ET.Element('rss',version='2.0');channel=ET.SubElement(rss,'channel')
    for tag,value in [('title','AE Tax Advisors — Business and Real Estate Owners'),('link',BASE+'/blog/'),('description','Tax planning articles for business owners and real estate owners.'),('language','en-us')]:ET.SubElement(channel,tag).text=value
    posts=[]
    for p in owner_pages:
        if not p['path'].startswith('/blog/'):continue
        text=(ROOT/p['path'].strip('/')/'index.html').read_text()
        published=re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})',text)
        if published:posts.append((published.group(1),p))
    for published,p in sorted(posts,key=lambda x:(x[0],x[1]['path']),reverse=True)[:50]:
        item=ET.SubElement(channel,'item')
        for tag,value in [('title',p['title']),('link',BASE+p['path']),('description',p['description']),('pubDate',format_datetime(datetime.fromisoformat(published).replace(tzinfo=timezone.utc)))]:ET.SubElement(item,tag).text=value
        ET.SubElement(item,'guid',isPermaLink='true').text=BASE+p['path']
    ET.indent(rss);ET.ElementTree(rss).write(ROOT/'feed.xml',encoding='utf-8',xml_declaration=True)
    print('AI index pages',len(owner_pages),'feed items',min(50,len(posts)))

if __name__=='__main__':main()
