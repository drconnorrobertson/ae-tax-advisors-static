const fs=require('fs'),path=require('path'),assert=require('assert');const {JSDOM}=require(process.env.AE_JSDOM_PATH||'jsdom');const root=path.resolve(__dirname,'..');const file='s-corp-tax-savings-calculator/index.html',source=fs.readFileSync(path.join(root,file),'utf8');const dom=new JSDOM(source,{runScripts:'outside-only'}),w=dom.window,d=w.document;w.eval([...source.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(x=>x[1]).find(x=>x.includes('var outputIds=')));
const out=id=>d.getElementById('sc-'+id).textContent;const money=n=>(n<0?'-$':'$')+Math.abs(Math.round(n)).toLocaleString('en-US');
function set(v={}){for(const[id,value]of Object.entries({'sc-profit':'180000','sc-wage':'95000','sc-costs':'3000','sc-filing':'250000','sc-other':'none',...v}))d.getElementById(id).value=value;d.getElementById('sc-profit').dispatchEvent(new w.Event('input'));}
assert.equal(out('net'),'—');set();assert.equal(out('dist'),'$74,733');
function verify(profit,wage,costs,threshold){set({'sc-profit':String(profit),'sc-wage':String(wage),'sc-costs':String(costs),'sc-filing':String(threshold)});const sebase=profit*.9235,se=Math.min(sebase,184500)*.124+sebase*.029+Math.max(sebase-threshold,0)*.009;const pr=Math.min(wage,184500)*.124+wage*.029+Math.max(wage-threshold,0)*.009;const remaining=profit-wage-Math.min(wage,184500)*.062-wage*.0145-costs;assert.equal(out('se'),money(se));assert.equal(out('pr'),money(pr));assert.equal(out('dist'),money(remaining));assert.equal(out('gross'),money(se-pr));assert.equal(out('net'),money(se-pr-costs));}
for(const t of [125000,200000,250000]){verify(500000,300000,5000,t);verify(180000,175000,3000,t);verify(180000,190000,3000,t);}
verify(180000,95000,9000,250000);assert.equal(out('dist'),'$68,733');
verify(0,0,0,250000);assert.equal(out('net'),'$0');
set({'sc-profit':'400','sc-wage':'300','sc-costs':'0'});assert.equal(out('se'),'$0');
for(const other of ['yes','unknown']){set({'sc-other':other});assert.equal(out('net'),'—');}
for(const id of ['sc-profit','sc-wage','sc-costs'])for(const val of ['','-1','invalid']){set({[id]:val});assert.equal(out('net'),'—');}
set({'sc-wage':'0'});assert.equal(out('net'),'—');
set({'sc-wage':'190000'});assert(out('dist').startsWith('-$'));assert(out('verdict').includes('exceed modeled business profit'));
const old=require('child_process').execFileSync('git',['show','f2d5962:'+file],{cwd:root,encoding:'utf8'});
assert.equal(source.match(/<link rel="canonical"[^>]+>/)[0],old.match(/<link rel="canonical"[^>]+>/)[0]);assert.deepEqual([...source.matchAll(/"datePublished"\s*:\s*"([^"]+)"/g)].map(x=>x[1]),[...old.matchAll(/"datePublished"\s*:\s*"([^"]+)"/g)].map(x=>x[1]));
for(const x of old.matchAll(/href="(\/case-studies\/[^\"]+)"/g))assert(source.includes(x[0]));
for(const block of source.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)){const j=JSON.parse(block[1]);if(j['@type']==='FAQPage')for(const q of j.mainEntity){assert(d.body.textContent.includes(q.name));assert(d.body.textContent.includes(q.acceptedAnswer.text));}}
assert(!source.includes('never income tax'));assert(!source.includes('Profit distributed free'));assert.equal(d.getElementById('sc-base').value,'184500');assert(d.getElementById('sc-base').readOnly);w.close();console.log('PASS remaining-profit expense arithmetic, negative profit/no clamp, filing thresholds, additional costs, other-earnings gates, invalid input and FAQ/publication preservation');
