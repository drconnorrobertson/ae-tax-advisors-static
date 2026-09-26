#!/usr/bin/env python3
"""Regenerate sitemap.xml.

Only canonical, indexable URLs are listed. Pages that canonicalize elsewhere
(the blog-staging duplicates) are excluded so crawl budget goes to the real
pages. lastmod comes from file mtime; priority and changefreq are derived from
where the page sits in the site hierarchy.
"""
import json
import re
import subprocess
import argparse
from datetime import date
from pathlib import Path
from discovery_inventory import eligible

BASE = "https://www.aetaxadvisors.com"
OUT = Path("sitemap.xml")
CASE_OUT = Path("sitemap-case-studies.xml")

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


def redirected_paths():
    """Return exact source URLs handled by permanent redirects."""
    try:
        config = json.loads(Path("vercel.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return set()
    return {
        rule["source"]
        for rule in config.get("redirects", [])
        if rule.get("statusCode") in (301, 308)
        and isinstance(rule.get("source"), str)
        and ":" not in rule["source"]
    }


def read(path):
    return path.read_text(errors="ignore")


def canonical_of(text, slug):
    m = re.search(r'<link rel="canonical" href="' + re.escape(BASE) + r'([^"]*)"', text)
    return m.group(1) if m else "/" + slug + "/" if slug else "/"


def baseline_lastmods():
    """Preserve committed lastmod values for files that did not change.

    A fresh checkout gives every file today's filesystem mtime. Using that
    timestamp would falsely tell crawlers that the entire site changed.
    """
    try:
        xml = subprocess.run(
            ["git", "show", "HEAD:sitemap.xml"], check=True,
            capture_output=True, text=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        xml = OUT.read_text(errors="ignore") if OUT.exists() else ""
    return dict(re.findall(r"<loc>" + re.escape(BASE) + r"([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", xml))


def changed_paths():
    try:
        output = subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=all"],
            check=True, capture_output=True, text=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return set()
    return {line[3:].split(" -> ")[-1] for line in output.splitlines() if len(line) > 3}


def main(preserve_changed=False):
    urls = []
    skipped = 0
    previous = baseline_lastmods()
    changed = changed_paths()
    redirects = redirected_paths()
    today = date.today().isoformat()
    for p in sorted(Path(".").rglob("index.html")):
        if ".git" in p.parts:
            continue
        d = str(p.parent).replace("\\", "/")
        slug = "" if d == "." else d
        url = "/" if slug == "" else "/" + slug + "/"

        text = read(p)
        # Drop anything that canonicalizes elsewhere or is explicitly noindexed.
        if not eligible(p.resolve(), text, dict.fromkeys(redirects)):
            skipped += 1
            continue

        pri, freq = classify(slug)
        rel = p.as_posix()
        if url not in previous:
            lastmod = today
        elif rel in changed and not preserve_changed:
            lastmod = today
        else:
            lastmod = previous[url]
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
    case_lines = ['<?xml version="1.0" encoding="UTF-8"?>',
                  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, lastmod, freq, pri in urls:
        if not url.startswith("/case-studies/") or url == "/case-studies/":
            continue
        case_lines += ["  <url>",
                       f"    <loc>{BASE}{url}</loc>",
                       f"    <lastmod>{lastmod}</lastmod>",
                       f"    <changefreq>{freq}</changefreq>",
                       f"    <priority>{pri}</priority>",
                       "  </url>"]
    case_lines.append("</urlset>")
    CASE_OUT.write_text("\n".join(case_lines) + "\n")
    print(f"sitemap.xml: {len(urls)} URLs written, {skipped} non-canonical URLs excluded")
    print(f"sitemap-case-studies.xml: {(len(case_lines) - 2) // 6} documented studies written")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--preserve-lastmod",
        action="store_true",
        help="keep committed lastmod values during metadata-only maintenance",
    )
    args = parser.parse_args()
    main(preserve_changed=args.preserve_lastmod)
