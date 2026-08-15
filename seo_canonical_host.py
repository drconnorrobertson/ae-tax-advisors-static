#!/usr/bin/env python3
"""Align every absolute URL to the host that actually serves content.

The Vercel project has www.aetaxadvisors.com as its primary domain, so
https://aetaxadvisors.com/... issues a 307 to https://www.aetaxadvisors.com/...
Every canonical tag, og:url, and schema URL on the site pointed at the
non-www host, which tells search engines the canonical URL is one that
immediately redirects away. This rewrites those absolute references to www so
the canonical target resolves 200 with no hop.

If the intent is for non-www to be primary instead, the fix is to change the
primary domain in Vercel and run this with --to-non-www.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

NON_WWW = "https://aetaxadvisors.com"
WWW = "https://www.aetaxadvisors.com"

TEXT_FILES = {".html", ".xml", ".txt", ".json"}


def main() -> int:
    to_non_www = "--to-non-www" in sys.argv
    src, dst = (WWW, NON_WWW) if to_non_www else (NON_WWW, WWW)

    # Avoid double-prefixing www when running the www direction repeatedly.
    pattern = re.compile(re.escape(src) + r"(?![a-zA-Z0-9.-])")

    changed_files = 0
    changed_refs = 0
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in TEXT_FILES:
            continue
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if src not in text:
            continue
        new, n = pattern.subn(dst, text)
        if n:
            path.write_text(new, encoding="utf-8")
            changed_files += 1
            changed_refs += n

    print(f"rewrote {changed_refs} absolute URLs across {changed_files} files")
    print(f"canonical host is now: {dst}")

    # Report any leftovers.
    leftover = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in TEXT_FILES or ".git" in path.parts:
            continue
        try:
            if pattern.search(path.read_text(encoding="utf-8")):
                leftover += 1
        except UnicodeDecodeError:
            continue
    print(f"files still referencing the old host: {leftover}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
