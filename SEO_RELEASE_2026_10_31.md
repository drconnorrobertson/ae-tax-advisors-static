# AE Tax website content audit and implementation, October 31, 2026

## Evidence and limits

Reviewed the current main-branch website source, public homepage and search-indexed amendment material. Source inventory contained 4,559 index.html files, including redirects, review holds, staging and nonindexable pages. This is not Google's indexed-page count. GSC Wizard refused even property discovery with subscription_required. No current query positions, traffic totals, ranking movements, conversion data or cannibalization findings can be substantiated from this session. Public search discovery is not a rank tracker.

## Decision

Prioritize two missing intents and remove five confirmed generic service placeholders through permanent redirects. Preserve substantive articles and existing provider comparison requirements. Do not delete low-traffic pages or consolidate distinct articles without query and landing-page evidence.

## Implemented page map

| Action | URL | Intent and destination |
| --- | --- | --- |
| Add | /services/c-corporation-tax-preparation/ | Form 1120 preparation, records, owner transactions, filing deliverables and scope. Existing C corporation material primarily covers strategy. |
| Add | /amended-tax-return-status-delays/ | Post-filing status, acknowledgment evidence, individual versus business tracking, delays and follow-up records. Existing amendment material primarily covers correcting returns. |
| Redirect 301 | /tax-services/ | /services/ |
| Redirect 301 | /tax-filing-and-compliance-services/ | /services/ |
| Redirect 301 | /schedule-a-real-estate-tax-consultation/ | /discovery/ |
| Redirect 301 | /schedule-a-real-estate-tax-consultation-2/ | /discovery/ |
| Redirect 301 | /mid-term-rental-tax-planning-and-preparation/ | /mid-term-rental-tax-accounting-setup/ |

Both slash variants are configured. The consolidation map updates production internal links and removes redirected sitemap entries. The new pages are listed in sitemap-pages.xml; production consolidation removes the redirected entries from all staged sitemaps. Added contextual links in /services/, /business-owner-small-business-tax/, /amended-tax-returns/ and /resources/. Both new pages have unique metadata, self-canonicals, one H1, breadcrumbs and the established discovery CTA. Service scope does not invent fees or turnaround promises. IRS references were checked for the new tax content. No case-study, credential or realized-savings claim was introduced.

## Exact next ranking-dependent pass

1. Restore GSC Wizard access through its subscription settings, or provide Search Console access/export. This is the remaining data dependency, not an implemented ranking check.
2. Export property totals, query rows, page rows and query-page pairs for the last 28 settled days versus the preceding 28, with 90-day context. Record country, device and query privacy coverage. Separate branded searches from nonbranded searches.
3. Review commercially relevant queries at average positions 4-20, prioritizing impressions and qualified inquiry intent. Map each query group to one primary commercial URL and distinct supporting educational URLs. Review the actual landing pages before editing.
4. Check overlapping query-page pairs. Merge only pages answering the same task with no distinct useful content. Transfer unique material, use a direct 301, replace internal links and remove the old URL from sitemaps. Keep informational, pricing, calculator and service intents distinct.
5. For uncovered query groups, first expand an existing relevant page. Add a URL only when its search intent and useful content are distinct. Avoid city or state expansion without substantive local relevance.
6. After deployment, inspect the two new URLs and five redirect destinations, and submit the current sitemap through Search Console. These submissions were not completed because GSC Wizard is unavailable.
7. Assess results at 28 and 56 days after release using the same filters: nonbrand impressions, clicks, CTR, average position, indexed status and qualified inquiry outcomes where available. No monitoring task was created.

## Validation

Run the required production build and provider-triplet checker. Inspect production new-page H1/canonical/link destinations, parse all sitemap XML, check redirect rules and inspect public responses after publishing. Record any live-verification limits in the user handoff.
