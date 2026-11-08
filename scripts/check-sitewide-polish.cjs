'use strict';
const fs=require('node:fs'),path=require('node:path'),{polish}=require('./ensure-sitewide-polish.cjs');const out=path.resolve(process.argv[2]||'public');let pages=0,footers=0,images=0;const errors=[];
function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const f=path.join(dir,e.name);if(e.isDirectory())walk(f);else if(e.isFile()&&f.endsWith('.html')){pages++;const s=fs.readFileSync(f,'utf8');if(polish(s)!==s)errors.push(path.relative(out,f)+': shared polish not stable');if(/<footer\b/i.test(s))footers++;images+=(s.match(/<img\b/gi)||[]).length;}}}
walk(out);console.log(JSON.stringify({pages,footers,images,errors}));if(errors.length)process.exitCode=1;
