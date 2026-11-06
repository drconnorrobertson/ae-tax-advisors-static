const fs=require('fs'),path=require('path'),assert=require('assert');
const {JSDOM}=require(process.env.AE_JSDOM_PATH||'jsdom');
const root=path.resolve(__dirname,'..');const source=fs.readFileSync(path.join(root,'bonus-depreciation-calculator/index.html'),'utf8');
const dom=new JSDOM(source,{runScripts:'outside-only'}),w=dom.window,d=w.document;
const script=[...source.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(x=>x[1]).find(x=>x.includes("function number(id, max)"));assert(script);w.eval(script);
function set(values={}){const defaults={'bd-cost':'250000','bd-life':'5','bd-business':'100','bd-income':'400000','bd-rate':'37','bd-other':'0','bd-type':'equipment','bd-acquired':'2026-03-01','bd-service':'2026-03-01','bd-qualified':'yes'};for(const [id,v]of Object.entries({...defaults,...values}))d.getElementById(id).value=v;d.getElementById('bd-cost').dispatchEvent(new w.Event('input'));}
const out=id=>d.getElementById('bd-'+id).textContent;
function withheld(v){set(v);assert.equal(out('value'),'—');}
assert.equal(out('value'),'—','unconfirmed default must not advertise a benefit');
for(const use of ['0','50','51','100']){set({'bd-business':use});assert.equal(out('basis'),'$'+Math.round(250000*Number(use)/100).toLocaleString('en-US'));if(use==='0'){for(const id of ['bonus','179','macrs','value'])assert.equal(out(id),'$0');}if(use==='50')assert.equal(out('179'),'$0');}
for(const use of ['', '-1','101','not a number'])withheld({'bd-business':use});
for(const id of ['bd-cost','bd-income','bd-rate','bd-other'])for(const value of ['','-1','invalid'])withheld({[id]:value});
for(const use of ['50','49']){set({'bd-type':'listed','bd-business':use});assert.equal(out('bonus'),'$0');assert.equal(out('179'),'$0');assert.equal(out('macrs'),'—');assert.equal(out('value'),'—');}
for(const use of ['51','100']){set({'bd-type':'listed','bd-business':use});assert.notEqual(out('bonus'),'—');assert.notEqual(out('bonus'),'$0');}
for(const type of ['vehicle','building','unknown'])withheld({'bd-type':type});
for(const life of ['27.5','39'])withheld({'bd-life':life});
for(const type of ['qip','land-improvement']){withheld({'bd-type':type});set({'bd-type':type,'bd-life':'15'});assert.equal(out('bonus'),'$250,000');if(type==='land-improvement')assert.equal(out('179'),'$0');else assert.equal(out('macrs'),'$8,333');}
for(const life of ['3','5','7','15','20']){set({'bd-life':life});assert.equal(out('bonus'),'$250,000');}
for(const v of [{'bd-acquired':''},{'bd-service':''},{'bd-acquired':'2025-01-19'},{'bd-service':'2025-12-31'},{'bd-service':'2027-01-01'},{'bd-acquired':'2026-04-01'},{'bd-qualified':'no'},{'bd-qualified':'unknown'}])withheld(v);
for(const dates of [{'bd-acquired':'2025-01-20','bd-service':'2026-01-01'},{'bd-acquired':'2026-12-31','bd-service':'2026-12-31'}]){set(dates);assert.equal(out('bonus'),'$250,000');}
set({'bd-income':'0'});assert.equal(out('179'),'$0');assert.equal(out('bonus'),'$250,000');
set({'bd-rate':'0'});assert.equal(out('value'),'$0');
set({'bd-other':'6400000'});assert.equal(out('179'),'$0');
// Mixed-use qualifying cost, annual investment thresholds, and income cap.
set({'bd-cost':'5000000','bd-business':'60','bd-income':'10000000'});assert.equal(out('basis'),'$3,000,000');assert.equal(out('179'),'$2,560,000');
set({'bd-cost':'4090000','bd-income':'10000000'});assert.equal(out('179'),'$2,560,000');
set({'bd-cost':'4090001','bd-income':'10000000'});assert.equal(out('179'),'$2,559,999');
set({'bd-cost':'6650000','bd-income':'10000000'});assert.equal(out('179'),'$0');
set({'bd-cost':'5000000','bd-business':'60','bd-income':'10000000','bd-other':'3650000'});assert.equal(out('179'),'$0');
set({'bd-cost':'5000000','bd-business':'60','bd-income':'750000'});assert.equal(out('179'),'$750,000');
assert(source.includes('Other qualifying Section 179 business-use cost'));
const old=require('child_process').execFileSync('git',['show','f2d5962:bonus-depreciation-calculator/index.html'],{cwd:root,encoding:'utf8'});
assert.deepEqual([...source.matchAll(/"datePublished"\s*:\s*"([^"]+)"/g)].map(x=>x[1]),[...old.matchAll(/"datePublished"\s*:\s*"([^"]+)"/g)].map(x=>x[1]));
assert.equal(source.match(/<link rel="canonical"[^>]+>/)[0],old.match(/<link rel="canonical"[^>]+>/)[0]);
for(const x of old.matchAll(/href="(\/case-studies\/[^\"]+)"/g))assert(source.includes(x[0]));
for(const block of source.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)){const j=JSON.parse(block[1]);if(j['@type']==='FAQPage')for(const q of j.mainEntity){assert(d.body.textContent.includes(q.name));assert(d.body.textContent.includes(q.acceptedAnswer.text));}}
assert(source.includes('article:modified_time" content="2026-11-06'));
dom.window.close();console.log('PASS input boundaries, listed-use tests, property classes, date gates, income/phaseout, FAQ parity and publication/case/canonical preservation');
