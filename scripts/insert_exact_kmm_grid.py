import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXACT_GALLERY_GRID_HTML = """
<!-- Exact 6 Gallery Photos Grid from Live Website -->
<div class="elementor-container" style="max-width: 1140px; margin: 30px auto;">
    <div class="tdh-gallery-photo-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; width: 100%;">
        <div class="tdh-gallery-item" style="border-radius: 12px; overflow: hidden; height: 230px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.06);"><img src="website-images/KMM_4076.webp" alt="TDH Skilled Professionals Dental Surgery" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" /></div>
        <div class="tdh-gallery-item" style="border-radius: 12px; overflow: hidden; height: 230px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.06);"><img src="website-images/KMM_4092.webp" alt="TDH Stay Flossy Wall Sign" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" /></div>
        <div class="tdh-gallery-item" style="border-radius: 12px; overflow: hidden; height: 230px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.06);"><img src="website-images/KMM_4124.webp" alt="TDH Luxury Consultation Desk" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" /></div>
        <div class="tdh-gallery-item" style="border-radius: 12px; overflow: hidden; height: 230px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.06);"><img src="website-images/KMM_4142.webp" alt="TDH 3D Intraoral CBCT Scanner" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" /></div>
        <div class="tdh-gallery-item" style="border-radius: 12px; overflow: hidden; height: 230px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.06);"><img src="website-images/KMM_4034.webp" alt="TDH Dental Surgery Operation Room" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" /></div>
        <div class="tdh-gallery-item" style="border-radius: 12px; overflow: hidden; height: 230px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.06);"><img src="website-images/KMM_4190.webp" alt="TDH Patient Consultation Session" style="width:100%; height:100%; object-fit:cover; transition: transform 0.4s ease;" /></div>
    </div>
</div>
"""

def insert_grid():
    index_file = os.path.join(ROOT_DIR, "index.html")
    with open(index_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    pos = content.find("Comfortable Environment")
    if pos != -1:
        # Find ending section tag for feature icons
        end_sec = content.find("</section>", pos)
        if end_sec != -1:
            end_sec = content.find("</section>", end_sec + 10)
            content = content[:end_sec] + f"\n{EXACT_GALLERY_GRID_HTML}\n" + content[end_sec:]
            print("Successfully inserted 6 exact KMM gallery photos into index.html")

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    insert_grid()
