const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'..'),cfg=JSON.parse(fs.readFileSync(path.join(root,'vercel.json'),'utf8')),out=path.join(root,cfg.outputDirectory||'.'),data=JSON.parse(fs.readFileSync(path.join(__dirname,'content-consolidation.json'),'utf8')),map=data.redirects;
function replaceUrl(u){let full=false,p=u;try{if(/^https?:/.test(u)){let n=new URL(u);if(n.host!==data.host)return u;full=true;p=n.pathname+n.search+n.hash}}catch{return u}let base=p.split(/[?#]/)[0],tail=p.slice(base.length),dest=map[base]||map[base.replace(/\/$/,'')]||map[base.replace(/\/$/,'')+'/'];return dest?(full?'https://'+data.host:'')+dest+tail:u;}
let changed=0;function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){if(e.name.startsWith('.')||['scripts','brand','node_modules','public','dist'].includes(e.name))continue;let f=path.join(dir,e.name);if(e.isDirectory()){walk(f);continue}if(!f.endsWith('.html'))continue;let h=fs.readFileSync(f,'utf8');let n=h.replace(/(href=")([^"]+)(")/g,(_,a,u,b)=>a+replaceUrl(u)+b);let seen=new Set();n=n.replace(/<li\b[^>]*data-library-item[^>]*>[\s\S]*?<\/li>/g,li=>{let u=(li.match(/href="([^"]+)"/)||[])[1];if(!u)return li;if(seen.has(u))return '';seen.add(u);return li;});if(n!==h){fs.writeFileSync(f,n);changed++}}}walk(out);
for(const name of fs.readdirSync(out)){if(!/^sitemap.*\.xml$/.test(name))continue;let f=path.join(out,name),x=fs.readFileSync(f,'utf8');x=x.replace(/<url>[^]*?<\/url>/g,t=>{let u=(t.match(/<loc>([^<]+)<\/loc>/)||[])[1];return u&&replaceUrl(u)!==u?'':t;});fs.writeFileSync(f,x);}
// Keep the service page readable as reviewed provider cohorts accumulate.
const studyPage=path.join(out,'cost-segregation-study','index.html');
if(fs.existsSync(studyPage)){
 const html=fs.readFileSync(studyPage,'utf8');
 const heading='Compare cost segregation providers by study scope';
 const pattern=/<!-- ([a-z0-9-]+):start -->\s*<section\b[^>]*>\s*<div\b[^>]*>\s*<h2>Compare cost segregation providers by study scope<\/h2>[\s\S]*?<\/section><!-- \1:end -->/g;
 const blocks=[...html.matchAll(pattern)];
 if(blocks.length>1){
  const groups={alternatives:[],comparisons:[]},seen=new Set();
  for(const block of blocks)for(const item of block[0].matchAll(/<li\b[^>]*>[\s\S]*?<\/li>/g)){
   const href=item[0].match(/href="([^"]+)"/)?.[1];
   if(!href)throw Error('Provider reading item has no destination');
   if(seen.has(href))continue;seen.add(href);
   const group=href.endsWith('-alternatives/')?'alternatives':'comparisons';
   groups[group].push(item[0]);
  }
  if(!groups.alternatives.length||!groups.comparisons.length)throw Error('Provider reading groups are incomplete');
  const opening=blocks[0][0].slice(0,blocks[0][0].indexOf('<h2>'));
  const intro=blocks[0][0].match(/<h2>[\s\S]*?<\/h2>\s*(<p>[\s\S]*?<\/p>)/)?.[1];
  if(!intro)throw Error('Provider reading introduction is missing');
  const merged=opening+'<h2>'+heading+'</h2>\n'+intro+'\n<h3>Provider alternatives</h3><ul>'+groups.alternatives.join('')+'</ul>\n<h3>Head-to-head provider comparisons</h3><ul>'+groups.comparisons.join('')+'</ul></div></section><!-- '+blocks[0][1]+':end -->';
  let first=true;
  const updated=html.replace(pattern,()=>{if(!first)return '';first=false;return merged;});
  fs.writeFileSync(studyPage,updated);
  console.log('Consolidated '+blocks.length+' provider reading sections; retained '+seen.size+' distinct destinations.');
 }
}
console.log('Consolidation: '+Object.keys(map).length+' permanent redirects; updated links in '+changed+' pages.');
