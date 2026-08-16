#!/usr/bin/env python3
"""Scenario builders for anonymized case studies.

Each builder returns a dict with a fully self-consistent set of figures: the
purchase price drives the land allocation, which drives depreciable basis,
which drives the reclassified amount, the deduction, and the tax result. No
number is invented independently of the others.

All studies are anonymized. No real client names, addresses, or identifying
details appear anywhere in this file or its output.
"""

from __future__ import annotations

import random

import case_data as D

# ---------------------------------------------------------------- helpers


def money(n: float) -> str:
    return f"${n:,.0f}"


def kmoney(n: float) -> str:
    """Round to the nearest thousand and render as $NNK / $N.NM."""
    if n >= 1_000_000:
        return f"${n / 1_000_000:.1f}M".replace(".0M", "M")
    return f"${round(n / 1000):,.0f}K"


def fed_rate(income: float) -> float:
    """Approximate top federal marginal rate for the scenario's income level."""
    if income >= 800_000:
        return 0.37
    if income >= 400_000:
        return 0.35
    if income >= 210_000:
        return 0.32
    if income >= 110_000:
        return 0.24
    return 0.22


def round_to(n: float, step: int) -> int:
    return int(round(n / step) * step)


def pick_state(rng: random.Random, want_tax: bool | None = None) -> tuple[str, float]:
    pool = D.STATES
    if want_tax is True:
        pool = [s for s in D.STATES if s[1] > 0.03]
    elif want_tax is False:
        pool = [s for s in D.STATES if s[1] == 0.0]
    return rng.choice(pool)


# ---------------------------------------------------------------- archetypes


def str_cost_seg(rng: random.Random, i: int) -> dict:
    prop, terrain, regions = rng.choice(D.STR_TYPES)
    region = rng.choice(regions)
    state, srate = pick_state(rng)

    price = round_to(rng.uniform(420_000, 2_400_000), 5_000)
    land_pct = rng.uniform(0.14, 0.26)
    land = round_to(price * land_pct, 1_000)
    basis = price - land
    reclass_pct = rng.uniform(0.26, 0.36)
    reclass = round_to(basis * reclass_pct, 1_000)

    # Remaining basis on 39-year nonresidential, mid-month, partial first year.
    months = rng.randint(2, 9)
    sl = round_to((basis - reclass) / 39 * ((months - 0.5) / 12), 100)
    yr1 = reclass + sl

    w2 = round_to(rng.uniform(240_000, 950_000), 5_000)
    gross = round_to(price * rng.uniform(0.06, 0.12), 500)
    opex = round_to(gross * rng.uniform(0.32, 0.48), 500)
    net_op = gross - opex
    loss = yr1 - net_op

    f = fed_rate(w2)
    combined = f + srate
    usable = min(loss, w2)
    savings = round_to(usable * combined, 500)

    hours = rng.randint(104, 218)
    avg_stay = round(rng.uniform(2.4, 6.2), 1)

    return {
        "cat": "Real Estate Investors",
        "kind": "str",
        "slug": f"str-{terrain}-{prop.split()[0].lower()}-cost-seg-{i}",
        "h1": f"{prop.title()} Owner Deducts {kmoney(yr1)} in Year One With Cost Segregation",
        "title": f"{prop.title()} STR: {kmoney(yr1)} Deduction",
        "desc": (f"How the owner of a {money(price)} {prop} in {region} used a cost segregation "
                 f"study and the short-term rental exception to deduct {money(yr1)} in the first "
                 f"year and reduce tax by approximately {money(savings)}."),
        "profile": [
            ("Asset", f"Short-term rental, {prop} in {region}"),
            ("Purchase price", money(price)),
            ("Owner's W-2 income", money(w2)),
            ("Entity", "Single-member LLC, Schedule E"),
            ("State", state),
            ("Key metric", f"{reclass_pct * 100:.0f}% of basis reclassified"),
            ("First-year tax reduction", money(savings)),
        ],
        "state": state,
        "savings": savings,
        "situation": (
            f"A married couple earning {money(w2)} in combined W-2 income purchased a {money(price)} "
            f"{prop} in {region} and began operating it as a short-term rental. The property "
            f"produced {money(gross)} of gross rental revenue in its first partial year against "
            f"{money(opex)} of operating expenses, leaving {money(net_op)} of net operating income "
            f"before depreciation."),
        "challenge": (
            f"Their prior preparer had set the property up on a straight 39-year schedule and "
            f"treated the resulting loss as passive. That produced almost no current-year benefit: "
            f"a passive loss on a rental cannot offset wages under IRC Section 469, so the deduction "
            f"was accumulating as a suspended carryforward while the couple continued paying tax at "
            f"a {f * 100:.0f}% federal marginal rate. Nobody had evaluated whether the property even "
            f"qualified as a rental activity in the first place."),
        "solution": [
            ("Established the short-term rental exception",
             f"The property's average period of customer use was {avg_stay} days, comfortably "
             f"under the seven-day threshold in Treasury Regulation 1.469-1T(e)(3)(ii)(A). That "
             f"removed the activity from the definition of a rental activity entirely, so the per se "
             f"passive rule of Section 469(c)(2) did not apply and only material participation was "
             f"required."),
            ("Documented material participation",
             f"We built a contemporaneous log covering guest communication, pricing and listing "
             f"management, supply runs, turnover coordination, and contractor supervision, totaling "
             f"{hours} hours. Because no other individual participated more, the owners satisfied "
             f"Test 3 under Treasury Regulation 1.469-5T(a)(3). Cleaning was engaged on a per-turn "
             f"basis rather than through a full-service manager specifically so that no third party "
             f"would out-participate the owners."),
            ("Completed an engineering-based cost segregation study",
             f"With {money(land)} allocated to land, the depreciable basis was {money(basis)}. The "
             f"study reclassified {money(reclass)}, or {reclass_pct * 100:.0f}% of basis, into "
             f"5-year, 7-year, and 15-year property: furnishings, appliances, flooring, cabinetry, "
             f"window treatments, decorative lighting, and site improvements including landscaping, "
             f"decking, and exterior lighting. All of it qualified for 100% bonus depreciation under "
             f"the OBBBA."),
            ("Applied the loss against wage income",
             f"First-year depreciation totaled {money(yr1)}, being {money(reclass)} of bonus "
             f"depreciation plus {money(sl)} of straight-line on the remaining basis. Netted against "
             f"{money(net_op)} of operating income, the activity produced a {money(loss)} loss. "
             f"Because the activity was non-rental and materially participated in, the loss offset "
             f"the couple's W-2 income directly."),
        ],
        "result": (
            f"The first-year deduction of {money(yr1)} produced approximately {money(savings)} of "
            f"combined federal and state tax reduction at a {combined * 100:.1f}% marginal rate. "
            f"We also modeled the exit: because the accelerated deductions will be recaptured on "
            f"sale, the plan assumes either a 1031 exchange into a replacement property or a hold "
            f"through the basis step-up at death, which converts the timing benefit into a permanent "
            f"one."),
        "takeaways": [
            f"An average stay of {avg_stay} days placed the property outside the rental category, which is what made the loss usable.",
            "Structuring cleaning per turnover rather than through a full-service manager preserved the 100-hour test.",
            f"Reclassifying {reclass_pct * 100:.0f}% of basis converted a 39-year deduction into a first-year one.",
            "Exit planning was set at the outset, because recapture determines whether this is a deferral or a permanent saving.",
        ],
        "faqs": [
            ("Why was this loss deductible against W-2 income?",
             f"<p>Because the average period of customer use was {avg_stay} days, the property was "
             f"not a rental activity under Treasury Regulation 1.469-1T(e)(3)(ii)(A). That removed "
             f"the automatic passive classification, leaving only the material participation "
             f"requirement, which the owners met under the 100-hour test.</p>"),
            ("Did the owners need real estate professional status?",
             "<p>No. Real estate professional status under Section 469(c)(7) applies to genuine "
             "rental activities and requires more than 750 hours plus more than half of all personal "
             "services in real property trades or businesses. The short-term rental exception is a "
             "separate and far more accessible path.</p>"),
            ("How much of the purchase price was reclassified?",
             f"<p>{money(reclass)}, or {reclass_pct * 100:.0f}% of the {money(basis)} depreciable "
             f"basis after the {money(land)} land allocation. That is a typical range for a "
             f"furnished short-term rental, where furnishings and site improvements make up a large "
             f"share of the investment.</p>"),
            ("What happens when the property is sold?",
             "<p>Accelerated depreciation on personal property is recaptured as ordinary income "
             "under Section 1245, and building depreciation is subject to unrecaptured Section 1250 "
             "gain at up to 25%. A 1031 exchange defers it and a step-up at death eliminates it, "
             "which is why the exit is planned before the study is ordered.</p>"),
        ],
        "related_pages": [
            ("/short-term-rental-tax-loophole-2026/", "The Short-Term Rental Tax Loophole in 2026"),
            ("/material-participation-short-term-rental-7-day-rule/", "Material Participation and the STR 7-Day Rule"),
            ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
            ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026 Under the OBBBA"),
        ],
    }


def ltr_lookback(rng: random.Random, i: int) -> dict:
    label, descriptor = rng.choice(D.LTR_TYPES)
    state, srate = pick_state(rng)

    price = round_to(rng.uniform(600_000, 6_500_000), 10_000)
    land_pct = rng.uniform(0.15, 0.25)
    land = round_to(price * land_pct, 1_000)
    basis = price - land
    years = rng.randint(4, 12)
    claimed = round_to(basis / 27.5 * years, 500)

    reclass_pct = rng.uniform(0.21, 0.32)
    reclass = round_to(basis * reclass_pct, 1_000)
    # Recomputed cumulative: bonus on reclassified in year one plus SL since.
    sl_since = round_to((basis - reclass) / 27.5 * years, 500)
    should_have = reclass + sl_since
    adj = should_have - claimed

    income = round_to(rng.uniform(280_000, 1_400_000), 5_000)
    f = fed_rate(income)
    combined = f + srate
    savings = round_to(min(adj, income) * combined, 500)

    return {
        "cat": "Real Estate Investors",
        "kind": "ltr",
        "slug": f"ltr-{label.split()[0].lower()}-form-3115-lookback-{i}",
        "h1": f"{label.title()} Owner Recovers {kmoney(adj)} of Missed Depreciation With Form 3115",
        "title": f"{label.title()} Lookback: {kmoney(adj)}",
        "desc": (f"How the owner of {descriptor} held for {years} years used a Form 3115 change in "
                 f"accounting method to claim {money(adj)} of previously missed depreciation in a "
                 f"single year, reducing tax by approximately {money(savings)}."),
        "profile": [
            ("Asset", f"Long-term rental, {descriptor}"),
            ("Purchase price", money(price)),
            ("Years held before study", f"{years} years"),
            ("Owner's other income", money(income)),
            ("State", state),
            ("Section 481(a) adjustment", money(adj)),
            ("Tax reduction", money(savings)),
        ],
        "state": state,
        "savings": savings,
        "situation": (
            f"The client had owned {descriptor} for {years} years, purchased for {money(price)}. "
            f"From the beginning it had been depreciated on a single 27.5-year straight-line "
            f"schedule with no component analysis, producing roughly {money(claimed)} of cumulative "
            f"depreciation over the holding period."),
        "challenge": (
            f"The client assumed that fixing {years} years of understated depreciation would require "
            f"amended returns, and that the three-year statute of limitations capped any recovery. "
            f"That belief had kept them from acting for several years. Meanwhile the property was "
            f"generating taxable income each year that could have been sheltered."),
        "solution": [
            ("Reframed the correction as a method change, not an amendment",
             f"Depreciation is a method of accounting. Because the original method had been used for "
             f"more than two consecutive years, correcting it is a change in method of accounting "
             f"rather than an error correction. That is made on Form 3115 with a Section 481(a) "
             f"adjustment capturing the entire cumulative difference back to the placed-in-service "
             f"year, with no statute of limitations cap and no amended returns."),
            ("Performed an engineering-based cost segregation study",
             f"With {money(land)} allocated to land, the depreciable basis was {money(basis)}. The "
             f"study reclassified {money(reclass)}, or {reclass_pct * 100:.0f}%, into 5-, 7-, and "
             f"15-year categories covering appliances, flooring, cabinetry, fixtures, and site "
             f"improvements including paving, landscaping, fencing, and exterior lighting."),
            ("Computed the Section 481(a) adjustment",
             f"Recomputed under the correct classifications, cumulative allowable depreciation "
             f"through the beginning of the year of change would have been {money(should_have)} "
             f"against {money(claimed)} actually claimed. The favorable adjustment of {money(adj)} "
             f"was deducted in full in the year of change, since negative adjustments are not spread."),
            ("Filed under automatic consent with the required duplicate copy",
             "The change was filed under the automatic consent procedures with no user fee, using "
             "the designated change number for depreciation method and recovery period changes. The "
             "original accompanied the timely filed return and a duplicate was filed separately with "
             "the IRS in Ogden. We also evaluated late partial disposition elections for components "
             "replaced during the holding period."),
        ],
        "result": (
            f"The {money(adj)} catch-up deduction reduced tax by approximately {money(savings)} at a "
            f"{combined * 100:.1f}% combined marginal rate, all in a single filing year, without "
            f"amending a single prior return. Going forward the property depreciates on the corrected "
            f"component schedule."),
        "takeaways": [
            f"A Form 3115 reached back all {years} years, well beyond the three-year amendment window.",
            "The catch-up was a negative Section 481(a) adjustment, deducted entirely in the year of change.",
            "Automatic consent meant no user fee and no advance IRS approval.",
            "The duplicate Ogden filing is mandatory and is the most commonly missed step.",
        ],
        "faqs": [
            ("Why not just amend the prior returns?",
             f"<p>Depreciation used for two or more consecutive years is an established method of "
             f"accounting, so correcting it is a method change rather than an error correction. The "
             f"method change is also better: it reached all {years} years at once, while amendments "
             f"would have been limited to the open statute period.</p>"),
            ("Is the catch-up deduction spread over several years?",
             "<p>No. A negative Section 481(a) adjustment, which is what a cost segregation lookback "
             "produces, is deducted in full in the year of change. Only positive adjustments that "
             "increase income are spread, generally over four years.</p>"),
            ("Does this trigger an audit?",
             "<p>Form 3115 is a routine filing made under automatic consent. What draws scrutiny is a "
             "large adjustment with no engineering study behind it. This filing included a full "
             "cost segregation report meeting the standards in the IRS Cost Segregation Audit "
             "Techniques Guide.</p>"),
            ("Could this be done in the year of sale?",
             "<p>Generally no. A change in accounting method is not available in the year the "
             "property is disposed of, which is why waiting until you are selling forfeits the "
             "opportunity entirely.</p>"),
        ],
        "related_pages": [
            ("/form-3115-cost-segregation-lookback/", "Form 3115 Cost Segregation Lookback"),
            ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
            ("/macrs-depreciation-schedule-2026/", "MACRS Depreciation Schedule 2026"),
            ("/rental-property-tax-planning/", "Rental Property Tax Planning"),
        ],
    }


# Compact display names for asset classes whose full label makes a title too long.
SHORT_LABEL = {
    "warehouse and distribution facility": "Warehouse",
    "retail strip center": "Retail Center",
    "multifamily property": "Multifamily",
    "flex industrial building": "Flex Industrial",
    "assisted living facility": "Assisted Living",
    "quick-service restaurant": "QSR",
    "limited-service motel": "Motel",
    "medical office building": "Medical Office",
    "dental practice building": "Dental Office",
    "brewery and taproom": "Brewery",
    "manufactured housing community": "MH Community",
}


def commercial_cost_seg(rng: random.Random, i: int) -> dict:
    label, lo, hi, descriptor = rng.choice(D.COMMERCIAL_TYPES)
    short = SHORT_LABEL.get(label, label.title())
    state, srate = pick_state(rng)

    price = round_to(rng.uniform(900_000, 18_000_000), 10_000)
    land_pct = rng.uniform(0.15, 0.28)
    land = round_to(price * land_pct, 1_000)
    basis = price - land
    reclass_pct = rng.uniform(lo, hi)
    reclass = round_to(basis * reclass_pct, 1_000)
    months = rng.randint(3, 10)
    sl = round_to((basis - reclass) / 39 * ((months - 0.5) / 12), 100)
    yr1 = reclass + sl

    income = round_to(rng.uniform(350_000, 3_200_000), 5_000)
    f = fed_rate(income)
    combined = f + srate
    savings = round_to(min(yr1, income) * combined, 500)

    return {
        "cat": "Commercial Real Estate",
        "kind": "commercial",
        "slug": f"commercial-{label.replace(' ', '-').lower()}-cost-seg-{i}",
        "h1": f"{label.title()} Owner Deducts {kmoney(yr1)} in Year One via Cost Segregation",
        "title": f"{short} Cost Seg: {kmoney(yr1)} Year One",
        "desc": (f"How the owner of {descriptor} purchased for {money(price)} reclassified "
                 f"{reclass_pct * 100:.0f}% of depreciable basis and deducted {money(yr1)} in the "
                 f"first year, reducing tax by approximately {money(savings)}."),
        "profile": [
            ("Asset", descriptor.capitalize()),
            ("Purchase price", money(price)),
            ("Depreciable basis", money(basis)),
            ("Owner's taxable income", money(income)),
            ("State", state),
            ("Reclassified", f"{money(reclass)} ({reclass_pct * 100:.0f}%)"),
            ("First-year tax reduction", money(savings)),
        ],
        "state": state,
        "savings": savings,
        "situation": (
            f"The client acquired {descriptor} for {money(price)} and placed it in service during "
            f"the year. The operating business generated {money(income)} of taxable income, taxed at "
            f"a {f * 100:.0f}% federal marginal rate before planning."),
        "challenge": (
            f"The closing statement allocated the purchase price between land and building and "
            f"nothing further. The entire {money(basis)} building allocation was headed for a "
            f"39-year straight-line schedule producing roughly {money(round_to(basis / 39, 100))} per year. For an "
            f"asset class where a large share of the investment sits in equipment, specialty "
            f"systems, and site improvements rather than structure, that treatment understated the "
            f"available deduction substantially."),
        "solution": [
            ("Engineering-based component analysis",
             f"We engaged an engineering firm to perform a detailed study using construction "
             f"documents, a site visit, and cost estimating. The study reclassified {money(reclass)}, "
             f"or {reclass_pct * 100:.0f}% of the {money(basis)} depreciable basis, into 5-year, "
             f"7-year, and 15-year MACRS classes."),
            ("Separated specialty systems from base building",
             "The largest single source of value was the mechanical, electrical, and plumbing "
             "installed to serve specific equipment rather than the building generally. Dedicated "
             "circuits, specialty piping, and exhaust and make-up air serving equipment were "
             "allocated to the equipment they serve rather than to 39-year building systems. This is "
             "the allocation a desktop study cannot support and an engineering study can."),
            ("Captured site improvements",
             "Paving, curbing, sidewalks, site lighting, drainage, landscaping and irrigation, "
             "fencing, and exterior signage were identified as 15-year land improvements, all "
             "eligible for bonus depreciation."),
            ("Applied 100% bonus depreciation",
             f"Because every reclassified category carries a recovery period of 20 years or less, "
             f"the full {money(reclass)} was deductible in year one under Section 168(k) as restored "
             f"by the OBBBA. Adding {money(sl)} of straight-line on the remaining structure brought "
             f"first-year depreciation to {money(yr1)}."),
        ],
        "result": (
            f"First-year depreciation of {money(yr1)} against {money(round_to(basis / 39, 100))} under the original "
            f"treatment reduced tax by approximately {money(savings)} at a {combined * 100:.1f}% "
            f"combined marginal rate. We also identified Section 179 as the correct vehicle for "
            f"future roof and HVAC replacements, which are 39-year property that bonus depreciation "
            f"cannot reach."),
        "takeaways": [
            f"Reclassifying {reclass_pct * 100:.0f}% of basis moved {money(reclass)} from a 39-year schedule into year one.",
            "Specialty MEP serving equipment, not the building, was the largest single value driver.",
            "Site improvements are 15-year property and fully bonus-eligible.",
            "Section 179, not bonus depreciation, is the tool for future roof and HVAC work.",
        ],
        "faqs": [
            (f"How much does a {label} typically reclassify?",
             f"<p>In this study, {reclass_pct * 100:.0f}% of depreciable basis. That is within the "
             f"normal range for this asset class, where equipment, specialty systems, and site work "
             f"make up a substantial share of the total investment relative to the building shell.</p>"),
            ("Is the deduction limited by passive activity rules?",
             "<p>Not here. The owner materially participates in the operating business, so the "
             "deduction is non-passive. Where real estate is held in a separate entity leasing to an "
             "operating company, the self-rental rules apply and a grouping election under "
             "Reg. 1.469-4 is often needed.</p>"),
            ("What happens on sale?",
             "<p>5- and 7-year property is recaptured as ordinary income under Section 1245, while "
             "land improvements and the building produce unrecaptured Section 1250 gain at up to "
             "25%. A 1031 exchange defers the entire amount.</p>"),
            ("Why not use a lower-cost desktop study?",
             "<p>The allocations that drive most of the value here, specialty MEP and site "
             "improvements, require engineering support. The IRS Cost Segregation Audit Techniques "
             "Guide identifies the detailed engineering approach as the most reliable method, and a "
             "study without it is the first thing challenged.</p>"),
        ],
        "related_pages": [
            ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
            ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026 Under the OBBBA"),
            ("/section-179-vs-bonus-depreciation-2026/", "Section 179 vs Bonus Depreciation in 2026"),
            ("/form-3115-cost-segregation-lookback/", "Form 3115 Cost Segregation Lookback"),
        ],
    }


def scorp_optimization(rng: random.Random, i: int) -> dict:
    biz = rng.choice(D.BUSINESS_TYPES)
    state, srate = pick_state(rng)

    revenue = round_to(rng.uniform(600_000, 6_000_000), 10_000)
    profit = round_to(revenue * rng.uniform(0.14, 0.34), 5_000)
    wage = round_to(profit * rng.uniform(0.35, 0.55), 5_000)
    distribution = profit - wage

    wage_base = 184_500
    se_ss = min(profit * 0.9235, wage_base) * 0.124
    se_med = profit * 0.9235 * 0.029
    se_total = se_ss + se_med

    pr_ss = min(wage, wage_base) * 0.124
    pr_med = wage * 0.029
    pr_total = pr_ss + pr_med

    gross_saving = round_to(se_total - pr_total, 100)
    costs = rng.randint(2400, 4200)
    net_saving = gross_saving - costs

    retirement = round_to(min(wage * 0.25, 46_000), 500)
    f = fed_rate(profit)
    retirement_value = round_to(retirement * (f + srate), 100)
    total = net_saving + retirement_value

    return {
        "cat": "Business Owners",
        "kind": "scorp",
        "slug": f"s-corp-election-reasonable-comp-{i}",
        "h1": f"{biz.title()} Saves {kmoney(total)} a Year With an S Election and Documented Reasonable Compensation",
        "title": f"S-Corp Election Saves {kmoney(total)} a Year",
        "desc": (f"How {biz} generating {money(revenue)} in revenue elected S-Corp treatment, set "
                 f"defensible reasonable compensation of {money(wage)}, and reduced tax by "
                 f"approximately {money(total)} per year."),
        "profile": [
            ("Business", biz.capitalize()),
            ("Annual revenue", money(revenue)),
            ("Net profit", money(profit)),
            ("Prior entity", "Single-member LLC, Schedule C"),
            ("State", state),
            ("Reasonable compensation set", money(wage)),
            ("Annual tax savings", money(total)),
        ],
        "state": state,
        "savings": total,
        "situation": (
            f"The client operated {biz} through a single-member LLC reporting on Schedule C, with "
            f"{money(revenue)} of revenue and {money(profit)} of net profit. All of that profit was "
            f"subject to self-employment tax, costing approximately {money(se_total)} per year before "
            f"income tax."),
        "challenge": (
            f"The owner had been told an S election would save money but had also been warned about "
            f"reasonable compensation exposure, and had done nothing for three years as a result. "
            f"The concern was legitimate: officer compensation is one of the most reliably adjusted "
            f"items in a small business examination, and an unsupported salary invites back payroll "
            f"tax, penalties, and interest across every open year."),
        "solution": [
            ("Elected S-Corp taxation for the existing LLC",
             "The LLC did not need to be converted to a corporation. Filing Form 2553 gave the "
             "entity S-Corp tax treatment while leaving the operating agreement, liability "
             "protection, and state law status untouched."),
            ("Built a defensible reasonable compensation analysis",
             f"Rather than applying a percentage rule, which has no authority behind it, we priced "
             f"the roles the owner actually performs against Bureau of Labor Statistics wage data and "
             f"industry compensation surveys, adjusted for hours worked, business size, and "
             f"geography. The blended figure supported {money(wage)} in annual W-2 compensation, "
             f"documented in a written compensation memorandum and an employment agreement adopted "
             f"before the year began."),
            ("Ran genuine payroll",
             f"Compensation was paid ratably through the year with quarterly Forms 941 and proper "
             f"deposits, not as a single December true-up. The remaining {money(distribution)} of "
             f"profit was distributed free of self-employment tax."),
            ("Layered a retirement plan on the new wage base",
             f"The W-2 wage created capacity for employer retirement contributions that did not "
             f"exist under Schedule C in the same form. A profit sharing contribution of "
             f"{money(retirement)} was added, worth approximately {money(retirement_value)} at the "
             f"owner's combined marginal rate."),
        ],
        "result": (
            f"Payroll tax fell from approximately {money(se_total)} to {money(pr_total)}, a gross "
            f"saving of {money(gross_saving)}. Net of roughly {money(costs)} in additional return "
            f"preparation and payroll processing costs, the entity change was worth {money(net_saving)} "
            f"per year, and the retirement contribution added approximately {money(retirement_value)} "
            f"more, for a combined annual benefit of about {money(total)}."),
        "takeaways": [
            "An existing LLC can elect S-Corp treatment without converting to a corporation.",
            "Reasonable compensation was priced from market wage data, not from a percentage rule.",
            "Payroll was run ratably through the year, since a single December true-up is a recognizable pattern.",
            "The S election reduces employment tax only; it never reduces income tax.",
        ],
        "faqs": [
            ("How was the reasonable compensation figure determined?",
             f"<p>By pricing each role the owner performs against Bureau of Labor Statistics "
             f"Occupational Employment and Wage Statistics and industry salary surveys, blending "
             f"them by time allocation, and adjusting for hours, business size, and geography. The "
             f"analysis supported {money(wage)} and was documented contemporaneously.</p>"),
            ("Is there a 60/40 rule for S-Corp salary?",
             "<p>No. There is no safe harbor percentage in the Code, regulations, or IRS guidance. "
             "The standard is a facts-and-circumstances analysis against what comparable businesses "
             "pay for comparable services, using the nine factors summarized in IRS Fact Sheet "
             "FS-2008-25.</p>"),
            ("Does the S election reduce income tax?",
             "<p>No. The profit is taxed at the same ordinary rates either way. The election reduces "
             "self-employment and payroll tax only, which is the entire source of the saving here.</p>"),
            ("Could a lower salary have saved more?",
             "<p>In the short term, yes, but it would have created examination exposure and, above "
             "the Section 199A taxable income thresholds, could have reduced the qualified business "
             "income deduction by more than the payroll tax it saved. We modeled both effects before "
             "setting the number.</p>"),
        ],
        "related_pages": [
            ("/reasonable-compensation-s-corp-irs/", "Reasonable Compensation for S-Corp Owners"),
            ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
            ("/business-owner-small-business-tax/", "Business Owner and Small Business Tax"),
            ("/cash-balance-plan-tax-deduction/", "Cash Balance Plan Tax Deduction"),
        ],
    }


def ccorp_shift(rng: random.Random, i: int) -> dict:
    biz = rng.choice(D.BUSINESS_TYPES)
    state, srate = pick_state(rng)

    profit = round_to(rng.uniform(700_000, 5_500_000), 10_000)
    shifted = round_to(profit * rng.uniform(0.22, 0.45), 5_000)
    saving = round_to(shifted * (0.37 - 0.21), 500)

    return {
        "cat": "Business Owners",
        "kind": "ccorp",
        "slug": f"c-corp-income-shift-{i}",
        "h1": f"{biz.title()} Shifts {kmoney(shifted)} of Income From 37% to 21%",
        "title": f"C-Corp Shift: {kmoney(shifted)} From 37% to 21%",
        "desc": (f"How {biz} with {money(profit)} of annual profit moved {money(shifted)} into a "
                 f"C corporation taxed at 21%, saving approximately {money(saving)} per year while "
                 f"funding growth."),
        "profile": [
            ("Business", biz.capitalize()),
            ("Annual profit", money(profit)),
            ("Structure", "S-Corp operating entity plus C-Corp management company"),
            ("State", state),
            ("Income shifted annually", money(shifted)),
            ("Rate arbitrage", "37% to 21%"),
            ("Annual tax savings", money(saving)),
        ],
        "state": state,
        "savings": saving,
        "situation": (
            f"The client owned {biz} generating {money(profit)} of annual profit, all flowing "
            f"through to a personal return taxed at the top 37% federal rate. The business was "
            f"reinvesting heavily and the owner did not need most of the cash personally."),
        "challenge": (
            f"Every dollar of retained earnings was being taxed at 37% before it could be "
            f"reinvested, even though it never reached the owner's bank account. At the same time, "
            f"the owner had been warned that C corporations create double taxation, which had ruled "
            f"the structure out in earlier conversations without any modeling."),
        "solution": [
            ("Established a C corporation to provide genuine services",
             "We formed a C corporation to provide management, administrative, marketing, and "
             "technology services to the operating entity under a written services agreement. The "
             "corporation employs staff, holds assets, and performs real functions. Without genuine "
             "substance, Section 482 permits the IRS to reallocate income between commonly "
             "controlled entities, so the arrangement was built to be defended on substance."),
            ("Priced the service fee at arm's length",
             f"The annual fee of {money(shifted)} was supported by a functional analysis comparing "
             f"the services provided to third-party market rates for equivalent outsourced "
             f"management, administrative, and marketing functions. The fee is deductible to the "
             f"operating entity and taxed to the corporation at the flat 21% rate under Section 11."),
            ("Documented the business purpose for accumulating earnings",
             "Because the strategy depends on retaining earnings, we addressed the accumulated "
             "earnings tax of Section 531 directly. The corporation maintains a written plan "
             "documenting expansion commitments, working capital requirements, and equipment "
             "acquisition schedules, which is the defense against a 20% penalty on earnings "
             "accumulated beyond the reasonable needs of the business."),
            ("Planned the extraction routes in advance",
             "The strategy only works if the second layer of tax is avoided or deferred. We mapped "
             "extraction through reasonable salary to owner-employees, arm's length rent on property "
             "the owner holds personally, deductible interest on documented shareholder loans, "
             "retirement plan contributions, and ultimately a stock sale positioned for Section 1202 "
             "qualified small business stock treatment."),
        ],
        "result": (
            f"Shifting {money(shifted)} annually from a 37% rate to a 21% rate produces roughly "
            f"{money(saving)} of federal tax savings each year, retained inside the business and "
            f"available for reinvestment. We modeled the position over a ten-year horizon rather "
            f"than a single year, because a one-year comparison ignores the second layer entirely "
            f"and makes the structure look better than it is."),
        "takeaways": [
            "The 21% rate only helps on earnings that stay in the corporation.",
            "The management fee must be arm's length and supported by real services, or Section 482 reallocates it.",
            "The accumulated earnings tax is the principal risk and is defended with contemporaneous documentation.",
            "Section 1202 qualified small business stock is what converts the deferral into a permanent benefit.",
        ],
        "faqs": [
            ("Does this create double taxation?",
             "<p>Only if earnings are distributed as dividends. The strategy is built around "
             "extraction routes that are taxed once: reasonable salary, arm's length rent, "
             "documented loan interest, retirement contributions, and ultimately a stock sale. A "
             "business that must distribute most of its earnings annually is not a good candidate.</p>"),
            ("What is the accumulated earnings tax risk?",
             "<p>Section 531 imposes a 20% penalty on earnings accumulated beyond the reasonable "
             "needs of the business, with a credit of $250,000, or $150,000 for personal service "
             "corporations. The defense is contemporaneous documentation of expansion plans, working "
             "capital needs, and specific commitments, which this corporation maintains.</p>"),
            ("Could the IRS challenge the management fee?",
             "<p>Yes, if it is not arm's length or the services are not real. Section 482 allows "
             "reallocation of income between commonly controlled entities. The fee here is supported "
             "by a functional analysis against third-party market rates, a written services "
             "agreement, and records of the services actually performed.</p>"),
            ("Should real estate go into the C corporation?",
             "<p>No. Appreciated property distributed out of a C corporation triggers gain at both "
             "the corporate and shareholder level, with no equivalent of the partnership rules "
             "permitting tax-free property distributions. Real estate stays in a separate "
             "pass-through entity.</p>"),
        ],
        "related_pages": [
            ("/c-corp-income-shifting-strategy/", "C-Corp Income Shifting Strategy"),
            ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
            ("/reasonable-compensation-s-corp-irs/", "Reasonable Compensation for S-Corp Owners"),
            ("/retirement-exit-ma-tax-strategy/", "Retirement, Exit and M&A Tax Strategy"),
        ],
    }


def retirement_stack(rng: random.Random, i: int) -> dict:
    practice = rng.choice(D.PRACTICE_TYPES + D.BUSINESS_TYPES)
    state, srate = pick_state(rng)
    age = rng.randint(44, 63)

    profit = round_to(rng.uniform(500_000, 3_000_000), 10_000)
    wage = round_to(min(profit * 0.4, 345_000), 5_000)

    deferral = 24_500
    catchup = 8_000 if age >= 50 else 0
    profit_sharing = round_to(wage * 0.06, 500)
    # Cash balance contribution scales sharply with age.
    cb_base = 70_000 + (age - 40) * 11_500
    cash_balance = round_to(min(cb_base * rng.uniform(0.85, 1.15), profit * 0.45), 5_000)

    total_contrib = deferral + catchup + profit_sharing + cash_balance
    f = fed_rate(profit)
    combined = f + srate
    savings = round_to(total_contrib * combined, 500)
    staff_cost = round_to(cash_balance * rng.uniform(0.06, 0.16), 500)

    return {
        "cat": "Business Owners",
        "kind": "retirement",
        "slug": f"cash-balance-401k-stack-{i}",
        "h1": f"{practice.title()} Owner Deducts {kmoney(total_contrib)} With a Cash Balance and 401(k) Stack",
        "title": f"Cash Balance Stack: {kmoney(total_contrib)} Deducted",
        "desc": (f"How the owner of {practice}, age {age}, combined a cash balance plan with a "
                 f"401(k) profit sharing plan to deduct {money(total_contrib)} in a single year and "
                 f"reduce tax by approximately {money(savings)}."),
        "profile": [
            ("Business", practice.capitalize()),
            ("Owner age", str(age)),
            ("Net profit", money(profit)),
            ("Owner W-2 compensation", money(wage)),
            ("State", state),
            ("Total deductible contribution", money(total_contrib)),
            ("Tax reduction", money(savings)),
        ],
        "state": state,
        "savings": savings,
        "situation": (
            f"The owner of {practice}, age {age}, was generating {money(profit)} of net profit and "
            f"contributing only to a 401(k), leaving the large majority of profit exposed at a "
            f"{f * 100:.0f}% federal marginal rate. With retirement roughly {65 - age} years away, "
            f"the accumulation timeline was short and the tax cost was high."),
        "challenge": (
            f"A defined contribution plan caps what goes in. Even at the maximum, annual additions "
            f"were limited to roughly $72,000 plus catch-up, which barely moved a {money(profit)} "
            f"profit figure. The owner needed a materially larger deduction without changing the "
            f"underlying business."),
        "solution": [
            ("Added a cash balance defined benefit plan",
             f"A defined benefit plan caps the benefit payable at retirement rather than the "
             f"contribution, and the required contribution is derived actuarially from the years "
             f"remaining to fund that benefit. At age {age}, the actuary supported an annual "
             f"contribution of approximately {money(cash_balance)}, an amount no defined "
             f"contribution plan could approach."),
            ("Coordinated with the existing 401(k) profit sharing plan",
             f"Employee deferrals of {money(deferral)}" +
             (f" plus {money(catchup)} in catch-up contributions" if catchup else "") +
             f" continued unaffected. Employer profit sharing was limited to 6% of covered "
             f"compensation, {money(profit_sharing)}, under the combined plan deduction limit of "
             f"Section 404(a)(7)."),
            ("Cross-tested to control staff cost",
             f"The plans were cross-tested on a benefits basis, which allows the owner a much larger "
             f"pay credit than staff while still satisfying the coverage and nondiscrimination "
             f"requirements of Sections 410(b) and 401(a)(4). Annual staff cost came to approximately "
             f"{money(staff_cost)}, a fraction of the owner's benefit."),
            ("Designed for funding flexibility",
             "The plan uses an actual rate of return interest crediting design, which passes "
             "investment risk to participants and largely eliminates funding volatility. The actuary "
             "computes a minimum and a maximum deductible contribution each year, and the range "
             "between them gives the owner room to contribute more in strong years and less in "
             "weak ones."),
        ],
        "result": (
            f"Total deductible retirement contributions reached {money(total_contrib)}, reducing tax "
            f"by approximately {money(savings)} at a {combined * 100:.1f}% combined marginal rate. "
            f"Net of roughly {money(staff_cost)} in staff contributions and administrative costs, "
            f"the structure remains strongly positive and is designed to run for at least five years."),
        "takeaways": [
            "Defined benefit plans cap the benefit, not the contribution, which is why the deduction scales with age.",
            f"At age {age}, the actuarial contribution reached {money(cash_balance)} on its own.",
            "Cross-testing on a benefits basis kept staff cost proportionate.",
            "Contributions are a funding obligation, so multi-year cash flow stability was a prerequisite.",
        ],
        "faqs": [
            ("Why is the contribution so much larger than a 401(k)?",
             f"<p>Because a defined benefit plan limits the benefit payable at retirement rather "
             f"than the annual contribution. The required contribution is computed actuarially from "
             f"the years remaining to fund that benefit, so at age {age} the figure is several times "
             f"what any defined contribution plan permits.</p>"),
            ("Did employees have to be covered?",
             f"<p>Yes. Coverage and nondiscrimination rules apply, so the plan cannot cover only the "
             f"owner. Cross-testing on a benefits basis allowed the owner a much larger credit while "
             f"staff cost stayed at approximately {money(staff_cost)} per year.</p>"),
            ("What if profit drops in a future year?",
             "<p>The actuary sets a minimum and a maximum deductible contribution, and the range "
             "between them provides real flexibility. In a sustained downturn the plan can be frozen "
             "to stop future accruals or terminated with assets rolled to IRAs.</p>"),
            ("Is this a permanent tax saving?",
             "<p>It is a deferral. Distributions are taxed as ordinary income in retirement. The "
             "strategy works because the deduction is taken at a high marginal rate now and "
             "distributions are expected at a lower rate later, which we modeled before "
             "recommending it.</p>"),
        ],
        "related_pages": [
            ("/cash-balance-plan-tax-deduction/", "Cash Balance Plan Tax Deduction"),
            ("/best-retirement-plan-business-owner-over-500k/", "Best Retirement Plan for Owners Over $500K"),
            ("/reasonable-compensation-s-corp-irs/", "Reasonable Compensation for S-Corp Owners"),
            ("/retirement-exit-ma-tax-strategy/", "Retirement, Exit and M&A Tax Strategy"),
        ],
    }


def entity_ptet(rng: random.Random, i: int) -> dict:
    biz = rng.choice(D.BUSINESS_TYPES)
    state = rng.choice(D.PTET_STATES)
    srate = dict(D.STATES).get(state, 0.05)

    profit = round_to(rng.uniform(600_000, 4_500_000), 10_000)
    entities = rng.randint(2, 5)
    state_tax = round_to(profit * srate, 500)
    f = fed_rate(profit)
    ptet_benefit = round_to(state_tax * f, 500)
    restructure_benefit = round_to(profit * rng.uniform(0.012, 0.028), 500)
    total = ptet_benefit + restructure_benefit

    return {
        "cat": "Business Owners",
        "kind": "entity",
        "slug": f"entity-restructure-ptet-{state.lower().replace(' ', '-')}-{i}",
        "h1": f"{biz.title()} Recovers {kmoney(total)} With Entity Restructuring and a PTET Election",
        "title": f"PTET and Restructuring: {kmoney(total)} Saved",
        "desc": (f"How {biz} operating across {entities} entities in {state} consolidated its "
                 f"structure and elected pass-through entity tax treatment, recovering "
                 f"approximately {money(total)} per year."),
        "profile": [
            ("Business", biz.capitalize()),
            ("Annual profit", money(profit)),
            ("Entities before", f"{entities} separate entities"),
            ("State", state),
            ("State tax paid at entity level", money(state_tax)),
            ("PTET federal benefit", money(ptet_benefit)),
            ("Total annual savings", money(total)),
        ],
        "state": state,
        "savings": total,
        "situation": (
            f"The client operated {biz} in {state} through {entities} separate entities that had "
            f"accumulated over time without a coherent plan, generating {money(profit)} of combined "
            f"annual profit. State income tax of roughly {money(state_tax)} was being paid personally "
            f"on the owner's return."),
        "challenge": (
            f"Two problems compounded each other. The {money(state_tax)} of state tax was a personal "
            f"itemized deduction subject to the state and local tax cap, so most of it produced no "
            f"federal benefit at all. Separately, the {entities}-entity structure was generating "
            f"duplicate filing fees, inconsistent intercompany treatment, and payroll spread across "
            f"multiple registrations without a defensible allocation."),
        "solution": [
            ("Elected pass-through entity tax treatment",
             f"{state} permits a pass-through entity to elect to pay state income tax at the entity "
             f"level. The entity-level tax is an ordinary and necessary business expense deductible "
             f"in computing federal taxable income, and it is not subject to the individual state and "
             f"local tax cap. The owner then receives a credit or exclusion on the state return. "
             f"This converted {money(state_tax)} of largely non-deductible personal state tax into a "
             f"fully deductible business expense."),
            ("Consolidated the operating entities",
             f"We collapsed the {entities} entities into a single operating company with a holding "
             f"structure above it, eliminating duplicate registered agent fees, franchise taxes, and "
             f"return preparation costs, and removing the inconsistent intercompany charges that had "
             f"built up between them."),
            ("Separated real estate and equipment from operations",
             "Real estate and titled equipment were moved into dedicated entities leasing to the "
             "operating company at arm's length rates. This isolates liability, creates a clean "
             "basis for depreciation planning, and produces rent that is taxed once without payroll "
             "tax. We addressed the self-rental rules of Reg. 1.469-2(f)(6) with a grouping election "
             "under Reg. 1.469-4 so that losses would not be stranded."),
            ("Rebuilt payroll and intercompany agreements",
             "Compensation was consolidated onto a single payroll with a documented allocation "
             "across functions, and written intercompany service and lease agreements were adopted "
             "so that every charge between entities has a stated basis."),
        ],
        "result": (
            f"The PTET election alone recovered approximately {money(ptet_benefit)} of federal tax "
            f"annually by converting capped personal state tax into a deductible entity expense. "
            f"Restructuring and the associated compliance and allocation improvements added roughly "
            f"{money(restructure_benefit)}, for a combined annual benefit of about {money(total)}."),
        "takeaways": [
            "The PTET election sidesteps the state and local tax cap by moving the tax to the entity level.",
            f"Consolidating {entities} entities removed duplicate filings and inconsistent intercompany charges.",
            "Separating real estate from operations required a grouping election to avoid the self-rental trap.",
            "Every intercompany charge now has a written agreement and a stated basis.",
        ],
        "faqs": [
            ("What is a pass-through entity tax election?",
             f"<p>It allows a partnership or S corporation to pay state income tax at the entity "
             f"level rather than passing it to owners. The entity-level tax is deductible in "
             f"computing federal income, and it is not subject to the individual state and local tax "
             f"cap, so it restores a federal deduction that would otherwise be lost.</p>"),
            ("Does every state offer this?",
             f"<p>No. A majority of states with an income tax have enacted a version, including "
             f"{state}, but the mechanics, election deadlines, and credit calculations differ "
             f"significantly. The election is generally annual and must be made on time.</p>"),
            ("Why separate real estate into its own entity?",
             "<p>It isolates liability, creates a clean depreciation and cost segregation platform, "
             "and produces rent taxed once without payroll tax. The tradeoff is the self-rental rule, "
             "which recharacterizes net rental income as non-passive while leaving losses passive, "
             "and that is resolved with a grouping election.</p>"),
            ("Is consolidating entities always the right move?",
             "<p>No. Separate entities are appropriate where they isolate genuinely different risks, "
             "hold different asset classes, or have different ownership. What does not work is "
             "entities that accumulated without a plan and carry duplicate cost with no "
             "corresponding benefit.</p>"),
        ],
        "related_pages": [
            ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
            ("/c-corp-income-shifting-strategy/", "C-Corp Income Shifting Strategy"),
            ("/multi-state-global-tax/", "Multi-State and Global Tax Planning"),
            ("/business-owner-small-business-tax/", "Business Owner and Small Business Tax"),
        ],
    }


def str_participation(rng: random.Random, i: int) -> dict:
    prop, terrain, regions = rng.choice(D.STR_TYPES)
    region = rng.choice(regions)
    state, srate = pick_state(rng)
    prof = rng.choice(D.PROFESSIONS_W2)

    w2 = round_to(rng.uniform(300_000, 1_100_000), 5_000)
    suspended = round_to(rng.uniform(90_000, 460_000), 1_000)
    hours = rng.randint(103, 189)
    avg_before = round(rng.uniform(8.5, 21.0), 1)
    avg_after = round(rng.uniform(3.1, 6.4), 1)

    f = fed_rate(w2)
    combined = f + srate
    savings = round_to(min(suspended, w2) * combined, 500)

    return {
        "cat": "Real Estate Investors",
        "kind": "participation",
        "slug": f"str-material-participation-release-{terrain}-{i}",
        "h1": f"{prof.title()} Releases {kmoney(suspended)} of Suspended Losses by Fixing Material Participation",
        "title": f"STR Losses Released: {kmoney(suspended)}",
        "desc": (f"How {prof} with a {prop} in {region} restructured operations to meet the "
                 f"seven-day rule and material participation tests, releasing {money(suspended)} of "
                 f"suspended losses worth approximately {money(savings)}."),
        "profile": [
            ("Client", prof.capitalize()),
            ("W-2 income", money(w2)),
            ("Asset", f"{prop.capitalize()} in {region}"),
            ("State", state),
            ("Average stay before / after", f"{avg_before} days / {avg_after} days"),
            ("Suspended losses released", money(suspended)),
            ("Tax reduction", money(savings)),
        ],
        "state": state,
        "savings": savings,
        "situation": (
            f"The client, {prof} earning {money(w2)}, owned a {prop} in {region} that had already "
            f"been cost segregated. The deductions had generated {money(suspended)} of losses that "
            f"were sitting suspended and producing no benefit whatsoever."),
        "challenge": (
            f"Two separate failures had made the losses passive. The property's average period of "
            f"customer use was {avg_before} days, above the seven-day threshold, so it remained a "
            f"rental activity subject to the per se passive rule of Section 469(c)(2). And a "
            f"full-service property manager was handling everything, logging far more hours than the "
            f"owner, which defeated the 100-hour material participation test even if the seven-day "
            f"issue had been solved. Clearing one hurdle without the other would have changed "
            f"nothing."),
        "solution": [
            ("Restructured booking policy to hold the seven-day average",
             f"Minimum stay was set to three nights and the maximum booking length was capped, with "
             f"a monitoring process that tracks the running annual average rather than checking it "
             f"after year end. The average period of customer use fell to {avg_after} days, placing "
             f"the property outside the definition of a rental activity under Treasury Regulation "
             f"1.469-1T(e)(3)(ii)(A)."),
            ("Replaced full-service management with unbundled vendors",
             "The full-service management agreement was terminated and replaced with a per-turnover "
             "cleaning contract and on-call maintenance. The owner took back guest communication, "
             "pricing, listing management, supply purchasing, and vendor supervision. No single "
             "individual now participates more than the owner, which is the requirement under "
             "Treasury Regulation 1.469-5T(a)(3)."),
            ("Built a contemporaneous, corroborated log",
             f"The owner logged {hours} hours across the year with dated entries, specific task "
             f"descriptions, and supporting evidence: booking platform message timestamps, supply "
             f"and repair receipts, contractor text threads, and calendar entries. Travel time was "
             f"deliberately excluded, since the IRS routinely challenges it, and entries were left "
             f"irregular rather than rounded."),
            ("Released the suspended losses",
             f"With the activity non-rental and material participation established, the current-year "
             f"loss became non-passive. Suspended losses of {money(suspended)} from prior years "
             f"became deductible as the activity generated the capacity to absorb them, offsetting "
             f"the client's W-2 income."),
        ],
        "result": (
            f"Releasing {money(suspended)} of previously suspended losses produced approximately "
            f"{money(savings)} of tax reduction at a {combined * 100:.1f}% combined marginal rate. "
            f"The cost segregation study had been done correctly two years earlier; the deductions "
            f"had simply been stranded by an operating structure nobody had reviewed against the "
            f"passive loss rules."),
        "takeaways": [
            "The seven-day rule and material participation are two separate hurdles and both must be cleared.",
            f"Cutting the average stay from {avg_before} to {avg_after} days changed the property's entire tax character.",
            "A full-service property manager is the single most common reason the 100-hour test fails.",
            "Deductions were never the problem here; the operating structure was.",
        ],
        "faqs": [
            ("Why were the losses suspended in the first place?",
             f"<p>The average stay of {avg_before} days kept the property classified as a rental "
             f"activity, which is passive per se under Section 469(c)(2) regardless of "
             f"participation. Even fixing that alone would not have helped, because the property "
             f"manager was out-participating the owner.</p>"),
            ("Can suspended losses be used once you qualify?",
             "<p>Yes. Suspended passive losses carry forward indefinitely and become deductible when "
             "the activity generates income, when other passive income is available, or when the "
             "activity's character changes so the losses are no longer passive. They are also fully "
             "released on a qualifying disposition.</p>"),
            ("Does terminating the property manager really matter?",
             "<p>It is often decisive. The 100-hour test requires that no other individual "
             "participate more than the taxpayer. A full-service manager almost always exceeds the "
             "owner's hours, which defeats the test regardless of how many hours the owner logs.</p>"),
            ("What documentation was required?",
             f"<p>A contemporaneous dated log of {hours} hours with specific task descriptions, "
             f"corroborated by booking platform timestamps, receipts, contractor communications, and "
             f"calendar entries. Reconstructed summaries with round numbers are consistently given "
             f"little weight by the Tax Court.</p>"),
        ],
        "related_pages": [
            ("/material-participation-short-term-rental-7-day-rule/", "Material Participation and the STR 7-Day Rule"),
            ("/short-term-rental-tax-loophole-2026/", "The Short-Term Rental Tax Loophole in 2026"),
            ("/reps-real-estate-professional-status/", "Real Estate Professional Status: How to Qualify"),
            ("/short-term-rental-tax-strategy/", "Short-Term Rental Tax Strategy"),
        ],
    }


def amendment_recovery(rng: random.Random, i: int) -> dict:
    who = rng.choice(D.PROFESSIONS_W2 + D.BUSINESS_TYPES)
    state, srate = pick_state(rng)
    years = rng.randint(2, 3)
    refund = round_to(rng.uniform(16_000, 118_000), 500)
    per_year = round_to(refund / years, 500)

    issues = rng.sample([
        ("unclaimed depreciation on a rental placed in service years earlier",
         "The prior preparer had never set up a depreciation schedule for a converted primary "
         "residence, so no depreciation had been claimed at all since the conversion date."),
        ("a missed home office and accountable plan reimbursement",
         "The business had been reimbursing the owner informally rather than under a written "
         "accountable plan, so legitimate expenses were being treated as nondeductible personal "
         "outlays instead of deductible business reimbursements."),
        ("an overlooked qualified business income deduction",
         "The Section 199A deduction had been computed incorrectly, treating the business as a "
         "specified service trade or business when it was not, which eliminated a deduction the "
         "client was entitled to claim in full."),
        ("unclaimed retirement plan contributions",
         "Employer contributions that had actually been funded were never reflected on the return, "
         "so the client had paid for the contribution without receiving the deduction."),
        ("a misapplied passive loss limitation",
         "Rental losses had been suspended even though the activity met the short-term rental "
         "exception and the owner materially participated, so deductible losses were treated as "
         "carryforwards."),
        ("uncaptured state credits and estimated payments",
         "State credits and previously made estimated payments had not been carried onto the return, "
         "resulting in an overstated balance due in each affected year."),
        ("incorrect basis on a securities sale",
         "Cost basis had been reported as zero on a broker statement that lacked basis information, "
         "so the entire proceeds had been taxed as gain rather than the actual appreciation."),
        ("a missed cost segregation catch-up on a commercial building",
         "A building had been on a single 39-year schedule with no component analysis since "
         "acquisition, understating depreciation in every year since."),
    ], k=min(2, 2))

    f = fed_rate(200_000)
    return {
        "cat": "Amendment Recovery",
        "kind": "amendment",
        "slug": f"amended-return-recovery-{i}",
        "h1": f"Amended Returns Recover {kmoney(refund)} Across {years} Prior Years",
        "title": f"Amended Returns Recover {kmoney(refund)}",
        "desc": (f"How a review of {years} prior year returns for {who} identified overlooked "
                 f"deductions and reporting errors, producing {money(refund)} in refunds through "
                 f"amended filings."),
        "profile": [
            ("Client", who.capitalize()),
            ("Years amended", f"{years} years"),
            ("State", state),
            ("Primary issues found", issues[0][0].capitalize()),
            ("Average recovery per year", money(per_year)),
            ("Total refund recovered", money(refund)),
        ],
        "state": state,
        "savings": refund,
        "situation": (
            f"A prior year review is part of every engagement we open. For this client, {who}, we "
            f"pulled the last {years} filed returns along with the underlying source documents "
            f"before doing any forward-looking planning."),
        "challenge": (
            f"Returns had been filed on time and appeared unremarkable. Nothing about them signaled "
            f"a problem, which is precisely why the errors had persisted. The client had no reason "
            f"to suspect anything and the preparer had no reason to revisit prior work."),
        "solution": [
            (f"Identified {issues[0][0]}", issues[0][1]),
            (f"Identified {issues[1][0]}", issues[1][1]),
            ("Confirmed the statute of limitations was open",
             "A claim for refund must generally be filed within three years of the return's filing "
             "date or two years from the date the tax was paid, whichever is later. All affected "
             "years remained inside that window, which is the threshold question before any "
             "amendment work begins."),
            ("Filed corrected returns with full substantiation",
             "Amended federal returns were filed with a clear explanation of each change and "
             "supporting schedules attached, along with corresponding state amendments. Where the "
             "correction involved a depreciation method rather than an error, we used a Form 3115 "
             "change in accounting method instead of an amendment, since an established method "
             "cannot be corrected by amending."),
        ],
        "result": (
            f"The amendments produced {money(refund)} in refunds across {years} years, an average of "
            f"{money(per_year)} per year, plus statutory interest. The same issues were corrected "
            f"prospectively so they would not repeat, which is generally worth more over time than "
            f"the refund itself."),
        "takeaways": [
            f"A routine prior year review recovered {money(refund)} that would otherwise have expired unclaimed.",
            "Refund claims are generally limited to three years, so the review has to happen before the window closes.",
            "Depreciation errors are corrected by Form 3115, not by amendment, because they are established methods.",
            "Correcting the issues prospectively is usually worth more than the refund.",
        ],
        "faqs": [
            ("How far back can amended returns go?",
             "<p>Generally three years from the date the original return was filed, or two years from "
             "the date the tax was paid, whichever is later. Once that window closes the refund is "
             "permanently lost, which is why a prior year review early in an engagement matters.</p>"),
            ("Does filing an amended return increase audit risk?",
             "<p>An amended return receives review, but a well-documented amendment with a clear "
             "explanation and supporting schedules is routine. The risk of leaving a known error "
             "uncorrected generally exceeds the risk of correcting it properly.</p>"),
            ("Do you get interest on the refund?",
             "<p>Yes. The IRS pays statutory interest on refunds, generally running from the later of "
             "the return due date or the filing date until the refund is issued.</p>"),
            ("Why use Form 3115 instead of amending for depreciation?",
             "<p>Because depreciation used for two or more consecutive years is an established method "
             "of accounting. Correcting it is a method change made on Form 3115, which also has the "
             "advantage of reaching back past the three-year amendment window to the "
             "placed-in-service year.</p>"),
        ],
        "related_pages": [
            ("/form-3115-cost-segregation-lookback/", "Form 3115 Cost Segregation Lookback"),
            ("/3-year-tax-lookback-cleanup/", "Three-Year Tax Lookback and Cleanup"),
            ("/tax-compliance-irs-representation/", "Tax Compliance and IRS Representation"),
            ("/accountable-plan/", "Accountable Plans Done Correctly"),
        ],
    }


def w2_high_income(rng: random.Random, i: int) -> dict:
    prof = rng.choice(D.PROFESSIONS_W2)
    state, srate = pick_state(rng)
    prop, terrain, regions = rng.choice(D.STR_TYPES)
    region = rng.choice(regions)

    w2 = round_to(rng.uniform(420_000, 2_100_000), 5_000)
    price = round_to(rng.uniform(600_000, 2_600_000), 5_000)
    land = round_to(price * rng.uniform(0.15, 0.25), 1_000)
    basis = price - land
    reclass = round_to(basis * rng.uniform(0.27, 0.35), 1_000)

    retirement = round_to(rng.uniform(28_000, 76_000), 500)
    charitable = round_to(rng.uniform(20_000, 95_000), 500)

    f = fed_rate(w2)
    combined = f + srate
    total_ded = reclass + retirement + charitable
    savings = round_to(min(total_ded, w2 * 0.8) * combined, 500)

    return {
        "cat": "Real Estate Investors",
        "kind": "w2",
        "slug": f"w2-high-income-reduction-{i}",
        "h1": f"{prof.title()} Reduces Taxable Income by {kmoney(total_ded)} Without Changing Jobs",
        "title": f"STR Investor Cuts Taxable Income {kmoney(total_ded)}",
        "desc": (f"How {prof} earning {money(w2)} combined a short-term rental cost segregation "
                 f"study, retirement contributions, and a donor advised fund to reduce taxable "
                 f"income by {money(total_ded)} and tax by approximately {money(savings)}."),
        "profile": [
            ("Client", prof.capitalize()),
            ("W-2 income", money(w2)),
            ("State", state),
            ("Real estate acquired", f"{money(price)} {prop} in {region}"),
            ("Total deductions generated", money(total_ded)),
            ("Marginal rate", f"{combined * 100:.1f}%"),
            ("Tax reduction", money(savings)),
        ],
        "state": state,
        "savings": savings,
        "situation": (
            f"The client, {prof} earning {money(w2)} in W-2 income, had no business entity and "
            f"almost no planning levers. Withholding was correct, deductions were limited to the "
            f"standard items, and the effective rate was as high as it can get for someone with a "
            f"single income source."),
        "challenge": (
            f"W-2 income is the hardest income to shelter. There is no entity to restructure, no "
            f"self-employment tax to reduce, and no business deductions to accelerate. Most of what "
            f"is marketed to high earners in this position either does not work or does not survive "
            f"examination. The client had already been approached with several arrangements that we "
            f"advised against."),
        "solution": [
            ("Acquired and structured a short-term rental",
             f"The client purchased a {money(price)} {prop} in {region} and operated it with an "
             f"average stay under seven days. That places the activity outside the definition of a "
             f"rental activity under Treasury Regulation 1.469-1T(e)(3)(ii)(A), so only material "
             f"participation is required for the loss to be non-passive and deductible against wages."),
            ("Documented material participation before year end",
             "Cleaning was contracted per turnover rather than through a full-service manager, so no "
             "individual out-participated the owners. Hours were logged contemporaneously with "
             "specific task descriptions and corroborating records. This was set up before the "
             "purchase closed, not reconstructed at filing time."),
            ("Completed a cost segregation study",
             f"With {money(land)} allocated to land, the study reclassified {money(reclass)} of the "
             f"{money(basis)} depreciable basis into 5-, 7-, and 15-year property, all eligible for "
             f"100% bonus depreciation under the OBBBA."),
            ("Maximized retirement and structured charitable giving",
             f"Employer plan deferrals and after-tax contributions were maximized at {money(retirement)}. "
             f"Separately, {money(charitable)} of appreciated securities held more than one year were "
             f"contributed to a donor advised fund, deducting fair market value while avoiding the "
             f"capital gain entirely, and bunching several years of intended giving into one high-rate "
             f"year."),
        ],
        "result": (
            f"Total deductions of {money(total_ded)} reduced tax by approximately {money(savings)} at "
            f"a {combined * 100:.1f}% combined marginal rate. The rental is now a recurring platform "
            f"rather than a one-year event, and the donor advised fund lets the client grant to "
            f"charities over time while having taken the deduction in the highest-rate year."),
        "takeaways": [
            "W-2 income has almost no built-in levers, so the plan had to create one through real estate.",
            "The short-term rental exception, not real estate professional status, is what made the loss usable.",
            "Donating appreciated securities deducts fair market value and avoids the capital gain entirely.",
            "Bunching several years of giving into one high-rate year materially increases its value.",
        ],
        "faqs": [
            ("Can a W-2 earner really deduct rental losses against wages?",
             "<p>Yes, in specific circumstances. A property with an average period of customer use of "
             "seven days or less is not a rental activity under Treasury Regulation "
             "1.469-1T(e)(3)(ii)(A), so the per se passive rule does not apply and only material "
             "participation is required. Without that exception the loss would be suspended.</p>"),
            ("Was real estate professional status needed?",
             "<p>No. REPS requires more than 750 hours plus more than half of all personal services "
             "in real property trades or businesses, which is not achievable alongside a demanding "
             "full-time career. The short-term rental exception is the accessible path.</p>"),
            ("Why donate securities instead of cash?",
             "<p>Contributing appreciated securities held more than one year allows a deduction at "
             "fair market value while permanently avoiding the capital gain that a sale would "
             "trigger. Donating cash after selling produces a smaller net benefit.</p>"),
            ("Is this repeatable in future years?",
             "<p>The retirement and charitable components are. The cost segregation deduction is "
             "largely a first-year event for a given property, so continuing the strategy means "
             "either acquiring additional properties or shifting to other levers, which is how the "
             "multi-year plan is built.</p>"),
        ],
        "related_pages": [
            ("/short-term-rental-tax-loophole-2026/", "The Short-Term Rental Tax Loophole in 2026"),
            ("/material-participation-short-term-rental-7-day-rule/", "Material Participation and the STR 7-Day Rule"),
            ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
            ("/individual-tax-planning-high-earners/", "Advanced Income and Entity Planning"),
        ],
    }


BUILDERS = [
    (str_cost_seg, 62),
    (ltr_lookback, 46),
    (commercial_cost_seg, 72),
    (scorp_optimization, 56),
    (ccorp_shift, 36),
    (retirement_stack, 46),
    (entity_ptet, 40),
    (str_participation, 36),
    (amendment_recovery, 40),
    (w2_high_income, 46),
]
