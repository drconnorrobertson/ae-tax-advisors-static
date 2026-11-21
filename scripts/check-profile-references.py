#!/usr/bin/env python3
"""Check generated profile/data/sitemap parity in the actual release output."""
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / (sys.argv[1] if len(sys.argv) > 1 else 'public')
data = json.loads((ROOT/'content/public-profile-references.json').read_text())
rows = data['profiles']
assert len(rows) == data['count']
base = 'https://www.aetaxadvisors.com'
expected = {base+'/profiles/'} | {base+'/profiles/'+r['slug']+'/' for r in rows}
ns = {'sm':'http://www.sitemaps.org/schemas/sitemap/0.9'}
actual = [n.text for n in ET.parse(OUT/'sitemap-profiles.xml').findall('sm:url/sm:loc',ns)]
assert set(actual) == expected and len(actual) == len(expected), 'Sitemap parity'
hub = (OUT/'profiles/index.html').read_text()
titles=set(); descriptions=set()
for row in rows:
    route='/profiles/'+row['slug']+'/'
    page=(OUT/route.strip('/')/'index.html').read_text()
    assert f'href="{route}"' in hub, 'Hub link missing: '+route
    assert f'href="{html.escape(row["url"],quote=True)}"' in page, 'External profile missing'
    canonical=re.findall(r'<link rel="canonical" href="([^"]+)"',page)
    assert canonical == [base+route], 'Canonical: '+route
    assert not re.search(r'<meta[^>]+content="[^"]*noindex',page,re.I), 'Noindex: '+route
    title=re.search(r'<title>(.*?)</title>',page,re.S)[1]
    desc=re.search(r'<meta name="description" content="([^"]+)"',page)[1]
    assert title not in titles and desc not in descriptions, 'Duplicate metadata'
    titles.add(title);descriptions.add(desc)
    for text in ['AE Tax Advisors','935 Lake Elmo Dr, Suite B','Billings, MT 59105','(631) 614-5762','team@aetaxadvisors.com']:
        assert text in page, 'Missing official fact: '+route
    schemas=[json.loads(s) for s in re.findall(r'<script type="application/ld\+json">(.*?)</script>',page,re.S)]
    assert schemas, 'No schema: '+route
    assert 'Public profile reference' in page or 'public profile reference' in page, 'Missing purpose'
print(json.dumps({'profile_pages':len(rows),'hub_pages':1,'sitemap_urls':len(actual),'unique_titles':len(titles),'errors':[]}))
