#!/usr/bin/env python3
"""Apply a researched competitor-name layer without multiplying equivalent URLs.

Only the dated profiles in the adjacent JSON file are source inputs. Existing
comparison URLs are retained; new firms get one comparison. Screenshot firms
also get an alternatives guide with a distinct, multi-provider shortlist.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import site_template as T

DATE = '2026-10-01'
FIRMS = json.loads(Path(__file__).with_name('competitor_name_profiles_20261001.json').read_text())
E = html.escape
HUB = '/compare/tax-planning-firms/'
CHANGED = []

def path(f):
    return '/compare/' + f.get('path_slug', f['slug'] + '-vs-ae-tax') + '/'

def sources(f):
    urls = [f['source']]
    if f.get('extra_source'):
        urls.append(f['extra_source'])
    return urls

def p(text):
    return '<p>' + E(text) + '</p>'

def source_links(f):
    return '<ul>' + ''.join(f'<li><a href="{E(u)}" rel="external noopener">{E(f["name"])} official {"services / website" if i == 0 else "company overview"}</a></li>' for i, u in enumerate(sources(f))) + '</ul>'

def disclosure(f):
    return p('Published by AE Tax Advisors, a competing provider. This comparison is not affiliated with or endorsed by ' + f['name'] + '. The overview below was checked against the linked official materials on October 1, 2026. Public marketing describes an offered service; your signed engagement determines what is included. Unconfirmed scope is a question to resolve, not proof a service is unavailable.')

def profile(f):
    name = E(f['name'])
    body = p(f['summary']) + '<dl><dt><strong>Who might compare this firm with AE?</strong></dt><dd>' + E(f['fit']) + '</dd><dt><strong>Key scope question</strong></dt><dd>' + E(f['question']) + '</dd></dl>'
    body += p(f['decision']) + source_links(f) + disclosure(f)
    body += f'<p><a href="#competitor-fees">Compare pricing and deliverables</a> · <a href="{HUB}">Browse tax planning firms by client fit</a></p>'
    return '<section class="content-section" id="competitor-overview"><div class="container narrow"><h2>' + name + ': firm overview and services</h2>' + body + '</div></section>'

def fees(f):
    return '<section class="content-section" id="competitor-fees"><div class="container narrow"><h2>' + E(f['name']) + ': pricing and engagement scope</h2>' + p('Request a current written quote from the firm for your income, entities, and required filings. This overview does not publish an unverified numeric competitor fee. Separate the planning project, implementation, annual returns, monthly accounting, and future advisory costs; a starting preparation fee is not the price of a complete planning engagement.') + '<p>AE Tax Advisors publishes <strong>$7,800 Strategic Tax Advisory and $9,800 Complex Tax Advisory</strong>. Returns, amendments, cost segregation, and additional work are separately scoped and priced. The standard advisory engagement has no required annual planning renewal; future work is governed by its agreed scope. <a href="/pricing/">See current AE pricing</a>.</p><p>Request matching written proposals using the <a href="/tools/tax-advisor-engagement-scorecard/">tax advisor engagement scorecard</a>. Compare the complete work and total cost on the same facts.</p></div></section>'

def comparison(f):
    rows = [
        ('Client fit to investigate', f['fit'], 'Profitable business owners, rental investors, and owners coordinating both.'),
        ('First scope question', f['question'], 'Which planning, prior-year review, study, amendment, and preparation deliverables are included?'),
        ('Pricing basis', 'Request a current proposal separating planning, execution, returns, and ongoing services.', '$7,800 strategic or $9,800 complex advisory; preparation, amendments, studies, and additional services separately scoped.'),
        ('Implementation accountability', 'Confirm the assigned professionals and any preparer or outside-provider handoffs.', 'Confirm the responsible professional and deadline for each action in the written scope.'),
        ('Future commitments', 'Confirm optional and required recurring work in the proposed contract.', 'No required annual planning renewal in the standard advisory engagement; future work is separately scoped.'),
    ]
    table = '<div style="overflow-x:auto"><table><caption>Compare the written engagement on the same facts; public offerings do not establish every contract term.</caption><thead><tr><th scope="col">Decision</th><th scope="col">' + E(f['name']) + '</th><th scope="col">AE Tax Advisors</th></tr></thead><tbody>'
    for label, other, ae in rows:
        table += '<tr><th scope="row">' + E(label) + '</th><td>' + E(other) + '</td><td>' + E(ae) + '</td></tr>'
    return T.section('Side-by-side engagement comparison', table + '</tbody></table></div>')

def faqs(f):
    return [
        ('What does ' + f['name'] + ' do?', p(f['summary'])),
        ('How should I compare ' + f['name'] + ' with AE Tax Advisors?', p(f['question'] + ' Compare the assigned professionals, written plan, execution responsibilities, covered filings, first-year total, and future fees.')),
        ('Does this page rate client reviews of ' + f['name'] + '?', p('No. This is a service and engagement comparison published by a competing firm, not an independent customer review or a rating of client satisfaction. Check recent reviews and professional credentials directly, and ask about experience with a situation like yours.')),
    ]

def save(page_path, title, description, body, firms, faqs=None):
    url = T.SITE + page_path
    citations = list(dict.fromkeys(u for f in firms for u in sources(f)))
    schemas = [T.article_schema(title=title, description=description, url=url, published=DATE, modified=DATE, section='Tax Advisor Comparison', about=[{'@type': 'Organization', 'name': f['name'], 'url': f['source']} for f in firms], citations=citations), T.breadcrumb_schema([('Home', '/'), ('Compare firms', '/compare/'), (title, page_path)])]
    if faqs:
        schemas.append(T.faq_schema(faqs))
    markup = T.build_page(title=title, description=description, path=page_path, body=body, schemas=schemas, published=DATE, modified=DATE, active_nav='/compare/')
    T.write_page(page_path, markup)
    CHANGED.append(page_path)

def update_schema(data, title, description, f):
    if isinstance(data, list):
        return [update_schema(x, title, description, f) for x in data]
    if not isinstance(data, dict):
        return data
    if data.get('@type') == 'Article':
        data.update(headline=title, description=description, dateModified=DATE)
        about = data.get('about', [])
        if not isinstance(about, list):
            about = [about]
        about = [x for x in about if isinstance(x, dict) and x.get('name') != f['name']]
        data['about'] = about + [{'@type': 'Organization', 'name': f['name'], 'url': f['source']}]
        citation = data.get('citation', [])
        if not isinstance(citation, list):
            citation = [citation]
        data['citation'] = list(dict.fromkeys(citation + sources(f)))
    if data.get('@type') == 'BreadcrumbList':
        data['itemListElement'][-1]['name'] = title
    for k, v in list(data.items()):
        if isinstance(v, (list, dict)):
            data[k] = update_schema(v, title, description, f)
    return data

for f in FIRMS:
    target = ROOT / path(f).strip('/') / 'index.html'
    title = f['name'] + ': Services & Comparison With AE Tax'
    description = 'Explore ' + f['name'] + "'s services, client fit, pricing questions, and implementation scope. Compare its public model with AE Tax Advisors."
    # Long names keep a concise, accurate search title.
    if len(title) > 78:
        title = f['name'] + ': Services & AE Tax Comparison'
    if target.exists() and f['slug'] != 'tax-alchemy':
        text = target.read_text()
        text = re.sub(r'<title>.*?</title>', '<title>' + E(title) + '</title>', text, count=1, flags=re.S)
        for selector, content in [('name="description"', description), ('property="og:title"', title), ('property="og:description"', description), ('name="twitter:title"', title), ('name="twitter:description"', description), ('property="article:modified_time"', DATE + 'T00:00:00-04:00')]:
            text = re.sub(r'(<meta\s+' + re.escape(selector) + r'\s+content=")[^"]*(")', lambda m: m[1] + E(content, quote=True) + m[2], text)
        text = re.sub(r'<h1>.*?</h1>', '<h1>' + E(title) + '</h1>', text, count=1, flags=re.S)
        text = re.sub(r'<p class="subtitle">.*?</p>', '<p class="subtitle">' + E(description) + '</p>', text, count=1, flags=re.S)
        text = re.sub(r'<script type="application/ld\+json">(.*?)</script>', lambda m: '<script type="application/ld+json">\n' + json.dumps(update_schema(json.loads(m[1]), title, description, f), indent=2) + '\n</script>', text, flags=re.S)
        # Repeatable generation replaces only our own blocks.
        text = re.sub(r'<section class="content-section" id="competitor-(?:overview|fees)">.*?</section>', '', text, flags=re.S)
        header = re.search(r'<section class="page-header">.*?</section>', text, re.S)
        assert header, target
        text = text[:header.end()] + '\n' + profile(f) + fees(f) + text[header.end():]
        target.write_text(text)
        CHANGED.append(path(f))
    else:
        fs = faqs(f)
        body = T.page_header(h1=E(title), subtitle=E(description), trail=[('Home', '/'), ('Compare firms', '/compare/'), (E(f['name']), path(f))]) + profile(f)
        body += T.section('How to decide between the engagements', p(f['decision']) + '<p>AE Tax Advisors focuses on business-owner and real estate tax planning, prior-year review, and separately scoped implementation and compliance work. <a href="/business-owner-tax-planning/">Review business planning</a> and <a href="/real-estate-investor-cpa/">real estate advisory</a> to see whether the work matches your situation.</p>')
        body += comparison(f) + fees(f)
        body += T.section('Questions to resolve before hiring', '<ol><li>' + E(f['question']) + '</li><li>Who writes the plan, performs each action, and prepares or reviews each return?</li><li>What records, deadlines, and outside professionals does the plan require?</li><li>Which services are excluded, and what future fees or renewal commitments apply?</li></ol>')
        body += T.faq_section(fs)
        body += T.related_section([(HUB, 'Compare tax planning firms by client fit'), ('/compare/tax-advisor-comparison-methodology/', 'How AE researches comparisons'), ('/pricing/', 'AE Tax Advisors pricing')])
        save(path(f), title, description, body, [f], fs)

categories = list(dict.fromkeys(f['category'] for f in FIRMS))
title = 'Tax Planning Firms: Business Owner & Real Estate Comparisons'
description = 'Compare tax planning firms by client fit, services, implementation, and accounting needs. Sourced profiles for business owners, investors, and physicians.'
body = T.page_header(h1=title, subtitle=description, trail=[('Home', '/'), ('Compare firms', '/compare/'), ('Tax planning firms', HUB)])
body += T.section('Start with the work you need', '<p>These firms offer personalized tax planning, advisory, or implementation that can overlap with AE Tax Advisors. Inclusion reflects public service overlap, not measured search popularity or evidence that a firm is inferior. Some specialize in owners and rentals; others fit physicians, executives, or businesses that also need an accounting and finance team.</p><p>AE Tax Advisors publishes this directory as a competing provider. Read the linked firm sources and request matching written proposals. Profiles checked October 1, 2026.</p>')
for category in categories:
    items = ''.join('<li><h3><a href="' + path(f) + '">' + E(f['name']) + '</a></h3>' + p(f['fit']) + '</li>' for f in FIRMS if f['category'] == category)
    body += T.section(category, '<ul class="related-links">' + items + '</ul>')
body += T.related_section([('/compare/tax-strategy-accounting-cfo-firms/', 'Tax strategy with accounting and CFO support'), ('/compare/tax-planning-implementation-firms/', 'Compare tax planning implementation models'), ('/compare/physician-business-real-estate-tax-advisors/', 'Physician, business, and real estate planning')])
save(HUB, title, description, body, FIRMS)

# These alternative guides answer a multi-provider shortlisting decision rather
# than duplicating the firm overview on each comparison URL.
by_slug = {f['slug']: f for f in FIRMS}
shortlists = {
    'pillar-advisors': ['dark-horse-cpas', 'incite-tax', 'peter-holtz-cpa', 'anomaly-cpa'],
    'graphite-financial': ['anomaly-cpa', 'dark-horse-cpas', 'pillar-advisors', 'gelt'],
    'tax-strategists-of-america': ['proactive-tax-advisors', 'tax-alchemy', 'keystone-cpa', 'fluency-tax'],
}
for slug, peers in shortlists.items():
    f = by_slug[slug]
    page_path = '/compare/' + slug + '-alternatives/'
    title = f['name'] + ' Alternatives: Compare Scope & Client Fit'
    description = 'Compare alternatives to ' + f['name'] + ' for tax strategy, implementation, and accounting. Choose by actual deliverables rather than brand alone.'
    body = T.page_header(h1=E(title), subtitle=E(description), trail=[('Home', '/'), ('Compare firms', '/compare/'), (E(f['name']) + ' alternatives', page_path)])
    body += T.section('When to consider another provider', p(f['decision']) + '<p>An alternative belongs on your shortlist when its scope fits an unmet need. There is no reason to switch if the current provider is covering the work well. This guide is published by AE Tax Advisors, a competing firm, and does not rank providers by client satisfaction.</p><p><a href="' + path(f) + '">Read the ' + E(f['name']) + ' service overview and comparison</a>.</p>')
    body += T.section('AE Tax Advisors: a planning and implementation option', '<p>Compare AE when the priority is a business and real estate tax plan, prior-year review, amendments, or cost segregation and related filings. Its published advisory tiers are $7,800 and $9,800; returns, studies, and other work are separately priced. Confirm the complete scope rather than treating an advisory fee as a bundled accounting price. <a href="/pricing/">See AE pricing</a>.</p>')
    for peer in peers:
        pf = by_slug[peer]
        body += T.section(E(pf['name']), p(pf['fit']) + p(pf['question']) + '<p><a href="' + path(pf) + '">Read services and comparison</a> · <a href="' + E(pf['source']) + '" rel="external noopener">Official website</a></p>')
    body += T.section('Compare the proposed work', '<p>Use the same entities, prior returns, income assumptions, and decision deadlines for every quote. Identify the planning deliverable, execution owner, preparer, and ongoing accounting responsibilities. Compare the first-year total and future obligations. A proposal with a missing service is a reason to ask a question before changing providers.</p>')
    body += T.related_section([(HUB, 'All tax planning firm comparisons'), ('/tools/tax-advisor-engagement-scorecard/', 'Compare written engagement proposals')])
    save(page_path, title, description, body, [f] + [by_slug[x] for x in peers])

guides = [
    ('tax-strategy-accounting-cfo-firms', 'Tax Strategy, Accounting & CFO Firms: Which Scope Fits?', ['dark-horse-cpas','pillar-advisors','graphite-financial','incite-tax','peter-holtz-cpa','anomaly-cpa'], 'Monthly books and management reporting can be the foundation of a tax plan. Before buying an outsourced finance package, define whether you need cleanup, recurring close, forecasts, a CFO, or a specific tax project. These are different jobs, with different fees and professional responsibilities.', 'A profitable founder with an existing controller may only need tax strategy. A company preparing for fundraising may need accrual accounting, board reporting, and forecasting as well. An owner with rentals may need personal and entity planning across the operating company and property portfolio. Compare the tax engagement and accounting scope separately.'),
    ('tax-planning-implementation-firms', 'Tax Planning Implementation Firms: Compare Who Does the Work', ['tax-strategists-of-america','tax-goddess','tax-alchemy','proactive-tax-advisors','gelt','keystone-cpa'], 'A useful tax plan identifies the decision, deadline, records, and person responsible for execution. Providers differ in whether they implement directly, coordinate outside professionals, hand instructions to an existing accountant, or offer different levels of support.', 'Keeping a trusted preparer can work if the strategist supplies records and the preparer reviews the proposed treatment. A coordinated planning and filing engagement can reduce handoffs, but still needs explicit responsibility for payroll, legal documents, elections, and property studies. Ask how unresolved assumptions are addressed before filing.'),
    ('physician-business-real-estate-tax-advisors', 'Tax Advisors for Physicians With Businesses & Rental Property', ['cerebral-tax-advisors','taxstra','hall-cpa','keystone-cpa','advise-re','benficial-cpa'], 'Physicians with business or rental income need more than a comparison of personal return prices. A hospital employee with investments, a locum contractor, and an owner of a medical practice have different planning needs. Select the firm that can coordinate the relevant income and ownership structures.', 'A W-2 physician considering a rental should ask who models income and investment outcomes before purchase. A locum contractor should compare compensation, retirement, estimated payments, and entity costs. A practice owner may also need payroll, accounting, and an eventual sale plan. Request a scope tied to the actual decision, not a generic promise of savings.'),
]
for slug, title, members, intro, scenario in guides:
    page_path = '/compare/' + slug + '/'
    description = 'Compare relevant firms by client situation, tax planning scope, implementation, and ongoing support. Includes official sources and AE Tax Advisors.'
    body = T.page_header(h1=title, subtitle=description, trail=[('Home', '/'), ('Compare firms', '/compare/'), (title, page_path)])
    body += T.section('Define the engagement first', p(intro) + p(scenario) + '<p>AE Tax Advisors publishes this guide as a competing provider. Firm inclusion reflects service overlap, not an independent ranking. Profiles checked October 1, 2026.</p>')
    for slug in members:
        f = by_slug[slug]
        body += T.section(E(f['name']), p(f['fit']) + p(f['question']) + '<p><a href="' + path(f) + '">Read the sourced service comparison</a> · <a href="' + E(f['source']) + '" rel="external noopener">Official website</a></p>')
    body += T.section('Where AE Tax Advisors fits', '<p>AE focuses on profitable business owners, real estate investors, and situations combining the two. Compare its written planning, prior-year review, amendments, studies, and return work with the exact proposal from another firm. Standard advisory is $7,800; complex advisory is $9,800. Preparation and other services are separate. <a href="/pricing/">Read pricing</a> and <a href="/bios/">meet the advisory team</a>.</p>')
    body += T.related_section([(HUB, 'Tax planning firm directory'), ('/tools/tax-advisor-engagement-scorecard/', 'Engagement comparison scorecard'), ('/compare/tax-advisor-comparison-methodology/', 'Comparison methodology')])
    save(page_path, title, description, body, [by_slug[x] for x in members])

# Make all profiles discoverable from the established comparison hub.
hub = ROOT / 'compare/index.html'
text = hub.read_text()
text = re.sub(r'<section class="content-section" id="tax-planning-firm-directory">.*?</section>', '', text, flags=re.S)
listing = '<section class="content-section" id="tax-planning-firm-directory"><div class="container narrow"><h2>Tax planning firms for business owners and real estate investors</h2><p>Explore sourced firm profiles, service scope, and client fit. These comparisons cover personalized advisory, implementation, and accounting services.</p><p><a href="' + HUB + '">Find a tax planning firm by your situation</a></p><ul class="related-links">' + ''.join('<li><a href="' + path(f) + '">' + E(f['name']) + ': services and AE comparison</a></li>' for f in FIRMS) + '</ul><p><a href="/compare/tax-strategy-accounting-cfo-firms/">Tax strategy with accounting and CFO support</a> · <a href="/compare/tax-planning-implementation-firms/">Implementation models</a> · <a href="/compare/physician-business-real-estate-tax-advisors/">Physician planning</a></p></div></section>'
header = re.search(r'<section class="page-header">.*?</section>', text, re.S)
assert header
text = text[:header.end()] + listing + text[header.end():]
hub.write_text(text)
CHANGED.append('/compare/')

# Existing alternatives remain intact, with a crawlable link to the firm profile.
for f in FIRMS:
    alt = ROOT / 'compare' / (f['slug'] + '-alternatives') / 'index.html'
    if not alt.exists() or f['slug'] in shortlists:
        continue
    text = alt.read_text()
    if 'id="firm-name-overview-link"' not in text:
        text = text.replace('</main>', '<section class="content-section" id="firm-name-overview-link"><div class="container narrow"><h2>Research ' + E(f['name']) + ' before comparing alternatives</h2><p><a href="' + path(f) + '">Read the firm overview, services, pricing questions, and comparison with AE Tax Advisors</a>.</p></div></section></main>', 1)
        alt.write_text(text)
        CHANGED.append('/compare/' + f['slug'] + '-alternatives/')

# Targeted XML edits preserve unrelated dates, ordering, and sitemap partitions.
for filename in ['sitemap.xml', 'sitemap-comparisons.xml']:
    target = ROOT / filename
    text = target.read_text()
    for page_path in sorted(set(CHANGED)):
        url = T.SITE + page_path
        block = re.search(r'<url>\s*<loc>' + re.escape(url) + r'</loc>.*?</url>', text, re.S)
        if block:
            updated = re.sub(r'<lastmod>.*?</lastmod>', '<lastmod>' + DATE + '</lastmod>', block[0])
            text = text[:block.start()] + updated + text[block.end():]
        else:
            text = text.replace('</urlset>', '  <url><loc>' + url + '</loc><lastmod>' + DATE + '</lastmod></url>\n</urlset>')
    target.write_text(text)

manifest = {'date': DATE, 'firm_count': len(FIRMS), 'pages': sorted(set(CHANGED)), 'firms': [{'name': f['name'], 'path': path(f), 'source': f['source'], 'category': f['category']} for f in FIRMS]}
(ROOT / 'scripts/competitor_name_search_manifest_20261001.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'firms': len(FIRMS), 'changed_pages': len(set(CHANGED))}, indent=2))
