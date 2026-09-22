import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FEATURE_CARD_BG_CSS = """
<!-- Live Website Feature Icon Boxes Background Images & Oval Dental Chair -->
<style>
/* Feature Box 1: Skilled Professionals */
.elementor-element-029862a .elementskit-infobox {
    background: linear-gradient(rgba(11, 19, 43, 0.45), rgba(11, 19, 43, 0.75)), url('website-images/KMM_4076.webp') center/cover no-repeat !important;
    border-radius: 16px !important;
    padding: 30px 20px !important;
    min-height: 220px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}
/* Feature Box 2: Gentle Treatment */
.elementor-element-842cfe9 .elementskit-infobox {
    background: linear-gradient(rgba(11, 19, 43, 0.45), rgba(11, 19, 43, 0.75)), url('website-images/KMM_4092.webp') center/cover no-repeat !important;
    border-radius: 16px !important;
    padding: 30px 20px !important;
    min-height: 220px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}
/* Feature Box 3: Hygiene Excellence */
.elementor-element-eea9b03 .elementskit-infobox {
    background: linear-gradient(rgba(11, 19, 43, 0.45), rgba(11, 19, 43, 0.75)), url('website-images/KMM_4124.webp') center/cover no-repeat !important;
    border-radius: 16px !important;
    padding: 30px 20px !important;
    min-height: 220px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}
/* Feature Box 4: Preventive Approach */
.elementor-element-2cea015 .elementskit-infobox {
    background: linear-gradient(rgba(11, 19, 43, 0.45), rgba(11, 19, 43, 0.75)), url('website-images/KMM_4142.webp') center/cover no-repeat !important;
    border-radius: 16px !important;
    padding: 30px 20px !important;
    min-height: 220px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}
/* Feature Box 5: Modern Facilities */
.elementor-element-6bd7a6a .elementskit-infobox {
    background: linear-gradient(rgba(11, 19, 43, 0.45), rgba(11, 19, 43, 0.75)), url('website-images/KMM_4034.webp') center/cover no-repeat !important;
    border-radius: 16px !important;
    padding: 30px 20px !important;
    min-height: 220px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}
/* Feature Box 6: Comfortable Environment */
.elementor-element-6b10e38 .elementskit-infobox {
    background: linear-gradient(rgba(11, 19, 43, 0.45), rgba(11, 19, 43, 0.75)), url('website-images/KMM_4190.webp') center/cover no-repeat !important;
    border-radius: 16px !important;
    padding: 30px 20px !important;
    min-height: 220px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}

/* Hover Zoom Effect */
.elementskit-infobox:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 12px 25px rgba(0,0,0,0.25) !important;
}

/* Ensure Text & Icons sit clearly over background images */
.elementskit-info-box-title {
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 18px !important;
    text-shadow: 0 2px 4px rgba(0,0,0,0.6) !important;
}
.elementskit-info-box-icon {
    color: #06B6D4 !important;
    font-size: 32px !important;
    margin-bottom: 12px !important;
}
.elementskit-info-box-icon svg {
    fill: #06B6D4 !important;
    width: 36px !important;
    height: 36px !important;
}

/* Oval Dental Chair Image in Column cb87659 */
.elementor-element-cb87659 .elementor-widget-wrap {
    background: url('website-images/treatment-1.webp') center/cover no-repeat !important;
    min-height: 380px !important;
    border-radius: 50% 50% 50% 50% / 40% 40% 40% 40% !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.12) !important;
    border: 4px solid #ffffff !important;
}
</style>
"""

DENTAL_CHAIR_OVAL_IMG_HTML = """
<div class="tdh-dental-chair-oval-container" style="text-align: center; padding: 10px;">
    <img src="website-images/treatment-1.webp" alt="TDH Dental Surgery Chair & Clinic Facility" style="width: 100%; max-width: 520px; height: auto; border-radius: 50% 50% 50% 50% / 40% 40% 40% 40%; box-shadow: 0 12px 30px rgba(0,0,0,0.12); border: 4px solid #ffffff;" />
</div>
"""

def update_index():
    index_file = os.path.join(ROOT_DIR, "index.html")
    with open(index_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # 1. Remove standalone tdh-gallery-photo-grid container if inserted below
    content = re.sub(r'<div class="elementor-container">\s*<div class="tdh-gallery-photo-grid".*?</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # 2. Inject FEATURE_CARD_BG_CSS into head
    if FEATURE_CARD_BG_CSS not in content and '</head>' in content:
        content = content.replace('</head>', f'{FEATURE_CARD_BG_CSS}\n</head>')
        
    # 3. Insert dental chair oval image inside column cb87659
    pos_cb = content.find('elementor-element-cb87659')
    if pos_cb != -1 and 'tdh-dental-chair-oval-container' not in content:
        insert_pos = content.find('<div class="elementor-widget-wrap">', pos_cb)
        if insert_pos != -1:
            insert_pos += len('<div class="elementor-widget-wrap">')
            content = content[:insert_pos] + f"\n{DENTAL_CHAIR_OVAL_IMG_HTML}\n" + content[insert_pos:]
            print("Inserted oval dental chair image into column cb87659")

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Updated index.html with feature card background photos & oval dental chair image")

if __name__ == "__main__":
    update_index()
