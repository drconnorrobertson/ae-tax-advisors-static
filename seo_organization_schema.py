#!/usr/bin/env python3
"""Convert every LocalBusiness-subtype schema block to Organization.

AE Tax Advisors serves clients nationwide. `ProfessionalService` and
`AccountingService` are both subtypes of `LocalBusiness` in schema.org, so they
signal local intent and can pull the site into local-pack style treatment. This
rewrites those blocks as `Organization`, which carries no locality signal, and
drops the LocalBusiness-only properties (openingHours, priceRange, areaServed
narrowed to states, geo) while keeping the office address as a plain
PostalAddress.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://www.aetaxadvisors.com"

LD_RE = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.DOTALL)

LOCAL_TYPES = {
    "LocalBusiness", "ProfessionalService", "AccountingService",
    "FinancialService", "LegalService", "Store",
}

# Properties that only make sense for a physical, locally-serving business.
LOCAL_ONLY_PROPS = {
    "openingHours", "openingHoursSpecification", "priceRange", "geo",
    "hasMap", "currenciesAccepted", "paymentAccepted", "branchOf",
    "isicV4", "smokingAllowed", "servesCuisine", "latitude", "longitude",
}


def is_local(node: dict) -> bool:
    t = node.get("@type")
    types = t if isinstance(t, list) else [t]
    return any(x in LOCAL_TYPES for x in types if isinstance(x, str))


def convert(node: dict) -> dict:
    """Rewrite a LocalBusiness-flavoured node as a national Organization."""
    out = {k: v for k, v in node.items() if k not in LOCAL_ONLY_PROPS}
    out["@type"] = "Organization"

    # A nationwide advisory firm serves the whole country, not a state list.
    out["areaServed"] = {"@type": "Country", "name": "United States"}

    # Keep the office address, but make clear it is a corporate location rather
    # than a service area.
    if "address" in out and isinstance(out["address"], dict):
        out["address"]["@type"] = "PostalAddress"

    # Order keys so @context/@type lead.
    ordered = {}
    for key in ("@context", "@type", "name", "alternateName", "description",
                "url", "logo", "image", "telephone", "email", "address"):
        if key in out:
            ordered[key] = out.pop(key)
    ordered.update(out)
    return ordered


def process(path: Path) -> bool:
    html = path.read_text(encoding="utf-8", errors="replace")
    changed = False

    def repl(m: re.Match) -> str:
        nonlocal changed
        try:
            data = json.loads(m.group(2))
        except json.JSONDecodeError:
            return m.group(0)

        def walk(node):
            nonlocal changed
            if isinstance(node, list):
                return [walk(x) for x in node]
            if isinstance(node, dict):
                if is_local(node):
                    changed = True
                    node = convert(node)
                return {k: walk(v) for k, v in node.items()}
            return node

        new = walk(data)
        if not changed:
            return m.group(0)
        return m.group(1) + "\n" + json.dumps(new, indent=2, ensure_ascii=False) + "\n" + m.group(3)

    new_html = LD_RE.sub(repl, html)
    if changed and new_html != html:
        path.write_text(new_html, encoding="utf-8")
        return True
    return False


def main() -> int:
    n = 0
    for p in sorted(ROOT.rglob("*.html")):
        if ".git" in p.parts:
            continue
        if process(p):
            n += 1
    print(f"pages converted to Organization schema: {n}")

    # Report anything left over.
    left = 0
    for p in ROOT.rglob("*.html"):
        if ".git" in p.parts:
            continue
        s = p.read_text(encoding="utf-8", errors="replace")
        if re.search(r'"@type":\s*(\[[^\]]*)?"(?:LocalBusiness|ProfessionalService|AccountingService)"', s):
            left += 1
    print(f"pages still carrying a LocalBusiness subtype: {left}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
