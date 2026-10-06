# Existing-page SEO and accuracy release

This release preserves the homepage, stylesheet and discovery booking
destination. It improves existing owner intent without creating a city or competitor
page batch. `build_seo_audit_release.py` owns the three enriched guides and the online
business/Florida subsections. Run it after any legacy generator that rewrites those pages.
The three rebuilt guides use the current homepage's shared navigation and footer.

## Content and source decisions

- `/blog/how-to-track-material-participation-hours-for-str/`: distinguish material
  participation from REPS, correct Test 3 and individual-provider comparisons, and explain
  reasonable substantiation without claiming daily logs are mandatory. Preserve the original
  August 22 publication date; FAQ copy and schema come from the same maintained answers.
- `/attorney-tax-planning/`: cover solo/S-corporation versus partnership practice decisions,
  law as a QBI specified service business, sustainable retirement funding and records.
  Remove automatic savings and payment-relabeling claims. Preserve the May 5 publication date.
- `/is-cost-segregation-worth-it/`: distinguish deductions from usable tax benefit,
  hypothetical first-year effects from lifetime ROI, and study fees from advisory scope.
- Shared `seo_topics.py` FAQs and their existing body/schema copies correct participation,
  recovery-period, aggregation, suspended-loss and advisory-scope explanations.
- `content_posts_a.py`, `content_posts_b.py`, `build_tools.py` and
  `scripts/batch_states.py` retain those distinctions in affected legacy sources.
- `/services/s-corp-election/` retains online-business-specific ownership, payroll,
  net-profit, deadline and state-obligation questions.
- `/florida/` retains business/rental advisory intent and distinguishes individual income
  tax, corporate depreciation adjustments, 6% state accommodation sales tax and local taxes.

Primary references: [IRS Publication 925](https://www.irs.gov/publications/p925),
[Publication 946](https://www.irs.gov/publications/p946),
[partnership guide](https://www.irs.gov/publications/p541),
[S-corporation compensation](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues),
[QBI overview](https://www.irs.gov/newsroom/qualified-business-income-deduction),
[retirement options](https://www.irs.gov/retirement-plans/choosing-a-retirement-plan-retirement-plan-options),
[Form 3115 instructions](https://www.irs.gov/instructions/i3115),
[Florida accommodation taxes](https://floridarevenue.com/Forms_library/current/brochure/gt800034.pdf),
and [Florida corporate instructions](https://floridarevenue.com/Forms_library/current/f1120n.pdf).
This is editorial source checking, not a claim of human CPA sign-off on a reader's facts.

Commercial wording follows the existing `/pricing/` page: $7,800 standard advisory,
two $3,900 installments 30 days apart, no required recurring annual planning fee,
and separately scoped returns, amendments, studies and additional work. Coverage is
limited by the signed agreement. No new commercial terms are introduced.

## Explicit URL decisions

The 150 baseline sitemap omissions have four decisions: three proposed merges,
one enriched retained page approved for discovery, and 146 review holds.
The separate homepage-graph count of 146 unreachable pages is not this arithmetic.

| Source | Retained target | Reason |
|---|---|---|
| `/tax-planning-for-law-firms/` | `/attorney-tax-planning/` | Empty body; target now covers law firm and partner decisions. |
| `/s-corp-for-online-business/` | `/services/s-corp-election/` | 37-word alias; target now contains a distinct online-business subsection. |
| `/tax-advisor-florida/` | `/florida/` | Overlapping state page with contradictory tax claims; retained page now covers advisory and correct state treatment. |

The merge sources have permanent Vercel redirects and small usable noindex fallback
documents. Their destinations are direct, self-canonical and eligible for discovery.
Current public attorney checks found a 200 self-canonical target with no noindex directive,
308 nonslash-to-slash redirect, and 307 non-www-to-www redirect. A historical Google
inspection reflects a July 21 crawl and an alternate-canonical verdict; current source
correctness does not guarantee Google's immediate canonical selection.

`/is-cost-segregation-worth-it/` is the one retained/enriched omission added to discovery.
`discovery_review_holds.json` records all other 146 omissions with review reasons. Their
URLs and page-level indexing remain unchanged. Holds prevent a generator from silently
promoting unreviewed pages in sitemaps or optional AI indexes. They are not noindex rules.
Before changing a hold, review existing search signals, competing page intent, factual
support and useful original content. The available search-data window does not validate
the most recent site changes; absence of returned rows is inconclusive.

## Public build boundary

Vercel builds the committed static content with `node scripts/build-public.cjs` and serves
`public/`. Deployment does not execute legacy content generators. HTML and allowlisted
assets, discovery files, verification keys and public machine-readable files are staged.
Python generators, repository/configuration files, tests, manifests, private source data
and other research files are excluded. The already-published `/research/` report and its
JSON/CSV exports are explicit exceptions; their public URLs were verified as 200 and
their content is unchanged. No new client records or case-study outcomes are added.

`public-downloads.json` explicitly allowlists the 16 existing public worksheets under
`downloads/` and five public CSV checklists/templates under `assets/`. Other source and
research CSVs are excluded except the already-published research export above. A release
regression test checks every local CSV link across the built HTML, the four STR-kit
downloads, and byte-for-byte preservation of all 21 approved files. The test reproduced
the missing-file failures before the allowlist correction and passes after rebuilding.

The shared discovery inventory honors exact permanent redirects, canonical/meta/header
directives, review holds and source/staging boundaries. The human sitemap uses this same
inventory. Unchanged committed sitemap lastmod values are retained; new approved pages
without a reliable date omit lastmod instead of claiming a sitewide refresh.

## Validation and review

```sh
python3 build_seo_audit_release.py
python3 -c "import build_sitemap_page as B; B.T.write_page('/sitemap/', B.build_sitemap_page())"
python3 generate_sitemap.py
python3 build_discovery_files.py
node scripts/normalize-internal-links.cjs --check
node scripts/build-public.cjs
node scripts/check-sitemaps.cjs
python3 -m unittest test_seo_audit_release test_owner_discovery test_commercial_integrity test_blog_discovery
git diff --check
```

Review the three proposed redirects and tax/commercial copy before merging. Check the
Vercel preview build when available, including the discovery booking flow, public research
downloads and a generator URL that should return 404. No manual deployment, DNS changes
or indexing submissions are part of this release. FAQ markup describes visible answers;
this release makes no FAQ rich-result, AI-citation or keyword-ranking promise.

Local release checks passed: 22 tests, redirect-link check, all sitemap destinations,
public JSON-LD syntax and `git diff --check`. The main map contains 1,565 approved URLs
(the previous 1,564 plus the rewritten ROI guide). The legacy `content_quality.py`
scanner still reports 187 errors and 197 warnings, versus the recorded baseline of
191 and 202. Its findings include held omissions, internal fixtures excluded from the
public build, and existing metadata/content debt. This release does not claim that the
entire legacy editorial backlog passes. The scoped release tests are run locally.
An optional PR-check workflow was kept outside this branch because the existing GitHub
push credential does not grant workflow-file permission; no credential scope was changed.

Follow-up work should prioritize existing guides with observed query demand (MACRS,
business phone/internet deductions, estimated-tax safe harbor, deadlines, and overlapping
STR-loophole intent). Evaluate and improve those pages individually before expanding URLs.
