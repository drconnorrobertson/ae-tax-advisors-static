#!/usr/bin/env python3
"""Keep the blog sitemap aligned with the site's canonical main sitemap."""
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def read_urls(path):
    result = {}
    for item in ET.parse(path).getroot().findall(NS + "url"):
        loc = item.findtext(NS + "loc")
        mod = item.findtext(NS + "lastmod") or "2026-09-22"
        if loc:
            result[loc] = mod
    return result


def main():
    canonical = read_urls(ROOT / "sitemap.xml")
    old_blog = read_urls(ROOT / "sitemap-blog.xml")
    # Preserve canonical root-level legacy blog articles, plus the /blog/ hub
    # and every canonical article under /blog/.
    selected = sorted(
        url for url in canonical
        if url in old_blog or urlparse(url).path.startswith("/blog/")
    )
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in selected:
        lines.extend([
            "  <url>",
            f"    <loc>{escape(url)}</loc>",
            f"    <lastmod>{escape(canonical[url])}</lastmod>",
            "  </url>",
        ])
    lines.append("</urlset>")
    output = "\n".join(lines) + "\n"
    ET.fromstring(output)
    (ROOT / "sitemap-blog.xml").write_text(output)
    print(f"Blog sitemap: {len(selected)} canonical URLs; removed {len(set(old_blog)-set(canonical))} stale URLs")


if __name__ == "__main__":
    main()
