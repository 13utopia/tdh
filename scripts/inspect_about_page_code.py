with open('e:/tdh/about/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Dedicated to Your Dental Health')
if pos != -1:
    pos_sec_start = html.rfind('<section', 0, pos)
    pos_sec_end = html.find('</section>', pos)
    print("=== LOCAL ABOUT PAGE SECTION HTML ===")
    print(html[pos_sec_start:pos_sec_end+10])
