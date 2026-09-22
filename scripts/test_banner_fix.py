import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROBUST_BANNER_CSS = """
<!-- Robust Hero Banner Fix CSS -->
<style>
#rev_slider_4_1_wrapper, 
.elementor-widget-slider_revolution,
#rev_slider_4_1,
rs-module-wrap,
rs-module {
    height: 550px !important;
    min-height: 550px !important;
    max-height: 700px !important;
    width: 100% !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    position: relative !important;
    overflow: hidden !important;
}

rs-slides {
    height: 100% !important;
    width: 100% !important;
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    visibility: visible !important;
    opacity: 1 !important;
    display: block !important;
}

rs-slide {
    height: 100% !important;
    width: 100% !important;
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    visibility: visible !important;
    opacity: 1 !important;
    display: block !important;
}

rs-slide img, .rev-slidebg, img.rs-lazyload {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    opacity: 1 !important;
    visibility: visible !important;
    display: block !important;
}

rs-layer {
    opacity: 1 !important;
    visibility: visible !important;
}
</style>
"""

def apply_banner_fix():
    html_files = ["index.html", os.path.join("about", "index.html"), os.path.join("appointment", "index.html")]
    
    for rel_path in html_files:
        full_path = os.path.join(ROOT_DIR, rel_path)
        if not os.path.exists(full_path):
            continue
            
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        if ROBUST_BANNER_CSS not in content and '</head>' in content:
            content = content.replace('</head>', f'{ROBUST_BANNER_CSS}\n</head>')
            
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Applied robust banner CSS to {full_path}")

if __name__ == "__main__":
    apply_banner_fix()
