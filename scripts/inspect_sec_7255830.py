with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('data-id="7255830"')
if pos != -1:
    pos_end = html.find('</section>', pos)
    print("=== DESKTOP SECTION 7255830 IN LOCAL INDEX.HTML ===")
    print(html[pos:pos_end+10])
