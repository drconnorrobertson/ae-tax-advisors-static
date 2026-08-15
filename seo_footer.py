#!/usr/bin/env python3
"""Install one canonical footer on every page.

The footer is defined here and written to every page, so it is identical
sitewide and future changes are a one-line edit plus a rerun. Press is linked
here and deliberately not in the top navigation.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SOCIAL = {
    "LinkedIn": ("https://www.linkedin.com/company/ae-tax-advisors",
                 "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"),
    "Facebook": ("https://www.facebook.com/aetaxadvisors",
                 "M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"),
    "Twitter/X": ("https://twitter.com/aetaxadvisors",
                  "M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"),
}

COLUMNS = [
    ("Company", [
        ("/about/", "About AE Tax"),
        ("/bios/", "Our Team"),
        ("/press/", "Press &amp; Media"),
        ("/ae-tax-advisors-reviews/", "Client Reviews"),
        ("/case-studies/", "Case Studies"),
        ("/pricing/", "Pricing"),
        ("/contact/", "Contact Us"),
        ("https://tax-mt.securefilepro.com/portal/#/login", "Client Portal"),
    ]),
    ("Services", [
        ("/business-owner-small-business-tax/", "Business Owner Tax"),
        ("/real-estate-tax-planning/", "Real Estate Tax Planning"),
        ("/cost-segregation-study/", "Cost Segregation Study"),
        ("/short-term-rental-tax-strategy/", "Short-Term Rental Strategy"),
        ("/rental-property-tax-planning/", "Rental Property Planning"),
        ("/retirement-exit-ma-tax-strategy/", "Retirement &amp; Exit Strategy"),
        ("/estate-trust-wealth-transfer/", "Estate &amp; Wealth Transfer"),
        ("/tax-compliance-irs-representation/", "IRS Representation"),
    ]),
    ("Popular Guides", [
        ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026"),
        ("/short-term-rental-tax-loophole-2026/", "STR Tax Loophole 2026"),
        ("/reps-real-estate-professional-status/", "Real Estate Pro Status"),
        ("/form-3115-cost-segregation-lookback/", "Form 3115 Lookback"),
        ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC 2026"),
        ("/cash-balance-plan-tax-deduction/", "Cash Balance Plans"),
        ("/macrs-depreciation-schedule-2026/", "MACRS Schedule 2026"),
        ("/section-179-vs-bonus-depreciation-2026/", "Section 179 vs Bonus"),
    ]),
    ("Resources", [
        ("/blog/", "Blog"),
        ("/compare/", "Compare Firms"),
        ("/faq/", "FAQ"),
        ("/glossary/", "Tax Glossary"),
        ("/guides/", "Guides &amp; Whitepapers"),
        ("/books/", "Books"),
        ("/sitemap/", "Site Map"),
        ("/discovery/", "Request a Consultation"),
    ]),
]


def social_html() -> str:
    parts = []
    for label, (href, path) in SOCIAL.items():
        parts.append(
            f'                    <a href="{href}" target="_blank" rel="noopener" '
            f'aria-label="{label}">\n'
            f'                        <svg width="20" height="20" viewBox="0 0 24 24" '
            f'fill="currentColor" aria-hidden="true" focusable="false">'
            f'<path d="{path}"/></svg>\n'
            f"                    </a>"
        )
    return "\n".join(parts)


def columns_html() -> str:
    out = []
    for heading, links in COLUMNS:
        items = "\n".join(
            f'                <a href="{href}">{label}</a>' for href, label in links
        )
        out.append(
            f'            <div class="footer-col">\n'
            f"                <h4>{heading}</h4>\n{items}\n"
            f"            </div>"
        )
    return "\n".join(out)


def build_footer() -> str:
    return f"""<footer>
        <div class="footer-inner">
            <div class="footer-col footer-brand">
                <a href="/" class="footer-logo"><img src="/assets/ae-tax-logo.png" alt="AE Tax Advisors" width="180" height="60" loading="lazy" decoding="async" style="object-fit: contain;"></a>
                <p>Strategic tax advisory for business owners and real estate investors.
                Headquartered in Billings, Montana, serving clients nationwide.</p>
                <div class="footer-social">
{social_html()}
                </div>
                <div class="footer-trust-badges">
                    <span class="trust-badge">&#9989; IRS Enrolled Agents</span>
                    <span class="trust-badge">&#9989; Licensed CPAs</span>
                    <span class="trust-badge">&#128274; SOC 2 Compliant</span>
                    <a href="/press/" class="trust-badge" style="text-decoration:none;color:rgba(255,255,255,0.5);">&#128240; As Featured In 29 Publications</a>
                </div>
                <p class="footer-address" style="margin-top:16px;">935 Lake Elmo Dr, Suite B<br>Billings, MT 59105</p>
                <p class="footer-phone"><a href="tel:+16316145762">(631) 614-5762</a></p>
                <p class="footer-email"><a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a></p>
            </div>
{columns_html()}
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 AE Tax Advisors. All rights reserved. | 935 Lake Elmo Dr, Suite B, Billings, MT 59105 | (631) 614-5762</p>
            <p class="footer-legal-links">
                <a href="/privacy-policy/">Privacy Policy</a> &middot;
                <a href="/terms-of-service/">Terms of Service</a> &middot;
                <a href="/disclaimer/">Disclaimer</a> &middot;
                <a href="/sitemap/">Site Map</a> &middot;
                <a href="/press/">Press</a>
            </p>
            <p class="footer-disclaimer">AE Tax Advisors provides tax advisory and compliance
            services nationwide. Content on this site is general information, not tax advice
            for your situation. Strategies depend on facts and circumstances.</p>
        </div>
    </footer>"""


FOOTER_RE = re.compile(r"<footer[^>]*>.*?</footer>", re.DOTALL)


def main() -> int:
    footer = build_footer()
    changed = skipped = 0
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts:
            continue
        html = path.read_text(encoding="utf-8", errors="replace")
        if "<footer" not in html:
            skipped += 1
            continue
        new = FOOTER_RE.sub(lambda _m: footer, html, count=1)
        # Remove any additional footers left over from older templates.
        extra = FOOTER_RE.findall(new)
        if len(extra) > 1:
            first = new.find("<footer")
            end = new.find("</footer>", first) + len("</footer>")
            tail = FOOTER_RE.sub("", new[end:])
            new = new[:end] + tail
        if new != html:
            path.write_text(new, encoding="utf-8")
            changed += 1
    print(f"footer installed on {changed} pages ({skipped} pages had no footer)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
