'use strict';
// Keep the standalone sitemap intact and index only its URLs missing from other child sitemaps.
const fs=require('node:fs'),path=require('node:path');
const out=path.resolve(process.argv[2]||'public');
const mainName='sitemap.xml';
const residualName='sitemap-main-only.xml';
const names=fs.readdirSync(out).filter(n=>/^sitemap.*\.xml$/.test(n)&&n!==residualName&&/<urlset\b/.test(fs.readFileSync(path.join(out,n),'utf8'))).sort();
const read=name=>fs.readFileSync(path.join(out,name),'utf8');
const locations=xml=>Array.from(xml.matchAll(/<loc>\s*([^<]+?)\s*<\/loc>/g), match=>match[1]);
const indexNames=names.filter(name=>name!==mainName);
if(names.includes(mainName)){
 const main=read(mainName);
 const covered=new Set(indexNames.flatMap(name=>locations(read(name))));
 const residual=main.replace(/<url(?:\s[^>]*)?>[\s\S]*?<\/url>/g,entry=>{
  const [url]=locations(entry);
  return url&&covered.has(url)?'':entry;
 });
 const remaining=locations(residual);
 const indexed=new Set([...covered,...remaining]);
 if(locations(main).some(url=>!indexed.has(url)))throw new Error('Main sitemap coverage changed');
 if(remaining.length){
  fs.writeFileSync(path.join(out,residualName),residual);
  indexNames.push(residualName);
 }else if(fs.existsSync(path.join(out,residualName))){
  fs.unlinkSync(path.join(out,residualName));
 }
}
indexNames.sort();
const xml='<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+indexNames.map(n=>'  <sitemap><loc>https://www.aetaxadvisors.com/'+n+'</loc></sitemap>').join('\n')+'\n</sitemapindex>\n';
for(const n of ['sitemap-index.xml','sitemap_index.xml'])fs.writeFileSync(path.join(out,n),xml);
console.log('Reconciled sitemap index aliases: '+indexNames.length+' existing leaf sitemaps.');
