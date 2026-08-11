"""Replace double hyphens used as dashes in visible prose with em dashes.

Only touches text nodes inside <main>, leaving tags, attributes, comments,
inline scripts, and styles untouched. Hyphenated compounds and HTML comment
delimiters are left alone.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Text between tags, excluding comment/script/style bodies handled separately.
TEXT_NODE = re.compile(r">([^<]+)<")
SKIP_BLOCK = re.compile(r"<(script|style)\b.*?</\1>|<!--.*?-->", re.S | re.I)

# " -- " and "word--word" used as a dash. Requires a non-hyphen on each side
# so "--" inside a longer run of hyphens (a rule, a comment marker) is skipped.
DASH = re.compile(r"(?<!-)--(?!-)")


def fix_text(text):
    if "--" not in text:
        return text, 0
    fixed, n = DASH.subn("&mdash;", text)
    # Collapse the spaces an em dash does not need.
    fixed = re.sub(r" +&mdash; +", "&mdash;", fixed)
    return fixed, n


def process(src):
    if "<main>" not in src or "</main>" not in src:
        return src, 0

    start = src.index("<main>")
    end = src.index("</main>")
    head, main, tail = src[:start], src[start:end], src[end:]

    # Protect script/style/comment blocks by stashing them.
    stash = []

    def hide(m):
        stash.append(m.group(0))
        return f"\x00{len(stash) - 1}\x00"

    main = SKIP_BLOCK.sub(hide, main)

    count = 0

    def repl(m):
        nonlocal count
        fixed, n = fix_text(m.group(1))
        count += n
        return ">" + fixed + "<"

    main = TEXT_NODE.sub(repl, main)
    main = re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], main)

    return head + main + tail, count


def main():
    files = changed = total = 0
    for root, dirs, names in os.walk(ROOT):
        if ".git" in root or root.endswith("scripts"):
            continue
        for name in names:
            if name != "index.html":
                continue
            path = os.path.join(root, name)
            src = open(path, errors="ignore").read()
            out, n = process(src)
            files += 1
            if n:
                open(path, "w").write(out)
                changed += 1
                total += n
    print(f"scanned {files} pages")
    print(f"{total} double hyphens replaced across {changed} pages")


if __name__ == "__main__":
    main()
