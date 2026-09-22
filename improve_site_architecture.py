#!/usr/bin/env python3
"""Repair crawl paths and connect existing topical pages to useful hubs."""
from __future__ import annotations

import re
from pathlib import Path

import build_case_studies
import build_sitemap_page
import site_template as T

ROOT = Path(__file__).resolve().parent
BASE = "https://www.aetaxadvisors.com"

HUB_LINKS = {
    "services/cost-segregation": [
        ("/services/cost-segregation-airbnb/", "Short-term rental studies"),
        ("/services/cost-segregation-commercial/", "Commercial property studies"),
        ("/services/cost-segregation-hotels/", "Hotel and hospitality studies"),
        ("/services/cost-segregation-multifamily/", "Multifamily studies"),
        ("/services/cost-segregation-self-storage/", "Self-storage studies"),
        ("/cost-segregation-car-wash/", "Car wash cost segregation"),
    ],
    "business-owner-small-business-tax": [
        ("/for/construction-contractors/", "Construction contractors"),
        ("/for/ecommerce-sellers/", "Ecommerce sellers"),
        ("/for/physicians-dentists/", "Physicians and dentists"),
        ("/for/restaurant-owners/", "Restaurant owners"),
    ],
    "resources": [
        ("/resources/amendment-self-assessment/", "Amended-return self-assessment"),
        ("/resources/cost-seg-roi-guide/", "Cost segregation ROI guide"),
        ("/resources/tax-planning-checklist/", "Tax planning checklist"),
    ],
    "locations": [
        ("/locations/maryland/", "Maryland tax advisory"),
        ("/locations/montana/", "Montana tax advisory"),
        ("/locations/pittsburgh/", "Pittsburgh tax advisory"),
    ],
    "pricing": [
        ("/cost-segregation-pricing/", "Cost segregation pricing"),
        ("/tax-advisory-cost-roi/", "Tax advisory cost and ROI"),
    ],
    "calculators": [
        ("/tools/cost-seg-calculator/", "Cost segregation calculator"),
    ],
    "guides": [
        ("/guides/rental-property-tax-questions/", "Rental property tax questions"),
        ("/guides/business-tax-questions/", "Business tax questions"),
        ("/research/", "Tax planning outcomes research"),
    ],
}


def add_hub_links() -> None:
    for hub, links in HUB_LINKS.items():
        path = ROOT / hub / "index.html"
        content = path.read_text()
        marker = f"site-architecture-links-{hub.replace('/', '-') }"
        if marker in content:
            continue
        assert "</main>" in content, path
        items = "\n".join(f'<li><a href="{href}">{label}</a></li>' for href, label in links)
        section = (f'<section class="content-section fade-in-section {marker}">'
                   '<div class="container narrow"><h2>Explore Related Resources</h2>'
                   f'<ul class="related-links">{items}</ul></div></section>')
        path.write_text(content.replace("</main>", section + "\n</main>", 1))


def rebuild_case_index() -> None:
    cases = build_case_studies.read_existing()
    cases.sort(key=lambda item: (item["cat"], item["title"]))
    (ROOT / "case-studies/index.html").write_text(
        build_case_studies.build_index(cases), encoding="utf-8"
    )


def build_research_hub() -> None:
    path = "/research/"
    description = ("Tax planning outcomes research from published AE Tax Advisors case studies, "
                   "with methods and downloadable data.")
    body = "\n".join([
        T.page_header(h1="Tax Planning Research", subtitle=description,
                      trail=[("Home", "/"), ("Research", path)]),
        T.section("Published outcomes analysis",
                  '<p>Explore the methodology, distribution, and limitations of reported results '
                  'in our <a href="/research/tax-planning-case-study-outcomes/">tax planning case study outcomes report</a>. '
                  'The report links the underlying case studies and data files so readers can review the sample.</p>'
                  '<p>For individual situations, browse the <a href="/case-studies/">case study library</a>. '
                  'Reported outcomes are specific to the clients described and do not predict future results.</p>'),
    ])
    page = T.build_page(title="Tax Planning Research | AE Tax Advisors",
                        description=description, path=path, body=body,
                        schemas=[T.breadcrumb_schema([("Home", "/"), ("Research", path)])],
                        published="2026-09-22", modified="2026-09-22", og_type="website")
    target = ROOT / "research/index.html"
    target.write_text(page, encoding="utf-8")


def normalize_metadata() -> None:
    # The duplicate tags are identical, so retaining the first changes no target.
    for slug in ("locations/baltimore", "locations/baltimore/tax-planning",
                 "locations/baltimore/entity-structuring", "locations/baltimore/cost-segregation"):
        path = ROOT / slug / "index.html"
        content = path.read_text()
        tag = f'<link rel="canonical" href="{BASE}/{slug}/">'
        content = content.replace(tag, "", content.count(tag)-1) if content.count(tag)>1 else content
        content = re.sub(r"(?m)^[ \t]+$", "", content)
        path.write_text(content)

    for slug in ("test-delete-me", "test-push-verification"):
        path = ROOT / "blog" / slug / "index.html"
        path.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8">'
                        '<meta name="robots" content="noindex, nofollow">'
                        '<title>Test page</title></head><body><p>Test page.</p></body></html>')

    for slug in ("locations/montana", "locations/maryland",
                 "locations/pittsburgh", "for/construction-contractors"):
        path = ROOT / slug / "index.html"
        content = path.read_text().replace(
            f'https://aetaxadvisors.com/{slug}/', f'{BASE}/{slug}/')
        path.write_text(content)

    for slug, new_title in (
        ("reasonable-compensation-s-corp-irs", "S-Corp Reasonable Compensation: IRS Factors and Case Law | AE Tax Advisors"),
        ("reasonable-compensation", "How to Set S-Corp Owner Salary | AE Tax Advisors"),
        ("services/reasonable-compensation", "Reasonable Compensation Analysis Service | AE Tax Advisors"),
    ):
        path = ROOT / slug / "index.html"
        content = path.read_text()
        old = "Reasonable Compensation for S-Corp Owners | AE Tax Advisors"
        for tag in ("title", "og:title", "twitter:title"):
            if tag == "title":
                content = content.replace(f"<title>{old}</title>", f"<title>{new_title}</title>", 1)
            else:
                content = content.replace(f'content="{old}"', f'content="{new_title}"', 1)
        path.write_text(content)

    # This skeletal old page targets the same hotel topic as the full service page.
    path = ROOT / "cost-segregation-hotels/index.html"
    content = path.read_text().replace(
        f'<link rel="canonical" href="{BASE}/cost-segregation-hotels/">',
        f'<link rel="canonical" href="{BASE}/services/cost-segregation-hotels/">',
    )
    path.write_text(content)


def sitemap() -> None:
    excluded = {"/blog/test-delete-me/", "/blog/test-push-verification/",
                "/cost-segregation-hotels/"}
    for file in ("sitemap.xml", "sitemap-blog.xml", "sitemap-pages.xml"):
        path = ROOT / file
        xml = path.read_text()
        for slug in excluded:
            # Works for compact and expanded URL elements without touching old dates.
            pattern = (r"\s*<url>\s*<loc>" + re.escape(BASE + slug)
                       + r"</loc>.*?</url>")
            xml = re.sub(pattern, "", xml, flags=re.S)
        if file != "sitemap-blog.xml" and f"{BASE}/research/" not in xml:
            entry = (f'  <url><loc>{BASE}/research/</loc><lastmod>2026-09-22</lastmod>'
                     '<changefreq>monthly</changefreq><priority>0.6</priority></url>\n')
            xml = xml.replace("</urlset>", entry + "</urlset>")
        path.write_text(xml)
    index = ROOT / "sitemap-index.xml"
    index.write_text(index.read_text().replace(
        "sitemap-pages.xml</loc><lastmod>2026-09-18",
        "sitemap-pages.xml</loc><lastmod>2026-09-22"))


def main() -> None:
    normalize_metadata()
    rebuild_case_index()
    build_research_hub()
    add_hub_links()
    sitemap()
    (ROOT / "sitemap/index.html").write_text(build_sitemap_page.build_sitemap_page())
    print("Repaired index, metadata, sitemap, broken link, and supporting hub links")


if __name__ == "__main__":
    main()
