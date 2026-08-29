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

# The page previously used a full-width alternating layout: one member per row,
# photo left then right, 350px portraits, 60px gaps and a rule between each.
# Fourteen people that way is an extremely long page with a visual rhythm that
# changes every row. This replaces it with one uniform card grid: circular
# headshots at a single size, equal-height cards, and a tight gutter.
STYLE = """
    /* Team page: uniform card grid. */
    .team-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 26px;
        margin: 36px auto 0;
        max-width: 1140px;
    }

    .team-member {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        height: 100%;
        background: var(--white);
        border: 1px solid rgba(27, 42, 74, 0.09);
        border-radius: 14px;
        padding: 34px 26px 30px;
        box-shadow: 0 1px 3px rgba(27, 42, 74, 0.05);
        transition: box-shadow 0.25s ease, transform 0.25s ease,
                    border-color 0.25s ease;
    }
    .team-member:hover {
        box-shadow: 0 10px 30px rgba(27, 42, 74, 0.10);
        border-color: rgba(197, 165, 90, 0.45);
        transform: translateY(-3px);
    }

    /* Fixed circle so every headshot presents identically regardless of the
       source image's aspect ratio. */
    .team-member-image {
        width: 128px;
        height: 128px;
        flex: 0 0 128px;
        border-radius: 50%;
        overflow: hidden;
        margin-bottom: 18px;
        background: var(--primary);
        box-shadow: 0 0 0 1px rgba(27, 42, 74, 0.10),
                    0 0 0 5px rgba(197, 165, 90, 0.14);
    }
    .team-member-image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center 22%;
        border-radius: 50%;
        display: block;
    }

    .team-member-content {
        display: flex;
        flex-direction: column;
        flex: 1 1 auto;
        width: 100%;
    }

    .team-member h2 {
        font-family: var(--font-heading);
        font-size: 19.5px;
        font-weight: 700;
        line-height: 1.3;
        color: var(--primary);
        margin: 0 0 5px;
        text-align: center;
    }
    .team-member-title {
        color: var(--accent);
        font-weight: 600;
        font-size: 11.5px;
        text-transform: uppercase;
        letter-spacing: 0.09em;
        line-height: 1.45;
        margin-bottom: 14px;
        min-height: 2.9em;      /* keeps one and two line titles aligned */
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .team-member p {
        font-size: 14.5px;
        line-height: 1.62;
        color: #555;
        margin: 0;
        text-align: center;
    }
    .team-member p + p {
        margin-top: 10px;
        font-size: 13.5px;
        color: #6b7280;
    }

    .team-member-links {
        margin-top: auto;
        padding-top: 18px;
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        justify-content: center;
    }
    .team-member-links a {
        font-size: 12.5px;
        font-weight: 600;
        padding: 9px 16px;
        border-radius: 6px;
        transition: all 0.2s ease;
    }

    .board-heading {
        font-family: var(--font-heading);
        font-size: 30px;
        font-weight: 700;
        color: var(--primary);
        text-align: center;
        margin-bottom: 10px;
    }

    @media (max-width: 1024px) {
        .team-grid { grid-template-columns: repeat(2, 1fr); gap: 22px; }
    }
    @media (max-width: 640px) {
        .team-grid { grid-template-columns: 1fr; gap: 18px; max-width: 460px; }
        .team-member { padding: 30px 22px 26px; }
        .team-member-image {
            width: 112px; height: 112px; flex-basis: 112px;
        }
        .team-member h2 { font-size: 18.5px; }
        .team-member-title { min-height: 0; margin-bottom: 12px; }
        .team-member p { font-size: 14px; }
        .board-heading { font-size: 25px; }
    }
"""

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
    "Jesse Gibson": (
        "Chief Revenue Officer",
        [
            "Jesse leads revenue strategy and client acquisition across AE Tax Advisors "
            "and its partner brands. He brings over a decade of experience scaling "
            "professional services firms, building high-performance sales teams, and "
            "designing the systems that turn qualified prospects into long-term advisory "
            "clients. His background spans business development, strategic partnerships, "
            "and go-to-market execution in financial services and real estate. At AE Tax, "
            "Jesse owns the full revenue pipeline from first touch through signed "
            "engagement, working directly with the advisory team to make sure every "
            "client relationship starts with the right expectations and ends with "
            "measurable results.",
            "<strong>Focus:</strong> Revenue strategy, client acquisition, and sales "
            "operations.",
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


STYLE_BLOCK = re.compile(r"(<style[^>]*>)(.*?)(</style>)", re.S)


def apply_style(html: str) -> tuple[str, bool]:
    """Swap the page's inline style block for the card-grid layout."""
    m = STYLE_BLOCK.search(html)
    if not m:
        return html, False
    if m.group(2).strip() == STYLE.strip():
        return html, False
    return html[: m.start(2)] + STYLE + html[m.end(2) :], True


def main() -> int:
    html = PAGE.read_text(encoding="utf-8")
    before = html
    problems = []

    html, styled = apply_style(html)
    print(f"layout css: {'updated' if styled else 'already current'}")

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
