import re

with open('index_raw.html', 'r', encoding='utf-8') as f:
    raw_html = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    curr_html = f.read()

def get_imgs(html, title):
    print(f"=== {title} IMGS & BGS ===")
    # html imgs
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    print(f"HTML Imgs ({len(imgs)}):")
    for img in imgs:
        if not img.endswith('.js') and not img.endswith('.css'):
            print("  -", img)
    # css bgs
    bgs = re.findall(r'background(?:-image)?:\s*url\(["\']?([^"\')]+)["\']?\)', html)
    print(f"Inline CSS BGs ({len(bgs)}):")
    for bg in set(bgs):
        print("  -", bg)
    print()

get_imgs(raw_html, "LIVE INDEX_RAW.HTML")
get_imgs(curr_html, "CURRENT INDEX.HTML")
