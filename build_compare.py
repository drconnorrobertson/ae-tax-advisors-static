#!/usr/bin/env python3
"""Build competitor comparison pages under /compare/."""

from __future__ import annotations

import sys

import site_template as T
import content_compare as C

PUBLISHED = "2026-08-15"
MODIFIED = "2026-08-15"
BASE = "/compare/"

CHECK = "&#10004; Yes"
CROSS = "&#10008; No"


def cell(value: str) -> str:
    v = value.strip()
    if v.lower() == "yes":
        return CHECK
    if v.lower() == "no":
        return CROSS
    return v


def table(name: str, rows: list[tuple[str, str, str]]) -> str:
    body = "\n".join(
        f"                    <tr><th scope=\"row\">{a}</th><td>{cell(b)}</td>"
        f"<td>{cell(c)}</td></tr>"
        for a, b, c in rows
    )
    return f"""            <div class="ae-table-scroll" style="overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%">
                <table class="compare-table">
                    <caption>Comparison based on publicly available information as of 2026.
                    Confirm current pricing and scope with each provider directly.</caption>
                    <thead>
                        <tr><th scope="col">&nbsp;</th><th scope="col">{name}</th>
                        <th scope="col">AE Tax Advisors</th></tr>
                    </thead>
                    <tbody>
{body}
                    </tbody>
                </table>
            </div>"""


def bullets(items: list[str]) -> str:
    return ("            <ul class=\"takeaway-list\">\n"
            + "\n".join(f"                <li>{i}</li>" for i in items)
            + "\n            </ul>")


def paras(items: list[str]) -> str:
    return "\n".join(f"            <p>{p}</p>" for p in items)


def numbered(items: list[tuple[str, str]]) -> str:
    """Ordered how-to style list, which also feeds the HowTo schema."""
    body = "\n".join(
        f"                <li><strong>{h}.</strong> {t}</li>" for h, t in items
    )
    return f"            <ol class=\"howto-list\">\n{body}\n            </ol>"


def howto_schema(url: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": "How to Evaluate a Cost Segregation or Tax Advisory Firm",
        "description": ("Six questions that separate a defensible cost segregation "
                        "engagement from a report that will not hold up."),
        "totalTime": "PT20M",
        "step": [
            {"@type": "HowToStep", "position": i, "name": h,
             "text": t, "url": f"{url}#evaluate"}
            for i, (h, t) in enumerate(C.EVALUATE, start=1)
        ],
    }


def build(comp: dict, siblings: list[tuple[str, str]]) -> str:
    path = f"{BASE}{comp['slug']}/"
    url = f"{T.SITE}{path}"
    name = comp["name"]

    body = "\n\n".join([
        T.page_header(
            h1=comp["h1"],
            subtitle=comp["desc"],
            trail=[("Home", "/"), ("Compare", BASE), (comp["title"], path)],
            cta="Get Your Free Estimate",
        ),
        f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="post-meta">By {T.AUTHOR}, {T.BRAND} &middot; Updated {MODIFIED}</p>
            <h2>The Short Version</h2>
{paras(comp['short'])}
        </div>
    </section>""",
        T.section(f"Who {name} Is", paras(comp["who"])),
        T.section("Who AE Tax Advisors Is", paras(C.AE_INTRO)),
        T.section("Side-by-Side Comparison", table(name, comp["table"])),
        T.section(
            f"Where {name} Is Strong",
            bullets(comp["pros_them"])
            + f"\n            <h3>Where the model has limits</h3>\n"
            + bullets(comp["cons_them"]),
        ),
        T.section(
            "Which One Should You Choose?",
            f"            <p><strong>Choose {name}</strong> if {comp['choose_them']}.</p>\n"
            f"            <p><strong>Choose AE Tax Advisors</strong> if {comp['choose_us']}.</p>\n"
            "            <p>These are not mutually exclusive. Plenty of clients use a specialist "
            "for the engineering work on a complex asset and AE Tax Advisors for the strategy, "
            "the filings, and the return. We are glad to work from someone else's study.</p>",
        ),
        T.section("Why Clients Choose AE Tax Advisors", bullets(C.AE_WHY)),
        f"""    <section class="content-section fade-in-section" id="evaluate">
        <div class="container narrow">
            <h2>How to Evaluate Any Provider, Including Us</h2>
            <p>Whichever firm you engage, these six questions separate a defensible
            engagement from a report that will not hold up. Ask them of {name}, ask them
            of us, and compare the answers rather than the marketing.</p>
{numbered(C.EVALUATE)}
        </div>
    </section>""",
        T.faq_section(comp["faqs"]),
        T.related_section(
            siblings + [
                ("/pricing/", "AE Tax Advisors Pricing"),
                ("/case-studies/", "Case Studies: Real Tax Planning Results"),
                ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
            ],
            "Keep Comparing",
        ),
    ])

    schemas = [
        T.article_schema(
            title=comp["h1"],
            description=comp["desc"],
            url=url,
            published=PUBLISHED,
            modified=MODIFIED,
            section="Comparison",
        ),
        T.faq_schema(comp["faqs"]),
        howto_schema(url),
        T.breadcrumb_schema([("Home", "/"), ("Compare", BASE), (comp["title"], path)]),
    ]

    return T.build_page(
        title=comp["title"] + " | AE Tax Advisors",
        description=comp["desc"],
        path=path,
        body=body,
        schemas=schemas,
        published=PUBLISHED,
        modified=MODIFIED,
    )


def main() -> int:
    all_slugs = [(c["slug"], c["name"]) for c in C.COMPETITORS]
    for i, comp in enumerate(C.COMPETITORS):
        sibs = [
            (f"{BASE}{s}/", f"{n} vs AE Tax Advisors")
            for s, n in all_slugs[i + 1:] + all_slugs[:i]
        ][:3]
        html = build(comp, sibs)
        out = T.write_page(f"{BASE}{comp['slug']}", html)
        words = len(T.strip_tags(html.split("<main>")[1].split("</main>")[0]).split())
        flag = "" if words >= 1500 else "  << UNDER 1500"
        print(f"{words:>5} words  {out.relative_to(T.ROOT)}{flag}")
    print(f"\n{len(C.COMPETITORS)} comparison pages built.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
