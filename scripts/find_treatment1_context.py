with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('data-id="2a9e7df"')
if pos != -1:
    print("=== SURROUNDING SECTIONS OF treatment-1.png (2a9e7df) IN LIVE HTML ===")
    print(html[max(0, pos-2000):min(len(html), pos+2000)])
