import os, re

# Define all 40 new case studies with their card info
new_cases = [
    # S-Corp Optimization (Business Owners)
    {"slug": "s-corp-officer-comp-correction", "category": "Business Owners", "title": "S-Corp Owner Saves $31K by Correcting $44K Officer Compensation", "desc": "How an S-Corp generating $1.3M in revenue was paying only $44K in officer compensation -- far below IRS reasonable compensation standards. AE Tax restructured comp to $95K, added accountable plan, home office, MERP, and Augusta Rule to save $31,000 per year while eliminating audit risk."},
    {"slug": "s-corp-qbi-threshold-optimization", "category": "Business Owners", "title": "Business Owner Saves $28K Optimizing QBI Before Phase-Out Thresholds", "desc": "How a business owner at $425K taxable income used retirement contributions, charitable timing, and income deferral to stay below QBI phase-out thresholds and preserve the full 20% deduction, saving $28,000 annually."},
    {"slug": "s-corp-payroll-setup-sole-prop", "category": "Business Owners", "title": "Freelance Consultant Saves $22K/Year with S-Corp Election + Solo 401(k)", "desc": "How a freelance consultant earning $340K on Schedule C elected S-Corp status, set payroll at $85K reasonable compensation, and implemented a Solo 401(k) to save $22,000 per year in self-employment and income taxes."},
    {"slug": "s-corp-multiple-businesses", "category": "Business Owners", "title": "Owner of Three S-Corps Saves $67K Through Aggregation + Cross-Entity Planning", "desc": "How a multi-business owner aggregated three S-Corps for QBI purposes, implemented cross-entity management fees, and consolidated retirement planning into a single defined benefit plan, saving $67,000 annually."},
    {"slug": "s-corp-late-election-relief", "category": "Business Owners", "title": "Business Owner Recovers $19K with Late S-Corp Election Under Rev. Proc. 2013-30", "desc": "How a business owner who missed the S-Corp election deadline filed Form 2553 with late election relief under Revenue Procedure 2013-30, retroactively saving $19,000 in self-employment taxes."},

    # Cost Seg STR (Real Estate Investors)
    {"slug": "str-lake-house-cost-seg", "category": "Real Estate Investors", "title": "Lake House STR Owner Claims $91K Tax Savings with Cost Segregation", "desc": "How a $750,000 lake house short-term rental generated $262,000 in first-year depreciation deductions through cost segregation and 100% bonus depreciation, saving the owner $91,000 in federal taxes."},
    {"slug": "str-portfolio-five-properties", "category": "Real Estate Investors", "title": "Five-Property STR Portfolio Generates $1.1M in Year 1 Deductions", "desc": "How a real estate investor with five STR properties totaling $3.2M in value used cost segregation across the entire portfolio to generate $1.1M in first-year deductions, offsetting W-2 income through REPS qualification."},
    {"slug": "str-form-3115-catchup", "category": "Real Estate Investors", "title": "STR Owner Claims $187K Catch-Up Depreciation via Form 3115", "desc": "How an STR owner who had held their property for 4 years without cost segregation filed Form 3115 to claim $187,000 in catch-up depreciation in a single tax year without amending prior returns."},
    {"slug": "str-mountain-cabin-bonus-dep", "category": "Real Estate Investors", "title": "Mountain Cabin STR Saves $68K with Cost Seg + Augusta Rule", "desc": "How a $520,000 mountain cabin STR used cost segregation to reclassify $182,000 into accelerated categories with 100% bonus depreciation, combined with the Augusta Rule for $34,000 in additional deductions."},

    # Cost Seg LTR (Real Estate Investors)
    {"slug": "ltr-duplex-cost-seg", "category": "Real Estate Investors", "title": "Duplex LTR Owner Claims $144K First-Year Deduction via Cost Segregation", "desc": "How a $480,000 duplex long-term rental generated $144,000 in first-year depreciation through cost segregation reclassifying 30% of the property into 5-year, 7-year, and 15-year accelerated categories."},
    {"slug": "ltr-apartment-building-24-units", "category": "Real Estate Investors", "title": "24-Unit Apartment Complex Generates $980K Year 1 Deduction", "desc": "How a 24-unit apartment building purchased for $2.8M used cost segregation to identify $980,000 in accelerated depreciation components, creating a massive first-year deduction for the investor."},
    {"slug": "ltr-section-1250-recapture-planning", "category": "Real Estate Investors", "title": "LTR Investor Saves $127K with 1031 Exchange + Cost Seg Recapture Planning", "desc": "How a long-term rental investor planning a sale used cost segregation analysis to model Section 1250 recapture exposure and structured a 1031 exchange to defer $127,000 in capital gains and recapture taxes."},
    {"slug": "ltr-inherited-property-step-up", "category": "Real Estate Investors", "title": "Inherited Property Generates $217K Deduction with Step-Up Basis + Cost Seg", "desc": "How an inherited long-term rental property with a stepped-up basis of $620,000 used cost segregation to maximize depreciation on the new basis, generating a $217,000 first-year deduction."},

    # Entity Restructuring (Business Owners)
    {"slug": "sole-prop-to-s-corp-contractor", "category": "Business Owners", "title": "General Contractor Saves $41K/Year Restructuring from Sole Prop to S-Corp", "desc": "How a general contractor earning $580,000 on Schedule C restructured to an S-Corp with $120,000 reasonable compensation, accountable plan, and Solo 401(k), saving $41,000 per year in taxes."},
    {"slug": "s-corp-to-c-corp-medical", "category": "Business Owners", "title": "Medical Practice Saves $72K Converting from S-Corp to C-Corp", "desc": "How a medical practice owner at $1.8M revenue converted from S-Corp to C-Corp for the 21% flat rate, implemented MERP and a defined benefit plan, and saved $72,000 per year through corporate-level tax planning."},
    {"slug": "partnership-to-s-corp", "category": "Business Owners", "title": "Two-Partner Consulting Firm Saves $36K with Partnership to S-Corp Conversion", "desc": "How a two-partner consulting firm restructured from a partnership to an S-Corp for self-employment tax savings, with each partner saving $18,000 per year through optimized reasonable compensation."},
    {"slug": "multi-entity-holding-company", "category": "Business Owners", "title": "Business Owner Saves $54K with Holding Company + IP Licensing Structure", "desc": "How a business owner with four operating LLCs created a holding company structure with centralized management, IP licensing, and tax-efficient distributions, saving $54,000 per year."},

    # High-Income W-2 (Real Estate Investors)
    {"slug": "w2-couple-str-offset", "category": "Real Estate Investors", "title": "Dual W-2 Couple ($882K) Saves $68K with STR Cost Segregation Strategy", "desc": "How a dual-income W-2 couple earning $882,000 combined purchased an STR with cost segregation to create $195,000 in paper losses offsetting W-2 income, saving $68,000 in their first year."},
    {"slug": "w2-rsu-donation-daf", "category": "Business Owners", "title": "Tech Executive Saves $47K Donating Appreciated RSUs to Donor-Advised Fund", "desc": "How a tech employee with $400K W-2 and $200K in RSU vesting donated appreciated stock to a Donor-Advised Fund, eliminating capital gains tax and claiming a full fair market value deduction, saving $47,000."},
    {"slug": "w2-backdoor-roth-mega", "category": "Business Owners", "title": "High-Income Earner Shelters $69K/Year via Backdoor + Mega Backdoor Roth", "desc": "How a W-2 earner at $550K used the backdoor Roth IRA and mega backdoor Roth through their employer plan to contribute $69,000 per year into tax-advantaged Roth retirement accounts."},
    {"slug": "w2-salt-cap-ptet-workaround", "category": "Business Owners", "title": "Business Owner Saves $23K with PTET Election Bypassing SALT Cap", "desc": "How a business-owning couple in a high-tax state used the Pass-Through Entity Tax election to bypass the $10,000 SALT cap, saving $23,000 in combined state and federal taxes."},

    # Amended Returns (Business Owners)
    {"slug": "amended-returns-missed-depreciation", "category": "Business Owners", "title": "Business Owner Recovers $42K from Prior CPA's Income Misclassification", "desc": "How a business owner's prior CPA misclassified $153,000 in consulting income as 'Other Income' instead of Schedule C. AE Tax filed 1040-X amendments for 3 years, recovering $42,000 in overpaid taxes."},
    {"slug": "amended-returns-missed-cost-seg", "category": "Real Estate Investors", "title": "Real Estate Investor Claims $340K Catch-Up Depreciation on 3 Properties", "desc": "How a real estate investor with three properties owned 5+ years that never had cost segregation studies filed Form 3115 to claim $340,000 in catch-up depreciation in a single tax year."},
    {"slug": "amended-returns-wrong-entity", "category": "Business Owners", "title": "Business Owner Recovers $48K Filing Late S-Corp Election + Amended Returns", "desc": "How a business owner operating as a sole proprietorship for 6 years filed a late S-Corp election under Rev. Proc. 2013-30 and amended returns, recovering $48,000 in overpaid self-employment taxes."},

    # Multi-Entity (Business Owners)
    {"slug": "multi-entity-real-estate-operating", "category": "Business Owners", "title": "Real Estate Investor + Business Owner Saves $83K with Management Company Structure", "desc": "How a real estate investor with an operating business and 6 rental properties created a management company structure with self-rental strategy under IRC Section 469, saving $83,000 annually."},
    {"slug": "multi-entity-family-income-splitting", "category": "Business Owners", "title": "Family Business Saves $39K with Multi-Entity Income Splitting Strategy", "desc": "How a family business owner used multiple entities to employ family members, shift income to lower tax brackets, and fund separate retirement plans for each family member, saving $39,000 per year."},

    # E-Commerce (Business Owners)
    {"slug": "ecommerce-amazon-fba-s-corp", "category": "Business Owners", "title": "Amazon FBA Seller ($2.1M) Saves $58K with S-Corp + Inventory Method Change", "desc": "How an Amazon FBA seller generating $2.1M in revenue restructured from Schedule C to S-Corp and implemented an inventory accounting method change under IRC Section 471, saving $58,000 annually."},
    {"slug": "ecommerce-dropship-multistate", "category": "Business Owners", "title": "Dropshipping Business Saves $31K by Consolidating Multi-State Entity Structure", "desc": "How a dropshipping business with nexus in 12 states consolidated its entity structure, reduced state filing obligations, and optimized for S-Corp tax savings, saving $31,000 per year."},

    # Medical/Dental (Business Owners)
    {"slug": "dental-practice-cost-seg-dso", "category": "Business Owners", "title": "Dentist Saves $156K with Cost Seg on Practice Building + Real Estate Separation", "desc": "How a dentist owning a $1.2M practice building performed cost segregation, separated real estate into a dedicated LLC, and leased it back to the practice, generating a $156,000 first-year deduction with asset protection."},
    {"slug": "physician-w2-str-reps", "category": "Real Estate Investors", "title": "High-Income Physician ($650K W-2) Saves $89K with Spouse REPS + STR Cost Seg", "desc": "How a high-income physician earning $650K W-2 qualified for Real Estate Professional Status through their spouse, using STR cost segregation to offset W-2 income and saving $89,000 annually."},

    # Construction (Business Owners)
    {"slug": "construction-completed-contract", "category": "Business Owners", "title": "Construction Company ($5M) Defers $320K with Completed Contract Method", "desc": "How a $5M construction company switched from percentage-of-completion to completed contract accounting method under IRC Section 460(e), deferring $320,000 in taxable income."},
    {"slug": "construction-equipment-section-179", "category": "Business Owners", "title": "Construction Company Claims Full $890K Equipment Deduction via Section 179", "desc": "How a construction company purchasing $890,000 in heavy equipment used Section 179 expensing and bonus depreciation to deduct the entire cost in Year 1, reducing taxable income dollar-for-dollar."},

    # Restaurant/Hospitality (Business Owners)
    {"slug": "restaurant-cost-seg-tip-credit", "category": "Business Owners", "title": "Restaurant Owner Saves $94K with Cost Seg + FICA Tip Credit Stacking", "desc": "How a restaurant owner with two locations used cost segregation on owned buildings and stacked the FICA tip credit under IRC Section 45B, saving $94,000 in combined income and payroll taxes."},
    {"slug": "hotel-boutique-renovation-cost-seg", "category": "Real Estate Investors", "title": "Boutique Hotel Renovation ($3.2M) Claims $1.28M via Cost Segregation", "desc": "How a boutique hotel undergoing a $3.2M renovation used cost segregation on the improvement costs, identifying $1.28M in accelerated components eligible for 100% bonus depreciation in Year 1."},

    # Tech Startups (Business Owners)
    {"slug": "tech-startup-rd-credit-qsbs", "category": "Business Owners", "title": "SaaS Founder Saves $45K/Year with R&D Credit + QSBS Section 1202 Planning", "desc": "How a SaaS founder used the R&D tax credit against payroll taxes plus Qualified Small Business Stock planning under Section 1202, saving $45,000 annually with a potential $10M exclusion on future exit."},
    {"slug": "tech-founder-equity-comp-83b", "category": "Business Owners", "title": "Startup Founder Saves $380K with 83(b) Election on Restricted Stock", "desc": "How a startup founder filed an 83(b) election on restricted stock at incorporation, paying minimal tax on nearly zero value, and saved $380,000 in ordinary income tax when the company was acquired 4 years later."},

    # Consultants/Freelancers (Business Owners)
    {"slug": "consultant-six-figure-s-corp", "category": "Business Owners", "title": "Management Consultant Saves $36K with S-Corp + Augusta Rule + Solo 401(k)", "desc": "How a management consultant earning $420,000 elected S-Corp status, implemented the Augusta Rule, accountable plan, and Solo 401(k), saving $36,000 per year through coordinated tax planning."},
    {"slug": "freelancer-home-office-vehicle", "category": "Business Owners", "title": "Freelance Designer Saves $18K with Home Office + Vehicle Section 179 + SEP-IRA", "desc": "How a freelance designer earning $185,000 implemented the home office deduction, Section 179 on a 6,000+ lb SUV, and a SEP-IRA to save $18,000 annually in federal and self-employment taxes."},

    # Real Estate Agents/Brokers (Business Owners)
    {"slug": "real-estate-broker-team-entity", "category": "Business Owners", "title": "Real Estate Broker ($1.4M GCI) Saves $52K with S-Corp + Group Health Plan", "desc": "How a real estate broker with $1.4M gross commission income and an 8-person team restructured commission flow through an S-Corp and implemented a group health plan, saving $52,000 per year."},
    {"slug": "real-estate-agent-investment-portfolio", "category": "Real Estate Investors", "title": "Real Estate Agent Saves $71K Using Commission Income to Fund STR Portfolio", "desc": "How a real estate agent used commission income to acquire STR investment properties, qualified as a Real Estate Professional, and used cost segregation on 3 properties to save $71,000 annually."},
]

# Read existing case studies index
with open('/sessions/admiring-festive-hopper/ae-tax-site/case-studies/index.html', 'r') as f:
    content = f.read()

# Build card HTML for new case studies
def make_card(cs):
    desc_short = cs['desc'][:160] + '...' if len(cs['desc']) > 160 else cs['desc']
    return f'''                <div class="case-study-card" style="background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:28px;transition:box-shadow 0.3s ease,transform 0.3s ease;">
                    <span style="background:var(--accent);color:var(--primary);font-size:0.7rem;font-weight:700;padding:3px 10px;border-radius:20px;text-transform:uppercase;display:inline-block;margin-bottom:10px;">{cs["category"]}</span>
                    <h3 style="font-size:1.05rem;margin-bottom:10px;line-height:1.4;">{cs["title"]}</h3>
                    <p style="font-size:0.9rem;color:#666;margin-bottom:14px;line-height:1.5;">{desc_short}</p>
                    <a href="/case-studies/{cs["slug"]}/" class="btn-secondary" style="margin-top:12px;display:inline-block;">Read the Full Case Study</a>
                </div>'''

# Split cards into Business Owners and Real Estate Investors
biz_cards = [make_card(cs) for cs in new_cases if cs['category'] == 'Business Owners']
rei_cards = [make_card(cs) for cs in new_cases if cs['category'] == 'Real Estate Investors']

biz_html = '\n'.join(biz_cards)
rei_html = '\n'.join(rei_cards)

# Find the end of the Business Owners grid and insert new business cards
# The existing structure has "Business Owners" grid then "Real Estate Investors" grid
# Find the closing </div> of the Business Owners grid (right before "<h2" for Real Estate)
biz_insert_marker = '            <h2 style="margin-top:48px;">Real Estate Investors</h2>'
content = content.replace(biz_insert_marker, biz_html + '\n            </div>\n\n            <h2 style="margin-top:48px;">Real Estate Investors</h2>')

# But we need to insert BEFORE the closing </div> of the business grid
# Actually, let's find the Real Estate section and insert REI cards before its closing </div>

# Find the CTA section that comes after all case studies
cta_marker = '''    <section class="content-section fade-in-section" style="background:var(--primary)'''
rei_insert_point = content.rfind('</div>\n', 0, content.find(cta_marker))

# Actually, let me just find the second grid's closing div before the CTA
# Simpler approach: insert REI cards right before the last </div> before the CTA section
lines = content.split('\n')
new_lines = []
in_rei_grid = False
rei_inserted = False
biz_inserted = False

for i, line in enumerate(lines):
    new_lines.append(line)
    # Insert biz cards right before the Real Estate Investors heading
    if not biz_inserted and 'Real Estate Investors</h2>' in line:
        # Insert cards before this heading but after the last card in the business grid
        # Actually we need to insert before the </div> that closes the business grid
        # Let's back up and insert before the </div> that's right before this h2
        # Remove the last </div> we added and insert cards then </div>
        for j in range(len(new_lines)-2, -1, -1):
            if '</div>' in new_lines[j] and 'case-study-grid' not in new_lines[j]:
                new_lines.insert(j, biz_html)
                biz_inserted = True
                break

# Rejoin
content = '\n'.join(new_lines)

# Now insert REI cards before the closing </div> of the REI grid
# Find the section with background:var(--primary) which is the CTA after case studies
cta_idx = content.find('section class="content-section fade-in-section" style="background:var(--primary)')
if cta_idx > 0:
    # Find the last </div>\n    </div>\n before the CTA
    search_area = content[:cta_idx]
    # Find the last </section> before CTA
    last_section = search_area.rfind('</section>')
    if last_section > 0:
        # Insert REI cards before </div> that closes the grid
        grid_close = search_area.rfind('</div>', 0, last_section)
        grid_close2 = search_area.rfind('</div>', 0, grid_close)
        content = content[:grid_close] + rei_html + '\n' + content[grid_close:]

with open('/sessions/admiring-festive-hopper/ae-tax-site/case-studies/index.html', 'w') as f:
    f.write(content)

print(f"Updated case-studies/index.html")
print(f"Business cards added: {len(biz_cards)}")
print(f"RE Investor cards added: {len(rei_cards)}")
