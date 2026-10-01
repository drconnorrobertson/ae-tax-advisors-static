# Service search release — October 1, 2026

This release improves existing destinations; it does not claim verified ranking positions or search volume. It preserves current site design, public routes, discovery booking, published fees and the residential-investment focus of cost segregation.

| Buyer intent | Primary destination | Changes |
| --- | --- | --- |
| Cost segregation company and rental-property studies | `/cost-segregation-study/` | Provider scope comparison and implementation checklist; existing residential positioning retained. |
| Airbnb / VRBO / STR tax planning | `/short-term-rental-tax-strategy/` | Service fit, operational review, study coordination, scope, fees and FAQs. |
| Proactive business-owner tax advisory | `/business-owner-tax-planning/` | Implementation deliverables, advisor-selection questions and related service paths. |
| Physician and medical practice tax planning | `/physician-tax-planning/` | Practice-owner and 1099 situations, owner pay, retirement and property coordination. |
| Evaluating a physician tax savings proposal | `/physician-tax-planning-save-six-figures/` | Distinct educational purpose; replaces unsupported savings promises with baseline comparison and hypothetical arithmetic. |
| S-corp owner salary education | `/reasonable-compensation/` | Duty inventory, pay evidence and payroll coordination; links to the analysis service. |
| Reasonable compensation analysis service | `/services/reasonable-compensation/` | Written deliverables, engagement scope and payroll handoff; distinct from the guide. |
| Form 3115 preparation and lookback study implementation | `/form-3115-cost-segregation/` | Correction-path review, history reconciliation, filing responsibilities, fees and FAQs. |
| CPA and tax support for real estate investors | `/real-estate-investor-cpa/` | Portfolio situations, return responsibilities, current team links and separately scoped fees. |
| Tax advisor in Billings, Montana | `/locations/billings/` | Published office details, local service fit and consistent AccountingService data. |

The homepage links to six service situations. Fifteen supporting pages receive contextual service links. Eight rebuilt destinations receive synchronized metadata, breadcrumbs, visible FAQs and corresponding structured data. No credentials, client outcomes, office hours or professional review are invented.

## Maintenance

Run `python3 scripts/optimize_service_search_20261001.py` after legacy generators. This script intentionally owns the eight rebuilt narratives and two marked expansions; future substantive changes should update this script or deliberately replace its ownership. It carries the October 1 date because it represents this release, not the date someone reruns it.

Run the link normalizer and blog index builder. Build the HTML sitemap separately with `build_sitemap_page.build_sitemap_page()` to avoid rebuilding partner content. Regenerate XML with `--preserve-lastmod`, then set lastmod only for substantively changed URLs. Rebuild discovery files afterward. `discovery_sections.md` preserves curated discovery-index additions from earlier releases; the generator normalizes their links and filters out ineligible targets.

The dedicated equipment-leasing consultation is now recognized by the CTA validator as a specialized appointment route. Its calendar is unchanged.

Use the existing schema, editorial, discovery, commercial-integrity, sitemap, link and calculator checks before publishing. Verify the production commit, public page content and booking destination after deployment. Submit only changed canonical pages to IndexNow. IndexNow acceptance is not confirmed indexing, and Google is not an IndexNow participant.

Search Console data is still needed to measure clicks, impressions, query changes and actual average position. Do not label these proposed keyword targets as ranking gains.
