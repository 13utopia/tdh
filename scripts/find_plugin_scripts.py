import re
import os

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\'][^>]*>', html, re.IGNORECASE)
print(f"Found {len(scripts)} external script tags:")
for s in scripts:
    if 'appointment' in s.lower() or 'fbuilder' in s.lower() or 'metform' in s.lower():
        print("  [PLUGIN JS]:", s)
