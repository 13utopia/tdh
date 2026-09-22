import re

with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos13 = html.find('data-id="6b4cda1"')
pos14 = html.find('data-id="7255830"')
pos15 = html.find('data-id="76dcae4"')

print("=== LIVE SECTION 13 (6b4cda1) ===")
if pos13 != -1:
    print(html[pos13:pos14 if pos14 != -1 else pos13+3000])

print("\n=== LIVE SECTION 14 (7255830) ===")
if pos14 != -1:
    print(html[pos14:pos15 if pos15 != -1 else pos14+3000])
