import re

with open('e:/tdh/about/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=== IMAGES IN ABOUT PAGE ===")
imgs = re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', html)
for i in set(imgs):
    print(" ", i)

print("\n=== SEARCH FOR JUNK WRAPPERS IN ABOUT PAGE ===")
junk = re.findall(r'gizmo|conversation-turn|text-token-text-primary', html)
print("Junk classes found:", len(junk))
