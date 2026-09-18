#!/usr/bin/env python3
"""
add_noindex.py - Add noindex meta tags to templated case study pages.

Targets case study directories matching templated patterns (numeric suffix variants)
and inserts <meta name="robots" content="noindex, follow"> after the viewport meta tag.

Run from the repo root directory:
    python3 add_noindex.py
"""

import os
import re
import glob

# Patterns for TEMPLATED case studies that should be noindexed.
# These all end with a numeric suffix (e.g., -395, -237, -181).
TEMPLATED_PATTERNS = [
    r"amended-return-recovery-\d+",
    r"c-corp-income-shift-\d+",
    r"cash-balance-401k-stack-\d+",
    r"commercial-.*-cost-seg-\d+",
    r"entity-restructure-ptet-.*-\d+",
    r"ltr-.*-form-3115-lookback-\d+",
    r"s-corp-election-reasonable-comp-\d+",
    r"str-coastal-beachfront-cost-seg-\d+",
    r"str-desert-desert-cost-seg-\d+",
    r"str-lake-lake-cost-seg-\d+",
    r"str-material-participation-release-.*-\d+",
    r"str-mountain-mountain-cost-seg-\d+",
    r"str-ski-ski-in-cost-seg-\d+",
    r"str-urban-downtown-cost-seg-\d+",
    r"str-urban-historic-cost-seg-\d+",
    r"str-vineyard-wine-cost-seg-\d+",
    r"w2-high-income-reduction-\d+",
    r"ltr-duplex-form-3115-lookback-\d+",
    r"ltr-fourplex-form-3115-lookback-\d+",
    r"ltr-mid-size-form-3115-lookback-\d+",
    r"ltr-mixed-form-3115-lookback-\d+",
    r"ltr-single-family-form-3115-lookback-\d+",
    r"ltr-small-form-3115-lookback-\d+",
    r"ltr-student-form-3115-lookback-\d+",
    r"ltr-townhome-form-3115-lookback-\d+",
    r"ltr-triplex-form-3115-lookback-\d+",
    r"ltr-workforce-form-3115-lookback-\d+",
]

# Compile a single regex that matches any templated pattern as a full directory name
COMBINED_PATTERN = re.compile(
    r"^(" + "|".join(TEMPLATED_PATTERNS) + r")$"
)

NOINDEX_TAG = '<meta name="robots" content="noindex, follow">'


def is_templated_case_study(dirname):
    """Check if a directory name matches a templated case study pattern."""
    return bool(COMBINED_PATTERN.match(dirname))


def add_noindex_to_file(filepath):
    """
    Add noindex meta tag to an HTML file after the viewport meta tag.
    Returns True if the file was modified, False otherwise.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if noindex tag already exists
    if 'noindex' in content:
        return False

    # Insert noindex tag after the viewport meta tag
    viewport_pattern = r'(<meta\s+name=["\']viewport["\'][^>]*>)'
    match = re.search(viewport_pattern, content, re.IGNORECASE)

    if match:
        insert_pos = match.end()
        new_content = (
            content[:insert_pos]
            + "\n    " + NOINDEX_TAG
            + content[insert_pos:]
        )
    else:
        # Fallback: insert before </head> if no viewport tag found
        head_close = content.find("</head>")
        if head_close == -1:
            print(f"  WARNING: No </head> found in {filepath}, skipping.")
            return False
        new_content = (
            content[:head_close]
            + "    " + NOINDEX_TAG + "\n"
            + content[head_close:]
        )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    case_studies_dir = os.path.join("case-studies")

    if not os.path.isdir(case_studies_dir):
        print(f"ERROR: Directory '{case_studies_dir}' not found.")
        print("Please run this script from the repo root directory.")
        return

    modified_count = 0
    skipped_count = 0
    not_found_count = 0
    total_checked = 0

    # Iterate through all subdirectories in case-studies/
    for entry in sorted(os.listdir(case_studies_dir)):
        entry_path = os.path.join(case_studies_dir, entry)

        if not os.path.isdir(entry_path):
            continue

        if not is_templated_case_study(entry):
            continue

        total_checked += 1
        index_path = os.path.join(entry_path, "index.html")

        if not os.path.isfile(index_path):
            print(f"  No index.html found: {entry_path}")
            not_found_count += 1
            continue

        if add_noindex_to_file(index_path):
            print(f"  MODIFIED: {index_path}")
            modified_count += 1
        else:
            print(f"  SKIPPED (already has noindex): {index_path}")
            skipped_count += 1

    print(f"\n{'='*60}")
    print(f"Templated case studies found:  {total_checked}")
    print(f"Files modified:                {modified_count}")
    print(f"Files skipped (already done):  {skipped_count}")
    print(f"Files not found:               {not_found_count}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
