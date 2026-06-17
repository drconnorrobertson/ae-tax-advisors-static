import re, datetime

new_slugs = [
    "s-corp-officer-comp-correction", "s-corp-qbi-threshold-optimization",
    "s-corp-payroll-setup-sole-prop", "s-corp-multiple-businesses",
    "s-corp-late-election-relief", "sole-prop-to-s-corp-contractor",
    "s-corp-to-c-corp-medical", "partnership-to-s-corp",
    "multi-entity-holding-company", "w2-rsu-donation-daf",
    "w2-backdoor-roth-mega", "w2-salt-cap-ptet-workaround",
    "amended-returns-missed-depreciation", "amended-returns-wrong-entity",
    "multi-entity-real-estate-operating", "multi-entity-family-income-splitting",
    "ecommerce-amazon-fba-s-corp", "ecommerce-dropship-multistate",
    "dental-practice-cost-seg-dso", "construction-completed-contract",
    "construction-equipment-section-179", "restaurant-cost-seg-tip-credit",
    "tech-startup-rd-credit-qsbs", "tech-founder-equity-comp-83b",
    "consultant-six-figure-s-corp", "freelancer-home-office-vehicle",
    "real-estate-broker-team-entity",
    "str-lake-house-cost-seg", "str-portfolio-five-properties",
    "str-form-3115-catchup", "str-mountain-cabin-bonus-dep",
    "ltr-duplex-cost-seg", "ltr-apartment-building-24-units",
    "ltr-section-1250-recapture-planning", "ltr-inherited-property-step-up",
    "w2-couple-str-offset", "amended-returns-missed-cost-seg",
    "physician-w2-str-reps", "hotel-boutique-renovation-cost-seg",
    "real-estate-agent-investment-portfolio",
]

today = "2026-06-16"

with open('/sessions/admiring-festive-hopper/ae-tax-site/sitemap.xml', 'r') as f:
    sitemap = f.read()

# Build new entries
new_entries = []
for slug in new_slugs:
    entry = f"""  <url>
    <loc>https://aetaxadvisors.com/case-studies/{slug}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>"""
    new_entries.append(entry)

# Insert before </urlset>
insert_text = '\n'.join(new_entries) + '\n'
sitemap = sitemap.replace('</urlset>', insert_text + '</urlset>')

with open('/sessions/admiring-festive-hopper/ae-tax-site/sitemap.xml', 'w') as f:
    f.write(sitemap)

print(f"Added {len(new_slugs)} URLs to sitemap.xml")
# Verify
count = sitemap.count('<url>')
print(f"Total URLs in sitemap: {count}")
