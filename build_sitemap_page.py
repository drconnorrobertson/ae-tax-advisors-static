#!/usr/bin/env python3
"""Build the human-readable /sitemap/ page and the /partners/ page."""

from __future__ import annotations

import html as _html
import re
import sys
from pathlib import Path

import site_template as T

ROOT = T.ROOT
PUBLISHED = "2026-08-15"
MODIFIED = "2026-08-15"

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.DOTALL)
NOINDEX_RE = re.compile(r'<meta name="robots" content="[^"]*noindex', re.I)
CANON_RE = re.compile(r'<link rel="canonical" href="https://aetaxadvisors\.com([^"]*)"')

# Buckets, in the order they appear on the page. Each is (heading, matcher).
SECTIONS: list[tuple[str, object]] = [
    ("Start Here", lambda u: u in {
        "/", "/about/", "/services/", "/pricing/", "/contact/", "/discovery/",
        "/bios/", "/press/", "/faq/", "/ae-tax-advisors-reviews/"}),
    ("Core Services", lambda u: u in {
        "/business-owner-small-business-tax/", "/real-estate-tax-planning/",
        "/cost-segregation-study/", "/short-term-rental-tax-strategy/",
        "/rental-property-tax-planning/", "/real-estate-investor-cpa/",
        "/retirement-exit-ma-tax-strategy/", "/individual-tax-planning-high-earners/",
        "/estate-trust-wealth-transfer/", "/tax-compliance-irs-representation/",
        "/multi-state-global-tax/", "/equipment-leasing-section-179/",
        "/crypto-mining-tax-strategy/", "/deferred-equity-compensation/",
        "/advanced-tax-planning-services/", "/audit-defense-compliance/"}),
    ("Cost Segregation by Property Type",
     lambda u: u.startswith("/cost-segregation-for-")),
    ("Cost Segregation by Profession",
     lambda u: u.endswith("-cost-segregation/") and not u.startswith("/cost-segregation")),
    ("Calculators and Tools",
     lambda u: "calculator" in u or u == "/calculators/"),
    ("Compare Firms", lambda u: u.startswith("/compare/")),
    ("Case Studies", lambda u: u.startswith("/case-studies/")),
    ("Blog", lambda u: u.startswith("/blog/")),
    ("Serving Investors by State", lambda u: u in STATE_URLS),
    ("Guides and Resources", lambda u: u in {
        "/glossary/", "/guides/", "/books/", "/blog/", "/calculators/",
        "/compare/", "/case-studies/"}),
]

STATES = [
    "alabama", "alaska", "arizona", "arkansas", "california", "colorado",
    "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho",
    "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine",
    "maryland", "massachusetts", "michigan", "minnesota", "mississippi",
    "missouri", "montana", "nebraska", "nevada", "new-hampshire", "new-jersey",
    "new-mexico", "new-york", "north-carolina", "north-dakota", "ohio",
    "oklahoma", "oregon", "pennsylvania", "rhode-island", "south-carolina",
    "south-dakota", "tennessee", "texas", "utah", "vermont", "virginia",
    "washington", "west-virginia", "wisconsin", "wyoming",
]
STATE_URLS = {f"/{s}/" for s in STATES}


def indexable_pages() -> list[tuple[str, str]]:
    """(url, label) for every canonical, indexable page."""
    out = []
    for p in sorted(ROOT.rglob("index.html")):
        if ".git" in p.parts:
            continue
        d = str(p.parent.relative_to(ROOT)).replace("\\", "/")
        url = "/" if d == "." else f"/{d}/"
        html = p.read_text(encoding="utf-8", errors="replace")
        if NOINDEX_RE.search(html):
            continue
        cm = CANON_RE.search(html)
        if cm and cm.group(1) != url:
            continue
        hm = H1_RE.search(html) or TITLE_RE.search(html)
        label = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", hm.group(1))).strip() if hm else url
        label = _html.unescape(label.split(" | AE Tax")[0])
        out.append((url, label))
    return out


def build_sitemap_page() -> str:
    pages = indexable_pages()
    used: set[str] = set()
    blocks = []

    for heading, match in SECTIONS:
        rows = []
        for url, label in pages:
            if url in used:
                continue
            try:
                ok = match(url)
            except Exception:
                ok = False
            if ok:
                rows.append((url, label))
        if not rows:
            continue
        # Case studies and blog are large; link the hub plus a sample.
        capped = heading in {"Case Studies", "Blog"}
        display = sorted(rows, key=lambda r: r[1])
        note = ""
        if capped and len(display) > 40:
            hub = [r for r in display if r[0].count("/") == 2]
            rest = [r for r in display if r not in hub][:39]
            display = hub + rest
            note = (f'            <p class="sitemap-note">Showing {len(display)} of '
                    f'{len(rows)} pages. Browse the full list on the section index.</p>\n')
        for url, _ in rows:
            used.add(url)
        items = "\n".join(
            f'                <li><a href="{url}">{T.esc(label)}</a></li>'
            for url, label in display
        )
        blocks.append(f"""    <section class="content-section fade-in-section">
        <div class="container">
            <h2>{heading} <span class="cs-count-inline">({len(rows)})</span></h2>
{note}            <ul class="sitemap-list">
{items}
            </ul>
        </div>
    </section>""")

    remaining = [(u, l) for u, l in pages if u not in used]
    if remaining:
        items = "\n".join(
            f'                <li><a href="{u}">{T.esc(l)}</a></li>'
            for u, l in sorted(remaining, key=lambda r: r[1])
        )
        blocks.append(f"""    <section class="content-section fade-in-section">
        <div class="container">
            <h2>All Other Pages <span class="cs-count-inline">({len(remaining)})</span></h2>
            <ul class="sitemap-list">
{items}
            </ul>
        </div>
    </section>""")

    body = f"""    <section class="page-header">
        <div class="container">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="/">Home</a> &rsaquo; <span>Site Map</span>
            </nav>
            <h1>Site Map</h1>
            <p class="subtitle">Every page on aetaxadvisors.com, organized by section.
            {len(pages)} pages in total.</p>
        </div>
    </section>

{chr(10).join(blocks)}"""

    schemas = [
        {"@context": "https://schema.org", "@type": "WebPage",
         "name": "Site Map", "url": f"{T.SITE}/sitemap/",
         "description": f"Complete index of all {len(pages)} pages on aetaxadvisors.com.",
         "publisher": {"@type": "Organization", "name": T.BRAND}},
        T.breadcrumb_schema([("Home", "/"), ("Site Map", "/sitemap/")]),
    ]
    return T.build_page(
        title="Site Map | AE Tax Advisors",
        description=(f"Complete site map for AE Tax Advisors: {len(pages)} pages covering "
                     "services, cost segregation, case studies, comparisons, calculators, "
                     "and guides."),
        path="/sitemap/", body=body, schemas=schemas,
        published=PUBLISHED, modified=MODIFIED, og_type="website",
    )


def build_partners_page() -> str:
    body = f"""    <section class="page-header">
        <div class="container">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="/">Home</a> &rsaquo; <span>Partners</span>
            </nav>
            <h1>Partners and Referral Relationships</h1>
            <p class="subtitle">The specialists we work alongside, and how referral
            relationships are disclosed.</p>
            <div class="cta-buttons">
                <a href="/discovery/" class="btn-cta btn-lg">Request a Consultation</a>
            </div>
        </div>
    </section>

    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="definition-lead">AE Tax Advisors is a tax advisory firm. We do not sell
            real estate, insurance, or investment products. Where a client needs expertise
            outside tax, we refer to specialists and disclose the relationship rather than
            absorbing the work into an engagement we are not the right firm for.</p>
        </div>
    </section>

    <section class="content-section fade-in-section">
        <div class="container narrow">
            <h2>Short-Term Rental Acquisition</h2>
            <h3>BNB Accelerator</h3>
            <p>BNB Accelerator is an education and acquisition program for investors buying and
            operating short-term rentals. Clients frequently arrive at tax planning after the
            property is already purchased, which is the wrong order: the seven-day average
            customer use test, the material participation plan, and the cost segregation timing
            all work better when they are decided before closing rather than after.</p>
            <p>For investors who want structured guidance on sourcing, underwriting, and
            operating short-term rentals, BNB Accelerator covers that side. We cover the tax
            side, and the two coordinate well because the tax outcome depends heavily on
            operating decisions such as minimum stay policy and whether a full-service property
            manager is engaged.</p>
            <p>If you are working through BNB Accelerator and want the tax strategy built
            alongside the acquisition rather than bolted on afterward, that is a good time to
            start a conversation.</p>
            <div class="center-cta" style="margin-top:18px;">
                <a href="/short-term-rentals/bnb-accelerator/" class="btn-secondary">
                    STR Tax Strategy for BNB Accelerator Investors</a>
            </div>
        </div>
    </section>

    <section class="content-section fade-in-section">
        <div class="container narrow">
            <h2>Specialists We Coordinate With</h2>
            <ul class="takeaway-list">
                <li><strong>Cost segregation engineering firms.</strong> On large or unusual
                assets we engage third-party engineering firms and build the tax work around
                their report. We are equally willing to work from a study you already have.</li>
                <li><strong>Energy incentive providers.</strong> Section 179D and 45L
                certifications require specific modeling and, in some cases, prevailing wage and
                apprenticeship compliance. We evaluate whether the incentive applies and
                coordinate a qualified provider.</li>
                <li><strong>Research credit specialists.</strong> A defensible R&amp;D credit
                study needs documentation infrastructure we do not maintain in-house.</li>
                <li><strong>Estate planning attorneys.</strong> Trust drafting and transfer tax
                planning are legal work. We coordinate the income tax side and the basis
                consequences.</li>
                <li><strong>Actuaries.</strong> Cash balance and defined benefit plan design
                requires an enrolled actuary to certify funding and sign Schedule SB.</li>
                <li><strong>Qualified intermediaries.</strong> A 1031 exchange requires a
                genuinely independent intermediary, which by statute cannot be your tax
                advisor.</li>
            </ul>
        </div>
    </section>

    <section class="content-section fade-in-section">
        <div class="container narrow">
            <h2>How We Handle Referrals</h2>
            <p>We tell you when a referral relationship exists. If we receive any compensation
            for a referral, you will know before you engage the other party. In most cases we
            do not, because the value of a referral network is that clients get the right
            specialist rather than the one that pays.</p>
            <p>We also work alongside your existing advisors rather than requiring you to
            replace them. Many engagements run in parallel with a client's current CPA, and we
            coordinate so positions are consistent across both.</p>
        </div>
    </section>

    <section class="content-section fade-in-section">
        <div class="container narrow">
            <h2>Working With Us as a Referral Partner</h2>
            <p>If you are a CPA, attorney, financial advisor, or real estate professional whose
            clients need cost segregation, entity restructuring, or advanced depreciation
            planning, we take referrals and return them. We do not solicit your compliance work,
            and we are glad to run a strategy engagement while you retain the return.</p>
            <p>Contact <a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a> or
            {T.PHONE} to discuss a referral relationship.</p>
        </div>
    </section>"""

    schemas = [
        {"@context": "https://schema.org", "@type": "WebPage",
         "name": "Partners and Referral Relationships",
         "url": f"{T.SITE}/partners/",
         "description": "Specialists AE Tax Advisors coordinates with and how referral relationships are disclosed.",
         "publisher": {"@type": "Organization", "name": T.BRAND}},
        T.breadcrumb_schema([("Home", "/"), ("Partners", "/partners/")]),
    ]
    return T.build_page(
        title="Partners and Referral Relationships | AE Tax Advisors",
        description=("The specialists AE Tax Advisors works alongside, including short-term "
                     "rental acquisition, energy incentives, R&D credits, estate counsel, and "
                     "actuaries, and how referral relationships are disclosed."),
        path="/partners/", body=body, schemas=schemas,
        published=PUBLISHED, modified=MODIFIED, og_type="website",
    )


def main() -> int:
    T.write_page("/partners/", build_partners_page())
    print("built: partners/index.html")
    T.write_page("/sitemap/", build_sitemap_page())
    print("built: sitemap/index.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
