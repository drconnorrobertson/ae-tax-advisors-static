'use strict';
const fs = require('node:fs');
const path = require('node:path');
const {residualSharedDiscoveryCtas} = require('./normalize-shared-discovery-cta.cjs');
const root = path.resolve(__dirname, '..', process.argv[2] || 'public');
const failures = [];
function walk(dir) {
  for (const entry of fs.readdirSync(dir, {withFileTypes: true})) {
    const file = path.join(dir, entry.name);
    if (entry.isSymbolicLink()) continue;
    if (entry.isDirectory()) walk(file);
    else if (entry.isFile() && file.endsWith('.html')) {
      const count = residualSharedDiscoveryCtas(fs.readFileSync(file, 'utf8'));
      if (count) failures.push({file:path.relative(root,file), count});
    }
  }
}
walk(root);
if (failures.length) {
  console.error('Uncorrected exact shared discovery promises:', JSON.stringify(failures));
  process.exitCode = 1;
} else console.log('PASS: no exact shared-footer discovery overpromise remains in staged HTML.');
