"""Search Console-informed snippets and homepage owner-content links."""
import html
import json
import re
from discovery_inventory import ROOT, BASE
from build_owner_decision_guides import POSTS

SNIPPETS = {
 'blog/macrs-depreciation-schedule-explained': ('MACRS Depreciation: Methods, Lives & Conventions | AE Tax', 'Understand MACRS recovery periods, depreciation methods and conventions for business equipment and rental property, with examples and planning limits.'),
 'blog/can-my-s-corp-pay-for-my-health-insurance': ('S-Corp Owner Health Insurance: W-2 Treatment | AE Tax', 'Learn how an S corporation handles health insurance for a more-than-2% owner, including W-2 reporting, reimbursement and deduction requirements.'),
 'blog/how-do-s-corp-distributions-work-and-are-they-taxed': ('S-Corp Distributions: Tax, Stock Basis & Salary | AE Tax', 'See when S-corp distributions are taxable, why stock basis matters, and how owner distributions differ from wages and shareholder loan repayments.'),
 'blog/what-is-a-disregarded-entity-and-how-is-it-taxed': ('Disregarded LLC: Business & Rental Tax Reporting | AE Tax', 'Understand how a single-member LLC reports business or rental income, why disregarded status matters, and which separate tax obligations can remain.'),
 'blog/section-1245-vs-1250-depreciation-recapture': ('Section 1245 vs. 1250: Depreciation Recapture | AE Tax', 'Compare depreciation recapture on business equipment and real estate, including why cost segregation affects the tax analysis when property is sold.'),
 'business-owner-tax-planning': ('Business Owner Tax Planning & Entity Strategy | AE Tax', 'Coordinate entity structure, owner compensation, retirement contributions and depreciation in a year-round tax plan for your operating business.'),
 'cost-segregation-calculator': ('Cost Segregation Calculator: Test Your Tax Benefit | AE Tax', 'Estimate additional first-year depreciation and usable federal tax benefit. Adjust land, asset allocation, recovery period, loss usability and study fee.'),
}

def main():
    for slug,(title,description) in SNIPPETS.items():
        p=ROOT/slug/'index.html';s=p.read_text()
        s=re.sub(r'<title>.*?</title>','<title>'+html.escape(title)+'</title>',s,count=1,flags=re.S)
        for attr,key,value in [('name','description',description),('property','og:title',title),('property','og:description',description),('name','twitter:title',title),('name','twitter:description',description)]:
            pattern=r'<meta '+attr+'="'+key+r'" content="[^"]*"\s*/?>'
            replacement='<meta '+attr+'="'+key+'" content="'+html.escape(value,quote=True)+'">'
            s=re.sub(pattern,replacement,s)
        def schema(m):
            data=json.loads(m.group(1));changed=False
            def walk(x):
                nonlocal changed
                if isinstance(x,dict):
                    if x.get('@type') in ('Article','BlogPosting','WebPage') and (x.get('url',BASE+'/'+slug+'/')==BASE+'/'+slug+'/'):
                        x['description']=description;changed=True
                        if slug=='cost-segregation-calculator':x['dateModified']='2026-09-26'
                    for v in x.values():walk(v)
                elif isinstance(x,list):
                    for v in x:walk(v)
            walk(data)
            return '<script type="application/ld+json">\n'+json.dumps(data,ensure_ascii=False,indent=2)+'\n</script>' if changed else m.group(0)
        s=re.sub(r'<script type="application/ld\+json">(.*?)</script>',schema,s,flags=re.S)
        if slug=='cost-segregation-calculator':
            s=s.replace('href="/cost-segregation-calculator/"','href="#estimate"')
            s=s.replace('<a href="/cost-segregation-airbnb/">Cost Segregation</a>','<a href="/cost-segregation-study/">Cost Segregation</a>')
        p.write_text(s)
    p=ROOT/'index.html';s=p.read_text()
    cards='\n'.join('<a href="/blog/'+post['slug']+'/" class="blog-card"><div class="blog-card-category">'+html.escape(post['category'])+'</div><h3>'+html.escape(post['title'])+'</h3><p>'+html.escape(post['description'])+'</p><span class="card-link">Read the guide &rarr;</span></a>' for post in (POSTS[2],POSTS[3],POSTS[4]))
    s=re.sub(r'(<section class="blog-preview fade-in-section">.*?<div class="card-grid-3">).*?(</div>\s*<div class="center-cta">)',lambda m:m.group(1)+cards+m.group(2),s,count=1,flags=re.S)
    s=s.replace('Expert strategies to optimize your tax situation','New decision guides for business owners and real estate owners')
    p.write_text(s)
    print('Optimized',len(SNIPPETS),'search snippets and 3 homepage article links')

if __name__=='__main__':main()
