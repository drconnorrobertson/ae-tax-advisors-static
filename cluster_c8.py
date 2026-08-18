#!/usr/bin/env python3
"""Cluster 8: Exit and succession tax planning.

The buyer here is an owner who is one to five years from selling, passing the
business to family, or restructuring ahead of either. The tax outcome of that
event is decided long before the letter of intent, which is why this cluster
is organised around the sequence of decisions rather than a list of strategies.
"""

from __future__ import annotations

from cluster_common import Cluster, Spoke

P = "exit-tax-planning-business-owners"

QSBS = Spoke(
    slug="qsbs-exclusion-section-1202",
    label="QSBS: excluding capital gain under Section 1202",
    title="QSBS Exclusion: Exclude Up to $10M in Capital Gains (Section 1202)",
    description=(
        "How qualified small business stock works, the five tests the stock has to "
        "pass, the holding period, what the 2025 law changed, and how the per-issuer "
        "cap gets multiplied with non-grantor trusts."
    ),
    h1="QSBS Exclusion: How to Exclude Up to $10M in Capital Gains Under Section 1202",
    subtitle=(
        "The single largest exclusion available to a business owner on a sale, and "
        "the one with the most ways to fail a test years before the exit."
    ),
    lead=(
        "The qualified small business stock exclusion under Internal Revenue Code Section 1202 "
        "allows an individual to exclude the greater of $10 million or 10 times basis of gain on "
        "the sale of stock in a qualifying domestic C corporation held more than five years. For "
        "stock issued after July 4, 2025, the 2025 tax act raised that per-issuer ceiling to $15 "
        "million and added a partial exclusion at three and four years. The exclusion is not "
        "elective and not retroactive: the stock either satisfied every test at issuance and "
        "throughout the holding period, or it did not."
    ),
    keywords=[
        "qsbs exclusion",
        "section 1202 qualified small business stock",
        "exclude capital gains business sale",
        "qsbs stacking trusts",
    ],
    body=[
        (
            "What Section 1202 Actually Does",
            "<p>Section 1202 excludes gain from federal income tax entirely. It is not a "
            "deferral and not a rate reduction. Gain that qualifies is never taxed, is not "
            "subject to the 3.8 percent net investment income tax, and for stock acquired "
            "after September 27, 2010 carries no alternative minimum tax preference.</p>"
            "<p>The ceiling applies per taxpayer, per issuing corporation. An owner with "
            "qualifying stock in two unrelated companies has a separate cap for each. That per "
            "taxpayer framing is what makes the planning in the trust section below possible, "
            "and it is the difference between excluding $10 million and excluding $40 million on "
            "the same sale.</p>"
            "<p>State treatment is separate. Most states follow the federal exclusion, several "
            "modify it, and a small number disallow it outright. The state answer has to be "
            "checked against the state of residence at the time of sale, which is itself a "
            "planning variable when a move is already under consideration.</p>"
        ),
        (
            "The Five Tests the Stock Has to Pass",
            "<p>All five apply. Failing any one disqualifies the entire position.</p>"
            "<p><strong>1. Domestic C corporation.</strong> The issuer must be a C corporation "
            "for substantially all of the holding period. S corporation stock never qualifies, "
            "and neither does an LLC interest or partnership interest.</p>"
            "<p><strong>2. Original issuance.</strong> The stock must be acquired directly from "
            "the corporation for money, property, or services. Stock bought from another "
            "shareholder does not qualify, though stock received by gift or inheritance can "
            "carry the original holder's status forward.</p>"
            "<p><strong>3. The gross assets test.</strong> The corporation's aggregate gross "
            "assets must not have exceeded $50 million at any point before, and immediately "
            "after, the stock was issued. The 2025 act raised this to $75 million for stock "
            "issued after July 4, 2025. Assets are measured at adjusted basis, not fair market "
            "value, with contributed property measured at fair market value on contribution.</p>"
            "<p><strong>4. The active business test.</strong> At least 80 percent of assets by "
            "value must be used in the active conduct of a qualified trade or business "
            "throughout substantially all of the holding period. Cash and investments held "
            "beyond reasonable working capital needs count against this, which is why a company "
            "that accumulates a large investment portfolio can fail the test in the years before "
            "a sale without anyone noticing.</p>"
            "<p><strong>5. The holding period.</strong> More than five years, running from "
            "issuance.</p>"
        ),
        (
            "What the 2025 Law Changed",
            "<p>The changes apply to stock issued after July 4, 2025. Stock issued on or before "
            "that date keeps the prior rules in full, which means many owners now hold two "
            "tranches governed by different regimes.</p>"
            "<div style=\"overflow-x:auto;\">"
            "<table>"
            "<thead><tr><th>Provision</th><th>Stock issued on or before 7/4/2025</th>"
            "<th>Stock issued after 7/4/2025</th></tr></thead>"
            "<tbody>"
            "<tr><td>Per-issuer cap</td><td>$10 million or 10x basis</td>"
            "<td>$15 million or 10x basis, indexed from 2027</td></tr>"
            "<tr><td>Gross assets ceiling</td><td>$50 million</td><td>$75 million</td></tr>"
            "<tr><td>Held 3 years</td><td>No exclusion</td><td>50 percent excluded</td></tr>"
            "<tr><td>Held 4 years</td><td>No exclusion</td><td>75 percent excluded</td></tr>"
            "<tr><td>Held 5 years or more</td><td>100 percent excluded</td>"
            "<td>100 percent excluded</td></tr>"
            "</tbody></table></div>"
            "<p>The tiered exclusion is the practical change. Under the old rules an owner who "
            "sold at four years and eleven months received nothing. Under the new rules the same "
            "sale excludes 75 percent of the gain, which changes how hard a seller should push "
            "to delay a closing.</p>"
        ),
        (
            "Which Businesses Qualify, and Which Are Excluded by Name",
            "<p>The statute excludes several categories outright, regardless of size or "
            "structure: health, law, engineering, architecture, accounting, actuarial science, "
            "performing arts, consulting, athletics, financial services, and brokerage services, "
            "where the principal asset is the reputation or skill of one or more employees. Also "
            "excluded are banking and insurance, farming, businesses eligible for percentage "
            "depletion, and any hotel, motel, or restaurant.</p>"
            "<p>That list eliminates a meaningful share of professional service firms, which is "
            "why Section 1202 rarely drives the plan for a medical or legal practice. Software, "
            "manufacturing, distribution, consumer products, technology services, and most "
            "product businesses do qualify.</p>"
            "<p>The line is not always obvious. A business that sells a technology product but "
            "delivers substantial implementation services can look like consulting on one set of "
            "facts and a product company on another. Where the answer is close, the file should "
            "document why the principal asset is the product rather than the people, and that "
            "documentation is far easier to assemble at issuance than during diligence.</p>"
        ),
        (
            "The S Corporation Problem",
            "<p>Most profitable owner-operated businesses are S corporations, and S corporation "
            "stock is permanently outside Section 1202. This is the most common reason the "
            "exclusion is unavailable to exactly the owner who would benefit most.</p>"
            "<p>Converting an S corporation to a C corporation starts a new five-year clock, and "
            "the basis of the stock deemed issued on conversion is the fair market value of the "
            "assets at that date. Only appreciation after the conversion is eligible. An owner "
            "converting a business already worth $12 million excludes nothing on that $12 "
            "million and starts qualifying only on growth from there.</p>"
            "<p>The conversion also means the corporation pays 21 percent on its earnings, and "
            "distributions are taxed again as dividends. That cost is real and recurring, so the "
            "conversion only makes sense where the expected exclusion outweighs several years of "
            "double taxation. Working that comparison is the reason the entity decision belongs "
            "in a model rather than a rule of thumb. Our "
            "<a href=\"/entity-structuring-business-owners/\">entity structuring guide</a> covers "
            "the same trade-off from the operating side.</p>"
        ),
        (
            "Stacking and Packing: Multiplying the Cap",
            "<p>Because the cap is per taxpayer, giving shares to additional taxpayers before a "
            "sale multiplies it. Two techniques do this.</p>"
            "<p><strong>Stacking</strong> transfers shares to non-grantor trusts, each of which "
            "is a separate taxpayer with its own exclusion. A founder with $60 million of "
            "qualifying gain and a $15 million cap might gift shares to three irrevocable "
            "non-grantor trusts for children, producing four caps and excluding the full "
            "amount. The trusts must be genuinely non-grantor, funded well before any binding "
            "agreement, and drafted with different beneficiaries to avoid being treated as a "
            "single trust under the multiple trust rules.</p>"
            "<p><strong>Packing</strong> uses the 10 times basis alternative. A shareholder who "
            "contributes appreciated property to the corporation in exchange for stock takes a "
            "Section 1202 basis equal to the property's fair market value, so a $5 million "
            "contribution supports $50 million of excluded gain rather than $15 million.</p>"
            "<p>Both require lead time. Gifts made after a letter of intent is signed invite an "
            "assignment of income argument, and gifts made in the same year as a sale face a "
            "valuation that is hard to discount when the sale price is already known. Two years "
            "of separation is comfortable, one year is workable, and thirty days is not.</p>"
        ),
        (
            "What It Is Worth",
            "<p>Consider a founder selling qualifying stock for $18 million with a basis near "
            "zero, resident in a state that follows the federal exclusion.</p>"
            "<div style=\"overflow-x:auto;\">"
            "<table>"
            "<thead><tr><th>Scenario</th><th>Taxable gain</th><th>Federal tax at 23.8 percent</th></tr></thead>"
            "<tbody>"
            "<tr><td>No QSBS</td><td>$18,000,000</td><td>$4,284,000</td></tr>"
            "<tr><td>QSBS, one $15M cap</td><td>$3,000,000</td><td>$714,000</td></tr>"
            "<tr><td>QSBS stacked across four taxpayers</td><td>$0</td><td>$0</td></tr>"
            "</tbody></table></div>"
            "<p>The gap between the second and third rows is entirely a function of work done "
            "years earlier. Nothing about the sale itself changes. This is the clearest example "
            "on the site of why exit planning has to start before the exit is on the calendar, "
            "and it is covered in sequence in the "
            "<a href=\"/exit-tax-planning-business-owners/\">exit tax planning guide</a>.</p>"
        ),
    ],
    takeaways=[
        "Section 1202 excludes gain permanently, with no net investment income tax and no AMT preference.",
        "S corporation stock never qualifies, and converting starts a new five-year clock at current value.",
        "Stock issued after July 4, 2025 gets a $15 million cap and partial exclusions at three and four years.",
        "Health, law, accounting, consulting, financial services, and restaurants are excluded by statute.",
        "The cap is per taxpayer, so non-grantor trusts funded well before a sale multiply it.",
        "Every test is evaluated at issuance and across the holding period, not at closing.",
    ],
    faqs=[
        (
            "Can I get QSBS treatment if my company is an LLC or S corporation?",
            "<p>Not on the interest you hold now. Section 1202 applies only to stock in a "
            "domestic C corporation. An LLC can convert to a C corporation and issue qualifying "
            "stock, but the five-year clock starts at conversion and only appreciation after "
            "that date is eligible, because basis is set at the fair market value of the "
            "contributed assets.</p>",
        ),
        (
            "What happens if I sell before five years?",
            "<p>For stock issued after July 4, 2025, a sale at three years excludes 50 percent "
            "of the gain and at four years excludes 75 percent. For older stock, a sale before "
            "five years excludes nothing. In either case a Section 1045 rollover can preserve "
            "the position by reinvesting the proceeds in other qualified small business stock "
            "within 60 days, with the original holding period carrying over.</p>",
        ),
        (
            "Does the exclusion apply to an asset sale?",
            "<p>No. Section 1202 applies to the sale of stock. If the buyer insists on buying "
            "assets, the corporation recognizes the gain and the exclusion is lost, which is "
            "one of the few situations where a seller should hold firm on structure. See "
            "<a href=\"/structuring-your-business-for-sale/\">how to structure your business for "
            "sale</a> for how that negotiation usually resolves.</p>",
        ),
        (
            "How many trusts can I use to stack the exclusion?",
            "<p>There is no statutory limit, but each trust must be a separate taxpayer with a "
            "genuine, distinct beneficial interest and its own purpose. Trusts created on the "
            "same day with the same terms and the same beneficiary invite consolidation under "
            "the multiple trust rules. In practice three to five trusts with different primary "
            "beneficiaries is a defensible structure and ten identical ones is not.</p>",
        ),
        (
            "Do I need to do anything to claim the exclusion?",
            "<p>It is reported on the return in the year of sale, but the substantiation is "
            "built over the life of the company: the issuance documents, the gross assets "
            "calculation at each issuance, and evidence the active business test was met "
            "throughout. Companies that never assembled that file end up reconstructing it under "
            "diligence pressure, and buyers price the uncertainty.</p>",
        ),
    ],
)

INSTALLMENT = Spoke(
    slug="installment-sale-tax-strategy",
    label="Installment sales: spreading the gain over years",
    title="Installment Sales: Spread Capital Gains Tax Over Multiple Years",
    description=(
        "How Section 453 installment reporting works, the interest charge above $5 "
        "million, related party limits, what cannot be reported on the installment "
        "method, and when a lump sum is the better answer."
    ),
    h1="Installment Sales: How to Spread Capital Gains Tax Over Multiple Years",
    subtitle=(
        "The oldest deferral in the code, and still the most useful one for a seller "
        "who does not need all the cash at closing."
    ),
    lead=(
        "An installment sale under Internal Revenue Code Section 453 lets a seller who receives "
        "at least one payment after the year of sale report gain proportionally as principal is "
        "collected, rather than all at once in the year of closing. The result is that a "
        "$4 million gain collected over five years is taxed in five pieces, which can hold the "
        "seller in lower brackets, reduce or avoid the net investment income tax in some years, "
        "and keep the deferred tax invested in the meantime. The method applies automatically "
        "unless the seller elects out."
    ),
    keywords=[
        "installment sale tax",
        "irc 453 installment method",
        "spread capital gains over years",
        "453a interest charge",
    ],
    body=[
        (
            "How the Gross Profit Ratio Works",
            "<p>The mechanics are simple arithmetic. Divide the gross profit by the total "
            "contract price to get the gross profit percentage, then apply that percentage to "
            "each principal payment received. The rest of each payment is a tax-free return of "
            "basis. Interest on the note is reported separately as ordinary income.</p>"
            "<p>A business sold for $5,000,000 with a basis of $1,000,000 has $4,000,000 of "
            "gross profit and an 80 percent gross profit ratio. Every dollar of principal "
            "collected carries 80 cents of gain.</p>"
            "<div style=\"overflow-x:auto;\">"
            "<table>"
            "<thead><tr><th>Year</th><th>Principal received</th><th>Gain recognized</th>"
            "<th>Basis recovered</th></tr></thead>"
            "<tbody>"
            "<tr><td>Closing</td><td>$1,500,000</td><td>$1,200,000</td><td>$300,000</td></tr>"
            "<tr><td>Year 2</td><td>$875,000</td><td>$700,000</td><td>$175,000</td></tr>"
            "<tr><td>Year 3</td><td>$875,000</td><td>$700,000</td><td>$175,000</td></tr>"
            "<tr><td>Year 4</td><td>$875,000</td><td>$700,000</td><td>$175,000</td></tr>"
            "<tr><td>Year 5</td><td>$875,000</td><td>$700,000</td><td>$175,000</td></tr>"
            "</tbody></table></div>"
            "<p>Reporting happens on Form 6252 each year until the note is retired. The gross "
            "profit ratio is fixed at the sale and does not change as payments come in, even if "
            "the note is later renegotiated.</p>"
        ),
        (
            "What Cannot Be Reported on the Installment Method",
            "<p>Several categories are carved out, and they are the reason a seller almost never "
            "defers the entire gain.</p>"
            "<p><strong>Depreciation recapture.</strong> Section 453(i) requires all Section "
            "1245 recapture, and Section 1250 recapture, to be recognized in the year of sale "
            "even if no cash is received. A seller with heavily depreciated equipment can owe "
            "ordinary income tax at closing on income they will not collect for years, which is "
            "a cash flow problem that has to be modeled before the structure is agreed.</p>"
            "<p><strong>Inventory and dealer property.</strong> Inventory, and property held by "
            "a dealer for sale to customers, are excluded outright.</p>"
            "<p><strong>Publicly traded securities.</strong> Excluded, which matters when part "
            "of the consideration is stock in a listed acquirer.</p>"
            "<p><strong>Accounts receivable in a cash basis business.</strong> These generate "
            "ordinary income as collected rather than installment gain.</p>"
            "<p>In a typical asset sale the allocation to equipment, receivables, and "
            "non-competition agreements produces immediate income while goodwill and going "
            "concern value carry the deferral. The purchase price allocation therefore does more "
            "than set the character of the gain, it sets how much of it can be deferred at all. "
            "That interaction is covered in "
            "<a href=\"/structuring-your-business-for-sale/\">structuring your business for "
            "sale</a>.</p>"
        ),
        (
            "The Section 453A Interest Charge Above $5 Million",
            "<p>Deferral is not free above a threshold. If the face amount of installment "
            "obligations a taxpayer holds at year end exceeds $5,000,000, and the individual "
            "sale price exceeded $150,000, Section 453A imposes an interest charge on the "
            "deferred tax attributable to the excess. The charge is computed at the underpayment "
            "rate and reported annually.</p>"
            "<p>It is not punitive, and it does not eliminate the benefit. It converts an "
            "interest-free deferral into a borrowing at roughly the federal underpayment rate, "
            "which is still attractive if the seller earns more than that on the money. What it "
            "does mean is that the analysis changes above $5 million of outstanding notes, and "
            "an owner comparing structures needs the after-charge number rather than the "
            "headline deferral.</p>"
            "<p>The related pledging rule in Section 453A(d) is easier to trip. Using the "
            "installment obligation as security for a loan is treated as receiving payment on "
            "the note, accelerating the gain to the extent of the loan proceeds. A seller who "
            "borrows against the note to fund something else has effectively cashed it in.</p>"
        ),
        (
            "Related Party Rules",
            "<p>Two provisions limit sales within a family or controlled group.</p>"
            "<p><strong>The two-year resale rule.</strong> Under Section 453(e), if a related "
            "buyer resells the property within two years, the original seller must accelerate "
            "gain as though they had received the resale proceeds. The rule exists to stop a "
            "family from converting a taxable sale into a deferred one while the cash leaves the "
            "group immediately.</p>"
            "<p><strong>Depreciable property.</strong> Section 453(g) denies the installment "
            "method entirely on a sale of depreciable property to a controlled entity unless the "
            "taxpayer establishes that tax avoidance was not a principal purpose.</p>"
            "<p>Neither rule prevents intrafamily installment sales, and they remain a standard "
            "succession tool. They do mean the structure has to be documented as a real sale at "
            "a defensible price with a note that is actually serviced, which is the same "
            "discipline required for the "
            "<a href=\"/estate-freeze-strategies-business-owners/\">estate freeze techniques</a> "
            "that use intentionally defective grantor trusts.</p>"
        ),
        (
            "When Spreading the Gain Actually Wins",
            "<p>Four situations where the installment method produces a materially better "
            "outcome than a lump sum.</p>"
            "<p><strong>Bracket and surtax management.</strong> A single-year $4 million gain "
            "sits entirely at the top capital gain rate plus the 3.8 percent net investment "
            "income tax. Spread across five years, part of each year's gain can land in the "
            "lower capital gain brackets, and in a year with modest other income the surtax "
            "exposure is smaller.</p>"
            "<p><strong>A pending state residency change.</strong> Gain recognized after "
            "establishing residence in a state with no income tax is generally not taxed by that "
            "state, though the former state may assert source rules on business income. This "
            "requires real planning rather than a change of address, but the difference on a "
            "$4 million gain in a 9 percent state is $360,000.</p>"
            "<p><strong>Offsetting losses arriving later.</strong> An owner with suspended "
            "passive losses, a cost segregation study planned on a replacement property, or "
            "capital loss carryforwards can time recognition against them.</p>"
            "<p><strong>Deal certainty.</strong> Sometimes the buyer simply cannot pay cash, and "
            "the choice is an installment note or no transaction at the agreed price. The tax "
            "treatment is then a benefit of a decision made for other reasons, which is the "
            "subject of "
            "<a href=\"/seller-financing-tax-strategy/\">seller financing as a strategy</a>.</p>"
        ),
        (
            "When to Elect Out",
            "<p>A seller can elect out of the installment method and report the entire gain in "
            "the year of sale. The election is made on a timely filed return and is difficult to "
            "revoke, so it deserves an actual calculation rather than a default.</p>"
            "<p>Electing out is usually right when rates are expected to rise, when the seller "
            "has expiring losses or credits that can absorb the gain now, when the outstanding "
            "note balance would push past the $5 million interest charge threshold with little "
            "offsetting benefit, or when the seller wants a clean basis position before making a "
            "large charitable gift.</p>"
            "<p>It is also worth remembering the credit risk. Deferring tax on money that is "
            "never collected is a poor trade. A note secured only by the business being sold, "
            "held by a buyer with thin equity, carries a real chance of default, and the tax "
            "consequences of repossession are their own project.</p>"
        ),
        (
            "State Tax, Residency, and the Note",
            "<p>State treatment is where installment planning either produces a large additional "
            "saving or an unpleasant surprise. Most states tax gain as it is recognized, so a "
            "seller who moves to a state with no income tax before the later payments arrive "
            "often escapes state tax on that portion. Several states, however, apply source "
            "rules to gain from a business that operated within their borders, and a few "
            "accelerate the entire gain when a taxpayer ceases residency.</p>"
            "<p>The planning is real but it is not a mailing address. Establishing residency "
            "means moving the center of the taxpayer's life: home, family, licenses, voter "
            "registration, professional affiliations, and days counted. High-tax states audit "
            "these changes aggressively, particularly where the departure coincides with a "
            "liquidity event, and the burden of proof sits with the taxpayer.</p>"
            "<p>A related question is what happens if the seller dies holding the note. An "
            "installment obligation is income in respect of a decedent, so the heirs do not "
            "receive a basis step-up on the deferred gain and continue reporting it as payments "
            "arrive. An offsetting estate tax deduction is available where estate tax was paid. "
            "Owners planning a long note should confirm this outcome is acceptable inside the "
            "broader estate plan rather than discover it later.</p>"
        ),
    ],
    takeaways=[
        "Installment reporting applies automatically when any payment arrives after the year of sale.",
        "The gross profit ratio is fixed at closing and applied to every principal payment.",
        "Depreciation recapture is taxed in the year of sale regardless of cash received.",
        "Above $5 million of outstanding notes, Section 453A charges interest on the deferred tax.",
        "Borrowing against the note is treated as collecting it and accelerates the gain.",
        "Electing out can be the better answer when losses, rate expectations, or credit risk favor it.",
    ],
    faqs=[
        (
            "Do I have to elect installment treatment?",
            "<p>No. It applies automatically to a qualifying sale with a deferred payment. The "
            "election that must be made affirmatively is the election out, which reports the "
            "full gain in the year of sale and is made on a timely filed return for that "
            "year.</p>",
        ),
        (
            "Can I use an installment sale for stock in my S corporation?",
            "<p>Yes. A sale of stock or membership interests can be reported on the installment "
            "method, and because it is a single asset the allocation problems of an asset sale "
            "do not arise. If the buyer requires an asset sale or a Section 338(h)(10) election, "
            "the deemed asset sale rules apply and the recapture carve-out comes back into "
            "play.</p>",
        ),
        (
            "What happens if the buyer defaults?",
            "<p>If the seller repossesses the business, gain is generally recognized to the "
            "extent of payments already received in excess of gain previously reported, and the "
            "repossessed property takes a new basis. The outcome depends heavily on the security "
            "agreement, which is why the note terms matter as much as the tax analysis.</p>",
        ),
        (
            "Does the installment method help with the 3.8 percent surtax?",
            "<p>It can. The net investment income tax applies once modified adjusted gross "
            "income crosses the threshold, so spreading gain does not avoid the surtax in years "
            "where income is still high, but it reduces the amount exposed in any single year "
            "and can eliminate it in low-income years. Gain from a business in which the seller "
            "materially participated may also fall outside net investment income under the "
            "Section 1411 rules, which should be checked before assuming the surtax applies "
            "at all.</p>",
        ),
    ],
)

SELLER_FIN = Spoke(
    slug="seller-financing-tax-strategy",
    label="Seller financing: carrying the note on your own deal",
    title="Seller Financing Tax Strategy for Business Sellers",
    description=(
        "Why carrying paper raises the price and widens the buyer pool, how the "
        "interest is taxed, the applicable federal rate and imputed interest rules, "
        "and how to secure the note properly."
    ),
    h1="Seller Financing Tax Strategy: Why Smart Business Sellers Finance Their Own Deals",
    subtitle=(
        "Carrying the note is a pricing decision, a tax decision, and a credit "
        "decision, and most sellers only think about the first one."
    ),
    lead=(
        "Seller financing means the seller takes a promissory note for part of the purchase "
        "price instead of cash at closing. It widens the buyer pool, typically supports a higher "
        "headline price, and qualifies the deferred portion for installment reporting, so tax on "
        "that gain is paid as principal is collected. The interest on the note is ordinary "
        "income, and the note must carry a stated rate at least equal to the applicable federal "
        "rate or the tax code will recharacterize part of the principal as interest anyway."
    ),
    keywords=[
        "seller financing tax treatment",
        "carrying the note business sale",
        "imputed interest applicable federal rate",
        "seller note tax strategy",
    ],
    body=[
        (
            "What Carrying the Note Buys the Seller",
            "<p>Three things, in order of how much they usually matter.</p>"
            "<p><strong>Price.</strong> A buyer who does not have to raise the full amount from "
            "a lender can pay more, and sellers who finance 20 to 40 percent of the price "
            "commonly realize a higher total than an all-cash deal would have produced. The "
            "premium is not free money, it is compensation for taking credit risk, but it is "
            "compensation the seller can actually price.</p>"
            "<p><strong>Buyer pool.</strong> Bank financing for the purchase of a privately held "
            "business is constrained, and a large share of qualified operators cannot close "
            "without seller paper. Refusing to carry a note removes those buyers from the "
            "process entirely.</p>"
            "<p><strong>Yield.</strong> A secured note on a business the seller knows intimately, "
            "at a rate above what the same money earns in a bond portfolio, is a reasonable "
            "asset to hold. Sellers who are otherwise going to sit in cash for a year after "
            "closing should compare the note rate to what the proceeds would actually earn.</p>"
        ),
        (
            "How the Payments Are Taxed",
            "<p>Every payment splits into three parts, and each part has a different rate.</p>"
            "<ul>"
            "<li><strong>Return of basis.</strong> Not taxed.</li>"
            "<li><strong>Gain.</strong> Taxed at capital gain rates as principal is collected, "
            "using the gross profit ratio fixed at closing. The mechanics are set out in the "
            "<a href=\"/installment-sale-tax-strategy/\">installment sale guide</a>.</li>"
            "<li><strong>Interest.</strong> Ordinary income in the year received, at rates up to "
            "37 percent, and potentially subject to the 3.8 percent net investment income "
            "tax.</li>"
            "</ul>"
            "<p>That rate difference creates an obvious temptation: state a low interest rate, "
            "raise the price, and convert ordinary income into capital gain. The code anticipated "
            "this, and the rules that stop it are the most important technical content on this "
            "page.</p>"
        ),
        (
            "Imputed Interest and the Applicable Federal Rate",
            "<p>If a note does not carry adequate stated interest, Sections 483 and 1274 impute "
            "it. The benchmark is the applicable federal rate, published monthly by the IRS in "
            "short-term, mid-term, and long-term versions depending on the note's term. Where "
            "the stated rate falls below the applicable rate, a portion of each payment is "
            "recharacterized as interest, which increases ordinary income and reduces the "
            "capital gain, precisely reversing what the seller was trying to achieve.</p>"
            "<p>Under Section 1274 the recharacterization is handled as original issue discount, "
            "which is worse than simply losing the rate arbitrage, because original issue "
            "discount accrues into income on a constant yield basis whether or not cash is "
            "received. A seller can end up reporting interest income in a year the buyer paid "
            "nothing.</p>"
            "<p>The practical rule is to state a rate at or above the applicable federal rate for "
            "the term, document it in the note, and negotiate price on its own terms. A "
            "commercially reasonable rate is usually well above the federal rate anyway, since "
            "the seller is taking subordinated credit risk on a small business.</p>"
        ),
        (
            "Structuring the Note So It Is Actually Collectible",
            "<p>The tax analysis is worthless if the money does not arrive. Terms that matter, "
            "roughly in order:</p>"
            "<ul>"
            "<li><strong>Security.</strong> A first or second lien on the business assets, "
            "perfected by a UCC-1 filing, and where possible a pledge of the equity so a default "
            "returns control of the company rather than a claim against it.</li>"
            "<li><strong>Personal guarantee.</strong> From the individual buyer, not only the "
            "acquisition entity, and supported by a personal financial statement obtained during "
            "diligence.</li>"
            "<li><strong>Covenants.</strong> Limits on additional debt, distributions, and "
            "compensation while the note is outstanding, with financial reporting at least "
            "quarterly.</li>"
            "<li><strong>Acceleration and cure.</strong> A short cure period and a clear "
            "acceleration trigger, so a slow decline does not become an unsecured position by "
            "the time anyone acts.</li>"
            "</ul>"
            "<p>Two structures deserve specific caution. A note secured by a standby letter of "
            "credit can retain installment treatment if the letter is genuinely standby and "
            "cannot be drawn absent default. Proceeds placed in an escrow the seller can reach "
            "are generally treated as received at closing, which defeats the deferral entirely. "
            "The difference between the two is drafting.</p>"
        ),
        (
            "Earnouts and Contingent Payments",
            "<p>Where part of the price depends on future performance, the payments are "
            "contingent and the basis recovery rules under the installment regulations apply. If "
            "a maximum price is stated, basis is recovered ratably against that maximum. If only "
            "a term is stated, basis is recovered ratably over the term. If neither is stated, "
            "basis recovery is spread over fifteen years, which is the worst outcome and "
            "entirely avoidable by stating a cap.</p>"
            "<p>Earnouts also raise a character question. Amounts tied to the seller's continued "
            "employment can be recharacterized as compensation, taxed at ordinary rates and "
            "subject to payroll tax. Keeping the earnout tied to business performance rather than "
            "the seller's service, and paying separately and reasonably for any transition work, "
            "keeps the two categories apart.</p>"
        ),
        (
            "When Not to Carry Paper",
            "<p>Seller financing is a poor fit when the seller needs the full proceeds "
            "immediately for a diversification plan or a "
            "<a href=\"/charitable-remainder-trust-business-exit/\">charitable structure</a>, "
            "when the buyer's operating experience does not support the risk, when the business "
            "depends on the seller's relationships in a way that makes post-closing performance "
            "genuinely uncertain, or when the seller's estate plan cannot absorb an illiquid "
            "note held at death.</p>"
            "<p>The honest framing is that carrying a note is an investment decision the seller "
            "is making in a business they are choosing to leave. It is often a good one, at a "
            "good rate, with better information than any other lender has. It is not a good one "
            "when the reason the buyer cannot get financing is that the business does not "
            "support it.</p>"
        ),
        (
            "Running the Numbers Against an All-Cash Deal",
            "<p>The comparison sellers rarely make is between a lower all-cash price and a "
            "higher price with a note attached. Consider a business where the all-cash offer is "
            "$4,500,000 and the financed alternative is $5,000,000 with $1,500,000 carried over "
            "five years at 8 percent.</p>"
            "<div style=\"overflow-x:auto;\">"
            "<table>"
            "<thead><tr><th>Element</th><th>All cash at $4.5M</th><th>$5.0M with a $1.5M note</th></tr></thead>"
            "<tbody>"
            "<tr><td>Cash at closing</td><td>$4,500,000</td><td>$3,500,000</td></tr>"
            "<tr><td>Principal collected later</td><td>$0</td><td>$1,500,000</td></tr>"
            "<tr><td>Interest collected over 5 years</td><td>$0</td><td>Roughly $325,000</td></tr>"
            "<tr><td>Gain recognized at closing</td><td>Full</td><td>70 percent</td></tr>"
            "<tr><td>Credit risk carried</td><td>None</td><td>$1,500,000</td></tr>"
            "</tbody></table></div>"
            "<p>The financed structure produces roughly $825,000 more in total consideration and "
            "defers tax on a portion of the gain, in exchange for taking subordinated risk on "
            "$1.5 million. Whether that is a good trade depends entirely on the buyer and the "
            "business, and it is a question the seller is better placed to answer than any "
            "outside lender.</p>"
            "<p>The reason to write it out is that the two offers are usually presented as though "
            "the higher number is simply better, or the cash number simply safer. Neither is "
            "true without the arithmetic.</p>"
        ),
    ],
    takeaways=[
        "Seller notes widen the buyer pool and usually support a higher total price.",
        "Principal carries capital gain at the fixed gross profit ratio; interest is ordinary income.",
        "State a rate at or above the applicable federal rate or interest gets imputed anyway.",
        "Original issue discount can force interest income in a year no cash was received.",
        "Perfect the security interest and take a personal guarantee before worrying about tax.",
        "State a maximum price on any earnout so basis recovery is not spread over fifteen years.",
    ],
    faqs=[
        (
            "What interest rate should a seller note carry?",
            "<p>At minimum the applicable federal rate for the note's term, published monthly by "
            "the IRS. Commercially, subordinated seller paper on a small business typically "
            "carries a materially higher rate, and pricing it at the federal minimum leaves "
            "money on the table without any tax benefit in exchange.</p>",
        ),
        (
            "Is the interest I receive subject to the 3.8 percent surtax?",
            "<p>Interest income is net investment income, so it is exposed once modified "
            "adjusted gross income crosses the threshold. The capital gain portion of each "
            "payment may be treated differently depending on whether the seller materially "
            "participated in the business, which is a separate analysis under Section 1411.</p>",
        ),
        (
            "Can I sell the note later?",
            "<p>Yes, but selling or otherwise disposing of an installment obligation accelerates "
            "the remaining deferred gain into the year of disposition. The same is true of using "
            "the note as loan collateral under the pledging rule. Sellers who expect to need "
            "liquidity should size the note accordingly rather than plan to monetize it.</p>",
        ),
        (
            "How much of the price should I finance?",
            "<p>There is no universal answer, but 10 to 30 percent is the common range in "
            "privately held business sales, with the seller note subordinated to any bank debt. "
            "The right number is the amount the seller can afford to lose entirely without "
            "changing their post-sale plan.</p>",
        ),
        (
            "Does a seller note affect how much the buyer can borrow?",
            "<p>Usually it helps. Lenders often treat properly subordinated seller paper with a "
            "standstill provision as part of the equity layer, which improves the buyer's "
            "coverage ratios and can enlarge the senior loan. That is one reason a seller "
            "carrying 15 percent frequently unlocks a deal that would not have closed at any "
            "price, and it is worth raising with the buyer's lender directly rather than "
            "negotiating the note in isolation.</p>",
        ),
        (
            "What happens to the note if I die before it is repaid?",
            "<p>The remaining deferred gain is income in respect of a decedent, so the heirs "
            "continue reporting gain as payments arrive rather than receiving a basis step-up on "
            "that portion. An estate tax deduction is available where estate tax was paid on the "
            "note. Sellers with long notes should confirm the estate plan accounts for an "
            "illiquid asset with a built-in tax liability.</p>",
        ),
    ],
)

STRUCTURE = Spoke(
    slug="structuring-your-business-for-sale",
    label="Structuring the business for sale: entity changes that save tax",
    title="How to Structure Your Business for Sale: Entity Changes That Save Tax",
    description=(
        "Asset sale versus stock sale, the C corporation double tax, S corporation "
        "built-in gains, F reorganizations with rollover equity, and separating real "
        "estate before a transaction."
    ),
    h1="How to Structure Your Business for Sale: Entity Changes That Save Tax",
    subtitle=(
        "Structure determines the tax bill before any strategy is applied to it, and "
        "most of the useful changes take years to season."
    ),
    lead=(
        "The largest single variable in the tax on a business sale is not the price, it is "
        "whether the transaction is an asset sale or an equity sale and what entity holds the "
        "assets. The same $6 million business can produce a 20 percent effective federal tax "
        "burden or something close to 40 percent depending on structure alone. Buyers prefer "
        "asset purchases because they get a stepped-up basis to depreciate; sellers prefer "
        "equity sales because gain is taxed once at capital rates. Most of the useful "
        "restructuring has a waiting period, which is why this work belongs three to five years "
        "before a transaction."
    ),
    keywords=[
        "structure business for sale tax",
        "asset sale vs stock sale",
        "s corp built in gains tax",
        "f reorganization rollover equity",
    ],
    body=[
        (
            "Asset Sale Versus Equity Sale",
            "<p>In an asset sale the buyer purchases the assets and assumes selected "
            "liabilities. The purchase price is allocated across asset classes under Section "
            "1060, and the buyer depreciates or amortizes the stepped-up basis, with goodwill "
            "amortized over fifteen years. In an equity sale the buyer purchases stock or "
            "membership interests, inherits the historical basis, and takes the liabilities that "
            "come with the entity.</p>"
            "<p>For the seller, the equity sale is generally a single capital gain. The asset "
            "sale produces a mix: ordinary income on depreciation recapture and receivables, "
            "capital gain on goodwill, and, if the seller is a C corporation, an entity-level tax "
            "before anything reaches the owner.</p>"
            "<p>The gap is negotiable because it is quantifiable. A buyer's step-up has a present "
            "value, and a seller who can calculate both sides can price the structure rather "
            "than concede it. Sellers who cannot run that math tend to accept an asset sale and "
            "absorb the difference silently.</p>"
        ),
        (
            "The C Corporation Double Tax",
            "<p>A C corporation that sells its assets pays 21 percent at the entity level, and "
            "the shareholders pay again on the distribution of the proceeds, at qualified "
            "dividend or capital gain rates plus the 3.8 percent surtax. The combined federal "
            "burden approaches 40 percent, against roughly 23.8 percent on a clean stock "
            "sale.</p>"
            "<p>Two responses exist. The first is to insist on a stock sale, which is also the "
            "only way to preserve any "
            "<a href=\"/qsbs-exclusion-section-1202/\">Section 1202 exclusion</a> the "
            "shareholders have earned. The second is personal goodwill: where the relationships, "
            "reputation, and know-how genuinely belong to the individual rather than the "
            "corporation, and no enforceable non-competition agreement transferred them to the "
            "company, a portion of the price can be paid directly to the owner and taxed once. "
            "The case law supports this on the right facts and rejects it where the owner has "
            "long been bound by a company non-compete, so the analysis has to begin with the "
            "employment documents.</p>"
        ),
        (
            "S Corporations and the Built-In Gains Tax",
            "<p>An S corporation that was previously a C corporation is subject to a corporate "
            "level tax at 21 percent on net built-in gain recognized during the five-year period "
            "after conversion. The tax is limited to appreciation that existed at the conversion "
            "date, which makes the appraisal performed at conversion the controlling document "
            "years later.</p>"
            "<p>The practical consequence is a clock. An owner who converts a C corporation to S "
            "status and sells assets in year three pays the corporate tax anyway. Converting and "
            "then waiting past the recognition period removes it. Since most sale processes take "
            "six to twelve months and most owners begin thinking about an exit two years out, "
            "the conversion decision usually has to be made before the exit is a concrete "
            "plan.</p>"
            "<p>Note the tension with Section 1202. Electing S status forfeits any future "
            "qualified small business stock exclusion, while remaining a C corporation preserves "
            "it and accepts double taxation on operating income in the meantime. Which way that "
            "resolves depends on the size of the expected gain, the years remaining to a sale, "
            "and how much cash the owner takes out annually. It is a modeling question, and it "
            "is worked in our <a href=\"/entity-structuring-business-owners/\">entity structuring "
            "guide</a>.</p>"
        ),
        (
            "The F Reorganization With an LLC Drop-Down",
            "<p>This is the standard structure in middle market S corporation sales, and it "
            "solves two problems at once.</p>"
            "<p>The shareholders contribute their stock to a newly formed holding company, which "
            "elects to treat the old operating company as a qualified subchapter S subsidiary. "
            "The subsidiary then converts to a single member LLC. The whole sequence is a "
            "reorganization under Section 368(a)(1)(F), treated as a mere change in form, and "
            "the S election survives.</p>"
            "<p>What it delivers: the buyer purchases LLC units and receives asset sale treatment "
            "with a full basis step-up, while the seller reports a single level of tax. It also "
            "makes rollover equity clean, so a seller who keeps 20 percent alongside a private "
            "equity buyer does so without the tax friction a direct stock sale would create. And "
            "it insulates the buyer from the risk that the S election was defective at some point "
            "in the company's history, which is one of the most common diligence findings in "
            "closely held companies.</p>"
            "<p>The related mechanism in a C corporation or consolidated group context is a "
            "Section 338(h)(10) or Section 336(e) election, which treats a stock purchase as a "
            "deemed asset sale. Both require a willing seller, because the seller bears the "
            "asset sale tax profile, so the election normally comes with a gross-up in the "
            "price.</p>"
        ),
        (
            "Separating Real Estate and Intellectual Property",
            "<p>Operating businesses that own their building should generally hold it in a "
            "separate entity, and the reasons compound at exit.</p>"
            "<p>A buyer valuing the operating company at a multiple of earnings will not pay a "
            "comparable multiple for real estate, so bundling the property into the sale usually "
            "undervalues it. Holding it separately lets the seller sell the business, keep the "
            "building, and lease it back at a market rate, converting a one-time gain into a "
            "long-term income stream. If the seller does want to sell the property, holding it "
            "outside the operating entity preserves the ability to use a "
            "<a href=\"/1031-exchange-planning/\">1031 exchange</a>, which is unavailable on the "
            "sale of an operating business.</p>"
            "<p>Separation also protects the depreciation planning already done. A "
            "<a href=\"/cost-segregation-study/\">cost segregation study</a> on a building held "
            "in a separate entity keeps producing deductions after the operating business is "
            "gone. The same structure is discussed from the operating perspective in "
            "<a href=\"/holding-company-vs-operating-company/\">holding company versus operating "
            "company</a>.</p>"
            "<p>Moving appreciated real estate out of a corporation immediately before a sale is "
            "a taxable distribution at fair market value, so this is a change to make early or "
            "not at all.</p>"
        ),
        (
            "Purchase Price Allocation",
            "<p>In an asset sale, buyer and seller must allocate the price across seven asset "
            "classes on Form 8594, and the allocations must be consistent. The negotiation is "
            "genuinely adverse: the buyer wants weight on equipment and non-competition "
            "agreements for faster deductions, the seller wants weight on goodwill for capital "
            "gain treatment.</p>"
            "<div style=\"overflow-x:auto;\">"
            "<table>"
            "<thead><tr><th>Allocation</th><th>Seller treatment</th><th>Buyer treatment</th></tr></thead>"
            "<tbody>"
            "<tr><td>Equipment</td><td>Ordinary recapture to prior depreciation</td><td>Depreciable, often fast</td></tr>"
            "<tr><td>Inventory</td><td>Ordinary income</td><td>Cost of goods sold</td></tr>"
            "<tr><td>Non-compete</td><td>Ordinary income</td><td>Amortized over 15 years</td></tr>"
            "<tr><td>Goodwill</td><td>Capital gain</td><td>Amortized over 15 years</td></tr>"
            "<tr><td>Real property</td><td>Capital gain with 1250 recapture</td><td>27.5 or 39 year life</td></tr>"
            "</tbody></table></div>"
            "<p>Because the non-compete is ordinary to the seller and amortized over fifteen "
            "years to the buyer, it is the item both sides should be least attached to, and it "
            "is frequently oversized out of habit. A seller who understands the table above can "
            "trade allocation for price knowingly.</p>"
        ),
        (
            "A Working Sequence",
            "<p>Ordered by how much lead time each item needs.</p>"
            "<ul>"
            "<li><strong>Five years out.</strong> Decide the C versus S question in light of "
            "Section 1202, and complete any conversion that starts a recognition period.</li>"
            "<li><strong>Three years out.</strong> Separate real estate and intellectual "
            "property into their own entities while values and transfer costs are lower.</li>"
            "<li><strong>Two years out.</strong> Complete any gifting to trusts intended to "
            "multiply exclusions or freeze value, before a price is observable.</li>"
            "<li><strong>Twelve months out.</strong> Run the F reorganization, clean up the "
            "S election history, and get the books to a quality of earnings standard.</li>"
            "<li><strong>At the letter of intent.</strong> Model the allocation and the "
            "after-tax proceeds under each structure before agreeing to either.</li>"
            "</ul>"
        ),
    ],
    takeaways=[
        "Structure moves the effective rate on a sale by fifteen points or more before any strategy applies.",
        "A C corporation asset sale is taxed twice; a stock sale is taxed once and preserves Section 1202.",
        "Built-in gains tax runs for five years after a C to S conversion, so the clock starts early.",
        "The F reorganization gives the buyer a basis step-up and the seller one level of tax.",
        "Real estate held outside the operating entity can be retained, leased back, or exchanged.",
        "Purchase price allocation is adversarial and quantifiable, so trade it deliberately.",
    ],
    faqs=[
        (
            "Should I convert my C corporation to an S corporation before selling?",
            "<p>Only with enough runway. The built-in gains tax applies to appreciation existing "
            "at conversion for five years afterward, so a conversion inside that window does not "
            "avoid the corporate level tax on an asset sale. It also forfeits any qualified small "
            "business stock exclusion, which for a fast-growing company can be worth more than "
            "the double tax it avoids.</p>",
        ),
        (
            "Why do buyers insist on an asset sale?",
            "<p>Two reasons. They get a stepped-up basis to depreciate and amortize, which is "
            "worth real money in present value terms, and they avoid inheriting unknown "
            "liabilities that travel with an entity. The first is negotiable through price; the "
            "second is usually addressed through representations, indemnities, and escrow.</p>",
        ),
        (
            "What is personal goodwill and can I actually claim it?",
            "<p>It is the portion of a business's value attributable to an individual owner's "
            "personal relationships, reputation, and expertise rather than to the company. Where "
            "the owner was never subject to an enforceable non-competition agreement with the "
            "company, courts have allowed part of the price to be paid to the owner directly and "
            "taxed once. Where such an agreement exists, the argument generally fails.</p>",
        ),
        (
            "Can I move my building out of the company right before I sell?",
            "<p>Distributing appreciated real estate out of a corporation is treated as a sale at "
            "fair market value, triggering tax at the entity level and again on the "
            "distribution. Doing it years earlier, or holding the property in a separate entity "
            "from the start, avoids that outcome. This is the clearest example of a structural "
            "decision that cannot be fixed at closing.</p>",
        ),
        (
            "How long does restructuring before a sale take?",
            "<p>The F reorganization itself takes weeks. The changes with waiting periods, the S "
            "conversion recognition period, gifts intended to survive valuation scrutiny, and "
            "the five-year qualified small business stock holding period, take years. A "
            "reasonable planning horizon is three to five years, and useful work is still "
            "possible at twelve months.</p>",
        ),
    ],
)

OZ = Spoke(
    slug="opportunity-zone-investing-after-business-sale",
    label="Opportunity zones after a sale: deferring and eliminating gain",
    title="Opportunity Zone Investing After a Business Sale",
    description=(
        "How qualified opportunity funds defer capital gain, what the ten-year hold "
        "eliminates, the December 31, 2026 recognition date, and what the 2025 law "
        "changed for investments starting in 2027."
    ),
    h1="Opportunity Zone Investing After a Business Sale: Defer and Reduce Capital Gains",
    subtitle=(
        "The only widely available structure that converts a taxable gain into an "
        "asset whose future appreciation is never taxed."
    ),
    lead=(
        "A qualified opportunity fund lets a taxpayer roll capital gain from any sale into a fund "
        "investing in designated distressed areas, deferring tax on the rolled gain and, after a "
        "ten-year hold, eliminating tax on all appreciation in the fund itself. The rolled gain "
        "must be invested within 180 days of recognition, and only the gain needs to be invested, "
        "not the principal. The 2025 tax act made the program permanent with new designations "
        "effective in 2027, which creates an unusual gap year for anyone selling a business in "
        "2026."
    ),
    keywords=[
        "opportunity zone after business sale",
        "qualified opportunity fund capital gains",
        "opportunity zone 2026",
        "defer capital gains opportunity zone",
    ],
    body=[
        (
            "The Two Benefits, and Which One Matters More",
            "<p>The structure delivers deferral and elimination, and they are frequently "
            "conflated.</p>"
            "<p><strong>Deferral</strong> postpones tax on the gain rolled into the fund until a "
            "statutory recognition date or an earlier disposition. It is a timing benefit worth "
            "the return on the deferred tax for the deferral period.</p>"
            "<p><strong>Elimination</strong> is the larger one. Hold the fund interest at least "
            "ten years and elect to step basis up to fair market value on sale, and the entire "
            "appreciation in the investment escapes tax permanently. On an investment that "
            "triples over a decade, this is worth substantially more than the deferral that "
            "preceded it, and it survives even where the deferral benefit has run out.</p>"
            "<p>That distinction is the single most useful thing to understand about the program "
            "in 2026, for the reason described next.</p>"
        ),
        (
            "The December 31, 2026 Recognition Date",
            "<p>Under the original program, deferred gain is recognized on the earlier of a "
            "disposition of the fund interest or December 31, 2026. A gain rolled into a fund in "
            "2026 is therefore recognized within months, and the deferral benefit is close to "
            "nil.</p>"
            "<p>The ten-year elimination is unaffected. An investor who rolls gain into a fund "
            "in 2026, pays the deferred tax with the 2026 return, and holds the position for a "
            "decade still eliminates all appreciation. The trade is simply a pure appreciation "
            "play rather than a deferral plus appreciation play, and it should be evaluated on "
            "that basis.</p>"
            "<p>This is where sellers get poor advice. A pitch built around deferral is selling a "
            "benefit that no longer exists for a 2026 investment. A pitch built around ten-year "
            "elimination is describing something real, and it needs to be measured against what "
            "the same capital would earn in an ordinary taxable investment, after tax.</p>"
        ),
        (
            "What the 2025 Law Changed",
            "<p>The 2025 act made the program permanent rather than letting the designations "
            "lapse. The principal features, which take effect for investments made after the new "
            "designations begin in 2027, are a rolling deferral period of five years from the "
            "date of investment rather than a single fixed recognition date, a basis step-up of "
            "10 percent after five years, an enhanced 30 percent step-up for funds investing in "
            "designated rural areas, and expanded reporting for funds and investors.</p>"
            "<p>Two planning implications follow for an owner selling in the next eighteen "
            "months. First, a sale closing late in 2026 may have a 180-day window that reaches "
            "into 2027, which is a question worth asking before the closing date is fixed. "
            "Second, the rural provisions are meaningfully more generous than the standard ones, "
            "and fund sponsors are building products around them.</p>"
            "<p>Regulatory guidance on the 2027 rules is still developing. Anything a sponsor "
            "presents as settled about the new regime should be checked against actual published "
            "guidance before capital is committed.</p>"
        ),
        (
            "The 180-Day Window and What Gain Qualifies",
            "<p>Only capital gain is eligible, whether short-term or long-term, from any source: "
            "a business sale, a real estate sale, or a securities portfolio. Ordinary income, "
            "including depreciation recapture taxed as ordinary income, is not eligible.</p>"
            "<p>The 180-day clock generally starts on the date the gain would be recognized. For "
            "gain reported on a Schedule K-1 from a partnership or S corporation, the investor "
            "can elect to start the clock at the end of the entity's tax year, or at the due date "
            "of the entity return, which frequently extends the practical deadline well into the "
            "following year. Sellers who think they have missed the window often have not.</p>"
            "<p>Only the gain must be invested. A business sold for $8 million with $2 million of "
            "basis produces $6 million of gain, and rolling the full $6 million shelters all of "
            "it while the $2 million of basis remains available as cash. This is a structural "
            "advantage over a "
            "<a href=\"/1031-exchange-planning/\">1031 exchange</a>, which requires reinvestment "
            "of the entire proceeds and is limited to real property.</p>"
        ),
        (
            "Fund and Business Requirements",
            "<p>The fund must hold at least 90 percent of its assets in qualified opportunity "
            "zone property, tested twice a year. Where the fund invests through an operating "
            "business rather than owning property directly, the business must satisfy its own "
            "tests: at least 70 percent of its tangible property located in the zone, at least 50 "
            "percent of gross income from the active conduct of a trade or business within it, "
            "and limits on nonqualified financial property.</p>"
            "<p>Property acquired by the fund must be either original use in the zone or "
            "substantially improved, meaning additions to basis exceeding the basis of the "
            "building within any 30-month period. Land is not subject to the substantial "
            "improvement requirement, which is why ground-up development and heavy "
            "rehabilitation dominate the fund landscape.</p>"
            "<p>Certain businesses are excluded, including golf courses, country clubs, massage "
            "parlors, hot tub facilities, tanning salons, racetracks, gambling facilities, and "
            "liquor stores.</p>"
        ),
        (
            "Who This Actually Fits",
            "<p>The investment risk is real and often understated in the tax conversation. "
            "Opportunity funds are illiquid for a decade, concentrated in development projects, "
            "dependent on sponsor execution, and priced with fee loads that vary widely. A "
            "mediocre project with perfect tax treatment loses to a good investment taxed "
            "normally.</p>"
            "<p>The profile that fits is a seller with a large capital gain, no immediate need "
            "for that portion of the proceeds, genuine willingness to hold a private real estate "
            "position for ten years, and the ability to evaluate the sponsor on the merits of the "
            "underlying development. Sellers who want liquidity, or who would not make the "
            "investment absent the tax benefit, are better served by the "
            "<a href=\"/installment-sale-tax-strategy/\">installment approach</a> or by paying "
            "the tax and investing the remainder in something they would own anyway.</p>"
        ),
        (
            "How It Compares to the Other Options",
            "<p>Sellers frequently ask why they would use an opportunity fund rather than one of "
            "the other reinvestment routes. The differences are structural rather than a matter "
            "of degree.</p>"
            "<div style=\"overflow-x:auto;\">"
            "<table>"
            "<thead><tr><th></th><th>Opportunity fund</th><th>1031 exchange</th><th>Installment note</th></tr></thead>"
            "<tbody>"
            "<tr><td>Amount to reinvest</td><td>Gain only</td><td>Full proceeds</td><td>None</td></tr>"
            "<tr><td>Eligible gain</td><td>Any capital gain</td><td>Real property only</td><td>Any deferred sale</td></tr>"
            "<tr><td>Deadline</td><td>180 days</td><td>45 and 180 days</td><td>Set in the deal</td></tr>"
            "<tr><td>Future appreciation</td><td>Untaxed after 10 years</td><td>Deferred until sale</td><td>Taxed normally</td></tr>"
            "<tr><td>Liquidity</td><td>Very low for a decade</td><td>Low</td><td>Scheduled payments</td></tr>"
            "</tbody></table></div>"
            "<p>The opportunity fund is the only one of the three that permanently eliminates tax "
            "on appreciation, and the only one available on the sale of an operating business "
            "rather than real property. It is also the most illiquid and the most dependent on a "
            "third-party sponsor, which is why it usually takes a portion of the proceeds rather "
            "than all of them.</p>"
        ),
    ],
    takeaways=[
        "Only the capital gain has to be reinvested, not the full proceeds.",
        "The ten-year hold eliminates tax on appreciation in the fund, which is the larger benefit.",
        "Deferred gain under the original program is recognized on December 31, 2026.",
        "The 2025 act makes the program permanent with new designations from 2027 and a rural enhancement.",
        "K-1 gain can start its 180-day clock at the entity year end, extending the deadline.",
        "Funds are illiquid for a decade, so sponsor and project quality decide the outcome.",
    ],
    faqs=[
        (
            "Do I have to reinvest all the sale proceeds?",
            "<p>No. Only the capital gain has to be invested in the fund to shelter it. The "
            "return of basis stays with the seller as cash. This is the main structural "
            "difference from a 1031 exchange, which requires the full proceeds to be reinvested "
            "and applies only to real property.</p>",
        ),
        (
            "Does gain from selling my business qualify, or only real estate gain?",
            "<p>Any capital gain qualifies, including gain from the sale of a business, stock, or "
            "other assets. The portion of a business sale taxed as ordinary income, such as "
            "depreciation recapture on equipment or income from a non-competition agreement, does "
            "not qualify.</p>",
        ),
        (
            "Is an opportunity zone investment still worth it in 2026?",
            "<p>The deferral component is largely spent because deferred gain is recognized on "
            "December 31, 2026. The ten-year elimination remains fully available and is the "
            "reason to consider it. Judge the investment as a decade-long private real estate "
            "commitment whose appreciation is untaxed, not as a deferral vehicle.</p>",
        ),
        (
            "What happens if I sell the fund interest before ten years?",
            "<p>The deferred gain becomes taxable if it has not already been recognized, and any "
            "appreciation in the fund is taxed normally. There is no partial credit for "
            "appreciation elimination below the ten-year mark, which is why the illiquidity has "
            "to be genuinely acceptable at the outset.</p>",
        ),
        (
            "How do I evaluate a qualified opportunity fund sponsor?",
            "<p>On the same basis as any private real estate investment, because that is what it "
            "is. Look at the sponsor's completed projects rather than the pipeline, the fee load "
            "at every layer, the amount of sponsor capital invested alongside investors, the "
            "leverage on each asset, and whether the ten-year hold period aligns with the "
            "project's natural life. A fund that needs to sell in year seven cannot deliver the "
            "benefit that justified the investment.</p>",
        ),
        (
            "Can I start my own opportunity fund?",
            "<p>Yes. A qualified opportunity fund can be a partnership or corporation that "
            "self-certifies on Form 8996, and owners who already intend to develop property in a "
            "designated zone frequently form their own rather than invest through a sponsor. It "
            "carries real compliance obligations, including the semiannual 90 percent asset test "
            "and the substantial improvement requirement, so it suits owners with an actual "
            "project rather than those looking only for the tax result.</p>",
        ),
    ],
)

CRT = Spoke(
    slug="charitable-remainder-trust-business-exit",
    label="Charitable remainder trusts: selling inside a tax-exempt trust",
    title="Charitable Remainder Trust for Business Exits",
    description=(
        "How a CRT sells an appreciated business interest without immediate capital "
        "gains tax, the CRAT, CRUT, NIMCRUT and flip variants, the prearranged sale "
        "trap, and the assets that cannot go in."
    ),
    h1="Charitable Remainder Trust for Business Exits: The Tax-Free Diversification Play",
    subtitle=(
        "The trust sells the asset, not the owner, and the trust does not pay capital "
        "gains tax. Everything else follows from that one fact."
    ),
    lead=(
        "A charitable remainder trust is an irrevocable trust that pays an income stream to the "
        "donor for life or a term of up to twenty years, then distributes what remains to "
        "charity. Because the trust is tax-exempt, it can sell a contributed business interest "
        "without paying capital gains tax at the sale, so the full pre-tax value is reinvested "
        "and the income stream is calculated on the larger amount. The donor also receives an "
        "income tax deduction for the present value of the charitable remainder, which must be at "
        "least 10 percent of the amount contributed."
    ),
    keywords=[
        "charitable remainder trust business sale",
        "crt capital gains avoidance",
        "nimcrut business owner",
        "crt diversification strategy",
    ],
    body=[
        (
            "The Mechanics, in Order",
            "<p>The sequence matters more than any single element.</p>"
            "<p>The owner contributes a portion of the business interest to the trust before any "
            "binding sale agreement exists. The trust becomes an owner of record. When the sale "
            "closes, the trust sells its interest and pays no tax on that gain, because a "
            "qualifying charitable remainder trust is exempt from income tax. The trust "
            "reinvests the full proceeds in a diversified portfolio and pays the donor the "
            "specified percentage each year. At the end of the term, the remainder passes to the "
            "named charity or donor advised fund.</p>"
            "<p>The immediate deduction is the present value of the projected remainder, computed "
            "using the Section 7520 rate, the payout percentage, and the term. Higher payouts and "
            "longer terms produce smaller deductions, and the remainder must clear 10 percent or "
            "the trust does not qualify at all.</p>"
        ),
        (
            "CRAT, CRUT, NIMCRUT, and the Flip",
            "<p>Four variants, and the choice is driven by the asset rather than by "
            "preference.</p>"
            "<p><strong>Charitable remainder annuity trust.</strong> Pays a fixed dollar amount, "
            "set as a percentage of the initial value, for the whole term. Predictable, no "
            "additional contributions permitted, and poorly suited to an illiquid asset because "
            "the payment obligation begins before the asset is sold.</p>"
            "<p><strong>Charitable remainder unitrust.</strong> Pays a fixed percentage of trust "
            "assets revalued annually, so the payment rises and falls with the portfolio. Allows "
            "additional contributions and is the more common structure.</p>"
            "<p><strong>Net income with makeup unitrust.</strong> Pays the lesser of the unitrust "
            "percentage or actual trust income, with a makeup account that tracks the shortfall "
            "and pays it out in later years when income exceeds the percentage. This lets a donor "
            "suppress distributions during high-earning years and take them later, which is a "
            "genuine income shifting tool.</p>"
            "<p><strong>Flip unitrust.</strong> Operates as a net income trust until a triggering "
            "event, usually the sale of the contributed asset, then converts to a standard "
            "unitrust. This is the right answer for a business exit, because it removes the "
            "obligation to distribute cash the trust does not yet have.</p>"
        ),
        (
            "Why the Sale Inside the Trust Is Not Taxed",
            "<p>The trust is exempt under Section 664, so the gain on the sale of the contributed "
            "interest is not taxed when realized. The gain is not forgiven; it is held in the "
            "trust's accounting and carried out to the donor over time through the ordering rules "
            "that govern distributions.</p>"
            "<p>Those rules assign each distribution to tiers in a fixed order: ordinary income "
            "first, then capital gain, then tax-exempt income, then return of principal. In "
            "practice a donor who contributed a highly appreciated business will receive "
            "distributions taxed largely as capital gain for many years. The benefit is not "
            "permanent exclusion, it is that the entire pre-tax amount was working from day one "
            "and the tax is paid slowly out of the earnings on it.</p>"
            "<p>On a $5 million interest with near-zero basis, paying $1.19 million of federal "
            "tax at closing leaves $3.81 million to invest. The trust invests $5 million. At a 6 "
            "percent return that difference compounds into a meaningfully larger income stream, "
            "which is the entire argument for the structure.</p>"
        ),
        (
            "The Prearranged Sale Trap",
            "<p>This is the failure mode that undoes the whole plan. If the donor is legally "
            "bound to sell at the moment of contribution, the IRS treats the gain as the donor's "
            "under the assignment of income doctrine, taxes it to them personally, and the trust "
            "provides no capital gains benefit at all.</p>"
            "<p>The distinction is between an expectation and an obligation. A signed purchase "
            "agreement, or a letter of intent with binding terms, before contribution is fatal. "
            "Contributing while negotiations are underway but nothing binding exists has been "
            "respected on the right facts, but it is uncomfortable ground.</p>"
            "<p>The safe practice is to contribute well before a transaction is documented, and "
            "to ensure the trustee has genuine authority to decline the sale. That is another "
            "reason exit planning belongs three or more years out, alongside the "
            "<a href=\"/qsbs-exclusion-section-1202/\">trust funding required to multiply the "
            "Section 1202 exclusion</a>, which carries the same timing discipline.</p>"
        ),
        (
            "What Cannot Go Into a CRT",
            "<p>Three restrictions eliminate a large share of candidates before the analysis "
            "starts.</p>"
            "<p><strong>S corporation stock.</strong> A charitable remainder trust is not a "
            "permitted S corporation shareholder. Contributing S stock terminates the S election, "
            "which is a catastrophic outcome for every other shareholder. Since most closely held "
            "operating businesses are S corporations, this is the single most common "
            "disqualifier.</p>"
            "<p><strong>Interests generating unrelated business taxable income.</strong> A CRT "
            "that receives unrelated business taxable income pays a 100 percent excise tax on "
            "that income. An operating partnership or LLC interest usually generates it, so an "
            "LLC interest is generally not suitable unless the entity's activity and debt profile "
            "have been examined carefully.</p>"
            "<p><strong>Debt-financed property.</strong> Property subject to a mortgage creates "
            "both unrelated business taxable income and potential self-dealing problems.</p>"
            "<p>What works cleanly: C corporation stock, unencumbered real estate, and marketable "
            "securities. For an S corporation owner, the practical alternatives are a charitable "
            "lead trust funded after the sale, a donor advised fund receiving cash proceeds, or "
            "restructuring the entity well in advance, which returns to "
            "<a href=\"/structuring-your-business-for-sale/\">how the business is structured for "
            "sale</a>.</p>"
        ),
        (
            "The Honest Downsides",
            "<p>The trust is irrevocable. The remainder goes to charity, not to children, and "
            "that is the price of the tax treatment. Owners who want both outcomes commonly pair "
            "the trust with a wealth replacement arrangement, using part of the income stream to "
            "fund a life insurance policy held in an irrevocable trust, so heirs receive a "
            "comparable amount outside the estate. That works, but it should be priced honestly, "
            "because insurance costs rise with age and health is not guaranteed.</p>"
            "<p>The income stream is also fixed by the document. A donor who later needs the "
            "principal cannot reach it. And the deduction, while real, is limited by the "
            "percentage of adjusted gross income rules with a five-year carryforward, so it is "
            "rarely usable in one year.</p>"
            "<p>Used well, this is one of the strongest structures available to a business owner "
            "with charitable intent and a highly appreciated position. Used because someone "
            "described it as a way to avoid tax, it commits capital irreversibly for a benefit "
            "the owner did not actually want.</p>"
        ),
        (
            "A Worked Comparison",
            "<p>An owner aged 60 contributes a $4,000,000 C corporation interest with negligible "
            "basis to a flip unitrust paying 6 percent for life, then the company sells.</p>"
            "<div style=\"overflow-x:auto;\">"
            "<table>"
            "<thead><tr><th></th><th>Outright sale</th><th>Sale inside the trust</th></tr></thead>"
            "<tbody>"
            "<tr><td>Tax at sale</td><td>About $952,000</td><td>$0</td></tr>"
            "<tr><td>Amount invested after the sale</td><td>$3,048,000</td><td>$4,000,000</td></tr>"
            "<tr><td>First-year income at 6 percent</td><td>$183,000</td><td>$240,000</td></tr>"
            "<tr><td>Income tax deduction</td><td>None</td><td>Present value of the remainder</td></tr>"
            "<tr><td>Principal available to heirs</td><td>Full</td><td>None, unless replaced</td></tr>"
            "</tbody></table></div>"
            "<p>The trust produces about 31 percent more annual income from the same asset, plus "
            "a current deduction, because the tax that would have been paid at closing stays "
            "invested. Distributions from that larger base are then taxed under the tier rules as "
            "they are received. The cost is the last row, which is why the wealth replacement "
            "question should be settled before the trust is signed rather than after.</p>"
        ),
    ],
    takeaways=[
        "The trust is tax-exempt, so it sells the contributed interest without capital gains tax at the sale.",
        "The full pre-tax amount is reinvested, which is where the economic advantage comes from.",
        "A flip unitrust is the right variant for an illiquid business interest.",
        "Distributions are taxed under four-tier ordering, so gain is carried out over time.",
        "S corporation stock cannot go into a CRT, and it terminates the S election if contributed.",
        "Contribute long before any binding agreement or the assignment of income doctrine applies.",
    ],
    faqs=[
        (
            "How much do I actually get to keep?",
            "<p>The donor keeps the income stream, typically 5 to 8 percent of trust value "
            "annually for life or a fixed term, plus the income tax deduction for the present "
            "value of the remainder. The remaining principal at the end of the term goes to "
            "charity. The comparison to make is between that income stream and what the after-tax "
            "proceeds of an outright sale would have produced.</p>",
        ),
        (
            "Can I be the trustee?",
            "<p>It is possible for a donor to serve as trustee, but it invites scrutiny over "
            "valuation and administration, and it complicates the argument that the trustee "
            "acted independently in the sale. Using an independent corporate trustee, at least "
            "for the period around a business sale, is the stronger position.</p>",
        ),
        (
            "What is the minimum size that makes sense?",
            "<p>Setup and ongoing administration typically run several thousand dollars a year "
            "in trustee, valuation, and tax preparation costs, so contributions below roughly $1 "
            "million rarely justify the structure. Above $2 million the economics are clear where "
            "charitable intent exists.</p>",
        ),
        (
            "What if my business is an S corporation?",
            "<p>Then a CRT is not available for the stock itself. The realistic options are "
            "restructuring years in advance, contributing appreciated non-operating assets such "
            "as real estate instead, or making a cash gift to a donor advised fund in the year "
            "of sale to offset the gain with a deduction. Each has a different profile and the "
            "right one depends on the size and timing of the gain.</p>",
        ),
    ],
)

FREEZE = Spoke(
    slug="estate-freeze-strategies-business-owners",
    label="Estate freezes: locking in today's value before growth",
    title="Estate Freeze Strategies for Business Owners",
    description=(
        "GRATs, sales to intentionally defective grantor trusts, family limited "
        "partnerships, valuation discounts, and preferred partnership freezes, with "
        "the 2026 exemption and the basis trade-off."
    ),
    h1="Estate Freeze Strategies for Business Owners: Lock In Today's Value Before Growth",
    subtitle=(
        "Transfer the growth, keep the value you have already built, and do it while "
        "the appraisal still supports a low number."
    ),
    lead=(
        "An estate freeze fixes the value of a business interest in the owner's estate at today's "
        "figure and shifts all future appreciation to the next generation, usually through a "
        "trust. The techniques are established and statutory: grantor retained annuity trusts, "
        "installment sales to intentionally defective grantor trusts, family limited partnerships "
        "with valuation discounts, and preferred partnership recapitalizations. The common "
        "requirement is that the transfer happens while the business is worth less than it will "
        "be, which for an owner heading toward a sale means before the market sets a price."
    ),
    keywords=[
        "estate freeze business owner",
        "grat vs idgt sale",
        "family limited partnership valuation discount",
        "transfer business to children tax free",
    ],
    body=[
        (
            "Why Freeze at All When the Exemption Is $15 Million",
            "<p>The 2025 act set the federal estate and gift tax exemption at $15 million per "
            "person beginning in 2026, indexed thereafter, and made it permanent rather than "
            "allowing the scheduled reduction. For a married couple that is $30 million of "
            "combined shelter, which covers most estates outright.</p>"
            "<p>Freezing still matters in three situations. A business growing at 15 percent "
            "annually doubles in five years, so an owner at $18 million today is at $36 million "
            "before an exit and well past the exemption. A permanent exemption is permanent only "
            "until Congress changes it, and the last three decades have seen it move repeatedly "
            "in both directions. And the generation-skipping transfer tax exemption, allocated "
            "properly to a trust that then appreciates, shelters growth for grandchildren in a "
            "way no post-death planning can replicate.</p>"
            "<p>Freezing is also cheapest exactly when it is least obviously needed, because the "
            "gift is measured at today's value.</p>"
        ),
        (
            "Grantor Retained Annuity Trusts",
            "<p>The owner transfers an interest to a trust and retains the right to an annuity "
            "for a term of years. The gift is the value transferred less the present value of the "
            "retained annuity, computed at the Section 7520 rate. Set the annuity so those two "
            "figures are nearly equal and the taxable gift approaches zero, which is why the "
            "structure is usually described as zeroed out.</p>"
            "<p>Everything the assets earn above the Section 7520 hurdle rate passes to the "
            "remainder beneficiaries free of gift tax. On a business interest that appreciates "
            "sharply, or one that receives a sale premium during the term, this can move a very "
            "large amount at no gift tax cost.</p>"
            "<p>Two limitations. If the grantor dies during the term, the assets are pulled back "
            "into the estate and the exercise was neutral rather than harmful, which argues for "
            "shorter terms and rolling GRATs. And the generation-skipping exemption cannot be "
            "allocated effectively during the term because of the estate tax inclusion period "
            "rules, so a GRAT is a poor vehicle for multigenerational planning.</p>"
        ),
        (
            "Sales to Intentionally Defective Grantor Trusts",
            "<p>The alternative, and usually the stronger one for an operating business. The "
            "owner gifts seed capital to an irrevocable grantor trust, commonly around 10 percent "
            "of the intended transaction, then sells business interests to the trust for a "
            "promissory note bearing interest at the applicable federal rate.</p>"
            "<p>Because the trust is a grantor trust for income tax purposes, the sale is "
            "disregarded: no capital gain on the sale, and no interest income on the note. The "
            "trust services the note from distributions on the transferred interest, and "
            "everything the business earns above the note rate accumulates in the trust outside "
            "the estate.</p>"
            "<p>The grantor also continues to pay the income tax on the trust's earnings, which "
            "further reduces the estate without being treated as an additional gift. Over a "
            "decade on a profitable business this tax burn is often the largest single element of "
            "the transfer.</p>"
            "<p>Compared with a GRAT: the note rate is typically lower than the Section 7520 "
            "hurdle, there is no mortality risk built into the structure, and generation-skipping "
            "exemption can be allocated at the outset. The cost is that a seed gift is required "
            "and the technique rests on long-standing practice rather than a statute written for "
            "it.</p>"
        ),
        (
            "Family Limited Partnerships and Valuation Discounts",
            "<p>Placing business or investment assets in a family limited partnership or manager "
            "managed LLC, then transferring non-controlling, non-marketable interests, supports "
            "valuation discounts for lack of control and lack of marketability. Combined "
            "discounts in the 20 to 35 percent range are commonly sustained with a proper "
            "appraisal, which means $10 million of assets can be transferred at a reported value "
            "closer to $7 million.</p>"
            "<p>The technique attracts scrutiny, and the case law is unforgiving where the "
            "formalities are absent. Courts have applied Section 2036 to pull assets back into "
            "the estate where the partnership had no legitimate non-tax purpose, where the "
            "decedent retained use of the assets, where personal expenses were paid from "
            "partnership accounts, or where funding happened on a deathbed.</p>"
            "<p>What survives review: a documented business reason such as consolidated "
            "management or creditor protection, funding while the owner is healthy and active, "
            "respect for the entity's formalities, pro rata distributions, and assets the owner "
            "does not personally use. Getting this right is the same discipline described in "
            "<a href=\"/holding-company-vs-operating-company/\">holding company versus operating "
            "company</a>.</p>"
        ),
        (
            "Preferred Partnership Freezes",
            "<p>Where the owner needs continuing cash flow, a recapitalization can split the "
            "entity into a preferred interest with a fixed cumulative return, retained by the "
            "owner, and a growth interest transferred to children or a trust. All appreciation "
            "above the preferred return accrues to the growth interest.</p>"
            "<p>Section 2701 governs this and is unforgiving. If the retained preferred interest "
            "does not carry a qualified payment right, meaning a fixed cumulative distribution "
            "that is actually paid, the retained interest is valued at zero for gift tax "
            "purposes and the entire entity is treated as gifted. Distributions must be made, not "
            "merely accrued indefinitely, and the preferred rate must be supportable by "
            "appraisal.</p>"
            "<p>Done correctly it is the most flexible freeze available to an owner who is not "
            "ready to give up income, which is a common position for someone five years from "
            "an exit.</p>"
        ),
        (
            "The Basis Trade-Off Nobody Mentions",
            "<p>Assets held at death receive a basis step-up to fair market value. Assets gifted "
            "during life carry the donor's basis over to the recipient. Freezing therefore trades "
            "an estate tax benefit for an income tax cost, and the trade is only worthwhile where "
            "estate tax is actually in play.</p>"
            "<p>For a couple with a $12 million estate and a $30 million combined exemption, "
            "gifting appreciated business interests can be a net negative: no estate tax was "
            "owed, and the children inherit a low basis they will pay capital gains on when they "
            "sell. For an estate expected to reach $50 million after a liquidity event, the "
            "estate tax at 40 percent dominates the basis question decisively.</p>"
            "<p>The calculation depends on projected estate size, the expected holding period "
            "after the transfer, and whether the asset will be sold at all. It is the first thing "
            "to run, before selecting a technique.</p>"
        ),
        (
            "Sequencing a Freeze With an Exit",
            "<p>Value is lowest, and the appraisal least contestable, before a sale process "
            "begins. Once a letter of intent exists, an appraiser cannot credibly value the "
            "interest below the price a real buyer has offered, and discounts for marketability "
            "become difficult to defend on an asset with a documented market.</p>"
            "<p>The practical sequence is to complete transfers two to three years before a "
            "process, file a gift tax return with adequate disclosure so the three-year statute "
            "of limitations on valuation begins running, keep contemporaneous appraisals, and "
            "only then run the sale. Owners who reverse that order pay tax on the growth they "
            "meant to transfer, which is the most expensive avoidable outcome in the whole "
            "<a href=\"/exit-tax-planning-business-owners/\">exit planning sequence</a>.</p>"
        ),
    ],
    takeaways=[
        "A freeze fixes today's value in the estate and moves future growth to the next generation.",
        "The 2026 exemption is $15 million per person, so freezing matters most for growing estates.",
        "GRATs carry mortality risk and cannot use generation-skipping exemption during the term.",
        "Sales to grantor trusts avoid gain, use the lower note rate, and let the grantor pay the tax.",
        "Partnership discounts of 20 to 35 percent survive review only with real formalities.",
        "Gifting forfeits the basis step-up, so run that comparison before choosing a technique.",
    ],
    faqs=[
        (
            "What is the estate tax exemption in 2026?",
            "<p>$15 million per person, $30 million for a married couple with portability, "
            "indexed for inflation in later years. The 2025 act set that level and removed the "
            "scheduled reduction. Amounts above it are taxed at 40 percent, and several states "
            "impose their own estate tax at much lower thresholds.</p>",
        ),
        (
            "GRAT or sale to a grantor trust, which is better for a business owner?",
            "<p>For an operating business expected to appreciate substantially, the sale to an "
            "intentionally defective grantor trust is usually stronger: the hurdle rate is lower, "
            "there is no mortality risk in the structure, and generation-skipping exemption can "
            "be allocated immediately. GRATs are attractive where the owner has little remaining "
            "exemption to spend on a seed gift.</p>",
        ),
        (
            "Are valuation discounts still allowed?",
            "<p>Yes. Discounts for lack of control and lack of marketability remain available "
            "with a qualified appraisal. What fails is the structure behind them: entities with "
            "no business purpose, commingled personal spending, disregarded formalities, or "
            "deathbed funding. The discount follows a real entity, not a paper one.</p>",
        ),
        (
            "Can I still control the business after a freeze?",
            "<p>Generally yes. Control can be retained through a small general partner or manager "
            "interest, or through voting shares while non-voting shares are transferred. What the "
            "owner cannot do is retain beneficial enjoyment of the transferred value, which is "
            "what Section 2036 targets and what pulls assets back into the estate.</p>",
        ),
        (
            "How long before a sale should a freeze happen?",
            "<p>Two to three years is the comfortable range. The objective is to complete the "
            "transfer, file the gift tax return with adequate disclosure, and let the valuation "
            "statute run before a buyer establishes a market price that makes the earlier "
            "appraisal look low.</p>",
        ),
    ],
)

CLUSTER = Cluster(
    key="exit",
    slug=P,
    label="Exit and Succession Tax Planning",
    title="Exit Tax Planning for Business Owners: Keep More When You Sell",
    description=(
        "A sequenced guide to the tax on a business exit: capital gain math, deal "
        "structure, QSBS, installment sales, opportunity zones, charitable trusts, "
        "entity separation, and estate freezes, with the lead time each one needs."
    ),
    h1="Exit Tax Planning for Business Owners: How to Keep More When You Sell",
    subtitle=(
        "The tax on a sale is decided in the years before the letter of intent, not "
        "in the closing documents."
    ),
    lead=(
        "Exit tax planning is the work of arranging ownership, entity structure, and timing so "
        "that a sale, transfer, or succession produces the lowest defensible tax, and it is "
        "almost entirely front-loaded. A business owner selling for $6 million faces a federal "
        "capital gain tax of roughly $1.4 million before state tax, and the available reductions, "
        "the Section 1202 exclusion, installment reporting, opportunity zone reinvestment, "
        "charitable structures, and estate freezes, all depend on decisions made one to five "
        "years earlier. By the time a letter of intent is signed, most of the outcome is fixed."
    ),
    keywords=[
        "exit tax planning business owners",
        "reduce taxes when selling a business",
        "business sale capital gains tax",
        "succession tax planning",
        "qsbs installment sale opportunity zone",
    ],
    body=[
        (
            "What Exit Planning Is, and When It Has to Start",
            "<p>Exit planning is often described as a valuation exercise. From a tax perspective "
            "it is a sequencing exercise. Every meaningful strategy on this page has a waiting "
            "period built into it, and the length of that waiting period is what determines when "
            "the work has to begin.</p>"
            "<div style=\"overflow-x:auto;\">"
            "<table>"
            "<thead><tr><th>Strategy</th><th>Lead time required</th><th>Still possible at signing?</th></tr></thead>"
            "<tbody>"
            "<tr><td>Section 1202 exclusion</td><td>5 years of stock ownership</td><td>No</td></tr>"
            "<tr><td>C to S conversion, built-in gains</td><td>5 years</td><td>No</td></tr>"
            "<tr><td>Trust funding for stacking or freeze</td><td>2 to 3 years</td><td>No</td></tr>"
            "<tr><td>Real estate separation</td><td>2 to 3 years</td><td>No</td></tr>"
            "<tr><td>Charitable remainder trust</td><td>Before any binding agreement</td><td>No</td></tr>"
            "<tr><td>F reorganization</td><td>Weeks to months</td><td>Usually</td></tr>"
            "<tr><td>Installment structure</td><td>Negotiated in the deal</td><td>Yes</td></tr>"
            "<tr><td>Opportunity zone reinvestment</td><td>180 days after closing</td><td>Yes</td></tr>"
            "</tbody></table></div>"
            "<p>Only the bottom three survive a late start. An owner who begins tax planning when "
            "the banker is engaged has already given up the largest items on the list, which is "
            "why we treat five years out as the beginning of the window and twelve months out as "
            "the last point at which structure can still be changed meaningfully.</p>"
        ),
        (
            "What the Tax Actually Is",
            "<p>Start with the number being reduced. A long-term capital gain on the sale of a "
            "business is taxed at 20 percent federal at the top bracket, plus the 3.8 percent net "
            "investment income tax where it applies, plus state income tax, which ranges from "
            "zero to over 13 percent. On an asset sale, portions of the price are taxed worse: "
            "depreciation recapture on equipment is ordinary income at up to 37 percent, "
            "unrecaptured Section 1250 gain on buildings is 25 percent, and amounts allocated to "
            "a non-competition agreement are ordinary income.</p>"
            "<div style=\"overflow-x:auto;\">"
            "<table>"
            "<thead><tr><th>Component</th><th>Federal rate</th><th>Notes</th></tr></thead>"
            "<tbody>"
            "<tr><td>Long-term capital gain</td><td>20%</td><td>Top bracket</td></tr>"
            "<tr><td>Net investment income tax</td><td>3.8%</td><td>May not apply if materially participating</td></tr>"
            "<tr><td>Unrecaptured Section 1250</td><td>25%</td><td>Buildings</td></tr>"
            "<tr><td>Section 1245 recapture</td><td>Up to 37%</td><td>Equipment, ordinary</td></tr>"
            "<tr><td>Non-compete allocation</td><td>Up to 37%</td><td>Ordinary income</td></tr>"
            "<tr><td>C corporation entity tax</td><td>21%</td><td>Then taxed again on distribution</td></tr>"
            "</tbody></table></div>"
            "<p>One nuance is worth knowing before assuming the surtax applies. Under Section "
            "1411, gain from the disposition of an interest in a business in which the seller "
            "materially participated can fall outside net investment income, to the extent "
            "determined under the deemed asset sale rules. On a $6 million gain that distinction "
            "alone is worth up to $228,000.</p>"
        ),
        (
            "Structure Decides the Answer Before Any Strategy Applies",
            "<p>The first fork is asset sale versus equity sale. The buyer wants assets, for a "
            "stepped-up basis to depreciate and to leave unknown liabilities behind. The seller "
            "wants equity, for one level of tax at capital rates. Between a C corporation asset "
            "sale and a clean stock sale the effective federal rate can differ by fifteen points "
            "or more on the same price.</p>"
            "<p>The structures that resolve this are well established. An F reorganization with "
            "an LLC drop-down gives an S corporation seller a single level of tax while the buyer "
            "still receives asset treatment, and it makes rollover equity clean where a private "
            "equity buyer wants the seller to retain a stake. A Section 338(h)(10) or 336(e) "
            "election achieves a similar result in other fact patterns, at a price the seller "
            "should be paid for. Personal goodwill can pull part of a C corporation sale out of "
            "the double tax where the owner was never bound by a company non-compete.</p>"
            "<p>The full comparison, including built-in gains exposure after a C to S conversion "
            "and how purchase price allocation is negotiated, is in "
            "<a href=\"/structuring-your-business-for-sale/\">how to structure your business for "
            "sale</a>.</p>"
        ),
        (
            "Excluding the Gain: Section 1202",
            "<p>The largest single reduction available is exclusion rather than deferral. "
            "Qualified small business stock under Section 1202 allows an individual to exclude "
            "the greater of $10 million, raised to $15 million for stock issued after July 4, "
            "2025, or 10 times basis, on stock in a domestic C corporation held more than five "
            "years. The excluded gain is not subject to the net investment income tax and carries "
            "no alternative minimum tax preference.</p>"
            "<p>Three facts govern whether it is available. The issuer must be a C corporation, "
            "so S corporation owners are outside it unless they convert and start a new clock. "
            "The corporation must have had gross assets under the ceiling at issuance and must "
            "have used 80 percent of its assets in an active qualified business, which excludes "
            "health, law, accounting, consulting, financial services, and restaurants by statute. "
            "And the cap is per taxpayer, so gifts to non-grantor trusts made well before a sale "
            "multiply it.</p>"
            "<p>The details, including what the 2025 act changed and how stacking is documented, "
            "are in the <a href=\"/qsbs-exclusion-section-1202/\">Section 1202 guide</a>.</p>"
        ),
        (
            "Spreading the Gain: Installment Sales and Seller Notes",
            "<p>Where exclusion is unavailable, the next lever is timing. Under Section 453, a "
            "seller who receives payments after the year of sale reports gain as principal is "
            "collected, using a gross profit ratio fixed at closing. Spread across five years, a "
            "$4 million gain can occupy lower brackets, reduce surtax exposure in individual "
            "years, and keep the deferred tax invested.</p>"
            "<p>The limits are specific. Depreciation recapture is taxed in full in the year of "
            "sale regardless of cash received. Inventory, dealer property, and publicly traded "
            "securities are excluded. Above $5 million of outstanding installment obligations, "
            "Section 453A charges interest on the deferred tax, and pledging the note as loan "
            "collateral accelerates the gain.</p>"
            "<p>Seller financing is the same mechanism approached as a deal term rather than a "
            "tax election. Carrying 10 to 30 percent of the price widens the buyer pool, usually "
            "raises the total price, and produces an interest stream that is ordinary income. The "
            "note has to carry at least the applicable federal rate or interest is imputed, "
            "converting capital gain into ordinary income and, under the original issue discount "
            "rules, accruing it before cash arrives.</p>"
            "<p>Both are covered in detail in the "
            "<a href=\"/installment-sale-tax-strategy/\">installment sale guide</a> and in "
            "<a href=\"/seller-financing-tax-strategy/\">seller financing tax strategy</a>.</p>"
        ),
        (
            "Deferring and Eliminating: Opportunity Zones",
            "<p>Rolling capital gain into a qualified opportunity fund within 180 days defers tax "
            "on the rolled amount and, after a ten-year hold, eliminates tax on all appreciation "
            "inside the fund. Only the gain has to be reinvested, not the full proceeds, which "
            "distinguishes it from a 1031 exchange and makes it available on the sale of an "
            "operating business rather than only real property.</p>"
            "<p>Two timing facts matter in 2026. Deferred gain under the original program is "
            "recognized on December 31, 2026, so a 2026 investment gets almost no deferral "
            "benefit and should be judged solely on the ten-year elimination. And the 2025 act "
            "made the program permanent with new designations effective in 2027, a rolling "
            "five-year deferral, a 10 percent basis step-up at five years, and a 30 percent "
            "step-up for rural funds. A late-2026 closing may have a 180-day window that reaches "
            "into the new regime, which is worth checking before a closing date is set. The "
            "details are in "
            "<a href=\"/opportunity-zone-investing-after-business-sale/\">opportunity zone "
            "investing after a business sale</a>.</p>"
        ),
        (
            "Removing the Gain: Charitable Structures",
            "<p>A charitable remainder trust is exempt from income tax, so a business interest "
            "contributed before any binding sale agreement can be sold inside the trust without "
            "capital gains tax at the sale. The full pre-tax amount is reinvested, the donor "
            "takes an income stream for life or a term, and an income tax deduction is allowed "
            "for the present value of the remainder passing to charity.</p>"
            "<p>The structure carries hard constraints. S corporation stock cannot be contributed, "
            "because a charitable remainder trust is not an eligible shareholder and the "
            "contribution would terminate the S election. Interests producing unrelated business "
            "taxable income face a 100 percent excise tax on that income. And contributing after "
            "a binding agreement exists collapses the plan under the assignment of income "
            "doctrine.</p>"
            "<p>Where a trust does not fit, a donor advised fund receiving cash in the year of "
            "sale still produces a deduction against the gain, and appreciated non-operating "
            "assets can often be given directly. The full analysis is in the "
            "<a href=\"/charitable-remainder-trust-business-exit/\">charitable remainder trust "
            "guide</a>.</p>"
        ),
        (
            "Restructuring Before the Sale",
            "<p>Two separations pay for themselves repeatedly, and both need years rather than "
            "months.</p>"
            "<p><strong>Real estate.</strong> A building held inside the operating company gets "
            "valued at an operating multiple in a sale, which usually undervalues it, and cannot "
            "be exchanged under Section 1031 as part of a business sale. Held separately, the "
            "owner can sell the business, keep the property, lease it back at market rent, and "
            "continue to benefit from any "
            "<a href=\"/cost-segregation-study/\">cost segregation study</a> already performed. "
            "Distributing appreciated property out of a corporation immediately before a sale is "
            "a taxable event at fair market value, so this is an early move or none at all.</p>"
            "<p><strong>Entity layering.</strong> Separating intellectual property, equipment, "
            "and management functions gives the seller assets that can be retained, licensed, or "
            "sold separately, and it isolates the operating risk a buyer is diligencing. The "
            "operating rationale for the same structure is in "
            "<a href=\"/holding-company-vs-operating-company/\">holding company versus operating "
            "company</a>, and the broader framework in our "
            "<a href=\"/entity-structuring-business-owners/\">entity structuring guide</a>.</p>"
        ),
        (
            "Passing the Business On: Estate Freezes",
            "<p>Not every exit is a sale. Where the business is going to family, or where a sale "
            "will create an estate well above the exemption, the objective shifts from reducing "
            "capital gain to moving future appreciation out of the estate at today's value.</p>"
            "<p>The 2026 federal exemption is $15 million per person and $30 million per couple, "
            "made permanent by the 2025 act, with a 40 percent rate above it. A business growing "
            "at 15 percent a year passes that threshold quickly, and several states impose their "
            "own estate tax at far lower levels.</p>"
            "<p>The techniques are a grantor retained annuity trust, which transfers appreciation "
            "above the Section 7520 hurdle at almost no gift tax cost; an installment sale to an "
            "intentionally defective grantor trust, which avoids gain on the sale, uses the lower "
            "applicable federal rate, and lets the grantor keep paying the income tax as a "
            "further transfer; and family limited partnerships, where non-controlling, "
            "non-marketable interests support discounts of 20 to 35 percent with a proper "
            "appraisal and real formalities.</p>"
            "<p>All of them work best before a buyer establishes a market price, and all trade "
            "the basis step-up at death for the estate tax saving, a comparison that has to be "
            "run first. See "
            "<a href=\"/estate-freeze-strategies-business-owners/\">estate freeze strategies</a>."
            "</p>"
        ),
        (
            "How These Combine",
            "<p>The strategies are not alternatives, and the interactions are where the planning "
            "value sits.</p>"
            "<p>A seller with qualifying stock might exclude $15 million under Section 1202, roll "
            "a portion of the excess gain into an opportunity fund, take an installment note for "
            "another portion to spread the remainder across years, and have gifted shares to "
            "non-grantor trusts three years earlier so the exclusion applies four times over.</p>"
            "<p>Some combinations conflict. Staying a C corporation to preserve Section 1202 "
            "means paying entity level tax on operating income for years first. Contributing "
            "stock to a charitable remainder trust removes it from the Section 1202 calculation. "
            "Gifting interests to a freeze trust reduces what the owner personally holds at sale, "
            "which changes the exclusion math. Each of these is resolvable, but only with a model "
            "that runs the alternatives against the actual numbers.</p>"
        ),
        (
            "What This Costs and How We Work",
            "<p>Our tax advisory engagement is $7,800, quoted flat in writing before any work "
            "begins, with split payment available. It covers the analysis, the projections, and "
            "the implementation steps with deadlines attached. Cost segregation studies are $1 "
            "per square foot subject to a $2,000 minimum, entity returns are $1,500, personal "
            "returns are $1,000, and amended returns are $2,500 each. Full detail is on the "
            "<a href=\"/pricing/\">pricing page</a>, and examples of completed work are in our "
            "<a href=\"/case-studies/\">case studies</a>.</p>"
            "<p>Exit work usually begins with a three-year lookback and a current-structure "
            "review, because the answer to what should change depends on what has already been "
            "done. If a sale is more than a year away, the sequence above is the agenda. If a "
            "letter of intent is already signed, the work narrows to deal structure, allocation, "
            "installment terms, and reinvestment, which is still worth doing and is worth "
            "considerably less than the same conversation two years earlier.</p>"
        ),
    ],
    takeaways=[
        "Most of the tax on a sale is determined one to five years before the letter of intent.",
        "Asset versus equity structure can move the effective federal rate by fifteen points.",
        "Section 1202 excludes gain permanently, but only for C corporation stock held five years.",
        "Installment reporting spreads gain; recapture is still taxed in the year of sale.",
        "Opportunity zones in 2026 are an appreciation play, not a deferral play.",
        "A charitable remainder trust cannot hold S corporation stock, which rules out most operators.",
        "Freezes move future growth out of the estate, at the cost of the basis step-up at death.",
    ],
    faqs=[
        (
            "How much tax will I pay when I sell my business?",
            "<p>On a clean equity sale, roughly 23.8 percent federally at the top bracket, being "
            "20 percent capital gain plus the 3.8 percent net investment income tax where it "
            "applies, plus state tax of zero to over 13 percent. An asset sale is higher because "
            "depreciation recapture and any non-competition allocation are ordinary income, and a "
            "C corporation asset sale is higher again because the proceeds are taxed at the "
            "entity and again on distribution.</p>",
        ),
        (
            "When should I start exit tax planning?",
            "<p>Five years before a target sale date if the business might qualify for the "
            "Section 1202 exclusion or needs a C to S conversion, because both carry five-year "
            "waiting periods. Three years is enough for trust funding, real estate separation, "
            "and estate freezes. Twelve months still allows deal structure work. After a letter "
            "of intent, the remaining levers are allocation, installment terms, and "
            "reinvestment.</p>",
        ),
        (
            "Can I avoid capital gains tax entirely when selling my business?",
            "<p>Sometimes, and only through specific provisions. A full Section 1202 exclusion "
            "eliminates federal tax on qualifying gain up to the cap, and stacking across "
            "non-grantor trusts can cover a larger amount. A charitable remainder trust avoids "
            "tax at the sale but carries the gain out through distributions over time and gives "
            "the remainder to charity. An opportunity fund eliminates tax on future appreciation "
            "rather than on the original gain. Anything presented as eliminating the tax without "
            "one of these mechanisms deserves scrutiny.</p>",
        ),
        (
            "Is an installment sale better than taking cash at closing?",
            "<p>It depends on rates, credit risk, and what else is happening in those years. "
            "Spreading gain helps where it moves income into lower brackets, where a state "
            "residency change is planned, or where losses will arrive later. It hurts where the "
            "buyer is a poor credit, where rates are expected to rise, or where the outstanding "
            "balance exceeds $5 million and the Section 453A interest charge applies without "
            "offsetting benefit.</p>",
        ),
        (
            "What happens if my business is an S corporation?",
            "<p>Several strategies narrow. Section 1202 is unavailable without converting to a C "
            "corporation and waiting five years, and a charitable remainder trust cannot hold the "
            "stock at all. What remains strong is the F reorganization for deal structure, "
            "installment reporting, opportunity zone reinvestment after the sale, real estate "
            "separation, and the full range of estate freeze techniques.</p>",
        ),
        (
            "Do I still need this if my estate is under the exemption?",
            "<p>The estate freeze portion may not apply, but the capital gain portion still does, "
            "and it is usually the larger number. A $6 million sale produces roughly $1.4 million "
            "of federal capital gains tax regardless of estate size. Freezing becomes relevant "
            "when the post-sale estate is projected above $15 million per person, which a "
            "liquidity event frequently causes.</p>",
        ),
        (
            "Can you work with my existing CPA?",
            "<p>Yes, and it is common on exit work. We produce the structure analysis, "
            "projections, and implementation steps, and the existing preparer files the returns. "
            "It works well when the split is explicit and both parties work from the same "
            "projections, as described in "
            "<a href=\"/tax-planning-vs-tax-preparation/\">tax planning versus tax "
            "preparation</a>.</p>",
        ),
    ],
    spokes=[
        QSBS,
        INSTALLMENT,
        SELLER_FIN,
        STRUCTURE,
        OZ,
        CRT,
        FREEZE,
    ],
)
