import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original index.html length:", len(html))

# 1. Remove Style block 14 (the Feature Box background CSS)
pattern_style14 = r'/\* Feature Box 1: Skilled Professionals \*/.*?\*/\s*}'
# Or match from /* Feature Box 1: Skilled Professionals */ to the closing </style>
pos_feat_style = html.find('/* Feature Box 1: Skilled Professionals */')
if pos_feat_style != -1:
    pos_style_end = html.find('</style>', pos_feat_style)
    if pos_style_end != -1:
        print("Removing custom feature box background style block...")
        html = html[:pos_feat_style] + html[pos_style_end+8:]

# 2. Fix Section 7255830 (Smile with Confidence Desktop)
# First remove casino spam text if present
spam_start = html.find('<h4>4. Risk Control and Budget Management</h4>')
if spam_start != -1:
    spam_end = html.find('</div>', html.find('<h3>Conclusion</h3>', spam_start))
    if spam_end != -1:
        print("Removing spam text inside section 7255830...")
        html = html[:spam_start] + html[spam_end:]

# Next, populate column cb87659 in section 7255830 with treatment-1.webp
pos_cb87659 = html.find('data-id="cb87659"')
if pos_cb87659 != -1:
    # Find <div class="elementor-widget-wrap"> right after pos_cb87659
    pos_wrap = html.find('<div class="elementor-widget-wrap">', pos_cb87659)
    if pos_wrap != -1 and pos_wrap < pos_cb87659 + 300:
        pos_wrap_end = html.find('</div>', pos_wrap)
        img_html = '''<div class="elementor-widget-wrap" style="display: flex; align-items: center; justify-content: center; height: 100%; min-height: 380px; padding: 20px;">
    <img src="website-images/treatment-1.webp" alt="TDH Dental Surgery Chair & Clinic Facility" style="width: 100%; max-width: 520px; height: auto; border-radius: 50% 50% 50% 50% / 40% 40% 40% 40%; box-shadow: 0 12px 30px rgba(0,0,0,0.12); border: 4px solid #ffffff;" />
</div>'''
        html = html[:pos_wrap] + img_html + html[pos_wrap_end+6:]
        print("Inserted treatment-1.webp into column cb87659 in section 7255830!")

# Also check mobile section 6b4cda1 / column 2dc7936
pos_2dc7936 = html.find('data-id="2dc7936"')
if pos_2dc7936 != -1:
    pos_wrap2 = html.find('<div class="elementor-widget-wrap', pos_2dc7936)
    if pos_wrap2 != -1 and pos_wrap2 < pos_2dc7936 + 300:
        # Check if treatment-1.webp is already inside pos_wrap2
        chunk_check = html[pos_2dc7936:pos_2dc7936+1000]
        if 'treatment-1.webp' not in chunk_check:
            pos_wrap2_close = html.find('</div>', pos_wrap2)
            img_html_mob = '''
<div class="tdh-dental-chair-oval-container" style="text-align: center; padding: 15px;">
    <img src="website-images/treatment-1.webp" alt="TDH Dental Surgery Chair & Clinic Facility" style="width: 100%; max-width: 500px; height: auto; border-radius: 50% 50% 50% 50% / 40% 40% 40% 40%; box-shadow: 0 12px 30px rgba(0,0,0,0.12); border: 4px solid #ffffff;" />
</div>
'''
            html = html[:pos_wrap2_close] + img_html_mob + html[pos_wrap2_close:]
            print("Inserted treatment-1.webp into column 2dc7936 for mobile section!")

with open('e:/tdh/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html length:", len(html))
