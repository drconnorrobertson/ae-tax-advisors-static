'use strict';
// Firm-approved copy policy, applied after generators and before release checks.
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(process.argv[2]||'public');
const audit='Audit defense is included at no additional cost with every AE Tax Advisors engagement.';
const credentials='IRS Enrolled Agents and Licensed CPAs with over 45 years of combined experience.';
const rows=[];
const names=require('./ae-team-names.json');
const namePattern=names.map(x=>x.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('|');
function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){
 const file=path.join(dir,e.name);if(e.isDirectory()){walk(file);continue;}if(!e.name.endsWith('.html'))continue;
 const rel=path.relative(root,file).replaceAll(path.sep,'/');let s=fs.readFileSync(file,'utf8');
 const url='/'+rel.replace(/index\.html$/,'');
 function sub(re,value,label){s=s.replace(re,(...args)=>{const old=args[0],next=typeof value==='function'?value(...args):value;if(old!==next)rows.push({page:url,section:label,old,new:next});return next;});}
 sub(/15\+ years across healthcare, professional services, real estate, and technology\./g,'Our team brings over 45 years of combined experience.','Experience');
 sub(/(?:15\+|15-plus|fifteen) years of (?:combined )?experience/gi,'over 45 years of combined experience','Experience');
 sub(/Our average rating is 4\.9\/5 stars\.\s*/g,'','Unsubstantiated rating');
 sub(/As Featured In 45 Publications/g,'Press &amp; Media','Unsubstantiated press count');
 sub(/See all 45 features/g,'Explore press coverage','Unsubstantiated press count');
 sub(/(?:all |All )?45 press (?:articles|features)/g,'press coverage','Unsubstantiated press count');
 sub(/<span class="trust-badge">IRS Enrolled Agents<\/span>\s*<span class="trust-badge">Licensed CPAs<\/span>/g,'<span class="trust-badge">'+credentials+'</span>','Shared credentials');
 // Do not alter depreciation recovery periods, property holding periods or competitor ratings.
 if(rel==='index.html'){
 sub(/<div><dt>Cost segregation studies<\/dt><dd>500\+<\/dd><\/div>/g,'<div><dt>Team experience</dt><dd>Over 45 years combined</dd></div>','Unsupported study count');
 sub(/<div><dt>Average client rating<\/dt><dd>4\.9 \/ 5<\/dd><\/div>/g,'<div><dt>Audit defense</dt><dd>Included at no additional cost</dd></div>','Unsupported rating');
 sub(/<span class="trust-fact"><strong>500\+<\/strong> cost segregation studies<\/span>/g,'<span class="trust-fact">'+credentials+'</span>','Trust bar');
 sub(/<span class="trust-fact"><strong>4\.9\/5<\/strong> average client rating<\/span>/g,'<span class="trust-fact">'+audit+'</span>','Trust bar');
 if(!s.includes('id="audit-defense-why"'))sub(/<p>Our team brings over 45 years of combined experience\.<\/p>/g,'<p>Our team brings over 45 years of combined experience.</p><p id="audit-defense-why">'+audit+'</p>','Why Choose Us');
 // Use callbacks for capture insertion rather than literal replacement tokens.
 if(!s.includes('id="audit-defense-service"'))sub(/<h2>Tax Planning Services<\/h2>/,m=>m+'<p id="audit-defense-service">'+audit+'</p>','Services');
 }
 if(['about/index.html','bios/index.html','services/index.html'].includes(rel)&&!s.includes('id="engagement-assurance"'))sub(/<\/main>/,m=>'<section class="content-section" id="engagement-assurance"><div class="container narrow"><h2>Experience and engagement support</h2><p>'+credentials+'</p><p>'+audit+'</p></div></section>'+m,'Engagement assurance');
 if(rel==='bios/index.html'){
 sub(/<main\b[^>]*>[\s\S]*?<\/main>/,()=>'<main><section class="content-section"><div class="container narrow"><h1>The AE Tax Advisors team</h1><p>'+credentials+'</p><p>Our team brings over 45 years of combined experience.</p><p>'+audit+'</p><p><a href="/discovery/">Book your free 30-minute discovery call</a></p></div></section></main>','Firm-only team page');
 sub(/<script\b([^>]*type=["']application\/ld\+json["'][^>]*)>([\s\S]*?)<\/script>/gi,(tag,attrs,body)=>{const data=JSON.parse(body);function clean(v){if(Array.isArray(v))return v.filter(x=>x?.['@type']!=='FAQPage').map(clean);if(v&&typeof v==='object'){if(v['@type']==='FAQPage')return null;return Object.fromEntries(Object.entries(v).map(([k,x])=>[k,clean(x)]));}return v;}const next=clean(data);return next?'<script'+attrs+'>'+JSON.stringify(next)+'</script>':'';},'Remove retired team FAQ schema');
 }
 if(rel==='about/index.html')sub(/<h2>Leadership<\/h2>\s*<p>[\s\S]*?<\/p>/,'<h2>Our Team</h2><p>'+credentials+'</p>','Firm-only team copy');
 if(rel==='faq/index.html'&&!s.includes('Is audit defense included?')){
 sub(/<\/main>/,m=>'<section class="content-section"><div class="container narrow"><h2>Is audit defense included?</h2><p>Yes. Audit defense is included with every engagement at no additional cost.</p></div></section>'+m,'Audit FAQ');
 sub(/<\/head>/,m=>'<script type="application/ld+json">'+JSON.stringify({'@context':'https://schema.org','@type':'FAQPage',mainEntity:[{'@type':'Question',name:'Is audit defense included?',acceptedAnswer:{'@type':'Answer',text:'Yes. Audit defense is included with every engagement at no additional cost.'}}]})+'</script>'+m,'Audit FAQ schema');
 }
 sub(/<script\b([^>]*type=["']application\/ld\+json["'][^>]*)>([\s\S]*?)<\/script>/gi,(tag,attrs,body)=>{const data=JSON.parse(body);let changed=false;function visit(v){if(Array.isArray(v))v.forEach(visit);else if(v&&typeof v==='object'){if(v['@type']==='Answer'&&typeof v.text==='string'&&names.some(n=>v.text.includes(n))){v.text='AE Tax Advisors provides coordinated tax advisory and client support through its team.';changed=true;}Object.values(v).forEach(visit);}}visit(data);return changed?'<script'+attrs+'>'+JSON.stringify(data)+'</script>':tag;},'Firm-only FAQ attribution');
 sub(new RegExp('<p\\b[^>]*>(?:(?!<\\/p>)[\\s\\S])*?(?:'+namePattern+')(?:(?!<\\/p>)[\\s\\S])*?<\\/p>','g'),'<p>AE Tax Advisors provides coordinated tax advisory and client support through its team.</p>','Firm-only narrative');
 sub(/<div class="faq-answer-inner">([\s\S]*?)<\/div>/g,(tag,body)=>names.some(n=>body.includes(n))?'<div class="faq-answer-inner">AE Tax Advisors provides coordinated tax advisory and client support through its team.</div>':tag,'Firm-only FAQ answer');
 // Executive identities in AE copy and metadata become firm attribution.
 sub(new RegExp(namePattern,'g'),'AE Tax Advisors','Firm attribution');
 sub(/\bChristina\b(?=[^<>]*(?:<|$))/g,'AE Tax Advisors','Firm attribution');
 if(s!==fs.readFileSync(file,'utf8'))fs.writeFileSync(file,s);
 }}
walk(root);
const report=process.argv[3]||process.env.AE_MEMO_CHANGELOG;
if(report)fs.writeFileSync(report,JSON.stringify(rows,null,2));
console.log('Memo V1 copy policy: '+rows.length+' replacements across '+new Set(rows.map(x=>x.page)).size+' pages.');
