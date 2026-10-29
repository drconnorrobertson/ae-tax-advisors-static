# Fourth 100-page business-owner FAQ release

Prepared October 29, 2026. Refreshed from production main 0a71370ad8e9943adb98f10858dabcfae9c1a28d, including the newer canonical sitemap restoration. The inventory contains 4,458 source pages, including all three previous 100-page releases and nonindexable/staging/workbook routes.

Question screening uses title similarity followed by full main-body unigram/bigram comparisons against the entire inventory and within the batch. Existing blog, service and sitemap discovery bodies are read from pre-release HEAD to prevent new draft links from contaminating the old comparison corpus. Scores are triage aids; they do not prove semantic uniqueness. Editorial review rejects duplicate core decisions and records replacements in rejected-intents.json. Overlap-review.csv contains nearest matches and the retained intent distinction. Shared statutory context across related pages is expected. No search-volume, ranking, demand or indexing claims are invented.

Each page has an original direct answer, hypothetical owner scenario, specific steps, decision-changing fact, error to avoid, records and next action. Primary citations are visible and synchronized with Article schema. AI assistance and absence of claimed individual professional review are disclosed. Collection pages explicitly identify tax-resolution specialists and AE's actual service focus.

The previous 300 FAQ sources are checked byte-for-byte against pre-release HEAD. Source and public verification also cover distinct title/H1/description, canonical, indexability, dates, discovery links, JSON-LD, source identity and internal links. Run scaled_content_guard.py before staging.

Reproduce: python3 scripts/publish-owner-faqs-20261029-d.py
Source verification: python3 scripts/verify-owner-faqs-20261029-d.py
Build: node scripts/build-release.cjs
Production verification: python3 scripts/verify-owner-faqs-20261029-d.py public
Additional required checks: node scripts/check-sitemaps.cjs; python3 scripts/check-provider-triplets.py public; python3 test_canonical_sitemap_discovery.py

Dedicated sitemap: sitemap-owner-faqs-20261029-d.xml. Previous discovery sections and source content are preserved. Publishing is complete only after the exact production commit is READY and all 100 custom-domain URLs plus the sitemap pass live checks.
