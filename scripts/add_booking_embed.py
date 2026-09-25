"""Add a compact booking link to blog articles that lack a call to action.

The booking calendar belongs on the discovery page. Articles link there.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG = os.path.join(ROOT, "blog")
BOOKING_LINK = '<a class="btn-cta" href="/discovery/">Choose a Time to Talk With AE Tax</a>'

CTA_MARKER = "background: #f0f4ff; border-left: 4px solid #2563eb"

EMBED = (
    '\n            ' + BOOKING_LINK + '\n'
)


CTA_BLOCK = (
    '        <hr style="margin: 48px 0; border: none; '
    'border-top: 1px solid #e5e7eb;">\n\n'
    '        <div class="compact-booking-cta" style="color:#1f2937;background: #f0f4ff; border-left: 4px solid #2563eb; '
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
    if BOOKING_LINK in src or 'api.leadconnectorhq.com/widget/booking/' in src:
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
