"""Give comparison cards distinct accessible link names."""

from html import unescape
from pathlib import Path
import re


PAGE = Path(__file__).resolve().parents[1] / "compare" / "index.html"
CARD = re.compile(r'<article class="cs-card">.*?</article>', re.DOTALL)
TITLE = re.compile(r'<h3><a[^>]*>(.*?)</a></h3>', re.DOTALL)
BUTTON = re.compile(r'(<a href="[^"]+" class="btn-secondary")(?: aria-label="[^"]*")?(>Read the Comparison</a>)')


def label_card(match: re.Match[str]) -> str:
    card = match.group(0)
    title_match = TITLE.search(card)
    if not title_match:
        return card
    title = unescape(re.sub(r"<[^>]+>", "", title_match.group(1))).strip()
    label = f'Read comparison: {title}'
    return BUTTON.sub(lambda button: f'{button.group(1)} aria-label="{label}"{button.group(2)}', card, count=1)


def main() -> None:
    before = PAGE.read_text(encoding="utf-8")
    after = CARD.sub(label_card, before)
    if after != before:
        PAGE.write_text(after, encoding="utf-8")
    count = after.count('aria-label="Read comparison:')
    print(f"Labeled {count} comparison links")


if __name__ == "__main__":
    main()
