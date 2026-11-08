#!/usr/bin/env python3
"""Preserve evidenced publication history; reject new duplicate-day or future blog releases."""
import collections,datetime,json,re,sys
from pathlib import Path
from zoneinfo import ZoneInfo
r=Path(__file__).resolve().parents[1];p=json.loads((r/'content/blog-publication-policy.json').read_text());entries=json.loads((r/'scripts/blog-catalog.json').read_text());baseline=json.loads((r/p['baseline']).read_text());by={e['url']:e for e in entries};errors=[];today=datetime.datetime.now(ZoneInfo('America/New_York')).date().isoformat();dates=collections.defaultdict(list)
for e in entries:
 date=e['date'];url=e['url']
 if url in baseline:
  if date!=baseline[url]:errors.append(url+': historical publication date changed without evidence review')
 else:
  if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',date):errors.append(url+': missing publication date')
  elif date<p['effectiveDate']:errors.append(url+': new content backdated before policy')
  elif date>today:errors.append(url+': future content must remain scheduled until release day')
  if any(x['url']!=url and x['date']==date for x in entries):errors.append(url+': another blog article has this publication date')
 dates[date].append(url)
print(json.dumps(dict(articles=len(entries),historicalArticles=len(baseline),newArticles=len(set(by)-set(baseline)),historicalDuplicateDateGroups=sum(len(v)>1 for v in dates.values()),errors=errors)));sys.exit(bool(errors))
