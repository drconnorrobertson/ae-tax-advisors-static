#!/usr/bin/env python3
"""Repair meta descriptions that are truncated, duplicated, or too short.

Replacement text is drawn from the page's own opening copy so each description
is unique and actually describes the page. og: and twitter: variants are kept
in sync. Run with --dry to preview.
"""
import html
import re
import sys
from collections import Counter
from pathlib import Path

MIN_LEN, MAX_LEN = 70, 158

# words that read as unfinished if a description ends on them
DANGLING = set("""a an the and or but nor so yet of to in on at by for from with without
into onto upon over under about across through during before after between among
that which who whom whose this these those as if then than when while where why how
is are was were be been being has have had do does did can could may might must
shall should will would your you our their its his her they we it not no more less
such very much many most some any each every other another new same own""".split())

SKIP_SLUG = re.compile(
    r"^(blog-staging/|.*(consultation|zoom|calendar|booking|thank-you|thanks|"
    r"check-in|onboarding|followup|recap|\d+-(minute|day)-)).*"
)


def slug_of(p):
    d = str(p.parent).replace("\\", "/")
    return "" if d == "." else d


def text_of(fragment):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", fragment, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    return re.sub(r"\s+", " ", t).strip()


def is_truncated(d):
    return len(d) >= 155 and not d.rstrip().endswith((".", "!", "?", '"'))


def compose(page_text, h1, fallback):
    """Build a description from the opening prose, cut on a sentence or word."""
    body = page_text
    # drop a leading restatement of the headline
    if h1 and body.lower().startswith(h1.lower()):
        body = body[len(h1):].strip(" .:-")

    if len(body) < 40:
        body = fallback

    if len(body) <= MAX_LEN:
        out = body
    else:
        # prefer a sentence boundary within range
        window = body[:MAX_LEN + 40]
        cuts = [m.end() for m in re.finditer(r"[.!?](?=\s|$)", window)
                if MIN_LEN <= m.end() <= MAX_LEN]
        if cuts:
            out = window[:cuts[-1]]
        else:
            out = body[:MAX_LEN]
            out = out[:out.rfind(" ")]
            # a hard cut usually strands a connector, so shed trailing
            # words that would leave the sentence obviously unfinished
            words = out.rstrip(" ,;:-").split()
            while len(words) > 8 and words[-1].lower().strip(",;:") in DANGLING:
                words.pop()
            out = " ".join(words).rstrip(" ,;:-")
    out = out.strip()
    if out and out[-1] not in ".!?":
        out += "."
    return out


def set_meta(t, name, value, prop=False):
    attr = "property" if prop else "name"
    pat = re.compile(r'(<meta ' + attr + r'="' + re.escape(name) + r'" content=")([^"]*)(">)')
    esc = html.escape(value, quote=True)
    if pat.search(t):
        return pat.sub(lambda m: m.group(1) + esc + m.group(3), t, count=1)
    return t


def main():
    dry = "--dry" in sys.argv
    pages = []
    descs = Counter()

    for p in sorted(Path(".").rglob("index.html")):
        if ".git" in p.parts:
            continue
        s = slug_of(p)
        t = p.read_text(errors="ignore")
        m = re.search(r'<meta name="description" content="([^"]*)"', t)
        d = html.unescape(m.group(1)) if m else ""
        descs[d] += 1
        pages.append((p, s, t, d, bool(m)))

    # Paragraphs repeated across many pages are boilerplate (disclaimers, CTAs)
    # and must never become a description, or we just trade one duplicate for
    # another.
    para_freq = Counter()
    for p, s, t, d, has in pages:
        mm = re.search(r"<main>(.*?)</main>", t, re.S)
        scope = mm.group(1) if mm else t
        for x in re.findall(r"<p[^>]*>(.*?)</p>", scope, re.S):
            para_freq[text_of(x)[:120]] += 1

    fixed = shown = 0
    for p, s, t, d, has in pages:
        if SKIP_SLUG.match(s + "/"):
            continue
        needs = (not has) or is_truncated(d) or len(d) < MIN_LEN or descs[d] > 1
        if not needs:
            continue

        mm = re.search(r"<main>(.*?)</main>", t, re.S)
        scope = mm.group(1) if mm else t
        h1m = re.search(r"<h1[^>]*>(.*?)</h1>", scope, re.S)
        h1 = text_of(h1m.group(1)) if h1m else ""

        paras = [text_of(x) for x in re.findall(r"<p[^>]*>(.*?)</p>", scope, re.S)]
        paras = [x for x in paras
                 if len(x) > 60
                 and "Published" not in x[:20]
                 and para_freq[x[:120]] <= 3]
        lead = paras[0] if paras else ""

        title = ""
        tm = re.search(r"<title>(.*?)</title>", t, re.S)
        if tm:
            title = re.sub(r"\s*\|\s*AE Tax Advisors\s*$", "", text_of(tm.group(1)))

        new = compose(lead, h1, f"{title or h1}: what it is, how it works, and who it applies to")
        if len(new) < MIN_LEN or new == d:
            continue

        if dry and shown < 8:
            print(f"\n/{s}/\n  OLD: {d[:150]}\n  NEW: {new}")
            shown += 1

        if not dry:
            t2 = set_meta(t, "description", new)
            t2 = set_meta(t2, "twitter:description", new)
            t2 = set_meta(t2, "og:description", new, prop=True)
            # keep JSON-LD description aligned where it repeated the old text
            if d and d in t2:
                t2 = t2.replace(f'"description": "{html.escape(d, quote=True)}"',
                                f'"description": "{html.escape(new, quote=True)}"')
            if t2 != t:
                p.write_text(t2)
        fixed += 1

    print(f"\n{'would fix' if dry else 'fixed'} {fixed} meta descriptions")


if __name__ == "__main__":
    main()
