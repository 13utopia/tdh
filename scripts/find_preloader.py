import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=== PRELOADER / OVERLAY SEARCH ===")
preloader_matches = re.findall(r'<div[^>]*class=[\"\'][^\"\']*(?:preloader|loading|overlay)[^\"\']*[\"\'][^>]*>', html, re.IGNORECASE)
print("Preloader divs found:", len(preloader_matches))
for p in preloader_matches:
    print("  ", p)

pos_pre = html.find('preloader')
if pos_pre != -1:
    print("\nSnippet around 'preloader':")
    print(html[max(0, pos_pre-200):min(len(html), pos_pre+500)])
