import re

with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos_recip = html.find('Service Recipient Says')
if pos_recip != -1:
    print("=== LIVE HTML CONTENT AFTER 'Service Recipient Says' ===")
    chunk = html[pos_recip:]
    print(chunk[:10000])

    # Find all image tags in this chunk
    imgs = re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', chunk)
    print("\nImages after Service Recipient Says in live HTML:", imgs)
