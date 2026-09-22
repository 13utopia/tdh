import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = [m.start() for m in re.finditer('treatment-1', html)]
print(f"Total occurrences of 'treatment-1' in index.html: {len(matches)}")

for i, pos in enumerate(matches):
    print(f"\n--- Occurrence {i+1} at index {pos} ---")
    print(html[max(0, pos-200):min(len(html), pos+400)])
