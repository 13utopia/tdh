import re

with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Gallery of TDH')
if pos != -1:
    sub = html[pos:pos+15000]
    print("=== LIVE HTML CONTENT AFTER 'Gallery of TDH' ===")
    
    # Find all images in this block
    img_matches = re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', sub)
    print("Images found after Gallery of TDH in live HTML:", img_matches)
    
    # Also find background-image styles in this block
    bg_matches = re.findall(r'style=[\"\'][^\"\']*background[^\"\']*[\"\']', sub)
    print("Background styles:", bg_matches)

    # Print out sections/widgets in this block
    widgets = re.findall(r'widget_type=[\"\']([^\"\']+)[\"\']', sub)
    print("Widget types:", list(set(widgets)))

    # Also search for KMM images or gallery images anywhere in live HTML
    all_imgs = re.findall(r'src=[\"\']([^\"\']*(?:KMM|gallery|treatment|uploads)[^\"\']*)[\"\']', html)
    print("\nAll KMM / treatment / uploads images in live HTML:", all_imgs)
