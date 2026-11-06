'use strict';
// Syntax guard only. Passing does not imply eligibility for a search rich result.
const fs = require('node:fs');
const path = require('node:path');
function inspect(html, filename) {
  let blocks = 0;
  const errors = [];
  for (const match of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script\s*>/gi)) {
    const type = match[1].match(/(?:^|\s)type\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+))/i);
    if (!type || (type[1] || type[2] || type[3]).toLowerCase() !== 'application/ld+json') continue;
    blocks++;
    try {
      const value = JSON.parse(match[2]);
      if (value === null || typeof value !== 'object') throw new Error('JSON-LD document must be an object or array');
    } catch (error) { errors.push(`${filename}: JSON-LD block ${blocks}: ${error.message}`); }
  }
  return {blocks, errors};
}
function scan(root) {
  const result = {htmlFiles:0, blocks:0, errors:[]};
  function walk(dir) {
    for (const entry of fs.readdirSync(dir, {withFileTypes:true})) {
      const target = path.join(dir, entry.name);
      if (entry.isDirectory()) walk(target);
      else if (entry.isFile() && entry.name.endsWith('.html')) {
        result.htmlFiles++;
        const found = inspect(fs.readFileSync(target, 'utf8'), path.relative(root,target));
        result.blocks += found.blocks; result.errors.push(...found.errors);
      }
    }
  }
  walk(root); return result;
}
if (require.main === module) {
  const result = scan(path.resolve(process.argv[2] || 'public'));
  console.log(JSON.stringify(result, null, 2));
  if (result.errors.length) process.exitCode = 1;
}
module.exports = {inspect, scan};
