#!/usr/bin/env python3
"""Render reviewed AE profile references before public staging.

Run before the production build. No account data or platform credentials belong here.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://www.aetaxadvisors.com'
DATA = json.loads((ROOT / 'content/public-profile-references.json').read_text())
ROWS = sorted(DATA['profiles'], key=lambda row: row['platform'].casefold())
assert len(ROWS) == DATA['count']
assert len({row['slug'] for row in ROWS}) == len({row['url'] for row in ROWS}) == len(ROWS)
assert all(not re.search(r'yelp|trustpilot|bbb\.|nthdegree|dan.?nicholson', row['url'] + row['platform'], re.I) for row in ROWS)
e = lambda value: html.escape(value, quote=True)
template = (ROOT / 'about/index.html').read_text()
template = re.sub(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>.*?</script>', '', template, flags=re.S|re.I)
template = re.sub(r'<span class="trust-badge">(?:IRS Enrolled Agents|Licensed CPAs|SOC 2 Compliant)</span>', '', template)
before, after = re.split(r'<main\b[^>]*>.*?</main>', template, maxsplit=1, flags=re.S|re.I)

STYLE = '''<style>
.profile-reference{padding:3rem 0}.profile-reference .container{max-width:1100px;margin:auto;padding:0 1.25rem}
.profile-reference h1{font-size:clamp(2rem,4vw,3rem);line-height:1.15;margin:.75rem 0 1rem}
.profile-reference h2{font-size:1.55rem;margin:1.75rem 0 .75rem}.profile-reference p,.profile-reference li{line-height:1.7}
.profile-reference a{overflow-wrap:anywhere}.profile-reference .profile-kicker{font-size:.9rem;letter-spacing:.07em;text-transform:uppercase;color:#476178}
.profile-reference .profile-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,250px),1fr));gap:1rem;list-style:none;padding:0}
.profile-reference .profile-grid li,.profile-reference .profile-panel{border:1px solid #d9e2e9;border-radius:12px;padding:1.25rem;background:#fff}
.profile-reference .profile-grid p{margin:.5rem 0 0;font-size:.95rem}.profile-reference .profile-url{word-break:break-word}
.profile-reference .profile-button{display:inline-block;padding:.8rem 1.1rem;background:#18394e;color:#fff;border-radius:6px;text-decoration:none;margin:.5rem 0}
.profile-reference dl{display:grid;grid-template-columns:minmax(100px,150px) 1fr;gap:.5rem 1rem}.profile-reference dt{font-weight:700}.profile-reference dd{margin:0;min-width:0;overflow-wrap:anywhere}
@media(max-width:480px){.profile-reference dl{display:block}.profile-reference dd{margin:0 0 .85rem}.profile-reference{padding:1.5rem 0}}
</style>'''

def render(route, title, description, body, platform=None):
    head = re.sub(r'<title>.*?</title>', '<title>'+e(title)+'</title>', before, count=1, flags=re.S)
    head = re.sub(r'(<meta\b[^>]*(?:name|property)=["\'](?:description|og:description|twitter:description)["\'][^>]*content=)["\'][^"\']*["\']', lambda m:m[1]+'"'+e(description)+'"', head)
    head = re.sub(r'(<meta\b[^>]*(?:property|name)=["\'](?:og:title|twitter:title)["\'][^>]*content=)["\'][^"\']*["\']', lambda m:m[1]+'"'+e(title)+'"', head)
    head = re.sub(r'<link rel="canonical" href="[^"]+">', '<link rel="canonical" href="'+BASE+route+'">', head)
    head = re.sub(r'(<meta property="og:url" content=")[^"]+', lambda m:m[1]+BASE+route, head)
    crumbs = [{'@type':'ListItem','position':1,'name':'Home','item':BASE+'/'}, {'@type':'ListItem','position':2,'name':'Public profiles','item':BASE+'/profiles/'}]
    if platform: crumbs.append({'@type':'ListItem','position':3,'name':platform,'item':BASE+route})
    schema={'@context':'https://schema.org','@graph':[{'@type':'WebPage','@id':BASE+route+'#webpage','url':BASE+route,'name':title,'description':description,'dateModified':'2026-11-21','publisher':{'@type':'Organization','name':'AE Tax Advisors','url':BASE+'/'}}, {'@type':'BreadcrumbList','itemListElement':crumbs}]}
    head=head.replace('</head>',STYLE+'\n<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False)+'</script>\n</head>')
    path=ROOT/route.strip('/')/'index.html';path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(head+'<main class="profile-reference" id="main-content"><div class="container">'+body+'</div></main>'+after)

def facts():
    return '''<section class="profile-panel" aria-labelledby="ae-official-details"><h2 id="ae-official-details">Current AE contact information</h2>
<dl><dt>Business</dt><dd>AE Tax Advisors</dd><dt>Address</dt><dd>935 Lake Elmo Dr, Suite B, Billings, MT 59105</dd>
<dt>Phone</dt><dd><a href="tel:+16316145762">(631) 614-5762</a></dd><dt>Email</dt><dd><a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a></dd>
<dt>Hours</dt><dd>Monday–Friday, 7:00 AM–3:00 PM Mountain Time. Saturday–Sunday closed.</dd><dt>Founded</dt><dd>2021</dd></dl>
<p>For current service scope, visit <a href="/services/">AE's services</a>, read <a href="/about/">about the firm</a>, or <a href="/contact/">contact AE directly</a>.</p></section>'''

for row in ROWS:
    name=e(row['platform']);url=e(row['url']);route='/profiles/'+row['slug']+'/'
    title='AE Tax Advisors on '+row['platform']+' | Public Profile Reference'
    description='Find AE Tax Advisors on '+row['platform']+'. View the public profile link and confirm AE’s current Billings address, phone and service information.'
    campaign_detail='<p>'+e(row['campaign_detail'])+'</p>' if row.get('campaign_detail') else ''
    campaign_section='<section aria-labelledby="campaign-context"><h2 id="campaign-context">What AE verified on '+name+'</h2><p>'+e(row['campaign_summary'])+'</p>'+campaign_detail+'</section>'
    body=f'''<nav aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/profiles/">Public profiles</a> / {name}</nav>
<p class="profile-kicker">AE public profile reference</p><h1>AE Tax Advisors on {name}</h1>
<p>{e(row['note'])}</p><section class="profile-panel" aria-labelledby="external-profile"><h2 id="external-profile">Open the {name} profile</h2>
<p><a class="profile-button" href="{url}" target="_blank" rel="noopener">Visit AE on {name} <span aria-hidden="true">↗</span></a></p>
<p class="profile-url"><strong>Exact external address:</strong> <a href="{url}">{url}</a></p>
<p><strong>Reference status:</strong> {e(row['status'])}. Found during AE's profile verification campaign; reference inventory compiled November 21, 2026.</p></section>
<section><h2>Check the business identity before making contact</h2><p>This reference is published by AE Tax Advisors to help you find the specific {name} page associated with the firm. Match the business name, Billings location and official website when a platform presents several similar results.</p>
<p>Third-party descriptions, categories and hours may differ from AE's current information. A public listing does not establish platform endorsement, professional licensing or that every field is managed by AE. Use the official details below when deciding how to reach the firm.</p></section>{campaign_section}
{facts()}<section><h2>Choose the next step for your tax questions</h2><p>For business-owner or real-estate planning, start with <a href="/services/tax-planning/">AE's tax-planning service</a>. For ongoing records, see <a href="/services/bookkeeping/">bookkeeping</a>. Discuss the work, timing and records needed before starting an engagement.</p>
<p>Keep tax returns and other confidential records out of public profile comments or messages. Ask AE for its secure document channel.</p><p><a href="/profiles/">Browse all public profile references</a></p></section>'''
    render(route,title,description,body,row['platform'])

cards=''.join('<li><h2><a href="/profiles/'+e(r['slug'])+'/">'+e(r['platform'])+'</a></h2><p>'+e(r['note'])+'</p><p><strong>'+e(r['status'])+'</strong></p></li>' for r in ROWS)
body=f'''<nav aria-label="Breadcrumb"><a href="/">Home</a> / Public profiles</nav><p class="profile-kicker">AE Tax Advisors online</p><h1>Public profiles and directory references</h1>
<p>Find the specific public pages associated with AE Tax Advisors across business directories, social networks and publication platforms. Each reference below links to the external page and provides AE's current official contact details.</p>
<p>These {len(ROWS)} references collect public pages found during AE's profile verification campaign. This reference inventory was compiled November 21, 2026. Some are independently maintained listings. Inclusion does not imply endorsement, ownership of the platform, professional accreditation or that its information is fully current.</p>
<p>Looking for help from AE? Go directly to <a href="/services/">services</a> or <a href="/contact/">contact the team</a>.</p><ul class="profile-grid">'''+cards+'</ul>'+facts()
render('/profiles/','AE Tax Advisors Public Profiles & Directory References',f'Find {len(ROWS)} public AE Tax Advisors profiles, directory listings and publication pages, with exact links and current official contact information.',body)

about=ROOT/'about/index.html';text=about.read_text()
intro='<p>Find AE Tax Advisors on these public profile platforms:</p>'
new_intro='<p>Find AE Tax Advisors on these public profile platforms. <a href="/profiles/">Browse the profile reference guide</a> for exact links and current official business details.</p>'
if intro in text:text=text.replace(intro,new_intro,1)
about.write_text(text)
routes=['/profiles/']+['/profiles/'+r['slug']+'/' for r in ROWS]
xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('  <url><loc>'+BASE+r+'</loc><lastmod>2026-11-21</lastmod></url>\n' for r in routes)+'</urlset>\n'
(ROOT/'sitemap-profiles.xml').write_text(xml)
for filename in ('sitemap-index.xml','sitemap_index.xml'):
    p=ROOT/filename;s=p.read_text()
    if '/sitemap-profiles.xml' not in s:s=s.replace('</sitemapindex>','  <sitemap><loc>'+BASE+'/sitemap-profiles.xml</loc></sitemap>\n</sitemapindex>')
    p.write_text(s)
print(json.dumps({'profile_pages':len(ROWS),'hub_pages':1,'sitemap_urls':len(routes),'output':'profiles/'}))
