#!/usr/bin/env python3
"""Focused source/output checks for the two reviewed purchase and exit guides.

Run from the repository root; optionally pass a staged public directory.
These checks do not substitute for the production build or tax review.
"""
import json
import re
import sys
from decimal import Decimal
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

REPO = Path(__file__).resolve().parents[1]
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else REPO
MANIFEST = json.loads((REPO / 'scripts/purchase-exit-guide-routes-20261106.json').read_text())
DOMAIN = 'https://www.aetaxadvisors.com'
CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    assert condition, message


def plain(value):
    return ' '.join(unescape(re.sub(r'<[^>]+>', ' ', value)).split())


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.meta = {}
        self.canonicals = []
        self.ids = []
        self.h1s = 0
        self.stack = []
        self.balance_errors = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag not in {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}:
            self.stack.append(tag)
        attrs = dict(attrs)
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag == 'meta':
            self.meta[attrs.get('name', attrs.get('property'))] = attrs.get('content')
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs['href'])
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'h1':
            self.h1s += 1


    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.balance_errors.append((self.getpos(), tag))


def schema(html):
    return [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', html, re.S)]


holds = set(json.loads((REPO / 'discovery_review_holds.json').read_text()))
redirects = json.loads((REPO / 'scripts/content-consolidation.json').read_text()).get('redirects', {})
vercel = json.loads((REPO / 'vercel.json').read_text())
redirects.update({r['source']: r['destination'] for r in vercel.get('redirects', []) if ':' not in r['source']})


def resolve_route(route):
    seen = set()
    while route in redirects:
        check(route not in seen, 'Redirect cycle: ' + route)
        seen.add(route)
        route = redirects[route]
    return route


def link_file(url):
    path = urlsplit(url).path
    if path.endswith('/'):
        path += 'index.html'
    return ROOT / path.lstrip('/')


pages = {}
for entry in MANIFEST['routes']:
    route = entry['path']
    html = (ROOT / route.lstrip('/') / 'index.html').read_text()
    p = Page(html)
    docs = schema(html)
    check(not p.stack and not p.balance_errors, route + ': balanced HTML elements')
    article = [x for x in docs if x.get('@type') in ('Article', 'BlogPosting')]
    check(len(article) == 1, route + ': one article schema')
    a = article[0]
    check(p.canonicals == [DOMAIN + route], route + ': self-canonical')
    check(a['url'] == a['mainEntityOfPage']['@id'] == DOMAIN + route, route + ': schema URL parity')
    check(a['datePublished'] == entry['datePublished'], route + ': original publication date')
    check(a['dateModified'] == MANIFEST['reviewed'], route + ': modification date')
    check('Updated November 6, 2026' in html, route + ': visible review date')
    check('noindex' not in p.meta.get('robots', '').lower(), route + ': indexable')
    check(route not in holds and route not in redirects, route + ': active route')
    check(p.h1s == 1, route + ': one H1')
    h1 = plain(re.search(r'<h1[^>]*>(.*?)</h1>', html, re.S)[1])
    check(h1 == a['headline'], route + ': heading/schema headline parity')
    check(len(p.ids) == len(set(p.ids)), route + ': unique element IDs')
    title = plain(re.search(r'<title>(.*?)</title>', html, re.S)[1])
    check(title == p.meta['og:title'] == p.meta['twitter:title'], route + ': title parity')
    desc = p.meta['description']
    check(desc == p.meta['og:description'] == p.meta['twitter:description'] == a['description'], route + ': description parity')
    check(100 <= len(desc) <= 170 and desc.endswith('.'), route + ': complete, concise description')
    faq = [x for x in docs if x.get('@type') == 'FAQPage']
    check(len(faq) == 1, route + ': one FAQ schema')
    visible_faqs = re.findall(r'<div class="faq-item">\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>\s*</div>', html, re.S)
    expected = [(x['name'], x['acceptedAnswer']['text']) for x in faq[0]['mainEntity']]
    check([(plain(q), plain(answer)) for q, answer in visible_faqs] == expected, route + ': exact visible/schema FAQ parity')
    check(len(expected) >= 6, route + ': specific decision FAQs')
    check('/case-studies/' in p.links, route + ': existing case-study navigation preserved')
    for source in entry['sources']:
        check(source in p.links, route + ': primary source link ' + source)
    main = re.search(r'<main>(.*?)</main>', html, re.S)[1]
    for href in Page(main).links:
        u = urlsplit(href)
        if u.netloc and u.netloc != 'www.aetaxadvisors.com':
            continue
        if not u.path.startswith('/'):
            continue
        target = resolve_route(u.path)
        check(target not in holds, route + ': link not held: ' + target)
        check(link_file(target).is_file(), route + ': internal route exists: ' + target)
        if u.fragment:
            check(u.fragment in Page(link_file(target).read_text()).ids, route + ': internal fragment exists: ' + href)
    for private in ['Search Console', 'GSC observations', 'click-through rate', 'impression count', 'client-service issue']:
        check(private.lower() not in html.lower(), route + ': no private-research text')
    pages[route] = (html, plain(main))

seller, seller_text = pages['/blog/irc-1060-asset-classification-business-sellers/']
vehicle, vehicle_text = pages['/blog/section-179-vehicle-6000-pound-gvwr/']
fee = ('Published standard advisory pricing is $7,800, paid as two $3,900 installments 30 days apart, '
       'with no required recurring annual planning fee. Returns, amendments, cost segregation and '
       'additional services are separately scoped and priced. Confirm current fees and deliverables in the written engagement.')
check(fee in seller_text, 'Original standard fees and scope preserved verbatim')
check('Published on June 20, 2026' in seller and 'Published August 13, 2026' in vehicle, 'Original visible publication dates')
check(2 * 3900 == 7800, 'Fee installment arithmetic')
check('Class V: Equipment, Vehicles, Land and Buildings' in seller_text, 'Class V includes real property')
check('does not, by itself, determine' in seller_text, 'Allocation and character distinguished')
check('Acquired amortizable Section 197 goodwill' in seller_text and 'Section 1245' in seller_text and 'Section 1231' in seller_text, 'Acquired-goodwill recapture and remaining gain')
check('five-year lookback' in seller_text, 'Section 1231 lookback covered')
check('Do not assign inventory its cost basis' in seller_text and 'fair market value' in seller_text, 'Inventory allocation uses valuation')
for phrase in ['Asset description and owner', 'Fair market value and evidence', 'Adjusted tax basis', 'Recapture and gain character', 'Entity and owner taxes', 'Retained real estate', 'Buyer/seller Form 8594 handoff']:
    check(phrase in seller_text, 'Seller workpaper: ' + phrase)
for obsolete in ['How quickly can strategies be implemented?', 'nearly every meaningful strategy has a deadline', 'their sale generates long-term capital gain taxed at a maximum federal rate of 20%', "inventory allocation at the seller's cost basis"]:
    check(obsolete not in seller_text, 'Removed misleading seller wording: ' + obsolete)
check(Decimal('100000') * (Decimal('.45') - Decimal('.25')) == Decimal('20000'), 'Hypothetical rate illustration arithmetic')
check('hypothetical rates' in seller_text and 'not a forecast' in seller_text, 'Hypothetical tax-rate example labeled')

for obsolete in ['$31,300', '$53,700', 'A mileage tracking app satisfies this', 'Vehicles with a gross vehicle weight rating over 6,000 pounds are excluded']:
    check(obsolete not in vehicle, 'Removed stale/overbroad vehicle wording: ' + obsolete)
for phrase in ['$32,000', '$2,560,000', '$4,090,000', 'Section 4.24', 'unloaded gross vehicle weight', 'manufacturer', 'acquired and placed in service after January 19, 2025', 'binding-contract', 'ready and available', 'related-party', 'Partners are not employees', 'shareholder-employee', 'Form W-2', 'prior mileage elections']:
    check(phrase.lower() in vehicle_text.lower(), 'Vehicle rule: ' + phrase)
for phrase in ['Vehicle classification and manufacturer evidence', 'Ownership and financing', 'Expected business use', 'Prior mileage-method elections', 'Acquisition and service dates', 'Deduction comparison', 'Payroll or reimbursement responsibility']:
    check(phrase in vehicle_text, 'Purchase checklist: ' + phrase)
check('GPS trips alone does not substantiate' in vehicle_text, 'Mileage-app limitation explicit')
check('commuting' in vehicle_text and 'business purpose' in vehicle_text and 'odometer' in vehicle_text, 'Substantiation elements present')
check('50% or less' in vehicle_text and 'recovery period' in vehicle_text and 'recapture' in vehicle_text, 'Recapture threshold and timing')
example = re.search(r'<table id="suv-example">(.*?)</table>', vehicle, re.S)[1]
rows = {plain(k): Decimal(plain(v).replace('$', '').replace(',', '')) for k,v in re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td></tr>', example, re.S)}
check(rows['Business basis'] == 85000, 'Vehicle example basis')
check(rows['Section 179 on the heavy SUV'] == 32000, 'Vehicle example 2026 SUV limit')
check(rows['Business basis'] - rows['Section 179 on the heavy SUV'] == rows['Remaining basis: $85,000 minus $32,000'] == 53000, 'Vehicle example remaining basis')
check(rows['100% bonus depreciation on eligible remaining basis'] == 53000, 'Vehicle example bonus amount')
check(rows['Section 179 on the heavy SUV'] + rows['100% bonus depreciation on eligible remaining basis'] == rows['Total first-year deduction'] == 85000, 'Vehicle example deduction total')
check(rows['Total first-year deduction'] * Decimal('.37') == rows['Illustrative reduction at an assumed 37% federal rate'] == 31450, 'Vehicle example illustrative tax arithmetic')
check(Decimal('85000') * Decimal('.70') == 59500 and '$59,500' in vehicle_text, 'Vehicle mixed-use basis arithmetic')
check('not a client result' in vehicle_text and 'not a credit, refund or guaranteed saving' in vehicle_text, 'Example limitations explicit')
print(f'PASS: {CHECKS} focused checks across {len(pages)} purchase/exit guides ({ROOT}).')
