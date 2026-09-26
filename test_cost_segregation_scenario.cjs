const assert = require('node:assert/strict');
const { estimate } = require('./assets/cost-segregation-scenario.js');
const x = { price: 1000000, land: 20, reclass: 20, life: 27.5, month: 1,
  rate: 32, usable: 100, fee: 3000, eligible: true };
const r = estimate(x);
assert.equal(Math.round(r.additional), 154424);
assert.equal(Math.round(r.net), 46416);
assert.equal(estimate({...x, usable: 0}).benefit, 0);
assert.equal(estimate({...x, usable: 0}).net, -3000);
assert.equal(estimate({...x, land: 100}).basis, 0);
assert.equal(estimate({...x, reclass: 0}).additional, 0);
assert.ok(Math.abs(estimate({...x, month: 12}).without - 800000/27.5/24) < 0.000001);
for (const bad of [{price:-1}, {land:101}, {life:30}, {eligible:false}, {month:1.2}, {fee:NaN}]) {
  assert.throws(() => estimate({...x, ...bad}));
}
console.log('Calculator: 13 numerical and invalid-input checks passed');
