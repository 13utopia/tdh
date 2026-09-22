with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos_book = html.find('data-id="c191d1a"')
if pos_book != -1:
    print("=== LIVE BOOKING SECTION c191d1a ===")
    print(html[pos_book:pos_book+4000])
