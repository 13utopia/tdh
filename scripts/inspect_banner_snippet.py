with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('rev_slider')
if pos != -1:
    print("=== SNIPPET AROUND REV_SLIDER ===")
    print(html[max(0, pos-300):min(len(html), pos+2000)])
