const fs = require('node:fs');
const path = require('node:path');
const targets = [
  'blog/form-3115-missed-depreciation/index.html',
  'blog/form-3115-cost-segregation-catch-up/index.html',
  'form-3115-cost-segregation/index.html',
  'form-3115-cost-segregation-lookback/index.html',
];
const choices = [
  ['/amended-return-vs-form-3115/', 'Which correction procedure should I discuss with my preparer?'],
  ['/form-3115-cost-segregation/', 'What belongs in the filing and implementation package?'],
  ['/form-3115-cost-segregation-lookback/', 'How is an existing property’s depreciation history reviewed?'],
  ['/form-3115-year-of-sale-rental-property/', 'What changes if the property is being sold?'],
];
function apply(root) {
  let changed = 0;
  for (const relative of targets) {
    const file = path.join(root, relative);
    const before = fs.readFileSync(file, 'utf8');
    let html = before.replace(/<!-- depreciation-reading-path:start -->[\s\S]*?<!-- depreciation-reading-path:end -->/g, '');
    const own = '/' + relative.replace(/index\.html$/, '');
    const links = choices.filter(([url]) => url !== own).map(([url, label]) => {
      if (!fs.existsSync(path.join(root, url, 'index.html'))) throw new Error('Missing reading-path destination: ' + url);
      return `<li><a href="${url}">${label}</a></li>`;
    }).join('');
    const block = '<!-- depreciation-reading-path:start --><nav aria-label="Choose a depreciation correction guide" style="padding:16px 20px;margin:24px 0;border:1px solid #dbe2ea;border-radius:8px"><p><strong>Choose the question you need to answer</strong></p><ul>' + links + '</ul></nav><!-- depreciation-reading-path:end -->';
    const h1end = html.indexOf('</h1>');
    const section = html.indexOf('<h2', h1end);
    if (h1end < 0 || section < 0) throw new Error('Missing article heading: ' + relative);
    html = html.slice(0, section) + block + html.slice(section);
    // Exclude repeated sales copy from snippets while retaining visible CTAs.
    html = html.replace(/<(div|section)\b([^>]*\bclass="[^"]*\b(?:compact-booking-cta|sticky-cta)\b[^"]*"[^>]*)>/g,
      (tag, name, attrs) => /\bdata-nosnippet\b/.test(attrs) ? tag : `<${name}${attrs} data-nosnippet>`);
    if (html !== before) { fs.writeFileSync(file, html); changed++; }
  }
  console.log(JSON.stringify({depreciationReadingPaths: targets.length, changed}));
}
module.exports = { apply };
if (require.main === module) apply(process.argv[2] || 'public');
