# Five competitor search clusters — November 6, 2026

Preserves the 15 established pricing/alternatives/AE-comparison URLs for Rainwater, Keystone, Tax Goddess, Tax Alchemy and Anderson. Replaces generic price estimates with sourced fees or quote-required status, separates the three reader intents and retains current provider scope corrections.

Adds four researched comparisons: Rainwater–Keystone, Rainwater–Tax Goddess, Anderson–Keystone and Anderson–Tax Alchemy. Refreshes Rainwater–Tax Alchemy and Tax Alchemy–Tax Goddess. The compare hub, tax-planning directory, business-owner service and real estate service link to these pages. The pricing directory and its JSON agree with current evidence. Peter Holtz pages remain unchanged.

`python3 scripts/refresh-five-competitors-20261106.py` renders this cohort only. Run it after any legacy full-provider generator; legacy generators are not executed by the production build. Provider-specific source facts and original buyer scenarios are in sources.json. No fake customer review, rating, named human reviewer, savings promise or guaranteed rank is added.

Validate with the full `node scripts/build-release.cjs`, then `python3 scripts/check-five-competitors.py public`. The latter checks all 21 pages, canonical/indexability, headings, title uniqueness, metadata, structured data, sources, directory evidence, internal destinations and anchors. Existing production guards cover all 300 provider-intent pages and the full sitemap set.

Four new URLs are in the existing comparison sitemap; substantive page changes are registered in reviewed-content-lastmod.json. Search Console performance/inspection remains unavailable through the expired GSC Wizard subscription. Publishing is not evidence of Google indexing or improved ranks.
