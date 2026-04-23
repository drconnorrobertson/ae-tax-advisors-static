#!/usr/bin/env python3
"""
AE Tax Advisors Static Site Generator
Generates all HTML pages with exact URL preservation for Vercel deployment.
"""
import os
import json
from datetime import datetime

SITE_URL = "https://aetaxadvisors.com"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ============================================================
# BRANDING
# ============================================================
COLORS = {
    "primary": "#408AAD",      # Teal/blue accent
    "accent": "#CC3366",       # Magenta accent
    "dark": "#333333",         # Dark text
    "medium": "#575A5F",       # Medium gray text
    "light_bg": "#F3F5F7",     # Light gray background
    "white": "#FFFFFF",
    "black": "#000000",
}

# ============================================================
# NAVIGATION
# ============================================================
NAV_ITEMS = [
    {"label": "Home", "url": "/"},
    {"label": "About Us", "url": "/about/"},
    {"label": "Bios", "url": "/bios/"},
    {"label": "Services", "url": "/services/", "children": [
        {"label": "Individual Tax Planning For High Earners", "url": "/individual-tax-planning-high-earners/"},
        {"label": "Business Owner & Small Business Tax Services", "url": "/business-owner-small-business-tax/"},
        {"label": "Deferred Compensation & Equity Compensation Advice", "url": "/deferred-equity-compensation/"},
        {"label": "Retirement & Exit / M&A Tax Strategy", "url": "/retirement-exit-ma-tax-strategy/"},
        {"label": "Multi-state & Global Tax Planning", "url": "/multi-state-global-tax/"},
        {"label": "Estate, Trust & Wealth Transfer Planning", "url": "/estate-trust-wealth-transfer/"},
        {"label": "Tax Compliance & IRS Representation", "url": "/tax-compliance-irs-representation/"},
        {"label": "Cost Segregation Studies", "url": "/cost-segregation-studies-for-real-estate-investors/"},
    ]},
    {"label": "Case Studies", "url": "/case-studies/"},
    {"label": "Resources", "url": "/resources/", "children": [
        {"label": "Blog", "url": "/blog/"},
        {"label": "FAQ", "url": "/faq/"},
        {"label": "Guides & Whitepapers", "url": "/guides/"},
        {"label": "Glossary", "url": "/glossary/"},
    ]},
    {"label": "Contact Us", "url": "/contact/"},
]

# ============================================================
# ALL POST URLS (from sitemaps)
# ============================================================
POST_SLUGS = [
    "blog",
    "10-common-tax-mistakes-most-professionals-make-every-year",
    "what-a-tax-advisor-really-does-and-why-it-matters-for-you",
    "the-ultimate-guide-to-tax-planning-for-high-income-w-2-earners",
    "how-ae-tax-advisors-helps-you-keep-more-of-what-you-earn",
    "understanding-adjusted-gross-income-and-how-to-reduce-it",
    "the-difference-between-tax-preparation-and-tax-planning",
    "should-hire-professional-tax",
    "tax-credits-vs-deductions-which-saves-you-more",
    "how-to-legally-lower-your-tax-bill-before-december-31",
    "how-ae-tax-advisors-designs-tax-plans-for-w-2-clients",
    "how-to-convert-w-2-income-into-passive-income-legally",
    "the-hidden-tax-benefits-of-hiring-family-members-in-your-business",
    "the-top-tax-write-offs-most-small-businesses-miss",
    "choose-right-entity-type",
    "build-bulletproof-audit-defense",
    "how-to-legally-pay-yourself-from-your-business",
    "advanced-strategies-for-reducing-self-employment-tax",
    "build-tax-advantaged-retirement-plan",
    "plan-quarterly-taxes-without",
    "how-to-prepare-for-year-end-tax-planning-like-a-pro",
    "the-smart-way-to-handle-business-vehicle-deductions",
    "depreciation-tax-strategy-7",
    "build-audit-proof-tax-documentation",
    "the-legal-way-to-deduct-meals-and-travel",
    "how-to-legally-pay-family-members-through-your-business",
    "use-family-management-company",
    "entity-restructuring-tax-3",
    "how-to-legally-combine-real-estate-and-business-ownership-for-tax-advantage",
    "use-holding-company-protect",
    "the-difference-between-tax-preparation-and-tax-planning-and-why-it-matters",
    "how-to-legally-reduce-self-employment-tax-through-entity-design",
    "the-ultimate-guide-to-s-corporation-salary-optimization",
    "the-ultimate-tax-checklist-for-small-business-owners",
    "top-deductions-most-small",
    "build-audit-proof-recordkeeping-system",
    "how-to-legally-deduct-meals-travel-and-entertainment",
    "deduct-vehicle-right-way",
    "the-complete-guide-to-business-travel-deductions",
    "deduct-home-office-correctly",
    "the-ultimate-guide-to-hiring-family-members-in-your-business",
    "set-accountable-plan-business",
    "depreciation-tax-strategy-7-5",
    "depreciation-tax-strategy-7-5-2",
    "how-to-defer-or-eliminate-capital-gains-through-a-1031-exchange",
    "how-to-use-cost-segregation-to-accelerate-real-estate-deductions",
    "how-to-legally-reimburse-yourself-for-home-office-expenses",
    "the-smart-way-to-deduct-vehicle-expenses-for-business",
    "the-complete-guide-to-travel-meals-and-entertainment-deductions",
    "the-smart-way-to-file-taxes-if-you-work-multiple-jobs",
    "10-common-tax-mistakes-employees-make-with-withholding",
    "how-to-deduct-business-gifts-bonuses-and-incentives",
    "the-ultimate-guide-to-fringe-benefits-and-tax-free-employee-perks",
    "the-ultimate-guide-to-fringe-benefits-and-tax-free-employee-perks-2",
    "how-to-write-off-your-cell-phone-and-internet-for-business-use",
    "the-complete-guide-to-hiring-family-members-in-your-business",
    "the-ultimate-guide-to-s-corporation-salary-optimization-2",
    "build-accountable-plan-business",
    "the-business-owners-guide-to-cost-segregation-studies-and-building-component-analysis",
    "the-business-owners-guide-to-qualified-improvement-property-qip-and-tenant-renovations",
    "the-business-owners-guide-to-179d-and-45l-energy-efficiency-tax-deductions",
    "the-business-owners-guide-to-installment-sales-and-deferred-gain-strategies",
    "the-business-owners-guide-to-the-qualified-business-income-qbi-deduction",
    "the-business-owners-guide-to-section-1202-qualified-small-business-stock-qsbs",
    "depreciation-tax-strategy-7-3",
    "the-business-owners-guide-to-passive-loss-rules-and-real-estate-professional-status-reps",
    "the-business-owners-guide-to-opportunity-zones-and-capital-gains-deferral",
    "depreciation-tax-strategy-7-4",
    "depreciation-tax-strategy-7-4-2",
    "depreciation-tax-strategy-7-2",
    "the-ultimate-guide-to-business-asset-disposal-and-replacement",
    "depreciation-tax-strategy-7-2-2",
    "the-complete-guide-to-1031-exchanges-and-tax-deferral",
    "the-business-owners-guide-to-passive-loss-rules-and-real-estate-professional-status",
    "the-business-owners-guide-to-the-at-risk-rules-and-loss-limitation-planning",
    "the-business-owners-guide-to-section-1031-like-kind-exchanges-and-tax-deferral",
    "the-business-owners-guide-to-section-754-partnership-basis-adjustments",
    "the-business-owners-guide-to-section-704c-built-in-gains-and-loss-allocations",
    "the-business-owners-guide-to-section-163j-interest-deduction-limitation-and-real-estate-election",
    "the-business-owners-guide-to-section-721-partnership-contributions-and-tax-deferral",
    "the-business-owners-guide-to-section-707-transactions-between-partner-and-partnership",
    "the-business-owners-guide-to-section-731-distributions-and-recognized-gain",
    "the-business-owners-guide-to-section-736-payments-to-retiring-or-deceased-partners",
    "the-business-owners-guide-to-section-751-hot-assets-and-ordinary-income-recharacterization",
    "the-business-owners-guide-to-section-743b-basis-adjustments-after-partner-transfer",
    "the-business-owners-guide-to-section-704d-loss-limitations-and-partner-basis-constraints",
    "the-business-owners-guide-to-section-465-at-risk-limitations-and-loss-recapture",
    "the-business-owners-guide-to-section-469-passive-activity-loss-rules-and-material-participation",
    "the-business-owners-guide-to-section-199a-qualified-business-income-qbi-deduction",
    "depreciation-tax-strategy-6",
    "the-business-owners-guide-to-section-163j-business-interest-limitation-rules",
    "the-business-owners-guide-to-section-453-installment-sales-and-deferred-gain-recognition",
    "the-business-owners-guide-to-section-1202-qualified-small-business-stock-qsbs-exclusion",
    "the-business-owners-guide-to-section-721-nonrecognition-rules-and-partnership-contributions",
    "the-business-owners-guide-to-section-704b-capital-accounts-and-partner-allocations",
    "the-business-owners-guide-to-section-754-basis-adjustments-and-partnership-step-ups",
    "the-business-owners-guide-to-section-751-hot-assets-and-ordinary-income-recharacterization-2",
    "the-business-owners-guide-to-section-465-at-risk-limitations-and-loss-recapture-2",
    "the-business-owners-guide-to-section-469-passive-activity-loss-rules-and-material-participation-2",
    "the-business-owners-guide-to-section-1031-like-kind-exchanges-and-deferral-strategy",
    "depreciation-tax-strategy-5",
    "depreciation-tax-strategy-4",
    "why-clean-books-matter-for-high-income-business-owners-and-how-ae-tax-advisors-fixes-financial-chaos",
    "real-estate-bookkeeping-10",
    "real-estate-bookkeeping-9",
    "cash-accrual-accounting-choose-3",
    "every-business-needs-monthly",
    "real-estate-bookkeeping-8",
    "what-every-business-owner-should-know-about-reconciling-accounts",
    "real-estate-bookkeeping-7",
    "why-your-accounting-method-matters-more-than-you-think",
    "why-your-accounting-method-matters-for-taxes-and-financial-clarity",
    "why-every-business-needs-a-monthly-close-process-and-how-ae-tax-advisors-handles-it",
    "real-estate-bookkeeping-6",
    "real-estate-bookkeeping-5",
    "cash-accrual-accounting-choose-2",
    "why-your-accounting-method-matters-more-than-you-think-2",
    "how-to-keep-books-as-a-high-earner-with-side-business-income",
    "real-estate-bookkeeping-4",
    "cash-accrual-accounting-choose",
    "real-estate-bookkeeping-3",
    "high-net-worth-tax-planning-strategies-for-families",
    "sophisticated-tax-planning-for-high-net-worth-individuals",
    "estate-tax-planning-advice-for-high-net-worth-families",
    "tax-planning-for-executives-with-stock-options",
    "tax-minimization-strategies-for-high-net-worth-entrepreneurs",
    "international-tax-planning-for-high-net-worth-individuals",
    "choose-right-high-net",
    "best-tax-advisor-for-high-net-worth-clients",
    "high-net-worth-tax-planning-services-in-your-city",
    "wealth-preservation-tax-planning-for-high-net-worth-individuals",
    "tax-planning-for-ultra-high-net-worth-families",
    "retirement-tax-planning-for-high-net-worth-couples",
    "high-net-worth-estate-and-gift-tax-planning-advice",
    "tax-estate-planning-high",
    "how-to-lower-taxes-on-high-income-for-high-net-worth-individuals",
    "tax-planning-for-high-net-worth-real-estate-investors",
    "tax-planning-strategies-for-high-net-worth-trust-and-estate",
    "bespoke-tax-planning-for-high-net-worth-clients",
    "high-net-worth-tax-compliance-and-planning-services",
    "tax-planning-for-high-net-worth-individuals-with-multiple-properties",
    "need-tax-advisor-specializing",
    "advanced-tax-reduction-strategies-for-high-net-worth-investors",
    "international-tax-planning-for-high-net-worth-individuals-2",
    "tax-optimization-strategies-for-high-net-worth-entrepreneurs",
    "tax-planning-for-high-net-worth-individuals-with-complex-investment-portfolios",
    "tax-planning-strategies-for-high-net-worth-individuals-with-business-exit-events",
    "tax-planning-for-high-net-worth-individuals-with-multi-state-income",
    "tax-planning-for-high-net-worth-families-with-generational-wealth-strategies",
    "tax-planning-for-high-net-worth-individuals-with-private-equity-income",
    "tax-planning-for-high-net-worth-individuals-with-stock-options-and-equity-compensation",
    "tax-planning-for-high-net-worth-individuals-transitioning-into-retirement",
    "tax-planning-for-high-net-worth-individuals-with-significant-real-estate-holdings",
    "tax-planning-for-high-net-worth-individuals-using-advanced-charitable-strategies",
    "tax-planning-for-high-net-worth-individuals-with-complex-partnership-and-k1-income",
    "tax-planning-for-high-net-worth-individuals-facing-large-capital-gains-events",
    "tax-planning-for-high-net-worth-individuals-with-international-investments",
    "tax-planning-for-high-net-worth-individuals-with-multiple-business-entities",
    "tax-planning-for-high-net-worth-individuals-with-deferred-compensation-packages",
    "tax-planning-for-high-net-worth-individuals-with-multiple-streams-of-passive-income",
    "how-business-owners-can-cut-taxes-without-risky-moves",
    "s-corp-vs-llc-what-changes-on-your-taxes-and-when-its-worth-it",
    "short-term-rental-tax-planning-the-playbook-most-hosts-never-use",
    "cost-segregation-explained-in-plain-english-for-real-estate-owners",
    "material-participation-for-real-estate-how-to-document-it-without-guessing",
    "real-estate-professional-status-what-it-is-and-what-the-irs-looks-for",
    "passive-activity-loss-rules-why-i-own-real-estate-is-not-enough",
    "real-estate-bookkeeping-2",
    "top-tax-deductions-business-owners-miss-because-they-lack-documentation",
    "accountable-plans-the-right-way-to-reimburse-yourself-from-your-business",
    "augusta-rule-for-business-owners-when-it-works-and-how-to-do-it-safely",
    "qbi-deduction-a-practical-guide-for-business-owners",
    "payroll-for-s-corps-reasonable-compensation-without-the-headache",
    "long-term-rental-tax-planning-depreciation-repairs-and-recordkeeping",
    "mid-term-rentals-the-tax-and-accounting-setup-most-owners-skip",
    "repairs-improvements-rule-changes-2",
    "pay-kids-family-business-2",
    "business-owners-can-cut",
    "s-corp-vs-llc-tax-savings",
    "short-term-rental-tax-planning-playbook",
    "cost-segregation-explained",
    "material-participation-real-estate-documentation",
    "real-estate-professional-status-reps",
    "passive-activity-loss-rules-real-estate",
    "real-estate-bookkeeping",
    "top-tax-deductions-business",
    "augusta-rule-business-owners",
    "accountable-plans-right-way",
    "qbi-deduction-guide",
    "reasonable-compensation-s-corp-payroll",
    "long-term-rental-tax-planning",
    "mid-term-rental-tax-accounting-setup",
    "repairs-improvements-rule-changes",
    "pay-kids-family-business",
    "home-office-deduction-business-owners",
    "vehicle-deductions-mileage-logs",
    "estimated-taxes-business-owners",
    "year-end-tax-planning-checklist",
    "1099s-small-business-system",
    "entity-restructuring-tax",
    "hiring-first-employee-payroll-setup",
    # post-sitemap2
    "s-corp-election-timing-late-relief",
    "cost-segregation-when-it-makes-sense",
    "short-term-rental-tax-planning-basics",
    "real-estate-professional-status-documentation",
    "home-office-deduction-the-compliance-first-guide-for-owners",
    "vehicle-deductions-mileage-logs-actual-expenses-and-what-works-best",
    "estimated-taxes-how-to-avoid-penalties-and-cash-flow-surprises",
    "year-end-tax-planning-checklist-20-moves-to-review-before-december-31",
    "1099s-small-businesses-simple",
    "entity-restructuring-tax-2",
    "hiring-first-employee-payroll",
    "s-corp-election-timing-deadlines-late-relief-and-how-to-fix-mistakes",
    "cost-segregation-when-it-works-when-it-doesnt-and-how-to-decide",
    "short-term-rental-tax-planning-the-core-concepts-most-hosts-miss",
    "real-estate-professional-status-the-documentation-system-that-makes-or-breaks-it",
    "rental-losses-and-passive-activity-rules-why-your-tax-loss-might-not-reduce-taxes-yet",
    "tax-planning-strategies-high-net-worth-individuals",
    "physician-tax-planning-save-six-figures",
    "w-2-tax-reduction-3",
    "s-corp-tax-strategies-high-net-worth-business-owners",
    "cost-segregation-studies-real-estate-tax-savings",
    "estate-tax-planning-strategies-high-net-worth-families",
    "tax-strategy-7",
    "tax-strategy-6",
    "real-estate-professional-status-qualify-save-taxes",
    "retirement-tax-planning-minimize-taxes-retirement-income",
    "cryptocurrency-tax-planning-high-net-worth-investors",
    "attorney-tax-planning-law-partners-big-law",
    "business-exit-tax-planning-minimize-taxes-selling-company",
    "multi-state-tax-planning-high-income-earners",
    "deferred-compensation-planning-high-income-executives",
    "defined-benefit-plans-tax-shelter-high-income-business-owners",
    "trusts-tax-planning-irrevocable-trusts-reduce-taxes",
    "irs-audit-defense-high-net-worth-taxpayers",
    "short-term-rental-tax-loophole-offset-w2-income",
    "1031-exchange-strategies-real-estate-investors",
    "net-investment-income-tax-reduce-3-8-percent-surtax",
    "tax-planning-tech-professionals-stock-options-rsu-espp",
    "tax-efficient-investing-strategies-high-net-worth-portfolios",
    "qualified-opportunity-zones-tax-deferred-investing",
    "depreciation-tax-strategy-3",
    "tax-planning-dentists-dental-practice-owners",
    "capital-gains-tax-planning-minimize-investment-profits",
    "solo-401k-plans-retirement-savings-self-employed",
    "tax-strategy-5",
    "tax-strategy-5-2",
    "tax-planning-real-estate-developers-builders",
    "tax-loss-carryforward-prior-year-losses-reduce-taxes",
    "qualified-business-income-deduction-20-percent-pass-through",
    "international-tax-planning-us-expats-global-investors",
    "energy-tax-credits-high-net-worth-investors-clean-energy",
    "tax-strategy-4",
    "tax-planning-startup-founders-formation-to-exit",
    "depreciation-tax-strategy-2",
    "alternative-minimum-tax-high-earners-minimize-amt",
    "estimated-tax-payments-avoiding-penalties-high-income",
    "tax-strategy-3",
    "tax-planning-private-equity-hedge-fund-investors",
    "w-2-tax-reduction-2",
    "year-end-tax-planning-checklist-high-net-worth",
    "tax-benefits-owning-rental-property-high-income-investors",
    "hiring-spouse-tax-benefits",
    "incentive-stock-options-vs-non-qualified-tax-comparison",
    "tax-planning-surgeons-surgical-specialists",
    "backdoor-roth-ira-high-earners-access-roth-benefits",
    "salt-deduction-cap-workarounds-high-income-taxpayers",
    "tax-implications-divorce-high-net-worth-individuals",
    "donor-advised-funds-high-earners",
    "tax-planning-professional-athletes-entertainers",
    "tax-strategy-2",
    "tax-credits-vs-tax-deductions-understanding-difference",
    "tax-planning-strategy-4",
    "ae-tax-advisors-reviews",
    "why-high-net-worth-clients-choose-ae-tax-advisors",
    "tax-planning-strategy-3",
    "ae-tax-advisors-faq",
    "ae-tax-advisors-vs-tax-relief-companies",
    "tax-planning-strategy-2",
    "cost-segregation-study",
    "w-2-tax-reduction",
    "tax-savings-strategy",
    "ae-tax-advisors-news-press-coverage",
    "makes-tax-advisors-different",
    "ae-tax-advisors-mission-values",
    "how-to-choose-tax-advisor-ae-tax-advisors-guide",
    "ae-tax-advisors-irs-compliance-audit-defense",
    "tax-strategy",
    "ae-tax-advisors-complaints",
    "tax-planning-strategy",
    "is-ae-tax-advisors-trustworthy",
    "the-3-year-tax-lookback-how-to-recover-thousands-in-missed-deductions",
    "cost-segregation-studies-explained-how-real-estate-investors-save-50k-100k-in-year-1",
    "s-corp-vs-c-corp-which-structure-saves-you-more-in-taxes",
    "how-high-income-w-2-earners-can-legally-reduce-their-tax-bill-by-50k",
    "short-term-rental-tax-loophole-the-str-strategy-that-offsets-w-2-income",
    "depreciation-tax-strategy",
    "5-tax-mistakes-real-estate-investors-make-and-how-to-fix-them",
    "what-is-a-tax-strategy-session-what-to-expect-when-you-work-with-ae-tax-advisors",
    "how-to-file-amended-tax-return-form-1040-x-guide",
    "real-estate-professional-status-reps-how-to-qualify",
    "what-is-a-cost-segregation-study",
    "tax-planning-for-doctors-physician-tax-strategies",
    "1031-exchange-explained-defer-capital-gains",
    "how-much-does-a-tax-advisor-cost",
    "qualified-opportunity-zones-2026-tax-benefits",
    "entity-restructuring-change-business-structure-tax-savings",
    "tax-deductions-rental-property-owners-complete-checklist",
    "cpa-costing-you-money",
    "irs-letter-what-to-do",
    "unfiled-tax-returns-help",
    "irs-penalty-abatement",
    "offer-in-compromise-irs",
    "stop-irs-wage-garnishment",
    "irs-tax-lien-vs-levy",
    "irs-installment-agreement",
    "currently-not-collectible-irs",
    "who-founded-ae-tax-advisors",
    "ae-tax-advisors-consultation",
]

# ============================================================
# ALL PAGE SLUGS (from page-sitemap.xml)
# ============================================================
PAGE_SLUGS = [
    "",  # homepage
    "3-year-tax-lookback-cleanup",
    "alicia-zoom",
    "strategy",
    "alicia-60min",
    "alicia-45min",
    "alicia-30min",
    "ashley-60min",
    "ashley-45min",
    "ashley-30min",
    "christina-30min",
    "christina-60min",
    "christina-45min",
    "60-minute-consultation",
    "7-day-recap",
    "7-day-followup",
    "resources-2",
    "retirement-exit-ma-tax-strategy",
    "services",
    "tax-compliance-irs-representation",
    "tax-filing-and-compliance-services",
    "tax-resolution-services-2",
    "zoom-consultation",
    "entrepreneurs-small-business-owners",
    "estate-trust-wealth-transfer",
    "executives-corporate-professionals",
    "glossary",
    "guides",
    "jack-zoom",
    "krister-zoom",
    "mark-zoom",
    "multi-state-global-tax",
    "nick-zoom",
    "onboarding",
    "onboarding-call",
    "guide",
    "real-estate-investors",
    "precall",
    "testimonials",
    "tax-services",
    "deferred-equity-compensation",
    "business-owner-small-business-tax",
    "about",
    "advanced-tax-planning-services",
    "30-day-followup",
    "30-minute-consultation",
    "30-day-recap",
    "bios",
    "connor-zoom",
    "individual-tax-planning-high-earners",
    "45-minute-consultation",
    "privacy-policy",
    "medical-legal-professionals",
    "discovery",
    "contact",
    "faq",
    "case-studies",
    "cost-segregation-studies-for-real-estate-investors",
    "cost-seg-estimator",
    "disclaimer",
    "christina-zoom",
    "s-corp-and-real-estate-coordination-for-active-businesses",
    "saving-over-185000-in-annual-taxes-for-a-high-earning-technology-executive-through-household-level-tax-engineering",
    "short-term-rental-tax-planning-and-preparation-2",
    "tech-executive-using-multiple-short-term-rentals-to-systematically-offset-w-2-income",
    "rental-tax-filing-cleanup-and-catch-up-support",
    "reducing-rsu-driven-tax-volatility-for-a-700000-w-2-tech-sales-executive-using-an-investment-tax-credit-strategy",
    "reducing-an-890000-w-2-tax-liability-by-layering-an-investment-tax-credit-strategy-and-a-short-term-rental-acquisition-in-the-same-year",
    "thank-you",
    "significant-reduction-in-w-2-driven-tax-exposure-without-aggressive-assumptions-or-complex-structures",
    "senior-executive-using-str-ltr-to-reduce-w-2-exposure-before-retirement",
    "reducing-real-estate-tax-exposure-through-short-term-rental-classification-and-bonus-depreciation",
    "reducing-business-tax-liability-through-the-rd-payroll-tax-credit-and-entity-level-planning",
    "reducing-business-owner-tax-exposure-through-a-c-corporation-election-fringe-benefits-and-earnings-retention",
    "reducing-a-volatile-commission-based-w-2-tax-burden-by-over-160000-through-income-stabilization-and-timing-strategy",
    "reducing-a-seven-figure-w-2-tax-bill-using-short-term-rental-losses-and-accelerated-depreciation",
    "executive-tax-planning-case-study",
    "reducing-a-seven-figure-executive-tax-bill-through-entity-structuring-accountable-plans-and-withholding-optimization",
    "reducing-a-seven-figure-business-owners-tax-bill-through-accounting-method-optimization-reimbursement-layering-and-depreciation-timing",
    "reducing-a-senior-corporate-leaders-tax-liability-by-over-190000-through-deferred-income-strategy-solar-credits-and-real-estate-offsets",
    "reducing-a-national-consulting-executives-tax-liability-by-over-155000-through-income-timing-and-asset-based-offsets",
    "reducing-a-high-income-professionals-tax-bill-through-multi-entity-coordination-loss-utilization-and-timing-discipline",
    "reducing-a-high-income-finance-executives-tax-liability-by-over-145000-through-equity-coordination-and-asset-based-offsets",
    "reducing-a-high-w-2-earners-tax-bill-through-short-term-rental-losses-long-term-rental-depreciation-and-income-coordination",
    "reducing-a-high-w-2-and-business-owners-tax-liability-to-near-zero-through-short-term-rental-conversion-bonus-depreciation-and-credit-coordination",
    "reducing-a-dual-high-income-physician-household-tax-bill-by-over-265000-using-real-estate-energy-credits-and-advanced-income-coordination",
    "reducing-a-c-suite-manufacturing-executives-tax-liability-by-over-210000-through-income-sequencing-and-incentivized-asset-planning",
    "reducing-a-big-law-partners-tax-liability-by-over-275000-through-asset-based-planning-and-income-coordination",
    "reducing-a-980000-combined-w-2-tax-burden-for-a-dual-physician-household-using-a-short-term-rental-strategy",
    "reducing-a-720000-w-2-tax-liability-using-an-investment-tax-credit-strategy-without-business-ownership",
    "reducing-a-640000-w-2-tax-burden-using-a-short-term-rental-and-accelerated-depreciation-strategy",
    "reducing-a-580000-w-2-tax-burden-through-short-term-rental-conversion-and-accelerated-depreciation-catch-up",
    "reducing-a-560000-w-2-tax-burden-using-an-investment-tax-credit-strategy-with-multi-year-carryforward-planning",
    "reducing-a-510000-w-2-tax-liability-through-a-short-term-rental-strategy-without-prior-real-estate-experience",
    "reducing-a-1200000-w-2-tax-burden-for-a-public-company-cfo-using-a-layered-conservative-tax-planning-strategy",
    "schedule-a-real-estate-tax-consultation-2",
    "real-estate-professional-status-and-material-participation-support",
    "real-estate-entity-structuring-for-rental-portfolios",
    "real-estate-bookkeeping-review-for-tax-readiness",
    "press",
    "physician-using-long-term-rentals-and-form-3115-catch-up-to-reduce-w-2-tax",
    "physician-household-using-one-str-and-one-ltr-conservatively",
    "multi-state-real-estate-tax-planning",
    "mid-term-rental-tax-planning-and-preparation",
    "married-w-2-household-using-str-long-term-rental-coordination",
    "married-w-2-couple-using-long-term-rentals-and-depreciation-timing",
    "long-term-rental-tax-planning-and-preparation-3",
    "long-term-rental-tax-planning-and-preparation-2",
    "high-income-w-2-earner-using-s-corporation-election-accountable-plan-and-bonus-timing-optimization",
    "high-income-tech-employee-using-str-conversion-to-offset-equity-compensation",
    "high-w-2-earner-using-one-str-and-strategic-long-term-rental-improvements",
    "high-w-2-earner-using-long-term-rentals-form-3115-catch-up-and-depreciation-timing",
    "high-w-2-earner-using-a-single-str-to-stabilize-taxes-over-multiple-years",
    "high-w-2-earner-offsetting-income-through-a-newly-acquired-short-term-rental-in-year-one",
    "eliminating-federal-income-tax-using-obscure-accounting-elections-compensation-arbitrage-and-timing-asymmetry",
    "eliminating-federal-income-tax-through-solar-itc-bonus-depreciation-and-entity-coordination",
    "eliminating-federal-income-tax-through-multi-entity-structuring-reimbursement-stacking-depreciation-and-credits",
    "eliminating-federal-income-tax-through-equipment-acquisition-bonus-depreciation-rd-credits-str-losses-and-entity-sequencing",
    "eliminating-federal-income-tax-through-a-form-3115-mega-catch-up-long-term-rental-optimization-and-multi-year-sequencing",
    "eliminating-federal-income-tax-for-a-seven-figure-w-2-earner-through-entity-layering-executive-benefits-credits-and-loss-sequencing",
    "dual-w-2-household-using-one-str-and-one-ltr-to-control-tax-volatility",
    "discovery-youtube",
    "discovery-facebook",
    "discover",
    "depreciation-and-fixed-asset-review-for-rental-properties",
    "cost-segregation-analysis-and-implementation-support",
    "correcting-missed-depreciation-and-reducing-a-620000-w-2-tax-burden-using-a-short-term-rental-reclassification-and-form-3115-catch-up-strategy",
    "ae-tax-advisors-onboarding-call-today-3",
    "ae-tax-advisors-onboarding-form",
    "ae-tax-advisors-onboarding-call-today-2",
    "ae-tax-advisors-onboarding-call-today",
    "ae-tax-advisors-onboarding-calendar",
    "achieving-over-310000-in-annual-tax-reduction-through-executive-compensation-and-income-timing-strategy",
    "1031-exchange-tax-coordination",
    "schedule-a-real-estate-tax-consultation",
    "terms-of-service",
    "long-term-rental-tax-planning-and-preparation",
    "resources",
    "industries-clients",
]

# ============================================================
# CATEGORY SLUGS
# ============================================================
CATEGORY_SLUGS = [
    "tax-basics-that-build-trust",
    "focused-strategies",
    "business-owner-tax-planning",
    "advanced-tax-strategies",
    "real-estate-depreciation",
    "retirement-legacy-planning",
    "trusts-family-strategy",
    "tax-deadlines-year-end-checklists",
    "audit-defense-compliance",
    "modern-tax-education-strategy-insights",
]


def slug_to_title(slug):
    """Convert a URL slug to a readable title."""
    if not slug:
        return "AE Tax Advisors | Tax Planning for High-Income Professionals"
    title = slug.replace("-", " ").title()
    # Fix common acronyms
    for old, new in [
        ("Irs", "IRS"), ("W 2", "W-2"), ("S Corp", "S-Corp"),
        ("C Corp", "C-Corp"), ("Llc", "LLC"), ("Qbi", "QBI"),
        ("Str", "STR"), ("Ltr", "LTR"), ("Ae ", "AE "),
        ("Reps", "REPS"), ("Rsu", "RSU"), ("Amt", "AMT"),
        ("Espp", "ESPP"), ("1031", "1031"), ("Rd ", "R&D "),
        ("Cfo", "CFO"), ("Faq", "FAQ"), ("M A", "M&A"),
        ("Qip", "QIP"), ("45l", "45L"), ("179d", "179D"),
        ("Cpa", "CPA"), ("1099", "1099"), ("401k", "401(k)"),
        ("3115", "3115"), ("Itc", "ITC"),
    ]:
        title = title.replace(old, new)
    return title


def get_base_html(title, content, canonical_path="/", page_type="page", description=""):
    """Generate full HTML page with branding."""
    if not description:
        description = f"{title} - AE Tax Advisors provides proactive tax planning for high-income professionals, executives, physicians, attorneys, and business owners."

    canonical_url = f"{SITE_URL}{canonical_path}"

    # Build nav HTML
    nav_html = ""
    for item in NAV_ITEMS:
        if "children" in item:
            children_html = ""
            for child in item["children"]:
                children_html += f'<a href="{child["url"]}" class="dropdown-item">{child["label"]}</a>\n'
            nav_html += f'''<div class="nav-dropdown">
                <a href="{item["url"]}" class="nav-link">{item["label"]} <span class="arrow">&#9662;</span></a>
                <div class="dropdown-content">{children_html}</div>
            </div>\n'''
        else:
            active = ' class="nav-link active"' if item["url"] == canonical_path else ' class="nav-link"'
            nav_html += f'<a href="{item["url"]}"{active}>{item["label"]}</a>\n'

    # Schema markup
    schema_local_business = json.dumps({
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "AE Tax Advisors",
        "description": "Proactive tax planning for high-income professionals, executives, physicians, attorneys, and business owners earning $500K or more.",
        "url": SITE_URL,
        "telephone": "",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Pittsburgh",
            "addressRegion": "PA",
            "addressCountry": "US"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "5",
            "reviewCount": "127",
            "bestRating": "5",
            "worstRating": "1"
        },
        "priceRange": "$$$",
        "openingHours": "Mo-Fr 09:00-17:00",
        "sameAs": []
    }, indent=2)

    schema_org = json.dumps({
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "AE Tax Advisors",
        "url": SITE_URL,
        "logo": f"{SITE_URL}/assets/logo.svg",
        "description": "Advanced tax strategies for high-net-worth individuals and business owners."
    }, indent=2)

    # FAQ schema for FAQ page
    faq_schema = ""
    if canonical_path == "/faq/":
        faq_schema = f'''<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": "What does AE Tax Advisors do?", "acceptedAnswer": {"@type": "Answer", "text": "AE Tax Advisors provides proactive, year-round tax planning for high-income professionals, executives, physicians, attorneys, and business owners earning $500K or more."}},
        {"@type": "Question", "name": "How much does AE Tax Advisors cost?", "acceptedAnswer": {"@type": "Answer", "text": "Our advisory engagement fee is $7,800 per year, which includes year-round proactive tax planning, quarterly check-ins, mid-year projections, and direct advisor access."}},
        {"@type": "Question", "name": "Who is AE Tax Advisors best suited for?", "acceptedAnswer": {"@type": "Answer", "text": "High-income W-2 earners, business owners, real estate investors, physicians, attorneys, executives, and anyone earning $500K or more who wants to legally reduce their tax liability."}},
        {"@type": "Question", "name": "Is AE Tax Advisors a CPA firm?", "acceptedAnswer": {"@type": "Answer", "text": "AE Tax Advisors is a tax advisory firm focused on proactive tax planning and strategy. We coordinate with your CPA or tax preparer to implement strategies."}},
        {"@type": "Question", "name": "What is the 3-Year Tax Lookback?", "acceptedAnswer": {"@type": "Answer", "text": "The 3-Year Tax Lookback is our process of reviewing your last three years of tax returns to identify missed deductions, credits, and planning opportunities that may result in amended return refunds."}},
    ]
}, indent=2)}
    </script>'''

    # Service schema for service pages
    service_schema = ""
    service_pages = [
        "/individual-tax-planning-high-earners/",
        "/business-owner-small-business-tax/",
        "/deferred-equity-compensation/",
        "/retirement-exit-ma-tax-strategy/",
        "/multi-state-global-tax/",
        "/estate-trust-wealth-transfer/",
        "/tax-compliance-irs-representation/",
        "/cost-segregation-studies-for-real-estate-investors/",
        "/services/",
    ]
    if canonical_path in service_pages:
        service_schema = f'''<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": title,
    "provider": {
        "@type": "ProfessionalService",
        "name": "AE Tax Advisors",
        "url": SITE_URL
    },
    "description": description,
    "areaServed": {
        "@type": "Country",
        "name": "United States"
    }
}, indent=2)}
    </script>'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | AE Tax Advisors</title>
    <meta name="description" content="{description[:160]}">
    <link rel="canonical" href="{canonical_url}">
    <meta property="og:title" content="{title} | AE Tax Advisors">
    <meta property="og:description" content="{description[:160]}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="AE Tax Advisors">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{title} | AE Tax Advisors">
    <meta name="twitter:description" content="{description[:160]}">
    <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/style.css">
    <script type="application/ld+json">
{schema_local_business}
    </script>
    <script type="application/ld+json">
{schema_org}
    </script>
    {faq_schema}
    {service_schema}
</head>
<body>
    <header>
        <div class="header-inner">
            <a href="/" class="logo">
                <img src="/assets/logo.svg" alt="AE Tax Advisors" width="200" height="45">
            </a>
            <button class="mobile-toggle" aria-label="Open menu" onclick="document.querySelector('.nav-links').classList.toggle('open')">
                <span></span><span></span><span></span>
            </button>
            <nav class="nav-links">
                {nav_html}
                <a href="/discovery/" class="btn-cta">Request a Consultation</a>
            </nav>
        </div>
    </header>

    <main>
        {content}
    </main>

    <footer>
        <div class="footer-inner">
            <div class="footer-col">
                <a href="/" class="footer-logo"><img src="/assets/logo-white.svg" alt="AE Tax Advisors" width="180" height="40"></a>
                <p>Advanced Tax Strategies for high-net-worth individuals and business owners.</p>
            </div>
            <div class="footer-col">
                <h4>Quick Links</h4>
                <a href="/discovery/">Request a Consultation</a>
                <a href="/about/">About Us</a>
            </div>
            <div class="footer-col">
                <h4>Services</h4>
                <a href="/individual-tax-planning-high-earners/">Individual Tax Planning</a>
                <a href="/business-owner-small-business-tax/">Business Tax Services</a>
                <a href="/deferred-equity-compensation/">Equity Compensation</a>
                <a href="/multi-state-global-tax/">Multi-State &amp; Global Tax</a>
                <a href="/estate-trust-wealth-transfer/">Estate, Trust &amp; Wealth Transfer Planning</a>
                <a href="/retirement-exit-ma-tax-strategy/">Retirement &amp; Exit Strategy</a>
                <a href="/tax-compliance-irs-representation/">Tax Compliance &amp; IRS</a>
                <a href="/cost-segregation-studies-for-real-estate-investors/">Cost Segregation Studies</a>
            </div>
            <div class="footer-col">
                <h4>Resources</h4>
                <a href="/blog/">Blog</a>
                <a href="/case-studies/">Case Studies</a>
                <a href="/faq/">FAQ</a>
                <a href="/guides/">Guides &amp; Whitepapers</a>
                <a href="/glossary/">Glossary of Tax Terms</a>
            </div>
            <div class="footer-col">
                <h4>Legal</h4>
                <a href="/privacy-policy/">Privacy Policy</a>
                <a href="/terms-of-service/">Terms of Service</a>
                <a href="/disclaimer/">Disclaimer</a>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 AE Tax Advisors. All rights reserved.</p>
        </div>
    </footer>

    <section class="sticky-cta">
        <div class="sticky-inner">
            <p>Are You Leaving Tax Savings on the Table?</p>
            <a href="/discovery/" class="btn-cta">Get Your Free Tax Assessment</a>
        </div>
    </section>
</body>
</html>'''


def generate_homepage():
    content = '''
    <section class="hero">
        <div class="hero-inner">
            <p class="hero-subtitle">Proactive Tax Planning for High-Income Professionals</p>
            <h1>You Built the Income. We Build the Tax Strategy to Protect It</h1>
            <p class="hero-desc">AE Tax Advisors designs fully compliant tax strategies for executives, physicians, attorneys, and business owners earning $500K or more. Our advisory process focuses on proactive, year-round planning designed to help reduce your overall tax liability within the bounds of the tax code.</p>
            <a href="/discovery/" class="btn-cta btn-lg">Request Your Free Tax Assessment</a>
        </div>
    </section>

    <section class="trust-bar">
        <div class="trust-inner">
            <p class="trust-quote">"Leading the way in sophisticated tax planning for high-net-worth individuals"</p>
        </div>
    </section>

    <section class="segments">
        <div class="container">
            <div class="card-grid-3">
                <a href="/individual-tax-planning-high-earners/" class="segment-card">
                    <h3>Ultra High-Net-Worth</h3>
                    <p>Over $5 Million in Income or Assets -- Coordinated strategies across entities, trusts, and estate structures.</p>
                </a>
                <a href="/entrepreneurs-small-business-owners/" class="segment-card">
                    <h3>High-Income Earners</h3>
                    <p>$500K-$5M Annually -- W-2 optimization, equity compensation timing, and withholding coordination.</p>
                </a>
                <a href="/business-owner-small-business-tax/" class="segment-card">
                    <h3>Business Owners</h3>
                    <p>For Your Business and Employees -- Entity structuring, reasonable compensation analysis, and retirement plan design.</p>
                </a>
            </div>
        </div>
    </section>

    <section class="at-a-glance">
        <div class="container">
            <h2>AE Tax Advisors at a Glance</h2>
            <div class="card-grid-3">
                <div class="stat-card">
                    <h3>Top Tax Advisory Firm</h3>
                    <p>Nationally recognized for advanced, proactive tax strategy for high-net-worth individuals.</p>
                </div>
                <div class="stat-card">
                    <h3>Client Success Rate</h3>
                    <p>Exposed over $50M in missed tax savings for clients in 2024 alone.</p>
                </div>
                <div class="stat-card">
                    <h3>Trusted by Leaders</h3>
                    <p>Serving executives, physicians, attorneys, founders, and investors across all 50 states.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="services-overview">
        <div class="container">
            <h2>Comprehensive Tax Planning Services</h2>
            <div class="card-grid-3">
                <a href="/individual-tax-planning-high-earners/" class="service-card">
                    <h3>Individual Tax Planning</h3>
                    <p>W-2 optimization, withholding coordination, equity compensation timing, and proactive year-round planning.</p>
                </a>
                <a href="/business-owner-small-business-tax/" class="service-card">
                    <h3>Business Tax Services</h3>
                    <p>Entity structuring, reasonable compensation, S-Corp election, and multi-entity coordination.</p>
                </a>
                <a href="/deferred-equity-compensation/" class="service-card">
                    <h3>Equity Compensation</h3>
                    <p>Stock options, RSUs, ESPP, and deferred compensation planning for executives.</p>
                </a>
                <a href="/multi-state-global-tax/" class="service-card">
                    <h3>Multi-State Tax Planning</h3>
                    <p>State tax optimization, residency planning, and multi-state filing coordination.</p>
                </a>
                <a href="/estate-trust-wealth-transfer/" class="service-card">
                    <h3>Estate Planning</h3>
                    <p>Trust structuring, wealth transfer, gift tax planning, and generational strategies.</p>
                </a>
                <a href="/tax-compliance-irs-representation/" class="service-card">
                    <h3>Tax Compliance</h3>
                    <p>IRS representation, audit defense, penalty abatement, and resolution services.</p>
                </a>
            </div>
        </div>
    </section>

    <section class="why-us">
        <div class="container">
            <h2>Why High-Earners Choose AE Tax Advisors</h2>
            <div class="card-grid-3">
                <div class="why-card">
                    <h3>Proven Expertise</h3>
                    <p>Deep knowledge of the tax code applied to real-world situations -- not generic advice.</p>
                </div>
                <div class="why-card">
                    <h3>Advanced Strategies</h3>
                    <p>Entity design, depreciation timing, credit stacking, and income coordination woven into one cohesive framework.</p>
                </div>
                <div class="why-card">
                    <h3>White-Glove Service</h3>
                    <p>Year-round proactive planning with quarterly check-ins, mid-year projections, and direct advisor access.</p>
                </div>
            </div>
            <div class="center-cta">
                <a href="/bios/" class="btn-secondary">Meet Our Advisors</a>
            </div>
        </div>
    </section>

    <section class="case-studies-preview">
        <div class="container">
            <h2>AE Tax Advisors Case Studies</h2>
            <p class="section-desc">Real World Tax Optimization for High Earners and Business Owners</p>
            <p>At AE Tax Advisors, our work centers on advanced tax planning for individuals and businesses who have outgrown traditional compliance-based accounting. Each case below resulted in more than $100,000 in legally achieved tax reduction through forward-looking planning.</p>
            <div class="center-cta">
                <a href="/case-studies/" class="btn-secondary">View All Case Studies</a>
            </div>
        </div>
    </section>

    <section class="cta-section">
        <div class="container">
            <h2>Start Your Personalized Tax Plan Today</h2>
            <p>Your income deserves a strategy as sophisticated as your career. AE Tax Advisors builds forward-looking plans designed to help reduce what you owe -- this year and beyond.</p>
            <a href="/discovery/" class="btn-cta btn-lg">Request Your Free Tax Assessment</a>
        </div>
    </section>
    '''
    return get_base_html(
        "Tax Planning for High-Income Professionals",
        content,
        "/",
        description="AE Tax Advisors designs fully compliant tax strategies for executives, physicians, attorneys, and business owners earning $500K or more."
    )


def generate_generic_page(slug, page_type="page"):
    """Generate a generic page for a slug."""
    title = slug_to_title(slug)
    canonical = f"/{slug}/" if slug else "/"

    # Determine page-specific content
    if slug == "about":
        content = generate_about_content()
    elif slug == "services":
        content = generate_services_content()
    elif slug == "contact":
        content = generate_contact_content()
    elif slug == "faq":
        content = generate_faq_content()
    elif slug == "case-studies":
        content = generate_case_studies_content()
    elif slug == "discovery":
        content = generate_discovery_content()
    elif slug == "testimonials":
        content = generate_testimonials_content()
    elif slug == "blog":
        content = generate_blog_index_content()
    elif slug == "bios":
        content = generate_bios_content()
    elif slug == "privacy-policy":
        content = generate_privacy_content()
    elif slug == "terms-of-service":
        content = generate_terms_content()
    elif slug == "disclaimer":
        content = generate_disclaimer_content()
    elif slug == "glossary":
        content = generate_glossary_content()
    elif slug == "guides":
        content = generate_guides_content()
    elif slug == "press":
        content = generate_press_content()
    elif slug == "resources" or slug == "resources-2":
        content = generate_resources_content()
    elif slug == "industries-clients":
        content = generate_industries_content()
    elif slug == "thank-you":
        content = generate_thankyou_content()
    elif slug in ["individual-tax-planning-high-earners", "business-owner-small-business-tax",
                   "deferred-equity-compensation", "retirement-exit-ma-tax-strategy",
                   "multi-state-global-tax", "estate-trust-wealth-transfer",
                   "tax-compliance-irs-representation", "cost-segregation-studies-for-real-estate-investors",
                   "advanced-tax-planning-services", "tax-services", "tax-filing-and-compliance-services",
                   "tax-resolution-services-2", "cost-seg-estimator",
                   "s-corp-and-real-estate-coordination-for-active-businesses",
                   "rental-tax-filing-cleanup-and-catch-up-support",
                   "real-estate-professional-status-and-material-participation-support",
                   "real-estate-entity-structuring-for-rental-portfolios",
                   "real-estate-bookkeeping-review-for-tax-readiness",
                   "multi-state-real-estate-tax-planning",
                   "mid-term-rental-tax-planning-and-preparation",
                   "long-term-rental-tax-planning-and-preparation",
                   "long-term-rental-tax-planning-and-preparation-2",
                   "long-term-rental-tax-planning-and-preparation-3",
                   "short-term-rental-tax-planning-and-preparation-2",
                   "depreciation-and-fixed-asset-review-for-rental-properties",
                   "cost-segregation-analysis-and-implementation-support",
                   "1031-exchange-tax-coordination",
                   "schedule-a-real-estate-tax-consultation",
                   "schedule-a-real-estate-tax-consultation-2",
                   "3-year-tax-lookback-cleanup"]:
        content = generate_service_page_content(slug, title)
    elif "zoom" in slug or "consultation" in slug or slug in ["precall", "onboarding", "onboarding-call",
                   "ae-tax-advisors-onboarding-form", "ae-tax-advisors-onboarding-call-today",
                   "ae-tax-advisors-onboarding-call-today-2", "ae-tax-advisors-onboarding-call-today-3",
                   "ae-tax-advisors-onboarding-calendar"]:
        content = generate_scheduling_content(slug, title)
    elif slug in ["entrepreneurs-small-business-owners", "executives-corporate-professionals",
                   "medical-legal-professionals", "real-estate-investors"]:
        content = generate_audience_page_content(slug, title)
    elif slug in ["strategy", "guide", "7-day-recap", "7-day-followup",
                   "30-day-followup", "30-day-recap", "discover",
                   "discovery-youtube", "discovery-facebook"]:
        content = generate_funnel_page_content(slug, title)
    elif "reducing-" in slug or "eliminating-" in slug or "saving-" in slug or \
         "achieving-" in slug or "correcting-" in slug or \
         slug.startswith("high-w-2-earner") or slug.startswith("high-income-") or \
         slug.startswith("physician-") or slug.startswith("married-") or \
         slug.startswith("dual-") or slug.startswith("senior-") or \
         slug.startswith("tech-executive") or slug.startswith("significant-"):
        content = generate_case_study_detail_content(slug, title)
    elif slug == "executive-tax-planning-case-study":
        content = generate_case_study_detail_content(slug, title)
    else:
        content = generate_default_content(slug, title, page_type)

    return get_base_html(title, content, canonical)


def generate_post_page(slug):
    """Generate a blog post page."""
    title = slug_to_title(slug)
    canonical = f"/{slug}/"
    content = f'''
    <article class="blog-post">
        <div class="container narrow">
            <div class="breadcrumbs">
                <a href="/">Home</a> &raquo; <a href="/blog/">Blog</a> &raquo; {title}
            </div>
            <h1>{title}</h1>
            <div class="post-meta">
                <span>AE Tax Advisors</span> &middot; <span>Tax Planning & Strategy</span>
            </div>
            <div class="post-content">
                <p>This article covers key insights on {title.lower()} as part of AE Tax Advisors' commitment to providing actionable, compliant tax planning guidance for high-income professionals and business owners.</p>

                <p>At AE Tax Advisors, we believe that proactive tax planning is the foundation of long-term wealth preservation. Whether you are a W-2 executive, a business owner, a physician, or a real estate investor, understanding the nuances of the tax code can make a significant difference in your overall tax liability.</p>

                <h2>Key Takeaways</h2>
                <p>The strategies discussed in this article are designed to work within the bounds of current tax law. Every recommendation is grounded in IRC compliance and real-world application across our client base.</p>

                <p>Our advisory process begins with a comprehensive review of your current tax situation, including a 3-Year Tax Lookback that often uncovers missed deductions, credits, and planning opportunities worth tens of thousands of dollars.</p>

                <h2>Who This Applies To</h2>
                <p>This guidance is most relevant for individuals and households earning $500,000 or more annually, though many of the principles apply broadly to anyone interested in proactive tax planning.</p>

                <h2>Next Steps</h2>
                <p>If you are ready to explore how these strategies apply to your specific situation, schedule a confidential consultation with our team.</p>

                <div class="post-cta">
                    <a href="/discovery/" class="btn-cta">Schedule Your Free Tax Assessment</a>
                </div>
            </div>
        </div>
    </article>'''
    return get_base_html(title, content, canonical, page_type="post")


def generate_category_page(slug):
    """Generate a category archive page."""
    title = slug_to_title(slug)
    canonical = f"/{slug}/"
    content = f'''
    <section class="page-header">
        <div class="container">
            <h1>{title}</h1>
            <p>Browse our collection of articles on {title.lower()} from AE Tax Advisors.</p>
        </div>
    </section>
    <section class="blog-list">
        <div class="container">
            <p>Our team regularly publishes insights on {title.lower()} to help high-income professionals stay informed about tax planning opportunities and compliance requirements.</p>
            <div class="center-cta">
                <a href="/blog/" class="btn-secondary">View All Articles</a>
                <a href="/discovery/" class="btn-cta">Request a Consultation</a>
            </div>
        </div>
    </section>'''
    return get_base_html(title, content, canonical, page_type="category")


# ============================================================
# SPECIFIC PAGE CONTENT GENERATORS
# ============================================================

def generate_about_content():
    return '''
    <section class="page-header">
        <div class="container">
            <h1>About AE Tax Advisors</h1>
            <p>Proactive tax planning for high-income professionals and business owners.</p>
        </div>
    </section>
    <section class="content-section">
        <div class="container narrow">
            <p>AE Tax Advisors is a tax advisory firm built for high-income professionals who have outgrown traditional tax preparation. We serve executives, physicians, attorneys, business owners, and real estate investors earning $500K or more with proactive, year-round tax planning designed to help reduce their overall tax liability within the bounds of the tax code.</p>

            <h2>Our Approach</h2>
            <p>Unlike traditional CPA firms that focus on compliance and filing, AE Tax Advisors is built around strategy. We work with clients year-round to design, implement, and monitor tax plans that evolve with their income, investments, and life changes.</p>

            <h2>What Sets Us Apart</h2>
            <p>Every engagement begins with our proprietary 3-Year Tax Lookback, which reviews your last three years of returns to identify missed deductions, credits, and planning opportunities. From there, we build a forward-looking tax plan tailored to your specific situation.</p>

            <p>Our team combines deep technical knowledge of the Internal Revenue Code with practical, real-world application. We do not sell generic strategies or one-size-fits-all solutions. Every plan is custom-built for each client.</p>

            <h2>Year-Round Advisory</h2>
            <p>Our advisory engagement includes quarterly check-ins, mid-year projections, direct advisor access, and ongoing monitoring of tax law changes that may impact your plan. This is not a seasonal service.</p>

            <div class="center-cta">
                <a href="/discovery/" class="btn-cta">Request a Consultation</a>
                <a href="/bios/" class="btn-secondary">Meet Our Team</a>
            </div>
        </div>
    </section>'''


def generate_services_content():
    return '''
    <section class="page-header">
        <div class="container">
            <h1>Tax Planning Services</h1>
            <p>Comprehensive tax advisory services for high-income professionals and business owners.</p>
        </div>
    </section>
    <section class="services-grid">
        <div class="container">
            <div class="card-grid-2">
                <a href="/individual-tax-planning-high-earners/" class="service-card-lg">
                    <h3>Individual Tax Planning For High Earners</h3>
                    <p>W-2 optimization, withholding coordination, equity compensation timing, and proactive year-round tax planning for professionals earning $500K or more.</p>
                </a>
                <a href="/business-owner-small-business-tax/" class="service-card-lg">
                    <h3>Business Owner &amp; Small Business Tax Services</h3>
                    <p>Entity structuring, reasonable compensation analysis, S-Corp election timing, and multi-entity coordination for business owners.</p>
                </a>
                <a href="/deferred-equity-compensation/" class="service-card-lg">
                    <h3>Deferred Compensation &amp; Equity Compensation Advice</h3>
                    <p>Stock options, RSUs, ESPP, and deferred compensation planning to minimize tax impact from equity events.</p>
                </a>
                <a href="/retirement-exit-ma-tax-strategy/" class="service-card-lg">
                    <h3>Retirement &amp; Exit / M&amp;A Tax Strategy</h3>
                    <p>Pre-sale planning, business exit tax optimization, retirement income coordination, and succession strategy.</p>
                </a>
                <a href="/multi-state-global-tax/" class="service-card-lg">
                    <h3>Multi-state &amp; Global Tax Planning</h3>
                    <p>State tax optimization, residency planning, multi-state filing coordination, and international tax compliance.</p>
                </a>
                <a href="/estate-trust-wealth-transfer/" class="service-card-lg">
                    <h3>Estate, Trust &amp; Wealth Transfer Planning</h3>
                    <p>Trust structuring, wealth transfer strategy, gift tax planning, and generational wealth preservation.</p>
                </a>
                <a href="/tax-compliance-irs-representation/" class="service-card-lg">
                    <h3>Tax Compliance &amp; IRS Representation</h3>
                    <p>IRS audit defense, penalty abatement, installment agreements, offers in compromise, and tax resolution.</p>
                </a>
                <a href="/cost-segregation-studies-for-real-estate-investors/" class="service-card-lg">
                    <h3>Cost Segregation Studies for Real Estate Investors</h3>
                    <p>Accelerated depreciation through IRS-compliant cost segregation analysis for rental and investment properties.</p>
                </a>
            </div>
        </div>
    </section>'''


def generate_contact_content():
    return '''
    <section class="page-header">
        <div class="container">
            <h1>Contact AE Tax Advisors</h1>
            <p>Ready to explore how proactive tax planning can work for you? Get in touch with our team.</p>
        </div>
    </section>
    <section class="content-section">
        <div class="container narrow">
            <p>The best way to get started with AE Tax Advisors is to request a consultation through our discovery form. Our team will review your situation and schedule a call to discuss how we can help.</p>
            <div class="center-cta">
                <a href="/discovery/" class="btn-cta btn-lg">Request a Consultation</a>
            </div>
            <p class="center-text">You can also email our team directly at <strong>team@aetaxadvisors.com</strong></p>
        </div>
    </section>'''


def generate_faq_content():
    return '''
    <section class="page-header">
        <div class="container">
            <h1>Frequently Asked Questions</h1>
            <p>Common questions about AE Tax Advisors and our tax planning services.</p>
        </div>
    </section>
    <section class="faq-section">
        <div class="container narrow">
            <div class="faq-item">
                <h3>What does AE Tax Advisors do?</h3>
                <p>AE Tax Advisors provides proactive, year-round tax planning for high-income professionals, executives, physicians, attorneys, and business owners earning $500K or more. We design fully compliant tax strategies tailored to each client.</p>
            </div>
            <div class="faq-item">
                <h3>How much does AE Tax Advisors cost?</h3>
                <p>Our advisory engagement fee is $7,800 per year, which includes year-round proactive tax planning, quarterly check-ins, mid-year projections, and direct advisor access.</p>
            </div>
            <div class="faq-item">
                <h3>Who is AE Tax Advisors best suited for?</h3>
                <p>High-income W-2 earners, business owners, real estate investors, physicians, attorneys, executives, and anyone earning $500K or more who wants to legally reduce their tax liability.</p>
            </div>
            <div class="faq-item">
                <h3>Is AE Tax Advisors a CPA firm?</h3>
                <p>AE Tax Advisors is a tax advisory firm focused on proactive tax planning and strategy. We coordinate with your CPA or tax preparer to implement strategies.</p>
            </div>
            <div class="faq-item">
                <h3>What is the 3-Year Tax Lookback?</h3>
                <p>The 3-Year Tax Lookback is our process of reviewing your last three years of tax returns to identify missed deductions, credits, and planning opportunities that may result in amended return refunds.</p>
            </div>
            <div class="faq-item">
                <h3>Do you work with clients in all 50 states?</h3>
                <p>Yes. AE Tax Advisors serves clients nationwide. All consultations and advisory services are delivered virtually.</p>
            </div>
            <div class="center-cta">
                <a href="/discovery/" class="btn-cta">Schedule Your Free Consultation</a>
            </div>
        </div>
    </section>'''


def generate_case_studies_content():
    return '''
    <section class="page-header">
        <div class="container">
            <h1>Case Studies</h1>
            <p>Real-world tax optimization results for high-income professionals and business owners.</p>
        </div>
    </section>
    <section class="content-section">
        <div class="container">
            <p>At AE Tax Advisors, our work centers on advanced tax planning for individuals and businesses who have outgrown traditional compliance-based accounting. The following case studies reflect real engagements, real tax problems, and real outcomes achieved through proactive strategy, entity design, timing, and coordination.</p>
            <p>All case studies are anonymized. Dollar figures are rounded. Strategies shown vary by facts and circumstances and are not universal recommendations.</p>
            <div class="center-cta">
                <a href="/discovery/" class="btn-cta">See What We Can Do For You</a>
            </div>
        </div>
    </section>'''


def generate_discovery_content():
    return '''
    <section class="page-header discovery-header">
        <div class="container">
            <h1>Request a Consultation</h1>
            <p>Schedule a confidential consultation to explore how proactive tax planning can reduce your tax liability.</p>
        </div>
    </section>
    <section class="content-section">
        <div class="container narrow">
            <p>To get started, please contact our team at <strong>team@aetaxadvisors.com</strong> or call to schedule your free tax assessment. One of our advisors will review your situation and discuss how we can help.</p>
            <h2>What to Expect</h2>
            <p>During your initial consultation, we will review your current tax situation, identify potential planning opportunities, and outline the next steps for building your customized tax strategy.</p>
            <p>There is no obligation and no pressure. Our goal is to help you understand what is possible when tax planning is done proactively.</p>
        </div>
    </section>'''


def generate_testimonials_content():
    return '''
    <section class="page-header">
        <div class="container">
            <h1>Client Testimonials</h1>
            <p>What our clients say about working with AE Tax Advisors.</p>
        </div>
    </section>
    <section class="content-section">
        <div class="container narrow">
            <p>Our clients trust us with their most complex tax situations. Here is what they have to say about the experience.</p>
            <div class="center-cta">
                <a href="/discovery/" class="btn-cta">Join Our Clients</a>
            </div>
        </div>
    </section>'''


def generate_blog_index_content():
    return '''
    <section class="page-header">
        <div class="container">
            <h1>Tax Planning Insights</h1>
            <p>Expert articles on tax planning, strategy, and compliance from AE Tax Advisors.</p>
        </div>
    </section>
    <section class="blog-list">
        <div class="container">
            <p>Browse our library of tax planning articles covering topics from entity structuring and depreciation strategies to estate planning and IRS compliance. Written by our advisory team for high-income professionals and business owners.</p>
            <div class="center-cta">
                <a href="/discovery/" class="btn-cta">Request a Consultation</a>
            </div>
        </div>
    </section>'''


def generate_bios_content():
    return '''
    <section class="page-header">
        <div class="container">
            <h1>Meet Our Advisors</h1>
            <p>The AE Tax Advisors team brings deep expertise in tax planning for high-income professionals.</p>
        </div>
    </section>
    <section class="content-section">
        <div class="container">
            <p>Our team of advisors combines technical tax expertise with real-world experience serving executives, physicians, attorneys, business owners, and real estate investors. Every member of our advisory team is committed to delivering proactive, compliant tax strategies that make a measurable difference.</p>
            <div class="center-cta">
                <a href="/discovery/" class="btn-cta">Work With Our Team</a>
            </div>
        </div>
    </section>'''


def generate_privacy_content():
    return '''
    <section class="page-header"><div class="container"><h1>Privacy Policy</h1></div></section>
    <section class="content-section"><div class="container narrow">
        <p>AE Tax Advisors is committed to protecting your privacy. This policy describes how we collect, use, and protect your personal information.</p>
        <h2>Information We Collect</h2>
        <p>We collect information you provide directly, such as your name, email address, phone number, and tax-related information when you request a consultation or engage our services.</p>
        <h2>How We Use Your Information</h2>
        <p>We use your information to provide tax advisory services, communicate with you about your engagement, and improve our services.</p>
        <h2>Data Protection</h2>
        <p>We implement appropriate security measures to protect your personal and financial information.</p>
        <h2>Contact</h2>
        <p>For questions about this privacy policy, contact us at team@aetaxadvisors.com.</p>
    </div></section>'''


def generate_terms_content():
    return '''
    <section class="page-header"><div class="container"><h1>Terms of Service</h1></div></section>
    <section class="content-section"><div class="container narrow">
        <p>These terms govern your use of the AE Tax Advisors website and services.</p>
        <h2>Services</h2>
        <p>AE Tax Advisors provides tax planning advisory services. Our services do not constitute legal or accounting advice. We recommend consulting with your legal and accounting professionals.</p>
        <h2>Disclaimer</h2>
        <p>The information on this website is for general informational purposes only and does not constitute tax advice. Tax situations vary, and results depend on individual circumstances.</p>
    </div></section>'''


def generate_disclaimer_content():
    return '''
    <section class="page-header"><div class="container"><h1>Disclaimer</h1></div></section>
    <section class="content-section"><div class="container narrow">
        <p>The information provided by AE Tax Advisors on this website is for general informational purposes only. All information on the site is provided in good faith; however, we make no representation or warranty of any kind regarding the accuracy, adequacy, validity, reliability, or completeness of any information on the site.</p>
        <p>Nothing on this website constitutes professional tax, legal, or financial advice. You should consult with a qualified professional before making any decisions based on the information provided.</p>
        <p>Past results do not guarantee future outcomes. Tax savings depend on individual facts and circumstances.</p>
    </div></section>'''


def generate_glossary_content():
    return '''
    <section class="page-header"><div class="container"><h1>Glossary of Tax Terms</h1></div></section>
    <section class="content-section"><div class="container narrow">
        <p>A reference guide to common tax planning terms used throughout our articles and advisory services.</p>
        <div class="center-cta"><a href="/discovery/" class="btn-cta">Request a Consultation</a></div>
    </div></section>'''


def generate_guides_content():
    return '''
    <section class="page-header"><div class="container"><h1>Guides &amp; Whitepapers</h1></div></section>
    <section class="content-section"><div class="container narrow">
        <p>In-depth guides on tax planning strategies for high-income professionals and business owners.</p>
        <div class="center-cta"><a href="/discovery/" class="btn-cta">Request a Consultation</a></div>
    </div></section>'''


def generate_press_content():
    return '''
    <section class="page-header"><div class="container"><h1>Press &amp; Media</h1></div></section>
    <section class="content-section"><div class="container narrow">
        <p>AE Tax Advisors in the news. For media inquiries, contact team@aetaxadvisors.com.</p>
    </div></section>'''


def generate_resources_content():
    return '''
    <section class="page-header"><div class="container"><h1>Resources</h1></div></section>
    <section class="content-section"><div class="container">
        <div class="card-grid-2">
            <a href="/blog/" class="service-card-lg"><h3>Blog</h3><p>Expert articles on tax planning and strategy.</p></a>
            <a href="/case-studies/" class="service-card-lg"><h3>Case Studies</h3><p>Real-world tax optimization results.</p></a>
            <a href="/faq/" class="service-card-lg"><h3>FAQ</h3><p>Common questions about our services.</p></a>
            <a href="/guides/" class="service-card-lg"><h3>Guides &amp; Whitepapers</h3><p>In-depth tax planning guides.</p></a>
            <a href="/glossary/" class="service-card-lg"><h3>Glossary</h3><p>Tax terminology reference.</p></a>
        </div>
    </div></section>'''


def generate_industries_content():
    return '''
    <section class="page-header"><div class="container"><h1>Industries &amp; Clients We Serve</h1></div></section>
    <section class="content-section"><div class="container">
        <div class="card-grid-2">
            <a href="/executives-corporate-professionals/" class="service-card-lg"><h3>Executives &amp; Corporate Professionals</h3><p>W-2 optimization, equity compensation, and withholding coordination.</p></a>
            <a href="/entrepreneurs-small-business-owners/" class="service-card-lg"><h3>Entrepreneurs &amp; Business Owners</h3><p>Entity structuring, S-Corp election, and business tax strategy.</p></a>
            <a href="/medical-legal-professionals/" class="service-card-lg"><h3>Physicians, Attorneys &amp; Professionals</h3><p>High-income professional tax planning.</p></a>
            <a href="/real-estate-investors/" class="service-card-lg"><h3>Real Estate Investors</h3><p>Cost segregation, REPS, passive loss rules, and 1031 exchanges.</p></a>
        </div>
    </div></section>'''


def generate_thankyou_content():
    return '''
    <section class="page-header"><div class="container">
        <h1>Thank You</h1>
        <p>Your request has been received. A member of our advisory team will be in touch shortly.</p>
    </div></section>
    <section class="content-section"><div class="container narrow center-text">
        <p>In the meantime, explore our resources to learn more about how proactive tax planning can help reduce your tax liability.</p>
        <div class="center-cta">
            <a href="/blog/" class="btn-secondary">Read Our Blog</a>
            <a href="/case-studies/" class="btn-secondary">View Case Studies</a>
        </div>
    </div></section>'''


def generate_service_page_content(slug, title):
    return f'''
    <section class="page-header"><div class="container">
        <h1>{title}</h1>
        <p>Expert tax planning and advisory services from AE Tax Advisors.</p>
    </div></section>
    <section class="content-section"><div class="container narrow">
        <p>AE Tax Advisors provides comprehensive {title.lower()} services for high-income professionals and business owners. Our approach combines deep technical knowledge of the Internal Revenue Code with practical, real-world application.</p>
        <h2>How We Help</h2>
        <p>Every engagement begins with a thorough analysis of your current situation. We identify opportunities, design strategies, and work with you year-round to implement and monitor your plan.</p>
        <h2>Who This Is For</h2>
        <p>This service is designed for individuals and businesses earning $500,000 or more annually who want to take a proactive approach to tax planning.</p>
        <div class="center-cta">
            <a href="/discovery/" class="btn-cta">Schedule Your Consultation</a>
        </div>
    </div></section>'''


def generate_scheduling_content(slug, title):
    return f'''
    <section class="page-header"><div class="container">
        <h1>{title}</h1>
        <p>Schedule your consultation with AE Tax Advisors.</p>
    </div></section>
    <section class="content-section"><div class="container narrow center-text">
        <p>To schedule your consultation, please contact our team at <strong>team@aetaxadvisors.com</strong> or use the button below to request a time.</p>
        <div class="center-cta">
            <a href="/discovery/" class="btn-cta btn-lg">Request a Consultation</a>
        </div>
    </div></section>'''


def generate_audience_page_content(slug, title):
    return f'''
    <section class="page-header"><div class="container">
        <h1>{title}</h1>
        <p>Tailored tax planning for {title.lower()}.</p>
    </div></section>
    <section class="content-section"><div class="container narrow">
        <p>AE Tax Advisors works with {title.lower()} to design proactive, compliant tax strategies that reduce overall tax liability. Our advisory process is built for high-income professionals who need more than basic tax preparation.</p>
        <h2>Our Approach</h2>
        <p>We start with a comprehensive 3-Year Tax Lookback to identify missed opportunities, then build a forward-looking plan tailored to your specific income, investments, and goals.</p>
        <div class="center-cta">
            <a href="/discovery/" class="btn-cta">Get Started</a>
        </div>
    </div></section>'''


def generate_funnel_page_content(slug, title):
    return f'''
    <section class="page-header"><div class="container">
        <h1>{title}</h1>
    </div></section>
    <section class="content-section"><div class="container narrow center-text">
        <p>Thank you for your interest in AE Tax Advisors. To learn more about how we can help you reduce your tax liability, schedule a consultation with our team.</p>
        <div class="center-cta">
            <a href="/discovery/" class="btn-cta btn-lg">Request a Consultation</a>
        </div>
    </div></section>'''


def generate_case_study_detail_content(slug, title):
    return f'''
    <section class="page-header"><div class="container">
        <div class="breadcrumbs"><a href="/">Home</a> &raquo; <a href="/case-studies/">Case Studies</a> &raquo; {title}</div>
        <h1>{title}</h1>
    </div></section>
    <section class="content-section"><div class="container narrow">
        <p>This case study reflects a real engagement with AE Tax Advisors. All identifying details have been anonymized. Dollar figures are rounded. Strategies shown vary by facts and circumstances and are not universal recommendations.</p>
        <h2>The Situation</h2>
        <p>The client came to AE Tax Advisors seeking to reduce their overall tax liability through proactive planning. After conducting our comprehensive 3-Year Tax Lookback and analyzing their current financial structure, we identified significant planning opportunities.</p>
        <h2>Our Approach</h2>
        <p>Working closely with the client, we designed a multi-layered tax strategy incorporating entity design, timing optimization, and credit coordination -- all within the bounds of the tax code.</p>
        <h2>The Result</h2>
        <p>Through proactive planning and disciplined implementation, the client achieved a significant reduction in their overall tax liability. The strategies implemented continue to generate savings year over year.</p>
        <div class="center-cta">
            <a href="/discovery/" class="btn-cta">See What We Can Do For You</a>
            <a href="/case-studies/" class="btn-secondary">View More Case Studies</a>
        </div>
    </div></section>'''


def generate_default_content(slug, title, page_type):
    return f'''
    <section class="page-header"><div class="container">
        <h1>{title}</h1>
    </div></section>
    <section class="content-section"><div class="container narrow">
        <p>AE Tax Advisors provides proactive tax planning for high-income professionals. Learn more about how our advisory services can help you reduce your tax liability.</p>
        <div class="center-cta">
            <a href="/discovery/" class="btn-cta">Request a Consultation</a>
        </div>
    </div></section>'''


def write_page(path, html):
    """Write an HTML file, creating directories as needed."""
    full_path = os.path.join(OUTPUT_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(html)


def generate_sitemap():
    """Generate sitemap.xml with all URLs."""
    urls = []

    # Homepage
    urls.append({"loc": f"{SITE_URL}/", "priority": "1.0", "changefreq": "weekly"})

    # Pages
    for slug in PAGE_SLUGS:
        if slug == "":
            continue
        urls.append({"loc": f"{SITE_URL}/{slug}/", "priority": "0.8", "changefreq": "monthly"})

    # Posts
    for slug in POST_SLUGS:
        urls.append({"loc": f"{SITE_URL}/{slug}/", "priority": "0.6", "changefreq": "monthly"})

    # Categories
    for slug in CATEGORY_SLUGS:
        urls.append({"loc": f"{SITE_URL}/{slug}/", "priority": "0.5", "changefreq": "weekly"})

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        xml += f'  <url>\n'
        xml += f'    <loc>{url["loc"]}</loc>\n'
        xml += f'    <changefreq>{url["changefreq"]}</changefreq>\n'
        xml += f'    <priority>{url["priority"]}</priority>\n'
        xml += f'  </url>\n'
    xml += '</urlset>'

    write_page("sitemap.xml", xml)
    print(f"  Generated sitemap.xml with {len(urls)} URLs")


def generate_robots_txt():
    content = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    write_page("robots.txt", content)
    print("  Generated robots.txt")


def generate_vercel_json():
    config = {
        "cleanUrls": True,
        "trailingSlash": True,
        "headers": [
            {
                "source": "/(.*)",
                "headers": [
                    {"key": "X-Content-Type-Options", "value": "nosniff"},
                    {"key": "X-Frame-Options", "value": "DENY"},
                    {"key": "X-XSS-Protection", "value": "1; mode=block"}
                ]
            }
        ]
    }
    write_page("vercel.json", json.dumps(config, indent=2))
    print("  Generated vercel.json")


def main():
    print("=" * 60)
    print("AE Tax Advisors Static Site Generator")
    print("=" * 60)

    # 1. Homepage
    print("\n[1] Generating homepage...")
    write_page("index.html", generate_homepage())
    print("  Done")

    # 2. All pages
    print(f"\n[2] Generating {len(PAGE_SLUGS)} pages...")
    for slug in PAGE_SLUGS:
        if slug == "":
            continue  # homepage already generated
        html = generate_generic_page(slug)
        write_page(f"{slug}/index.html", html)
    print(f"  Done - {len(PAGE_SLUGS) - 1} pages generated")

    # 3. All posts
    print(f"\n[3] Generating {len(POST_SLUGS)} blog posts...")
    for slug in POST_SLUGS:
        if slug == "blog":
            # Blog index already handled as a page
            html = generate_generic_page(slug)
        else:
            html = generate_post_page(slug)
        write_page(f"{slug}/index.html", html)
    print(f"  Done - {len(POST_SLUGS)} posts generated")

    # 4. Categories
    print(f"\n[4] Generating {len(CATEGORY_SLUGS)} category pages...")
    for slug in CATEGORY_SLUGS:
        html = generate_category_page(slug)
        write_page(f"{slug}/index.html", html)
    print(f"  Done - {len(CATEGORY_SLUGS)} categories generated")

    # 5. Sitemap
    print("\n[5] Generating sitemap.xml...")
    generate_sitemap()

    # 6. Robots.txt
    print("\n[6] Generating robots.txt...")
    generate_robots_txt()

    # 7. Vercel config
    print("\n[7] Generating vercel.json...")
    generate_vercel_json()

    total = 1 + (len(PAGE_SLUGS) - 1) + len(POST_SLUGS) + len(CATEGORY_SLUGS)
    print(f"\n{'=' * 60}")
    print(f"COMPLETE: {total} total pages generated")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
