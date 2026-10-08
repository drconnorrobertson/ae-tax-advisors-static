import html,json,re,xml.etree.ElementTree as ET
from pathlib import Path
import site_template as T
from build_approved_comparison_pages import render
from build_competitor_coverage_20261008 import patch
ROOT=Path(__file__).resolve().parent;DATE='2026-10-08'
pages=json.loads((ROOT/'content/adjacent-audiences-20261008.json').read_text())
def main():
 paths=[]
 for p in pages:
  path='/compare/'+p['slug']+'/';target=ROOT/path.strip('/')/'index.html'
  # All four researched intents have one designated owner. Rebuild in place.
  published=DATE
  if target.exists():
   m=re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})',target.read_text())
   if m:published=m[1]
  trail=[('Home','/'),('Compare services','/compare/'),(p['title'],path)]
  markup,_=render(p['body'].splitlines(),p['slug'])
  body=T.page_header(h1=html.escape(p['title']),subtitle=html.escape(p['description']),trail=trail)+T.section('Compare the help you need',markup)+T.CTA_BLOCK
  schemas=[T.article_schema(title=p['title'],description=p['description'],url=T.SITE+path,published=published,modified=DATE,section='Physician service comparison',citations=p['sources']+[T.SITE+'/pricing/']),T.breadcrumb_schema(trail)]
  doc=T.build_page(title=p['title']+' | AE',description=p['description'],path=path,body=body,schemas=schemas,published=published,modified=DATE,active_nav='/compare/',extra_head='<link rel="stylesheet" href="/assets/footer.css?v=20261001">')
  T.write_page(path,'\n'.join(line.rstrip() for line in doc.splitlines())+'\n');paths.append(path)
 marker='adjacent-audiences-20261008'
 links='<ul>'+''.join('<li><a href="'+path+'">'+html.escape(p['title'])+'</a></li>' for path,p in zip(paths,pages))+'</ul>'
 section='<!-- '+marker+':start -->'+T.section('Physician financial resources and the next planning step','<p>Compare education, debt advice, household financial planning, and a defined business or property tax project.</p>'+links)+'<!-- '+marker+':end -->'
 hubs=['/compare/','/physician-tax-planning/','/compare/best-tax-advisors-physicians-rental-property/']
 for path in hubs:
  target=ROOT/path.strip('/')/'index.html';doc=target.read_text();doc=re.sub('<!-- '+marker+':start -->.*?<!-- '+marker+':end -->','',doc,flags=re.S)
  doc=doc.replace('</main>',section+'\n</main>',1)
  def schema(m):
   obj=json.loads(m[1])
   if obj.get('@type')=='Article':obj['dateModified']=DATE
   return T.jsonld(obj)
  doc=re.sub(r'<script type="application/ld\+json">(.*?)</script>',schema,doc,flags=re.S)
  target.write_text(doc)
 for filename in ['sitemap.xml','sitemap-comparisons.xml']:
  target=ROOT/filename;xml=target.read_text()
  for path in paths+hubs:
   if filename=='sitemap-comparisons.xml' and not path.startswith('/compare/'):continue
   url=T.SITE+path;node='<url><loc>'+html.escape(url)+'</loc><lastmod>'+DATE+'</lastmod></url>';pattern=r'<url>\s*<loc>'+re.escape(url)+r'</loc>.*?</url>'
   if re.search(pattern,xml,re.S):xml=re.sub(pattern,node,xml,flags=re.S)
   else:xml=xml.replace('</urlset>',node+'\n</urlset>')
  ET.fromstring(xml);target.write_text(xml)
 (ROOT/'_gen/adjacent-audiences-20261008.json').write_text(json.dumps({'new_paths':paths,'updated_hubs':hubs,'sources':{p['slug']:p['sources'] for p in pages}},indent=2)+'\n')
 print('Published source files for four distinct adjacent-audience guides.')
if __name__=='__main__':main()
