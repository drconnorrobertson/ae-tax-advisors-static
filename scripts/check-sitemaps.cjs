'use strict';
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const config = JSON.parse(fs.readFileSync(path.join(root, 'vercel.json'), 'utf8'));
const redirected = new Set((config.redirects || []).filter(r => !/[:*()]/.test(r.source)).map(r => r.source));
const errors = [];
let urls = 0;
for (const filename of fs.readdirSync(root).filter(f => /^sitemap.*\.xml$/.test(f))) {
  const xml = fs.readFileSync(path.join(root, filename), 'utf8');
  for (const match of xml.matchAll(/<loc>(.*?)<\/loc>/g)) {
    const url = new URL(match[1].replace(/&amp;/g, '&'));
    if (!['aetaxadvisors.com', 'www.aetaxadvisors.com'].includes(url.hostname)) {
      errors.push(filename + ': external URL ' + url.href); continue;
    }
    if (redirected.has(url.pathname)) errors.push(filename + ': redirecting URL ' + url.pathname);
    const file = path.join(root, url.pathname);
    const target = fs.existsSync(file) && fs.statSync(file).isFile() ? file : path.join(file, 'index.html');
    if (!fs.existsSync(target)) { errors.push(filename + ': missing file ' + url.pathname); continue; }
    if (target.endsWith('.html')) {
      urls++;
      const html = fs.readFileSync(target, 'utf8');
      for (const meta of html.match(/<meta\b[^>]*>/gi) || []) {
        if (/name\s*=\s*["'](?:robots|googlebot)["']/i.test(meta) && /content\s*=\s*["'][^"']*noindex/i.test(meta)) errors.push(filename + ': noindex URL ' + url.pathname);
      }
    }
  }
}
console.log(JSON.stringify({ urls, errors }, null, 2));
if (errors.length) process.exitCode = 1;
