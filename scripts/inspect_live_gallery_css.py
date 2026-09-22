import re

with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Gallery of TDH')
if pos != -1:
    chunk = html[pos:pos+12000]
    
    # Extract elementor data-ids and style attributes
    elements = re.findall(r'<div[^>]+data-id=[\"\']([^\"\']+)[\"\'][^>]*>', chunk)
    print("Elementor IDs under Gallery of TDH in live HTML:", elements)
    
    # Find all style tags or classes in live HTML for these IDs
    for el_id in list(set(elements))[:10]:
        css_matches = re.findall(r'\.elementor-element-' + el_id + r'[^\{]*\{[^\}]*\}', html)
        print(f"\nCSS rules for element {el_id}:")
        for c in css_matches:
            print(" ", c)
