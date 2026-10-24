'use strict';
const fs = require('node:fs'), path = require('node:path');
const root = path.resolve(__dirname, '../public'), failures = [];
const excluded = /nth[\s._-]*degree|nthdegree|dan\s+nicholson/i;
function walk(dir) {
  for (const entry of fs.readdirSync(dir, {withFileTypes:true})) {
    const file = path.join(dir,entry.name);
    if (entry.isDirectory()) {walk(file);continue;}
    const relative = path.relative(root,file).split(path.sep).join('/');
    if (!/\.(html|xml|txt|json|js|csv)$/i.test(file)) continue;
    const content = fs.readFileSync(file,'utf8');
    if (excluded.test(relative)) {
      if (!file.endsWith('.html') || !/<meta\b[^>]*name=["']robots["'][^>]*content=["'][^"']*noindex/i.test(content)) failures.push(relative+': dedicated route lacks noindex');
    }
    if (excluded.test(content)) failures.push(relative+': excluded provider mention or link');
  }
}
walk(root);
if(failures.length){console.error(failures.join('\n'));process.exit(1);}
console.log('Provider exclusion passed across public HTML, structured data, links, sitemaps and discovery files.');
