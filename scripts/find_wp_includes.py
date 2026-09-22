import re
import os

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

matches = re.findall(r'src=["\']([^"\']*wp-includes[^"\']*)["\']', html, re.IGNORECASE)
print(f"Found {len(matches)} wp-includes script tags:")
for m in matches:
    print(" -", m)
