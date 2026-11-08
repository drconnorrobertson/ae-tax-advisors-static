"""Keep existing discovery entries aligned with explicitly reviewed pages."""
from pathlib import Path
from html.parser import HTMLParser
import json
import re
import sys

REPO = Path(__file__).resolve().parent.parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else REPO
reviewed = json.loads((REPO / 'content/reviewed-content-lastmod.json').read_text())


class Metadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.title = ''
        self.description = ''
        self.noindex = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'title':
            self.in_title = True
        if tag == 'meta':
            name = attrs.get('name', '').lower()
            if name == 'description':
                self.description = attrs.get('content', '')
            if name in ('robots', 'googlebot') and 'noindex' in attrs.get('content', '').lower():
                self.noindex = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def metadata(route):
    relative = route.strip('/')
    candidates = [ROOT / relative / 'index.html', ROOT / (relative + '.html')]
    source = next((p for p in candidates if p.is_file()), None)
    if source is None:
        return None
    result = Metadata()
    result.feed(source.read_text())
    if result.noindex or not result.title or not result.description:
        return None
    title = re.sub(r'\s*\|\s*AE Tax Advisors.*$', '', result.title).strip()
    title = title.replace('[', '\\[').replace(']', '\\]')
    description = ' '.join(result.description.split())
    return title, description


target = ROOT / 'llms-full.txt'
changed = 0
if target.exists():
    lines = []
    for line in target.read_text().splitlines():
        match = re.match(r'^- \[.*\]\((https://www\.aetaxadvisors\.com(/[^)]*))\):.*$', line)
        if match and match[2] in reviewed:
            current = metadata(match[2])
            if current:
                title, description = current
                updated = f'- [{title}]({match[1]}): {description}'
                changed += updated != line
                line = updated
        lines.append(line)
    target.write_text('\n'.join(lines) + '\n')
print(f'Reviewed discovery metadata synchronized: {changed} entries.')
