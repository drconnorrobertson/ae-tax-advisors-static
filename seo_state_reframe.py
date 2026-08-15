#!/usr/bin/env python3
"""Reframe state pages away from local-search intent.

AE Tax Advisors is a national firm. These pages exist to show expertise serving
investors who own property in a given state, not to compete in that state's
local pack. This rewrites "Cost Segregation Study in <State>" style phrasing to
"Cost Segregation for <State> Real Estate Investors", strips "near me" and
local-service language, and removes any state-narrowed areaServed from schema.
"""

from __future__ import annotations

import html as _html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

STATES = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
    "Washington", "West Virginia", "Wisconsin", "Wyoming",
]
SLUG_TO_STATE = {s.lower().replace(" ", "-"): s for s in STATES}

LD_RE = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.DOTALL)


def rewrites(state: str) -> list[tuple[re.Pattern, str]]:
    s = re.escape(state)
    return [
        # Headline / title phrasing
        (re.compile(rf"Cost Segregation Study in {s}\b"),
         f"Cost Segregation for {state} Real Estate Investors"),
        (re.compile(rf"Cost Segregation Studies in {s}\b"),
         f"Cost Segregation for {state} Real Estate Investors"),
        (re.compile(rf"Cost Segregation in {s}\b"),
         f"Cost Segregation for {state} Real Estate Investors"),
        (re.compile(rf"\b{s} Tax Advisor\b"),
         f"Tax Advisors for {state} Investors"),
        (re.compile(rf"\bTax Advisor in {s}\b"),
         f"Tax Advisors for {state} Investors"),
        (re.compile(rf"\bCPA in {s}\b"), f"CPA for {state} Investors"),
        (re.compile(rf"\bTax Planning in {s}\b"),
         f"Tax Planning for {state} Investors"),
        # Local-service language
        (re.compile(r"\bnear me\b", re.I), "for investors nationwide"),
        (re.compile(rf"\bserving the {s} area\b", re.I),
         f"working with investors who own property in {state}"),
        (re.compile(rf"\blocal {s}\b", re.I), state),
        (re.compile(r"\byour local tax (advisor|firm|cpa)\b", re.I),
         r"your dedicated tax \1"),
    ]


def clean_schema(html: str, state: str) -> str:
    """Drop state-narrowed areaServed so the markup reads as national."""

    def repl(m: re.Match) -> str:
        try:
            data = json.loads(m.group(2))
        except json.JSONDecodeError:
            return m.group(0)

        def walk(node):
            if isinstance(node, list):
                return [walk(x) for x in node]
            if isinstance(node, dict):
                if node.get("@type") == "Organization" and "areaServed" in node:
                    node["areaServed"] = {"@type": "Country", "name": "United States"}
                return {k: walk(v) for k, v in node.items()}
            return node

        return (m.group(1) + "\n"
                + json.dumps(walk(data), indent=2, ensure_ascii=False)
                + "\n" + m.group(3))

    return LD_RE.sub(repl, html)


def main() -> int:
    changed = 0
    for slug, state in SLUG_TO_STATE.items():
        path = ROOT / slug / "index.html"
        if not path.exists():
            continue
        html = path.read_text(encoding="utf-8")
        before = html
        for pat, repl in rewrites(state):
            html = pat.sub(repl, html)
        html = clean_schema(html, state)
        if html != before:
            path.write_text(html, encoding="utf-8")
            changed += 1
            print(f"reframed: /{slug}/")
    print(f"\n{changed} state pages reframed for national positioning.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
