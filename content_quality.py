#!/usr/bin/env python3
"""Editorial SEO gate for every canonical, indexable page.

This complements seo_validate.py by checking the quality leaks that are most
likely to make a large site look mechanically produced: broken currency,
sentence-fragment snippets, duplicate indexable titles, very thin pages, and
sitemap/canonical drift.
"""

from __future__ import annotations

import html
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://www.aetaxadvisors.com"
NOINDEX = re.compile(r'<meta name="robots" content="[^"]*noindex', re.I)
CANON = re.compile(r'<link rel="canonical" href="https://(?:www\.)?aetaxadvisors\.com([^"]*)"')
TITLE = re.compile(r'<title>(.*?)</title>', re.S)
DESC = re.compile(r'<meta name="description" content="([^"]*)"', re.S)
DANGLING = {
    "a", "an", "the", "and", "or", "but", "of", "to", "in", "on", "at", "by",
    "for", "from", "with", "without", "that", "which", "as", "when", "while",
}
BOOKING = re.compile(
    r'https://(?:api\.leadconnectorhq\.com|link\.aetaxadvisors\.com)'
    r'/widget/booking/([A-Za-z0-9_-]+)'
)
PARAGRAPH = re.compile(r'<p\b[^>]*>(.*?)</p>', re.I | re.S)
BUTTON_LINK = re.compile(
    r'<a\b(?=[^>]*(?:\bclass=["\'][^"\']*\b(?:btn-cta|btn-primary|button)\b'
    r'|\bstyle=["\'][^"\']*(?:display\s*:\s*inline-block|background\s*:)))'
    r'[^>]*>.*?</a>', re.I | re.S
)
DISCOVERY_BOOKING_ID = "FggCeBoxIuOuZZrTaVV1"
# These are purpose-built appointment routes, not sitewide marketing CTAs.
SPECIALIZED_BOOKING_PAGES = {
    "/30-minute-consultation/",
    "/45-minute-consultation/",
    "/60-minute-consultation/",
    "/alicia-30min/",
    "/alicia-45min/",
    "/alicia-60min/",
    "/alicia-survey/",
    "/ashley-30min/",
    "/ashley-45min/",
    "/ashley-60min/",
    "/christina-30min/",
    "/christina-45min/",
    "/christina-60min/",
    "/connor-1-1/",
    "/execupgrades/",
    "/onboarding/",
    "/q4-planning-call/",
}


def page_url(path: Path) -> str:
    rel = path.parent.relative_to(ROOT).as_posix()
    return "/" if rel == "." else f"/{rel}/"


def visible_words(markup: str) -> int:
    main = re.search(r'<main[^>]*>(.*?)</main>', markup, re.I | re.S)
    scope = main.group(1) if main else markup
    scope = re.sub(r'<(?:script|style)[^>]*>.*?</(?:script|style)>', ' ', scope, flags=re.I | re.S)
    return len(re.findall(r"\b[\w'-]+\b", html.unescape(re.sub(r'<[^>]+>', ' ', scope))))


def main() -> int:
    sitemap = set(re.findall(r'<loc>' + re.escape(SITE) + r'([^<]*)</loc>',
                             (ROOT / 'sitemap.xml').read_text()))
    titles: dict[str, list[str]] = defaultdict(list)
    errors: list[str] = []
    warnings: list[str] = []
    indexable: set[str] = set()
    try:
        config = json.loads((ROOT / 'vercel.json').read_text())
        redirects = {
            rule['source'] for rule in config.get('redirects', [])
            if rule.get('statusCode') in (301, 308)
            and isinstance(rule.get('source'), str)
            and ':' not in rule['source']
        }
    except (OSError, json.JSONDecodeError):
        redirects = set()

    for path in sorted(ROOT.rglob('index.html')):
        if '.git' in path.parts:
            continue
        text = path.read_text(encoding='utf-8', errors='replace')
        url = page_url(path)
        booking_ids = set(BOOKING.findall(text))
        if url not in SPECIALIZED_BOOKING_PAGES:
            for booking_id in sorted(booking_ids - {DISCOVERY_BOOKING_ID}):
                errors.append(
                    f'{path.relative_to(ROOT).as_posix()}: marketing CTA uses '
                    f'non-discovery booking calendar {booking_id}'
                )
        cm = CANON.search(text)
        canonical = cm.group(1) if cm else None
        if NOINDEX.search(text) or (canonical and canonical != url) or url in redirects:
            continue
        indexable.add(url)
        label = path.relative_to(ROOT).as_posix()

        if '$$' in text:
            errors.append(f'{label}: doubled currency symbol')
        tm = TITLE.search(text)
        if tm:
            titles[html.unescape(tm.group(1)).strip()].append(label)
        dm = DESC.search(text)
        if not dm:
            errors.append(f'{label}: missing meta description')
        else:
            desc = html.unescape(dm.group(1)).strip()
            ending = re.search(r'\b(' + '|'.join(sorted(DANGLING, key=len, reverse=True))
                               + r')\W*$', desc, re.I)
            if len(desc) >= 105 and ending:
                errors.append(f'{label}: unfinished meta description ({ending.group(1)})')
            if len(desc) > 170:
                warnings.append(f'{label}: meta description is {len(desc)} characters')

        count = visible_words(text)
        if count < 250 and not url.startswith(('/discovery/', '/contact/')):
            warnings.append(f'{label}: thin indexable page ({count} words)')

    # Standalone .html articles are also published, even though sitemap parity
    # above uses directory index.html pages. Check every HTML document so a
    # booking button cannot split prose on either route format.
    html_pages_checked = 0
    for path in sorted(ROOT.rglob('*.html')):
        if '.git' in path.parts:
            continue
        html_pages_checked += 1
        text = path.read_text(encoding='utf-8', errors='replace')
        main_markup = re.search(r'<main\b[^>]*>(.*?)</main>', text, re.I | re.S)
        body_markup = main_markup.group(1) if main_markup else text
        for paragraph in PARAGRAPH.finditer(body_markup):
            if not BUTTON_LINK.search(paragraph.group(1)):
                continue
            surrounding = BUTTON_LINK.sub('', paragraph.group(1))
            surrounding = html.unescape(re.sub(r'<[^>]+>', ' ', surrounding)).strip()
            if surrounding:
                label = path.relative_to(ROOT).as_posix()
                errors.append(f'{label}: button CTA embedded in paragraph text')
                break

    for title, paths in titles.items():
        if len(paths) > 1:
            errors.append(f'duplicate indexable title: {title} :: {", ".join(paths)}')

    for path in sorted((ROOT / 'scripts').rglob('*.py')):
        text = path.read_text(encoding='utf-8', errors='replace')
        for booking_id in sorted(set(BOOKING.findall(text)) - {DISCOVERY_BOOKING_ID}):
            errors.append(
                f'{path.relative_to(ROOT).as_posix()}: page generator uses '
                f'non-discovery booking calendar {booking_id}'
            )

    for url in sorted(indexable - sitemap):
        errors.append(f'{url}: canonical indexable URL missing from sitemap.xml')
    for url in sorted(sitemap - indexable):
        errors.append(f'{url}: sitemap URL is not canonical and indexable')

    print(f'canonical indexable pages: {len(indexable)}')
    print(f'sitemap URLs:              {len(sitemap)}')
    print(f'HTML pages CTA-scanned:    {html_pages_checked}')
    print(f'errors:                    {len(errors)}')
    for item in errors[:40]:
        print(f'  ERROR {item}')
    print(f'warnings:                  {len(warnings)}')
    for item in warnings[:30]:
        print(f'  WARN  {item}')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
