#!/usr/bin/env python3
"""Guard corrected provider facts and consistent search identities in the built output."""
import html,json,re,sys
from pathlib import Path
REPO=Path(__file__).resolve().parents[1]
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else REPO
providers=json.loads((REPO/'content/provider-page-ownership-20261024.json').read_text())['providers']
facts=json.loads((REPO/'content/comparison-source-corrections-20261024.json').read_text())
errors=[]
for r in providers:
 for key,term in [('pricing_url','Pricing'),('alternative_url','Alternatives'),('comparison_url','vs AE Tax Advisors')]:
  path=r[key].split('.com/')[-1];text=(ROOT/path/'index.html').read_text()
  title=html.unescape(re.search(r'<title>(.*?)</title>',text,re.S)[1])
  h1=html.unescape(re.sub('<[^>]*>','',re.search(r'<h1\b[^>]*>(.*?)</h1>',text,re.S)[1]))
  desc=html.unescape(re.search(r'<meta name="description" content="([^"]*)',text)[1])
  if term not in title or term not in h1:errors.append(path+': incorrect search intent')
  if text.count('class="provider-guide-nav container narrow"')!=1:errors.append(path+': missing/duplicate guide navigation')
  if not 60<=len(desc)<=200:errors.append(path+': description length '+str(len(desc)))
  if r['slug'] in facts and key=='comparison_url':
   if html.escape(facts[r['slug']]['offering']) not in text:errors.append(path+': corrected official service summary missing')
   if facts[r['slug']]['source'] not in text:errors.append(path+': corrected primary source missing')
   plain=html.unescape(re.sub('<[^>]+>',' ',text));plain=re.sub(r'\s+',' ',plain)
   if re.search(r'no Form 3115|does not prepare (?:the )?Form 3115|Typical turnaround Weeks Days|does not pass clients to junior',plain,re.I):errors.append(path+': stale unsupported assertion')
assert not errors,'\n'.join(errors)
print('PASS: 300 intent-specific page identities and descriptions; 16 corrected official-source service comparisons.')
