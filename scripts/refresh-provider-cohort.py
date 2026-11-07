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
if len(sys.argv) != 2 or not re.fullmatch(r'[a-z0-9-]+', sys.argv[1]):
    raise SystemExit('Usage: refresh-provider-cohort.py COHORT_DIRECTORY_NAME')
DATA = ROOT / 'content' / sys.argv[1]
config = json.loads((DATA / 'cohort.json').read_text())
DATE = config.get('date', DATE)
from datetime import date
REVIEW_DATE = date.fromisoformat(DATE).strftime('%B %-d, %Y')
STUDY = config.get('mode') == 'costseg'
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
if STUDY:
    AE_SCOPE = 'AE offers standalone cost segregation studies at $1 per square foot, with a $2,000 minimum per study. AE Tax Advisors provides tax planning for business owners and real estate investors as a separate service. Advisory, return preparation, amendments and other implementation work are separately scoped and priced.'
    AE_TERMS = 'Request a property-specific study quote and identify the report deliverables, preparer handoff and audit-support terms. Confirm any Form 3115 preparation and return filing separately; a study fee is not an all-inclusive tax engagement.'

def disclosure():
    return p(f'Published by AE Tax Advisors, a competing service provider. This is a commercial comparison of public service information, not an independent ranking or firsthand customer review. Sources checked {REVIEW_DATE}; confirm current availability and fees directly.')

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
    return T.section('Official sources and research date', p('Service descriptions are attributed to the linked provider websites. AE has not independently verified advertised savings, customer outcomes or service delivery. A public service menu does not establish the contents of your engagement.') + '<ul>' + ''.join('<li>' + link(u, label) + '</li>' for u, label in dict(items).items()) + '</ul>' + p(f'Researched {REVIEW_DATE} by AE Tax Advisors. No customer star rating or universal winner is assigned.'))

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
    schemas = [T.article_schema(title=title, description=desc, url=T.SITE + path, published=published, modified=DATE, section='Cost segregation comparisons' if STUDY else 'Tax advisor comparisons', citations=citations), T.breadcrumb_schema(trail)]
    if faqs:
        body += T.faq_section([(E(q), p(a)) for q, a in faqs])
        schemas.append(T.faq_schema([(q, p(a)) for q, a in faqs]))
    body += sources(slugs)
    body += T.related_section([(route(s, k), providers[s]['name'] + label) for s in slugs for k, label in [('alternative', ' alternatives'), ('pricing', ' pricing'), ('comparison', ' vs AE Tax Advisors')]] + [('/compare/', 'Browse tax advisor comparisons'), ('/pricing/', 'AE service pricing'), ('/case-studies/', 'AE case studies and their limitations')])
    doc = T.build_page(title=title + ' | AE Tax Advisors', description=desc, path=path, body=head + body, schemas=schemas, published=published, modified=DATE, active_nav='/compare/', extra_head='<link rel="stylesheet" href="/assets/competitor-pricing.css?v=20261024">\n<script defer src="/assets/booking-events.js"></script>')
    if STUDY:
        doc = re.sub(r'(<main\b[^>]*>)(.*?)(</main>)', lambda m: m[1] + m[2].replace('href="/discovery/"', 'href="/cost-seg-discovery/"').replace('>Book a Call<', '>Book a Cost Seg Discovery Call<') + m[3], doc, count=1, flags=re.S)
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(doc)
    written.append(path)

def common_request(d):
    records = ('Give each firm the same property address, square footage, closing statement, placed-in-service date, improvement records and existing depreciation schedules. Identify the owner entity, return preparer and deadline. Request a written scope for inspection, engineering analysis, report schedules, support and separately billed implementation. Send sensitive records through the firm’s secure intake process.' if STUDY else 'Give shortlisted firms the same entity list, current financials, prior returns, property schedule and next decision date. Request a written work plan identifying each deliverable, assigned professional, client dependency, implementation deadline and separately billed service. Send sensitive records through the firm’s secure intake process.')
    return T.section('Ask for a proposal you can compare', ul(d['questions']) + p(records))

for s, d in providers.items():
    n = d['name']
    peers = d['peers']
    shortlist = [('AE Tax Advisors', 'Standalone property studies with separately scoped tax planning and return implementation.' if STUDY else 'Business-owner and rental-property planning with a defined advisory engagement; separately priced filing and study work.', '/pricing/', 'AE service scope')]
    shortlist += [(providers[x]['name'], providers[x]['fit'], providers[x]['sources'][0][0], 'Official service information') for x in peers]
    body = T.section('Which ' + E(n) + ' alternative fits your needs?', p(d['alternative_intro']) + disclosure() + p(AE_SCOPE) + table(('Option', 'When to evaluate it', 'Evidence'), [(E(name), E(fit), link(url, label)) for name, fit, url, label in shortlist]))
    body += T.section('When to keep ' + E(n) + ' on your shortlist', p(d['keep']) + '<p>' + link(d['sources'][0][0], 'Read the provider’s own description') + '. ' + E(d['boundary']) + '</p>').replace('<section ', '<section id="provider-review" ', 1)
    body += T.section('A situation worth comparing', p(d['scenario']) + p(d['decision']))
    scope_note = ('A software report, an engineering study and a tax advisory engagement buy different work. Compare inspection method, report detail, travel, CPA questions, support and any separately priced Form 3115 or return work.' if STUDY else 'A planning fee, a recurring membership and a full accounting relationship buy different work. Add filing, amendments, studies, legal work and future support to the same scope before comparing totals.')
    body += T.section('Compare total cost before switching', '<p>' + link(route(s, 'pricing'), n + ' pricing and quote checklist') + '. ' + E(scope_note) + '</p>' + p(AE_TERMS))
    body += common_request(d)
    body += T.section('Research customer reviews separately', p('If you are searching for ' + n + ' reviews, check the exact business identity, review date, purchased service and original platform. Ask for relevant references and a redacted sample deliverable. Testimonials do not establish the technical scope of your proposal. This alternatives guide does not verify customer experiences.'))
    alt_desc = ('Compare ' + n + ' alternatives by study method, property fit, fees, CPA handoff and audit support. Review AE’s standalone study scope.' if STUDY else 'Compare ' + n + ' alternatives by client fit, planning, implementation and filing. Review sourced differences and AE Tax Advisors’ advisory scope.')
    save(route(s, 'alternative'), n + ' Alternatives: Compare Services and Fit', alt_desc, body, [s] + peers, [(f'What are the alternatives to {n}?', 'Consider AE Tax Advisors, ' + ', '.join(providers[x]['name'] for x in peers) + '. Match the selection to the work you need; the list is not an independent ranking.'), (f'Can I switch from {n} to AE Tax Advisors?', 'Discuss whether AE accepts your required scope and deadlines before ending an engagement. Arrange the secure transfer of returns, books, depreciation records and unfinished work. Check cancellation and renewal terms with your current firm.')], 'alternative')

    body = T.section('What does ' + E(n) + ' cost?', p(d['fee']) + p(d['fee_context']) + disclosure())
    body = body.replace('<section ', '<section id="competitor-price-review" ', 1)
    body += T.section('Separate the services in your quote', table(('Cost component', 'What to verify'), [(E(label), E(text)) for label, text in d['cost_rows']]))
    body += T.section('Compare ' + E(n) + ' fees with AE’s scope', p(AE_SCOPE) + p(AE_TERMS) + p(d['price_comparison']) + '<p>' + link('/pricing/', 'See current AE pricing') + ' · ' + link(route(s, 'comparison'), n + ' vs AE Tax Advisors') + '</p>')
    body += T.section('A fee comparison using your records', p(d['scenario']) + p('Build two complete quotes for the same property and service scope. Separate study fees from travel, additional buildings, expedited work, audit support and return implementation. A software price is not an engineering-study quote. Lower cost or a larger preliminary deduction estimate alone does not establish a better fit.' if STUDY else 'Build two complete quotes for that same situation. Do not subtract a planning-only price from a package that includes different work. Identify first-year charges, required companion services, optional work, renewal choices and the date by which notice must be given. Lower cost alone does not establish a better fit or a larger tax benefit.'))
    if STUDY:
        body += T.section('AE study-price examples', table(('Square footage', 'Published-rate arithmetic'), [('1,500 square feet', '$2,000 minimum study price.'), ('3,000 square feet', '$3,000 study price at $1 per square foot.')]) + p('These are arithmetic examples using AE’s published rate, not quotes for a particular property or estimates of tax savings. Confirm the covered area and study scope. Return preparation, amendments, advisory and other work are separately priced.'))
    body += common_request(d)
    price_title = n + (' Pricing: Study Fees and Scope' if STUDY else ' Pricing: Fees, Scope and Renewal')
    price_desc = ('Review ' + n + ' study pricing, fee evidence, inspection scope and CPA handoff. Compare a matched property quote with AE’s published study rate.' if STUDY else 'Review ' + n + ' pricing evidence, scope exclusions and renewal questions. Compare complete engagement costs with AE Tax Advisors’ published fees.')
    save(route(s, 'pricing'), price_title, price_desc, body, [s], [(f'Are {n} fees publicly available?', d['fee']), (f'Does the {n} fee include filing and implementation?', d['filing_answer'])], 'pricing')

    body = T.section('The practical difference', p(d['vs_intro']) + p(AE_SCOPE) + disclosure())
    body += T.section('Compare the engagement', table(('Decision', n, 'AE Tax Advisors'), [(E('Public model'), E(d['summary']), 'A standalone cost segregation study, with advisory and return work separately scoped.' if STUDY else 'A defined tax advisory engagement for business owners and real estate investors.'), (E('Implementation and filing'), E(d['filing_answer']), 'Agree on the professional responsible for each task. Returns, amendments, studies and additional work have separate scopes and prices.'), (E('Fees and support' if STUDY else 'Fees and future support'), link(route(s, 'pricing'), 'See sourced fees and scope questions'), E('$1 per square foot, $2,000 minimum per study. Confirm inspection, support and separately scoped tax work.' if STUDY else '$7,800 standard; $9,800 complex advisory. No required standard annual planning renewal; support is limited to the agreed period.')), (E('Key buying question'), E(d['questions'][0]), E(d['ae_question']))]))
    body += T.section('Choose ' + E(n) + ' when its proposal matches these needs', p(d['keep']))
    body += T.section('Consider AE for this situation', p(d['scenario']) + p(d['decision']) + p('AE can scope a standalone study and discuss separately contracted advisory or return work. Retain your existing preparer when that arrangement fits, and agree on the report handoff before work begins. Neither provider is the universal choice. A discovery call determines potential fit; detailed analysis follows an agreed engagement.' if STUDY else 'AE can discuss planning across the operating business, owner income and real estate. Confirm prior-year review, implementation and affected returns in the proposal. Neither provider is the universal choice. A discovery call determines potential fit; detailed analysis follows an agreed engagement.'))
    body += common_request(d)
    vs_desc = ('Compare ' + n + ' vs AE Tax Advisors on study method, pricing, CPA coordination and support. Separate the study from return implementation.' if STUDY else 'Compare ' + n + ' vs AE Tax Advisors on planning, implementation, filing, fees and support. Choose using sourced services and matching proposals.')
    save(route(s, 'comparison'), n + ' vs AE Tax Advisors: Services and Fees', vs_desc, body, [s], [(f'Is {n} or AE Tax Advisors a better fit?', d['decision']), ('Can I keep my existing tax preparer?', 'Ask how the study report and schedules will be delivered to your preparer. Identify who evaluates any accounting-method change, prepares required forms, signs the return and handles follow-up questions. AE’s responsibilities depend on the agreed scope.' if STUDY else 'Ask each firm whether its proposed planning engagement permits coordination with your current preparer. Identify who signs the return, implements recommendations and checks completion. AE’s responsibilities depend on the agreed scope.')], 'comparison')

# Researched comparisons chosen for actual overlap in buyer needs.
pairs = config['pairs']
for left, right, slug, scenario, question in pairs:
    l, r = providers[left], providers[right]
    title = l['name'] + ' vs ' + r['name'] + ': Services and Scope'
    body = T.section('Start with the decision you need to make', p(scenario) + disclosure())
    body += T.section('What to compare', table(('Provider', 'Public service focus', 'Research the proposal'), [(E(d['name']), E(d['fit']), link(route(s, 'pricing'), 'Fees and quote questions')) for s, d in [(left, l), (right, r)]]))
    checklist = ['Price the same property, owner entity, buildings, improvements and study year.', 'Confirm inspection method, engineering review, report schedules and support.', 'Identify who answers CPA questions and who handles any Form 3115 or return implementation.', 'Separate the study price, travel, added buildings, deadline charges and additional tax work.'] if STUDY else ['List each entity, owner return, property and tax year covered.', 'Identify the written deliverable, responsible professional and client dependencies.', 'Separate advice, implementation, legal documents, studies, filing and future support.', 'Compare initial fees, required companion services, cancellation dates and renewal choices.']
    body += T.section('Ask both firms the same question', '<blockquote>' + p(question) + '</blockquote>' + ul(checklist))
    evaluation = ('Ask each firm to walk through a redacted report for a comparable property: the records used, inspection evidence, reconciliation to the property’s supported basis, component-level schedules and the package supplied to the accountant. Ask who explains an allocation when the preparer has a question. A preliminary estimate is not a completed report or confirmation that the owner can use the deductions.' if STUDY else 'Ask each firm to walk through one recommendation using your records: the decision being modeled, alternatives considered, assumptions, implementation steps, deadline and evidence that the work is complete. A verbal strategy discussion and a prepared filing are different deliverables. Ask where each appears in the quote.')
    body += T.section('A practical way to evaluate the answers', p(evaluation) + p('Retain the provider that can meet your actual requirements, including work already in progress. A change of firm needs a handover plan for records, upcoming payments, filing deadlines and outstanding tasks. Do not infer that a service is unavailable merely because it is not described on the public page reviewed.'))
    positioning = ('AE publishes this comparison and also supplies cost segregation services. If you want a third proposal, ask AE to quote the same property and report scope. Its published study rate is a starting comparison point, not evidence that all three engagements include identical services or support.' if STUDY else 'AE publishes this comparison and also competes for tax advisory work. If you want a third proposal, ask AE to address the same facts and responsibilities. The published advisory fee is a starting comparison point, not a statement that all three engagements include identical work.')
    body += T.section('Where AE Tax Advisors fits', p(AE_SCOPE) + p(AE_TERMS) + p(positioning))
    save('/compare/' + slug + '/', title, 'Compare ' + l['name'] + ' and ' + r['name'] + ' on client fit, services, implementation and complete fees. Published by AE Tax Advisors.', body, [left, right])

# Add crawlable reciprocal links to the new comparison options and relevant service hubs.
pair_links = [('/compare/' + slug + '/', providers[l]['name'] + ' vs ' + providers[r]['name']) for l, r, slug, _, _ in pairs]
for s in providers:
    local = [(path, label) for path, label in pair_links if s in path]
    for intent in ('alternative', 'pricing', 'comparison'):
        f = ROOT / route(s, intent).strip('/') / 'index.html'
        text = f.read_text()
        anchor = T.CTA_BLOCK.replace('href="/discovery/"', 'href="/cost-seg-discovery/"').replace('>Book a Call<', '>Book a Cost Seg Discovery Call<') if STUDY else T.CTA_BLOCK
        text = text.replace(anchor, T.related_section(local, 'Compare other firms on your shortlist') + anchor, 1)
        f.write_text(text)

hub_links = [(route(s, 'alternative'), d['name'] + ' alternatives') for s, d in providers.items()] + pair_links
for path in config['hub_routes']:
    f = ROOT / path.strip('/') / 'index.html'
    text = f.read_text()
    marker = '<!-- ' + config['marker'] + ':start -->'
    text = re.sub(re.escape(marker) + r'.*?<!-- ' + re.escape(config['marker']) + ':end -->', '', text, flags=re.S)
    body = p('Choosing a cost segregation provider? Compare study method, property fit, report support and the handoff to your preparer. Separate the study fee from additional tax work. AE publishes these commercial comparisons and also supplies studies.' if STUDY else 'Choosing a tax planning firm? Compare the service model, full project cost and who completes the work. AE Tax Advisors publishes these commercial guides and also offers advisory services.')
    body += '<ul>' + ''.join('<li>' + link(u, label) + '</li>' for u, label in hub_links) + '</ul>'
    block = marker + T.section('Compare cost segregation providers by study scope' if STUDY else 'Compare tax advisory firms by the work you need', body) + '<!-- ' + config['marker'] + ':end -->'
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
                   kind='published' if s in config['published'] else 'quote',
                   status=d.get('price_status', 'Published program fees — confirm scope' if s in config['published'] else 'Current quote required'))
        for key in ('estimateBasis', 'benchmarkSources', 'estimateCategory'):
            row.pop(key, None)
directory.setdefault('cohortReviewed', {}).update({s: DATE for s in providers})
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
text = re.sub(r'\d+ providers:.*?(?:Every row shows a numeric cost and its evidence type\.|a benchmark estimate is not the named provider’s fee\.)', f'{len(directory["providers"])} providers: {published} with sourced published prices, {estimates} with labeled AE comparable-work estimates and {quotes} requiring a current quote. Read each row’s evidence type; a benchmark estimate is not the named provider’s fee.', text, count=1, flags=re.S)
if 'tax-alchemy' in providers:
    text = re.sub(r'<article><h3>Tax Alchemy</h3>.*?</article>', '<article><h3>Tax Alchemy</h3><p class="pricing-fee">$20,000–$150,000</p><p>Official FAQ advisory range, checked November 6, 2026. Confirm included implementation and filing.</p>' + link(route('tax-alchemy', 'pricing'), 'Review current fee evidence') + '</article>', text, count=1, flags=re.S)
text = text.replace('<option value="">All prices and estimates</option>', '<option value="">All evidence types</option>')
if '<option value="quote">' not in text:
    text = text.replace('<option value="estimate">AE budget estimates</option>', '<option value="estimate">AE budget estimates</option><option value="quote">Current quote required</option>')
text = text.replace('All amounts are USD.', 'All amounts are USD. Selected provider cohorts were separately researched November 6, 2026.', 1) if 'provider cohort' not in text else text
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
print(json.dumps({'pages': len(written), 'new_comparisons': config['new_comparisons'], 'optimized_provider_pages': 3 * len(providers), 'refreshed_pair_comparisons': config['refreshed_pair_comparisons'], 'discovery_hubs': len(config['hub_routes'])}))
