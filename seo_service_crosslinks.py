#!/usr/bin/env python3
"""Cross-link service pages to relevant blog posts and case studies.

Each service page gets a block linking to on-topic articles and case studies,
chosen by matching the page's topic against the library rather than by hand.
"""

from __future__ import annotations

import html as _html
import re
import sys
from pathlib import Path

import seo_topics as TOPICS

ROOT = Path(__file__).resolve().parent

H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.DOTALL)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
DESC_RE = re.compile(r'<meta name="description" content="(.*?)"', re.DOTALL)
H2_RE = re.compile(r"<h[23][^>]*>(.*?)</h[23]>", re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")
MAIN_RE = re.compile(r"(<main[^>]*>)(.*?)(</main>)", re.DOTALL)
MARKER = 'id="explore-more"'

SERVICE_PAGES = [
    "cost-segregation-study", "business-owner-small-business-tax",
    "real-estate-tax-planning", "short-term-rental-tax-strategy",
    "rental-property-tax-planning", "real-estate-investor-cpa",
    "retirement-exit-ma-tax-strategy", "individual-tax-planning-high-earners",
    "estate-trust-wealth-transfer", "tax-compliance-irs-representation",
    "multi-state-global-tax", "equipment-leasing-section-179",
    "deferred-equity-compensation",
    "audit-defense-compliance", "advanced-tax-planning-services",
    "cost-segregation-studies-for-real-estate-investors",
    "services/bookkeeping", "services/entity-structuring",
    "services/tax-planning", "services/cost-segregation", "services",
    "cost-segregation-for-multifamily", "cost-segregation-for-self-storage",
    "cost-segregation-for-hotel-motel", "cost-segregation-for-restaurant",
    "cost-segregation-for-car-wash", "cost-segregation-for-warehouse",
    "cost-segregation-for-medical-office", "cost-segregation-for-dental-office",
    "cost-segregation-for-retail", "cost-segregation-for-office-building",
]


def text_of(s: str) -> str:
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", s)).strip()


def index_library() -> tuple[dict, dict]:
    """Map topic -> [(url, title)] for blog posts and case studies."""
    blog: dict[str, list] = {}
    cases: dict[str, list] = {}

    for base, bucket in (("blog", blog), ("case-studies", cases)):
        d = ROOT / base
        if not d.is_dir():
            continue
        for sub in sorted(d.iterdir()):
            if not sub.is_dir():
                continue
            f = sub / "index.html"
            if not f.exists():
                continue
            html = f.read_text(encoding="utf-8", errors="replace")
            hm = H1_RE.search(html) or TITLE_RE.search(html)
            title = _html.unescape(text_of(hm.group(1))).split(" | AE Tax")[0] if hm else sub.name
            headings = " ".join(text_of(x) for x in H2_RE.findall(html)[:15])
            topic = TOPICS.classify(title, title, headings, text_of(html)[:3000])
            bucket.setdefault(topic, []).append((f"/{base}/{sub.name}/", title))
    return blog, cases


def block(articles, studies) -> str:
    a = "\n".join(
        f'                    <li><a href="{u}">{_html.escape(t)}</a></li>'
        for u, t in articles
    )
    c = "\n".join(
        f'                    <li><a href="{u}">{_html.escape(t)}</a></li>'
        for u, t in studies
    )
    parts = []
    if a:
        parts.append(f"""            <h3>Related Articles</h3>
            <ul class="related-links">
{a}
            </ul>""")
    if c:
        parts.append(f"""            <h3>Related Case Studies</h3>
            <ul class="related-links">
{c}
            </ul>""")
    if not parts:
        return ""
    return f"""
    <section class="content-section fade-in-section" {MARKER}>
        <div class="container narrow">
            <h2>Explore This Topic Further</h2>
{chr(10).join(parts)}
            <div class="center-cta" style="margin-top:22px;">
                <a href="/case-studies/" class="btn-secondary">Browse All Case Studies</a>
            </div>
        </div>
    </section>
"""


def main() -> int:
    blog, cases = index_library()
    print(f"library indexed: {sum(len(v) for v in blog.values())} posts, "
          f"{sum(len(v) for v in cases.values())} case studies")

    added = 0
    for slug in SERVICE_PAGES:
        path = ROOT / slug / "index.html"
        if not path.exists():
            continue
        html = path.read_text(encoding="utf-8")
        if MARKER in html:
            continue

        hm = H1_RE.search(html) or TITLE_RE.search(html)
        title = text_of(hm.group(1)) if hm else slug
        headings = " ".join(text_of(x) for x in H2_RE.findall(html)[:15])
        topic = TOPICS.classify(title, title, headings, text_of(html)[:3000])

        # Stable rotation so neighbouring service pages do not show the same list.
        seed = sum(ord(ch) for ch in slug)
        pool_a = blog.get(topic, []) or blog.get("cost_seg", [])
        pool_c = cases.get(topic, []) or cases.get("cost_seg", [])
        pick_a = [pool_a[(seed + i) % len(pool_a)] for i in range(min(5, len(pool_a)))] if pool_a else []
        pick_c = [pool_c[(seed + i) % len(pool_c)] for i in range(min(4, len(pool_c)))] if pool_c else []

        b = block(pick_a, pick_c)
        if not b:
            continue

        m = MAIN_RE.search(html)
        if m:
            at = m.end(2)
        else:
            at = html.rfind("<footer")
            if at == -1:
                continue
        path.write_text(html[:at] + b + html[at:], encoding="utf-8")
        added += 1
        print(f"  cross-linked ({TOPICS.TOPICS[topic][1]}): /{slug}/")

    print(f"\n{added} service pages cross-linked to blog posts and case studies.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
