import re,json,html,unicodedata,sys
from pathlib import Path
root=Path(sys.argv[1] if len(sys.argv)>1 else 'public')
def clean(s):
 s=re.sub(r'<[^>]*>',' ',html.unescape(str(s)));s=unicodedata.normalize('NFKC',s).lower();return re.sub(r'[^a-z0-9]+',' ',s).strip()
rows=[];pages=0;questions=0
def walk(x):
 if isinstance(x,dict):
  t=x.get('@type');types=t if isinstance(t,list) else [t]
  if 'FAQPage' in types:yield x
  for v in x.values():yield from walk(v)
 elif isinstance(x,list):
  for v in x:yield from walk(v)
for p in root.rglob('*.html'):
 s=p.read_text()
 if re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex',s):continue
 visible=clean(re.sub(r'<(script|style|head)\b[^>]*>[\s\S]*?</\1>',' ',s,flags=re.I));bad=[];n=0
 for b in re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>([\s\S]*?)</script>',s,re.I):
  try:j=json.loads(b)
  except Exception:continue
  for faq in walk(j):
   for q in faq.get('mainEntity',[]):
    if not isinstance(q,dict):continue
    n+=1;a=q.get('acceptedAnswer',{});a=a.get('text','') if isinstance(a,dict) else '';qn=q.get('name','')
    missing=[]
    if clean(qn) not in visible:missing.append('question')
    if clean(a) not in visible:missing.append('answer')
    if missing:bad.append({'question':qn,'missing':missing,'answer':a})
 if n:pages+=1;questions+=n
 if bad:rows.append({'route':'/'+str(p.parent.relative_to(root)).strip('.')+'/','mismatches':bad})
out={'pagesWithFaq':pages,'questions':questions,'pagesWithMismatches':len(rows),'rows':rows}
print(json.dumps(out));sys.exit(1 if rows else 0)
