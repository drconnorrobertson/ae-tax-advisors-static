#!/usr/bin/env python3
"""Build /press/ from content_press.PRESS.

Adding a mention means adding one dict to that list and rerunning this script.
"""

from __future__ import annotations

import sys
from collections import Counter
from urllib.parse import urlparse

import site_template as T
import content_press as P

BASE = "/press/"
PUBLISHED = "2026-08-15"
MODIFIED = "2026-08-15"

PRESS_CSS = """
    <style>
      .press-filters{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 26px}
      .press-chip{background:#fff;border:1px solid #d9dde3;color:var(--dark);border-radius:999px;
        padding:11px 18px;font-size:14px;font-weight:600;cursor:pointer;min-height:44px;
        font-family:inherit;transition:background .2s,border-color .2s,color .2s}
      .press-chip:hover{border-color:var(--accent);color:var(--accent)}
      .press-chip[aria-pressed="true"]{background:var(--primary);border-color:var(--primary);color:#fff}
      .press-list{list-style:none;padding:0;margin:0;display:grid;gap:18px}
      .press-item{background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:24px 26px;
        transition:box-shadow .3s ease,transform .3s ease}
      .press-item:hover{box-shadow:var(--shadow-md);transform:translateY(-2px)}
      .press-meta{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:10px}
      .press-outlet{background:var(--primary);color:#fff;font-size:.72rem;font-weight:700;
        letter-spacing:.04em;text-transform:uppercase;padding:5px 12px;border-radius:5px}
      .press-topic{background:var(--light-bg);color:var(--medium);font-size:.72rem;font-weight:600;
        padding:5px 12px;border-radius:20px;border:1px solid #e5e7eb}
      .press-item h3{font-size:1.08rem;line-height:1.45;margin:0 0 10px}
      .press-item h3 a{color:var(--dark)}
      .press-item h3 a:hover{color:var(--accent)}
      .press-item p{color:var(--medium);font-size:.94rem;line-height:1.6;margin-bottom:14px}
      .press-link{font-weight:600;display:inline-flex;align-items:center;gap:6px;min-height:44px}
      .press-link .ext{font-size:.8em;opacity:.75}
      .press-count{font-size:14px;color:var(--medium);margin-bottom:16px}
      @media (max-width:768px){
        .press-item{padding:20px}
        .press-filters{width:100%}
        .press-chip{flex:1 1 auto;text-align:center}
      }
    </style>"""

PRESS_JS = """
    <script>
    (function(){
      var list = document.getElementById('press-list');
      if(!list) return;
      var items = Array.prototype.slice.call(list.querySelectorAll('.press-item'));
      var chips = Array.prototype.slice.call(document.querySelectorAll('.press-chip'));
      var count = document.getElementById('press-count');
      function render(topic){
        var n = 0;
        items.forEach(function(li){
          var show = topic === 'all' || li.dataset.topic === topic;
          li.style.display = show ? '' : 'none';
          if(show) n++;
        });
        count.textContent = n + (n === 1 ? ' article' : ' articles');
      }
      chips.forEach(function(chip){
        chip.addEventListener('click', function(){
          chips.forEach(function(c){ c.setAttribute('aria-pressed','false'); });
          chip.setAttribute('aria-pressed','true');
          render(chip.dataset.topic);
        });
      });
      render('all');
    })();
    </script>"""


def outlet_domain(url: str) -> str:
    return urlparse(url).netloc.replace("www.", "")


def main() -> int:
    press = P.PRESS
    topics = [t for t, _ in Counter(p["topic"] for p in press).most_common()]

    chips = ['            <button class="press-chip" data-topic="all" aria-pressed="true">'
             f'All ({len(press)})</button>']
    for t in topics:
        n = sum(1 for p in press if p["topic"] == t)
        chips.append(f'            <button class="press-chip" data-topic="{T.esc(t)}" '
                     f'aria-pressed="false">{T.esc(t)} ({n})</button>')

    rows = "\n".join(
        f"""            <li class="press-item" data-topic="{T.esc(p['topic'])}">
                <div class="press-meta">
                    <span class="press-outlet">{T.esc(p['outlet'])}</span>
                    <span class="press-topic">{T.esc(p['topic'])}</span>
                </div>
                <h3><a href="{p['url']}" target="_blank" rel="noopener nofollow">{T.esc(p['title'])}</a></h3>
                <p>{T.esc(p['summary'])}</p>
                <a href="{p['url']}" target="_blank" rel="noopener nofollow" class="press-link">
                    Read on {T.esc(p['outlet'])} <span class="ext" aria-hidden="true">&#8599;</span>
                    <span class="sr-only">(opens in a new tab)</span>
                </a>
            </li>"""
        for p in press
    )

    body = f"""    <section class="page-header">
        <div class="container">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="/">Home</a> &rsaquo; <span>Press</span>
            </nav>
            <h1>Press and Media</h1>
            <p class="subtitle">AE Tax Advisors in the press. {len(press)} features covering
            cost segregation, entity structuring, retirement plan design, and IRS-compliant
            tax strategy.</p>
            <div class="cta-buttons">
                <a href="/discovery/" class="btn-cta btn-lg">Request a Consultation</a>
            </div>
        </div>
    </section>

    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="definition-lead">AE Tax Advisors is a national tax advisory firm
            headquartered in Billings, Montana, working with business owners, real estate
            investors, and high-income professionals in every state. The features below cover
            the firm's approach to cost segregation, entity structuring, reasonable
            compensation, retirement plan design, and IRS representation.</p>
        </div>
    </section>

    <section class="content-section fade-in-section">
        <div class="container">
            <h2>In The Press</h2>
            <div class="press-filters" role="group" aria-label="Filter press by topic">
{chr(10).join(chips)}
            </div>
            <p class="press-count" id="press-count" aria-live="polite">{len(press)} articles</p>
            <ul class="press-list" id="press-list">
{rows}
            </ul>
        </div>
    </section>

    <section class="content-section fade-in-section">
        <div class="container narrow">
            <h2>Media Inquiries</h2>
            <p>For interview requests, expert commentary on tax legislation, or background on
            cost segregation, depreciation strategy, entity structuring, or IRS procedure,
            contact us at <a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a>
            or {T.PHONE}. {T.AUTHOR} is available for comment on federal tax matters affecting
            business owners and real estate investors.</p>
        </div>
    </section>"""

    org_id = f"{T.SITE}/#organization"
    schemas = [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": "Press and Media | AE Tax Advisors",
            "description": f"{len(press)} press features covering AE Tax Advisors.",
            "url": f"{T.SITE}{BASE}",
            "about": {"@id": org_id},
            "mainEntity": {
                "@type": "ItemList",
                "numberOfItems": len(press),
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": i,
                        "item": {
                            "@type": "NewsArticle",
                            "headline": p["title"],
                            "url": p["url"],
                            "abstract": p["summary"],
                            "publisher": {"@type": "Organization", "name": p["outlet"]},
                            "about": {"@id": org_id},
                            "mentions": {"@id": org_id},
                        },
                    }
                    for i, p in enumerate(press, start=1)
                ],
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "Organization",
            "@id": org_id,
            "name": T.BRAND,
            "url": T.SITE,
            "logo": f"{T.SITE}/assets/ae-tax-logo.png",
            "subjectOf": [{"@type": "NewsArticle", "headline": p["title"], "url": p["url"]}
                          for p in press],
        },
        T.breadcrumb_schema([("Home", "/"), ("Press", BASE)]),
    ]

    html = T.build_page(
        title="Press and Media | AE Tax Advisors",
        description=(f"AE Tax Advisors in the press: {len(press)} features covering cost "
                     "segregation, entity structuring, retirement plan design, real estate "
                     "professional status, and IRS representation."),
        path=BASE,
        body=body,
        schemas=schemas,
        published=PUBLISHED,
        modified=MODIFIED,
        og_type="website",
        extra_head=PRESS_CSS,
    ).replace("</body>", PRESS_JS + "\n</body>")

    T.write_page(BASE, html)
    print(f"/press/ built with {len(press)} mentions across {len(topics)} topics")
    for t in topics:
        print(f"   {t}: {sum(1 for p in press if p['topic'] == t)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
