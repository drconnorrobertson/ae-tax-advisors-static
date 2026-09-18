#!/usr/bin/env python3
"""
add_faq_schema.py - Add FAQPage JSON-LD schema to service pages.

Scans service page HTML files for FAQ content (div.faq-item with h3 questions
and p answers), generates FAQPage schema markup, and inserts it before </head>.

Run from the repo root directory:
    python3 add_faq_schema.py
"""

import os
import re
import json
import html


# Target directories to scan for FAQ content
TARGET_DIRS = [
    "services",
    "cost-segregation-study",
    "real-estate-tax-planning",
    "short-term-rental-tax-strategy",
    "rental-property-tax-planning",
    "business-owner-small-business-tax",
    "retirement-exit-ma-tax-strategy",
    "individual-tax-planning-high-earners",
    "equipment-leasing-section-179",
    "estate-trust-wealth-transfer",
    "tax-compliance-irs-representation",
    "pricing",
    "about",
    "faq",
    "ae-tax-advisors-faq",
]


def strip_html_tags(text):
    """Remove HTML tags from a string and decode HTML entities."""
    clean = re.sub(r"<[^>]+>", "", text)
    clean = html.unescape(clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean


def extract_faq_items(content):
    """
    Extract FAQ question-answer pairs from HTML content.
    Looks for <div class="faq-item"> blocks containing <h3> questions and <p> answers.
    """
    faq_items = []

    # Pattern to match faq-item divs and extract their content
    # This handles nested divs by being generous with content matching
    faq_item_pattern = re.compile(
        r'<div[^>]*class="[^"]*faq-item[^"]*"[^>]*>(.*?)</div>\s*(?=<div[^>]*class="[^"]*faq-item|$)',
        re.DOTALL | re.IGNORECASE
    )

    # Alternative: match faq-item blocks more broadly
    # Split content around faq-item markers
    parts = re.split(r'<div[^>]*class="[^"]*faq-item[^"]*"[^>]*>', content, flags=re.IGNORECASE)

    for part in parts[1:]:  # Skip content before first faq-item
        # Extract question from h3
        h3_match = re.search(r"<h3[^>]*>(.*?)</h3>", part, re.DOTALL | re.IGNORECASE)
        if not h3_match:
            continue

        question = strip_html_tags(h3_match.group(1))

        # Extract answer from p tags (may be multiple paragraphs)
        # Get all p tag content after the h3
        after_h3 = part[h3_match.end():]
        p_matches = re.findall(r"<p[^>]*>(.*?)</p>", after_h3, re.DOTALL | re.IGNORECASE)

        if not p_matches:
            continue

        # Combine all paragraph text as the answer
        answer = " ".join(strip_html_tags(p) for p in p_matches if strip_html_tags(p))

        if question and answer:
            faq_items.append({"question": question, "answer": answer})

    return faq_items


def has_faq_schema(content):
    """Check if FAQPage schema already exists in the HTML."""
    return '"@type": "FAQPage"' in content or '"@type":"FAQPage"' in content


def has_faq_content(content):
    """Check if the page has FAQ item divs."""
    return bool(re.search(r'class="[^"]*faq-item[^"]*"', content, re.IGNORECASE))


def generate_faq_schema(faq_items):
    """Generate FAQPage JSON-LD schema markup."""
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }

    for item in faq_items:
        schema["mainEntity"].append({
            "@type": "Question",
            "name": item["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["answer"]
            }
        })

    script_tag = (
        '<script type="application/ld+json">\n'
        + json.dumps(schema, indent=2, ensure_ascii=False)
        + "\n</script>"
    )

    return script_tag


def process_file(filepath):
    """
    Process a single HTML file: extract FAQs and insert schema if needed.
    Returns a status string: 'modified', 'skipped_has_schema', 'skipped_no_faq', or 'error'.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except (IOError, UnicodeDecodeError) as e:
        print(f"  ERROR reading {filepath}: {e}")
        return "error"

    # Check if FAQ schema already exists
    if has_faq_schema(content):
        return "skipped_has_schema"

    # Check if page has FAQ content
    if not has_faq_content(content):
        return "skipped_no_faq"

    # Extract FAQ items
    faq_items = extract_faq_items(content)

    if not faq_items:
        print(f"  WARNING: Found faq-item divs but could not extract Q&A pairs: {filepath}")
        return "skipped_no_faq"

    # Generate schema
    schema_tag = generate_faq_schema(faq_items)

    # Insert before </head>
    head_close_pos = content.find("</head>")
    if head_close_pos == -1:
        head_close_pos = content.find("</HEAD>")

    if head_close_pos == -1:
        print(f"  WARNING: No </head> tag found in {filepath}, skipping.")
        return "error"

    new_content = (
        content[:head_close_pos]
        + schema_tag + "\n"
        + content[head_close_pos:]
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  MODIFIED: {filepath} ({len(faq_items)} FAQ items)")
    return "modified"


def main():
    modified_files = []
    skipped_schema = []
    skipped_no_faq = []
    errors = []

    for target_dir in TARGET_DIRS:
        if not os.path.isdir(target_dir):
            print(f"  Directory not found: {target_dir}/")
            continue

        # Check for index.html in the directory
        index_path = os.path.join(target_dir, "index.html")

        if not os.path.isfile(index_path):
            # Try the directory itself as a file path pattern
            # Some sites use directory/index.html, others use directory.html
            alt_path = target_dir + ".html"
            if os.path.isfile(alt_path):
                index_path = alt_path
            else:
                print(f"  No index.html found in: {target_dir}/")
                continue

        status = process_file(index_path)

        if status == "modified":
            modified_files.append(index_path)
        elif status == "skipped_has_schema":
            skipped_schema.append(index_path)
        elif status == "skipped_no_faq":
            skipped_no_faq.append(index_path)
        elif status == "error":
            errors.append(index_path)

    print(f"\n{'='*60}")
    print(f"FAQ Schema Insertion Summary")
    print(f"{'='*60}")
    print(f"Directories scanned:           {len(TARGET_DIRS)}")
    print(f"Files modified:                {len(modified_files)}")
    print(f"Skipped (schema exists):       {len(skipped_schema)}")
    print(f"Skipped (no FAQ content):      {len(skipped_no_faq)}")
    print(f"Errors:                        {len(errors)}")
    print(f"{'='*60}")

    if modified_files:
        print("\nModified files:")
        for f in modified_files:
            print(f"  - {f}")

    if skipped_schema:
        print("\nAlready had FAQPage schema:")
        for f in skipped_schema:
            print(f"  - {f}")


if __name__ == "__main__":
    main()
