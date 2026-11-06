#!/usr/bin/env python3
"""Verify that build-aware preservation allows known transforms only."""
from pathlib import Path
from tax_review_build_normalization import normalize_baseline_html
ROOT=Path(__file__).resolve().parents[1]
n=lambda s:normalize_baseline_html(s,ROOT)
assert n('<a href="/discovery/" class="btn-cta nav-cta">Request a Consultation</a>')=='<a href="/discovery/" class="btn-cta nav-cta">Book a Call</a>'
assert n('<a href="/discovery/" class="btn-cta">Request a Consultation</a>')=='<a href="/discovery/" class="btn-cta">Request a Consultation</a>'
assert n('<a href="/discovery/" class="nav-cta">A Different Message</a>')=='<a href="/discovery/" class="nav-cta">A Different Message</a>'
assert n('<a href="/business-owner-tax-planning/?q=1#fees">Fees $1,500</a>')=='<a href="/business-owner-small-business-tax/?q=1#fees">Fees $1,500</a>'
assert n('<a href="https://www.aetaxadvisors.com/business-owner-tax-planning/">Guide</a>')=='<a href="https://www.aetaxadvisors.com/business-owner-small-business-tax/">Guide</a>'
for value in ['<a href="https://example.org/business-owner-tax-planning/">External</a>',
              '<a href="/not-a-configured-redirect/">Unchanged</a>',
              '<a href="/case-studies/example/">Client outcome $50,000</a>',
              '<p>Fee: $2,000. Historical tax outcome: $12,345.</p>']:
    assert n(value)==value
# Unknown CTA, href, fee and case-text changes remain detectable.
for original,altered in [
    ('<a href="/discovery/" class="nav-cta">Request a Consultation</a>','<a href="/discovery/" class="nav-cta">Purchase Now</a>'),
    ('<a href="/business-owner-tax-planning/">Guide</a>','<a href="/wrong-target/">Guide</a>'),
    ('<p>Fee: $2,000.</p>','<p>Fee: $1,000.</p>'),
    ('<a href="/case-studies/example/">Outcome $50,000</a>','<a href="/case-studies/example/">Outcome $75,000</a>')]:
    assert n(original)!=altered
# One documented, route-specific cost-segregation CTA. No general booking
# exemption, no changed caption/target, and no arbitrary navigation replacement.
route='/blog/form-3115-cost-segregation-catch-up/'
old='<a class="btn-cta" href="/discovery/">Choose a Time to Talk With AE Tax</a>'
expected='<a class="btn-cta" href="/cost-seg-discovery/">Book a Cost Seg Discovery Call</a>'
assert normalize_baseline_html(old,ROOT,route=route)==expected
assert normalize_baseline_html(old,ROOT,route='/blog/another-form-3115-page/')==old
assert normalize_baseline_html(old,ROOT)==old
for other in [old.replace('Choose a Time to Talk With AE Tax','Different caption'),
              old.replace('href="/discovery/"','href="/other-booking/"'),
              old.replace('class="btn-cta"','class="btn-cta nav-cta"')]:
    assert normalize_baseline_html(other,ROOT,route=route)==other
for altered in [expected.replace('/cost-seg-discovery/','/wrong-target/'),
                expected.replace('Book a Cost Seg Discovery Call','Different caption')]:
    assert normalize_baseline_html(old,ROOT,route=route)!=altered
for original,altered in [('<p>Fee: $2,000.</p>','<p>Fee: $1,000.</p>'),
                         ('<a href="/case-studies/example/">Outcome $50,000</a>',
                          '<a href="/case-studies/example/">Outcome $75,000</a>')]:
    assert normalize_baseline_html(old+original,ROOT,route=route)!=expected+altered
print('PASS: exact build transforms and first route-specific cost-seg CTA allowed; unknown routes, captions, targets, prices and case changes rejected.')

# The second reviewed cost-seg route has its own four exact legacy anchors.
for route,label,attrs in [
 ('/cost-segregation-complete-guide-2026/','schedule a free consultation',''),
 ('/cost-segregation-complete-guide-2026/','Schedule Your Free Consultation',' class="btn-cta"'),
 ('/blog/form-3115-cost-segregation-catch-up/','Book a Call',''),
]:
 old='<a href="/discovery/"'+attrs+'>'+label+'</a>'
 expected='<a href="/cost-seg-discovery/"'+attrs+'>Book a Cost Seg Discovery Call</a>'
 assert normalize_baseline_html(old,ROOT,route)==expected
 assert normalize_baseline_html(old,ROOT,'/unreviewed/')==old
 changed=old.replace(label,'Unreviewed caption')
 assert normalize_baseline_html(changed,ROOT,route)==changed
 assert normalize_baseline_html(old,ROOT,route)!=expected.replace('/cost-seg-discovery/','/wrong-target/')
print('PASS both exact cost-seg route/caption allowlists and unrelated-route rejection.')
