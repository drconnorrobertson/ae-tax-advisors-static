"""Idempotently organize the public case library using only published profile facts."""
from pathlib import Path
import re,json,html
ROOT=Path(__file__).resolve().parents[1]
f=ROOT/'case-studies/index.html';s=f.read_text()
incomes={
's-corp-qbi-threshold-optimization':(425000,'Taxable income before planning'),
'four-llc-consolidation-management-company':(480000,'Combined net business income'),
'sole-prop-to-s-corp-contractor':(580000,'Net business profit'),
'husband-wife-three-businesses-joint-optimization':(780000,'Household income'),
'insurance-agency-commission-entity-optimization':(520000,'Owner income'),
'landscaping-contractor-section-179-stacking':(285000,'Owner income'),
'law-firm-partner-s-corp-cash-balance-plan':(980000,'Net income'),
'marketing-agency-home-office-augusta-rule-s-corp':(410000,'Owner income'),
'airbnb-arbitrage-operator-business-expense-optimization':(185000,'Net business income'),
'w2-couple-str-offset':(882000,'Combined W-2 income'),
'physician-w2-str-reps':(650000,'W-2 income'),
'physician-reps-qualification-cost-seg-combo':(860000,'Combined income'),
'professional-athlete-entity-setup-real-estate-offset':(3000000,'Contract and endorsement income'),
'tech-consulting-firm-ic-classification-accountable-plan':(620000,'Owner income'),
'private-medical-practice-c-corp-defined-benefit':(680000,'Average owner income'),
'medical-practice-c-corp-retirement-stacking':(680000,'Owner compensation'),
'fix-and-flip-dealer-vs-investor-classification':(420000,'Net flip income'),
'triple-net-lease-passive-income-grouping-elections':(480000,'Net rental income')}
owner_extra={'airbnb-arbitrage-operator-business-expense-optimization','auto-dealership-cost-seg-fleet-depreciation','hotel-boutique-investor-cost-seg-ffe-energy-credits','dental-practice-cost-seg-entity-restructuring','dental-practice-cost-seg-dso','fix-and-flip-dealer-vs-investor-classification','land-developer-installment-sale-like-kind-exchange','physician-reps-qualification-cost-seg-combo','professional-athlete-entity-setup-real-estate-offset','multi-entity-real-estate-operating','real-estate-agent-investment-portfolio','real-estate-broker-team-entity','restaurant-cost-seg-tip-credit','self-storage-facility-cost-seg-automation','veterinary-practice-cost-seg-section-179'}
nonowners={'w2-couple-str-offset','physician-w2-str-reps','w2-household-tax-planning-before-new-investments','triple-net-lease-passive-income-grouping-elections'}
labels={'under100':'Under $100k','100to250':'$100k–$250k','250to500':'$250k–$500k','500to1m':'$500k–$1M','1mplus':'$1M+','unknown':'Income not specified'}
profiles=[]
def card(m):
 c=m.group();slug=re.search(r'href="/case-studies/([^/]+)/',c)[1];cat=re.search(r'data-cat="([^"]+)"',c)[1]
 page=(ROOT/'case-studies'/slug/'index.html').read_text()
 main=page.split('<main',1)[-1].split('</main>',1)[0]
 text=html.unescape(re.sub('<[^>]+>',' ',main))
 owner='owner' if cat=='Business Owners' or slug in owner_extra else 'unspecified'
 if slug in nonowners or ('W-2' in text and 'Individual (W-2' in text):owner='nonowner'
 # A business and a property portfolio can appear in the same case.
 estate='yes' if cat!='Business Owners' or slug in {'owner-retirement-property-advisory-sequence','dental-practice-business-rental-tax-roadmap','trade-business-owner-rental-planning','multi-business-owner-property-entity-review','husband-wife-three-businesses-joint-optimization','franchise-owner-seven-locations-centralized-planning','mixed-use-developer-bonus-depreciation-opportunity-zone'} else 'no'
 if re.search(r'Property Studies|Rental Planning|Property Planning|Business and Rental',re.search(r'<h[23][^>]*>(.*?)</h[23]>',c,re.S)[1],re.I): estate='yes'
 income,basis=incomes.get(slug,(None,None))
 band='unknown' if income is None else 'under100' if income<100000 else '100to250' if income<250000 else '250to500' if income<500000 else '500to1m' if income<1000000 else '1mplus'
 title=html.unescape(re.sub('<[^>]+>','',re.search(r'<h[23][^>]*>(.*?)</h[23]>',c,re.S)[1]))
 profiles.append(dict(slug=slug,title=title,income=band,income_basis=basis,ownership=owner,real_estate=estate,source='/case-studies/'+slug+'/'))
 c=re.sub(r' data-(?:income|ownership|estate)="[^"]*"','',c)
 c=c.replace('<article ',f'<article data-income="{band}" data-ownership="{owner}" data-estate="{estate}" ',1)
 c=re.sub(r'<div class="cs-profile-tags">.*?</div>','',c,flags=re.S)
 ownlabel={'owner':'Business owner','nonowner':'No operating business shown','unspecified':'Ownership not specified'}[owner]
 tag=f'<div class="cs-profile-tags"><span>{labels[band]}</span><span>{ownlabel}</span><span>{"Real estate in this case" if estate=="yes" else "No real estate shown"}</span>'+(f'<small>{html.escape(basis)}</small>' if basis else '')+'</div>'
 return re.sub(r'(</h[23]>)',lambda m:m.group()+tag,c,count=1)
s=re.sub(r'<article class="cs-card"[^>]*>.*?</article>|<article data-income="[^"]*"[^>]*class="cs-card"[^>]*>.*?</article>',card,s,flags=re.S)
assert len(profiles)==103,len(profiles)
controls='''<div class="cs-profile-finder"><h2>Find a Case That Looks Like You</h2><p>Combine filters to match your income, business and property situation. Income means the published income or net profit figure, not business revenue or property value. Cases without a published figure remain available under “Income not specified.”</p><div class="cs-profile-fields">'''
for ident,label,opts in [('income','Annual income / net profit',[('all','Any income')]+list(labels.items())),('ownership','Business ownership',[('all','Any ownership profile'),('owner','Business owner'),('nonowner','Non-business owner / W-2'),('unspecified','Ownership not specified')]),('estate','Real estate',[('all','With or without real estate'),('yes','Real estate in the case'),('no','No real estate shown')])]:
 controls+=f'<label for="cs-{ident}">{label}<select id="cs-{ident}">'+''.join(f'<option value="{v}">{t}</option>' for v,t in opts)+'</select></label>'
controls+='''</div><p class="cs-profile-note">Ownership describes the operating business shown in the case. “No real estate shown” describes the story’s scope; it does not confirm a client has no property.</p><button type="button" id="cs-reset" class="cs-chip">Clear all filters</button></div>'''
if '<div class="cs-profile-finder">' in s:s=re.sub(r'<div class="cs-profile-finder">.*?</button></div>',lambda m:controls,s,flags=re.S)
else:s=s.replace('<div class="cs-filters"',controls+'\n<div class="cs-filters"',1)
css='<link rel="stylesheet" href="/assets/case-profile-filters.css?v=20261002">'
if css not in s:s=s.replace('</head>',css+'\n</head>')
s=re.sub(r'<script>\s*\(function\(\)\{\s*var grid = document.getElementById\(\'cs-grid\'\);.*?</script>','<script src="/assets/case-profile-filters.js?v=20261002" defer></script>',s,flags=re.S)
def schema(m):
 d=json.loads(m[1])
 if d.get('@type')=='CollectionPage':
  d['dateModified']='2026-10-01';d['mainEntity']={'@type':'ItemList','numberOfItems':len(profiles),'itemListElement':[{'@type':'ListItem','position':i+1,'name':p['title'],'url':'https://www.aetaxadvisors.com'+p['source']} for i,p in enumerate(profiles)]}
 if d.get('@type')=='ItemList' and d.get('name')=='Primary navigation':
  d['itemListElement']=[x for x in d['itemListElement'] if '/case-studies/' not in x.get('url','') or x.get('url','').endswith('/case-studies/')];d['numberOfItems']=len(d['itemListElement'])
 return '<script type="application/ld+json">'+json.dumps(d,ensure_ascii=False)+'</script>'
s=re.sub(r'<script type="application/ld\+json">(.*?)</script>',schema,s,flags=re.S)
s=s.replace('75 Tax Planning Results','103 Tax Planning Case Studies')
f.write_text(s)
(ROOT/'scripts/case-profile-metadata.json').write_text(json.dumps(profiles,indent=2)+'\n')
print('Tagged',len(profiles),'cases;',sum(p['income']!='unknown' for p in profiles),'published income figures')
