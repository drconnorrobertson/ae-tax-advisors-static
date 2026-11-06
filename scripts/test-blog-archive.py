"""Author-time safety fixtures and deterministic output check (not deployment)."""
import hashlib, json, subprocess, sys
from pathlib import Path
from unittest.mock import patch
import blog_archive as a
route=a.load()[0]['url'];source=a.ROOT/route.strip('/')/'index.html'
# Held entries cannot be promoted by registration or rendering.
with patch.object(a,'restrictions',return_value=({route},{})):
 try:a.article(route);raise AssertionError('Held article admitted')
 except ValueError as e:assert 'held' in str(e)
# Redirects resolve only to another supported, approved article route.
other=a.load()[1]['url']
with patch.object(a,'restrictions',return_value=(set(),{route:other})):
 assert a.article(route)['url']==other
with patch.object(a,'restrictions',return_value=(set(),{route:other,other:route})):
 try:a.article(route);raise AssertionError('Cycle admitted')
 except ValueError as e:assert 'cycle' in str(e)
read=Path.read_text
for addition,reason in [('<meta name="robots" content="noindex">','noindex'),('<p>Nth Degree CPAs</p>','Excluded provider')]:
 def fixture(p,*args,**kwargs):
  value=read(p,*args,**kwargs)
  return value.replace('</head>',addition+'</head>') if p==source else value
 with patch.object(Path,'read_text',fixture):
  try:a.article(route);raise AssertionError('Restricted article admitted')
  except ValueError as e:assert reason in str(e),str(e)
for invalid in ['/blog/../private/','/blog/page/2/','https://other.example/blog/post/']:
 try:a.article(invalid);raise AssertionError('Unsafe route admitted')
 except ValueError:pass
# Explicit clean-URL routes can be backed by flat HTML, without scanning it in.
import tempfile
with tempfile.TemporaryDirectory() as temporary:
    temp=Path(temporary)
    flat_route='/blog/explicit-flat-fixture/'
    doc='<html><head><link rel="canonical" href="'+a.SITE+flat_route+'"><meta name="description" content="Reviewed flat-source fixture."></head><body><h1>Flat source</h1></body></html>'
    flat=temp/'blog/explicit-flat-fixture.html';flat.parent.mkdir(parents=True);flat.write_text(doc)
    with patch.object(a,'ROOT',temp), patch.object(a,'restrictions',return_value=(set(),{})):
        assert a.article(flat_route)['title']=='Flat source'
        directory=temp/'blog/explicit-flat-fixture/index.html';directory.parent.mkdir();directory.write_text(doc)
        assert a.article(flat_route)['url']==flat_route
        directory.write_text(doc.replace('Flat source','Conflicting title'))
        try:a.article(flat_route);raise AssertionError('Conflicting sources admitted')
        except ValueError as e:assert 'Conflicting directory and flat' in str(e)
        overrides=temp/'scripts/blog-archive-source-overrides.json';overrides.parent.mkdir();overrides.write_text(json.dumps({flat_route:'blog/explicit-flat-fixture.html'}))
        assert a.article(flat_route)['title']=='Flat source'
        overrides.write_text(json.dumps({flat_route:'../outside.html'}))
        try:a.article(flat_route);raise AssertionError('Unsafe override admitted')
        except ValueError as e:assert 'Conflicting directory and flat' in str(e)
paths=[a.ROOT/'blog/index.html',a.CATALOG,a.ROOT/'assets/blog-search-index.json',a.ROOT/'sitemap-blog-archive.xml',a.ROOT/'sitemap-index.xml',a.ROOT/'sitemap_index.xml']+list((a.ROOT/'blog/page').glob('*/index.html'))
def snapshot():return {str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths}
before=snapshot();a.render();assert snapshot()==before,'Renderer not idempotent'
a.register_routes([route]);assert snapshot()==before,'Existing registration changed output'
subprocess.run([sys.executable,str(a.ROOT/'scripts/check-blog-archive.py')],check=True)
print('PASS catalog safety: holds, noindex, provider exclusion, canonical redirect/cycle, unsafe paths, renderer and registration idempotence.')
