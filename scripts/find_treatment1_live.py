with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('treatment-1.png')
if pos != -1:
    print("=== LIVE SITE LOCATION OF treatment-1.png ===")
    print(html[max(0, pos-800):min(len(html), pos+1500)])
else:
    print("treatment-1.png not found in live_index.html!")
