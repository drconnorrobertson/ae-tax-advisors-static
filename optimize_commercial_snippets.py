"""Keep buyer-intent snippets explicit and free of unsupported savings promises."""
import html,re
from discovery_inventory import ROOT
SNIPPETS={
'blog/how-much-does-a-cost-segregation-study-cost':('How Much Does a Cost Segregation Study Cost? Fees & Scope','Compare cost segregation study fees, report scope and implementation costs. AE lists $1 per square foot with a $2,000 minimum; confirm your written quote.'),
'cost-segregation-airbnb':('Airbnb & Short-Term Rental Cost Segregation | AE Tax','Review cost segregation for your Airbnb or short-term rental, including property basis, participation records, study scope and usable tax benefit.'),
'cost-segregation-for-multifamily':('Multifamily Cost Segregation Studies | AE Tax Advisors','Evaluate a cost segregation study for your apartment building or multifamily portfolio. Review asset allocations, study scope and tax implementation.'),
'cost-segregation-for-warehouse':('Warehouse Cost Segregation Studies | AE Tax Advisors','Warehouse owners: evaluate building components, land improvements and depreciation with a property-specific cost segregation review. See study scope and fees.'),
'cost-segregation-for-self-storage':('Self-Storage Cost Segregation Studies | AE Tax Advisors','Review cost segregation for a self-storage facility, including building systems, site improvements, depreciation and the study implementation process.'),
'cost-segregation-for-medical-office':('Medical Office Cost Segregation Studies | AE Tax','Own a medical office building? Review cost segregation for specialized systems, property improvements and supported depreciation classifications.'),
'cost-segregation-for-dental-office':('Dental Office Cost Segregation Studies | AE Tax Advisors','Dental practice and property owners: coordinate building cost segregation with equipment, tenant improvements and tax-return implementation.'),
'cost-segregation-owner-occupied-commercial':('Owner-Occupied Commercial Cost Segregation | AE Tax','Own the building used by your business? Evaluate cost segregation, ownership structure, depreciation and implementation costs before ordering a study.'),
'cost-segregation-study-timeline-process':('Cost Segregation Study Timeline & Process | AE Tax','Understand the steps from property records to a completed cost segregation report, including review dependencies, delivery and tax-return coordination.'),
'cost-segregation-documents-checklist':('Cost Segregation Documents Checklist | AE Tax Advisors','Prepare closing records, land support, improvement invoices and depreciation schedules for a cost segregation study. See what to gather before requesting a quote.'),
'form-3115-cost-segregation':('Form 3115 for Cost Segregation & Lookback Studies | AE Tax','Review catch-up depreciation and Form 3115 for an existing property. Understand prior schedules, method-change eligibility and filing coordination.'),
'best-tax-advisor-for-business-owners':('Choosing a Tax Advisor for Business Owners | AE Tax','Compare business tax advisors by planning scope, implementation support, fee clarity and coordination with your CPA. Questions to ask before an engagement.'),
'best-cpa-for-real-estate-investors':('Choosing a CPA for Real Estate Investors | AE Tax','Compare tax support for your rental or commercial portfolio: depreciation, multi-entity work, transaction planning, return scope and fees.')}
def main():
 for slug,(title,desc) in SNIPPETS.items():
  p=ROOT/slug/'index.html';s=p.read_text()
  s=re.sub(r'<title>.*?</title>',lambda m:'<title>'+html.escape(title)+'</title>',s,count=1,flags=re.S)
  for attr,key,value in [('name','description',desc),('property','og:title',title),('property','og:description',desc),('name','twitter:title',title),('name','twitter:description',desc)]:
   s=re.sub(r'<meta '+attr+'="'+key+'" content="[^"]*"\s*/?>',lambda m:'<meta '+attr+'="'+key+'" content="'+html.escape(value,quote=True)+'">',s)
  if slug.startswith('blog/how-much'):
   marker='<!-- ae-study-fee -->'
   block=marker+'<aside style="padding:24px;border:1px solid #d5dce3;border-radius:8px;margin:24px 0;"><h2>AE Tax Advisors study pricing</h2><p>Published standard pricing is <strong>$1 per square foot, with a $2,000 minimum per study</strong>. Cost segregation is separate from advisory. Confirm the property scope, Form 3115 preparation, return implementation and support in your written quote.</p><p><a href="/cost-segregation-study-cost-pricing/">See AE pricing examples and the proposal checklist</a> or <a href="/cost-segregation-study/">review the study service</a>.</p></aside><!-- /ae-study-fee -->'
   s=re.sub(re.escape(marker)+'.*?<!-- /ae-study-fee -->','',s,flags=re.S)
   anchor='<h2>What a Cost Segregation Quote Should Include</h2>'
   assert anchor in s
   s=s.replace(anchor,block+anchor,1)
   s=s.replace('Most business owners and investors overpay their taxes by tens of thousands of dollars every year. Our team identifies the strategies your current CPA is missing.','Review your property records, study scope and implementation needs with the team before deciding whether a study is worthwhile.')
  p.write_text(s)
 print('Updated',len(SNIPPETS),'commercial search snippets')
if __name__=='__main__':main()
