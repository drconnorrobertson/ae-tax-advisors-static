import re,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
paths=['/services/','/resources/','/cost-segregation-for-warehouse/']
block='''<section class="content-section" id="tax-advisory-buying-guide"><div class="container narrow"><h2>Before You Hire a Tax Advisor</h2><p>Start with the decision you need help making, then compare the scope and complete cost. These guides give business owners and property investors practical questions, worksheets and worked examples.</p><ol><li><a href="/blog/why-7800-tax-advisory-saves-50k/">Decide whether tax advisory is worth the cost</a> — define the baseline and test a smaller-benefit case.</li><li><a href="/blog/how-much-should-you-pay-tax-advisory/">Choose a service scope and budget</a> — distinguish preparation, focused review and coordinated planning.</li><li><a href="/blog/how-to-evaluate-tax-advisor/">Evaluate the advisor</a> — compare credentials, relevant work and responsibility.</li><li><a href="/blog/comparing-tax-advisory-fees-apples-to-oranges/">Compare written proposals</a> — account for required extras and renewal terms.</li><li><a href="/blog/what-you-actually-get-with-ae-tax-advisors/">Confirm the AE engagement</a> — put deliverables, support and implementation owners in writing.</li></ol><p>Bring your entities, available records and decision date to <a href="/discovery/">a call with AE</a>. The written agreement determines your work and fees; these guides do not promise a tax result.</p></div></section>'''
for path in paths:
 f=ROOT/path.strip('/')/'index.html';s=f.read_text()
 if path!='/cost-segregation-for-warehouse/':
  assert 'id="tax-advisory-buying-guide"' not in s
  s=s.replace('</main>',block+'\n</main>',1)
 else:
  assert 'Why $7,800 in Tax Advisory Fees Saves $50K+ in Taxes' in s
  s=s.replace('Why $7,800 in Tax Advisory Fees Saves $50K+ in Taxes','Is Tax Advisory Worth the Cost for Your Situation?')
 if path!='/cost-segregation-for-warehouse/': s=re.sub(r'("dateModified"\s*:\s*")[^"]+("\s*[,}])',r'\g<1>2026-10-07\2',s)
 if path!='/cost-segregation-for-warehouse/': s=re.sub(r'(<meta property="article:modified_time" content=")[^"]+',r'\g<1>2026-10-07T00:00:00-04:00',s)
 f.write_text(s)
for f in ROOT.glob('sitemap*.xml'):
 s=f.read_text();original=s
 for path in paths[:2]:
  pat=r'<url>\s*<loc>'+re.escape('https://www.aetaxadvisors.com'+path)+r'</loc>[\s\S]*?</url>'
  s=re.sub(pat,lambda m:re.sub(r'<lastmod>[^<]*</lastmod>','<lastmod>2026-10-07</lastmod>',m.group()),s)
 if s!=original:f.write_text(s)
(ROOT/'_gen/ae-buyer-reading-path.json').write_text(json.dumps({'changedUrls':['https://www.aetaxadvisors.com'+p for p in paths],'purpose':'Connect service/resource discovery to five distinct hiring decisions; correct stale value-guide link label.'},indent=2)+'\n')
print('Added two reading paths and corrected one link label')
