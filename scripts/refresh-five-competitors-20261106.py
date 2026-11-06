#!/usr/bin/env python3
"""Publish the researched five-provider cohort without regenerating other providers."""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import site_template as T

DATE = '2026-11-06'
E = html.escape
DATA = ROOT / 'content/five-competitors-20261106'
providers = json.loads((DATA / 'sources.json').read_text())
ownership = {r['slug']: r for r in json.loads((ROOT / 'content/provider-page-ownership-20261024.json').read_text())['providers']}
written = []

def p(text):
    return '<p>' + E(text) + '</p>'

def link(url, text):
    return '<a href="' + E(url, quote=True) + '">' + E(text) + '</a>'

def ul(items):
    return '<ul>' + ''.join('<li>' + E(i) + '</li>' for i in items) + '</ul>'

def table(headers, rows):
    return '<div class="pricing-table-scroll" role="region" aria-label="Compare engagement scope" tabindex="0"><table><thead><tr>' + ''.join('<th scope="col">' + E(h) + '</th>' for h in headers) + '</tr></thead><tbody>' + ''.join('<tr><th scope="row">' + row[0] + '</th>' + ''.join('<td>' + cell + '</td>' for cell in row[1:]) + '</tr>' for row in rows) + '</tbody></table></div>'

def route(s, intent):
    return ownership[s][intent + '_url'].removeprefix(T.SITE)

AE_SCOPE = 'AE Tax Advisors provides tax planning for business owners and real estate investors. Standard advisory is $7,800 and complex advisory is $9,800. Returns, amendments, cost segregation and additional work are separately scoped and priced.'
AE_TERMS = 'The standard advisory engagement has no required annual planning renewal. Confirm the support period, implementation assignments and exclusions in the written agreement; future work can require a new engagement.'

def disclosure():
    return p('Published by AE Tax Advisors, a competing service provider. This is a commercial comparison of public service information, not an independent ranking or firsthand customer review. Sources checked November 6, 2026; confirm current availability and fees directly.')

def nav(s, intent):
    return '<nav class="provider-guide-nav container narrow" aria-label="' + E(providers[s]['name']) + ' guides">' + ''.join('<a href="' + route(s, k) + '"' + (' aria-current="page"' if k == intent else '') + '>' + label + '</a>' for k, label in [('pricing', 'Pricing and fees'), ('alternative', 'Alternatives'), ('comparison', 'Compare with AE')]) + '</nav>'

def sources(slugs):
    items = []
    for s in slugs:
        d = providers[s]
        items.extend((u, d['name'] + ' — ' + label) for u, label in d['sources'])
        # Preserve the directory's established official-source link.
        items.append((ownership[s]['official_source'], d['name'] + ' directory source'))
    items += [(T.SITE + '/pricing/', 'AE fees and scope'), (T.SITE + '/compare/tax-advisor-comparison-methodology/', 'AE comparison methodology')]
    return T.section('Official sources and research date', p('Service descriptions are attributed to the linked provider websites. AE has not independently verified advertised savings, customer outcomes or service delivery. A public service menu does not establish the contents of your engagement.') + '<ul>' + ''.join('<li>' + link(u, label) + '</li>' for u, label in dict(items).items()) + '</ul>' + p('Researched November 6, 2026 by AE Tax Advisors. No customer star rating or universal winner is assigned.'))

def save(path, title, desc, body, slugs, faqs=None, intent=None):
    file = ROOT / path.strip('/') / 'index.html'
    old = file.read_text() if file.exists() else ''
    m = re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})', old)
    published = m[1] if m else DATE
    trail = [('Home', '/'), ('Compare firms', '/compare/'), (title, path)]
    head = T.page_header(h1=E(title), subtitle=E(desc), trail=trail)
    if intent:
        head += nav(slugs[0], intent)
    citations = list(dict.fromkeys(u for s in slugs for u, _ in providers[s]['sources'])) + [T.SITE + '/pricing/']
    schemas = [T.article_schema(title=title, description=desc, url=T.SITE + path, published=published, modified=DATE, section='Tax advisor comparisons', citations=citations), T.breadcrumb_schema(trail)]
    if faqs:
        body += T.faq_section([(E(q), p(a)) for q, a in faqs])
        schemas.append(T.faq_schema([(q, p(a)) for q, a in faqs]))
    body += sources(slugs)
    body += T.related_section([(route(s, k), providers[s]['name'] + label) for s in slugs for k, label in [('alternative', ' alternatives'), ('pricing', ' pricing'), ('comparison', ' vs AE Tax Advisors')]] + [('/compare/', 'Browse tax advisor comparisons'), ('/pricing/', 'AE service pricing'), ('/case-studies/', 'AE case studies and their limitations')])
    doc = T.build_page(title=title + ' | AE Tax Advisors', description=desc, path=path, body=head + body, schemas=schemas, published=published, modified=DATE, active_nav='/compare/', extra_head='<link rel="stylesheet" href="/assets/competitor-pricing.css?v=20261024">')
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(doc)
    written.append(path)

def common_request(d):
    return T.section('Ask for a proposal you can compare', ul(d['questions']) + p('Give shortlisted firms the same entity list, current financials, prior returns, property schedule and next decision date. Request a written work plan identifying each deliverable, assigned professional, client dependency, implementation deadline and separately billed service. Send sensitive records through the firm’s secure intake process.'))

for s, d in providers.items():
    n = d['name']
    peers = d['peers']
    shortlist = [('AE Tax Advisors', 'Business-owner and rental-property planning with a defined advisory engagement; separately priced filing and study work.', '/pricing/', 'AE service scope')]
    shortlist += [(providers[x]['name'], providers[x]['fit'], providers[x]['sources'][0][0], 'Official service information') for x in peers]
    body = T.section('Which ' + E(n) + ' alternative fits your needs?', p(d['alternative_intro']) + disclosure() + p(AE_SCOPE) + table(('Option', 'When to evaluate it', 'Evidence'), [(E(name), E(fit), link(url, label)) for name, fit, url, label in shortlist]))
    body += T.section('When to keep ' + E(n) + ' on your shortlist', p(d['keep']) + '<p>' + link(d['sources'][0][0], 'Read the provider’s own description') + '. ' + E(d['boundary']) + '</p>').replace('<section ', '<section id="provider-review" ', 1)
    body += T.section('A situation worth comparing', p(d['scenario']) + p(d['decision']))
    body += T.section('Compare total cost before switching', '<p>' + link(route(s, 'pricing'), n + ' pricing and quote checklist') + '. ' + E('A planning fee, a recurring membership and a full accounting relationship buy different work. Add filing, amendments, studies, legal work and future support to the same scope before comparing totals.') + '</p>' + p(AE_TERMS))
    body += common_request(d)
    body += T.section('Research customer reviews separately', p('If you are searching for ' + n + ' reviews, check the exact business identity, review date, purchased service and original platform. Ask for relevant references and a redacted sample deliverable. Testimonials do not establish the technical scope of your proposal. This alternatives guide does not verify customer experiences.'))
    save(route(s, 'alternative'), n + ' Alternatives: Compare Services and Fit', 'Compare ' + n + ' alternatives by client fit, planning, implementation and filing. Review sourced differences and AE Tax Advisors’ advisory scope.', body, [s] + peers, [(f'What are the alternatives to {n}?', 'Consider AE Tax Advisors, ' + ', '.join(providers[x]['name'] for x in peers) + '. Match the selection to the work you need; the list is not an independent ranking.'), (f'Can I switch from {n} to AE Tax Advisors?', 'Discuss whether AE accepts your required scope and deadlines before ending an engagement. Arrange the secure transfer of returns, books, depreciation records and unfinished work. Check cancellation and renewal terms with your current firm.')], 'alternative')

    body = T.section('What does ' + E(n) + ' cost?', p(d['fee']) + p(d['fee_context']) + disclosure())
    body = body.replace('<section ', '<section id="competitor-price-review" ', 1)
    body += T.section('Separate the services in your quote', table(('Cost component', 'What to verify'), [(E(label), E(text)) for label, text in d['cost_rows']]))
    body += T.section('Compare ' + E(n) + ' fees with AE’s scope', p(AE_SCOPE) + p(AE_TERMS) + p(d['price_comparison']) + '<p>' + link('/pricing/', 'See current AE pricing') + ' · ' + link(route(s, 'comparison'), n + ' vs AE Tax Advisors') + '</p>')
    body += T.section('A fee comparison using your records', p(d['scenario']) + p('Build two complete quotes for that same situation. Do not subtract a planning-only price from a package that includes different work. Identify first-year charges, required companion services, optional work, renewal choices and the date by which notice must be given. Lower cost alone does not establish a better fit or a larger tax benefit.'))
    body += common_request(d)
    save(route(s, 'pricing'), n + ' Pricing: Fees, Scope and Renewal', 'Review ' + n + ' pricing evidence, scope exclusions and renewal questions. Compare complete engagement costs with AE Tax Advisors’ published fees.', body, [s], [(f'Are {n} fees publicly available?', d['fee']), (f'Does the {n} fee include filing and implementation?', d['filing_answer'])], 'pricing')

    body = T.section('The practical difference', p(d['vs_intro']) + p(AE_SCOPE) + disclosure())
    body += T.section('Compare the engagement', table(('Decision', n, 'AE Tax Advisors'), [(E('Public model'), E(d['summary']), 'A defined tax advisory engagement for business owners and real estate investors.'), (E('Implementation and filing'), E(d['filing_answer']), 'Agree on the professional responsible for each task. Returns, amendments, studies and additional work have separate scopes and prices.'), (E('Fees and future support'), link(route(s, 'pricing'), 'See sourced pricing and renewal questions'), E('$7,800 standard; $9,800 complex advisory. No required standard annual planning renewal; support is limited to the agreed period.')), (E('Key buying question'), E(d['questions'][0]), E(d['ae_question']))]))
    body += T.section('Choose ' + E(n) + ' when its proposal matches these needs', p(d['keep']))
    body += T.section('Consider AE for this situation', p(d['scenario']) + p(d['decision']) + p('AE can discuss planning across the operating business, owner income and real estate. Confirm prior-year review, implementation and affected returns in the proposal. Neither provider is the universal choice. A discovery call determines potential fit; detailed analysis follows an agreed engagement.'))
    body += common_request(d)
    save(route(s, 'comparison'), n + ' vs AE Tax Advisors: Services and Fees', 'Compare ' + n + ' vs AE Tax Advisors on planning, implementation, filing, fees and support. Choose using sourced services and matching proposals.', body, [s], [(f'Is {n} or AE Tax Advisors a better fit?', d['decision']), ('Can I keep my existing tax preparer?', 'Ask each firm whether its proposed planning engagement permits coordination with your current preparer. Identify who signs the return, implements recommendations and checks completion. AE’s responsibilities depend on the agreed scope.')], 'comparison')

# Four missing comparisons and two existing comparisons with genuine buyer overlap.
pairs = [
 ('rainwater-cpa','keystone-cpa','rainwater-cpa-vs-keystone-cpa','Your company needs quarterly planning, and you also own rental property. Compare the company-level planning calendar with the property decisions and ask who combines them into the owner return.','Which projections will be updated during the year, and which property records and existing depreciation schedules will be reviewed?'),
 ('anderson-advisors','keystone-cpa','anderson-advisors-vs-keystone-cpa','You are buying another rental and have been advised to create an entity. Compare the legal ownership work with the tax analysis; they solve related but distinct problems.','Who reviews the legal structure, prepares any documents and determines how income and depreciation reach the tax return?'),
 ('rainwater-cpa','tax-goddess','rainwater-cpa-vs-tax-goddess','You run a profitable company and want more than an annual filing meeting. Compare a recurring review calendar with a strategy program, and make implementation assignments explicit.','Will the proposal deliver updated projections, a written strategy, implementation help, or a combination—and how will completion be checked?'),
 ('anderson-advisors','tax-alchemy','anderson-advisors-vs-tax-alchemy','You own several entities and need to decide whether your first purchase should be legal structuring or a tax advisory engagement. Separate the two scopes before comparing headline prices.','Which legal documents, tax recommendations, elections and returns will each licensed professional deliver?'),
 ('rainwater-cpa','tax-alchemy','rainwater-cpa-vs-tax-alchemy','You need a tax plan and want help putting it into practice. Compare the planning period, meeting schedule and filing arrangement using the same financial statements and entity list.','Does the agreement cover implementation, which returns are prepared, and what happens after the initial service period?'),
 ('tax-alchemy','tax-goddess','tax-alchemy-vs-tax-goddess','You are comparing two tax strategy programs and want a provider to help execute the recommendations. Compare the actual advisory program rather than an educational product or a different continuing-support tier.','Which program is being quoted, who performs implementation and filing, and what renews after the first year?'),
]
for left, right, slug, scenario, question in pairs:
    l, r = providers[left], providers[right]
    title = l['name'] + ' vs ' + r['name'] + ': Services and Scope'
    body = T.section('Start with the decision you need to make', p(scenario) + disclosure())
    body += T.section('What to compare', table(('Provider', 'Public service focus', 'Research the proposal'), [(E(d['name']), E(d['fit']), link(route(s, 'pricing'), 'Fees and quote questions')) for s, d in [(left, l), (right, r)]]))
    body += T.section('Ask both firms the same question', '<blockquote>' + p(question) + '</blockquote>' + ul(['List each entity, owner return, property and tax year covered.', 'Identify the written deliverable, responsible professional and client dependencies.', 'Separate advice, implementation, legal documents, studies, filing and future support.', 'Compare initial fees, required companion services, cancellation dates and renewal choices.']))
    body += T.section('A practical way to evaluate the answers', p('Ask each firm to walk through one recommendation using your records: the decision being modeled, alternatives considered, assumptions, implementation steps, deadline and evidence that the work is complete. A verbal strategy discussion and a prepared filing are different deliverables. Ask where each appears in the quote.') + p('Retain the provider that can meet your actual requirements, including work already in progress. A change of firm needs a handover plan for records, upcoming payments, filing deadlines and outstanding tasks. Do not infer that a service is unavailable merely because it is not described on the public page reviewed.'))
    body += T.section('Where AE Tax Advisors fits', p(AE_SCOPE) + p(AE_TERMS) + p('AE publishes this comparison and also competes for tax advisory work. If you want a third proposal, ask AE to address the same facts and responsibilities. The published advisory fee is a starting comparison point, not a statement that all three engagements include identical work.'))
    save('/compare/' + slug + '/', title, 'Compare ' + l['name'] + ' and ' + r['name'] + ' on client fit, services, implementation and complete fees. Published by AE Tax Advisors.', body, [left, right])

# Add crawlable reciprocal links to the new comparison options and relevant service hubs.
pair_links = [('/compare/' + slug + '/', providers[l]['name'] + ' vs ' + providers[r]['name']) for l, r, slug, _, _ in pairs]
for s in providers:
    local = [(path, label) for path, label in pair_links if s in path]
    for intent in ('alternative', 'pricing', 'comparison'):
        f = ROOT / route(s, intent).strip('/') / 'index.html'
        text = f.read_text()
        text = text.replace(T.CTA_BLOCK, T.related_section(local, 'Compare other firms on your shortlist') + T.CTA_BLOCK, 1)
        f.write_text(text)

hub_links = [(route(s, 'alternative'), d['name'] + ' alternatives') for s, d in providers.items()] + pair_links
for path in ('/compare/', '/compare/tax-planning-firms/', '/business-owner-small-business-tax/', '/real-estate-tax-planning/'):
    f = ROOT / path.strip('/') / 'index.html'
    text = f.read_text()
    marker = '<!-- five-competitor-discovery:start -->'
    text = re.sub(re.escape(marker) + r'.*?<!-- five-competitor-discovery:end -->', '', text, flags=re.S)
    body = p('Choosing a tax planning firm? Compare the service model, full project cost and who completes the work. AE Tax Advisors publishes these commercial guides and also offers advisory services.')
    body += '<ul>' + ''.join('<li>' + link(u, label) + '</li>' for u, label in hub_links) + '</ul>'
    block = marker + T.section('Compare tax advisory firms by the work you need', body) + '<!-- five-competitor-discovery:end -->'
    assert '</main>' in text, path
    f.write_text(text.replace('</main>', block + '</main>', 1))

# Keep the shared shopping directory consistent with these current reviews.
directory_file = ROOT / 'compare/competitor-pricing/prices.json'
directory = json.loads(directory_file.read_text())
vendor_file = ROOT / 'content/vendor-pricing-20261024.json'
vendors = json.loads(vendor_file.read_text())
for records in (directory['providers'], vendors):
    for row in records:
        s = row['slug']
        if s not in providers:
            continue
        d = providers[s]
        row.update(fee=d['fee'], qualification=d['fee_context'], reviewed=DATE,
                   source=d['sources'][0][0], additionalSources=[u for u, _ in d['sources'][1:]],
                   kind='published' if s in ('keystone-cpa', 'tax-alchemy') else 'quote',
                   status='Published program fees — confirm scope' if s in ('keystone-cpa', 'tax-alchemy') else 'Current quote required')
        for key in ('estimateBasis', 'benchmarkSources', 'estimateCategory'):
            row.pop(key, None)
directory['cohortReviewed'] = {s: DATE for s in providers}
directory_file.write_text(json.dumps(directory, indent=2, ensure_ascii=False) + '\n')
vendor_file.write_text(json.dumps(vendors, indent=2, ensure_ascii=False) + '\n')
directory_html = ROOT / 'compare/competitor-pricing/index.html'
text = directory_html.read_text()
for row in directory['providers']:
    s = row['slug']
    if s not in providers:
        continue
    path = route(s, 'pricing')
    pattern = r'<tr\b[^>]*>\s*<th scope="row"><a href="' + re.escape(path) + r'">.*?</tr>'
    replacement = '<tr data-provider="' + E(providers[s]['name'].lower(), quote=True) + '" data-kind="' + row['kind'] + '" data-category="' + row['category'] + '"><th scope="row">' + link(path, providers[s]['name'] + ' pricing') + '<br><small>' + link(route(s, 'alternative'), 'Alternatives') + ' · ' + link(route(s, 'comparison'), 'Compare with AE') + '</small></th><td>' + E(row['category']) + '</td><td>' + E(row['fee']) + '</td><td><strong>' + E(row['status']) + '</strong><br>' + link(path + '#competitor-price-review', 'Current sources and scope') + '</td></tr>'
    text, count = re.subn(pattern, lambda _: replacement, text, flags=re.S)
    assert count == 1, ('directory row', s, count)
published = sum(r['kind'] == 'published' for r in directory['providers'])
estimates = sum(r['kind'] == 'estimate' for r in directory['providers'])
quotes = sum(r['kind'] == 'quote' for r in directory['providers'])
text = re.sub(r'100 providers:.*?Every row shows a numeric cost and its evidence type\.', f'100 providers: {published} with sourced published prices, {estimates} with labeled AE comparable-work estimates and {quotes} requiring a current quote. Read each row’s evidence type; a benchmark estimate is not the named provider’s fee.', text, count=1, flags=re.S)
text = re.sub(r'<article><h3>Tax Alchemy</h3>.*?</article>', '<article><h3>Tax Alchemy</h3><p class="pricing-fee">$20,000–$150,000</p><p>Official FAQ advisory range, checked November 6, 2026. Confirm included implementation and filing.</p>' + link(route('tax-alchemy', 'pricing'), 'Review current fee evidence') + '</article>', text, count=1, flags=re.S)
text = text.replace('<option value="">All prices and estimates</option>', '<option value="">All evidence types</option>')
if '<option value="quote">' not in text:
    text = text.replace('<option value="estimate">AE budget estimates</option>', '<option value="estimate">AE budget estimates</option><option value="quote">Current quote required</option>')
text = text.replace('All amounts are USD.', 'All amounts are USD. The five-provider cohort was separately researched November 6, 2026.', 1) if 'The five-provider cohort' not in text else text
directory_html.write_text(text)

# Register new URLs in the already-discovered comparison sitemap, and date substantive changes.
sitemap = ROOT / 'sitemap-comparisons.xml'
xml = sitemap.read_text()
for path in written:
    url = T.SITE + path
    if '<loc>' + url + '</loc>' not in xml:
        xml = xml.replace('</urlset>', '<url><loc>' + url + '</loc><lastmod>' + DATE + '</lastmod></url>\n</urlset>')
sitemap.write_text(xml)
dates_file = ROOT / 'content/reviewed-content-lastmod.json'
dates = json.loads(dates_file.read_text())
dates.update({path: DATE for path in written})
dates_file.write_text(json.dumps(dates, indent=2) + '\n')
(DATA / 'pages.json').write_text(json.dumps(written, indent=2) + '\n')
for path in written:
    f = ROOT / path.strip('/') / 'index.html'
    f.write_text('\n'.join(line.rstrip() for line in f.read_text().splitlines()) + '\n')
print(json.dumps({'pages': len(written), 'new_comparisons': 4, 'optimized_provider_pages': 15, 'refreshed_pair_comparisons': 2, 'discovery_hubs': 4}))
