#!/usr/bin/env python3
"""Build a site wide internal link web.

Classifies every content page into a topic cluster, scores page pairs on
weighted token overlap, and injects a Related Reading block containing the
cluster pillar plus the closest neighbours. Run with --dry to inspect.
"""
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BASE = "https://aetaxadvisors.com"

# Pages that are funnels, bookings, or staging: no link block, and never a target.
EXCLUDE_PAT = re.compile(
    r"^(blog-staging/|locations/|.*(consultation|zoom|calendar|booking|schedule|"
    r"thank-you|thanks|check-in|survey|onboarding|followup|recap|check-out|"
    r"discovery|contact|privacy-policy|terms-of-service|disclaimer|sitemap|"
    r"\d+-(minute|day)-)).*"
)
EXCLUDE_EXACT = {
    "", "blog", "guides", "glossary", "faq", "services", "pricing", "about",
    "bios", "case-studies", "client-results", "books", "404",
}

CLUSTERS = {
    "cost-seg": {
        "pillar": ("/cost-segregation-studies-for-real-estate-investors/",
                   "Cost Segregation Studies for Real Estate Investors"),
        "kw": ["cost segregation", "cost seg", "depreciation", "macrs", "bonus depreciation",
               "form 3115", "3115", "lookback", "accelerated depreciation", "section 168",
               "partial asset disposition", "recapture", "1245", "1250", "placed in service",
               "component", "qip", "qualified improvement", "section 179", "land improvement"],
    },
    "real-estate": {
        "pillar": ("/real-estate-tax-planning/", "Real Estate Tax Planning"),
        "kw": ["rental", "short term rental", "str", "airbnb", "vrbo", "landlord",
               "real estate professional", "reps", "material participation", "passive activity",
               "469", "1031", "like kind", "exchange", "tenant", "property manager",
               "long term rental", "ltr", "syndication", "brrrr", "house hack",
               "opportunity zone", "seven day", "7 day", "grouping election"],
    },
    "entity": {
        "pillar": ("/business-owner-tax-planning/", "Business Owner Tax Planning"),
        "kw": ["s corp", "s-corp", "c corp", "c-corp", "llc", "entity", "partnership",
               "reasonable compensation", "qbi", "199a", "self employment tax", "payroll",
               "form 2553", "shareholder basis", "distribution", "holding company",
               "operating agreement", "qsbs", "1202", "ptet", "salt"],
    },
    "planning": {
        "pillar": ("/advanced-tax-planning-services/", "Advanced Tax Planning Services"),
        "kw": ["tax planning", "tax strategy", "high income", "high net worth", "augusta rule",
               "280a", "accountable plan", "retirement plan", "cash balance", "defined benefit",
               "solo 401k", "sep ira", "deferred compensation", "stock options", "rsu",
               "estate", "trust", "gift tax", "charitable", "estimated tax", "year end",
               "capital gains", "deduction", "credit", "write off", "vehicle", "home office"],
    },
    "irs": {
        "pillar": ("/tax-compliance-irs-representation/", "Tax Compliance and IRS Representation"),
        "kw": ["irs", "audit", "notice", "penalty", "lien", "levy", "garnishment",
               "offer in compromise", "installment agreement", "unfiled", "amended return",
               "1040-x", "statute of limitations", "innocent spouse", "abatement", "resolution"],
    },
}

STOP = set("""a an the and or of for to in on with your you how what when why is are be
this that it its as at by from we our us can do does not no if then than into
guide explained complete ultimate best top most make makes made get gets tax taxes
ae advisors more less about over under vs versus need needs new using use used""".split())


def slug_of(p):
    d = str(p.parent).replace("\\", "/")
    return "" if d == "." else d


def tokens(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [w for w in words if w not in STOP and len(w) > 2]


def load_pages():
    pages = {}
    for p in sorted(Path(".").rglob("index.html")):
        if ".git" in p.parts:
            continue
        s = slug_of(p)
        if s in EXCLUDE_EXACT or EXCLUDE_PAT.match(s + "/"):
            continue
        t = p.read_text(errors="ignore")
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", t, re.S)
        ti = re.search(r"<title>(.*?)</title>", t, re.S)
        if not h1 and not ti:
            continue
        raw = re.sub(r"<[^>]+>", " ", (h1.group(1) if h1 else ti.group(1)))
        title = re.sub(r"\s*\|\s*AE Tax Advisors\s*$", "", raw).strip()
        title = re.sub(r"\s+", " ", title)
        if not title:
            continue
        # cluster from title plus the first slice of body copy
        body = re.sub(r"<[^>]+>", " ", t[:40000]).lower()
        blob = (title.lower() + " " + s.replace("-", " ") + " ") * 3 + body
        scores = {c: sum(blob.count(k) for k in cfg["kw"]) for c, cfg in CLUSTERS.items()}
        cluster = max(scores, key=scores.get)
        if scores[cluster] == 0:
            cluster = "planning"
        pages[s] = {
            "path": p,
            "url": "/" + s + "/",
            "title": title,
            "toks": Counter(tokens(title + " " + s.replace("-", " "))),
            "cluster": cluster,
            "is_location": bool(re.match(r"^[a-z-]+$", s)) and bool(
                re.search(r"\bin ([A-Z][a-z]+)", title)),
            "has_block": ("related-articles" in t or "Related Reading" in t
                          or "related-posts" in t),
        }
    return pages


def build_idf(pages):
    df = Counter()
    for pg in pages.values():
        df.update(set(pg["toks"]))
    n = len(pages)
    return {w: math.log(n / (1 + c)) for w, c in df.items()}


def signature(title):
    """Family key so near identical templated titles do not crowd a block.

    'Cost Segregation Study in Utah' and '... in Texas' share a signature, so
    only one of them can appear in any single Related Reading list.
    """
    toks = [w for w in tokens(title)][:4]
    return " ".join(toks)


def related_for(slug, pages, idf, k=8):
    me = pages[slug]
    scored = []
    for other, pg in pages.items():
        if other == slug:
            continue
        shared = set(me["toks"]) & set(pg["toks"])
        if not shared:
            continue
        score = sum(idf.get(w, 0) for w in shared)
        if pg["cluster"] == me["cluster"]:
            score *= 1.6
        # Prefer substantive articles over thin templated location pages.
        if pg["is_location"] and not me["is_location"]:
            score *= 0.35
        scored.append((-score, other))
    scored.sort()

    picked, seen, sigs = [], set(), Counter()
    pillar_url, pillar_title = CLUSTERS[me["cluster"]]["pillar"]
    if pillar_url != me["url"] and Path(pillar_url.strip("/") + "/index.html").exists():
        picked.append((pillar_url, pillar_title + " (Pillar Guide)"))
        seen.add(pillar_url)
    for _, other in scored:
        if len(picked) >= k:
            break
        pg = pages[other]
        if pg["url"] in seen:
            continue
        sig = signature(pg["title"])
        if sigs[sig] >= 1:
            continue
        picked.append((pg["url"], pg["title"]))
        seen.add(pg["url"])
        sigs[sig] += 1
    return picked


BLOCK = """
    <section class="content-section related-reading"><div class="container narrow">
        <h2>Related Reading</h2>
        <ul class="related-articles">
{items}
        </ul>
    </div></section>
"""


def render_block(links):
    items = "\n".join(
        f'            <li><a href="{u}">{t}</a></li>' for u, t in links
    )
    return BLOCK.format(items=items)


def main():
    dry = "--dry" in sys.argv
    pages = load_pages()
    idf = build_idf(pages)
    print(f"content pages: {len(pages)}")
    print("cluster sizes:", dict(Counter(p["cluster"] for p in pages.values())))

    injected = 0
    samples = 0
    for slug, pg in sorted(pages.items()):
        if pg["has_block"]:
            continue
        links = related_for(slug, pages, idf)
        if len(links) < 4:
            continue
        if dry and samples < 4:
            print(f"\n--- /{slug}/  [{pg['cluster']}]  {pg['title'][:60]}")
            for u, t in links:
                print(f"      {u}  {t[:58]}")
            samples += 1
        if not dry:
            t = pg["path"].read_text(errors="ignore")
            if "</main>" not in t:
                continue
            t = t.replace("</main>", render_block(links) + "\n</main>", 1)
            pg["path"].write_text(t)
        injected += 1
    print(f"\n{'would inject' if dry else 'injected'} Related Reading on {injected} pages")


if __name__ == "__main__":
    main()
