"""Add navigation and discovery for the owner-approved comparison release."""
from pathlib import Path
import sys,json,re,html
import xml.etree.ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import build_approved_comparison_pages as C
import site_template as T
ROOT=T.ROOT
PREFERRED='/compare/p4-tax-alternatives/'
OLD='/compare/p4-tax-and-consulting-alternatives/'

def main():
 C.build()
 p=ROOT/'vercel.json';config=json.loads(p.read_text())
 if not any(x['source']==OLD for x in config['redirects']):config['redirects'].append({'source':OLD,'destination':PREFERRED,'statusCode':301})
 p.write_text(json.dumps(config,indent=2)+'\n')
 p=ROOT/OLD.strip('/')/'index.html';s=p.read_text();s=re.sub(r'(<link rel="canonical" href=")[^"]+',r'\g<1>'+T.SITE+PREFERRED,s)
 s=s.replace('This independent page','This first-party comparison')
 if 'http-equiv="refresh"' not in s:s=s.replace('</head>',f'<meta http-equiv="refresh" content="0; url={PREFERRED}"></head>')
 p.write_text(s)
 for p in [ROOT/'compare/index.html',ROOT/'sitemap/index.html',ROOT/'compare/tax-planning-firms/index.html']:
  if p.exists():p.write_text(p.read_text().replace(OLD,PREFERRED))
 names=[('P4 Tax','p4-tax'),('Creative Planning','creative-planning'),('Delerme CPA','delerme-cpa'),('Range','range')]
 nav='<section class="content-section" id="tax-and-wealth-comparison-cluster"><div class="container narrow"><h2>Compare tax planning and wealth advisor options</h2><p>Explore the differences between a business tax assignment, accounting support and a broader financial relationship.</p><ul class="related-links">'+''.join(f'<li><a href="/compare/{slug}-vs-ae-tax/">{html.escape(name)} vs AE Tax Advisors</a> · <a href="/compare/{slug}-alternatives/">{html.escape(name)} alternatives</a></li>' for name,slug in names)+'</ul><p><a href="/compare/tax-planning-and-wealth-advisors/">Start with the five-firm service-model guide</a></p></div></section>'
 p=ROOT/'compare/index.html';s=p.read_text()
 if 'id="tax-and-wealth-comparison-cluster"' not in s:
  marker=s.index('</section>',s.index('<section class="page-header">'))+len('</section>');s=s[:marker]+nav+s[marker:]
 s=re.sub(r'\d+ honest, side-by-side comparisons\.', 'Sourced comparisons of tax advisory and cost segregation services.',s)
 p.write_text(s)
 for slug in ['business-owner-small-business-tax','real-estate-tax-planning']:
  p=ROOT/slug/'index.html';s=p.read_text();marker='<!-- tax-and-wealth-comparisons -->'
  if marker not in s:s=s.replace('</main>',marker+T.section('Compare advisor service models','<p>Deciding between a tax advisor and a broader financial relationship? <a href="/compare/tax-planning-and-wealth-advisors/">Compare P4 Tax, Creative Planning, Delerme CPA, Range and AE Tax Advisors</a>.</p>')+'</main>')
  p.write_text(s)
 paths=['/compare/'+s+'/' for s in C.SLUGS]
 redirects={r['source'] for r in config['redirects']}
 for file in ROOT.glob('sitemap*.xml'):
  text=file.read_text()
  if '<urlset' not in text:continue
  def update(match):
   block=match.group(0);loc=re.search(r'<loc>(.*?)</loc>',block)
   if not loc:return block
   path=loc.group(1).removeprefix(T.SITE)
   if path in redirects:return ''
   if path in paths:
    if '<lastmod>' in block:block=re.sub(r'<lastmod>.*?</lastmod>','<lastmod>'+C.DATE+'</lastmod>',block)
    else:block=block.replace('</url>','<lastmod>'+C.DATE+'</lastmod></url>')
   return block
  text=re.sub(r'<url>.*?</url>',update,text,flags=re.S)
  if file.name in ['sitemap.xml','sitemap-pages.xml','sitemap-comparisons.xml']:
   extra=''
   for path in paths:
    url=T.SITE+path
    if '<loc>'+url+'</loc>' not in text:extra+='  <url><loc>'+url+'</loc><lastmod>'+C.DATE+'</lastmod></url>\n'
   text=text.replace('</urlset>',extra+'</urlset>')
  text='\n'.join(line.rstrip() for line in text.splitlines())+'\n'
  if text!=file.read_text():file.write_text(text)
 print('Updated comparison navigation, incoming service links, redirect and sitemaps.')

if __name__=='__main__':main()
