#!/usr/bin/env python3
"""Shared machinery for the topic-cluster build.

A cluster is one pillar page plus its supporting posts, wired together so
every spoke links up to the pillar, the pillar links down to every spoke, and
siblings link across. That link geometry is the whole point of the structure,
so it is computed here from a single registry rather than hand-maintained in
each page's copy, where it would drift the moment a post is added.

Two kinds of spoke exist:

  NEW      a page this build writes.
  ADOPTED  a page the site already ranks for. The topic is already covered,
           so publishing a second page on it would split the equity between
           two URLs competing for one query. Instead the existing page is
           pulled into the cluster: it gets a link up to the pillar injected
           into it, and the pillar links down to it.

Everything is idempotent. Re-running rewrites generated pages in place and
re-injects backlinks only where they are missing.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import site_template as T

ROOT = Path(__file__).resolve().parent
PUBLISHED = "2026-08-17"
MODIFIED = "2026-08-17"


@dataclass
class Spoke:
    """One supporting post in a cluster."""

    slug: str
    label: str                 # anchor text used in cluster link lists
    adopted: bool = False      # True: page already exists, do not rewrite
    title: str = ""
    description: str = ""
    h1: str = ""
    subtitle: str = ""
    lead: str = ""             # definition paragraph, for AI overview capture
    keywords: list[str] = field(default_factory=list)
    body: list[tuple[str, str]] = field(default_factory=list)   # (H2, html)
    faqs: list[tuple[str, str]] = field(default_factory=list)
    takeaways: list[str] = field(default_factory=list)

    @property
    def href(self) -> str:
        return f"/{self.slug}/"


@dataclass
class Cluster:
    """A pillar page and the spokes that support it."""

    key: str
    slug: str
    label: str
    adopted_pillar: bool = False
    title: str = ""
    description: str = ""
    h1: str = ""
    subtitle: str = ""
    lead: str = ""
    keywords: list[str] = field(default_factory=list)
    body: list[tuple[str, str]] = field(default_factory=list)
    faqs: list[tuple[str, str]] = field(default_factory=list)
    takeaways: list[str] = field(default_factory=list)
    spokes: list[Spoke] = field(default_factory=list)

    @property
    def href(self) -> str:
        return f"/{self.slug}/"


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def _sections(body: list[tuple[str, str]]) -> str:
    return "\n".join(T.section(h, html) for h, html in body)


def _byline() -> str:
    return (
        '            <p class="post-meta">By AE Tax Advisors Team &middot; '
        f"Billings, Montana &middot; Updated {MODIFIED}</p>"
    )


def _lead_block(lead: str) -> str:
    return f"""    <section class="content-section fade-in-section">
        <div class="container narrow">
{_byline()}
{T.definition(lead)}
        </div>
    </section>"""


def render_pillar(c: Cluster, others: list[Cluster]) -> str:
    """Pillar page: lead, body, spoke hub, cross-cluster links, FAQ."""
    trail = [("Home", "/"), ("Guides", "/guides/"), (c.label, c.href)]

    spoke_links = [(s.href, s.label) for s in c.spokes]
    cross = [(o.href, o.label) for o in others if o.key != c.key]

    parts = [
        T.page_header(h1=c.h1, subtitle=c.subtitle, trail=trail),
        _lead_block(c.lead),
        _sections(c.body),
    ]
    if c.takeaways:
        parts.append(T.takeaways(c.takeaways))
    parts += [
        T.related_section(spoke_links, heading=f"{c.label}: The Full Guide Series"),
        T.faq_section(c.faqs),
        T.related_section(cross, heading="Other Tax Strategy Guides"),
    ]

    schemas = [
        T.article_schema(
            title=c.title,
            description=c.description,
            url=f"{T.SITE}{c.href}",
            published=PUBLISHED,
            modified=MODIFIED,
            section="Tax Strategy",
            keywords=c.keywords,
        ),
        T.faq_schema(c.faqs),
        T.breadcrumb_schema(trail),
    ]
    return T.build_page(
        title=c.title,
        description=c.description,
        path=c.href,
        body="\n".join(parts),
        schemas=schemas,
        published=PUBLISHED,
        modified=MODIFIED,
    )


def render_post(s: Spoke, c: Cluster) -> str:
    """Supporting post: lead, body, link up to pillar, links across siblings."""
    trail = [("Home", "/"), (c.label, c.href), (s.label, s.href)]

    siblings = [(o.href, o.label) for o in c.spokes if o.slug != s.slug][:6]

    parts = [
        T.page_header(h1=s.h1, subtitle=s.subtitle, trail=trail),
        _lead_block(s.lead),
        _sections(s.body),
    ]
    if s.takeaways:
        parts.append(T.takeaways(s.takeaways))
    parts.append(
        T.related_section(
            [(c.href, f"{c.label}: the complete guide")],
            heading="Start With the Pillar Guide",
        )
    )
    parts.append(T.faq_section(s.faqs))
    if siblings:
        parts.append(T.related_section(siblings, heading="More in This Series"))

    schemas = [
        T.article_schema(
            title=s.title,
            description=s.description,
            url=f"{T.SITE}{s.href}",
            published=PUBLISHED,
            modified=MODIFIED,
            section=c.label,
            keywords=s.keywords,
        ),
        T.faq_schema(s.faqs),
        T.breadcrumb_schema(trail),
    ]
    return T.build_page(
        title=s.title,
        description=s.description,
        path=s.href,
        body="\n".join(parts),
        schemas=schemas,
        published=PUBLISHED,
        modified=MODIFIED,
    )


# ---------------------------------------------------------------------------
# Backlink injection for adopted pages
# ---------------------------------------------------------------------------

MARKER = "cluster-pillar-link"


def backlink_block(c: Cluster) -> str:
    return f"""    <section class="content-section fade-in-section {MARKER}">
        <div class="container narrow">
            <h2>Part of Our {c.label} Guide</h2>
            <p>This article is one part of a larger strategy. For the full framework,
            including how this fits with the other moves available to a profitable
            business, read <a href="{c.href}">{c.h1}</a>.</p>
        </div>
    </section>"""


def inject_backlink(slug: str, c: Cluster) -> str:
    """Add a link up to the pillar on an already-published page."""
    path = ROOT / slug / "index.html"
    if not path.exists():
        return "missing"
    html = path.read_text(encoding="utf-8")
    if MARKER in html:
        # Already wired into a cluster; refresh the target in case it moved.
        return "present"
    if "</main>" not in html:
        return "no-main"
    html = html.replace("</main>", backlink_block(c) + "\n    </main>", 1)
    path.write_text(html, encoding="utf-8")
    return "injected"


HUB_MARKER = "cluster-spoke-hub"


def hub_block(c: Cluster) -> str:
    """The spoke list, for injecting into a pillar that already exists."""
    items = "\n".join(
        f'                <li><a href="{s.href}">{s.label}</a></li>' for s in c.spokes
    )
    return f"""    <section class="content-section fade-in-section {HUB_MARKER}">
        <div class="container narrow">
            <h2>{c.label}: The Full Guide Series</h2>
            <ul class="related-links">
{items}
            </ul>
        </div>
    </section>"""


def inject_hub(c: Cluster) -> str:
    """Wire an already-published pillar to its spokes.

    Rewritten in place on every run so newly added spokes appear without the
    block being duplicated.
    """
    path = ROOT / c.slug / "index.html"
    if not path.exists():
        return "missing"
    html = path.read_text(encoding="utf-8")
    block = hub_block(c)

    if HUB_MARKER in html:
        pattern = re.compile(
            r'    <section class="content-section fade-in-section '
            + re.escape(HUB_MARKER)
            + r'">.*?\n    </section>',
            re.S,
        )
        updated = pattern.sub(lambda _: block, html, count=1)
        if updated == html:
            return "present"
        path.write_text(updated, encoding="utf-8")
        return "refreshed"

    if "</main>" not in html:
        return "no-main"
    path.write_text(html.replace("</main>", block + "\n    </main>", 1), encoding="utf-8")
    return "injected"


def word_count(c_or_s) -> int:
    text = " ".join(html for _, html in c_or_s.body)
    text += " " + c_or_s.lead
    text += " " + " ".join(f"{q} {a}" for q, a in c_or_s.faqs)
    text += " " + " ".join(getattr(c_or_s, "takeaways", []))
    return len(T.strip_tags(text).split())
