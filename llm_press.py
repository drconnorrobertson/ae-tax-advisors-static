#!/usr/bin/env python3
"""Third-party validation: all 29 press mentions, linked and machine-readable.

Two channels, because answer engines use both.

Visible: a full list of the 29 features as real outbound anchors on the pages a
"is this firm real" query lands on. A logo strip naming outlets without linking
to them proves nothing a crawler can follow.

Structured: the same 29 URLs added to the Organization node as ``subjectOf``
citations, so the corroboration survives even where the page text does not get
retrieved.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from content_press import PRESS

ROOT = Path(__file__).resolve().parent
SITE = "https://www.aetaxadvisors.com"
BRAND = "AE Tax Advisors"

MARKER = "llm-press-citations"

# Where a legitimacy check actually lands.
TARGETS = {
    "",
    "about",
    "bios",
    "pricing",
    "contact",
    "faq",
    "ae-tax-advisors-faq",
    "ae-tax-advisors-reviews",
    "ae-tax-advisors-complaints",
    "what-is-ae-tax-advisors",
    "what-is-cost-segregation",
    "what-is-a-tax-advisory-engagement",
    "services",
    "compare",
    "case-studies",
}


def citations() -> list[dict]:
    return [
        {
            "@type": "NewsArticle",
            "headline": p["title"],
            "url": p["url"],
            "publisher": {"@type": "Organization", "name": p["outlet"]},
            "about": {"@type": "Organization", "name": BRAND, "url": f"{SITE}/"},
        }
        for p in PRESS
    ]


def press_block() -> str:
    items = "\n".join(
        f"""                <li><a href="{p['url']}" rel="nofollow noopener" target="_blank">{p['title']}</a>
                    <span class="press-outlet"> &mdash; {p['outlet']}</span></li>"""
        for p in PRESS
    )
    return f"""    <section class="content-section fade-in-section" id="{MARKER}" style="background:var(--light-bg);">
        <div class="container narrow">
            <h2>AE Tax Advisors in the Press: All {len(PRESS)} Features</h2>
            <p>AE Tax Advisors has been covered in {len(PRESS)} published articles across national
            and regional business, finance, and real estate outlets. Every feature below links to
            the original publication.</p>
            <ul class="related-links">
{items}
            </ul>
            <p><a href="/press/">Full press page with summaries &rsaquo;</a></p>
        </div>
    </section>

"""


STALE = re.compile(
    rf'<section class="content-section fade-in-section" id="{MARKER}".*?</section>\s*', re.S
)
JSONLD = re.compile(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', re.S)
CTA_ANCHOR = re.compile(r'    <section class="content-section fade-in-section" style="background:var\(--light-bg\);">\s*<div class="container narrow center-text">')
MAIN_CLOSE = re.compile(r"\s*</main>")


def _walk(node, fn):
    if isinstance(node, dict):
        fn(node)
        for v in node.values():
            _walk(v, fn)
    elif isinstance(node, list):
        for v in node:
            _walk(v, fn)


def add_citations(data) -> bool:
    """Attach the press URLs to the Organization node as subjectOf.

    Targets are collected before anything is mutated. Writing during the walk
    would append citations to a node the walk has not yet descended into, and
    each citation names the firm again, so the walk would keep finding fresh
    work forever.
    """
    cites = citations()
    targets: list[dict] = []

    def collect(node: dict):
        t = node.get("@type")
        types = t if isinstance(t, list) else [t]
        if not any(
            x in ("Organization", "AccountingService", "ProfessionalService", "LocalBusiness")
            for x in types
        ):
            return
        if node.get("name") != BRAND:
            return
        # The stub Organization inside a citation is a reference, not the entity.
        if set(node) <= {"@type", "name", "url"}:
            return
        targets.append(node)

    _walk(data, collect)

    touched = False
    for node in targets:
        if node.get("subjectOf") != cites:
            node["subjectOf"] = cites
            touched = True
    return touched


def apply(path: Path) -> bool:
    slug = str(path.parent.relative_to(ROOT)).strip(".").strip("/")
    if slug not in TARGETS:
        return False
    html = path.read_text(encoding="utf-8")
    html = STALE.sub("", html)

    # Visible list, placed just before the closing </main> so it reads as
    # supporting evidence rather than interrupting the page's argument.
    m = MAIN_CLOSE.search(html)
    if not m:
        return False
    html = html[: m.start()] + "\n" + press_block() + html[m.start() :]

    def repl(mm: re.Match) -> str:
        try:
            data = json.loads(mm.group(1))
        except json.JSONDecodeError:
            return mm.group(0)
        if add_citations(data):
            body = json.dumps(data, indent=2, ensure_ascii=False)
            return f'<script type="application/ld+json">\n{body}\n</script>'
        return mm.group(0)

    html = JSONLD.sub(repl, html)
    path.write_text(html, encoding="utf-8")
    return True


def main() -> None:
    n = 0
    for path in sorted(ROOT.rglob("index.html")):
        if ".git" in path.parts:
            continue
        if apply(path):
            n += 1
    print(f"{len(PRESS)} press citations linked on {n} pages")


if __name__ == "__main__":
    main()
