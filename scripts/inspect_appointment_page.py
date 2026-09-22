import os
import re

with open(os.path.join('e:\\tdh', 'appointment', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

forms = re.findall(r'<form[^>]*>.*?</form>', html, re.DOTALL | re.IGNORECASE)
print(f"Found {len(forms)} forms in appointment/index.html")
for idx, fm in enumerate(forms[:3]):
    print(f"--- Form {idx+1} ---")
    print(fm[:200])
