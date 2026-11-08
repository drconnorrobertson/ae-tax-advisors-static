'use strict';
// Safe shared publishing transforms: no tax copy, canonical or date rewrites.
const dimensions = require('../content/site-image-dimensions.json');
const config=require('../vercel.json');
const redirects=new Map((config.redirects||[]).filter(x=>(x.permanent||[301,308].includes(x.statusCode))&&!/[:*()]/.test(x.source)&&x.destination.startsWith('/')).map(x=>[x.source,x.destination]));
const guides = [
 ['/guides/str-tax-cost-segregation/', 'STR and cost segregation questions'],
 ['/compare/tax-influencer-alternatives/', 'Compare tax educators and service scopes'],
 ['/resources/', 'Planning tools and resources']
];
function attr(tag,name) { return tag.match(new RegExp('\\b'+name+'\\s*=\\s*(["\'])(.*?)\\1','i'))?.[2]; }
function add(tag,values){return tag.replace(/\s*\/?>$/,end=>' '+values+end);}
function normalize(href){
 if(!href||(!href.startsWith('/')&&!/^https?:\/\//i.test(href)))return href;
 let u;try{u=new URL(href.replace(/&amp;/g,'&'),'https://www.aetaxadvisors.com');}catch{return href;}
 if(!['www.aetaxadvisors.com','aetaxadvisors.com'].includes(u.hostname))return href;
 let p=u.pathname,seen=new Set();while(redirects.has(p)){if(seen.has(p))throw Error('Redirect cycle: '+p);seen.add(p);p=redirects.get(p);}
 return seen.size?(p+u.search+u.hash).replace(/&/g,'&amp;'):href;
}
function polish(html) {
 html=html.replace(/<script\b[^>]*>[\s\S]*?<\/script>|<!--[\s\S]*?-->|<a\b[^>]*>/gi,tag=>!/^<a\b/i.test(tag)?tag:tag.replace(/(\bhref\s*=\s*)(["'])(.*?)\2/gi,(m,p,q,u)=>p+q+normalize(u)+q));
 html = html.replace(/<img\b[^>]*>/gi, tag => {
  if (!/\bdecoding\s*=/i.test(tag)) tag=add(tag,'decoding="async"');
  const src=attr(tag,'src')?.split(/[?#]/)[0]; const d=dimensions[src];
  if (!d) return tag;
  const w=attr(tag,'width'),h=attr(tag,'height');
  if (!w && !h) tag=add(tag,`width="${d[0]}" height="${d[1]}"`);
  else if (!w && /^\d+$/.test(h))tag=add(tag,`width="${Math.max(1,Math.round(Number(h)*d[0]/d[1]))}"`);
  else if (!h && /^\d+$/.test(w))tag=add(tag,`height="${Math.max(1,Math.round(Number(w)*d[1]/d[0]))}"`);
  return tag;
 });
 html=html.replace(/<footer\b[^>]*>[\s\S]*?<\/footer>/gi,footer=>{
  // Footer columns are peers of main content sections, so expose level-two headings.
  footer=footer.replace(/<h4\b([^>]*)>([\s\S]*?)<\/h4>/gi,(_,attrs,body)=>'<h2'+attrs+' data-footer-heading>'+body+'</h2>');
  if(footer.includes('data-planning-libraries'))return footer;
  const links=guides.filter(([url])=>!footer.includes('href="'+url+'"'));
  if(!links.length)return footer;
  const block='<nav class="planning-library-links" data-planning-libraries aria-label="Planning libraries">'+links.map(([url,label])=>`<a href="${url}">${label}</a>`).join('')+'</nav>';
  return footer.replace(/<\/footer>/i,block+'$&');
 });
 return html;
}
module.exports={polish};
