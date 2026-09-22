import os, re

files = ['e:/tdh/index.html', 'e:/tdh/about/index.html', 'e:/tdh/appointment/index.html']

css_inject = '''
<style id="tdh-blank-fix">
/* Disable preloader overlay completely to prevent blank page freeze */
.medizco-preloder, .medizco-preloader, #preloader {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
}

/* Ensure all animated elements are immediately visible */
.elementor-invisible {
    visibility: visible !important;
    opacity: 1 !important;
    animation: none !important;
}

/* Force RevSlider and main containers visible */
#rev_slider_4_1_wrapper, rs-module-wrap, rs-module, rs-slide {
    visibility: visible !important;
    opacity: 1 !important;
    min-height: 450px !important;
}
</style>
'''

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()

        # Remove existing preloader div if present
        html = re.sub(r'<div[^>]*class=[\"\']medizco-preloder[\"\'][^>]*>.*?</div>', '', html, flags=re.DOTALL)

        # Inject fix into <head>
        if 'id="tdh-blank-fix"' not in html:
            html = html.replace('</head>', css_inject + '\n</head>')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Fixed blank page triggers in {fpath}")
