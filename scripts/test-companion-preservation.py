"""Keep the independently published companion section through archive refreshes."""
from pathlib import Path
import hashlib,re,sys
import blog_archive as archive
ROOT=Path(__file__).resolve().parents[1]
START='<!-- external-companions:start -->';END='<!-- external-companions:end -->'
block=archive.external_companion_block((ROOT/'blog/index.html').read_text())
assert block and block.count('<li>')==6
assert re.search(r'<main\b[^>]*>'+re.escape(block),(ROOT/'blog/index.html').read_text())
links=re.findall(r'href="([^"]+)"',block)
assert len(links)==len(set(links))==6
for link in links:assert (ROOT/link.strip('/')/'index.html').is_file()
assert archive.external_companion_block('No marked section')==''
fixture=START+'<section><p>Keep every byte &amp; link.</p></section>'+END
assert archive.external_companion_block('<main>'+fixture+'</main>')==fixture
for bad in [START,END,END+START,fixture+fixture,START+'<main>Bad</main>'+END,START+END+END]:
 try:archive.external_companion_block(bad)
 except ValueError:pass
 else:raise AssertionError('Malformed marker fixture accepted')
files=[ROOT/'blog/index.html',*sorted((ROOT/'blog/page').glob('*/index.html')),ROOT/'assets/blog-search-index.json',ROOT/'sitemap-blog-archive.xml']
files += [ROOT/link.strip('/')/'index.html' for link in links] + [ROOT/'build_external_companions.py',ROOT/'sitemap.xml',ROOT/'sitemap-blog.xml']
def hashes():return {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
before=hashes();archive.render();assert hashes()==before
archive.render();assert hashes()==before
assert archive.external_companion_block((ROOT/'blog/index.html').read_text())==block
for p in (ROOT/'blog/page').glob('*/index.html'):assert START not in p.read_text()
if len(sys.argv)>1:assert archive.external_companion_block((Path(sys.argv[1])/'blog/index.html').read_text())==block
print('PASS: six existing companion links, exact section preservation, two idempotent archive renders, six malformed-marker fixtures, no archive-page duplication.')
