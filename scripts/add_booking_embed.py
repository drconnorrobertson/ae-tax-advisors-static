"""Add the booking calendar embed to blog articles that lack it.

Two cases. Articles that already close with a CTA box get the iframe appended
below the existing button, keeping both conversion paths. Articles that end in
plain prose with no CTA at all get a full CTA block built around the calendar.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG = os.path.join(ROOT, "blog")
BOOKING = "https://api.leadconnectorhq.com/widget/booking/5bPhybfzi6mKUTgn5GMg"

CTA_MARKER = "background: #f0f4ff; border-left: 4px solid #2563eb"

EMBED = (
    '\n            <iframe src="%s" allow="payment" '
    'style="width:100%%;border:none;overflow:hidden;min-height:700px;'
    'border-radius:8px;background:#fff;" scrolling="no" '
    'title="Book a tax strategy call with AE Tax Advisors"></iframe>\n'
    '            <p style="margin-top:18px;margin-bottom:0;font-size:15px;">'
    'Prefer to talk first? Call <a href="tel:+16316145762">(631) 614-5762</a> '
    'or email <a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a>'
    '.</p>\n        ' % BOOKING
)


CTA_BLOCK = (
    '        <hr style="margin: 48px 0; border: none; '
    'border-top: 1px solid #e5e7eb;">\n\n'
    '        <div style="background: #f0f4ff; border-left: 4px solid #2563eb; '
    'padding: 24px 28px; border-radius: 8px; margin-top: 32px;">\n'
    '            <h3 style="margin-top: 0; color: #1e3a8a;">'
    'Find Out What This Is Worth in Your Situation</h3>\n'
    '            <p style="margin-bottom: 20px;">Every strategy on this page '
    'depends on your income, your entity structure, and your state. Book a '
    'call and we will tell you what applies to you and what it is worth.</p>'
    + EMBED.rstrip() + '\n        </div>\n\n'
)

CLOSE = "    </div></section>"


def process(src):
    if BOOKING in src:
        return src, False

    if CTA_MARKER in src:
        start = src.index(CTA_MARKER)
        end = src.index("</div>", start)
        box = src[start:end]
        return src[:start] + box.rstrip() + EMBED + src[end:], True

    # No CTA box at all: append a complete one before the section closes.
    if "<main>" not in src or CLOSE not in src:
        return src, False
    at = src.index(CLOSE, src.index("<main>"))
    return src[:at] + CTA_BLOCK + src[at:], True


def main():
    changed = 0
    for slug in sorted(os.listdir(BLOG)):
        path = os.path.join(BLOG, slug, "index.html")
        if not os.path.exists(path):
            continue
        src = open(path).read()
        out, did = process(src)
        if did:
            open(path, "w").write(out)
            changed += 1
    print(f"booking embed added to {changed} articles")


if __name__ == "__main__":
    main()
