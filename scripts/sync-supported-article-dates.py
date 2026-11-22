"""Remove a stale optional OG update time only when visible and canonical article dates agree.

Do not infer a clock time from a day-only editorial date or change publication,
JSON-LD, visible copy, sitemap dates, or pages whose evidence is ambiguous.
"""
from pathlib import Path
from html.parser import HTMLParser
import datetime
import json
import re
import sys

MONTHS = {m: i for i, m in enumerate('January February March April May June July August September October November December'.split(), 1)}
ARTICLE_TYPES = {'Article', 'BlogPosting', 'NewsArticle'}

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.og = []; self.canonicals = []; self.graphs = []
        self.current = None; self.main = 0; self.skip = 0; self.visible = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('property') == 'article:modified_time':
            self.og.append((attrs.get('content', ''), self.get_starttag_text()))
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs.get('href', ''))
        if tag == 'main': self.main += 1
        if tag in ('script', 'style'): self.skip += 1
        if tag == 'script' and attrs.get('type') == 'application/ld+json': self.current = ''
    def handle_data(self, text):
        if self.current is not None: self.current += text
        if self.main and not self.skip: self.visible.append(text)
    def handle_endtag(self, tag):
        if tag == 'script' and self.current is not None:
            try: self.graphs.append(json.loads(self.current))
            except ValueError: pass  # The production JSON-LD gate handles malformed data.
            self.current = None
        if tag in ('script', 'style'): self.skip -= 1
        if tag == 'main': self.main -= 1

def articles(value):
    if isinstance(value, dict):
        kinds = value.get('@type', [])
        if isinstance(kinds, str): kinds = [kinds]
        if ARTICLE_TYPES.intersection(kinds): yield value
        for child in value.values(): yield from articles(child)
    elif isinstance(value, list):
        for child in value: yield from articles(child)

def matches(article, canonical):
    main = article.get('mainEntityOfPage')
    if isinstance(main, dict): main = main.get('@id') or main.get('url')
    return article.get('url') == canonical or main == canonical

def reconcile(source):
    page = Page(); page.feed(source)
    if len(page.og) != 1 or len(page.canonicals) != 1: return source, None
    canonical = page.canonicals[0]
    if not canonical.startswith('https://www.aetaxadvisors.com/'): return source, None
    dates = {a.get('dateModified') for graph in page.graphs for a in articles(graph) if matches(a, canonical)}
    if len(dates) != 1: return source, None
    supported = next(iter(dates))
    if not isinstance(supported, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', supported): return source, None
    try: datetime.date.fromisoformat(supported)
    except ValueError: return source, None
    text = ' '.join(' '.join(page.visible).split()); visible_dates = set()
    for match in re.finditer(r'(?:Last\s+)?Updated\s+(' + '|'.join(MONTHS) + r')\s+(\d{1,2}),?\s+(\d{4})', text, re.I):
        try: visible_dates.add(datetime.date(int(match[3]), MONTHS[match[1].capitalize()], int(match[2])).isoformat())
        except ValueError: pass
    if visible_dates != {supported}: return source, None
    old, tag = page.og[0]
    if not re.match(r'\d{4}-\d{2}-\d{2}', old) or old[:10] == supported: return source, None
    if source.count(tag) != 1: return source, None
    return source.replace(tag, '', 1), {'canonical': canonical, 'removedOpenGraphTime': old, 'supportedArticleDate': supported}

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else 'public')
    check_only = '--check' in sys.argv[2:]
    rows = []; scanned = 0
    for path in root.rglob('*.html'):
        scanned += 1; source = path.read_text(); updated, reason = reconcile(source)
        if reason:
            rows.append({'path': str(path.relative_to(root)), **reason})
            if not check_only: path.write_text(updated)
    print(json.dumps({'htmlScanned': scanned, 'staleOptionalTimes': len(rows), 'mode': 'check' if check_only else 'remove-stale-only', 'rows': rows}))
    if check_only and rows: raise SystemExit(1)

if __name__ == '__main__': main()
