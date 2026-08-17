#!/usr/bin/env python3
"""Rebuild /blog/ as a filterable, searchable card index with dates and categories."""

from __future__ import annotations

import html as _html
import re
import sys
from pathlib import Path

import site_template as T
import seo_topics as TOPICS

BASE = "/blog/"
OUT = T.ROOT / "blog"
PUBLISHED = "2026-08-15"
MODIFIED = "2026-08-15"

H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.DOTALL)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
DESC_RE = re.compile(r'<meta name="description" content="(.*?)"', re.DOTALL)
PUB_RE = re.compile(r'<meta property="article:published_time" content="(\d{4})-(\d{2})-(\d{2})')
MOD_RE = re.compile(r'<meta property="article:modified_time" content="(\d{4})-(\d{2})-(\d{2})')
DATEPUB_RE = re.compile(r'"datePublished":\s*"(\d{4})-(\d{2})-(\d{2})')
H2_RE = re.compile(r"<h[23][^>]*>(.*?)</h[23]>", re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")

MONTHS = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def text_of(s: str) -> str:
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", s)).strip()


def collect() -> list[dict]:
    posts = []
    for d in sorted(OUT.iterdir()):
        if not d.is_dir():
            continue
        f = d / "index.html"
        if not f.exists():
            continue
        html = f.read_text(encoding="utf-8", errors="replace")

        hm = H1_RE.search(html) or TITLE_RE.search(html)
        title = _html.unescape(text_of(hm.group(1))) if hm else d.name
        title = title.split(" | AE Tax")[0]

        dm = DESC_RE.search(html)
        desc = _html.unescape(re.sub(r"\s+", " ", dm.group(1)).strip()) if dm else ""

        date = None
        for rx in (PUB_RE, DATEPUB_RE, MOD_RE):
            m = rx.search(html)
            if m:
                date = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
                break

        headings = " ".join(text_of(x) for x in H2_RE.findall(html)[:20])
        topic = TOPICS.classify(title, title, headings, text_of(html)[:4000])

        posts.append({
            "slug": d.name,
            "title": title,
            "desc": desc,
            "date": date,
            "category": TOPICS.TOPICS[topic][1],
        })
    return posts


# Periods that end an abbreviation, not a sentence. "IRC Sec. 179" must not
# become the whole card blurb.
ABBREV = {
    "sec", "secs", "reg", "regs", "treas", "rev", "proc", "rul", "no", "nos",
    "u.s", "i.e", "e.g", "etc", "vs", "approx", "mr", "mrs", "ms", "dr", "st",
    "inc", "corp", "co", "ltd", "llc", "jr", "sr", "est", "avg", "fig",
}
MIN_BLURB = 45


def one_line(desc: str, limit: int = 120) -> str:
    """One clean sentence for a card. Never a mid-word or mid-citation cut."""
    desc = desc.strip()
    if not desc:
        return ""

    # Candidate sentence endings, skipping abbreviation periods.
    ends = []
    for m in re.finditer(r"[.!?](?=\s|$)", desc):
        word = re.search(r"([\w.]+)$", desc[: m.start()])
        if m.group(0) == "." and word and word.group(1).lower() in ABBREV:
            continue
        ends.append(m.end())

    # Shortest ending that says something and still fits on one line.
    for end in ends:
        if end >= MIN_BLURB:
            return desc[:end] if end <= limit else _clip(desc, limit)
    if ends and ends[-1] == len(desc) and len(desc) <= limit:
        return desc
    return desc if len(desc) <= limit else _clip(desc, limit)


def _clip(desc: str, limit: int) -> str:
    return desc[:limit].rsplit(" ", 1)[0].rstrip(",;:. ") + "..."


def date_label(d) -> str:
    if not d:
        return ""
    return f"{MONTHS[d[1]]} {d[2]}, {d[0]}"


def iso(d) -> str:
    return f"{d[0]:04d}-{d[1]:02d}-{d[2]:02d}" if d else ""


BLOG_CSS = """
    <style>
      .blog-toolbar{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin:6px 0 18px}
      .blog-search{flex:1 1 280px;min-width:0;padding:13px 16px;font-size:16px;
        border:1px solid #d9dde3;border-radius:8px;min-height:48px;font-family:inherit;color:var(--dark)}
      .blog-search:focus{outline:2px solid var(--accent);outline-offset:1px;border-color:var(--accent)}
      .blog-filters{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px}
      .blog-chip{background:#fff;border:1px solid #d9dde3;color:var(--dark);border-radius:999px;
        padding:10px 16px;font-size:13.5px;font-weight:600;cursor:pointer;min-height:44px;
        font-family:inherit;transition:background .2s,border-color .2s,color .2s}
      .blog-chip:hover{border-color:var(--accent);color:var(--accent)}
      .blog-chip[aria-pressed="true"]{background:var(--primary);border-color:var(--primary);color:#fff}
      .blog-count{font-size:14px;color:var(--medium);margin-bottom:18px}
      /* Text-only article list. No thumbnails and no placeholder blocks: an
         article index for a tax practice is read, not browsed by picture, and
         a coloured block holding two initials is worse than no image at all. */
      .blog-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(340px,100%),1fr));gap:14px 26px}
      .blog-card{background:#fff;border:1px solid #e9ebef;border-radius:10px;
        padding:22px 24px 20px;display:flex;flex-direction:column;
        transition:border-color .2s ease,box-shadow .2s ease}
      .blog-card:hover{border-color:#cfd5de;box-shadow:0 4px 16px rgba(27,42,74,.07)}
      .blog-body{display:flex;flex-direction:column;flex:1}
      .blog-meta{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:9px}
      .blog-cat{background:var(--accent);color:var(--primary);font-size:.66rem;font-weight:700;
        padding:3px 9px;border-radius:20px;text-transform:uppercase;letter-spacing:.04em}
      .blog-date{font-size:12.5px;color:var(--medium)}
      .blog-card h3{font-family:var(--font-heading);font-size:1.06rem;font-weight:700;
        line-height:1.34;margin-bottom:8px}
      .blog-card h3 a{color:var(--dark);text-decoration:none}
      .blog-card h3 a:hover{color:var(--accent)}
      .blog-card p{font-size:.885rem;color:var(--medium);line-height:1.55;margin-bottom:14px}
      /* A quiet text link, not a button. The whole card title is already a
         link; this is a secondary affordance and should read like one. */
      .blog-readmore{margin-top:auto;align-self:flex-start;font-size:13px;font-weight:600;
        color:var(--primary);text-decoration:none;letter-spacing:.01em}
      .blog-readmore::after{content:" \\2192";color:var(--accent);transition:margin-left .2s ease}
      .blog-readmore:hover{color:var(--accent)}
      .blog-readmore:hover::after{margin-left:3px}
      .blog-empty{padding:36px 0;color:var(--medium)}
      .blog-more{display:block;margin:28px auto 0}
      @media (max-width:768px){
        .blog-grid{grid-template-columns:1fr;gap:12px}
        .blog-chip{flex:1 1 auto;text-align:center}
        .blog-card{padding:20px 20px 18px}
      }
    </style>"""

BLOG_JS = """
    <script>
    (function(){
      var grid=document.getElementById('blog-grid'); if(!grid) return;
      var cards=Array.prototype.slice.call(grid.querySelectorAll('.blog-card'));
      var chips=Array.prototype.slice.call(document.querySelectorAll('.blog-chip'));
      var search=document.getElementById('blog-search');
      var count=document.getElementById('blog-count');
      var empty=document.getElementById('blog-empty');
      var more=document.getElementById('blog-more');
      var PAGE=36, shown=PAGE, cat='all';
      function match(c){
        if(cat!=='all' && c.dataset.cat!==cat) return false;
        var q=(search.value||'').trim().toLowerCase();
        return !q || c.dataset.text.indexOf(q)!==-1;
      }
      function render(){
        var n=0, vis=0;
        cards.forEach(function(c){
          if(match(c)){ n++; if(n<=shown){c.style.display='';vis++;} else c.style.display='none'; }
          else c.style.display='none';
        });
        count.textContent=n+(n===1?' article':' articles');
        empty.style.display=n===0?'block':'none';
        more.style.display=n>vis?'':'none';
      }
      chips.forEach(function(ch){ ch.addEventListener('click',function(){
        chips.forEach(function(x){x.setAttribute('aria-pressed','false');});
        ch.setAttribute('aria-pressed','true'); cat=ch.dataset.cat; shown=PAGE; render();
      });});
      search.addEventListener('input',function(){shown=PAGE;render();});
      more.addEventListener('click',function(){shown+=PAGE;render();});
      render();
    })();
    </script>"""


def main() -> int:
    posts = collect()
    # Newest first, undated last.
    posts.sort(key=lambda p: (p["date"] is not None, p["date"] or (0, 0, 0)), reverse=True)

    cats: dict[str, int] = {}
    for p in posts:
        cats[p["category"]] = cats.get(p["category"], 0) + 1
    ordered = sorted(cats.items(), key=lambda x: -x[1])

    chips = ['            <button class="blog-chip" data-cat="all" aria-pressed="true">'
             f'All ({len(posts)})</button>']
    for c, n in ordered:
        chips.append(f'            <button class="blog-chip" data-cat="{T.esc(c)}" '
                     f'aria-pressed="false">{T.esc(c)} ({n})</button>')

    cards = []
    for p in posts:
        blurb = one_line(p["desc"])
        searchable = T.esc((p["title"] + " " + p["desc"] + " " + p["category"]).lower())
        dl = date_label(p["date"])
        date_html = (f'<time class="blog-date" datetime="{iso(p["date"])}">{dl}</time>'
                     if dl else "")
        cards.append(
            f"""            <article class="blog-card" data-cat="{T.esc(p['category'])}" data-text="{searchable}">
                <div class="blog-body">
                    <div class="blog-meta">
                        <span class="blog-cat">{T.esc(p['category'])}</span>
                        {date_html}
                    </div>
                    <h3><a href="{BASE}{p['slug']}/">{T.esc(p['title'])}</a></h3>
                    <p>{T.esc(blurb)}</p>
                    <a href="{BASE}{p['slug']}/" class="blog-readmore">Read article</a>
                </div>
            </article>"""
        )

    body = f"""    <section class="page-header">
        <div class="container">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="/">Home</a> &rsaquo; <span>Blog</span>
            </nav>
            <h1>Tax Strategy Blog</h1>
            <p class="subtitle">{len(posts)} articles on cost segregation, depreciation,
            entity structuring, retirement plan design, and IRS procedure.</p>
            <div class="cta-buttons">
                <a href="/discovery/" class="btn-cta btn-lg">Get Your Free Estimate</a>
            </div>
        </div>
    </section>

    <section class="content-section fade-in-section">
        <div class="container">
            <label for="blog-search" class="sr-only">Search articles</label>
            <div class="blog-toolbar">
                <input type="search" id="blog-search" class="blog-search"
                    placeholder="Search by topic, strategy, or IRC section" autocomplete="off">
            </div>
            <div class="blog-filters" role="group" aria-label="Filter by category">
{chr(10).join(chips)}
            </div>
            <p class="blog-count" id="blog-count" aria-live="polite">{len(posts)} articles</p>
            <div class="blog-grid" id="blog-grid">
{chr(10).join(cards)}
            </div>
            <p class="blog-empty" id="blog-empty" style="display:none;">No articles match that
            search. Try a broader term such as "cost segregation", "S-Corp", or "depreciation".</p>
            <button class="btn-secondary blog-more" id="blog-more" type="button">Show more articles</button>
        </div>
    </section>"""

    schemas = [
        {"@context": "https://schema.org", "@type": "Blog",
         "name": "AE Tax Advisors Tax Strategy Blog",
         "url": f"{T.SITE}{BASE}",
         "description": f"{len(posts)} articles on tax strategy for business owners and real estate investors.",
         "publisher": {"@id": f"{T.SITE}/#organization"},
         "blogPost": [
             {"@type": "BlogPosting", "headline": p["title"],
              "url": f"{T.SITE}{BASE}{p['slug']}/",
              **({"datePublished": iso(p["date"])} if p["date"] else {})}
             for p in posts[:50]
         ]},
        T.breadcrumb_schema([("Home", "/"), ("Blog", BASE)]),
    ]

    html = T.build_page(
        title="Tax Strategy Blog | AE Tax Advisors",
        description=(f"{len(posts)} articles on cost segregation, bonus depreciation, entity "
                     "structuring, real estate professional status, retirement plan design, "
                     "and IRS procedure."),
        path=BASE, body=body, schemas=schemas,
        published=PUBLISHED, modified=MODIFIED,
        og_type="website", extra_head=BLOG_CSS,
    ).replace("</body>", BLOG_JS + "\n</body>")

    (OUT / "index.html").write_text(html, encoding="utf-8")
    dated = sum(1 for p in posts if p["date"])
    print(f"blog index rebuilt: {len(posts)} posts ({dated} with dates), "
          f"{len(ordered)} categories")
    for c, n in ordered[:10]:
        print(f"   {c}: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
