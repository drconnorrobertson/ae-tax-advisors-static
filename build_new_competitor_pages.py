#!/usr/bin/env python3
"""Publish researched, distinct comparisons requested September 28, 2026."""

import html
import site_template as T

DATE = "2026-09-28"
BASE = "/compare/"

PAGES = [
    {
        "slug": "andrew-cordle-vs-ae-tax",
        "name": "Andrew Cordle",
        "title": "Andrew Cordle vs AE Tax Advisors: Education or Tax Engagement?",
        "description": "Compare Andrew Cordle's public financial education and real estate content with AE Tax Advisors' tax planning and filing engagement. See what to verify before buying.",
        "lead": "Andrew Cordle publishes business, wealth, real estate, and tax education. AE Tax Advisors sells a defined tax advisory engagement. If you found a useful Cordle article about a tax strategy, the next question is who will test that idea against your returns and implement it for your facts.",
        "facts": [
            "Cordle's public site emphasizes financial literacy, business structures, a newsletter, and wealth education. His separate real estate site describes investing education.",
            "His tax articles discuss topics such as cost segregation, real estate professional status, and retirement structures. An article is general education and does not establish eligibility on a specific return.",
            "The public pages reviewed did not establish a standard, directly comparable annual tax preparation and advisory package or fee. Ask for a written scope if you are considering a particular Cordle offer or referral.",
        ],
        "sources": [("Andrew Cordle official site", "https://andrewcordle.com/"), ("Andrew Cordle tax articles", "https://andrewcordle.com/category/tax/"), ("Andrew Cordle real estate education", "https://andrewcordlerei.com/")],
        "rows": [
            ("Public emphasis", "Financial literacy, business and wealth education, real estate content", "Individualized business and real estate tax planning"),
            ("Personal tax return review", "Confirm within the specific offer", "Included in advisory analysis"),
            ("Written tax implementation", "Confirm provider and scope", "Planning and implementation are scoped in the engagement"),
            ("Business and individual return filing", "Confirm within the specific offer", "Available, priced separately"),
            ("Published tax advisory price", "No directly comparable standard fee confirmed", "$7,800 strategic or $9,800 complex advisory"),
        ],
        "strength": "Cordle is a useful source of business and real estate education for someone exploring how owners build and protect wealth. His public content can introduce strategies worth discussing with a qualified advisor. An education product, event, referral, or separate professional engagement may have a different scope, so identify the actual provider before comparing prices.",
        "fit": "Choose Cordle's educational content when you want ideas and a broader business or investing perspective. Choose a defined AE Tax engagement when you want a professional to review your entities, books, returns, and properties, model applicable tax rules, and coordinate the resulting filings. You can read his content and still hire a tax advisor to test it.",
        "questions": [
            "Who is the contracting firm and the individual who signs or reviews the return?",
            "Is the offer education, coaching, a referral, or personalized tax advice?",
            "Will someone verify basis, at-risk rules, material participation, and passive loss limits before claiming real estate deductions?",
            "Who prepares amendments, elections, depreciation schedules, Form 3115 when applicable, and the final return?",
            "What are the complete first-year and renewal fees?",
        ],
        "faqs": [
            ("Does Andrew Cordle prepare tax returns?", "The public pages reviewed are focused on education and did not establish a standard return-preparation engagement. Ask the specific program or professional provider who will prepare and sign your return before purchasing."),
            ("Is AE Tax Advisors an alternative to Andrew Cordle?", "For personalized tax planning and return implementation, AE Tax Advisors is an option to compare. For events, financial literacy, or general real estate investing education, the offerings serve different purposes."),
            ("Can I use a tax idea from Andrew Cordle's content?", "Bring the article to your tax professional. Eligibility and timing depend on your facts, including ownership, business use, basis, participation, and the year a property is placed in service."),
        ],
        "related": [("/compare/jasmine-dilucci-vs-ae-tax/", "Jasmine DiLucci vs AE Tax Advisors"), ("/compare/karlton-dennis-vs-ae-tax/", "Karlton Dennis vs AE Tax Advisors")],
    },
    {
        "slug": "karlton-dennis-vs-ae-tax",
        "name": "Karlton Dennis and Tax Alchemy",
        "title": "Karlton Dennis (Tax Alchemy) vs AE Tax Advisors (2026)",
        "description": "Compare Karlton Dennis's Tax Alchemy with AE Tax Advisors using each firm's published scope and pricing. Tax Alchemy lists $20,000 to $150,000 fees.",
        "lead": "Karlton Dennis leads Tax Alchemy, which publicly offers tax planning, implementation, and return filing for advisory clients. This is a direct tax advisory comparison. The clearest difference visible in the published materials is price and the scope to request in writing, not a claim that one team lacks tax expertise.",
        "facts": [
            "Tax Alchemy's own FAQ describes a one-year planning and implementation engagement priced from $20,000 to $150,000, depending on strategies and complexity.",
            "Tax Alchemy says its advisory clients may have individual, business, and trust or estate returns filed by its tax strategists. Do not assume filing is unavailable or outsourced.",
            "Its public materials also describe support for business owners and real estate investors, entity structure, and planning outside real estate.",
        ],
        "sources": [("Tax Alchemy official FAQ", "https://taxalchemy.com/faqs/"), ("Karlton Dennis at Tax Alchemy", "https://taxalchemy.com/karlton-dennis/")],
        "rows": [
            ("Published advisory fee", "$20,000 to $150,000 flat fee, based on strategy", "$7,800 strategic or $9,800 complex advisory"),
            ("Engagement period", "One year, renewable", "Confirm term in engagement letter"),
            ("Planning and implementation", "Both described publicly", "Both available within defined scope"),
            ("Tax return filing", "Available to Tax Alchemy advisory clients", "Available, priced separately"),
            ("Business and real estate focus", "Both", "Both"),
            ("Cost segregation and prior-year correction", "Confirm deliverables and any extra fees", "Available; scope and separate service fees apply"),
        ],
        "strength": "Tax Alchemy has a substantial tax education presence and expressly offers planning plus implementation. Its FAQ gives a useful fee range and confirms filing for advisory clients. A buyer seeking a higher-budget, year-long program should request a sample plan and a precise list of strategies, filings, access, and renewal terms.",
        "fit": "Choose Tax Alchemy if its program, assigned team, and written implementation scope fit the complexity and value of your situation. Choose AE Tax Advisors if you want the published $7,800 or $9,800 advisory tier and separately scoped returns, amendments, and real estate work. Compare total first-year cost on the same set of deliverables.",
        "questions": [
            "What strategies will be implemented this tax year, and who owns each task?",
            "Which business, individual, and trust returns are included in the quote?",
            "Are prior-year amendments, cost segregation studies, and Form 3115 included or separately billed?",
            "Who will review the passive activity, at-risk, basis, and documentation limits?",
            "What is the renewal fee and what continuing work does it cover?",
        ],
        "faqs": [
            ("How much does it cost to work with Karlton Dennis's Tax Alchemy?", "Tax Alchemy's official FAQ says its flat-fee tax planning and implementation services range from $20,000 to $150,000. The price of your particular engagement requires a quote. AE Tax Advisors publishes $7,800 strategic and $9,800 complex advisory tiers, with other work priced separately."),
            ("Does Tax Alchemy file tax returns?", "Yes. Its official FAQ says its advisory clients can have individual, business, and trust or estate returns filed through Tax Alchemy. Ask which returns are included in your proposal."),
            ("What is a Karlton Dennis alternative for a business owner?", "AE Tax Advisors is one option for an owner seeking a written tax plan, return review, and implementation. Compare the assigned professionals, exact deliverables, first-year total, and renewal terms."),
        ],
        "related": [("/compare/tax-alchemy-vs-ae-tax/", "More on Tax Alchemy and AE Tax Advisors"), ("/compare/jasmine-dilucci-vs-ae-tax/", "Jasmine DiLucci vs AE Tax Advisors")],
    },
    {
        "slug": "jasmine-dilucci-vs-ae-tax",
        "name": "Jasmine DiLucci and DiLucci CPA Firm",
        "title": "Jasmine DiLucci CPA Firm vs AE Tax Advisors (2026)",
        "description": "Compare Jasmine DiLucci's CPA firm with AE Tax Advisors on tax planning, bookkeeping, IRS resolution, returns, business owners, and real estate tax work.",
        "lead": "Jasmine DiLucci's firm provides a broad accounting and tax relationship, including bookkeeping and IRS resolution. AE Tax Advisors concentrates on proactive owner and real estate tax planning, prior-year analysis, and related filings. The choice depends on whether you need ongoing accounting and an IRS case, a targeted planning project, or both.",
        "facts": [
            "The firm's official site identifies Jasmine DiLucci as an attorney, CPA, and enrolled agent, and describes a father-daughter firm with John DiLucci.",
            "DiLucci CPA Firm lists tax planning and return preparation, bookkeeping, and IRS tax resolution, including installment agreements, penalty abatement, and offers in compromise evaluation.",
            "It describes federal and state business and individual return filing, including partnerships, S corporations, and C corporations. Its site does not publish one universal advisory price for a like-for-like comparison.",
        ],
        "sources": [("DiLucci CPA Firm official services", "https://dilucci.com/")],
        "rows": [
            ("Public focus", "Tax, accounting, bookkeeping, and IRS resolution", "Tax advisory for profitable owners and real estate investors"),
            ("Credentials described", "Jasmine DiLucci: attorney, CPA, EA", "CPA-led tax advisory team"),
            ("Business and individual returns", "Yes, listed service", "Yes, priced separately"),
            ("Bookkeeping", "Full-service and review options listed", "Book cleanup and coordination as scoped"),
            ("IRS resolution", "Prominent specialist service", "Confirm representation scope for your case"),
            ("Published advisory price", "Request a proposal", "$7,800 strategic or $9,800 complex advisory"),
        ],
        "strength": "DiLucci CPA Firm's combination of tax law credentials, bookkeeping, return preparation, and IRS resolution is valuable when the books and a live IRS issue need attention alongside planning. The published service menu is broader than a tax strategy alone. Ask which professional will lead each part of your engagement and how the work is coordinated.",
        "fit": "Choose DiLucci CPA Firm if you want ongoing bookkeeping and tax compliance under one roof or need its tax resolution practice. Choose AE Tax Advisors if your primary project is reviewing a profitable business and property portfolio for current and prior-year tax opportunities, then coordinating the applicable returns and studies. Request written proposals for identical deliverables before deciding.",
        "questions": [
            "Who prepares and reviews each return and who handles any IRS matter?",
            "Does the proposal include monthly bookkeeping, cleanup, or only tax planning?",
            "Will prior-year returns, depreciation schedules, and entity elections be reviewed?",
            "If real estate losses are proposed, who analyzes material participation and passive activity limits?",
            "What is included in the first-year fee, and what recurs next year?",
        ],
        "faqs": [
            ("Is Jasmine Delucci the same person as Jasmine DiLucci?", "The tax attorney, CPA, and enrolled agent who leads the firm spells her name Jasmine DiLucci on her official website. This page uses that spelling."),
            ("Does DiLucci CPA Firm do bookkeeping and IRS resolution?", "Yes. Both are prominently listed on its official website, alongside planning and tax return preparation. Ask for a proposal tailored to the services you actually need."),
            ("Is AE Tax Advisors a Jasmine DiLucci alternative?", "AE Tax Advisors is an option for business and real estate tax planning, prior-year review, and related filings. If you need substantial bookkeeping or a specialized IRS debt-resolution matter, compare those capabilities and fees explicitly."),
        ],
        "related": [("/compare/karlton-dennis-vs-ae-tax/", "Karlton Dennis vs AE Tax Advisors"), ("/compare/andrew-cordle-vs-ae-tax/", "Andrew Cordle vs AE Tax Advisors")],
    },
    {
        "slug": "tax-goddess-vs-ae-tax",
        "name": "Tax Goddess Business Services",
        "title": "Tax Goddess vs AE Tax Advisors (2026 Comparison)",
        "description": "Compare Tax Goddess Business Services and AE Tax Advisors on business owner tax planning, program scope, pricing transparency, implementation, and real estate work.",
        "lead": "Tax Goddess Business Services and AE Tax Advisors both market proactive tax planning to business owners. Tax Goddess emphasizes its Strategic Tax Coaching process and an elite offer for owners earning $1 million or more. AE Tax Advisors publishes specific advisory tiers and separate service prices. Compare a written plan and implementation duties, not advertised savings rates.",
        "facts": [
            "Tax Goddess identifies Shauna A. Wekherlien, CPA, MTax, as its leader and describes a tax strategy practice for business leaders, professionals, and entrepreneurs.",
            "Its Strategic Tax Coaching page describes a proprietary planning process. The elite offer page is directed at owners earning at least $1 million.",
            "The firm advertises aggregate savings and an average client tax rate. Those are the firm's marketing claims, not a prediction for an individual taxpayer. Request the methodology and a projection using your own facts.",
            "A directly comparable standard advisory fee was not confirmed on the reviewed service pages. Request a complete written proposal.",
        ],
        "sources": [("Tax Goddess official website", "https://taxgoddess.com/"), ("Strategic Tax Coaching", "https://taxgoddess.com/strategic-tax-coaching/"), ("Elite Tax Strategy", "https://taxgoddess.com/elite-tax-strategy/")],
        "rows": [
            ("Public positioning", "Proactive tax strategy and Strategic Tax Coaching", "Business and real estate tax advisory"),
            ("High-income owner offer", "Elite page addresses business owners earning $1M+", "Engagement fit assessed on discovery call"),
            ("Published advisory fee", "Request a current proposal", "$7,800 strategic or $9,800 complex advisory"),
            ("Prior-year returns and amendments", "Confirm exact scope and fees", "Review available; amendments separately priced"),
            ("Business and individual filing", "Confirm what the specific offer includes", "Available, priced separately"),
            ("Real estate and cost segregation", "Confirm property-specific work and provider", "Available, separately scoped"),
        ],
        "strength": "Tax Goddess has a clear business-owner audience and an established branded planning process. Its elite page is explicit about the $1 million plus owner profile. For an owner whose facts match that profile, ask to see how the team moves from a proposed strategy to documentation, implementation, and signed returns.",
        "fit": "Choose Tax Goddess if its assigned team, coaching process, and written scope meet your needs and the proposed fee is justified by your own projections. Choose AE Tax Advisors if published advisory tiers, a prior-year review, separately priced filing, and real estate implementation fit your project. Both firms should be asked to quantify the opportunity after limitations and implementation costs.",
        "questions": [
            "Who designs the plan and who implements each item?",
            "Are tax returns, amended returns, cost segregation, and bookkeeping included or extra?",
            "How is a proposed savings figure calculated for my facts, including limitations and future tax effects?",
            "What documents and elections will support each position?",
            "What are the first-year and renewal fees and the assigned team's meeting cadence?",
        ],
        "faqs": [
            ("Is Tax Goddess an alternative to AE Tax Advisors?", "Yes. Both address proactive planning for business owners, but their offers and written scopes should be compared on the same set of deliverables. AE Tax Advisors publishes advisory tiers, while Tax Goddess should be asked for a tailored quote."),
            ("Does Tax Goddess guarantee a specific tax rate for me?", "Its site advertises results and an average rate for its clients. An average or marketing claim does not establish your likely result. Ask for the calculation, client cohort, and a fact-specific projection before relying on it."),
            ("How much does Tax Goddess cost?", "A directly comparable standard fee was not confirmed on the reviewed service pages. Request a current written proposal that separates planning, implementation, filing, any study, and renewal."),
        ],
        "related": [("/compare/karlton-dennis-vs-ae-tax/", "Karlton Dennis vs AE Tax Advisors"), ("/compare/jasmine-dilucci-vs-ae-tax/", "Jasmine DiLucci vs AE Tax Advisors")],
    },
]


def p(text):
    return f"            <p>{html.escape(text)}</p>"


def bullets(items):
    return '            <ul class="takeaway-list">\n' + '\n'.join(f"                <li>{html.escape(x)}</li>" for x in items) + '\n            </ul>'


def render(data):
    path = f"{BASE}{data['slug']}/"
    crumb = [("Home", "/"), ("Compare", BASE), (data["name"], path)]
    cells = '\n'.join(f'<tr><th scope="row">{html.escape(a)}</th><td>{html.escape(b)}</td><td>{html.escape(c)}</td></tr>' for a, b, c in data['rows'])
    table = f'''            <div class="ae-table-scroll" style="overflow-x:auto"><table class="compare-table">
                <caption>Publicly described services reviewed September 28, 2026. Verify current scope and fees in a proposal.</caption>
                <thead><tr><th scope="col">Decision factor</th><th scope="col">{html.escape(data['name'])}</th><th scope="col">AE Tax Advisors</th></tr></thead><tbody>{cells}</tbody></table></div>'''
    sources = ' '.join(f'<a href="{html.escape(url)}" rel="nofollow external noopener">{html.escape(label)}</a>' for label, url in data['sources'])
    faqs = [(q, p(a).strip()) for q, a in data['faqs']]
    body = '\n'.join([
        T.page_header(h1=data['title'], subtitle=data['description'], trail=crumb),
        T.section("The short answer", p(data['lead'])),
        T.section("What the public materials say", bullets(data['facts']) + f'            <p><strong>Sources:</strong> {sources}</p>'),
        T.section("Compare the actual work", table),
        T.section(f"Where {data['name']} may fit", p(data['strength'])),
        T.section("How to choose", p(data['fit']) + p("AE Tax Advisors publishes $7,800 strategic and $9,800 complex advisory tiers. Returns, amendments, and studies are separately scoped. See the current pricing page for the complete service menu.")),
        T.section("Five questions to put in the engagement letter", bullets(data['questions'])),
        T.faq_section(faqs),
        T.related_section(data['related'] + [("/pricing/", "AE Tax Advisors pricing"), ("/discovery/", "Book a discovery call")], "Related comparisons"),
        T.section("Editorial disclosure", p("AE Tax Advisors publishes this independent comparison and is not affiliated with the people or firms discussed. Services and prices can change. A service that is not confirmed in public materials may still be available; ask each provider directly. This page is general information, not personal tax advice.")),
    ])
    schema = [T.article_schema(title=data['title'], description=data['description'], url=T.SITE + path, published=DATE, modified=DATE, section="Tax Advisory Comparison", keywords=[data['name'], data['name'].split(' and ')[0] + ' alternatives', 'AE Tax Advisors'], citations=[u for _, u in data['sources']] + [T.SITE + '/pricing/']), T.breadcrumb_schema(crumb)]
    return T.build_page(title=data['title'], description=data['description'], path=path, body=body, schemas=schema, published=DATE, modified=DATE)


if __name__ == "__main__":
    for data in PAGES:
        print(T.write_page(BASE + data['slug'], render(data)))
