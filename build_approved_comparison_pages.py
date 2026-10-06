#!/usr/bin/env python3
"""Render owner-approved October 6 comparison copy without editorial metadata.

Run after older comparison generators if rebuilding this cluster.
"""
import html
import json
import re
from pathlib import Path
import site_template as T

DATE = '2026-10-06'
COPY = T.ROOT / 'content/comparison-pages-20261006.md'
SLUGS = ['p4-tax-vs-ae-tax','p4-tax-alternatives','creative-planning-vs-ae-tax',
 'creative-planning-alternatives','delerme-cpa-vs-ae-tax','delerme-cpa-alternatives',
 'range-vs-ae-tax','range-alternatives','tax-planning-and-wealth-advisors']


def inline(s):
    links=[]
    def link(m):
        url=m.group(2)
        if url.startswith(T.SITE):url=url[len(T.SITE):] or '/'
        if not (url.startswith('/') or url.startswith('https://')):raise ValueError(url)
        links.append('<a href="'+html.escape(url,quote=True)+'">'+html.escape(m.group(1))+'</a>')
        return f'LINKTOKEN{len(links)-1}ENDTOKEN'
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,s)
    s=html.escape(s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<em>\1</em>',s)
    for i,l in enumerate(links):s=s.replace(f'LINKTOKEN{i}ENDTOKEN',l)
    return s


def render(lines, slug):
    result=[];toc=[];i=0;faq_added=False;table_n=0
    while i<len(lines):
        line=lines[i].strip()
        if not line or line=='---':i+=1;continue
        if line.startswith('## '):
            label=line[3:];anchor=re.sub('[^a-z0-9]+','-',label.lower()).strip('-')
            toc.append((anchor,label));result.append(f'<h2 id="{anchor}">{inline(label)}</h2>');i+=1;continue
        if line.startswith('### '):
            label=line[4:]
            if label.endswith('?') and not faq_added:
                result.append('<h2 id="frequently-asked-questions">Frequently Asked Questions</h2>')
                toc.append(('frequently-asked-questions','Frequently Asked Questions'));faq_added=True
            result.append('<h3>'+inline(label)+'</h3>');i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=[x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',x) for x in row):rows.append(row)
                i+=1
            table_n+=1;n=len(rows[0]);assert all(len(r)==n for r in rows)
            caption='Public offerings and interview criteria reviewed October 6, 2026. Confirm current scope directly.'
            result.append(f'<div class="ae-table-scroll"><table class="compare-table comparison-table" style="--comparison-columns:{n}"><caption>{caption}</caption><thead><tr>'+''.join('<th scope="col">'+inline(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>')
            for row in rows[1:]:result.append('<tr><th scope="row">'+inline(row[0])+'</th>'+''.join('<td>'+inline(c)+'</td>' for c in row[1:])+'</tr>')
            result.append('</tbody></table></div>');continue
        if line.startswith('- '):
            result.append('<ul>')
            while i<len(lines) and lines[i].strip().startswith('- '):result.append('<li>'+inline(lines[i].strip()[2:])+'</li>');i+=1
            result.append('</ul>');continue
        paragraph=[]
        while i<len(lines) and lines[i].strip() and not lines[i].strip().startswith(('## ','### ','|','- ')) and lines[i].strip()!='---':paragraph.append(lines[i].strip());i+=1
        text=' '.join(paragraph)
        cls=' class="comparison-disclosure"' if text.startswith('*Published by') or text.startswith('*AE Tax Advisors') or text.startswith('*This first-party') else ''
        result.append('<p'+cls+'>'+inline(text)+'</p>')
    return '\n'.join(result),toc


def build():
    source=COPY.read_text();shared=source.split('### AE Tax Advisors fees and engagement scope\n\n',1)[1].split('\n---',1)[0]
    segments=source.split('# PAGE ')[1:]
    for index,(slug,part) in enumerate(zip(SLUGS,segments),1):
        title=re.search(r'\*\*Title tag:\*\* (.*)',part).group(1)
        desc=re.search(r'\*\*Meta description:\*\* (.*)',part).group(1)
        raw=part[part.index('\n# ')+1:].strip().removesuffix('---').strip()
        lines=raw.splitlines();heading=lines.pop(0)[2:]
        markup,toc=render(lines,slug)
        if index in [1,3,5,7]:
            markup+='\n<aside class="comparison-pricing" aria-labelledby="ae-engagement-fees"><h2 id="ae-engagement-fees">AE Tax Advisors fees and engagement scope</h2><p>'+inline(shared)+'</p></aside>'
        nav='<nav class="comparison-toc" aria-label="On this page"><strong>On this page</strong><ul>'+''.join(f'<li><a href="#{a}">{html.escape(label)}</a></li>' for a,label in toc)+'</ul></nav>' if toc else ''
        path='/compare/'+slug+'/'
        file=T.ROOT/path.strip('/')/'index.html';published=DATE
        if file.exists():
            old=file.read_text();m=re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})',old)
            if m:published=m.group(1)
        trail=[('Home','/'),('Compare','/compare/'),(heading,path)]
        body=T.page_header(h1=html.escape(heading),subtitle=html.escape(desc),trail=trail)+'\n<section class="content-section comparison-content"><div class="container narrow"><p class="comparison-updated">Reviewed October 6, 2026 · AE Tax Advisors</p>'+nav+'<article class="comparison-article" aria-label="'+html.escape(heading,quote=True)+'">'+markup+'</article></div></section>'
        citations=sorted(set(re.findall(r'https://[^)\s]+',raw)))
        schemas=[T.article_schema(title=heading,description=desc,url=T.SITE+path,published=published,modified=DATE,section='Tax advisor comparisons',citations=citations),T.breadcrumb_schema(trail)]
        faqs=[]
        for m in re.finditer(r'### ([^\n]+\?)\n\n(.*?)(?=\n### |\n## |\Z)',raw,re.S):
            answer=m.group(2).split('\n\n',1)[0];faqs.append((m.group(1),'<p>'+inline(answer)+'</p>'))
        if faqs:schemas.append(T.faq_schema(faqs))
        document=T.build_page(title=title,description=desc,path=path,body=body,schemas=schemas,published=published,modified=DATE,active_nav='/compare/',extra_head='<link rel="stylesheet" href="/assets/footer.css?v=20261001">')
        document=document.replace('<main id="main-content"','<main class="comparison-page" id="main-content"')
        T.write_page(path, "\n".join(line.rstrip() for line in document.splitlines())+"\n")
    print('Rendered',len(segments),'approved comparison pages.')

if __name__=='__main__':build()
