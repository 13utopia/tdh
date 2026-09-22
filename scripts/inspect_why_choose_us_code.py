with open('e:/tdh/about/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Why Choose Us?')
if pos != -1:
    pos_sec_start = html.rfind('<section', 0, pos)
    pos_sec_end = html.find('</section>', html.find('Emergency Care', pos)) + 10
    print("=== LOCAL WHY CHOOSE US SECTION HTML ===")
    print(html[pos_sec_start:pos_sec_end+100])
else:
    print("Why Choose Us? not found in about/index.html!")
