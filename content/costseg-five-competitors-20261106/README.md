# Cost segregation competitor cohort — November 6, 2026

Refreshes the 15 established pricing, alternatives and AE-comparison pages for Madison SPECS, Engineered Tax Services, KBKG, Cost Segregation Authority and Maven. Preserves every established URL, including `/compare/cost-seg-authority-vs-ae-tax/`.

Adds Madison–ETS, ETS–KBKG and KBKG–Maven comparisons. Refreshes the four existing CSA comparison pages with these providers. Links the 22-page cohort from the compare hub, cost segregation company guide, study service page, study pricing page and real estate tax planning page.

Cost-segregation mode in the shared renderer leads with AE's standalone study price ($1/square foot, $2,000 minimum) and keeps advisory, method-change preparation and full return work separately scoped. CTAs within the article use the established cost-seg-discovery route. Existing first-party event hooks now include that route; event tests cover it and continue to reject personal data and untrusted completion messages.

Evidence checked November 6, 2026: Madison's JavaScript-rendered official FAQ states its typical $4,000–$11,000 fixed-fee range; ETS describes property-specific fixed quotes; KBKG's current linked CPA Handbook gives a general $5,000–$15,000 professional-study range, distinct from its software price example; CSA publishes $3,000 starting studies and its terms establish the CSA Partners business identity; Maven publishes study ranges and separately prices Form 3115 preparation at $995. These are provider descriptions and public price guidance, not independently tested service results or property quotes.

No claims that competitors cannot implement Form 3115, cannot support their reports, or offer only a report are introduced. Report support is distinguished from taxpayer-level return work, and preliminary depreciation estimates are not described as usable deductions or realized savings.

Render: `python3 scripts/refresh-costseg-five-competitors-20261106.py`.
Validate: `node scripts/build-release.cjs`; `python3 scripts/check-five-competitors.py public costseg-five-competitors-20261106`; run the same checker for both previous cohorts; `node scripts/test-booking-events.cjs`.

The 41 previous source pages are hash-protected by preservation.json and remain unchanged. Rerendering this cohort is idempotent. Legacy full-directory generators are not part of the production build; run the researched cohort command after those tools when needed.

Publishing, indexable markup and sitemap inclusion do not establish Google indexing or rank improvements. GSC Wizard subscription access remains unavailable.
