with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Gallery of TDH')
if pos != -1:
    pos_start = html.rfind('<section', 0, pos)
    # find end of section
    pos_end = html.find('</section>', html.find('tdh-gallery-photo-grid', pos))
    if pos_end != -1:
        print("=== LOCAL GALLERY SECTION HTML ===")
        print(html[pos_start:pos_end+10])
    else:
        print("pos_end not found, snippet:")
        print(html[pos_start:pos+3000])
