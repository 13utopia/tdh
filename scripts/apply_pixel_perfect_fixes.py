import re

def fix_all():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fix Choose Us Section Feature Card Overlap (Section cc3a4c5)
    # Ensure .medizco_service_box_4 has relative positioning and margins
    css_fix = """
<style id="tdh-layout-fixes">
/* Choose Us Feature Card Spacing Fix */
.medizco_service_box_4 {
    position: relative !important;
    margin-bottom: 24px !important;
    clear: both !important;
    display: flex !important;
    align-items: flex-start !important;
}

/* Our Treatment Box Styling */
.tdh-treatment-card {
    background: #ffffff !important;
    padding: 35px 24px !important;
    border-radius: 12px !important;
    border: 1px solid #e2e8f0 !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05) !important;
    text-align: center !important;
    transition: all 0.3s ease !important;
    height: 100% !important;
}
.tdh-treatment-card:hover {
    transform: translateY(-6px) !important;
    box-shadow: 0 15px 35px rgba(0,174,240,0.15) !important;
    border-color: #00aef0 !important;
}

/* Infographic Banner Text Colors against Dark Background */
.elementor-element-160abb1 .ekit-heading--title,
.elementor-element-160abb1 .elementskit-section-title {
    color: #ffffff !important;
    font-size: 34px !important;
    font-weight: 800 !important;
    font-family: 'Exo', sans-serif !important;
    text-shadow: 0 2px 10px rgba(0,0,0,0.3);
}

.elementor-element-160abb1 .elementskit-info-box-title {
    color: #ffffff !important;
    font-size: 20px !important;
    font-weight: 700 !important;
    font-family: 'Exo', sans-serif !important;
}

.elementor-element-160abb1 p {
    color: rgba(255, 255, 255, 0.9) !important;
    font-size: 14px !important;
    line-height: 1.6 !important;
}
</style>
"""

    if 'id="tdh-layout-fixes"' not in html:
        html = html.replace('</head>', css_fix + '\n</head>')

    # 2. Fix Typo in Booking Section: "Book Now ental Wellness
    html = html.replace('"Book Now ental Wellness', 'for Your')

    # Remove stray pattern-1.png broken image
    html = re.sub(r'<img[^>]*pattern-1\.png[^>]*>', '', html)

    # 3. Section 160abb1 ("Ensures Your Best Dental Health Ever") inline style fix
    html = re.sub(
        r'<section class="elementor-section elementor-top-section elementor-element elementor-element-160abb1 medizco_infographic_section[^"]*" data-id="160abb1"[^>]*>',
        '<section class="elementor-section elementor-top-section elementor-element elementor-element-160abb1 medizco_infographic_section elementor-section-boxed elementor-section-height-default" data-id="160abb1" data-element_type="section" style="background-image: url(\'website-images/Untitled-design-28.webp\') !important; background-position: center center !important; background-size: cover !important; background-repeat: no-repeat !important; padding: 90px 0 80px 0 !important; position: relative !important;">',
        html
    )

    # 4. Section 7255830 ("Smile with Confidence") - Add translucent white card container on left side for high contrast
    old_smile_left = """        <!-- Left Column: Content & Contact Details -->
        <div class="elementor-column elementor-col-50 tdh-smile-col-left" style="flex: 1; min-width: 320px; padding: 20px;">
            <div class="tdh-smile-content">"""

    new_smile_left = """        <!-- Left Column: Content & Contact Details -->
        <div class="elementor-column elementor-col-50 tdh-smile-col-left" style="flex: 1; min-width: 320px; padding: 10px;">
            <div class="tdh-smile-content" style="background: rgba(255, 255, 255, 0.92); padding: 35px 40px; border-radius: 20px; box-shadow: 0 15px 35px rgba(0,0,0,0.12); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.8); max-width: 520px;">"""

    html = html.replace(old_smile_left, new_smile_left)

    # 5. Fix Testimonial Avatars: 4-1.webp, 2-1.webp, 3-1.webp
    html = re.sub(
        r'<img[^>]*src="website-images/4-1\.webp"[^>]*>',
        '<img src="website-images/4-1.webp" alt="Suraj Astodiya" style="width: 70px; height: 70px; border-radius: 50%; object-fit: cover; border: 2px solid #00aef0;" />',
        html
    )
    html = re.sub(
        r'<img[^>]*src="website-images/2-1\.webp"[^>]*>',
        '<img src="website-images/2-1.webp" alt="Jasmin Radhiki" style="width: 70px; height: 70px; border-radius: 50%; object-fit: cover; border: 2px solid #00aef0;" />',
        html
    )
    html = re.sub(
        r'<img[^>]*src="website-images/3-1\.webp"[^>]*>',
        '<img src="website-images/3-1.webp" alt="Yash Parekh" style="width: 70px; height: 70px; border-radius: 50%; object-fit: cover; border: 2px solid #00aef0;" />',
        html
    )

    # Write back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Applied all pixel-perfect fixes to index.html.")

if __name__ == '__main__':
    fix_all()
