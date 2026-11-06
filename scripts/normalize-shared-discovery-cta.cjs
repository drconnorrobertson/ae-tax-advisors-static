'use strict';
// Mechanical release repair only: one exact legacy paragraph, known CTA DOM,
// and observed discovery-link variants. All surrounding bytes remain intact.
const config = require('./shared-discovery-cta.json');
const escape = value => value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const old = config.old_paragraph.split(/\s+/).map(escape).join('\\s+');
const prefix = '(<section class="content-section fade-in-section" style="background:var\\(--light-bg\\);">\\s*' +
  '<div class="container narrow center-text">\\s*<h2(?: id="answer-section-9")?>Talk Through Your Situation</h2>\\s*<p>)';
const suffix = '(</p>\\s*<div class="center-cta" style="margin-top:20px;">\\s*(?:' +
  config.anchors.map(escape).join('|') + ')\\s*</div>\\s*</div>\\s*</section>)';
function normalizeSharedDiscoveryCta(html) {
  let count = 0;
  const updated = html.replace(new RegExp(prefix + '(' + old + ')' + suffix, 'g'), (_, before, paragraph, after) => {
    count++;
    return before + config.new_paragraph + after;
  });
  return {html: updated, count};
}
function residualSharedDiscoveryCtas(html) {
  // Unknown link variants are not rewritten, but still fail the release guard.
  const sections = html.match(/<section\b[^>]*>[\s\S]*?<\/section>/g) || [];
  return sections.filter(section =>
    section.startsWith('<section class="content-section fade-in-section" style="background:var(--light-bg);">') &&
    /<div class="container narrow center-text">\s*<h2(?:\s[^>]*)?>Talk Through Your Situation<\/h2>/.test(section) &&
    new RegExp('<p>' + old + '</p>').test(section)).length;
}
module.exports = {normalizeSharedDiscoveryCta, residualSharedDiscoveryCtas};
