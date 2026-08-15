#!/usr/bin/env python3
"""SEO pass over existing pages.

For every page that lacks them, this adds:
  * a visible FAQ block plus matching FAQPage schema (schema mirrors visible
    text, which is what Google requires),
  * a definition-style opening paragraph for AI overview extraction,
  * a block of 3 to 5 related internal links,
  * an improved meta description where the existing one is missing or weak,
  * "2026" in the title where the page is year-sensitive and has no year.

Run with --dry to preview counts without writing.
"""

from __future__ import annotations

import html as _html
import json
import re
import sys
from pathlib import Path

import seo_topics as TOPICS
import site_template as T

ROOT = Path(__file__).resolve().parent

# blog-staging is not in the sitemap and duplicates live content; it is handled
# separately (noindex) rather than optimized.
SKIP_DIR_PARTS = {".git", "assets", "blog-staging", "case-studies"}

# Pages that should not receive marketing FAQ blocks.
SKIP_SLUG_PATTERNS = re.compile(
    r"(^|/)(privacy-policy|terms-of-service|disclaimer|thank-you|thanks|"
    r"404|sitemap|search|unsubscribe|confirm|calendar|onboarding-call-today|"
    r"[a-z]+-(30|45|60)min|[a-z]+-zoom|[a-z]+-survey)(/|$)"
)

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
DESC_RE = re.compile(r'(<meta name="description" content=")(.*?)(">)', re.DOTALL)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.DOTALL)
H2_RE = re.compile(r"<h[23][^>]*>(.*?)</h[23]>", re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")
FIRST_P_RE = re.compile(r"<p[^>]*>(.*?)</p>", re.DOTALL)

# Year-sensitive pages benefit from a year in the title.
YEAR_WORTHY = re.compile(
    r"\b(guide|rules?|limits?|rates?|changes?|update|strategy|strategies|"
    r"deduction|depreciation|checklist|explained|how to|what is|planning|"
    r"comparison|vs\b|best|top)\b", re.I
)
HAS_YEAR = re.compile(r"\b(20\d\d)\b")


def text_of(markup: str) -> str:
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", markup)).strip()


def page_files() -> list[Path]:
    out = []
    for p in ROOT.rglob("index.html"):
        parts = p.relative_to(ROOT).parts
        if any(x in SKIP_DIR_PARTS for x in parts):
            continue
        rel = "/" + "/".join(parts[:-1])
        if SKIP_SLUG_PATTERNS.search(rel + "/"):
            continue
        out.append(p)
    if (ROOT / "404.html").exists():
        pass
    return sorted(out)


TRAILING_CTA_RE = re.compile(
    r'\n\s*<section[^>]*class="[^"]*(?:post-cta|cta-section|content-section)[^"]*"[^>]*>'
    r'(?:(?!</section>).)*?(?:Schedule|Discovery|Consultation|Assessment|Talk Through)'
    r'.*?</section>',
    re.DOTALL,
)


def insert_point(html: str, bounds: tuple[int, int]) -> int:
    """End of <main>, but before a trailing CTA section if one is there."""
    inner = html[bounds[0]:bounds[1]]
    matches = list(TRAILING_CTA_RE.finditer(inner))
    if matches:
        last = matches[-1]
        # Only treat it as trailing if little follows it.
        if len(inner) - last.end() < 400:
            return bounds[0] + last.start()
    return bounds[1]


def main_bounds(html: str) -> tuple[int, int] | None:
    m = re.search(r"<main[^>]*>", html)
    if m:
        end = html.find("</main>", m.end())
        if end != -1:
            return m.end(), end
    # Pages built without a <main> element: treat everything between the site
    # header and the footer as the content region.
    hm = re.search(r"</header>", html)
    fm = re.search(r"<footer[^>]*>", html)
    if hm and fm and fm.start() > hm.end():
        return hm.end(), fm.start()
    return None


def build_faq_html(faqs: list[tuple[str, str]]) -> str:
    items = "\n".join(
        f"""                <div class="faq-item">
                    <h3>{_html.escape(q)}</h3>
                    <p>{a}</p>
                </div>"""
        for q, a in faqs
    )
    return f"""
    <section class="content-section fade-in-section" id="faq">
        <div class="container narrow">
            <h2>Frequently Asked Questions</h2>
{items}
        </div>
    </section>
"""


def build_links_html(links: list[tuple[str, str]]) -> str:
    items = "\n".join(
        f'                    <li><a href="{href}">{_html.escape(label)}</a></li>'
        for href, label in links
    )
    return f"""
    <section class="content-section fade-in-section">
        <div class="container narrow">
            <h2>Related Reading</h2>
            <ul class="related-links">
{items}
            </ul>
        </div>
    </section>
"""


def faq_schema_block(faqs: list[tuple[str, str]]) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": text_of(a)},
            }
            for q, a in faqs
        ],
    }
    return ('<script type="application/ld+json">\n'
            + json.dumps(data, indent=2, ensure_ascii=False)
            + "\n</script>\n")


def improve_description(current: str, topic: str, title: str, body_text: str) -> str | None:
    """Return a better description, or None to keep the current one."""
    cur = _html.unescape(current or "").strip()
    if 70 <= len(cur) <= 165:
        return None
    if len(cur) > 165:
        # Trim on a sentence or word boundary rather than mid-word.
        trimmed = cur[:162]
        cut = max(trimmed.rfind(". "), trimmed.rfind("? "))
        if cut > 90:
            return trimmed[: cut + 1]
        cut = trimmed.rfind(" ")
        return trimmed[:cut].rstrip(",;:") + "..."
    # Too short or missing: build one from the topic definition.
    definition = TOPICS.DEFINITIONS.get(topic, TOPICS.DEFINITIONS["firm"])
    clean_title = re.sub(r"\s*\|\s*AE Tax Advisors\s*$", "", title).strip()
    base = f"{clean_title}. {definition}"
    if len(base) > 165:
        trimmed = base[:162]
        cut = trimmed.rfind(" ")
        base = trimmed[:cut].rstrip(",;:") + "..."
    return base


def improve_title(title: str) -> str | None:
    """Add 2026 to year-sensitive titles that carry no year."""
    clean = re.sub(r"\s*\|\s*AE Tax Advisors\s*$", "", title).strip()
    if HAS_YEAR.search(clean):
        return None
    if not YEAR_WORTHY.search(clean):
        return None
    # Repair titles truncated mid-phrase, e.g. "... for Business Owners and".
    clean = re.sub(r"\s+(and|or|the|a|an|for|with|to|of|in)$", "", clean, flags=re.I)
    candidate = f"{clean} (2026)"
    if len(candidate) + len(" | AE Tax Advisors") > 70:
        # Too long with the brand: keep the year, drop the brand suffix.
        return candidate if len(candidate) <= 70 else None
    return f"{candidate} | AE Tax Advisors"


def process(path: Path, dry: bool) -> dict:
    html = path.read_text(encoding="utf-8", errors="replace")
    orig = html
    rel = "/" + "/".join(path.relative_to(ROOT).parts[:-1]) + "/"
    if rel == "//":
        rel = "/"
    slug = path.parent.name or "home"

    bounds = main_bounds(html)
    stats = {"faq": 0, "links": 0, "definition": 0, "desc": 0, "title": 0}

    tm = TITLE_RE.search(html)
    title = text_of(tm.group(1)) if tm else ""
    hm = H1_RE.search(html)
    h1 = text_of(hm.group(1)) if hm else ""
    headings = " ".join(text_of(x) for x in H2_RE.findall(html)[:25])
    body_text = text_of(html[bounds[0]:bounds[1]]) if bounds else text_of(html)

    topic = TOPICS.classify(title, h1, headings, body_text)

    # ---- title
    if tm:
        new_title = improve_title(title)
        if new_title and new_title != title:
            html = html[: tm.start(1)] + _html.escape(new_title, quote=False) + html[tm.end(1):]
            stats["title"] = 1
            # Keep og/twitter titles aligned with the document title.
            for prop in ('property="og:title"', 'name="twitter:title"'):
                html = re.sub(
                    r'(<meta ' + re.escape(prop) + r' content=")(.*?)(">)',
                    lambda m: m.group(1) + _html.escape(new_title, quote=True) + m.group(3),
                    html, count=1, flags=re.DOTALL,
                )

    # ---- meta description
    dm = DESC_RE.search(html)
    if dm:
        new_desc = improve_description(dm.group(2), topic, title, body_text)
        if new_desc:
            html = html[: dm.start(2)] + _html.escape(new_desc, quote=True) + html[dm.end(2):]
            stats["desc"] = 1
    else:
        new_desc = improve_description("", topic, title, body_text)
        head = re.search(r"</title>", html)
        if head and new_desc:
            ins = (f'\n    <meta name="description" content="'
                   f'{_html.escape(new_desc, quote=True)}">')
            html = html[: head.end()] + ins + html[head.end():]
            stats["desc"] = 1

    # Recompute bounds after head edits.
    bounds = main_bounds(html)

    # ---- definition lead paragraph
    already_definitional = False
    if bounds:
        first_ps = FIRST_P_RE.findall(html[bounds[0]:bounds[1]])[:3]
        for fp in first_ps:
            t = text_of(fp)
            if len(t) > 180 and re.match(
                r"^(A|An|The)?\s*[A-Z][^.]{0,80}\b(is|are|refers to|means)\b", t
            ):
                already_definitional = True
                break
    substantial = len(body_text.split()) >= 400

    if (bounds and "definition-lead" not in html
            and substantial and not already_definitional):
        inner = html[bounds[0]:bounds[1]]
        # Place after the first section heading if there is one, else at the top.
        definition = TOPICS.DEFINITIONS.get(topic, TOPICS.DEFINITIONS["firm"])
        block = f"""
    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="definition-lead">{definition}</p>
        </div>
    </section>
"""
        # Insert after the page header section when present so the masthead
        # stays first.
        ph = re.search(r'<section class="page-header">.*?</section>', inner, re.DOTALL)
        if ph:
            pos = bounds[0] + ph.end()
        else:
            pos = bounds[0]
        html = html[:pos] + block + html[pos:]
        stats["definition"] = 1
        bounds = main_bounds(html)

    # ---- FAQ block + schema
    if bounds and "FAQPage" not in html:
        faqs = TOPICS.faqs_for(topic, slug, n=4)
        ip = insert_point(html, bounds)
        html = html[:ip] + build_faq_html(faqs) + html[ip:]
        head_close = html.find("</head>")
        if head_close != -1:
            html = html[:head_close] + faq_schema_block(faqs) + html[head_close:]
        stats["faq"] = 1
        bounds = main_bounds(html)

    # ---- related links
    has_related = ("related-links" in html
                   or re.search(r">\s*Related (?:Reading|Articles|Resources|Guides)\s*<", html))
    if bounds and not has_related:
        links = TOPICS.links_for(topic, slug, rel, n=4)
        if links:
            ip = insert_point(html, bounds)
            html = html[:ip] + build_links_html(links) + html[ip:]
            stats["links"] = 1

    if html != orig and not dry:
        path.write_text(html, encoding="utf-8")
    stats["changed"] = int(html != orig)
    stats["topic"] = topic
    return stats


def main() -> int:
    dry = "--dry" in sys.argv
    files = page_files()
    totals = {"faq": 0, "links": 0, "definition": 0, "desc": 0, "title": 0, "changed": 0}
    topics: dict[str, int] = {}
    for p in files:
        s = process(p, dry)
        for k in totals:
            totals[k] += s.get(k, 0)
        topics[s["topic"]] = topics.get(s["topic"], 0) + 1

    print(("DRY RUN " if dry else "") + f"pages examined: {len(files)}")
    print(f"  FAQ blocks added:        {totals['faq']}")
    print(f"  Related link blocks:     {totals['links']}")
    print(f"  Definition paragraphs:   {totals['definition']}")
    print(f"  Descriptions improved:   {totals['desc']}")
    print(f"  Titles updated with year:{totals['title']}")
    print(f"  Pages changed:           {totals['changed']}")
    print("\nTopic distribution:")
    for k, v in sorted(topics.items(), key=lambda x: -x[1]):
        print(f"  {TOPICS.TOPICS[k][1]:<28} {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
