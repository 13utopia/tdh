import os
import re

with open(os.path.join('e:\\tdh', 'index_raw.html'), 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

pos = raw.find('7255830')
if pos != -1:
    cols = re.findall(r'<div[^>]+class=["\'][^"\']*elementor-column[^"\']*["\'][^>]*>', raw[pos:pos+15000])
    print(f"Found {len(cols)} columns in section 7255830:")
    for c in cols:
        print(" -", c)
