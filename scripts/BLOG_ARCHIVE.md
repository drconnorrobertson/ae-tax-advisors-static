# Approved blog archive

`blog-catalog.json` is the explicit publication list, not a filesystem inventory.
The initial migration includes all 1,232 article links already present on the
approved blog index at f2d5962, including 409 routes outside its 823 cards.
`blog-archive-migration.json` records every source route and canonical destination.
No holds were released and no article content or publication dates were changed.

## Authoring

After reviewing a new article and deliberately approving its discovery, run:

    python3 scripts/update_blog_index.py --register /blog/approved-article/

Existing batch authors call `blog_archive.register_routes()` with only their
explicit batch paths. Categories use the prior card category where available,
then articleSection, then the documented “Tax Strategy” fallback. Publication
dates come from article metadata; absent dates remain absent, never invented.
For a metadata refresh after reviewing an existing article revision, register that
specific route again. Render validates eligibility but intentionally uses the
catalog metadata snapshot; it does not silently adopt unreviewed title/description
changes. Explicit registration refreshes the approved route's title, description
and publication date from its source while preserving its existing category.
Both `/blog/slug/index.html` and `/blog/slug.html` may supply a clean-URL article.
If both exist and their bytes differ, registration fails unless the route has an
explicit selection in `blog-archive-source-overrides.json`. Four baseline routes
(auto-dealership, ecommerce, franchise and veterinary owner guides) already have
both files. Their directory versions preserve the initial migration selection.
This map does not change deployment routing, remove either file, or establish
which variant Vercel serves. Verify live route precedence separately at integration,
especially for the reviewed franchise and veterinary drafts. Unlisted conflicts
fail closed. No directory scanning or automatic enrollment of flat files occurs.

The deterministic renderer commits 36-card pages, visible-only collection schema,
a compact public search index, and the archive sitemap. Each page has its own
canonical. Search/filter variants retain that archive canonical. The original
article sitemaps are unchanged. Never point every archive canonical to page one.

The template retains the shared header/footer and local UX assets. Edit
`blog-archive-template.html` for archive-wide chrome and `assets/blog-archive.css`
for archive styles. Do not paste article lists into blog/index.html. The historical
index updater and site upgrader now delegate to the approved renderer; FAQ batch
checks inspect the union of archive pages rather than demanding all links on page
one. Restriction failures stop rendering and require explicit catalog review.

## Progressive enhancement

Static archive cards and numbered/previous/next links work without JavaScript.
Search fetches `/assets/blog-search-index.json` only when a query or category is
used. Results use DOM APIs, combined text/category matching, 36-result increments,
and URL history. Clearing restores the original static cards. A failed request
leaves static browsing usable and offers retry. There is no new tracking.

## Checks

    python3 scripts/test-blog-archive.py
    AE_JSDOM_PATH=/path/to/jsdom node scripts/test-blog-search.cjs
    node scripts/build-release.cjs

Deployment only stages committed catalog outputs and runs the read-only archive
coverage gate. It does not run the catalog renderer or discover new content.
Only the exact public search-index JSON is added to the staging allowlist.
The independent shared-UX branch also edits build-public.cjs; retain both its
helper injection and this exact JSON allowlist entry when integrating.
