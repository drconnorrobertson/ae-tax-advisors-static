'use strict';
// Run with AE_JSDOM_PATH pointing to an installed jsdom package. No network or submissions.
const {JSDOM, VirtualConsole}=require(process.env.AE_JSDOM_PATH || 'jsdom');
const fs=require('fs'),path=require('path'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const specs=[
 ['tools/property-review-prep/index.html','intakeForm','tools/property-review-prep/intake.js'],
 ['cost-segregation-calculator/index.html','cost-seg-scenario','assets/cost-segregation-scenario.js'],
 ['cost-segregation-calculator/index.html','holding-period-form','assets/holding-period-cashflow.js'],
 ['rental-property-sale-tax-calculator/index.html','rental-sale-form','assets/rental-sale-calculator.js']
];
function create(file){const dom=new JSDOM(fs.readFileSync(path.join(root,file),'utf8'),{url:'https://www.aetaxadvisors.com/'+file.replace('index.html',''),runScripts:'outside-only',virtualConsole:new VirtualConsole()});dom.window.HTMLElement.prototype.scrollIntoView=function(){};return dom;}
for(const [file,id,script] of specs){
 let dom=create(file),w=dom.window,f=w.document.getElementById(id);
 assert.equal(f.querySelector('[data-local-controls]').disabled,true);
 assert.equal(Array.from(new w.FormData(f).entries()).length,0);
 for(const input of f.querySelectorAll('input,select,textarea,button')) assert(input.matches(':disabled'),id+' control must be disabled before initialization');
 let submitted=false;f.addEventListener('submit',()=>{submitted=true;});f.querySelector('[type=submit]').click();assert.equal(submitted,false);
 assert.equal(f.querySelectorAll('[name]').length,0,'No named data before JavaScript');
 dom.window.close();
 // Failure while attaching an early listener must leave the input fieldset disabled.
 dom=create(file);w=dom.window;f=w.document.getElementById(id);
 const realAdd=f.addEventListener.bind(f);let attempts=0;
 f.addEventListener=(...args)=>{if(++attempts===2)throw new Error('simulated partial initialization failure');realAdd(...args);};
 assert.throws(()=>w.eval(fs.readFileSync(path.join(root,script),'utf8')));assert(f.querySelector('[data-local-controls]').disabled);assert.equal(Array.from(new w.FormData(f).entries()).length,0);
 assert.notEqual(f.dataset.localInitialized,'true');f.addEventListener=realAdd;
 w.eval(fs.readFileSync(path.join(root,script),'utf8'));assert.equal(f.dataset.localInitialized,'true');
 let reads=0;f.reportValidity=()=>{reads++;return false;};
 const retryEvent=new w.Event('submit',{cancelable:true});f.dispatchEvent(retryEvent);assert(retryEvent.defaultPrevented);
 if(id==='intakeForm'||id==='rental-sale-form')assert.equal(reads,1,'Retry must not retain partial submit listener');
 dom.window.close();
 // Normal initialization, successful calculation, error handling and repeat submission.
 dom=create(file);w=dom.window;f=w.document.getElementById(id);
 let registrations=0;const add=w.EventTarget.prototype.addEventListener;
 w.EventTarget.prototype.addEventListener=function(...args){registrations++;return add.apply(this,args);};
 w.eval(fs.readFileSync(path.join(root,script),'utf8'));const once=registrations;
 w.eval(fs.readFileSync(path.join(root,script),'utf8'));assert.equal(registrations,once,'Double initialization must not add any handlers');
 let toolEvents=0;w.document.addEventListener('ae:tool-complete',()=>toolEvents++);
 assert.equal(f.querySelector('[data-local-controls]').disabled,false);assert.equal(f.querySelector('[type=submit]').disabled,false);
 f.reportValidity=()=>true;
 if(id==='intakeForm'){f.elements.property.value='Property A';f.elements.type.value='Commercial property';f.elements.state.value='PA';f.elements.price.value='500000';f.elements.land.value='100000';}
 if(id==='cost-seg-scenario'){f.elements.eligible.checked=true;f.elements.life.value='39';f.elements.fee.value='3000';}
 if(id==='holding-period-form'){for(const [key,value] of Object.entries({years:'3',fee:'3000',exitTax:'10000',discount:'5',benefits:'20000,-2000,-2000'}))f.elements[key].value=value;}
 if(id==='rental-sale-form')w.document.getElementById('sale-eligible').checked=true;
 function submit(){const ev=new w.Event('submit',{bubbles:true,cancelable:true});assert.equal(f.dispatchEvent(ev),false);assert(ev.defaultPrevented);}
 submit();
 if(id==='intakeForm'){assert(w.document.getElementById('summary').textContent.includes('Property A'));assert.equal(w.document.getElementById('summaryCard').hidden,false);}
 if(id==='cost-seg-scenario')assert(w.document.getElementById('scenario-result').querySelector('dl'));
 if(id==='holding-period-form'){assert(w.document.getElementById('holding-period-result').querySelector('table'));assert.equal(toolEvents,1);}
 if(id==='rental-sale-form')assert.equal(w.document.getElementById('sale-output').hidden,false);
 if(id==='intakeForm'){
  let downloads=0;w.URL.createObjectURL=()=>{downloads++;return 'blob:test';};w.URL.revokeObjectURL=()=>{};w.HTMLAnchorElement.prototype.click=function(){};w.document.getElementById('downloadBtn').click();assert.equal(downloads,1);
  f.elements.land.value='900000';submit();assert(f.elements.land.validationMessage);
  f.elements.land.value='100000';f.elements.land.dispatchEvent(new w.Event('input',{bubbles:true}));
  assert.equal(f.elements.land.validationMessage,'');assert.equal(w.document.getElementById('summaryCard').hidden,true);
  submit();assert.equal(w.document.getElementById('summaryCard').hidden,false);
  f.elements.land.setCustomValidity('test');f.reset();assert.equal(f.elements.land.validationMessage,'');assert.equal(w.document.getElementById('summaryCard').hidden,true);
 }
 // Force a handler failure after activation; preventDefault still executes first.
 if(id==='intakeForm'||id==='rental-sale-form')f.reportValidity=()=>{throw new Error('simulated validation failure');};
 else {const target=w.document.getElementById(id==='cost-seg-scenario'?'scenario-result':'holding-period-result');target.replaceChildren=()=>{throw new Error('simulated rendering failure');};}
 submit();submit();assert.equal(w.location.search,'');
 dom.window.close();console.log('PASS '+id+': no-JS, partial initialization retry, double initialization, normal output, post-init failure, repeat submit');
}
