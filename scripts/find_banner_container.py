import os

with open(os.path.join('e:\\tdh', 'index_raw.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pos = html.find('Banner-scaled')
while pos != -1:
    print(f"Found Banner-scaled at pos {pos}:")
    start = max(0, pos - 200)
    end = min(len(html), pos + 400)
    print(html[start:end])
    print("=" * 50)
    pos = html.find('Banner-scaled', pos + 1)
