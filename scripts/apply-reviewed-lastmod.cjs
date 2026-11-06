'use strict';
// Only explicitly reviewed substantive changes receive a sitemap lastmod.
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const out = path.resolve(root, process.argv[2] || 'public');
const dates = JSON.parse(fs.readFileSync(path.join(root,'content/reviewed-content-lastmod.json'),'utf8'));
for (const [route,date] of Object.entries(dates)) {
  if (!/^\/[a-z0-9\/-]+\/$/.test(route) || !/^\d{4}-\d{2}-\d{2}$/.test(date) || Number.isNaN(Date.parse(date))) throw new Error('Invalid reviewed date record: '+route);
  const relative = route.replace(/^\/|\/$/g, '');
  const candidates = [path.join(out,relative,'index.html'), path.join(out,relative+'.html')];
  if (!candidates.some(file => fs.existsSync(file) && fs.statSync(file).isFile())) throw new Error('Missing reviewed page: '+route);
}
let changed=0;
for (const filename of fs.readdirSync(out).filter(f=>/^sitemap.*\.xml$/.test(f))) {
  const p=path.join(out,filename); const xml=fs.readFileSync(p,'utf8');
  const next=xml.replace(/<url>\s*<loc>([^<]+)<\/loc>([\s\S]*?)<\/url>/g,(full,loc,body)=>{
    const u=new URL(loc); const date=dates[u.pathname];
    if (!date || u.origin!=='https://www.aetaxadvisors.com') return full;
    const tag='<lastmod>'+date+'</lastmod>'; changed++;
    body=/<lastmod>[^<]*<\/lastmod>/.test(body)?body.replace(/<lastmod>[^<]*<\/lastmod>/,tag):tag+body;
    return '<url><loc>'+loc+'</loc>'+body+'</url>';
  });
  if (next!==xml) fs.writeFileSync(p,next);
}
console.log('Reviewed content dates applied to '+changed+' sitemap entries.');
