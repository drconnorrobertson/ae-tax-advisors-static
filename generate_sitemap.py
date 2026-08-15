#!/usr/bin/env python3
"""Regenerate sitemap.xml.

Only canonical, indexable URLs are listed. Pages that canonicalize elsewhere
(the blog-staging duplicates) are excluded so crawl budget goes to the real
pages. lastmod comes from file mtime; priority and changefreq are derived from
where the page sits in the site hierarchy.
"""
import re
from datetime import date
from pathlib import Path

BASE = "https://aetaxadvisors.com"
OUT = Path("sitemap.xml")

PRIORITY = [
    (re.compile(r"^$"), "1.0", "weekly"),
    (re.compile(r"^(services|pricing|blog|case-studies|about|contact|discovery)$"), "0.9", "weekly"),
    (re.compile(r"^(cost-segregation|real-estate|business-owner|advanced-tax|"
                r"individual-tax|rental-property|tax-compliance)"), "0.9", "monthly"),
    (re.compile(r"^blog/"), "0.7", "monthly"),
    (re.compile(r"^(locations|case-studies)/"), "0.6", "monthly"),
]
DEFAULT = ("0.7", "monthly")


def classify(slug):
    for pat, pri, freq in PRIORITY:
        if pat.match(slug):
            return pri, freq
    return DEFAULT


NOINDEX = re.compile(r'<meta name="robots" content="[^"]*noindex', re.I)


def read(path):
    return path.read_text(errors="ignore")


def canonical_of(text, slug):
    m = re.search(r'<link rel="canonical" href="' + re.escape(BASE) + r'([^"]*)"', text)
    return m.group(1) if m else "/" + slug + "/" if slug else "/"


def main():
    urls = []
    skipped = 0
    for p in sorted(Path(".").rglob("index.html")):
        if ".git" in p.parts:
            continue
        d = str(p.parent).replace("\\", "/")
        slug = "" if d == "." else d
        url = "/" if slug == "" else "/" + slug + "/"

        text = read(p)
        # Drop anything that canonicalizes elsewhere or is explicitly noindexed.
        if canonical_of(text, slug) != url or NOINDEX.search(text):
            skipped += 1
            continue

        pri, freq = classify(slug)
        lastmod = date.fromtimestamp(p.stat().st_mtime).isoformat()
        urls.append((url, lastmod, freq, pri))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, lastmod, freq, pri in urls:
        lines += ["  <url>",
                  f"    <loc>{BASE}{url}</loc>",
                  f"    <lastmod>{lastmod}</lastmod>",
                  f"    <changefreq>{freq}</changefreq>",
                  f"    <priority>{pri}</priority>",
                  "  </url>"]
    lines.append("</urlset>")
    OUT.write_text("\n".join(lines) + "\n")
    print(f"sitemap.xml: {len(urls)} URLs written, {skipped} non-canonical URLs excluded")


if __name__ == "__main__":
    main()
