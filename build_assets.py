#!/usr/bin/env python3
"""Build asset-class cost segregation pages and the cost seg audit defense guide."""

from __future__ import annotations

import sys

import site_template as T
import content_assets as A

PUBLISHED = "2026-08-15"
MODIFIED = "2026-08-15"


def money(n: int) -> str:
    return f"${n:,.0f}"


def paras(items: list[str]) -> str:
    return "\n".join(f"            <p>{p}</p>" for p in items)


def bullets(items: list[str]) -> str:
    return ('            <ul class="takeaway-list">\n'
            + "\n".join(f"                <li>{i}</li>" for i in items)
            + "\n            </ul>")


def component_block(components: dict[str, str]) -> str:
    rows = "\n".join(
        f"                <li><strong>{k} property:</strong> {v}.</li>"
        for k, v in components.items()
    )
    return f'            <ul class="takeaway-list">\n{rows}\n            </ul>'


def numbered(items: list[tuple[str, str]]) -> str:
    body = "\n".join(
        f"                <li><strong>{h}.</strong> {t}</li>" for h, t in items
    )
    return f'            <ol class="howto-list">\n{body}\n            </ol>'


def process_section() -> str:
    return f"""    <section class="content-section fade-in-section" id="process">
        <div class="container narrow">
            <h2>How a Cost Segregation Engagement Actually Runs</h2>
            <p>Six steps, in this order. The first one matters most and is the one most
            providers skip, because it is the step that can conclude you should not buy a
            study at all.</p>
{numbered(A.PROCESS)}
        </div>
    </section>"""


def process_schema(url: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": "How a Cost Segregation Engagement Works",
        "description": ("The six steps of a defensible cost segregation engagement, from "
                        "confirming the deduction is usable through modeling the exit."),
        "totalTime": "P30D",
        "step": [
            {"@type": "HowToStep", "position": i, "name": h, "text": t,
             "url": f"{url}#process"}
            for i, (h, t) in enumerate(A.PROCESS, start=1)
        ],
    }


def returns_table(rows: list[tuple]) -> str:
    body = []
    for label, price, basis, pct in rows:
        b = int(basis.replace("$", "").replace(",", ""))
        reclass = round(b * pct / 100 / 1000) * 1000
        yr1 = reclass + round((b - reclass) / 39 * 0.5 / 1000) * 1000
        body.append(
            f"                    <tr><th scope=\"row\">{label}</th><td>{price}</td>"
            f"<td>{basis}</td><td>{pct}% / {money(reclass)}</td>"
            f"<td>~{money(yr1)}</td></tr>"
        )
    return f"""            <div class="ae-table-scroll" style="overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%">
                <table class="compare-table">
                    <caption>Illustrative. Assumes 100% bonus depreciation on reclassified
                    property and a partial first year on the remaining basis. Actual results
                    depend on the property, its age, and the supported land allocation.</caption>
                    <thead><tr><th scope="col">Property</th><th scope="col">Price</th>
                    <th scope="col">Depreciable basis</th><th scope="col">Reclassified</th>
                    <th scope="col">Year 1 deduction</th></tr></thead>
                    <tbody>
{chr(10).join(body)}
                    </tbody>
                </table>
            </div>"""


ASSET_FAQ_TAIL = [
 ("Can I do a study on a property I bought years ago?",
  "<p>Yes. A Form 3115 change in accounting method captures every missed deduction from the "
  "placed-in-service year in a single Section 481(a) adjustment claimed in the current year. "
  "No amended returns are needed and there is no three-year limitation.</p>"),
 ("What happens to the accelerated depreciation when I sell?",
  "<p>Personal property is recaptured as ordinary income under Section 1245 to the extent of "
  "gain, and building and land improvement depreciation is subject to unrecaptured Section "
  "1250 gain at up to 25%. A 1031 exchange defers it, and holding until death eliminates it "
  "through the basis step-up under Section 1014.</p>"),
 ("Will the deduction offset my other income?",
  "<p>It depends on the passive activity rules. For an owner-operated business the loss is "
  "generally non-passive where you materially participate. For a property held in a separate "
  "entity and leased to your operating company, the self-rental rules apply and a grouping "
  "election under Reg. 1.469-4 is often needed.</p>"),
]


def build_asset(a: dict) -> str:
    path = f"/{a['slug']}/"
    url = f"{T.SITE}{path}"
    asset = a["asset"]

    faqs = [
        (f"How much does a {asset} cost segregation study reclassify?",
         f"<p>Typically {a['lo']}% to {a['hi']}% of depreciable basis. The range depends on "
         f"the property's age, construction, and how much of the investment sits in equipment "
         f"and site work rather than building structure.</p>"),
        (f"Is a cost segregation study worth it on a {asset}?",
         "<p>Generally yes once depreciable basis exceeds roughly $500,000, provided you can "
         "use the deduction in the current year. The binding question is not the size of the "
         "deduction but whether the passive activity rules, basis limits, and excess business "
         "loss limitation allow you to claim it now.</p>"),
    ] + ASSET_FAQ_TAIL

    body_parts = [
        T.page_header(
            h1=a["h1"],
            subtitle=a["desc"],
            trail=[("Home", "/"), ("Cost Segregation", "/cost-segregation-study/"),
                   (a["title"], path)],
            cta="Get Your Free Estimate",
        ),
        f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="post-meta">By {T.AUTHOR}, {T.BRAND} &middot; Billings, Montana &middot;
            Updated {MODIFIED}</p>
{T.definition(a['definition'])}
        </div>
    </section>""",
        T.section(f"Why {asset.title()}s Reclassify the Way They Do", paras(a["why"])),
        T.section("Component Breakdown", component_block(a["components"])),
        T.section("Illustrative Returns", returns_table(a["table"])),
    ]
    for heading, items in a["extra"]:
        body_parts.append(T.section(heading, paras(items)))

    body_parts.append(process_section())
    body_parts += [
        T.takeaways([
            f"{asset.title()}s typically reclassify {a['lo']}% to {a['hi']}% of depreciable basis.",
            "Land allocation drives the result as much as the component study does.",
            "A property held for years can still be caught up in full through a Form 3115.",
            "Section 179, not bonus depreciation, is the tool for roofs and HVAC on nonresidential buildings.",
            "The passive activity analysis decides whether the deduction is usable this year.",
        ]),
        T.faq_section(faqs),
        T.related_section([
            ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
            ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026 Under the OBBBA"),
            ("/form-3115-cost-segregation-lookback/", "Form 3115 Cost Segregation Lookback"),
            ("/section-179-vs-bonus-depreciation-2026/", "Section 179 vs Bonus Depreciation"),
            ("/cost-segregation-audit-defense/", "What Happens If Your Study Is Audited"),
            ("/case-studies/", "Case Studies: Real Tax Planning Results"),
        ]),
    ]

    schemas = [
        T.article_schema(title=a["h1"], description=a["desc"], url=url,
                         published=PUBLISHED, modified=MODIFIED,
                         section="Cost Segregation"),
        T.faq_schema(faqs),
        process_schema(url),
        T.breadcrumb_schema([("Home", "/"),
                             ("Cost Segregation", "/cost-segregation-study/"),
                             (a["title"], path)]),
    ]
    return T.build_page(title=a["title"] + " | AE Tax Advisors", description=a["desc"],
                        path=path, body="\n\n".join(body_parts), schemas=schemas,
                        published=PUBLISHED, modified=MODIFIED)


def build_audit(a: dict) -> str:
    path = f"/{a['slug']}/"
    url = f"{T.SITE}{path}"
    body_parts = [
        T.page_header(h1=a["h1"], subtitle=a["desc"],
                      trail=[("Home", "/"), ("Cost Segregation", "/cost-segregation-study/"),
                             (a["title"], path)],
                      cta="Talk to a Tax Strategist"),
        f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="post-meta">By {T.AUTHOR}, {T.BRAND} &middot; Updated {MODIFIED}</p>
{T.definition(a['definition'])}
        </div>
    </section>""",
    ]
    for heading, items in a["sections"]:
        body_parts.append(T.section(heading, paras(items)))
    body_parts += [T.faq_section(a["faqs"]), T.related_section(a["related"])]

    schemas = [
        T.article_schema(title=a["h1"], description=a["desc"], url=url,
                         published=PUBLISHED, modified=MODIFIED,
                         section="IRS Representation"),
        T.faq_schema(a["faqs"]),
        T.breadcrumb_schema([("Home", "/"),
                             ("Cost Segregation", "/cost-segregation-study/"),
                             (a["title"], path)]),
    ]
    return T.build_page(title=a["title"] + " | AE Tax Advisors", description=a["desc"],
                        path=path, body="\n\n".join(body_parts), schemas=schemas,
                        published=PUBLISHED, modified=MODIFIED)


def main() -> int:
    for a in A.ASSETS:
        html = build_asset(a)
        out = T.write_page(a["slug"], html)
        w = len(T.strip_tags(html.split("<main>")[1].split("</main>")[0]).split())
        print(f"{w:>5} words  {out.relative_to(T.ROOT)}")
    for a in A.AUDIT_PAGES:
        html = build_audit(a)
        out = T.write_page(a["slug"], html)
        w = len(T.strip_tags(html.split("<main>")[1].split("</main>")[0]).split())
        print(f"{w:>5} words  {out.relative_to(T.ROOT)}")
    print(f"\n{len(A.ASSETS) + len(A.AUDIT_PAGES)} pages built.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
