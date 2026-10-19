const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const listeners = {};
const emitted = [];
const frame = {src:'https://api.leadconnectorhq.com/widget/booking/sOAjhMz5kyJbrPJ6tVDm?email=private@example.com'};
const document = {
  documentElement:{},
  addEventListener(name,handler){listeners[name]=handler;},
  dispatchEvent(event){emitted.push(event.detail);},
  querySelectorAll(){return [frame];}
};
const context = {URL,WeakSet,location:new URL('https://www.aetaxadvisors.com/discovery/?email=private@example.com'),
  window:{},document,CustomEvent:class {constructor(name,opts){this.detail=opts.detail;}},
  MutationObserver:class {constructor(handler){this.handler=handler;}observe(){}}};
vm.createContext(context);
const source = fs.readFileSync('assets/booking-events.js','utf8');
vm.runInContext(source,context);
assert.equal(emitted.length,1);
assert.equal(emitted[0].event,'ae_calendar_view');
function click(href){listeners.click({target:{closest:()=>({href})}});}
click('https://www.aetaxadvisors.com/discovery/?email=private@example.com');
click('https://api.leadconnectorhq.com/widget/booking/5bPhybfzi6mKUTgn5GMg?phone=1234567890');
assert.deepEqual(emitted.map(x=>x.event),['ae_calendar_view','ae_booking_cta_click','ae_calendar_open']);
assert.equal(/private|1234567890|email=|phone=/.test(JSON.stringify(emitted)),false);
click('https://example.com/widget/booking/fake');
click('javascript:alert(1)');
assert.equal(emitted.length,3);
assert.equal(listeners.message,undefined,'Untrusted iframe messages must not create booking completions');
vm.runInContext(source,context);
assert.equal(emitted.length,3,'Repeated initialization must not emit duplicate views');
assert.equal(context.window.dataLayer.length,3);
console.log('Booking hooks: events, privacy, destination restrictions and duplicate-init checks passed.');
