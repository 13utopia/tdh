import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original index.html size:", len(html))

# 1. Remove tdh-dental-chair-oval-container blocks
html_clean = re.sub(r'<div\s+class=[\"\']tdh-dental-chair-oval-container[\"\'].*?</div>\s*</div>', '</div>', html, flags=re.DOTALL)
html_clean = re.sub(r'<div\s+class=[\"\']tdh-dental-chair-oval-container[\"\'].*?</div>', '', html_clean, flags=re.DOTALL)

# 2. Clean column cb87659 in section 7255830 (remove forced treatment-1.webp from smile section)
pos_cb87659 = html_clean.find('data-id="cb87659"')
if pos_cb87659 != -1:
    pos_wrap = html_clean.find('<div class="elementor-widget-wrap"', pos_cb87659)
    if pos_wrap != -1 and pos_wrap < pos_cb87659 + 300:
        pos_wrap_end = html_clean.find('</div>', pos_wrap)
        # Restore empty elementor-widget-wrap as in live HTML
        html_clean = html_clean[:pos_wrap] + '<div class="elementor-widget-wrap"></div>' + html_clean[pos_wrap_end+6:]

with open('e:/tdh/index.html', 'w', encoding='utf-8') as f:
    f.write(html_clean)

print("Updated index.html size:", len(html_clean))
