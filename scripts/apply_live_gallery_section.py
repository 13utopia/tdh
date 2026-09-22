import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos_5d8 = html.find('data-id="5d8ecd4"')
if pos_5d8 != -1:
    pos_sec_start = html.rfind('<section', 0, pos_5d8)
    pos_sec_end = html.find('</section>', html.find('tdh-gallery-photo-grid', pos_5d8))
    if pos_sec_end != -1:
        pos_sec_end += 10
    else:
        # find the closing section tag after pos_5d8
        pos_sec_end = html.find('</section>', pos_5d8) + 10

    new_gallery_html = '''<section class="elementor-section elementor-top-section elementor-element elementor-element-5d8ecd4 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="5d8ecd4" data-element_type="section" data-e-type="section" style="background-color: #2b3036 !important; padding: 70px 0 80px 0 !important;">
    <div class="elementor-container elementor-column-gap-default" style="max-width: 1140px; margin: 0 auto;">
        <div class="elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-ce289d1" data-id="ce289d1" data-element_type="column" data-e-type="column">
            <div class="elementor-widget-wrap elementor-element-populated">
                <!-- Section Title -->
                <div class="elementor-element elementor-element-17df0c7 elementor-widget elementor-widget-elementskit-heading" data-id="17df0c7" data-element_type="widget" data-widget_type="elementskit-heading.default" style="margin-bottom: 40px; text-align: center;">
                    <div class="elementor-widget-container">
                        <div class="ekit-wid-con">
                            <div class="ekit-heading elementskit-section-title-wraper text_center">
                                <h2 class="ekit-heading--title elementskit-section-title" style="color: #ffffff !important; font-size: 34px !important; font-weight: 700 !important; letter-spacing: -0.5px;">Gallery of TDH</h2>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Live Website 3x2 Photo Grid (Matching Screenshot 1) -->
                <div class="tdh-live-gallery-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; width: 100%;">
                    
                    <!-- Photo 1: Dentist Treating Patient -->
                    <div class="tdh-live-gallery-item" style="position: relative; height: 240px; overflow: hidden; border-radius: 4px; box-shadow: 0 4px 15px rgba(0,0,0,0.25);">
                        <img src="website-images/KMM_4076.webp" alt="TDH Dental Surgery Care" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" />
                    </div>

                    <!-- Photo 2: Stay Flossy Wall Sign -->
                    <div class="tdh-live-gallery-item" style="position: relative; height: 240px; overflow: hidden; border-radius: 4px; box-shadow: 0 4px 15px rgba(0,0,0,0.25);">
                        <img src="website-images/KMM_4092.webp" alt="TDH Stay Flossy Wall Interior" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" />
                    </div>

                    <!-- Photo 3: Luxury Office Desk -->
                    <div class="tdh-live-gallery-item" style="position: relative; height: 240px; overflow: hidden; border-radius: 4px; box-shadow: 0 4px 15px rgba(0,0,0,0.25);">
                        <img src="website-images/KMM_4124.webp" alt="TDH Consultation Suite" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" />
                    </div>

                    <!-- Photo 4: 3D X-Ray Scanner -->
                    <div class="tdh-live-gallery-item" style="position: relative; height: 240px; overflow: hidden; border-radius: 4px; box-shadow: 0 4px 15px rgba(0,0,0,0.25);">
                        <img src="website-images/KMM_4142.webp" alt="TDH 3D Intraoral Scanner" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" />
                    </div>

                    <!-- Photo 5: Dental Treatment Room with Modern Facilities Tag Overlay -->
                    <div class="tdh-live-gallery-item" style="position: relative; height: 240px; overflow: hidden; border-radius: 4px; box-shadow: 0 4px 15px rgba(0,0,0,0.25);">
                        <img src="website-images/KMM_4034.webp" alt="TDH Modern Dental Facilities" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" />
                        <div style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); background: rgba(11, 19, 43, 0.75); color: #ffffff; padding: 6px 16px; border-radius: 20px; font-size: 13px; font-weight: 500; display: flex; align-items: center; gap: 8px; backdrop-filter: blur(4px);">
                            <svg aria-hidden="true" width="14" height="14" fill="#1cba9f" viewBox="0 0 512 512"><path d="M443.98 96.25c-11.01-45.22-47.11-82.06-92.01-93.72-32.19-8.36-63 5.1-89.14 24.33-3.25 2.39-6.96 3.73-10.5 5.48l28.32 18.21c7.42 4.77 9.58 14.67 4.8 22.11-4.46 6.95-14.27 9.86-22.11 4.8L162.83 12.84c-20.7-10.85-43.38-16.4-66.81-10.31-44.9 11.67-81 48.5-92.01 93.72-10.13 41.62-.42 80.81 21.5 110.43 23.36 31.57 32.68 68.66 36.29 107.35 4.4 47.16 10.33 94.16 20.94 140.32l7.8 33.95c3.19 13.87 15.49 23.7 29.67 23.7 13.97 0 26.15-9.55 29.54-23.16l34.47-138.42c4.56-18.32 20.96-31.16 39.76-31.16s35.2 12.85 39.76 31.16l34.47 138.42c3.39 13.61 15.57 23.16 29.54 23.16 14.18 0 26.48-9.83 29.67-23.7l7.8-33.95c10.61-46.15 16.53-93.16 20.94-140.32 3.61-38.7 12.93-75.78 36.29-107.35 21.95-29.61 31.66-68.8 21.53-110.43z"></path></svg>
                            Modern Facilities
                        </div>
                    </div>

                    <!-- Photo 6: Doctor Consultation Session -->
                    <div class="tdh-live-gallery-item" style="position: relative; height: 240px; overflow: hidden; border-radius: 4px; box-shadow: 0 4px 15px rgba(0,0,0,0.25);">
                        <img src="website-images/KMM_4190.webp" alt="TDH Doctor Consultation" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" />
                    </div>

                </div>
            </div>
        </div>
    </div>
</section>'''

    html_updated = html[:pos_sec_start] + new_gallery_html + html[pos_sec_end:]

    # Add hover effect style to head
    hover_css = '''
<style id="tdh-gallery-hover-style">
.tdh-live-gallery-item:hover img {
    transform: scale(1.06) !important;
}
@media (max-width: 768px) {
    .tdh-live-gallery-grid {
        grid-template-columns: repeat(1, 1fr) !important;
    }
}
</style>
'''
    if 'id="tdh-gallery-hover-style"' not in html_updated:
        html_updated = html_updated.replace('</head>', hover_css + '\n</head>')

    with open('e:/tdh/index.html', 'w', encoding='utf-8') as f:
        f.write(html_updated)

    print("Successfully replaced Gallery of TDH section with live dark theme version!")
