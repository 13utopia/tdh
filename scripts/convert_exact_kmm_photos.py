import os
from PIL import Image

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOADS_2023_12 = os.path.join(ROOT_DIR, "wp-content", "uploads", "2023", "12")
WEBSITE_IMAGES_DIR = os.path.join(ROOT_DIR, "website-images")

# List of exact 6 gallery photos from user screenshot
KMM_FILES = [
    "KMM_4076.jpg", # 1. Doctors operating on patient
    "KMM_4092.jpg", # 2. Stay Flossy TDH wall sign
    "KMM_4124.jpg", # 3. Consultation desk with blue chairs
    "KMM_4142.jpg", # 4. 3D CBCT intraoral scanner scan
    "KMM_4034.jpg", # 5. Operating room with blue dental chairs
    "KMM_4190.jpg"  # 6. Doctor consultation session
]

def convert_kmm_images():
    for f_name in KMM_FILES:
        src_path = os.path.join(UPLOADS_2023_12, f_name)
        out_name = f"{os.path.splitext(f_name)[0]}.webp"
        out_path = os.path.join(WEBSITE_IMAGES_DIR, out_name)
        
        if os.path.exists(src_path):
            with Image.open(src_path) as img:
                img = img.convert("RGB")
                img.save(out_path, "WEBP", quality=82, method=4)
            print(f"Converted {f_name} -> {out_name}")
        else:
            print(f"Warning: {src_path} not found")

EXACT_GALLERY_GRID_HTML = """
<!-- Exact 6 Gallery Photos Grid from Live Website -->
<div class="tdh-gallery-photo-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 30px;">
    <div class="tdh-gallery-item" style="border-radius: 12px; overflow: hidden; height: 230px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.06);"><img src="website-images/KMM_4076.webp" alt="TDH Skilled Professionals Dental Surgery" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" /></div>
    <div class="tdh-gallery-item" style="border-radius: 12px; overflow: hidden; height: 230px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.06);"><img src="website-images/KMM_4092.webp" alt="TDH Stay Flossy Wall Sign" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" /></div>
    <div class="tdh-gallery-item" style="border-radius: 12px; overflow: hidden; height: 230px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.06);"><img src="website-images/KMM_4124.webp" alt="TDH Luxury Consultation Desk" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" /></div>
    <div class="tdh-gallery-item" style="border-radius: 12px; overflow: hidden; height: 230px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.06);"><img src="website-images/KMM_4142.webp" alt="TDH 3D Intraoral CBCT Scanner" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" /></div>
    <div class="tdh-gallery-item" style="border-radius: 12px; overflow: hidden; height: 230px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.06);"><img src="website-images/KMM_4034.webp" alt="TDH Dental Surgery Operation Room" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" /></div>
    <div class="tdh-gallery-item" style="border-radius: 12px; overflow: hidden; height: 230px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.06);"><img src="website-images/KMM_4190.webp" alt="TDH Patient Consultation Session" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" /></div>
</div>
"""

def update_index_html():
    index_file = os.path.join(ROOT_DIR, "index.html")
    with open(index_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Replace existing tdh-gallery-photo-grid
    if 'class="tdh-gallery-photo-grid"' in content:
        import re
        content = re.sub(
            r'<div class="tdh-gallery-photo-grid".*?</div>\s*</div>',
            EXACT_GALLERY_GRID_HTML,
            content,
            flags=re.DOTALL
        )
        print("Updated index.html with exact KMM gallery photos")

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    convert_kmm_images()
    update_index_html()
