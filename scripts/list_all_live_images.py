import re

with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=== ALL IMAGES IN LIVE HTML ===")
imgs = re.findall(r'<img[^>]+>', html)
for i, img in enumerate(imgs):
    print(f"{i+1}: {img}\n")

print("=== ALL BACKGROUND IMAGES IN LIVE HTML ===")
bgs = re.findall(r'url\([^\)]+\)', html)
for bg in set(bgs):
    print(bg)
