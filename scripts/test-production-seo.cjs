'use strict';
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const {spawnSync} = require('node:child_process');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ae-seo-test-'));
const page = '/compare/kbkg-vs-ae-tax/';
const file = path.join(dir, page, 'index.html');
const good = '<link rel="canonical" href="https://www.aetaxadvisors.com' + page + '"><a href="/compare/kbkg-vs-ae-tax/">Self</a>';
function run() { return spawnSync(process.execPath, [path.join(__dirname, 'check-production-seo.cjs'), dir], {encoding:'utf8'}); }
try {
  for (const p of JSON.parse(fs.readFileSync(path.join(root, 'content/seo-refresh-20261106/pages.json')))) {
    const f = path.join(dir,p,'index.html'); fs.mkdirSync(path.dirname(f),{recursive:true}); fs.writeFileSync(f,good.replace('href="https://www.aetaxadvisors.com' + page + '"', 'href="https://www.aetaxadvisors.com' + p + '"'));
  }
  fs.writeFileSync(path.join(dir, 'sitemap.xml'), '<urlset>' + JSON.parse(fs.readFileSync(path.join(root, 'content/seo-refresh-20261106/pages.json'))).map(p => '<url><loc>https://www.aetaxadvisors.com'+p+'</loc></url>').join('') + '</urlset>');
  assert.equal(run().status,0,'valid production output should pass');
  for (const bad of [good.replace('/compare/kbkg-vs-ae-tax/','/wrong/'), good+'<meta name="robots" content="noindex">', good+'<a href="/missing-output/">Broken</a>']) {
    fs.writeFileSync(file,bad); assert.equal(run().status,1,'invalid output should fail');
  }
  fs.unlinkSync(file); assert.equal(run().status,1,'missing output should fail');
  console.log('PASS: valid output, canonical mismatch, noindex, broken internal link and missing output fixtures.');
} finally { fs.rmSync(dir,{recursive:true,force:true}); }
