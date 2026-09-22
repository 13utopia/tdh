import re

with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[^>]+class=[\"\'][^\"\']*elementor-top-section[^\"\']*[\"\'][^>]*>', html)
print(f"Total elementor top sections in live HTML: {len(sections)}")

for i, s in enumerate(sections[-5:]):
    pos = html.find(s)
    chunk = html[pos:pos+2500]
    print(f"\n=== LIVE TOP SECTION #{len(sections)-4+i} ===")
    print(s)
    imgs = re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', chunk)
    print("  Images in section:", imgs)
    text_snippet = re.sub(r'<[^>]+>', ' ', chunk)[:200]
    print("  Text snippet:", ' '.join(text_snippet.split()))
