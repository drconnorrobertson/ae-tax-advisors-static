#!/usr/bin/env python3
"""Keep utility and duplicate URLs out of the search index.

The pages remain live for clients and campaigns. Search engines can still crawl
their links, but the primary sitemap is reserved for substantive search pages.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROBOTS = re.compile(r'<meta name="robots" content="[^"]*">', re.I)
CANONICAL = re.compile(r'<link rel="canonical" href="[^"]*">', re.I)

NOINDEX = {
    "alicia-survey", "alicia-zoom", "christina-zoom", "jack-zoom",
    "krister-zoom", "mark-zoom", "nick-zoom", "connor-zoom",
    "ashley-30min", "ashley-45min", "ashley-60min",
    "alicia-30min", "alicia-45min", "alicia-60min",
    "christina-30min", "christina-45min", "christina-60min",
    "thank-you", "onboarding", "onboarding-call",
    "ae-tax-advisors-onboarding-calendar", "ae-tax-advisors-onboarding-form",
    "ae-tax-advisors-onboarding-call-today",
    "ae-tax-advisors-onboarding-call-today-2",
    "ae-tax-advisors-onboarding-call-today-3",
    "check-in", "precall", "7-day-recap", "7-day-followup",
    "30-day-recap", "30-day-followup", "30-minute-consultation",
    "45-minute-consultation", "60-minute-consultation", "zoom-consultation",
    "connor-1-1", "discovery-facebook", "discovery-youtube",
    "blog/test-delete-me", "blog/test-push-verification",
    "christina-30", "christina-60", "tools/property-review-prep",
}

# These thin legacy URLs overlap a stronger page. Canonicals consolidate their
# signals while preserving the old URL for visitors and inbound links.
CANONICAL_TARGETS = {
    "discover": "/discovery/",
    "schedule-a-real-estate-tax-consultation": "/discovery/",
    "schedule-a-real-estate-tax-consultation-2": "/discovery/",
    "strategy": "/advanced-tax-planning-services/",
    "focused-strategies": "/advanced-tax-planning-services/",
    "guide": "/guides/",
    "resources-2": "/guides/",
    "tax-services": "/services/",
    "long-term-rental-tax-planning-and-preparation-3": "/long-term-rental-tax-planning-and-preparation/",
    "tax-resolution-services-2": "/tax-compliance-irs-representation/",
    "cost-segregation-for-car-wash": "/cost-segregation-car-wash/",
}


def set_noindex(path: Path) -> bool:
    source = path.read_text(encoding="utf-8")
    tag = '<meta name="robots" content="noindex, follow">'
    updated = ROBOTS.sub(tag, source, count=1) if ROBOTS.search(source) else source.replace(
        "</title>", "</title>\n    " + tag, 1
    )
    if updated == source:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def set_canonical(path: Path, target: str) -> bool:
    source = path.read_text(encoding="utf-8")
    tag = f'<link rel="canonical" href="https://www.aetaxadvisors.com{target}">'
    if not CANONICAL.search(source):
        raise RuntimeError(f"missing canonical: {path}")
    updated = CANONICAL.sub(tag, source, count=1)
    if updated == source:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    changed = 0
    for slug in sorted(NOINDEX):
        path = ROOT / slug / "index.html"
        if not path.exists():
            raise FileNotFoundError(path)
        changed += set_noindex(path)
    for slug, target in sorted(CANONICAL_TARGETS.items()):
        path = ROOT / slug / "index.html"
        if not path.exists():
            raise FileNotFoundError(path)
        changed += set_canonical(path, target)
    print(f"search hygiene updated: {changed} pages")
    print(f"utility pages noindexed: {len(NOINDEX)}")
    print(f"legacy URLs consolidated: {len(CANONICAL_TARGETS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
