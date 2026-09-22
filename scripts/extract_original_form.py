import os
import re

with open(os.path.join('e:\\tdh', 'index_raw.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Locate elementor shortcode section around cp_appbooking
pattern = re.compile(r'(<div[^>]*class="[^"]*elementor-widget-shortcode[^"]*"[^>]*>.*?)(?:</form>\s*</div>\s*</div>\s*</div>)', re.DOTALL | re.IGNORECASE)
m = pattern.search(html)

if m:
    print("Found elementor shortcode container:")
    print(m.group(0)[:500])
else:
    print("Not found by regex")
