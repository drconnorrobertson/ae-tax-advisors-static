# Website publishing rules

- Never publish, recommend, compare, link to, or include Nth Degree, Nth Degree CPAs, nthdegreecpas.com, or Dan Nicholson in any page, directory, article, dataset, structured data, sitemap, discovery file, or other public output.
- Keep the exclusion checks in the production build. Existing removed URLs must remain retired/noindex or redirect to the generic retired page; never restore their content.
- The competitor directory contains 100 allowed providers, including Tax Hive. Each needs three distinct, self-canonical, indexable pages: pricing, alternatives, and comparison with AE. Do not use one page for both alternatives and comparison.
- Use each provider's own website for statements about its services and fees. Identify AE estimates and their benchmark sources separately from the provider's published prices.
- Before publishing, run the production build and `python3 scripts/check-provider-triplets.py public`.
- After running legacy comparison generators, run `python3 scripts/improve-provider-comparisons.py` to retain the official-source corrections and intent-specific search metadata. Do not restore unsupported capability checkboxes, turnaround rankings, or claims that a provider cannot supply Form 3115 without checking its current service offering.
