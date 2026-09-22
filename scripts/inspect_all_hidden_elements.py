import re
import os

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find inline styles with visibility:hidden or display:none
hidden_inline = re.findall(r'<[^>]+style=["\'][^"\']*(?:visibility:\s*hidden|display:\s*none|opacity:\s*0)[^"\']*["\'][^>]*>', html, re.IGNORECASE)
print(f"Found {len(hidden_inline)} elements with inline hidden styles:")
for h in hidden_inline[:15]:
    print(" -", h[:160])
