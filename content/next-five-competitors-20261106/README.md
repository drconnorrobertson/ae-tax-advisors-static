# Second competitor cohort — November 6, 2026

Refreshes the 15 existing pricing, alternatives and AE-comparison pages for P4 Tax, Delerme CPA, Taxstra, WCG CPAs and Anomaly CPA. Preserves each established URL and creates five comparisons: P4–Delerme, P4–Anomaly, Taxstra–WCG, Anomaly–WCG and Delerme–Taxstra.

The pages distinguish planning projects, accounting subscriptions, annual advisory packages, execution and return preparation. Current official WCG and Anomaly starting fees are disclosed even where they are below AE's advisory fee. P4, Delerme and Taxstra require current quotes; comparable-work estimates are not presented as their prices. Buyer scenarios are illustrative, not client outcomes.

The cohort links from five existing service/comparison hubs, synchronizes the shopping directory and JSON, and includes the existing first-party booking-event hook. This records clicks and calendar activity; it is not confirmation of booked appointments or closed revenue. Sitemap dates apply to substantive cohort changes. No customer rating, fake human review, competitor-capability exclusion or ranking promise is added.

Render with `python3 scripts/refresh-next-five-competitors-20261106.py`. The renderer is shared with the first cohort; the original command remains available as a wrapper. It does not render unrelated providers. Run cohort refreshes after legacy whole-directory generators, which are not part of the production build.

Validate with `node scripts/build-release.cjs`, `python3 scripts/check-five-competitors.py public next-five-competitors-20261106` and `python3 scripts/check-five-competitors.py public` for the original cohort. The new preservation manifest verifies the original 21 source pages remain byte-identical. Renderer rerun idempotence and existing booking-event tests also pass.

Primary sources checked November 6, 2026 are linked in sources.json and on the pages. Publishing and sitemap inclusion do not prove Google indexing or ranking improvements; GSC Wizard subscription access remains expired.
