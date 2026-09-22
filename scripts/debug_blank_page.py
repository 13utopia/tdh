import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=== CHECKING FOR BLANK PAGE CAUSES ===")

# 1. Check body style or hidden classes on body/main/article
body_match = re.search(r'<body[^>]*>', html)
if body_match:
    print("Body tag:", body_match.group(0))

# 2. Search for any global visibility/display rules in style tags
styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
for i, s in enumerate(styles):
    if 'body' in s or 'display: none' in s or 'visibility: hidden' in s or 'opacity: 0' in s:
        print(f"\nStyle block #{i+1} matching hidden/blank conditions:")
        lines = [line.strip() for line in s.split('\n') if any(k in line for k in ['body', 'display', 'visibility', 'opacity', 'elementor-invisible', 'rs-slide', 'rev_slider'])]
        print('\n'.join(lines[:30]))
