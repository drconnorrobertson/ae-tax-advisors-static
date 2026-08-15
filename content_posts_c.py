#!/usr/bin/env python3
"""Long-tail keyword posts, batch C: entity structure, compensation, retirement."""

POSTS = [

# ---------------------------------------------------------------- 11
{
"slug": "s-corp-vs-llc-tax-comparison-2026",
"h1": "S-Corp vs LLC Tax Comparison 2026: What Actually Changes on Your Return",
"title": "S-Corp vs LLC Tax Comparison 2026",
"description": "An LLC and an S-Corp are not alternatives, they are different layers. Here is what the S election actually changes in 2026, where the savings come from, and the income level where it starts to pay.",
"subtitle": "The comparison most people make is the wrong one. An LLC is a legal entity, an S-Corp is a tax election, and the real question is whether to make the election.",
"keywords": ["S-Corp vs LLC 2026", "S corporation tax comparison", "self employment tax savings"],
"definition": "An LLC is a state-law legal entity and an S-Corp is a federal tax election under IRC Subchapter S, so a single LLC can be taxed as a disregarded entity, a partnership, or an S-Corp. The practical comparison in 2026 is between default pass-through taxation, where all net profit is subject to self-employment tax, and S-Corp taxation, where the owner takes reasonable W-2 wages subject to payroll tax and the remaining profit is distributed free of self-employment tax. The election typically begins to pay for itself once net profit reaches roughly $60,000 to $80,000 per owner.",
"sections": [
 ("The Comparison Is Not LLC vs S-Corp", [
  "An LLC is formed under state law and governs liability, ownership, and governance. It has no default federal tax treatment of its own. A single-member LLC is disregarded and reported on Schedule C, a multi-member LLC defaults to partnership taxation on Form 1065, and either can elect S-Corp treatment on Form 2553.",
  "So the real decision is whether to make the S election, and it can be made by an LLC or a corporation. Making the election does not change your liability protection, your operating agreement, or your state filing status. It changes how profit is characterized and taxed.",
  "This matters because many owners form a corporation when they wanted an LLC, on the belief that S-Corp status required it. An LLC taxed as an S-Corp gives you the payroll tax result with the simpler state law entity.",
 ]),
 ("Where the Savings Actually Come From", [
  "Under default treatment, all net earnings from self-employment are subject to SE tax at 15.3%, comprising 12.4% Social Security up to the annual wage base and 2.9% Medicare with no cap, plus the 0.9% additional Medicare tax above $200,000 single or $250,000 married filing jointly. Half of the SE tax is deductible above the line.",
  "Under S-Corp treatment, only the owner's W-2 wages are subject to payroll tax. Distributions of remaining profit are not subject to SE tax or payroll tax.",
  "The saving is therefore 15.3% of the amount characterized as distribution rather than wages, up to the wage base, and 2.9% to 3.8% above it. It is not a saving on income tax. The profit is taxed at ordinary rates either way.",
  "That last point is worth emphasizing because it is widely misunderstood. An S election does not reduce income tax. It reduces employment tax only.",
 ]),
 ("A Numerical Comparison at Several Income Levels", [
  "<div class=\"ae-table-scroll\" style=\"overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%\"><table><thead><tr><th>Net profit</th><th>SE tax as LLC</th><th>Reasonable wage</th><th>Payroll tax as S-Corp</th><th>Gross saving</th><th>Net of ~$3,000 costs</th></tr></thead><tbody>"
  "<tr><td>$60,000</td><td>~$8,478</td><td>$40,000</td><td>~$6,120</td><td>~$2,358</td><td>~ -$642</td></tr>"
  "<tr><td>$100,000</td><td>~$14,130</td><td>$60,000</td><td>~$9,180</td><td>~$4,950</td><td>~$1,950</td></tr>"
  "<tr><td>$180,000</td><td>~$25,433</td><td>$95,000</td><td>~$14,535</td><td>~$10,898</td><td>~$7,898</td></tr>"
  "<tr><td>$350,000</td><td>~$32,911</td><td>$150,000</td><td>~$22,950</td><td>~$9,961</td><td>~$6,961</td></tr>"
  "<tr><td>$700,000</td><td>~$45,193</td><td>$220,000</td><td>~$29,258</td><td>~$15,935</td><td>~$12,935</td></tr>"
  "</tbody></table></div>",
  "These are approximations using the 2026 Social Security wage base and standard rates, and they ignore state payroll taxes and unemployment insurance, which reduce the benefit somewhat. Confirm current-year figures before relying on them.",
  "Two patterns are visible. Below roughly $60,000 of profit, the compliance cost exceeds the saving. And the saving does not scale linearly, because above the Social Security wage base only the Medicare portion is at stake, so the marginal benefit per dollar shifted drops from 15.3% to 2.9% or 3.8%.",
 ]),
 ("The Costs You Are Trading Against", [
  "An S-Corp requires a separate return on Form 1120-S with K-1s to shareholders, actual payroll with quarterly Forms 941, annual Form 940, W-2 and W-3 filings, and state payroll registration and returns.",
  "Realistic annual cost is $1,500 to $2,500 for the tax return and $600 to $1,500 for payroll processing, plus state unemployment insurance and any state-level entity or franchise taxes. Several states impose an S-Corp franchise tax or minimum fee that can materially change the math.",
  "There are also structural costs. Reasonable compensation must be documented and defended. Basis must be tracked, and distributions in excess of basis are taxable gain. Health insurance for a more-than-2% shareholder must run through W-2 wages to be deductible. And the S-Corp cannot allocate income disproportionately to ownership, which a partnership can.",
 ]),
 ("Ownership and Eligibility Restrictions", [
  "S-Corps have eligibility rules that partnerships do not. No more than 100 shareholders, only one class of stock, and shareholders limited to individuals, certain trusts and estates, and certain exempt organizations. Nonresident aliens cannot be shareholders, and corporations and partnerships cannot hold S-Corp stock.",
  "The single class of stock requirement is the one that most often forces a different answer. If you need preferred returns, waterfall distributions, or special allocations, an S-Corp cannot do it and an LLC taxed as a partnership can. This is why real estate ventures with outside investors are almost never S-Corps.",
  "Real estate is generally a poor fit for S-Corp treatment for a second reason: distributing appreciated property out of an S-Corp triggers gain recognition as though it were sold at fair market value, while a partnership can generally distribute property without gain. Locking appreciating real estate inside an S-Corp creates an exit problem that is difficult to undo.",
 ]),
 ("Interaction With the Section 199A Deduction", [
  "The qualified business income deduction under Section 199A, made permanent by the OBBBA, allows up to a 20% deduction against qualified business income, and it interacts with the wage decision in a way that cuts against minimizing wages.",
  "Below the taxable income thresholds, the deduction is simply 20% of QBI and W-2 wages are irrelevant. Above the thresholds, the deduction is limited to the greater of 50% of W-2 wages, or 25% of W-2 wages plus 2.5% of the unadjusted basis of qualified property.",
  "For a specified service trade or business, including health, law, accounting, consulting, athletics, financial services, and any business whose principal asset is the reputation or skill of its employees or owners, the deduction phases out entirely above the thresholds regardless of wages.",
  "For non-service businesses above the thresholds, wages are the constraint on the deduction. Reducing your W-2 wage to save payroll tax can reduce the 199A deduction by more than the payroll tax saved. This is the single most common modeling error we correct on new engagements, and it flips the answer at higher income levels.",
 ]),
 ("When to Elect, and When Not To", [
  "Elect when net profit reliably exceeds roughly $80,000 per owner, the business is not a real estate holding entity, ownership is simple and eligible, and you are prepared to run genuine payroll.",
  "Do not elect when profit is volatile or below the breakeven, when you hold appreciating real estate, when you need special allocations or multiple equity classes, when you have ineligible owners, or when the QBI wage limitation would cost more than the payroll tax saved.",
  "Timing matters. Form 2553 is generally due within two months and fifteen days after the beginning of the tax year the election is to take effect. Revenue Procedure 2013-30 provides relief for late elections within three years and seventy-five days where there was reasonable cause, which is granted routinely when the facts support it.",
 ]),
],
"faqs": [
 ("Is an S-Corp better than an LLC?",
  "<p>The question conflates two different things. An LLC is a state law entity and an S-Corp is a federal tax election, and an LLC can elect S-Corp taxation. The real question is whether to make the election, which generally pays off once net profit exceeds roughly $60,000 to $80,000 per owner.</p>"),
 ("How much does an S-Corp election actually save?",
  "<p>It saves 15.3% self-employment tax on the profit characterized as distribution rather than wages, up to the Social Security wage base, and 2.9% to 3.8% above it. On $180,000 of profit with a $95,000 reasonable wage, the gross saving is roughly $10,900 before compliance costs of $2,000 to $4,000.</p>"),
 ("Does an S-Corp reduce income tax?",
  "<p>No. Profit is taxed at the same ordinary rates whether it flows through an LLC or an S-Corp. The election reduces employment tax only. Any advisor describing S-Corp savings as income tax savings is describing it incorrectly.</p>"),
 ("Should I put rental real estate in an S-Corp?",
  "<p>Generally no. Rental income is not subject to self-employment tax to begin with, so there is nothing to save, and distributing appreciated property out of an S-Corp triggers gain as though it had been sold. An LLC taxed as a partnership avoids both problems.</p>"),
 ("Can minimizing my S-Corp wage backfire?",
  "<p>Yes, in two ways. It invites a reasonable compensation adjustment on examination, with back payroll tax, penalties, and interest. And above the Section 199A taxable income thresholds, the QBI deduction for a non-service business is limited by W-2 wages, so a lower wage can cost more in lost deduction than it saves in payroll tax.</p>"),
],
"related": [
 ("/reasonable-compensation-s-corp-irs/", "Reasonable Compensation for S-Corp Owners"),
 ("/c-corp-income-shifting-strategy/", "C-Corp Income Shifting Strategy"),
 ("/cash-balance-plan-tax-deduction/", "Cash Balance Plan Tax Deduction"),
 ("/business-owner-small-business-tax/", "Business Owner and Small Business Tax Services"),
 ("/advanced-tax-strategies/", "Advanced Tax Strategies for Business Owners"),
],
"takeaways": [
 "An LLC can elect S-Corp taxation; the two are layers, not alternatives.",
 "The election saves employment tax only, never income tax.",
 "Breakeven is roughly $60,000 to $80,000 of net profit per owner after compliance costs.",
 "Above the Section 199A thresholds, a lower wage can cost more in lost QBI deduction than it saves in payroll tax.",
 "Appreciating real estate does not belong in an S-Corp because distributions trigger gain.",
]},

# ---------------------------------------------------------------- 12
{
"slug": "reasonable-compensation-s-corp-irs",
"h1": "Reasonable Compensation for S-Corp Owners: What the IRS Actually Requires",
"title": "Reasonable Compensation for S-Corp Owners",
"description": "The IRS has no safe harbor percentage for S-Corp reasonable compensation. Here are the nine factors courts apply, the case law that defines the standard, and how to build a defensible position.",
"subtitle": "There is no 60/40 rule, no 50% rule, and no published percentage. There is a facts-and-circumstances standard, nine factors, and a body of case law.",
"keywords": ["reasonable compensation S-Corp", "S corp officer compensation", "IRS reasonable salary"],
"definition": "Reasonable compensation is the amount an S-Corp must pay a shareholder-employee as W-2 wages for services rendered before making distributions, required because IRC Section 3121(d)(1) treats corporate officers who perform more than minor services as employees. The IRS has never published a safe harbor percentage. The standard is what a comparable business would pay a comparable person for comparable services, determined under a facts-and-circumstances analysis using nine factors developed in case law and summarized in IRS Fact Sheet FS-2008-25.",
"sections": [
 ("Why This Is the Most Examined Item on an 1120-S", [
  "The S-Corp structure creates an obvious incentive: every dollar moved from wages to distributions saves 15.3% up to the wage base and 2.9% or 3.8% above it. The IRS understands this incentive precisely, and officer compensation is one of the most reliable adjustment items in a small business examination.",
  "The remedy is not subtle. When the IRS recharacterizes distributions as wages, the result is back employment taxes for both employer and employee halves, failure to deposit penalties under Section 6656, failure to file penalties on payroll returns, accuracy-related penalties under Section 6662, and interest, applied across all open years. A three-year adjustment on a meaningfully understated salary regularly exceeds six figures.",
  "The Treasury Inspector General for Tax Administration has repeatedly flagged S-Corp officer compensation as an underreporting area, which keeps enforcement attention on it.",
 ]),
 ("The Nine Factors", [
  "IRS Fact Sheet FS-2008-25 and the case law behind it identify the factors that determine reasonableness.",
  "<strong>1. Training and experience.</strong> Education, credentials, and years in the field.",
  "<strong>2. Duties and responsibilities.</strong> What the officer actually does day to day, and the scope of authority.",
  "<strong>3. Time and effort devoted to the business.</strong> Full time, part time, or nominal.",
  "<strong>4. Dividend history.</strong> A pattern of large distributions with small wages is itself evidence.",
  "<strong>5. Payments to non-shareholder employees.</strong> If a non-owner manager earns more than the owner, that is difficult to explain.",
  "<strong>6. Timing and manner of paying bonuses to key people.</strong>",
  "<strong>7. What comparable businesses pay for similar services.</strong> The core of any defensible analysis.",
  "<strong>8. Compensation agreements.</strong> Written employment agreements set before the fact carry weight.",
  "<strong>9. The use of a formula to determine compensation.</strong> A consistent, documented formula applied across years is persuasive.",
  "No factor controls, and the analysis is holistic. But factor 7 is where a defense is built or lost, because it is the only one that produces an objective number.",
 ]),
 ("What the Case Law Establishes", [
  "<strong>Watson v. Commissioner</strong> (8th Cir. 2012) is the leading modern case. A CPA and partner in an accounting firm paid himself $24,000 in wages while taking roughly $175,000 in distributions in each of two years. The court sustained a recharacterization to $91,044 per year, relying on an expert's analysis of what comparable accounting professionals earned. The case establishes that courts will use market compensation data and that a token salary alongside substantial distributions will not survive.",
  "<strong>David E. Watson, P.C. v. United States</strong> confirmed that the inquiry is what the corporation should have paid for the services actually rendered, not what the shareholder chose to designate.",
  "<strong>Radtke v. United States</strong> (7th Cir. 1990) addressed the extreme case of an attorney paying himself zero salary and taking all profit as dividends. The court had no difficulty recharacterizing the entire amount as wages.",
  "<strong>Spicer Accounting v. United States</strong> (9th Cir. 1990) reached the same conclusion where an accountant worked full time and was paid only distributions.",
  "The pattern across these cases is consistent: zero or token compensation for a shareholder performing substantial services fails, and the recharacterized amount is set by reference to market data.",
 ]),
 ("How to Set a Defensible Number", [
  "Start with the market rate for the role, not with the profit. The question is what you would have to pay someone else to do what you do.",
  "Use real data sources: Bureau of Labor Statistics Occupational Employment and Wage Statistics, industry salary surveys, trade association compensation studies, and regional adjustments. Where a shareholder performs multiple roles, price each role separately and blend them by time allocation. An owner who spends 60% of their time practicing and 40% managing should be priced against both a practitioner salary and a manager salary.",
  "Adjust for the realities of the business: hours actually worked, whether the owner is part time, the size of the business, and geographic wage differences.",
  "Then sanity check against the business. Compensation cannot exceed what the business can pay, and it should bear a rational relationship to the value the owner's services generate as distinct from the return on invested capital. This is the legitimate argument for a wage below total profit: profit attributable to capital, to other employees, or to intangible assets is a return on investment rather than compensation for services.",
  "Document the analysis contemporaneously, adopt a written compensation agreement, and apply the same methodology consistently each year. A documented, reasoned position is defended very differently from a number chosen at year end.",
 ]),
 ("Common Mistakes", [
  "<strong>Using a percentage rule.</strong> There is no 60/40 rule. It appears in blog posts, not in authority. A 60/40 split can be far too low for a professional services business and far too high for a capital-intensive one.",
  "<strong>Setting the wage after the year closes.</strong> Compensation for services should be paid as the services are performed. A single December payroll run to true up the year is a recognizable pattern.",
  "<strong>Paying zero wages in a profitable year.</strong> The clearest way to lose.",
  "<strong>Ignoring the multiple-role reality.</strong> Owners who both produce and manage are frequently priced against only the lower of the two roles.",
  "<strong>Forgetting more-than-2% shareholder health insurance.</strong> Premiums must be included in W-2 Box 1 wages to be deductible by the shareholder above the line, and they count toward the compensation analysis.",
  "<strong>Ignoring the Section 199A interaction.</strong> Above the taxable income thresholds, the QBI deduction for a non-service business is limited by W-2 wages, so an artificially low salary can reduce the deduction by more than the payroll tax it saves.",
 ]),
 ("Correcting a Position That Is Too Low", [
  "If prior year compensation was clearly inadequate, the exposure grows with every open year. There are workable paths forward.",
  "Increase current-year compensation to a properly supported level and document the methodology going forward. This does not fix prior years but it stops the accrual and demonstrates good faith.",
  "Where prior years were materially wrong, amended payroll returns and corrected W-2s are possible, and voluntarily correcting before examination substantially improves the penalty posture.",
  "Where the S election itself was a poor fit, revoking it or restructuring may be the better answer than defending an indefensible wage history.",
  "The decision depends on the size of the gap and the number of open years, and it is worth modeling rather than guessing.",
 ]),
],
"faqs": [
 ("Is there a 60/40 rule for S-Corp salary?",
  "<p>No. There is no safe harbor percentage anywhere in the Code, regulations, or IRS guidance. The 60/40 rule is an internet convention with no authority behind it. The standard is a facts-and-circumstances analysis against what comparable businesses pay for comparable services.</p>"),
 ("What happens if the IRS says my salary was too low?",
  "<p>Distributions are recharacterized as wages, producing back employment taxes for both halves, failure to deposit and failure to file penalties, accuracy-related penalties, and interest across all open years. Adjustments spanning three years frequently exceed six figures.</p>"),
 ("How do I determine a reasonable salary?",
  "<p>Price the roles you actually perform using market data such as BLS Occupational Employment and Wage Statistics and industry salary surveys, blend them by time allocation, adjust for hours and geography, and sanity check against what the business can pay. Document the analysis contemporaneously and apply it consistently.</p>"),
 ("Can I pay myself zero salary if the business had a loss?",
  "<p>Generally yes. Reasonable compensation is required for services rendered, and where the business genuinely cannot pay, no wage may be appropriate. But taking distributions while paying no wages is the fact pattern that lost in Radtke and Spicer, so distributions and zero wages should not coexist.</p>"),
 ("Does my health insurance count as compensation?",
  "<p>Yes. Premiums paid for a more-than-2% shareholder must be included in W-2 Box 1 wages, though they are exempt from Social Security and Medicare tax when a proper plan exists. They count toward the total compensation figure in the reasonableness analysis and enable the above-the-line self-employed health insurance deduction.</p>"),
],
"related": [
 ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
 ("/c-corp-income-shifting-strategy/", "C-Corp Income Shifting Strategy"),
 ("/cash-balance-plan-tax-deduction/", "Cash Balance Plan Tax Deduction"),
 ("/accountable-plan/", "Accountable Plans: Reimbursing Yourself Correctly"),
 ("/business-owner-small-business-tax/", "Business Owner and Small Business Tax Services"),
],
"takeaways": [
 "No safe harbor percentage exists; the 60/40 rule has no authority behind it.",
 "Factor seven, what comparable businesses pay, is where a defensible position is actually built.",
 "Watson, Radtke, and Spicer all establish that token or zero salaries with substantial distributions fail.",
 "Price each role you perform separately and blend by time allocation.",
 "Above the Section 199A thresholds, an artificially low wage can cost more in lost QBI deduction than it saves.",
]},

# ---------------------------------------------------------------- 13
{
"slug": "c-corp-income-shifting-strategy",
"h1": "C-Corp Income Shifting Strategy: Moving Income From 37% to 21%",
"title": "C-Corp Income Shifting: 37% to 21%",
"description": "A C-Corp pays a flat 21% while top individual rates reach 37%. Here is how income shifting works, where the traps are, and when the double taxation cost outweighs the rate arbitrage.",
"subtitle": "The 16-point spread between the top individual rate and the corporate rate is real, but capturing it requires solving the second layer of tax.",
"keywords": ["C-Corp income shifting", "21% corporate rate", "C corp vs S corp", "accumulated earnings tax"],
"definition": "C-Corp income shifting is a strategy that moves business income from a pass-through structure taxed at individual rates of up to 37% into a C corporation taxed at the flat 21% rate under IRC Section 11, capturing the rate differential on income that can be retained inside the corporation rather than distributed. The strategy only produces a permanent benefit where the retained earnings are eventually extracted at favorable rates or never extracted as dividends, because a dividend distribution adds a second layer of tax that can push the combined rate above the pass-through alternative.",
"sections": [
 ("The Arithmetic of the Spread", [
  "A pass-through owner in the top bracket pays 37% federal on business income, plus 3.8% net investment income tax on passive income or 0.9% additional Medicare on earned income, plus state tax. A C corporation pays a flat 21% federal regardless of income level.",
  "On $1,000,000 of income retained in the business, the pass-through owner pays roughly $370,000 and the C corporation pays $210,000. That is $160,000 of additional capital retained and available for reinvestment each year.",
  "The catch is the second layer. If that after-tax corporate income is later distributed as a qualified dividend, the shareholder pays up to 20% plus 3.8% NIIT, bringing the combined federal rate to roughly 39.8%, which is worse than the 37% pass-through rate before considering the Section 199A deduction.",
  "So the strategy is not about the 21% rate. It is about the fact that the second layer is optional, deferrable, and sometimes avoidable entirely.",
 ]),
 ("When the Strategy Works", [
  "<strong>Capital-intensive growth.</strong> A business reinvesting all earnings into equipment, inventory, facilities, or headcount never distributes, so the second layer never arrives. The 21% rate funds growth with 16 cents more on the dollar.",
  "<strong>Section 1202 qualified small business stock.</strong> This is the strongest case. QSBS held more than five years can exclude a substantial portion of gain on sale, and the OBBBA expanded the regime with a tiered exclusion beginning at three years, a higher per-issuer cap, and an increased gross asset ceiling. A founder building toward an exit can pay 21% during the build and potentially exclude much of the gain at sale, which no pass-through structure can replicate.",
  "<strong>Specified service businesses above the 199A thresholds.</strong> A consultant, physician, or attorney whose income exceeds the phase-out gets no QBI deduction at all, which removes the pass-through structure's main advantage and narrows the comparison.",
  "<strong>Fringe benefit access.</strong> A C corporation can deduct benefits that a more-than-2% S-Corp shareholder cannot receive tax free, including full medical reimbursement plans under Section 105, group term life up to the statutory limit, disability coverage, and certain educational assistance.",
  "<strong>Charitable and timing flexibility.</strong> A fiscal year end can shift income between years, and the corporation is a separate taxpayer with its own brackets and its own year.",
 ]),
 ("The Structures Used to Shift Income", [
  "<strong>Management company structure.</strong> An operating pass-through pays a C corporation for genuine management, administrative, marketing, or IT services. The fee is deductible to the payer and taxed at 21% in the C corporation. The fee must be reasonable in amount and supported by an actual service agreement and actual services, or Section 482 allows the IRS to reallocate income between commonly controlled entities.",
  "<strong>Intellectual property licensing.</strong> A C corporation owns trademarks, software, or processes and licenses them to the operating entity for arm's length royalties. This works best where the IP was developed in or contributed to the corporation from the start, since transferring appreciated IP later has its own consequences.",
  "<strong>Captive services or equipment leasing.</strong> The corporation owns equipment and leases it to the operating business, capturing both the rate arbitrage and depreciation deductions inside the corporation.",
  "<strong>Direct conversion.</strong> Revoking an S election or converting an LLC to corporate taxation. This is the simplest and the least reversible, and it triggers the built-in gains considerations discussed below.",
  "In every case the fee must be arm's length and the services or property real. These structures fail on substance, not on form.",
 ]),
 ("The Traps", [
  "<strong>Accumulated earnings tax.</strong> Section 531 imposes a 20% penalty tax on earnings accumulated beyond the reasonable needs of the business. There is a credit of $250,000, or $150,000 for personal service corporations in health, law, engineering, architecture, accounting, actuarial science, performing arts, and consulting. Accumulating cash without a documented business purpose is exactly what this provision targets, and contemporaneous documentation of expansion plans, working capital needs, and contingencies is the defense.",
  "<strong>Personal holding company tax.</strong> Section 541 imposes a 20% tax on undistributed personal holding company income where a closely held corporation derives 60% or more of adjusted ordinary gross income from passive sources such as dividends, interest, rents, and royalties. An IP licensing structure can walk into this if the corporation has little else.",
  "<strong>Built-in gains tax.</strong> Converting from C to S later triggers Section 1374 on gains built in at conversion, recognized within the five-year period. This is the reverse direction, but it matters because it makes the C election harder to unwind.",
  "<strong>Trapped appreciated assets.</strong> Getting appreciated property out of a C corporation is expensive. Real estate in particular should almost never sit in a C corporation, because a later distribution or liquidation triggers gain at the corporate level and again at the shareholder level.",
  "<strong>Loss of loss pass-through.</strong> C corporation losses stay at the corporate level as NOL carryforwards subject to the 80% taxable income limitation. They do not offset the owner's other income.",
 ]),
 ("Getting Money Out Without a Dividend", [
  "The strategy depends on extraction paths that are not dividends.",
  "Reasonable salary to owner-employees is deductible to the corporation and taxed once, though it carries payroll tax. It is the primary release valve and the reasonableness standard mirrors the S-Corp analysis.",
  "Rent for property the owner holds personally and leases to the corporation, at arm's length rates, is deductible to the corporation and taxed once to the owner, without payroll tax.",
  "Interest on genuine shareholder loans, properly documented with market rate terms, is likewise deductible and taxed once.",
  "Retirement plan contributions on behalf of owner-employees are deductible and defer tax entirely, and a C corporation with a defined benefit or cash balance plan can move very large amounts.",
  "Sale of stock, ideally as qualified small business stock under Section 1202, converts the entire accumulated value into capital gain with a potentially large exclusion. This is the intended exit for the growth-oriented version of the strategy.",
 ]),
 ("How We Decide", [
  "We model at least a full ten-year horizon, not a single year. Any comparison that stops at year one makes the C corporation look better than it is, because it ignores the second layer entirely.",
  "The inputs that decide it are the proportion of earnings that must be distributed to fund the owner's lifestyle, the expected exit and whether Section 1202 is available, whether the business is a specified service business above the 199A thresholds, the state tax treatment of corporations versus pass-throughs including any pass-through entity tax election, and the type of assets the business will accumulate.",
  "A business that distributes most of its earnings to its owner every year is almost never a good C corporation candidate, regardless of the rate spread. A business reinvesting everything toward a stock sale in seven years frequently is.",
 ]),
],
"faqs": [
 ("Does converting to a C-Corp actually save tax?",
  "<p>Only on income retained in the corporation. The 21% corporate rate beats a 37% individual rate on retained earnings, but distributing those earnings as qualified dividends adds a second layer that brings the combined federal rate to roughly 39.8%. The strategy works when earnings stay in the business or exit as capital gain rather than dividends.</p>"),
 ("What is the accumulated earnings tax?",
  "<p>A 20% penalty tax under Section 531 on earnings accumulated beyond the reasonable needs of the business, with a credit of $250,000 or $150,000 for personal service corporations. It is the principal risk in a strategy built on retaining earnings, and it is defended with contemporaneous documentation of expansion plans and working capital needs.</p>"),
 ("Can I use a management company to shift income to a C-Corp?",
  "<p>Yes, if the arrangement is real. The C corporation must actually provide services, the fee must be arm's length, and there must be a written agreement with supporting records. Section 482 allows the IRS to reallocate income between commonly controlled entities where the pricing does not reflect economic reality.</p>"),
 ("Should I hold real estate in a C-Corp?",
  "<p>Almost never. Appreciated property distributed out of a C corporation triggers gain at the corporate level and again at the shareholder level, and there is no equivalent of the partnership rules that allow tax-free property distributions. Real estate belongs in a partnership or disregarded entity.</p>"),
 ("What makes Section 1202 QSBS so important here?",
  "<p>It is the exit that makes the strategy permanent rather than deferred. Qualified small business stock in a C corporation can exclude a substantial portion of gain on sale after the required holding period, and the OBBBA expanded the regime with tiered exclusions starting at three years and higher caps. No pass-through structure offers an equivalent.</p>"),
],
"related": [
 ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
 ("/reasonable-compensation-s-corp-irs/", "Reasonable Compensation for S-Corp Owners"),
 ("/cash-balance-plan-tax-deduction/", "Cash Balance Plan Tax Deduction"),
 ("/c-corp-tax-strategy/", "C-Corp Tax Strategy Services"),
 ("/retirement-exit-ma-tax-strategy/", "Retirement, Exit and M&A Tax Strategy"),
],
"takeaways": [
 "The 21% rate only helps on earnings that stay in the corporation; dividends push the combined rate above 37%.",
 "Section 1202 QSBS is what converts the deferral into a permanent benefit for growth companies.",
 "Management fees and IP royalties must be arm's length and substantiated, or Section 482 reallocates them.",
 "The accumulated earnings tax and personal holding company tax are the two penalty regimes to plan around.",
 "Never hold appreciating real estate in a C corporation; extraction is prohibitively expensive.",
]},

# ---------------------------------------------------------------- 14
{
"slug": "cash-balance-plan-tax-deduction",
"h1": "Cash Balance Plan Tax Deduction: How High Earners Deduct Six Figures",
"title": "Cash Balance Plan Tax Deduction 2026",
"description": "A cash balance plan can produce a six-figure annual deduction for a business owner, far beyond a 401(k). Here is how contribution limits are calculated, what it costs to run, and who it fits.",
"subtitle": "For a profitable owner over 45 with stable cash flow, no other strategy produces a deduction this large without changing the underlying business.",
"keywords": ["cash balance plan tax deduction", "cash balance plan limits", "defined benefit plan business owner"],
"definition": "A cash balance plan is a defined benefit retirement plan that expresses each participant's benefit as a hypothetical account balance credited annually with a pay credit and a guaranteed interest credit. Because the deductible contribution is actuarially determined by the benefit promised at retirement rather than capped at a flat dollar limit, contributions rise sharply with the participant's age, allowing an owner in their fifties or sixties to deduct well over $200,000 per year, on top of 401(k) and profit sharing contributions.",
"sections": [
 ("Why the Deduction Is So Much Larger Than a 401(k)", [
  "A defined contribution plan caps what goes in. The Section 415(c) annual additions limit governs total contributions to a participant's account, and for 2026 that figure is roughly $72,000 plus catch-up contributions for those 50 and older.",
  "A defined benefit plan caps what comes out. Section 415(b) limits the annual benefit payable at retirement, roughly $290,000 per year for 2026. The contribution required to fund that benefit is then computed actuarially, and it depends almost entirely on how many years remain until retirement.",
  "That inversion is the whole point. A 40-year-old has 22 years to fund the benefit; a 58-year-old has four. The 58-year-old's required annual contribution is therefore several times larger, and it is fully deductible.",
  "Approximate maximum cash balance contributions by age, assuming compensation supports the benefit: age 40 around $90,000 to $120,000, age 45 around $130,000 to $160,000, age 50 around $180,000 to $215,000, age 55 around $230,000 to $270,000, age 60 around $280,000 to $330,000, and age 65 potentially above $350,000. These are illustrative, and the actual number comes from an actuary applying the plan's formula and assumptions to the specific participant.",
 ]),
 ("Stacking With a 401(k) and Profit Sharing", [
  "Cash balance plans are almost always paired with a 401(k) profit sharing plan, and the combination is where the total deduction comes from.",
  "The employee deferral, roughly $24,500 for 2026 with an additional catch-up for those 50 and older, is unaffected by the cash balance plan.",
  "Employer profit sharing is limited when a defined benefit plan covers the same employees. Under the combined plan deduction limit of Section 404(a)(7), employer contributions to the defined contribution plan are generally limited to 6% of covered compensation when a defined benefit plan is also maintained, unless the defined benefit plan is PBGC-covered, in which case the limit does not apply.",
  "A typical stack for a 55-year-old owner: roughly $24,500 in deferrals, roughly $8,000 in catch-up, roughly $20,000 in profit sharing at the 6% limit, and roughly $250,000 in cash balance contributions, producing a total deduction above $300,000. At a combined 42% marginal rate that is roughly $126,000 of current-year tax deferred.",
 ]),
 ("The Employee Cost Nobody Mentions First", [
  "Cash balance plans are qualified plans and must satisfy coverage under Section 410(b) and nondiscrimination under Section 401(a)(4). You cannot cover only the owner if you have employees.",
  "In practice, the plans are cross-tested on a benefits basis, which allows the owner to receive a much larger pay credit than staff while still passing, because the owner is older and has fewer years to accrue. Typical staff pay credits run 5% to 8% of compensation, sometimes structured as a combination of cash balance credits and profit sharing.",
  "The rule of thumb is that staff cost runs 5% to 12% of covered payroll depending on demographics. For a practice with three employees and $200,000 of staff payroll, that is $10,000 to $24,000 per year, which is small relative to a $250,000 owner deduction. For a business with forty employees and $2,000,000 of staff payroll, the arithmetic frequently does not work.",
  "This is why cash balance plans concentrate among professional practices and small owner-heavy businesses: few employees, high owner compensation, and a large age gap between owner and staff.",
 ]),
 ("Funding Obligations and Flexibility", [
  "This is a defined benefit plan, which means the contribution is a funding obligation, not a discretionary choice. Minimum required contributions apply under Section 430, and failure to meet them triggers excise taxes under Section 4971.",
  "There is meaningful flexibility within a range. The actuary computes a minimum and a maximum deductible contribution, and the spread between them is often substantial, which lets an owner contribute more in strong years and less in weak ones.",
  "The interest crediting rate is a design lever. A fixed rate creates predictable obligations but exposes the plan to investment shortfalls that must be made up. An actual rate of return crediting design passes investment risk to participants and largely eliminates funding volatility, which is why most modern small plans use it.",
  "Plans can be frozen if circumstances change, stopping future accruals while preserving accrued benefits, and they can be terminated with assets rolled to IRAs. Neither is free, and the IRS expects a plan to be established with the intent of permanence, generally interpreted as several years of operation.",
 ]),
 ("Setup, Cost, and Deadlines", [
  "Establishment requires a plan document, an enrolled actuary, and a trustee. Annual administration includes an actuarial valuation, Form 5500 filing with Schedule SB signed by the actuary, participant statements, and PBGC premiums where the plan is covered. Professional service employer plans covering fewer than 26 participants are generally exempt from PBGC coverage.",
  "Realistic costs are $2,000 to $5,000 for setup and $2,500 to $6,000 per year in ongoing actuarial and administrative fees, plus investment management. Against a six-figure deduction, this is not the deciding factor.",
  "On timing, the SECURE Act permits a plan to be adopted as late as the due date of the employer's return, including extensions, for the first plan year. That means a plan can often be established after year end and still produce a deduction for the closed year, though employee deferrals cannot be made retroactively.",
 ]),
 ("Who It Fits and Who It Does Not", [
  "It fits an owner aged 45 or older, with net business income consistently above roughly $400,000, few employees relative to owner compensation, cash flow stable enough to sustain contributions for at least five years, and a genuine intent to save rather than a one-year desire for a deduction.",
  "It does not fit a business with volatile income that cannot commit to multi-year funding, a business with a large young workforce where staff cost overwhelms the benefit, an owner under 40 for whom the contribution advantage over a 401(k) profit sharing plan is modest, or an owner who needs the cash for business reinvestment.",
  "It is worth adding that this is a deferral, not an exclusion. Distributions are taxed as ordinary income in retirement. The strategy works when the deduction is taken at a 40%+ marginal rate and the distributions come out at a lower rate, or when the balance is rolled to an IRA and managed across a long horizon. An owner who expects higher rates in retirement should model that before committing.",
 ]),
],
"faqs": [
 ("How much can I contribute to a cash balance plan?",
  "<p>It depends almost entirely on age, because the contribution is actuarially derived from the benefit promised at retirement. Approximate maximums run from $90,000 to $120,000 at age 40 up to $280,000 to $330,000 at age 60, assuming compensation supports the benefit. An actuary produces the actual figure.</p>"),
 ("Can I have a cash balance plan and a 401(k)?",
  "<p>Yes, and they are almost always paired. Employee deferrals are unaffected, but employer profit sharing contributions are generally limited to 6% of covered compensation under the combined plan deduction limit of Section 404(a)(7) unless the defined benefit plan is PBGC-covered.</p>"),
 ("Do I have to cover my employees?",
  "<p>Yes. Coverage and nondiscrimination rules apply, so you cannot cover only the owner. Cross-testing on a benefits basis allows the owner to receive a much larger credit than staff, and typical staff cost runs 5% to 12% of covered payroll, which is why these plans fit owner-heavy businesses with few employees.</p>"),
 ("What if I cannot afford the contribution in a bad year?",
  "<p>The actuary sets a minimum and a maximum deductible contribution, and the range between them provides real flexibility. In a sustained downturn a plan can be frozen to stop future accruals, or terminated with assets rolled to IRAs. Missing a minimum required contribution without taking one of those steps triggers excise tax under Section 4971.</p>"),
 ("When must the plan be established?",
  "<p>Under the SECURE Act, a plan can generally be adopted as late as the due date of the employer's tax return including extensions for the first plan year, so a plan established after year end can still produce a deduction for that closed year. Employee salary deferrals, however, cannot be made retroactively.</p>"),
],
"related": [
 ("/s-corp-vs-llc-tax-comparison-2026/", "S-Corp vs LLC Tax Comparison 2026"),
 ("/c-corp-income-shifting-strategy/", "C-Corp Income Shifting Strategy"),
 ("/reasonable-compensation-s-corp-irs/", "Reasonable Compensation for S-Corp Owners"),
 ("/best-retirement-plan-business-owner-over-500k/", "Best Retirement Plan for Business Owners Over $500K"),
 ("/retirement-exit-ma-tax-strategy/", "Retirement, Exit and M&A Tax Strategy"),
],
"takeaways": [
 "Defined benefit plans cap the benefit, not the contribution, which is why the deduction scales with age.",
 "A 55-year-old owner can commonly stack past $300,000 of total deductible retirement contributions.",
 "Staff cost of 5% to 12% of covered payroll is what determines whether the plan works.",
 "Contributions are a funding obligation, so multi-year cash flow stability is a prerequisite.",
 "SECURE Act timing allows adoption after year end, up to the extended return due date.",
]},

# ---------------------------------------------------------------- 15
{
"slug": "cost-segregation-for-restaurant",
"h1": "Cost Segregation for Restaurants",
"title": "Cost Segregation for Restaurants 2026",
"description": "Restaurants reclassify 30% to 40% of basis thanks to kitchen equipment, specialty MEP, and decorative finishes. Here is what qualifies, how leasehold improvements work, and what returns look like.",
"subtitle": "Kitchens, bars, dining room finishes, and the specialty plumbing and electrical that serve them make restaurants one of the strongest asset classes for reclassification.",
"keywords": ["cost segregation restaurant", "restaurant depreciation", "qualified improvement property restaurant"],
"definition": "Cost segregation for restaurants is an engineering study that reallocates a restaurant property's cost from the 39-year nonresidential recovery period into 5-year, 7-year, and 15-year MACRS classes. Restaurants typically reclassify 30% to 40% of depreciable basis, driven by commercial kitchen equipment, walk-in refrigeration, bar and beverage systems, decorative finishes and lighting, and the specialty plumbing, electrical, and ventilation installed to serve that equipment rather than the building generally.",
"sections": [
 ("Why Restaurants Reclassify So Strongly", [
  "The build-out is the asset. A restaurant shell is a fairly ordinary commercial box, and most of the money goes into what is installed inside it.",
  "The kitchen alone is a large 5-year bucket: ranges, ovens, fryers, griddles, hoods, walk-in coolers and freezers, prep tables, dishwashing systems, ice machines, and point-of-sale equipment.",
  "The dining room adds furniture, decorative and accent lighting, millwork and booth seating, window treatments, wall coverings, and specialty flooring.",
  "The bar contributes beverage systems, glass washers, under-counter refrigeration, taps and lines, and back-bar millwork.",
  "The largest engineering judgment concerns the mechanical, electrical, and plumbing that serves this equipment specifically. Dedicated gas lines to cooking equipment, kitchen exhaust and make-up air systems, grease waste piping, dedicated electrical circuits to appliances, and refrigeration line sets are frequently allocable to the equipment they serve rather than to the building's base systems. On a full build-out this specialty MEP allocation can exceed the equipment itself.",
 ]),
 ("Component Detail", [
  "<strong>5-year property:</strong> kitchen equipment and appliances, walk-in refrigeration boxes and systems, hoods and exhaust fans serving equipment, bar and beverage systems, dining and bar furniture, decorative lighting, wall coverings and decorative finishes, signage inside the premises, point-of-sale and audiovisual systems, and specialty electrical and plumbing serving specific equipment.",
  "<strong>7-year property:</strong> office furniture and certain fixtures without an assigned class life.",
  "<strong>15-year property:</strong> land improvements including parking, drive-through lanes and canopies, sidewalks and patios, landscaping and irrigation, site lighting, fencing, drainage, and exterior signage. Qualified improvement property also carries a 15-year life.",
  "<strong>39-year property:</strong> structural frame, foundation, roof, exterior envelope, and base building mechanical, electrical, plumbing, and fire protection.",
  "Patios and outdoor dining are worth attention. Hardscaping, patio heaters, outdoor lighting, and railings often reclassify well, and many operators added substantial outdoor infrastructure in recent years that has never been analyzed.",
 ]),
 ("Owned Property vs Leasehold Improvements", [
  "Most restaurant operators lease. That changes the analysis but does not eliminate it.",
  "Where the tenant pays for the build-out, the tenant owns the improvements for tax purposes and depreciates them. Interior improvements to nonresidential property placed in service after the building was first placed in service generally qualify as qualified improvement property with a 15-year recovery period, which is bonus-eligible at 100%.",
  "Note the exclusions from QIP: enlargements of the building, elevators and escalators, and internal structural framework. Those remain 39-year property.",
  "A cost segregation study on a leasehold build-out separates the 5-year equipment and specialty systems from the 15-year QIP and the 39-year structural work, and the first two categories are fully deductible in year one.",
  "Tenant improvement allowances complicate this. Where the landlord funds the improvements and owns them, the landlord depreciates them and the tenant may have income under Section 110 rules or a reduction in basis, depending on how the lease is written. The lease language determines the answer, and it is worth reading before the study rather than after.",
  "If the lease ends before the improvements are fully depreciated, the remaining basis is generally deductible on abandonment, which is a commonly missed deduction when a location closes.",
 ]),
 ("Illustrative Returns", [
  "<div class=\"ae-table-scroll\" style=\"overflow-x:auto;-webkit-overflow-scrolling:touch;max-width:100%\"><table><thead><tr><th>Scenario</th><th>Cost</th><th>Depreciable basis</th><th>Reclassified</th><th>Year 1 deduction</th></tr></thead><tbody>"
  "<tr><td>Leasehold build-out, fast casual</td><td>$850,000</td><td>$850,000</td><td>38% / $323,000</td><td>~$850,000 (QIP + equip.)</td></tr>"
  "<tr><td>Owned building, full service</td><td>$2,600,000</td><td>$2,050,000</td><td>36% / $738,000</td><td>~$779,000</td></tr>"
  "<tr><td>Owned building with patio, brewpub</td><td>$4,400,000</td><td>$3,500,000</td><td>39% / $1,365,000</td><td>~$1,420,000</td></tr>"
  "<tr><td>Three-location group, owned</td><td>$9,200,000</td><td>$7,400,000</td><td>35% / $2,590,000</td><td>~$2,713,000</td></tr>"
  "</tbody></table></div>",
  "The leasehold case is worth reading closely. Where the entire build-out is 5-year equipment plus 15-year QIP with no 39-year structural component, essentially the whole investment is bonus-eligible and deductible in year one. That is a materially better outcome than owning the building, and many operators do not realize it.",
 ]),
 ("Related Credits and Deductions Worth Coordinating", [
  "The FICA tip credit under Section 45B provides a credit for employer Social Security and Medicare taxes paid on employee tips above the amount treated as wages for minimum wage purposes. For a full-service restaurant this is often tens of thousands of dollars annually and it is routinely missed.",
  "The Work Opportunity Tax Credit applies to hires from targeted groups, which fits restaurant hiring patterns well, but it requires Form 8850 certification submitted within 28 days of the start date, so it cannot be claimed retroactively.",
  "Section 179 covers roofs, HVAC, fire protection, and security systems on nonresidential buildings, which bonus depreciation cannot reach because they are 39-year property. For an owner replacing a rooftop HVAC unit, this is the only accelerated path.",
  "Energy incentives under Section 179D may apply to significant lighting, HVAC, and envelope upgrades.",
  "These stack with the cost segregation study rather than competing with it, and they should be evaluated together.",
 ]),
 ("Timing Around Openings, Remodels, and Closures", [
  "Restaurants turn over their physical assets faster than almost any other business, and each event is a planning point.",
  "At opening, the study should be performed in the year the location is placed in service so the depreciation schedule is correct from the first return. Pre-opening expenditures are a separate analysis: start-up costs under Section 195 are deductible up to a limited amount in the first year with the remainder amortized over 180 months, and they should not be mixed into the depreciable build-out.",
  "At remodel, the study captures new short-life property while a partial disposition election writes off the undepreciated basis of what came out. A dining room refresh that replaces flooring, lighting, and seating frequently leaves the original components sitting on the fixed asset schedule, so the operator is depreciating two sets of the same assets.",
  "The repair regulations matter throughout. Not every remodel dollar is a capital improvement. The betterment, adaptation, and restoration framework of Reg. 1.263(a)-3 allows a meaningful share of routine refresh spending to be deducted currently, and the routine maintenance safe harbor covers recurring work expected more than once in a ten-year period. Sorting a remodel budget into repairs, short-life property, and structure before the work starts is worth substantially more than analyzing invoices afterward.",
  "At closure, the remaining basis in leasehold improvements is generally deductible on abandonment, and any equipment sold or scrapped produces its own gain or loss.",
 ]),
 ("Passive Loss Treatment and Structure", [
  "An operating restaurant is a trade or business, not a rental activity, so losses are non-passive for an owner who materially participates. There is no need to navigate the rental exceptions that short-term rental owners rely on.",
  "Many restaurant groups hold the real estate in a separate LLC that leases to the operating entity. This is sound for liability and estate planning, but it triggers the self-rental rules of Reg. 1.469-2(f)(6), under which net rental income from a self-rental is recharacterized as non-passive while net rental losses remain passive. That asymmetry can strand losses in the property entity.",
  "A grouping election under Reg. 1.469-4 treating the rental and the operating business as a single activity often resolves this, where the entities are under common control and constitute an appropriate economic unit. The election should be made deliberately and documented with the return.",
 ]),
],
"faqs": [
 ("How much does a restaurant cost segregation study reclassify?",
  "<p>Typically 30% to 40% of depreciable basis. The drivers are commercial kitchen equipment, walk-in refrigeration, bar systems, decorative finishes, and the dedicated plumbing, electrical, and ventilation serving that equipment rather than the building generally.</p>"),
 ("Can I do a cost segregation study on a leased restaurant space?",
  "<p>Yes, where you paid for and own the build-out. Interior improvements generally qualify as qualified improvement property with a 15-year life that is bonus-eligible, and the equipment is 5-year property. On a pure leasehold build-out with no structural work, close to the entire investment can be deductible in year one.</p>"),
 ("What happens to my improvements if I close the location?",
  "<p>The remaining undepreciated basis in leasehold improvements is generally deductible on abandonment when the lease terminates and you surrender the space. This is one of the most commonly missed deductions when a restaurant closes a location.</p>"),
 ("Is restaurant income passive?",
  "<p>No, an operating restaurant is a trade or business and losses are non-passive for an owner who materially participates. If the real estate sits in a separate entity leasing to the operating company, the self-rental rules apply and a grouping election under Reg. 1.469-4 is often needed to avoid stranding losses.</p>"),
 ("What other credits should a restaurant be claiming?",
  "<p>The Section 45B FICA tip credit is the largest routinely missed item for full-service restaurants. The Work Opportunity Tax Credit fits restaurant hiring but requires Form 8850 within 28 days of hire. Section 179 covers roofs and HVAC that bonus depreciation cannot reach, and Section 179D may apply to energy upgrades.</p>"),
],
"related": [
 ("/cost-segregation-study/", "Cost Segregation Study: How It Works and What It Costs"),
 ("/cost-segregation-for-hotel-motel/", "Cost Segregation for Hotels and Motels"),
 ("/section-179-vs-bonus-depreciation-2026/", "Section 179 vs Bonus Depreciation in 2026"),
 ("/bonus-depreciation-2026-obbba/", "Bonus Depreciation 2026 Under the OBBBA"),
 ("/cost-segregation-for-multifamily/", "Cost Segregation for Multifamily Properties"),
],
"takeaways": [
 "Restaurants reclassify 30% to 40% of basis, with specialty MEP often exceeding the equipment itself.",
 "A pure leasehold build-out can be almost entirely deductible in year one as QIP plus 5-year equipment.",
 "Abandonment of remaining leasehold basis on a closure is a routinely missed deduction.",
 "The Section 45B FICA tip credit is the largest overlooked item for full-service operators.",
 "Separating real estate into its own entity triggers self-rental rules that often require a grouping election.",
]},

]
