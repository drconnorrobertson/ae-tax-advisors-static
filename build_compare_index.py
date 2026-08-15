#!/usr/bin/env python3
"""Rebuild /compare/ as a complete, grouped index of every comparison page."""

from __future__ import annotations

import html as _html
import re
import sys
from pathlib import Path

import site_template as T

BASE = "/compare/"
OUT = T.ROOT / "compare"
PUBLISHED = "2026-08-15"
MODIFIED = "2026-08-15"

H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.DOTALL)
DESC_RE = re.compile(r'<meta name="description" content="(.*?)"', re.DOTALL)

# Grouping keeps a 30-plus page index legible.
GROUPS = [
    ("Cost Segregation Specialists",
     ("kbkg", "re-cost-seg", "cssi", "madison-specs", "capstan", "bedford",
      "engineered-tax-services", "cost-seg-authority", "cost-seg-smart",
      "diy-cost-segregation")),
    ("National Accounting Firms",
     ("moss-adams", "cherry-bekaert", "kpmg", "deloitte")),
    ("Real Estate Tax Firms",
     ("hall-cpa", "the-real-estate-cpa", "advise-re", "tax-alchemy",
      "anderson-advisors", "mark-kohler", "wcg-cpas")),
    ("Software and Retail Preparers",
     ("turbotax", "hr-block")),
    ("Buyer's Guides",
     ("best-", "bnb-", "bnb-mastery")),
]


def collect() -> list[dict]:
    items = []
    for d in sorted(OUT.iterdir()):
        if not d.is_dir():
            continue
        f = d / "index.html"
        if not f.exists():
            continue
        html = f.read_text(encoding="utf-8", errors="replace")
        hm = H1_RE.search(html)
        dm = DESC_RE.search(html)
        title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", hm.group(1))).strip() if hm else d.name
        desc = re.sub(r"\s+", " ", dm.group(1)).strip() if dm else ""
        items.append({
            "slug": d.name,
            "title": _html.unescape(title),
            "desc": _html.unescape(desc),
        })
    return items


def group_of(slug: str) -> str:
    for name, prefixes in GROUPS:
        if any(slug.startswith(p) for p in prefixes):
            return name
    return "More Comparisons"


def main() -> int:
    items = collect()
    for it in items:
        it["group"] = group_of(it["slug"])

    order = [g for g, _ in GROUPS] + ["More Comparisons"]
    sections = []
    for g in order:
        rows = sorted((i for i in items if i["group"] == g), key=lambda x: x["title"])
        if not rows:
            continue
        cards = "\n".join(
            f"""                <article class="cs-card">
                    <h3><a href="{BASE}{r['slug']}/">{T.esc(r['title'])}</a></h3>
                    <p>{T.esc(r['desc'][:165] + ('...' if len(r['desc']) > 165 else ''))}</p>
                    <a href="{BASE}{r['slug']}/" class="btn-secondary">Read the Comparison</a>
                </article>"""
            for r in rows
        )
        sections.append(f"""    <section class="content-section fade-in-section">
        <div class="container">
            <h2>{g} <span class="cs-count-inline">({len(rows)})</span></h2>
            <div class="cs-grid">
{cards}
            </div>
        </div>
    </section>""")

    body = f"""    <section class="page-header">
        <div class="container">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="/">Home</a> &rsaquo; <span>Compare</span>
            </nav>
            <h1>Compare Tax Advisors and Cost Segregation Firms</h1>
            <p class="subtitle">{len(items)} honest, side-by-side comparisons. Every firm
            listed here is legitimate and good at something. These pages explain what each
            one is actually built for so you can pick the right instrument.</p>
            <div class="cta-buttons">
                <a href="/discovery/" class="btn-cta btn-lg">Get Your Free Estimate</a>
            </div>
        </div>
    </section>

    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="definition-lead">Choosing a cost segregation or tax advisory firm comes
            down to one question: do you need a study, or do you need a strategy? Specialist
            engineering firms produce defensible studies and hand them to your CPA. National
            accounting firms bring breadth and assurance capability at enterprise scale.
            Advisory firms like AE Tax Advisors run the passive activity analysis, prepare the
            Form 3115, and file the return that uses the study.</p>
        </div>
    </section>

{chr(10).join(sections)}"""

    schemas = [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": "Compare Tax Advisors and Cost Segregation Firms",
            "description": (f"{len(items)} side-by-side comparisons of cost segregation "
                            "and tax advisory firms."),
            "url": f"{T.SITE}{BASE}",
            "publisher": {"@type": "Organization", "name": T.BRAND},
        },
        T.breadcrumb_schema([("Home", "/"), ("Compare", BASE)]),
    ]

    html = T.build_page(
        title=f"Compare Tax Advisors and Cost Seg Firms | AE Tax Advisors",
        description=(f"{len(items)} honest side-by-side comparisons of cost segregation and "
                     "tax advisory firms, covering methodology, pricing model, property fit, "
                     "and what each firm does after the study."),
        path=BASE,
        body=body,
        schemas=schemas,
        published=PUBLISHED,
        modified=MODIFIED,
        og_type="website",
    )
    (OUT / "index.html").write_text(html, encoding="utf-8")
    print(f"compare index rebuilt: {len(items)} comparisons")
    for g in order:
        n = sum(1 for i in items if i["group"] == g)
        if n:
            print(f"   {g}: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
