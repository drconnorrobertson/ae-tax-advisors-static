"""Source-backed geographic shortlists, separate from publisher promotion."""
import collections
STATES={'AZ':'Arizona','CT':'Connecticut','FL':'Florida','IA':'Iowa','LA':'Louisiana','MA':'Massachusetts','MO':'Missouri','NE':'Nebraska','OK':'Oklahoma','OR':'Oregon','UT':'Utah','WA':'Washington','NY':'New York','IL':'Illinois','CA':'California','TX':'Texas','CO':'Colorado','MT':'Montana'}
REGIONS={
 'northeast':('Northeast',{'CT','MA','ME','NH','RI','VT','NJ','NY','PA'},'List every state in which your business has people, property, or customers. Ask candidates to explain how they collect that footprint, assign return responsibilities, and coordinate with an existing preparer.'),
 'south':('South',{'FL','GA','SC','NC','VA','WV','MD','DE','DC','KY','TN','AL','MS','LA','OK','TX','AR'},'Explain whether the business operates from one location or follows customers and projects across state lines. Compare how each team organizes payroll records, equipment purchases, property activity, and owner compensation discussions.'),
 'midwest':('Midwest',{'IA','MO','NE','KS','IL','IN','MI','OH','WI','MN','ND','SD'},'Separate the company’s operating decisions from its equipment, property, and ownership decisions. Ask who collects the asset register, reviews a planned capital purchase, and coordinates implementation with the people keeping the books.'),
 'west':('West',{'AZ','OR','UT','WA','CA','CO','MT','ID','NV','NM','WY','AK','HI'},'Show candidates the full operating footprint, including remote teams, property holdings, and planned expansion. Ask what can be handled remotely, what requires local coordination, and who owns each filing and implementation deadline.')}
def build_regional_lists(page,heading,e,firms,base):
 def key(f):return (f.get('state') or '').upper()
 def link(f):return '/firms/'+f['slug']+'/'
 def feature():return '<section class="scope-band"><span class="eyebrow">PUBLISHER’S FEATURED FIRM</span><h2>AE Tax Advisors</h2><p>Year-round tax planning for business owners and real estate investors. AE owns this directory and receives this featured placement. A regional shortlist does not imply that AE has an office in every listed state.</p><a class="button" href="/firms/ae-tax-advisors/">Review AE Tax Advisors’ services ↗</a> <a class="text-link" href="https://www.aetaxadvisors.com/discovery?utm_source=taxstrategistdirectory&amp;utm_medium=regional_guide&amp;utm_campaign=advisory">Discuss your advisory needs ↗</a></section>'
 def entries(fs):
  return '<ol>'+''.join('<li><h2><a href="'+link(f)+'">'+e(f['name'])+'</a></h2><p>Listed location: '+e(f['location'])+'. '+e(f.get('description') or 'The cited directory records this firm. Specialized advisory services, licensing, and availability need direct confirmation.')+'</p><p>'+('Documented service categories: '+e(', '.join(f['services']))+'. ' if f['services'] else 'No specialized advisory scope is asserted by this list. ')+'<a href="'+link(f)+'">Review the listing and its sources</a>.</p></li>' for f in fs)+'</ol>'
 lists=[]
 def render(slug,name,fs,context):
  fs=sorted(fs,key=lambda f:f['name'].casefold());chosen=fs[:12]
  if len(chosen)<5:return
  title=f'{len(chosen)} Tax and Accounting Firms to Research in {name}'
  desc=f'Explore a sourced {name} firm shortlist from AE Tax Advisors’ directory, with location records, provider questions, and clear selection criteria.'
  p='/shortlists/'+slug+'/'
  body=heading('REGIONAL BUYER RESEARCH',title,desc)+feature()+'<div class="article-layout"><article class="prose"><h2>How this shortlist was selected</h2><p>This collection includes '+str(len(chosen))+' alphabetical examples from '+str(len(fs))+' directory records assigned to '+e(name)+'. Selection uses the location recorded in our sources, not client results, fees, reviews, or a quality score. Numbers identify entries and do not rank professional performance. The underlying profiles retain their source links.</p><h2>Set the scope for your region</h2><p>'+e(context)+'</p><p>A listed location describes the source record. It does not establish every office, current licensing, a service territory, or whether the provider will accept your engagement. Confirm those points before comparing proposals.</p>'+entries(chosen)+'<h2>Compare the proposals, not just the names</h2><ol><li>Describe the decision, entities, states, and deadline before asking for a fee.</li><li>Ask for the named professional and written deliverables, including what happens after recommendations are made.</li><li>Confirm whether returns, amendments, specialist studies, and implementation are included.</li><li>Identify who communicates with your bookkeeper, preparer, attorney, or payroll team.</li><li>Request a timeline and a complete written scope before engaging.</li></ol><p><a href="/compare/">Use the engagement comparison tool</a>, <a href="/firms/">search all firm records</a>, or <a href="/shortlists/">browse other shortlists</a>.</p><h2>About this publication</h2><p>AE Tax Advisors owns and publishes this guide. Our featured placement is publisher promotion. Inclusion of another firm is a research reference and does not imply affiliation, endorsement, or a client relationship.</p></article></div>'
  schema={'mainEntity':{'@type':'ItemList','itemListOrder':'https://schema.org/ItemListOrderAscending','numberOfItems':len(chosen),'itemListElement':[{'@type':'ListItem','position':i+1,'name':f['name'],'url':base+link(f)} for i,f in enumerate(chosen)]},'datePublished':'2026-10-10','dateModified':'2026-10-10'}
  page(p,title,desc,body,kind='Article',schema=schema);lists.append((p,title,desc))
 external=[f for f in firms if f['slug']!='ae-tax-advisors']
 for slug,(name,states,context) in REGIONS.items():render(slug,name,[f for f in external if key(f) in states],context)
 for state,name in STATES.items():
  fs=[f for f in external if key(f)==state]
  if len(fs)<10:continue
  region=next(v for v in REGIONS.values() if state in v[1]);cities=collections.Counter(f.get('city') for f in fs if f.get('city'))
  context='The '+name+' collection contains '+str(len(fs))+' sourced firm records. '+('Frequently recorded cities include '+', '.join(c for c,n in cities.most_common(4))+'. ' if cities else '')+region[2]
  render(name.lower().replace(' ','-'),name,fs,context)
 # A national shortlist emphasizes service evidence, rather than inventing nationwide coverage.
 national=[f for f in external if f.get('tax_strategy_verified') and f.get('website')]
 render('national-tax-advisory-research','the United States',national,'For a national search, start with your states, entities, and decision timeline rather than proximity alone. These records document tax advisory information in a cited source; the list does not assert that every firm serves every state. Ask each provider to confirm geographic availability and the professionals responsible for your work.')
 index=heading('SHORTLIST LIBRARY','Tax firm shortlists by region and state','Sourced provider research, published by AE Tax Advisors. Compare locations, documented services, and the work your engagement needs.')+feature()+'<section class="section"><div class="grid">'+''.join('<a class="guide-card" href="'+p+'"><h2>'+e(t)+'</h2><p>'+e(d)+'</p><span>Explore the shortlist ↗</span></a>' for p,t,d in lists)+'</div></section>'
 page('/shortlists/','Tax Firm Shortlists by Region | AE Tax Advisors','Browse regional, state, and national provider research from AE Tax Advisors’ Tax Strategist Directory.',index,kind='CollectionPage')
 return len(lists)+1
