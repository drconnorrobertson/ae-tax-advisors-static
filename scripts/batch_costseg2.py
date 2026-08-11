"""Batch: additional cost segregation property types."""

from blog_gen import write_all

C = "Cost Segregation"
D = "2026-08-11"

ARTICLES = [
{
"slug": "cost-segregation-student-housing",
"title": "Cost Segregation for Student Housing: Furnishings, Amenities, and the 27.5 Year Question",
"meta_title": "Cost Segregation for Student Housing (2026 Guide) | AE Tax Advisors",
"meta_desc": "Student housing reclassifies 28 to 38 percent of basis. Furnishings, amenity space, by-the-bed leasing, and residential classification explained for 2026.",
"category": C, "date": D,
"intro": [
"Student housing reclassifies higher than conventional multifamily, typically 28% to 38% of depreciable basis, for one structural reason. Purpose-built student housing is delivered furnished, and furniture is five-year property.",
"Add an amenity program that a conventional apartment building does not have, and the gap widens further.",
],
"sections": [
("Furnishings Are the Largest Difference", [
"A 600-bed purpose-built community delivers 600 beds, desks, chairs, dressers, and mattresses, plus living room and common area furniture in every unit. At $2,200 to $3,400 per bed, that is $1,300,000 to $2,000,000 of five-year property.",
"Where furniture is acquired separately from the building, it is straightforwardly five-year property fully deductible under IRC Sec. 168(k). Where a community is acquired with furniture in place, the purchase price allocation must separate it, and a study is the mechanism.",
"Appliances in each unit follow the same treatment. A community with 180 units has 180 refrigerators, ranges, dishwashers, and in-unit laundry sets.",
]),
("The Amenity Program", [
"Student housing competes on amenities in a way conventional multifamily does not. Fitness centers, study lounges, gaming rooms, computer labs, tanning, coffee bars, and pools are standard rather than exceptional.",
"Fitness equipment, audiovisual systems, gaming and computer equipment, coffee and vending equipment, specialty flooring in fitness areas, and decorative lighting throughout the amenity program are five-year property.",
"Network infrastructure is substantial. A community guaranteeing high-speed connectivity to 600 residents carries a real fiber, switching, and access point investment, all of which is five-year property along with the conduit dedicated to it.",
"Access control is another meaningful item. Card and mobile credential systems, door hardware controllers, and camera coverage across a large site are equipment.",
]),
("Residential Classification and By-the-Bed Leasing", [
"Student housing is generally residential rental property on a 27.5-year schedule under IRC Sec. 168(e)(2)(A), which requires that 80% or more of gross rental income be from dwelling units.",
"By-the-bed leasing does not change this. Each apartment remains a dwelling unit, and leasing individual bedrooms within it is a leasing convention rather than a change in the character of the space.",
"The classification can shift where a property provides substantial services, such as meal plans or resident life programming resembling a dormitory operation. Communities operating under a university agreement with meal service should confirm the classification rather than assume it.",
]),
("Site Work", [
"Fifteen-year land improvements typically run 8% to 12%. Student communities carry heavy surface parking, often with structured or covered components, plus site lighting engineered for safety, extensive walkways, courtyards, pool decks, sport courts, bike infrastructure, and perimeter fencing.",
"Where the property includes a structured parking deck, the classification depends on whether it is freestanding or integrated into the building envelope. Freestanding decks are generally 15-year land improvements. The access control equipment within is five-year property in either case.",
]),
("Worked Example: 180-Unit Community", [
"An investor acquires a 180-unit, 552-bed purpose-built community for $47,000,000. Land is allocated at $4,600,000, leaving $42,400,000 depreciable.",
"The study identifies five-year property of $11,872,000 (28%), covering furnishings, appliances, amenity equipment, network infrastructure, access control, and finishes. Fifteen-year land improvements are $4,240,000 (10%). Structure is $26,288,000 (62%).",
"Reclassified basis of $16,112,000 is deductible in year one under IRC Sec. 168(k), plus $956,000 of structural depreciation, for approximately $17,068,000 against $1,541,818 on a straight-line schedule.",
]),
("Turnover Creates Recurring Deductions", [
"Student housing turns over almost entirely each August. Furniture is replaced on a three to five year cycle across the portfolio, and each replacement is new five-year property fully deductible when placed in service.",
"Just as important, the remaining basis in furniture and finishes removed can be written off through a partial asset disposition election under Treasury Regulation Sec. 1.168(i)-8. This requires component-level records, which is exactly what a study produces.",
"An operator replacing furniture in 60 units a year generates both a new deduction on the replacements and a disposition deduction on what was removed. Most operators claim only the first.",
]),
("Passive Loss Considerations", [
"Student housing is a rental activity under IRC Sec. 469 despite the intensive management. Leases run twelve months, average stays far exceed seven days, and the seven-day exception in Treasury Regulation Sec. 1.469-1T(e)(3)(ii)(A) does not apply.",
"That means the loss is passive unless the owner qualifies as a real estate professional or has passive income to absorb it. For institutional and syndicated ownership this is the normal expectation. For an individual operator, the aggregation election under Treasury Regulation Sec. 1.469-9(g) is generally necessary.",
]),
],
"faqs": [
("Is student housing 27.5-year or 39-year property?",
 "Generally 27.5-year residential rental property under IRC Sec. 168(e)(2)(A), since 80% or more of gross rental income comes from dwelling units. By-the-bed leasing does not change this. Properties providing meal service or dormitory-style programming should confirm rather than assume."),
("What percentage of basis reclassifies?",
 "Typically 28% to 38%, higher than conventional multifamily. Furnishings alone can be $1.3 million to $2 million on a 600-bed community, and the amenity program adds fitness, network, access control, and audiovisual equipment a conventional building does not have."),
("Can I deduct furniture replacements every year?",
 "Yes. Furniture placed in service is five-year property fully deductible under IRC Sec. 168(k). You can also write off the remaining basis in what you removed through a partial asset disposition election under Treas. Reg. Sec. 1.168(i)-8, which requires component-level records."),
("Does student housing qualify for the short-term rental exception?",
 "No. Leases are typically twelve months and average customer use far exceeds seven days, so the exception in Treas. Reg. Sec. 1.469-1T(e)(3)(ii)(A) does not apply. The activity is a rental and losses are passive absent real estate professional status."),
("Is the parking deck a 15-year or 39-year asset?",
 "It depends on integration. A freestanding parking structure is generally a 15-year land improvement. Parking integrated into the building envelope is typically part of the 39-year or 27.5-year structure. The access control equipment within is five-year property either way."),
],
"related": [
("/blog/cost-segregation-large-multifamily-100-plus-units/", "Cost segregation for large multifamily"),
("/blog/partial-asset-disposition-overlooked-tax-strategy/", "Partial asset dispositions"),
("/blog/how-to-depreciate-furnished-rentals/", "Depreciating furnished rentals"),
],
"cta_head": "Furniture Alone Can Justify the Study",
"cta_body": "Send us the unit and bed count, the FF and E schedule, and the closing detail. We will size the reclassification and the recurring turnover deductions.",
},

{
"slug": "cost-segregation-parking-garages",
"title": "Cost Segregation for Parking Garages: Structure, Equipment, and the Freestanding Test",
"meta_title": "Cost Segregation for Parking Garages (2026 Guide) | AE Tax Advisors",
"meta_desc": "A freestanding parking garage may be 15-year land improvement property rather than 39-year structure. Classification tests and equipment treatment for 2026.",
"category": C, "date": D,
"intro": [
"Parking garages present one of the more consequential classification questions in commercial real estate. Depending on how a structure is characterized, its recovery period can be 15 years or 39 years, and the difference on a $14,000,000 deck is enormous.",
"The analysis turns on whether the structure is an inherently permanent building or a land improvement, and the answer is fact specific.",
],
"sections": [
("The Building Versus Land Improvement Question", [
"A building is generally a structure enclosing a space with walls and a roof, providing shelter for people or property. Parking decks often lack complete walls, lack a roof over the top level, and shelter vehicles rather than occupants.",
"Where an open-air parking structure is genuinely freestanding and does not function as a building, the position that it is a land improvement under IRC Sec. 168(e)(3)(C) with a 15-year recovery period has meaningful support.",
"Where the structure is enclosed, climate controlled, or physically integrated with an adjacent building, it is generally part of that building and takes the building's recovery period.",
"This is not a position to take casually. It should be supported by an engineering analysis addressing enclosure, integration, function, and construction detail, and documented in the study rather than asserted.",
]),
("Equipment Is Clear Regardless", [
"Whatever the structure's classification, the operating equipment is five-year personal property under IRC Sec. 168(e)(3)(B).",
"That includes gate arms and barriers, ticket dispensers and pay stations, license plate recognition systems, cameras and monitoring, parking guidance systems with space sensors and displays, revenue control software and hardware, and electric vehicle charging equipment.",
"EV charging is increasingly substantial. A garage installing 40 Level 2 chargers and two DC fast chargers carries meaningful equipment cost plus dedicated electrical infrastructure. Under the functional analysis in Treasury Regulation Sec. 1.48-1(e)(2), the dedicated switchgear, conduit, and distribution serving the chargers classify with the chargers.",
]),
("Lighting, Signage, and Finishes", [
"Garage lighting is a large item and frequently reclassifiable. Where fixtures serve the parking function rather than general building illumination, they follow the parking structure's classification, and decorative or wayfinding lighting is generally five-year property.",
"Directional and wayfinding signage, level identification, painted striping, wheel stops, bollards, and speed bumps are separable. Striping and wheel stops in particular are commonly folded into a single paving line item when they are distinct and shorter-lived.",
"Elevator and stair towers within a garage are generally structural, and elevators specifically are excluded from qualified improvement property treatment under IRC Sec. 168(e)(6).",
]),
("Surface Lots Are Simpler", [
"A surface parking lot is unambiguously a 15-year land improvement. Paving, base course, curbing, striping, wheel stops, lighting on poles, drainage, and landscape islands all qualify.",
"For a property owner with substantial surface parking, this is one of the cleanest and largest reclassification opportunities available, and it requires no aggressive positions.",
]),
("Worked Example: Freestanding Deck", [
"An investor acquires a freestanding six-level open-air parking deck for $16,400,000. Land is allocated at $2,900,000, leaving $13,500,000 depreciable.",
"The engineering analysis supports treatment of the open-air structure as a land improvement, given the absence of enclosure, the absence of a roof over the top level, and no physical integration with an adjacent building.",
"The study identifies five-year property of $945,000 (7%), covering revenue control, guidance systems, cameras, EV charging and its dedicated distribution, and wayfinding. Fifteen-year property is $12,555,000 (93%), covering the structure, lighting, striping, and site work.",
"The entire $13,500,000 is bonus eligible under IRC Sec. 168(k), producing a full first-year deduction against $346,154 on a 39-year schedule.",
"Had the structure been classified as a 39-year building, the first-year deduction would have been roughly $1,268,000. The classification decision is worth over $12,000,000 of first-year deduction.",
]),
("Recapture and Documentation", [
"Land improvements are Sec. 1250 property depreciated on a straight-line basis under MACRS, so there is generally no Sec. 1250 recapture at ordinary rates, though unrecaptured Sec. 1250 gain applies at up to 25%.",
"The five-year equipment is Sec. 1245 property and recaptures fully as ordinary income.",
"Given the size of the position on a structure classification, documentation quality matters more here than on almost any other property type. The study should include the engineering rationale, photographs, construction drawings, and a clear statement of the factors supporting the conclusion.",
]),
],
"faqs": [
("Is a parking garage 15-year or 39-year property?",
 "It depends on whether the structure functions as a building. A freestanding open-air deck without enclosure, without a roof over the top level, and not integrated with an adjacent building has meaningful support for 15-year land improvement treatment. An enclosed or integrated structure generally takes the building's period."),
("What parking equipment qualifies as five-year property?",
 "Gate arms, ticket dispensers, pay stations, license plate recognition, cameras, parking guidance sensors and displays, revenue control hardware and software, and EV charging equipment, along with the dedicated electrical infrastructure serving the chargers."),
("Is a surface parking lot always 15-year property?",
 "Yes. Paving, base course, curbing, striping, wheel stops, pole lighting, drainage, and landscape islands are all 15-year land improvements under IRC Sec. 168(e)(3)(C). This requires no aggressive position and is one of the cleanest reclassifications available."),
("How is EV charging infrastructure treated?",
 "The chargers themselves are five-year equipment. Under the functional analysis in Treas. Reg. Sec. 1.48-1(e)(2), the dedicated switchgear, conduit, and distribution serving them classify with the chargers rather than as general building electrical."),
("How much documentation does the structure classification need?",
 "More than any other item in the study. The position can be worth eight figures of first-year deduction on a large deck, so it should be supported by engineering analysis addressing enclosure, integration, and function, with drawings and photographs in the workpapers."),
],
"related": [
("/blog/cost-segregation-office-buildings/", "Cost segregation for office buildings"),
("/blog/cost-segregation-retail-strip-centers/", "Cost segregation for retail strip centers"),
("/blog/how-to-evaluate-cost-segregation-study/", "How to evaluate a cost segregation study"),
],
"cta_head": "The Classification Decision Is Worth More Than the Study",
"cta_body": "On a parking structure, one determination drives the entire result. Send us the drawings and construction detail and we will assess it properly.",
},

{
"slug": "cost-segregation-breweries-and-distilleries",
"title": "Cost Segregation for Breweries and Distilleries: Production Equipment Meets Taproom",
"meta_title": "Cost Segregation for Breweries and Distilleries (2026) | AE Tax Advisors",
"meta_desc": "Breweries reclassify 40 to 55 percent of basis. Brewhouse, glycol, drainage, and taproom treatment under IRC Sec. 168 explained for owners in 2026.",
"category": C, "date": D,
"intro": [
"Breweries and distilleries reclassify at rates near the top of commercial real estate, commonly 40% to 55% of depreciable basis. The reason is that a production facility is industrial equipment with a bar attached, and both halves reclassify well.",
"The category most owners miss is not the tanks. It is the infrastructure serving them.",
],
"sections": [
("Production Equipment Is Obvious, Infrastructure Is Not", [
"Brewhouse vessels, fermenters, brite tanks, stills, mash tuns, chillers, pumps, packaging and canning lines, kegging equipment, grain handling, and laboratory equipment are five-year personal property under IRC Sec. 168(e)(3)(B). Most owners handle these correctly because they arrive on equipment invoices.",
"The infrastructure inside the construction contract is where the value hides. Glycol distribution loops, compressed air and CO2 lines, process water treatment and distribution, steam distribution, dedicated high-capacity electrical service and panels serving production equipment, and process drainage all exist to run equipment.",
"Under the functional analysis reflected in Treasury Regulation Sec. 1.48-1(e)(2), utilities serving specific equipment rather than the building generally are classified with the equipment they serve. On a production facility, this infrastructure alone commonly reaches 12% to 18% of construction cost.",
]),
("Floors and Drainage", [
"Trench drains, floor sinks, and the sloped and sealed floor systems in production areas are engineered for the process, not for the building. Epoxy and urethane cement flooring in a brewhouse is a chemical-resistant wear surface applied over a structural slab, and it is a finish rather than a structural component.",
"Wastewater pretreatment systems, required by many municipalities for brewery discharge, are equipment. So are the pH adjustment systems, holding tanks, and monitoring equipment supporting them.",
"On a facility with 12,000 square feet of production space, drainage and specialty flooring together are typically $180,000 to $400,000.",
]),
("Cold Storage and Walk-Ins", [
"Walk-in coolers and cold rooms are freestanding insulated equipment enclosures assembled inside a building. The panels, doors, refrigeration units, condensers, and controls are five-year property.",
"This is one of the most commonly misclassified items in food and beverage facilities, because a large walk-in looks like a room. It is equipment.",
]),
("The Taproom Reclassifies Like Retail", [
"Taprooms carry substantial five-year property. Draft systems including towers, lines, couplers, and glycol runs to the bar, bar equipment, ice machines, glass washers, point of sale hardware, sound and audiovisual systems, decorative and accent lighting, millwork and bar casework, furniture, and specialty finishes all qualify.",
"Outdoor beer gardens contribute 15-year land improvements: patio hardscape, fencing, shade structures, string lighting infrastructure, fire features, and landscaping.",
]),
("Worked Example: Production Brewery With Taproom", [
"An operator builds a 22,000 square foot brewery with a 3,400 square foot taproom for $8,900,000 including land. Land is $1,100,000, leaving $7,800,000 depreciable.",
"The study identifies five-year property of $3,432,000 (44%), covering brewhouse and cellar equipment, packaging, glycol and process utilities, drainage and specialty flooring, walk-ins, and the full taproom fit-out. Seven-year property is $234,000 (3%). Fifteen-year land improvements are $624,000 (8%), covering the beer garden, paving, and site work. Structure is $3,510,000 (45%).",
"Reclassified basis of $4,290,000 is deductible in year one under IRC Sec. 168(k), plus $90,000 of structural depreciation, for approximately $4,380,000 against $200,000 on a straight 39-year schedule.",
]),
("Operating Business Treatment", [
"A brewery is a trade or business, not a rental activity. The passive analysis under IRC Sec. 469 turns solely on material participation under Treasury Regulation Sec. 1.469-5T, and an owner-operator clears the 500-hour test easily.",
"The deduction is therefore non-passive and offsets other active income in the year taken, which is a materially better position than a real estate investor holds.",
"Where the building is owned through a separate entity leasing to the operating company, the self-rental rules under Treasury Regulation Sec. 1.469-2(f)(6) apply and a grouping election under Treasury Regulation Sec. 1.469-4 should be evaluated before the study is commissioned.",
]),
("Excise Tax and Inventory Are Separate Issues", [
"Federal excise tax on beer and spirits, TTB reporting, and inventory accounting for finished goods and raw materials are separate from the depreciation analysis but affect the same return.",
"Producers with average annual gross receipts under the IRC Sec. 448(c) threshold may treat inventory as non-incidental materials and supplies rather than applying full inventory accounting, which is simpler and often faster. This is worth reviewing alongside the study, since both are method questions.",
]),
],
"faqs": [
("What percentage does a brewery reclassify?",
 "Commonly 40% to 55% of depreciable basis. Production equipment is obvious, but the larger overlooked category is the infrastructure inside the construction contract: glycol loops, process water, compressed air and CO2, dedicated electrical, and process drainage."),
("Is glycol piping five-year property?",
 "Yes, where it serves production equipment rather than the building generally. Under the functional test in Treas. Reg. Sec. 1.48-1(e)(2), utilities serving specific equipment classify with that equipment. Glycol runs to fermenters and to the taproom draft system both qualify."),
("How are walk-in coolers classified?",
 "As five-year equipment. Panels, doors, refrigeration units, condensers, and controls are a freestanding insulated equipment enclosure assembled inside a building, not a structural component. This is among the most commonly misclassified items in food and beverage facilities."),
("Is epoxy flooring in the brewhouse deductible faster?",
 "Yes. Chemical-resistant epoxy and urethane cement flooring applied over a structural slab is a wear surface serving the process, treated as a finish rather than a structural component. The slab beneath it remains structure."),
("Can the deduction offset my other income?",
 "If you operate the brewery, yes. It is a trade or business rather than a rental activity, so only material participation under Treas. Reg. Sec. 1.469-5T applies and the loss is non-passive. If you own the building separately, review the self-rental rules first."),
],
"related": [
("/blog/cost-segregation-restaurants-qip-treatment/", "Cost segregation for restaurants and QIP"),
("/blog/self-rental-rules-business-rents-from-you/", "Self-rental rules explained"),
("/equipment-leasing/", "Equipment financing and Section 179 planning"),
],
"cta_head": "The Construction Contract Hides the Best Items",
"cta_body": "Most brewery studies find more value in the plumbing and electrical line items than in the tanks. Send us the contract detail and equipment schedule.",
},

{
"slug": "cost-segregation-manufacturing-facilities",
"title": "Cost Segregation for Manufacturing Facilities: Process Loads and Dedicated Utilities",
"meta_title": "Cost Segregation for Manufacturing Facilities (2026) | AE Tax Advisors",
"meta_desc": "Manufacturing plants reclassify 35 to 50 percent of basis. Process utilities, foundations, cranes, and specialty power under IRC Sec. 168 for 2026.",
"category": C, "date": D,
"intro": [
"Manufacturing facilities produce among the strongest cost segregation results in commercial real estate, commonly 35% to 50% of depreciable basis. The building is a shell, and nearly everything inside it exists to run a process.",
"The largest opportunity is almost always the electrical and mechanical infrastructure, which routinely sits inside a general contractor's line items rather than being broken out.",
],
"sections": [
("Dedicated Process Utilities", [
"A plant running CNC machining, injection molding, welding, or coating carries electrical service far beyond what the building itself requires. Transformers, switchgear, motor control centers, busway, panels, conduit, and wiring dedicated to production equipment are five-year property under the functional analysis reflected in Treasury Regulation Sec. 1.48-1(e)(2).",
"The same applies to compressed air distribution, process cooling water loops, dust and fume collection, process gas distribution, and dedicated exhaust. These serve equipment, not occupants.",
"General building lighting, office HVAC, restroom plumbing, and life safety systems remain structural. The distinction is function, and it requires an engineering review of the drawings rather than an allocation formula.",
"On a fitted plant, dedicated process utilities alone commonly reach 15% to 25% of construction cost.",
]),
("Equipment Foundations and Pits", [
"Reinforced concrete foundations poured specifically to support production equipment, isolation pads, machine pits, and below-grade trenches for utility runs to equipment are generally classified with the equipment they support rather than as building slab.",
"This is a meaningful item in heavy manufacturing. A press line requiring a 4-foot reinforced foundation with vibration isolation is not the same asset as the surrounding 6-inch floor slab, and it should not be depreciated as though it were.",
"Documentation of the structural purpose is what supports the classification, which means the study needs the structural drawings.",
]),
("Cranes, Hoists, and Material Handling", [
"Overhead bridge cranes, jib cranes, monorails, hoists, conveyors, and automated storage and retrieval systems are five-year property.",
"Crane runway beams and their supporting columns are a closer question. Where the runway system is integral to the building's structural frame, it is generally structural. Where it is a separate support system installed for the crane, it can often be classified with the crane. The construction method decides it.",
]),
("Specialty Environments", [
"Clean rooms, environmental chambers, paint booths, and curing ovens are equipment enclosures rather than building space. Wall and ceiling panel systems, HEPA filtration, dedicated air handling, and controls serving them are five-year property.",
"Paint booths in particular carry substantial ventilation, filtration, and fire suppression that exists entirely for the booth.",
]),
("Site Work on Industrial Property", [
"Fifteen-year land improvements typically run 8% to 14%. Manufacturing sites carry heavy-duty paving for truck traffic, rail spurs where present, trailer parking, dolly pads, site lighting, security fencing and gates, storm drainage and detention, oil-water separators, and outdoor material storage areas.",
"Rail spurs are worth calling out because they are large and are sometimes overlooked entirely. Track, ties, ballast, switches, and grade crossings are depreciable land improvements.",
]),
("Worked Example: 140,000 Square Foot Plant", [
"A manufacturer builds a 140,000 square foot plant for $23,600,000 including land. Land is $2,400,000, leaving $21,200,000 depreciable, excluding production machinery purchased separately.",
"The study identifies five-year property of $8,268,000 (39%), covering dedicated electrical distribution, compressed air, process cooling, dust collection, equipment foundations, crane systems, and paint booth infrastructure. Seven-year property is $636,000 (3%). Fifteen-year land improvements are $2,332,000 (11%). Structure is $9,964,000 (47%).",
"Reclassified basis of $11,236,000 is deductible in year one under IRC Sec. 168(k), plus $255,487 of structural depreciation, for approximately $11,491,487 against $543,590 on a straight 39-year schedule.",
"At a 32% blended rate, the first-year federal deferral exceeds $3,500,000.",
]),
("Interaction With Section 179 and State Rules", [
"Manufacturing owners frequently have both bonus depreciation and Sec. 179 available. Sec. 179 cannot create a loss and is elected asset by asset, which gives precision. Bonus has no dollar cap and can create a net operating loss.",
"For a plant expansion producing more deduction than income, bonus is generally the only provision that can absorb it.",
"State conformity matters more here than in most contexts because the dollar amounts are large. States requiring bonus addbacks with multi-year recovery, or decoupling entirely, produce state results that diverge sharply from the federal number. Model both before committing to a placed-in-service date.",
]),
],
"faqs": [
("What percentage does a manufacturing plant reclassify?",
 "Commonly 35% to 50% of depreciable basis. Dedicated process utilities are typically the largest category at 15% to 25% of construction cost, followed by equipment foundations, material handling, and specialty environments."),
("Are equipment foundations separate from the building slab?",
 "Generally yes, where they were poured specifically to support production equipment with isolation, reinforcement, or depth beyond what the building requires. The structural drawings are what support the classification, so a study needs them."),
("Is dedicated electrical service five-year property?",
 "Where it serves production equipment rather than the building generally, yes. Transformers, switchgear, motor control centers, busway, and dedicated conduit and wiring follow the equipment under Treas. Reg. Sec. 1.48-1(e)(2). General lighting and office power remain structural."),
("How are overhead cranes treated?",
 "The crane, hoist, and controls are five-year property. Runway beams and supports are a closer question: integral to the building frame means structural, while a separate support system installed for the crane can often be classified with it. Construction method decides."),
("Should I use Section 179 or bonus depreciation?",
 "For a large plant expansion, bonus depreciation is usually the only provision that can absorb the deduction, since Sec. 179 has a dollar cap and cannot create a loss. Sec. 179 is better where you want to land taxable income on a specific number or capture a state benefit."),
],
"related": [
("/blog/cost-segregation-warehouse-industrial-buildings/", "Cost segregation for warehouses and industrial buildings"),
("/blog/section-179-vs-bonus-depreciation-difference/", "Section 179 versus bonus depreciation"),
("/blog/equipment-depreciation-schedules-macrs-recovery-periods/", "MACRS recovery periods for equipment"),
],
"cta_head": "The Value Is in the Drawings",
"cta_body": "Manufacturing studies are won or lost on the electrical and mechanical documentation. Send us the construction contract and the drawing set.",
},

{
"slug": "cost-segregation-daycare-and-childcare-centers",
"title": "Cost Segregation for Daycare and Childcare Centers: Playgrounds, Casework, and Safety Systems",
"meta_title": "Cost Segregation for Daycare and Childcare Centers (2026) | AE Tax Advisors",
"meta_desc": "Childcare centers reclassify 30 to 42 percent of build-out cost. Playground surfacing, casework, safety systems, and QIP treatment explained for 2026.",
"category": C, "date": D,
"intro": [
"Childcare centers reclassify well, typically 30% to 42% of build-out cost, and the reasons are specific to the use. Licensing requirements drive substantial fixture, safety, and site investment that a generic commercial tenant does not carry.",
"The single largest item is usually outside the building.",
],
"sections": [
("Playgrounds Are a Major Component", [
"Licensed centers require age-segregated outdoor play areas with specific square footage per child, fall-height-rated surfacing, and secure fencing.",
"Playground equipment structures, swings, climbers, and play panels are five-year personal property. Poured-in-place rubber surfacing and engineered wood fiber systems are typically treated with the equipment they serve or as 15-year land improvements depending on installation, and the split should be documented.",
"Shade structures, fencing and gates, walkways, and site drainage serving the play areas are 15-year land improvements.",
"On a 12,000 square foot center serving 150 children, the outdoor program commonly runs $180,000 to $400,000 installed, a much larger share of total cost than at a comparable office or retail build-out.",
]),
("Interior Casework and Fixtures", [
"Cubby systems, low storage units, changing stations, child-height sinks and counters, activity tables, and classroom casework are manufactured equipment-grade fixtures rather than site-built structural millwork, generally classifying at five or seven years.",
"Kitchen equipment in centers providing meals follows standard food service treatment: ranges, refrigeration, walk-ins, dishwashing, and hoods are five-year property, along with the dedicated utilities serving them.",
"Laundry equipment, common in infant rooms, is five-year property with its dedicated plumbing and electrical.",
]),
("Safety and Security Systems", [
"Access control at every entry, camera systems covering classrooms and playgrounds, intercom and paging, parent notification systems, and check-in kiosks are five-year property along with the low-voltage cabling serving them.",
"Licensing drives coverage levels well beyond a typical commercial build-out, so this category is proportionally larger than in other property types.",
]),
("Finishes and Flooring", [
"Resilient and carpet flooring, rubber flooring in infant and toddler rooms, wall protection systems, decorative and accent lighting, acoustic treatments, and specialty wall coverings are five-year property.",
"Partition systems dividing age groups are worth review. Genuinely demountable partitions are personal property. Drywall on studs is structure.",
]),
("QIP Covers the Structural Remainder", [
"Most centers occupy existing nonresidential buildings. Interior improvements placed in service after the building itself generally qualify as qualified improvement property under IRC Sec. 168(e)(6), carrying a 15-year recovery period with full bonus eligibility.",
"That means new partition walls, ceilings, general lighting, and general HVAC in a leasehold build-out are recovered in year one under IRC Sec. 168(k) rather than over 39 years.",
"Between five-year property, 15-year land improvements, and QIP, a childcare build-out is frequently close to fully deductible in the opening year.",
]),
("Worked Example: 150-Child Center", [
"An operator completes an 11,800 square foot center for $2,240,000 in construction cost including site work, plus $310,000 of equipment and furnishings.",
"The study allocates construction to five-year property of $739,200 (33%), 15-year land improvements of $291,200 (13%), QIP of $1,097,600 (49%), and non-qualifying structural components of $112,000 (5%). All $310,000 of equipment is five-year property.",
"Under IRC Sec. 168(k), the five-year property, land improvements, QIP, and equipment are all bonus eligible, producing approximately $2,438,000 of first-year deduction against a $2,550,000 total investment.",
"At a 35% marginal rate that is roughly $853,000 of federal tax reduction in the opening year, when a center is typically at its lowest enrollment and highest debt service.",
]),
("Operating Business Treatment and Multi-Site Growth", [
"A childcare center is a trade or business. Material participation under Treasury Regulation Sec. 1.469-5T is not a close question for an owner-operator, so the deduction is non-passive and offsets other active income.",
"Operators opening a center a year generate a recurring deduction stream that offsets the profit from mature locations, which is the same structural advantage multi-site physical therapy and fitness operators enjoy.",
"Where the operator owns the real estate through a separate entity, the self-rental rules under Treasury Regulation Sec. 1.469-2(f)(6) apply and a grouping election under Treasury Regulation Sec. 1.469-4 should be evaluated before the study.",
]),
],
"faqs": [
("What percentage of a childcare build-out reclassifies?",
 "Typically 30% to 42% to five-year property, plus substantial 15-year land improvements from the playground program and 15-year QIP on the interior. Between all three, a leasehold build-out is often close to fully deductible in the opening year."),
("Is playground surfacing depreciable?",
 "Yes. Poured-in-place rubber and engineered wood fiber systems are depreciable, classified either with the play equipment they serve or as 15-year land improvements depending on installation. The play structures themselves are five-year personal property."),
("How is classroom casework classified?",
 "Cubbies, low storage, changing stations, child-height sinks and counters, and activity furniture are manufactured equipment-grade fixtures, generally five or seven year property rather than structural millwork."),
("What is QIP and does it apply to a daycare?",
 "Qualified improvement property under IRC Sec. 168(e)(6) is interior improvement to a nonresidential building placed in service after the building itself. It carries a 15-year life with full bonus eligibility, covering partition walls, ceilings, and general lighting and HVAC in a leasehold build-out."),
("Can I use the deduction against my other income?",
 "Yes, if you operate the center. It is a trade or business rather than a rental activity, so material participation under Treas. Reg. Sec. 1.469-5T controls and the loss is non-passive. Owners who also hold the real estate separately should review self-rental rules first."),
],
"related": [
("/blog/cost-segregation-fitness-centers-gyms/", "Cost segregation for gyms and fitness centers"),
("/blog/self-rental-rules-business-rents-from-you/", "Self-rental rules explained"),
("/blog/section-179-deduction-2026-complete-guide/", "Section 179 complete guide"),
],
"cta_head": "Opening Year Is When You Need the Cash",
"cta_body": "Childcare build-outs are largely deductible in year one when handled correctly. Send us the construction contract, site plan, and equipment list.",
},

{
"slug": "cost-segregation-auto-repair-and-collision-centers",
"title": "Cost Segregation for Auto Repair and Collision Centers: Lifts, Booths, and Compressed Air",
"meta_title": "Cost Segregation for Auto Repair and Collision Centers (2026) | AE Tax Advisors",
"meta_desc": "Repair and collision facilities reclassify 40 to 55 percent of basis. Lifts, paint booths, compressed air, and dedicated power under IRC Sec. 168 for 2026.",
"category": C, "date": D,
"intro": [
"Auto repair and collision facilities reclassify at rates near the top of the commercial range, commonly 40% to 55% of depreciable basis. The building is a steel shell with high bays and overhead doors. Everything that makes it a shop is equipment.",
"Collision centers with paint booths run higher still, because a booth is a substantial equipment package with its own ventilation, filtration, and fire suppression.",
],
"sections": [
("Lifts, Foundations, and Bay Equipment", [
"Vehicle lifts are five-year personal property, and so are the reinforced concrete foundations poured specifically to support them. A two-post or four-post lift requires a thickened, reinforced pad that differs from the surrounding slab, and that foundation is classified with the lift rather than as building floor.",
"Alignment racks, tire machines, balancers, brake lathes, diagnostic equipment, fluid distribution and evacuation systems, waste oil collection and heaters, and welding equipment are all five-year property.",
"In-ground lifts and their pits require the same analysis, with the pit structure and its drainage classified with the equipment it houses.",
]),
("Compressed Air and Dedicated Power", [
"Every bay runs compressed air. The compressor, dryer, receiver tank, and the entire distribution loop with drops at each bay exist to operate tools, not to serve the building.",
"Under the functional analysis reflected in Treasury Regulation Sec. 1.48-1(e)(2), this infrastructure classifies with the equipment it serves. So does the dedicated electrical service, panels, and receptacles feeding lifts, welders, and shop equipment.",
"General lighting, office HVAC, and restroom plumbing remain structural. On a 14-bay facility, compressed air and dedicated power alone commonly reach 8% to 12% of construction cost.",
]),
("Paint Booths and Prep Areas", [
"A downdraft paint booth is an equipment enclosure, not building space. The booth panels, doors, lighting, air makeup unit, exhaust fans, filtration, heating, and controls are five-year property.",
"Prep stations, mixing rooms with their explosion-proof electrical and ventilation, curing lamps, and the dedicated fire suppression serving the booth follow the same treatment.",
"Booth foundations and the pits for downdraft airflow are classified with the booth. On a collision center, the paint operation alone is frequently $350,000 to $900,000 of five-year property.",
]),
("Site Work Is Substantial", [
"Fifteen-year land improvements typically run 10% to 16%. Repair facilities require heavy-duty paving engineered for vehicle traffic and storage, large customer and vehicle storage lots, security fencing and gates, site lighting, drainage with oil-water separators, and signage foundations.",
"Collision centers carry particularly large storage lots for vehicles awaiting parts or insurance approval, and that acreage of paving is real basis.",
"Pylon and monument sign cabinets and their electrical service are five-year property, while the foundations are 15-year land improvements.",
]),
("Worked Example: Collision Center", [
"An operator builds a 22,000 square foot collision center for $5,600,000 including land. Land is $800,000, leaving $4,800,000 depreciable.",
"The study identifies five-year property of $2,208,000 (46%), covering lifts and foundations, frame machines, two paint booths with air makeup and filtration, prep stations, mixing room, compressed air distribution, dedicated power, and shop equipment. Seven-year property is $144,000 (3%). Fifteen-year land improvements are $672,000 (14%). Structure is $1,776,000 (37%).",
"Reclassified basis of $3,024,000 is deductible in year one under IRC Sec. 168(k), plus $45,538 of structural depreciation, for approximately $3,069,538 against $123,077 on a straight 39-year schedule.",
"At a 37% marginal rate for an owner-operator, that is roughly $1,090,000 of federal tax deferred in the first year.",
]),
("Operating Business Advantage", [
"A repair or collision shop is a trade or business, not a rental. The passive analysis under IRC Sec. 469 turns solely on material participation under Treasury Regulation Sec. 1.469-5T, and an owner-operator clears the 500-hour test without difficulty.",
"The deduction is non-passive and available against other active income immediately, which is a materially stronger position than a real estate investor holds with a comparable study.",
"Where the building sits in a separate entity leasing to the shop, self-rental rules under Treasury Regulation Sec. 1.469-2(f)(6) apply. A grouping election under Treasury Regulation Sec. 1.469-4 is frequently appropriate and should be evaluated before the study.",
]),
("Recapture Considerations", [
"With roughly 46% of basis in Sec. 1245 property, a sale generates substantial ordinary income recapture. Operators planning a five to seven year hold should model the exit rather than assume capital gain treatment on the whole gain.",
"This does not argue against the study. The deduction is worth far more than the recapture drag on a present value basis, particularly where the owner is in a high bracket now and anticipates a lower one later. But it should be modeled rather than discovered.",
]),
],
"faqs": [
("Are vehicle lift foundations part of the building?",
 "Generally no. A reinforced pad poured specifically to support a lift differs from the surrounding slab and is classified with the lift as five-year property. The structural drawings supporting that distinction should be in the study workpapers."),
("Is compressed air distribution five-year property?",
 "Yes, where it serves shop equipment rather than the building. The compressor, dryer, receiver, and the full distribution loop with bay drops exist to operate tools, and classify with that equipment under Treas. Reg. Sec. 1.48-1(e)(2)."),
("How is a paint booth classified?",
 "As equipment. The booth panels, doors, lighting, air makeup unit, exhaust, filtration, heating, controls, foundations, and dedicated fire suppression are all five-year property. On a collision center this is frequently $350,000 to $900,000 alone."),
("What percentage does a repair facility reclassify?",
 "Commonly 40% to 55% of depreciable basis. Collision centers with paint operations sit at the top of the range. General repair shops without paint typically land in the low forties."),
("Can the deduction offset my other income?",
 "Yes, if you operate the shop. It is a trade or business rather than a rental activity, so only material participation under Treas. Reg. Sec. 1.469-5T applies and the loss is non-passive. Owners holding the real estate separately should review self-rental rules first."),
],
"related": [
("/blog/cost-segregation-car-wash-facilities/", "Cost segregation for car washes"),
("/blog/tax-strategy-for-auto-dealership-owners/", "Tax strategy for auto dealership owners"),
("/blog/depreciation-recapture-planning/", "Depreciation recapture planning"),
],
"cta_head": "Shop Build-Outs Sit on the Wrong Schedule Constantly",
"cta_body": "If your construction contract went onto the books as one 39-year number, roughly half of it belongs somewhere else. Send us the contract and equipment schedule.",
},

{
"slug": "cost-segregation-ambulatory-surgery-centers",
"title": "Cost Segregation for Ambulatory Surgery Centers: Medical Gas, Sterile Processing, and OR Build-Out",
"meta_title": "Cost Segregation for Ambulatory Surgery Centers (2026) | AE Tax Advisors",
"meta_desc": "ASCs reclassify 40 to 55 percent of build-out cost. Medical gas, OR air handling, sterile processing, and QIP treatment explained for owners in 2026.",
"category": C, "date": D,
"intro": [
"Ambulatory surgery centers reclassify at the top of the healthcare range, commonly 40% to 55% of build-out cost. An operating room is a mechanical system with walls around it, and the systems serving it are equipment.",
"ASCs are also usually physician-owned through a syndicated structure, which makes the passive activity analysis unusually important and unusually favorable.",
],
"sections": [
("Medical Gas and Vacuum Systems", [
"Oxygen, nitrous oxide, medical air, and nitrogen distribution, along with the vacuum and waste anesthetic gas disposal systems, serve equipment and patients rather than the building.",
"Manifolds, source equipment, alarm panels, zone valve boxes, distribution piping, and outlets are five-year property under the functional analysis reflected in Treasury Regulation Sec. 1.48-1(e)(2).",
"On a four-OR center, the medical gas package alone commonly runs $180,000 to $350,000 installed, and it is routinely buried inside a mechanical contractor's line item.",
]),
("Operating Room Air Handling", [
"Operating rooms require dedicated air handling with high air change rates, HEPA filtration, positive pressure relationships, and precise temperature and humidity control. This is not building comfort HVAC.",
"Where an air handling unit and its distribution serve the OR environment specifically, it classifies with the function it serves rather than as general building mechanical. The same applies to the dedicated units serving sterile processing and to the negative pressure systems where present.",
"General office and waiting area HVAC remains structural. The split requires the mechanical drawings, which is why an engineering-based study matters more here than in simpler property types.",
]),
("Sterile Processing", [
"Autoclaves and steam sterilizers, washer disinfectors, ultrasonic cleaners, cart washers, and their dedicated steam, water treatment, drainage, and exhaust are five-year property.",
"Reverse osmosis and deionized water systems serving sterile processing are equipment. So are the stainless casework, sinks, and pass-through systems that make up the department.",
]),
("Imaging, Surgical Equipment, and Low Voltage", [
"C-arms, surgical microscopes, tables, lights, anesthesia machines, monitoring, electrosurgical units, endoscopy towers and reprocessors, and warming cabinets are five-year property, and most arrive on equipment invoices.",
"Boom systems and ceiling-mounted equipment columns are equipment, though their structural supports may be building. The distinction should be documented.",
"Low voltage is substantial: nurse call, clinical communications, camera systems, access control, data cabling, and the integration equipment tying them together. Lead shielding serving imaging equipment can often be classified with that equipment, while the framing and drywall around it remain structural.",
]),
("QIP Covers the Structural Remainder", [
"ASCs are typically built out in existing medical office buildings. Interior improvements placed in service after the building itself generally qualify as qualified improvement property under IRC Sec. 168(e)(6), with a 15-year recovery period and full bonus eligibility.",
"That covers partition walls, ceilings, general lighting, and general HVAC. Between five-year property and QIP, an ASC build-out is frequently close to fully deductible in the year it opens.",
"Note the QIP exclusions. Enlargements, elevators and escalators, and internal structural framework do not qualify and remain on the 39-year schedule.",
]),
("Worked Example: Four-OR Center", [
"A physician group completes a 16,400 square foot, four-OR ASC build-out for $6,900,000 in construction cost, plus $2,800,000 of medical equipment.",
"The study allocates construction to five-year property of $3,105,000 (45%), covering medical gas, OR air handling, sterile processing infrastructure, low voltage, casework, and finishes. QIP is $3,381,000 (49%). Non-qualifying structural components are $414,000 (6%). All $2,800,000 of equipment is five-year property.",
"Under IRC Sec. 168(k), five-year property, QIP, and equipment are all bonus eligible, producing approximately $9,286,000 of first-year deduction against a $9,700,000 total investment.",
]),
("The Passive Activity Analysis Is Favorable", [
"An ASC is an operating business, not a rental activity. For a physician-owner who performs cases at the center, material participation under Treasury Regulation Sec. 1.469-5T is generally satisfied through the significant participation or facts and circumstances tests, and often through the 500-hour test.",
"That makes the deduction non-passive and available against practice income and other active income immediately, which is a substantially better outcome than a syndicated real estate investment produces.",
"For a physician-owner with a small percentage interest who performs limited cases, the analysis is closer and should be documented. Participation hours should be tracked contemporaneously, particularly for owners whose primary practice is elsewhere.",
"Where the ASC leases its space from a related entity, the self-rental rules under Treasury Regulation Sec. 1.469-2(f)(6) apply to the property company, and a grouping election under Treasury Regulation Sec. 1.469-4 should be evaluated.",
]),
],
"faqs": [
("What percentage of an ASC build-out reclassifies?",
 "Commonly 40% to 55% of construction cost to five-year property, with most of the balance qualifying as 15-year QIP. Between the two, an ASC build-out is frequently close to fully deductible in the opening year."),
("Is medical gas piping five-year property?",
 "Yes. Manifolds, source equipment, alarm panels, zone valves, distribution piping, and outlets serve equipment and patients rather than the building, and classify with the function they serve under Treas. Reg. Sec. 1.48-1(e)(2)."),
("How is operating room HVAC treated?",
 "Where an air handling unit and its distribution serve the OR environment specifically, with high air change rates, HEPA filtration, and pressure control, it classifies with that function rather than as general building mechanical. Office and waiting area HVAC remains structural."),
("Can a physician owner use the deduction against practice income?",
 "Generally yes. An ASC is an operating business rather than a rental activity, so material participation under Treas. Reg. Sec. 1.469-5T controls. Physicians performing cases at the center typically satisfy it, making the loss non-passive."),
("What does not qualify as QIP?",
 "Enlargements of the building, elevators and escalators, and internal structural framework are excluded under IRC Sec. 168(e)(6) and remain on the 39-year schedule. Everything else in a qualifying interior improvement generally qualifies at 15 years with full bonus eligibility."),
],
"related": [
("/blog/cost-segregation-medical-office-buildings/", "Cost segregation for medical office buildings"),
("/blog/tax-strategy-for-surgeons/", "Tax strategy for surgeons"),
("/blog/how-does-syndication-k1-income-affect-my-taxes/", "How syndication K-1 income affects your taxes"),
],
"cta_head": "Document Participation Before the K-1 Arrives",
"cta_body": "The deduction is large and the passive analysis decides whether you can use it. Send us the build-out detail and your ownership and case volume.",
},

{
"slug": "cost-segregation-mixed-use-buildings",
"title": "Cost Segregation for Mixed Use Buildings: The 80 Percent Test and Split Schedules",
"meta_title": "Cost Segregation for Mixed Use Buildings (2026 Guide) | AE Tax Advisors",
"meta_desc": "Mixed use properties may be 27.5 or 39 year property depending on the 80 percent gross rental income test. How the classification and QIP split work in 2026.",
"category": C, "date": D,
"intro": [
"A building with apartments above and retail below raises a question that changes the entire depreciation schedule. Is it residential rental property on 27.5 years, or nonresidential real property on 39 years?",
"The answer is not a square footage allocation, and it is not split between the two uses. The whole building goes one way or the other, based on a gross rental income test that owners can partially influence.",
],
"sections": [
("The 80 Percent Gross Rental Income Test", [
"Under IRC Sec. 168(e)(2)(A), residential rental property means a building from which 80% or more of gross rental income for the taxable year is rental income from dwelling units.",
"The test is applied annually, on gross rental income, not on square footage, not on unit count, and not on value.",
"A building where apartments generate $920,000 and ground floor retail generates $210,000 has residential income of 81.4% and qualifies as residential rental property. The entire building, including the retail portion, depreciates over 27.5 years.",
"Shift the numbers slightly, to $880,000 residential and $240,000 retail, and residential income is 78.6%. The entire building, including the apartments, depreciates over 39 years.",
"This is a genuine cliff, and it can move year to year as leases roll. A building can qualify in one year and not the next, which creates real complexity in maintaining the schedule.",
]),
("What Counts Toward the Test", [
"The test looks at rental income from dwelling units. A dwelling unit is a house or apartment used to provide living accommodations, excluding units in a hotel, motel, or other establishment where more than half the units are used on a transient basis.",
"Short-term rental units within the building may therefore fail to count as dwelling units, which can push a building that looks residential over the line into nonresidential treatment.",
"Common area charges, parking income, laundry income, and other non-rental revenue are generally excluded from the computation on both sides, though the treatment of parking rented to residential tenants versus to the public warrants attention.",
"Where the building has vacant space, income from that space is zero, which can distort the ratio in either direction during lease-up or a re-tenanting period.",
]),
("Planning Around the Test", [
"Because the test turns on gross rental income, it responds to leasing decisions. An owner near the line who values 27.5-year treatment should be aware that adding retail rent or losing a residential tenant can flip it.",
"Where a building sits close to 80%, structuring the retail lease so that a larger share of the tenant's payment is a recovery of operating expenses rather than base rent may affect the computation, though the substance has to support the characterization.",
"Where a building is decisively nonresidential, the analysis shifts to maximizing QIP on the interior improvements rather than fighting for 27.5-year treatment.",
"This is worth modeling before signing a ground floor lease. The difference between a 27.5-year and 39-year schedule on a $9,000,000 building is roughly $97,000 of annual depreciation.",
]),
("The Cost Segregation Result Is Strong Either Way", [
"The classification affects only the structural component. The reclassified five-year and 15-year property is unaffected and is bonus eligible regardless.",
"Mixed use buildings reclassify well, typically 22% to 30%. Residential units contribute appliances, cabinetry, flooring, and window treatments. Retail space contributes tenant finish, decorative lighting, and dedicated power and data. Site work contributes parking, lighting, hardscape, and signage.",
"Qualified improvement property under IRC Sec. 168(e)(6) applies only to nonresidential real property. In a building classified as residential rental, the retail build-out does not qualify as QIP, which is a meaningful and frequently missed consequence of the 27.5-year classification.",
"That creates a genuine tradeoff. Residential classification gives a faster structural schedule but forfeits QIP treatment on the commercial build-out. Which is better depends on how much interior improvement work the owner funds.",
]),
("Worked Example: Urban Mixed Use", [
"An investor acquires a five-story building with 28 apartments and 6,800 square feet of ground floor retail for $11,400,000. Land is allocated at $1,900,000, leaving $9,500,000 depreciable.",
"Residential rents are $1,046,000 and retail rents are $238,000, so residential income is 81.5% of gross rental income. The building qualifies as residential rental property on a 27.5-year schedule.",
"A study identifies five-year property of $1,710,000 (18%) and 15-year land improvements of $855,000 (9%). Structure is $6,935,000 (73%).",
"Reclassified basis of $2,565,000 is deductible in year one under IRC Sec. 168(k), plus $252,182 of structural depreciation, for approximately $2,817,182.",
"Under 39-year treatment, structural depreciation would have been $177,821, roughly $74,000 less annually. Over a ten-year hold, the residential classification is worth approximately $740,000 of additional depreciation.",
"The offsetting cost is that the landlord's future retail build-out allowances will not qualify as QIP and will sit on the 27.5-year schedule instead of being fully deductible.",
]),
("Annual Testing and Documentation", [
"Because the test is applied annually, the classification should be recomputed each year and documented. A building that qualifies in year one and fails in year four presents a genuine question about the appropriate schedule going forward.",
"The conservative practice is to compute the ratio annually, retain the supporting rent roll, and address any change with a clear position rather than continuing on the original schedule by default.",
"Where the change is durable rather than temporary, a change in method of accounting on Form 3115 may be the appropriate mechanism to move to the correct recovery period.",
]),
],
"faqs": [
("Is a mixed use building 27.5-year or 39-year property?",
 "The entire building goes one way based on a single test. Under IRC Sec. 168(e)(2)(A), if 80% or more of gross rental income comes from dwelling units, the whole building is residential rental at 27.5 years. Below 80%, the whole building is nonresidential at 39 years."),
("Is the test based on square footage?",
 "No. It is based on gross rental income for the taxable year. A building where apartments occupy 85% of the square footage but produce only 76% of gross rental income fails the test and is nonresidential property."),
("Can the classification change from year to year?",
 "Yes, because the test is applied annually. Lease rollover, vacancy, or a rent increase on the commercial space can flip a building across the line. The ratio should be recomputed and documented each year rather than assumed."),
("Does QIP apply to the retail space in a residential building?",
 "No. Qualified improvement property under IRC Sec. 168(e)(6) applies only to nonresidential real property. In a building classified as residential rental, commercial tenant improvements do not qualify as QIP, which is a real and frequently missed cost of that classification."),
("Do short-term rental units count as dwelling units?",
 "Often not. A dwelling unit excludes units in an establishment where more than half the units are used on a transient basis. Short-term rental units within a mixed use building can push the residential income ratio below 80% and change the whole building's schedule."),
],
"related": [
("/blog/landlord-guide-depreciation-27-5-vs-39-year/", "27.5 versus 39 year depreciation"),
("/blog/cost-segregation-small-multifamily-5-20-units/", "Cost segregation for small multifamily"),
("/blog/cost-segregation-retail-strip-centers/", "Cost segregation for retail strip centers"),
],
"cta_head": "Run the Test Before You Sign the Retail Lease",
"cta_body": "The 80 percent line moves with your rent roll and it decides your whole schedule. Send us the rent roll and we will compute where you stand.",
},
]

if __name__ == "__main__":
    write_all(ARTICLES)
