with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=== VERIFICATION REPORT ===")

# 1. Check feature box backgrounds
feat_bgs = [m for m in ['KMM_4076.webp', 'KMM_4092.webp', 'KMM_4124.webp'] if f"url('{m}')" in html or f'url("{m}")' in html]
print("Feature box background image overrides remaining:", feat_bgs)

# 2. Check treatment-1.webp in Section 7255830
pos_7255 = html.find('data-id="7255830"')
if pos_7255 != -1:
    pos_7255_end = html.find('</section>', pos_7255)
    sec_7255_html = html[pos_7255:pos_7255_end]
    has_chair = 'treatment-1.webp' in sec_7255_html
    print("Section 7255830 (Smile Desktop) has treatment-1.webp:", has_chair)

# 3. Check treatment-1.webp in Section 6b4cda1
pos_6b4 = html.find('data-id="6b4cda1"')
if pos_6b4 != -1:
    pos_6b4_end = html.find('</section>', pos_6b4)
    sec_6b4_html = html[pos_6b4:pos_6b4_end]
    has_chair_mob = 'treatment-1.webp' in sec_6b4_html
    print("Section 6b4cda1 (Smile Mobile) has treatment-1.webp:", has_chair_mob)

# 4. Check Gallery Grid below feature icon boxes
pos_gallery = html.find('Gallery of TDH')
if pos_gallery != -1:
    pos_grid = html.find('tdh-gallery-photo-grid', pos_gallery)
    print("Gallery Grid present after 'Gallery of TDH':", pos_grid != -1)
