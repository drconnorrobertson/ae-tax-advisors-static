#!/usr/bin/env python3
"""Summarize an actual GSC Pages CSV. No API, credentials or invented query data.
Usage: python3 scripts/report-gsc-content-groups.py CURRENT.csv [PREVIOUS.csv]
Use equal complete 28-day periods and identical Search Console filters.
"""
import csv,json,re,sys
from collections import defaultdict
from urllib.parse import urlparse

def group(url):
 p=urlparse(url).path
 for name,pattern in [('solar-investment','solar'),('equipment-investment','equipment.*(leas|invest)|heavy-equipment'),('provider-comparisons','^/compare/'),('short-term-rental','str-|short-term|airbnb'),('cost-segregation-depreciation','cost-seg|bonus-depreciation|macrs'),('amended-returns','amend|1040'),('workbooks','^/workbooks/')]:
  if re.search(pattern,p):return name
 return 'general-tax-planning'
def read(file):
 out=defaultdict(lambda:dict(clicks=0,impressions=0,positionImpressions=0,pages=0))
 with open(file,encoding='utf-8-sig') as f:
  for r in csv.DictReader(f):
   url=r.get('Top pages') or r.get('Page') or r.get('URL')
   if not url:raise ValueError('Expected a Search Console Pages export, not Queries or Dates')
   n=lambda k:float(r[k].replace(',',''))
   d=out[group(url)];d['clicks']+=n('Clicks');d['impressions']+=n('Impressions');d['positionImpressions']+=n('Position')*n('Impressions');d['pages']+=1
 for d in out.values():
  d['ctr']=d['clicks']/d['impressions'] if d['impressions'] else 0
  d['averagePosition']=d.pop('positionImpressions')/d['impressions'] if d['impressions'] else None
 return dict(out)
if __name__=='__main__':
 current=read(sys.argv[1]);output={'current':current,'scope':'Exported rows only; GSC export limits and filters affect coverage.'}
 if len(sys.argv)>2:
  prev=read(sys.argv[2]);output['previous']=prev;output['clickDelta']={k:v['clicks']-prev.get(k,{}).get('clicks',0) for k,v in current.items()}
 print(json.dumps(output,indent=2))
