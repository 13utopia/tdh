import re

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Typography fix: Ensure headings use Exo font
    old_typo = """h1, h2, h3, h4, h5, h6, 
.ekit-heading--title, 
.elementskit-section-title, 
.elementskit-info-box-title, 
.elementor-heading-title,
.elementskit-btn,
.ekit-btn {
    font-family: 'Roboto', 'Exo', sans-serif !important;
}"""

    new_typo = """h1, h2, h3, h4, h5, h6, 
.ekit-heading--title, 
.elementskit-section-title, 
.elementskit-info-box-title, 
.elementor-heading-title,
.elementskit-btn,
.ekit-btn {
    font-family: 'Exo', 'Roboto', sans-serif !important;
    font-weight: 700;
}"""
    content = content.replace(old_typo, new_typo)

    # Also check if any variant exists
    content = re.sub(
        r'font-family:\s*[\'"]Roboto[\'"],\s*[\'"]Exo[\'"]',
        "font-family: 'Exo', 'Roboto'",
        content
    )

    # 2. Section 160abb1 background image fix ("Ensures Your Best Dental Health Ever")
    content = re.sub(
        r'(<section[^>]*data-id="160abb1"[^>]*)(class="[^"]*")',
        r'\1 \2 style="background-image: url(\'website-images/Untitled-design-28.webp\') !important; background-position: center center !important; background-size: cover !important; background-repeat: no-repeat !important; padding: 90px 0 80px 0 !important;"',
        content
    )

    # 3. Section 8f07a53 background image fix ("Gallery of TDH" header)
    content = re.sub(
        r'(<section[^>]*data-id="8f07a53"[^>]*)(class="[^"]*")',
        r'\1 \2 style="background-image: url(\'website-images/Canadian-Car-Shipping-1.webp\') !important; background-position: center center !important; background-size: cover !important; background-repeat: no-repeat !important;"',
        content
    )

    # 4. Section 7255830 background image & bottom image fix ("Smile with Confidence")
    # Replace plain white section style with 3.webp background image
    old_sec_7255830 = r'<section class="elementor-section elementor-top-section elementor-element elementor-element-7255830 elementor-section-boxed elementor-section-height-default" data-id="7255830" data-element_type="section" style="padding: 60px 0 !important; background-color: #ffffff !important;">'
    new_sec_7255830 = r'<section class="elementor-section elementor-top-section elementor-element elementor-element-7255830 elementor-section-boxed elementor-section-height-default" data-id="7255830" data-element_type="section" style="padding: 140px 0 120px 0 !important; background-image: url(\'website-images/3.webp\') !important; background-position: center left !important; background-size: cover !important; background-repeat: no-repeat !important; min-height: 480px;">'
    
    content = content.replace(old_sec_7255830, new_sec_7255830)

    # In section 7255830, remove the duplicated circular treatment-1.webp from column 2
    old_col2_img = """        <!-- Right Column: Vignette Circular Dental Chair Image (Matching Screenshot 2) -->
        <div class="elementor-column elementor-col-50 tdh-smile-col-right" style="flex: 1; min-width: 320px; padding: 20px; display: flex; justify-content: center; align-items: center;">
            <div style="width: 100%; max-width: 460px; position: relative;">
                <img src="website-images/treatment-1.webp" alt="Smile with Confidence Dental Surgery" style="width: 100%; height: 460px; border-radius: 50%; object-fit: cover; box-shadow: 0 15px 40px rgba(0,0,0,0.08);" />
            </div>
        </div>"""

    new_col2_img = """        <!-- Right Column: Space for 3.webp Background Image Graphic -->
        <div class="elementor-column elementor-col-50 tdh-smile-col-right" style="flex: 1; min-width: 320px; min-height: 350px;">
        </div>"""

    content = content.replace(old_col2_img, new_col2_img)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html updated successfully.")

def update_page(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix font family order
    content = re.sub(
        r'font-family:\s*[\'"]Roboto[\'"],\s*[\'"]Exo[\'"]',
        "font-family: 'Exo', 'Roboto'",
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"{file_path} updated successfully.")

if __name__ == '__main__':
    update_index()
    update_page('about/index.html')
    update_page('appointment/index.html')
