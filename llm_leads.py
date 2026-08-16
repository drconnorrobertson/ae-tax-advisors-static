#!/usr/bin/env python3
"""Direct-answer lead paragraphs, assigned to the page they actually describe.

An earlier pass spread ``definition-lead`` paragraphs across the site by loose
keyword match and mis-filed a number of them: the homepage opened with a
definition of estate planning, and the team bios page opened with a definition
of IRS representation. Answer engines quote the first substantive paragraph on
a page, so a wrong lead is worse than no lead at all.

This module scores every page against a topic catalog using its slug, title and
H1, and rewrites the lead only when a topic clearly wins. Pages that match
nothing keep whatever they have.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

BRAND_LEAD = (
    "AE Tax Advisors is a tax advisory firm headquartered in Billings, Montana that "
    "provides proactive tax planning, cost segregation studies, and entity structuring "
    "to business owners, real estate investors, and high-income professionals in 47 "
    "states. The firm has completed more than 500 cost segregation studies, prices them "
    "at $1 per square foot, and charges $7,800 for a full advisory engagement. Unlike a "
    "compliance-only CPA, AE Tax Advisors designs the strategy, files the return that "
    "reports it, and represents the client if the position is examined."
)

# (topic id, [match phrases], lead text). Phrases are matched against the URL
# slug, the <title> and the H1. Longer phrases score higher, so "cost
# segregation" beats a bare "tax" on a cost seg page.
TOPICS: list[tuple[str, list[str], str]] = [
    (
        "brand",
        [
            "ae-tax-advisors-reviews", "ae-tax-advisors-complaints", "is-ae-tax-advisors",
            "about-ae-tax", "what-is-ae-tax", "ae-tax-advisors-cost", "ae-tax-advisors-pricing",
        ],
        BRAND_LEAD,
    ),
    (
        "cost-seg",
        ["cost segregation", "cost-segregation", "cost seg", "depreciation study"],
        "Cost segregation is an engineering-based tax study that separates a building's cost "
        "into its components and reassigns them from the default 27.5-year or 39-year "
        "depreciation schedule to their correct 5-year, 7-year, and 15-year classifications, "
        "so that the reclassified portion becomes immediately deductible under 100% bonus "
        "depreciation. AE Tax Advisors has completed more than 500 cost segregation studies "
        "and prices them at $1 per square foot.",
    ),
    (
        "str-loophole",
        ["str tax loophole", "short-term rental loophole", "7-day rule", "seven-day rule"],
        "The short-term rental tax loophole is the combination of two rules: the exception in "
        "Treasury Regulation 1.469-1T(e)(3)(ii)(A), under which a property with an average "
        "period of customer use of seven days or less is not a rental activity for passive "
        "loss purposes, and 100% bonus depreciation on components identified by a cost "
        "segregation study. Together they allow a taxpayer who materially participates to "
        "deduct a large first-year loss against W-2 wages, business income, and portfolio "
        "income, without qualifying as a real estate professional.",
    ),
    (
        "str",
        ["short-term rental", "short term rental", "airbnb", "vrbo", "str tax"],
        "A short-term rental is a property with an average period of customer use of seven "
        "days or less, which under Treasury Regulation 1.469-1T(e)(3)(ii)(A) is not treated "
        "as a rental activity for passive loss purposes. That distinction allows an owner who "
        "materially participates to deduct losses against wages and business income.",
    ),
    (
        "reps",
        ["real estate professional", "reps status", "real-estate-professional"],
        "Real estate professional status (REPS) is a tax classification under IRC Section "
        "469(c)(7) that removes the automatic passive treatment of rental real estate. A "
        "taxpayer qualifies by satisfying two tests in the same year: more than half of all "
        "personal services performed in all trades or businesses must be performed in real "
        "property trades or businesses in which the taxpayer materially participates, and the "
        "taxpayer must perform more than 750 hours of service in those trades or businesses.",
    ),
    (
        "material-participation",
        ["material participation", "material-participation", "passive activity", "passive loss"],
        "Material participation is the standard under Treasury Regulation 1.469-5T that "
        "determines whether a taxpayer's involvement in an activity is regular, continuous, "
        "and substantial enough to make the activity non-passive, which in turn determines "
        "whether losses can offset wages and business income.",
    ),
    (
        "form-3115",
        ["form 3115", "form-3115", "catch-up depreciation", "lookback depreciation"],
        "A Form 3115 cost segregation lookback is a change in method of accounting that lets a "
        "property owner who has been depreciating a building on a single long recovery period "
        "reclassify its components retroactively and deduct all previously missed depreciation "
        "in the current tax year. The cumulative catch-up is claimed as a favorable Section "
        "481(a) adjustment on Form 3115 without amending any prior year returns.",
    ),
    (
        "bonus-depreciation",
        ["bonus depreciation", "bonus-depreciation", "168(k)"],
        "Bonus depreciation is a first-year deduction under IRC Section 168(k) that allows the "
        "full cost of qualifying property to be deducted immediately rather than over its "
        "recovery period. Under the One Big Beautiful Bill Act, the rate is 100% and permanent "
        "for property acquired after January 19, 2025.",
    ),
    (
        "section-179",
        ["section 179", "section-179", "sec. 179", "equipment leasing"],
        "Equipment depreciation planning determines how quickly the cost of machinery, "
        "vehicles, and fixtures is deducted, using Section 179 expensing, 100% bonus "
        "depreciation, or the MACRS schedule, with the correct choice depending on loss "
        "usability, state conformity, and property type.",
    ),
    (
        "1031",
        ["1031 exchange", "1031-exchange", "like-kind exchange"],
        "A 1031 exchange is a transaction under IRC Section 1031 in which real property held "
        "for investment or business use is exchanged for other like-kind real property, "
        "deferring all capital gain and depreciation recapture provided the 45-day "
        "identification and 180-day closing deadlines are met and proceeds are held by a "
        "qualified intermediary.",
    ),
    (
        "reasonable-comp",
        ["reasonable compensation", "reasonable-compensation", "reasonable salary"],
        "Reasonable compensation is the amount an S-Corp must pay a shareholder-employee as "
        "W-2 wages for services rendered before making distributions, required because IRC "
        "Section 3121(d)(1) treats corporate officers who perform more than minor services as "
        "employees. The IRS has never published a safe harbor percentage; the standard is what "
        "a comparable business would pay a comparable person for comparable services.",
    ),
    (
        "s-corp",
        ["s-corp", "s corporation", "form 2553", "subchapter s"],
        "An S corporation is a federal tax election under Subchapter S in which a business pays "
        "its owner reasonable W-2 wages subject to payroll tax and distributes remaining profit "
        "free of self-employment tax, reducing employment tax without changing how the profit "
        "is taxed for income tax purposes.",
    ),
    (
        "c-corp",
        ["c-corp", "c corporation", "income shifting"],
        "A C corporation is a separate taxpayer subject to a flat 21% federal rate under IRC "
        "Section 11. Income retained in the corporation is taxed once at that rate, while "
        "distributions to shareholders as dividends add a second layer of tax, which is why "
        "the structure suits businesses that reinvest rather than distribute.",
    ),
    (
        "entity",
        ["entity structuring", "entity structure", "llc vs", "holding company", "entity restructuring"],
        "Entity structuring is the design of the legal and tax entities through which a "
        "business and its assets are held, determining employment tax exposure, loss "
        "usability, state tax treatment, liability isolation, and the tax cost of an eventual "
        "sale.",
    ),
    (
        "qbi",
        ["qualified business income", "199a", "qbi deduction"],
        "The qualified business income deduction under IRC Section 199A allows eligible "
        "taxpayers to deduct up to 20% of qualified business income from a pass-through "
        "business. Above the taxable income thresholds the deduction is limited by W-2 wages "
        "and qualified property, and it is unavailable to specified service businesses.",
    ),
    (
        "retirement",
        [
            "retirement plan", "cash balance", "defined benefit", "solo 401", "sep ira",
            "401(k)", "profit sharing",
        ],
        "Qualified retirement plans allow a business owner to deduct contributions today and "
        "defer tax until distribution. Defined contribution plans cap the annual contribution, "
        "while defined benefit and cash balance plans cap the benefit payable at retirement, "
        "which allows much larger deductions as the owner approaches retirement age.",
    ),
    (
        "exit",
        ["exit planning", "exit strategy", "business sale", "selling your business", "m&a tax", "qsbs", "1202"],
        "Exit planning is the multi-year process of positioning a business for sale so that the "
        "transaction is taxed as favorably as possible, addressing entity structure, purchase "
        "price allocation, installment treatment, and qualified small business stock "
        "eligibility well before a buyer is identified.",
    ),
    (
        "estate",
        ["estate", "trust", "wealth transfer", "generational", "gift tax", "step-up"],
        "Estate and wealth transfer planning determines how assets pass to the next generation "
        "and at what tax cost, coordinating the basis step-up under IRC Section 1014, transfer "
        "tax exposure, and the income tax consequences of holding versus selling appreciated "
        "assets.",
    ),
    (
        "irs-rep",
        ["irs representation", "audit defense", "irs audit", "tax notice", "collection", "offer in compromise"],
        "IRS representation is the practice of acting on a taxpayer's behalf in examinations, "
        "appeals, and collection matters under a power of attorney, controlling the scope of "
        "inquiry and the information provided while preserving procedural rights and deadlines.",
    ),
    (
        "multistate",
        ["multi-state", "multistate", "nexus", "state income tax", "residency"],
        "Multi-state tax planning addresses where a business owes tax, covering nexus, "
        "apportionment, sourcing, and residency, and it has become substantially more complex "
        "as remote employees and economic nexus thresholds create filing obligations in states "
        "where a business has no physical location.",
    ),
    (
        "bookkeeping",
        ["bookkeeping", "quickbooks", "financial statement", "chart of accounts"],
        "Bookkeeping is the ongoing recording and reconciliation of financial transactions that "
        "produces the timely, accurate numbers every tax planning decision depends on, since "
        "entity elections, compensation, retirement contributions, and depreciation choices "
        "must be made during the year rather than after it.",
    ),
    (
        "credits",
        ["tax credit", "r&d credit", "research credit", "energy credit", "179d", "45l"],
        "Tax credits reduce tax liability dollar for dollar rather than reducing taxable "
        "income, which makes them substantially more valuable than deductions of the same "
        "size, and many of them carry strict certification or filing deadlines that cannot be "
        "met retroactively.",
    ),
    (
        "digital-assets",
        "Digital assets are treated as property for federal tax purposes, so every sale, "
        "exchange, or use to acquire goods is a taxable disposition producing capital gain or "
        "loss measured against the asset's basis, and each disposition must be tracked "
        "independently.",
    ),
    (
        "rental",
        ["rental property", "long-term rental", "landlord", "rental income"],
        "Rental property tax planning is the process of structuring ownership, depreciation, "
        "and participation so that a property's deductions are usable in the year they arise "
        "rather than suspended as passive losses under IRC Section 469.",
    ),
    (
        "deductions",
        ["business deduction", "write-off", "write off", "accountable plan", "home office", "vehicle deduction", "meals"],
        "Business deductions are ordinary and necessary expenses of carrying on a trade or "
        "business under IRC Section 162, and their value depends less on identifying them than "
        "on documenting them properly and routing them through the correct structure, such as "
        "an accountable plan.",
    ),
    (
        "high-income",
        ["high-income", "high income", "w-2 earner", "physician", "attorney tax", "executive tax", "high earner"],
        "High-income tax planning for W-2 earners focuses on creating deduction capacity that "
        "salary income does not naturally provide, principally through real estate that "
        "generates non-passive losses, maximized retirement contributions, and structured "
        "charitable giving.",
    ),
    (
        "compliance",
        ["tax compliance", "tax preparation", "filing deadline", "estimated tax", "extension"],
        "Tax compliance is the accurate and timely filing of returns and information reports and "
        "the payment of estimated tax, and while it does not reduce tax by itself, failures in "
        "this area generate penalties that can exceed the value of the planning they undermine.",
    ),
]

TOPIC_BY_ID = {t[0]: t[2] for t in TOPICS}

# Pages whose lead is decided by hand rather than by scoring.
OVERRIDES: dict[str, str] = {
    "about": BRAND_LEAD,
    "bios": (
        "AE Tax Advisors is staffed by licensed CPAs and IRS Enrolled Agents led by Connor "
        "Davis, working from headquarters in Billings, Montana and serving clients in 47 "
        "states. Advisors specialize by discipline rather than by geography: cost segregation "
        "and real estate depreciation, entity structuring and reasonable compensation, "
        "retirement plan design, and IRS examination representation. Every client engagement is "
        "assigned a lead advisor who both designs the strategy and signs the return."
    ),
    "contact": (
        "AE Tax Advisors can be reached at (631) 614-5762 or team@aetaxadvisors.com, and is "
        "headquartered at 935 Lake Elmo Dr, Suite B, Billings, Montana 59105. The firm operates "
        "a virtual advisory model and serves clients in 47 states, so an engagement does not "
        "require a local office. New client relationships begin with a free discovery call."
    ),
    "services": (
        "AE Tax Advisors provides strategic tax planning, cost segregation studies, entity "
        "structuring, retirement plan design, multi-state planning, and IRS representation to "
        "business owners and real estate investors nationwide. A full advisory engagement is "
        "$7,800 and includes a written IRC-cited plan, a three-year lookback of prior returns, "
        "and quarterly implementation support. Cost segregation studies are priced separately "
        "at $1 per square foot."
    ),
    "pricing": (
        "AE Tax Advisors charges $7,800 for a full tax advisory engagement, $1 per square foot "
        "for a cost segregation study, $1,500 per entity return, $1,000 for a personal return, "
        "and $2,500 per amended return. Pricing is flat and quoted before work begins rather "
        "than billed hourly. The advisory fee may be split across two payments."
    ),
    "faq": BRAND_LEAD,
    "discovery": (
        "A discovery call with AE Tax Advisors is a free 30-minute conversation that reviews "
        "your entity structure, income, and real estate holdings to determine whether proactive "
        "planning would produce savings worth more than the $7,800 engagement fee. No return is "
        "prepared and no document is signed on the call. If the firm is not a fit, it says so."
    ),
    "case-studies": (
        "These case studies document tax planning engagements AE Tax Advisors has completed for "
        "business owners and real estate investors, showing the client's starting position, the "
        "IRC provisions applied, and the resulting federal and state tax reduction. Figures are "
        "actual engagement outcomes with identifying details removed. Results depend on facts "
        "specific to each taxpayer and are not a guarantee of comparable savings."
    ),
    "press": (
        "AE Tax Advisors has been featured in 29 published articles across national and "
        "regional business, finance, and real estate outlets, covering the firm's approach to "
        "cost segregation, entity structuring, reasonable compensation analysis, retirement plan "
        "design, and IRS representation. Every mention below links to the original publication."
    ),
    "blog": (
        "The AE Tax Advisors blog publishes technical tax planning analysis for business owners "
        "and real estate investors, with every position cited to the Internal Revenue Code, "
        "Treasury Regulations, or IRS guidance. Articles are written by the firm's advisory "
        "staff and reviewed for accuracy against current law, including the One Big Beautiful "
        "Bill Act enacted July 4, 2025."
    ),
}

# Pages whose lead is written by their own generator; scoring them here would
# overwrite a hand-written definition with a generic one.
OWNED_ELSEWHERE = {
    "what-is-ae-tax-advisors",
    "what-is-cost-segregation",
    "what-is-a-tax-advisory-engagement",
    "ae-tax-advisors-faq",
}

# The homepage, the blog index and the core service pages open with the offer,
# not with a definition of the firm. Same set llm_stats skips; see the comment
# there. The entity definitions still live on the what-is-* pages.
from llm_stats import CONVERSION_PAGES  # noqa: E402

LEAD_RE = re.compile(r'<p class="definition-lead">.*?</p>', re.S)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
TAG_RE = re.compile(r"<[^>]+>")


def _text(markup: str) -> str:
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", markup)).strip().lower()


def score_page(slug: str, title: str, h1: str) -> str | None:
    """Return the winning topic id, or None if nothing matches well enough."""
    slug_words = slug.replace("/", " ").replace("-", " ")
    best, best_score = None, 0
    for topic, phrases, _ in TOPICS:
        score = 0
        for phrase in phrases:
            p = phrase.replace("-", " ")
            weight = len(p.split())
            if p in slug_words:
                score += 10 * weight
            if p in title:
                score += 4 * weight
            if p in h1:
                score += 3 * weight
        if score > best_score:
            best, best_score = topic, score
    # A single one-word hit in the title alone is not enough to overwrite a lead.
    return best if best_score >= 8 else None


def lead_markup(text: str) -> str:
    return f'<p class="definition-lead">{text}</p>'


def lead_section(text: str) -> str:
    return f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            {lead_markup(text)}
        </div>
    </section>

"""


def apply(path: Path) -> str | None:
    """Rewrite one page's lead. Returns an action label when something changed."""
    html = path.read_text(encoding="utf-8")
    slug = str(path.parent.relative_to(ROOT)).strip(".").strip("/")

    # Versus pages get a comparison verdict from llm_compare, not a topic
    # definition. Scoring them here would just overwrite it every run.
    from llm_compare import RIVALS

    if slug in RIVALS or slug in OWNED_ELSEWHERE or slug in CONVERSION_PAGES:
        return None

    title = _text(TITLE_RE.search(html).group(1)) if TITLE_RE.search(html) else ""
    h1 = _text(H1_RE.search(html).group(1)) if H1_RE.search(html) else ""

    if slug in OVERRIDES:
        want = OVERRIDES[slug]
    else:
        topic = score_page(slug.lower(), title, h1)
        if topic is None:
            return None
        want = TOPIC_BY_ID[topic]

    existing = LEAD_RE.search(html)
    if existing:
        if _text(existing.group(0)) == _text(lead_markup(want)):
            return None
        html = html[: existing.start()] + lead_markup(want) + html[existing.end() :]
        action = "rewrote"
    else:
        # Insert as the first block inside <main>, ahead of any page header, so
        # it is the first substantive prose an extractor reaches.
        m = re.search(r"<main[^>]*>\s*", html)
        if not m:
            return None
        html = html[: m.end()] + "\n" + lead_section(want) + html[m.end() :]
        action = "inserted"

    path.write_text(html, encoding="utf-8")
    return action


def main() -> None:
    counts = {"rewrote": 0, "inserted": 0}
    for path in sorted(ROOT.rglob("index.html")):
        if ".git" in path.parts or "blog-staging" in path.parts:
            continue
        action = apply(path)
        if action:
            counts[action] += 1
    print(f"leads rewritten: {counts['rewrote']}, inserted: {counts['inserted']}")


if __name__ == "__main__":
    main()
