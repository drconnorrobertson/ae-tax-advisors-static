# Simple line-based insertion - no string replacement issues
with open('/sessions/admiring-festive-hopper/ae-tax-site/case-studies/index.html', 'r') as f:
    lines = f.readlines()

def card(slug, cat, title, desc):
    return f'''                <div class="case-study-card" style="background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:28px;transition:box-shadow 0.3s ease,transform 0.3s ease;">
                    <span style="background:var(--accent);color:var(--primary);font-size:0.7rem;font-weight:700;padding:3px 10px;border-radius:20px;text-transform:uppercase;display:inline-block;margin-bottom:10px;">{cat}</span>
                    <h3 style="font-size:1.05rem;margin-bottom:10px;line-height:1.4;">{title}</h3>
                    <p style="font-size:0.9rem;color:#666;margin-bottom:14px;line-height:1.5;">{desc}</p>
                    <a href="/case-studies/{slug}/" class="btn-secondary" style="margin-top:12px;display:inline-block;">Read the Full Case Study</a>
                </div>
'''

biz = [
    card("s-corp-officer-comp-correction","Business Owners","S-Corp Owner Saves $31K by Correcting $44K Officer Compensation","How an S-Corp generating $1.3M in revenue was paying only $44K in officer compensation, far below IRS standards. Restructured to $95K, added accountable plan, home office, MERP, and Augusta Rule..."),
    card("s-corp-qbi-threshold-optimization","Business Owners","Business Owner Saves $28K Optimizing QBI Before Phase-Out Thresholds","How a business owner at $425K taxable income used retirement contributions, charitable timing, and income deferral to preserve the full 20% QBI deduction..."),
    card("s-corp-payroll-setup-sole-prop","Business Owners","Freelance Consultant Saves $22K/Year with S-Corp Election + Solo 401(k)","How a freelance consultant earning $340K on Schedule C elected S-Corp status, set payroll at $85K reasonable compensation, and implemented a Solo 401(k)..."),
    card("s-corp-multiple-businesses","Business Owners","Owner of Three S-Corps Saves $67K Through Aggregation + Cross-Entity Planning","How a multi-business owner aggregated three S-Corps for QBI, implemented cross-entity management fees, and consolidated retirement into a defined benefit plan..."),
    card("s-corp-late-election-relief","Business Owners","Business Owner Recovers $19K with Late S-Corp Election Under Rev. Proc. 2013-30","How a business owner who missed the S-Corp deadline filed Form 2553 with late election relief, retroactively saving $19,000 in self-employment taxes..."),
    card("sole-prop-to-s-corp-contractor","Business Owners","General Contractor Saves $41K/Year Restructuring from Sole Prop to S-Corp","How a general contractor earning $580K on Schedule C restructured to an S-Corp with $120K reasonable compensation, accountable plan, and Solo 401(k)..."),
    card("s-corp-to-c-corp-medical","Business Owners","Medical Practice Saves $72K Converting from S-Corp to C-Corp","How a medical practice at $1.8M revenue converted from S-Corp to C-Corp for the 21% flat rate, implemented MERP and a defined benefit plan, saving $72,000/yr..."),
    card("partnership-to-s-corp","Business Owners","Two-Partner Consulting Firm Saves $36K with Partnership to S-Corp Conversion","How a two-partner consulting firm restructured from partnership to S-Corp for SE tax savings, each partner saving $18,000 per year..."),
    card("multi-entity-holding-company","Business Owners","Business Owner Saves $54K with Holding Company + IP Licensing Structure","How a business owner with four LLCs created a holding company with centralized management, IP licensing, and tax-efficient distributions..."),
    card("w2-rsu-donation-daf","Business Owners","Tech Executive Saves $47K Donating Appreciated RSUs to Donor-Advised Fund","How a tech employee with $400K W-2 and $200K in RSU vesting donated appreciated stock to a DAF, eliminating capital gains and claiming full FMV deduction..."),
    card("w2-backdoor-roth-mega","Business Owners","High-Income Earner Shelters $69K/Year via Backdoor + Mega Backdoor Roth","How a W-2 earner at $550K used the backdoor Roth IRA and mega backdoor Roth through their employer plan to contribute $69,000/yr in Roth accounts..."),
    card("w2-salt-cap-ptet-workaround","Business Owners","Business Owner Saves $23K with PTET Election Bypassing SALT Cap","How a business-owning couple in a high-tax state used the Pass-Through Entity Tax election to bypass the $10,000 SALT cap, saving $23,000 combined..."),
    card("amended-returns-missed-depreciation","Business Owners","Business Owner Recovers $42K from Prior CPA's Income Misclassification","How a prior CPA misclassified $153K in consulting income as Other Income instead of Schedule C. Filed 1040-X amendments for 3 years, recovering $42,000..."),
    card("amended-returns-wrong-entity","Business Owners","Business Owner Recovers $48K Filing Late S-Corp Election + Amended Returns","How a sole proprietor for 6 years filed a late S-Corp election under Rev. Proc. 2013-30 and amended returns, recovering $48,000 in overpaid SE taxes..."),
    card("multi-entity-real-estate-operating","Business Owners","Investor + Business Owner Saves $83K with Management Company Structure","How a real estate investor with an operating business and 6 rentals created a management company with self-rental strategy under IRC Section 469..."),
    card("multi-entity-family-income-splitting","Business Owners","Family Business Saves $39K with Multi-Entity Income Splitting Strategy","How a family business used multiple entities to employ family members, shift income to lower brackets, and fund separate retirement plans..."),
    card("ecommerce-amazon-fba-s-corp","Business Owners","Amazon FBA Seller ($2.1M) Saves $58K with S-Corp + Inventory Method Change","How an Amazon FBA seller at $2.1M restructured from Schedule C to S-Corp and implemented an inventory accounting method change under IRC Section 471..."),
    card("ecommerce-dropship-multistate","Business Owners","Dropshipping Business Saves $31K by Consolidating Multi-State Entity Structure","How a dropshipping business with nexus in 12 states consolidated its entity structure and reduced state filing obligations, saving $31,000 per year..."),
    card("dental-practice-cost-seg-dso","Business Owners","Dentist Saves $156K with Cost Seg on Practice Building + RE Separation","How a dentist owning a $1.2M practice building performed cost seg, separated real estate into a dedicated LLC, and leased it back for $156K Year 1 deduction..."),
    card("construction-completed-contract","Business Owners","Construction Company ($5M) Defers $320K with Completed Contract Method","How a $5M construction company switched from percentage-of-completion to completed contract method under IRC Section 460(e), deferring $320,000..."),
    card("construction-equipment-section-179","Business Owners","Construction Company Claims Full $890K Equipment Deduction via Section 179","How a construction company purchasing $890K in heavy equipment used Section 179 and bonus depreciation to deduct the entire cost in Year 1..."),
    card("restaurant-cost-seg-tip-credit","Business Owners","Restaurant Owner Saves $94K with Cost Seg + FICA Tip Credit Stacking","How a restaurant owner with two locations used cost seg on owned buildings and stacked the FICA tip credit under IRC Section 45B, saving $94,000..."),
    card("tech-startup-rd-credit-qsbs","Business Owners","SaaS Founder Saves $45K/Year with R&amp;D Credit + QSBS Section 1202 Planning","How a SaaS founder used R&amp;D tax credit against payroll taxes plus QSBS planning under Section 1202, saving $45K annually with potential $10M exclusion..."),
    card("tech-founder-equity-comp-83b","Business Owners","Startup Founder Saves $380K with 83(b) Election on Restricted Stock","How a startup founder filed an 83(b) election on restricted stock at incorporation, paying minimal tax, saving $380,000 when the company was acquired..."),
    card("consultant-six-figure-s-corp","Business Owners","Management Consultant Saves $36K with S-Corp + Augusta Rule + Solo 401(k)","How a management consultant earning $420K elected S-Corp, implemented Augusta Rule, accountable plan, and Solo 401(k), saving $36,000 per year..."),
    card("freelancer-home-office-vehicle","Business Owners","Freelance Designer Saves $18K with Home Office + Vehicle Section 179 + SEP-IRA","How a freelance designer earning $185K implemented home office deduction, Section 179 on a 6,000+ lb SUV, and SEP-IRA to save $18,000 annually..."),
    card("real-estate-broker-team-entity","Business Owners","Real Estate Broker ($1.4M GCI) Saves $52K with S-Corp + Group Health Plan","How a broker with $1.4M gross commission income and 8-person team restructured commission flow through S-Corp and group health plan, saving $52,000/yr..."),
]

rei = [
    card("str-lake-house-cost-seg","Real Estate Investors","Lake House STR Owner Claims $91K Tax Savings with Cost Segregation","How a $750K lake house STR generated $262K in first-year depreciation through cost segregation and 100% bonus depreciation, saving $91,000..."),
    card("str-portfolio-five-properties","Real Estate Investors","Five-Property STR Portfolio Generates $1.1M in Year 1 Deductions","How an investor with five STRs totaling $3.2M used cost seg across the portfolio to generate $1.1M in Year 1 deductions, offsetting W-2 income via REPS..."),
    card("str-form-3115-catchup","Real Estate Investors","STR Owner Claims $187K Catch-Up Depreciation via Form 3115","How an STR owner who held property 4 years without cost seg filed Form 3115 to claim $187,000 in catch-up depreciation in a single tax year..."),
    card("str-mountain-cabin-bonus-dep","Real Estate Investors","Mountain Cabin STR Saves $68K with Cost Seg + Augusta Rule","How a $520K mountain cabin STR used cost seg to reclassify $182K into accelerated categories with bonus depreciation, plus Augusta Rule for $34K additional..."),
    card("ltr-duplex-cost-seg","Real Estate Investors","Duplex LTR Owner Claims $144K First-Year Deduction via Cost Segregation","How a $480K duplex LTR generated $144K in first-year depreciation by reclassifying 30% into 5-year, 7-year, and 15-year accelerated categories..."),
    card("ltr-apartment-building-24-units","Real Estate Investors","24-Unit Apartment Complex Generates $980K Year 1 Deduction","How a 24-unit apartment building purchased for $2.8M used cost seg to identify $980K in accelerated components for a massive first-year deduction..."),
    card("ltr-section-1250-recapture-planning","Real Estate Investors","LTR Investor Saves $127K with 1031 Exchange + Cost Seg Recapture Planning","How an LTR investor planning a sale used cost seg analysis to model Section 1250 recapture and structured a 1031 exchange to defer $127K in taxes..."),
    card("ltr-inherited-property-step-up","Real Estate Investors","Inherited Property Generates $217K Deduction with Step-Up Basis + Cost Seg","How an inherited LTR with stepped-up basis of $620K used cost seg to maximize depreciation on the new basis, generating $217K Year 1 deduction..."),
    card("w2-couple-str-offset","Real Estate Investors","Dual W-2 Couple ($882K) Saves $68K with STR Cost Segregation Strategy","How a dual-income W-2 couple earning $882K purchased an STR with cost seg to create $195K in paper losses offsetting W-2 income, saving $68,000..."),
    card("amended-returns-missed-cost-seg","Real Estate Investors","Investor Claims $340K Catch-Up Depreciation on 3 Properties via Form 3115","How an investor with three properties owned 5+ years that never had cost seg filed Form 3115 to claim $340,000 in catch-up depreciation..."),
    card("physician-w2-str-reps","Real Estate Investors","High-Income Physician ($650K) Saves $89K with Spouse REPS + STR Cost Seg","How a physician earning $650K W-2 qualified for REPS through spouse, using STR cost seg to offset W-2 income and saving $89,000 annually..."),
    card("hotel-boutique-renovation-cost-seg","Real Estate Investors","Boutique Hotel Renovation ($3.2M) Claims $1.28M via Cost Segregation","How a boutique hotel undergoing a $3.2M renovation used cost seg on improvements, identifying $1.28M in accelerated components for bonus depreciation..."),
    card("real-estate-agent-investment-portfolio","Real Estate Investors","Real Estate Agent Saves $71K Using Commission Income to Fund STR Portfolio","How a real estate agent used commission income to acquire STR properties, qualified as REPS, and used cost seg on 3 properties to save $71,000 annually..."),
]

# Find the exact line numbers for insertion points
# Line 233 (0-indexed 232) is "            </div>" closing the Business Owners grid
# Line 303 (0-indexed 302) is "            </div>" closing the Real Estate Investors grid
# Line 374 (0-indexed 373) is "            </div>" closing the Multi-Entity grid

# Find insertion lines by looking for the closing </div> just before each h2
biz_insert = None
rei_insert = None

for i, line in enumerate(lines):
    if 'Real Estate Investors</h2>' in line:
        # Insert biz cards before the </div> on the line before this h2
        for j in range(i-1, -1, -1):
            if lines[j].strip() == '</div>':
                biz_insert = j
                break
        break

for i, line in enumerate(lines):
    if 'Multi-Entity' in line and '</h2>' in line:
        for j in range(i-1, -1, -1):
            if lines[j].strip() == '</div>':
                rei_insert = j
                break
        break

print(f"Business insert at line {biz_insert}, RE insert at line {rei_insert}")

# Insert in reverse order (so line numbers don't shift)
biz_text = ''.join(biz)
rei_text = ''.join(rei)

# Insert REI cards first (later in file)
lines.insert(rei_insert, rei_text)
# Now biz_insert is still valid since it's before rei_insert
lines.insert(biz_insert, biz_text)

with open('/sessions/admiring-festive-hopper/ae-tax-site/case-studies/index.html', 'w') as f:
    f.writelines(lines)

print("Done!")
