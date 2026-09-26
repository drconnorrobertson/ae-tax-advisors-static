"""Repair discovery paths and consolidate the cost segregation calculator."""
from pathlib import Path
import re
import json
import site_template as T

ROOT = T.ROOT
CALCULATOR = '''
<!-- owner-calculator:start -->
<section class="content-section" id="estimate"><div class="container narrow">
<h2>Cost segregation calculator: test a first-year scenario</h2>
<p>This calculator is for a new acquisition with components independently confirmed as eligible for 100% federal bonus depreciation. It does not determine eligibility or calculate a prior-year Form 3115 adjustment. Enter your own assumptions; property type does not establish a reclassification percentage or a recovery period.</p>
<form id="cost-seg-scenario">
<div class="scenario-grid">
<label>Total acquisition basis before land ($)<input name="price" type="number" min="0" max="1000000000000" step="any" value="1000000" required></label>
<label>Supported land allocation (%)<input name="land" type="number" min="0" max="100" step="any" value="20" required></label>
<label>Assumed bonus-eligible reclassification (%)<input name="reclass" type="number" min="0" max="100" step="any" value="20" required></label>
<label>Confirmed building recovery period<select name="life" required><option value="">Select after classification review</option><option value="27.5">27.5-year residential rental</option><option value="39">39-year nonresidential</option></select></label>
<label>Month placed in service<select name="month" required><option value="1">January</option><option value="2">February</option><option value="3">March</option><option value="4">April</option><option value="5">May</option><option value="6">June</option><option value="7">July</option><option value="8">August</option><option value="9">September</option><option value="10">October</option><option value="11">November</option><option value="12">December</option></select></label>
<label>Assumed federal marginal tax rate (%)<input name="rate" type="number" min="0" max="100" step="any" value="32" required></label>
<label>Additional deduction usable this year (%)<input name="usable" type="number" min="0" max="100" step="any" value="0" required></label>
<label>Your quoted study and implementation fee ($)<input name="fee" type="number" min="0" max="1000000000" step="any" placeholder="Enter quoted total" required></label>
</div>
<p id="scenario-scope">The 20% reclassification default is an illustration, not a typical result or property-specific estimate. Usable deduction starts at zero until you enter a reviewed assumption. Confirm basis, at-risk, passive-loss and other limitations. Short guest stays alone do not establish a 39-year recovery period. The fee is your input, not an AE quote.</p>
<label class="scenario-check"><input name="eligible" type="checkbox" required> I am modeling qualifying assets eligible for 100% bonus depreciation, with no election out, and a confirmed GDS building classification.</label>
<p><button class="btn-cta" type="submit">Calculate scenario</button></p>
</form>
<div id="scenario-result" role="status" aria-live="polite">Choose the assumptions above to calculate. No personal information is collected or sent by this calculator.</div>
<noscript><p>JavaScript is needed for interactive results. The calculation method and example below can be read without it.</p></noscript>
<h3>Calculation method and a worked example</h3>
<p>Depreciable basis equals acquisition basis less land. The assumed reclassified portion receives 100% bonus; the remaining building uses straight-line GDS depreciation with a mid-month fraction of (12.5 minus the calendar month number) divided by 12. The same fraction applies to the without-study comparison. The difference is multiplied by the entered usable percentage and federal marginal rate, then the entered fee is subtracted.</p>
<p>For $1,000,000 of basis, 20% land, 20% qualifying reclassification, 27.5 years and January service, the additional first-year deduction is approximately $154,424. If all of it is usable at an assumed 32% rate, the illustrative federal reduction is $49,416; after a $3,000 entered fee, the current cash benefit is $46,416. If none is currently usable, the immediate reduction is $0 and the fee still costs $3,000.</p>
<p>This is a sensitivity calculation, not a tax-return estimate. It excludes state tax, deduction interactions, the tax treatment of the fee, future depreciation differences, sale recapture, financing and time value. A full holding-period projection may change the decision. See <a href="https://www.irs.gov/publications/p946">IRS Publication 946</a> and <a href="https://www.irs.gov/publications/p925">Publication 925</a> for the underlying depreciation and loss-limitation rules.</p>
<p><a href="/blog/cost-segregation-related-party-property-purchase/">Related-party acquisition review</a> · <a href="/blog/elect-out-bonus-depreciation-asset-class/">Bonus elections by asset class</a> · <a href="/cost-segregation-study/">Request a property-specific study proposal</a></p>
</div></section>
<!-- owner-calculator:end -->
'''
CSS = '''<style id="owner-calculator-style">#estimate{padding:24px 0}#estimate>.container{padding:0}.scenario-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}.scenario-grid label{display:flex;flex-direction:column;gap:6px;font-weight:600}.scenario-grid input,.scenario-grid select{width:100%;min-height:48px;padding:10px;font:inherit;border:1px solid #7b8794;border-radius:6px}.scenario-check{display:block;margin:20px 0}.scenario-check input{width:20px;height:20px;vertical-align:middle}#scenario-result{padding:20px;background:#edf4f7;color:#142d42;margin:24px 0}#scenario-result dt{font-weight:600}#scenario-result dd{margin:0 0 12px}#cost-seg-scenario :focus-visible{outline:3px solid #176084;outline-offset:3px}@media(max-width:650px){.scenario-grid{grid-template-columns:1fr}}</style>'''

def main():
    config_path = ROOT/'vercel.json'
    config = json.loads(config_path.read_text())
    targets = {'/tools/cost-seg-calculator/':'/cost-segregation-calculator/',
               '/cost-segregation-savings-calculator/':'/cost-segregation-calculator/',
               '/cost-seg-estimator/':'/cost-segregation-calculator/'}
    known = {r['source'] for r in config['redirects']}
    for source,destination in targets.items():
        if source not in known:
            config['redirects'].insert(0,dict(source=source,destination=destination,statusCode=301))
    # A real article feed replaces a redirect to the blog landing page.
    for rule in config['redirects']:
        if rule['source'] == '/feed/': rule['destination'] = '/feed.xml'
    config['redirects'] = [r for r in config['redirects'] if not (r['source']=='/onboarding/' and r.get('statusCode')==200)]
    if not any(h['source']=='/feed.xml' for h in config['headers']):
        config['headers'].insert(0,dict(source='/feed.xml',headers=[dict(key='Content-Type',value='application/rss+xml; charset=utf-8')]))
    config_path.write_text(json.dumps(config,indent=2)+'\n')
    changed=0
    for path in ROOT.rglob('*.html'):
        s=path.read_text();original=s
        for source,destination in targets.items():
            s=s.replace('href="'+source+'"','href="'+destination+'"')
        if s!=original:path.write_text(s);changed+=1
    print('Pages with calculator links made direct:',changed)
    p=ROOT/'cost-segregation-calculator/index.html';s=p.read_text()
    s=re.sub(r'<!-- owner-calculator:start -->.*?<!-- owner-calculator:end -->','',s,flags=re.S)
    s=re.sub(r'<style id="owner-calculator-style">.*?</style>','',s,flags=re.S)
    s=s.replace('<script src="/assets/cost-segregation-scenario.js" defer></script>','')
    s=s.replace('</head>',CSS+'\n<script src="/assets/cost-segregation-scenario.js" defer></script>\n</head>')
    # The existing page has one long article rather than a separate masthead.
    # Put the tool before the first explanatory heading, inside that article.
    marker='<h2>How Accurate Is a Cost Segregation Calculator Before You Pay for a Study?</h2>'
    s=s.replace(marker,CALCULATOR+'\n'+marker,1)
    s=re.sub(r'<title>.*?</title>','<title>Cost Segregation Calculator: Test Your Tax Benefit | AE Tax</title>',s,count=1,flags=re.S)
    p.write_text(re.sub(r"(?m)[ \t]+$", "", s))
    # One group lets Google, Bing and AI bots inherit the same restrictions.
    robots='''# Public search and AI retrieval access. No crawler-specific override of these rules.
User-agent: *
Allow: /
Disallow: /*?utm_
Disallow: /*?fbclid
Disallow: /*?gclid
Disallow: /*?ref=
Disallow: /*?v=

# Staging pages remain crawlable so crawlers can read their noindex directives.
# Search visibility is governed by canonical URLs and page-level robots tags.
User-agent: AhrefsBot
Disallow: /
User-agent: SemrushBot
Disallow: /
User-agent: DotBot
Disallow: /
User-agent: MJ12bot
Disallow: /

Sitemap: https://www.aetaxadvisors.com/sitemap.xml
Sitemap: https://www.aetaxadvisors.com/sitemap-cost-segregation.xml
Sitemap: https://www.aetaxadvisors.com/sitemap-owner-guides.xml

# Optional human-readable service and content index:
# https://www.aetaxadvisors.com/llms.txt
'''
    (ROOT/'robots.txt').write_text(robots)

if __name__=='__main__':main()
