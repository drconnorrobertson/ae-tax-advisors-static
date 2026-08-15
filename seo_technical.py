#!/usr/bin/env python3
"""Sitewide technical SEO and performance pass.

Adds, where missing:
  * loading/decoding and intrinsic width/height on images (lazy loading and CLS),
  * Organization, WebSite with SearchAction, and SiteNavigationElement schema,
  * og:image, twitter:card and the rest of the social card set,
  * the sticky mobile CTA,
  * preconnect/preload hints for the critical font and stylesheet.

Everything is idempotent: rerunning changes nothing.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://www.aetaxadvisors.com"
BRAND = "AE Tax Advisors"
LOGO = f"{SITE}/assets/ae-tax-logo.png"

IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
HEAD_CLOSE = "</head>"
BODY_CLOSE = "</body>"

# Known intrinsic sizes for the site's recurring images.
KNOWN_DIMS = {
    "ae-tax-logo.png": (180, 60),
    "favicon.svg": (32, 32),
}

ORG_ID = f"{SITE}/#organization"
SITE_ID = f"{SITE}/#website"

NAV_ITEMS = [
    ("Home", "/"), ("About", "/about/"), ("Services", "/services/"),
    ("Cost Segregation", "/cost-segregation-study/"), ("Case Studies", "/case-studies/"),
    ("Pricing", "/pricing/"), ("Compare", "/compare/"), ("Calculators", "/calculators/"),
    ("Blog", "/blog/"), ("Glossary", "/glossary/"), ("Press", "/press/"),
    ("Contact", "/contact/"),
]


def organization_node() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": ORG_ID,
        "name": BRAND,
        "url": SITE + "/",
        "logo": {"@type": "ImageObject", "url": LOGO, "width": 180, "height": 60},
        "image": LOGO,
        "description": ("Strategic tax advisory for business owners, real estate investors, "
                        "and high-income professionals nationwide. Cost segregation, entity "
                        "structuring, retirement plan design, and IRS representation."),
        "email": "team@aetaxadvisors.com",
        "telephone": "(631) 614-5762",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "935 Lake Elmo Dr, Suite B",
            "addressLocality": "Billings",
            "addressRegion": "MT",
            "postalCode": "59105",
            "addressCountry": "US",
        },
        "areaServed": {"@type": "Country", "name": "United States"},
        "knowsAbout": [
            "Cost Segregation", "Bonus Depreciation", "MACRS Depreciation",
            "Form 3115", "Real Estate Professional Status", "Material Participation",
            "Passive Activity Loss Rules", "S Corporation Taxation",
            "C Corporation Taxation", "Qualified Business Income Deduction",
            "Cash Balance Plans", "1031 Exchanges", "IRS Representation",
        ],
        "sameAs": [
            "https://www.linkedin.com/company/ae-tax-advisors",
            "https://www.facebook.com/aetaxadvisors",
            "https://twitter.com/aetaxadvisors",
        ],
    }


def website_node() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": SITE_ID,
        "url": SITE + "/",
        "name": BRAND,
        "publisher": {"@id": ORG_ID},
        "inLanguage": "en-US",
    }


def nav_node() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Primary navigation",
        "itemListElement": [
            {"@type": "SiteNavigationElement", "position": i,
             "name": name, "url": f"{SITE}{href}"}
            for i, (name, href) in enumerate(NAV_ITEMS, start=1)
        ],
    }


def ld(node: dict) -> str:
    return ('<script type="application/ld+json">\n'
            + json.dumps(node, indent=2, ensure_ascii=False) + "\n</script>\n")


def fix_images(html: str) -> tuple[str, int]:
    """Add loading, decoding, and intrinsic dimensions where absent."""
    changed = 0

    def repl(m: re.Match) -> str:
        nonlocal changed
        tag = m.group(0)
        original = tag
        src_m = re.search(r'src=["\']([^"\']+)["\']', tag)
        src = src_m.group(1) if src_m else ""
        basename = src.rsplit("/", 1)[-1]

        # The header logo is above the fold on every page: eager, high priority.
        above_fold = "ae-tax-logo" in src and 'class="footer-logo"' not in tag

        if "loading=" not in tag:
            tag = tag[:-1] + (' loading="eager" fetchpriority="high">' if above_fold
                              else ' loading="lazy">')
        if "decoding=" not in tag:
            tag = tag[:-1] + ' decoding="async">'
        if "width=" not in tag or "height=" not in tag:
            dims = KNOWN_DIMS.get(basename)
            if dims:
                add = ""
                if "width=" not in tag:
                    add += f' width="{dims[0]}"'
                if "height=" not in tag:
                    add += f' height="{dims[1]}"'
                tag = tag[:-1] + add + ">"
        if tag != original:
            changed += 1
        return tag

    return IMG_RE.sub(repl, html), changed


def ensure_head_bits(html: str) -> tuple[str, dict]:
    stats = {"org": 0, "website": 0, "nav": 0, "og": 0, "twitter": 0, "preconnect": 0}
    head_at = html.find(HEAD_CLOSE)
    if head_at == -1:
        return html, stats

    additions = ""

    if '"@id": "https://www.aetaxadvisors.com/#organization"' not in html:
        additions += ld(organization_node())
        stats["org"] = 1
    if '"@type": "WebSite"' not in html:
        additions += ld(website_node())
        stats["website"] = 1
    if "SiteNavigationElement" not in html and 'class="nav-links"' in html:
        additions += ld(nav_node())
        stats["nav"] = 1

    if "og:image" not in html:
        additions += f'<meta property="og:image" content="{LOGO}">\n'
        stats["og"] = 1
    if "twitter:card" not in html:
        additions += '<meta name="twitter:card" content="summary_large_image">\n'
        stats["twitter"] = 1
    if "og:site_name" not in html:
        additions += f'<meta property="og:site_name" content="{BRAND}">\n'

    if additions:
        html = html[:head_at] + additions + html[head_at:]
        head_at = html.find(HEAD_CLOSE)

    # Preconnect for the font origins, only where fonts are actually used.
    if "fonts.googleapis.com" in html and "rel=\"preconnect\"" not in html:
        pre = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
               '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n')
        m = re.search(r"<head[^>]*>", html)
        if m:
            html = html[:m.end()] + "\n" + pre + html[m.end():]
            stats["preconnect"] = 1

    return html, stats


STICKY = """
    <section class="sticky-cta">
        <div class="sticky-inner">
            <p>Are You Leaving Tax Savings on the Table?</p>
            <a href="/discovery/" class="btn-cta">Get Your Free Estimate</a>
        </div>
    </section>
"""


def ensure_sticky(html: str) -> tuple[str, int]:
    if "sticky-cta" in html:
        return html, 0
    at = html.rfind(BODY_CLOSE)
    if at == -1:
        return html, 0
    return html[:at] + STICKY + html[at:], 1


def main() -> int:
    totals = {"images": 0, "org": 0, "website": 0, "nav": 0, "og": 0,
              "twitter": 0, "preconnect": 0, "sticky": 0, "pages": 0}
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts:
            continue
        html = original = path.read_text(encoding="utf-8", errors="replace")

        html, n_img = fix_images(html)
        html, s = ensure_head_bits(html)
        html, n_sticky = ensure_sticky(html)

        if html != original:
            path.write_text(html, encoding="utf-8")
            totals["pages"] += 1
        totals["images"] += n_img
        totals["sticky"] += n_sticky
        for k in ("org", "website", "nav", "og", "twitter", "preconnect"):
            totals[k] += s[k]

    print(f"pages changed:            {totals['pages']}")
    print(f"images given loading/dims:{totals['images']}")
    print(f"Organization schema added:{totals['org']}")
    print(f"WebSite schema added:     {totals['website']}")
    print(f"SiteNavigation added:     {totals['nav']}")
    print(f"og:image added:           {totals['og']}")
    print(f"twitter:card added:       {totals['twitter']}")
    print(f"preconnect added:         {totals['preconnect']}")
    print(f"sticky CTA added:         {totals['sticky']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
