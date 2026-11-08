"use strict";
const assert=require('node:assert/strict');const {inspect}=require('./check-video-metadata.cjs');
const fixture=d=>'<script type="application/ld+json">'+JSON.stringify({'@context':'https://schema.org','@graph':[{'@type':'VideoObject',uploadDate:d}]})+'</script>';
for(const d of ['2026-09-27', '2026-09-27T19:20:40','not a date','2026-09-27T25:20:40Z'])assert.equal(inspect(fixture(d)).errors.length,1,d);
for(const d of ['2026-09-27T19:20:40-04:00','2026-09-27T23:20:40Z'])assert.deepEqual(inspect(fixture(d)),{videos:1,errors:[]});
assert.deepEqual(inspect('<main>No video</main>'),{videos:0,errors:[]});
console.log('PASS nested VideoObject timezone validation, invalid times and non-video pages');
