# Owner content and discovery maintenance

The primary audiences are business owners and real estate owners. New guides must address a distinct decision, cite applicable primary sources, label hypothetical examples, and link to the relevant service hub. Do not claim individual CPA review without an actual review.

`discovery_inventory.py` defines the common eligibility rule: an explicit self-canonical, no page-level noindex, and no exact permanent redirect. `build_blog_index.py`, `generate_sitemap.py`, and `build_discovery_files.py` use that rule. Sitemap presence describes eligibility, not confirmed search-engine indexing.

After publishing content:

1. Run `python build_blog_index.py`.
2. Run `python generate_sitemap.py`. Use `--preserve-lastmod` for metadata-only or internal-link maintenance. For mixed changes, preserve existing dates and update lastmod only for substantively changed URLs.
3. Run `python build_discovery_files.py` to refresh the optional AI summaries, topic sitemaps and feed.
4. Run `python seo_validate.py`, `python content_quality.py`, `python schema_hygiene.py`, `python -m unittest test_owner_discovery.py`, and `node test_cost_segregation_scenario.cjs`.
5. Check new content against existing coverage with `python scaled_content_guard.py` before committing. Review similar-intent pages manually as well.
6. After deployment, verify the actual canonical routes, redirects, key file and sitemap, then submit only changed public URLs through `submit_indexnow.py`.

The canonical calculator is `/cost-segregation-calculator/`. Three legacy calculator routes permanently redirect there. It models a deliberately limited new-acquisition, 100%-bonus scenario. Inputs do not establish tax eligibility. Do not restore property-type percentages as asserted facts, classify an STR solely by length of stay, or equate a deduction with immediately usable savings.

The homepage article cards and eight targeted snippets are maintained by `optimize_owner_snippets.py`. The September 26 guides and their two CSV checklists are maintained by `build_owner_decision_guides.py`. Calculator layout and consolidation are maintained by `improve_owner_discovery.py`; run the snippet updater afterward if rebuilding it. These are deliberate editorial tools, not scheduled mass-publishing jobs.

The optional AI summaries link to published pricing and make clear that cost segregation is separately priced. They do not carry unsupported review counts, named credentials, blanket bonus eligibility, or guaranteed outcomes. Google requires no special AI text file or schema for AI features: https://developers.google.com/search/docs/appearance/ai-features

Search and AI crawlers use the wildcard robots group. Staging remains crawlable so its existing noindex directives can be read. Robots.txt cannot force crawling or indexing. A CDN firewall can independently block crawlers and should be checked using verified bot traffic rather than a user-agent string alone.

## Commercial intent release (September 26, 2026)

`improve_commercial_pages.py` owns the four main commercial narratives. Run it after older page generators or `optimize_owner_snippets.py`, which may otherwise restore earlier copy. It preserves selected established resource sections. `commercial_intents.json` maps reviewed supporting pages to the appropriate service destination; `build_commercial_paths.py` applies those links. `optimize_commercial_snippets.py` owns the 13 buyer-intent snippets and the published AE fee box on the existing study-cost blog article.

Keep the market-pricing blog article distinct from the AE service-pricing destination. The retired `/cost-segregation-pricing/` route redirects directly to `/cost-segregation-study-cost-pricing/`. Update internal links as part of any future consolidation. Do not redirect pages based only on similar words: use actual intent and query-to-page evidence.

Release sequence: regenerate commercial pages, contextual paths and commercial snippets, then the blog index, canonical sitemap and discovery files. Preserve sitemap lastmod for markup-only fixes; update the date only for substantive content changes. Run `python3 -m unittest test_commercial_integrity test_owner_discovery`, `python3 schema_hygiene.py`, `python3 content_quality.py`, `python3 seo_validate.py` and the calculator tests. Breadcrumb arrays must contain ListItem objects, never social-profile URL strings. The schema hygiene gate now detects this defect.

Prices are taken from the published pricing page. A future fee change must update service narratives, FAQs, snippet text and the article fee box together. No projection or article example is a guaranteed saving. Search Console exports and performance notes remain outside the public repository.
