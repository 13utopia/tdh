import re
import os

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

imgs = re.findall(r'<img[^>]*src=["\']([^"\']+)["\'][^>]*>', html, re.IGNORECASE)
print(f"Found {len(imgs)} image tags:")
for img in imgs:
    if 'banner' in img.lower() or 'website-images' in img.lower():
        print("  [IMG SRC]:", img)
