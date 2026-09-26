#!/usr/bin/env python3
"""Validate JSON-LD and remove AE's ineligible self-review markup.

Google does not show self-serving Organization/LocalBusiness review snippets.
Run with --fix after changing templates, then run without flags as a release gate.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPTS = re.compile(
    r'(<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)',
    re.I | re.S,
)
ORG_TYPES = {"Organization", "AccountingService", "ProfessionalService", "LocalBusiness"}


def types(node: dict) -> set[str]:
    value = node.get("@type")
    if isinstance(value, str):
        return {value}
    return {x for x in value if isinstance(x, str)} if isinstance(value, list) else set()


def scrub(value, fix: bool, findings: list[str]) -> bool:
    changed = False
    if isinstance(value, dict):
        if "BreadcrumbList" in types(value):
            items = value.get("itemListElement")
            if not isinstance(items, list):
                findings.append("breadcrumb itemListElement must be an array")
            else:
                valid = [item for item in items if isinstance(item, dict) and "ListItem" in types(item)]
                if len(valid) != len(items):
                    findings.append("non-ListItem entries in breadcrumb")
                    if fix:
                        value["itemListElement"] = valid
                        changed = True
                for position, item in enumerate(valid, 1):
                    if item.get("position") != position:
                        findings.append("breadcrumb positions must be sequential")
                        if fix:
                            item["position"] = position
                            changed = True
                    if not item.get("name"):
                        findings.append("breadcrumb name missing")
        if value.get("name") == "AE Tax Advisors" and types(value) & ORG_TYPES:
            for field in ("aggregateRating", "review"):
                if field in value:
                    findings.append(field)
                    if fix:
                        del value[field]
                        changed = True
        for child in value.values():
            changed = scrub(child, fix, findings) or changed
    elif isinstance(value, list):
        for child in value:
            changed = scrub(child, fix, findings) or changed
    return changed


def inspect(path: Path, fix: bool) -> tuple[list[str], int]:
    source = path.read_text(encoding="utf-8", errors="replace")
    findings: list[str] = []
    edits = 0

    def replace(match: re.Match) -> str:
        nonlocal edits
        try:
            data = json.loads(match.group(2))
        except json.JSONDecodeError as error:
            findings.append(f"invalid JSON-LD: {error}")
            return match.group(0)
        issues: list[str] = []
        if not scrub(data, fix, issues):
            findings.extend(issues)
            return match.group(0)
        findings.extend(issues)
        edits += 1
        return match.group(1) + "\n" + json.dumps(data, indent=2, ensure_ascii=False) + "\n" + match.group(3)

    updated = SCRIPTS.sub(replace, source)
    if fix and edits:
        path.write_text(updated, encoding="utf-8")
    return findings, edits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true")
    args = parser.parse_args()
    pages = list(ROOT.rglob("*.html"))
    issues = 0
    updated = 0
    samples = []
    for path in pages:
        if ".git" in path.parts:
            continue
        findings, edits = inspect(path, args.fix)
        issues += len(findings)
        updated += bool(edits)
        if findings and len(samples) < 8:
            samples.append(f"{path.relative_to(ROOT)}: {', '.join(findings[:3])}")
    print(f"pages inspected: {len(pages)}")
    print(f"schema issues found: {issues}")
    print(f"pages updated: {updated}")
    for sample in samples:
        print(f"  {sample}")
    return 0 if args.fix or issues == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
