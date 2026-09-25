#!/usr/bin/env python3
"""Replace oversized inline booking widgets with a compact discovery CTA.

Appointment pages keep their calendars. This is intentionally idempotent so a
later content refresh can run the cleanup again without changing other markup.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WIDGET = re.compile(
    r'<iframe\b[^>]*src="https://api\.leadconnectorhq\.com/widget/booking/[^\"]+"[^>]*>\s*</iframe>',
    re.I | re.S,
)
PANEL = re.compile(
    r'\s*<div class="booking-panel">\s*<h3>Book a Free Discovery Call</h3>.*?</div>',
    re.I | re.S,
)
CALENDAR_WRAP = re.compile(
    r'<div id="ghl-calendar"[^>]*>\s*'
    r'<iframe\b[^>]*src="https://api\.leadconnectorhq\.com/widget/booking/[^\"]+"[^>]*>\s*</iframe>'
    r'\s*</div>',
    re.I | re.S,
)
CTA = '<a class="btn-cta" href="/discovery/">Choose a Time to Talk With AE Tax</a>'
CARD = '<div style="background: #f0f4ff; border-left: 4px solid #2563eb;'
PHONE_LINE = re.compile(
    r'\s*<p style="margin-top:18px;margin-bottom:0;font-size:15px;">Prefer to talk first\?.*?</p>',
    re.I | re.S,
)
APPOINTMENT_SLUGS = {
    '30-minute-consultation', '45-minute-consultation', '60-minute-consultation',
    'alicia-30min', 'alicia-45min', 'alicia-60min', 'alicia-survey',
    'ashley-30min', 'ashley-45min', 'ashley-60min',
    'christina-30min', 'christina-45min', 'christina-60min',
    'connor-1-1', 'discovery', 'execupgrades', 'onboarding', 'q4-planning-call',
}


def main() -> None:
    changed = 0
    removed = 0
    for path in ROOT.rglob('index.html'):
        if '.git' in path.parts or path.parent.name in APPOINTMENT_SLUGS:
            continue
        source = path.read_text(encoding='utf-8', errors='replace')
        updated, panels = PANEL.subn('', source)
        updated, wraps = CALENDAR_WRAP.subn(CTA, updated)
        updated, embeds = WIDGET.subn(CTA, updated)
        if panels or wraps or embeds:
            updated = updated.replace('Pick a time below.', 'Choose a time on our booking page.')
            updated = updated.replace('pick a time below.', 'choose a time on our booking page.')
            updated = updated.replace('calendar below', 'booking page')
        if CTA in updated:
            updated = updated.replace(CARD, '<div class="compact-booking-cta" style="color:#1f2937;background: #f0f4ff; border-left: 4px solid #2563eb;')
            updated = updated.replace(
                '<div class="compact-booking-cta" style="background: #f0f4ff;',
                '<div class="compact-booking-cta" style="color:#1f2937;background: #f0f4ff;',
            )
            updated = PHONE_LINE.sub('', updated)
        if updated != source:
            path.write_text(updated, encoding='utf-8')
            changed += 1
            removed += panels + wraps + embeds
    print(f'Updated {changed} content pages; removed {removed} inline booking widgets or panels.')


if __name__ == '__main__':
    main()
