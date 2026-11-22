"""Selected IRS Table A-1 reference, checked Nov22 against 2025 Pub946 p71.
Not a taxpayer eligibility or return calculator.
"""
from pathlib import Path
from decimal import Decimal as D
from html.parser import HTMLParser
import csv,re,sys
root=Path(sys.argv[1] if len(sys.argv)>1 else 'public')
class Tables(HTMLParser):
 def __init__(self):super().__init__();self.tables=[];self.table=None;self.row=None;self.cell=None
 def handle_starttag(self,t,a):
  if t=='table':self.table=[]
  elif t=='tr':self.row=[]
  elif t in ('td','th'):self.cell=''
 def handle_data(self,d):
  if self.cell is not None:self.cell+=d
 def handle_endtag(self,t):
  if t in ('td','th') and self.cell is not None:self.row.append(self.cell.strip());self.cell=None
  elif t=='tr' and self.row is not None:self.table.append(self.row);self.row=None
  elif t=='table':self.tables.append(self.table);self.table=None
reference={5:'20.00 32.00 19.20 11.52 11.52 5.76',7:'14.29 24.49 17.49 12.49 8.93 8.92 8.93 4.46',15:'5.00 9.50 8.55 7.70 6.93 6.23 5.90 5.90 5.91 5.90 5.91 5.90 5.91 5.90 5.91 2.95'}
s=(root/'blog/macrs-depreciation-schedule-explained/index.html').read_text();p=Tables();p.feed(s)
table=next(t for t in p.tables if t[0]==['Year','5 year (200% DB)','7 year (200% DB)','15 year (150% DB)'])
assert '</p></p>' not in s
assert len(table)==17
with (root/'assets/macrs-half-year-table-a1-selected-rates.csv').open() as f:rows=list(csv.DictReader(f))
assert len(rows)==30
for col,cls in enumerate((5,7,15),1):
 vals=reference[cls].split();actual=[r for r in rows if int(r['gds_recovery_years'])==cls]
 assert [r['percent'] for r in actual]==vals
 assert [int(r['recovery_year']) for r in actual]==list(range(1,len(vals)+1))
 assert sum(map(D,vals))==D('100.00')
 for year,val in enumerate(vals,1):assert table[year][0]==str(year) and table[year][col]==val+'%'
 for year in range(len(vals)+1,17):assert table[year][col]==''
 assert all(r['convention']=='half-year' and r['source_edition']=='2025' and r['method']==('150% DB' if cls==15 else '200% DB') for r in actual)
basis=D('10000')*D('.8')-D('3000');assert basis==5000
assert basis*D('.2')==1000 and basis*D('.32')==1600
assert D(40000)/D(100000)==D('.4') and not D(40000)/D(100000)>D('.4')
assert round(D(41000)/D(101000)*100,2)==D('40.59')
assert D('1000000')*D('.00152')==1520 and D('1000000')*D('.03485')==34850
for text in ['not for bonus depreciation','exactly 40% does not trigger it','not the straight-line schedule for QIP','not $4,000 of tax savings','same-year placements and dispositions']:
 assert text in re.sub('<[^>]+>','',s),text
assert s.count('tabindex="0"')>=3 and s.count('<caption>')>=3
for old in ['9 through 15','applies to all real property','every personal property asset','each switching to straight line']:assert old not in s,old
print('PASS: 30 IRS rates in 16 HTML rows and CSV; 3 complete schedules; independent basis/convention examples; exception scope and keyboard regions.')
