import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Smile with Confidence')
if pos != -1:
    pos_sec_start = html.rfind('<section', 0, pos)
    pos_sec_end = html.find('</section>', pos)
    print("=== LOCAL INDEX.HTML SMILE WITH CONFIDENCE SECTION ===")
    print(html[pos_sec_start:pos_sec_end+10])
