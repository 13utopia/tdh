import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VISIBILITY_CSS_OVERRIDE = """
<!-- Global Visibility Override for Elementor & RevSlider -->
<style>
.elementor-invisible {
    visibility: visible !important;
    opacity: 1 !important;
    transform: none !important;
    animation: none !important;
}
#rev_slider_4_1_wrapper, #rev_slider_4_1, rs-module-wrap, rs-module, rs-slides, rs-slide {
    visibility: visible !important;
    opacity: 1 !important;
    min-height: 500px;
}
rs-slide img, .rev-slidebg {
    opacity: 1 !important;
    visibility: visible !important;
}
</style>
"""

def fix_all_visibility():
    html_files = [
        "index.html",
        os.path.join("about", "index.html"),
        os.path.join("appointment", "index.html")
    ]
    
    for rel_path in html_files:
        full_path = os.path.join(ROOT_DIR, rel_path)
        if not os.path.exists(full_path):
            continue
            
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # 1. Remove style="visibility:hidden;..." from rs-module-wrap
        content = re.sub(
            r'(<rs-module-wrap[^>]*style=["\'])visibility:\s*hidden;?',
            r'\1visibility:visible;',
            content,
            flags=re.IGNORECASE
        )
        
        # 2. Remove elementor-invisible class from all tags
        content = re.sub(
            r'class=["\']([^"\']*)\belementor-invisible\b([^"\']*)["\']',
            r'class="\1\2"',
            content,
            flags=re.IGNORECASE
        )
        # Clean double spaces in class names
        content = re.sub(r'class=" +', 'class="', content)
        content = re.sub(r' +class=', ' class=', content)

        # 3. Inject CSS Override in head
        if VISIBILITY_CSS_OVERRIDE not in content and '</head>' in content:
            content = content.replace('</head>', f'{VISIBILITY_CSS_OVERRIDE}\n</head>')

        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Fixed visibility for {full_path}")

if __name__ == "__main__":
    fix_all_visibility()
