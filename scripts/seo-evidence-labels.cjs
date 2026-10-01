const fs=require('fs'), cp=require('child_process');
const files=cp.execSync('git diff --name-only',{encoding:'utf8'}).trim().split('\n').filter(p=>p.startsWith('case-studies/')&&p!=='case-studies/index.html');
for(const p of files){
  const original=cp.execFileSync('git',['show','HEAD:'+p],{encoding:'utf8'});
  const hypothetical=/hypothetical|not verified AE client|not a verified client outcome|teaching assumptions/i.test(original);
  let s=fs.readFileSync(p,'utf8');
  s=s.replace(/<aside style="background:#f8f9fa;border-left:4px solid #1a365d;padding:20px;margin:24px 0">.*?<\/aside>/s,'');
  const label=hypothetical?'Illustrative planning example':'Publisher-reported case study';
  const note=hypothetical?'The figures on this page are hypothetical teaching inputs, not a verified client result or prediction of savings.':'The outcome is publisher-reported and anonymized. The underlying returns and realization of savings have not been independently verified for this website update.';
  const block=`<section class="content-section" id="case-evidence"><div class="container narrow"><h2>${label}</h2><p>${note} Depreciation, deductions, income offsets, estimated tax benefits, and realized refunds are different measures. Review the assumptions and limitations before applying the example to your property.</p></div></section>`;
  s=s.replace(/<main>/,`<main>${block}`);
  const t=s.match(/<title>(.*?)<\/title>/s)[1];
  s=s.replace(/(<meta (?:name|property)="(?:og:title|twitter:title)" content=")[^"]*(")/g,`$1${t}$2`);
  fs.writeFileSync(p,s);
  console.log(p,label);
}
