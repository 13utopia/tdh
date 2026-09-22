import urllib.request
import re

url = 'https://tanyadentalhouse.in/about/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)
live_about_html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

pos = live_about_html.find('Our Tooth Gallery')
if pos != -1:
    print("=== LIVE ABOUT PAGE - OUR TOOTH GALLERY ===")
    print(live_about_html[pos-200:pos+3000])

with open('e:/tdh/about/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    local_about_html = f.read()

pos_loc = local_about_html.find('Our Tooth Gallery')
if pos_loc != -1:
    print("\n=== LOCAL ABOUT PAGE - OUR TOOTH GALLERY ===")
    print(local_about_html[pos_loc-200:pos_loc+3000])
