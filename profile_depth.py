"""Render attributed record evidence and documented gaps for every firm."""
import json,re,html
from pathlib import Path
E=lambda s:html.escape(str(s or ''),quote=True)
p=Path(__file__).parent/'data/profile-enrichment.json'
RESEARCH=json.loads(p.read_text()) if p.exists() else {}
CATEGORIES=[(r'tax','Tax services'),(r'accounting|bookkeep','Accounting and bookkeeping'),(r'payroll','Payroll'),(r'cfo|outsourc','CFO or outsourced finance'),(r'audit|assurance','Audit and assurance'),(r'estate|trust','Estate or trust matters'),(r'wealth|retire','Wealth or retirement services'),(r'transaction|valuation','Transaction or valuation work'),(r'advisory|consult','Advisory or consulting')]
def values(v):
 if isinstance(v,list):return [str(x) for x in v if isinstance(x,(str,int,float))]
 return [v] if isinstance(v,str) and v else []
def profile_depth(f):
 d=RESEARCH.get(f['slug'],{});industries=values(f.get('directory_reported_industries'));services=values(f.get('services')) or values(f.get('directory_reported_services'));website=f.get('website');source=f.get('directory_url') or f.get('source_url');loc=f.get('location','Location not confirmed')
 out='<section class="profile-evidence" aria-label="Firm evidence and scope research"><h2>Research record for '+E(f['name'])+'</h2>'
 out+='<p>This profile separates public-source facts from the questions a prospective client still needs answered. AE Tax Advisors publishes this directory; a listing is not an independent endorsement.</p><dl class="facts"><dt>Recorded location</dt><dd>'+E(loc)+'</dd><dt>Official website in our record</dt><dd>'+(('<a href="'+E(website)+'">'+E(website)+'</a>') if website else 'Not yet confirmed. Use the cited record to identify the firm before sharing documents.')+'</dd><dt>Public source check</dt><dd>'
 if d.get('status')=='fetched' and d.get('identity_matched'):out+='Retrieved October 13, 2026; firm-name match found. This is a source identity check, not verification of credentials or performance.'
 elif d.get('status')=='fetched':out+='Retrieved October 13, 2026; firm identity was not confidently matched. Existing attributed record details remain subject to confirmation.'
 elif d:out+='Attempted October 13, 2026; the source could not be reviewed successfully. This does not establish that the firm or service is unavailable.'
 else:out+='No new successful source check recorded. Confirm the current public listing and engagement directly.'
 out+='</dd></dl>'
 if industries:out+='<h3>Industries reported in the cited directory</h3><ul>'+''.join('<li>'+E(v)+'</li>' for v in industries)+'</ul><p>These categories come from the cited professional-directory record and may be self-reported. Ask for experience with your business model, entity structure and jurisdictions; a category does not verify specialist expertise.</p>'
 if services:out+='<h3>Turn the recorded services into a written scope</h3><table><caption>Questions tied to '+E(f['name'])+'’s recorded service categories</caption><thead><tr><th scope="col">Recorded category</th><th scope="col">Confirm in the proposal</th></tr></thead><tbody>'+''.join('<tr><th scope="row">'+E(s)+'</th><td>Which deliverables, responsible professionals, deadlines and exclusions apply to this category? Is it included in the quoted fee or separately scoped?</td></tr>' for s in services)+'</tbody></table>'
 if d.get('source_excerpt'):out+='<h3>How the firm describes itself</h3><blockquote><p>'+E(d['source_excerpt'])+'</p></blockquote><p>A short excerpt from the firm’s public website, checked October 13, 2026. This is the provider’s description, not an independently verified claim. <a href="'+E(d['source_url'])+'">Read the original in context</a>.</p>'
 text=' '.join(d.get('service_headings',[]));cats=[label for pattern,label in CATEGORIES if re.search(pattern,text,re.I)]
 if cats:out+='<h3>Topics found on the firm’s public website</h3><p>The checked website includes headings relating to '+E(', '.join(cats).lower())+'. These are navigation and service-description signals, not confirmation that the firm will accept your engagement. <a href="'+E(d['source_url'])+'">Review the original website</a> and request the current service scope.</p>'
 unknown=[]
 if not website:unknown.append('The firm’s current official website and secure contact channel.')
 if not services:unknown.append('The current service list and whether it includes forward-looking tax planning rather than only preparation.')
 if not industries:unknown.append('Experience with clients in your industry and a relevant reference or redacted example.')
 unknown+=['The named professional responsible for your work and independently checked credentials.','Current fees, renewal terms, implementation duties and what happens after the initial deliverable.']
 out+='<h3>What remains unverified for '+E(f['name'])+'</h3><ul>'+''.join('<li>'+E(v)+'</li>' for v in unknown)+'</ul><h3>Prepare for a useful first conversation</h3><p>Bring an entity and owner summary, filing jurisdictions, recent returns, current financial reports and a timeline of the decisions ahead. Ask '+E(f['name'])+' to identify which records it needs before quoting, and send sensitive information only through a verified secure channel.</p>'
 if source:out+='<p><a href="'+E(source)+'">Consult the attributed firm or directory record</a> · <a href="/corrections/?firm='+E(f['slug'])+'">Suggest a source-supported correction</a>.</p>'
 return out+'</section>'
