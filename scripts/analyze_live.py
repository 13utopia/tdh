import urllib.request
import re

url = 'https://tanyadentalhouse.in/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8')

with open('e:/tdh/scripts/live_index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Downloaded live HTML ({len(html)} bytes)")

# Search for Skilled Professionals context
pos = html.find('Skilled Professionals')
if pos != -1:
    print("=== Skilled Professionals section in LIVE HTML ===")
    print(html[max(0, pos-800):min(len(html), pos+4000)])

# Also search for images around that section
pos_gallery = html.find('Gallery')
if pos_gallery != -1:
    print("=== Gallery section in LIVE HTML ===")
    print(html[max(0, pos_gallery-500):min(len(html), pos_gallery+4000)])
