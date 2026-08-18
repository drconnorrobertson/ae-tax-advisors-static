#!/usr/bin/env python3
"""Build every topic cluster: pillars, new supporting posts, and backlinks.

Run after editing any cluster_c*.py module. Idempotent.
"""

from __future__ import annotations

import importlib
import sys

import cluster_common as C
import site_template as T

MODULES = [
    "cluster_c1",
    "cluster_c2",
    "cluster_c3",
    "cluster_c4",
    "cluster_c5",
    "cluster_c6",
    "cluster_c7",
    "cluster_c8",
]

MIN_PILLAR_WORDS = 2000


def load() -> list[C.Cluster]:
    clusters = []
    for name in MODULES:
        try:
            mod = importlib.import_module(name)
        except ModuleNotFoundError:
            continue
        importlib.reload(mod)
        clusters.append(mod.CLUSTER)
    return clusters


def main() -> int:
    clusters = load()
    if not clusters:
        print("no cluster modules found")
        return 1

    pillars = new_posts = adopted = 0
    problems: list[str] = []

    for c in clusters:
        # Pillar
        if c.adopted_pillar:
            status = C.inject_hub(c)
            if status in ("missing", "no-main"):
                problems.append(f"{c.slug}: pillar hub {status}")
            else:
                pillars += 1
        else:
            words = C.word_count(c)
            if words < MIN_PILLAR_WORDS:
                problems.append(f"{c.slug}: pillar is {words} words, under {MIN_PILLAR_WORDS}")
            T.write_page(c.href, C.render_pillar(c, clusters))
            pillars += 1

        # Spokes
        for s in c.spokes:
            if s.adopted:
                status = C.inject_backlink(s.slug, c)
                if status in ("missing", "no-main"):
                    problems.append(f"{c.slug} -> /{s.slug}/: {status}")
                else:
                    adopted += 1
            else:
                T.write_page(s.href, C.render_post(s, c))
                new_posts += 1

        # Every cluster needs a real hub of supporting content.
        if len(c.spokes) < 5:
            problems.append(f"{c.slug}: only {len(c.spokes)} spokes, target is 5-8")

    print(f"pillars written : {pillars}")
    print(f"new posts       : {new_posts}")
    print(f"adopted linked  : {adopted}")
    if problems:
        print("\nproblems:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\nall clusters built cleanly")
    return 0


if __name__ == "__main__":
    sys.exit(main())
