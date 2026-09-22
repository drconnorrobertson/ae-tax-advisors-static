#!/usr/bin/env python3
"""Remove the incorrect inference that the seven-day passive test sets building life."""
from pathlib import Path
import re
import json

ROOT = Path(__file__).resolve().parent
BLOG = ROOT / "blog"
EXCLUDE = {"str-39-year-recovery-period-nonresidential"}
SOURCE = "/blog/str-39-year-recovery-period-nonresidential/"
TODAY = "2026-09-22"

REPLACEMENT = (
    "<p>The seven-day average-customer-use rule is a passive-activity test, "
    "not the depreciation classification test. An STR building's 27.5- or "
    "39-year recovery period requires a separate analysis of gross rental "
    "income from dwelling units and the transient-establishment exclusion "
    "under Section 168. See <a href=\"" + SOURCE + "\">the STR building-life "
    "guide</a> and IRS <a href=\"https://www.irs.gov/publications/p946\">"
    "Publication 946</a> before assigning a building life.</p>"
)

PATTERN = re.compile(r"<p\b[^>]*>.*?</p>", re.S | re.I)
STAY = re.compile(r"(?:seven|7)[ -]?day", re.I)
LIFE = re.compile(r"39[ -]?year|nonresidential real property", re.I)
FALSE_INFERENCE = re.compile(
    r"(?:because|therefore|which means|so |automatically|classif|treated as|"
    r"applies to|longer recovery period|not residential|instead|generally|typically|usually)", re.I
)
SCHEMA_ANSWER = (
    "The seven-day average-customer-use rule affects passive-activity classification. "
    "The building's 27.5- or 39-year recovery period requires a separate analysis "
    "under Section 168, including the dwelling-unit income and transient-establishment rules."
)


def correct_paragraphs(source):
    # Only edit visible body, never JSON-LD or metadata.
    head, remainder = source.split("<main", 1)
    main, foot = remainder.split("</main>", 1)
    count = 0

    def fix(match):
        nonlocal count
        paragraph = match.group(0)
        if ("the STR building-life guide" not in paragraph
                and STAY.search(paragraph) and LIFE.search(paragraph)):
            count += 1
            return REPLACEMENT
        return paragraph

    main = PATTERN.sub(fix, main)
    return head + "<main" + main + "</main>" + foot, count


def correct_schema(source):
    def fix_script(match):
        try:
            data = json.loads(match.group(1))
        except json.JSONDecodeError:
            return match.group(0)
        changed = False

        def walk(obj):
            nonlocal changed
            if isinstance(obj, dict):
                for key, value in list(obj.items()):
                    if key == "text" and isinstance(value, str) and STAY.search(value) and LIFE.search(value):
                        obj[key] = SCHEMA_ANSWER
                        changed = True
                    else:
                        walk(value)
            elif isinstance(obj, list):
                for child in obj:
                    walk(child)

        walk(data)
        if not changed:
            return match.group(0)
        return '<script type="application/ld+json">\n' + json.dumps(data, indent=2) + '\n</script>'

    return re.sub(r'<script type="application/ld\+json">(.*?)</script>',
                  fix_script, source, flags=re.S)


def main():
    changed = {}
    for path in BLOG.glob("*/index.html"):
        if path.parent.name in EXCLUDE:
            continue
        old = path.read_text()
        if "<main" not in old:
            continue
        new, count = correct_paragraphs(old)
        new = correct_schema(new)
        if new == old:
            continue
        changed[path.parent.name] = count
        path.write_text(new)

    # These titles/headlines made the same blanket assertion.
    path = BLOG / "cost-segregation-study-airbnb-property-owners/index.html"
    text = path.read_text()
    text = text.replace("The 39-Year Trap Nobody Warns You About", "The Building-Life Question Owners Should Check")
    text = text.replace(
        "Airbnb properties with average stays of 7 days or less are 39-year nonresidential property, not 27.5-year.",
        "Airbnb building life requires a separate residential-versus-transient lodging analysis."
    )
    path.write_text(text)

    # The STR library pillar contained the same inference in its section,
    # comparison table, FAQ, metadata, and structured data.
    path = ROOT / "short-term-rentals/index.html"
    text = path.read_text()
    text = text.replace("cost segregation on a 39-year recovery period",
                        "cost segregation with a property-specific building recovery period")
    text = text.replace("cost segregation studies on a 39-year recovery period",
                        "cost segregation studies with a property-specific building recovery period")
    text = text.replace("Cost Segregation on a 39-Year Recovery Period",
                        "Cost Segregation and the Building Recovery Period")
    text = text.replace("Why short-term rentals are 39-year property",
                        "How to determine the building recovery period")
    text = text.replace(
        "Passing the two tests makes a loss deductible. Cost segregation is what makes the loss large. On short-term rentals it works differently than on long-term rentals, and the difference starts with the recovery period.",
        "The stay and participation tests can affect passive-loss treatment, while basis, at-risk, and other limits still apply. A cost segregation study may accelerate eligible components; the building's recovery period requires its own classification analysis."
    )
    text = text.replace(
        "The 27.5-year residential recovery period under IRC Sec. 168(e)(2)(A) applies to buildings composed of dwelling units. A unit used on a transient basis is expressly not a dwelling unit for that purpose. A property with an average stay of seven days or less is transient by any ordinary reading of the term, so it lands in nonresidential real property with a <strong>39-year recovery period</strong> and the mid-month convention under IRC Sec. 168(e)(2)(B).",
        "The passive-activity seven-day test does not itself set a building's depreciation life. Under IRC Sec. 168(e)(2) and <a href=\"https://www.irs.gov/publications/p946\">IRS Publication 946</a>, residential rental property generally uses 27.5 years when the dwelling-unit income test is met; a unit in a hotel, motel, or other establishment with predominantly transient use is excluded from the dwelling-unit definition. Nonresidential real property generally uses 39 years. Document the building's facts and use before selecting a schedule. <a href=\"/blog/str-39-year-recovery-period-nonresidential/\">Read the separate building-life analysis.</a>"
    )
    text = text.replace("Owners hear 39 years and assume they have lost something. Two reasons that is usually wrong.",
                        "Once the building is classified, evaluate separate short-life assets and any improvement rules on their own facts.")
    text = text.replace("<h3>Nonresidential unlocks QIP</h3>", "<h3>Check QIP separately</h3>")
    text = text.replace(
        "Qualified Improvement Property under IRC Sec. 168(e)(6) covers interior improvements to <strong>nonresidential</strong> buildings placed in service after the building was. QIP carries a 15-year life and full bonus eligibility. A 27.5-year residential rental cannot use it at all. Renovating an STR is materially better treated than renovating a long-term rental.",
        "Qualified Improvement Property can apply to qualifying interior improvements to <strong>nonresidential</strong> buildings after the building was first placed in service, subject to exclusions for enlargements, elevators, escalators, and internal structural framework. It is not automatic for an STR or for every renovation. First establish building classification, then classify each improvement."
    )
    text = text.replace("<td>39 years, nonresidential, mid-month convention.</td>",
                        "<td>27.5 or 39 years for the building, based on the separate residential-rental classification; mid-month convention.</td>")
    text = text.replace("<td>Available. 15-year life, bonus eligible.</td>",
                        "<td>Only for qualifying interior improvements if the building is nonresidential and the other QIP tests are met.</td>")
    text = text.replace("The 39-Year Recovery Period</a>", "The 27.5- or 39-Year Question</a>")
    text = text.replace("Why STRs are nonresidential property, what that costs, and the QIP advantage it buys you.",
                        "How the residential-rental and transient-lodging rules determine building life.")
    text = text.replace(
        "Generally 39 years. Residential rental property qualifies for the 27.5-year recovery period under IRC Sec. 168(e)(2)(A) only when the building consists of dwelling units, and a unit rented on a transient basis is not a dwelling unit for that purpose. A property with an average stay of seven days or less is transient by any reasonable reading, so it falls into nonresidential real property with a 39-year recovery period under IRC Sec. 168(e)(2)(B) and the mid-month convention. Owners often hear that as bad news. It usually is not. The structural component is the smallest part of a well-executed first-year strategy, and nonresidential classification unlocks Qualified Improvement Property treatment for interior improvements, which carries a 15-year life and full bonus depreciation eligibility that a 27.5-year residential property does not get.",
        "It depends on the building's separate classification under IRC Sec. 168(e)(2). The passive-activity seven-day average-stay rule does not automatically make an STR building 39-year property. Residential rental property generally uses 27.5 years when the dwelling-unit income test is met; qualifying transient lodging may be nonresidential real property with a 39-year period. QIP requires its own improvement analysis. See IRS Publication 946."
    )
    text = text.replace("The 39-year question in detail.", "The building-life question in detail.")
    text = text.replace("<span>39-year straight line, partial year</span>",
                        "<span>39-year straight line, partial year (assumed classification)</span>")
    text = text.replace(
        "A short-stay property is not a rental activity. It is a trade or business.",
        "An activity that meets this exception is not treated as a rental activity for Section 469; whether it is a trade or business for another tax rule requires its own facts."
    )
    text = text.replace(
        "Trade or business losses are non-passive when you materially participate. They offset W-2 wages, K-1 income, consulting income, and capital gains without a real estate professional election anywhere in sight.",
        "A qualifying nonrental activity can be nonpassive when the taxpayer materially participates. Whether a resulting loss can offset other income also depends on basis, at-risk, personal-use, and other applicable limitations."
    )
    text = text.replace(
        "Everything on this page reduces to a pair of questions the IRS will ask if the return is examined: <strong>was the average stay seven days or less</strong>, and <strong>did you materially participate</strong>. Pass both and the loss is deductible against ordinary income. Fail either and the loss suspends until you have passive income or sell the property. There is no partial credit, and neither test is satisfied by intent. Both are satisfied by records.",
        "Begin with two questions: <strong>does the activity meet a rental exception</strong>, such as the seven-day average-customer-use test, and <strong>did the taxpayer materially participate</strong>? Then apply basis, at-risk, vacation-home, and other loss limits. A failed test does not always lead to the same result; preserve separate records for each issue."
    )
    text = text.replace(
        "if you materially participate in that non-rental trade or business, the loss it generates is non-passive and can offset W-2 wages, business income, and other ordinary income.",
        "if you materially participate in a qualifying nonrental activity, its loss may be nonpassive; basis, at-risk, personal-use, and other limits must then be applied before it can offset other income."
    )
    text = text.replace(
        "Nothing about this is a loophole in the pejorative sense. It is the plain operation of the regulations, and it fails only when the seven-day test or the material participation test is not actually met.",
        "The actual result depends on the facts, the activity definition, and all applicable loss limits."
    )
    path.write_text(text)

    # Existing link labels should describe the corrected guide accurately.
    old_anchor = 'href="/blog/str-39-year-recovery-period-nonresidential/">Why Your Short-Term Rental Is 39-Year Property, Not 27.5'
    new_anchor = 'href="/blog/str-39-year-recovery-period-nonresidential/">Is a Short-Term Rental 27.5- or 39-Year Property?'
    for path in ROOT.rglob("index.html"):
        if ".git" in path.parts:
            continue
        text = path.read_text(errors="replace")
        if old_anchor in text:
            path.write_text(text.replace(old_anchor, new_anchor))

    # Preserve publication dates while marking substantive revisions as current.
    revised = [p for p in BLOG.glob("*/index.html")
               if "the STR building-life guide" in p.read_text(errors="replace")]
    revised += [BLOG / "str-39-year-recovery-period-nonresidential/index.html",
                ROOT / "short-term-rentals/index.html",
                ROOT / "short-term-rental-tax-strategy/index.html"]
    revised_urls = set()
    for page in revised:
        html = page.read_text()
        html = re.sub(r'("dateModified"\s*:\s*")[0-9]{4}-[0-9]{2}-[0-9]{2}("\s*)',
                      lambda m: m.group(1) + TODAY + m.group(2), html)
        page.write_text(html)
        rel = page.parent.relative_to(ROOT).as_posix()
        revised_urls.add(f"https://www.aetaxadvisors.com/{rel}/")
    for sitemap in (ROOT / "sitemap.xml", ROOT / "sitemap-blog.xml"):
        xml = sitemap.read_text()
        for url in revised_urls:
            xml = re.sub(r'(<loc>' + re.escape(url) + r'</loc>\s*<lastmod>)[^<]+',
                         lambda m: m.group(1) + TODAY, xml)
        sitemap.write_text(xml)

    path = BLOG / "cost-segregation-short-term-rental-airbnb-properties/index.html"
    text = path.read_text()
    text = text.replace("The 39-Year Trade and Why It Wins", "Building Life and Asset Classes")
    text = text.replace("Why short-term rentals depreciate over 39 years", "How to analyze the 27.5- or 39-year building life")
    path.write_text(text)

    # Update the prominent pillar anchor to match the revised page.
    path = ROOT / "short-term-rental-tax-strategy/index.html"
    text = path.read_text().replace(
        'href="/blog/str-39-year-recovery-period-nonresidential/">Why Your Short-Term Rental Is 39-Year Property, Not 27.5',
        'href="/blog/str-39-year-recovery-period-nonresidential/">Is a Short-Term Rental 27.5- or 39-Year Property?'
    )
    path.write_text(text)
    print("Corrected", sum(changed.values()), "claim paragraphs on", len(changed), "pages")
    for slug, count in sorted(changed.items()):
        print(slug, count)


if __name__ == "__main__":
    main()
