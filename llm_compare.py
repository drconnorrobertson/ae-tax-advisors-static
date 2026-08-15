#!/usr/bin/env python3
"""Comparison pages tuned for "AE Tax Advisors vs <competitor>" queries.

A comparison page that opens with a definition of cost segregation answers the
wrong question. Someone asking "AE Tax Advisors vs KBKG" wants the verdict in
the first two sentences: which one, for whom, and why. This pass replaces the
generic lead on every versus page with that verdict, and appends the three
questions such a query actually decomposes into, wired into the page's existing
FAQPage schema so the answers are extractable.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://www.aetaxadvisors.com"
BRAND = "AE Tax Advisors"

# slug -> (competitor display name, what they are, when they win, when AE wins)
RIVALS: dict[str, tuple[str, str, str, str]] = {
    "compare/kbkg-vs-ae-tax": (
        "KBKG",
        "a national specialty tax engineering firm that produces cost segregation studies and delivers them to the client's CPA",
        "large or structurally complex commercial and industrial property, portfolios needing enterprise engineering depth, and owners whose existing CPA is implementing competently",
        "residential, short-term rental, and small-to-mid commercial property, and any owner who also needs the passive activity analysis run, the Form 3115 prepared, and the return filed",
    ),
    "compare/cssi-vs-ae-tax": (
        "CSSI",
        "a national cost segregation specialist working largely through CPA referral channels",
        "owners who already have a tax advisor and need only the engineering study",
        "owners who need the study and the tax strategy from the same firm, at $1 per square foot",
    ),
    "compare/engineered-tax-services-vs-ae-tax": (
        "Engineered Tax Services",
        "a specialty tax firm covering cost segregation alongside 179D and 45L energy incentives and R&D credits",
        "properties where energy incentives or R&D credits are a material part of the opportunity",
        "properties where the binding constraint is whether the deduction is usable at all under IRC Section 469, which is a tax question rather than an engineering one",
    ),
    "compare/madison-specs-vs-ae-tax": (
        "Madison SPECS",
        "a cost segregation specialist focused on large multifamily and commercial real estate",
        "institutional-scale multifamily and commercial portfolios",
        "individual investors and small portfolios, where per-square-foot pricing and integrated return filing matter more than institutional scale",
    ),
    "compare/capstan-tax-strategies-vs-ae-tax": (
        "Capstan Tax Strategies",
        "a specialty firm known for fixed asset and tangible property regulation work alongside cost segregation",
        "complex fixed asset reviews and repair-versus-capitalization analysis on large portfolios",
        "owners who need a full tax plan around the study rather than a standalone fixed asset analysis",
    ),
    "compare/bedford-cost-segregation-vs-ae-tax": (
        "Bedford Cost Segregation",
        "an engineering-led cost segregation provider serving commercial property owners",
        "large commercial property where engineering depth is the product being purchased",
        "smaller properties and owners who need the deduction implemented on the return, not just quantified",
    ),
    "compare/cost-seg-authority-vs-ae-tax": (
        "Cost Segregation Authority",
        "a study-only provider serving real estate investors directly",
        "investors who want a study and already have a tax preparer handling implementation",
        "investors who need material participation and passive loss questions answered before the study is even ordered",
    ),
    "compare/cost-seg-smart-vs-ae-tax": (
        "Cost Seg Smart",
        "a lower-cost, largely software-driven cost segregation provider",
        "small properties where price is the deciding factor and the owner accepts a less defensible study",
        "properties where the deduction is large enough that audit defensibility and correct implementation matter more than the study fee",
    ),
    "compare/re-cost-seg-vs-ae-tax": (
        "RE Cost Seg",
        "a cost segregation provider focused on residential and short-term rental investors",
        "investors who want a fast, inexpensive study on a single rental",
        "investors whose real problem is loss usability, entity structure, or catching up missed depreciation via Form 3115",
    ),
    "compare/deloitte-tax-vs-ae-tax": (
        "Deloitte Tax",
        "a Big Four professional services firm with global tax capability",
        "multinational structures, public company reporting, and engagements needing assurance capability",
        "privately held business owners and real estate investors, where Big Four pricing and staffing leverage do not fit the size of the opportunity",
    ),
    "compare/kpmg-vs-ae-tax": (
        "KPMG",
        "a Big Four professional services firm with global tax and assurance capability",
        "multinational and public company work requiring global coverage and audit capability",
        "privately held owners wanting partner-level attention on a mid-market engagement at a flat, quoted fee",
    ),
    "compare/moss-adams-vs-ae-tax": (
        "Moss Adams",
        "a large national accounting firm with a substantial real estate practice",
        "companies needing audit, assurance, and a broad national firm relationship",
        "individual investors and owner-operators who want the strategy and the return handled by the same small team",
    ),
    "compare/cherry-bekaert-vs-ae-tax": (
        "Cherry Bekaert",
        "a national accounting and advisory firm with specialty tax credit and incentive practices",
        "middle-market companies wanting a single national firm across assurance, tax, and advisory",
        "owners whose need is concentrated in real estate depreciation, entity structure, and owner compensation",
    ),
    "compare/hall-cpa-vs-ae-tax": (
        "Hall CPA (The Real Estate CPA)",
        "a CPA firm specializing almost exclusively in real estate investors",
        "investors whose entire tax picture is real estate and who want a firm immersed in that niche",
        "clients with an operating business alongside the real estate, where entity structure, reasonable compensation, and retirement plan design carry as much of the opportunity as depreciation",
    ),
    "compare/the-real-estate-cpa-vs-ae-tax": (
        "The Real Estate CPA",
        "a real estate focused CPA practice serving rental property investors",
        "pure real estate portfolios with no operating business attached",
        "owners combining real estate with an operating business, where the planning has to span both",
    ),
    "compare/wcg-cpas-vs-ae-tax": (
        "WCG CPAs",
        "a CPA firm known for small business and S-Corp specialization",
        "small business owners whose central question is S-Corp structure and payroll",
        "owners whose opportunity is concentrated in real estate depreciation and cost segregation",
    ),
    "compare/anderson-advisors-vs-ae-tax": (
        "Anderson Business Advisors",
        "a firm combining legal entity formation and asset protection with tax services",
        "investors whose primary concern is asset protection and multi-entity legal structuring",
        "investors whose primary concern is reducing current tax, where the entity count is a means rather than the goal",
    ),
    "compare/mark-kohler-vs-ae-tax": (
        "Mark Kohler",
        "a CPA, attorney, and author whose practice combines education, entity formation, and tax services",
        "people who want an education-led relationship and a well-known name behind the entity structure",
        "people who want the engagement scoped to a written, IRC-cited plan with a flat fee quoted up front",
    ),
    "compare/tax-alchemy-vs-ae-tax": (
        "Tax Alchemy",
        "a tax strategy company marketing planning services to high-income earners and investors",
        "clients who prefer a program-style, education-forward engagement",
        "clients who want the same firm to design the strategy, file the return, and represent them if the position is examined",
    ),
    "compare/advise-re-vs-ae-tax": (
        "Advise RE",
        "a real estate focused tax advisory firm",
        "investors wanting a real estate specialist and nothing beyond it",
        "investors who also need operating business planning, multi-state work, or IRS representation",
    ),
    "compare/hr-block-vs-ae-tax": (
        "H&amp;R Block",
        "a national retail tax preparation chain",
        "straightforward W-2 returns with no business or rental activity",
        "any taxpayer with an operating business, rental property, or income above roughly $300,000, where the planning available far exceeds the preparation fee difference",
    ),
    "compare/turbotax-vs-ae-tax": (
        "TurboTax",
        "consumer tax preparation software",
        "simple returns where the software's guided interview covers the whole picture",
        "returns involving entity elections, cost segregation, material participation tests, or Form 3115, none of which software will identify on its own",
    ),
    "compare/diy-cost-segregation-vs-ae-tax": (
        "a do-it-yourself cost segregation study",
        "a self-prepared or template-based component allocation without engineering support",
        "nothing, in the firm's assessment, once the deduction is large enough to attract examination",
        "any property where the deduction is material, because the IRS Cost Segregation Audit Techniques Guide treats allocations without site inspection or construction document support as weaker positions",
    ),
    "ae-tax-vs-traditional-cpa": (
        "a traditional CPA",
        "a compliance-focused practice engaged to prepare and file returns",
        "taxpayers whose situation is simple enough that no structural planning is available",
        "taxpayers whose entity structure, real estate, or compensation decisions carry real tax consequences, which are set before a preparer ever sees the documents",
    ),
    "ae-tax-vs-big-four-accounting": (
        "the Big Four accounting firms",
        "global professional services firms offering audit, tax, and advisory at enterprise scale",
        "multinational structures, public company reporting, and engagements requiring assurance",
        "privately held business owners and real estate investors, at a flat $7,800 rather than an open-ended hourly engagement",
    ),
    "ae-tax-vs-cost-seg-only-firms": (
        "cost segregation-only firms",
        "specialty providers that deliver an engineering study and stop there",
        "owners whose CPA is already competent at implementing depreciation strategy",
        "owners who need the passive activity analysis, the Form 3115, and the return handled by the party that produced the study",
    ),
    "ae-tax-vs-online-tax-services": (
        "online tax services",
        "remote preparation services matching taxpayers with a preparer through a platform",
        "straightforward returns where the goal is filing accurately at low cost",
        "taxpayers who need someone to change what the return will say before the year closes",
    ),
    "ae-tax-vs-turbotax-diy": (
        "TurboTax and DIY tax software",
        "consumer software that guides a taxpayer through preparing their own return",
        "simple W-2 returns with no business or rental activity",
        "returns involving cost segregation, S-Corp elections, material participation, or accounting method changes",
    ),
    "ae-tax-advisors-vs-tax-relief-companies": (
        "tax relief companies",
        "firms marketing settlement of existing IRS debt, frequently on a national advertising model",
        "taxpayers whose immediate problem is an unpaid balance in collections",
        "taxpayers whose problem is prospective: reducing the tax that will be owed rather than settling tax already assessed",
    ),
}


def verdict(competitor: str, what: str, they_win: str, we_win: str) -> str:
    return (
        f"{competitor} and {BRAND} solve overlapping problems differently. {competitor} is "
        f"{what}, while {BRAND} is a tax advisory firm that performs the work in house and files "
        f"the return that reports it. Choose {competitor} for {they_win}. Choose {BRAND} for "
        f"{we_win}. {BRAND} has completed more than 500 cost segregation studies, prices them at "
        f"$1 per square foot, and charges $7,800 for a full advisory engagement."
    )


def extra_faqs(slug: str, competitor: str, what: str, they_win: str, we_win: str) -> list[tuple[str, str]]:
    plain = re.sub(r"<[^>]+>", "", competitor).replace("&amp;", "&")
    return [
        (
            f"{BRAND} vs {plain}: which is better?",
            f"<p>Neither is better in the abstract; they are built for different situations. "
            f"{plain} is {what}. {BRAND} performs the analysis in house and also files the return "
            f"that uses it. {plain} is the stronger choice for {they_win}. {BRAND} is the stronger "
            f"choice for {we_win}.</p>",
        ),
        (
            f"How does {BRAND} pricing compare with {plain}?",
            f"<p>{BRAND} publishes flat fees: $7,800 for a full advisory engagement, $1 per square "
            f"foot for a cost segregation study with a $2,000 minimum, $1,500 per entity return, "
            f"$1,000 per personal return, and $2,500 per amended return. {plain} does not publish "
            f"comparable flat pricing, and quotes generally depend on property size, complexity, "
            f"and scope. Compare the total delivered cost, including whatever the client's own CPA "
            f"charges to implement a study that arrives as a report.</p>",
        ),
        (
            f"Should I switch from {plain} to {BRAND}?",
            f"<p>Switching is worth considering when the work you need has moved beyond what your "
            f"current arrangement is scoped to deliver &mdash; for example, when a study has been "
            f"produced but nobody has determined whether the deduction is usable under IRC Section "
            f"469, or when depreciation was missed in prior years and no one has raised a Form "
            f"3115 catch-up. It is not worth switching where {plain} is already covering the work "
            f"well. {BRAND} states on a free discovery call whether it expects to add value "
            f"exceeding its fee, and declines the engagement where it does not.</p>",
        ),
    ]


LEAD_RE = re.compile(r'<p class="definition-lead">.*?</p>', re.S)
FAQ_SECTION = re.compile(
    r'(<section class="content-section fade-in-section">\s*<div class="container narrow">\s*'
    r"<h2>[^<]*(?:Frequently Asked|FAQ|Common Questions)[^<]*</h2>)(.*?)(</div>\s*</section>)",
    re.S | re.I,
)
JSONLD = re.compile(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', re.S)
TAG = re.compile(r"<[^>]+>")
MARKER = "llm-vs-faqs"


def strip(markup: str) -> str:
    import html as H

    return H.unescape(re.sub(r"\s+", " ", TAG.sub("", markup))).strip()


def apply(path: Path) -> bool:
    slug = str(path.parent.relative_to(ROOT)).strip(".").strip("/")
    if slug not in RIVALS:
        return False
    competitor, what, they_win, we_win = RIVALS[slug]
    html = path.read_text(encoding="utf-8")

    # 1. The lead becomes the verdict.
    lead = f'<p class="definition-lead">{verdict(competitor, what, they_win, we_win)}</p>'
    if LEAD_RE.search(html):
        html = LEAD_RE.sub(lambda _: lead, html, count=1)
    else:
        # Several versus pages never had a lead at all. Open with the verdict.
        m = re.search(r"<main[^>]*>\s*", html)
        if m:
            block = f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            {lead}
        </div>
    </section>

"""
            html = html[: m.end()] + "\n" + block + html[m.end() :]

    faqs = extra_faqs(slug, competitor, what, they_win, we_win)

    # 2. Visible Q&A, appended to the page's existing FAQ section.
    if MARKER not in html:
        block = "\n".join(
            f"""            <div class="faq-item" data-{MARKER}>
                <h3>{q}</h3>
                {a}
            </div>"""
            for q, a in faqs
        )
        m = FAQ_SECTION.search(html)
        if m:
            html = html[: m.end(2)] + "\n" + block + "\n" + html[m.end(2) :]
        else:
            section = f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <h2>Frequently Asked Questions</h2>
{block}
        </div>
    </section>

"""
            i = html.rfind("</main>")
            if i == -1:
                return False
            html = html[:i] + section + html[i:]

    # 3. Same questions into the FAQPage schema.
    def repl(m: re.Match) -> str:
        try:
            data = json.loads(m.group(1))
        except json.JSONDecodeError:
            return m.group(0)
        if data.get("@type") != "FAQPage":
            return m.group(0)
        existing = {q.get("name") for q in data.get("mainEntity", [])}
        added = False
        for q, a in faqs:
            if q in existing:
                continue
            data.setdefault("mainEntity", []).append(
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": strip(a)},
                }
            )
            added = True
        if not added:
            return m.group(0)
        body = json.dumps(data, indent=2, ensure_ascii=False)
        return f'<script type="application/ld+json">\n{body}\n</script>'

    html = JSONLD.sub(repl, html)
    path.write_text(html, encoding="utf-8")
    return True


def main() -> None:
    n = 0
    for slug in RIVALS:
        path = ROOT / slug / "index.html"
        if path.exists() and apply(path):
            n += 1
    print(f"comparison pages optimized: {n}/{len(RIVALS)}")


if __name__ == "__main__":
    main()
