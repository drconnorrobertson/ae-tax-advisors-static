# AE provider comparisons and cost segregation decision guides

This release enriches 100 provider-comparison pages and 16 cost segregation pages. It preserves established URLs and existing body content. Eight major-firm profiles and four distinct cost segregation guides are new; 92 comparison pages and 12 cost segregation pages receive decision-oriented additions. The compare, cost segregation resource, and blog hubs link the relevant pages. Sitemaps retain all prior entries and include the new guides.

The 100 providers are an editorial coverage list, not an objective ranking of the largest or best firms. Ten direct competitors receive extra individual analysis: TaxAlchemy, Hall CPA, Keystone CPA, Taxstra, WCG, Tax Goddess, Prime Path, Neil Jesani Advisors, Peter Holtz CPA, and Rainwater CPA. Major-firm coverage includes Deloitte, PwC, EY, KPMG, RSM, Baker Tilly, BDO, Grant Thornton, CBIZ, and Forvis Mazars; this group is not labeled a revenue-ranked top ten.

## Content decisions

- AE is the first option recommended for a focused planning project. Public competitor services are described respectfully and linked to official sources. No inferred private prices, customer ratings, service deficiencies, or guaranteed savings are added.
- Each provider has an individual buyer situation, scope question, and published service description. Category guidance explains the relevant comparison, such as study versus advisory, practice versus owner work, or company versus founder work.
- Existing alternatives and direct comparison pages retain their existing content. The new enrichment is maintained as a marked section rather than replacing prior approved copy.
- Advisory pricing follows current published terms: $7,800 Strategic / $9,800 Complex, standard two $3,900 installments 30 days apart, no required annual planning renewal, and separate prices for returns, amendments, studies, and additional work.
- Cost segregation content distinguishes a property study from deduction usability, activity classification, participation, and reporting. Technical references use IRS publications and guidance. This is source-checked editorial content, not a claim of individual tax advice or human professional sign-off.
- The redirected W-2 cost segregation blog URL is not revived. Its addition goes to the retained `/short-term-rental-tax-strategy/` route.
- Small-property, quote, manager-participation, and renovation guidance enrich existing topic pages rather than adding overlapping candidates.

## Maintenance

Run `python3 build_seo_campaign_20261007.py` after legacy generators affecting these routes. Source copy is in `content/seo-campaign-20261007/`; the rendered route manifest is `_gen/seo-campaign-20261007-manifest.json`. The generator is idempotent and preserves previous publication dates on enriched pages.

Validation: `python3 -m unittest test_seo_campaign_20261007 test_comparison_release test_commercial_integrity`. The checks cover 100-provider scope, 12 new routes, single H1, self-canonicals, robots eligibility, structured-data parsing, inserted internal links, sitemaps, preservation of existing body content, and shared brand assets. Local browser review covers a new major-firm profile and a cost segregation guide.

## Measurement

After deployment, record the release date and track the comparison and cost segregation groups separately. Review Google Search Console query/page pairs after enough data accumulates; compare equal periods and avoid attributing all movement to this release. Track booked and qualified consultations in analytics or CRM. Competitor names and long-tail phrases are keyword hypotheses until observed data establishes demand. No ranking or traffic outcome is guaranteed.

Google's guidance favors useful original analysis and warns against scaled unoriginal pages made primarily for rankings: https://developers.google.com/search/docs/fundamentals/creating-helpful-content and https://developers.google.com/search/docs/essentials/spam-policies. Expand profiles based on identifiable buyer value and observed demand, rather than multiplying near-identical review/alternative/pricing URLs.
