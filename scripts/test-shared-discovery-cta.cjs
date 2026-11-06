'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {normalizeSharedDiscoveryCta:n, residualSharedDiscoveryCtas:residual} = require('./normalize-shared-discovery-cta.cjs');
const c = require('./shared-discovery-cta.json');
assert.ok(c.new_paragraph.includes('study or advisory'));
assert.ok(c.new_paragraph.includes('agreed written scope'));
assert.ok(!/complimentary|free|30.minute|paid advisory engagement/i.test(c.new_paragraph));
function fixture(anchor=c.anchors[0], heading='') {
  return '<section class="content-section fade-in-section" style="background:var(--light-bg);">\n' +
    '  <div class="container narrow center-text">\n<h2'+heading+'>Talk Through Your Situation</h2>\n' +
    '<p>'+c.old_paragraph+'</p>\n<div class="center-cta" style="margin-top:20px;">\n'+anchor+'\n</div>\n</div>\n</section>';
}
let checks=0;
for(const anchor of c.anchors) for(const heading of ['', ' id="answer-section-9"']) {
  const old=fixture(anchor, heading), expected=old.replace(c.old_paragraph,c.new_paragraph);
  assert.deepEqual(n(old),{html:expected,count:1});
  assert.equal(residual(old),1);assert.equal(residual(expected),0);
  assert.deepEqual(n(expected),{html:expected,count:0});
  assert.equal(expected.replace(c.new_paragraph,c.old_paragraph),old);
  checks++;
}
const old=fixture();
const negatives=[
  '<p>'+c.old_paragraph+'</p>',
  '<footer><p>'+c.old_paragraph+'</p><a href="/discovery/">Book a Call</a></footer>',
  '<section class="case-study"><h2>Client result</h2><p>'+c.old_paragraph+'</p></section>',
  old.replace('Talk Through Your Situation','Client results'),
  old.replace('container narrow center-text','container narrow'),
  old.replace('content-section fade-in-section','case-study'),
  old.replace('/discovery/','/unknown-booking/'),
  old.replace('Book a Call','Purchase Now'),
  old.replace('class="btn-cta btn-lg"','class="btn-cta btn-lg" data-extra="1"'),
  old.replace('<h2>','<h2 id="answer-section-10">'),
  old.replace('what it is worth','an estimated refund'),
  old.replace('</p>',' Fee $7,800. Client saved $50,000.</p>'),
];
for(const value of negatives) assert.deepEqual(n(value),{html:value,count:0});
// Unknown links/headings stay untouched and are detected, not guessed at.
assert.equal(residual(negatives[6]),1);
assert.equal(residual(negatives[9]),1);
assert.equal(residual(negatives[0]),0);
const context='<title>Original title</title><time>2026-08-17</time><p>Fee $7,800; client result $50,000.</p>';
assert.equal(n(context+old+context).html,context+old.replace(c.old_paragraph,c.new_paragraph)+context);
assert.equal(n(old+old).count,2);
const root=path.resolve(__dirname,'..');
assert.equal(JSON.parse(fs.readFileSync(path.join(root,'vercel.json'))).buildCommand,'node scripts/build-release.cjs');
assert.ok(fs.readFileSync(path.join(root,'scripts/build-public.cjs'),'utf8').includes('normalizeSharedDiscoveryCta(html)'));
assert.ok(fs.readFileSync(path.join(root,'scripts/build-release.cjs'),'utf8').includes('node scripts/check-shared-discovery-cta.cjs public'));
console.log(`PASS: ${checks} exact positive DOM fixtures; ${negatives.length} negative fixtures; byte preservation, duplicates, idempotence, unknown-variant guard and Vercel build hooks.`);
// Optional final-release check: routing may send the same scoped copy to either
// calendar. Inspect actual post-routing sections rather than only source fixtures.
if (process.argv[2]) {
  const staged = path.resolve(root, process.argv[2]);
  const compact = s => s.replace(/\s+/g, ' ').trim();
  const expected = compact(c.new_paragraph);
  const counts = {'/discovery/':0, '/cost-seg-discovery/':0};
  const pageCounts = {'/discovery/':new Set(), '/cost-seg-discovery/':new Set()};
  const expectedGeneral = new Set(c.anchors.map(a => a.match(/>([^<]+)<\/a>$/)[1]));
  let paragraphs=0;
  function inspect(dir) {
    for (const entry of fs.readdirSync(dir, {withFileTypes:true})) {
      const file=path.join(dir,entry.name);
      if (entry.isSymbolicLink()) continue;
      if (entry.isDirectory()) inspect(file);
      else if (file.endsWith('.html')) {
        const html=fs.readFileSync(file,'utf8');
        for (const section of html.match(/<section\b[^>]*>[\s\S]*?<\/section>/g) || []) {
          if (!compact(section).includes(expected)) continue;
          assert.ok(/<h2(?: id="answer-section-9")?>Talk Through Your Situation<\/h2>/.test(section),file);
          const anchor=section.match(/<a\b([^>]*)>([^<]*)<\/a>/);
          assert.ok(anchor,file);
          const href=anchor[1].match(/href="([^"]+)"/)[1];
          assert.ok(href in counts,`${file}: unexpected final destination ${href}`);
          assert.ok(anchor[1].includes('class="btn-cta btn-lg"'),file);
          if (href==='/cost-seg-discovery/') assert.equal(anchor[2],'Book a Cost Seg Discovery Call',file);
          else assert.ok(expectedGeneral.has(anchor[2]),file);
          assert.ok(!/complimentary|free|30.minute|paid advisory engagement/i.test(expected),file);
          counts[href]++;pageCounts[href].add(file);paragraphs++;
        }
      }
    }
  }
  inspect(staged);
  assert.ok(counts['/discovery/']>0 && counts['/cost-seg-discovery/']>0);
  console.log('PASS final post-routing scope: '+JSON.stringify({paragraphs,paragraphsByDestination:counts,pagesByDestination:Object.fromEntries(Object.entries(pageCounts).map(([k,v])=>[k,v.size]))}));
}
