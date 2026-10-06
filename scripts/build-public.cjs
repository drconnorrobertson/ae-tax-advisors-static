'use strict';
// Stage committed public content only. No generator is executed at deployment.
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const out = path.join(root, 'public');
const forbidden = new Set(['public', 'scripts', 'research', 'node_modules']);
const rootNames = new Set(['robots.txt', 'llms.txt', 'llms-full.txt', 'llms.md', 'feed.xml']);
const jsonNames = new Set(['assets/ad-booking-config.json', 'compare/tax-advisory-firm-comparison.json']);
const toolScripts = new Set(['tools/property-review-prep/intake.js']);
// Already-published report and exports derived from public case studies.
// Other research and source datasets remain outside the public build.
const publicResearch = new Set(['research/index.html', 'research/tax-planning-case-study-outcomes/index.html', 'research/tax-planning-case-study-outcomes.json', 'research/tax-planning-case-study-outcomes.csv']);
const assetTypes = new Set(['.css', '.js', '.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp', '.avif', '.ico', '.woff', '.woff2', '.ttf', '.otf', '.mp4', '.webm', '.pdf']);
function allowed(relative) {
  const parts = relative.split('/');
  if (relative === '.well-known/llms.txt') return true;
  if (publicResearch.has(relative)) return true;
  if (parts.some(p => p.startsWith('.') || p.startsWith('_') || p.startsWith('test-') || forbidden.has(p))) return false;
  const ext = path.extname(relative).toLowerCase();
  if (ext === '.html') return true;
  if (jsonNames.has(relative) || toolScripts.has(relative)) return true;
  if (['assets', 'css', 'images'].includes(parts[0]) && assetTypes.has(ext)) return true;
  if (parts.length === 1 && (rootNames.has(relative) || /^sitemap.*\.xml$/.test(relative))) return true;
  // Existing public IndexNow verification files; do not admit arbitrary txt.
  return parts.length === 1 && /^[a-f0-9]{30,64}\.txt$/.test(relative) && fs.existsSync(path.join(root, relative)) &&
    fs.readFileSync(path.join(root, relative), 'utf8').trim() === relative.slice(0, -4);
}
function walk(dir) {
  for (const entry of fs.readdirSync(dir, {withFileTypes: true})) {
    const source = path.join(dir, entry.name);
    const relative = path.relative(root, source).split(path.sep).join('/');
    if (entry.isSymbolicLink()) continue;
    if (entry.isDirectory()) {
      if (relative === '.well-known') { walk(source); continue; }
      if (relative === 'research' || relative === 'research/tax-planning-case-study-outcomes') { walk(source); continue; }
      if (entry.name.startsWith('.') || entry.name.startsWith('_') || entry.name.startsWith('test-') || forbidden.has(entry.name)) continue;
      walk(source);
    } else if (entry.isFile() && allowed(relative)) {
      const target = path.join(out, relative);
      fs.mkdirSync(path.dirname(target), {recursive: true});
      fs.copyFileSync(source, target);
    }
  }
}
function build() {
  fs.rmSync(out, {recursive: true, force: true});
  fs.mkdirSync(out);
  walk(root);
  console.log('Staged public HTML, assets, discovery files and verification keys in public/.');
}
if (require.main === module) build();
module.exports = {allowed, build, root, out};
