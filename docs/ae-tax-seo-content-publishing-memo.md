# AE Tax Advisors SEO Content Publishing Memo

Date: September 14, 2026  
Repository: `drconnorrobertson/ae-tax-advisors-static`

## Objective

Build the most useful and technically credible online tax-strategy library for high-income business owners and real estate investors. The success metric is qualified organic leads, not raw article count.

## Immediate Direction

The site already contains hundreds of pages and several overlapping articles on the same subjects. The content team should not publish a topic solely because it appears on a keyword list. Every proposed page must first be checked against the repository and live sitemap.

The first operating principle is:

> Strengthen, consolidate, or redirect an existing page when it already serves the same search intent. Create a new page only when the searcher needs a meaningfully different answer.

## Required Workflow for Every Article

1. Search the repository, sitemap, and Google for the target topic and close variations.
2. Identify one primary keyword, one search intent, and one canonical AE page.
3. Decide whether the work is a new page, an expansion of an existing page, or a consolidation of overlapping pages.
4. Prepare an outline that answers the decision the searcher is trying to make.
5. Add an original AE contribution such as a calculation, anonymized client pattern, case analysis, checklist, dataset, or calculator.
6. Support tax claims with primary authority. Use the Internal Revenue Code, Treasury Regulations, IRS forms and instructions, revenue procedures, revenue rulings, and relevant court decisions.
7. Route tax-sensitive content to a named tax reviewer before publication.
8. Add internal links to the pillar page, supporting articles, calculator or case study, and discovery page.
9. Validate the HTML, structured data, links, canonical URL, mobile layout, and sitemap entry.
10. Publish through a focused GitHub pull request that states the target query, existing pages checked, and why the change does not create cannibalization.

## Content Standard

Every publishable page must include:

- A distinct title tag and meta description
- One canonical URL using the `www.aetaxadvisors.com` domain convention
- One H1 followed by a logical H2 and H3 hierarchy
- A direct answer near the top of the page
- A worked example or other first-party value
- Clear assumptions for every calculation
- Primary authority links placed near the claims they support
- Author and tax-review attribution
- An updated or published date
- Article or WebPage structured data, as appropriate
- FAQ schema only when the visible page contains the same questions and answers
- Contextual internal links with descriptive anchor text
- A relevant AE Tax call to action
- A general-information disclaimer

Avoid unsupported savings promises, invented case studies, fixed reasonable-compensation percentages, universal claims, vague phrases such as “the IRS allows,” and duplicate pages with only the industry or city name changed.

## Topic Architecture and Priority

### Priority 1: S Corporation Strategy

Use `/s-corp-tax-strategy/` as the primary pillar. Supporting content should cover genuinely distinct intent such as reasonable compensation, Section 199A wage limits, basis, health insurance, retirement-plan contribution capacity, late elections, shareholder loans, audit corrections, and entity comparisons.

Before creating additional S-corp pages, map and consolidate the existing salary-optimization, reasonable-compensation, tax-savings, late-election, and S-corp-versus-LLC pages. The cluster already contains overlap.

### Priority 2: Cost Segregation by Property and Situation

Build or improve pages for short-term rentals, multifamily, hotels, medical and dental offices, restaurants, self-storage, warehouses, retail centers, car washes, assisted living, salons, and franchises.

Each page needs property-specific assets, a realistic basis allocation, a placed-in-service assumption, depreciation classes, bonus-depreciation treatment, passive-loss limitations, and a decision section explaining when a study may not help.

### Priority 3: Form 3115 and Catch-Up Depreciation

Create one authoritative hub and tightly scoped support pages covering late cost segregation, Section 481(a) adjustments, prior-year depreciation errors, renovations, inherited property, 1031 exchanges, sold property, and recapture. Do not split minor wording variations into separate articles.

### Priority 4: Short-Term Rental Tax Strategy

Own the seven-day and 30-day rules, material-participation tests, spouse participation, property-manager effects, documentation, cost segregation, bonus depreciation, loss-use limitations, and the comparison with real estate professional status.

### Priority 5: Real Estate Professional Status

Build around the 750-hour test, more-than-half test, qualifying activities, investor activities, grouping election, spouse rules, full-time employment, documentation, and Tax Court cases. Case summaries must include facts, taxpayer evidence, IRS position, holding, and the practical lesson.

### Priority 6: High-Income Business Owner Planning

Create distinct, modeled guides for $250,000, $500,000, $750,000, $1 million, $2 million, and $5 million of profit. Each guide must use different assumptions and show why salary, QBI, retirement plans, entity structure, state tax, real estate, and exit planning change at that income level.

### Priority 7: Tax Return Second Opinion

Build a clean path from “my CPA missed this” searches to AE's three-year tax lookback. Cover Form 1120-S, Form 1065, Form 1040, missed depreciation, missed QBI, missed retirement deductions, basis errors, and amendment deadlines.

### Priority 8: Industry Pages

Start with industries where AE has real operating or client expertise: physicians, dentists, chiropractors, attorneys, consultants, agencies, construction, real estate brokers, e-commerce, SaaS, veterinary practices, med spas, salons, franchises, and insurance agencies.

Each page must contain industry-specific economics, entity issues, payroll patterns, retirement-plan opportunities, equipment or real-estate considerations, and exit risks. Replacing one profession name with another is not acceptable.

### Priority 9: Calculators and Original Research

Prioritize tools that answer a money question: S-corp savings, reasonable-compensation scenarios, QBI, Solo 401(k), cost segregation, bonus depreciation, STR loss use, Section 179, vehicle deductions, 1031 exchanges, depreciation recapture, and business-sale tax.

The strongest linkable asset is an anonymized AE cost-segregation report using completed-study data by property type, price range, basis reclassified, recovery period, and estimated first-year deduction. Publish only aggregated and properly anonymized data.

## Cannibalization Rules

Two pages should not target the same primary query and solve the same problem. When overlap is found:

1. Select the URL with the strongest history, backlinks, relevance, and internal-link support.
2. Merge the best unique material into that URL.
3. Redirect weaker URLs to the selected canonical page when technically appropriate.
4. Replace old internal links with links to the selected page.
5. Remove redirected URLs from the sitemap.
6. Recheck title tags, H1s, canonicals, structured data, and related-reading blocks.

Do not use a canonical tag as a substitute for a proper redirect when a duplicate page is being retired.

## Article Brief Template

Every assignment should contain:

- Primary query
- Search intent
- Target reader
- Existing AE pages reviewed
- Canonical URL or proposed slug
- Unique angle
- Required calculation or original evidence
- Primary authorities to review
- H1 and proposed section outline
- Internal links in and out
- CTA
- Named writer
- Named tax reviewer
- Publication deadline
- Update trigger, such as an annual IRS limit or law change

## Quality-Control Checklist

Before merge, confirm:

- The article is materially different from every existing AE page
- Numerical assumptions are visible and calculations reproduce correctly
- Current-year thresholds were checked against primary authority
- The title, description, H1, canonical, Open Graph URL, and JSON-LD URL agree
- Visible FAQ text matches FAQ schema
- There are no broken internal or external links
- Tables work on mobile
- The page uses the current site header, footer, logo, and CTA
- The sitemap includes the final canonical URL once
- The article has a named tax reviewer or is held from publication

## First 30 Days

Week 1: Inventory and map the S-corp, reasonable-compensation, accountable-plan, REPS, material-participation, 1031, and cost-segregation clusters.  
Week 2: Consolidate the highest-overlap S-corp pages and upgrade the pillar with current-year models and primary authority.  
Week 3: Upgrade the cost-segregation pillar and publish one original property-type analysis using real AE data.  
Week 4: Upgrade the STR and REPS pillars, then publish one Tax Court case roundup and one downloadable participation log.

The content team should report pages consolidated, pages redirected, new qualified organic landing pages, impressions, non-brand clicks, discovery-page conversions, and assisted pipeline. Article count by itself is not a meaningful KPI.
