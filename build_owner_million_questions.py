#!/usr/bin/env python3
"""Editorial mapping of 100 owner questions to existing and new distinct articles."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

import site_template as T

ROOT = Path(__file__).resolve().parent
DATE = "2026-09-26"
HUB = "/guides/million-profit-business-owner-tax-questions/"
START = "<!-- million-owner-answer:start -->"
END = "<!-- million-owner-answer:end -->"
GROUPS = [
    "Tax bill and entity choice", "S corporation pay and distributions",
    "QBI and deductions", "Estimated taxes and cash flow",
    "Retirement and benefits", "Equipment and depreciation",
    "Real estate and cost segregation", "Owner expenses and family planning",
    "State taxes and multiple entities", "Sale, amendments, and audit exposure",
]
SOURCES = [
    "https://www.irs.gov/businesses/small-businesses-self-employed/s-corporations",
    "https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues",
    "https://www.irs.gov/instructions/i8995a",
    "https://www.irs.gov/faqs/estimated-tax",
    "https://www.irs.gov/publications/p560",
    "https://www.irs.gov/publications/p946",
    "https://www.irs.gov/publications/p925",
    "https://www.irs.gov/publications/p463",
    "https://www.irs.gov/newsroom/qualified-business-income-deduction",
    "https://www.irs.gov/publications/p537",
]
OVERRIDES = {
    1: "https://www.irs.gov/publications/p334",
    18: "https://www.irs.gov/publications/p15",
    20: "https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis",
    32: "https://www.irs.gov/faqs/estimated-tax",
    34: "https://www.irs.gov/instructions/i2210",
    38: "https://www.irs.gov/payments/payment-plans-installment-agreements",
    47: "https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues",
    58: "https://www.irs.gov/newsroom/working-families-tax-cuts",
    61: "https://www.irs.gov/publications/p925",
    67: "https://www.irs.gov/instructions/i3115",
    68: "https://www.irs.gov/publications/p925",
    69: "https://www.irs.gov/publications/p925",
    71: "https://www.irs.gov/publications/p15",
    75: "https://www.irs.gov/publications/p463",
    79: "https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-stock-and-debt-basis",
    81: "https://www.irs.gov/pub/irs-drop/n-20-75.pdf",
    82: "https://www.irs.gov/pub/irs-drop/n-20-75.pdf",
    83: "https://www.pa.gov/agencies/revenue",
    84: "https://www.pa.gov/agencies/revenue",
    85: "https://www.pa.gov/agencies/revenue",
    90: "https://www.irs.gov/publications/p542",
    93: "https://www.irs.gov/instructions/i1040sd",
    95: "https://www.irs.gov/publications/p537",
    97: "https://www.irs.gov/instructions/i3115",
}
SHORT_TITLES = {
    1: "$1 Million Business Profit: How Much Tax? | AE Tax",
    27: "Does Hiring Employees Increase QBI? | AE Tax",
    29: "Rental QBI Alongside a Business | AE Tax",
    30: "S Corp Salary and the QBI Tradeoff | AE Tax",
    32: "110% Estimated Tax Safe Harbor for Owners | AE Tax",
    33: "When Business Profit Doubles Midyear | AE Tax",
    34: "Year-End Payroll Withholding and Estimated Tax | AE Tax",
    35: "S Corp Estimated Tax: Owner or Company? | AE Tax",
    36: "Why Business Profit Can Exceed Cash | AE Tax",
    37: "Owner Draws Versus Business Expenses | AE Tax",
    38: "IRS Payment Plan for a Business Tax Bill | AE Tax",
    40: "Tax Planning After Year-End | AE Tax",
    46: "Retirement Plans for a Business With Employees | AE Tax",
    50: "Retirement Plan Before a Business Sale | AE Tax",
    52: "Equipment Paid in December, Delivered in January | AE Tax",
    58: "2026 Software Development Tax Costs | AE Tax",
    75: "Family Travel and Business Deductions | AE Tax",
    76: "Hiring a Spouse: Pay and Retirement | AE Tax",
    82: "S Corp State Tax and PTET Elections | AE Tax",
    83: "Pennsylvania Owner With Multistate Clients | AE Tax",
    84: "Remote Employees and State Tax Nexus | AE Tax",
    85: "Moving a Business to Florida: State Tax | AE Tax",
    90: "Related-Party Business Tax Reporting | AE Tax",
    98: "Records for Large Business Tax Deductions | AE Tax",
}


def esc(x: str) -> str:
    return html.escape(x, quote=True)


def records() -> list[dict]:
    questions = (ROOT / "owner_million_questions.txt").read_text().splitlines()
    answers = (ROOT / "owner_million_answers.txt").read_text().splitlines()
    targets = (ROOT / "owner_million_targets.txt").read_text().splitlines()
    assert len(questions) == len(answers) == len(targets) == 100
    assert len(set(targets)) == 100, "Each question needs its own article"
    return [dict(id=i+1, question=q, answer=a, slug=s,
                 url=f"/blog/{s}/", group=GROUPS[i//10],
                 source=OVERRIDES.get(i+1, SOURCES[i//10]))
            for i, (q, a, s) in enumerate(zip(questions, answers, targets))]


def examples() -> dict[int, tuple[str, str, str]]:
    result = {}
    for line in (ROOT / "owner_million_new_examples.txt").read_text().splitlines():
        number, scenario, records, caution = line.split("|", 3)
        result[int(number)] = scenario, records, caution
    return result


def depth() -> dict[int, str]:
    result = {}
    for line in (ROOT / "owner_million_new_depth.txt").read_text().splitlines():
        number, paragraph = line.split("|", 1)
        result[int(number)] = paragraph
    return result


def module(r: dict, neighbors: list[dict]) -> str:
    source = r["source"]
    links = " ".join(f'<a href="{n["url"]}">{esc(n["question"])}</a>' for n in neighbors)
    return (f'{START}<section class="content-section fade-in-section" id="million-owner-answer-{r["id"]}">'
            f'<div class="container" style="max-width:850px">'
            f'<h2>{esc(r["question"])}</h2><p>{esc(r["answer"])}</p>'
            f'<p>For the underlying rules, see <a href="{esc(source)}">the official tax guidance</a>. '
            f'The relevant tax year, entity documents, actual transactions, and state filings determine the result.</p>'
            f'<p>Continue with {links}, or <a href="{HUB}">browse the full owner question guide</a>.</p>'
            f'<p><a href="/discovery/">Book a Call</a> to work through your actual figures and records.</p>'
            f'</div></section>{END}')


def main() -> None:
    rows = records()
    details = examples()
    assert set(details) == set(depth()), "Every new article needs a distinct second analysis"
    assert all((ROOT / r["url"].strip("/") / "index.html").exists() or r["id"] in details for r in rows)
    for r in rows:
        i = r["id"]-1
        neighbors = [rows[10*(i//10)+(i+1)%10], rows[10*(i//10)+(i+2)%10]]
        path = ROOT / r["url"].strip("/") / "index.html"
        addition = module(r, neighbors)
        if i+1 not in details:
            page = path.read_text()
            page = re.sub(re.escape(START)+r".*?"+re.escape(END), "", page, flags=re.S)
            assert '</main>' in page, path
            page = page.replace('</main>', addition+'\n</main>', 1)
            page = re.sub(r'(?m)(?:^[ \t]*\n)+(?='+re.escape(START)+')', '\n', page)
            path.write_text(page)
        else:
            scenario, records_text, caution = details[i+1]
            title = r["question"]
            trail = [("Home", "/"), ("Owner tax questions", HUB), (title, r["url"])]
            intro = ('This guide addresses a specific decision for a U.S. business owner '
                     'with roughly $1 million in annual profit. The amount of profit is a '
                     'planning scenario, not a shortcut to a tax answer.')
            body = T.page_header(h1=esc(title), subtitle="A practical owner tax decision", trail=trail, cta="Book a Call")
            body += T.section("The direct answer", f'<p>{esc(r["answer"])}</p>')
            body += T.section("Work through the facts", f'<p>{esc(scenario)}</p><p>{esc(depth()[i+1])}</p><p>{esc(caution)}</p>')
            body += T.section("Records to prepare", f'<p>{esc(records_text)}</p><p>Compare the available choices on the same set of facts, including current-year tax, later-year effects and administrative cost. A hypothetical illustration is not a filed client result or a promised tax saving.</p>')
            body += T.section("Related decisions", '<ul>'+''.join(f'<li><a href="{x["url"]}">{esc(x["question"])}</a></li>' for x in neighbors)+'</ul>')
            body += T.section("Primary reference and next step", f'<p><a href="{esc(r["source"])}">Review the official guidance</a> for the relevant tax year. The entity documents, complete return, actual transactions and applicable state rules should be checked before implementation.</p><p><a href="{HUB}">Explore the 100 owner tax questions</a> or <a href="/discovery/">Book a Call</a>.</p>')
            desc = title.rstrip('?') + ': answer, decision factors, example and records for business owners.'
            page = T.build_page(title=SHORT_TITLES[i+1], description=desc[:165], path=r["url"], body=body,
                schemas=[T.article_schema(title=title, description=desc, url=T.SITE+r["url"], published=DATE,
                                          modified=DATE, section=r["group"], citations=[r["source"]]),
                         T.breadcrumb_schema(trail)], published=DATE, modified=DATE)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(page)
    trail = [("Home", "/"), ("Owner tax questions", HUB)]
    body = T.page_header(h1="100 Tax Questions for Owners Earning $1 Million in Profit",
        subtitle="Direct answers and detailed articles on entity choice, owner pay, deductions, real estate and exits.",
        trail=trail, cta="Book a Call")
    body += T.section("How to use this guide", '<p>These are editorial questions for U.S. business owners, not a measured ranking of Google search volume. Each question links to a distinct article with the relevant decision, records and tax rules. Start with your entity, income and cash-flow facts; an assumed $1 million profit does not establish a deduction or a specific tax rate.</p>')
    for group in GROUPS:
        group_rows = [r for r in rows if r["group"] == group]
        body += T.section(group, '<ol start="'+str(group_rows[0]["id"])+ '">'+''.join(
            f'<li><a href="{r["url"]}">{esc(r["question"])}</a></li>' for r in group_rows)+'</ol>')
    body += T.section("Plan with your actual numbers", '<p>Bring prior returns, current financials, payroll, ownership documents, and asset records. <a href="/discovery/">Book a Call</a> with AE Tax Advisors to review the next decision.</p>')
    desc = "100 practical tax questions for business owners earning about $1 million in annual profit, with articles on entities, owner pay, QBI, real estate, state tax and exits."
    hub = T.build_page(title="100 Tax Questions for $1 Million Profit Business Owners | AE Tax",
        description=desc, path=HUB, body=body, schemas=[T.breadcrumb_schema(trail)],
        published=DATE, modified=DATE)
    dest = ROOT / HUB.strip('/') / 'index.html'; dest.parent.mkdir(parents=True, exist_ok=True); dest.write_text(hub)
    (ROOT / 'owner_million_manifest.json').write_text(json.dumps(rows, indent=2)+'\n')
    print(f"Mapped {len(rows)} distinct articles; {len(details)} new guides; expanded {len(rows)-len(details)} existing")


if __name__ == "__main__":
    main()
