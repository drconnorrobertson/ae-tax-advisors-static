#!/usr/bin/env python3
"""Inject a self-contained global nav (incl. /pricing/) into standalone landing
pages that do not load /assets/style.css. Scoped `aegn-` class names so the
pages' own inline CSS is untouched."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

TARGETS = [
    "short-term-rentals/index.html",
    "short-term-rentals/bnb-accelerator/index.html",
    "cost-segregation-landing/index.html",
    "equipment-leasing/index.html",
    "equipment-leasing-landing/index.html",
]

NAV_ITEMS = [
    ("/", "Home"),
    ("/about/", "About"),
    ("/services/", "Services"),
    ("/cost-segregation-study/", "Cost Segregation"),
    ("/case-studies/", "Case Studies"),
    ("/pricing/", "Pricing"),
    ("/blog/", "Blog"),
    ("/contact/", "Contact"),
]

NAV_CSS = """
<style id="aegn-style">
.aegn{position:sticky;top:0;z-index:9999;background:#fff;border-bottom:1px solid rgba(0,0,0,.07);
box-shadow:0 1px 3px rgba(0,0,0,.05);font-family:'Inter',-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif}
.aegn *{box-sizing:border-box}
.aegn-inner{max-width:1200px;margin:0 auto;padding:10px 16px;display:flex;align-items:center;
justify-content:space-between;gap:12px}
.aegn-logo{display:flex;align-items:center;flex-shrink:0}
.aegn-logo img{height:44px;width:auto;display:block;object-fit:contain}
.aegn-links{display:flex;align-items:center;gap:2px;flex-wrap:wrap}
.aegn-links a{color:#1B2A4A;font-size:14px;font-weight:500;padding:10px 12px;border-radius:6px;
text-decoration:none;white-space:nowrap;line-height:1.2;transition:background .2s,color .2s}
.aegn-links a:hover{background:#F8F9FA;color:#C8A94A}
.aegn-cta{background:#C8A94A;color:#1B2A4A !important;font-weight:600;padding:12px 22px !important;
border-radius:6px;margin-left:6px}
.aegn-cta:hover{background:#d4b757;color:#1B2A4A !important}
.aegn-toggle{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;
padding:12px;min-width:48px;min-height:48px;align-items:center;justify-content:center}
.aegn-toggle span{display:block;width:24px;height:2px;background:#1B2A4A;border-radius:2px}
@media (max-width:992px){
  .aegn-toggle{display:flex}
  .aegn-links{display:none;position:absolute;top:100%;left:0;right:0;background:#fff;
  flex-direction:column;align-items:stretch;padding:8px 12px 16px;gap:0;
  box-shadow:0 12px 24px rgba(0,0,0,.12);max-height:80vh;overflow-y:auto}
  .aegn-links.aegn-open{display:flex}
  .aegn-links a{padding:14px 12px;min-height:48px;display:flex;align-items:center;
  border-bottom:1px solid #f0f0f0;border-radius:0}
  .aegn-cta{margin:12px 0 0;justify-content:center;border-radius:6px;border-bottom:none}
  .aegn-inner{position:relative;padding:8px 12px}
  .aegn-logo img{height:38px}
}
</style>
"""


def nav_html() -> str:
    links = "\n".join(
        f'      <a href="{href}">{label}</a>' for href, label in NAV_ITEMS
    )
    return f"""{NAV_CSS}
<div class="aegn">
  <div class="aegn-inner">
    <a href="/" class="aegn-logo" aria-label="AE Tax Advisors home">
      <img src="/assets/ae-tax-logo.png" alt="AE Tax Advisors" width="180" height="44">
    </a>
    <button class="aegn-toggle" aria-label="Open menu" aria-expanded="false"
      onclick="var n=this.parentNode.querySelector('.aegn-links');var o=n.classList.toggle('aegn-open');this.setAttribute('aria-expanded',o);">
      <span></span><span></span><span></span>
    </button>
    <nav class="aegn-links" aria-label="Main navigation">
{links}
      <a href="/discovery/" class="aegn-cta">Request a Consultation</a>
    </nav>
  </div>
</div>
"""


def ensure_viewport(html: str) -> str:
    if re.search(r'name=["\']viewport["\']', html):
        return html
    return re.sub(
        r"(<head[^>]*>)",
        r'\1\n<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        html,
        count=1,
    )


def main() -> int:
    changed = 0
    for rel in TARGETS:
        path = ROOT / rel
        if not path.exists():
            print(f"skip (missing): {rel}")
            continue
        html = path.read_text(encoding="utf-8")
        if 'class="aegn"' in html:
            print(f"skip (already has nav): {rel}")
            continue
        html = ensure_viewport(html)
        m = re.search(r"<body[^>]*>", html)
        if not m:
            print(f"skip (no body): {rel}")
            continue
        html = html[: m.end()] + "\n" + nav_html() + html[m.end():]
        path.write_text(html, encoding="utf-8")
        changed += 1
        print(f"nav injected: {rel}")
    print(f"\n{changed} landing pages updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
