#!/usr/bin/env python3
"""Make pre-existing FAQPage schema match visible page content.

Google requires the question and answer text in FAQPage markup to be visible to
the user. Some legacy pages carry FAQ schema with no corresponding on-page
content, and a few carry two FAQPage blocks. This renders the schema's Q&As as a
visible section and collapses duplicate FAQPage blocks into one.
"""

from __future__ import annotations

import html as _html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

LD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")
MAIN_RE = re.compile(r"(<main[^>]*>)(.*?)(</main>)", re.DOTALL)


def visible_text(html: str) -> str:
    m = MAIN_RE.search(html)
    src = m.group(2) if m else html
    return re.sub(r"\s+", " ", _html.unescape(TAG_RE.sub(" ", src)))


def entities(obj) -> list[dict]:
    ents = obj.get("mainEntity")
    if isinstance(ents, dict):
        ents = [ents]
    if not isinstance(ents, list):
        return []
    return [e for e in ents if isinstance(e, dict) and e.get("name")]


def answer_text(ent: dict) -> str:
    ans = ent.get("acceptedAnswer") or {}
    if isinstance(ans, list):
        ans = ans[0] if ans else {}
    if not isinstance(ans, dict):
        return ""
    return str(ans.get("text", ""))


def render(faqs: list[tuple[str, str]]) -> str:
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


def main() -> int:
    fixed = deduped = 0
    for path in sorted(ROOT.rglob("index.html")):
        if any(x in path.parts for x in (".git", "assets", "blog-staging")):
            continue
        html = path.read_text(encoding="utf-8", errors="replace")
        if "FAQPage" not in html:
            continue

        blocks = []  # (match, parsed)
        for m in LD_RE.finditer(html):
            try:
                data = json.loads(m.group(1))
            except json.JSONDecodeError:
                continue
            if isinstance(data, dict) and data.get("@type") == "FAQPage":
                blocks.append((m, data))
        if not blocks:
            continue

        # Collapse duplicate FAQPage blocks, keeping the richest one.
        if len(blocks) > 1:
            keep = max(blocks, key=lambda b: len(entities(b[1])))
            drop = [b[0] for b in blocks if b is not keep]
            for m in sorted(drop, key=lambda x: x.start(), reverse=True):
                html = html[: m.start()] + html[m.end():]
            blocks = [keep]
            deduped += 1
            # Offsets shifted; re-find the surviving block.
            for m in LD_RE.finditer(html):
                try:
                    data = json.loads(m.group(1))
                except json.JSONDecodeError:
                    continue
                if isinstance(data, dict) and data.get("@type") == "FAQPage":
                    blocks = [(m, data)]
                    break

        _, data = blocks[0]
        ents = entities(data)
        if not ents:
            continue

        vis = visible_text(html)
        missing = [
            (str(e["name"]), answer_text(e))
            for e in ents
            if re.sub(r"\s+", " ", _html.unescape(str(e["name"]))) not in vis
        ]
        if not missing:
            if deduped:
                path.write_text(html, encoding="utf-8")
            continue

        mm = MAIN_RE.search(html)
        if not mm:
            continue
        insert_at = mm.end(2)
        html = html[:insert_at] + render(missing) + html[insert_at:]
        path.write_text(html, encoding="utf-8")
        fixed += 1

    print(f"pages given visible FAQ content to match schema: {fixed}")
    print(f"pages with duplicate FAQPage blocks collapsed:   {deduped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
