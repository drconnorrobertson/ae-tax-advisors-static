"""Rebuild 100 retained owner FAQs from individually written editorial records.

This is an explicit editorial migration, not a deployment-time generator.
It preserves canonical URLs, original publication dates, navigation and booking.
"""
import html
import json
import re
import runpy
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'content/long-tail-refresh-20261104'
DATE = '2026-11-04'
SITE = 'https://www.aetaxadvisors.com'
E = html.escape
GROUPS = runpy.run_path(str(ROOT / 'scripts/owner_faq_articles.py'))['GROUPS']
P = 'https://www.irs.gov/publications/'
I = 'https://www.irs.gov/instructions/'
B = 'https://www.irs.gov/businesses/small-businesses-self-employed/'
R = 'https://www.irs.gov/retirement-plans/'
CONFIG = {
 'S-Corp Planning': ('/services/reasonable-compensation/', 'S corporation compensation services', [(B+'s-corporation-compensation-and-medical-insurance-issues', 'IRS: S corporation compensation and health insurance'),(P+'p560', 'IRS Publication 560: retirement plan rules')], 'Bring the owner duty summary, payroll register and shareholder payment detail to a compensation review.'),
 'Tax Compliance': ('/services/quarterly-estimates/', 'Estimated-tax planning and payment review', [(P+'p505', 'IRS Publication 505: withholding and estimated tax'),(P+'p544', 'IRS Publication 544: asset dispositions')], 'Bring the current household projection, payment confirmations and latest payroll records to an estimated-tax review.'),
 'Business Deductions': ('/business-owner-small-business-tax/', 'Business owner tax advisory', [(P+'p463', 'IRS Publication 463: travel, vehicles and accountable arrangements'),(P+'p527', 'IRS Publication 527: rental property expenses')], 'Bring the expense report, itemized support and reimbursement history to an owner-expense review.'),
 'Retirement Planning': ('/retirement-exit-ma-tax-strategy/', 'Business owner retirement planning', [(P+'p560','IRS Publication 560: small-business retirement plans'),(R+'one-participant-401k-plans','IRS: one-participant 401(k) plans'),(R+'retirement-plan-faqs-regarding-contributions-s-corporation','IRS: S corporation retirement contributions')], 'Bring the employee census, ownership list, current plan documents and contribution history to a retirement-plan review.'),
 'Entity Structuring': ('/business-owner-small-business-tax/', 'Business owner entity and return coordination', [(I+'i7203','IRS Form 7203 instructions: stock and debt basis'),(P+'p925','IRS Publication 925: passive-activity and at-risk rules')], 'Bring the prior basis schedule, K-1s and dated shareholder transactions to an entity and owner-return review.'),
 'Rental Property': ('/rental-property-tax-planning/', 'Rental property tax planning', [(P+'p527','IRS Publication 527: rental income, costs and use'),(P+'p946','IRS Publication 946: depreciation'),(B+'tangible-property-final-regulations','IRS: tangible property improvement rules')], 'Bring the property ledger, lease or platform statements and asset records to a rental tax review.'),
 'Material Participation': ('/short-term-rental-tax-strategy/', 'Short-term rental tax planning', [(P+'p925','IRS Publication 925: activity classification and participation'),(P+'p527','IRS Publication 527: rental property and personal use')], 'Bring the reservation history, owner and spouse work records, manager duties and prior elections to an STR participation review.'),
 'Cost Segregation': ('/cost-segregation-study/', 'Cost segregation study and implementation scope', [(P+'p946','IRS Publication 946: depreciation and bonus eligibility'),(P+'p925','IRS Publication 925: loss limitations'),('https://www.irs.gov/pub/irs-pdf/p5653.pdf','IRS cost segregation audit technique guide: study methodology')], 'Bring closing records, land support, improvements and existing depreciation schedules to a property-specific study review.'),
 '1031 Exchanges': ('/real-estate-tax-planning/', 'Real estate tax planning before a transaction', [(P+'p544','IRS Publication 544: gain, basis and like-kind exchanges'),(P+'p527','IRS Publication 527: rental asset records')], 'Bring the proposed sale terms, asset history, ownership structure and intermediary documents before committing to the closing arrangement.'),
 'Tax Return Mistakes': ('/form-3115-cost-segregation/', 'Missed depreciation and Form 3115 planning', [(I+'i3115','IRS Form 3115 instructions: accounting method changes'),(P+'p946','IRS Publication 946: depreciation corrections'),(P+'p925','IRS Publication 925: deduction limitations')], 'Bring filed returns, detailed asset schedules, elections and disposition dates to a depreciation-correction review.')
}

def slug(title):
 return 'owner-faq-' + re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

def section(heading, body, ident):
 return f'<section class="content-section fade-in-section" id="{ident}"><div class="container narrow"><h2>{E(heading)}</h2>{body}</div></section>\n'

def para(s):
 return '<p>'+E(s)+'</p>'

class Text(HTMLParser):
 def __init__(self): super().__init__(); self.parts=[]
 def handle_data(self, text): self.parts.append(text)

def plain(s):
 p=Text();p.feed(s);return ' '.join(' '.join(p.parts).split())

def records():
 groups={};g=None
 for line in (DATA/'editorial.txt').read_text().splitlines():
  if not line:continue
  if line.startswith('['):g=line[1:-1];groups[g]=[];continue
  bits=line.split('|');assert len(bits)==7
  groups[g].append(dict(zip(['seo_title','heading','analysis','example','steps','faq_q','faq_a'],bits)))
 result=[]
 for g,_,_,rows in GROUPS:
  assert len(groups[g])==len(rows)==10
  for original,extra in zip(rows,groups[g]):
   title,answer,example=original
   result.append(dict(extra,group=g,title=title,answer=answer,original_example=example,path='/blog/'+slug(title)+'/'))
 assert len(result)==100
 return result

def apply():
 rows=records();manifest=[]
 holds=json.loads((ROOT/'discovery_review_holds.json').read_text())
 redirects={x['source'] for x in json.loads((ROOT/'vercel.json').read_text())['redirects']}
 for n,r in enumerate(rows):
  route=r['path'];p=ROOT/route.strip('/')/'index.html';s=p.read_text()
  assert route not in holds and route not in redirects,route
  assert SITE+route in s
  service,label,sources,cta=CONFIG[r['group']]
  first=r['analysis'].split('. ')[0]+'.'
  description=first if 75<=len(first)<=180 else r['faq_a']
  # Complete editorial sentences rather than clipped snippets.
  if len(description)>185:description=r['seo_title']+'. Read the decision factors, worked examples and preparation checklist.'
  title=r['seo_title']+' | AE Tax Advisors'
  steps=r['steps'].split(';');assert len(steps)==3
  # Three related retained articles, including one cross-cluster decision.
  base=(n//10)*10;i=n%10
  cross={0:30,1:8,2:50,3:7,4:90,5:70,6:72,7:95,8:78,9:79}[n//10]
  related=[rows[base+(i+1)%10],rows[base+(i+3)%10],rows[cross]]
  assert len({x['path'] for x in related})==3
  body='<!-- long-tail-refresh:20261104:start -->\n'
  body+=section('The direct answer',para(r['answer'])+f'<p class="article-meta">By <a href="/about/">AE Tax Advisors Team</a>. Updated November 4, 2026.</p>', 'direct-answer')
  body+=section(r['heading'],para(r['analysis']), 'decision-factors')
  body+=section('Work through the example', '<p><strong>Hypothetical illustration, not a client result.</strong></p>'+para(r['example'])+'<h3>Another situation to compare</h3>'+para(r['original_example']), 'worked-example')
  body+=section('Prepare your review file','<ol>'+''.join('<li>'+E(x)+'.</li>' for x in steps)+'</ol><p>For each item, note the supporting document, its date and any unresolved question. Keep the completed review with the relevant tax-year records.</p>', 'preparation-checklist')
  body+=section('A related question','<h3>'+E(r['faq_q'])+'</h3>'+para(r['faq_a']), 'related-question')
  source_html='<ul>'+''.join('<li><a href="'+E(u,quote=True)+'">'+E(l)+'</a></li>' for u,l in sources)+'</ul>'
  source_html+='<p>References checked November 4, 2026. Use the instructions and later guidance applicable to the return year. IRS publications explain general rules; the cost segregation audit technique guide describes examination methodology and is not binding legal authority. Examples omit facts that can change an individual result.</p>' if r['group']=='Cost Segregation' else '<p>References checked November 4, 2026. Use the instructions and later guidance applicable to the return year. This article provides general education; the relevant entity, tax year, elections and state rules can change the result.</p>'
  body+=section('Primary sources and scope',source_html+'<p><a href="/editorial-policy/">Read our editorial and source standards</a>.</p>', 'primary-sources')
  body+=section('Continue with the next decision','<ul>'+''.join('<li><a href="'+x['path']+'">'+E(x['title'])+'</a></li>' for x in related)+'</ul><p><a href="'+service+'">'+E(label)+'</a></p>', 'related-reading')
  body+=section('Discuss the records behind your decision',para(cta)+'<p>Confirm the review scope, responsible preparer and any separately priced work in the written engagement.</p><p><a href="/discovery/" class="btn-cta">Discuss My '+('Property' if n>=50 else 'Business')+' Tax Questions</a></p>', 'next-step')
  body+='<!-- long-tail-refresh:20261104:end -->\n'
  # Keep the page header, navigation and footer exactly as authored.
  start=s.index('</section>',s.index('<main'))+len('</section>')
  end=s.index('</main>',start)
  s=s[:start]+body+'    '+s[end:]
  s=re.sub(r'(<p class="subtitle">).*?(</p>)',lambda m:m[1]+E(r['seo_title'])+'. Examples, decision factors and records to prepare.'+m[2],s,count=1,flags=re.S)
  s=re.sub(r'<title>.*?</title>','<title>'+E(title)+'</title>',s,count=1,flags=re.S)
  for attr,key,val in [('name','description',description),('property','og:title',title),('property','og:description',description),('name','twitter:title',title),('name','twitter:description',description),('property','article:modified_time',DATE+'T12:00:00-05:00')]:
   pattern=r'(<meta\s+'+attr+r'="'+re.escape(key)+r'"\s+content=")[^"]*(")'
   s,count=re.subn(pattern,lambda m:m[1]+E(val,quote=True)+m[2],s);assert count==1,(route,key,count)
  wc=len(plain(body).split())
  def schema(m):
   obj=json.loads(m[1]);typ=obj.get('@type')
   if typ in ('BlogPosting','Article'):
    obj.update(headline=r['title'],description=description,dateModified=DATE,wordCount=wc,citation=[u for u,_ in sources])
   if typ=='FAQPage':obj['mainEntity']=[{'@type':'Question','name':r['faq_q'],'acceptedAnswer':{'@type':'Answer','text':r['faq_a']}}]
   return '<script type="application/ld+json">'+json.dumps(obj,ensure_ascii=False,indent=2)+'</script>'
  s=re.sub(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',schema,s,flags=re.S)
  p.write_text(s)
  manifest.append(dict(path=route,group=r['group'],title=r['title'],seo_title=r['seo_title'],description=description,article_words=wc,related=[x['path'] for x in related],service=service,sources=[u for u,_ in sources]))
 # Refresh lastmod only for the 100 genuinely changed URLs, without a new sitemap.
 urls={SITE+r['path'] for r in rows};changed_maps=[]
 for p in ROOT.glob('sitemap*.xml'):
  s=p.read_text();original=s
  def entry(m):
   t=m[0];loc=re.search(r'<loc>(.*?)</loc>',t)
   if loc and html.unescape(loc[1]) in urls:
    if '<lastmod>' in t:t=re.sub(r'<lastmod>.*?</lastmod>','<lastmod>'+DATE+'</lastmod>',t)
    else:t=t.replace('</url>','<lastmod>'+DATE+'</lastmod></url>')
   return t
  s=re.sub(r'<url>.*?</url>',entry,s,flags=re.S)
  if s!=original:p.write_text(s);changed_maps.append(p.name)
 (DATA/'manifest.json').write_text(json.dumps({'date':DATE,'pages_modified':100,'sitemaps_modified':changed_maps,'pages':manifest},indent=2)+'\n')
 print(json.dumps({'pages_modified':len(manifest),'article_words':sum(r['article_words'] for r in manifest),'minimum_article_words':min(r['article_words'] for r in manifest),'sitemaps_modified':changed_maps}))

if __name__=='__main__':apply()
