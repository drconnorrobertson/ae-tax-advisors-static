const fs=require('fs'),path=require('path');
module.exports=function(root,stratum){
let count=0;function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){if(e.name.startsWith('.')||['node_modules','public','content'].includes(e.name))continue;const f=path.join(dir,e.name);if(e.isDirectory()){walk(f);continue}if(!f.endsWith('.html'))continue;let h=fs.readFileSync(f,'utf8');const rel=path.relative(root,f);if(/^(cost-seg-discovery|discovery)\//.test(rel))continue;
const heading=(h.match(/<h1\b[^>]*>([\s\S]*?)<\/h1>/i)||[])[1]||'';
const intent=/cost[- ]seg(?:regation)?|form[- ]?3115|depreciation[- ](?:study|studies)/i.test(rel+' '+heading);
const n=h.replace(/(<a\b[^>]*href=")([^"]+)("[^>]*>)([\s\S]*?)(<\/a>)/gi,(all,a,url,b,label,c)=>{
const general=/(?:^|aetaxadvisors\.com)\/discovery\/?(?:\?|$)/.test(url);
const old=stratum&&(/(?:^|\/)(?:booking|free-estimate)\/(?:index\.html)?(?:\?|$)/.test(url));
if(!(general||old))return all;
const explicit=/cost[- ]seg/i.test(label);
// Shared navigation and footers on AE retain general advisory scheduling.
const shared=/class="[^"]*(?:nav|sticky|mobile)/i.test(a+b);
if(!stratum&&!explicit&&(!intent||shared))return all;
const query=url.includes('?')?url.slice(url.indexOf('?')):'';
return a+'/cost-seg-discovery/'+query+b+'Book a Cost Seg Discovery Call'+c;
});if(n!==h){fs.writeFileSync(f,n);count++}
}}
walk(root);
const sitemap=path.join(root,'sitemap.xml');if(fs.existsSync(sitemap)){let x=fs.readFileSync(sitemap,'utf8');const domain=stratum?'www.stratumcostsegregation.com':'www.aetaxadvisors.com';const url='https://'+domain+'/cost-seg-discovery/';if(!x.includes('<loc>'+url+'</loc>')&&x.includes('</urlset>'))fs.writeFileSync(sitemap,x.replace('</urlset>','<url><loc>'+url+'</loc></url></urlset>'));}
console.log('Cost seg booking: updated '+count+' pages');};
