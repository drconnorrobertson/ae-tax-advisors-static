"""Build the editorial property records library into the public staging tree."""
from collections import defaultdict
from html import escape
from pathlib import Path
import re
import sys

ORIGIN = "https://www.aetaxadvisors.com"
BASE = "/guides/property-records/"
SECTION = Path(__file__).parent
RESOURCES = {
    "Closing and acquisition": ("/workbooks/rental-acquisition/", "Rental acquisition workbooks"),
    "Construction and renovations": ("/workbooks/improvements/", "Improvement records workbooks"),
    "Rental operations": ("/workbooks/rental-operations/", "Rental operations workbooks"),
    "Short-term rentals": ("/guides/str-documentation-kit/", "Short-term rental documentation kit"),
    "Study deliverables": ("/workbooks/cost-segregation/", "Cost segregation workbooks"),
    "Existing property": ("/workbooks/cost-segregation/", "Cost segregation workbooks"),
    "Sale preparation": ("/workbooks/property-sale/", "Property sale workbooks"),
    "Ownership and financing": ("/workbooks/owner-funding/", "Owner funding workbooks"),
    "Insurance and interruptions": ("/workbooks/rental-operations/", "Rental operations workbooks"),
    "Adviser handoffs": ("/workbooks/advisor-selection/", "Tax adviser workbooks"),
    "Income reconciliation": ("/workbooks/rental-operations/", "Rental operations workbooks"),
    "Equipment and property records": ("/workbooks/vehicles-equipment/", "Equipment records workbooks"),
    "Mixed use and commercial": ("/workbooks/improvements/", "Improvement records workbooks"),
    "Multistate portfolios": ("/workbooks/multistate/", "Multistate workbooks"),
    "Portfolio planning": ("/guides/rental-property-tax-questions/", "Rental property tax questions"),
}


def slug(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def load_topics():
    categories = defaultdict(list)
    category = None
    for line in (SECTION / "property-records-topics.txt").read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            category = line[2:]
            continue
        title, scenario, records, check = line.split("|")
        if not category or not all((title, scenario, records, check)):
            raise ValueError(f"Incomplete topic: {line}")
        categories[category].append((title, scenario, records, check))
    titles = [slug(row[0]) for rows in categories.values() for row in rows]
    if set(categories) != set(RESOURCES) or len(titles) != 150 or len(set(titles)) != 150:
        raise ValueError("Expected 150 unique records guides across the defined categories")
    return categories


def link(path, title):
    return f'<a href="{escape(path)}">{escape(title)}</a>'


def page(path, title, description, body):
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} | AE Tax Advisors</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{ORIGIN}{path}">
<link rel="stylesheet" href="/assets/style.css">
</head><body>
<header><nav class="container" aria-label="Site navigation">{link("/", "AE Tax Advisors")} · {link("/guides/", "Guides")}</nav></header>
<main id="main-content" class="content-section"><article class="container narrow">
<h1>{escape(title)}</h1>
{body}
</article></main></body></html>
"""


def generate(root):
    categories = load_topics()
    pages = {}
    groups = []
    for category, rows in categories.items():
        category_path = BASE + "#" + slug(category)
        groups.append(f'<section id="{slug(category)}"><h2>{escape(category)}</h2><ul>' +
                      "".join(f"<li>{link(BASE + slug(title) + '/', title)}</li>" for title, *_ in rows) +
                      "</ul></section>")
        for index, (title, scenario, records, check) in enumerate(rows):
            neighbors = [rows[(index + 1) % len(rows)], rows[(index - 1) % len(rows)]]
            related = "".join(f"<li>{link(BASE + slug(item[0]) + '/', item[0])}</li>" for item in neighbors)
            resource = link(*RESOURCES[category])
            body = f"""<p>{link(category_path, category + " records guides")}</p>
<p>{escape(scenario)}</p>
<h2>What to collect</h2><p>{escape(records)}</p>
<h2>What to verify before sharing the file</h2><p>{escape(check)}</p>
<h2>Record the result</h2><p>Keep the source file, property identifier, period covered and the name of the person responsible for resolving open questions. Send sensitive records through the secure channel agreed with your adviser.</p>
<h2>Related records and worksheets</h2><ul>{related}<li>{resource}</li></ul>"""
            path = BASE + slug(title) + "/"
            pages[path] = page(path, title, scenario + " " + records, body)
    pages[BASE] = page(BASE, "Real estate tax records guides",
                       "Find 150 focused real estate records checklists for acquisitions, rentals, construction, cost segregation, financing, and sale preparation.",
                       "<p>Find the record you need to reconcile, what evidence to keep, and what to verify before handing it to your adviser.</p>" + "\n".join(groups))
    for url, html in pages.items():
        destination = root / url.strip("/") / "index.html"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(html, encoding="utf-8")

    entries = "".join(f"  <url><loc>{ORIGIN}{url}</loc></url>\n" for url in sorted(pages))
    (root / "sitemap-property-records.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + entries + "</urlset>\n", encoding="utf-8")

    guides = root / "guides" / "index.html"
    text = guides.read_text(encoding="utf-8")
    marker = "</main>"
    if text.count(marker) != 1:
        raise ValueError("Expected one guides main content region")
    block = '<section class="content-section"><div class="container narrow"><h2>Real estate tax records</h2><p>' + link(BASE, "Browse 150 property records guides") + "</p></div></section>"
    guides.write_text(text.replace(marker, block + marker), encoding="utf-8")
    print(f"Built {len(pages) - 1} property records guides and their library hub.")


if __name__ == "__main__":
    generate(Path(sys.argv[1]))
