"use strict";
// Validate the video date shape Google reported; this does not guarantee rich results.
const fs=require('node:fs'),path=require('node:path');
function inspect(html,name='fixture') {
 const errors=[];let videos=0;
 function walk(v) {
  if(!v||typeof v!=='object')return;
  const types=Array.isArray(v['@type'])?v['@type']:[v['@type']];
  if(types.includes('VideoObject')) {
   videos++;
   if(typeof v.uploadDate!=='string'||!/^\d{4}-\d{2}-\d{2}T(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d(?:\.\d+)?(?:Z|[+-](?:0\d|1[0-4]):[0-5]\d)$/.test(v.uploadDate)||!Number.isFinite(Date.parse(v.uploadDate)))errors.push(name+': VideoObject uploadDate must be a valid ISO datetime with timezone');
  }
  for(const x of Object.values(v))if(x&&typeof x==='object')Array.isArray(x)?x.forEach(walk):walk(x);
 }
 for(const m of html.matchAll(/<script\b[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)) {
  try {walk(JSON.parse(m[1]));}catch(e){errors.push(name+': invalid JSON-LD: '+e.message);}
 }
 return {videos,errors};
}
function scan(root) {
 const result={videos:0,errors:[]};
 function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=path.join(dir,e.name);if(e.isDirectory())walk(p);else if(e.isFile()&&p.endsWith('.html')){const r=inspect(fs.readFileSync(p,'utf8'),path.relative(root,p));result.videos+=r.videos;result.errors.push(...r.errors);}}}
 walk(root);return result;
}
if(require.main===module){const r=scan(path.resolve(process.argv[2]||'public'));console.log(JSON.stringify(r));if(r.errors.length)process.exitCode=1;}
module.exports={inspect,scan};
