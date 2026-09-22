import re
import os

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pattern = re.compile(r'<section[^>]*class="[^"]*elementor-element-([a-zA-Z0-9]+)[^"]*"[^>]*data-settings=["\']([^"\']+)["\']', re.IGNORECASE)
matches = pattern.findall(html)

print(f"Found {len(matches)} sections with data-settings:")
for el_id, ds in matches:
    if 'banner' in ds.lower() or 'image' in ds.lower() or 'url' in ds.lower() or 'classic' in ds.lower():
        print(f"Section {el_id}: {ds[:150]}")
