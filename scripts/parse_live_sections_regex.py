import re

with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find elementor top sections
top_sec_matches = re.findall(r'<section[^>]+class=[\"\'][^\"\']*elementor-top-section[^\"\']*[\"\'][^>]*>', html)

print(f"Found {len(top_sec_matches)} top sections:")
for i, m in enumerate(top_sec_matches):
    data_id = re.search(r'data-id=[\"\']([^\"\']+)[\"\']', m)
    sec_id = data_id.group(1) if data_id else 'unknown'
    print(f"\nTop Section {i+1} (data-id={sec_id}):")
    # find where this tag starts
    pos = html.find(m)
    end_pos = min(len(html), pos + 1500)
    chunk = html[pos:end_pos]
    # extract headings or text snippet
    text_clean = re.sub(r'<[^>]+>', ' ', chunk)
    text_clean = ' '.join(text_clean.split())[:150]
    print(f"  Snippet: {text_clean}")
    # extract images
    imgs = re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', chunk)
    print(f"  Images in chunk: {imgs}")
