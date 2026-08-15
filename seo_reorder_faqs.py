#!/usr/bin/env python3
"""Rewrite the FAQ blocks injected by seo_enhance so the most page-relevant
question leads, and keep the FAQPage schema in sync with the visible text.

Only touches blocks this project injected (identified by `id="faq"`), so
hand-written FAQ sections elsewhere on the site are left alone.
"""

from __future__ import annotations

import html as _html
import json
import re
import sys
from pathlib import Path

import seo_topics as TOPICS
import seo_enhance as E

ROOT = Path(__file__).resolve().parent

INJECTED_FAQ = re.compile(
    r'\n    <section class="content-section fade-in-section" id="faq">\n'
    r'        <div class="container narrow">\n'
    r"            <h2>Frequently Asked Questions</h2>\n"
    r".*?\n"
    r"        </div>\n"
    r"    </section>\n",
    re.DOTALL,
)
FAQ_SCHEMA = re.compile(
    r'<script type="application/ld\+json">\s*\{\s*"@context":\s*"https://schema\.org",'
    r'\s*"@type":\s*"FAQPage".*?</script>\n?',
    re.DOTALL,
)


def main() -> int:
    changed = 0
    for path in sorted(ROOT.rglob("index.html")):
        if any(x in path.parts for x in (".git", "assets", "blog-staging", "case-studies")):
            continue
        html = path.read_text(encoding="utf-8", errors="replace")
        m = INJECTED_FAQ.search(html)
        if not m:
            continue

        # Build the ranking context from the page WITHOUT its current FAQ
        # block: the existing questions are h3 headings, and including them
        # would make every question rank against itself.
        without_faq = html[: m.start()] + html[m.end():]

        tm = E.TITLE_RE.search(without_faq)
        hm = E.H1_RE.search(without_faq)
        title = E.text_of(tm.group(1)) if tm else ""
        h1 = E.text_of(hm.group(1)) if hm else ""
        headings = " ".join(E.text_of(x) for x in E.H2_RE.findall(without_faq)[:25])
        bounds = E.main_bounds(without_faq)
        body = E.text_of(without_faq[bounds[0]:bounds[1]]) if bounds else ""
        topic = TOPICS.classify(title, h1, headings, body)
        slug = path.parent.name or "home"

        faqs = TOPICS.faqs_for(topic, slug, n=4, context=f"{title} {h1} {headings}")

        html = html[: m.start()] + E.build_faq_html(faqs) + html[m.end():]

        sm = FAQ_SCHEMA.search(html)
        if sm:
            html = html[: sm.start()] + E.faq_schema_block(faqs) + html[sm.end():]

        path.write_text(html, encoding="utf-8")
        changed += 1

    print(f"FAQ blocks reordered by relevance: {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
