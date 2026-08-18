#!/usr/bin/env python3
"""Surface the topic-cluster pillars on the /guides/ hub.

The pillars are already linked from their spokes, but /guides/ is the page a
reader lands on looking for the long-form material, so the pillars belong
there too. Rewritten in place on each run rather than appended, so the list
stays current without duplicating.
"""

from __future__ import annotations

import importlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MARKER = "cluster-pillar-index"
MODULES = [f"cluster_c{i}" for i in range(1, 9)]

BLURBS = {
    "s-corp": "Payroll tax, reasonable compensation, and where the savings actually stop.",
    "high-income": "What applies at $500K to $1M of profit, in the order it should be worked.",
    "cost-seg": "Accelerated depreciation on property you already own.",
    "entity": "The structure that determines what every other strategy can do.",
    "retirement": "The largest deduction most profitable owners will ever access.",
    "real-estate": "Using property depreciation against operating business income.",
    "planning-vs-prep": "Why compliance and strategy are different engagements.",
    "exit": "Selling, passing on, or restructuring the business, and the tax that turns on it.",
}


def block(clusters) -> str:
    items = []
    for c in clusters:
        blurb = BLURBS.get(c.key, "")
        items.append(
            f'                <li><a href="{c.href}"><strong>{c.label}</strong></a>'
            f"<br>{blurb}</li>"
        )
    body = "\n".join(items)
    return f"""    <section class="content-section fade-in-section {MARKER}">
        <div class="container narrow">
            <h2>Tax Strategy Pillar Guides</h2>
            <p>Eight complete guides for business owners at $500,000 or more of profit.
            Each links to the full series of supporting articles on that topic.</p>
            <ul class="related-links">
{body}
            </ul>
        </div>
    </section>"""


def main() -> int:
    clusters = []
    for name in MODULES:
        try:
            mod = importlib.import_module(name)
        except ModuleNotFoundError:
            continue
        clusters.append(mod.CLUSTER)
    if not clusters:
        print("no clusters found")
        return 1

    path = ROOT / "guides" / "index.html"
    if not path.exists():
        print("guides/index.html missing")
        return 1

    html = path.read_text(encoding="utf-8")
    new = block(clusters)

    if MARKER in html:
        pattern = re.compile(
            r'    <section class="content-section fade-in-section '
            + re.escape(MARKER)
            + r'">.*?\n    </section>',
            re.S,
        )
        updated = pattern.sub(lambda _: new, html, count=1)
        action = "refreshed"
    else:
        updated = html.replace("</main>", new + "\n    </main>", 1)
        action = "injected"

    if updated == html:
        print("guides hub: unchanged")
        return 0
    path.write_text(updated, encoding="utf-8")
    print(f"guides hub: {action} {len(clusters)} pillar links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
