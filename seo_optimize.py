#!/usr/bin/env python3
"""
AE Tax Advisors - Comprehensive SEO Optimization Script
Handles: pillar-cluster linking, service cross-linking, location linking,
blog index optimization, on-page SEO fixes, sitemap verification, breadcrumbs
"""

import os
import re
import json
from collections import defaultdict
from pathlib import Path

SITE_ROOT = "/tmp/ae-tax-seo2"
BASE_URL = "https://aetaxadvisors.com"

# ============================================================
# CONFIGURATION: Content taxonomy and linking rules
# ============================================================

PILLAR_PAGES = {
    "cost-seg": {
        "path": "/cost-segregation-studies-for-real-estate-investors/",
        "title": "Cost Segregation Studies",
        "keywords": ["cost segregation", "cost seg", "depreciation", "macrs", "bonus depreciation", 
                      "form 3115", "lookback", "accelerated depreciation", "section 168", 
                      "partial asset disposition", "component reclassification"],
    },
    "tax-planning": {
        "path": "/advanced-tax-planning-services/",
        "title": "Advanced Tax Planning",
        "keywords": ["tax planning", "tax strategy", "tax advisory", "tax reduction", 
                      "tax savings", "proactive tax", "tax optimization", "strategic tax",
                      "three-year lookback", "tax assessment"],
    },
    "entity-structuring": {
        "path": "/business-owner-tax-planning/",
        "title": "Business Owner Tax Planning",
        "keywords": ["entity structuring", "s-corp", "c-corp", "llc", "business structure",
                      "entity optimization", "section 199a", "qbi deduction", "reasonable compensation",
                      "entity election", "form 2553", "holding company"],
    },
    "bookkeeping": {
        "path": "/services/bookkeeping/",
        "title": "Bookkeeping Services",
        "keywords": ["bookkeeping", "financial statements", "accounting records", 
                      "financial reporting", "monthly bookkeeping", "reconciliation"],
    },
}

SERVICE_PAGES = {
    "/services/cost-segregation/": {
        "title": "Cost Segregation Studies",
        "related": ["/services/tax-planning/", "/services/entity-structuring/", "/services/bookkeeping/"],
        "pillar": "cost-seg",
    },
    "/services/tax-planning/": {
        "title": "Strategic Tax Planning",
        "related": ["/services/cost-segregation/", "/services/entity-structuring/", "/services/bookkeeping/"],
        "pillar": "tax-planning",
    },
    "/services/entity-structuring/": {
        "title": "Entity Structuring",
        "related": ["/services/tax-planning/", "/services/cost-segregation/", "/services/bookkeeping/"],
        "pillar": "entity-structuring",
    },
    "/services/bookkeeping/": {
        "title": "Bookkeeping Services",
        "related": ["/services/tax-planning/", "/services/cost-segregation/", "/services/entity-structuring/"],
        "pillar": "bookkeeping",
    },
}

LOCATION_PAGES = {
    "/locations/baltimore/": "Baltimore, MD",
    "/locations/billings/": "Billings, MT",
}

# Category classification for blog posts
CATEGORY_KEYWORDS = {
    "Cost Segregation": ["cost segregation", "cost seg", "depreciation", "macrs", "form 3115", 
                          "section 168", "bonus depreciation", "lookback depreciation", "partial asset disposition"],
    "Entity Structuring": ["entity structur", "s-corp", "c-corp", "llc", "business structure", 
                            "form 2553", "section 199a", "qbi deduction", "reasonable compensation",
                            "entity restructur", "holding company"],
    "Tax Planning": ["tax planning", "tax strategy", "tax advisory", "tax reduction", "tax savings",
                      "proactive tax", "strategic tax", "tax optimization", "tax assessment"],
    "Real Estate": ["real estate", "rental propert", "str ", "short-term rental", "long-term rental",
                     "real estate professional", "material participation", "passive loss",
                     "1031 exchange", "rental income", "investment property"],
    "Business Owners": ["business owner", "small business", "business tax", "entrepreneur",
                         "practice owner", "professional service", "augusta rule"],
    "IRS Compliance": ["irs audit", "audit defense", "irs representation", "tax compliance",
                        "amended return", "installment agreement", "currently not collectible"],
}

# Stats tracking
stats = {
    "pillar_links_added": 0,
    "blog_contextual_links_added": 0,
    "service_crosslinks_added": 0,
    "location_links_added": 0,
    "breadcrumbs_added": 0,
    "seo_fixes": 0,
    "sitemap_entries_added": 0,
    "sitemap_entries_removed": 0,
    "broken_links_fixed": 0,
    "alt_text_added": 0,
    "blog_index_categories_added": 0,
    "duplicate_titles_fixed": 0,
}

# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def read_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def get_all_pages():
    """Get all HTML pages in the site."""
    pages = {}
    for root, dirs, files in os.walk(SITE_ROOT):
        dirs[:] = [d for d in dirs if d != ".git" and d != "scripts"]
        for f in files:
            if f == "index.html":
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(root, SITE_ROOT)
                if rel_path == ".":
                    url_path = "/"
                else:
                    url_path = "/" + rel_path + "/"
                pages[url_path] = full_path
    return pages

def get_title(content):
    m = re.search(r"<title>(.*?)</title>", content, re.DOTALL)
    return m.group(1).strip() if m else ""

def get_h1(content):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.DOTALL)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""

def get_meta_desc(content):
    m = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', content)
    return m.group(1).strip() if m else ""

def classify_page(url_path, content):
    """Classify a page into categories based on URL and content."""
    categories = []
    text = (url_path + " " + content).lower()
    for cat, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                categories.append(cat)
                break
    return categories if categories else ["Tax Planning"]

def is_blog_post(url_path):
    """Determine if a URL is a blog post (not a service/location/utility page)."""
    non_blog = ["/services/", "/locations/", "/about/", "/contact/", "/discovery/",
                "/privacy-policy/", "/terms-of-service/", "/disclaimer/", "/faq/",
                "/ae-tax-advisors-faq/", "/case-studies/", "/guides/", "/glossary/",
                "/bios/", "/blog/", "/404", "/30-minute-consultation/", "/45-minute-consultation/",
                "/nick-zoom/", "/ashley-45min/", "/mark-zoom/", "/30-day-followup/",
                "/30-day-recap/", "/tax-services/", "/focused-strategies/",
                "/individual-tax-planning-high-earners/", "/business-owner-small-business-tax/",
                "/deferred-equity-compensation/", "/retirement-exit-ma-tax-strategy/",
                "/multi-state-global-tax/", "/estate-trust-wealth-transfer/",
                "/tax-compliance-irs-representation/", "/cost-segregation-studies-for-real-estate-investors/",
                "/advanced-tax-planning-services/", "/business-owner-tax-planning/",
                "/short-term-rental-tax-strategy/", "/equipment-leasing-section-179/",
                "/crypto-mining-tax-strategy/", "/real-estate-bookkeeping/",
                "/who-founded-ae-tax-advisors/"]
    if url_path == "/":
        return False
    for prefix in non_blog:
        if url_path == prefix or url_path.startswith(prefix):
            return False
    return True

def get_page_relevance_score(url_path, content, keywords):
    """Score how relevant a page is to a set of keywords."""
    text = (url_path.replace("-", " ") + " " + get_h1(content) + " " + get_title(content)).lower()
    body_text = re.sub(r"<[^>]+>", " ", content).lower()
    score = 0
    for kw in keywords:
        if kw in text:
            score += 3  # Title/URL match is high value
        if kw in body_text:
            score += 1
    return score


# ============================================================
# 1. PILLAR-CLUSTER INTERNAL LINKING
# ============================================================

def add_pillar_related_articles(pages):
    """Add Related Articles sections to pillar pages."""
    print("\n=== Adding Related Articles to Pillar Pages ===")
    
    # Score all blog posts against each pillar
    blog_posts = {}
    for url, filepath in pages.items():
        if is_blog_post(url) or url.startswith("/blog/"):
            if url == "/blog/":
                continue
            content = read_file(filepath)
            h1 = get_h1(content)
            if h1:
                blog_posts[url] = {"filepath": filepath, "content": content, "h1": h1}
    
    for pillar_key, pillar_info in PILLAR_PAGES.items():
        pillar_path = pillar_info["path"]
        if pillar_path not in pages:
            print(f"  WARNING: Pillar page not found: {pillar_path}")
            continue
        
        filepath = pages[pillar_path]
        content = read_file(filepath)
        
        # Score and rank blog posts
        scored = []
        for url, post in blog_posts.items():
            score = get_page_relevance_score(url, post["content"], pillar_info["keywords"])
            if score > 0:
                scored.append((score, url, post["h1"]))
        
        scored.sort(reverse=True)
        top_posts = scored[:10]
        
        if not top_posts:
            print(f"  No relevant posts found for {pillar_key}")
            continue
        
        # Build Related Articles HTML
        articles_html = '\n    <section class="content-section fade-in-section" style="background: var(--neutral-50, #f8f9fa);">\n'
        articles_html += '        <div class="container narrow">\n'
        articles_html += f'            <h2>Related Articles: {pillar_info["title"]}</h2>\n'
        articles_html += '            <p>Explore our in-depth articles on this topic:</p>\n'
        articles_html += '            <ul style="list-style: none; padding: 0;">\n'
        
        for score, url, h1 in top_posts:
            articles_html += f'                <li style="margin-bottom: 12px; padding: 12px 16px; background: var(--white, #fff); border-radius: 8px; border: 1px solid rgba(0,0,0,0.06);"><a href="{url}" style="color: var(--accent, #C9A44A); font-weight: 500; text-decoration: none;">{h1}</a></li>\n'
            stats["pillar_links_added"] += 1
        
        articles_html += '            </ul>\n'
        # Add links to service pages
        articles_html += '            <p style="margin-top: 24px;"><strong>Related Services:</strong> '
        service_links = []
        for svc_path, svc_info in SERVICE_PAGES.items():
            if svc_path != pillar_path:
                service_links.append(f'<a href="{svc_path}" style="color: var(--accent, #C9A44A);">{svc_info["title"]}</a>')
                stats["pillar_links_added"] += 1
        articles_html += " | ".join(service_links)
        articles_html += '</p>\n'
        # Add location links
        articles_html += '            <p><strong>Serving:</strong> '
        loc_links = []
        for loc_path, loc_name in LOCATION_PAGES.items():
            loc_links.append(f'<a href="{loc_path}" style="color: var(--accent, #C9A44A);">{loc_name}</a>')
            stats["pillar_links_added"] += 1
        articles_html += " | ".join(loc_links)
        articles_html += '</p>\n'
        articles_html += '        </div>\n'
        articles_html += '    </section>\n'
        
        # Insert before CTA section
        if '<section class="cta-section' in content:
            content = content.replace(
                '<section class="cta-section',
                articles_html + '\n    <section class="cta-section'
            )
        else:
            content = content.replace("</main>", articles_html + "\n    </main>")
        
        write_file(filepath, content)
        print(f"  Added {len(top_posts)} related articles to {pillar_key} pillar page")
    
    return blog_posts


def add_contextual_links_to_blog_posts(pages, blog_posts):
    """Add contextual internal links within blog post body text."""
    print("\n=== Adding Contextual Links to Blog Posts ===")
    
    # Get the newest 50 blog posts (by date in content or by path)
    blog_with_dates = []
    for url, post in blog_posts.items():
        date_match = re.search(r'"datePublished":\s*"(\d{4}-\d{2}-\d{2})"', post["content"])
        if not date_match:
            date_match = re.search(r'Published on (\w+ \d+, \d{4})', post["content"])
        date_str = date_match.group(1) if date_match else "2020-01-01"
        blog_with_dates.append((date_str, url, post))
    
    blog_with_dates.sort(reverse=True)
    target_posts = blog_with_dates[:50]
    
    # Link insertion rules: keyword -> (url, anchor text)
    link_rules = [
        # Service pages
        ("cost segregation stud", "/services/cost-segregation/", "cost segregation studies"),
        ("cost segregation", "/cost-segregation-studies-for-real-estate-investors/", "cost segregation"),
        ("strategic tax planning", "/services/tax-planning/", "strategic tax planning"),
        ("tax planning services", "/advanced-tax-planning-services/", "tax planning services"),
        ("entity structuring", "/services/entity-structuring/", "entity structuring"),
        ("entity structure", "/business-owner-tax-planning/", "entity structuring for business owners"),
        ("bookkeeping", "/services/bookkeeping/", "bookkeeping services"),
        # Key blog posts (newer ones)
        ("form 3115", "/blog/3115-change-accounting-method-playbook/", "Form 3115"),
        ("real estate professional status", "/blog/real-estate-professional-status-qualification-guide/", "real estate professional status"),
        ("material participation", "/blog/material-participation-str-investors/", "material participation"),
        ("bonus depreciation", "/blog/bonus-depreciation-2025-2026-real-estate-investors/", "bonus depreciation"),
        ("partial asset disposition", "/blog/partial-asset-disposition-overlooked-tax-strategy/", "partial asset disposition"),
        ("section 168", "/blog/irc-section-168-accelerated-depreciation-explained/", "IRC Section 168"),
        ("s-corp to c-corp", "/blog/s-corp-to-c-corp-conversion-when-it-makes-sense/", "S-Corp to C-Corp conversion"),
        ("augusta rule", "/blog/augusta-rule-rent-your-home-to-your-business/", "the Augusta Rule"),
        ("qbi deduction", "/blog/qbi-deduction-optimization-real-estate/", "QBI deduction optimization"),
        ("llc structure", "/blog/structure-llcs-asset-protection-tax-benefit/", "LLC structuring"),
        ("lookback depreciation", "/blog/lookback-depreciation-recovering-missed-deductions/", "lookback depreciation"),
        ("1031 exchange", "/blog/1031-exchange-alternatives/", "1031 exchange strategies"),
        ("depreciation recapture", "/blog/depreciation-recapture-planning/", "depreciation recapture planning"),
    ]
    
    links_added = 0
    for date_str, url, post in target_posts:
        filepath = post["filepath"]
        content = read_file(filepath)
        
        # Find the main content area
        main_match = re.search(r'(<div class="post-content">)(.*?)(</div>\s*</div>\s*</section>)', content, re.DOTALL)
        if not main_match:
            # Try alternate structure for /blog/ posts
            main_match = re.search(r'(<div class="container narrow">)(.*?)(</div>\s*</section>\s*</main>)', content, re.DOTALL)
        if not main_match:
            continue
        
        body = main_match.group(2)
        original_body = body
        links_in_this_post = 0
        max_links = 5  # Don't over-link
        
        for keyword, link_url, anchor_text in link_rules:
            if links_in_this_post >= max_links:
                break
            if link_url == url:  # Don't link to self
                continue
            if f'href="{link_url}"' in body:  # Already linked
                continue
            
            # Find keyword in text (not inside HTML tags or existing links)
            pattern = re.compile(
                r'(?<![<>/"\'])(?<!</a)(?<!href=")(' + re.escape(keyword) + r')(?![^<]*>)(?![^<]*</a>)',
                re.IGNORECASE
            )
            
            match = pattern.search(body)
            if match:
                # Replace first occurrence only
                replacement = f'<a href="{link_url}">{anchor_text}</a>'
                body = body[:match.start()] + replacement + body[match.end():]
                links_in_this_post += 1
                links_added += 1
        
        if body != original_body:
            content = content[:main_match.start(2)] + body + content[main_match.end(2):]
            write_file(filepath, content)
    
    stats["blog_contextual_links_added"] = links_added
    print(f"  Added {links_added} contextual links across {len(target_posts)} blog posts")


# ============================================================
# 2. SERVICE PAGE CROSS-LINKING
# ============================================================

def add_service_crosslinks(pages):
    """Add 'You May Also Need' sections to service pages."""
    print("\n=== Adding Service Page Cross-Links ===")
    
    for svc_path, svc_info in SERVICE_PAGES.items():
        if svc_path not in pages:
            print(f"  WARNING: Service page not found: {svc_path}")
            continue
        
        filepath = pages[svc_path]
        content = read_file(filepath)
        
        # Build "You May Also Need" section
        crosslink_html = '\n    <section class="content-section fade-in-section" style="background: var(--neutral-50, #f8f9fa);">\n'
        crosslink_html += '        <div class="container narrow">\n'
        crosslink_html += '            <h2>You May Also Need</h2>\n'
        crosslink_html += '            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">\n'
        
        for related_path in svc_info["related"]:
            if related_path in SERVICE_PAGES:
                related_info = SERVICE_PAGES[related_path]
                desc_map = {
                    "/services/cost-segregation/": "Accelerate depreciation deductions on investment properties with IRS-compliant engineering studies.",
                    "/services/tax-planning/": "Year-round proactive tax strategy with IRC-cited analysis and quarterly planning sessions.",
                    "/services/entity-structuring/": "Optimize your business structure for maximum tax efficiency and asset protection.",
                    "/services/bookkeeping/": "Accurate financial records that power smarter tax decisions and audit-ready documentation.",
                }
                desc = desc_map.get(related_path, "Expert tax advisory services for business owners and real estate investors.")
                crosslink_html += f'                <a href="{related_path}" style="display: block; padding: 20px; background: var(--white, #fff); border-radius: 8px; border: 1px solid rgba(0,0,0,0.06); text-decoration: none; transition: transform 0.2s, box-shadow 0.2s;" onmouseover="this.style.transform=\'translateY(-2px)\';this.style.boxShadow=\'0 4px 12px rgba(0,0,0,0.1)\'" onmouseout="this.style.transform=\'none\';this.style.boxShadow=\'none\'">\n'
                crosslink_html += f'                    <h3 style="color: var(--dark, #1B2A4A); margin-bottom: 8px; font-size: 16px;">{related_info["title"]}</h3>\n'
                crosslink_html += f'                    <p style="color: var(--medium, #5A6B80); font-size: 14px; margin: 0;">{desc}</p>\n'
                crosslink_html += '                </a>\n'
                stats["service_crosslinks_added"] += 1
        
        crosslink_html += '            </div>\n'
        # Add pillar page link
        pillar_key = svc_info["pillar"]
        if pillar_key in PILLAR_PAGES:
            pillar = PILLAR_PAGES[pillar_key]
            crosslink_html += f'            <p style="margin-top: 24px; text-align: center;"><a href="{pillar["path"]}" style="color: var(--accent, #C9A44A); font-weight: 500;">Learn more about our {pillar["title"].lower()} approach &rarr;</a></p>\n'
            stats["service_crosslinks_added"] += 1
        # Location links
        crosslink_html += '            <p style="margin-top: 12px; text-align: center;"><strong>Available in:</strong> '
        loc_links = []
        for loc_path, loc_name in LOCATION_PAGES.items():
            loc_links.append(f'<a href="{loc_path}" style="color: var(--accent, #C9A44A);">{loc_name}</a>')
            stats["service_crosslinks_added"] += 1
        crosslink_html += " | ".join(loc_links)
        crosslink_html += '</p>\n'
        crosslink_html += '        </div>\n'
        crosslink_html += '    </section>\n'
        
        # Insert before CTA section
        if '<section class="cta-section' in content:
            content = content.replace(
                '<section class="cta-section',
                crosslink_html + '\n    <section class="cta-section'
            )
        else:
            content = content.replace("</main>", crosslink_html + "\n    </main>")
        
        write_file(filepath, content)
        print(f"  Added cross-links to {svc_path}")


# ============================================================
# 3. LOCATION PAGE LINKING
# ============================================================

def add_location_crosslinks(pages):
    """Add service links to location pages and vice versa."""
    print("\n=== Adding Location Page Cross-Links ===")
    
    for loc_path, loc_name in LOCATION_PAGES.items():
        if loc_path not in pages:
            print(f"  WARNING: Location page not found: {loc_path}")
            continue
        
        filepath = pages[loc_path]
        content = read_file(filepath)
        
        # Add comprehensive service links section
        services_html = '\n    <section class="content-section fade-in-section">\n'
        services_html += '        <div class="container narrow">\n'
        services_html += f'            <h2>All Tax Advisory Services in {loc_name}</h2>\n'
        services_html += '            <p>Our full suite of tax advisory services is available to business owners and real estate investors in the greater ' + loc_name + ' area:</p>\n'
        services_html += '            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 20px;">\n'
        
        all_services = [
            ("/services/cost-segregation/", "Cost Segregation Studies", "Accelerate depreciation and reduce year-one tax liability on investment properties."),
            ("/services/tax-planning/", "Strategic Tax Planning", "Year-round proactive tax strategy with IRC-cited analysis."),
            ("/services/entity-structuring/", "Entity Structuring", "Optimize your business entity for maximum tax efficiency."),
            ("/services/bookkeeping/", "Bookkeeping", "Accurate financial records powering smarter tax decisions."),
            ("/cost-segregation-studies-for-real-estate-investors/", "Cost Seg for Real Estate Investors", "Dedicated cost segregation for residential and commercial properties."),
            ("/advanced-tax-planning-services/", "Advanced Tax Planning", "Complex multi-entity and multi-strategy tax optimization."),
            ("/business-owner-tax-planning/", "Business Owner Tax Planning", "Entity structuring and tax planning for owners earning $300K-$3M+."),
        ]
        
        for svc_url, svc_title, svc_desc in all_services:
            if f'href="{svc_url}"' not in content:
                services_html += f'                <a href="{svc_url}" style="display: block; padding: 16px; background: var(--white, #fff); border-radius: 8px; border: 1px solid rgba(0,0,0,0.06); text-decoration: none;">\n'
                services_html += f'                    <h3 style="color: var(--dark, #1B2A4A); font-size: 15px; margin-bottom: 6px;">{svc_title}</h3>\n'
                services_html += f'                    <p style="color: var(--medium, #5A6B80); font-size: 13px; margin: 0;">{svc_desc}</p>\n'
                services_html += '                </a>\n'
                stats["location_links_added"] += 1
        
        services_html += '            </div>\n'
        services_html += '        </div>\n'
        services_html += '    </section>\n'
        
        # Insert before CTA section
        if '<section class="cta-section' in content:
            content = content.replace(
                '<section class="cta-section',
                services_html + '\n    <section class="cta-section'
            )
        write_file(filepath, content)
        print(f"  Added service links to {loc_path}")


# ============================================================
# 4. BLOG INDEX OPTIMIZATION
# ============================================================

def optimize_blog_index(pages):
    """Add category filters and pagination to blog index."""
    print("\n=== Optimizing Blog Index ===")
    
    blog_index_path = pages.get("/blog/")
    if not blog_index_path:
        print("  WARNING: Blog index not found")
        return
    
    content = read_file(blog_index_path)
    
    # Check if filter bar already exists
    if 'blog-filter-bar' in content and 'data-category=' in content:
        print("  Blog filter bar already exists, enhancing...")
    
    # Add category data attributes to blog cards
    # First, let's identify the blog cards and add category attributes
    all_blog_urls = []
    for url, filepath in pages.items():
        if (is_blog_post(url) or (url.startswith("/blog/") and url != "/blog/")):
            page_content = read_file(filepath)
            categories = classify_page(url, page_content)
            all_blog_urls.append((url, get_h1(page_content), categories))
    
    # Check if filter JS exists
    if 'filterBlog' not in content:
        # Add filter bar before the grid
        filter_html = '''
            <div class="blog-filter-bar" id="blogFilters">
                <button class="blog-filter active" onclick="filterBlog('all')">All</button>
                <button class="blog-filter" onclick="filterBlog('Cost Segregation')">Cost Segregation</button>
                <button class="blog-filter" onclick="filterBlog('Entity Structuring')">Entity Structuring</button>
                <button class="blog-filter" onclick="filterBlog('Tax Planning')">Tax Planning</button>
                <button class="blog-filter" onclick="filterBlog('Real Estate')">Real Estate</button>
                <button class="blog-filter" onclick="filterBlog('Business Owners')">Business Owners</button>
                <button class="blog-filter" onclick="filterBlog('IRS Compliance')">IRS Compliance</button>
            </div>
'''
        # Insert before blog-index-grid
        content = content.replace(
            '<div class="blog-index-grid"',
            filter_html + '            <div class="blog-index-grid" id="blogGrid"'
        )
        stats["blog_index_categories_added"] = 7
    
    # Add data-category to each blog card
    for url, h1, categories in all_blog_urls:
        cat_attr = " ".join(categories)
        href_pattern = f'href="{url}"'
        if href_pattern in content and 'data-categories' not in content.split(href_pattern)[0].split('blog-index-card')[-1]:
            content = content.replace(
                f'href="{url}" class="blog-index-card"',
                f'href="{url}" class="blog-index-card" data-categories="{cat_attr}"'
            )
            content = content.replace(
                f'class="blog-index-card">\n                    <div class="blog-card-category blog-badge"',
                f'class="blog-index-card" data-categories="{cat_attr}">\n                    <div class="blog-card-category blog-badge"'
            ) if f'data-categories' not in content.split(f'href="{url}"')[0][-200:] else None
    
    # Add load-more / pagination and filter JS
    if 'blogLoadMore' not in content:
        pagination_js = '''
    <script>
    (function() {
        var POSTS_PER_PAGE = 30;
        var currentPage = 1;
        var currentFilter = 'all';
        
        function filterBlog(category) {
            currentFilter = category;
            currentPage = 1;
            var cards = document.querySelectorAll('.blog-index-card');
            var shown = 0;
            cards.forEach(function(card) {
                var cats = (card.getAttribute('data-categories') || '').toLowerCase();
                var match = category === 'all' || cats.indexOf(category.toLowerCase()) !== -1;
                if (match && shown < POSTS_PER_PAGE) {
                    card.style.display = '';
                    shown++;
                } else if (match) {
                    card.style.display = 'none';
                } else {
                    card.style.display = 'none';
                }
            });
            // Update active filter button
            document.querySelectorAll('.blog-filter').forEach(function(btn) {
                btn.classList.remove('active');
                if (btn.textContent.trim() === category || (category === 'all' && btn.textContent.trim() === 'All')) {
                    btn.classList.add('active');
                }
            });
            // Show/hide load more
            var total = document.querySelectorAll('.blog-index-card[data-categories' + (category === 'all' ? '' : '*="' + category + '"') + ']').length;
            var loadMoreBtn = document.getElementById('blogLoadMore');
            if (loadMoreBtn) {
                loadMoreBtn.style.display = shown < countMatching(category) ? '' : 'none';
            }
        }
        
        function countMatching(category) {
            var cards = document.querySelectorAll('.blog-index-card');
            var count = 0;
            cards.forEach(function(card) {
                var cats = (card.getAttribute('data-categories') || '').toLowerCase();
                if (category === 'all' || cats.indexOf(category.toLowerCase()) !== -1) count++;
            });
            return count;
        }
        
        function loadMore() {
            currentPage++;
            var cards = document.querySelectorAll('.blog-index-card');
            var matching = 0;
            var shown = 0;
            cards.forEach(function(card) {
                var cats = (card.getAttribute('data-categories') || '').toLowerCase();
                var match = currentFilter === 'all' || cats.indexOf(currentFilter.toLowerCase()) !== -1;
                if (match) {
                    matching++;
                    if (matching <= currentPage * POSTS_PER_PAGE) {
                        card.style.display = '';
                        shown++;
                    }
                }
            });
            var loadMoreBtn = document.getElementById('blogLoadMore');
            if (loadMoreBtn && shown >= countMatching(currentFilter)) {
                loadMoreBtn.style.display = 'none';
            }
        }
        
        // Initial page load: show first batch
        window.addEventListener('DOMContentLoaded', function() {
            filterBlog('all');
        });
        
        // Expose functions globally
        window.filterBlog = filterBlog;
        window.loadMore = loadMore;
    })();
    </script>
'''
        # Add load more button
        load_more_html = '''
            <div class="blog-load-more">
                <button id="blogLoadMore" class="btn-cta" onclick="loadMore()" style="background: var(--accent, #C9A44A); color: var(--primary, #1B2A4A); border: none; padding: 14px 32px; border-radius: 8px; font-weight: 600; cursor: pointer;">Load More Articles</button>
            </div>
'''
        # Insert load more after grid closes
        content = content.replace('</div>\n            </div>\n        </section>', 
                                   '</div>\n' + load_more_html + '            </div>\n        </section>')
        
        # Insert JS before closing body
        content = content.replace('</body>', pagination_js + '\n</body>')
    
    write_file(blog_index_path, content)
    print(f"  Blog index optimized with filters and pagination")


# ============================================================
# 5. ON-PAGE SEO FIXES
# ============================================================

def fix_onpage_seo(pages):
    """Fix SEO issues: titles, meta descriptions, alt text, breadcrumbs, broken links."""
    print("\n=== Fixing On-Page SEO Issues ===")
    
    titles_seen = {}
    all_valid_urls = set(pages.keys())
    broken_links = []
    
    for url, filepath in pages.items():
        content = read_file(filepath)
        original = content
        
        # --- Fix duplicate/missing titles ---
        title = get_title(content)
        if not title:
            h1 = get_h1(content)
            if h1:
                new_title = f"{h1} | AE Tax Advisors"
                content = content.replace("<title></title>", f"<title>{new_title}</title>")
                stats["duplicate_titles_fixed"] += 1
        elif title in titles_seen and url != titles_seen[title]:
            # Duplicate title - make unique by prepending H1
            h1 = get_h1(content)
            if h1 and h1 not in title:
                new_title = f"{h1} | AE Tax Advisors"
                content = content.replace(f"<title>{title}</title>", f"<title>{new_title}</title>")
                stats["duplicate_titles_fixed"] += 1
        else:
            titles_seen[title] = url
        
        # --- Fix missing/generic meta descriptions ---
        meta_desc = get_meta_desc(content)
        if not meta_desc or len(meta_desc) < 50:
            h1 = get_h1(content)
            if h1:
                new_desc = f"{h1} - Expert tax advisory from AE Tax Advisors. Serving business owners and real estate investors nationwide."
                if meta_desc:
                    content = content.replace(f'content="{meta_desc}"', f'content="{new_desc}"')
                else:
                    content = content.replace('</title>', f'</title>\n    <meta name="description" content="{new_desc}">')
                stats["seo_fixes"] += 1
        
        # --- Fix missing alt text on images ---
        img_pattern = re.compile(r'<img\s+([^>]*)>', re.IGNORECASE)
        for match in img_pattern.finditer(content):
            attrs = match.group(1)
            if 'alt=' not in attrs:
                # Add descriptive alt text
                src_match = re.search(r'src="([^"]*)"', attrs)
                src = src_match.group(1) if src_match else ""
                alt_text = "AE Tax Advisors"
                if "logo" in src.lower():
                    alt_text = "AE Tax Advisors"
                elif "team" in src.lower():
                    alt_text = "AE Tax Advisors team"
                content = content.replace(match.group(0), match.group(0).replace("<img ", '<img alt="' + alt_text + '" '))
                stats["alt_text_added"] += 1
        
        # --- Add breadcrumbs to blog posts that lack them ---
        if (is_blog_post(url) or (url.startswith("/blog/") and url != "/blog/")) and 'breadcrumbs' not in content:
            h1 = get_h1(content)
            if h1:
                breadcrumb_html = f'<div class="breadcrumbs"><a href="/">Home</a> &raquo; <a href="/blog/">Blog</a> &raquo; {h1}</div>\n            '
                # Insert after <h1> or before it
                h1_match = re.search(r'<h1[^>]*>', content)
                if h1_match:
                    content = content[:h1_match.start()] + breadcrumb_html + content[h1_match.start():]
                    stats["breadcrumbs_added"] += 1
                    
                    # Also add BreadcrumbList schema if not present
                    if '"BreadcrumbList"' not in content:
                        breadcrumb_schema = f'''    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE_URL}/"}},
    {{"@type": "ListItem", "position": 2, "name": "Blog", "item": "{BASE_URL}/blog/"}},
    {{"@type": "ListItem", "position": 3, "name": "{h1}"}}
  ]
}}
    </script>
'''
                        content = content.replace('</head>', breadcrumb_schema + '</head>')
        
        # --- Fix canonical URLs pointing to blog-staging ---
        if 'blog-staging' in content:
            content = content.replace('/blog-staging/', '/blog/')
            stats["seo_fixes"] += 1
        
        # --- Check for broken internal links ---
        internal_links = re.findall(r'href="(/[^"#]*)"', content)
        for link in internal_links:
            normalized = link.rstrip("/") + "/" if not link.endswith("/") and "." not in link.split("/")[-1] else link
            if normalized not in all_valid_urls and link not in ["/assets/style.css", "/assets/favicon.svg", "/assets/ae-tax-logo.png"] and not link.startswith("/assets/"):
                # Check if it's a page that exists without trailing slash
                if link.rstrip("/") + "/" in all_valid_urls:
                    content = content.replace(f'href="{link}"', f'href="{link.rstrip("/") + "/"}"')
                    stats["broken_links_fixed"] += 1
        
        if content != original:
            write_file(filepath, content)
    
    print(f"  Fixed {stats['duplicate_titles_fixed']} duplicate/missing titles")
    print(f"  Added {stats['alt_text_added']} alt text attributes")
    print(f"  Added {stats['breadcrumbs_added']} breadcrumb navigations")
    print(f"  Fixed {stats['broken_links_fixed']} broken/incorrect links")
    print(f"  Fixed {stats['seo_fixes']} other SEO issues")


# ============================================================
# 6. SITEMAP VERIFICATION
# ============================================================

def verify_sitemap(pages):
    """Verify sitemap.xml includes all pages and remove 404s."""
    print("\n=== Verifying Sitemap ===")
    
    sitemap_path = os.path.join(SITE_ROOT, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        print("  WARNING: sitemap.xml not found, creating...")
    
    content = read_file(sitemap_path) if os.path.exists(sitemap_path) else ""
    
    # Parse existing sitemap URLs
    existing_urls = set(re.findall(r'<loc>(.*?)</loc>', content))
    existing_paths = set()
    for url in existing_urls:
        path = url.replace(BASE_URL, "")
        if not path.endswith("/") and "." not in path.split("/")[-1]:
            path += "/"
        existing_paths.add(path)
    
    # Find missing pages
    missing = []
    for url_path in pages.keys():
        full_url = BASE_URL + url_path
        if url_path not in existing_paths and full_url not in existing_urls:
            # Skip utility pages
            skip = ["/404", "/nick-zoom/", "/ashley-45min/", "/mark-zoom/", 
                    "/30-minute-consultation/", "/45-minute-consultation/",
                    "/30-day-followup/", "/30-day-recap/"]
            if url_path not in skip:
                missing.append(url_path)
    
    # Find 404 entries (pages in sitemap but not on disk)
    removed = []
    for full_url in existing_urls:
        path = full_url.replace(BASE_URL, "")
        if not path.endswith("/") and "." not in path.split("/")[-1]:
            path += "/"
        if path not in pages and path != "/":
            # Check without trailing slash
            if path.rstrip("/") + "/" not in pages:
                removed.append(full_url)
    
    # Add missing pages to sitemap
    new_entries = ""
    for path in sorted(missing):
        new_entries += f"""  <url>
    <loc>{BASE_URL}{path}</loc>
    <lastmod>2026-06-09</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
"""
        stats["sitemap_entries_added"] += 1
    
    if new_entries:
        content = content.replace("</urlset>", new_entries + "</urlset>")
    
    # Remove 404 entries
    for url in removed:
        pattern = re.compile(r'\s*<url>\s*<loc>' + re.escape(url) + r'</loc>.*?</url>', re.DOTALL)
        content = pattern.sub("", content)
        stats["sitemap_entries_removed"] += 1
    
    write_file(sitemap_path, content)
    print(f"  Added {stats['sitemap_entries_added']} missing pages to sitemap")
    print(f"  Removed {stats['sitemap_entries_removed']} 404/dead entries from sitemap")


# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    print("=" * 60)
    print("AE Tax Advisors - SEO Optimization")
    print("=" * 60)
    
    pages = get_all_pages()
    print(f"\nTotal pages found: {len(pages)}")
    
    # 1. Pillar-cluster linking
    blog_posts = add_pillar_related_articles(pages)
    add_contextual_links_to_blog_posts(pages, blog_posts)
    
    # 2. Service page cross-linking
    add_service_crosslinks(pages)
    
    # 3. Location page linking
    add_location_crosslinks(pages)
    
    # 4. Blog index optimization
    optimize_blog_index(pages)
    
    # 5. On-page SEO fixes
    fix_onpage_seo(pages)
    
    # 6. Sitemap verification
    verify_sitemap(pages)
    
    # Print summary
    print("\n" + "=" * 60)
    print("OPTIMIZATION COMPLETE - SUMMARY")
    print("=" * 60)
    total_links = (stats["pillar_links_added"] + stats["blog_contextual_links_added"] + 
                   stats["service_crosslinks_added"] + stats["location_links_added"])
    print(f"\nTotal internal links added: {total_links}")
    print(f"  - Pillar page related articles: {stats['pillar_links_added']}")
    print(f"  - Blog contextual links: {stats['blog_contextual_links_added']}")
    print(f"  - Service cross-links: {stats['service_crosslinks_added']}")
    print(f"  - Location service links: {stats['location_links_added']}")
    print(f"\nSEO fixes:")
    print(f"  - Breadcrumbs added: {stats['breadcrumbs_added']}")
    print(f"  - Duplicate titles fixed: {stats['duplicate_titles_fixed']}")
    print(f"  - Alt text added: {stats['alt_text_added']}")
    print(f"  - Broken links fixed: {stats['broken_links_fixed']}")
    print(f"  - Canonical/meta fixes: {stats['seo_fixes']}")
    print(f"  - Blog categories added: {stats['blog_index_categories_added']}")
    print(f"\nSitemap:")
    print(f"  - Pages added to sitemap: {stats['sitemap_entries_added']}")
    print(f"  - Dead entries removed: {stats['sitemap_entries_removed']}")
    print(f"\nTotal pages processed: {len(pages)}")

if __name__ == "__main__":
    main()
