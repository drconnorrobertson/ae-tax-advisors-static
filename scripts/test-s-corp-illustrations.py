#!/usr/bin/env python3
"""Independent math, FAQ parity, source and preservation checks; no build.

--output-root can inspect staged output. --baseline-ref preserves publication,
fees, historical examples and tables against a git revision. The optional
--reviewed-baseline-root verifies this pass preserves earlier reviewed copy.
"""
import argparse
import ast
from decimal import Decimal as D, ROUND_HALF_UP
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit
from tax_review_build_normalization import normalize_baseline_html

REPO = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--output-root', type=Path, default=REPO)
p.add_argument('--policy-root', type=Path, default=REPO)
p.add_argument('--built-output', action='store_true', help='Allow only the exact documented release presentation/link transforms.')
p.add_argument('--baseline-ref', default='f2d5962')
p.add_argument('--reviewed-baseline-root', type=Path)
a = p.parse_args()
ROOT, POLICY = a.output_root.resolve(), a.policy_root.resolve()
cohort = json.loads((REPO / 'content/s-corp-illustrations-20261106.json').read_text())
routes = [r for group in cohort['groups'].values() for r in group]
assert len(routes) == len(set(routes)) == 5
assert [len(v) for v in cohort['groups'].values()] == [4, 1]
assert cohort['reviewed_date'] == '2026-11-06'
assert all(r.startswith('/') and r.endswith('/') and '/case-studies/' not in r for r in routes)
assert all(urlsplit(u).hostname in ('www.irs.gov', 'www.ssa.gov', 'www.ftb.ca.gov') for u in cohort['sources'])
ENTITY, HNW, LATE, REFUND, COMPARE = routes

# Deliberately separate from any site calculator/generator. IRS Schedule SE
# line 4a and lines 7-12, Publication 15, Topic 560 and SSA historical bases.
BASES = {2024:D('168600'), 2025:D('176100'), 2026:D('184500')}
def se(profit, year=2026, threshold='200000'):
    net = D(profit) * D('0.9235')
    social = min(net, BASES[year]) * D('0.124')
    medicare = net * D('0.029')
    additional = max(D(0), net - D(threshold)) * D('0.009')
    return {'net':net, 'social':social, 'medicare':medicare,
            'schedule_se':social+medicare, 'additional':additional,
            'total':social+medicare+additional}
def payroll(wages, year=2026, threshold='200000'):
    wage = D(wages)
    fica = min(wage, BASES[year]) * D('0.124') + wage * D('0.029')
    additional = max(D(0), wage - D(threshold)) * D('0.009')
    return {'fica':fica, 'additional':additional, 'total':fica+additional, 'employer':fica/2}
def money(n, digits=2):
    return f'${n:,.{digits}f}'

assert se('1000000')['schedule_se'] == D('49659.50')
assert se('1000000')['total'] == D('56171')
assert payroll('600000')['total'] == D('43878')
assert se('1000000')['total'] - payroll('600000')['total'] == D('12293')
assert se('500000')['net'] == D('461750')
assert se('500000')['schedule_se'] == D('36268.75')
assert se('500000')['additional'] == D('2355.75')
assert se('500000')['total'] == D('38624.50')
assert [payroll(w)['total'] for w in ['700000','600000','400000']] == list(map(D,['47678','43878','36278']))
assert payroll('700000')['total'] - payroll('400000')['total'] == D('11400')
assert se('300000')['total'] - payroll('130000')['total'] == D('11715.90')
assert se('300000')['total'] - payroll('100000')['total'] == D('16305.90')
# Prevent the 2026 correction from being silently applied to a historical year.
assert se('300000',2024)['total'] - payroll('130000',2024)['total'] == D('9744.30')
assert se('300000',2024)['total'] - payroll('100000',2024)['total'] == D('14334.30')
assert se('200000')['total'] == D('28234.30')
assert payroll('100000')['total'] == D('15300')
assert se('200000')['total'] - payroll('100000')['total'] == D('12934.30')
assert D('200000') - D('100000') - payroll('100000')['employer'] == D('92350')
assert D('1000000') - D('600000') - payroll('600000')['employer'] == D('379861')

# Verify rounded cells in the existing MFJ table without rewriting that table.
for profit,wages,expected in [
 ('60000','40000',['8478','6120','2358','-642']),
 ('100000','60000',['14130','9180','4950','1950']),
 ('180000','95000',['25433','14535','10898','7898']),
 ('350000','150000',['32911','22950','9961','6961']),
 ('700000','220000',['45193','29258','15935','12935'])]:
    st=se(profit,threshold='250000')['total'];pt=payroll(wages,threshold='250000')['total']
    actual=[v.quantize(D(1),rounding=ROUND_HALF_UP) for v in [st,pt,st-pt,st-pt-D(3000)]]
    assert actual == list(map(D,expected)), (profit,actual)

# IRS Notice 2025-67 limits; catch-up amounts are alternatives, not additive.
assert D('24500') + D('47500') == D('72000')
assert D('72000') + D('8000') == D('80000')
assert D('72000') + D('11250') == D('83250')

def baseline(path):
    value = subprocess.check_output(['git','show',a.baseline_ref+':'+path],cwd=REPO,text=True)
    return normalize_baseline_html(value, POLICY, route="/" + path.removesuffix("index.html")) if a.built_output else value
def normalize(value):
    return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',value))).strip()
def walk(x):
    if isinstance(x,dict):
        yield x
        for v in x.values():yield from walk(v)
    elif isinstance(x,list):
        for v in x:yield from walk(v)
def schemas(s):
    return list(walk([json.loads(x) for x in re.findall(r'<script\b[^>]*type=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script>',s,re.S)]))
def matches(pattern,route):
    if pattern=='/(.*)':return True
    if ':' in pattern:
        prefix=pattern.split(':',1)[0]
        return route.startswith(prefix) or (pattern.endswith('*') and route.rstrip('/')==prefix.rstrip('/'))
    return pattern.rstrip('/')==route.rstrip('/')

class Page(HTMLParser):
    def __init__(self,s):
        super().__init__();self.canonical=[];self.h1=0;self.indexable=True;self.feed(s)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1':self.h1+=1
        if tag=='link' and 'canonical' in a.get('rel','').split():self.canonical.append(a.get('href'))
        if tag=='meta' and a.get('name','').lower() in ('robots','googlebot') and 'noindex' in a.get('content','').lower():self.indexable=False
        if tag=='meta' and a.get('http-equiv','').lower()=='refresh':self.indexable=False

config=json.loads((POLICY/'vercel.json').read_text())
holds=json.loads((POLICY/'discovery_review_holds.json').read_text())
pages={};faq_count=0
for route in routes:
    path=route.strip('/')+'/index.html'
    current=(ROOT/path).read_text();old=baseline(path);pages[route]=current
    view=Page(current)
    assert view.canonical==['https://www.aetaxadvisors.com'+route]==Page(old).canonical,route
    assert view.h1==1 and view.indexable,route
    assert route not in holds,route
    assert not any(matches(x['source'],route) for x in config.get('redirects',[])),route
    for rule in config.get('headers',[]):
        if matches(rule['source'],route):
            assert not any(h['key'].lower()=='x-robots-tag' and 'noindex' in h['value'].lower() for h in rule['headers']),route
    objects=schemas(current);old_objects=schemas(old)
    assert [o['datePublished'] for o in objects if 'datePublished' in o]==[o['datePublished'] for o in old_objects if 'datePublished' in o],route
    assert re.findall(r'<meta[^>]*property="article:published_time"[^>]*>',current)==re.findall(r'<meta[^>]*property="article:published_time"[^>]*>',old),route
    assert set(o['dateModified'] for o in objects if 'dateModified' in o)=={cohort['reviewed_date']},route
    # Table numbers, historic case links, fee amounts, layout and navigation
    # survive. Only educational illustrations are permitted to change numbers.
    for tag in ('table','blockquote','header','footer'):
        assert re.findall(fr'<{tag}\b[^>]*>.*?</{tag}>',current,re.S)==re.findall(fr'<{tag}\b[^>]*>.*?</{tag}>',old,re.S),(route,tag)
    for link in re.findall(r'<a\b[^>]*>.*?</a>',old,re.S):
        assert current.count(link)>=old.count(link),(route,'original link',link)
    visible=normalize(re.sub(r'<script\b[^>]*>.*?</script>','',current,flags=re.S))
    old_questions={o['name'] for o in old_objects if o.get('@type')=='Question'}
    questions=[o for o in objects if o.get('@type')=='Question']
    assert old_questions=={o['name'] for o in questions},route
    for q in questions:
        assert normalize(q['name']) in visible and normalize(q['acceptedAnswer']['text']) in visible,(route,'FAQ parity',q['name'])
        faq_count+=1
    if route in cohort['groups']['employment_tax_examples']:
        for phrase in ('2026','filing single','no other wages','hypothetical gross employment-tax comparisons','not documented client outcomes','QBI','state taxes','unemployment taxes','compliance costs'):
            assert phrase in visible,(route,phrase)
        for url in cohort['sources'][:5]:assert url in current,(route,url)
    # Earlier generic-copy correction must remain present.
    assert 'Income-tax results can also change, including through the Section 199A' in current,route

for value in ['56,171','49,659.50','6,511.50','43,878','12,293','379,861','461,750','36,268.75','2,355.75','38,624.50']:
    assert '$'+value in pages[ENTITY],value
for stale in ['$153,000','$91,800','$61,200','$70,748','$76,500','creating a 50% marginal','within the first month','IRS will accept if audited','20% to 30% of revenue','on or before December 31']:
    assert stale not in pages[ENTITY],stale
# Explicit professional-fee preservation, distinct from tax-benefit numbers.
assert '$1,500 to $3,000' in pages[ENTITY]
original_comparison = baseline(COMPARE.strip('/')+'/index.html')
price_paragraph = next(x for x in re.findall(r'<p\b[^>]*>.*?</p>', original_comparison, re.S)
                       if x.startswith('<p>Realistic annual cost is'))
assert price_paragraph in pages[COMPARE], 'return/payroll fee ranges changed'
protected_changes = subprocess.check_output(['git', 'diff', '--name-only', a.baseline_ref,
    '--', 'case-studies', 'case_engine.py', 'case_data.py'], cwd=REPO, text=True)
assert not protected_changes, 'historical cases or case generators changed'
assert 'Multi-entity reconciliation workpaper:' in pages[ENTITY]
assert 'Without those inputs, no annual savings amount can be supported.' in pages[ENTITY]
assert 'Section 1402(a)(13)' in pages[ENTITY]
assert 'two months and 15 days' in pages[ENTITY]
assert 'no more than 100 shareholders' in pages[ENTITY]
for value in ['47,678','43,878','36,278','11,400','21,589','20,139','17,239','778,411','879,861','1,082,761','24,500','72,000','360,000','8,000','11,250','150,000','290,000']:
    assert '$'+value in pages[HNW],value
for stale in ['$107,100','$91,800','$61,200','$45,900','$163,500','$140,000','$277,000','$225,000','additional $80,000 to $100,000+','25% of $560,000','for 2024). The employer']:
    assert stale not in pages[HNW],stale
for phrase in ['not distributions or remaining pass-through profit','not a contribution or deduction limit','Roth catch-up contributions do not provide a current income-tax deduction','not an additional amount on top of the ordinary catch-up','eligible common-law employees','related businesses','There is no 50% to 60% of profit safe harbor']:
    assert phrase in pages[HNW],phrase
for value in ['31,605.90','30,912.45','693.45','11,715.90','16,305.90']:
    assert '$'+value in pages[LATE],value
assert '$20,000 or more annually' not in pages[LATE]
assert '2024 threshold' not in pages[LATE]
assert 'amended returns automatically cure inconsistent reporting' in pages[LATE]
for value in ['28,234.30','15,300','12,934.30','7,650','92,350']:
    assert '$'+value in pages[REFUND],value
assert 'savings can exceed $15,000' not in pages[REFUND]
assert 'pays self-employment tax only on the reasonable salary' not in pages[REFUND]
assert 'not a prior-year refund amount' in pages[REFUND]
assert 'married filing jointly' in pages[COMPARE]
assert 'a spouse with no wages or self-employment income' in pages[COMPARE]
assert 'not a complete net tax benefit or a fee quote' in pages[COMPARE]

# Historical 2025 service example is outside the correction. Preserve its dollar
# sequence/tables even when another reviewed change corrects unrelated prose.
service='services/s-corp-election/index.html'
old_service=baseline(service);new_service=(ROOT/service).read_text()
dollars=lambda s:re.findall(r'\$[\d,.]+',s)
assert dollars(old_service)==dollars(new_service),'historical service values changed'
assert re.findall(r'<table\b.*?</table>',old_service,re.S)==re.findall(r'<table\b.*?</table>',new_service,re.S),'historical service table changed'

# Parse active generator data without executing any site generator.
modules={f:ast.parse((REPO/f).read_text()) for f in ['build_tools.py','cluster_c1.py','content_posts_a.py','content_posts_c.py','seo_topics.py']}
posts=next(ast.literal_eval(x.value) for x in modules['content_posts_c.py'].body if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='POSTS' for t in x.targets))
comparison=next(x for x in posts if x['slug']=='s-corp-vs-llc-tax-comparison-2026')
disclosure=next(s for _,blocks in comparison['sections'] for s in blocks if s.startswith('Table assumptions:'))
assert disclosure in pages[COMPARE]
shared_answer='There is no fixed savings percentage. Compare Schedule SE tax after the 92.35% net-earnings adjustment with both employer and employee payroll taxes on supportable wages, accounting for the Social Security wage base, other earnings, filing status, and Additional Medicare Tax. Then model income-tax/QBI effects, state taxes, unemployment taxes, and compliance costs to estimate a net benefit.'
assert shared_answer in (REPO/'seo_topics.py').read_text()
for route in cohort['groups']['employment_tax_examples']:
    for question in schemas(pages[route]):
        if question.get('@type')=='Question' and question['name']=='How much does an S-Corp election save?':
            assert question['acceptedAnswer']['text']==shared_answer

# Review follow-up: no flat-rate shortcut, automatic midyear conversion/loss
# benefit, distribution deferral, state wage advantage, or deduction reversal.
assert 'marginal benefit per dollar shifted drops from' not in pages[COMPARE]
assert 'There is no fixed savings percentage.' in pages[COMPARE]
assert 'Owner W-2 compensation is not QBI' in pages[COMPARE]
assert 'phase in over the applicable range' in pages[COMPARE]
assert 'not a separate short-year sole-proprietor return' in pages[LATE]
assert 'cannot simply divide that year by choosing a mid-year S election' in pages[LATE]
assert 'Losses are not automatically deductible against other income' in pages[LATE]
assert 'basis, at-risk, passive-activity, and excess-business-loss' in pages[LATE]
assert 'it does not amplify the refund' in pages[REFUND]
assert 'Additional Medicare Tax is not included in this half-SE-tax deduction' in pages[REFUND]
assert 'delaying a distribution does not defer that pass-through income' in pages[HNW]
assert 'debt basis does not support a tax-free distribution' in pages[HNW]
assert 'There is no general rule that replacing an S-Corp distribution with W-2 wages lowers California personal income tax' in pages[HNW]
assert 'does not automatically reduce reasonable compensation' in pages[HNW]
for stale in ['which face employment taxes but less state income tax burden', 'lowering the reasonable compensation base', 'amplifies the refund', 'it eliminates the compliance burden of amending multiple years']:
    assert all(stale not in page for page in pages.values()), stale

# Restore only the specifically reviewed comparison-page replacements when
# checking against the earlier generic-copy baseline. Everything else, including
# all table values and all professional-fee wording, remains byte-identical.
comparison_replacements = [['It saves 15.3% self-employment tax on the profit characterized as distribution rather than wages, up to the Social Security wage base, and 2.9% to 3.8% above it. On $180,000 of profit with a $95,000 reasonable wage, the gross saving is roughly $10,900 before compliance costs of $2,000 to $4,000.', "There is no fixed savings percentage. Under the table's 2026 married-filing-jointly assumptions, $180,000 of profit and an assumed $95,000 wage produce roughly $10,900 of gross employment-tax savings before compliance costs of $2,000 to $4,000. Actual net benefit requires a supportable salary and modeling of remaining business profit after employer payroll taxes, income-tax/QBI effects, state taxes, and unemployment taxes."], ['Two patterns are visible. Below roughly $60,000 of profit, the compliance cost exceeds the saving. And the saving does not scale linearly, because above the Social Security wage base only the Medicare portion is at stake, so the marginal benefit per dollar shifted drops from 15.3% to 2.9% or 3.8%.', 'At the $60,000 profit and $40,000 wage assumptions shown, the illustrative compliance cost exceeds the gross saving. This is not a universal breakeven point. Savings depend on the 92.35% self-employment net-earnings adjustment, supportable wages, the Social Security wage base, other earnings, filing status, and applicable Medicare taxes. Calculate both tax regimes separately rather than multiplying an assumed distribution by a flat rate.'], ['Below the taxable income thresholds, the deduction is simply 20% of QBI and W-2 wages are irrelevant. Above the thresholds, the deduction is limited to the greater of 50% of W-2 wages, or 25% of W-2 wages plus 2.5% of the unadjusted basis of qualified property.', 'The deduction is generally up to 20% of QBI, subject to limits including taxable income less net capital gain. Owner W-2 compensation is not QBI, and deductible employer payroll costs can reduce QBI even below the taxable-income thresholds. The wage-and-property limitations phase in over the applicable range above those thresholds; they do not switch on in full immediately.'], ['For a specified service trade or business, including health, law, accounting, consulting, athletics, financial services, and any business whose principal asset is the reputation or skill of its employees or owners, the deduction phases out entirely above the thresholds regardless of wages.', 'For a specified service trade or business, such as many health, law, accounting, consulting, or financial-service businesses, Section 199A eligibility phases out over the applicable taxable-income range. Above that range, an owner generally cannot claim a QBI deduction from the specified service business, even if it pays W-2 wages. Check the actual business classification and current-year thresholds.'], ['For non-service businesses above the thresholds, wages are the constraint on the deduction. Reducing your W-2 wage to save payroll tax can reduce the 199A deduction by more than the payroll tax saved. This is the single most common modeling error we correct on new engagements, and it flips the answer at higher income levels.', 'For a business that is not a specified service trade or business, the fully applicable limitation generally uses the greater of 50% of W-2 wages or 25% of W-2 wages plus 2.5% of qualifying property basis. Reducing owner wages can lower this limit while also changing QBI, so payroll-tax and income-tax effects must be modeled together. A lower salary does not automatically improve the total tax result.']]
if a.reviewed_baseline_root:
    before=(a.reviewed_baseline_root/COMPARE.strip('/')/'index.html').read_text()
    comparison_source=(REPO/COMPARE.strip('/')/'index.html').read_text()
    restored=comparison_source.replace('<p>'+disclosure+'</p>\n            ','')
    for old,new in comparison_replacements:
        restored=restored.replace(new,old)
    assert restored==before
    for f in ['build_tools.py','cluster_c1.py','content_posts_a.py']:
        assert (REPO/f).read_bytes()==(a.reviewed_baseline_root/f).read_bytes(),f
    before_c=(a.reviewed_baseline_root/'content_posts_c.py').read_text()
    restored_c=(REPO/'content_posts_c.py').read_text().replace('  "'+disclosure+'",\n','')
    for old,new in comparison_replacements:
        restored_c=restored_c.replace(new,old)
    assert restored_c==before_c

print(f'PASS: 5 pages; 4 independent employment-tax examples; 5 MFJ table rows; {faq_count} FAQ answers; retirement limits; publication, fee, table, historical service and prior-copy preservation.')
