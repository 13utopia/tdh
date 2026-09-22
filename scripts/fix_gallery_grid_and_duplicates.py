import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RESPONSIVE_DISPLAY_CSS = """
<!-- Elementor Responsive Display Rules to Remove Duplicates -->
<style>
@media (min-width: 1025px) {
    .elementor-hidden-desktop {
        display: none !important;
    }
}
@media (max-width: 1024px) {
    .elementor-hidden-tablet, .elementor-hidden-phone {
        display: none !important;
    }
}
.tdh-gallery-photo-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 30px;
}
@media (max-width: 768px) {
    .tdh-gallery-photo-grid {
        grid-template-columns: repeat(1, 1fr);
    }
}
.tdh-gallery-item {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    height: 240px;
    border: 1px solid #e2e8f0;
}
.tdh-gallery-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
}
.tdh-gallery-item:hover img {
    transform: scale(1.05);
}
</style>
"""

GALLERY_PHOTO_GRID_HTML = """
<!-- Gallery Photo Grid -->
<div class="tdh-gallery-photo-grid">
    <div class="tdh-gallery-item"><img src="website-images/4-1.webp" alt="TDH Clinic Interior" /></div>
    <div class="tdh-gallery-item"><img src="website-images/2-1.webp" alt="TDH Dental Surgery Suite" /></div>
    <div class="tdh-gallery-item"><img src="website-images/3-1.webp" alt="TDH Treatment Room" /></div>
    <div class="tdh-gallery-item"><img src="website-images/Untitled-design-34-1.webp" alt="TDH Advanced Dental Equipment" /></div>
    <div class="tdh-gallery-item"><img src="website-images/Untitled-design-35.webp" alt="TDH Patient Lounge" /></div>
    <div class="tdh-gallery-item"><img src="website-images/Untitled-design-36.webp" alt="TDH Dental Care Practice" /></div>
</div>
"""

def fix_gallery_and_duplicates():
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
        grid_html = GALLERY_PHOTO_GRID_HTML.replace("website-images/", img_prefix)
        
        # 1. Inject Responsive Display CSS
        if RESPONSIVE_DISPLAY_CSS not in content and '</head>' in content:
            content = content.replace('</head>', f'{RESPONSIVE_DISPLAY_CSS}\n</head>')
            
        # 2. Add Gallery Photo Grid under Gallery of TDH features in index.html
        if rel_path == "index.html":
            pos_icon = content.find('Comfortable Environment')
            if pos_icon != -1 and 'tdh-gallery-photo-grid' not in content:
                # Insert grid after comfortable environment section wrapper
                insert_pos = content.find('</section>', pos_icon)
                if insert_pos != -1:
                    insert_pos = content.find('</section>', insert_pos + 10)
                    content = content[:insert_pos] + f'\n<div class="elementor-container">{grid_html}</div>\n' + content[insert_pos:]
                    print("Inserted photo grid into index.html under Gallery of TDH")

        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Fixed responsive duplicates for {full_path}")

if __name__ == "__main__":
    fix_gallery_and_duplicates()
