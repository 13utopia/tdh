with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('rev_slider')
if pos != -1:
    pos_sec_start = html.rfind('<section', 0, pos)
    pos_sec_end = html.find('</section>', pos) + 10
    print("=== LOCAL BANNER SECTION HTML ===")
    print(html[pos_sec_start:pos_sec_end])
else:
    print("rev_slider not found in index.html!")
