import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Smile with Confidence')
if pos != -1:
    print("=== LOCAL INDEX.HTML - Smile with Confidence Section ===")
    print(html[max(0, pos-300):min(len(html), pos+3000)])
