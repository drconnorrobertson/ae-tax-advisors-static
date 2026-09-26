"""Audit public search/AI retrieval readiness; this does not prove provider indexing.

Local: python3 audit_ai_access.py
Live: python3 audit_ai_access.py --live --output /path/outside/site/report.json
Live probes use named user agents from our machine, not provider-owned IP addresses.
"""
import argparse, concurrent.futures, json, re, urllib.request, urllib.robotparser
from html.parser import HTMLParser
from pathlib import Path
from discovery_inventory import BASE, ROOT, inventory

BOTS = ['OAI-SearchBot','ChatGPT-User','GPTBot','Claude-SearchBot','Claude-User','ClaudeBot',
        'PerplexityBot','Perplexity-User','Googlebot','Google-Extended','bingbot','Applebot',
        'Applebot-Extended','MistralAI-User','MistralAI-Index','DuckDuckBot','CCBot','UnlistedSearchCrawler']
LIVE_BOTS=['OAI-SearchBot','ChatGPT-User','Claude-SearchBot','Claude-User','PerplexityBot',
           'Perplexity-User','Googlebot','bingbot','Applebot','MistralAI-User']
PATHS=['/robots.txt','/llms.txt','/llms-full.txt','/sitemap.xml','/business-owner-tax-planning/',
       '/real-estate-tax-planning/','/cost-segregation-study/','/cost-segregation-study-cost-pricing/']
RESTRICTED=re.compile(r'\b(noindex|none|nosnippet|noarchive|nocache|noai)\b|max-snippet\s*:\s*0\b',re.I)
class Directives(HTMLParser):
    def __init__(self,text):
        super().__init__();self.bad=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);name=a.get('name','').lower()
        if tag=='meta' and name in {b.lower() for b in BOTS}|{'robots'} and RESTRICTED.search(a.get('content','')):
            self.bad.append({'agent':name,'content':a['content']})

def local_audit():
    pages=inventory();rp=urllib.robotparser.RobotFileParser();rp.parse((ROOT/'robots.txt').read_text().splitlines())
    blocked=[];restricted=[]
    for p in pages:
        for bot in BOTS:
            if not rp.can_fetch(bot,BASE+p['path']):blocked.append({'path':p['path'],'agent':bot})
        file=ROOT/p['path'].strip('/')/'index.html'
        for issue in Directives(file.read_text()).bad:restricted.append({'path':p['path'],**issue})
    return {'canonical_pages':len(pages),'crawler_tokens_tested':len(BOTS),'robots_checks':len(pages)*len(BOTS),
            'blocked':blocked,'restrictive_page_directives':restricted}

def probe(pair):
    bot,path=pair
    try:
        request=urllib.request.Request(BASE+path,headers={'User-Agent':f'{bot}/1.0 (AE site-owner synthetic access check)'})
        with urllib.request.urlopen(request,timeout=25) as r:
            body=r.read();header=r.headers.get('X-Robots-Tag','');ctype=r.headers.get('Content-Type','')
            expected=ROOT/path.lstrip('/')
            if path.endswith('/'):expected/='index.html'
            return {'agent':bot,'path':path,'status':r.status,'url':r.url,'content_type':ctype,
                    'x_robots_tag':header,'restrictive_header':bool(RESTRICTED.search(header)),
                    'matches_public_file':body==expected.read_bytes()}
    except Exception as e:return {'agent':bot,'path':path,'error':str(e)}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--live',action='store_true');parser.add_argument('--output',type=Path);args=parser.parse_args()
    result={'meaning':'Access/readiness checks, not proof of provider crawling, indexing, training or citations. Live user-agent probes originate from our machine, not provider networks.','local':local_audit()}
    if args.live:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:result['live']=list(pool.map(probe,[(bot,path) for bot in LIVE_BOTS for path in PATHS]))
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['local'],indent=2))
    live=result.get('live',[]);fail=[r for r in live if r.get('status')!=200 or not r.get('matches_public_file') or r.get('restrictive_header')]
    if live:print(json.dumps({'live_probes':len(live),'passed':len(live)-len(fail),'failures':fail},indent=2))
    return int(bool(result['local']['blocked'] or result['local']['restrictive_page_directives'] or fail))
if __name__=='__main__':raise SystemExit(main())
