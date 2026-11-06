"""Exact existing release transforms allowed by tax-content preservation tests.

This does not edit output or normalize arbitrary markup/text. Mirrors only the
known navigation caption, configured consolidation hrefs, and fixed footer
changes in build-public.cjs / consolidate-content.cjs / improve-editorial-discovery.py,
plus exact route-and-tag-specific CTAs from cost-seg-routing.cjs and the
known shared discovery CTA paragraph from normalize-shared-discovery-cta.cjs.
"""
import json
import re
from pathlib import Path
from urllib.parse import urlsplit



def normalize_shared_discovery_cta(value, policy_root):
    """Mirror the staged paragraph-only transform, with the identical DOM gate."""
    config = json.loads((Path(policy_root) / 'scripts/shared-discovery-cta.json').read_text())
    old = r'\s+'.join(re.escape(word) for word in config['old_paragraph'].split())
    anchors = '|'.join(re.escape(anchor) for anchor in config['anchors'])
    prefix = (r'(<section class="content-section fade-in-section" style="background:var\(--light-bg\);">\s*'
              r'<div class="container narrow center-text">\s*'
              r'<h2(?: id="answer-section-9")?>Talk Through Your Situation</h2>\s*<p>)')
    suffix = (r'(</p>\s*<div class="center-cta" style="margin-top:20px;">\s*(?:' + anchors +
              r')\s*</div>\s*</div>\s*</section>)')
    return re.sub(prefix + '(' + old + ')' + suffix,
                  lambda m: m[1] + config['new_paragraph'] + m[3], value)


def normalize_baseline_html(value, policy_root, route=None):
    policy_root = Path(policy_root)
    value = normalize_shared_discovery_cta(value, policy_root)
    consolidation = json.loads((policy_root / 'scripts/content-consolidation.json').read_text())
    host = consolidation['host']
    mapping = consolidation['redirects']
    config = json.loads((policy_root / 'vercel.json').read_text())
    redirects = {r['source']: r['destination'] for r in config.get('redirects', [])
                 if r.get('statusCode') in (301, 308) or r.get('permanent') is True}
    for source, target in mapping.items():
        assert target.startswith('/') and not target.startswith('//'), (source, target)
        assert redirects.get(source) == target, ('unverified consolidation redirect', source, target)

    def footer(m):
        s = m.group(0)
        if '>Upload My Documents</a>' not in s:
            upload = '<a href="https://aetaxadvisors.taxdome.com/">Upload My Documents</a>'
            portal = '<a href="https://aetaxadvisors.taxdome.com/">Client Portal</a>'
            if portal in s:
                s = s.replace(portal, portal + '\n' + upload, 1)
            else:
                s = s.replace('</footer>', '<p class="footer-legal-links">' + upload + '</p></footer>', 1)
        s = re.sub(r'<span class="trust-badge">[^<]*SOC 2 Compliant</span>', '', s)
        if 'href="/data-security-policy/"' not in s:
            term = '<a href="/terms-of-service/">Terms of Service</a>'
            s = s.replace(term, term + ' &middot; <a href="/data-security-policy/">Data Security Policy</a>', 1)
        if 'href="/ai-disclosure/"' not in s:
            disclosure = '<a href="/ai-disclosure/">AI Disclosure</a>'
            if '<a href="/disclaimer/">' in s:
                s = s.replace('<a href="/disclaimer/">', disclosure + ' &middot; <a href="/disclaimer/">', 1)
            else:
                s = s.replace('</footer>', '<p class="footer-legal-links">' + disclosure + '</p></footer>', 1)
        return s
    value = re.sub(r'<footer\b[^>]*>.*?</footer>', footer, value, flags=re.I | re.S)

    def href(m):
        original = m.group(1)
        path = original
        absolute = bool(re.match(r'^https?:', original))
        if absolute:
            parsed = urlsplit(original)
            if parsed.netloc != host:
                return m.group(0)
            path = parsed.path + ('?' + parsed.query if parsed.query else '') + ('#' + parsed.fragment if parsed.fragment else '')
        base = re.split(r'[?#]', path, maxsplit=1)[0]
        tail = path[len(base):]
        target = mapping.get(base) or mapping.get(base.rstrip('/')) or mapping.get(base.rstrip('/') + '/')
        if not target:
            return m.group(0)
        return 'href="' + ('https://' + host if absolute else '') + target + tail + '"'
    value = re.sub(r'href="([^"]+)"', href, value)
    value = re.sub(r'(<a\b[^>]*class="[^"]*(?:nav-cta|header-cta)[^"]*"[^>]*>)Request a Consultation(</a>)',
                   r'\1Book a Call\2', value, flags=re.I)
    # Exact existing cost-seg-routing.cjs transformations on two reviewed routes.
    # These labels/hrefs are checked individually; no arbitrary booking exemption.
    costseg_anchors = {
        '/blog/form-3115-cost-segregation-catch-up/': [
            '<a class="btn-cta" href="/discovery/">Choose a Time to Talk With AE Tax</a>',
            '<a href="/discovery/">Book a Call</a>',
            '<a href="/discovery/">Request a Consultation</a>',
            '<a href="/discovery/" class="btn-cta">Get Your Free Tax Assessment</a>',
        ],
        '/cost-segregation-complete-guide-2026/': [
            '<a href="/discovery/">schedule a free consultation</a>',
            '<a href="/discovery/" class="btn-cta">Schedule Your Free Consultation</a>',
            '<a href="/discovery/">Request a Consultation</a>',
            '<a href="/discovery/" class="btn-cta">Get Your Free Tax Assessment</a>',
        ],
    }
    for old in costseg_anchors.get(route, []):
        new = re.sub(r'>[^<]*</a>$', '>Book a Cost Seg Discovery Call</a>', old.replace('href="/discovery/"','href="/cost-seg-discovery/"'))
        value = value.replace(old, new)
    return value
