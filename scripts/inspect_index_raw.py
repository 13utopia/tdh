import re

with open('index_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('wp-content/uploads/elementor/css/post-2.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's list all sections with data-id
sections = re.findall(r'<section[^>]*data-id="([^"]+)"[^>]*>', html)
print(f"Total sections with data-id: {len(sections)}")

for sid in set(sections):
    # Find background image in post-2.css
    bgs = re.findall(r'\.elementor-element-' + sid + r'[^{]*\{[^}]*background-image:\s*url\(["\']?([^"\')]+)["\']?\)', css)
    padds = re.findall(r'\.elementor-element-' + sid + r'[^{]*\{[^}]*padding:\s*([^;\}]+)', css)
    if bgs or padds:
        print(f"Section {sid}:")
        if bgs: print(f"  BG: {bgs}")
        if padds: print(f"  Padding: {padds}")
