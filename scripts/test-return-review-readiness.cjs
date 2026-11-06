'use strict';
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const path = require('node:path');
const source = fs.readFileSync(path.join(__dirname, '../assets/return-review-readiness.js'), 'utf8');
class Element {
  constructor() { this.children = []; this.disabled = true; this.handlers = {}; this.textContent = ''; }
  addEventListener(name, fn) { this.handlers[name] = fn; }
  append(child) { this.children.push(child); }
  replaceChildren() { this.children = []; }
  click() { if (!this.disabled) this.handlers.click(); }
}
const groups = Array.from({length:10}, (_, i) => {
  const inputs = ['confirmed', 'review', 'unsure', 'na'].map(value => ({value, checked:false}));
  return {dataset:{topic:'Topic '+i}, inputs, querySelector:() => inputs.find(input => input.checked)};
});
const button = new Element(); const reset = new Element(); const result = new Element();
const root = {querySelectorAll:selector => selector.startsWith('fieldset') ? groups : groups.flatMap(group => group.inputs)};
const document = {getElementById:id => ({'return-readiness':root,'readiness-summary':button,'readiness-reset':reset,'readiness-result':result}[id]),createElement:() => new Element()};
vm.runInNewContext(source,{document});
assert.equal(button.disabled,false); assert.equal(reset.disabled,false);
button.click(); assert.equal(result.children[1].children.length,10);
groups.forEach(group => {group.inputs[0].checked=true;});
button.click(); assert.equal(result.children[1].children.length,0);
groups[0].inputs[0].checked=false; groups[0].inputs[1].checked=true;
button.click(); assert.equal(result.children[1].children.length,1);
button.click(); assert.equal(result.children.length,3); assert.equal(result.children[1].children.length,1);
reset.click(); assert.equal(result.children.length,0); assert.equal(groups.flatMap(group=>group.inputs).some(input=>input.checked),false);
vm.runInNewContext(source,{document:{getElementById:()=>null}});
console.log('PASS: readiness summary, repeat, reset and missing-root behavior');
