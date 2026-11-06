"""Read-only release checks for approved, crawlable blog archive coverage."""
from pathlib import Path
from urllib.parse import urlsplit
import collections, html, json, re, sys, xml.etree.ElementTree as ET
import blog_archive as archive
ROOT = archive.ROOT
out = ROOT / (sys.argv[1] if len(sys.argv)>1 else '.')
entries=archive.load();expected={e['url'] for e in entries};assert len(expected)==len(entries)
migration=json.loads((ROOT/'scripts/blog-archive-migration.json').read_text())
original={e['canonical'] for e in migration['routes'] if 'canonical' in e}
additional={e['canonical'] for e in migration['routes'] if e.get('origin')=='additional-approved-link'}
assert len(original)==1232 and len(additional)==409 and original<=expected
search=json.loads((out/'assets/blog-search-index.json').read_text())
assert {e['url']for e in search}==expected and len(search)==len(expected)
assert collections.Counter(e['category'] for e in search)==collections.Counter(e['category'] for e in entries)
pages=(len(entries)+archive.PAGE_SIZE-1)//archive.PAGE_SIZE
seen=[];titles=set();canonicals=set();max_size=0
for number in range(1,pages+1):
 route=archive.archive_path(number);p=out/route.strip('/')/'index.html';s=p.read_text();max_size=max(max_size,len(s.encode()))
 assert s.count('<h1>')==1,route
 title=re.search('<title>(.*?)</title>',s,re.S)[1];assert title not in titles; titles.add(title)
 canonical=re.findall(r'<link[^>]*rel="canonical"[^>]*href="([^"]+)"',s);assert canonical==[archive.SITE+route];canonicals.update(canonical)
 assert 'noindex' not in archive.Metadata(s).meta.get('robots','')
 cards=re.findall(r'<article class="blog-card">.*?</article>',s,re.S)
 urls=[re.search(r'href="([^"]+)"',c)[1]for c in cards]
 assert len(cards)==min(archive.PAGE_SIZE,len(entries)-(number-1)*archive.PAGE_SIZE)
 seen+=urls
 schemas=[json.loads(j) for j in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S)]
 collection=[d for d in schemas if d.get('@type')=='CollectionPage'];assert len(collection)==1
 items=collection[0]['mainEntity']['itemListElement'];assert [urlsplit(i['url']).path for i in items]==urls
 assert collection[0]['mainEntity']['numberOfItems']==len(cards)
 assert not any(d.get('@type')=='Blog' for d in schemas),'Old full-catalog schema restored'
 nav=re.search(r'<nav id="blog-pagination".*?</nav>',s,re.S)[0]
 if number>1:assert 'href="'+archive.archive_path(number-1)+'"'in nav
 if number<pages:assert 'href="'+archive.archive_path(number+1)+'"'in nav
 assert '/blog/page/1/' not in s
 assert len(s.encode())<100000,'Unbounded archive payload: '+route
 assert '/assets/blog-search.js' in s and 'fetch(' not in s
 main=re.search(r'<main\b.*?</main>',s,re.S)[0]
 for href in re.findall(r'href="([^"]+)"',main):
  if not href.startswith('/') or href.startswith('//'):continue
  f=out/urlsplit(html.unescape(href)).path.lstrip('/')
  assert f.is_file() or (f/'index.html').is_file() or f.with_suffix('.html').is_file(),href
assert set(seen)==expected and len(seen)==len(expected),'Coverage missing or duplicated'
assert additional<=set(seen),'Noncard migration links lost'
for e in entries: assert archive.article(e['url'],e['category'])['url']==e['url']
ns={'s':archive.NS};xml=ET.parse(out/'sitemap-blog-archive.xml');locs={e.text for e in xml.findall('s:url/s:loc',ns)}
assert locs==canonicals
for name in ['sitemap-index.xml','sitemap_index.xml']:assert '/sitemap-blog-archive.xml' in (out/name).read_text()
# Keep every article in existing discovery XML as well as the paginated archive.
sitemap_articles=set()
for p in out.glob('sitemap*.xml'):
 for node in ET.parse(p).iter():
  if node.tag.endswith('loc') and node.text:sitemap_articles.add(urlsplit(node.text).path)
assert expected<=sitemap_articles,'Article sitemap coverage lost'
print(f'PASS blog archive: {len(expected)} unique articles, all {len(additional)} extra approved routes, {pages} crawlable pages, visible-only schema, valid links/holds/canonicals/sitemaps; maximum HTML {max_size:,} bytes.')
