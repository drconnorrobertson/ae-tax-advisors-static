#!/usr/bin/env python3
"""Add structured data that is grounded in each page's visible content.

FAQPage entries are built only from question headings that actually appear on
the page, with the answer taken from the copy underneath. Nothing is invented,
so the markup always matches what a reader sees. BreadcrumbList is added where
the page already renders a breadcrumb trail.
"""
import html
import json
import re
import sys
from pathlib import Path

BASE = "https://aetaxadvisors.com"
MAX_FAQ = 8
MIN_FAQ = 2
LISTING = {"blog", "faq", "guides", "glossary", "case-studies", "services",
           "blog-staging", ""}
MIN_ANSWER = 90
MAX_ANSWER = 900


def slug_of(p):
    d = str(p.parent).replace("\\", "/")
    return "" if d == "." else d


def clean(fragment):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", fragment, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def extract_faqs(main_html):
    """Pull question headings and the prose that answers them."""
    parts = re.split(r"(<h[23][^>]*>.*?</h[23]>)", main_html, flags=re.S)
    faqs = []
    for i, chunk in enumerate(parts):
        m = re.match(r"<h[23][^>]*>(.*?)</h[23]>", chunk, re.S)
        if not m:
            continue
        q = clean(m.group(1))
        if not q.endswith("?") or not (12 <= len(q) <= 180):
            continue
        body = parts[i + 1] if i + 1 < len(parts) else ""
        # answer = the paragraphs and list items before the next heading
        blocks = re.findall(r"<(?:p|li)[^>]*>(.*?)</(?:p|li)>", body, re.S)
        ans = " ".join(clean(b) for b in blocks).strip()
        if len(ans) < MIN_ANSWER:
            continue
        if len(ans) > MAX_ANSWER:
            cut = ans[:MAX_ANSWER]
            dot = cut.rfind(". ")
            ans = cut[: dot + 1] if dot > 200 else cut.rsplit(" ", 1)[0] + "."
        faqs.append((q, ans))
        if len(faqs) >= MAX_FAQ:
            break
    return faqs


def extract_breadcrumb(main_html, url, title):
    m = re.search(r'<div class="breadcrumbs">(.*?)</div>', main_html, re.S)
    if not m:
        return None
    items, pos = [], 0
    for href, label in re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', m.group(1), re.S):
        label = clean(label)
        if not label:
            continue
        pos += 1
        items.append({
            "@type": "ListItem",
            "position": pos,
            "name": label,
            "item": BASE + href if href.startswith("/") else href,
        })
    if not items:
        return None
    tail = clean(re.sub(r"<a\b.*?</a>", "", m.group(1), flags=re.S)).strip(" »>|/")
    items.append({
        "@type": "ListItem",
        "position": pos + 1,
        "name": (tail or title)[:120],
        "item": BASE + url,
    })
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": items}


def insert_schema(t, obj):
    block = ('    <script type="application/ld+json">\n'
             + json.dumps(obj, indent=2) + "\n    </script>\n")
    return t.replace("</head>", block + "</head>", 1)


def main():
    dry = "--dry" in sys.argv
    added_faq = added_bc = 0
    shown = 0

    for p in sorted(Path(".").rglob("index.html")):
        if ".git" in p.parts or "blog-staging" in p.parts:
            continue
        # listing pages render article titles as headings, not real Q&A
        if slug_of(p) in LISTING:
            continue
        t = p.read_text(errors="ignore")
        if "</head>" not in t:
            continue
        mm = re.search(r"<main>(.*?)</main>", t, re.S)
        if not mm:
            continue
        main_html = mm.group(1)
        s = slug_of(p)
        url = "/" if s == "" else "/" + s + "/"
        tm = re.search(r"<title>(.*?)</title>", t, re.S)
        title = re.sub(r"\s*\|\s*AE Tax Advisors\s*$", "", clean(tm.group(1))) if tm else s
        changed = False

        if "FAQPage" not in t:
            faqs = extract_faqs(main_html)
            if len(faqs) >= MIN_FAQ:
                obj = {
                    "@context": "https://schema.org",
                    "@type": "FAQPage",
                    "mainEntity": [
                        {"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer", "text": a}}
                        for q, a in faqs
                    ],
                }
                if dry and shown < 3:
                    print(f"\n/{s}/  ({len(faqs)} FAQs)")
                    for q, a in faqs[:2]:
                        print(f"   Q: {q}\n   A: {a[:110]}...")
                    shown += 1
                if not dry:
                    t = insert_schema(t, obj)
                added_faq += 1
                changed = True

        if "BreadcrumbList" not in t:
            bc = extract_breadcrumb(main_html, url, title)
            if bc and len(bc["itemListElement"]) >= 2:
                if not dry:
                    t = insert_schema(t, bc)
                added_bc += 1
                changed = True

        if changed and not dry:
            p.write_text(t)

    verb = "would add" if dry else "added"
    print(f"\n{verb} FAQPage on {added_faq} pages, BreadcrumbList on {added_bc} pages")


if __name__ == "__main__":
    main()
