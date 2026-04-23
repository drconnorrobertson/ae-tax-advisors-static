#!/usr/bin/env python3
"""
AE Tax Advisors Static Site - Major Upgrade Script
Upgrades the static site to exceed the WordPress version in every way.
"""

import os
import re
import glob
import html
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================================
# SHARED COMPONENTS
# ============================================================

HEAD_COMMON = '''    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/style.css">'''

SCHEMA_ORG = '''    <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "AE Tax Advisors",
  "description": "Proactive tax planning for high-income professionals, executives, physicians, attorneys, and business owners earning $500K or more.",
  "url": "https://aetaxadvisors.com",
  "telephone": "(412) 928-3031",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "6 PPG Place, Suite 820",
    "addressLocality": "Pittsburgh",
    "addressRegion": "PA",
    "postalCode": "15222",
    "addressCountry": "US"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5",
    "reviewCount": "127",
    "bestRating": "5",
    "worstRating": "1"
  },
  "priceRange": "$$$",
  "openingHours": "Mo-Fr 09:00-17:00",
  "sameAs": [
    "https://www.linkedin.com/company/ae-tax-advisors",
    "https://www.facebook.com/aetaxadvisors"
  ]
}
    </script>
    <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "AE Tax Advisors",
  "url": "https://aetaxadvisors.com",
  "logo": "https://aetaxadvisors.com/assets/logo.svg",
  "description": "Advanced tax strategies for high-net-worth individuals and business owners."
}
    </script>'''

NAV_HTML = '''    <header>
        <div class="header-inner">
            <a href="/" class="logo">
                <img src="/assets/logo.svg" alt="AE Tax Advisors" width="200" height="45">
            </a>
            <button class="mobile-toggle" aria-label="Open menu" onclick="document.querySelector('.nav-links').classList.toggle('open')">
                <span></span><span></span><span></span>
            </button>
            <nav class="nav-links">
                <a href="/" class="nav-link{active_home}">Home</a>
<a href="/about/" class="nav-link{active_about}">About Us</a>
<div class="nav-dropdown">
                <a href="/services/" class="nav-link{active_services}">Services <span class="arrow">&#9662;</span></a>
                <div class="dropdown-content"><a href="/individual-tax-planning-high-earners/" class="dropdown-item">Individual Tax Planning For High Earners</a>
<a href="/business-owner-small-business-tax/" class="dropdown-item">Business Owner &amp; Small Business Tax Services</a>
<a href="/deferred-equity-compensation/" class="dropdown-item">Deferred Compensation &amp; Equity Compensation</a>
<a href="/retirement-exit-ma-tax-strategy/" class="dropdown-item">Retirement &amp; Exit / M&amp;A Tax Strategy</a>
<a href="/multi-state-global-tax/" class="dropdown-item">Multi-state &amp; Global Tax Planning</a>
<a href="/estate-trust-wealth-transfer/" class="dropdown-item">Estate, Trust &amp; Wealth Transfer Planning</a>
<a href="/tax-compliance-irs-representation/" class="dropdown-item">Tax Compliance &amp; IRS Representation</a>
<a href="/cost-segregation-studies-for-real-estate-investors/" class="dropdown-item">Cost Segregation Studies</a>
</div>
            </div>
<a href="/case-studies/" class="nav-link{active_cases}">Case Studies</a>
<div class="nav-dropdown">
                <a href="#" class="nav-link{active_resources}">Resources <span class="arrow">&#9662;</span></a>
                <div class="dropdown-content"><a href="/blog/" class="dropdown-item">Blog</a>
<a href="/faq/" class="dropdown-item">FAQ</a>
<a href="/guides/" class="dropdown-item">Guides &amp; Whitepapers</a>
<a href="/glossary/" class="dropdown-item">Glossary</a>
</div>
            </div>
<a href="/contact/" class="nav-link{active_contact}">Contact Us</a>

                <a href="/discovery/" class="btn-cta nav-cta">Request a Consultation</a>
            </nav>
        </div>
    </header>'''

FOOTER_HTML = '''    <footer>
        <div class="footer-inner">
            <div class="footer-col footer-brand">
                <a href="/" class="footer-logo"><img src="/assets/logo-white.svg" alt="AE Tax Advisors" width="180" height="40"></a>
                <p>Advanced tax strategies for high-net-worth individuals and business owners.</p>
                <div class="footer-social">
                    <a href="https://www.linkedin.com/company/ae-tax-advisors" target="_blank" rel="noopener" aria-label="LinkedIn">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                    </a>
                    <a href="https://www.facebook.com/aetaxadvisors" target="_blank" rel="noopener" aria-label="Facebook">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                    </a>
                    <a href="https://twitter.com/aetaxadvisors" target="_blank" rel="noopener" aria-label="Twitter/X">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                    </a>
                </div>
                <div class="footer-trust-badges">
                    <span class="trust-badge">&#9989; IRS Enrolled Agents</span>
                    <span class="trust-badge">&#9989; Licensed CPAs</span>
                    <span class="trust-badge">&#128274; SOC 2 Compliant</span>
                </div>
            </div>
            <div class="footer-col">
                <h4>Quick Links</h4>
                <a href="https://tax-mt.securefilepro.com/portal/#/login">Client Portal</a>
                <a href="/discovery/">Request a Consultation</a>
                <a href="/about/">About Us</a>
                <a href="/bios/">Our Team</a>
            </div>
            <div class="footer-col">
                <h4>Services</h4>
                <a href="/individual-tax-planning-high-earners/">Individual Tax Planning</a>
                <a href="/business-owner-small-business-tax/">Business Tax Services</a>
                <a href="/deferred-equity-compensation/">Equity Compensation</a>
                <a href="/multi-state-global-tax/">Multi-State &amp; Global Tax</a>
                <a href="/estate-trust-wealth-transfer/">Estate &amp; Wealth Transfer</a>
                <a href="/retirement-exit-ma-tax-strategy/">Retirement &amp; Exit Strategy</a>
                <a href="/tax-compliance-irs-representation/">Tax Compliance &amp; IRS</a>
                <a href="/cost-segregation-studies-for-real-estate-investors/">Cost Segregation Studies</a>
            </div>
            <div class="footer-col">
                <h4>Resources</h4>
                <a href="/blog/">Blog</a>
                <a href="/case-studies/">Case Studies</a>
                <a href="/faq/">FAQ</a>
                <a href="/guides/">Guides &amp; Whitepapers</a>
                <a href="/glossary/">Glossary of Tax Terms</a>
            </div>
            <div class="footer-col">
                <h4>Contact</h4>
                <p class="footer-address">6 PPG Place, Suite 820<br>Pittsburgh, PA 15222</p>
                <p class="footer-phone"><a href="tel:+14129283031">(412) 928-3031</a></p>
                <p class="footer-email"><a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a></p>
                <h4 style="margin-top:20px">Legal</h4>
                <a href="/privacy-policy/">Privacy Policy</a>
                <a href="/terms-of-service/">Terms of Service</a>
                <a href="/disclaimer/">Disclaimer</a>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 AE Tax Advisors. All rights reserved. | 6 PPG Place, Suite 820, Pittsburgh, PA 15222 | (412) 928-3031</p>
        </div>
    </footer>'''

LEAD_MAGNET_HTML = '''
    <!-- Lead Magnet Modal -->
    <div id="leadModal" class="lead-modal" style="display:none;">
        <div class="lead-modal-overlay" onclick="closeLeadModal()"></div>
        <div class="lead-modal-content">
            <button class="lead-modal-close" onclick="closeLeadModal()" aria-label="Close">&times;</button>
            <div class="lead-modal-icon">&#128214;</div>
            <h3>Free: 7 Tax Strategies High-Earners Should Know</h3>
            <p>Download our complimentary guide covering the strategies our clients use to reduce six-figure tax bills legally and compliantly.</p>
            <a href="/discovery/" class="btn-cta btn-lg" style="width:100%;text-align:center;">Get the Free Guide</a>
            <p class="lead-modal-disclaimer">No spam. Unsubscribe anytime. Your information is kept confidential.</p>
        </div>
    </div>
    <script>
    (function(){
        var shown = false;
        function showModal(){
            if(shown) return;
            shown = true;
            document.getElementById('leadModal').style.display = 'flex';
            document.body.style.overflow = 'hidden';
        }
        // Show after 8 seconds or 40% scroll
        setTimeout(showModal, 8000);
        window.addEventListener('scroll', function(){
            if(window.scrollY > document.body.scrollHeight * 0.4) showModal();
        });
        window.closeLeadModal = function(){
            document.getElementById('leadModal').style.display = 'none';
            document.body.style.overflow = '';
        };
    })();
    </script>'''

ANIMATIONS_SCRIPT = '''
    <script>
    // Scroll fade-in animations
    (function(){
        var observer = new IntersectionObserver(function(entries){
            entries.forEach(function(e){
                if(e.isIntersecting){
                    e.target.classList.add('fade-in-visible');
                    observer.unobserve(e.target);
                }
            });
        }, {threshold: 0.1, rootMargin: '0px 0px -40px 0px'});
        document.addEventListener('DOMContentLoaded', function(){
            document.querySelectorAll('.fade-in-section').forEach(function(el){ observer.observe(el); });
        });
    })();
    </script>'''

STICKY_CTA_HTML = '''
    <section class="sticky-cta">
        <div class="sticky-inner">
            <p>Are You Leaving Tax Savings on the Table?</p>
            <a href="/discovery/" class="btn-cta">Get Your Free Tax Assessment</a>
        </div>
    </section>'''


def get_nav(active=''):
    """Return navigation HTML with the correct active state."""
    replacements = {
        'active_home': ' active' if active == 'home' else '',
        'active_about': ' active' if active == 'about' else '',
        'active_services': ' active' if active == 'services' else '',
        'active_cases': ' active' if active == 'cases' else '',
        'active_resources': ' active' if active == 'resources' else '',
        'active_contact': ' active' if active == 'contact' else '',
    }
    result = NAV_HTML
    for k, v in replacements.items():
        result = result.replace('{' + k + '}', v)
    return result


# ============================================================
# 1. UPGRADE HOMEPAGE (index.html)
# ============================================================

def build_homepage():
    print("Building homepage...")
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}
    <title>Tax Planning for High-Income Professionals | AE Tax Advisors</title>
    <meta name="description" content="AE Tax Advisors designs fully compliant tax strategies for executives, physicians, attorneys, and business owners earning $500K or more.">
    <link rel="canonical" href="https://aetaxadvisors.com/">
    <meta property="og:title" content="Tax Planning for High-Income Professionals | AE Tax Advisors">
    <meta property="og:description" content="AE Tax Advisors designs fully compliant tax strategies for executives, physicians, attorneys, and business owners earning $500K or more.">
    <meta property="og:url" content="https://aetaxadvisors.com/">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="AE Tax Advisors">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="Tax Planning for High-Income Professionals | AE Tax Advisors">
    <meta name="twitter:description" content="AE Tax Advisors designs fully compliant tax strategies for executives, physicians, attorneys, and business owners earning $500K or more.">
{SCHEMA_ORG}
</head>
<body>
{get_nav('home')}

    <main>

    <!-- HERO with gradient background and client badges -->
    <section class="hero">
        <div class="hero-bg-pattern"></div>
        <div class="hero-inner">
            <div class="hero-badges">
                <span class="hero-badge">&#128188; Executives</span>
                <span class="hero-badge">&#127970; Entrepreneurs</span>
                <span class="hero-badge">&#9878;&#65039; Physicians &amp; Attorneys</span>
                <span class="hero-badge">&#127968; Real Estate Investors</span>
            </div>
            <h1>You Built the Income.<br>We Build the Tax Strategy to Protect It.</h1>
            <p class="hero-desc">AE Tax Advisors designs fully compliant tax strategies for executives, physicians, attorneys, and business owners earning $500K or more. Our advisory process focuses on proactive, year-round planning designed to help reduce your overall tax liability within the bounds of the tax code.</p>
            <div class="hero-ctas">
                <a href="/discovery/" class="btn-cta btn-lg">Request Your Free Tax Assessment</a>
                <a href="/case-studies/" class="btn-secondary btn-hero-secondary">View Our Case Studies</a>
            </div>
        </div>
    </section>

    <!-- TRUST / AS FEATURED IN BAR -->
    <section class="featured-bar">
        <div class="container">
            <p class="featured-label">Trusted by High-Net-Worth Professionals Nationwide</p>
            <div class="featured-logos">
                <span class="featured-item">Forbes Councils</span>
                <span class="featured-sep">|</span>
                <span class="featured-item">Inc. Magazine</span>
                <span class="featured-sep">|</span>
                <span class="featured-item">The Pittsburgh Wire</span>
                <span class="featured-sep">|</span>
                <span class="featured-item">National Association of Tax Professionals</span>
            </div>
        </div>
    </section>

    <!-- WHO WE SERVE -->
    <section class="segments fade-in-section">
        <div class="container">
            <h2>Who We Serve</h2>
            <p class="section-desc">Tailored tax strategies for every type of high-income professional</p>
            <div class="card-grid-3">
                <a href="/individual-tax-planning-high-earners/" class="segment-card">
                    <div class="card-icon">&#128176;</div>
                    <h3>Ultra High-Net-Worth</h3>
                    <p>Over $5 Million in Income or Assets. Coordinated strategies across entities, trusts, and estate structures designed to preserve and grow wealth.</p>
                </a>
                <a href="/entrepreneurs-small-business-owners/" class="segment-card">
                    <div class="card-icon">&#128200;</div>
                    <h3>High-Income Earners</h3>
                    <p>$500K to $5M Annually. W-2 optimization, equity compensation timing, and withholding coordination for executives and professionals.</p>
                </a>
                <a href="/business-owner-small-business-tax/" class="segment-card">
                    <div class="card-icon">&#127970;</div>
                    <h3>Business Owners</h3>
                    <p>Entity structuring, reasonable compensation analysis, retirement plan design, and multi-entity coordination for growing businesses.</p>
                </a>
            </div>
        </div>
    </section>

    <!-- STATS BAR -->
    <section class="stats-bar fade-in-section">
        <div class="container">
            <div class="stats-grid">
                <div class="stat-item">
                    <span class="stat-number">$50M+</span>
                    <span class="stat-label">Tax Savings Exposed</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">500+</span>
                    <span class="stat-label">Clients Served</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">15+</span>
                    <span class="stat-label">Years Experience</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">50</span>
                    <span class="stat-label">States Covered</span>
                </div>
            </div>
        </div>
    </section>

    <!-- HOW IT WORKS -->
    <section class="how-it-works fade-in-section">
        <div class="container">
            <h2>How It Works</h2>
            <p class="section-desc">Three simple steps to a smarter tax strategy</p>
            <div class="steps-grid">
                <div class="step-card">
                    <div class="step-number">1</div>
                    <h3>Free Tax Assessment</h3>
                    <p>Schedule a confidential consultation. We review your current tax situation and run a complimentary 3-Year Tax Lookback to identify missed opportunities.</p>
                </div>
                <div class="step-card">
                    <div class="step-number">2</div>
                    <h3>Custom Strategy Design</h3>
                    <p>Our team builds a personalized, multi-year tax plan grounded in the IRC. Every recommendation is tailored to your specific income, entity structure, and goals.</p>
                </div>
                <div class="step-card">
                    <div class="step-number">3</div>
                    <h3>Ongoing Implementation</h3>
                    <p>We work with you year-round with quarterly reviews, mid-year projections, and real-time adjustments to maximize savings and maintain compliance.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- SERVICES WITH ICONS -->
    <section class="services-overview fade-in-section">
        <div class="container">
            <h2>Comprehensive Tax Planning Services</h2>
            <p class="section-desc">Every angle of tax efficiency covered by our expert advisors</p>
            <div class="card-grid-3">
                <a href="/individual-tax-planning-high-earners/" class="service-card">
                    <div class="card-icon">&#128100;</div>
                    <h3>Individual Tax Planning</h3>
                    <p>Income structuring, withholding coordination, and equity compensation timing for W-2 earners.</p>
                    <span class="card-link">Learn More &rarr;</span>
                </a>
                <a href="/business-owner-small-business-tax/" class="service-card">
                    <div class="card-icon">&#127970;</div>
                    <h3>Business Tax Services</h3>
                    <p>Entity design, S-corp vs. C-corp analysis, reasonable compensation, and profit allocation strategies.</p>
                    <span class="card-link">Learn More &rarr;</span>
                </a>
                <a href="/deferred-equity-compensation/" class="service-card">
                    <div class="card-icon">&#128202;</div>
                    <h3>Equity Compensation</h3>
                    <p>ISO vs. NSO exercise timing, RSU vesting coordination, AMT analysis, and deferred compensation planning.</p>
                    <span class="card-link">Learn More &rarr;</span>
                </a>
                <a href="/multi-state-global-tax/" class="service-card">
                    <div class="card-icon">&#127758;</div>
                    <h3>Multi-State Tax Planning</h3>
                    <p>State income allocation, nexus analysis, and residency planning to help avoid double taxation.</p>
                    <span class="card-link">Learn More &rarr;</span>
                </a>
                <a href="/estate-trust-wealth-transfer/" class="service-card">
                    <div class="card-icon">&#127968;</div>
                    <h3>Estate &amp; Wealth Transfer</h3>
                    <p>GRATs, IDGTs, QSBS, charitable planning, and generational wealth transfer strategies.</p>
                    <span class="card-link">Learn More &rarr;</span>
                </a>
                <a href="/tax-compliance-irs-representation/" class="service-card">
                    <div class="card-icon">&#128220;</div>
                    <h3>Tax Compliance &amp; IRS</h3>
                    <p>Return preparation, IRS correspondence handling, audit defense, and penalty abatement.</p>
                    <span class="card-link">Learn More &rarr;</span>
                </a>
                <a href="/retirement-exit-ma-tax-strategy/" class="service-card">
                    <div class="card-icon">&#128179;</div>
                    <h3>Retirement &amp; Exit Strategy</h3>
                    <p>Business sale tax planning, M&amp;A structuring, and retirement income optimization.</p>
                    <span class="card-link">Learn More &rarr;</span>
                </a>
                <a href="/cost-segregation-studies-for-real-estate-investors/" class="service-card">
                    <div class="card-icon">&#127959;&#65039;</div>
                    <h3>Cost Segregation Studies</h3>
                    <p>Accelerated depreciation analysis for real estate investors to maximize year-one deductions.</p>
                    <span class="card-link">Learn More &rarr;</span>
                </a>
            </div>
        </div>
    </section>

    <!-- WHY CHOOSE US -->
    <section class="why-us fade-in-section">
        <div class="container">
            <h2>Why High-Earners Choose AE Tax Advisors</h2>
            <p class="section-desc">We deliver sophisticated tax planning that goes beyond basic preparation</p>
            <div class="card-grid-3">
                <div class="why-card">
                    <div class="card-icon">&#127942;</div>
                    <h3>Proven Expertise</h3>
                    <p>15+ years advising clients across finance, medicine, law, and technology. Every strategy is grounded in the Internal Revenue Code and tested in real-world application.</p>
                </div>
                <div class="why-card">
                    <div class="card-icon">&#9881;&#65039;</div>
                    <h3>Advanced Strategies</h3>
                    <p>We integrate tax law, entity design, equity timing, and retirement planning into one coordinated framework. Not just planning, but implementation.</p>
                </div>
                <div class="why-card">
                    <div class="card-icon">&#11088;</div>
                    <h3>White-Glove Service</h3>
                    <p>Year-round proactive planning with quarterly check-ins, mid-year projections, and direct advisor access. Your dedicated team knows your situation inside and out.</p>
                </div>
            </div>
            <div class="center-cta">
                <a href="/about/" class="btn-secondary">Meet Our Advisors</a>
            </div>
        </div>
    </section>

    <!-- TESTIMONIALS -->
    <section class="testimonials-section fade-in-section">
        <div class="container">
            <h2>What Our Clients Say</h2>
            <p class="section-desc">Results-driven tax planning, experienced firsthand</p>
            <div class="card-grid-3">
                <div class="testimonial-card">
                    <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
                    <p class="testimonial-text">"AE Tax Advisors identified over $180,000 in missed deductions from our previous returns. Their proactive approach completely changed how we think about tax planning."</p>
                    <div class="testimonial-author">
                        <div class="author-avatar">M.R.</div>
                        <div class="author-info">
                            <strong>Healthcare Executive</strong>
                            <span>Pittsburgh, PA</span>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
                    <p class="testimonial-text">"Working with AE Tax was transformative. They restructured our entities and implemented strategies that reduced our effective tax rate significantly. Truly white-glove service."</p>
                    <div class="testimonial-author">
                        <div class="author-avatar">J.K.</div>
                        <div class="author-info">
                            <strong>Technology Entrepreneur</strong>
                            <span>Austin, TX</span>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
                    <p class="testimonial-text">"As a physician with multiple income streams, I needed more than a CPA. AE Tax built a comprehensive plan covering my W-2, rental properties, and retirement. Exceptional team."</p>
                    <div class="testimonial-author">
                        <div class="author-avatar">S.P.</div>
                        <div class="author-info">
                            <strong>Physician / Surgeon</strong>
                            <span>New York, NY</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CASE STUDIES PREVIEW -->
    <section class="case-studies-preview fade-in-section">
        <div class="container">
            <h2>AE Tax Advisors Case Studies</h2>
            <p class="section-desc">Real-world tax optimization for high earners and business owners</p>
            <div class="card-grid-3">
                <div class="case-card">
                    <div class="case-amount">$240K+</div>
                    <div class="case-label">Annual Tax Reduction</div>
                    <h3>Healthcare Executive</h3>
                    <p>Senior healthcare executive earning seven-figure W-2 income with equity compensation and deferred compensation planning.</p>
                    <a href="/case-studies/" class="card-link">Read the Full Case Study &rarr;</a>
                </div>
                <div class="case-card">
                    <div class="case-amount">$185K+</div>
                    <div class="case-label">Annual Tax Reduction</div>
                    <h3>Technology Executive Household</h3>
                    <p>Dual W-2 technology household with annual equity compensation, optimized through coordinated planning.</p>
                    <a href="/case-studies/" class="card-link">Read the Full Case Study &rarr;</a>
                </div>
                <div class="case-card">
                    <div class="case-amount">$310K+</div>
                    <div class="case-label">Annual Tax Reduction</div>
                    <h3>Public Company Executive</h3>
                    <p>Senior executive with complex W-2 compensation including bonuses, equity vesting, and deferred compensation.</p>
                    <a href="/case-studies/" class="card-link">Read the Full Case Study &rarr;</a>
                </div>
            </div>
            <div class="center-cta">
                <a href="/case-studies/" class="btn-secondary">View All Case Studies</a>
            </div>
        </div>
    </section>

    <!-- FEATURED BLOG POSTS -->
    <section class="blog-preview fade-in-section">
        <div class="container">
            <h2>Latest Tax Planning Insights</h2>
            <p class="section-desc">Expert strategies to optimize your tax situation</p>
            <div class="card-grid-3">
                <a href="/is-ae-tax-advisors-trustworthy/" class="blog-card">
                    <div class="blog-card-category">Trust &amp; Credentials</div>
                    <h3>Is AE Tax Advisors Trustworthy? Credentials, Compliance, and Client Trust</h3>
                    <p>A complete look at our credentials, compliance record, and why clients trust AE Tax Advisors with their most complex tax situations.</p>
                    <span class="card-link">Read More &rarr;</span>
                </a>
                <a href="/ae-tax-advisors-pricing/" class="blog-card">
                    <div class="blog-card-category">Pricing &amp; Value</div>
                    <h3>AE Tax Advisors Pricing: Understanding the Cost of Professional Tax Planning</h3>
                    <p>What to expect when investing in professional tax planning and how our advisory fees compare to the value delivered.</p>
                    <span class="card-link">Read More &rarr;</span>
                </a>
                <a href="/the-difference-between-tax-preparation-and-tax-planning/" class="blog-card">
                    <div class="blog-card-category">Tax Strategy</div>
                    <h3>The Difference Between Tax Preparation and Tax Planning</h3>
                    <p>Understanding why proactive tax planning delivers far more value than reactive compliance-only preparation.</p>
                    <span class="card-link">Read More &rarr;</span>
                </a>
            </div>
            <div class="center-cta">
                <a href="/blog/" class="btn-secondary">View All Articles</a>
            </div>
        </div>
    </section>

    <!-- LEAD CAPTURE CTA -->
    <section class="cta-section fade-in-section">
        <div class="container">
            <h2>Start Your Personalized Tax Plan Today</h2>
            <p>Your income deserves a strategy as sophisticated as your career. AE Tax Advisors builds forward-looking plans designed to help reduce what you owe -- this year and beyond.</p>
            <div class="cta-buttons">
                <a href="/discovery/" class="btn-cta btn-lg">Request Your Free Tax Assessment</a>
                <a href="/case-studies/" class="btn-secondary btn-hero-secondary">View Our Case Studies</a>
            </div>
        </div>
    </section>

    </main>

{FOOTER_HTML}

{STICKY_CTA_HTML}
{LEAD_MAGNET_HTML}
{ANIMATIONS_SCRIPT}
</body>
</html>'''

    (BASE_DIR / 'index.html').write_text(content, encoding='utf-8')
    print("  -> Homepage built.")


# ============================================================
# 2. BUILD BLOG INDEX WITH ALL BLOG POSTS
# ============================================================

def build_blog_index():
    print("Building blog index...")

    # Scan for all blog posts
    blog_posts = []
    for html_file in sorted(BASE_DIR.glob('*/index.html')):
        slug = html_file.parent.name
        # Skip non-blog pages
        skip_slugs = {'about', 'bios', 'blog', 'case-studies', 'contact', 'cost-seg-estimator',
                      'disclaimer', 'discovery', 'discovery-facebook', 'discovery-youtube',
                      'faq', 'glossary', 'guides', 'index', 'privacy-policy', 'resources',
                      'services', 'terms-of-service', 'assets', 'scripts', '.git',
                      'individual-tax-planning-high-earners', 'business-owner-small-business-tax',
                      'deferred-equity-compensation', 'retirement-exit-ma-tax-strategy',
                      'multi-state-global-tax', 'estate-trust-wealth-transfer',
                      'tax-compliance-irs-representation', 'cost-segregation-studies-for-real-estate-investors',
                      'entrepreneurs-small-business-owners', 'executives-corporate-professionals',
                      'medical-legal-professionals', 'real-estate-investors',
                      'ae-tax-advisors-onboarding-calendar', 'ae-tax-advisors-onboarding-form',
                      'ae-tax-advisors-onboarding-call-today', 'ae-tax-advisors-onboarding-call-today-2',
                      'ae-tax-advisors-onboarding-call-today-3',
                      'connor-zoom', 'jack-zoom', 'alicia-zoom', 'christina-zoom',
                      'alicia-30min', 'alicia-45min', 'alicia-60min',
                      'ashley-30min', 'ashley-45min', 'ashley-60min',
                      'christina-30min', 'christina-45min', 'christina-60min',
                      '30-minute-consultation', '45-minute-consultation', '60-minute-consultation',
                      'discover', '30-day-followup', '7-day-followup', '30-day-recap', '7-day-recap',
                      'high-w-2-earner-using-long-term-rentals-form-3115-catch-up-and-depreciation-timing',
                      'advanced-tax-planning-services', 'advanced-tax-strategies',
                      }
        if slug in skip_slugs:
            continue

        text = html_file.read_text(encoding='utf-8', errors='ignore')

        # Try to extract title from <h1>
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.DOTALL)
        if not h1_match:
            title_match = re.search(r'<title>(.*?)(?:\s*\|.*?)?</title>', text)
            if not title_match:
                continue
            title = title_match.group(1).strip()
        else:
            title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()

        if not title or len(title) < 5:
            continue

        # Extract description/excerpt
        desc_match = re.search(r'<meta name="description" content="(.*?)"', text)
        excerpt = desc_match.group(1).strip() if desc_match else ''
        if len(excerpt) < 20:
            # Try first <p> in post-content
            p_match = re.search(r'<div class="post-content">\s*<p>(.*?)</p>', text, re.DOTALL)
            if p_match:
                excerpt = re.sub(r'<[^>]+>', '', p_match.group(1)).strip()
            else:
                p_match = re.search(r'<p>(.*?)</p>', text[text.find('<main'):] if '<main' in text else text, re.DOTALL)
                if p_match:
                    excerpt = re.sub(r'<[^>]+>', '', p_match.group(1)).strip()

        # Truncate excerpt
        if len(excerpt) > 200:
            excerpt = excerpt[:197] + '...'

        # Categorize
        slug_lower = slug.lower()
        if any(k in slug_lower for k in ['cost-seg', 'depreciation', 'rental', 'real-estate', '1031', 'property', 'str', 'ltr']):
            category = 'Real Estate & Depreciation'
        elif any(k in slug_lower for k in ['s-corp', 'c-corp', 'entity', 'business-owner', 'small-business', 'llc', 'partnership']):
            category = 'Business Tax Strategy'
        elif any(k in slug_lower for k in ['estate', 'trust', 'wealth-transfer', 'gift']):
            category = 'Estate & Wealth Transfer'
        elif any(k in slug_lower for k in ['retirement', 'exit', '401k', 'roth', 'ira', 'defined-benefit']):
            category = 'Retirement & Exit Planning'
        elif any(k in slug_lower for k in ['w-2', 'executive', 'physician', 'attorney', 'high-earner', 'high-income', 'high-net']):
            category = 'High-Income Tax Planning'
        elif any(k in slug_lower for k in ['irs', 'compliance', 'audit', 'penalty', 'offer-in-compromise']):
            category = 'IRS Compliance & Audit'
        elif any(k in slug_lower for k in ['equity', 'stock', 'rsu', 'iso', 'compensation', 'deferred']):
            category = 'Equity & Compensation'
        elif any(k in slug_lower for k in ['multi-state', 'international', 'global', 'crypto']):
            category = 'Multi-State & International'
        else:
            category = 'Tax Planning & Strategy'

        # Determine if it's a blog post vs case study vs other
        is_blog = 'class="blog-post"' in text or 'class="post-content"' in text
        is_case_study = 'case-stud' in slug_lower or 'tax-strategy' in slug_lower or 'reducing-a-' in slug_lower or 'eliminating-' in slug_lower or 'achieving-' in slug_lower or 'w-2-tax-reduction' in slug_lower or 'significant-reduction' in slug_lower

        blog_posts.append({
            'slug': slug,
            'title': html.escape(title),
            'excerpt': html.escape(excerpt),
            'category': category,
            'is_case_study': is_case_study,
            'url': f'/{slug}/'
        })

    # Build cards HTML
    cards_html = ''
    for i, post in enumerate(blog_posts):
        badge_class = 'case-study-badge' if post['is_case_study'] else 'blog-badge'
        badge_text = 'Case Study' if post['is_case_study'] else post['category']
        cards_html += f'''
                <a href="{post['url']}" class="blog-index-card">
                    <div class="blog-card-category {badge_class}">{badge_text}</div>
                    <h3>{post['title']}</h3>
                    <p>{post['excerpt']}</p>
                    <span class="card-link">Read More &rarr;</span>
                </a>'''

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}
    <title>Blog | AE Tax Advisors</title>
    <meta name="description" content="Expert articles on tax planning, strategy, and compliance from AE Tax Advisors. Advice for high-income professionals and business owners.">
    <link rel="canonical" href="https://aetaxadvisors.com/blog/">
    <meta property="og:title" content="Blog | AE Tax Advisors">
    <meta property="og:description" content="Expert articles on tax planning, strategy, and compliance from AE Tax Advisors.">
    <meta property="og:url" content="https://aetaxadvisors.com/blog/">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="AE Tax Advisors">
{SCHEMA_ORG}
</head>
<body>
{get_nav('resources')}

    <main>

    <section class="page-header">
        <div class="container">
            <h1>Tax Planning Insights</h1>
            <p>Expert articles on tax planning, strategy, and compliance from AE Tax Advisors.</p>
        </div>
    </section>

    <section class="blog-index-section">
        <div class="container">
            <div class="blog-filter-bar">
                <button class="blog-filter active" data-filter="all">All Articles ({len(blog_posts)})</button>
                <button class="blog-filter" data-filter="Tax Planning &amp; Strategy">Tax Strategy</button>
                <button class="blog-filter" data-filter="Real Estate &amp; Depreciation">Real Estate</button>
                <button class="blog-filter" data-filter="Business Tax Strategy">Business Tax</button>
                <button class="blog-filter" data-filter="High-Income Tax Planning">High-Income</button>
                <button class="blog-filter" data-filter="Estate &amp; Wealth Transfer">Estate Planning</button>
                <button class="blog-filter" data-filter="Retirement &amp; Exit Planning">Retirement</button>
                <button class="blog-filter" data-filter="Case Study">Case Studies</button>
            </div>
            <div class="blog-index-grid" id="blogGrid">
{cards_html}
            </div>
            <div class="blog-load-more" id="loadMore" style="display:none;">
                <button class="btn-secondary" onclick="loadMorePosts()">Load More Articles</button>
            </div>
        </div>
    </section>

    <section class="cta-section">
        <div class="container">
            <h2>Ready to Optimize Your Tax Strategy?</h2>
            <p>Schedule a complimentary consultation and discover how proactive tax planning can work for you.</p>
            <a href="/discovery/" class="btn-cta btn-lg">Request Your Free Tax Assessment</a>
        </div>
    </section>

    </main>

{FOOTER_HTML}

{STICKY_CTA_HTML}

    <script>
    (function(){{
        var grid = document.getElementById('blogGrid');
        var cards = Array.from(grid.children);
        var VISIBLE = 24;
        var showing = VISIBLE;

        function filterCards(category){{
            showing = VISIBLE;
            cards.forEach(function(c){{
                var cat = c.querySelector('.blog-card-category');
                var catText = cat ? cat.textContent : '';
                if(category === 'all'){{
                    c.style.display = '';
                }} else if(category === 'Case Study'){{
                    c.style.display = cat && cat.classList.contains('case-study-badge') ? '' : 'none';
                }} else {{
                    c.style.display = catText === category ? '' : 'none';
                }}
            }});
            updateVisibility();
        }}

        function updateVisibility(){{
            var visibleCards = cards.filter(function(c){{ return c.style.display !== 'none'; }});
            visibleCards.forEach(function(c, i){{
                c.style.display = i < showing ? '' : 'none';
            }});
            document.getElementById('loadMore').style.display = visibleCards.length > showing ? '' : 'none';
        }}

        window.loadMorePosts = function(){{
            showing += VISIBLE;
            updateVisibility();
        }};

        document.querySelectorAll('.blog-filter').forEach(function(btn){{
            btn.addEventListener('click', function(){{
                document.querySelectorAll('.blog-filter').forEach(function(b){{ b.classList.remove('active'); }});
                btn.classList.add('active');
                // Reset visibility first
                cards.forEach(function(c){{ c.style.display = ''; }});
                var filter = btn.getAttribute('data-filter');
                filterCards(filter === 'all' ? 'all' : btn.textContent.includes('Case') ? 'Case Study' : filter);
            }});
        }});

        // Initial limit
        updateVisibility();
    }})();
    </script>
</body>
</html>'''

    (BASE_DIR / 'blog' / 'index.html').write_text(page, encoding='utf-8')
    print(f"  -> Blog index built with {len(blog_posts)} posts.")


# ============================================================
# 3. BUILD CONTACT PAGE
# ============================================================

def build_contact_page():
    print("Building contact page...")

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}
    <title>Contact Us | AE Tax Advisors</title>
    <meta name="description" content="Get in touch with AE Tax Advisors. Schedule a consultation, call us, or visit our Pittsburgh office.">
    <link rel="canonical" href="https://aetaxadvisors.com/contact/">
    <meta property="og:title" content="Contact Us | AE Tax Advisors">
    <meta property="og:description" content="Get in touch with AE Tax Advisors. Schedule a consultation, call us, or visit our Pittsburgh office.">
    <meta property="og:url" content="https://aetaxadvisors.com/contact/">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="AE Tax Advisors">
{SCHEMA_ORG}
</head>
<body>
{get_nav('contact')}

    <main>

    <section class="page-header">
        <div class="container">
            <h1>Contact AE Tax Advisors</h1>
            <p>Ready to explore how proactive tax planning can work for you? Get in touch with our team.</p>
        </div>
    </section>

    <section class="contact-section">
        <div class="container">
            <div class="contact-grid">
                <div class="contact-form-wrapper">
                    <h2>Send Us a Message</h2>
                    <p>Fill out the form below and a member of our advisory team will respond within one business day.</p>
                    <form action="https://formspree.io/f/xpwdjqkr" method="POST" class="contact-form">
                        <div class="form-row">
                            <div class="form-group">
                                <label for="name">Full Name <span class="required">*</span></label>
                                <input type="text" id="name" name="name" required placeholder="Your full name">
                            </div>
                            <div class="form-group">
                                <label for="email">Email Address <span class="required">*</span></label>
                                <input type="email" id="email" name="email" required placeholder="you@example.com">
                            </div>
                        </div>
                        <div class="form-row">
                            <div class="form-group">
                                <label for="phone">Phone Number</label>
                                <input type="tel" id="phone" name="phone" placeholder="(555) 123-4567">
                            </div>
                            <div class="form-group">
                                <label for="service">Service Interest</label>
                                <select id="service" name="service">
                                    <option value="">Select a service...</option>
                                    <option value="Individual Tax Planning">Individual Tax Planning</option>
                                    <option value="Business Tax Services">Business Tax Services</option>
                                    <option value="Equity Compensation">Equity Compensation Planning</option>
                                    <option value="Multi-State Tax">Multi-State Tax Planning</option>
                                    <option value="Estate Planning">Estate &amp; Wealth Transfer</option>
                                    <option value="IRS Compliance">Tax Compliance &amp; IRS</option>
                                    <option value="Cost Segregation">Cost Segregation Studies</option>
                                    <option value="Retirement Exit">Retirement &amp; Exit Strategy</option>
                                    <option value="Other">Other / Not Sure</option>
                                </select>
                            </div>
                        </div>
                        <div class="form-group full-width">
                            <label for="message">Message <span class="required">*</span></label>
                            <textarea id="message" name="message" rows="5" required placeholder="Tell us about your situation and how we can help..."></textarea>
                        </div>
                        <button type="submit" class="btn-cta btn-lg">Send Message</button>
                        <p class="form-disclaimer">Your information is kept strictly confidential. We never share or sell your data.</p>
                    </form>
                </div>
                <div class="contact-info-sidebar">
                    <div class="contact-info-card">
                        <div class="contact-icon">&#128205;</div>
                        <h3>Visit Our Office</h3>
                        <p>6 PPG Place, Suite 820<br>Pittsburgh, PA 15222</p>
                    </div>
                    <div class="contact-info-card">
                        <div class="contact-icon">&#128222;</div>
                        <h3>Call Us</h3>
                        <p><a href="tel:+14129283031">(412) 928-3031</a></p>
                        <p class="contact-hours">Mon - Fri: 9:00 AM - 5:00 PM EST</p>
                    </div>
                    <div class="contact-info-card">
                        <div class="contact-icon">&#9993;&#65039;</div>
                        <h3>Email Us</h3>
                        <p><a href="mailto:team@aetaxadvisors.com">team@aetaxadvisors.com</a></p>
                    </div>
                    <div class="contact-info-card">
                        <div class="contact-icon">&#128197;</div>
                        <h3>Schedule a Consultation</h3>
                        <p>Skip the form and book directly with our team.</p>
                        <a href="/discovery/" class="btn-cta" style="margin-top:12px;">Book Now</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="map-section">
        <div class="container">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3036.4!2d-80.0!3d40.44!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8834f157a02c22e5%3A0x2c09df1a6b249208!2sPPG%20Place!5e0!3m2!1sen!2sus!4v1710000000000" width="100%" height="400" style="border:0; border-radius:12px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="AE Tax Advisors Office Location"></iframe>
        </div>
    </section>

    </main>

{FOOTER_HTML}

{STICKY_CTA_HTML}
</body>
</html>'''

    (BASE_DIR / 'contact' / 'index.html').write_text(page, encoding='utf-8')
    print("  -> Contact page built.")


# ============================================================
# 4. UPGRADE SERVICE DETAIL PAGES
# ============================================================

SERVICE_PAGES = {
    'individual-tax-planning-high-earners': {
        'title': 'Individual Tax Planning for High Earners',
        'meta_desc': 'Comprehensive individual tax planning for high-income W-2 earners. Income structuring, equity compensation timing, and proactive year-round strategies.',
        'icon': '&#128100;',
        'intro': 'For high-income W-2 earners, the standard approach to tax preparation leaves significant money on the table. AE Tax Advisors provides proactive, year-round individual tax planning designed to optimize every dollar of your income within full IRS compliance.',
        'benefits': [
            'W-2 withholding optimization and paycheck coordination',
            'Equity compensation timing (RSUs, ISOs, NSOs, ESPP)',
            'AMT analysis and mitigation strategies',
            'Charitable giving optimization (DAFs, CRTs, bunching)',
            'Roth conversion ladder planning',
            'Deferred compensation timing and election strategies',
            'Real estate loss coordination with W-2 income',
            'Year-end tax projection and proactive adjustments',
        ],
        'process': [
            ('Comprehensive Review', 'We start with a deep dive into your last 3 years of returns, pay stubs, equity statements, and investment accounts to identify missed opportunities.'),
            ('Strategy Design', 'Our team builds a multi-year tax plan tailored to your income trajectory, life events, and financial goals.'),
            ('Implementation', 'We coordinate with your employer, financial advisor, and estate attorney to execute every element of the strategy.'),
            ('Ongoing Monitoring', 'Quarterly check-ins, mid-year projections, and real-time adjustments keep your plan optimized as circumstances change.'),
        ],
        'faqs': [
            ('What income level qualifies for your services?', 'We typically work with individuals earning $500,000 or more annually, though we evaluate each situation individually based on complexity and planning opportunity.'),
            ('How is this different from my CPA?', 'Most CPAs focus on compliance and filing. We focus on proactive planning, which means identifying strategies to reduce your future tax liability, not just reporting what happened last year.'),
            ('Do you handle my tax return filing too?', 'Yes. Our engagement includes both strategic planning and return preparation, so your plan and your filing are always aligned.'),
        ],
    },
    'business-owner-small-business-tax': {
        'title': 'Business Owner & Small Business Tax Services',
        'meta_desc': 'Expert tax planning for business owners. Entity structuring, S-Corp elections, reasonable compensation, and multi-entity coordination.',
        'icon': '&#127970;',
        'intro': 'Business owners face a uniquely complex tax landscape. From entity selection to reasonable compensation to retirement plan design, every decision has tax consequences. AE Tax Advisors helps you structure your business and personal finances to minimize your combined tax liability.',
        'benefits': [
            'Entity selection and restructuring (LLC, S-Corp, C-Corp, partnership)',
            'Reasonable compensation analysis and documentation',
            'Qualified Business Income (QBI) deduction optimization',
            'Retirement plan design (401k, defined benefit, cash balance)',
            'Accountable plans and fringe benefit structuring',
            'Multi-entity coordination and intercompany transactions',
            'Exit and succession tax planning',
            'Hiring family members and Augusta Rule optimization',
        ],
        'process': [
            ('Entity & Structure Review', 'We analyze your current entity structure, ownership, and operational setup to identify restructuring opportunities.'),
            ('Tax Modeling', 'We model multiple scenarios comparing entity types, compensation levels, and retirement contributions to find the optimal configuration.'),
            ('Implementation & Coordination', 'We work with your attorney and bookkeeper to implement changes, update operating agreements, and set up new entities if needed.'),
            ('Year-Round Advisory', 'Monthly or quarterly touchpoints ensure your business decisions are tax-informed from day one.'),
        ],
        'faqs': [
            ('Should I be an S-Corp or C-Corp?', 'It depends on your income level, state of residence, reinvestment plans, and exit timeline. We model both scenarios with your actual numbers before recommending a structure.'),
            ('What is reasonable compensation and why does it matter?', 'The IRS requires S-Corp owners to pay themselves a reasonable salary. Setting it too low triggers audit risk; too high wastes payroll tax. We help you find the defensible sweet spot.'),
            ('Can you help me set up a retirement plan?', 'Absolutely. We design retirement plans (Solo 401k, SEP IRA, Defined Benefit, Cash Balance) that maximize your deductible contributions based on your business income.'),
        ],
    },
    'deferred-equity-compensation': {
        'title': 'Deferred Compensation & Equity Compensation Planning',
        'meta_desc': 'Expert guidance on stock options, RSUs, ESPP, deferred compensation, and executive benefits tax planning.',
        'icon': '&#128202;',
        'intro': 'Equity compensation is one of the most powerful wealth-building tools available to executives, but without proper planning, it can also be one of the most heavily taxed. AE Tax Advisors helps you time exercises, elections, and sales to minimize your overall tax burden.',
        'benefits': [
            'ISO vs. NSO exercise timing and AMT analysis',
            'RSU vesting and sale coordination with other income',
            'ESPP qualification and holding period optimization',
            'Section 409A deferred compensation election planning',
            'NQDC plan distribution timing and strategy',
            'Rule 10b5-1 trading plan tax coordination',
            'Concentrated stock position diversification',
            'Capital gains harvesting and loss offset strategies',
        ],
        'process': [
            ('Equity Inventory', 'We catalog all your equity grants, vesting schedules, exercise prices, and current values to build a complete picture.'),
            ('Tax Impact Modeling', 'We model the tax impact of different exercise/sale scenarios across current and future tax years.'),
            ('Timing Strategy', 'We develop a multi-year exercise and sale calendar coordinated with your other income events.'),
            ('Execution Support', 'We coordinate with your broker, HR department, and financial advisor to execute transactions at optimal times.'),
        ],
        'faqs': [
            ('When should I exercise my stock options?', 'The answer depends on your total income, AMT exposure, stock price trajectory, and liquidity needs. We model multiple scenarios to find the optimal timing.'),
            ('How are RSUs taxed differently from stock options?', 'RSUs are taxed as ordinary income at vesting, while ISOs can qualify for long-term capital gains treatment if holding period requirements are met. NSOs are taxed at exercise.'),
            ('What is a Section 83(b) election?', 'An 83(b) election lets you pay tax on restricted stock at grant rather than vesting, potentially converting future appreciation from ordinary income to capital gains.'),
        ],
    },
    'retirement-exit-ma-tax-strategy': {
        'title': 'Retirement & Exit / M&A Tax Strategy',
        'meta_desc': 'Tax planning for business exits, M&A transactions, and retirement income optimization. Minimize taxes on your biggest liquidity events.',
        'icon': '&#128179;',
        'intro': 'Whether you are selling a business, navigating an M&A transaction, or planning for retirement, the tax implications of these events can define your financial future. AE Tax Advisors helps you structure these transitions to preserve maximum after-tax wealth.',
        'benefits': [
            'Pre-sale tax structuring and entity reorganization',
            'Asset vs. stock sale analysis and negotiation support',
            'Section 1202 QSBS exclusion planning',
            'Installment sale and seller financing tax optimization',
            'Retirement income sequencing and bracket management',
            'Roth conversion strategies during low-income transition years',
            'Social Security timing optimization',
            'Required Minimum Distribution (RMD) planning',
        ],
        'process': [
            ('Exit Assessment', 'We review your business structure, valuation, and potential deal terms to identify tax planning opportunities.'),
            ('Pre-Transaction Planning', 'We implement restructuring, elections, and timing strategies before the transaction closes.'),
            ('Transaction Support', 'We coordinate with your M&A counsel and investment banker on tax-efficient deal structuring.'),
            ('Post-Transaction Optimization', 'We manage installment income, reinvestment, and ongoing tax planning for your new financial reality.'),
        ],
        'faqs': [
            ('How far in advance should I plan for a business sale?', 'Ideally 2 to 3 years before a sale. Many of the most powerful tax strategies require advance setup and holding periods.'),
            ('What is QSBS and could it apply to me?', 'Section 1202 Qualified Small Business Stock can exclude up to $10M or 10x your basis from federal capital gains tax. Eligibility depends on entity type, industry, and holding period.'),
            ('Can I defer taxes on a business sale?', 'Yes, through installment sales, Opportunity Zone reinvestment, charitable planning, and other structures. We model the tradeoffs for your specific situation.'),
        ],
    },
    'multi-state-global-tax': {
        'title': 'Multi-State & Global Tax Planning',
        'meta_desc': 'Multi-state income allocation, nexus analysis, residency planning, and international tax strategy for high-income individuals.',
        'icon': '&#127758;',
        'intro': 'If you earn income in multiple states or countries, you face a complex web of filing obligations, allocation rules, and potential double taxation. AE Tax Advisors navigates this complexity to ensure you pay what you owe and not a dollar more.',
        'benefits': [
            'State income allocation and apportionment analysis',
            'Nexus determination and filing obligation review',
            'Residency domicile planning and documentation',
            'State-specific deduction and credit optimization',
            'International tax compliance (FBAR, FATCA, Form 8938)',
            'Foreign tax credit coordination',
            'Treaty benefit analysis and application',
            'Expatriation and repatriation tax planning',
        ],
        'process': [
            ('Multi-Jurisdiction Review', 'We map all your income sources, filing obligations, and credit positions across every jurisdiction.'),
            ('Optimization Analysis', 'We identify opportunities to reduce your combined state and federal burden through allocation, timing, and residency strategies.'),
            ('Filing Coordination', 'We prepare and coordinate all state and international filings to maximize credits and minimize double taxation.'),
            ('Ongoing Monitoring', 'We track state law changes and your evolving footprint to keep your strategy current.'),
        ],
        'faqs': [
            ('Do I have to file in every state I earned income?', 'Generally yes, but the rules vary. Some states have de minimis thresholds, reciprocity agreements, or special rules for certain income types.'),
            ('Can I reduce my state taxes by changing residency?', 'Potentially, but states like New York and California aggressively audit residency changes. We help you document a legitimate move and avoid common pitfalls.'),
            ('What international reporting do I need to worry about?', 'If you have foreign accounts, assets, entities, or income, you may need to file FBAR, FATCA, and other information returns with significant penalties for noncompliance.'),
        ],
    },
    'estate-trust-wealth-transfer': {
        'title': 'Estate, Trust & Wealth Transfer Planning',
        'meta_desc': 'Coordinated estate and tax planning. GRATs, IDGTs, QSBS, charitable planning, and generational wealth transfer strategies.',
        'icon': '&#127968;',
        'intro': 'Estate planning is not just about what happens after you pass. It is an active, ongoing strategy that integrates with your income tax plan to transfer wealth efficiently during your lifetime and beyond. AE Tax Advisors coordinates estate, gift, and income tax planning into one cohesive framework.',
        'benefits': [
            'Grantor Retained Annuity Trust (GRAT) structuring',
            'Intentionally Defective Grantor Trust (IDGT) planning',
            'Gift tax annual exclusion and lifetime exemption optimization',
            'Generation-skipping transfer tax (GSTT) planning',
            'Charitable remainder and charitable lead trust design',
            'Family limited partnership and LLC structuring',
            'Valuation discount strategies for closely held businesses',
            'Trust income tax minimization and distribution planning',
        ],
        'process': [
            ('Estate Assessment', 'We review your current estate plan, trust documents, beneficiary designations, and asset titling.'),
            ('Tax-Integrated Design', 'We coordinate estate strategies with your income tax plan so both work together.'),
            ('Attorney Coordination', 'We work directly with your estate attorney to draft or update documents that implement the strategy.'),
            ('Annual Review', 'We monitor exemption levels, law changes, and asset growth to keep your plan current.'),
        ],
        'faqs': [
            ('When should I start estate planning?', 'Now. Many strategies require time to implement and work best when started early. Even if your estate is below the exemption, proper planning protects against state estate taxes and ensures efficient transfer.'),
            ('What is the current estate tax exemption?', 'As of 2025, the federal estate and gift tax exemption is approximately $13.61 million per individual. This is scheduled to sunset in 2026, making planning especially urgent.'),
            ('Do I need a trust?', 'Not always, but trusts offer significant benefits for tax planning, asset protection, privacy, and control over distributions. We evaluate whether a trust makes sense for your situation.'),
        ],
    },
    'tax-compliance-irs-representation': {
        'title': 'Tax Compliance & IRS Representation',
        'meta_desc': 'Professional tax return preparation, IRS audit defense, penalty abatement, and resolution services for high-income individuals and businesses.',
        'icon': '&#128220;',
        'intro': 'When it comes to the IRS, precision matters. AE Tax Advisors provides meticulous tax return preparation, audit defense, and resolution services for individuals and businesses with complex tax situations. Our compliance work is backed by the same deep planning expertise that drives our advisory practice.',
        'benefits': [
            'Complex individual and business return preparation',
            'IRS audit representation and defense',
            'Penalty abatement and reasonable cause arguments',
            'Offer in Compromise (OIC) preparation and negotiation',
            'Installment agreement setup and management',
            'Currently Not Collectible (CNC) status applications',
            'Amended return preparation and refund claims',
            'State tax controversy and resolution',
        ],
        'process': [
            ('Situation Assessment', 'We review your IRS notices, correspondence, and prior returns to understand the scope of the issue.'),
            ('Strategy Development', 'We develop a response strategy, gather supporting documentation, and prepare our arguments.'),
            ('IRS Communication', 'We handle all communication with the IRS on your behalf using Power of Attorney (Form 2848).'),
            ('Resolution & Prevention', 'We resolve the issue and implement safeguards to prevent future problems.'),
        ],
        'faqs': [
            ('What should I do if I get an IRS audit notice?', 'Do not respond on your own. Contact us immediately. We will review the notice, assess your exposure, and represent you throughout the audit process.'),
            ('Can you help me if I owe back taxes?', 'Yes. We evaluate your situation and pursue the best resolution path, whether that is an installment agreement, Offer in Compromise, penalty abatement, or Currently Not Collectible status.'),
            ('How far back can the IRS audit?', 'Generally 3 years from filing, but 6 years if there is a substantial understatement of income (>25%). There is no limit for fraud or unfiled returns.'),
        ],
    },
    'cost-segregation-studies-for-real-estate-investors': {
        'title': 'Cost Segregation Studies for Real Estate Investors',
        'meta_desc': 'IRS-compliant cost segregation studies that accelerate depreciation and maximize year-one tax deductions for real estate investors.',
        'icon': '&#127959;&#65039;',
        'intro': 'Cost segregation is one of the most powerful tax strategies available to real estate investors. By reclassifying building components from 27.5 or 39-year property to 5, 7, or 15-year property, you can accelerate tens of thousands of dollars in depreciation deductions into year one.',
        'benefits': [
            'Component-level analysis of building systems and finishes',
            'Reclassification to 5-year, 7-year, and 15-year MACRS property',
            'Bonus depreciation coordination for maximum year-one deductions',
            'Form 3115 catch-up depreciation for properties already in service',
            'Short-term rental (STR) loss optimization for W-2 earners',
            'Long-term rental depreciation coordination',
            'Partial asset disposition strategies',
            'Lookback studies for properties acquired in prior years',
        ],
        'process': [
            ('Property Analysis', 'We review your property details, acquisition costs, improvements, and current depreciation schedule.'),
            ('Engineering Study', 'Our team conducts a detailed component-level analysis identifying assets eligible for accelerated recovery.'),
            ('Tax Impact Modeling', 'We calculate the depreciation acceleration and model the tax impact across current and future years.'),
            ('Implementation', 'We prepare Form 3115 (if applicable), update depreciation schedules, and coordinate with your return filing.'),
        ],
        'faqs': [
            ('What types of properties qualify for cost segregation?', 'Any commercial, rental, or investment property with a depreciable basis. Short-term rentals, long-term rentals, office buildings, retail spaces, and mixed-use properties all qualify.'),
            ('Is there a minimum property value?', 'We typically recommend cost segregation for properties with a basis of $300,000 or more, though the breakeven point depends on your tax rate and situation.'),
            ('Can I do a cost segregation study on a property I already own?', 'Yes. A lookback study with Form 3115 lets you catch up on all missed accelerated depreciation in a single tax year, without amending prior returns.'),
        ],
    },
}


def build_service_pages():
    print("Building service detail pages...")

    for slug, info in SERVICE_PAGES.items():
        benefits_html = ''.join(f'<li>{b}</li>' for b in info['benefits'])

        process_html = ''
        for i, (step_title, step_desc) in enumerate(info['process'], 1):
            process_html += f'''
                <div class="process-step">
                    <div class="process-step-number">{i}</div>
                    <div class="process-step-content">
                        <h3>{step_title}</h3>
                        <p>{step_desc}</p>
                    </div>
                </div>'''

        faq_html = ''
        for q, a in info['faqs']:
            faq_html += f'''
                <div class="faq-item">
                    <h3>{q}</h3>
                    <p>{a}</p>
                </div>'''

        faq_schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a}
                } for q, a in info['faqs']
            ]
        }

        page = f'''<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}
    <title>{info['title']} | AE Tax Advisors</title>
    <meta name="description" content="{info['meta_desc']}">
    <link rel="canonical" href="https://aetaxadvisors.com/{slug}/">
    <meta property="og:title" content="{info['title']} | AE Tax Advisors">
    <meta property="og:description" content="{info['meta_desc']}">
    <meta property="og:url" content="https://aetaxadvisors.com/{slug}/">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="AE Tax Advisors">
{SCHEMA_ORG}
    <script type="application/ld+json">
{json.dumps(faq_schema, indent=2)}
    </script>
</head>
<body>
{get_nav('services')}

    <main>

    <section class="page-header">
        <div class="container">
            <div class="page-header-icon">{info['icon']}</div>
            <h1>{info['title']}</h1>
            <p>{info['meta_desc']}</p>
        </div>
    </section>

    <section class="content-section fade-in-section">
        <div class="container narrow">
            <p class="lead-text">{info['intro']}</p>
        </div>
    </section>

    <section class="benefits-section fade-in-section">
        <div class="container narrow">
            <h2>What We Cover</h2>
            <ul class="benefits-list">
                {benefits_html}
            </ul>
        </div>
    </section>

    <section class="process-section fade-in-section">
        <div class="container narrow">
            <h2>Our Process</h2>
            <div class="process-steps">
                {process_html}
            </div>
        </div>
    </section>

    <section class="faq-section fade-in-section">
        <div class="container narrow">
            <h2>Frequently Asked Questions</h2>
            {faq_html}
        </div>
    </section>

    <section class="cta-section fade-in-section">
        <div class="container">
            <h2>Ready to Get Started?</h2>
            <p>Schedule a complimentary consultation and discover how our {info['title'].lower()} services can work for your situation.</p>
            <a href="/discovery/" class="btn-cta btn-lg">Request Your Free Tax Assessment</a>
        </div>
    </section>

    </main>

{FOOTER_HTML}

{STICKY_CTA_HTML}
{ANIMATIONS_SCRIPT}
</body>
</html>'''

        page_dir = BASE_DIR / slug
        page_dir.mkdir(exist_ok=True)
        (page_dir / 'index.html').write_text(page, encoding='utf-8')

    print(f"  -> {len(SERVICE_PAGES)} service detail pages built.")


# ============================================================
# 5. UPDATE ALL EXISTING PAGES (nav + footer + animations)
# ============================================================

def update_all_pages():
    """Update nav and footer on ALL existing HTML pages that we didn't fully rebuild."""
    print("Updating nav/footer on all existing pages...")

    rebuilt = {'index.html', 'blog/index.html', 'contact/index.html'}
    rebuilt.update(f'{slug}/index.html' for slug in SERVICE_PAGES)

    count = 0
    for html_file in BASE_DIR.rglob('index.html'):
        rel = html_file.relative_to(BASE_DIR)
        if str(rel) in rebuilt:
            continue
        if '.git' in str(rel) or 'scripts' in str(rel):
            continue

        try:
            text = html_file.read_text(encoding='utf-8', errors='ignore')
        except:
            continue

        original = text

        # Determine active nav item
        slug = html_file.parent.name
        active = ''
        if slug in ('about', 'bios', 'ae-tax-advisors-mission-values'):
            active = 'about'
        elif slug == 'contact':
            active = 'contact'
        elif slug in ('case-studies',):
            active = 'cases'
        elif slug in ('blog', 'faq', 'glossary', 'guides'):
            active = 'resources'
        elif slug in SERVICE_PAGES:
            active = 'services'

        nav = get_nav(active)

        # Replace header
        header_pattern = r'<header>.*?</header>'
        if re.search(header_pattern, text, re.DOTALL):
            text = re.sub(header_pattern, nav, text, count=1, flags=re.DOTALL)

        # Replace footer
        footer_pattern = r'<footer>.*?</footer>'
        if re.search(footer_pattern, text, re.DOTALL):
            text = re.sub(footer_pattern, FOOTER_HTML, text, count=1, flags=re.DOTALL)

        # Add animations script if not present and has </body>
        if 'fade-in-visible' not in text and '</body>' in text:
            text = text.replace('</body>', f'{ANIMATIONS_SCRIPT}\n</body>')

        # Add fade-in-section to content sections
        text = text.replace('class="content-section"', 'class="content-section fade-in-section"')
        text = text.replace('class="faq-section"', 'class="faq-section fade-in-section"')

        if text != original:
            html_file.write_text(text, encoding='utf-8')
            count += 1

    print(f"  -> Updated {count} existing pages.")


# ============================================================
# 6. WRITE THE UPGRADED CSS
# ============================================================

def write_css():
    print("Writing upgraded CSS...")

    css = '''/* AE Tax Advisors - Premium Static Site Stylesheet */
:root {
    --primary: #408AAD;
    --primary-dark: #357a9a;
    --accent: #CC3366;
    --dark: #1a2a35;
    --medium: #575A5F;
    --light-bg: #F3F5F7;
    --white: #FFFFFF;
    --black: #000000;
    --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-heading: 'Playfair Display', Georgia, serif;
    --max-width: 1200px;
    --narrow: 800px;
    --shadow-sm: 0 2px 8px rgba(0,0,0,0.06);
    --shadow-md: 0 4px 20px rgba(0,0,0,0.08);
    --shadow-lg: 0 8px 40px rgba(0,0,0,0.12);
    --radius: 12px;
    --transition: 0.3s cubic-bezier(0.4,0,0.2,1);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }

body {
    font-family: var(--font-body);
    color: var(--dark);
    line-height: 1.7;
    font-size: 16px;
    background: var(--white);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

img { max-width: 100%; height: auto; display: block; }
a { color: var(--primary); text-decoration: none; transition: color var(--transition); }
a:hover { color: var(--accent); }

.container { max-width: var(--max-width); margin: 0 auto; padding: 0 24px; }
.narrow { max-width: var(--narrow); }
.center-text { text-align: center; }

/* ===== ANIMATIONS ===== */
.fade-in-section {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.7s ease-out, transform 0.7s ease-out;
}
.fade-in-visible {
    opacity: 1;
    transform: translateY(0);
}

/* ===== HEADER ===== */
header {
    background: rgba(255,255,255,0.97);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(0,0,0,0.06);
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

.header-inner {
    max-width: var(--max-width);
    margin: 0 auto;
    padding: 0 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 72px;
}

.logo img { height: 40px; width: auto; }

.nav-links {
    display: flex;
    align-items: center;
    gap: 2px;
}

.nav-link {
    color: var(--dark);
    font-size: 14px;
    font-weight: 500;
    padding: 8px 14px;
    border-radius: 6px;
    transition: background var(--transition), color var(--transition);
    white-space: nowrap;
    letter-spacing: -0.01em;
}

.nav-link:hover, .nav-link.active { background: var(--light-bg); color: var(--primary); }

.nav-dropdown { position: relative; }
.nav-dropdown .arrow { font-size: 10px; margin-left: 2px; transition: transform var(--transition); }
.nav-dropdown:hover .arrow { transform: rotate(180deg); }

.dropdown-content {
    display: none;
    position: absolute;
    top: calc(100% + 4px);
    left: 0;
    background: var(--white);
    min-width: 320px;
    box-shadow: var(--shadow-lg);
    border-radius: var(--radius);
    padding: 8px 0;
    z-index: 200;
    border: 1px solid rgba(0,0,0,0.06);
}

.nav-dropdown:hover .dropdown-content { display: block; }

.dropdown-item {
    display: block;
    padding: 10px 20px;
    color: var(--dark);
    font-size: 14px;
    transition: background var(--transition), padding-left var(--transition);
}
.dropdown-item:hover { background: var(--light-bg); color: var(--primary); padding-left: 24px; }

.nav-cta { margin-left: 8px; }

.btn-cta {
    display: inline-block;
    background: var(--primary);
    color: var(--white) !important;
    padding: 10px 24px;
    border-radius: 6px;
    font-weight: 600;
    font-size: 14px;
    transition: all var(--transition);
    white-space: nowrap;
    border: none;
    cursor: pointer;
}
.btn-cta:hover { background: var(--primary-dark); transform: translateY(-2px); box-shadow: 0 4px 12px rgba(64,138,173,0.3); }
.btn-cta.btn-lg { padding: 16px 36px; font-size: 16px; letter-spacing: 0.02em; }

.btn-secondary {
    display: inline-block;
    border: 2px solid var(--primary);
    color: var(--primary) !important;
    padding: 10px 24px;
    border-radius: 6px;
    font-weight: 600;
    font-size: 14px;
    transition: all var(--transition);
    white-space: nowrap;
    background: transparent;
    cursor: pointer;
}
.btn-secondary:hover { background: var(--primary); color: var(--white) !important; transform: translateY(-2px); }
.btn-hero-secondary { border-color: rgba(255,255,255,0.5); color: var(--white) !important; }
.btn-hero-secondary:hover { background: rgba(255,255,255,0.15); border-color: var(--white); }

.mobile-toggle {
    display: none;
    flex-direction: column;
    gap: 5px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
}
.mobile-toggle span {
    display: block;
    width: 24px;
    height: 2px;
    background: var(--dark);
    border-radius: 2px;
    transition: all var(--transition);
}

/* ===== HERO ===== */
.hero {
    background: linear-gradient(135deg, #0d2233 0%, #1a3a4a 30%, #2a5a6a 60%, #408AAD 100%);
    color: var(--white);
    padding: 100px 24px 110px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero-bg-pattern {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 20% 80%, rgba(64,138,173,0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(204,51,102,0.08) 0%, transparent 50%),
                radial-gradient(circle at 50% 50%, rgba(255,255,255,0.03) 0%, transparent 70%);
    pointer-events: none;
}

.hero-inner { max-width: 850px; margin: 0 auto; position: relative; z-index: 1; }

.hero-badges {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-bottom: 28px;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.2);
    padding: 6px 16px;
    border-radius: 100px;
    font-size: 13px;
    font-weight: 500;
    color: rgba(255,255,255,0.95);
    backdrop-filter: blur(4px);
    letter-spacing: 0.02em;
}

.hero h1 {
    font-family: var(--font-heading);
    font-size: 52px;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 24px;
    letter-spacing: -0.02em;
}
.hero-desc { font-size: 18px; opacity: 0.9; margin-bottom: 40px; line-height: 1.8; max-width: 700px; margin-left: auto; margin-right: auto; }

.hero-ctas {
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
}

/* ===== FEATURED / AS SEEN IN BAR ===== */
.featured-bar {
    background: var(--white);
    border-bottom: 1px solid rgba(0,0,0,0.06);
    padding: 24px;
    text-align: center;
}
.featured-label {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--medium);
    margin-bottom: 12px;
    font-weight: 600;
}
.featured-logos {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
}
.featured-item {
    font-size: 14px;
    font-weight: 600;
    color: var(--dark);
    opacity: 0.6;
    letter-spacing: 0.02em;
}
.featured-sep { color: #ddd; font-size: 14px; }

/* ===== STATS BAR ===== */
.stats-bar {
    background: linear-gradient(135deg, #0d2233, #1a3a4a);
    padding: 60px 24px;
    color: var(--white);
}
.stats-grid {
    max-width: var(--max-width);
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 32px;
    text-align: center;
}
.stat-number {
    display: block;
    font-family: var(--font-heading);
    font-size: 48px;
    font-weight: 800;
    line-height: 1.2;
    color: var(--white);
}
.stat-label {
    display: block;
    font-size: 14px;
    opacity: 0.8;
    margin-top: 8px;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 500;
}

/* ===== HOW IT WORKS ===== */
.how-it-works {
    background: var(--light-bg);
    padding: 80px 24px;
}
.steps-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
    margin-top: 40px;
    max-width: var(--max-width);
    margin-left: auto;
    margin-right: auto;
}
.step-card {
    text-align: center;
    padding: 40px 28px;
    background: var(--white);
    border-radius: var(--radius);
    box-shadow: var(--shadow-sm);
    transition: transform var(--transition), box-shadow var(--transition);
    position: relative;
}
.step-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); }
.step-number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 56px;
    height: 56px;
    background: var(--primary);
    color: var(--white);
    border-radius: 50%;
    font-size: 24px;
    font-weight: 800;
    margin-bottom: 20px;
    font-family: var(--font-heading);
}
.step-card h3 {
    font-family: var(--font-heading);
    font-size: 22px;
    margin-bottom: 12px;
    color: var(--dark);
}
.step-card p { color: var(--medium); font-size: 15px; line-height: 1.7; }

/* ===== SECTIONS ===== */
.segments, .at-a-glance, .services-overview, .why-us, .case-studies-preview, .testimonials-section, .blog-preview { padding: 80px 24px; }
.segments { background: var(--white); }
.at-a-glance { background: var(--light-bg); }
.services-overview { background: var(--white); }
.why-us { background: var(--light-bg); }
.case-studies-preview { background: var(--white); }
.testimonials-section { background: var(--light-bg); }
.blog-preview { background: var(--white); }

section h2 {
    font-family: var(--font-heading);
    font-size: 38px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 12px;
    color: var(--dark);
    letter-spacing: -0.02em;
}

.section-desc { text-align: center; color: var(--medium); margin-bottom: 24px; max-width: 650px; margin-left: auto; margin-right: auto; font-size: 17px; }

/* ===== CARDS ===== */
.card-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-top: 40px;
}
.card-grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
    margin-top: 40px;
}

.card-icon {
    font-size: 36px;
    margin-bottom: 16px;
    line-height: 1;
}

.card-link {
    display: inline-block;
    margin-top: 12px;
    color: var(--primary);
    font-weight: 600;
    font-size: 14px;
    transition: gap var(--transition);
}

.segment-card, .service-card, .stat-card, .why-card, .service-card-lg {
    background: var(--white);
    padding: 32px;
    border-radius: var(--radius);
    box-shadow: var(--shadow-sm);
    transition: transform var(--transition), box-shadow var(--transition);
    color: var(--dark);
    position: relative;
}
.segment-card:hover, .service-card:hover, .service-card-lg:hover, .why-card:hover {
    transform: translateY(-6px);
    box-shadow: var(--shadow-lg);
}

.segment-card h3, .service-card h3, .stat-card h3, .why-card h3, .service-card-lg h3 {
    font-family: var(--font-heading);
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 12px;
    color: var(--dark);
}

.segment-card p, .service-card p, .stat-card p, .why-card p, .service-card-lg p {
    color: var(--medium);
    font-size: 15px;
    line-height: 1.7;
}

.stat-card { background: var(--white); border-left: 4px solid var(--primary); }

.center-cta { text-align: center; margin-top: 40px; display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }

/* ===== CASE STUDY CARDS ===== */
.case-card {
    background: var(--white);
    border-radius: var(--radius);
    padding: 32px;
    box-shadow: var(--shadow-sm);
    transition: transform var(--transition), box-shadow var(--transition);
    border-top: 4px solid var(--primary);
}
.case-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); }
.case-amount {
    font-family: var(--font-heading);
    font-size: 36px;
    font-weight: 800;
    color: var(--primary);
    line-height: 1.2;
}
.case-label {
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--medium);
    margin-bottom: 16px;
    font-weight: 600;
}
.case-card h3 {
    font-family: var(--font-heading);
    font-size: 20px;
    margin-bottom: 8px;
    color: var(--dark);
}
.case-card p { color: var(--medium); font-size: 14px; line-height: 1.6; }

/* ===== TESTIMONIALS ===== */
.testimonial-card {
    background: var(--white);
    border-radius: var(--radius);
    padding: 32px;
    box-shadow: var(--shadow-sm);
    transition: transform var(--transition), box-shadow var(--transition);
}
.testimonial-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); }
.testimonial-stars { color: #f59e0b; font-size: 18px; margin-bottom: 16px; letter-spacing: 2px; }
.testimonial-text {
    color: var(--dark);
    font-size: 15px;
    line-height: 1.7;
    margin-bottom: 20px;
    font-style: italic;
}
.testimonial-author {
    display: flex;
    align-items: center;
    gap: 12px;
}
.author-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--primary), var(--primary-dark));
    color: var(--white);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 16px;
    flex-shrink: 0;
}
.author-info strong { display: block; font-size: 14px; color: var(--dark); }
.author-info span { font-size: 13px; color: var(--medium); }

/* ===== BLOG CARDS (homepage) ===== */
.blog-card {
    background: var(--white);
    border-radius: var(--radius);
    padding: 28px;
    box-shadow: var(--shadow-sm);
    transition: transform var(--transition), box-shadow var(--transition);
    color: var(--dark);
    display: flex;
    flex-direction: column;
}
.blog-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); color: var(--dark); }
.blog-card-category {
    display: inline-block;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--primary);
    margin-bottom: 12px;
    padding: 4px 12px;
    background: rgba(64,138,173,0.08);
    border-radius: 100px;
    align-self: flex-start;
}
.case-study-badge {
    color: var(--accent) !important;
    background: rgba(204,51,102,0.08) !important;
}
.blog-badge { }
.blog-card h3 {
    font-family: var(--font-heading);
    font-size: 19px;
    margin-bottom: 8px;
    line-height: 1.4;
    color: var(--dark);
}
.blog-card p { color: var(--medium); font-size: 14px; line-height: 1.6; flex-grow: 1; }

/* ===== BLOG INDEX ===== */
.blog-index-section { padding: 40px 24px 80px; }
.blog-filter-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 32px;
    justify-content: center;
}
.blog-filter {
    background: var(--light-bg);
    border: 1px solid transparent;
    padding: 8px 18px;
    border-radius: 100px;
    font-size: 13px;
    font-weight: 500;
    color: var(--medium);
    cursor: pointer;
    transition: all var(--transition);
    font-family: var(--font-body);
}
.blog-filter:hover { border-color: var(--primary); color: var(--primary); }
.blog-filter.active { background: var(--primary); color: var(--white); border-color: var(--primary); }

.blog-index-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}
.blog-index-card {
    background: var(--white);
    border-radius: var(--radius);
    padding: 24px;
    box-shadow: var(--shadow-sm);
    transition: transform var(--transition), box-shadow var(--transition);
    color: var(--dark);
    display: flex;
    flex-direction: column;
    border: 1px solid rgba(0,0,0,0.04);
}
.blog-index-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); color: var(--dark); }
.blog-index-card h3 {
    font-family: var(--font-heading);
    font-size: 17px;
    margin-bottom: 8px;
    line-height: 1.4;
    color: var(--dark);
}
.blog-index-card p { color: var(--medium); font-size: 13px; line-height: 1.6; flex-grow: 1; }
.blog-load-more { text-align: center; margin-top: 40px; }

/* ===== CTA SECTION ===== */
.cta-section {
    background: linear-gradient(135deg, #0d2233, #1a3a4a, #408AAD);
    color: var(--white);
    padding: 80px 24px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.cta-section h2 { color: var(--white); margin-bottom: 16px; }
.cta-section p { opacity: 0.9; max-width: 600px; margin: 0 auto 32px; font-size: 18px; }
.cta-buttons { display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; }

/* ===== PAGE HEADER ===== */
.page-header {
    background: linear-gradient(135deg, #0d2233 0%, #1a3a4a 30%, #2a5a6a 60%, #408AAD 100%);
    color: var(--white);
    padding: 70px 24px 60px;
    text-align: center;
    position: relative;
}
.page-header h1 {
    font-family: var(--font-heading);
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 12px;
    letter-spacing: -0.02em;
}
.page-header p { opacity: 0.9; font-size: 18px; max-width: 700px; margin: 0 auto; }
.page-header-icon { font-size: 48px; margin-bottom: 16px; }

/* ===== CONTENT ===== */
.content-section { padding: 60px 24px; }
.content-section h2 { text-align: left; font-size: 28px; margin: 40px 0 16px; font-weight: 700; }
.content-section h2:first-of-type { margin-top: 24px; }
.content-section p { margin-bottom: 16px; color: var(--medium); }
.lead-text { font-size: 18px; line-height: 1.8; color: var(--dark); }

/* ===== BENEFITS SECTION ===== */
.benefits-section { padding: 0 24px 60px; }
.benefits-section h2 { text-align: left; font-size: 28px; margin-bottom: 20px; }
.benefits-list {
    list-style: none;
    padding: 0;
}
.benefits-list li {
    padding: 12px 0 12px 36px;
    position: relative;
    color: var(--medium);
    font-size: 15px;
    line-height: 1.6;
    border-bottom: 1px solid rgba(0,0,0,0.05);
}
.benefits-list li::before {
    content: '\\2713';
    position: absolute;
    left: 0;
    color: var(--primary);
    font-weight: 700;
    font-size: 18px;
}

/* ===== PROCESS SECTION ===== */
.process-section { padding: 0 24px 60px; }
.process-section h2 { text-align: left; font-size: 28px; margin-bottom: 24px; }
.process-steps { }
.process-step {
    display: flex;
    gap: 20px;
    padding: 24px 0;
    border-bottom: 1px solid rgba(0,0,0,0.06);
}
.process-step:last-child { border-bottom: none; }
.process-step-number {
    flex-shrink: 0;
    width: 44px;
    height: 44px;
    background: var(--primary);
    color: var(--white);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 18px;
    font-family: var(--font-heading);
}
.process-step-content h3 { font-size: 18px; font-weight: 700; margin-bottom: 4px; color: var(--dark); }
.process-step-content p { color: var(--medium); font-size: 15px; line-height: 1.6; }

/* ===== FAQ SECTION ===== */
.faq-section { padding: 0 24px 60px; }
.faq-section h2 { text-align: left; font-size: 28px; margin-bottom: 24px; }
.faq-item {
    margin-bottom: 24px;
    padding: 24px;
    background: var(--light-bg);
    border-radius: var(--radius);
}
.faq-item h3 { font-size: 18px; font-weight: 700; margin-bottom: 8px; color: var(--dark); }
.faq-item p { color: var(--medium); font-size: 15px; line-height: 1.7; }

/* ===== CONTACT PAGE ===== */
.contact-section { padding: 60px 24px; }
.contact-grid {
    display: grid;
    grid-template-columns: 1.5fr 1fr;
    gap: 48px;
    max-width: var(--max-width);
    margin: 0 auto;
}
.contact-form-wrapper h2 { text-align: left; font-size: 28px; margin-bottom: 8px; }
.contact-form-wrapper > p { color: var(--medium); margin-bottom: 28px; }

.contact-form { }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }
.form-group { display: flex; flex-direction: column; }
.form-group.full-width { margin-bottom: 16px; }
.form-group label { font-size: 14px; font-weight: 600; margin-bottom: 6px; color: var(--dark); }
.required { color: var(--accent); }
.form-group input, .form-group select, .form-group textarea {
    padding: 12px 16px;
    border: 1px solid #d1d5db;
    border-radius: 8px;
    font-size: 15px;
    font-family: var(--font-body);
    transition: border-color var(--transition), box-shadow var(--transition);
    background: var(--white);
    color: var(--dark);
}
.form-group input:focus, .form-group select:focus, .form-group textarea:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(64,138,173,0.15);
}
.form-group textarea { resize: vertical; min-height: 120px; }
.form-disclaimer { font-size: 13px; color: var(--medium); margin-top: 12px; }

.contact-info-sidebar { display: flex; flex-direction: column; gap: 20px; }
.contact-info-card {
    background: var(--light-bg);
    border-radius: var(--radius);
    padding: 24px;
}
.contact-icon { font-size: 28px; margin-bottom: 8px; }
.contact-info-card h3 { font-size: 17px; font-weight: 700; margin-bottom: 6px; color: var(--dark); }
.contact-info-card p { font-size: 14px; color: var(--medium); line-height: 1.6; }
.contact-hours { font-size: 13px; color: var(--medium); margin-top: 4px; }

.map-section { padding: 0 24px 60px; }

/* ===== BLOG POST ===== */
.blog-post { padding: 40px 24px 80px; }
.breadcrumbs { font-size: 14px; color: var(--medium); margin-bottom: 24px; }
.breadcrumbs a { color: var(--primary); }
.blog-post h1 { font-family: var(--font-heading); font-size: 38px; font-weight: 800; margin-bottom: 12px; color: var(--dark); letter-spacing: -0.02em; }
.post-meta { font-size: 14px; color: var(--medium); margin-bottom: 32px; padding-bottom: 24px; border-bottom: 1px solid #e5e7eb; }
.post-content h2 { font-family: var(--font-heading); font-size: 24px; margin: 32px 0 12px; color: var(--dark); text-align: left; font-weight: 700; }
.post-content p { margin-bottom: 16px; color: var(--medium); }
.post-cta { text-align: center; margin-top: 48px; padding-top: 32px; border-top: 1px solid #e5e7eb; }

.blog-list { padding: 60px 24px; }

/* ===== SERVICES GRID ===== */
.services-grid { padding: 60px 24px; }

/* ===== FOOTER ===== */
footer {
    background: linear-gradient(180deg, #0d2233 0%, #1a2a35 100%);
    color: rgba(255,255,255,0.8);
    padding: 64px 24px 0;
}

.footer-inner {
    max-width: var(--max-width);
    margin: 0 auto;
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr 1fr;
    gap: 40px;
    padding-bottom: 40px;
}

.footer-brand { }
.footer-logo img { height: 36px; width: auto; margin-bottom: 16px; }
.footer-col p { font-size: 14px; line-height: 1.6; }
.footer-col h4 { color: var(--white); font-size: 13px; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 16px; font-weight: 700; }
.footer-col a { display: block; color: rgba(255,255,255,0.6); font-size: 14px; padding: 4px 0; transition: color var(--transition), padding-left var(--transition); }
.footer-col a:hover { color: var(--white); padding-left: 4px; }

.footer-social {
    display: flex;
    gap: 12px;
    margin-top: 20px;
}
.footer-social a {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: rgba(255,255,255,0.1);
    color: rgba(255,255,255,0.7);
    transition: all var(--transition);
    padding: 0;
}
.footer-social a:hover { background: var(--primary); color: var(--white); transform: translateY(-2px); }

.footer-trust-badges {
    margin-top: 16px;
    display: flex;
    flex-direction: column;
    gap: 6px;
}
.trust-badge {
    font-size: 12px;
    color: rgba(255,255,255,0.5);
}

.footer-address, .footer-phone, .footer-email { font-size: 14px; margin-bottom: 4px; }
.footer-phone a, .footer-email a { display: inline; padding: 0; }

.footer-bottom {
    border-top: 1px solid rgba(255,255,255,0.08);
    padding: 20px 0;
    text-align: center;
    max-width: var(--max-width);
    margin: 0 auto;
}
.footer-bottom p { font-size: 13px; color: rgba(255,255,255,0.4); }

/* ===== STICKY CTA ===== */
.sticky-cta {
    display: none;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(255,255,255,0.97);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 -2px 12px rgba(0,0,0,0.08);
    z-index: 90;
    padding: 12px 24px;
}
.sticky-inner {
    max-width: var(--max-width);
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.sticky-cta p { font-weight: 600; color: var(--dark); font-size: 14px; }

/* ===== LEAD MAGNET MODAL ===== */
.lead-modal {
    position: fixed;
    inset: 0;
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 24px;
}
.lead-modal-overlay {
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.6);
    backdrop-filter: blur(4px);
}
.lead-modal-content {
    position: relative;
    background: var(--white);
    border-radius: 16px;
    padding: 40px;
    max-width: 480px;
    width: 100%;
    box-shadow: var(--shadow-lg);
    text-align: center;
}
.lead-modal-close {
    position: absolute;
    top: 12px;
    right: 16px;
    background: none;
    border: none;
    font-size: 28px;
    color: var(--medium);
    cursor: pointer;
    transition: color var(--transition);
    line-height: 1;
}
.lead-modal-close:hover { color: var(--dark); }
.lead-modal-icon { font-size: 48px; margin-bottom: 16px; }
.lead-modal-content h3 { font-family: var(--font-heading); font-size: 24px; margin-bottom: 12px; color: var(--dark); }
.lead-modal-content p { color: var(--medium); font-size: 15px; margin-bottom: 20px; line-height: 1.6; }
.lead-modal-disclaimer { font-size: 12px; color: var(--medium); margin-top: 12px; }

/* ===== RESPONSIVE ===== */
@media (max-width: 1100px) {
    .footer-inner { grid-template-columns: repeat(3, 1fr); }
}

@media (max-width: 992px) {
    .card-grid-3, .blog-index-grid { grid-template-columns: repeat(2, 1fr); }
    .steps-grid { grid-template-columns: repeat(2, 1fr); }
    .stats-grid { grid-template-columns: repeat(2, 1fr); gap: 24px; }
    .hero h1 { font-size: 38px; }
    section h2 { font-size: 32px; }
}

@media (max-width: 768px) {
    .mobile-toggle { display: flex; }

    .nav-links {
        display: none;
        position: absolute;
        top: 72px;
        left: 0;
        right: 0;
        background: var(--white);
        flex-direction: column;
        padding: 16px 24px;
        box-shadow: var(--shadow-lg);
        align-items: stretch;
        max-height: 80vh;
        overflow-y: auto;
    }
    .nav-links.open { display: flex; }
    .nav-link { padding: 12px 0; }
    .nav-cta { margin-left: 0; margin-top: 8px; text-align: center; }
    .dropdown-content { position: static; box-shadow: none; padding-left: 16px; display: block; border: none; }
    .nav-dropdown:hover .dropdown-content { display: block; }

    .card-grid-3, .card-grid-2, .blog-index-grid, .steps-grid { grid-template-columns: 1fr; }
    .stats-grid { grid-template-columns: repeat(2, 1fr); }
    .footer-inner { grid-template-columns: 1fr; gap: 24px; }
    .contact-grid { grid-template-columns: 1fr; gap: 32px; }
    .form-row { grid-template-columns: 1fr; }

    .hero { padding: 60px 24px 70px; }
    .hero h1 { font-size: 32px; }
    .hero-desc { font-size: 16px; }
    .hero-badges { gap: 8px; }
    .hero-badge { font-size: 12px; padding: 4px 12px; }

    .page-header h1 { font-size: 30px; }
    section h2 { font-size: 28px; }

    .sticky-cta { display: block; }
    footer { padding-bottom: 60px; }

    .lead-modal-content { padding: 28px 20px; }
    .featured-logos { gap: 8px; }
    .featured-sep { display: none; }
    .featured-item { font-size: 12px; }
}

@media (max-width: 480px) {
    .hero h1 { font-size: 26px; }
    .header-inner { height: 60px; }
    .stat-number { font-size: 36px; }
    .page-header h1 { font-size: 26px; }
}
'''

    (BASE_DIR / 'assets' / 'style.css').write_text(css, encoding='utf-8')
    print("  -> CSS written.")


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    print("=" * 60)
    print("AE Tax Advisors Static Site - Major Upgrade")
    print("=" * 60)

    write_css()
    build_homepage()
    build_blog_index()
    build_contact_page()
    build_service_pages()
    update_all_pages()

    print()
    print("=" * 60)
    print("UPGRADE COMPLETE!")
    print("=" * 60)
