'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {ensureSharedUx} = require('./ensure-shared-ux.cjs');
const header = `<header><button class="mobile-toggle" aria-controls="primary-nav" aria-expanded="false" onclick="var n=document.querySelector('.nav-links');var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o);this.setAttribute('aria-label',o?'Close menu':'Open menu');">Menu</button><nav id="primary-nav" class="nav-links"><div class="nav-dropdown"><a class="nav-link" href="/services/">Services</a><div class="dropdown-content"><a href="/pricing/">Pricing</a></div></div></nav></header>`;
const fixture = `<html><head></head><body>${header}<main><table><caption>Example</caption><tr><td>Wide data</td></tr></table></main></body></html>`;
const enhanced = ensureSharedUx(fixture);
assert.match(enhanced, /<script defer src="\/assets\/site-ux.js" data-ae-navigation-only="true"><\/script>/);
assert.equal(ensureSharedUx(enhanced), enhanced);
assert.ok(enhanced.includes(header), 'inline handler and header unchanged');
for (const untouched of [fixture.replace(header, ''), fixture.replace('aria-controls="primary-nav"','aria-controls="other"'), fixture.replace('id="primary-nav"','id="other"'), fixture.replace('</head>', '<script defer src="/assets/site-ux.js?v=1"></script></head>')]) assert.equal(ensureSharedUx(untouched), untouched);
const root = path.resolve(__dirname, '..');
const discovery = fs.readFileSync(path.join(root, 'discovery/index.html'), 'utf8');
assert.equal(ensureSharedUx(discovery), discovery, 'no-header discovery unchanged');
console.log('PASS build fixtures: gated injection, idempotence, inline preservation, existing version, no-header discovery');
// DOM tests use an optional development-only jsdom installation, never shipped.
const jsdomPath = process.env.AE_JSDOM_PATH;
if (!jsdomPath) { console.log('DOM tests require AE_JSDOM_PATH pointing to a local jsdom installation'); process.exit(0); }
const {JSDOM} = require(jsdomPath);
const dom = new JSDOM(enhanced, {url:'https://www.aetaxadvisors.com/', runScripts:'dangerously'});
const {window:w} = dom; const d=w.document;
let onBreakpoint;
w.matchMedia = () => ({matches:true, addEventListener:(name,fn)=>{onBreakpoint=fn;}});
Object.defineProperty(w.HTMLElement.prototype, 'clientWidth', {get(){return 320;}});
Object.defineProperty(w.HTMLElement.prototype, 'scrollWidth', {get(){return this.classList.contains('ae-table-scroll') ? 640 : 320;}});
const source=fs.readFileSync(path.join(root,'assets/site-ux.js'),'utf8');
const executionTag=d.querySelector('script[src="/assets/site-ux.js"]');
Object.defineProperty(d, 'currentScript', {configurable:true,get:()=>executionTag});
w.eval(source);
const button=d.querySelector('.mobile-toggle'),menu=d.querySelector('#primary-nav'),sub=d.querySelector('.mobile-submenu-toggle');
button.click(); assert.ok(menu.classList.contains('open')); assert.equal(button.getAttribute('aria-expanded'),'true');
sub.click(); assert.equal(sub.getAttribute('aria-expanded'),'true'); assert.ok(d.querySelector('.nav-dropdown').classList.contains('submenu-open'));
sub.click(); assert.equal(sub.getAttribute('aria-expanded'),'false');
sub.click(); d.dispatchEvent(new w.KeyboardEvent('keydown',{key:'Escape',bubbles:true}));
assert.ok(!menu.classList.contains('open')); assert.equal(d.activeElement,button); assert.equal(sub.getAttribute('aria-expanded'),'false');
button.click();d.querySelector('main').click();assert.ok(!menu.classList.contains('open'));
button.click();sub.click();onBreakpoint();assert.ok(!menu.classList.contains('open'));assert.equal(sub.getAttribute('aria-expanded'),'false');
assert.equal(d.querySelectorAll('.skip-link').length,1);assert.equal(d.querySelector('.skip-link').getAttribute('href'),'#main-content');assert.equal(d.querySelector('main').tabIndex,-1);
assert.equal(d.querySelectorAll('.ae-table-scroll').length,1);assert.equal(d.querySelector('.ae-table-scroll').tabIndex,0);assert.equal(d.querySelector('.ae-table-scroll').getAttribute('role'),'region');
w.dispatchEvent(new w.Event('resize'));w.eval(source);
assert.equal(d.querySelectorAll('.ae-table-scroll').length,1);assert.equal(d.querySelectorAll('.mobile-submenu-toggle').length,1);assert.equal(d.querySelectorAll('.skip-link').length,1);
button.click();button.click();assert.ok(!menu.classList.contains('open'),'no double-toggle handler added');
console.log('PASS DOM: menu, submenu, Escape/focus, outside click, breakpoint reset, skip link, accessible tables, repeated initialization');
w.close();
// Exercise the appended filter in real script executions, including its DOM-ready callback.
for (const route of ['how-to-fire-your-cpa','irs-audit-defense-business-owners','switching-cpas-mid-year-guide']) {
  for (const navigationOnly of [true,false]) {
    const tag = navigationOnly ? ' data-ae-navigation-only="true"' : '';
    const page = new JSDOM(`<html><head></head><body><a id="representation" href="/tax-compliance-irs-representation/">Representation</a><a id="other" href="/pricing/">Pricing</a><script${tag}>${source}</script></body></html>`, {url:`https://www.aetaxadvisors.com/${route}/`,runScripts:'dangerously'});
    page.window.document.dispatchEvent(new page.window.Event('DOMContentLoaded'));
    assert.equal(!!page.window.document.getElementById('representation'), navigationOnly, route+' scope isolation');
    assert.ok(page.window.document.getElementById('other'));
    page.window.close();
  }
}
console.log('PASS filter isolation: all three newly enhanced routes preserve representation link; legacy executions still filter it');
