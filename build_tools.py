#!/usr/bin/env python3
"""Build interactive calculators, the expanded glossary, the HTML sitemap, and
the partners page."""

from __future__ import annotations

import html as _html
import re
import sys
from pathlib import Path

import site_template as T

PUBLISHED = "2026-08-15"
MODIFIED = "2026-08-15"
ROOT = T.ROOT

CALC_CSS = """
    <style>
      .calc{background:#fff;border:1px solid #e5e7eb;border-radius:14px;padding:26px;
        box-shadow:var(--shadow-sm);margin:8px 0 12px}
      .calc-row{display:grid;grid-template-columns:1fr 1fr;gap:18px}
      .calc-field{display:flex;flex-direction:column;gap:6px;margin-bottom:16px;min-width:0}
      .calc-field label{font-size:14px;font-weight:600;color:var(--dark)}
      .calc-field .hint{font-size:12.5px;color:var(--medium);font-weight:400}
      .calc-field input,.calc-field select{padding:12px 14px;font-size:16px;min-height:48px;
        border:1px solid #d9dde3;border-radius:8px;font-family:inherit;color:var(--dark);
        background:#fff;width:100%}
      .calc-field input:focus,.calc-field select:focus{outline:2px solid var(--accent);
        outline-offset:1px;border-color:var(--accent)}
      .calc-out{background:var(--primary);color:#fff;border-radius:12px;padding:24px;margin-top:20px}
      .calc-out h3{color:#fff;font-size:1.05rem;margin-bottom:16px}
      .calc-lines{display:grid;gap:10px}
      .calc-line{display:flex;justify-content:space-between;gap:16px;align-items:baseline;
        padding-bottom:9px;border-bottom:1px solid rgba(255,255,255,.14);font-size:15px}
      .calc-line:last-child{border-bottom:none}
      .calc-line span:first-child{color:rgba(255,255,255,.8)}
      .calc-line span:last-child{font-weight:700;white-space:nowrap}
      .calc-line.headline{font-size:20px;padding-top:6px}
      .calc-line.headline span:last-child{color:var(--accent);font-size:24px}
      .calc-note{font-size:12.5px;color:var(--medium);line-height:1.6;margin-top:14px}
      @media (max-width:768px){
        .calc{padding:20px}
        .calc-row{grid-template-columns:1fr;gap:0}
        .calc-line{flex-direction:column;gap:2px}
        .calc-line span:last-child{font-size:18px}
        .calc-line.headline span:last-child{font-size:22px}
      }
    </style>"""


def field(fid, label, value, hint="", kind="number", options=None, step=None):
    if options:
        opts = "\n".join(
            f'                    <option value="{v}"{" selected" if v == value else ""}>{lab}</option>'
            for v, lab in options
        )
        control = (f'                <select id="{fid}">\n{opts}\n                </select>')
    else:
        st = f' step="{step}"' if step else ""
        control = (f'                <input type="{kind}" id="{fid}" value="{value}"'
                   f' inputmode="decimal"{st}>')
    hint_html = f'\n                <span class="hint">{hint}</span>' if hint else ""
    return f"""            <div class="calc-field">
                <label for="{fid}">{label}</label>{hint_html}
{control}
            </div>"""


# ---------------------------------------------------------------- calculators

COST_SEG_CALC = {
 "slug": "cost-segregation-savings-calculator",
 "h1": "Cost Segregation Savings Calculator",
 "title": "Cost Segregation Calculator: Estimate Your Deduction",
 "desc": "Estimate the first-year deduction and tax savings from a cost segregation study on your property. Adjust purchase price, land allocation, property type, and marginal rate.",
 "definition": "A cost segregation savings calculator estimates the first-year depreciation deduction a study would produce by applying a typical reclassification percentage for your property type to your depreciable basis, then applying 100% bonus depreciation to the reclassified amount. It is an estimate, not a study: the actual result depends on an engineering analysis of your specific property.",
 "form": [
   ("cs-price", "Purchase price", "1200000", "What you paid for the property, excluding closing costs allocated elsewhere.", "number", None, "1000"),
   ("cs-land", "Land allocation (%)", "20", "Land is not depreciable. An appraisal should support this.", "number", None, "1"),
   ("cs-type", "Property type", "0.30", "Drives the typical reclassification percentage.", None,
     [("0.46","Car wash (35-46%)"),("0.42","Hotel / hospitality (30-45%)"),
      ("0.36","Restaurant (30-40%)"),("0.34","Self-storage (27-39%)"),
      ("0.32","Short-term rental, furnished (26-36%)"),("0.30","Multifamily (22-33%)"),
      ("0.28","Medical / dental office (22-35%)"),("0.26","Retail center (20-31%)"),
      ("0.24","Long-term rental (21-32%)"),("0.21","Office building (15-26%)"),
      ("0.19","Warehouse / industrial (14-26%)")], None),
   ("cs-rate", "Combined marginal tax rate (%)", "37", "Federal plus state, on the income the deduction offsets.", "number", None, "0.1"),
   ("cs-life", "Recovery period", "39", "39 years for nonresidential and short-term rentals, 27.5 for long-term residential rentals.", None,
     [("39","39 years (nonresidential / STR)"),("27.5","27.5 years (residential rental)")], None),
   ("cs-months", "Months in service this year", "12", "Real property uses a mid-month convention.", "number", None, "1"),
 ],
 "js": """
      function fmt(n){ return '$' + Math.round(n).toLocaleString('en-US'); }
      function calc(){
        var price = +document.getElementById('cs-price').value || 0;
        var landPct = Math.min(Math.max(+document.getElementById('cs-land').value || 0, 0), 90);
        var reclassPct = +document.getElementById('cs-type').value || 0.3;
        var rate = Math.min(Math.max(+document.getElementById('cs-rate').value || 0, 0), 60) / 100;
        var life = +document.getElementById('cs-life').value || 39;
        var months = Math.min(Math.max(+document.getElementById('cs-months').value || 12, 1), 12);

        var land = price * landPct / 100;
        var basis = Math.max(price - land, 0);
        var reclass = basis * reclassPct;
        var remaining = basis - reclass;
        var sl = remaining / life * ((months - 0.5) / 12);
        var withStudy = reclass + sl;
        var without = basis / life * ((months - 0.5) / 12);
        var extra = withStudy - without;
        var savings = extra * rate;

        document.getElementById('cs-basis').textContent = fmt(basis);
        document.getElementById('cs-reclass').textContent = fmt(reclass) + '  (' + Math.round(reclassPct*100) + '%)';
        document.getElementById('cs-without').textContent = fmt(without);
        document.getElementById('cs-with').textContent = fmt(withStudy);
        document.getElementById('cs-extra').textContent = fmt(extra);
        document.getElementById('cs-savings').textContent = fmt(savings);
      }
 """,
 "outputs": [("cs-basis","Depreciable basis"),("cs-reclass","Reclassified to 5/7/15-year"),
             ("cs-without","Year 1 depreciation without a study"),
             ("cs-with","Year 1 depreciation with a study"),
             ("cs-extra","Additional first-year deduction")],
 "headline": ("cs-savings", "Estimated first-year tax savings"),
 "note": "This is an estimate using typical reclassification ranges by property type. An engineering study prices your actual components and can land above or below this range. The estimate also assumes you can use the deduction this year, which depends on the passive activity rules of IRC Section 469, your basis, the at-risk rules, and the excess business loss limitation. Accelerated depreciation is recaptured on sale under Sections 1245 and 1250 unless deferred through a 1031 exchange or eliminated by the basis step-up at death.",
 "faqs": [
   ("How accurate is a cost segregation calculator?",
    "<p>It is directionally useful and not a substitute for a study. The calculator applies a typical reclassification percentage for the property type. An engineering study prices your actual components, and the result commonly lands several percentage points above or below the estimate depending on site work, specialty systems, and build-out.</p>"),
   ("Does this account for whether I can actually use the deduction?",
    "<p>No, and that is the most important caveat. A rental loss is passive by default under IRC Section 469 and cannot offset wages unless you qualify as a real estate professional or the property meets the short-term rental exception with material participation. The calculator shows the deduction, not its usability.</p>"),
   ("What land allocation should I use?",
    "<p>Use the allocation your appraisal supports. It commonly runs 15% to 30% depending on the market and property type, and it matters enormously: moving from 20% to 30% on a $1 million property removes $100,000 from depreciable basis and roughly $30,000 from the first-year deduction.</p>"),
   ("Is my short-term rental 27.5 or 39 years?",
    "<p>Generally 39 years. Residential rental property requires that 80% or more of gross rental income come from dwelling units, and a unit is not a dwelling unit if more than half its use is transient. A property averaging seven days or less per stay is typically nonresidential real property.</p>"),
 ],
}

SCORP_CALC = {
 "slug": "s-corp-tax-savings-calculator",
 "h1": "S-Corp Tax Savings Calculator",
 "title": "S-Corp Tax Savings Calculator (2026)",
 "desc": "Estimate the self-employment tax you would save by electing S-Corp treatment, net of payroll and compliance costs, based on your net profit and reasonable compensation.",
 "definition": "An S-Corp tax savings calculator estimates the employment tax difference between default pass-through taxation, where all net profit is subject to self-employment tax, and S-Corp taxation, where only reasonable W-2 wages are subject to payroll tax. The saving is 15.3% on the amount characterized as distribution up to the Social Security wage base, and 2.9% to 3.8% above it. An S election reduces employment tax only, never income tax.",
 "form": [
   ("sc-profit", "Net business profit", "180000", "Before any owner wage, after all other expenses.", "number", None, "1000"),
   ("sc-wage", "Planned reasonable compensation", "95000", "Priced from market wage data for the roles you perform, not a percentage rule.", "number", None, "1000"),
   ("sc-base", "Social Security wage base", "184500", "Adjusts annually. Confirm the current figure before relying on it.", "number", None, "100"),
   ("sc-costs", "Added annual compliance cost", "3000", "1120-S preparation plus payroll processing and state filings.", "number", None, "100"),
   ("sc-filing", "Filing status", "250000", "Sets the additional Medicare tax threshold.", None,
     [("250000","Married filing jointly"),("200000","Single / head of household")], None),
 ],
 "js": """
      function fmt(n){ return (n<0?'-$':'$') + Math.abs(Math.round(n)).toLocaleString('en-US'); }
      function calc(){
        var profit = Math.max(+document.getElementById('sc-profit').value || 0, 0);
        var wage = Math.max(+document.getElementById('sc-wage').value || 0, 0);
        var base = Math.max(+document.getElementById('sc-base').value || 0, 0);
        var costs = Math.max(+document.getElementById('sc-costs').value || 0, 0);
        var thresh = +document.getElementById('sc-filing').value || 250000;
        if (wage > profit) wage = profit;

        // Sole prop / partnership: SE tax on 92.35% of profit
        var seBase = profit * 0.9235;
        var seSS = Math.min(seBase, base) * 0.124;
        var seMed = seBase * 0.029;
        var seAdd = Math.max(seBase - thresh, 0) * 0.009;
        var seTotal = seSS + seMed + seAdd;

        // S-Corp: payroll tax on wage only (both halves)
        var prSS = Math.min(wage, base) * 0.124;
        var prMed = wage * 0.029;
        var prAdd = Math.max(wage - thresh, 0) * 0.009;
        var prTotal = prSS + prMed + prAdd;

        var gross = seTotal - prTotal;
        var net = gross - costs;
        var distribution = profit - wage;

        document.getElementById('sc-se').textContent = fmt(seTotal);
        document.getElementById('sc-pr').textContent = fmt(prTotal);
        document.getElementById('sc-dist').textContent = fmt(distribution);
        document.getElementById('sc-gross').textContent = fmt(gross);
        document.getElementById('sc-net').textContent = fmt(net);
        var verdict = document.getElementById('sc-verdict');
        if (net > 1500) verdict.textContent = 'An S election likely pays for itself at this profit level.';
        else if (net > 0) verdict.textContent = 'Marginal. The saving is real but thin against the added complexity.';
        else verdict.textContent = 'At this profit level the compliance cost exceeds the saving.';
      }
 """,
 "outputs": [("sc-se","Self-employment tax as an LLC / sole prop"),
             ("sc-pr","Payroll tax as an S-Corp"),
             ("sc-dist","Profit distributed free of employment tax"),
             ("sc-gross","Gross employment tax saved")],
 "headline": ("sc-net", "Net annual saving after costs"),
 "extra_out": ("sc-verdict", ""),
 "note": "This estimates employment tax only. An S election does not reduce income tax. Two factors can reverse the answer: an unsupported wage invites a reasonable compensation adjustment with back payroll tax, penalties, and interest across every open year; and above the Section 199A taxable income thresholds, the qualified business income deduction for a non-service business is limited by W-2 wages, so a lower salary can cost more in lost deduction than it saves in payroll tax. State payroll taxes, unemployment insurance, and state entity-level fees are not included.",
 "faqs": [
   ("At what profit does an S-Corp election make sense?",
    "<p>Generally once net profit reliably exceeds roughly $60,000 to $80,000 per owner. Below that, the added cost of a separate 1120-S return, payroll processing, and state filings tends to exceed the employment tax saved.</p>"),
   ("What reasonable compensation should I enter?",
    "<p>The amount a comparable business would pay someone else to do what you do, priced from Bureau of Labor Statistics wage data and industry surveys and blended across the roles you actually perform. There is no 60/40 rule and no safe harbor percentage anywhere in the Code or IRS guidance.</p>"),
   ("Does an S-Corp reduce my income tax?",
    "<p>No. Profit is taxed at the same ordinary rates either way. The election reduces self-employment and payroll tax only.</p>"),
   ("Should I put rental property in an S-Corp?",
    "<p>Generally no. Rental income is not subject to self-employment tax, so there is nothing to save, and distributing appreciated property out of an S corporation triggers gain as though it had been sold at fair market value.</p>"),
 ],
}

BONUS_CALC = {
 "slug": "bonus-depreciation-calculator",
 "h1": "Bonus Depreciation Calculator",
 "title": "Bonus Depreciation Calculator (2026)",
 "desc": "Compare first-year deductions under 100% bonus depreciation, Section 179 expensing, and regular MACRS for an equipment or asset purchase, and see the tax value of each.",
 "definition": "A bonus depreciation calculator compares the first-year deduction available under IRC Section 168(k) bonus depreciation, Section 179 expensing, and standard MACRS for a given asset purchase. Under the One Big Beautiful Bill Act, bonus depreciation is 100% and permanent for qualifying property acquired after January 19, 2025, so both bonus and Section 179 generally produce a full first-year deduction, and the choice turns on loss creation, state conformity, and property type.",
 "form": [
   ("bd-cost", "Asset cost", "250000", "Total placed in service this year.", "number", None, "500"),
   ("bd-life", "MACRS recovery period", "5", "Bonus depreciation applies to 20 years or less.", None,
     [("3","3-year"),("5","5-year (vehicles, computers, appliances)"),
      ("7","7-year (furniture, most equipment)"),("15","15-year (land improvements, QIP)"),
      ("20","20-year"),("27.5","27.5-year (residential rental)"),
      ("39","39-year (nonresidential real property)")], None),
   ("bd-business", "Business use (%)", "100", "Below 50% disables accelerated methods on listed property.", "number", None, "1"),
   ("bd-income", "Business taxable income", "400000", "Section 179 cannot exceed this. Bonus depreciation can.", "number", None, "1000"),
   ("bd-rate", "Combined marginal tax rate (%)", "37", "Federal plus state.", "number", None, "0.1"),
 ],
 "js": """
      function fmt(n){ return '$' + Math.round(n).toLocaleString('en-US'); }
      function calc(){
        var cost = Math.max(+document.getElementById('bd-cost').value || 0, 0);
        var life = +document.getElementById('bd-life').value || 5;
        var use = Math.min(Math.max(+document.getElementById('bd-business').value || 100, 0), 100)/100;
        var income = Math.max(+document.getElementById('bd-income').value || 0, 0);
        var rate = Math.min(Math.max(+document.getElementById('bd-rate').value || 0, 0), 60)/100;

        var basis = cost * use;
        var bonusEligible = life <= 20;
        var s179Eligible = life <= 20;

        var bonus = bonusEligible ? basis : 0;
        var s179 = s179Eligible ? Math.min(basis, income, 2560000) : 0;

        // Regular MACRS year 1, half-year convention
        var r1;
        if (life <= 10) r1 = (2/life) * 0.5;
        else if (life <= 20) r1 = (1.5/life) * 0.5;
        else r1 = (1/life) * (11.5/12);
        var macrs = basis * r1;

        document.getElementById('bd-basis').textContent = fmt(basis);
        document.getElementById('bd-bonus').textContent = bonusEligible ? fmt(bonus) : 'Not eligible (over 20-year life)';
        document.getElementById('bd-179').textContent = s179Eligible ? fmt(s179) : 'Not eligible';
        document.getElementById('bd-macrs').textContent = fmt(macrs);
        var best = Math.max(bonus, s179, macrs);
        document.getElementById('bd-value').textContent = fmt(best * rate);
        var note = document.getElementById('bd-verdict');
        if (!bonusEligible) note.textContent = 'Real property over a 20-year life is not bonus eligible. Section 179 can still cover roofs, HVAC, fire protection, and security systems on nonresidential buildings.';
        else if (s179 < bonus) note.textContent = 'Bonus depreciation gives the larger deduction here, and unlike Section 179 it can create a loss.';
        else note.textContent = 'Both reach the full basis. Prefer Section 179 if your state decouples from bonus depreciation, or if you want asset-level control.';
      }
 """,
 "outputs": [("bd-basis","Depreciable basis (after business use)"),
             ("bd-bonus","100% bonus depreciation"),
             ("bd-179","Section 179 expensing"),
             ("bd-macrs","Regular MACRS, year 1")],
 "headline": ("bd-value", "Tax value of the largest deduction"),
 "extra_out": ("bd-verdict", ""),
 "note": "Section 179 is capped (approximately $2.56 million for 2026, with a phase-out beginning around $4.09 million of purchases) and cannot create or increase a loss. Bonus depreciation is uncapped and can. Passenger automobiles are separately limited by the Section 280F luxury auto caps, which this calculator does not apply. Many states decouple from federal bonus depreciation and require an addback, so confirm your state treatment before relying on the federal result.",
 "faqs": [
   ("Is bonus depreciation still 100% in 2026?",
    "<p>Yes. The One Big Beautiful Bill Act restored the 100% rate on a permanent basis for qualifying property acquired after January 19, 2025, removing the phase-down that would have cut it to 20% in 2026 and zero in 2027.</p>"),
   ("Should I use Section 179 or bonus depreciation?",
    "<p>Use bonus depreciation when you need the deduction to create a loss, since Section 179 cannot. Use Section 179 for roofs, HVAC, fire protection, and security systems on nonresidential buildings, which bonus cannot reach, and in states that decouple from bonus depreciation.</p>"),
   ("Does this calculator handle vehicles?",
    "<p>Not the luxury auto limits. Passenger automobiles are capped under Section 280F regardless of method. Vehicles above 6,000 pounds gross vehicle weight rating fall outside that definition and have separate rules, and business use must exceed 50% for accelerated methods.</p>"),
   ("What is the mid-quarter convention?",
    "<p>If more than 40% of the total basis of personal property placed in service during the year falls in the fourth quarter, the mid-quarter convention replaces the half-year convention for every asset placed in service that year, reducing first-year MACRS deductions. This calculator assumes the half-year convention.</p>"),
 ],
}

CALCULATORS = [COST_SEG_CALC, SCORP_CALC, BONUS_CALC]


def build_calculator(c: dict) -> str:
    path = f"/{c['slug']}/"
    url = f"{T.SITE}{path}"

    fields = "\n".join(field(*f) for f in c["form"])
    outs = "\n".join(
        f'                <div class="calc-line"><span>{label}</span>'
        f'<span id="{fid}">&mdash;</span></div>'
        for fid, label in c["outputs"]
    )
    hid, hlabel = c["headline"]
    extra = ""
    if c.get("extra_out"):
        eid, _ = c["extra_out"]
        extra = (f'\n            <p class="calc-note" id="{eid}" '
                 f'style="color:rgba(255,255,255,.85);margin-top:14px;"></p>')

    calc_html = f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
            <h2>Run the Numbers</h2>
            <div class="calc">
                <div class="calc-row">
{fields}
                </div>
                <div class="calc-out">
                    <h3>Estimated Result</h3>
                    <div class="calc-lines">
{outs}
                        <div class="calc-line headline"><span>{hlabel}</span>
                        <span id="{hid}">&mdash;</span></div>
                    </div>{extra}
                </div>
                <p class="calc-note">{c['note']}</p>
            </div>
            <div class="center-cta" style="margin-top:22px;">
                <a href="/discovery/" class="btn-cta btn-lg">Get a Real Estimate for Your Property</a>
            </div>
        </div>
    </section>"""

    body = "\n\n".join([
        T.page_header(h1=c["h1"], subtitle=c["desc"],
                      trail=[("Home", "/"), ("Calculators", "/calculators/"), (c["title"], path)],
                      cta="Talk to a Tax Strategist"),
        f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
{T.definition(c['definition'])}
        </div>
    </section>""",
        calc_html,
        T.faq_section(c["faqs"]),
        T.related_section([
            ("/cost-segregation-study/", "Cost Segregation Study: How It Works"),
            ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026 Under the OBBBA"),
            ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
            ("/section-179-vs-bonus-depreciation-2026/", "Section 179 vs Bonus Depreciation"),
            ("/calculators/", "All Tax Calculators"),
            ("/pricing/", "Pricing"),
        ]),
    ])

    schemas = [
        {"@context": "https://schema.org", "@type": "WebApplication",
         "name": c["h1"], "url": url, "applicationCategory": "FinanceApplication",
         "operatingSystem": "Any", "browserRequirements": "Requires JavaScript",
         "description": c["desc"],
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "publisher": {"@type": "Organization", "name": T.BRAND}},
        T.faq_schema(c["faqs"]),
        T.breadcrumb_schema([("Home", "/"), ("Calculators", "/calculators/"), (c["title"], path)]),
    ]

    js = f"""
    <script>
    (function(){{
{c['js']}
      var ids = {[f[0] for f in c['form']]!r};
      ids.forEach(function(id){{
        var el = document.getElementById(id);
        if(el){{ el.addEventListener('input', calc); el.addEventListener('change', calc); }}
      }});
      calc();
    }})();
    </script>"""

    return T.build_page(
        title=c["title"] + " | AE Tax Advisors", description=c["desc"], path=path,
        body=body, schemas=schemas, published=PUBLISHED, modified=MODIFIED,
        extra_head=CALC_CSS,
    ).replace("</body>", js + "\n</body>")


def build_calc_index() -> str:
    existing = [
        ("/cost-segregation-calculator/", "Cost Segregation Calculator",
         "Original cost segregation estimator."),
        ("/tax-savings-calculator/", "Tax Savings Calculator",
         "General tax savings estimator across common strategies."),
    ]
    cards = "\n".join(
        f"""                <article class="cs-card">
                    <h3><a href="/{c['slug']}/">{T.esc(c['h1'])}</a></h3>
                    <p>{T.esc(c['desc'])}</p>
                    <a href="/{c['slug']}/" class="btn-secondary">Open Calculator</a>
                </article>"""
        for c in CALCULATORS
    ) + "\n" + "\n".join(
        f"""                <article class="cs-card">
                    <h3><a href="{href}">{T.esc(name)}</a></h3>
                    <p>{T.esc(d)}</p>
                    <a href="{href}" class="btn-secondary">Open Calculator</a>
                </article>"""
        for href, name, d in existing
        if (ROOT / href.strip("/") / "index.html").exists()
    )

    body = f"""    <section class="page-header">
        <div class="container">
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <a href="/">Home</a> &rsaquo; <span>Calculators</span>
            </nav>
            <h1>Tax Calculators</h1>
            <p class="subtitle">Free estimators for cost segregation, S-Corp elections, and
            depreciation decisions. Every one shows its assumptions.</p>
            <div class="cta-buttons">
                <a href="/discovery/" class="btn-cta btn-lg">Get a Real Estimate</a>
            </div>
        </div>
    </section>

    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="definition-lead">These calculators estimate outcomes using standard
            assumptions and typical ranges. They are useful for sizing a decision and are not
            a substitute for analysis of your specific facts, particularly the passive activity
            rules that determine whether a deduction is usable in the current year.</p>
        </div>
    </section>

    <section class="content-section fade-in-section">
        <div class="container">
            <h2>Available Calculators</h2>
            <div class="cs-grid">
{cards}
            </div>
        </div>
    </section>"""

    schemas = [
        {"@context": "https://schema.org", "@type": "CollectionPage",
         "name": "Tax Calculators", "url": f"{T.SITE}/calculators/",
         "description": "Free tax calculators for cost segregation, S-Corp elections, and depreciation.",
         "publisher": {"@type": "Organization", "name": T.BRAND}},
        T.breadcrumb_schema([("Home", "/"), ("Calculators", "/calculators/")]),
    ]
    return T.build_page(
        title="Tax Calculators | AE Tax Advisors",
        description=("Free tax calculators: cost segregation savings, S-Corp election savings, "
                     "and bonus depreciation versus Section 179 comparison."),
        path="/calculators/", body=body, schemas=schemas,
        published=PUBLISHED, modified=MODIFIED, og_type="website",
    )


def main() -> int:
    for c in CALCULATORS:
        html = build_calculator(c)
        out = T.write_page(c["slug"], html)
        print(f"calculator: {out.relative_to(ROOT)}")
    T.write_page("/calculators/", build_calc_index())
    print("calculator index: calculators/index.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
