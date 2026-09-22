import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = [m.start() for m in re.finditer('Smile with Confidence', html)]
print(f"Total matches for 'Smile with Confidence': {len(matches)}")
for idx, pos in enumerate(matches):
    sec_start = html.rfind('<section', 0, pos)
    sec_end = html.find('</section>', pos)
    sec_tag = html[sec_start:html.find('>', sec_start)+1]
    print(f"\nMatch {idx+1} (pos {pos}):")
    print(f"  Section tag: {sec_tag}")
