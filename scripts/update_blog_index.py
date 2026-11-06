"""Render the approved archive, optionally registering explicit reviewed routes.

Usage: python3 scripts/update_blog_index.py --register /blog/approved-article/
Never scans unpublished files or lifts discovery holds.
"""
from blog_archive import register_routes, render
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--register', nargs='+')
    args = parser.parse_args()
    register_routes(args.register) if args.register else render()
