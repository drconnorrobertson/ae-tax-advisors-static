"""Batch: cost segregation by property type (asset classes not yet covered)."""

from blog_gen import write_all

C = "Cost Segregation"
D = "2026-08-10"

ARTICLES = [
{
"slug": "cost-segregation-warehouse-industrial-buildings",
"title": "Cost Segregation for Warehouses and Industrial Buildings: What Actually Reclassifies",
"meta_title": "Cost Segregation for Warehouses and Industrial Buildings (2026 Guide) | AE Tax Advisors",
"meta_desc": "Warehouses reclassify 18 to 30 percent of basis. How racking, dock equipment, specialty power, and paving are treated under IRC Sec. 168 in 2026.",
"category": C, "date": D,
"intro": [
"Warehouses have a reputation as poor cost segregation candidates. The building is a shell, the argument goes, so there is nothing to reclassify. That reputation is half right and expensive to accept without testing.",
"A bare distribution shell may land at 12% to 15% reclassification. But the moment a warehouse is fitted out for a real operation, with racking, dock equipment, dedicated power, and heavy site work, studies routinely reach 20% to 30%. On a $12 million building, the difference between assuming and testing is roughly $1.5 million of first-year deduction.",
],
"sections": [
("Why the Shell Assumption Fails", [
"The shell itself really is mostly 39-year property under IRC Sec. 168(e)(2)(B). Tilt-up panels, structural steel, roof, and slab are structure and stay structure.",
"What changes the math is everything bolted to, poured into, or run through that shell. Industrial tenants are equipment-heavy by definition, and the tax code classifies by function rather than by whether something is attached to a building.",
]),
("Racking Is Often the Single Largest Item", [
"Pallet racking, cantilever racking, mezzanine platforms, and conveyor systems are five-year personal property under IRC Sec. 168(e)(3)(B). This holds even when racking is anchored to the slab, because anchoring for stability does not convert equipment into a structural component.",
"The distinction that matters is whether the mezzanine is a structural floor or an equipment platform. A bolted steel mezzanine supporting shelving, removable without damaging the building, is equipment. A poured second floor integral to the structure is not. Documentation of the installation method decides this, which is why the study should be built from construction detail rather than from the closing statement.",
"In a fitted-out fulfillment building, racking and material handling alone can represent 15% to 22% of depreciable basis.",
]),
("Dedicated Power and Specialty Systems", [
"Warehouses with automation, refrigeration, battery charging stations for forklifts, or compressed air run substantial dedicated electrical and mechanical infrastructure. Under the functional analysis reflected in Treasury Regulation Sec. 1.48-1(e)(2), utilities serving specific equipment rather than the building generally are classified with the equipment they serve.",
"That means the transformer, panels, conduit, and wiring feeding an automated sortation line follow the sortation line to five-year treatment. General lighting, office HVAC, and life safety systems remain structural.",
"Cold storage is a category of its own. Refrigeration equipment, insulated panel systems, and the specialized floors and vapor barriers supporting them push reclassification well above a dry warehouse, frequently past 35%.",
]),
("Site Work Is Larger Than It Looks", [
"Fifteen-year land improvements under IRC Sec. 168(e)(3)(C) run high on industrial sites, commonly 8% to 14%. Truck courts require heavy-duty paving engineered for tractor trailer loads, which is expensive per square foot and often covers more acreage than the building footprint.",
"Add trailer parking, concrete dolly pads, site lighting on poles, security fencing and gates, retention ponds, storm drainage, and landscaping buffers required by zoning. On a distribution facility with a 130-foot truck court, site work is rarely a rounding error.",
]),
("Dock Equipment and Building Fit-Out", [
"Dock levelers, dock seals and shelters, bumpers, vehicle restraints, and dock lights are five-year equipment. So are high-speed and air curtain doors serving operations, though sectional overhead doors forming the building envelope are typically structural.",
"Office build-out inside the shell contributes as well. Carpet, decorative millwork, dedicated office power and data cabling, and specialty finishes reclassify at the same rates they would in any office space, and a 12,000 square foot office within a warehouse is a meaningful basis component.",
]),
("Worked Example: Fitted Distribution Building", [
"An investor acquires a 180,000 square foot distribution building for $14,600,000. Land is allocated at $2,100,000, leaving $12,500,000 depreciable. The study identifies five-year property of $2,375,000 (19%), seven-year property of $250,000 (2%), fifteen-year land improvements of $1,375,000 (11%), and 39-year structure of $8,500,000 (68%).",
"Reclassified basis of $4,000,000 is deductible in year one under IRC Sec. 168(k). Structure contributes $218,000. First-year depreciation totals approximately $4,218,000 against $320,513 on a straight-line 39-year schedule.",
"At a 37% marginal rate, that is roughly $1.44 million of deferred federal tax in a single year on a property most owners would have written off as a poor candidate.",
]),
("The Tenant Improvement Question", [
"Industrial landlords should separate what they funded from what the tenant funded before commissioning a study. Improvements paid for by the landlord are the landlord's depreciable basis. Improvements paid for by the tenant generally are not, regardless of who benefits at lease end.",
"Landlord-funded interior improvements to a nonresidential building may also qualify as qualified improvement property under IRC Sec. 168(e)(6), which carries its own 15-year life and bonus eligibility. Getting the QIP split right often matters more than the personal property split on a heavy build-out.",
]),
],
"faqs": [
("Is cost segregation worth it on a plain warehouse shell?",
 "Usually yes, though the percentage is lower. A bare shell may reclassify only 12% to 15%, but land improvements on industrial sites are large and the absolute dollars still tend to justify a study on buildings above roughly $1.5 million. The answer changes entirely once racking, dock equipment, or specialty power are present."),
("Is pallet racking really five-year property if it is bolted to the floor?",
 "Yes. Anchoring equipment for stability does not make it a structural component. The test under IRC Sec. 168 is function, not attachment. Racking serves the storage operation, not the building, and is treated as five-year personal property."),
("How is cold storage treated differently?",
 "Cold storage reclassifies far higher, frequently above 35%. Refrigeration equipment, dedicated power, insulated panel systems, and the specialized floor assemblies serving them are equipment or equipment-related rather than general building structure."),
("Does a truck court count as a land improvement?",
 "Yes. Heavy-duty paving, dolly pads, trailer parking, site lighting, fencing, and drainage are 15-year land improvements under IRC Sec. 168(e)(3)(C) and are fully bonus eligible. On distribution properties this class alone often exceeds 10% of depreciable basis."),
("Can I still do a study on a warehouse I bought three years ago?",
 "Yes. A look-back study paired with Form 3115 lets you claim the entire missed deduction in the current year as a Sec. 481(a) adjustment, with no amended returns required. Nothing is lost by having waited, though the time value of the deferral is."),
],
"related": [
("/blog/cost-segregation-commercial-property-guide/", "Cost segregation for commercial property: the complete owner guide"),
("/blog/form-3115-cost-segregation-catch-up/", "Form 3115 and catch-up depreciation on properties you already own"),
("/equipment-leasing/", "Equipment leasing and Section 179 planning"),
],
"cta_head": "Test the Assumption Before You Skip the Study",
"cta_body": "Send us the closing statement and the fit-out detail on your industrial property. We will size the reclassification and tell you plainly whether a study pays for itself.",
},

{
"slug": "cost-segregation-retail-strip-centers",
"title": "Cost Segregation for Retail Strip Centers: Where the 25 Percent Comes From",
"meta_title": "Cost Segregation for Retail Strip Centers (2026 Guide) | AE Tax Advisors",
"meta_desc": "Strip centers commonly reclassify 22 to 30 percent of basis. How parking, pylon signage, storefronts, and tenant build-out are classified in 2026.",
"category": C, "date": D,
"intro": [
"Retail strip centers are among the most consistently rewarding cost segregation candidates in commercial real estate, and the reason is geometry. A strip center devotes more land to parking than to building, and parking is a 15-year asset.",
"Typical studies land between 22% and 30% of depreciable basis. Centers with heavy tenant build-out, drive-through pads, or extensive signage programs run higher.",
],
"sections": [
("Parking Fields Drive the Result", [
"A neighborhood center with a 4.5 to 1 parking ratio has more depreciable dollars in asphalt, base course, curbing, striping, wheel stops, and lighting than most owners expect. All of it is 15-year land improvement property under IRC Sec. 168(e)(3)(C), and all of it is bonus eligible.",
"Add site drainage, storm inlets, retention basins, sidewalks outside the building line, landscape islands, irrigation, and trash enclosures. Land improvements on a strip center commonly reach 14% to 20% of depreciable basis on their own, which is roughly double what an office tower produces.",
]),
("Signage Is Frequently Missed", [
"Pylon and monument signs are among the most commonly misclassified items on retail properties. The sign cabinet, faces, internal illumination, and electrical service to the sign are five-year personal property. The concrete foundation and any masonry base are typically 15-year land improvements.",
"A single lighted pylon on a highway frontage can run $80,000 to $200,000 installed. Multiply that across a center with multiple monument signs and directional signage and the class becomes material rather than incidental.",
]),
("Storefronts and Tenant Build-Out", [
"Interior finish work in retail space reclassifies well. Decorative lighting, accent millwork, vinyl and carpet flooring, movable partitions, counters and casework, specialty ceiling treatments, and dedicated power and data serving tenant equipment are five-year property.",
"Storefront glazing itself is generally structural, but the awnings, canopies, and decorative facade elements that give a center its character often are not, particularly when they are ornamental rather than load bearing or weather protective for the structure.",
"Landlord-funded improvements to the interior of a nonresidential building also qualify as qualified improvement property under IRC Sec. 168(e)(6) when placed in service after the building was first placed in service. QIP carries a 15-year life and full bonus eligibility, which means a large share of a landlord's TI allowance is recoverable quickly even where it is not personal property.",
]),
("Pad Sites and Drive-Throughs", [
"Outparcels with quick service restaurants change the analysis meaningfully. Drive-through lanes, order canopies, menu boards, preview boards, speaker systems, and directional striping are a mix of five-year equipment and 15-year improvements.",
"Where the landlord built the pad and leases it improved, that basis belongs to the landlord. Where the tenant built it under a ground lease, it generally does not. This is worth confirming from the lease before a study begins, because misattributed pad improvements are one of the more common quality issues in cheap studies.",
]),
("Worked Example: Neighborhood Center", [
"An investor acquires a 46,000 square foot neighborhood center for $9,400,000. Land is allocated at $1,900,000, leaving $7,500,000 depreciable. The study finds five-year property of $825,000 (11%), fifteen-year land improvements of $1,275,000 (17%), and 39-year structure of $5,400,000 (72%).",
"Reclassified basis of $2,100,000 is deductible in year one under IRC Sec. 168(k), plus $138,462 of structural depreciation, for approximately $2,238,462 in year one against $192,308 on a straight 39-year schedule.",
"At a 37% marginal rate that is roughly $756,000 of federal tax deferred in the first year.",
]),
("Passive Loss Treatment Still Governs", [
"Retail centers are rental activities, so the deduction runs into IRC Sec. 469. Unless you qualify as a real estate professional under IRC Sec. 469(c)(7) or have other passive income to absorb it, a large first-year loss suspends and carries forward rather than offsetting wages.",
"That is not a reason to skip the study. Suspended losses are not lost losses, and they free up the moment other passive income appears or the property is disposed of in a fully taxable transaction. But it does mean the study should be timed against your broader income picture rather than commissioned reflexively at closing.",
]),
("Partial Asset Dispositions on Re-Tenanting", [
"Strip centers turn over. When you demolish a former tenant's build-out to make room for a new one, the remaining basis in what you removed can be written off through a partial asset disposition election under Treasury Regulation Sec. 1.168(i)-8.",
"This election only works if the components were separately identified, which is precisely what a cost segregation study produces. Owners who run studies get a second, recurring benefit every time they re-tenant a space, and owners who do not simply keep depreciating walls that no longer exist.",
]),
],
"faqs": [
("What percentage does a strip center typically reclassify?",
 "Most neighborhood and community centers land between 22% and 30% of depreciable basis. Parking and site work drive the outcome, so a center with a generous parking ratio and multiple pylon signs will sit at the top of that range."),
("Are pylon signs really five-year property?",
 "The sign cabinet, faces, illumination, and dedicated electrical service are five-year personal property. The concrete foundation and masonry base are generally 15-year land improvements. Splitting the two is standard practice in a properly documented study."),
("Can I use the losses against my W2 income?",
 "Generally not. Retail leasing is a rental activity under IRC Sec. 469, so losses are passive unless you qualify as a real estate professional or the loss is absorbed by other passive income. Suspended losses carry forward indefinitely and release on a fully taxable disposition."),
("How is landlord tenant improvement money treated?",
 "Landlord-funded interior improvements to a nonresidential building placed in service after the building generally qualify as qualified improvement property under IRC Sec. 168(e)(6), carrying a 15-year life and full bonus eligibility. Personal property components within the build-out reclassify to five years."),
("What is a partial asset disposition and why does it matter for retail?",
 "It is an election under Treas. Reg. Sec. 1.168(i)-8 to write off the remaining basis in a building component you remove. Because retail spaces are re-tenanted regularly, strip center owners with a component-level study can claim these write-offs repeatedly over a hold period."),
],
"related": [
("/blog/partial-asset-disposition-overlooked-tax-strategy/", "Partial asset dispositions: the overlooked write-off"),
("/blog/passive-activity-loss-rules-for-real-estate-investors/", "Passive activity loss rules for real estate investors"),
("/blog/cost-segregation-commercial-property-guide/", "Cost segregation for commercial property"),
],
"cta_head": "Retail Sites Reclassify Higher Than Owners Expect",
"cta_body": "Send us the site plan and closing detail on your center. We will estimate the five-year and 15-year components and tell you what the first-year deduction looks like against your actual income picture.",
},

{
"slug": "cost-segregation-office-buildings",
"title": "Cost Segregation for Office Buildings: Realistic Expectations and Where the Value Hides",
"meta_title": "Cost Segregation for Office Buildings (2026 Guide) | AE Tax Advisors",
"meta_desc": "Office buildings reclassify 15 to 25 percent of basis. How cabling, tenant finishes, QIP, and parking structures are classified under IRC Sec. 168 in 2026.",
"category": C, "date": D,
"intro": [
"Office buildings sit in the middle of the cost segregation range. They do not produce car wash numbers, and owners who expect 45% reclassification will be disappointed. Well-executed studies typically land between 15% and 25% of depreciable basis.",
"The value in office is concentrated in three places that generic studies routinely undercount: low-voltage infrastructure, tenant finish work, and the qualified improvement property analysis on everything done after the building opened.",
],
"sections": [
("Low-Voltage Infrastructure", [
"Modern office buildings carry substantial data cabling, network equipment rooms, access control systems, security cameras, audiovisual infrastructure, and distributed antenna systems. These are five-year personal property under IRC Sec. 168(e)(3)(B), along with the conduit and pathways dedicated to them.",
"The dedicated power supporting them follows the same treatment. A UPS system and its distribution serving a server room exists to run equipment, not to light the building, and under the functional analysis in Treasury Regulation Sec. 1.48-1(e)(2) it is classified with the equipment it serves.",
"On a technology-heavy office fit-out, low-voltage and its supporting infrastructure alone can reach 6% to 10% of depreciable basis.",
]),
("Tenant Finishes Reclassify Well", [
"Carpet and resilient flooring, decorative and accent lighting, millwork and reception casework, demountable partitions, window treatments, appliances in break rooms, and specialty wall coverings are all five-year property.",
"Movable partition systems deserve particular attention. Where a partition system is genuinely demountable and relocatable without material damage, it is personal property. Where it is drywall on studs, it is structure. On a large floor plate this distinction is worth six figures, and it turns on installation detail that only shows up in the construction documents.",
]),
("Qualified Improvement Property Is Where Office Wins", [
"Any interior improvement to a nonresidential building placed in service after the building was first placed in service generally qualifies as QIP under IRC Sec. 168(e)(6), excluding enlargements, elevators and escalators, and internal structural framework.",
"QIP carries a 15-year recovery period and is fully bonus eligible. For an office owner, this means that a $3 million renovation of floors four through eight is not stuck on a 39-year schedule, even for the portions that are plainly building rather than personal property.",
"Owners who renovated between 2018 and 2020 should confirm this was handled correctly. The CARES Act retroactively fixed the drafting error that had assigned QIP a 39-year life, and returns filed before that correction frequently still carry the wrong schedule. Form 3115 corrects it in the current year without amending.",
]),
("Parking Structures and Site Work", [
"Surface parking is a 15-year land improvement and behaves like any other paving. Structured parking is different and often misunderstood. A freestanding parking garage is generally 15-year land improvement property, while parking integrated into the building envelope is typically part of the 39-year structure.",
"Within either, the equipment is separable. Gate arms, ticket dispensers, license plate readers, payment kiosks, and the controls running them are five-year property regardless of what they sit in.",
]),
("Worked Example: Suburban Office", [
"An investor acquires a 78,000 square foot suburban office building for $11,200,000. Land is allocated at $1,700,000, leaving $9,500,000 depreciable. The study identifies five-year property of $1,235,000 (13%), fifteen-year land improvements of $760,000 (8%), and 39-year structure of $7,505,000 (79%).",
"Reclassified basis of $1,995,000 is deductible in year one under IRC Sec. 168(k), plus $192,436 of structural depreciation, for roughly $2,187,436 against $243,590 on a straight 39-year schedule.",
"That is not a car wash result. On a 37% marginal rate it is still approximately $700,000 of deferred federal tax from a study that costs a small fraction of that.",
]),
("The Vacancy Problem Nobody Models", [
"Office owners carrying vacancy should think carefully about timing. A large first-year passive loss is only useful if there is passive income to absorb it or the owner qualifies as a real estate professional under IRC Sec. 469(c)(7).",
"An owner with a partially vacant building, negative cash flow, and no other passive income may be better served by running the study in the year of stabilization or lease-up rather than at acquisition. The look-back mechanism under Form 3115 preserves the option, so waiting costs nothing but the time value of money and gives you the flexibility to place the deduction where it does work.",
]),
],
"faqs": [
("What percentage does an office building typically reclassify?",
 "Most office studies land between 15% and 25% of depreciable basis. Technology-heavy fit-outs and buildings with substantial surface parking sit at the top of the range. Older buildings with minimal tenant finish and structured parking sit at the bottom."),
("Is data cabling really five-year property?",
 "Yes. Structured cabling, network hardware, access control, camera systems, and the conduit dedicated to them are five-year personal property. The dedicated power serving equipment rooms follows the same treatment under the functional test in Treas. Reg. Sec. 1.48-1(e)(2)."),
("What is qualified improvement property and why does it matter for office?",
 "QIP is interior improvement to a nonresidential building placed in service after the building itself, excluding enlargements, elevators, escalators, and structural framework. It carries a 15-year life with full bonus eligibility, which recovers renovation cost far faster than the 39-year default."),
("Are demountable partitions personal property?",
 "When they are genuinely relocatable without material damage, yes, they are five-year property. Drywall partitions on metal studs are structural. The classification turns on installation method documented in the construction records, not on how the manufacturer markets the product."),
("Should I run the study at acquisition or wait?",
 "It depends on whether you can use the loss. If you have no passive income and do not qualify as a real estate professional, a large first-year loss suspends. A look-back study with Form 3115 lets you claim the full catch-up in a later year when the deduction is usable."),
],
"related": [
("/blog/form-3115-cost-segregation-catch-up/", "Form 3115 and catch-up depreciation"),
("/blog/passive-activity-loss-rules-for-real-estate-investors/", "Passive activity loss rules for investors"),
("/blog/real-estate-professional-status-qualification-guide/", "Qualifying for real estate professional status"),
],
"cta_head": "Office Studies Are About Timing as Much as Percentage",
"cta_body": "We will model the reclassification and, just as importantly, tell you which tax year the deduction should land in. Bring the rent roll and your other income sources.",
},

{
"slug": "cost-segregation-gas-stations-convenience-stores",
"title": "Cost Segregation for Gas Stations and Convenience Stores: A 15-Year Building",
"meta_title": "Cost Segregation for Gas Stations and Convenience Stores (2026) | AE Tax Advisors",
"meta_desc": "Retail motor fuel outlets can depreciate the entire building over 15 years under IRC Sec. 168(e)(3)(E)(iii). How the 50 percent tests work in 2026.",
"category": C, "date": D,
"intro": [
"Gas stations occupy a unique position in the depreciation rules. Under IRC Sec. 168(e)(3)(E)(iii), a qualifying retail motor fuels outlet is 15-year property in its entirety, building included. Not the parking. Not the canopy. The building.",
"This provision is old, well settled, and routinely missed by preparers who default every commercial structure to 39 years. Combined with a component study on the equipment, a fuel outlet can produce one of the fastest cost recovery profiles in commercial real estate.",
],
"sections": [
("The Two Qualifying Tests", [
"A structure qualifies as a retail motor fuels outlet if it meets either of two alternative tests. The first is a size and function test: the property is 1,400 square feet or less, and it is used to a substantial extent in the retail marketing of petroleum products.",
"The second is a revenue test: 50% or more of gross revenues derived from the property are from petroleum sales. This is the test most modern stations rely on, because today's convenience store footprints routinely exceed 1,400 square feet.",
"There is also a third path where 50% or more of the floor space is devoted to petroleum marketing. Any one of the three qualifies the structure. The tests are measured on the facts of the specific property, so a high-volume travel center with a large food operation may fail while a conventional station on the same block passes.",
]),
("Documenting the Revenue Test", [
"The revenue test is where planning matters. Fuel is a high-revenue, low-margin product, which works in the taxpayer's favor because the test is applied to gross revenues rather than gross profit. A station selling $4.2 million of fuel and $1.6 million of in-store merchandise passes comfortably at 72%.",
"Where it gets close is at high-margin food service concepts. A station with a branded quick service restaurant inside can push in-store revenue above the fuel line, particularly in low fuel price years. The classification should be tested against actual gross receipts and documented contemporaneously rather than assumed.",
]),
("What Sits Outside the Building", [
"Even where the building qualifies for 15-year treatment, the equipment is faster. Dispensers, submersible pumps, point-of-sale systems, air and vacuum equipment, car wash equipment on site, and the canopy lighting are five-year personal property under IRC Sec. 168(e)(3)(B).",
"Underground storage tanks and their associated piping, monitoring systems, and containment are generally five-year property as well, since they are equipment serving the fuel operation rather than a structural component of any building.",
"The canopy itself is typically a 15-year land improvement, as is the paving, striping, lighting, signage foundations, and drainage. Pylon sign cabinets and their electrical service are five-year property.",
]),
("Store Fixtures and Coolers", [
"Interior fit-out reclassifies heavily. Walk-in coolers and their refrigeration systems, reach-in cases, gondola shelving, checkout counters, coffee and fountain equipment, food service equipment, security systems, and decorative and accent lighting are five-year property.",
"Walk-in cooler boxes deserve specific mention because they are commonly misclassified as structure when they are freestanding, insulated equipment enclosures assembled inside a building. They are equipment.",
]),
("Worked Example: Single Station", [
"An operator builds a station and convenience store for $3,800,000 including land. Land is $700,000, leaving $3,100,000 depreciable. Fuel revenue is 68% of gross receipts, so the building qualifies as a retail motor fuels outlet.",
"The study identifies five-year property of $1,178,000 (38%), and the remaining $1,922,000 (62%), consisting of the qualifying building, canopy, and site improvements, all falls into 15-year treatment.",
"Because both classes are bonus eligible under IRC Sec. 168(k), essentially the entire $3,100,000 depreciable basis is deductible in year one. At a 37% marginal rate on an owner-operator who materially participates, that is roughly $1,147,000 of federal tax deferred.",
]),
("Operating Business, Not Rental", [
"An owner-operated station is a trade or business, not a rental activity. That means the passive activity analysis under IRC Sec. 469 turns only on material participation under Treasury Regulation Sec. 1.469-5T, and an operator running the site clears the 500-hour test without difficulty.",
"The deduction is therefore non-passive and available against other active income immediately. This is the structural advantage operating businesses hold over rental real estate, and it is why station owners frequently see a larger cash benefit than an apartment owner with a comparable study.",
"Where the station is leased to an unrelated operator, the owner is a landlord and the passive rules apply normally. Where it is leased to an entity the owner controls, the self-rental rules under Treasury Regulation Sec. 1.469-2(f)(6) require careful handling.",
]),
],
"faqs": [
("Can the entire gas station building really be depreciated over 15 years?",
 "Yes, if it qualifies as a retail motor fuels outlet under IRC Sec. 168(e)(3)(E)(iii). The property must be 1,400 square feet or less, or derive 50% or more of gross revenues from petroleum sales, or devote 50% or more of floor space to petroleum marketing. Meeting any one test qualifies the structure."),
("What if my convenience store sells more merchandise than fuel?",
 "Then the revenue test fails and you would need to qualify under the size or floor space test instead. High-volume food service concepts are the usual failure case. The test uses gross revenues, not gross profit, which generally favors fuel given its high sales volume."),
("Are underground storage tanks five-year property?",
 "Generally yes. Tanks, product piping, leak detection and monitoring systems, and containment serve the fuel dispensing operation rather than functioning as a structural component of a building, so they are treated as equipment."),
("Is the canopy 15-year or five-year property?",
 "The canopy structure and its foundations are typically 15-year land improvements. The lighting fixtures, dispensers underneath, and any signage cabinets mounted on it are five-year personal property. A study should split these rather than classify the canopy as a single item."),
("Can I use the deduction against my other income?",
 "If you operate the station yourself, yes. An owner-operated station is a trade or business, so only material participation under Treas. Reg. Sec. 1.469-5T applies and the loss is non-passive. If you lease the station to a third party, standard passive activity rules apply."),
],
"related": [
("/blog/cost-segregation-car-wash-facilities/", "Cost segregation for car washes"),
("/blog/self-rental-rules-business-rents-from-you/", "Self-rental rules when your business rents from you"),
("/blog/irc-section-168-accelerated-depreciation-explained/", "IRC Sec. 168 accelerated depreciation explained"),
],
"cta_head": "Most Station Owners Are on the Wrong Depreciation Schedule",
"cta_body": "If your building is sitting on a 39-year schedule, it may be on the wrong one entirely. Send us the property detail and a revenue summary and we will test whether it qualifies as a retail motor fuels outlet.",
},

{
"slug": "cost-segregation-assisted-living-senior-housing",
"title": "Cost Segregation for Assisted Living and Senior Housing: The 27.5 vs 39 Year Question",
"meta_title": "Cost Segregation for Assisted Living and Senior Housing (2026) | AE Tax Advisors",
"meta_desc": "Senior housing reclassifies 25 to 35 percent of basis. How service level determines 27.5 vs 39 year treatment and what reclassifies in 2026.",
"category": C, "date": D,
"intro": [
"Senior housing produces strong cost segregation results, commonly 25% to 35% of depreciable basis, because these buildings are dense with fixtures, specialty systems, and equipment that a conventional apartment building does not have.",
"But before any of that matters, there is a threshold question that changes the whole schedule: is the property residential rental property on 27.5 years, or nonresidential real property on 39 years? The answer depends on service level, and it is decided property by property.",
],
"sections": [
("Where the 27.5 Year Line Falls", [
"Under IRC Sec. 168(e)(2)(A), residential rental property is a building from which 80% or more of gross rental income is rental income from dwelling units. The regulations exclude establishments where more than half the units are used on a transient basis.",
"Independent living communities generally qualify as residential rental property. Residents lease apartments, live independently, and pay rent. The 27.5-year schedule applies.",
"Skilled nursing facilities generally do not. Revenue is predominantly for medical and personal care services rather than for occupancy of a dwelling unit, and the facility functions as a healthcare operation. The 39-year schedule applies.",
"Assisted living sits between them and is genuinely fact dependent. A community where residents hold apartment leases and purchase care services separately looks residential. A community where a single all-inclusive fee covers heavy personal care, meals, and supervision looks nonresidential. The fee structure and the revenue breakdown are the evidence, so how the operator bills is a tax decision as much as an operations decision.",
]),
("What Reclassifies Regardless of Schedule", [
"Senior housing carries far more five-year property than conventional multifamily. Commercial kitchen equipment, walk-in coolers, dishwashing systems, laundry equipment, nurse call and emergency response systems, wander management and door monitoring, medication carts and dispensing systems, salon and therapy equipment, and dedicated generator and transfer switch capacity are all equipment.",
"Interior finishes contribute heavily too. Decorative and accent lighting, carpet and resilient flooring, millwork in dining and common areas, handrails and grab bars, window treatments, and appliances in resident units are five-year property.",
"Communities are also fixture-dense in a way that raises the count. A 96-unit assisted living building has 96 kitchenettes, 96 bathroom fixture sets, and a common area program with dining, activity, salon, therapy, and wellness spaces that a conventional apartment building simply does not have.",
]),
("Site Work and Land Improvements", [
"Fifteen-year land improvements run 8% to 13%. Senior communities require generous surface parking for staff and visitors, covered drop-off canopies, accessible walkways and ramps, resident courtyards and secured memory care gardens, walking paths, site lighting engineered for low-vision residents, fencing, and emergency generator pads.",
"Memory care courtyards are worth calling out because they are typically fully enclosed with substantial hardscape, secured gates, and specialty landscaping. This is a meaningful improvement package rather than incidental landscaping.",
]),
("Worked Example: Assisted Living Community", [
"An operator acquires an 88-unit assisted living community for $19,800,000. Land is allocated at $2,300,000, leaving $17,500,000 depreciable. The property bills an all-inclusive care fee and is classified as nonresidential on a 39-year schedule.",
"The study identifies five-year property of $3,850,000 (22%), seven-year property of $525,000 (3%), fifteen-year land improvements of $1,925,000 (11%), and 39-year structure of $11,200,000 (64%).",
"Reclassified basis of $6,300,000 is deductible in year one under IRC Sec. 168(k), plus $287,180 of structural depreciation, for approximately $6,587,180 against $448,718 on a straight 39-year schedule.",
]),
("The Operating Business Advantage", [
"Where the owner also operates the community, this is a trade or business rather than a rental activity. Personal care services are substantial, meals are provided, and staff are on site continuously. Under IRC Sec. 469 the analysis then turns only on material participation, and an owner-operator readily meets it.",
"That makes the deduction non-passive and usable against other active income. Where ownership and operations are separated through an operating company and a property company, the structure has to be built deliberately. The self-rental rules under Treasury Regulation Sec. 1.469-2(f)(6) can recharacterize rental income as non-passive without giving the corresponding loss the same treatment, which is exactly the wrong outcome. This structure should be reviewed before the study, not after.",
]),
("Look-Back Studies on Stabilized Communities", [
"Many senior housing owners built or acquired during a development wave and have been depreciating on a straight schedule for years. A look-back study with Form 3115 captures the entire missed deduction as a Sec. 481(a) adjustment in the current year, no amended returns required.",
"For a stabilized community that is now generating meaningful taxable income, this is often better timing than a study at acquisition would have been, when the property was in lease-up and generating losses anyway.",
]),
],
"faqs": [
("Is assisted living 27.5-year or 39-year property?",
 "It depends on the service model. Independent living generally qualifies as residential rental property at 27.5 years. Skilled nursing is generally nonresidential at 39 years. Assisted living is fact dependent, turning on whether 80% or more of gross rental income is rent from dwelling units under IRC Sec. 168(e)(2)(A)."),
("Does the fee structure really change the depreciation schedule?",
 "It can. Where residents hold apartment leases and buy care services separately, the rental income share is easier to establish. Where a single all-inclusive fee covers heavy care, the property looks less like residential rental. The billing model is evidence, so it deserves attention before it is set."),
("What percentage of basis typically reclassifies?",
 "Senior housing commonly reaches 25% to 35%, higher than conventional multifamily. Commercial kitchens, nurse call systems, laundry, generators, salon and therapy spaces, and unit-level fixtures across dozens of units all add up."),
("Can I use the loss against my other income?",
 "If you operate the community, yes. Substantial services make this a trade or business rather than a rental activity, so material participation under Treas. Reg. Sec. 1.469-5T controls. If you own the real estate and lease it to an operator, review the self-rental rules before assuming the answer."),
("I bought the community four years ago. Is it too late?",
 "No. A look-back study with Form 3115 claims the full cumulative missed depreciation in the current year through a Sec. 481(a) adjustment. For a stabilized community now producing taxable income, this timing is often better than a study at acquisition."),
],
"related": [
("/blog/cost-segregation-medical-office-buildings/", "Cost segregation for medical office buildings"),
("/blog/self-rental-rules-business-rents-from-you/", "Self-rental rules explained"),
("/blog/landlord-guide-depreciation-27-5-vs-39-year/", "27.5 vs 39 year depreciation for landlords"),
],
"cta_head": "Get the Schedule Right Before You Get the Study",
"cta_body": "The 27.5 versus 39 year determination changes everything downstream. Send us your fee schedule and revenue breakdown and we will resolve the classification first, then size the study.",
},

{
"slug": "cost-segregation-mobile-home-parks",
"title": "Cost Segregation for Mobile Home Parks: Almost Everything Is a Land Improvement",
"meta_title": "Cost Segregation for Mobile Home Parks (2026 Guide) | AE Tax Advisors",
"meta_desc": "Mobile home parks reclassify 50 to 75 percent of basis because nearly all improvements are 15-year land improvements. Full breakdown for 2026.",
"category": C, "date": D,
"intro": [
"Mobile home parks are the strangest cost segregation asset class in real estate, and the strangeness works entirely in the owner's favor. A park with tenant-owned homes has almost no 39-year building at all.",
"What you actually bought is land, utilities, roads, and pads. Utilities, roads, and pads are 15-year land improvements. Reclassification percentages of 50% to 75% of depreciable basis are routine, and on a park with no park-owned homes the number can go higher.",
],
"sections": [
("The Structural Component Is Tiny", [
"On a typical 120-pad community, the only 39-year structures are the office, a laundry building, maybe a clubhouse or maintenance shed. That might be 4,000 square feet against 18 acres of improved land.",
"Everything else is site work. Interior roads and their base, concrete pads, driveways, utility distribution, street lighting, mail kiosks, playground and amenity areas, fencing, signage foundations, and landscaping. All of it falls under IRC Sec. 168(e)(3)(C) as 15-year land improvement property, and all of it is bonus eligible under IRC Sec. 168(k).",
]),
("Utility Infrastructure Is the Largest Class", [
"Water distribution mains and laterals, sewer collection lines and lift stations, natural gas distribution, and electrical distribution including pedestals, transformers, and meter banks represent the bulk of a park's depreciable basis.",
"On many parks, buried utility infrastructure alone accounts for 30% to 45% of the improved value. It is invisible, which is exactly why it goes uncounted in a purchase price allocation done from a closing statement rather than from an engineering analysis.",
"Individual meters and pedestals at each pad are worth separate treatment. Where the park has submetered water or electric, the meters themselves are five-year equipment even though the distribution lines feeding them are 15-year improvements.",
]),
("Park-Owned Homes Change the Math", [
"Homes owned by the park and rented to residents are a separate asset class entirely. A manufactured home held for rental is generally 27.5-year residential rental property if it is affixed and treated as real property, or five to seven year personal property if it retains its character as a vehicle or is otherwise not permanently affixed.",
"The determination turns on affixation, titling, and state law characterization. Many park operators have a mix, and the mix should be inventoried rather than lumped. Where homes are properly treated as personal property, they are bonus eligible, which is a substantially better outcome than 27.5-year treatment.",
]),
("Worked Example: 120-Pad Community", [
"An investor acquires a 120-pad community for $6,400,000. Land is allocated at $1,400,000, leaving $5,000,000 depreciable. There are no park-owned homes.",
"The study identifies five-year property of $350,000 (7%), consisting of meters, pedestal equipment, laundry equipment, office fixtures, and site amenity equipment. Fifteen-year land improvements come to $3,400,000 (68%), covering roads, pads, all buried utilities, lighting, and fencing. The remaining $1,250,000 (25%) is 39-year structure, mostly the office, clubhouse, and laundry.",
"Reclassified basis of $3,750,000 is deductible in year one under IRC Sec. 168(k), plus $32,051 of structural depreciation, for approximately $3,782,051 in year one against $181,818 under a blended straight-line approach.",
"At a 37% marginal rate that is roughly $1.39 million of federal tax deferred on a $6.4 million acquisition.",
]),
("The Allocation Fight Worth Having", [
"Because land is not depreciable and land improvements are, the land versus improvement allocation matters more on a mobile home park than on almost any other asset. A lazy allocation that assigns 40% of purchase price to raw land is leaving enormous value on the table.",
"The correct approach values the land as if unimproved, based on comparable raw acreage in the market, and treats the remainder as improvements. In a market where raw ground trades at $12,000 an acre, an 18-acre park does not have $2.6 million of land value regardless of what the appraisal for the lender said.",
"This is an engineering and valuation exercise, and it is the single highest leverage decision in a park study.",
]),
("Passive Loss Planning", [
"Park ownership is generally a rental activity, so IRC Sec. 469 applies and losses are passive unless the owner qualifies as a real estate professional under IRC Sec. 469(c)(7) or has passive income to absorb them.",
"Parks that provide substantial services, which is uncommon, can be a different analysis. Most operators are landlords. That said, park owners frequently hold multiple parks, and grouping elections under Treasury Regulation Sec. 1.469-4 can make the material participation analysis materially easier across a portfolio.",
]),
],
"faqs": [
("Why do mobile home parks reclassify so much higher than apartments?",
 "Because there is almost no building. What you buy is land, roads, pads, and buried utility infrastructure, and nearly all of that is 15-year land improvement property under IRC Sec. 168(e)(3)(C). Reclassification of 50% to 75% of depreciable basis is routine."),
("Are buried utility lines really depreciable?",
 "Yes. Water mains, sewer collection lines, gas distribution, and electrical distribution serving the pads are 15-year land improvements. They are frequently the single largest component of a park's depreciable basis and are commonly missed when allocation is done from a closing statement alone."),
("How are park-owned homes treated?",
 "It depends on affixation and titling. Homes permanently affixed and treated as real property are generally 27.5-year residential rental property. Homes retaining their character as personal property are five to seven year property and bonus eligible, which is a better outcome. Inventory the mix rather than assuming."),
("Does the land allocation really matter that much?",
 "More than on any other asset class. Land is not depreciable and nearly everything else in a park is 15-year property. Valuing the land as raw unimproved acreage against local comparables, rather than accepting a lender appraisal split, is often the highest value decision in the entire study."),
("Can I offset my W2 income with park losses?",
 "Generally not, because park ownership is a rental activity subject to IRC Sec. 469. Unless you qualify as a real estate professional or have passive income to absorb the loss, it suspends and carries forward. It releases on a fully taxable disposition or when passive income appears."),
],
"related": [
("/blog/passive-activity-loss-rules-for-real-estate-investors/", "Passive activity loss rules for real estate investors"),
("/blog/grouping-elections-real-estate-irc-469/", "Grouping elections under IRC Sec. 469"),
("/blog/real-estate-professional-status-qualification-guide/", "Real estate professional status qualification"),
],
"cta_head": "Parks Produce the Highest Reclassification in Real Estate",
"cta_body": "If you own a community and have been depreciating it as though it were a building, the correction is worth running. Send us the acreage, pad count, and closing detail.",
},

{
"slug": "cost-segregation-rv-parks-campgrounds",
"title": "Cost Segregation for RV Parks and Campgrounds: Site Work Is the Whole Asset",
"meta_title": "Cost Segregation for RV Parks and Campgrounds (2026 Guide) | AE Tax Advisors",
"meta_desc": "RV parks reclassify 55 to 75 percent of basis. Why campgrounds qualify as operating businesses and how the seven-day rule affects the deduction in 2026.",
"category": C, "date": D,
"intro": [
"RV parks and campgrounds combine two features that rarely appear together: almost all of the depreciable basis is 15-year land improvement property, and the activity usually qualifies as an operating business rather than a rental.",
"The first fact produces reclassification of 55% to 75%. The second means the resulting loss is frequently non-passive and usable against other active income. Together they make campgrounds one of the most tax-efficient real estate adjacent assets available.",
],
"sections": [
("Nearly Everything Is a Land Improvement", [
"An RV park is roads, pads, and utilities. Site pads and their gravel or concrete surfaces, interior roads, water distribution, sewer collection and dump stations, electrical distribution with 30 and 50 amp pedestals, site lighting, fencing, signage foundations, and landscaping are all 15-year property under IRC Sec. 168(e)(3)(C).",
"Amenity infrastructure follows the same treatment. Pool decks and their surrounding hardscape, pickleball and basketball courts, playground surfacing, dog park fencing, fire ring installations, and pavilion foundations are land improvements.",
"The 39-year structures are limited to the office, bathhouse, laundry building, and any enclosed clubhouse. On a 140-site park these might total 6,000 square feet against 25 acres of improved ground.",
]),
("The Five-Year Components", [
"Electrical pedestals themselves, water and electric meters, laundry equipment, pool pumps and filtration and heating equipment, WiFi network infrastructure and access points, gate and access control systems, cameras, propane dispensing equipment, store fixtures and coolers, golf carts and maintenance equipment, and playground apparatus are five-year personal property.",
"WiFi is worth calling out. Modern parks compete on connectivity, and a mesh network covering 25 acres with fiber backhaul, distribution nodes, and access points is a real capital item, not an afterthought. It is five-year property.",
]),
("Campgrounds Are Operating Businesses", [
"This is the structural advantage. Under Treasury Regulation Sec. 1.469-1T(e)(3)(ii)(A), an activity is not a rental activity where the average period of customer use is seven days or less. RV parks and campgrounds overwhelmingly meet this, since the average stay is measured in nights.",
"Where the activity is not a rental activity, the passive loss analysis under IRC Sec. 469 turns solely on material participation under Treasury Regulation Sec. 1.469-5T. An owner-operator running the park clears the 500-hour test. Even a semi-absentee owner can often qualify under the 100-hour and substantially-all test or the facts and circumstances test.",
"The result is that a large first-year deduction from a campground study is generally non-passive and available against wages, business income, and other active income immediately. This is the same mechanism that makes short-term rentals attractive, applied to a much larger asset.",
"Longer-stay parks are the exception. A park catering to monthly and seasonal residents may have an average customer use period well above seven days, and would then be evaluated as a rental activity under the ordinary rules. Average stay data should be pulled from the reservation system, not estimated.",
]),
("Worked Example: 140-Site Park", [
"An operator acquires a 140-site RV resort for $8,900,000. Land is allocated at $1,600,000, leaving $7,300,000 depreciable. The average stay is 4.2 nights.",
"The study identifies five-year property of $949,000 (13%), fifteen-year land improvements of $4,672,000 (64%), and 39-year structure of $1,679,000 (23%).",
"Reclassified basis of $5,621,000 is deductible in year one under IRC Sec. 168(k), plus $43,051 of structural depreciation, for approximately $5,664,051 in year one.",
"Because the average stay is under seven days and the owner materially participates, the loss is non-passive. At a 37% marginal rate the first-year federal benefit is roughly $2.1 million, usable against other active income rather than suspended.",
]),
("Development and Expansion Costs", [
"Parks expand constantly, adding sites, upgrading pedestals from 30 to 50 amp, extending utility runs, and building amenities. Each expansion is a new placed-in-service event with its own bonus eligibility.",
"This is a recurring benefit rather than a one-time event. An operator adding 30 sites a year at $28,000 per site of improvement cost is generating roughly $840,000 of predominantly 15-year, bonus eligible basis annually. Tracking those additions at the component level rather than lumping them into a single land improvement account also preserves partial asset disposition elections under Treasury Regulation Sec. 1.168(i)-8 when components are later replaced.",
]),
("Recapture and Exit Planning", [
"With 13% of basis in Sec. 1245 property and 64% in Sec. 1250 land improvements, the recapture profile is mixed. Sec. 1245 property recaptures fully as ordinary income. Land improvements are Sec. 1250 property, and because they are depreciated on a straight-line basis under MACRS, there is generally no Sec. 1250 recapture, though unrecaptured Sec. 1250 gain at 25% applies.",
"That is a materially better exit profile than a car wash or gas station with half its basis in equipment. Operators planning a five to seven year hold should still model the exit, but campgrounds carry less recapture drag than most heavily reclassified assets.",
]),
],
"faqs": [
("Why do RV parks reclassify 55% or more?",
 "Because the asset is site work rather than building. Pads, roads, buried utilities, pedestals, and amenity hardscape are all 15-year land improvements under IRC Sec. 168(e)(3)(C). The only 39-year components are typically an office, bathhouse, and laundry building."),
("Is an RV park a passive activity?",
 "Usually not. Under Treas. Reg. Sec. 1.469-1T(e)(3)(ii)(A), an activity with an average customer use period of seven days or less is not a rental activity. Campgrounds almost always meet this, so only material participation under Treas. Reg. Sec. 1.469-5T applies and the loss is generally non-passive."),
("What if my park is mostly monthly and seasonal residents?",
 "Then the average stay likely exceeds seven days and the activity is evaluated as a rental. Pull the actual average customer use period from your reservation system rather than estimating, because this single fact determines whether the deduction offsets active income."),
("Are electrical pedestals five-year or 15-year property?",
 "The pedestal units, meters, and receptacles are five-year equipment. The buried distribution lines, conduit, and transformers feeding them are 15-year land improvements. A proper study splits these rather than treating the electrical system as one item."),
("Does expanding the park create new deductions?",
 "Yes. Every expansion phase is a separate placed-in-service event with its own bonus depreciation eligibility. Since expansion costs are predominantly 15-year land improvements, an operator adding sites annually generates a recurring stream of fully bonus eligible basis."),
],
"related": [
("/blog/cost-segregation-mobile-home-parks/", "Cost segregation for mobile home parks"),
("/blog/str-loophole-7-day-rule-explained/", "The seven-day rule explained"),
("/blog/material-participation-tests-str-owners/", "Material participation tests explained"),
],
"cta_head": "Campgrounds Combine Two Rare Tax Advantages",
"cta_body": "High reclassification and non-passive treatment rarely appear in the same asset. Send us your site count, closing detail, and average stay data and we will model both.",
},

{
"slug": "cost-segregation-fitness-centers-gyms",
"title": "Cost Segregation for Gyms and Fitness Centers: Equipment, Flooring, and Locker Rooms",
"meta_title": "Cost Segregation for Gyms and Fitness Centers (2026 Guide) | AE Tax Advisors",
"meta_desc": "Fitness centers reclassify 30 to 45 percent of basis. How equipment, specialty flooring, locker rooms, and pools are treated under IRC Sec. 168 in 2026.",
"category": C, "date": D,
"intro": [
"Fitness facilities reclassify heavily, typically 30% to 45% of depreciable basis, and full service clubs with aquatics push higher. The reason is that a gym is a shell filled with equipment, specialty surfaces, and mechanical systems that exist to serve members rather than the building.",
"Owners who bought a building and did a large build-out often carry all of it on a 39-year schedule. That is usually wrong by a wide margin.",
],
"sections": [
("Equipment Is the Obvious Part", [
"Cardio machines, selectorized strength equipment, free weights and racks, functional training rigs, turf sleds, cable systems, recovery and stretching equipment, sound and audiovisual systems, member check-in kiosks, and tanning and recovery equipment are five-year personal property under IRC Sec. 168(e)(3)(B).",
"Most operators already expense or depreciate this correctly because it arrives on an equipment invoice. The problem is what is buried in the construction contract.",
]),
("Specialty Flooring Is Not Structure", [
"Rubber flooring, weight room platforms, sprung group fitness floors, turf lanes, and court surfaces are among the most commonly misclassified items in a fitness build-out. When installed over a structural slab as a wear surface serving the activity, they are five-year property, not part of the building.",
"The distinction is whether the flooring is a structural component or a finish serving the specific use. Poured rubber over concrete, rolled goods, interlocking tiles, and modular platforms are finishes. The slab beneath them is structure.",
"On a 30,000 square foot club, specialty flooring alone commonly runs $250,000 to $500,000 installed.",
]),
("Locker Rooms and Wet Areas", [
"Lockers, benches, vanities and countertops, mirrors, hair dryers, and towel systems are five-year property. So are sauna and steam room equipment, including generators and controls, though the enclosure itself may be structural depending on how it is built.",
"Wet area finishes are more nuanced. Tile applied to structural walls and floors is generally a structural component. Decorative wall panels, partition systems for showers and changing areas that are demountable, and specialty ceiling systems in humid environments are frequently reclassifiable.",
"Dedicated mechanical serving these areas follows the equipment analysis. High-capacity exhaust and dehumidification serving a pool deck or steam room exists for that function rather than for general building comfort, and under Treasury Regulation Sec. 1.48-1(e)(2) is classified with the function it serves.",
]),
("Aquatics Changes the Numbers", [
"Indoor pools carry heavy equipment loads. Pumps, filtration, heaters, chemical controllers, UV or ozone systems, pool covers, lifts, and dehumidification units are five-year property. The pool shell and deck are structure or land improvement depending on whether it is indoor or outdoor.",
"An outdoor pool complex is 15-year land improvement property along with its decking, fencing, and site lighting. That is a better result than the indoor equivalent, which sits inside the 39-year building envelope.",
]),
("Worked Example: Full Service Club", [
"An operator builds out a 34,000 square foot club for $6,700,000 including the building shell purchase. Land is allocated at $850,000, leaving $5,850,000 depreciable.",
"The study identifies five-year property of $2,047,500 (35%), seven-year property of $175,500 (3%), fifteen-year land improvements of $468,000 (8%), and 39-year structure of $3,159,000 (54%).",
"Reclassified basis of $2,691,000 is deductible in year one under IRC Sec. 168(k), plus $81,000 of structural depreciation, for approximately $2,772,000 against $150,000 on a straight 39-year schedule.",
]),
("Gyms Are Operating Businesses", [
"A fitness facility is a trade or business, not a rental activity. That means the analysis under IRC Sec. 469 runs only through material participation under Treasury Regulation Sec. 1.469-5T, and an owner-operator clears the 500-hour test easily.",
"The deduction is therefore non-passive and available against other active income in the year taken. For a multi-unit franchisee or an owner with other business income, this is the difference between a suspended loss and a current-year refund.",
"Where the operator leases the building from a related property company, the self-rental rules under Treasury Regulation Sec. 1.469-2(f)(6) apply and the structure needs review. The building basis sits in the property company, and how that entity's loss is characterized depends on the arrangement.",
]),
("Qualified Improvement Property on Renovations", [
"Clubs renovate constantly. Any interior improvement to a nonresidential building placed in service after the building itself generally qualifies as QIP under IRC Sec. 168(e)(6), carrying a 15-year life and full bonus eligibility.",
"That means the non-personal-property portion of a renovation is recovered over 15 years rather than 39. Combined with partial asset disposition elections under Treasury Regulation Sec. 1.168(i)-8 on what was torn out, a renovation cycle produces two separate deductions that most operators claim neither of.",
]),
],
"faqs": [
("Is rubber gym flooring five-year property?",
 "Generally yes. Rubber flooring, weight platforms, sprung floors, and turf installed over a structural slab as a wear surface serving the fitness activity are finishes, not structural components. The concrete slab beneath is structure. This is one of the most commonly missed items in fitness build-outs."),
("What percentage does a gym typically reclassify?",
 "Most fitness facilities land between 30% and 45% of depreciable basis. Full service clubs with aquatics, spa, and extensive locker rooms sit at the top. Small studio concepts in leased space sit lower but still reclassify well relative to build-out cost."),
("Is the deduction usable against my other income?",
 "If you operate the gym, yes. A fitness facility is a trade or business rather than a rental activity, so only material participation under Treas. Reg. Sec. 1.469-5T applies and the loss is non-passive. Owner-operators clear the 500-hour test without difficulty."),
("How are outdoor pools treated differently from indoor pools?",
 "Outdoor pool complexes, including the shell, decking, fencing, and site lighting, are 15-year land improvements. Indoor pools sit inside the 39-year building envelope, though the pumps, filtration, heaters, chemical systems, and dehumidification equipment are five-year property in either case."),
("Can I claim a deduction on equipment I tear out during a renovation?",
 "Yes, through a partial asset disposition election under Treas. Reg. Sec. 1.168(i)-8. This requires that components were separately identified, which is what a cost segregation study produces. Clubs on a renovation cycle can claim this repeatedly."),
],
"related": [
("/blog/partial-asset-disposition-overlooked-tax-strategy/", "Partial asset dispositions explained"),
("/blog/self-rental-rules-business-rents-from-you/", "Self-rental rules when your business rents from you"),
("/equipment-leasing/", "Equipment financing and Section 179 planning"),
],
"cta_head": "Most Club Build-Outs Sit on the Wrong Schedule",
"cta_body": "If your construction contract went onto the books as one 39-year number, there is likely a large correction available. Send us the contract detail and we will size it.",
},

{
"slug": "cost-segregation-dental-offices",
"title": "Cost Segregation for Dental Offices: Operatories, Plumbing, and the Build-Out",
"meta_title": "Cost Segregation for Dental Offices (2026 Guide) | AE Tax Advisors",
"meta_desc": "Dental practices reclassify 35 to 50 percent of build-out cost. How operatory plumbing, vacuum, air, and imaging systems classify under IRC Sec. 168 in 2026.",
"category": C, "date": D,
"intro": [
"Dental build-outs reclassify at rates that surprise most practice owners, commonly 35% to 50% of construction cost. A dental office is not a room with chairs in it. It is a distributed mechanical system with plumbing, vacuum, compressed air, and electrical runs to every operatory.",
"That infrastructure serves equipment, not the building, and under IRC Sec. 168 it follows the equipment it serves.",
],
"sections": [
("Operatory Infrastructure Follows the Chair", [
"Each operatory requires dedicated water and drain lines, a vacuum line, a compressed air line, and dedicated electrical and data. These runs exist solely to operate dental equipment. Under the functional analysis reflected in Treasury Regulation Sec. 1.48-1(e)(2), utilities serving specific equipment rather than the building generally are classified with that equipment as five-year property.",
"On a 10-operatory practice, that is 10 sets of dedicated runs plus the central vacuum pump, air compressor, and their mechanical room infrastructure. This alone commonly accounts for 15% to 22% of build-out cost, and it is almost always buried inside a general contractor's plumbing and electrical line items rather than broken out.",
]),
("Equipment That Arrives on Invoices", [
"Chairs, delivery units, lights, x-ray units, panoramic and cone beam imaging, intraoral scanners, milling units, sterilization equipment, cabinetry, nitrous systems, and practice management hardware are all five-year property. Most practices depreciate these correctly because they arrive as equipment purchases.",
"Casework is the item most often lumped into construction. Operatory cabinetry, sterilization center casework, and lab benches are equipment-grade fixtures, generally five-year or seven-year property, not building improvements, when they are manufactured units installed rather than site-built millwork integral to the structure.",
]),
("Finishes and Interior Work", [
"Vinyl and resilient flooring, carpet in administrative areas, decorative and accent lighting, reception millwork, window treatments, wall coverings, signage, security systems, and the audiovisual and sound masking systems that dental practices install for privacy are five-year property.",
"Lead-lined walls in imaging rooms are a nuanced item. The lead shielding installed to serve radiographic equipment can often be classified with that equipment rather than as a structural wall, though the framing and drywall around it are structural. The split should be documented.",
]),
("Qualified Improvement Property Handles the Rest", [
"Most dental build-outs occur in existing nonresidential buildings. Interior improvements to a nonresidential building placed in service after the building was first placed in service generally qualify as QIP under IRC Sec. 168(e)(6).",
"QIP carries a 15-year recovery period with full bonus eligibility. This matters enormously for practices, because it means the portion of a build-out that is genuinely building, new partition walls, ceilings, general lighting, and general HVAC, is recovered over 15 years rather than 39, and is fully deductible in year one under IRC Sec. 168(k).",
"Between five-year personal property and 15-year QIP, a leasehold dental build-out can be very close to fully deductible in the first year. Practices that put a $900,000 build-out on a 39-year schedule are leaving nearly the entire deduction on the table.",
]),
("Worked Example: 10-Operatory Practice", [
"A practice owner completes a 4,800 square foot build-out in leased space for $1,150,000 in construction cost, plus $680,000 in equipment.",
"The study allocates construction cost to five-year property of $402,500 (35%), and 15-year QIP of $690,000 (60%), with $57,500 (5%) remaining as structural components not eligible for QIP treatment. The $680,000 of equipment is five-year property in full.",
"Under IRC Sec. 168(k), the $402,500 of reclassified construction, the $690,000 of QIP, and the $680,000 of equipment are all bonus eligible, producing approximately $1,772,500 of first-year deduction against a total investment of $1,830,000.",
"At a 37% marginal rate, that is roughly $656,000 of federal tax reduction in the year the practice opens, which is often exactly when the owner needs the cash.",
]),
("Practice Owners Materially Participate", [
"A dental practice is a trade or business. The owner works in it daily. Material participation under Treasury Regulation Sec. 1.469-5T is not a close question, so the deduction is non-passive and offsets practice income and other active income directly.",
"Where the practice owner also owns the building through a separate entity, the self-rental rules under Treasury Regulation Sec. 1.469-2(f)(6) apply to the rent arrangement. The building itself is a separate cost segregation opportunity with its own study, and coordinating the two, plus the reasonable compensation and entity structure questions that come with a profitable practice, is where most of the planning value sits.",
]),
("Timing the Deduction Against Practice Income", [
"A new practice or a large expansion often produces a first-year deduction larger than first-year income. Excess business loss limitations under IRC Sec. 461(l) can defer part of it, and net operating loss carryforwards under IRC Sec. 172 are limited to 80% of taxable income in subsequent years.",
"For an associate buying in or a doctor opening a second location while the first one is profitable, this rarely binds. For a startup practice with no other income, electing out of bonus depreciation on some asset classes and using Sec. 179 selectively can produce a better multi-year result than taking everything at once.",
]),
],
"faqs": [
("What percentage of a dental build-out reclassifies?",
 "Commonly 35% to 50% of construction cost to five-year property, with much of the balance qualifying as 15-year QIP. Between the two, a leasehold dental build-out is often close to fully deductible in the first year under IRC Sec. 168(k)."),
("Is the plumbing to each operatory really five-year property?",
 "Yes, when it serves dental equipment rather than the building generally. Dedicated water, drain, vacuum, and compressed air runs to operatories exist to operate equipment. Restroom plumbing and general building water service remain structural."),
("What is QIP and why does it matter for a dental office?",
 "Qualified improvement property is interior improvement to a nonresidential building placed in service after the building itself, under IRC Sec. 168(e)(6). It carries a 15-year life with full bonus eligibility, so the genuinely structural part of your build-out is still recovered in year one rather than over 39 years."),
("Can I use the deduction against my practice income?",
 "Yes. A dental practice is a trade or business in which the owner materially participates, so the deduction is non-passive and offsets practice income and other active income directly. This is a better position than most real estate investors are in."),
("I built out my office four years ago. Can I still fix it?",
 "Yes. A look-back study paired with Form 3115 claims the entire cumulative missed deduction in the current year as a Sec. 481(a) adjustment, with no amended returns needed. Build-outs sitting on a 39-year schedule are the most common correction we run for practice owners."),
],
"related": [
("/blog/tax-strategy-for-dentists/", "Tax strategy for dental practice owners"),
("/blog/cost-segregation-medical-office-buildings/", "Cost segregation for medical office buildings"),
("/blog/form-3115-cost-segregation-catch-up/", "Form 3115 catch-up depreciation"),
],
"cta_head": "Your Build-Out Is Probably on the Wrong Schedule",
"cta_body": "Send us the construction contract and equipment schedule from your build-out. We will tell you how much of it should have been deducted in year one, and whether a Form 3115 catch-up is available.",
},

{
"slug": "cost-segregation-veterinary-clinics",
"title": "Cost Segregation for Veterinary Clinics: Kennels, Surgery, and Imaging Build-Out",
"meta_title": "Cost Segregation for Veterinary Clinics (2026 Guide) | AE Tax Advisors",
"meta_desc": "Veterinary clinics reclassify 35 to 50 percent of build-out cost. How kennel runs, surgical suites, imaging, and QIP are classified under IRC Sec. 168 in 2026.",
"category": C, "date": D,
"intro": [
"Veterinary clinics reclassify at rates comparable to dental practices, generally 35% to 50% of build-out cost, and multi-doctor hospitals with surgery, imaging, and boarding run higher.",
"The reason is the same. A veterinary hospital is a distributed mechanical and equipment system that happens to sit inside a building, and the tax code classifies by function.",
],
"sections": [
("Kennel and Boarding Areas", [
"Kennel runs, cage banks, gates and dividers, and the elevated flooring and drainage systems serving them are equipment rather than structure. Modern kennel systems are manufactured, modular, and removable, which supports five-year classification under IRC Sec. 168(e)(3)(B).",
"The dedicated mechanical serving these areas follows the same logic. High air-change ventilation, dedicated exhaust, and the specialized floor drains and trench drains installed for sanitation serve the kennel function rather than general building comfort, and under Treasury Regulation Sec. 1.48-1(e)(2) they classify with the function they serve.",
"Epoxy and seamless resinous flooring in kennel and treatment areas is a wear and sanitation surface applied over a structural slab. It is a finish, not a structural component.",
]),
("Surgical and Treatment Suites", [
"Surgical tables, lights, anesthesia machines and scavenging systems, monitoring equipment, autoclaves and sterilization, dental units, treatment tables, and wet tables with their dedicated plumbing are five-year property.",
"Medical gas systems, including oxygen and nitrous distribution, manifolds, and outlets, serve equipment rather than the building and follow the same treatment. Same for the dedicated vacuum and scavenging lines running to each treatment position.",
"Casework throughout treatment, pharmacy, and lab areas is generally equipment-grade fixture rather than site-built structural millwork, and classifies at five or seven years accordingly.",
]),
("Imaging Rooms", [
"Digital radiography, ultrasound, CT where present, and their dedicated power and data are five-year property. Lead shielding installed specifically to serve radiographic equipment can often be classified with that equipment, though the framing and drywall around it remain structural. This split should be documented rather than assumed in either direction.",
]),
("Reception, Exam, and Retail", [
"Exam room casework and tables, scales, computer and practice management hardware, sound masking, security and camera systems, decorative and accent lighting, resilient flooring and carpet, reception millwork, retail display fixtures, and signage are five-year property.",
"Clinics increasingly build retail and grooming areas, which reclassify like any retail fit-out. Display shelving, grooming tubs and their dedicated plumbing, dryers, and grooming tables are equipment.",
]),
("QIP Covers the Structural Remainder", [
"Most veterinary build-outs occur in existing nonresidential buildings. Interior improvements placed in service after the building itself generally qualify as qualified improvement property under IRC Sec. 168(e)(6), carrying a 15-year recovery period with full bonus eligibility.",
"That means new partition walls, ceilings, general lighting, and general HVAC in a leasehold build-out are recovered in year one under IRC Sec. 168(k) rather than over 39 years. Combined with the five-year personal property, a veterinary build-out is frequently close to fully deductible in the year it opens.",
]),
("Worked Example: Multi-Doctor Hospital", [
"An owner completes a 6,200 square foot hospital build-out for $1,480,000 in construction cost, plus $520,000 in medical equipment.",
"The study allocates construction to five-year property of $592,000 (40%), 15-year QIP of $814,000 (55%), and structural components not eligible for QIP of $74,000 (5%). All $520,000 of equipment is five-year property.",
"Under IRC Sec. 168(k), the five-year property, the QIP, and the equipment are all bonus eligible, producing approximately $1,926,000 of first-year deduction against a $2,000,000 total investment.",
"At a 37% marginal rate that is roughly $713,000 of federal tax reduction in the opening year, when a practice owner is typically carrying the heaviest debt service.",
]),
("Owning the Building", [
"Many veterinary owners buy the real estate through a separate entity and lease it to the practice. That building is its own cost segregation opportunity with its own study, typically reclassifying 20% to 30%.",
"The interaction matters. Under the self-rental rules in Treasury Regulation Sec. 1.469-2(f)(6), net rental income from a property leased to a business in which you materially participate is recharacterized as non-passive, but a net rental loss generally is not. A large first-year depreciation deduction in the property company can therefore create a suspended passive loss rather than a current deduction, which is the opposite of what most owners expect.",
"There are structural answers, including grouping elections under Treasury Regulation Sec. 1.469-4 where the requirements are met. This should be addressed before the study is commissioned, not after the return is filed.",
]),
],
"faqs": [
("What percentage of a veterinary build-out reclassifies?",
 "Typically 35% to 50% of construction cost to five-year property, with most of the balance qualifying as 15-year QIP. Multi-doctor hospitals with surgery, imaging, and boarding sit at the top of the range."),
("Are kennel runs five-year property?",
 "Generally yes. Modern kennel systems are manufactured, modular, and removable equipment rather than structural components. The dedicated ventilation, exhaust, and trench drainage serving them follow the same treatment under the functional test in Treas. Reg. Sec. 1.48-1(e)(2)."),
("Is epoxy flooring a structural component?",
 "No. Seamless resinous and epoxy flooring applied over a structural slab is a wear and sanitation finish serving the clinical function, not a structural component. The slab beneath it is structure."),
("How are medical gas systems classified?",
 "Oxygen and nitrous distribution, manifolds, outlets, and scavenging lines serve equipment rather than the building and are five-year property. The same applies to dedicated vacuum lines running to treatment positions."),
("I own the building through a separate LLC. Does that change anything?",
 "Yes, significantly. Self-rental rules under Treas. Reg. Sec. 1.469-2(f)(6) can leave a large depreciation loss in the property company suspended rather than currently deductible. Grouping elections under Treas. Reg. Sec. 1.469-4 may solve it, but the structure should be reviewed before the study is run."),
],
"related": [
("/blog/cost-segregation-dental-offices/", "Cost segregation for dental offices"),
("/blog/self-rental-rules-business-rents-from-you/", "Self-rental rules explained"),
("/blog/grouping-elections-real-estate-irc-469/", "Grouping elections under IRC Sec. 469"),
],
"cta_head": "Two Studies, One Plan",
"cta_body": "If you own both the practice and the building, the two studies interact and the sequence matters. Send us the build-out contract and the real estate closing detail and we will model them together.",
},
]

if __name__ == "__main__":
    write_all(ARTICLES)
