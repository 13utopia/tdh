import re
import os

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

matches = re.findall(r'[^"\'\s=]*banner[^"\'\s>]*', html, re.IGNORECASE)
print(f"Found {len(matches)} banner occurrences:")
for m in matches[:10]:
    print(" -", m)
