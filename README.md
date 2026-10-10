# Tax Strategist Directory

Static provider research directory and buyer publication for established businesses. AE Tax Advisors holds the first owner-selected featured position, disclosed throughout the site. Other directory listings are alphabetical. It does not assign independent best-provider ratings.

Build: `python3 build.py`. Validate: `python3 check.py` and `node --check app.js`.

The build consumes `data/firms.json` and `data/guides.json` (or their `.gz` equivalents), creates individual source-backed profiles, paginated directory pages, documented location pages, buyer guides, static metadata, and partitioned sitemaps. All core listing links and article text are server-served HTML. Search, shortlist, and proposal comparison progressively enhance the static content. Shortlists and worksheet notes remain in browser storage.

The editorial focus is provider selection, hiring, engagement scope, communication, implementation responsibilities, proposals, and client fit. AE's existing sitemap is retained as an audit input to detect exact slug conflicts. AE's main site remains the destination for detailed tax strategy education, services, pricing and booking. Search intent is separated by design, but rankings can still overlap; assess actual queries after indexing before expanding competing topics.

Research records identify industry or professional society sources. Society service lists are self-reported. A listing does not verify an individual license or specialized tax strategy expertise. Only entries with documented official tax-services evidence receive the corresponding flag. Do not generate independent ratings, fabricated reviews, pricing, or credentials.

Vercel project: prj_0K4izs2hYAd2EbWgT4OnzAJclSBg. Apex domain: taxstrategistdirectory.com. The www host redirects to the apex. Retain deployment protection. Custom domains are exempt from its default SSO protection. GoDaddy DNS must point to the project before the purchased host serves the site.

Future additions should expand geographic diversity and enrich sourced service evidence before increasing listing count. Publish distinct buyer guides rather than tax-code strategy replicas. Submission email links are live mailto links; there is no pretend claim form or backend. No analytics or advertising trackers are installed.

## October 9 expansion

The industry hiring library combines 60 editorial operating contexts and 44 distinct advisory procurement decisions. Each brief supplies a document list, provider interview, printable notes, and a downloadable CSV scope worksheet. It does not assert a firm provides a service or that a tax strategy applies. Edit the two data/hiring-*.tsv source tables; build.py calls hiring_library.py and publishes HTML, Markdown alternatives and sitemap coverage. Adjacent Markdown representations remain noindex through vercel.json.

282 new profiles were identity-matched to official CPA society detail pages; listed services remain attributed to those records. These public business records are not independent license verification. The primary keyword map is data/keyword-map.csv. Keyword targets have no measured search-volume or ranking claim.

AE discovery links identify campaign source and placement. The shared CTA and home feature lead to the existing AE discovery page. Run the build and check scripts before release; checks require at least 5,000 indexable URLs.
