'use strict';
const assert=require('node:assert/strict'),{polish}=require('./ensure-sitewide-polish.cjs');
let s='<html><head><meta name="robots" content="noindex"></head><img src="/assets/ae-tax-logo.png" height="50" loading="eager" fetchpriority="high"><footer>Footer</footer></html>';
let p=polish(s);assert.match(p,/width="50"/);assert.match(p,/decoding="async"/);assert.match(p,/loading="eager"/);assert.match(p,/fetchpriority="high"/);assert.match(p,/content="noindex"/);assert.equal(polish(p),p);
assert.equal(polish('<img src="/assets/ae-tax-logo.png" width="180" height="60" decoding="sync">'),'<img src="/assets/ae-tax-logo.png" width="180" height="60" decoding="sync">');
assert.match(polish('<a href="/cost-seg-estimator/?source=a&amp;ref=b#result">Estimate</a>'),/href="\/cost-segregation-calculator\/\?source=a&amp;ref=b#result"/);
assert.equal(polish('<a href="https://example.com/cost-seg-estimator/">External</a>'),'<a href="https://example.com/cost-seg-estimator/">External</a>');
assert.equal(polish('<a href="#question">Answer</a>'),'<a href="#question">Answer</a>');
console.log('PASS shared image, navigation, redirect query/hash, noindex and idempotence regression cases');
