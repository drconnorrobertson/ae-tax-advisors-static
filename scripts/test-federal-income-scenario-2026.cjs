'use strict';
const assert=require('node:assert/strict'),fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'..'),model=require('../assets/federal-income-scenario-2026.js');
const {JSDOM}=require(process.env.AE_JSDOM_PATH||'jsdom');
// Independent IRS schedule threshold/tax fixtures, Rev. Proc. 2025-32 section 4.01.
const fixtures={single:[[12400,1240],[50400,5800],[105700,17966],[201775,41024],[256225,58448],[640600,192979.25]],mfj:[[24800,2480],[100800,11600],[211400,35932],[403550,82048],[512450,116896],[768700,206583.50]],mfs:[[12400,1240],[50400,5800],[105700,17966],[201775,41024],[256225,58448],[384350,103291.75]],hoh:[[17700,1770],[67450,7740],[105700,16155],[201750,39207],[256200,56631],[640600,191171]]};
const rates=[.10,.12,.22,.24,.32,.35,.37];const close=(a,b)=>assert(Math.abs(a-b)<1e-7,`${a} != ${b}`);
for(const [status,points]of Object.entries(fixtures)){
 close(model.ordinaryTax(0,status),0);
 points.forEach(([income,tax],i)=>{close(model.ordinaryTax(income,status),tax);close(model.ordinaryTax(income-1,status),tax-rates[i]);close(model.ordinaryTax(income+1,status),tax+rates[i+1]);});
 close(model.ordinaryTax(1000000,status),points[5][1]+(1000000-points[5][0])*.37);
 const equal=model.compare({status,income:1000000,mode:'standard',change:0});close(equal.difference,0);close(equal.baseline,1000000-model.standard[status]);
 const excess=model.compare({status,income:100,mode:'taxable',change:500});assert.equal(excess.proposed,0);assert.equal(excess.unusedReduction,400);assert.equal(excess.difference,10);
}
assert.deepEqual(model.standard,{single:16100,mfj:32200,mfs:16100,hoh:24150});
for(const bad of [-1,NaN,Infinity,'',null,1e12+1]){assert.throws(()=>model.ordinaryTax(bad,'single'));assert.throws(()=>model.compare({status:'single',income:100,mode:'taxable',change:bad}));}
assert.throws(()=>model.ordinaryTax(100,'invalid'));assert.throws(()=>model.compare({status:'single',income:100,mode:'reviewed',deduction:NaN,change:0}));
close(model.compare({status:'single',income:100000,mode:'reviewed',deduction:20000,change:10000}).baseline,80000);
for(const route of ['tax-savings-calculator','business-owner-tax-calculator']){
 const source=fs.readFileSync(path.join(root,route,'index.html'),'utf8'),script=fs.readFileSync(path.join(root,'assets/federal-income-scenario-2026.js'),'utf8');
 assert(source.includes('$7,800')&&source.includes('$3,900')&&source.includes('30 days apart'));
 const plain=new JSDOM(source).window.document;
 const published=route==='tax-savings-calculator'?'2026-01-06':'2026-10-03';
 let foundDate=false;
 for(const node of plain.querySelectorAll('script[type="application/ld+json"]')){
  const data=JSON.parse(node.textContent);
  if(data.datePublished){assert.equal(data.datePublished,published);foundDate=true;}
  if(data.dateModified)assert.equal(data.dateModified,'2026-11-06');
  if(data['@type']==='FAQPage')for(const q of data.mainEntity){assert(plain.body.textContent.includes(q.name));assert(plain.body.textContent.includes(q.acceptedAnswer.text));}
  if(data['@type']==='WebApplication')assert(data.description.includes('No assumed strategy eligibility'));
 }
 assert(foundDate);assert.equal(plain.querySelectorAll('h1').length,1);
 assert.equal(plain.querySelector('link[rel=canonical]').href,'https://www.aetaxadvisors.com/'+route+'/');
 const dom=new JSDOM(source,{runScripts:'outside-only',url:'https://www.aetaxadvisors.com/'+route+'/'}),w=dom.window,d=w.document,f=d.querySelector('form[data-federal-scenario]');
 assert(f.querySelector('fieldset').disabled);assert.equal([...new w.FormData(f)].length,0);assert.equal(f.querySelectorAll('[name]').length,0);
 let added=0;const add=f.addEventListener.bind(f);f.addEventListener=(...args)=>{added++;return add(...args);};
 w.eval(script);const first=added;w.eval(script);assert.equal(first,added);assert(!f.querySelector('fieldset').disabled);
 const set=(id,value)=>{d.getElementById(id).value=value;};const submit=()=>{const e=new w.Event('submit',{cancelable:true});assert.equal(f.dispatchEvent(e),false);assert(e.defaultPrevented);};
 d.getElementById('federal-confirm').checked=true;
 set('federal-income','1000000');submit();assert.equal(d.getElementById('federal-result').querySelector('dd:last-of-type').textContent,'$0.00');
 assert(!/amendmentRecovery|firstYearBenefit|cbContrib|estimatedPropertyValue|runCalculator|calculateSavings/.test(source));
 set('federal-income','100000');set('federal-change','10000');submit();assert.equal(d.getElementById('federal-result').querySelector('dd:last-of-type').textContent,'$2,200.00');
 set('federal-income','');submit();assert(d.getElementById('federal-error').textContent);assert(d.getElementById('federal-result').hidden);
 set('federal-income','-1');submit();assert(d.getElementById('federal-error').textContent);
 set('federal-income','0');submit();assert(!d.getElementById('federal-result').hidden);
 set('federal-income','100');set('federal-change','500');submit();assert(d.getElementById('federal-result').textContent.includes('$400.00'));
 f.dispatchEvent(new w.Event('input',{bubbles:true}));assert(d.getElementById('federal-result').hidden);f.reset();assert.equal(d.getElementById('federal-change').value,'0');
 assert.equal(w.location.search,'');dom.window.close();console.log('PASS '+route+': no-JS privacy, initialized/double-init, old $1M scenario, blank/negative/zero/excess, input/reset');
}
console.log('PASS all 2026 bracket boundaries, filing statuses, standard deductions, high income and invalid-input fixtures');
