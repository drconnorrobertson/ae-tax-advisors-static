#!/usr/bin/env python3
"""Submit every canonical URL on the site to IndexNow.

IndexNow notifies Bing, Yandex, Seznam, Naver and other participating engines
that URLs have changed. Google does not participate; it is covered by the
sitemap and normal crawling.

Usage:
    python3 submit_indexnow.py            # submit every URL in sitemap.xml
    python3 submit_indexnow.py --dry      # show what would be sent
    python3 submit_indexnow.py <url>...   # submit specific URLs
"""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent

KEY = "d1abe8dd1952d605902db4522d2536d3"
HOST = "aetaxadvisors.com"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/IndexNow"

# IndexNow accepts at most 10,000 URLs per request; keep batches well under it.
BATCH = 1000
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def urls_from_sitemap() -> list[str]:
    sm = ROOT / "sitemap.xml"
    if not sm.exists():
        print("sitemap.xml not found. Run generate_sitemap.py first.", file=sys.stderr)
        return []
    root = ET.parse(sm).getroot()
    return [e.text.strip() for e in root.iter(NS + "loc") if e.text]


def verify_key_file() -> bool:
    """The key file must be reachable at the host root for IndexNow to trust us."""
    f = ROOT / f"{KEY}.txt"
    if not f.exists():
        print(f"WARNING: {KEY}.txt is missing from the site root.", file=sys.stderr)
        return False
    content = f.read_text(encoding="utf-8").strip()
    if content != KEY:
        print(f"WARNING: {KEY}.txt content does not match the key.", file=sys.stderr)
        return False
    return True


def submit(batch: list[str], dry: bool) -> tuple[int, str]:
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": batch,
    }
    if dry:
        return 0, f"DRY RUN: would submit {len(batch)} URLs"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8",
                 "User-Agent": "AE-Tax-Advisors-IndexNow/1.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")[:200]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")[:300]
    except Exception as e:  # network failure, DNS, timeout
        return 0, f"ERROR: {e}"


STATUS_MEANING = {
    200: "OK, URLs submitted",
    202: "Accepted, key validation pending",
    400: "Bad request, check the payload",
    403: "Forbidden, key not valid for this host",
    422: "Unprocessable, URLs do not match the host",
    429: "Too many requests, slow down",
}


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry" in sys.argv

    urls = args or urls_from_sitemap()
    if not urls:
        print("No URLs to submit.")
        return 1

    # Only submit URLs on our own host; IndexNow rejects mismatches.
    urls = [u for u in urls if f"//{HOST}/" in u or u.rstrip("/").endswith(f"//{HOST}")]
    urls = sorted(set(urls))

    key_ok = verify_key_file()
    print(f"host:         {HOST}")
    print(f"key file:     {'verified' if key_ok else 'MISSING OR MISMATCHED'}")
    print(f"key location: {KEY_LOCATION}")
    print(f"URLs to submit: {len(urls)}")
    print()

    batches = [urls[i:i + BATCH] for i in range(0, len(urls), BATCH)]
    ok = failed = 0
    for i, batch in enumerate(batches, start=1):
        status, body = submit(batch, dry)
        meaning = STATUS_MEANING.get(status, "see response")
        label = "OK" if status in (200, 202) or dry else "FAILED"
        if status in (200, 202) or dry:
            ok += len(batch)
        else:
            failed += len(batch)
        print(f"batch {i}/{len(batches)}  {len(batch):>5} URLs  "
              f"HTTP {status}  {label}  ({meaning})")
        if body and status not in (200, 202):
            print(f"    {body}")
        if not dry and i < len(batches):
            time.sleep(2)

    print()
    print(f"submitted: {ok}   failed: {failed}")
    if failed:
        print("Retry failed batches once the key file is live at the host root.")
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
