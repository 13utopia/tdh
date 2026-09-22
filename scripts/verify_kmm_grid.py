import os
import re

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

kmm_matches = re.findall(r'website-images/KMM_[0-9]+\.webp', html, re.IGNORECASE)
print(f"Found {len(kmm_matches)} KMM photo matches in index.html:")
for k in kmm_matches:
    print(" -", k)
