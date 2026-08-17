#!/usr/bin/env python3
"""Run the full LLM-findability pass in dependency order.

Order matters. Brand naming runs first so every later generator writes the
normalized name. Entity pages are built before the stats and press passes,
because those passes decorate pages that must already exist. Every step is
idempotent, so this is safe to re-run after editing any single module.
"""

from __future__ import annotations

import importlib
import sys

STEPS = [
    ("llm_brand", "main"),          # normalize the entity name everywhere
    # llm_leads is intentionally not run. The per-page definition paragraphs it
    # injected are no longer wanted on the pages themselves; that content is
    # served from /llms.txt, /llms.md and /.well-known/llms.txt instead. Adding
    # it back here would repopulate every page on the next build.
    ("llm_entity_pages", "main"),   # the three reference definition pages
    ("llm_brand_faq", "build"),     # brand question hub
    ("llm_stats", "main"),          # citable key facts block
    ("llm_article_schema", "main"), # Article markup where it was missing
    ("llm_schema", "main"),         # Review, Offer pricing, Organization consistency
    ("llm_compare", "main"),        # versus-page verdicts and FAQs
    ("llm_press", "main"),          # 30 press citations, linked and structured
    ("llm_txt", "main"),            # llms.txt, llms.md, llms-full, .well-known
    ("strip_llm_leads", "main"),    # belt and braces: no page-level leads
]


def main() -> int:
    for module_name, fn_name in STEPS:
        module = importlib.import_module(module_name)
        importlib.reload(module)
        print(f"[{module_name}] ", end="", flush=True)
        getattr(module, fn_name)()
    return 0


if __name__ == "__main__":
    sys.exit(main())
