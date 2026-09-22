import os

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pos = html.find('cp_appbooking')
if pos != -1:
    print("Found cp_appbooking at pos", pos)
    start = max(0, pos - 200)
    end = min(len(html), pos + 800)
    print(html[start:end])
else:
    print("cp_appbooking not found")
