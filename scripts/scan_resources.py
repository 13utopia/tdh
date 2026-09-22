import re
import urllib.request

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script[^>]+src=[\"\']([^\"\']+)[\"\']', html)
print(f"Total external scripts: {len(scripts)}")
for s in scripts:
    print("SCRIPT:", s)

links = re.findall(r'<link[^>]+href=[\"\']([^\"\']+)[\"\']', html)
print(f"\nTotal external links: {len(links)}")
for l in links:
    if 'css' in l or 'js' in l:
        print("LINK:", l)
