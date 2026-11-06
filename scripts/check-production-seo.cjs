'use strict';
// Check the output we deploy, after consolidation and exclusion stages.
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const out = path.resolve(root, process.argv[2] || 'public');
const config = JSON.parse(fs.readFileSync(path.join(root, 'vercel.json'), 'utf8'));
const redirects = new Map((config.redirects || []).filter(r => !/[:*()]/.test(r.source)).map(r => [r.source, r.destination]));
const hosts = new Set(['aetaxadvisors.com', 'www.aetaxadvisors.com']);
const errors = [];
const seen = new Set();
function attr(tag, name) { return tag.match(new RegExp('\\b' + name + '\\s*=\\s*(["\\\'])(.*?)\\1', 'i'))?.[2]; }
function resolveFile(p) {
  let decoded; try { decoded = decodeURIComponent(p); } catch { return null; }
  const file = path.resolve(out, '.' + decoded);
  if (file !== out && !file.startsWith(out + path.sep)) return null;
  for (const candidate of [file, path.join(file, 'index.html'), file + '.html'])
    if (fs.existsSync(candidate) && fs.statSync(candidate).isFile()) return candidate;
  return null;
}
let sitemapUrls = 0;
for (const filename of fs.readdirSync(out).filter(f => /^sitemap.*\.xml$/.test(f))) {
  const xml = fs.readFileSync(path.join(out, filename), 'utf8');
  for (const m of xml.matchAll(/<loc>(.*?)<\/loc>/g)) {
    let url;
    try { url = new URL(m[1].replace(/&amp;/g, '&')); } catch { errors.push(`${filename}: invalid URL ${m[1]}`); continue; }
    if (url.protocol !== 'https:' || !hosts.has(url.hostname)) { errors.push(`${filename}: invalid origin ${url.href}`); continue; }
    const file = resolveFile(url.pathname);
    if (!file) { errors.push(`${filename}: missing production file ${url.pathname}`); continue; }
    if (!file.endsWith('.html')) continue;
    sitemapUrls++;
    if (redirects.has(url.pathname)) errors.push(`${filename}: redirect in sitemap ${url.pathname}`);
    const html = fs.readFileSync(file, 'utf8');
    const robots = [...html.matchAll(/<meta\b[^>]*>/gi)].map(m => m[0]).filter(t => /^(robots|googlebot)$/i.test(attr(t, 'name') || ''));
    if (robots.some(t => /\bnoindex\b/i.test(attr(t, 'content') || ''))) errors.push(`${filename}: noindex ${url.pathname}`);
    const canonicals = [...html.matchAll(/<link\b[^>]*>/gi)].map(m => m[0]).filter(t => /\bcanonical\b/i.test(attr(t, 'rel') || ''));
    if (canonicals.length !== 1 || attr(canonicals[0], 'href') !== url.href) errors.push(`${filename}: canonical mismatch ${url.pathname}`);
    seen.add(url.pathname);
  }
}
// Check every internal navigation link on the explicitly maintained release cohort.
const manifest = path.join(root, 'content/seo-refresh-20261106/pages.json');
let links = 0;
if (fs.existsSync(manifest)) for (const page of JSON.parse(fs.readFileSync(manifest, 'utf8'))) {
  const file = resolveFile(page);
  if (!file) { errors.push(`release page missing: ${page}`); continue; }
  const html = fs.readFileSync(file, 'utf8');
  if (!seen.has(page)) errors.push(`release page absent from sitemaps: ${page}`);
  for (const m of html.matchAll(/<a\b[^>]*>/gi)) {
    const href = attr(m[0], 'href');
    if (!href || /^(mailto:|tel:|javascript:|#)/i.test(href)) continue;
    let url; try { url = new URL(href.replace(/&amp;/g, '&'), 'https://www.aetaxadvisors.com' + page); } catch { errors.push(`${page}: invalid href ${href}`); continue; }
    if (!hosts.has(url.hostname)) continue;
    links++;
    let p = url.pathname; const visited = new Set();
    while (redirects.has(p)) {
      if (visited.has(p)) { errors.push(`${page}: redirect cycle ${href}`); break; }
      visited.add(p); const next = new URL(redirects.get(p), url.origin);
      if (!hosts.has(next.hostname)) { p = null; break; }
      p = next.pathname;
    }
    if (p && !resolveFile(p)) errors.push(`${page}: broken production link ${href}`);
  }
}
console.log(JSON.stringify({output:path.relative(root,out), sitemapUrls, uniqueSitemapUrls:seen.size, releaseLinks:links, errors}, null, 2));
if (errors.length) process.exitCode = 1;
