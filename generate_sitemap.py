import os
from datetime import datetime
from pathlib import Path

# Find all index.html files
html_files = []
for root, dirs, files in os.walk('.'):
    if 'index.html' in files:
        # Get the path relative to root
        path = os.path.relpath(root, '.')
        if path == '.':
            url_path = '/'
        else:
            url_path = '/' + path.replace('./', '').replace(os.sep, '/') + '/'
        html_files.append(url_path)

# Sort the URLs
html_files.sort()

# Generate sitemap
print('<?xml version="1.0" encoding="UTF-8"?>')
print('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for url_path in html_files:
    print(f'  <url>')
    print(f'    <loc>https://aetaxadvisors.com{url_path}</loc>')
    print(f'    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>')
    print(f'    <changefreq>monthly</changefreq>')
    print(f'  </url>')

print('</urlset>')
