'use strict';
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '../public');
const failures = [];
function walk(dir) {
  for (const entry of fs.readdirSync(dir, {withFileTypes: true})) {
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) { walk(file); continue; }
    if (!file.endsWith('.html')) continue;
    const relative = path.relative(root, file).split(path.sep).join('/');
    if (!relative.startsWith('compare/')) continue;
    if (/nth-degree/i.test(relative)) failures.push(relative + ': retired comparison page');
    const content = fs.readFileSync(file, 'utf8')
      .replace(/<script\b[^>]*>[^]*?<\/script>/g, '');
    if (/nth[\s.-]*degree|dan\s+nicholson|\bDan\b/i.test(content)) failures.push(relative + ': mention outside recommendation section');
  }
}
walk(root);
if (failures.length) { console.error(failures.join('\n')); process.exit(1); }
console.log('Nth Degree check passed: no comparison pages or competitive-context mentions.');
