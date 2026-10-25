'use strict';
// Preserve the validated release stages within Vercel's command-length limit.
const {execSync} = require('node:child_process');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
for (const command of [
  "node scripts/build-public.cjs",
  "node scripts/brand-check.mjs public",
  "node scripts/consolidate-content.cjs",
  "node scripts/check-nth-degree.cjs",
  "python3 scripts/improve-editorial-discovery.py public",
  "python3 scripts/enforce-provider-exclusion.py public",
  "node scripts/check-nth-degree.cjs",
  "python3 scripts/check-provider-triplets.py public",
  "python3 scripts/check-provider-content.py public"
]) execSync(command, {cwd:root,stdio:'inherit'});
