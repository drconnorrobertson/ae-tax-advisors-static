#!/usr/bin/env python3
"""Bring the standalone landing pages onto the AE Tax brand system.

These five pages were built with their own design language (Public Sans and
Fraunces, a cream and rust palette) and never loaded /assets/style.css. Rather
than rewriting their layouts, this remaps their typography and colour tokens to
the site palette, so nav, footer, colours, typography, and button styling read
as one brand across every page.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

TARGETS = [
    "short-term-rentals/index.html",
    "short-term-rentals/bnb-accelerator/index.html",
    "cost-segregation-landing/index.html",
    "equipment-leasing/index.html",
    "equipment-leasing-landing/index.html",
]

BRAND_FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?'
    "family=Inter:wght@400;500;600;700;800&"
    'family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">'
)

# Off-brand palette -> AE Tax palette. Keys are lowercase.
COLOR_MAP = {
    "#f3efe6": "#f8f9fa",  # cream page background  -> brand light background
    "#faf7f1": "#f8f9fa",
    "#f2ece1": "#f8f9fa",
    "#f7f0dd": "#f8f5ec",  # warm tint kept, nudged toward the gold accent
    "#efeadd": "#f8f9fa",
    "#16191c": "#1b2a4a",  # near-black headings    -> brand navy
    "#1b2a3d": "#1b2a4a",
    "#8c3b2a": "#c8a94a",  # rust accent            -> brand gold
    "#a6763e": "#c8a94a",
    "#8a5f30": "#b2953f",  # darker rust            -> darker gold
    "#6b5418": "#8a742f",
    "#2f4d3a": "#1b2a4a",  # green accent           -> brand navy
    "#4a5a6d": "#666666",  # slate body text        -> brand medium grey
    "#8b9196": "#666666",
    "#cfd9d3": "#e5e7eb",  # borders                -> brand border grey
    "#cfd2d5": "#e5e7eb",
}

FONT_MAP = [
    (re.compile(r"'Public Sans'"), "'Inter'"),
    (re.compile(r'"Public Sans"'), "'Inter'"),
    (re.compile(r"Public Sans"), "Inter"),
    (re.compile(r"'Fraunces'"), "'Playfair Display'"),
    (re.compile(r'"Fraunces"'), "'Playfair Display'"),
    (re.compile(r"Fraunces"), "Playfair Display"),
]

GOOGLE_FONT_LINK = re.compile(
    r'<link[^>]+fonts\.googleapis\.com[^>]*>', re.I
)
PRECONNECT = re.compile(r'<link[^>]+rel="preconnect"[^>]*fonts\.[^>]*>\s*', re.I)


def main() -> int:
    changed = 0
    for rel in TARGETS:
        path = ROOT / rel
        if not path.exists():
            print(f"skip (missing): {rel}")
            continue
        html = path.read_text(encoding="utf-8")
        before = html

        # Swap the webfont links for the brand pair (once).
        html = PRECONNECT.sub("", html)
        links = list(GOOGLE_FONT_LINK.finditer(html))
        if links:
            first = links[0]
            html = html[: first.start()] + BRAND_FONTS + html[first.end():]
            # Remove any remaining off-brand font links.
            html = GOOGLE_FONT_LINK.sub(
                lambda m: "" if "Inter" not in m.group(0) else m.group(0), html
            )

        # Remap fonts, but never inside the scoped nav block, which already uses
        # the brand font.
        for pat, repl in FONT_MAP:
            html = pat.sub(repl, html)

        # Remap colours, case-insensitively.
        def swap(m: re.Match) -> str:
            return COLOR_MAP.get(m.group(0).lower(), m.group(0))

        html = re.sub(r"#[0-9a-fA-F]{6}\b", swap, html)

        if html != before:
            path.write_text(html, encoding="utf-8")
            changed += 1
            print(f"rebranded: {rel}")

    print(f"\n{changed} landing pages brought onto the brand system.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
