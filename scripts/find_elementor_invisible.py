import re
import os

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

invisible = re.findall(r'<[^>]+class=["\'][^"\']*elementor-invisible[^"\']*["\'][^>]*>', html, re.IGNORECASE)
print(f"Found {len(invisible)} elements with 'elementor-invisible' class:")
for inv in invisible[:15]:
    print(" -", inv[:160])
