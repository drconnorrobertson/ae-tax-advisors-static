"""Reject table-row text outside cells and unmatched cell-end tags.

These defects can move explanatory text away from its associated amount in a
browser. This is a focused source-markup check, not a complete HTML validator.
Optional cell-end tags and nested tables remain supported. Reads files only.
"""
from html.parser import HTMLParser
from pathlib import Path
import json
import sys

class TableCells(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.tables = 0
        self.errors = []
        self.hidden = 0

    def problem(self, kind, text=None):
        item = {'kind': kind, 'line': self.getpos()[0], 'table': self.stack[-1]['number']}
        if text:
            item['text'] = text.strip()[:160]
        self.errors.append(item)

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag == 'table':
            self.tables += 1
            self.stack.append({'row': False, 'cell': False, 'number': self.tables})
        elif self.stack:
            current = self.stack[-1]
            if tag == 'tr':
                current.update(row=True, cell=False)
            elif tag in ('td', 'th'):
                # Starting another cell implicitly closes the previous one.
                current['cell'] = True

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)
        if not self.stack:
            return
        current = self.stack[-1]
        if tag == 'table':
            self.stack.pop()
        elif tag == 'tr':
            current.update(row=False, cell=False)
        elif tag in ('td', 'th'):
            if not current['cell']:
                self.problem('unmatched-cell-end')
            current['cell'] = False

    def handle_data(self, data):
        if self.stack and not self.hidden and data.strip():
            current = self.stack[-1]
            if current['row'] and not current['cell']:
                self.problem('row-text-outside-cell', data)

def check(root):
    pages = tables = error_count = 0
    examples = []
    for path in sorted(root.rglob('*.html')):
        pages += 1
        parser = TableCells()
        parser.feed(path.read_text())
        tables += parser.tables
        error_count += len(parser.errors)
        for error in parser.errors:
            if len(examples) < 20:
                examples.append({'path': str(path.relative_to(root)), **error})
    return {'htmlPages': pages, 'tables': tables, 'errorCount': error_count, 'errors': examples}

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else 'public')
    if not root.is_dir():
        raise SystemExit('Missing production HTML directory: ' + str(root))
    result = check(root)
    if not result['htmlPages']:
        raise SystemExit('No production HTML pages found: ' + str(root))
    print(json.dumps(result))
    raise SystemExit(bool(result['errorCount']))

if __name__ == '__main__':
    main()
