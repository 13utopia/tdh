import os
import re

with open(os.path.join('e:\\tdh', 'index_raw.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find data-settings attributes
data_settings = re.findall(r'data-settings=["\']([^"\']+)["\']', html)
print(f"Found {len(data_settings)} data-settings attributes")
for ds in data_settings:
    if 'banner' in ds.lower() or 'image' in ds.lower() or 'bg' in ds.lower():
        print("Data Setting:", ds[:300])

# Find inline styles with background-image
bg_styles = re.findall(r'style=["\'][^"\']*background-image:[^"\']*["\']', html)
print(f"\nFound {len(bg_styles)} inline background-image styles:")
for bg in bg_styles[:10]:
    print("Style:", bg)
