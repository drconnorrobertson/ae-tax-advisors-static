#!/usr/bin/env node
'use strict';
// Use the site's permanent redirects as the authority for internal link targets.
// Default: dry run. --write applies changes; --check fails on stale links.
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const config = JSON.parse(fs.readFileSync(path.join(root, 'vercel.json'), 'utf8'));
const redirects = new Map();
for (const rule of config.redirects || []) {
  if (![301, 308].includes(rule.statusCode) || /[:*()]/.test(rule.source) || !rule.destination.startsWith('/')) continue;
  if (redirects.has(rule.source) && redirects.get(rule.source) !== rule.destination) throw new Error('Conflicting redirect: ' + rule.source);
  redirects.set(rule.source, rule.destination);
}
function finalTarget(source) {
  const seen = new Set();
  while (redirects.has(source)) {
    if (seen.has(source)) throw new Error('Redirect loop: ' + source);
    seen.add(source);
    source = redirects.get(source);
  }
  return source;
}
function exists(url) {
  const file = path.join(root, url.split(/[?#]/)[0]);
  return (fs.existsSync(file) && fs.statSync(file).isFile()) || fs.existsSync(path.join(file, 'index.html'));
}
for (const source of redirects.keys()) {
  const target = finalTarget(source);
  if (!exists(target)) throw new Error('Missing redirect destination: ' + source + ' -> ' + target);
}
function normalize(href) {
  let url;
  try { url = new URL(href, 'https://www.aetaxadvisors.com/'); } catch { return href; }
  if (!['aetaxadvisors.com', 'www.aetaxadvisors.com'].includes(url.hostname) || !['http:', 'https:'].includes(url.protocol)) return href;
  // Relative hrefs require page context and are intentionally left unchanged.
  if (!href.startsWith('/') && !/^https?:\/\//i.test(href)) return href;
  const key = redirects.has(url.pathname) ? url.pathname : url.pathname.replace(/\/?$/, '/');
  if (!redirects.has(key)) return href;
  const target = finalTarget(key);
  return target + url.search + url.hash;
}
function htmlFiles(dir) {
  const result = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name.startsWith('.') || ['node_modules', 'scripts', 'public'].includes(entry.name)) continue;
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) result.push(...htmlFiles(file));
    else if (entry.isFile() && entry.name.endsWith('.html')) result.push(file);
  }
  return result;
}
const write = process.argv.includes('--write');
const check = process.argv.includes('--check');
let pages = 0, links = 0;
const counts = new Map();
for (const file of htmlFiles(root)) {
  const original = fs.readFileSync(file, 'utf8');
  const updated = original.replace(/<a\b[^>]*>/gi, tag => tag.replace(/(\bhref\s*=\s*)(["'])(.*?)\2/gi, (attribute, prefix, quote, href) => {
    const replacement = normalize(href);
    if (replacement === href) return attribute;
    links++;
    counts.set(href, (counts.get(href) || 0) + 1);
    return prefix + quote + replacement + quote;
  }));
  if (updated !== original) {
    pages++;
    if (write) fs.writeFileSync(file, updated);
  }
}
console.log(JSON.stringify({ mode: write ? 'write' : check ? 'check' : 'dry-run', pages, links, redirects: redirects.size, targets: Object.fromEntries(counts) }, null, 2));
if (check && links) process.exitCode = 1;
