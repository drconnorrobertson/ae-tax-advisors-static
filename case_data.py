#!/usr/bin/env python3
"""Reference data for anonymized case study generation.

Nothing in this file identifies a real person. Professions, states, and property
descriptors are combined to build representative scenarios; all figures are
computed by the engine so each study is internally consistent.
"""

# State top marginal individual rates, approximate for 2026. Used only to
# compute an illustrative combined rate, never presented as authoritative.
STATES = [
    ("Montana", 0.059), ("Texas", 0.0), ("Florida", 0.0), ("Tennessee", 0.0),
    ("Nevada", 0.0), ("Washington", 0.0), ("Wyoming", 0.0), ("South Dakota", 0.0),
    ("Alaska", 0.0), ("New Hampshire", 0.0), ("California", 0.133),
    ("New York", 0.109), ("New Jersey", 0.1075), ("Oregon", 0.099),
    ("Minnesota", 0.0985), ("Massachusetts", 0.09), ("Hawaii", 0.11),
    ("Vermont", 0.0875), ("Wisconsin", 0.0765), ("Maine", 0.0715),
    ("South Carolina", 0.062), ("Connecticut", 0.0699), ("Idaho", 0.05695),
    ("Utah", 0.0455), ("Colorado", 0.044), ("Arizona", 0.025),
    ("North Carolina", 0.0425), ("Georgia", 0.0519), ("Illinois", 0.0495),
    ("Pennsylvania", 0.0307), ("Ohio", 0.035), ("Michigan", 0.0425),
    ("Virginia", 0.0575), ("Maryland", 0.0575), ("Missouri", 0.047),
    ("Kansas", 0.0558), ("Oklahoma", 0.0475), ("Arkansas", 0.039),
    ("Alabama", 0.05), ("Mississippi", 0.044), ("Louisiana", 0.03),
    ("Kentucky", 0.04), ("Indiana", 0.0305), ("Iowa", 0.038),
    ("Nebraska", 0.052), ("New Mexico", 0.059), ("West Virginia", 0.0482),
    ("Delaware", 0.066), ("Rhode Island", 0.0599), ("North Dakota", 0.025),
]

NO_TAX_STATES = {s for s, r in STATES if r == 0.0}

# States with an enacted pass-through entity tax workaround (illustrative set).
PTET_STATES = [
    "California", "New York", "New Jersey", "Minnesota", "Illinois", "Georgia",
    "Colorado", "Massachusetts", "Connecticut", "Oregon", "Wisconsin",
    "South Carolina", "Arizona", "Louisiana", "Michigan", "Ohio", "Maryland",
    "Virginia", "North Carolina", "Oklahoma", "Kansas", "Alabama", "Missouri",
    "New Mexico", "Rhode Island", "Utah", "Idaho", "Iowa", "Arkansas",
]

# ---------------------------------------------------------------- STR
STR_TYPES = [
    ("beachfront cottage", "coastal", ["Outer Banks", "Gulf Coast", "Emerald Coast",
        "Cape Cod", "the Alabama coast", "the Oregon coast", "Amelia Island",
        "the Jersey Shore", "Padre Island", "the Carolina coast"]),
    ("mountain cabin", "mountain", ["the Smoky Mountains", "the Blue Ridge",
        "the Wasatch Range", "the Poconos", "the White Mountains", "the Ozarks",
        "the Sierra foothills", "the Bitterroot Valley", "the San Juans",
        "the Green Mountains"]),
    ("downtown loft", "urban", ["a downtown arts district", "a riverfront district",
        "a historic downtown core", "a convention district", "a university district",
        "a medical district", "a stadium district", "a revitalized warehouse district"]),
    ("lake house", "lake", ["Lake of the Ozarks", "Table Rock Lake", "Lake Norman",
        "Flathead Lake", "Lake Chelan", "Finger Lakes region", "Lake Travis",
        "Deep Creek Lake", "Lake Michigan shoreline", "Smith Mountain Lake"]),
    ("ski-in condo", "ski", ["a Rocky Mountain ski corridor", "a New England ski region",
        "a Sierra Nevada resort area", "a Wasatch resort corridor",
        "a northern Michigan ski area"]),
    ("desert casita", "desert", ["greater Phoenix", "the Sonoran corridor",
        "the Palm Springs area", "southern Utah near the national parks",
        "the high desert"]),
    ("wine country cottage", "vineyard", ["a Napa Valley corridor",
        "the Willamette Valley", "the Finger Lakes wine region",
        "the Texas Hill Country", "a Virginia wine corridor"]),
    ("historic townhouse", "urban", ["a French Quarter adjacent district",
        "a historic garden district", "a preserved downtown district",
        "a waterfront historic district"]),
]

# ---------------------------------------------------------------- LTR
LTR_TYPES = [
    ("single-family rental portfolio", "four single-family rentals"),
    ("duplex", "a side-by-side duplex"),
    ("triplex", "a three-unit building"),
    ("fourplex", "a four-unit building"),
    ("small apartment building", "a twelve-unit apartment building"),
    ("mid-size apartment complex", "a thirty-four-unit garden complex"),
    ("townhome portfolio", "six attached townhomes"),
    ("mixed residential portfolio", "a nine-property residential portfolio"),
    ("student housing property", "a purpose-built student housing property"),
    ("workforce housing complex", "a twenty-two-unit workforce housing property"),
]

# ---------------------------------------------------------------- Commercial
COMMERCIAL_TYPES = [
    # (label, reclass low, reclass high, descriptor)
    ("restaurant", 0.30, 0.40, "a full-service restaurant building"),
    ("quick-service restaurant", 0.32, 0.41, "a drive-through quick-service location"),
    ("boutique hotel", 0.33, 0.44, "a boutique hotel"),
    ("limited-service motel", 0.29, 0.36, "a limited-service motel"),
    ("self-storage facility", 0.27, 0.39, "a climate-controlled self-storage facility"),
    ("medical office building", 0.22, 0.32, "a multi-specialty medical office building"),
    ("dental practice building", 0.24, 0.34, "a purpose-built dental office"),
    ("veterinary clinic", 0.25, 0.35, "a small-animal veterinary clinic"),
    ("warehouse and distribution facility", 0.14, 0.24, "a distribution warehouse"),
    ("flex industrial building", 0.17, 0.27, "a flex industrial building"),
    ("multifamily property", 0.22, 0.33, "a garden-style apartment community"),
    ("retail strip center", 0.20, 0.30, "a multi-tenant retail strip center"),
    ("car wash", 0.35, 0.46, "an express tunnel car wash"),
    ("auto service center", 0.26, 0.36, "a multi-bay auto service center"),
    ("day care center", 0.25, 0.35, "a licensed early childhood center"),
    ("fitness facility", 0.28, 0.38, "a full-service fitness facility"),
    ("assisted living facility", 0.24, 0.34, "an assisted living community"),
    ("brewery and taproom", 0.31, 0.41, "a production brewery with taproom"),
    ("office building", 0.15, 0.25, "a suburban office building"),
    ("mobile home park", 0.30, 0.42, "a manufactured housing community"),
]

# ---------------------------------------------------------------- Businesses
BUSINESS_TYPES = [
    "an e-commerce brand", "a digital marketing agency", "a general contracting firm",
    "a specialty trades contractor", "an IT managed services provider",
    "a residential landscaping company", "a commercial cleaning company",
    "an insurance agency", "a freight brokerage", "a boutique law practice",
    "an architecture studio", "an engineering consultancy", "a physical therapy practice",
    "a chiropractic practice", "an optometry practice", "a dental practice",
    "a med spa", "a veterinary practice", "a staffing firm",
    "a management consulting practice", "a wealth management practice",
    "a bookkeeping and CFO services firm", "a software development shop",
    "a SaaS company", "a food manufacturing business", "a craft beverage producer",
    "a HVAC contracting business", "an electrical contracting business",
    "a plumbing contractor", "a roofing contractor", "a fencing and decking company",
    "a pool construction company", "a custom cabinetry shop", "a print and signage shop",
    "a photography and video studio", "an event production company",
    "a franchise restaurant group", "a fitness studio group", "a salon and spa group",
    "a pet care and boarding business", "a trucking and logistics company",
    "an equipment rental business", "a security systems installer",
    "a solar installation company", "a medical billing company",
    "a home health agency", "a tutoring and enrichment company",
    "a specialty pharmacy", "a diagnostic imaging center", "a surgical practice",
]

PROFESSIONS_W2 = [
    "an emergency medicine physician", "an anesthesiologist", "a radiologist",
    "a hospitalist", "an orthopedic surgeon", "a cardiologist", "a dermatologist",
    "a psychiatrist", "a CRNA", "a pharmacist executive",
    "a software engineering director", "a principal software engineer",
    "a data science lead", "a product management director",
    "a petroleum engineer", "a structural engineering principal",
    "an aerospace systems engineer", "a semiconductor design engineer",
    "an investment banking vice president", "a private equity principal",
    "a corporate finance executive", "a regional sales director",
    "a pharmaceutical sales executive", "a commercial airline captain",
    "a technology sales executive", "a management consulting partner",
    "a marketing vice president", "a supply chain executive",
    "a biotech research director", "an actuarial director",
    "a corporate attorney", "a litigation partner", "a patent attorney",
    "a university department chair", "a hospital administrator",
    "an engineering program manager", "a cybersecurity director",
    "a chief technology officer", "a chief operating officer",
    "a clinical director",
]

PRACTICE_TYPES = [
    "a family dental practice", "an orthodontic practice", "an oral surgery practice",
    "a dermatology practice", "an ophthalmology practice", "a cardiology group",
    "an orthopedic group", "a pediatric practice", "an internal medicine practice",
    "a physical therapy group", "a behavioral health practice",
    "an anesthesia group", "a radiology group", "a urology practice",
    "an ENT practice", "a plastic surgery practice", "a fertility practice",
    "a dermatopathology lab", "a sleep medicine practice", "a pain management practice",
]

# Narrative connectors used to vary sentence openings across studies.
OPENERS = [
    "The client came to us", "This engagement began", "We were introduced to this client",
    "The situation arrived", "This client reached out", "We picked up this engagement",
    "The client engaged us", "This case came in",
]
