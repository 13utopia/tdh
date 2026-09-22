import urllib.request
import re

url = 'https://tanyadentalhouse.in/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

pos_recip = html.find('Service Recipient Says')
print("=== LIVE HOMEPAGE BOTTOM SECTIONS ===")
if pos_recip != -1:
    print(html[pos_recip-500:min(len(html), pos_recip+8000)])

# Find all images in bottom half of live homepage
pos_half = len(html) // 2
bottom_imgs = re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', html[pos_half:])
print("\n=== ALL IMAGES IN BOTTOM HALF OF LIVE HOMEPAGE ===")
for img in set(bottom_imgs):
    print("  -", img)
