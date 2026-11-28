"""Build worked tax FAQs and link them from the relevant filing or planning guides."""

from collections import defaultdict
from html import escape
import json
from pathlib import Path
import sys

ORIGIN = "https://www.aetaxadvisors.com"
COLLECTIONS = {
    "rental-partnership-basis-questions": (
        "Rental partnership basis questions",
        "Partnership basis and K-1 questions for rental property owners",
        "Worked examples on K-1 capital, rental loss limits, inside basis, liabilities and distributions.",
        "Trace the amounts reported by the partnership to the records maintained by each partner.",
        "/tax-planning-for-high-net-worth-individuals-with-complex-partnership-and-k1-income/",
    ),
    "real-estate-exchange-reporting-questions": (
        "Real estate exchange reporting questions",
        "1031 exchange deadlines, gain and basis questions",
        "Worked examples for identification, exchange deadlines, cash received and replacement property basis.",
        "Reconcile the exchange records before reporting gain or preparing a replacement property depreciation schedule.",
        "/1031-exchange-guide/",
    ),
    "rental-sale-reporting-questions": (
        "Rental sale reporting questions",
        "Tax reporting questions when a rental property sells",
        "Worked examples for sale proceeds, mortgage payoff, adjusted basis and depreciation-related gain.",
        "Reconcile the closing statement and asset schedules before computing gain.",
        "/rental-property-sale-tax-calculator/",
    ),
    "rental-at-risk-tax-questions": (
        "Rental at-risk tax questions",
        "At-risk loss limitation questions for rental property owners",
        "Worked examples on limit ordering, financing, loss protection, recapture and carryforwards.",
        "Follow the loss through the at-risk calculation before applying the passive activity rules.",
        "/passive-activity-loss-rules-real-estate/",
    ),
    "real-estate-professional-hours-questions": (
        "Real estate professional hours questions",
        "Real estate professional status and participation hours questions",
        "Worked examples on the 750-hour test, other work, employee ownership and spouse participation.",
        "Separate the hours used to establish your status from those used to evaluate each rental activity.",
        "/real-estate-professional-status/",
    ),
    "rental-income-reporting-questions": (
        "Rental income reporting questions",
        "Rental income reporting questions for landlords",
        "Worked examples for advance rent, lease cancellation payments, unpaid rent and noncash rent.",
        "Reconcile each receipt with the lease, payment records and applicable reporting rule.",
        "/rental-property-tax-planning/",
    ),
    "cost-segregation-documentation-questions": (
        "Cost segregation documentation questions",
        "Cost segregation study documentation questions",
        "Worked examples on estimated costs, indirect costs, component descriptions and asset schedules.",
        "Review the evidence that connects a study’s allocations to your depreciation records.",
        "/cost-segregation-study/",
    ),
    "rental-financing-tax-questions": (
        "Rental financing tax questions",
        "Rental refinance and mortgage tax questions",
        "Worked examples on tracing loan proceeds, refinance points, mortgage payments and appraisal fees.",
        "Reconcile the loan records before classifying interest and other costs.",
        "/rental-property-tax-planning/",
    ),
    "rental-repair-capital-questions": (
        "Rental repair and capitalization questions",
        "Rental repair and capital improvement tax questions",
        "Worked examples on building systems, pre-existing defects and repair safe harbors.",
        "Compare the work performed with the tax rules that determine how its cost is reported.",
        "/rental-property-tax-planning/",
    ),
    "rental-conversion-tax-questions": (
        "Rental conversion tax questions",
        "Tax questions when a home changes between personal and rental use",
        "Worked examples for conversion basis, rental availability, mixed use, depreciation and sale reporting.",
        "Trace the dates and values that change the tax treatment when a home changes use.",
        "/rental-property-tax-planning/",
    ),
    "depreciation-method-filing-questions": (
        "Depreciation method filing questions",
        "Depreciation method filing and Form 3115 questions",
        "Worked examples on depreciation correction history, study scope, filing evidence and adjustment schedules.",
        "Trace the records behind the change from the original depreciation schedule through filing.",
        "/form-3115-cost-segregation/",
    ),
    "rental-loss-disposition-questions": (
        "Rental loss disposition questions",
        "Suspended rental loss questions for sales and transfers",
        "Worked examples for sales, installment reporting, exchanges, gifts and inherited rental property.",
        "Follow the suspended loss balance through the transaction that changes ownership.",
        "/passive-activity-loss-rules-real-estate/",
    ),
    "business-property-tax-questions": (
        "Business property tax questions",
        "Tax questions for business owners who own or lease real estate",
        "Worked examples for self-rentals, buildouts, depreciation schedules and business asset sales.",
        "Review the records that connect your operating business with its property.",
        "/rental-property-tax-planning/",
    ),
    "short-term-rental-tax-questions": (
        "Short-term rental tax questions",
        "Short-term rental tax questions for property owners",
        "Worked examples for personal use, booking activity, guest services, material participation and rental receipts.",
        "Find the tax question that matches your booking records, guest service or participation decision.",
        "/short-term-rental-tax-strategy/",
    ),
    "return-correction-questions": (
        "Return correction questions",
        "Return correction questions for business and rental owners",
        "Worked answers on amended returns and correcting rental or business tax schedules.",
        "Find the correction that matches your filing decision.",
        "/amended-tax-returns/",
    ),
    "depreciation-decision-questions": (
        "Depreciation decision questions",
        "Cost segregation and depreciation questions for property owners",
        "Worked examples for acquisition basis, cost segregation studies, renovation schedules and rental sales.",
        "Find the depreciation question that matches your purchase, renovation or sale.",
        "/real-estate-depreciation/",
    ),
}


def link(path, title):
    return f'<a href="{escape(path)}">{escape(title)}</a>'


def page(route, title, description, body, data):
    schema = {"@context": "https://schema.org", "@graph": data}
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} | AE Tax Advisors</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{ORIGIN}{route}">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False).replace("<", chr(92) + "u003c")}</script>
</head><body>
<header><nav class="container" aria-label="Site navigation">{link("/", "AE Tax Advisors")} · {link("/guides/", "Guides")}</nav></header>
<main id="main-content" class="content-section"><article class="container narrow">
<h1>{escape(title)}</h1>
{body}
</article></main></body></html>
"""


def breadcrumbs(route, title, base, label):
    trail = [("/", "Home"), ("/guides/", "Guides")]
    if route != base:
        trail.append((base, label))
    trail.append((route, title))
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": position, "name": name, "item": ORIGIN + path}
        for position, (path, name) in enumerate(trail, start=1)
    ]}


def generate(root, collection):
    base = f"/guides/{collection}/"
    label, hub_title, description, intro, pillar = COLLECTIONS[collection]
    source_file = Path(__file__).with_name(f"{collection}.txt")
    topics = defaultdict(list)
    category = None
    for line in source_file.read_text().splitlines():
        if line.startswith("# "):
            category = line[2:]
        elif line.strip():
            fields = line.split("|")
            if not category or len(fields) != 8 or not all(fields):
                raise ValueError(f"Incomplete question: {line}")
            topics[category].append(fields)

    hub = []
    pages = {}
    links = defaultdict(list)
    for heading, rows in topics.items():
        hub.append(f"<h2>{escape(heading)}</h2><ul>" + "".join(
            f"<li>{link(base + slug + '/', title)}</li>" for slug, title, *_ in rows
        ) + "</ul>")
        for slug, title, direct, example, question, answer, parent, source in rows:
            route = base + slug + "/"
            if route in pages:
                raise ValueError(f"Duplicate route: {route}")
            parent = "/" + parent + "/"
            links[parent].append((route, title))
            related = "".join(f"<li>{link(base + row[0] + '/', row[1])}</li>"
                              for row in rows if row[0] != slug)
            body = f"""<p>{link(base, label)}</p>
<p>{escape(direct)}</p>
<h2>Worked example</h2><p>{escape(example)}</p>
<h2>Frequently asked questions</h2><h3>{escape(question)}</h3><p>{escape(answer)}</p>
<h2>Related guides</h2><ul><li>{link(parent, "Read the related tax guide")}</li>{related}</ul>
<h2>Source</h2><p>{link(source, "IRS instructions and guidance")}</p>"""
            faq = {"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in [(title, direct), (question, answer)]
            ]}
            pages[route] = page(route, title, direct, body, [breadcrumbs(route, title, base, label), faq])
    pages[base] = page(base, hub_title, description,
                       f"<p>{escape(intro)}</p>" + "".join(hub),
                       [breadcrumbs(base, hub_title, base, label)])
    for route, content in pages.items():
        destination = root / route.strip("/") / "index.html"
        if destination.exists():
            raise ValueError(f"Existing route: {route}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content)

    links["/guides/"].append((base, hub_title))
    links[pillar].append((base, hub_title))
    for route, items in links.items():
        target = root / route.strip("/") / "index.html"
        text = target.read_text()
        if text.count("</main>") != 1:
            raise ValueError(f"Expected one main content region: {route}")
        items_html = "".join(f"<li>{link(path, label)}</li>" for path, label in items)
        section = f'<section class="content-section"><div class="container narrow"><h2>{escape(label)}</h2><ul>{items_html}</ul></div></section>'
        target.write_text(text.replace("</main>", section + "</main>"))

    entries = "".join(f"  <url><loc>{ORIGIN}{url}</loc><lastmod>2026-11-27</lastmod></url>\n" for url in sorted(pages))
    (root / f"sitemap-{collection}.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + entries + "</urlset>\n"
    )
    print(f"Built {len(pages) - 1} worked FAQs for {collection}.")


if __name__ == "__main__":
    for collection in COLLECTIONS:
        generate(Path(sys.argv[1]), collection)
