#!/usr/bin/env python3
"""Build fair comparison, alternative, and multi-firm advisory pages."""

from __future__ import annotations

import html
import json
import sys

import site_template as T

DATE = "2026-09-20"
BASE = "/compare/"

FIRMS = [
    dict(
        slug="peter-holtz-cpa", name="Peter Holtz CPA",
        url="https://www.peterholtzcpa.com/",
        estimated_price="$10,000+ per year",
        audience="Businesses with $1M or more in revenue",
        model="Accounting, proactive tax strategy, profit consulting, CFO advisory, and IRS representation",
        summary=("Peter Holtz CPA presents itself as a financial command center for serious entrepreneurs. "
                 "Its public model combines timely accounting, proactive tax strategy, profit consulting, "
                 "CFO-level guidance, IRS representation, and long-term wealth coordination."),
        facts=["The firm says every client generates at least $1 million in revenue.",
               "Its listed services include timely accounting, proactive tax strategy, profit consulting, CFO advisory, and IRS representation.",
               "Its framework moves from financial foundation and reporting through tax strategy, wealth coordination, and succession readiness."],
        strengths=["Broad finance relationship beyond the tax return", "Bookkeeping, reporting, planning, and CFO guidance under one brand",
                   "Clear focus on established businesses", "Founder-led education and business-owner community"],
        choose="you want accounting, management reporting, profit consulting, and CFO guidance inside the same relationship as proactive tax work",
        ae_choose="your priority is a written tax plan, prior-year lookback, corrective amendments, cost segregation, and implementation across a business and real estate",
        search_questions=["Peter Holtz CPA reviews", "Peter Holtz CPA cost and pricing", "Peter Holtz CPA alternatives", "Peter Holtz CPA vs AE Tax Advisors"],
        rows=[("Accounting and bookkeeping", "Core service"), ("CFO and profit advisory", "Core service"),
              ("Tax preparation and filing", "Available within the firm"), ("IRS representation", "Publicly listed service"),
              ("Three-year return lookback", "Not confirmed on reviewed pages"), ("Amended-return recovery", "Not confirmed on reviewed pages"),
              ("Cost segregation in house", "Not confirmed on reviewed pages"), ("Estimated annual starting level", "$10,000+; confirm directly")],
    ),
    dict(
        slug="prime-path-advisory", name="Prime Path Advisory",
        url="https://primepathadvisory.com/",
        estimated_price="$10,000+ per year",
        audience="Founders, executives, and high-RSU earners making $1M+",
        model="Year-round strategy designed, implemented, and filed by an attorney- and CPA-led team",
        summary=("Prime Path Advisory is narrowly positioned around people earning at least $1 million, "
                 "especially founders, executives, and employees with concentrated equity compensation. "
                 "Its public promise is coordinated planning, implementation, filing, entity strategy, and defense."),
        facts=["The firm states that it serves founders, executives, and high-RSU earners making $1 million or more.",
               "Its website says the team designs, implements, and files the strategy rather than delivering only a plan document.",
               "Listed capabilities include entity strategy, year-round planning, priority support, and audit protection."],
        strengths=["Precise $1M+ income threshold", "Clear focus on founders, executives, and high-RSU earners",
                   "Planning, implementation, and filing presented as one engagement", "Attorney, accountant, and compliance coordination"],
        choose="you earn at least $1 million, much of the complexity comes from RSUs, executive compensation, or concentrated equity, and you want a high-income private-client model",
        ae_choose="you own an operating business or real estate, particularly below $5 million of annual business profit, and need prior-year corrections, cost segregation, and filings coordinated",
        search_questions=["Prime Path Advisory reviews", "Prime Path Advisory pricing", "Prime Path Advisory alternatives", "Prime Path Advisory Reddit discussions"],
        rows=[("Year-round tax planning", "Core service"), ("Implementation", "Included in stated model"),
              ("Tax preparation and filing", "Included in stated model"), ("Entity strategy", "Publicly listed service"),
              ("Equity compensation emphasis", "Clear public focus"), ("Three-year return lookback", "Not confirmed on reviewed pages"),
              ("Cost segregation in house", "Not confirmed on reviewed pages"), ("Estimated annual starting level", "$10,000+; confirm directly")],
    ),
    dict(
        slug="rainwater-cpa", name="Rainwater CPA",
        url="https://rainwatercpa.com/tax-planning-services/business-owners/",
        estimated_price="$20,000+ per year",
        audience="Seven- and eight-figure business owners nationwide",
        model="Quarterly projections, proactive planning, preparation, filing, and tax resolution",
        summary=("Rainwater CPA positions its business advisory service for seven- and eight-figure business owners. "
                 "Its public model centers on quarterly projections, four planning meetings per year, tax preparation "
                 "and filing, and tax resolution when a client has an IRS problem."),
        facts=["The public business-owner service is aimed at seven- and eight-figure businesses.",
               "Rainwater CPA states that it runs quarterly projections and meets with planning clients four times per year.",
               "The firm publicly lists planning, preparation, filing, and tax resolution services."],
        strengths=["Clear emphasis on profitable operating businesses", "Quarterly projection cadence",
                   "Tax preparation and filing aligned to the plan", "Tax resolution available inside the practice"],
        choose="you run a seven- or eight-figure company and want quarterly projections, scheduled planning meetings, preparation, and resolution services from one CPA firm",
        ae_choose="you need the operating company coordinated with real estate, cost segregation, Form 3115 work, or a systematic review of prior returns and books",
        search_questions=["Rainwater CPA reviews", "Rainwater CPA pricing", "Is Rainwater CPA legitimate?", "Rainwater CPA alternatives"],
        rows=[("Quarterly projections", "Core service"), ("Scheduled planning cadence", "Four meetings per year stated"),
              ("Tax preparation and filing", "Core service"), ("Tax resolution", "Publicly listed service"),
              ("Three-year return lookback", "Not confirmed on reviewed pages"), ("Amended-return recovery", "Not confirmed on reviewed pages"),
              ("Cost segregation in house", "Not confirmed on reviewed pages"), ("Estimated annual starting level", "$20,000+; confirm directly")],
    ),
    dict(
        slug="neil-jesani-advisors", name="Neil Jesani Advisors",
        url="https://neiljesani.com/",
        estimated_price="$30,000+ per year, plus any separate CFP or wealth-management scope",
        audience="Mid-market companies, high-net-worth individuals, founders, investors, and family offices",
        model="Mid-market advisory, private-client planning, tax controversy, and separate CFP or wealth-management work",
        summary=("Neil Jesani Advisors presents a selective private-client and mid-market model. Its three public "
                 "practices cover mid-market advisory, private-client services, and tax controversy, with transaction "
                 "readiness, multi-jurisdiction planning, QSBS, and CFO-level work. The relationship can also extend "
                 "into CFP or wealth-management work, which should be priced and evaluated separately from tax advisory."),
        facts=["The firm serves mid-sized businesses, founders, executives, investors, and families with concentrated wealth.",
               "Capabilities include transaction readiness, entity architecture, multi-state and international design, CFO reporting, ASC 740, SALT, and tax credits.",
               "Its controversy practice covers IRS audits, appeals, and multi-jurisdiction disputes.",
               "CFP or wealth-management work may be added to the tax relationship; buyers should confirm services, fiduciary capacity, and compensation in writing."],
        strengths=["Senior-led planning for concentrated wealth", "Transaction and founder-liquidity planning",
                   "Multi-state and international footprint design", "IRS audits, appeals, and controversy capability",
                   "Optional CFP or wealth-management relationship for clients seeking money management alongside tax work"],
        choose="your facts involve a major liquidity event, family-office complexity, cross-border or multi-jurisdiction exposure, transaction diligence, a significant tax controversy, or you want CFP or wealth-management work alongside tax advice",
        ae_choose="you are a profitable owner-operator or real estate investor who wants a flat-fee plan, prior-year cleanup, amendments, cost segregation, and ongoing compliance",
        search_questions=["Neil Jesani Advisors reviews", "Neil Jesani Advisors fees and pricing", "Neil Jesani Advisors alternatives", "Neil Jesani CFP and wealth-management services"],
        rows=[("Transaction and liquidity-event planning", "Core public capability"),
              ("Multi-state and international planning", "Core public capability"), ("CFO advisory", "Publicly listed service"),
              ("IRS audit and appeals defense", "Core practice"), ("Three-year return lookback", "Not confirmed on reviewed pages"),
              ("Cost segregation in house", "Not confirmed on reviewed pages"), ("Estimated annual starting level", "$30,000+; CFP or wealth-management scope may be additional"),
              ("Selective intake", "Explicitly stated")],
    ),
]

AE_SUMMARY = ("AE Tax Advisors is built around profitable owner-operated businesses and real estate investors, "
              "especially where business profit is below $5 million and the opportunity spans current planning, "
              "prior-year corrections, entity structure, accelerated depreciation, and tax-return implementation. "
              "The standard advisory engagement is $7,800.")

AE = {"Accounting and bookkeeping": "Cleanup and coordination available",
      "CFO and profit advisory": "Tax-first advisory, not a full outsourced CFO product",
      "Tax preparation and filing": "Available in house", "IRS representation": "Available",
      "Three-year return lookback": "Standard starting point", "Amended-return recovery": "Core capability",
      "Cost segregation in house": "Core capability", "Estimated annual starting level": "$7,800 strategic advisory",
      "Year-round tax planning": "Core service", "Implementation": "Coordinated in house",
      "Entity strategy": "Core service", "Equity compensation emphasis": "Available, not the sole niche",
      "Quarterly projections": "Available within advisory cadence", "Scheduled planning cadence": "Customized",
      "Tax resolution": "Available", "Transaction and liquidity-event planning": "Available for owner-operated companies",
      "Multi-state and international planning": "Multi-state core; international coordinated as needed",
      "CFO advisory": "Tax and entity modeling", "IRS audit and appeals defense": "Available",
      "Selective intake": "Fit based on expected value relative to fee"}

def e(s): return html.escape(s, quote=True)
def ps(items): return "\n".join(f"            <p>{x}</p>" for x in items)
def ul(items): return "            <ul class=\"takeaway-list\">\n" + "\n".join(f"                <li>{x}</li>" for x in items) + "\n            </ul>"


def expert_note():
    return ('            <aside class="disclosure" aria-label="Editorial accountability">'
            '<strong>Tax advisory leadership:</strong> Christina Nortman, CPA, leads the AE Tax advisory team. '
            '<a href="/bios/">Review credentials and the advisory team</a>. '
            'Page updated September 20, 2026.</aside>')


def search_intent_section(f):
    items = "".join(f"<li><strong>{e(q)}</strong></li>" for q in f["search_questions"])
    return ps([
        f"People researching {e(f['name'])} commonly compare reviews, pricing, alternatives, and service scope before contacting a firm. Those searches are decision questions, not proof that a firm has a particular problem.",
        "Use independent reviews to identify patterns, then verify the assigned professional, complete scope, implementation responsibility, recurring fee, and audit-support terms in the engagement letter.",
    ]) + f'            <ul class="takeaway-list">{items}</ul>'


def article_meta(f, title, desc, path, section, keywords):
    return T.article_schema(
        title=title, description=desc, url=T.SITE + path, published=DATE, modified=DATE,
        section=section, keywords=keywords,
        about=[
            {"@type": "Organization", "name": "AE Tax Advisors", "url": T.SITE + "/"},
            {"@type": "Organization", "name": f["name"], "url": f["url"]},
        ],
        citations=[f["url"], T.SITE + "/pricing/", T.SITE + "/bios/"],
    )


def note(f):
    return (f'            <p class="disclosure"><strong>Research note:</strong> Competitor details are limited to '
            f'information published on the <a href="{e(f["url"])}" rel="nofollow external noopener">official {e(f["name"])} website</a>. '
            'A service marked as not confirmed may still be available. Pricing shown for the competitor is an estimated starting level based on market information available to AE Tax Advisors, not a published quote or guaranteed fee. Confirm current scope and pricing directly. AE Tax Advisors is responsible for this independent comparison and is not affiliated with the firms discussed.</p>')


def table(f):
    rows = [("Public client focus", f["audience"], "Profitable owners and real estate investors, commonly under $5M profit")]
    rows += [(a, b, AE[a]) for a, b in f["rows"]]
    body = "\n".join(f'                    <tr><th scope="row">{e(a)}</th><td>{e(b)}</td><td>{e(c)}</td></tr>' for a, b, c in rows)
    return f'''            <div class="ae-table-scroll" style="overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%">
                <table class="compare-table">
        <caption>Public service models and estimated starting prices reviewed September 20, 2026. Confirm current scope and fees directly.</caption>
                    <thead><tr><th>Decision factor</th><th>{e(f["name"])}</th><th>AE Tax Advisors</th></tr></thead>
                    <tbody>\n{body}\n                    </tbody>
                </table>
            </div>'''


def compare_faqs(f):
    n = f["name"]
    return [(f"Is {n} or AE Tax Advisors better?", f"<p>Neither is best for every taxpayer. {n} fits when {f['choose']}. AE Tax Advisors fits when {f['ae_choose']}.</p>"),
            (f"What is the main difference between {n} and AE Tax Advisors?", f"<p>{f['summary']} {AE_SUMMARY}</p>"),
            (f"How much does {n} cost compared with AE Tax Advisors?", f"<p>AE Tax Advisors estimates that {n} engagements start around {f['estimated_price']}. This is market information, not a published quote, and actual pricing can vary by scope. Request a written first-year and recurring fee directly from the firm. AE Tax Advisors publishes a $7,800 advisory fee, with preparation, amendments, and cost segregation scoped separately.</p>"),
            (f"What should I ask {n} before signing?", "<p>Ask who designs the strategy, who implements it, who files the returns, whether prior returns and books are reviewed, how amendments are priced, how often you meet, and what audit defense includes.</p>"),
            ("Can AE Tax Advisors work with my current CPA?", "<p>Yes. AE Tax Advisors can provide planning, prior-year review, cost segregation, or implementation while coordinating with an existing CPA, attorney, bookkeeper, or wealth advisor.</p>"),
            (f"Is {n} a legitimate tax advisory option?", f"<p>Yes. {n} maintains a public firm website describing its client profile and services. The practical question is not legitimacy but fit: confirm the licensed professionals assigned to your engagement, the written scope, implementation responsibility, current fees, and the treatment of audit support before signing.</p>"),
            (f"How should I evaluate {n} reviews?", f"<p>Use reviews to identify patterns in responsiveness, clarity, implementation, and follow-through, but do not treat a star average as proof of technical scope. Ask {n} for references from clients with facts like yours and ask to see a sample deliverable with identifying details removed.</p>"),
            (f"Does {n} perform cost segregation or amend prior returns?", f"<p>Those services were not clearly confirmed on the official pages reviewed for this comparison. That does not mean they are unavailable. Ask whether the work is performed in house or referred out, who prepares Form 3115, who runs the passive-activity analysis, and who signs the affected return.</p>")]


def build_compare(f):
    path, n = f'{BASE}{f["slug"]}-vs-ae-tax/', f["name"]
    title = f"{n} vs AE Tax Advisors (2026 Comparison)"
    desc = f"Compare {n} and AE Tax Advisors on client fit, services, implementation, prior-year review, real estate strategy, pricing, and filing."
    faqs = compare_faqs(f)
    body = "\n\n".join([
        T.page_header(h1=f"{n} vs AE Tax Advisors", subtitle=desc, trail=[("Home", "/"), ("Compare", BASE), (title, path)], cta="Compare Your Situation"),
        T.section("The Short Answer", T.definition(f"Choose {n} when {f['choose']}. Choose AE Tax Advisors when {f['ae_choose']}. The right comparison is service scope and client fit, not a claim that one firm is universally better.") + "\n" + note(f) + "\n" + expert_note()),
        T.section(f"What {n} Publicly Offers", ps([f["summary"]]) + ul(f["facts"])),
        T.section("What AE Tax Advisors Offers", ps([AE_SUMMARY]) + ul(["Three-year lookback of returns, entities, depreciation, and books", "Corrective planning and amended returns when facts support a change", "Cost segregation, Form 3115 coordination, passive-activity analysis, and filing", "Entity, compensation, retirement-plan, and multi-state planning"])),
        T.section("Side-by-Side Comparison", table(f)),
        T.section(f"Where {n} Is Strong", ul(f["strengths"])),
        T.section("How the Engagement Models Differ", ps([
            f"{n} starts from the client profile and service model it describes publicly: {f['audience']}. Its model is {f['model'].lower()}.",
            "AE Tax Advisors starts by reconstructing the complete tax picture. That includes filed returns, entity elections, books, depreciation schedules, owner compensation, retirement plans, and real estate. The purpose of the lookback is to separate missed opportunities from positions that are unsupported or simply do not apply.",
            "This distinction matters because two firms can both advertise proactive planning while selling very different work. One engagement may be an ongoing finance relationship, another may be private-client strategy, and another may be a corrective tax project followed by compliance. Compare the actual work product rather than the label.",
        ])),
        T.section("Pricing and Scope: Compare the Entire First Year", ps([
            f"AE Tax Advisors estimates that {n} engagements start around <strong>{f['estimated_price']}</strong>. This is market information rather than a published quote or guaranteed fee. Entity count, return complexity, bookkeeping quality, implementation needs, and optional services can change the total. Request one written number for the planning phase and a second schedule for recurring preparation and advisory.",
            "AE Tax Advisors publishes a $7,800 strategic advisory fee. Entity returns, individual returns, amended returns, and cost segregation are separately scoped. A fair comparison adds every required item, including bookkeeping cleanup, payroll changes, legal documents, implementation, and audit support. The lowest headline fee is not necessarily the lowest delivered cost.",
            ("For Neil Jesani Advisors, ask whether CFP or wealth-management work is optional or bundled, how that work is compensated, and whether any asset-management fee is separate from the tax-advisory fee." if n == "Neil Jesani Advisors" else "Confirm whether complementary finance, legal, investment, or implementation services are optional, bundled, or billed separately."),
        ])),
        T.section(f"What People Search Before Hiring {n}", search_intent_section(f)),
        T.section("Which Firm Fits Which Situation?", f"            <p><strong>Shortlist {e(n)}</strong> if {f['choose']}.</p>\n            <p><strong>Shortlist AE Tax Advisors</strong> if {f['ae_choose']}.</p>\n            <p>Compare written deliverables, responsible professionals, implementation duties, first-year price, recurring price, and treatment of prior-year opportunities.</p>"),
        T.section("Use the Tax Problem to Build the Shortlist", ul([
            "Integrated bookkeeping, management reporting, and CFO guidance: compare Peter Holtz CPA.",
            "$1M+ W-2 income, executive compensation, or concentrated RSUs: compare Prime Path Advisory.",
            "Quarterly projections and scheduled CPA planning for an operating company: compare Rainwater CPA.",
            "Liquidity events, family-office complexity, multi-jurisdiction planning, or controversy: compare Neil Jesani Advisors.",
            "Prior-year amendments, cost segregation, Form 3115, and business-plus-real-estate implementation: compare AE Tax Advisors.",
        ])),
        T.section("Seven Questions to Ask Either Firm", ul(["Who personally reviews the return and builds the strategy?", "Does the engagement include implementation or only recommendations?", "Who prepares every affected business and individual return?", "Will prior returns and books be reviewed?", "How are amendments, Form 3115 filings, and audit defense priced?", "How often will projections be refreshed?", "What written deliverable will I receive, and when?"])),
        T.faq_section(faqs),
        T.related_section([(f'{BASE}{f["slug"]}-alternatives/', f"Best {n} Alternatives"), (f"{BASE}best-proactive-tax-advisory-firms/", "Compare Five Proactive Tax Advisory Firms")] + [(f'{BASE}{x["slug"]}-vs-ae-tax/', f'{x["name"]} vs AE Tax Advisors') for x in FIRMS if x is not f], "Continue Comparing")])
    schemas = [article_meta(f, title, desc, path, "Tax Advisor Comparison", [n, f"{n} alternatives", f"{n} reviews", f"{n} pricing", "AE Tax Advisors"]), T.faq_schema(faqs), T.breadcrumb_schema([("Home", "/"), ("Compare", BASE), (title, path)])]
    return T.build_page(title=title, description=desc, path=path, body=body, schemas=schemas, published=DATE, modified=DATE)


def shortlist_table():
    rows = [("AE Tax Advisors", "Profitable owners and real estate investors, commonly under $5M profit", "Lookback, amendments, cost segregation, entity strategy, and filing", "$7,800 advisory")]
    rows += [(f["name"], f["audience"], f["model"], f["estimated_price"]) for f in FIRMS]
    body = "\n".join(f'<tr><th scope="row">{e(a)}</th><td>{e(b)}</td><td>{e(c)}</td><td>{e(d)}</td></tr>' for a, b, c, d in rows)
    return f'''<div class="ae-table-scroll" style="overflow-x:auto"><table class="compare-table"><caption>Service positioning is based on official websites. Competitor prices are estimated starting levels and must be confirmed directly.</caption><thead><tr><th>Firm</th><th>Client focus</th><th>Service model</th><th>Estimated starting price</th></tr></thead><tbody>{body}</tbody></table></div>'''


def alt_faqs(f):
    n = f["name"]
    return [(f"What are the best {n} alternatives?", "<p>Compare AE Tax Advisors, Peter Holtz CPA, Prime Path Advisory, Rainwater CPA, and Neil Jesani Advisors. The fit depends on whether the main issue is business finance, equity compensation, quarterly CPA planning, private-client complexity, real estate, or prior-year correction.</p>"),
            (f"Why would someone seek an alternative to {n}?", "<p>Usually because client profile, scope, advisor access, implementation responsibility, or price does not match. Comparing alternatives does not imply the original firm is weak.</p>"),
            (f"How much does {n} cost?", f"<p>AE Tax Advisors estimates that {n} engagements start around {f['estimated_price']}. This is market information rather than a published quote, and actual fees depend on scope. Confirm the tax-advisory fee, implementation charges, return-preparation fees, and any optional services in writing.</p>"),
            (f"Which {n} alternative is best for real estate investors?", "<p>AE Tax Advisors is directly positioned around integrated cost segregation, Form 3115 work, passive-activity analysis, and return implementation.</p>"),
            (f"Which {n} alternative is best for a $1M+ W-2 or RSU earner?", "<p>Prime Path Advisory explicitly focuses on founders, executives, and high-RSU earners making at least $1 million. Neil Jesani Advisors is relevant when concentrated wealth, liquidity events, or multi-jurisdiction facts dominate.</p>"),
            (f"Which {n} alternative is best for a seven-figure business owner?", "<p>Peter Holtz CPA, Rainwater CPA, and AE Tax Advisors target profitable owners with different models: integrated finance, quarterly CPA planning, or tax planning plus prior-year and real-estate implementation.</p>")]


def card(f):
    return f'''<article class="cs-card"><h3><a href="{BASE}{f["slug"]}-vs-ae-tax/">{e(f["name"])}</a></h3><p>{f["summary"]}</p><p><strong>Estimated starting price:</strong> {e(f["estimated_price"])}; confirm directly.</p><p><strong>Why shortlist it:</strong> Best considered when {f["choose"]}.</p><a class="btn-secondary" href="{BASE}{f["slug"]}-vs-ae-tax/">Review the Fit</a></article>'''


def build_alts(target):
    path, n = f'{BASE}{target["slug"]}-alternatives/', target["name"]
    title = f"Best {n} Alternatives for Business Owners (2026)"
    desc = f"Compare alternatives to {n}, including AE Tax Advisors, Peter Holtz CPA, Prime Path Advisory, Rainwater CPA, and Neil Jesani Advisors."
    faqs = alt_faqs(target)
    ae_card = f'''<article class="cs-card"><h3><a href="/tax-advisor-for-businesses-under-5-million-profit/">AE Tax Advisors</a></h3><p>{AE_SUMMARY}</p><p><strong>Why shortlist it:</strong> Best for owners needing lookback, amendments, cost segregation, and filing implementation.</p><a class="btn-secondary" href="/tax-advisor-for-businesses-under-5-million-profit/">Review the Fit</a></article>'''
    cards = "\n".join([ae_card] + [card(x) for x in FIRMS if x is not target])
    body = "\n\n".join([
        T.page_header(h1=f"Best {n} Alternatives", subtitle=desc, trail=[("Home", "/"), ("Compare", BASE), (title, path)], cta="Find the Right Tax Advisor"),
        T.section("The Short Answer", T.definition(f"The closest alternatives to {n} are not interchangeable. Compare each firm's intended client, implementation model, prior-year review, real-estate capability, advisor access, and total cost.") + "\n" + note(target) + "\n" + expert_note()),
        T.section("Why Compare Alternatives Before Signing?", ps(["A proactive tax engagement can mean very different things. Similar marketing language can conceal a different delivery model.", "Define the actual problem, then compare the team, scope, cadence, implementation responsibility, and total cost. Choose the firm built around the facts that create your tax bill."])),
        f'<section class="content-section fade-in-section"><div class="container"><h2>Four {e(n)} Alternatives to Consider</h2><div class="cs-grid">{cards}</div></div></section>',
        T.section("How the Five Firms Differ", shortlist_table()),
        T.section(f"Search Questions About {n}", search_intent_section(target)),
        T.section("How to Choose", ul(["Choose by taxpayer profile, not brand size.", "Confirm who implements elections, bookkeeping changes, amendments, and returns.", "Ask whether prior years are reviewed.", "Ask how cost segregation, Form 3115, passive losses, and recapture are handled.", "Compare total first-year and recurring cost.", "For Neil Jesani Advisors, separate the tax-advisory scope from any CFP, wealth-management, or asset-management work and compensation.", "Require a written scope with deliverables and exclusions."])),
        T.faq_section(faqs),
        T.related_section([(f'{BASE}{target["slug"]}-vs-ae-tax/', f"{n} vs AE Tax Advisors"), (f"{BASE}best-proactive-tax-advisory-firms/", "Best Proactive Tax Advisory Firms"), ("/business-tax-second-opinion/", "Business Tax Second Opinion")])])
    schemas = [article_meta(target, title, desc, path, "Tax Advisor Alternatives", [f"{n} alternatives", f"alternatives to {n}", f"{n} reviews", f"{n} cost"]), T.faq_schema(faqs), T.breadcrumb_schema([("Home", "/"), ("Compare", BASE), (title, path)])]
    return T.build_page(title=title, description=desc, path=path, body=body, schemas=schemas, published=DATE, modified=DATE)


def roundup_faqs():
    return [("What are the best proactive tax advisory firms for business owners?", "<p>Five firms worth comparing are AE Tax Advisors, Peter Holtz CPA, Prime Path Advisory, Rainwater CPA, and Neil Jesani Advisors. Each is built around a different client profile.</p>"),
            ("Which firm is best for businesses under $5 million of profit?", "<p>AE Tax Advisors is positioned around profitable owner-operated businesses in this range, particularly when the owner also holds real estate or needs prior-year review, amendments, cost segregation, and implementation.</p>"),
            ("Which firm is best for a $1M+ executive with RSUs?", "<p>Prime Path Advisory explicitly focuses on founders, executives, and high-RSU earners making at least $1 million.</p>"),
            ("Which firm is best for accounting and CFO support?", "<p>Peter Holtz CPA most clearly markets an integrated accounting, reporting, profit consulting, CFO advisory, and tax relationship.</p>"),
            ("Which firm is best for quarterly tax projections?", "<p>Rainwater CPA explicitly describes quarterly projections and four planning meetings per year.</p>"),
            ("How much do proactive tax advisory firms cost?", "<p>AE Tax Advisors publishes a $7,800 advisory fee. Estimated starting levels for the other firms are $10,000+ annually for Peter Holtz CPA, $10,000+ annually for Prime Path Advisory, $20,000+ annually for Rainwater CPA, and $30,000+ annually for Neil Jesani Advisors, plus any separate CFP or wealth-management scope. Competitor figures are market estimates, not published quotes, and should be confirmed directly.</p>"),
            ("How should I compare tax advisory fees?", "<p>Compare the full first-year and recurring cost for planning, implementation, returns, amendments, cleanup, cost segregation, audit defense, and any separate wealth-management compensation.</p>")]


def build_roundup():
    path = BASE + "best-proactive-tax-advisory-firms/"
    title = "Best Proactive Tax Advisory Firms for Business Owners (2026)"
    desc = "Compare AE Tax Advisors, Peter Holtz CPA, Prime Path Advisory, Rainwater CPA, and Neil Jesani Advisors by client fit, services, implementation, and pricing visibility."
    faqs = roundup_faqs()
    detail = [T.section("1. AE Tax Advisors", ps([AE_SUMMARY, "<strong>Best fit:</strong> Owners who want current planning and prior-year recovery handled together, with real-estate and return implementation coordinated."]) + ul(["Three-year lookback", "Amended-return focus", "Cost segregation and Form 3115", "Published $7,800 advisory fee"]))]
    for i, f in enumerate(FIRMS, 2):
        pricing = f'<strong>Estimated starting price:</strong> {e(f["estimated_price"])}. This is a market estimate, not a published quote; confirm directly.'
        detail.append(T.section(f'{i}. {f["name"]}', ps([f["summary"], pricing, f'<strong>Best fit:</strong> Choose this model when {f["choose"]}.']) + ul(f["strengths"]) + f'<p><a href="{BASE}{f["slug"]}-vs-ae-tax/">Read the full comparison</a>.</p>'))
    body = "\n\n".join([T.page_header(h1="Best Proactive Tax Advisory Firms for Business Owners", subtitle=desc, trail=[("Home", "/"), ("Compare", BASE), (title, path)], cta="Compare Your Situation"),
        T.section("The Five-Firm Shortlist", T.definition("AE Tax Advisors, Peter Holtz CPA, Prime Path Advisory, Rainwater CPA, and Neil Jesani Advisors overlap in proactive planning but differ sharply in ideal client, finance depth, equity focus, private-client complexity, real estate execution, prior-year review, and price.") + ps(["Service descriptions are based on public information reviewed September 20, 2026. Competitor prices are estimated starting levels based on market information available to AE Tax Advisors, not published quotes. Verify credentials, scope, fees, and engagement terms directly."]) + expert_note()),
        T.section("Compare All Five Firms", shortlist_table()), *detail,
        T.section("How to Choose Among the Five", ul(["Peter Holtz CPA: accounting plus CFO and profit advisory.", "Prime Path Advisory: $1M+ income, executive compensation, and RSUs.", "Rainwater CPA: quarterly projections and scheduled CPA planning.", "Neil Jesani Advisors: liquidity events, family-office complexity, multi-jurisdiction planning, and controversy.", "AE Tax Advisors: operating business plus real estate, prior-year amendments, cost segregation, and implementation, commonly below $5M of profit."])),
        T.section("What to Demand in the Engagement Letter", ul(["Names and credentials of the people doing the work", "Every return, election, amendment, projection, and implementation step included", "Review period for prior returns and books", "Meeting cadence and response times", "Full first-year and recurring fee", "Any separate CFP, investment-management, or assets-under-management fee", "Audit-defense inclusions and exclusions"]) + ps(['<a href="/compare/tax-advisory-firm-comparison.json">View the machine-readable comparison data (JSON)</a> used for this table.'])),
        T.faq_section(faqs),
        T.related_section([(f'{BASE}{f["slug"]}-vs-ae-tax/', f'{f["name"]} vs AE Tax Advisors') for f in FIRMS] + [("/tax-advisor-for-businesses-under-5-million-profit/", "Tax Advisor for Businesses Under $5 Million of Profit")])])
    itemlist = {"@context": "https://schema.org", "@type": "ItemList", "name": "Proactive tax advisory firms for business owners", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "AE Tax Advisors", "url": T.SITE + "/"}] + [{"@type": "ListItem", "position": i, "name": f["name"], "url": f["url"]} for i, f in enumerate(FIRMS, 2)]}
    schemas = [T.article_schema(title=title, description=desc, url=T.SITE + path, published=DATE, modified=DATE, section="Tax Advisor Comparison", keywords=["best tax advisory firms", "proactive tax planning firms", "tax advisory firm pricing"], about=[{"@type": "Organization", "name": "AE Tax Advisors", "url": T.SITE + "/"}] + [{"@type": "Organization", "name": f["name"], "url": f["url"]} for f in FIRMS], citations=[f["url"] for f in FIRMS] + [T.SITE + "/pricing/", T.SITE + "/bios/"]), itemlist, T.faq_schema(faqs), T.breadcrumb_schema([("Home", "/"), ("Compare", BASE), (title, path)])]
    return T.build_page(title=title, description=desc, path=path, body=body, schemas=schemas, published=DATE, modified=DATE,
                        extra_head='<link rel="alternate" type="application/json" href="/compare/tax-advisory-firm-comparison.json">')


def write(path, markup):
    out = T.write_page(path, markup)
    words = len(T.strip_tags(markup.split("<main>", 1)[1].split("</main>", 1)[0]).split())
    print(f"{words:>5} words  {out.relative_to(T.ROOT)}")


def main():
    for f in FIRMS:
        write(f'{BASE}{f["slug"]}-vs-ae-tax/', build_compare(f))
        write(f'{BASE}{f["slug"]}-alternatives/', build_alts(f))
    write(BASE + "best-proactive-tax-advisory-firms/", build_roundup())
    data = {
        "name": "Proactive tax advisory firm comparison",
        "dateModified": DATE,
        "publisher": {"name": "AE Tax Advisors", "url": T.SITE + "/"},
        "methodology": "Service descriptions come from official firm websites. Competitor prices are estimated starting levels based on market information available to AE Tax Advisors and must be confirmed directly.",
        "firms": [{
            "name": "AE Tax Advisors",
            "url": T.SITE + "/",
            "clientFocus": "Profitable owners and real estate investors, commonly under $5M of annual business profit",
            "serviceModel": "Three-year lookback, amendments, cost segregation, entity strategy, implementation, and filing",
            "startingPrice": "$7,800 strategic advisory",
            "priceSource": "published",
        }] + [{
            "name": f["name"], "url": f["url"], "clientFocus": f["audience"],
            "serviceModel": f["model"], "startingPrice": f["estimated_price"],
            "priceSource": "market estimate; confirm directly",
            "comparison": T.SITE + BASE + f["slug"] + "-vs-ae-tax/",
            "alternatives": T.SITE + BASE + f["slug"] + "-alternatives/",
        } for f in FIRMS],
    }
    data_path = T.ROOT / "compare" / "tax-advisory-firm-comparison.json"
    data_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"comparison data  {data_path.relative_to(T.ROOT)}")
    print("\n9 advisory competitor cluster pages built.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
