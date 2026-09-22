import os
import re

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pattern = re.compile(r'(<div[^>]*class="[^"]*(?:elementor-widget-appointment|appointment|booking)[^"]*"[^>]*>.*?</div>\s*</div>\s*</div>)', re.DOTALL | re.IGNORECASE)
matches = pattern.findall(html)

print(f"Found {len(matches)} appointment widget containers")
for idx, m in enumerate(matches[:3]):
    print(f"--- Match {idx+1} ---")
    print(m[:300])
