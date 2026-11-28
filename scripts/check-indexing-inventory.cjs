'use strict';
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'..'),out=path.resolve(root,process.argv[2]||'public');
const attr=(tag,n)=>tag.match(new RegExp('\\b'+n+'=["\']([^"\']+)["\']','i'))?.[1];
const config=JSON.parse(fs.readFileSync(path.join(root,'vercel.json'),'utf8'));
const redirects=new Set(config.redirects.filter(r=>! /[:*()]/.test(r.source)).map(r=>r.source));
const errors=[],known=new Set(),counts={},urlsBySitemap=new Map();
for(const n of fs.readdirSync(out).filter(n=>/^sitemap.*\.xml$/.test(n))){
 const xml=fs.readFileSync(path.join(out,n),'utf8'),local=new Set();if(!/<urlset\b/.test(xml))continue;
 for(const m of xml.matchAll(/<loc>([^<]+)<\/loc>/g)){
  const u=new URL(m[1]);if(local.has(u.href))errors.push(n+': duplicate '+u.pathname);local.add(u.href);known.add(u.href);
  if(u.origin!=='https://www.aetaxadvisors.com'||u.search||u.hash)errors.push(n+': noncanonical URL '+u.href);
  if(redirects.has(u.pathname))errors.push(n+': redirect '+u.pathname);
 }counts[n]=local.size;urlsBySitemap.set(n,local);
}
const a=fs.readFileSync(path.join(out,'sitemap-index.xml'),'utf8'),b=fs.readFileSync(path.join(out,'sitemap_index.xml'),'utf8');
if(a!==b)errors.push('Submitted sitemap index aliases differ');
const indexedUrls=new Set();
for(const [name,urls] of urlsBySitemap){
 if(a.includes('/'+name+'</loc>')){
  for(const url of urls)indexedUrls.add(url);
 }else if(name!=='sitemap.xml'){
  errors.push('Sitemap omitted from index: '+name);
 }
}
for(const url of urlsBySitemap.get('sitemap.xml')||[]){
 if(!indexedUrls.has(url))errors.push('Main sitemap URL lost from index: '+url);
}
const data=JSON.parse(fs.readFileSync(path.join(root,'content/indexing-recovery-routes.json'),'utf8'));
let eligible=0;
for(const route of data){
 const r={URL:"https://www.aetaxadvisors.com"+route,route};
 if(!known.has(r.URL))errors.push('Eligible recovery URL lost from sitemap: '+r.route);else eligible++;
}
const fixes=JSON.parse(fs.readFileSync(path.join(root,'content/indexing-recovery-redirects.json'),'utf8'));
for(const [src,dest] of Object.entries(fixes)){
 const r=config.redirects.find(r=>r.source===src);if(!r||r.destination!==dest)errors.push('Recovery redirect missing: '+src);
}
console.log(JSON.stringify({uniqueSitemapUrls:known.size,leafSitemaps:Object.keys(counts).length,discoveredRecoveryUrls:eligible,redirectFixes:Object.keys(fixes).length,errors},null,2));
if(errors.length)process.exitCode=1;
