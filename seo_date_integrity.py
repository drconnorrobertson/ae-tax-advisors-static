#!/usr/bin/env python3
"""Audit and reconcile page-level publication metadata.

The site has accumulated more than one schema block on some URLs.  This tool
keeps every page-level date signal aligned with the strongest existing source
instead of inventing a new or artificially old publication date.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any, Iterator


ROOT = Path(__file__).resolve().parent
PAGE_TYPES = {"Article", "BlogPosting", "NewsArticle", "WebPage", "Blog", "CollectionPage"}
SCRIPT = re.compile(
    r'(<script[^>]+type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)',
    re.I | re.S,
)
CANONICAL = re.compile(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)', re.I)
OG_PUBLISHED = re.compile(
    r'<meta\s+property=["\']article:published_time["\']\s+content=["\']([^"\']+)', re.I
)
OG_MODIFIED = re.compile(
    r'<meta\s+property=["\']article:modified_time["\']\s+content=["\']([^"\']+)', re.I
)
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def iso(value: Any) -> str | None:
    match = ISO_DATE.search(str(value or ""))
    return match.group(0) if match else None


def norm_url(value: Any) -> str:
    url = str(value or "").replace(
        "https://aetaxadvisors.com", "https://www.aetaxadvisors.com"
    )
    return url.rstrip("/") + "/" if url else ""


def node_types(node: dict[str, Any]) -> set[str]:
    value = node.get("@type")
    if isinstance(value, str):
        return {value}
    if isinstance(value, list):
        return {item for item in value if isinstance(item, str)}
    return set()


def node_url(node: dict[str, Any]) -> str:
    value = node.get("url") or node.get("@id")
    main = node.get("mainEntityOfPage")
    if not value and isinstance(main, dict):
        value = main.get("@id")
    elif not value and isinstance(main, str):
        value = main
    return norm_url(value)


def walk(value: Any, depth: int = 0) -> Iterator[tuple[dict[str, Any], int]]:
    if isinstance(value, dict):
        yield value, depth
        for child in value.values():
            yield from walk(child, depth + 1)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child, depth + 1)


def page_nodes(data: Any, canonical: str) -> list[dict[str, Any]]:
    nodes = []
    for node, depth in walk(data):
        if not node_types(node) & PAGE_TYPES:
            continue
        url = node_url(node)
        if url == canonical or (depth == 0 and not url):
            nodes.append(node)
    return nodes


def source_rank(node: dict[str, Any]) -> tuple[int, int]:
    types = node_types(node)
    if "BlogPosting" in types or "NewsArticle" in types:
        rank = 0
    elif "Article" in types and not node.get("isAccessibleForFree"):
        rank = 1
    elif "WebPage" in types or "Blog" in types or "CollectionPage" in types:
        rank = 2
    else:
        rank = 3
    completeness = -int(bool(iso(node.get("datePublished")))) - int(bool(iso(node.get("dateModified"))))
    return rank, completeness


def choose_dates(source: str, nodes: list[dict[str, Any]]) -> tuple[str | None, str | None]:
    published_meta = OG_PUBLISHED.search(source)
    modified_meta = OG_MODIFIED.search(source)
    published = iso(published_meta.group(1)) if published_meta else None
    modified = iso(modified_meta.group(1)) if modified_meta else None

    dated = [
        node for node in nodes
        if iso(node.get("datePublished")) or iso(node.get("dateModified"))
    ]
    anchor = min(dated, key=source_rank) if dated else None
    if not published and anchor:
        published = iso(anchor.get("datePublished"))
    if not modified and anchor:
        modified = iso(anchor.get("dateModified"))
    modified = modified or published
    if published and modified and modified < published:
        modified = published
    return published, modified


def inspect(path: Path, fix: bool) -> tuple[int, bool]:
    source = path.read_text(encoding="utf-8", errors="ignore")
    canonical_match = CANONICAL.search(source)
    if not canonical_match:
        return 0, False
    canonical = norm_url(canonical_match.group(1))

    parsed: list[tuple[re.Match[str], Any, list[dict[str, Any]]]] = []
    all_nodes: list[dict[str, Any]] = []
    for match in SCRIPT.finditer(source):
        try:
            data = json.loads(match.group(2))
        except json.JSONDecodeError:
            continue
        nodes = page_nodes(data, canonical)
        parsed.append((match, data, nodes))
        all_nodes.extend(nodes)

    published, modified = choose_dates(source, all_nodes)
    today = date.today().isoformat()
    values = []
    for node in all_nodes:
        if iso(node.get("datePublished")):
            values.append(("published", iso(node.get("datePublished"))))
        if iso(node.get("dateModified")):
            values.append(("modified", iso(node.get("dateModified"))))
    for regex, label in ((OG_PUBLISHED, "published"), (OG_MODIFIED, "modified")):
        match = regex.search(source)
        if match and iso(match.group(1)):
            values.append((label, iso(match.group(1))))

    issues = 0
    for label, value in values:
        expected = published if label == "published" else modified
        if value > today or (expected and value != expected):
            issues += 1
    if published and modified and modified < published:
        issues += 1

    if not fix or not issues or not published or not modified:
        return issues, False

    replacements: list[tuple[int, int, str]] = []
    for match, data, nodes in parsed:
        changed = False
        for node in nodes:
            if "datePublished" in node and iso(node.get("datePublished")) != published:
                node["datePublished"] = published
                changed = True
            if "dateModified" in node and iso(node.get("dateModified")) != modified:
                node["dateModified"] = modified
                changed = True
        if changed:
            body = "\n" + json.dumps(data, indent=2, ensure_ascii=False) + "\n"
            replacements.append((match.start(2), match.end(2), body))

    updated = source
    for start, end, body in reversed(replacements):
        updated = updated[:start] + body + updated[end:]
    if updated != source:
        path.write_text(updated, encoding="utf-8")
        return issues, True
    return issues, False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fix", action="store_true", help="reconcile conflicting page-level dates")
    args = parser.parse_args()

    issue_pages = 0
    issue_values = 0
    changed = 0
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts:
            continue
        issues, wrote = inspect(path, args.fix)
        if issues:
            issue_pages += 1
            issue_values += issues
        changed += int(wrote)

    if args.fix:
        print(f"date metadata reconciled: {changed} pages")
        return 0
    print(f"date-integrity conflicts: {issue_pages} pages ({issue_values} values)")
    return 1 if issue_pages else 0


if __name__ == "__main__":
    raise SystemExit(main())
