#!/usr/bin/env python3
"""Generate the anonymized case study library and its filterable index.

Existing hand-written case studies under /case-studies/ are preserved and are
folded into the index alongside the generated ones.
"""

from __future__ import annotations

import html as _html
import random
import re
import sys
from pathlib import Path

import site_template as T
import case_engine as E

PUBLISHED = "2026-08-15"
MODIFIED = "2026-08-15"
BASE = "/case-studies/"
OUT = T.ROOT / "case-studies"

SEED = 20260815


def profile_table(rows: list[tuple[str, str]]) -> str:
    body = "\n".join(
        f"                    <tr><th>{k}</th><td>{v}</td></tr>" for k, v in rows
    )
    return f"""            <div class="ae-table-scroll" style="overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%">
                <table class="case-profile">
                    <caption class="sr-only">Client profile</caption>
{body}
                </table>
            </div>"""


def build_study(sc: dict, related_cases: list[tuple[str, str]]) -> str:
    path = f"{BASE}{sc['slug']}/"
    url = f"{T.SITE}{path}"

    solution_blocks = "\n".join(
        f"""            <h3>{i}. {head}</h3>
            <p>{text}</p>"""
        for i, (head, text) in enumerate(sc["solution"], start=1)
    )

    body = "\n\n".join([
        T.page_header(
            h1=sc["h1"],
            subtitle=sc["desc"],
            trail=[("Home", "/"), ("Case Studies", BASE), (sc["title"], path)],
            cta="See What We Could Do For You",
        ),
        f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="post-meta">{sc['cat']} &middot; Anonymized client case study &middot;
            AE Tax Advisors, Billings, Montana</p>
            <h2>Client Profile</h2>
{profile_table(sc['profile'])}
        </div>
    </section>""",
        T.section("The Situation", f"            <p>{sc['situation']}</p>"),
        T.section("The Challenge", f"            <p>{sc['challenge']}</p>"),
        T.section("What We Did", solution_blocks),
        T.section("The Result", f"            <p>{sc['result']}</p>"),
        T.takeaways(sc["takeaways"]),
        T.faq_section(sc["faqs"]),
        T.related_section(sc["related_pages"] + related_cases, "Related Reading"),
    ])

    schemas = [
        T.article_schema(
            title=sc["h1"],
            description=sc["desc"],
            url=url,
            published=PUBLISHED,
            modified=MODIFIED,
            section="Case Study",
        ),
        T.faq_schema(sc["faqs"]),
        T.breadcrumb_schema([("Home", "/"), ("Case Studies", BASE), (sc["title"], path)]),
    ]

    return T.build_page(
        title=sc["title"] + " | AE Tax Advisors",
        description=sc["desc"],
        path=path,
        body=body,
        schemas=schemas,
        published=PUBLISHED,
        modified=MODIFIED,
        active_nav=BASE,
    )


# ---------------------------------------------------------------- index

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.DOTALL)
DESC_RE = re.compile(r'<meta name="description" content="(.*?)"', re.DOTALL)

CATEGORY_HINTS = [
    ("Real Estate Investors", ("str-", "ltr-", "cost-seg", "cost-segregation",
                               "rental", "real-estate", "1031", "reps",
                               "material-participation", "property", "multifamily",
                               "mobile-home", "land-developer", "fix-and-flip",
                               "triple-net", "airbnb")),
    ("Commercial Real Estate", ("hotel", "restaurant", "self-storage", "warehouse",
                                "dental-practice-cost", "medical", "commercial",
                                "auto-dealership", "veterinary", "brewery")),
    ("Business Owners", ("s-corp", "c-corp", "entity", "llc", "partnership",
                         "business", "franchise", "consultant", "saas", "ecommerce",
                         "e-commerce", "construction", "manufacturing", "trucking",
                         "agency", "firm", "cash-balance", "401k", "retirement",
                         "equipment", "insurance", "landscaping",
                         "tech-", "nonprofit", "international")),
    ("Amendment Recovery", ("amended", "amendment", "3115", "lookback",
                            "late-election", "correction")),
]


def classify(slug: str, title: str) -> str:
    text = (slug + " " + title).lower()
    for cat, hints in CATEGORY_HINTS:
        if any(h in text for h in hints):
            return cat
    return "Business Owners"


def read_existing() -> list[dict]:
    """Pick up hand-written case studies already in the repo."""
    out = []
    for d in sorted(OUT.iterdir()):
        if not d.is_dir():
            continue
        f = d / "index.html"
        if not f.exists():
            continue
        html = f.read_text(encoding="utf-8", errors="replace")
        tm = TITLE_RE.search(html)
        hm = H1_RE.search(html)
        dm = DESC_RE.search(html)
        title = (hm.group(1) if hm else (tm.group(1) if tm else d.name)).strip()
        title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", title))
        title = title.split(" | AE Tax")[0]
        desc = re.sub(r"\s+", " ", dm.group(1)).strip() if dm else ""
        out.append({
            "slug": d.name,
            "title": _html.unescape(title),
            "desc": _html.unescape(desc),
            "cat": classify(d.name, title),
        })
    return out


INDEX_CSS = """
    <style>
      .cs-toolbar{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin:8px 0 28px}
      .cs-search{flex:1 1 260px;min-width:0;padding:13px 16px;font-size:16px;
        border:1px solid #d9dde3;border-radius:8px;min-height:48px;font-family:inherit;color:var(--dark)}
      .cs-search:focus{outline:2px solid var(--accent);outline-offset:1px;border-color:var(--accent)}
      .cs-filters{display:flex;flex-wrap:wrap;gap:8px}
      .cs-chip{background:#fff;border:1px solid #d9dde3;color:var(--dark);border-radius:999px;
        padding:11px 18px;font-size:14px;font-weight:600;cursor:pointer;min-height:44px;
        font-family:inherit;transition:background .2s,border-color .2s,color .2s}
      .cs-chip:hover{border-color:var(--accent);color:var(--accent)}
      .cs-chip[aria-pressed="true"]{background:var(--primary);border-color:var(--primary);color:#fff}
      .cs-count{font-size:14px;color:var(--medium);margin-bottom:18px}
      .cs-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(310px,100%),1fr));gap:22px}
      .cs-card{background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:24px;
        display:flex;flex-direction:column;transition:box-shadow .3s ease,transform .3s ease}
      .cs-card:hover{box-shadow:var(--shadow-md);transform:translateY(-3px)}
      .cs-tag{background:var(--accent);color:var(--primary);font-size:.7rem;font-weight:700;
        padding:4px 11px;border-radius:20px;text-transform:uppercase;align-self:flex-start;margin-bottom:12px}
      .cs-card h3{font-size:1.02rem;line-height:1.4;margin-bottom:10px}
      .cs-card h3 a{color:var(--dark)}
      .cs-card h3 a:hover{color:var(--accent)}
      .cs-card p{font-size:.9rem;color:var(--medium);line-height:1.55;margin-bottom:16px}
      .cs-card .btn-secondary{margin-top:auto;align-self:flex-start}
      .cs-empty{padding:36px 0;color:var(--medium)}
      .cs-more{display:block;margin:28px auto 0}
      .sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;
        clip:rect(0,0,0,0);white-space:nowrap;border:0}
      @media (max-width:768px){
        .cs-grid{grid-template-columns:1fr}
        .cs-filters{width:100%}
        .cs-chip{flex:1 1 auto;text-align:center}
      }
    </style>"""

INDEX_JS = """
    <script>
    (function(){
      var grid = document.getElementById('cs-grid');
      if(!grid) return;
      var cards = Array.prototype.slice.call(grid.querySelectorAll('.cs-card'));
      var chips = Array.prototype.slice.call(document.querySelectorAll('.cs-chip'));
      var search = document.getElementById('cs-search');
      var count = document.getElementById('cs-count');
      var empty = document.getElementById('cs-empty');
      var more = document.getElementById('cs-more');
      var PAGE = 48, shown = PAGE, activeCat = 'all';

      function matches(card){
        if(activeCat !== 'all' && card.dataset.cat !== activeCat) return false;
        var q = (search.value || '').trim().toLowerCase();
        if(!q) return true;
        return card.dataset.text.indexOf(q) !== -1;
      }
      function render(){
        var n = 0, visible = 0;
        cards.forEach(function(c){
          if(matches(c)){
            n++;
            if(n <= shown){ c.style.display = ''; visible++; }
            else { c.style.display = 'none'; }
          } else { c.style.display = 'none'; }
        });
        count.textContent = n + (n === 1 ? ' case study' : ' case studies');
        empty.style.display = n === 0 ? 'block' : 'none';
        more.style.display = n > visible ? '' : 'none';
      }
      chips.forEach(function(chip){
        chip.addEventListener('click', function(){
          chips.forEach(function(c){ c.setAttribute('aria-pressed', 'false'); });
          chip.setAttribute('aria-pressed', 'true');
          activeCat = chip.dataset.cat;
          shown = PAGE;
          render();
        });
      });
      search.addEventListener('input', function(){ shown = PAGE; render(); });
      more.addEventListener('click', function(){ shown += PAGE; render(); });
      render();
    })();
    </script>"""


def build_index(items: list[dict]) -> str:
    cats = ["Real Estate Investors", "Commercial Real Estate", "Business Owners",
            "Amendment Recovery"]
    present = [c for c in cats if any(i["cat"] == c for i in items)]

    chips = ['            <button class="cs-chip" data-cat="all" aria-pressed="true">'
             f'All ({len(items)})</button>']
    for c in present:
        n = sum(1 for i in items if i["cat"] == c)
        chips.append(f'            <button class="cs-chip" data-cat="{T.esc(c)}" '
                     f'aria-pressed="false">{c} ({n})</button>')

    cards = []
    for it in items:
        blurb = it["desc"][:190].rstrip()
        if len(it["desc"]) > 190:
            blurb += "..."
        searchable = T.esc((it["title"] + " " + it["desc"] + " " + it["cat"] + " "
                            + it.get("keywords", "")).lower())
        cards.append(
            f"""            <article class="cs-card" data-cat="{T.esc(it['cat'])}" data-text="{searchable}">
                <span class="cs-tag">{it['cat']}</span>
                <h3><a href="{BASE}{it['slug']}/">{T.esc(it['title'])}</a></h3>
                <p>{T.esc(blurb)}</p>
                <a href="{BASE}{it['slug']}/" class="btn-secondary">Read the Case Study</a>
            </article>"""
        )

    body = f"""    <section class="page-header">
        <div class="container">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="/">Home</a> &rsaquo; <span>Case Studies</span>
            </nav>
            <h1>Case Studies</h1>
            <p class="subtitle">{len(items)} anonymized tax planning results for business owners,
            real estate investors, and high-income professionals.</p>
        </div>
    </section>

    <section class="content-section fade-in-section fade-in-visible">
        <div class="container">
            <p>Every case study below reflects the kind of work we do: cost segregation and
            depreciation strategy, entity design, reasonable compensation, retirement plan
            structuring, pass-through entity tax elections, and prior year recovery. All studies are
            anonymized, all figures are rounded, and no client names or identifying details appear
            anywhere. Strategies depend entirely on facts and circumstances and are not universal
            recommendations.</p>

            <label for="cs-search" class="sr-only">Search case studies</label>
            <div class="cs-toolbar">
                <input type="search" id="cs-search" class="cs-search"
                    placeholder="Search by strategy, industry, or property type" autocomplete="off">
            </div>
            <div class="cs-filters" role="group" aria-label="Filter by client type">
{chr(10).join(chips)}
            </div>

            <p class="cs-count" id="cs-count" aria-live="polite">{len(items)} case studies</p>

            <div class="cs-grid" id="cs-grid">
{chr(10).join(cards)}
            </div>
            <p class="cs-empty" id="cs-empty" style="display:none;">No case studies match that
            search. Try a broader term such as "cost segregation", "S-Corp", or "short-term rental".</p>
            <button class="btn-secondary cs-more" id="cs-more" type="button">Show more case studies</button>
        </div>
    </section>"""

    schemas = [
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": "AE Tax Advisors Case Studies",
            "description": (f"{len(items)} anonymized tax planning case studies covering cost "
                            "segregation, entity structuring, reasonable compensation, retirement "
                            "plan design, and prior year recovery."),
            "url": f"{T.SITE}{BASE}",
            "publisher": {"@type": "Organization", "name": T.BRAND},
        },
        T.breadcrumb_schema([("Home", "/"), ("Case Studies", BASE)]),
    ]

    html = T.build_page(
        title=f"Case Studies | {len(items)} Tax Planning Results | AE Tax Advisors",
        description=(f"{len(items)} anonymized case studies showing real tax planning outcomes: "
                     "cost segregation, S-Corp and C-Corp structuring, retirement plan design, "
                     "and amended return recovery."),
        path=BASE,
        body=body,
        schemas=schemas,
        published=PUBLISHED,
        modified=MODIFIED,
        active_nav=BASE,
        og_type="website",
        extra_head=INDEX_CSS,
    )
    return html.replace("</body>", INDEX_JS + "\n</body>")


def main() -> int:
    rng = random.Random(SEED)
    scenarios: list[dict] = []
    seen: set[str] = set()

    for builder, n in E.BUILDERS:
        for k in range(n):
            sc = builder(rng, len(scenarios) + 1)
            if sc["slug"] in seen:
                sc["slug"] = f"{sc['slug']}-b"
            seen.add(sc["slug"])
            scenarios.append(sc)

    # Titles are built from rounded figures, so collisions are expected. Add the
    # state, then a counter, so every page keeps a unique <title>.
    used: dict[str, int] = {}
    for sc in scenarios:
        title = sc["title"]
        if title in used:
            candidate = f"{title} ({sc.get('state', 'US')})"
            if candidate in used:
                used[title] += 1
                candidate = f"{title} ({sc.get('state', 'US')}, {used[title]})"
            title = candidate
        used.setdefault(title, 1)
        sc["title"] = title

    # Cross-link each study to three siblings in the same category.
    by_cat: dict[str, list[dict]] = {}
    for sc in scenarios:
        by_cat.setdefault(sc["cat"], []).append(sc)

    written = 0
    for sc in scenarios:
        pool = [s for s in by_cat[sc["cat"]] if s["slug"] != sc["slug"]]
        picks = rng.sample(pool, k=min(3, len(pool)))
        related = [(f"{BASE}{p['slug']}/", p["title"]) for p in picks]
        html = build_study(sc, related)
        T.write_page(f"{BASE}{sc['slug']}", html)
        written += 1

    existing = read_existing()
    generated_slugs = {s["slug"] for s in scenarios}
    merged = [
        {
            "slug": s["slug"],
            "title": s["title"],
            "desc": s["desc"],
            "cat": s["cat"],
            "keywords": " ".join(v for _, v in s["profile"]),
        }
        for s in scenarios
    ] + [e for e in existing if e["slug"] not in generated_slugs]

    merged.sort(key=lambda x: (x["cat"], x["title"]))
    (OUT / "index.html").write_text(build_index(merged), encoding="utf-8")

    print(f"Generated case studies: {written}")
    print(f"Pre-existing preserved:  {len(merged) - written}")
    print(f"Total in index:          {len(merged)}")
    for c in sorted({m['cat'] for m in merged}):
        print(f"   {c}: {sum(1 for m in merged if m['cat'] == c)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
