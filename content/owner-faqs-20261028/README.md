# Business-owner FAQ release — October 28, 2026

100 new pages answer distinct, long-tail business-owner questions. Each has a bespoke direct answer, illustrative scenario, procedural steps, required records, mistake to avoid, implementation decision and a fact that changes the answer. Examples are hypothetical, not claimed client results. No named professional review is asserted.

The release updates PTET, amended-return and QSBS material on four existing URLs. The site keeps its existing design and canonical URLs. The blog and HTML sitemap link every new FAQ, with selected links from relevant services and a dedicated registered XML sitemap.

Sources are linked in the page bodies. Keyword targets are editorial, not measured rankings or search volumes. A title-similarity review against the existing inventory identified one duplicate spouse-withholding topic, which was replaced with a question about tax distributions among partners in different states. Repository five-word-shingle comparisons found no duplication errors or warnings for the 100 new pages.

Regenerate with `python3 scripts/seo-expansion-20261028.py`.

Validate with:

- `node scripts/build-release.cjs`
- `python3 scripts/verify-owner-faqs-20261028.py public`
- `python3 scaled_content_guard.py` before adding the new pages to Git staging
- `node scripts/check-sitemaps.cjs`

The production build includes brand, provider-exclusion, 100-provider/300-page triplet and provider-content checks. The release verifier checks all 100 pages for indexability, canonical URLs, unique titles/questions, metadata, structured data, internal links, minimum content, hypothetical labels and sitemap/discovery membership. The manifest lists the exact public paths.
