"""Regression controls for amount/explanation association and CLI failure."""
from pathlib import Path
import importlib.util
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('table_cells', ROOT / 'check-table-cells.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def parse(source):
    parser = module.TableCells()
    parser.feed(source)
    return parser

# Shape found in the syndication ledger: an amount is closed, but the next
# explanatory cell lacks its opening tag. Browsers move that text out of its row.
broken = '<table><tr><th>Record</th><td>$61,000</td>Ordinary recapture</td></tr></table>'
assert {e['kind'] for e in parse(broken).errors} == {'row-text-outside-cell', 'unmatched-cell-end'}
fixed = '<table><tr><th>Record</th><td>$61,000</td><td>Ordinary recapture</td></tr></table>'
assert not parse(fixed).errors
assert not parse('<table><tr><td>A<td>B<tr><td>C<td>D</table>').errors
assert not parse('<table><tr><td><table><tr><td>Nested</td></tr></table></td><td>Outer</td></tr></table>').errors
assert not parse('<table><caption>Amounts</caption><tr><td colspan="2"><strong>Note</strong></td></tr></table>').errors
assert not parse('<table><tr><script>var example = "text";</script><td>A</td></tr></table>').errors
assert parse('<table><tr><td>A</td></td></tr></table>').errors[0]['kind'] == 'unmatched-cell-end'
with tempfile.TemporaryDirectory(prefix='ae-table-check-') as name:
    folder = Path(name)
    page = folder / 'example.html'
    page.write_text(broken)
    args = [sys.executable, str(ROOT / 'check-table-cells.py'), str(folder)]
    result = subprocess.run(args, capture_output=True, text=True)
    report = json.loads(result.stdout)
    assert result.returncode == 1 and report['errorCount'] == 2
    assert all(e['path'] == 'example.html' for e in report['errors'])
    page.write_text(fixed)
    result = subprocess.run(args, capture_output=True, text=True)
    assert result.returncode == 0 and json.loads(result.stdout)['errorCount'] == 0
print('PASS: actual defect shape rejected; corrected, optional-end, nested, spanning and script-containing tables accepted; CLI fails and recovers.')
