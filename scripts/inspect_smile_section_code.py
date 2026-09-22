with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

matches = [m.start() for m in re.finditer('Smile with Confidence', html)]
print(f"Total matches for 'Smile with Confidence' in index.html: {len(matches)}")

for i, pos in enumerate(matches):
    sec_start = html.rfind('<section', 0, pos)
    sec_end = html.find('</section>', pos)
    print(f"\n=== MATCH {i+1} at index {pos} ===")
    print(html[sec_start:sec_end+10])
