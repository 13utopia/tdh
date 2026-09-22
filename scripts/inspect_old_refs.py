import re
import os

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

pattern = re.compile(r'[^"\'\s=]+wp-content/uploads/[^"\'\s>]+\.(?:png|jpg|jpeg|gif|webp|svg)', re.IGNORECASE)
matches = pattern.findall(content)

print(f"Found {len(matches)} matches in index.html:")
for m in matches[:10]:
    print(" -", m)
