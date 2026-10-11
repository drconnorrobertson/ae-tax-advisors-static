# Provider comparison release — October 11, 2026

500 new pages: 496 unique provider pairs and four searchable shortlist guides, covering 131 distinct providers. Existing comparison URLs and editorial holds are preserved.

## Selection evidence

AE Search Console, July 11–October 8, 2026, surfaced provider-name queries including Prime Path Advisory (246 impressions on the exact brand query, plus review and Reddit variants), Tax Alchemy reviews (91), Hall CPA reviews (22), and Neil Jesani review variants. These measure visibility of AE's property, not total monthly market search volume. Search Console rows can omit anonymized queries and the retrieved list was capped at 1,000 rows.

Reddit discovery also identified Tax Hive, Collective, 1-800Accountant and Mark J. Kohler as relevant names in buyer discussions. These were editorial discovery signals, not verified customer outcomes or numeric search-volume estimates. The additional weights in demand.json for those four providers are editorial priorities, not impressions. No forum allegation or testimonial is used as a factual comparative claim.

Discovery links:

- https://www.reddit.com/r/AdvancedTaxStrategies/comments/1r5e727/where_do_i_start_high_income_low_financialtax/
- https://www.reddit.com/r/accountants/comments/1oz5bxj/is_tax_hive_worth_it/
- https://www.reddit.com/r/Entrepreneur/comments/o0jt1p/does_anyone_have_experience_using_collectivecom/
- https://www.reddit.com/r/smallbusiness/comments/1aw5wmf
- https://www.reddit.com/r/ChubbyFIRE/comments/slmqza/advice_for_finding_an_accountant_going_into_tax/

## Sources and content

Profiles combine the site's earlier official-source research with newly checked official websites. The source-check file records 104 successful HTTP responses and 27 blocked/error responses; an HTTP success alone does not establish a full editorial re-review. Each profile therefore retains its actual research date (October 1, 8 or 11), and each page links its primary sources. No competitor prices or savings are inferred.

Pairs are selected within broad service-model groups. Breadth is established before remaining slots are filled with demand-prioritized comparisons. Every provider has at least two comparison pages. Comparisons include separate service descriptions, buyer situations, proposal questions, implementation considerations, a fee-scope discussion, AE's disclosed role and research limitations. The four guides expose all 496 comparisons through crawlable links and a provider search field.

## Validation

The dedicated release tests verify the exact page count, unique pairs, 131-provider coverage, titles, canonicals, H1s, structured data, publisher disclosure, internal links, sitemap coverage and public-build inclusion. Existing comparison-release and competitor-coverage tests also pass. The sitemap validator reports no errors.

A broader commercial-integrity test has an existing failure: commercial_intents.json still names /business-owner-tax-planning/ as a direct destination even though vercel.json redirects it to /business-owner-small-business-tax/. Neither file was changed by this release. This does not affect the new batch's direct comparison URLs.
