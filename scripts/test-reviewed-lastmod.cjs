'use strict';
const fs=require('node:fs');const os=require('node:os');const path=require('node:path');const {execFileSync}=require('node:child_process');const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');const dates=JSON.parse(fs.readFileSync(path.join(root,'content/reviewed-content-lastmod.json'),'utf8'));const out=fs.mkdtempSync(path.join(os.tmpdir(),'ae-lastmod-test-'));const files=[];
try {
 Object.keys(dates).forEach((route,i)=>{const rel=route.replace(/^\/|\/$/g,'');const f=i===1?path.join(out,rel+'.html'):path.join(out,rel,'index.html');fs.mkdirSync(path.dirname(f),{recursive:true});fs.writeFileSync(f,'<!doctype html><title>Fixture</title>');files.push(f);});
 const entries=Object.keys(dates).map(route=>'<url><loc>https://www.aetaxadvisors.com'+route+'</loc><lastmod>2020-01-01</lastmod></url>').join('');const sitemap=path.join(out,'sitemap-test.xml');fs.writeFileSync(sitemap,'<urlset>'+entries+'<url><loc>https://www.aetaxadvisors.com/untouched/</loc><lastmod>2020-01-01</lastmod></url></urlset>');
 const run=()=>execFileSync(process.execPath,[path.join(__dirname,'apply-reviewed-lastmod.cjs'),out],{stdio:'pipe'});
 run();const once=fs.readFileSync(sitemap,'utf8');for(const [route,date] of Object.entries(dates))assert.ok(once.includes('<loc>https://www.aetaxadvisors.com'+route+'</loc><lastmod>'+date+'</lastmod>'));assert.ok(once.includes('/untouched/</loc><lastmod>2020-01-01</lastmod>'));run();assert.equal(fs.readFileSync(sitemap,'utf8'),once);fs.unlinkSync(files[0]);assert.throws(run);console.log('PASS: directory/flat routes, reviewed-only updates, idempotence and missing-page rejection');
} finally {fs.rmSync(out,{recursive:true,force:true});}
