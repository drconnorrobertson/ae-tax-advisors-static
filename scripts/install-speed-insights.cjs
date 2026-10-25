'use strict';
// Install the static-site runtime in publish output without regenerating content.
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(process.argv[2] || 'public');
const snippet = '<script>window.si=window.si||function(){(window.siq=window.siq||[]).push(arguments)};</script><script defer src="/_vercel/speed-insights/script.js"></script>';
let installed = 0;
function walk(dir) {
  for (const entry of fs.readdirSync(dir, {withFileTypes:true})) {
    const file = path.join(dir,entry.name);
    if (entry.isDirectory()) walk(file);
    else if (entry.isFile() && file.endsWith('.html')) {
      const original = fs.readFileSync(file,'utf8');
      if (original.includes('/_vercel/speed-insights/script.js')) continue;
      if (!/<\/body\s*>/i.test(original)) continue;
      fs.writeFileSync(file,original.replace(/<\/body\s*>/i,snippet+'$&'));
      installed++;
    }
  }
}
walk(root);
console.log('Speed Insights static runtime added to '+installed+' published HTML pages.');
