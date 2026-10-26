"""Render the expanded existing credential guide in the standard directory shell."""
from pathlib import Path
import json
import html
import shutil


def render_credential_guide(page, root, out, base):
    guide=json.loads((root/'editorial-guides/credentials.json').read_text())
    e=html.escape
    core=''.join('<'+b['type']+'>'+e(b['text'])+'</'+b['type']+'>' for b in guide['blocks'])
    sources=''.join('<li><a href="'+e(url,quote=True)+'">'+e(label)+'</a></li>' for url,label in guide['sources'])
    related=''.join('<li><a href="'+e(url,quote=True)+'">'+e(label)+'</a></li>' for url,label in guide['links'])
    faq=json.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':guide['faqs']}).replace('<','\\u003c')
    body='<section class="page-head"><span class="eyebrow">Credentials and engagement scope</span><h1>'+e(guide['title'])+'</h1><p>'+e(guide['description'])+'</p><p>Published October 13, 2026 · Updated October 26, 2026</p></section><div class="article-layout"><article class="prose"><div id="editorial-body">'+core+'</div><script type="application/ld+json">'+faq+'</script><section><h2>Fictional research worksheet</h2><p><a href="/assets/credential-research-example.csv" download>Download the fictional credential-research example (CSV)</a>. No real person, license number or credential status is represented.</p></section><section><h2>Primary sources and scope</h2><ul>'+sources+'</ul><p>AI-assisted website editorial content with checked fictional examples. Sources checked October 26, 2026. No actual credential verification, named professional review or client outcome is asserted.</p></section><section><h2>Related buyer research</h2><ul>'+related+'</ul></section></article><aside class="profile-aside"><h2>Separate the research tasks</h2><p>Identify the responsible individual, research the relevant credential, then compare the actual proposed engagement.</p><a class="button" href="/firms/">Research firms</a><p><a href="/methodology/">Read publisher and listing disclosures</a></p></aside></div>'
    page(guide['route'],guide['title'],guide['description'],body,kind='Article',schema={'author':{'@type':'Organization','name':'Tax Strategist Directory website editorial'},'datePublished':guide['published'],'dateModified':'2026-10-26','wordCount':guide['words'],'mainEntityOfPage':base+guide['route']})
    (out/'assets').mkdir(exist_ok=True)
    shutil.copyfile(root/'editorial-assets/credential-research-example.csv',out/'assets/credential-research-example.csv')
