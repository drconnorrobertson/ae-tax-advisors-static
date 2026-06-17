import re

new_cases = [
    {"slug": "s-corp-officer-comp-correction", "cat": "Business Owners", "title": "S-Corp Owner Saves $31K by Correcting $44K Officer Compensation", "desc": "How an S-Corp generating $1.3M in revenue was paying only $44K in officer compensation -- far below IRS reasonable compensation standards. AE Tax restructured comp to $95K, added accountable plan, home office, MERP, and Augusta Rule..."},
    {"slug": "s-corp-qbi-threshold-optimization", "cat": "Business Owners", "title": "Business Owner Saves $28K Optimizing QBI Before Phase-Out Thresholds", "desc": "How a business owner at $425K taxable income used retirement contributions, charitable timing, and income deferral to stay below QBI phase-out thresholds and preserve the full 20% deduction..."},
    {"slug": "s-corp-payroll-setup-sole-prop", "cat": "Business Owners", "title": "Freelance Consultant Saves $22K/Year with S-Corp Election + Solo 401(k)", "desc": "How a freelance consultant earning $340K on Schedule C elected S-Corp status, set payroll at $85K reasonable compensation, and implemented a Solo 401(k)..."},
    {"slug": "s-corp-multiple-businesses", "cat": "Business Owners", "title": "Owner of Three S-Corps Saves $67K Through Aggregation + Cross-Entity Planning", "desc": "How a multi-business owner aggregated three S-Corps for QBI, implemented cross-entity management fees, and consolidated retirement into a defined benefit plan..."},
    {"slug": "s-corp-late-election-relief", "cat": "Business Owners", "title": "Business Owner Recovers $19K with Late S-Corp Election Under Rev. Proc. 2013-30", "desc": "How a business owner who missed the S-Corp deadline filed Form 2553 with late election relief under Revenue Procedure 2013-30, retroactively saving $19,000..."},
    {"slug": "sole-prop-to-s-corp-contractor", "cat": "Business Owners", "title": "General Contractor Saves $41K/Year Restructuring from Sole Prop to S-Corp", "desc": "How a general contractor earning $580K on Schedule C restructured to an S-Corp with $120K reasonable compensation, accountable plan, and Solo 401(k)..."},
    {"slug": "s-corp-to-c-corp-medical", "cat": "Business Owners", "title": "Medical Practice Saves $72K Converting from S-Corp to C-Corp", "desc": "How a medical practice at $1.8M revenue converted from S-Corp to C-Corp for the 21% flat rate, implemented MERP and a defined benefit plan, saving $72,000/yr..."},
    {"slug": "partnership-to-s-corp", "cat": "Business Owners", "title": "Two-Partner Consulting Firm Saves $36K with Partnership to S-Corp Conversion", "desc": "How a two-partner consulting firm restructured from partnership to S-Corp for SE tax savings, each partner saving $18,000 per year through optimized comp..."},
    {"slug": "multi-entity-holding-company", "cat": "Business Owners", "title": "Business Owner Saves $54K with Holding Company + IP Licensing Structure", "desc": "How a business owner with four LLCs created a holding company with centralized management, IP licensing, and tax-efficient distributions, saving $54,000/yr..."},
    {"slug": "w2-rsu-donation-daf", "cat": "Business Owners", "title": "Tech Executive Saves $47K Donating Appreciated RSUs to Donor-Advised Fund", "desc": "How a tech employee with $400K W-2 and $200K in RSU vesting donated appreciated stock to a DAF, eliminating capital gains and claiming full FMV deduction..."},
    {"slug": "w2-backdoor-roth-mega", "cat": "Business Owners", "title": "High-Income Earner Shelters $69K/Year via Backdoor + Mega Backdoor Roth", "desc": "How a W-2 earner at $550K used the backdoor Roth IRA and mega backdoor Roth through their employer plan to contribute $69,000/yr into Roth accounts..."},
    {"slug": "w2-salt-cap-ptet-workaround", "cat": "Business Owners", "title": "Business Owner Saves $23K with PTET Election Bypassing SALT Cap", "desc": "How a business-owning couple in a high-tax state used the Pass-Through Entity Tax election to bypass the $10,000 SALT cap, saving $23,000 combined..."},
    {"slug": "amended-returns-missed-depreciation", "cat": "Business Owners", "title": "Business Owner Recovers $42K from Prior CPA's Income Misclassification", "desc": "How a prior CPA misclassified $153K in consulting income as 'Other Income' instead of Schedule C. Filed 1040-X amendments for 3 years, recovering $42,000..."},
    {"slug": "amended-returns-wrong-entity", "cat": "Business Owners", "title": "Business Owner Recovers $48K Filing Late S-Corp Election + Amended Returns", "desc": "How a sole proprietor for 6 years filed a late S-Corp election under Rev. Proc. 2013-30 and amended returns, recovering $48,000 in overpaid SE taxes..."},
    {"slug": "multi-entity-real-estate-operating", "cat": "Business Owners", "title": "Investor + Business Owner Saves $83K with Management Company Structure", "desc": "How a real estate investor with an operating business and 6 rentals created a management company with self-rental strategy under IRC Section 469, saving $83K..."},
    {"slug": "multi-entity-family-income-splitting", "cat": "Business Owners", "title": "Family Business Saves $39K with Multi-Entity Income Splitting Strategy", "desc": "How a family business used multiple entities to employ family members, shift income to lower brackets, and fund separate retirement plans, saving $39,000/yr..."},
    {"slug": "ecommerce-amazon-fba-s-corp", "cat": "Business Owners", "title": "Amazon FBA Seller ($2.1M) Saves $58K with S-Corp + Inventory Method Change", "desc": "How an Amazon FBA seller at $2.1M restructured from Schedule C to S-Corp and implemented an inventory accounting method change under IRC Section 471..."},
    {"slug": "ecommerce-dropship-multistate", "cat": "Business Owners", "title": "Dropshipping Business Saves $31K by Consolidating Multi-State Entity Structure", "desc": "How a dropshipping business with nexus in 12 states consolidated its entity structure and reduced state filing obligations, saving $31,000 per year..."},
    {"slug": "dental-practice-cost-seg-dso", "cat": "Business Owners", "title": "Dentist Saves $156K with Cost Seg on Practice Building + RE Separation", "desc": "How a dentist owning a $1.2M practice building performed cost seg, separated real estate into a dedicated LLC, and leased it back to the practice for $156K..."},
    {"slug": "construction-completed-contract", "cat": "Business Owners", "title": "Construction Company ($5M) Defers $320K with Completed Contract Method", "desc": "How a $5M construction company switched from percentage-of-completion to completed contract method under IRC Section 460(e), deferring $320,000 in income..."},
    {"slug": "construction-equipment-section-179", "cat": "Business Owners", "title": "Construction Company Claims Full $890K Equipment Deduction via Section 179", "desc": "How a construction company purchasing $890K in heavy equipment used Section 179 and bonus depreciation to deduct the entire cost in Year 1..."},
    {"slug": "restaurant-cost-seg-tip-credit", "cat": "Business Owners", "title": "Restaurant Owner Saves $94K with Cost Seg + FICA Tip Credit Stacking", "desc": "How a restaurant owner with two locations used cost seg on owned buildings and stacked the FICA tip credit under IRC Section 45B, saving $94,000 combined..."},
    {"slug": "tech-startup-rd-credit-qsbs", "cat": "Business Owners", "title": "SaaS Founder Saves $45K/Year with R&amp;D Credit + QSBS Section 1202 Planning", "desc": "How a SaaS founder used R&amp;D tax credit against payroll taxes plus QSBS planning under Section 1202, saving $45K annually with potential $10M exclusion..."},
    {"slug": "tech-founder-equity-comp-83b", "cat": "Business Owners", "title": "Startup Founder Saves $380K with 83(b) Election on Restricted Stock", "desc": "How a startup founder filed an 83(b) election on restricted stock at incorporation, paying minimal tax, and saved $380,000 when the company was acquired..."},
    {"slug": "consultant-six-figure-s-corp", "cat": "Business Owners", "title": "Management Consultant Saves $36K with S-Corp + Augusta Rule + Solo 401(k)", "desc": "How a management consultant earning $420K elected S-Corp, implemented Augusta Rule, accountable plan, and Solo 401(k), saving $36,000 per year..."},
    {"slug": "freelancer-home-office-vehicle", "cat": "Business Owners", "title": "Freelance Designer Saves $18K with Home Office + Vehicle Section 179 + SEP-IRA", "desc": "How a freelance designer earning $185K implemented home office deduction, Section 179 on a 6,000+ lb SUV, and SEP-IRA to save $18,000 annually..."},
    {"slug": "real-estate-broker-team-entity", "cat": "Business Owners", "title": "Real Estate Broker ($1.4M GCI) Saves $52K with S-Corp + Group Health Plan", "desc": "How a broker with $1.4M gross commission income and an 8-person team restructured commission flow through S-Corp and group health plan, saving $52,000/yr..."},
]

new_rei = [
    {"slug": "str-lake-house-cost-seg", "cat": "Real Estate Investors", "title": "Lake House STR Owner Claims $91K Tax Savings with Cost Segregation", "desc": "How a $750K lake house STR generated $262K in first-year depreciation through cost segregation and 100% bonus depreciation, saving $91,000 in federal taxes..."},
    {"slug": "str-portfolio-five-properties", "cat": "Real Estate Investors", "title": "Five-Property STR Portfolio Generates $1.1M in Year 1 Deductions", "desc": "How an investor with five STRs totaling $3.2M used cost segregation across the portfolio to generate $1.1M in Year 1 deductions, offsetting W-2 income via REPS..."},
    {"slug": "str-form-3115-catchup", "cat": "Real Estate Investors", "title": "STR Owner Claims $187K Catch-Up Depreciation via Form 3115", "desc": "How an STR owner who held property 4 years without cost seg filed Form 3115 to claim $187,000 in catch-up depreciation in a single tax year..."},
    {"slug": "str-mountain-cabin-bonus-dep", "cat": "Real Estate Investors", "title": "Mountain Cabin STR Saves $68K with Cost Seg + Augusta Rule", "desc": "How a $520K mountain cabin STR used cost seg to reclassify $182K into accelerated categories with bonus depreciation, plus Augusta Rule for $34K additional..."},
    {"slug": "ltr-duplex-cost-seg", "cat": "Real Estate Investors", "title": "Duplex LTR Owner Claims $144K First-Year Deduction via Cost Segregation", "desc": "How a $480K duplex LTR generated $144K in first-year depreciation by reclassifying 30% into 5-year, 7-year, and 15-year accelerated categories..."},
    {"slug": "ltr-apartment-building-24-units", "cat": "Real Estate Investors", "title": "24-Unit Apartment Complex Generates $980K Year 1 Deduction", "desc": "How a 24-unit apartment building purchased for $2.8M used cost seg to identify $980K in accelerated components for a massive first-year deduction..."},
    {"slug": "ltr-section-1250-recapture-planning", "cat": "Real Estate Investors", "title": "LTR Investor Saves $127K with 1031 Exchange + Cost Seg Recapture Planning", "desc": "How an LTR investor planning a sale used cost seg analysis to model Section 1250 recapture and structured a 1031 exchange to defer $127K in taxes..."},
    {"slug": "ltr-inherited-property-step-up", "cat": "Real Estate Investors", "title": "Inherited Property Generates $217K Deduction with Step-Up Basis + Cost Seg", "desc": "How an inherited LTR with stepped-up basis of $620K used cost segregation to maximize depreciation on the new basis, generating $217K Year 1 deduction..."},
    {"slug": "w2-couple-str-offset", "cat": "Real Estate Investors", "title": "Dual W-2 Couple ($882K) Saves $68K with STR Cost Segregation Strategy", "desc": "How a dual-income W-2 couple earning $882K purchased an STR with cost seg to create $195K in paper losses offsetting W-2 income, saving $68,000 Year 1..."},
    {"slug": "amended-returns-missed-cost-seg", "cat": "Real Estate Investors", "title": "Investor Claims $340K Catch-Up Depreciation on 3 Properties via Form 3115", "desc": "How an investor with three properties owned 5+ years that never had cost seg filed Form 3115 to claim $340,000 in catch-up depreciation in a single year..."},
    {"slug": "physician-w2-str-reps", "cat": "Real Estate Investors", "title": "High-Income Physician ($650K) Saves $89K with Spouse REPS + STR Cost Seg", "desc": "How a physician earning $650K W-2 qualified for REPS through spouse, using STR cost seg to offset W-2 income and saving $89,000 annually..."},
    {"slug": "hotel-boutique-renovation-cost-seg", "cat": "Real Estate Investors", "title": "Boutique Hotel Renovation ($3.2M) Claims $1.28M via Cost Segregation", "desc": "How a boutique hotel undergoing a $3.2M renovation used cost seg on improvements, identifying $1.28M in accelerated components for 100% bonus depreciation..."},
    {"slug": "real-estate-agent-investment-portfolio", "cat": "Real Estate Investors", "title": "Real Estate Agent Saves $71K Using Commission Income to Fund STR Portfolio", "desc": "How a real estate agent used commission income to acquire STR properties, qualified as REPS, and used cost seg on 3 properties to save $71,000 annually..."},
]

def card_html(cs):
    return f'''                <div class="case-study-card" style="background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:28px;transition:box-shadow 0.3s ease,transform 0.3s ease;">
                    <span style="background:var(--accent);color:var(--primary);font-size:0.7rem;font-weight:700;padding:3px 10px;border-radius:20px;text-transform:uppercase;display:inline-block;margin-bottom:10px;">{cs["cat"]}</span>
                    <h3 style="font-size:1.05rem;margin-bottom:10px;line-height:1.4;">{cs["title"]}</h3>
                    <p style="font-size:0.9rem;color:#666;margin-bottom:14px;line-height:1.5;">{cs["desc"]}</p>
                    <a href="/case-studies/{cs["slug"]}/" class="btn-secondary" style="margin-top:12px;display:inline-block;">Read the Full Case Study</a>
                </div>'''

with open('/sessions/admiring-festive-hopper/ae-tax-site/case-studies/index.html', 'r') as f:
    html = f.read()

# Strategy: find the marker for "Real Estate Investors" h2, insert biz cards before it (but after the last existing biz card)
# Then find the marker for "Multi-Entity" h2, insert REI cards before it
biz_cards_str = '\n'.join(card_html(c) for c in new_cases)
rei_cards_str = '\n'.join(card_html(c) for c in new_rei)

# Insert business owner cards before the Real Estate Investors heading
rei_heading = '<h2 style="margin-top:48px;">Real Estate Investors</h2>'
html = html.replace(rei_heading, biz_cards_str + '\n            </div>\n\n            ' + rei_heading, 1)

# Insert RE investor cards before the Multi-Entity heading
multi_heading = '<h2 style="margin-top:48px;">Multi-Entity &amp; Complex</h2>'
html = html.replace(multi_heading, rei_cards_str + '\n            </div>\n\n            ' + multi_heading, 1)

with open('/sessions/admiring-festive-hopper/ae-tax-site/case-studies/index.html', 'w') as f:
    f.write(html)

print("Done!")
