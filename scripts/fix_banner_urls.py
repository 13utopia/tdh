import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def clean_urls():
    html_files = [
        ("index.html", False),
        (os.path.join("about", "index.html"), True),
        (os.path.join("appointment", "index.html"), True)
    ]
    
    for rel_path, is_subdir in html_files:
        full_path = os.path.join(ROOT_DIR, rel_path)
        if not os.path.exists(full_path):
            continue
            
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        img_prefix = "../website-images/" if is_subdir else "website-images/"
        
        # Clean up corrupted prefixes like //tanyadentalhouse.inwebsite-images/
        content = re.sub(
            r'(?:https?:)?//tanyadentalhouse\.in(?:/)?website-images/',
            img_prefix,
            content,
            flags=re.IGNORECASE
        )
        
        # Also clean up any unescaped wp-content/uploads/ references
        content = re.sub(
            r'(?:https?:)?//tanyadentalhouse\.in(?:/)?wp-content/uploads/[^"\'\s,\)\\]*?/([^"\'\s,\)\\]+?\.(?:png|jpg|jpeg|gif|webp|svg))',
            rf'{img_prefix}\1',
            content,
            flags=re.IGNORECASE
        )
        
        # Convert any .jpg/.png to .webp in website-images references
        def webp_sub(m):
            fname = m.group(1)
            ext = os.path.splitext(fname)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png']:
                return f"{img_prefix}{os.path.splitext(fname)[0]}.webp"
            return m.group(0)
            
        content = re.sub(rf'{img_prefix}([^"\'\s,\)\\]+)', webp_sub, content)
        
        # Add explicit background image CSS for section banners
        hero_banner_css = f"""
<style>
.elementor-element-c0b8969, .elementor-element-31518f8, .elementor-section-height-min-height {{
    background-image: url("{img_prefix}Banner-scaled.webp") !important;
    background-size: cover !important;
    background-position: center center !important;
}}
</style>
"""
        if hero_banner_css not in content and '</head>' in content:
            content = content.replace('</head>', f'{hero_banner_css}</head>')

        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Cleaned URLs in {full_path}")

if __name__ == "__main__":
    clean_urls()
