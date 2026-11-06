"""Validate the complete approved archive instead of pruning a page-local subset.

Resolve withdrawn or redirected articles explicitly in scripts/blog-catalog.json,
then rerender. A broken link must not silently delete approved discovery.
"""
from pathlib import Path
import subprocess, sys
if __name__ == '__main__':
    subprocess.run([sys.executable, str(Path(__file__).with_name('check-blog-archive.py'))], check=True)
