"""Add focused contextual service paths to an explicit, reviewed article list."""
import json, re
from discovery_inventory import ROOT, eligible, redirects
from site_template import section
MARKER='<!-- commercial-owner-path -->'
def main():
 mapping=redirects(); count=0; skipped=[]
 for group in json.loads((ROOT/'commercial_intents.json').read_text()):
  block=MARKER+section(group['heading'],f'<p>{group["copy"]}</p><ul><li><a href="{group["destination"]}">{group["label"]}</a></li><li><a href="{group["secondary"]}">{group["secondary_label"]}</a></li><li><a href="/discovery/">Schedule a discovery call</a></li></ul>')+'<!-- /commercial-owner-path -->'
  for slug in group['support']:
   p=ROOT/slug/'index.html'
   if not p.exists(): raise ValueError('Missing reviewed source '+slug)
   s=p.read_text()
   if not eligible(p,s,mapping):skipped.append(slug);continue
   s=re.sub(re.escape(MARKER)+'.*?<!-- /commercial-owner-path -->','',s,flags=re.S)
   # After the first substantive content section, before long educational detail.
   main_start=s.index('<main');sections=list(re.finditer(r'</section>',s[main_start:]))
   if len(sections)<2:raise ValueError('Unexpected article layout '+slug)
   position=main_start+sections[1].end()
   s=s[:position]+block+s[position:];p.write_text(s);count+=1
 print('Contextual paths added to',count,'eligible owner pages; skipped',skipped)
if __name__=='__main__':main()
