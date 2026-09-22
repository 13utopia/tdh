import os
import re

with open(os.path.join('e:\\tdh', 'index_raw.html'), 'r', encoding='utf-8', errors='ignore') as f:
    raw_html = f.read()

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    curr_html = f.read()

raw_sections = re.findall(r'<section[^>]*class=["\']([^"\']+)["\'][^>]*data-id=["\']([^"\']+)["\']', raw_html, re.IGNORECASE)
curr_sections = re.findall(r'<section[^>]*class=["\']([^"\']+)["\'][^>]*data-id=["\']([^"\']+)["\']', curr_html, re.IGNORECASE)

print(f"Raw HTML sections count: {len(raw_sections)}")
for cls, sid in raw_sections:
    print(f"  Section ID: {sid} | Classes: {cls[:80]}")

print(f"\nCurrent HTML sections count: {len(curr_sections)}")
for cls, sid in curr_sections:
    print(f"  Section ID: {sid} | Classes: {cls[:80]}")
