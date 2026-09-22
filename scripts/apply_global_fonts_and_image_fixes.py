import re, os

files = [
    ('e:/tdh/index.html', ''),
    ('e:/tdh/about/index.html', '../'),
    ('e:/tdh/appointment/index.html', '../')
]

google_fonts_html = '''
<!-- Official Google Fonts Import for Live Site Accuracy: Roboto & Exo -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Exo:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;0,900;1,400;1,700&display=swap" rel="stylesheet">
'''

global_font_css = '''
<style id="tdh-global-typography">
/* Global Pixel-Perfect Typography Rules Matching https://tanyadentalhouse.in/ */
body, p, span, li, a, input, select, textarea, label {
    font-family: 'Roboto', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
}

h1, h2, h3, h4, h5, h6, 
.ekit-heading--title, 
.elementskit-section-title, 
.elementskit-info-box-title, 
.elementor-heading-title,
.elementskit-btn,
.ekit-btn {
    font-family: 'Roboto', 'Exo', sans-serif !important;
}

.sub-title, .tel_num, .elementskit-info-box-title {
    font-family: 'Exo', 'Roboto', sans-serif !important;
}
</style>
'''

for fpath, rel_prefix in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        # 1. Inject Google Fonts link if missing
        if 'fonts.googleapis.com/css2?family=Exo' not in html:
            html = html.replace('</head>', google_fonts_html + '\n</head>')

        # 2. Inject global font CSS if missing
        if 'id="tdh-global-typography"' not in html:
            html = html.replace('</head>', global_font_css + '\n</head>')

        # 3. Clean placeholder images
        html = html.replace(f'{rel_prefix}website-images/Untitled-design-32.webp', f'{rel_prefix}website-images/logo-1-1024x367.webp')
        html = html.replace('website-images/Untitled-design-32.webp', f'{rel_prefix}website-images/logo-1-1024x367.webp')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"Applied typography and image fixes to {fpath}")
