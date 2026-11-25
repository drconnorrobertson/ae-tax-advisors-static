"""Publish AE's comparison guides from the providers' public materials."""
from html import escape
from xml.etree import ElementTree as ET

import site_template as T

DATE = "2026-11-25"
TRM = ("TRM CPA services and assessment", "https://trm.cpa/")
TRM_REVIEWS = ("Tyler McBroom’s client testimonial video", "https://www.youtube.com/watch?v=OySdK1V-afQ")
TRM_BBB = ("BBB business profile", "https://www.bbb.org/us/fl/palm-beach-gardens/profile/cpa/trm-tax-and-cfo-services-inc-0633-92050986")
GROWTH = ("Growth Circle membership", "https://growyournetworth.com/growthcircle")
CHECKOUT = ("Growth Circle checkout and billing terms", "https://growyournetworth.com/growth-circle-checkout")
TRUSTPILOT = ("Amplifi – Braiden Shaw on Trustpilot", "https://www.trustpilot.com/review/growyournetworth.com")
AE = ("AE Tax Advisors pricing", "/pricing/")
AE_FEES = (
    "AE publishes $7,800 for Strategic Tax Advisory and $9,800 for Complex Tax Advisory. "
    "Strategic has no required annual planning renewal. Returns, amendments and cost segregation "
    "studies are separately scoped. The agreement specifies the support period and audit defense coverage."
)

TYLER = [
    ("tyler-mcbroom-alternatives", "Tyler McBroom Alternatives for Business Tax Planning",
     "Compare alternatives to Tyler McBroom and TRM CPA for tax planning, filing, bookkeeping and CFO support.",
     [
         ("For a written tax plan across a business and rentals",
          "AE Tax Advisors is an option if you own an operating company and rental real estate and need one plan that accounts for both. Ask which household returns, entities and properties are in scope, how prior-year opportunities are evaluated and who implements each recommendation."),
         ("For one firm to handle planning and recurring accounting",
          "TRM CPA advertises proactive tax planning, preparation and filing, bookkeeping and CFO-level support. When evaluating other firms with similar services, ask for one written scope showing monthly close deadlines, reporting, planning meetings and which returns are covered."),
         ("For a second opinion or help with a single issue",
          "If your books and filing are already covered, compare a focused second opinion with a broader engagement. For example, ask a tax advisor to review owner compensation or a rental acquisition and specify the analysis, deadline and handoff to your current preparer."),
     ], [TRM, AE]),
    ("tyler-mcbroom-vs-ae-tax", "Tyler McBroom’s TRM CPA vs AE Tax Advisors",
     "Compare TRM CPA and AE Tax Advisors on planning, bookkeeping, return preparation, advisory fees and fit.",
     [
         ("What TRM CPA offers",
          "Tyler McBroom’s firm describes an ongoing model for business owners that combines tax planning, bookkeeping and CFO-level support. It also advertises business and personal filing. Ask how those services are packaged and which professional leads your account."),
         ("What AE Tax Advisors offers",
          "AE focuses on business and real estate tax planning. Its published scope includes entity review, prior-year amendment analysis and return preparation oversight. Complex advisory includes multi-entity and real estate portfolio planning. " + AE_FEES),
         ("Compare both proposals using the same facts",
          "Suppose you own an S corporation and two rentals and already have a bookkeeper. Give both firms the same entity list, returns and property schedules. Ask who reviews owner pay and depreciation, who prepares each return and what ongoing accounting would add to the fee. If you also need monthly financial reporting, ask for the deliverables and delivery dates in writing."),
     ], [TRM, AE]),
    ("tyler-mcbroom-pricing", "Tyler McBroom Pricing: TRM CPA Fees and AE Tax Costs",
     "See what TRM CPA publishes about pricing, what to ask for in a quote, and AE Tax Advisors’ published fees.",
     [
         ("How much does TRM CPA charge?",
          "TRM CPA advertises a free tax assessment for qualified business owners. AE did not find a public price for paid TRM CPA advisory on the firm’s service and assessment pages reviewed November 25, 2026. Contact TRM for current terms and a written quote."),
         ("How to compare the full cost",
          "Ask for the onboarding charge, total first-year fee and any minimum commitment. Request itemized pricing for planning, business and personal returns, monthly bookkeeping and CFO meetings. Ask which charges recur and how scope changes or additional entities are billed."),
         ("AE Tax Advisors’ published fees",
          AE_FEES + " AE lists business returns starting at $1,500 and eligible owner and investor personal returns starting at $1,000. Confirm your scope before comparing the first-year totals."),
     ], [TRM, AE]),
    ("tyler-mcbroom-reviews", "Tyler McBroom Reviews: How to Evaluate TRM CPA",
     "Find TRM CPA review sources and see what to look for when evaluating Tyler McBroom’s tax advisory firm.",
     [
         ("Where to read about client experiences",
          "Tyler McBroom publishes a video with selected TRM CPA client testimonials. The Better Business Bureau also hosts a profile for TRM Tax and CFO Services, Inc. Use the links below to see each source in context. This guide is published by AE Tax Advisors, a competing firm."),
         ("Read for the service you plan to buy",
          "Look for feedback from a business with a similar number of entities and a similar need for planning, filing or monthly accounting. Details about who answered questions, how often the team met and whether filings and follow-up were completed can help you assess fit."),
         ("Ask for evidence in the proposal",
          "If a review mentions tax savings, ask the firm what kind of analysis it would prepare for your facts and how it would document assumptions. Ask for a sample deliverable, the name of your lead advisor and an explanation of who owns implementation and filing."),
     ], [TRM, TRM_REVIEWS, TRM_BBB]),
]

BRAIDEN = [
    ("braiden-shaw-alternatives", "Braiden Shaw Alternatives for Tax Planning and Wealth Education",
     "Compare alternatives to Braiden Shaw’s Amplifi Growth Circle by tax planning, education and investment goals.",
     [
         ("For learning and community", "Growth Circle offers financial education, group calls and a private investing community. Compare memberships on curriculum, instructor access, renewal cost and what is required to participate in individual deals."),
         ("For a tax plan based on your records", "Consider AE Tax Advisors or another tax advisory firm if you need help reviewing business entities, rental properties or prior returns. Ask who will review your records, model the options and coordinate filing or implementation."),
         ("For ongoing portfolio advice", "If you need individualized investment advice, compare registered investment advisers on fees, services and conflicts. Ask how the adviser is paid and whether they review existing holdings before recommending changes."),
     ], [GROWTH, CHECKOUT, AE]),
    ("growth-circle-vs-ae-tax", "Braiden Shaw’s Growth Circle vs AE Tax Advisors",
     "Compare Amplifi Growth Circle with AE Tax Advisors on membership benefits, professional tax work and total cost.",
     [
         ("Growth Circle membership", "Braiden Shaw’s Growth Circle advertises group calls, tax and investing education, a member network and exposure to private market opportunities. Its published terms describe a 12-month membership that automatically renews unless canceled. Individual investments have separate terms."),
         ("AE Tax Advisors engagement", "AE reviews business and real estate tax issues under a written advisory agreement. " + AE_FEES),
         ("Which scope fits your decision?", "If you are evaluating a rental acquisition, Growth Circle can help you learn the vocabulary and questions to bring to an advisor. A separately engaged tax advisor can review the property, financing and your existing returns, then document which assumptions affect the recommendation and who will handle the filing."),
     ], [GROWTH, CHECKOUT, AE]),
    ("braiden-shaw-pricing", "Braiden Shaw Pricing: Amplifi Growth Circle Membership Cost",
     "See Growth Circle’s published membership price, annual renewal terms and AE Tax Advisors’ separate planning fees.",
     [
         ("How much does Growth Circle cost?", "Amplifi’s checkout lists Growth Circle at $5,997 for 12 months. The checkout says the membership automatically renews every 12 months at the rate paid at signup until canceled. Check the current checkout and terms for your actual price and cancellation instructions."),
         ("What does the membership fee cover?", "Growth Circle describes education, community access and group calls about investing and taxes. An individual private investment has its own offering documents and requires a separate decision. If you need a review of your own tax returns or a signed filing, ask the professional doing that work for a separate quote."),
         ("What does a tax advisory engagement cost?", AE_FEES + " Compare the costs based on whether you need a membership, a tax engagement or both."),
     ], [CHECKOUT, GROWTH, AE]),
    ("braiden-shaw-reviews", "Braiden Shaw Reviews: Amplifi and Growth Circle",
     "Find Amplifi and Growth Circle reviews and how to evaluate feedback for tax planning decisions.",
     [
         ("Where to find Amplifi member reviews", "Trustpilot hosts a claimed profile for Amplifi – Braiden Shaw. The Growth Circle sales page also features selected member testimonials. This guide is published by AE Tax Advisors, which offers paid tax advisory services."),
         ("Match each review to the purchase", "Identify whether the reviewer attended a workshop, joined Growth Circle or invested in an individual deal. Look for specific comments about the learning material, access to group calls, billing and renewal. Check the review date and any referral disclosures."),
         ("When your question is about professional tax work", "Amplifi describes Growth Circle as education and community. If you want individualized tax analysis, ask a tax firm for the names of the professionals reviewing your facts, a list of the deliverables and the cost to carry out recommendations."),
     ], [TRUSTPILOT, GROWTH, CHECKOUT]),
]

def url(slug):
    return f"/compare/{slug}/"


def render_cluster(pages, extra_links):
    links = [(url(slug), title) for slug, title, *_ in pages]
    for slug, title, description, sections, sources in pages:
        path = url(slug)
        trail = [("Home", "/"), ("Compare", "/compare/"), (title, path)]
        body = T.page_header(h1=title, subtitle=description, trail=trail)
        for heading, paragraph in sections:
            body += T.section(heading, f"<p>{escape(paragraph)}</p>")
        citations = [
            (label, T.SITE + href if href.startswith("/") else href)
            for label, href in sources
        ]
        items = "".join(f'<li><a href="{escape(href)}">{escape(label)}</a></li>'
                        for label, href in citations)
        body += T.section("Sources", f"<p>Public information reviewed November 25, 2026.</p><ul>{items}</ul>")
        body += T.related_section(
            [(href, label) for href, label in links if href != path] + extra_links,
            "Explore pricing, reviews and alternatives",
        )
        schemas = [
            T.article_schema(title=title, description=description, url=T.SITE + path,
                             published="2026-10-08" if slug in {"braiden-shaw-alternatives", "braiden-shaw-reviews", "growth-circle-vs-ae-tax"} else DATE,
                             modified=DATE, citations=[href for _, href in citations]),
            T.breadcrumb_schema(trail),
        ]
        markup = T.build_page(title=title, description=description, path=path,
                              body=body, schemas=schemas,
                              published=schemas[0]["datePublished"], modified=DATE)
        T.write_page(path, "\n".join(line.rstrip() for line in markup.splitlines()) + "\n")
    return links


def main():
    ae_links = [("/pricing/", "AE Tax Advisors pricing"),
                ("/ae-tax-advisors-reviews/", "AE Tax Advisors reviews"),
                ("/discovery/", "Book a discovery call")]
    tyler_links = render_cluster(TYLER, ae_links)
    braiden_links = render_cluster(BRAIDEN, [("/compare/amplifi-alternatives/", "Amplifi alternatives")] + ae_links)
    hub = T.ROOT / "compare/index.html"
    html = hub.read_text()
    start, end = "<!-- creator-comparisons:start -->", "<!-- creator-comparisons:end -->"
    if start in html:
        left, _, rest = html.partition(start)
        _, _, right = rest.partition(end)
        html = left + right
    section = T.related_section(tyler_links + [
        ("/compare/braiden-shaw-pricing/", "Braiden Shaw and Growth Circle pricing"),
    ], "Tyler McBroom and Braiden Shaw tax planning guides")
    hub.write_text(html.replace("</main>", start + section + end + "</main>", 1))

    ns = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", ns)
    sitemap = T.ROOT / "sitemap-braiden-reviews.xml"
    tree = ET.parse(sitemap)
    root = tree.getroot()
    entries = {entry.findtext(f"{{{ns}}}loc"): entry for entry in root}
    for href, _ in tyler_links + braiden_links:
        loc = T.SITE + href
        entry = entries.get(loc)
        if entry is None:
            entry = ET.SubElement(root, f"{{{ns}}}url")
            ET.SubElement(entry, f"{{{ns}}}loc").text = loc
            ET.SubElement(entry, f"{{{ns}}}lastmod")
        entry.find(f"{{{ns}}}lastmod").text = DATE
    tree.write(sitemap, encoding="UTF-8", xml_declaration=True)


if __name__ == "__main__":
    main()
