#!/usr/bin/env python3
"""Rewrite the team bios on /bios/, and remove departed members.

The page is hand-maintained HTML, so this rewrites the content block of each
card in place rather than regenerating the page. Card markup, image tags and
ordering are left untouched.

Bios are 2-3 sentences, written around what the person does for clients.
Hard facts that belong to a real person (licences, degrees, prior firms) are
preserved rather than invented or dropped, and the affiliated-partner legal
disclosures are carried through verbatim.

Idempotent: re-running produces the same file.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGE = ROOT / "bios" / "index.html"

REMOVE = ["Miguel Gonzales"]

# name -> (title, [paragraph html, ...])
BIOS: dict[str, tuple[str, list[str]]] = {
    "Christina Nortman, CPA": (
        "Managing Partner, Northeast Region",
        [
            "Christina leads the firm's Northeast practice from Maryland, bringing Big "
            "Four discipline from PwC and CohnReznick to owner-operated businesses. She "
            "works with high-income business owners and real estate investors who have "
            "outgrown reactive tax preparation and want the strategy designed before the "
            "year closes.",
            "<strong>Background:</strong> Bachelor's and Master of Science in Accounting, "
            "University of Baltimore.",
        ],
    ),
    "Mark Simonsen, CPA": (
        "Founding Principal, Mountain West Region",
        [
            "Mark founded the firm's Mountain West practice and works from Montana with "
            "deep roots in the local business community. He builds advanced tax strategy "
            "for business owners, real estate investors, and entrepreneurs whose "
            "situations have outgrown a standard compliance relationship.",
            "<strong>Specialty:</strong> Advanced tax strategy and entity structuring for "
            "business owners and real estate investors.",
        ],
    ),
    "Adam West, EA": (
        "Resolution and Compliance, Southeast Region",
        [
            "Adam leads the Southeast practice from Macon, Georgia, where he is also a "
            "partner at Gonser, West &amp; Associates. As an Enrolled Agent he handles tax "
            "compliance and IRS representation, pairing local accessibility with "
            "national-caliber planning.",
            "<strong>Services:</strong> Accounting, consulting, tax compliance, and IRS "
            "representation.",
        ],
    ),
    "Sidhartha Sen": (
        "Strategic Advisory",
        [
            "Sidhartha advises on finance, operations, and business development, "
            "structuring the complex financial arrangements that advanced tax planning "
            "often depends on. He works across the firm's growth initiatives and with "
            "clients whose situations span several entities.",
            "<strong>Focus:</strong> Financial strategy, operations, and growth "
            "initiatives.",
        ],
    ),
    "Jacques Snyman": (
        "Head of Operations and Integration",
        [
            "Jacques runs the operational systems behind every engagement, from intake "
            "through delivery. His work is the reason a client's experience stays "
            "consistent regardless of which advisor or region is handling the file.",
            "<strong>Focus:</strong> Operations, systems infrastructure, and client "
            "experience.",
        ],
    ),
    "Avatar Tripathi": (
        "Head of Social Media",
        [
            "Avatar leads the firm's digital presence and thought leadership, turning "
            "technical tax strategy into material business owners will actually read. He "
            "manages content strategy and engagement across every platform the firm "
            "publishes on.",
            "<strong>Focus:</strong> Content strategy, digital marketing, and community "
            "engagement.",
        ],
    ),
    "Ashik Zaman": (
        "Head of Development &amp; Technology",
        [
            "Ashik builds and maintains the technical infrastructure behind the firm's "
            "planning, compliance, and client portal systems. His work keeps client "
            "documents secure and the advisory team's tooling fast enough to model "
            "strategy while a client is still on the call.",
            "<strong>Focus:</strong> Platform development, technology infrastructure, and "
            "data security.",
        ],
    ),
    "Alicia Orellana": (
        "Director of Operations",
        [
            "Alicia owns client onboarding, coordinating document collection, scheduling, "
            "and communication from first contact through implementation. She also works "
            "with the advisory team to research and refine the less conventional planning "
            "approaches that unusual situations call for.",
            "<strong>Focus:</strong> Client onboarding, engagement coordination, and "
            "alternative strategy research.",
        ],
    ),
    "James Rollan Rosales": (
        "Executive Assistant",
        [
            "Executive Assistant at AE Tax Advisors focused on administrative execution, "
            "operational support, and internal organization, enabling leadership to focus "
            "on sales, client relationships, and fulfillment.",
        ],
    ),
    "Krister Myrlonn, EA": (
        "Tax Associate",
        [
            "Krister is an Enrolled Agent licensed by the IRS, working on entity "
            "structuring, cost segregation analysis, and tax optimization for high-income "
            "business owners and real estate investors. He is based at the firm's "
            "Billings, Montana headquarters.",
            "<strong>Background:</strong> Montana State University Billings.",
        ],
    ),
    "Jem Elizshel Alcantara": (
        "Administrative Associate",
        [
            "Jem supports daily operations, client onboarding, and communications, and is "
            "often the person keeping an engagement moving between milestones. Her work "
            "makes sure nothing stalls between a client's first contact and the delivered "
            "plan.",
            "<strong>Focus:</strong> Operations, onboarding, and client communications.",
        ],
    ),
    "Jacob Simany, Esq.": (
        "Tax Attorney",
        [
            "Jacob is a tax attorney, former IRS Office of Chief Counsel litigator, and "
            "founder of Simany Law. He advises clients on tax controversy and IRS dispute "
            "resolution, drawing on insider experience with how the IRS actually develops, "
            "negotiates, and settles cases.",
            "<strong>Advisory Focus:</strong> Tax controversy and litigation, IRS dispute "
            "resolution, succession and estate planning.",
        ],
    ),
    "Michael A. Zara, Esq.": (
        "Business Attorney",
        [
            "Mike is a business attorney with nearly two decades of experience and a "
            "background in accounting, which lets him read a transaction financially and "
            "legally at the same time. He advises clients on entity structuring, business "
            "formation, contracts, mergers and acquisitions, and corporate governance.",
            "<strong>Background:</strong> J.D., University of Denver Sturm College of Law; "
            "B.S. in Accounting, Arizona State University. Licensed in Colorado, Arizona, "
            "Georgia, and North Carolina.",
        ],
    ),
    "Scott Nortman": (
        "Qualified Mortgage Lending Specialist, Third Party",
        [
            "Scott is an affiliated mortgage lending partner specializing in investment "
            "property financing, portfolio lending, and DSCR loans. He helps clients "
            "secure the financing behind short-term rental acquisitions and real estate "
            "portfolio expansion.",
            "<strong>Third-Party Disclosure:</strong> As a third-party lending specialist, "
            "Scott operates independently of AE Tax Advisors and provides his own "
            "representations and warranties on all mortgage products and services.",
        ],
    ),
}


def _match_div(html: str, start: int) -> int:
    """Index just past the </div> closing the <div> that starts at `start`."""
    depth, i = 0, start
    tag = re.compile(r"<(/?)div\b", re.I)
    while i < len(html):
        m = tag.search(html, i)
        if not m:
            return -1
        depth += -1 if m.group(1) else 1
        i = m.end()
        if depth == 0:
            close = html.find(">", i)
            return close + 1 if close != -1 else -1
    return -1


def remove_member(html: str, name: str) -> tuple[str, bool]:
    """Delete a whole team-member card, and its preceding HTML comment."""
    m = re.search(rf"<h2>\s*{re.escape(name)}\s*</h2>", html)
    if not m:
        return html, False
    card = html.rfind('<div class="team-member">', 0, m.start())
    if card == -1:
        return html, False
    end = _match_div(html, card)
    if end == -1:
        return html, False

    start = card
    # Take the "<!-- Name -->" comment above the card with it.
    before = html[:card]
    cm = re.search(r"[ \t]*<!--[^>]*-->\s*\Z", before)
    if cm:
        start = cm.start()
    while end < len(html) and html[end] in "\r\n":
        end += 1
    return html[:start] + html[end:], True


def content_block(name: str, title: str, paras: list[str], indent: str) -> str:
    lines = [f'{indent}<div class="team-member-content">',
             f"{indent}    <h2>{name}</h2>",
             f'{indent}    <div class="team-member-title">{title}</div>']
    for i, p in enumerate(paras):
        style = ' style="margin-top: 12px;"' if i else ""
        lines.append(f"{indent}    <p{style}>{p}</p>")
    lines.append(f"{indent}</div>")
    return "\n".join(lines)


def rewrite_member(html: str, name: str, title: str, paras: list[str]) -> tuple[str, bool]:
    m = re.search(rf"<h2>\s*{re.escape(name)}\s*</h2>", html)
    if not m:
        return html, False
    blk = html.rfind('<div class="team-member-content">', 0, m.start())
    if blk == -1:
        return html, False
    end = _match_div(html, blk)
    if end == -1:
        return html, False
    line_start = html.rfind("\n", 0, blk) + 1
    indent = html[line_start:blk]
    return html[:blk] + content_block(name, title, paras, indent).lstrip() + html[end:], True


def main() -> int:
    html = PAGE.read_text(encoding="utf-8")
    before = html
    problems = []

    for name in REMOVE:
        html, ok = remove_member(html, name)
        print(f"removed {name}: {'yes' if ok else 'NOT FOUND (already gone?)'}")

    n = 0
    for name, (title, paras) in BIOS.items():
        html, ok = rewrite_member(html, name, title, paras)
        if ok:
            n += 1
        else:
            problems.append(name)

    PAGE.write_text(html, encoding="utf-8")
    print(f"bios rewritten: {n}/{len(BIOS)}")
    if problems:
        print("NOT FOUND:", ", ".join(problems))
        return 1
    print("changed" if html != before else "no change")
    return 0


if __name__ == "__main__":
    sys.exit(main())
