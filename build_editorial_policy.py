#!/usr/bin/env python3
"""Build the public editorial and content-quality policy page."""

from __future__ import annotations

import site_template as T

PATH = "/editorial-policy/"
PUBLISHED = "2026-09-23"


def build() -> str:
    title = "Editorial Policy and Tax Content Standards | AE Tax Advisors"
    description = (
        "How AE Tax Advisors researches, reviews, sources, updates, and corrects "
        "tax content for business owners and real estate investors."
    )
    body = "\n".join([
        T.page_header(
            h1="Editorial Policy and Tax Content Standards",
            subtitle="The standards behind our tax guides, comparisons, calculators, and case studies.",
            trail=[("Home", "/"), ("Editorial Policy", PATH)],
            cta="Ask About Your Situation",
        ),
        T.section(
            "Purpose",
            T.definition(
                "AE Tax Advisors publishes educational tax content to help business owners and "
                "real estate investors understand the rule, the decision it affects, the records "
                "that support it, and the point where individualized advice is required."
            ) +
            "            <p>Our goal is decision-useful accuracy, not a page count. Each indexable "
            "page should answer a distinct question or serve a distinct navigational purpose. We "
            "do not treat a change in city, industry, or keyword wording as enough reason to "
            "publish another page.</p>",
        ),
        T.section(
            "How We Research Tax Topics",
            """            <p>We start with primary authority whenever it is available. Depending on the topic, that includes the Internal Revenue Code, Treasury Regulations, IRS forms and instructions, revenue procedures, revenue rulings, notices, publications, audit technique guides, and court decisions. State-specific statements are checked against the applicable state tax authority.</p>
            <p>Secondary sources can help explain context, but they do not replace controlling authority. Pages link directly to useful primary sources when a reader would benefit from verifying a rule or procedure.</p>
            <p>Tax outcomes depend on facts. Our content distinguishes the legal rule from the practical filing decision and calls out common limitations such as basis, at-risk rules, passive-activity rules, state conformity, recapture, timing, and documentation.</p>""",
        ),
        T.section(
            "Writing and Review Standards",
            """            <ul class="takeaway-list">
                <li><strong>Direct answer first.</strong> Informational pages should answer the core question near the top.</li>
                <li><strong>Distinct intent.</strong> A new page must address a meaningfully different decision, fact pattern, audience need, or source set.</li>
                <li><strong>Concrete examples.</strong> Examples are illustrative and identify the facts that can change the result.</li>
                <li><strong>Source discipline.</strong> Time-sensitive thresholds, deadlines, and procedural claims are checked against current primary guidance.</li>
                <li><strong>No guaranteed outcomes.</strong> Savings figures are presented as documented examples or modeled estimates, with limitations stated.</li>
                <li><strong>Useful next steps.</strong> Readers should leave knowing what to verify, what records to gather, and when professional review is appropriate.</li>
            </ul>""",
        ),
        T.section(
            "Dates, Updates, and Corrections",
            """            <p>A publication date identifies when an article first appeared. A modification date should change only when the substance changes, not because a build or formatting process ran. Time-sensitive guides are reviewed when federal or state law, IRS guidance, filing procedures, or published thresholds change.</p>
            <p>If you identify a material error or an outdated source, email <a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a> with the page URL and supporting authority. We review supported corrections and update the page, its structured data, and its modification date when warranted.</p>""",
        ),
        T.section(
            "How We Use Technology",
            """            <p>Technology may assist with research organization, formatting, internal linking, quality checks, and identifying coverage gaps. It does not change the standard for publication. Content must still be coherent, fact-specific, sourceable, non-duplicative, and useful to a reader.</p>
            <p>Programmatic templates are appropriate for consistent navigation and structured data. They are not a substitute for original analysis. Pages that do not add enough value should not be indexed merely to increase inventory.</p>""",
        ),
        T.section(
            "Case Studies, Calculators, and Comparisons",
            """            <p>Case studies describe specific or illustrative facts and do not promise a similar result. Calculators provide estimates based on the inputs and assumptions shown; they are not tax-return calculations. Comparison pages should identify the source and date for third-party information and separate verified facts from analysis or estimates.</p>
            <p>Nothing on this site creates an advisor-client relationship or replaces advice based on a complete set of facts. See our <a href="/disclaimer/">disclaimer</a>, <a href="/research/">research</a>, and <a href="/case-studies/">case study library</a> for additional context.</p>""",
        ),
        T.related_section([
            ("/bios/", "Meet the AE Tax Advisors Team"),
            ("/research/", "Tax Planning Research"),
            ("/tax-rule-guides/", "Federal Tax Rule Guides"),
            ("/sitemap/", "Complete Site Map"),
        ], heading="Related Trust and Research Resources"),
    ])
    schemas = [
        {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": "Editorial Policy and Tax Content Standards",
            "description": description,
            "url": f"{T.SITE}{PATH}",
            "publisher": {"@id": f"{T.SITE}/#organization"},
            "datePublished": PUBLISHED,
            "dateModified": PUBLISHED,
        },
        T.breadcrumb_schema([("Home", "/"), ("Editorial Policy", PATH)]),
    ]
    return T.build_page(
        title=title, description=description, path=PATH, body=body,
        schemas=schemas, published=PUBLISHED, modified=PUBLISHED,
        og_type="website", active_nav="/guides/",
    )


def main() -> int:
    print(T.write_page(PATH, build()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
