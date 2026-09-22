#!/usr/bin/env python3
"""Publish researched, situation-specific tax articles and connect them to hubs."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

import seo_render

seo_render.BASE = "https://www.aetaxadvisors.com"
ROOT = Path(__file__).parent
DATE = "2026-09-22"

ARTICLES = [
    dict(
        slug="rental-purchase-seller-credits-basis",
        title="How Seller Credits Affect Rental Property Tax Basis",
        description="A seller credit at a rental closing can change purchase price, basis, or a separate expense. Learn how to classify the credit and document the allocation.",
        category="Real Estate Tax Planning",
        hub="rental",
        lead="A seller credit is not a tax category by itself. Its treatment depends on what the credit pays for and whether the purchase price, an owner expense, or a seller obligation changed.",
        body="""
<h2>Start with the settlement statement, then read the contract</h2>
<p>A closing disclosure may put several economically different items in one column called “seller credit.” One might be a negotiated reduction in the price of a property with known defects. Another might reimburse buyer loan charges. A third might settle property taxes attributable to the seller's ownership period. They should not automatically receive the same tax treatment. Match each line to the purchase agreement, invoices, tax bill, and lender documents before posting a journal entry.</p>
<p>The buyer's starting basis generally includes the amount paid for the property plus eligible acquisition costs. A genuine price concession generally lowers what the buyer paid. By contrast, a cost that is separately deductible or a cost of borrowing does not become building basis merely because it appeared at closing. The land/building allocation must then be applied to the resulting acquisition basis; land is not depreciated.</p>
<h2>Distinguish three common credit patterns</h2>
<p><strong>Price reduction for condition.</strong> If the seller agrees to a lower effective purchase price because the roof needs work, the credit may reduce the property's cost basis. The buyer must still classify the subsequent roof work on its own facts; a substantial replacement is not converted into a current repair simply because the seller funded it indirectly.</p>
<p><strong>Buyer closing costs.</strong> If a credit pays title or transfer charges that otherwise enter acquisition basis, the buyer should consider both the gross charge and offsetting credit, avoiding a double increase in basis. If it pays loan origination charges, those costs are generally analyzed as financing costs over the loan's life. If it pays a prepaid insurance premium, the coverage period matters.</p>
<p><strong>Seller-period obligations.</strong> A property tax proration is tied to periods of ownership. The buyer and seller generally allocate real property taxes under the applicable federal rule regardless of which party writes the check. A rent or security-deposit transfer also needs its own treatment; a refundable tenant deposit is a liability, not purchase-price income to be blended into basis.</p>
<h2>Illustrative closing</h2>
<p>Assume a buyer agrees to $500,000 for a duplex, receives a $12,000 credit for a documented price concession, and pays $4,000 of eligible title and recording costs. The initial property cost calculation could begin at $488,000 plus qualifying acquisition charges, followed by a supportable allocation between land and improvements. If $3,000 of the seller credit instead paid lender fees, the financing component needs a separate schedule. These numbers are illustrative; the signed contract and actual settlement flows control.</p>
<h2>Records and a clean basis schedule</h2>
<p>Keep the executed purchase agreement and addenda, final settlement statement, invoices paid through escrow, lender fee detail, tax prorations, and an allocation support file such as an appraisal. Record the full transaction once, then reconcile cash paid, debt assumed, and every credit. Maintain separate schedules for land, building, later improvements, and loan costs. This makes future depreciation and sale calculations auditable.</p>
<p>For the broader distinction between purchase basis and operating deductions, see the <a href="/guides/rental-property-tax-questions/">rental property tax questions hub</a> and <a href="/blog/rental-property-closing-costs-basis/">rental closing-cost guide</a>. The IRS's <a href="https://www.irs.gov/publications/p551">Publication 551</a> explains basis and settlement costs; <a href="https://www.irs.gov/publications/p527">Publication 527</a> covers rental expenses and depreciation.</p>
""",
    ),
    dict(
        slug="rental-lease-up-costs-before-first-tenant",
        title="Rental Lease-Up Costs Before the First Tenant",
        description="Which costs can a landlord deduct before the first tenant moves in? Separate ready-for-rent operating costs from acquisition and improvement costs.",
        category="Real Estate Tax Planning",
        hub="rental",
        lead="The first rent check is not the decisive date for every rental deduction. A property can be in service when it is ready and available for rent, even while the owner is still searching for a tenant.",
        body="""
<h2>Establish the ready-and-available date</h2>
<p>Depreciation generally starts when a rental is ready and available for its intended use. The date can precede the first signed lease, but a listing alone is weak evidence if a kitchen is unusable or required occupancy approvals are missing. Keep photos, listing history, permits, inspection approvals, utility activation, property-manager correspondence, and the first application. A contemporaneous timeline is more persuasive than reconstructing the date years later.</p>
<p>Once the property is genuinely held out for rent, normal operating costs can arise during vacancy: utilities, insurance, management, advertising, and ordinary maintenance. They still need the usual business-purpose and allocation analysis. A period of personal use, or a property taken off the rental market for a major renovation, changes the facts. The absence of tenants does not by itself make an otherwise eligible expense personal.</p>
<h2>Do not bundle repairs and improvements</h2>
<p>Painting and minor fixes may be ordinary repairs when they keep the property in efficient operating condition. Replacing a roof, adding a bathroom, or rehabilitating a building can instead create or improve a capital asset. Work done immediately after purchase deserves a particularly careful look: invoices may reflect a plan to put an acquired property into usable condition, not independent recurring maintenance. Describe the work item by item rather than calling the entire contractor payment “make-ready.”</p>
<p>Property acquisition charges belong in a basis analysis; loan charges generally follow financing rules. Furnishings and appliances may have separate depreciation treatment from the building. Expenses incurred before a rental business is actually operating can raise startup or capitalization questions, so the ready-for-rent chronology and the nature of the activity matter. A single “pre-tenant costs” account hides these distinctions.</p>
<h2>Illustrative timeline</h2>
<p>Suppose a landlord closes on June 1. A broken heating system prevents occupancy until July 15. The home is photographed, listed, and available to qualified applicants on July 16, but the first tenant arrives September 1. July 16 can be the placed-in-service date if the property was genuinely ready then. Depreciation and eligible vacancy-period operating costs do not automatically wait until September. The heating work itself needs a repair-versus-improvement review; its invoice should not be classified by the later lease date alone.</p>
<h2>Prepare a two-column workpaper</h2>
<p>For every lease-up invoice, record the service date, what was done, the property area affected, and whether the cost is tied to acquisition, borrowing, restoration, or ordinary operation. Then document the ready-and-available date. Separate any owner travel, personal furnishings, and utilities used during personal occupancy. This produces defensible schedules for the return and makes later basis adjustments easier.</p>
<p>See the <a href="/blog/rental-property-placed-in-service-date/">placed-in-service date guide</a> and the <a href="/guides/rental-property-tax-questions/">rental topic hub</a>. IRS <a href="https://www.irs.gov/publications/p527">Publication 527</a> discusses when rental property is placed in service, vacant rentals, and expense classification.</p>
""",
    ),
    dict(
        slug="1031-exchange-debt-relief-boot",
        title="Does Debt Relief Create Boot in a 1031 Exchange?",
        description="Learn how mortgages paid off or assumed in a real estate exchange can create taxable boot, and why replacement debt alone is not the full calculation.",
        category="Real Estate Tax Planning",
        hub="rental",
        lead="An exchanger can receive taxable value without receiving cash. Relief from a mortgage on the relinquished property is generally treated like money received in a Section 1031 exchange, subject to the complete exchange calculation.",
        body="""
<h2>Why loan balances belong in the exchange worksheet</h2>
<p>Section 1031 permits deferral of gain on qualifying exchanges of business or investment real property when its requirements are met. It does not make a transaction tax-free by label alone. Cash received, nonqualifying property, and certain debt relief can cause current recognition of gain. A qualified intermediary and exchange timing matter, but neither removes boot created by the economics of the deal.</p>
<p>When another party assumes a liability or the exchanger's mortgage is paid off with exchange proceeds, the exchanger has been relieved of debt. Liabilities the exchanger assumes on replacement property can offset that relief in the exchange computation. Cash the exchanger contributes may also affect net boot. The correct result comes from the full closing statements and Form 8824 calculation; simply comparing the two mortgage balances may miss cash received, exchange expenses, or other liabilities.</p>
<h2>Work an illustrative example</h2>
<p>Assume an investor sells qualifying rental real estate for $800,000, with $300,000 of debt discharged, then acquires qualifying replacement real estate for $750,000 with $250,000 of new debt. At a high level, the $50,000 net reduction in liabilities can function as boot if not offset by other consideration the exchanger provides. Recognition is limited by realized gain and the detailed rules. This is not a $50,000 tax bill; it is a potential amount of gain recognized before rates and character are determined.</p>
<p>Now suppose the investor instead buys an $800,000 replacement property with $250,000 of new debt and adds $50,000 of cash to the $500,000 exchange proceeds. The exchange's net money calculation can change. Conversely, taking $50,000 cash from the intermediary is a separate source of boot. An investor can have a seemingly equal-value property exchange yet still receive cash or debt relief, so value and debt tests should be modeled together before contracts are signed.</p>
<h2>Watch for nonqualifying items and gain character</h2>
<p>Only qualifying real property receives Section 1031 treatment. Allocations to furniture, equipment, or certain intangible items can be taxable even when included in the same sale contract. Depreciation history can affect the character and rate of recognized gain. Exchange expenses, loan fees, prorated rent, deposits, and property tax adjustments should be classified separately; the net wire transfer is not the tax answer.</p>
<h2>Build the closing package</h2>
<p>Retain both signed contracts, intermediary agreement, closing statements, loan payoff letters, new loan documents, valuations and allocations, and the depreciation/basis schedule for the old property. Reconcile the intermediary's receipts and disbursements to the taxpayer's cash flows. Have the tax computation reviewed before a sale closes when debt will be replaced with less debt.</p>
<p>For the portfolio context, see <a href="/real-estate-tax-planning/">real estate tax planning</a> and the <a href="/guides/rental-property-tax-questions/">rental questions hub</a>. The primary rules and examples are in IRS <a href="https://www.irs.gov/publications/p544">Publication 544</a> and the <a href="https://www.irs.gov/instructions/i8824">Form 8824 instructions</a>.</p>
""",
    ),
    dict(
        slug="rental-foreclosure-recourse-vs-nonrecourse-debt",
        title="Rental Foreclosure: Recourse vs. Nonrecourse Debt",
        description="A foreclosed rental can trigger sale gain or loss and possibly cancellation-of-debt income. The loan's recourse status changes the calculation.",
        category="Real Estate Tax Planning",
        hub="rental",
        lead="A rental foreclosure is treated as a property disposition for federal tax purposes. With recourse debt, a separate cancellation-of-debt question may also arise; with nonrecourse debt, the unpaid debt is generally part of amount realized.",
        body="""
<h2>First determine who remained liable for the debt</h2>
<p>Recourse debt means the borrower is personally liable for the unpaid balance under the applicable documents and law. Nonrecourse debt generally limits the lender to the collateral. A loan's label is a starting point, not the complete answer: guarantees, modifications, state law, and deficiency rights matter. Obtain the note, guarantees, foreclosure notice, payoff calculation, and any deficiency waiver before preparing the return.</p>
<p>The property disposition is measured against adjusted basis, which includes appropriate capitalized costs and reflects depreciation allowed or allowable. A foreclosure can create gain even when the owner receives no cash. Suspended passive losses, at-risk rules, and prior depreciation may change the tax return consequences, so do not equate “I lost the property” with a tax loss.</p>
<h2>Two different calculations</h2>
<p>For nonrecourse debt, the full unpaid debt generally enters amount realized when the lender takes the property, even if it exceeds fair market value. There usually is no separate cancellation-of-debt income from that same discharge. For recourse debt, amount realized generally reflects the property's fair market value; the difference between the debt and that value can be cancellation-of-debt income if the lender forgives it. The COD amount may qualify for an exclusion, but exclusions have their own requirements and possible tax-attribute reductions.</p>
<h2>Illustrative comparison</h2>
<p>Assume adjusted rental basis is $400,000, unpaid debt is $500,000, and fair market value at foreclosure is $350,000. In a simplified nonrecourse case, the $500,000 debt can be the amount realized, producing $100,000 disposition gain. In a simplified recourse case, the $350,000 property value can produce a $50,000 disposition loss, while the remaining $150,000 of forgiven debt is analyzed separately as COD income. Transaction costs, other liabilities, debt terms, and loss limits can change an actual return.</p>
<h2>Do not overlook the tax forms</h2>
<p>A lender may issue Form 1099-A for acquisition or abandonment of secured property and Form 1099-C for cancelled debt. These are evidence to reconcile, not a substitute for the legal and basis analysis. Confirm the property's fair market value, outstanding principal, accrued interest treatment, and dates on the forms. If an insolvency or qualified real property business indebtedness exclusion may apply, evaluate the precise tests and Form 982 rather than omitting the income by assumption.</p>
<p>The <a href="/guides/rental-property-tax-questions/">rental tax hub</a> links to basis and loss guides. IRS <a href="https://www.irs.gov/publications/p4681">Publication 4681</a> explains foreclosures and debt cancellation, and <a href="https://www.irs.gov/publications/p544">Publication 544</a> covers property dispositions.</p>
""",
    ),
    dict(
        slug="suspended-rental-losses-death-basis-step-up",
        title="What Happens to Suspended Rental Losses at Death?",
        description="Suspended passive rental losses do not simply transfer to heirs. See how the basis increase can reduce the deduction on the decedent's final return.",
        category="Real Estate Tax Planning",
        hub="rental",
        lead="A decedent's suspended passive losses from a rental may become deductible on the final return only to the extent they exceed the increase in basis the heir receives. The losses do not simply move to the heir's tax return.",
        body="""
<h2>Why death differs from a taxable sale</h2>
<p>Rental losses can be suspended under the passive-activity rules for years when the owner lacks sufficient passive income or a qualifying exception. A fully taxable sale to an unrelated party has one release rule. Transfer at death has a different rule: the decedent's unused passive losses from the activity are allowed on the final return only to the extent they exceed the basis increase in the property transferred at death.</p>
<p>This rule prevents a double benefit where an heir takes a higher tax basis and the decedent also deducts all previously suspended losses. It is not a statement that every inherited property receives a full basis step-up; ownership structure, estate valuation, and other basis rules have to be established first. The estate and income tax workpapers should be reconciled rather than prepared independently.</p>
<h2>Illustrative calculation</h2>
<p>Suppose the owner has $90,000 of suspended passive rental losses attributable to a property, and the basis increase at death for that property is $65,000. In a simplified example, $25,000 may be allowed on the decedent's final return under this special rule; $65,000 is not carried to the heir. If the basis increase were $100,000, these particular suspended losses would not produce a final-return deduction through the death rule. Other passive activities and limits still require separate review.</p>
<h2>Trace losses by activity and owner</h2>
<p>Do not use a single portfolio loss total. Identify the relevant rental activity, any valid grouping elections, ownership percentage, prior-year Form 8582 carryforwards, and basis/at-risk limits. A passive loss that never passed the basis or at-risk limitation is not necessarily in the same category as a loss suspended solely under Section 469. Joint ownership, partnerships, and S corporations add pass-through schedules that need to be matched to the decedent's records.</p>
<h2>Coordinate the final return and heir basis</h2>
<p>Collect the decedent's depreciation schedules, prior Forms 8582, K-1s if relevant, deed and entity documents, date-of-death valuation, and estate tax filings. Determine the basis immediately before death and the heir's basis under the applicable rules. Show the basis increase and released loss calculation in a memo attached to the final-return file. An heir should separately establish their own depreciation starting point if the inherited property is held for rent.</p>
<p>Related reading: <a href="/blog/rental-property-inherited-basis/">inherited rental basis</a> and the <a href="/guides/rental-property-tax-questions/">rental tax hub</a>. IRS <a href="https://www.irs.gov/publications/p925">Publication 925</a> provides the death rule and an example; <a href="https://www.irs.gov/publications/p551">Publication 551</a> covers inherited property basis.</p>
""",
    ),
    dict(
        slug="consignment-inventory-tax-ownership",
        title="Who Owns Consignment Inventory for Tax Purposes?",
        description="Consigned goods usually stay in the consignor's inventory until sold. Learn how sellers and shops should reconcile stock, commissions, and revenue.",
        category="Business Tax Planning",
        hub="business",
        lead="Merchandise placed in another business's store is not automatically sold to that store. In a genuine consignment, the consignor generally retains inventory ownership until a customer buys the item.",
        body="""
<h2>Read the commercial terms before the ledger</h2>
<p>A consignment arrangement gives a shop possession of goods while the supplier retains ownership until sale. The agreement should say who sets prices, bears damage or return risk, insures the stock, can retrieve it, and owes payment only after a customer purchase. If the shop has an unconditional obligation to buy the goods, the arrangement may instead be a wholesale sale despite a “consignment” label.</p>
<p>For the consignor, goods still out on consignment generally remain in ending inventory. Shipping them to the shop is a movement of stock, not automatically revenue. When the shop sells to an end customer, the consignor records the sale under its tax accounting method and removes the related cost from inventory. The consignee generally excludes those goods from its own inventory and recognizes its commission or other fee under its accounting method.</p>
<h2>Reconcile the year-end stock count</h2>
<p>Ask each consignee for a statement showing beginning units, receipts, customer sales, returns, damaged units, and ending units. Tie this statement to serial numbers or SKUs in the supplier's inventory ledger. A physical count at the supplier's own warehouse omits stock held elsewhere; that omission can understate ending inventory and overstate cost of goods sold. The shop should likewise avoid reporting another owner's goods as purchased inventory.</p>
<h2>Illustrative transaction</h2>
<p>A maker delivers 100 lamps costing $80 each to a retailer. By year-end, 30 have sold and 70 remain in the retailer's stockroom. Under a genuine consignment, the maker's ending inventory still includes the 70 unsold lamps, or $5,600 at this simplified cost. The maker separately accounts for the 30 sales and their $2,400 cost. The retailer reports its earned commission, rather than taking all 100 lamps into purchased inventory. Actual revenue presentation depends on the contracts and accounting method.</p>
<h2>Returns, damage, and marketplaces</h2>
<p>Customer returns can reverse or adjust a prior sale; damaged stock may require separate valuation evidence. Online marketplaces may function as agents in some arrangements and purchasers in others. Payment processor deposits can be net of fees and refunds, so bank deposits alone do not prove gross sales. Keep the contracts, statements, payment reports, and shipping records together.</p>
<p>For adjacent reporting issues, use the <a href="/guides/business-tax-questions/">business tax hub</a> and <a href="/blog/reconcile-1099-k-gross-payments-to-tax-return/">1099-K reconciliation guide</a>. IRS <a href="https://www.irs.gov/publications/p334">Publication 334</a> specifically explains the inventory treatment of goods sent or received on consignment.</p>
""",
    ),
    dict(
        slug="reconcile-1099-k-gross-payments-to-tax-return",
        title="How to Reconcile 1099-K Gross Payments to Business Revenue",
        description="A Form 1099-K can exceed bank deposits and taxable sales. Build a reconciliation for fees, refunds, sales tax, transfers, and duplicate forms.",
        category="Business Tax Planning",
        hub="business",
        lead="Form 1099-K reports gross payment transactions, not automatically taxable profit or even the exact revenue line on a business return. A useful tax workpaper explains every material difference.",
        body="""
<h2>Begin with processor-level gross, not net deposits</h2>
<p>Payment processors can subtract fees, refunds, chargebacks, reserves, and other amounts before transferring cash to a bank. The Form 1099-K gross amount is generally unadjusted for these items. If a shop reports only bank deposits as sales, it may omit both revenue and separately deductible processing fees. Export the full transaction history, not just the monthly payout report.</p>
<p>Map each processor or marketplace to the entity and tax year that received the form. Then reconcile the reported gross to transaction-level customer charges. A marketplace may issue one form while another processor issues a second form on overlapping activity; avoid doubling sales. Conversely, a cash or check sale will not appear on Form 1099-K and still needs to be reported if taxable.</p>
<h2>Classify each adjustment</h2>
<p>Returns and refunds generally reduce the underlying sales amount under the business's accounting method. Merchant fees are usually separate expenses. Sales tax collected as an agent for a state is analyzed apart from the seller's revenue; whether a marketplace collected and remitted it matters. Tips, shipping charged to customers, deposits, and gift-card redemptions each need treatment based on the underlying transaction. A personal transfer mistakenly included on a business form should be documented as such, not silently netted against genuine sales.</p>
<h2>Illustrative bridge</h2>
<p>Suppose a processor reports $250,000 on Form 1099-K. Its annual statement shows $12,000 of refunds, $7,000 of processing fees, and $15,000 of sales tax collected for remittance. The processor deposits might be only $216,000. That does not mean revenue is automatically $216,000. A starting bridge is $250,000 gross less the $12,000 refunded sales and the $15,000 tax collected as agent, producing $223,000 of sales before other adjustments; the $7,000 fee is separately analyzed as an expense. Verify the processor's actual definitions before using these illustrative numbers.</p>
<h2>Make the workpaper reviewable</h2>
<p>For each 1099-K, store a copy, the processor annual report, payout reports, transaction export, refund/chargeback log, and sales-tax remittance report. Show the amount on the form, each reconciling category, and where it lands on the tax return. If the form names the wrong taxpayer or has an error, contact the issuer for correction and retain correspondence. A reconciliation helps answer an IRS matching notice without altering correct income to match an incorrect form.</p>
<p>See the <a href="/guides/business-tax-questions/">business topic hub</a> and <a href="/blog/consignment-inventory-tax-ownership/">consignment inventory guide</a>. The IRS's <a href="https://www.irs.gov/businesses/what-to-do-with-form-1099-k">Form 1099-K guidance</a> discusses gross amounts, adjustments, and incorrect forms.</p>
""",
    ),
    dict(
        slug="franchise-initial-fees-vs-royalties-tax-treatment",
        title="Initial Franchise Fees vs. Ongoing Royalties: Tax Treatment",
        description="Initial franchise rights and recurring royalties often have different tax timing. Learn what to separate before booking a franchise agreement.",
        category="Business Tax Planning",
        hub="business",
        lead="A franchise agreement can bundle the price of long-lived rights with recurring payments for ongoing use and services. The buyer should separate those components before deciding when costs are deductible.",
        body="""
<h2>Identify what the initial payment buys</h2>
<p>A payment to acquire a franchise, trademark, or trade name commonly creates a Section 197 intangible. A qualifying acquired Section 197 intangible is generally amortized over 180 months, beginning with the later of the month acquired or the month the trade or business begins. Paying the fee in cash does not by itself make it immediately deductible. The agreement may also include equipment, inventory, leasehold improvements, training, or preopening services that require their own analysis and allocation.</p>
<p>Do not assume every line described as an “initial fee” is an intangible. Read the contract, invoice schedules, and deliverables. Identify whether the payment is for a transferable right, an asset, a startup service, a refundable deposit, or a continuing obligation. A purchase-price allocation prepared after the fact without commercial support can be difficult to defend.</p>
<h2>Then examine recurring royalties</h2>
<p>Ongoing royalties based on sales or use of the franchise can often be ordinary business costs as the obligation arises, subject to the business's accounting method and the exact agreement. Fixed periodic payments that effectively finance an acquisition price may be treated differently. Marketing fund contributions, software subscriptions, rent, and required product purchases are separate costs even when the franchisor bills them together.</p>
<h2>Illustrative agreement</h2>
<p>A new operator pays $120,000 for franchise rights, $40,000 for equipment, $10,000 for opening inventory, and 6% of monthly gross sales as an ongoing royalty. In a simplified allocation, the franchise-right cost may be amortized under Section 197, equipment follows its own depreciation rules, inventory becomes cost of goods sold when sold, and the sales-based royalty is analyzed as a recurring operating charge. The result depends on the agreement and when the business actually begins operations.</p>
<h2>What changes on exit?</h2>
<p>A later sale of the franchise raises basis, accumulated amortization, and potential recapture or gain-character questions. Payments for noncompete agreements or customer relationships may be separate Section 197 assets in an acquisition. Keep the original allocation, amortization schedule, amendments, royalty statements, and any transfer approval fees. Without these, the seller may struggle to substantiate remaining basis.</p>
<p>For business acquisitions generally, see the <a href="/guides/business-tax-questions/">business tax hub</a> and <a href="/blog/business-purchase-price-allocation-assets/">asset purchase allocation guide</a>. IRS <a href="https://www.irs.gov/instructions/i4562">Form 4562 instructions</a> discuss Section 197 intangibles, including franchises, and their amortization.</p>
""",
    ),
    dict(
        slug="s-corp-midyear-shareholder-change-income-allocation",
        title="How an S Corp Allocates Income When Ownership Changes Midyear",
        description="A midyear S corporation share sale can allocate taxable income differently from cash distributions. Compare daily allocation with a closing-of-books election.",
        category="Business Tax Planning",
        hub="business",
        lead="When S corporation ownership changes during a tax year, shareholders cannot simply assign taxable income by when cash was distributed. The default allocation uses shares and days, unless a valid special election applies.",
        body="""
<h2>The default per-share, per-day rule</h2>
<p>An S corporation generally allocates its income, loss, deduction, and credit among shareholders on a per-share, per-day basis. If one owner sells stock midyear, each owner receives a Schedule K-1 share based on the days and shares held, even if most of the profit was earned before or after closing. Purchase agreements that promise the buyer “post-closing profits” do not themselves change the federal allocation rule.</p>
<p>Cash distributions follow a separate path. A shareholder can receive cash that differs from the income allocated on the K-1. Stock basis, distribution ordering, and possible accumulated C corporation earnings matter to the taxability of that cash. A buyer should therefore review both the income allocation and expected distributions before agreeing to a price adjustment.</p>
<h2>When a closing-of-books election may help</h2>
<p>For a qualifying disposition of a shareholder's entire interest, Section 1377 permits an election to treat the corporation's year as two separate tax years for allocation purposes. A qualifying disposition can include certain other ownership changes under applicable rules. The election has procedural and consent requirements, and the corporation must maintain books accurate enough to determine items in each period. It should be modeled before the return is filed, not improvised after K-1s are issued.</p>
<h2>Illustrative result</h2>
<p>Assume a corporation has one share outstanding and the seller transfers it to a buyer on July 1. The business earns $20,000 in the first half and $180,000 in the second half. Under the default method, the $200,000 annual income is allocated by days of ownership, roughly half to each owner. A valid closing-of-books election could instead allocate the actual $20,000 first-period result to the seller and $180,000 second-period result to the buyer, subject to the detailed rules. The difference is material even though the annual corporate income is identical.</p>
<h2>Transaction checklist</h2>
<p>Confirm the legal transfer date, share count, existing shareholder agreements, books through closing, prior K-1s, and any built-in gains or separately stated items. Make the tax allocation clause consistent with the chosen method and arrange for required consents. Reconcile payroll, distributions, and loans to the same cutoff. State tax treatment may differ from the federal K-1 allocation and deserves a separate check.</p>
<p>See the <a href="/guides/business-tax-questions/">business tax hub</a> and <a href="/blog/business-s-corp-distribution-basis/">S corporation distribution guide</a>. IRS <a href="https://www.irs.gov/instructions/i1120s">Form 1120-S instructions</a> explain shareholder allocations and elections.</p>
""",
    ),
    dict(
        slug="s-corp-accumulated-earnings-profits-distribution-order",
        title="S Corp Distributions With Old C Corp Earnings and Profits",
        description="An S corporation with accumulated C corporation earnings can distribute cash under special ordering rules. Learn why AAA and stock basis both matter.",
        category="Business Tax Planning",
        hub="business",
        lead="An S corporation that used to be a C corporation may still have accumulated earnings and profits. In that case, cash distributions can move through different tax buckets, including a potentially taxable dividend layer.",
        body="""
<h2>Locate the inherited C corporation balance</h2>
<p>Accumulated earnings and profits (E&P) is a tax account from C corporation years or certain acquisitions. It is not the same as retained earnings on financial statements. If the corporation has no accumulated E&P, the ordinary S corporation distribution and basis rules are generally the main issue. If it does, the ordering provisions under Section 1368 require a more detailed schedule.</p>
<p>The accumulated adjustments account (AAA) generally tracks S corporation income and loss adjustments relevant to the distribution order. It is not shareholder stock basis: AAA is a corporate account; basis is maintained separately for each shareholder. A corporation can have enough AAA for an ordering step while a particular shareholder has insufficient basis for the expected tax result.</p>
<h2>Apply the sequence, not the bank balance</h2>
<p>In general, a distribution from an S corporation with accumulated E&P is first treated under the AAA layer, then as a dividend to the extent of accumulated E&P, then under remaining stock-basis rules, with excess potentially gain. Special elections and certain negative balances can alter the computation. The accounting entry “distribution” does not identify which tax layer a payment came from.</p>
<h2>Illustrative schedule</h2>
<p>Assume the corporation has $40,000 of AAA available for the applicable distribution computation, $30,000 of accumulated E&P, and pays a single $80,000 distribution. A simplified ordering worksheet first considers $40,000 under the AAA layer, then up to $30,000 as a dividend, then the remaining $10,000 under stock-basis rules. Each shareholder's actual basis and the detailed allocation rules must be checked. The example shows why an $80,000 cash transfer need not have one tax character.</p>
<h2>Plan before declaring distributions</h2>
<p>Reconstruct historical C corporation E&P from prior returns and adjustments; do not substitute book retained earnings. Roll AAA forward from the last reliable Form 1120-S, separately track other adjustments, and update each shareholder's stock basis. Consider whether an election to distribute E&P first is available and desirable; it requires compliance with the Form 1120-S instructions and may affect shareholder tax. Coordinate distribution timing with the corporation's earnings, shareholder transactions, and state tax rules.</p>
<p>For related owner issues, see the <a href="/blog/business-s-corp-distribution-basis/">distribution and stock-basis guide</a> and the <a href="/guides/business-tax-questions/">business topic hub</a>. IRS <a href="https://www.irs.gov/instructions/i1120s">Form 1120-S instructions</a> explain AAA, accumulated E&P, and distribution reporting.</p>
""",
    ),
]

# Each guide has a different practical follow-through rather than a reused FAQ block.
FOLLOW_THROUGH = {
    "rental-purchase-seller-credits-basis": """
<h2>Questions to resolve before filing</h2>
<p>Was the concession fixed in the signed purchase agreement, negotiated after an inspection, or merely a lender-approved cap on buyer costs? Did the closing agent actually use the whole credit? A $10,000 permitted credit with only $7,000 of eligible charges is not the same transaction as a $10,000 price reduction. Review the final, not preliminary, settlement statement and trace unused amounts. If the seller paid a buyer obligation directly outside escrow, retain proof of payment and describe why that payment was made.</p>
<p>Also compare the appraisal's land/building percentages to local assessment data and the contract's allocation. An unsupported allocation can inflate depreciation even when the total property basis is right. If a seller funds a post-closing escrow for repairs, document who owns the escrow and when funds are released. That arrangement may differ from a concession delivered at closing, and the later invoices still need independent classification.</p>
""",
    "rental-lease-up-costs-before-first-tenant": """
<h2>Advertising is evidence, but actual availability matters</h2>
<p>A listing dated June 1 may show intent, yet the property may not be ready until later if contractors still control the premises or the owner cannot lawfully lease it. Conversely, a property can be available without a tenant application if it is habitable, priced, and actively offered. Record the first date the property could have been occupied under a normal lease, then explain any later change in status. If the owner pauses marketing for a renovation, document that pause and revisit the cost treatment during the project.</p>
<p>Mixed-use expenses deserve their own allocation. If the owner stays in the home while preparing it, utilities and cleaning cannot all be treated as rental expenses merely because a listing exists. If a newly purchased duplex has one rentable unit and one undergoing reconstruction, consider whether the units have different ready dates and whether shared costs can be reasonably allocated. This is more precise than assigning one date to the entire parcel.</p>
""",
    "1031-exchange-debt-relief-boot": """
<h2>Model the exchange before choosing replacement financing</h2>
<p>A lender may offer an attractive smaller loan on replacement property. That commercial choice can affect the exchange's recognized gain if the seller's old debt was larger. Prepare a sources-and-uses schedule with sale proceeds, debt payoff, exchange costs, cash added, new debt, and any cash withdrawn. Update the schedule when purchase prices or loans change. A last-minute reduction in replacement debt may create a different outcome from the exchange model approved weeks earlier.</p>
<p>Do not use a slogan such as “trade up in value and debt” as the filed tax calculation. It is a planning screen, not a substitute for analyzing liabilities, cash, and all property received. A zero-cash distribution from the intermediary can still leave debt-relief boot. Equally, a lower replacement mortgage does not prove boot without considering other qualifying consideration the exchanger provided. Ask the intermediary for a final accounting and reconcile it to both title-company statements.</p>
""",
    "rental-foreclosure-recourse-vs-nonrecourse-debt": """
<h2>Separate economic loss from tax character</h2>
<p>A property purchased for $600,000 may have an adjusted basis far below that amount after years of depreciation. This can produce tax gain at foreclosure despite a steep fall in market value. A recourse case can also have a property loss and ordinary cancellation-of-debt income in the same year; those amounts are not automatically netted into one capital loss. A reviewer should determine disposition character, passive-loss effects, and COD exclusions in the correct order.</p>
<p>Timing also matters. The foreclosure or deed-transfer date may differ from the date the lender later cancels a deficiency balance. If the owner negotiates a short sale or deed in lieu, read the settlement and release documents to see which obligations ended and when. Retain evidence of fair market value at transfer, such as an appraisal or broker analysis, because a lender form can use an amount that needs investigation.</p>
""",
    "suspended-rental-losses-death-basis-step-up": """
<h2>Pay special attention to pass-through ownership</h2>
<p>If a partnership owns the rental, the decedent transfers a partnership interest, not a direct deed in the building. Outside basis, inside basis, any Section 754 election, and the value of the inherited interest can affect the analysis. The partnership's final K-1 for the decedent and the successor's first K-1 should be coordinated. An inherited interest with debt allocations requires particular care because liabilities can change partner basis without changing property value in the same way.</p>
<p>For direct ownership, a valuation dated near death and a complete depreciation history help establish both the basis increase and the final-return loss release. The preparer should preserve a schedule showing which suspended losses were used against passive income before applying the death rule. If several rentals were grouped as one activity under a valid election, retain the original election and consistently apply that activity definition. Without that history, the final-return deduction can be overstated or missed.</p>
""",
    "consignment-inventory-tax-ownership": """
<h2>Define the shop's role in the contract</h2>
<p>Some arrangements give the retailer discretion to mark down goods, but that fact alone does not answer ownership. Read the payment clause: must the retailer pay for all goods delivered, or only for goods sold to customers? Can the maker demand return of unsold stock? Who bears theft and shrinkage? Those terms help distinguish a consignment from a completed sale on credit. If the parties changed their practice without amending the contract, keep emails and settlement statements showing what actually happened.</p>
<p>At year-end, the maker and retailer should agree on a stock confirmation. Differences between the physical count and the maker's ledger should be investigated rather than forced into cost of goods sold. A damaged or missing item may represent a claim against the retailer, an insurance recovery, or an inventory loss depending on the facts. The commission statement should show customer price, sales tax, refunds, the shop's commission, and the net remittance so both businesses can report consistently.</p>
""",
    "reconcile-1099-k-gross-payments-to-tax-return": """
<h2>One transaction can appear in multiple systems</h2>
<p>A restaurant may book a delivery-platform sale in its point-of-sale system while the platform also reports a 1099-K. The 1099-K is a reporting form, not an additional sale to add to the point-of-sale total. Match transactions using order IDs, dates, and gross charges. Likewise, transfers between the owner's own accounts should be identified with both sides of the transfer. Summing bank deposits, POS sales, and 1099-K amounts is a common way to count the same revenue twice.</p>
<p>Make a separate column for unresolved differences. Small timing differences around December 31 may arise when a payment is processed on one date and paid out on another. A material unmatched balance should lead to a transaction-level investigation, not an arbitrary “1099-K adjustment.” Keep the bridge with the return for future years; a consistent method makes it easier to spot a processor changing its gross-reporting definition.</p>
""",
    "franchise-initial-fees-vs-royalties-tax-treatment": """
<h2>Look for embedded financing and preopening costs</h2>
<p>An agreement may let the franchisee pay an initial fee in installments. The payment schedule does not necessarily change when the intangible was acquired; it may create a payable and interest component. Conversely, a contingent fee calculated solely on future sales can have different treatment from a fixed acquisition price. A tax workpaper should identify the right acquired, the date operations began, the stated principal, and any financing terms.</p>
<p>Training and launch support should be documented by deliverable. Some services occur before the business opens and may fall under startup rules; others may be part of the franchise acquisition or ordinary operating services. Required remodeling is analyzed as a physical asset, even if the franchisor manages the construction. Ask for an itemized franchisor invoice or build an allocation supported by the contract and independent costs. Avoid treating every charge on the opening statement as a 15-year intangible.</p>
""",
    "s-corp-midyear-shareholder-change-income-allocation": """
<h2>Coordinate purchase agreement economics with the tax method</h2>
<p>Stock purchase agreements often include a tax distribution, estimated-tax reimbursement, or working-capital adjustment. These clauses can shift cash between buyer and seller, but they do not replace the K-1 allocation rules. If the parties expect the seller to bear only preclosing tax, the agreement should say whether a closing-of-books election will be pursued and who must consent. If the election is unavailable or not made, model a cash true-up using the default per-day allocation.</p>
<p>Separately stated items matter too. A capital gain on a corporate asset sale, charitable contribution, or credit can affect shareholders differently from ordinary income. The corporation should close its books through the transfer date if it intends to use an actual-period allocation and verify that the transfer qualifies. State pass-through entity tax elections and estimated payments can add a second layer of allocation that should be reconciled before issuing final K-1s.</p>
""",
    "s-corp-accumulated-earnings-profits-distribution-order": """
<h2>Reconstruct old tax accounts before paying cash</h2>
<p>A company that elected S status years ago may have lost the workpapers supporting its final C corporation E&P. Start with the historical Form 1120 returns, Schedule M-1 adjustments, distributions, and any acquisitions that brought E&P into the corporation. An accountant may need to reconstruct a tax E&P balance rather than copying the retained-earnings line from QuickBooks. The balance can affect both shareholder tax and corporate rules for passive investment income.</p>
<p>Prepare a distribution ledger by date and shareholder. The year's income and loss items, AAA, any elections, and individual stock bases must be updated consistently. If the company has multiple shareholders, a payment to one owner cannot be classified by looking only at that owner's bank receipt. Board approvals and shareholder consents should match the tax workpaper. Before an extraordinary distribution, compare the projected dividend layer with the owners' tax positions and cash needs.</p>
""",
}

ADDITIONAL_DETAIL = {
    "rental-foreclosure-recourse-vs-nonrecourse-debt": "The debt's tax basis can also differ from the statement balance if it includes unpaid interest or fees. Interest that would have been deductible if paid may receive separate treatment when forgiven. Ask for a transaction-level lender ledger rather than using only the headline 1099-C amount. This matters most when the lender capitalized fees or the borrower made payments after default.",
    "consignment-inventory-tax-ownership": "For high-value items, the parties can add a periodic signed inventory confirmation and photographs to their routine reporting. The maker should reconcile goods shipped to goods sold, returned, or still held. The retailer should reconcile sales proceeds to commissions and remittances. These two independent reconciliations help identify missing goods and keep ownership, revenue, and cost of goods sold aligned.",
    "reconcile-1099-k-gross-payments-to-tax-return": "If an incorrect form cannot be corrected before filing, report the underlying transactions correctly and preserve a clear explanation of the difference. Do not invent an offsetting business expense solely to force the return to match the information return. A documented reconciliation is more useful if an automated IRS notice arrives later, especially where the form included personal transfers or duplicated processor activity.",
    "franchise-initial-fees-vs-royalties-tax-treatment": "A franchise's renewal payment may buy an extension of rights rather than ordinary monthly service, so review renewals separately from royalties. If the franchisee buys an existing unit from another owner, goodwill and customer relationships may also enter the acquisition allocation. The purchase agreement and Form 8594, when applicable, should be consistent with the buyer's asset schedules and the seller's reported allocation.",
    "s-corp-midyear-shareholder-change-income-allocation": "The transfer date needs more than a signed term sheet. Inspect the stock ledger, closing documents, payment conditions, and any escrow or delayed-transfer terms. A one-day difference may be small for ordinary income but material if the corporation recognizes a large transaction on that day. Preserve the ownership-by-day schedule used to produce each K-1 so the allocation can be explained later.",
    "s-corp-accumulated-earnings-profits-distribution-order": "If a corporation has made S elections, revocations, or acquisitions over time, its tax accounts may have discontinuities that ordinary bookkeeping will not show. Map the corporate timeline before using an old AAA schedule. A dividend layer can also affect the shareholder's qualified-dividend reporting, subject to applicable requirements. The company should identify that layer on the shareholder reporting rather than relying on the owner to infer it from a cash transfer.",
}

HUBS = {
    "rental": ROOT / "guides/rental-property-tax-questions/index.html",
    "business": ROOT / "guides/business-tax-questions/index.html",
}


def update_hub(kind):
    path = HUBS[kind]
    page = path.read_text()
    start = "<!-- deep-tax-guides:start -->"
    end = "<!-- deep-tax-guides:end -->"
    entries = [a for a in ARTICLES if a["hub"] == kind]
    rows = "\n".join(
        f'<li><a href="/blog/{a["slug"]}/">{a["title"]}</a><br>{a["description"]}</li>'
        for a in entries
    )
    block = f'{start}\n<section class="content-section"><div class="container narrow"><h2>Detailed tax decision guides</h2><ul class="related-links">{rows}</ul></div></section>\n{end}'
    if start in page:
        page = re.sub(re.escape(start) + r".*?" + re.escape(end), block, page, flags=re.S)
    else:
        page = page.replace("    </main>", block + "\n    </main>", 1)
    path.write_text(page)


def update_sitemap(name):
    path = ROOT / name
    xml = path.read_text()
    for article in ARTICLES:
        url = f'https://www.aetaxadvisors.com/blog/{article["slug"]}/'
        if url not in xml:
            xml = xml.replace("</urlset>", f"<url><loc>{url}</loc><lastmod>{DATE}</lastmod></url>\n</urlset>")
    ET.fromstring(xml)
    path.write_text(xml)


def main():
    for a in ARTICLES:
        post = {**a, "h1": a["title"], "breadcrumb": a["title"], "date": DATE,
                "date_display": "September 22, 2026",
                "cta_head": "Need a transaction-specific tax review?",
                "cta_text": "We can review the documents, basis, and reporting choices for your situation.",
                "related": [(f'/guides/{"rental-property" if a["hub"] == "rental" else "business"}-tax-questions/', "Explore the topic hub")]}
        post["body"] = a["body"] + FOLLOW_THROUGH[a["slug"]]
        if a["slug"] in ADDITIONAL_DETAIL:
            post["body"] += "<p>" + ADDITIONAL_DETAIL[a["slug"]] + "</p>\n"
        seo_render.write_post(post, ROOT)
    for kind in HUBS:
        update_hub(kind)
    for sitemap in ("sitemap.xml", "sitemap-blog.xml"):
        update_sitemap(sitemap)
    print(f"Generated {len(ARTICLES)} deep guides and updated two hubs and two sitemaps")


if __name__ == "__main__":
    main()
