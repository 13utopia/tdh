import os

with open(os.path.join('e:\\tdh', 'index_raw.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pos = html.find('cp_appbooking')
if pos != -1:
    start = max(0, pos - 500)
    end = min(len(html), pos + 1500)
    print("--- Original Raw Booking Section ---")
    print(html[start:end])
