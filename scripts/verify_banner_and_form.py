import os
import re

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

rev_imgs = re.findall(r'<img[^>]*class="[^"]*rev-slidebg[^"]*"[^>]*>', html, re.IGNORECASE)
print(f"Found {len(rev_imgs)} RevSlider background image tags:")
for img in rev_imgs:
    print(" -", img)

has_form = 'id="tdh-appointment-card"' in html
print(f"\nSimple Appointment Card present in index.html: {has_form}")
