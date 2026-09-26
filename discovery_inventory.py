"""One canonical/indexable inventory for public discovery files."""
from html.parser import HTMLParser
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
BASE = 'https://www.aetaxadvisors.com'

class Metadata(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.canonical = None
        self.noindex = False
        self.title = ''
        self.description = ''
        self.in_title = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'link' and 'canonical' in a.get('rel', '').lower().split():
            self.canonical = a.get('href')
        if tag == 'meta':
            if a.get('name', '').lower() in ('robots', 'googlebot'):
                self.noindex |= 'noindex' in a.get('content', '').lower() or a.get('content', '').lower() == 'none'
            if a.get('name', '').lower() == 'description':
                self.description = a.get('content', '')
        if tag == 'title':
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data

def redirects():
    config = json.loads((ROOT / 'vercel.json').read_text())
    return {r['source']: r['destination'] for r in config.get('redirects', [])
            if r.get('statusCode') in (301, 308) and ':' not in r['source']}

def page_url(path):
    rel = path.parent.relative_to(ROOT).as_posix()
    return '/' if rel == '.' else '/' + rel + '/'

def eligible(path, text=None, redirect_map=None):
    text = path.read_text(encoding='utf-8') if text is None else text
    meta = Metadata(text)
    url = page_url(path)
    redirect_map = redirects() if redirect_map is None else redirect_map
    return bool(not meta.noindex and meta.canonical == BASE + url and url not in redirect_map)

def inventory():
    result = []
    mapping = redirects()
    for path in sorted(ROOT.rglob('index.html')):
        if '.git' in path.parts:
            continue
        text = path.read_text(encoding='utf-8')
        if eligible(path, text, mapping):
            meta = Metadata(text)
            result.append({'path': page_url(path), 'title': meta.title,
                           'description': meta.description})
    return result
