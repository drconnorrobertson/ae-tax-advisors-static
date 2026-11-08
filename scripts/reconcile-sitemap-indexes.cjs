'use strict';
// Preserve existing index eligibility. Reconcile submitted index aliases to the same inventory.
const fs=require('node:fs'),path=require('node:path');
const out=path.resolve(process.argv[2]||'public');
const names=fs.readdirSync(out).filter(n=>/^sitemap.*\.xml$/.test(n)&&/<urlset\b/.test(fs.readFileSync(path.join(out,n),'utf8'))).sort();
const xml='<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+names.map(n=>'  <sitemap><loc>https://www.aetaxadvisors.com/'+n+'</loc></sitemap>').join('\n')+'\n</sitemapindex>\n';
for(const n of ['sitemap-index.xml','sitemap_index.xml'])fs.writeFileSync(path.join(out,n),xml);
console.log('Reconciled sitemap index aliases: '+names.length+' existing leaf sitemaps.');
