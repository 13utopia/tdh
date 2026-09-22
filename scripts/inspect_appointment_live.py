import urllib.request
import re

url = 'https://tanyadentalhouse.in/appointment/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)
live_app_html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

print("=== LIVE APPOINTMENT PAGE ANALYSIS ===")
headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', live_app_html, re.DOTALL)
for h in headings:
    print("  Heading:", re.sub(r'<[^>]+>', '', h).strip())

imgs = re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', live_app_html)
print("\nImages in live appointment page:", list(set(imgs)))

with open('e:/tdh/appointment/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    local_app_html = f.read()

print("\n=== LOCAL APPOINTMENT PAGE ANALYSIS ===")
local_headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', local_app_html, re.DOTALL)
for h in local_headings:
    print("  Local Heading:", re.sub(r'<[^>]+>', '', h).strip())
