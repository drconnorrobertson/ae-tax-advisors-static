#!/usr/bin/env python3
"""Build the long-tail posts.

Where a topic already lives at an existing URL, the new content upgrades that
URL in place rather than creating a competing duplicate. REMAP holds those
redirects, and every internal reference is rewritten to match.
"""
import re
import shutil
from pathlib import Path

import seo_render
import seo_posts_depreciation as dep
import seo_posts_realestate as re_
import seo_posts_business as biz

# new slug -> existing URL that already ranks for this topic
REMAP = {
    "bonus-depreciation-2026": "bonus-depreciation-2025-2026-real-estate-investors",
    "seven-day-rule-short-term-rental": "what-is-the-7-day-rule-for-short-term-rentals",
    "reverse-1031-exchange": "reverse-1031-exchange-explained",
    "ptet-pass-through-entity-tax-election": "pass-through-entity-tax-election-salt-cap-workaround",
}

# title/description tuning where the existing URL implies a narrower intent
OVERRIDES = {
    "bonus-depreciation-2025-2026-real-estate-investors": {
        "title_tag": "Bonus Depreciation 2025-2026 for Real Estate Investors | AE Tax Advisors",
    },
}

ALL = dep.POSTS + re_.POSTS + biz.POSTS


def remap_links(text):
    for new, old in REMAP.items():
        text = text.replace(f"/blog/{new}/", f"/blog/{old}/")
    return text


def main():
    seen = set()
    for post in ALL:
        p = dict(post)
        p["slug"] = REMAP.get(p["slug"], p["slug"])
        assert p["slug"] not in seen, f"duplicate slug {p['slug']}"
        seen.add(p["slug"])

        p["body"] = remap_links(p["body"])
        p["related"] = [(remap_links(h), t) for h, t in p["related"]]
        p["faqs"] = [(q, remap_links(a)) for q, a in p.get("faqs", [])]
        p.update(OVERRIDES.get(p["slug"], {}))

        out = seo_render.write_post(p)
        print(f"  {out}")

    # remove the superseded duplicate directories
    for new in REMAP:
        d = Path("blog") / new
        if d.exists():
            shutil.rmtree(d)
            print(f"  removed duplicate blog/{new}/")

    print(f"{len(ALL)} posts built ({len(REMAP)} upgraded existing URLs)")


if __name__ == "__main__":
    main()
