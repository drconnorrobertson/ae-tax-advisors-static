# Research-led existing-page refresh, November 6, 2026

This release strengthens existing comparison and tax-information pages without creating near-duplicate URLs or removing pricing. The refreshed cohort is recorded in pages.json. Existing provider triplets, exclusion policies, staging noindex rules, booking destinations and fee disclosures are preserved.

## Research and interpretation

The canonical www Search Console property, rather than the non-www URL-prefix property, is the relevant portfolio view. The browser review reported 6.84K clicks, 891K impressions, 0.8% CTR and average position 7.9 for October 7–November 3, 2026, Web. Those UI-rounded figures are not an exported query-to-page analysis, a conversion report or a promise of improvement.

Historical non-www exclusions should not trigger bulk redirects. Eight sampled 404 paths were absent from the current output and had no current public HTML/XML/TXT references. Forbidden samples were historical WordPress paths, and noindex samples included intentionally staged pages. Current intended-to-rank pages need individual inspection; this release does not claim to fix Google's indexing decisions.

## Technical changes

- Validate all production sitemap URLs after consolidation and exclusion stages: origin, target existence, noindex, canonical parity and explicit redirect conflicts.
- Validate internal navigation targets and exact redirect chains for the maintained content cohort.
- Remove unreliable sitemap-index lastmod fields instead of advertising fabricated freshness. Individual URL modification dates are separate.
- Add regression fixtures proving the output validator rejects missing files, noindex, canonical mismatches and broken internal links.

## Validation

Run `node scripts/build-release.cjs`, `python3 scripts/check-provider-triplets.py public`, `node scripts/test-production-seo.cjs` and `git diff --check`. Release output must preserve all required provider triplets and published pricing. The link gate covers the release cohort, not every historical page. Search performance should be evaluated after enough settled data; current query visibility is not qualified-lead attribution.
