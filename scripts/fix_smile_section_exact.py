import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace both desktop 7255830 and mobile 6b4cda1 sections with the clean, perfectly styled section
new_smile_section = '''<section class="elementor-section elementor-top-section elementor-element elementor-element-7255830 elementor-section-boxed elementor-section-height-default" data-id="7255830" data-element_type="section" style="padding: 60px 0 !important; background-color: #ffffff !important;">
    <div class="elementor-container elementor-column-gap-default" style="max-width: 1140px; margin: 0 auto; display: flex; align-items: center; flex-wrap: wrap;">
        
        <!-- Left Column: Content & Contact Details -->
        <div class="elementor-column elementor-col-50 tdh-smile-col-left" style="flex: 1; min-width: 320px; padding: 20px;">
            <div class="tdh-smile-content">
                
                <!-- Title Block with Cyan Tooth Icon -->
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="flex-shrink: 0; width: 48px; height: 48px;">
                        <svg viewBox="0 0 512 512" style="width: 100%; height: 100%;">
                            <path d="M443.98 96.25c-11.01-45.22-47.11-82.06-92.01-93.72-32.19-8.36-63 5.1-89.14 24.33-3.25 2.39-6.96 3.73-10.5 5.48l28.32 18.21c7.42 4.77 9.58 14.67 4.8 22.11-4.46 6.95-14.27 9.86-22.11 4.8L162.83 12.84c-20.7-10.85-43.38-16.4-66.81-10.31-44.9 11.67-81 48.5-92.01 93.72-10.13 41.62-.42 80.81 21.5 110.43 23.36 31.57 32.68 68.66 36.29 107.35 4.4 47.16 10.33 94.16 20.94 140.32l7.8 33.95c3.19 13.87 15.49 23.7 29.67 23.7 13.97 0 26.15-9.55 29.54-23.16l34.47-138.42c4.56-18.32 20.96-31.16 39.76-31.16s35.2 12.85 39.76 31.16l34.47 138.42c3.39 13.61 15.57 23.16 29.54 23.16 14.18 0 26.48-9.83 29.67-23.7l7.8-33.95c10.61-46.15 16.53-93.16 20.94-140.32 3.61-38.7 12.93-75.78 36.29-107.35 21.95-29.61 31.66-68.8 21.53-110.43z" fill="#00aef0"/>
                        </svg>
                    </div>
                    <div>
                        <h2 style="color: #00aef0 !important; font-size: 30px !important; font-weight: 700 !important; line-height: 1.2 !important; margin: 0 0 2px 0 !important;">Smile with Confidence</h2>
                        <h3 style="color: #1a1a1a !important; font-size: 22px !important; font-weight: 700 !important; margin: 0 !important;">With Our Expert Care.</h3>
                    </div>
                </div>

                <p style="color: #4a5568 !important; font-size: 15px !important; line-height: 1.6 !important; margin-bottom: 25px !important; max-width: 480px;">
                    Transform your smile with our expert dental care, ensuring confidence and optimal oral health for everyone we serve.
                </p>

                <!-- Phone Contact Box -->
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="width: 44px; height: 44px; border: 1.5px solid #00aef0; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #00aef0; background: #ffffff; flex-shrink: 0;">
                        <svg width="20" height="20" fill="currentColor" viewBox="0 0 512 512">
                            <path d="M497.39 361.8l-112-48a24 24 0 0 0-28 6.9l-49.6 60.6A370.66 370.66 0 0 1 131.6 204.4l60.6-49.6a24 24 0 0 0 6.9-28l-48-112A24.16 24.16 0 0 0 122.6.61l-104 24A24 24 0 0 0 0 48c0 256 208 464 464 464a24 24 0 0 0 23.39-18.6l24-104a24.23 24.23 0 0 0-14-27.6z"/>
                        </svg>
                    </div>
                    <a href="tel:9998681444" style="color: #00aef0 !important; font-size: 22px !important; font-weight: 700 !important; text-decoration: none !important;">+91 99986 81444</a>
                </div>

                <!-- Location Address Box -->
                <div style="display: flex; align-items: flex-start; gap: 15px;">
                    <div style="width: 44px; height: 44px; border: 1.5px solid #00aef0; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #1a1a1a; background: #ffffff; flex-shrink: 0; margin-top: 2px;">
                        <svg width="20" height="20" fill="currentColor" viewBox="0 0 384 512">
                            <path d="M172.268 501.67C26.97 291.031 0 269.413 0 192 0 85.961 85.961 0 192 0s192 85.961 192 192c0 77.413-26.97 99.031-172.268 309.67-9.535 13.774-29.93 13.773-39.464 0zM192 272c44.183 0 80-35.817 80-80s-35.817-80-80-80-80 35.817-80 80 35.817 80 80 80z"/>
                        </svg>
                    </div>
                    <p style="color: #1a1a1a !important; font-size: 15px !important; font-weight: 700 !important; line-height: 1.4 !important; margin: 0 !important; max-width: 420px;">
                        57, Orchid Sky, O7, Club O7 Rd, opp. Sky City Road, Shela, Ahmedabad, Gujarat 380058
                    </p>
                </div>

            </div>
        </div>

        <!-- Right Column: Vignette Circular Dental Chair Image (Matching Screenshot 2) -->
        <div class="elementor-column elementor-col-50 tdh-smile-col-right" style="flex: 1; min-width: 320px; padding: 20px; display: flex; justify-content: center; align-items: center;">
            <div style="width: 100%; max-width: 460px; position: relative;">
                <img src="website-images/treatment-1.webp" alt="Smile with Confidence Dental Surgery" style="width: 100%; height: 460px; border-radius: 50%; object-fit: cover; box-shadow: 0 15px 40px rgba(0,0,0,0.08);" />
            </div>
        </div>

    </div>
</section>'''

# Replace section 6b4cda1 and 7255830
pos_6b4 = html.find('data-id="6b4cda1"')
pos_7255 = html.find('data-id="7255830"')

if pos_6b4 != -1 and pos_7255 != -1:
    pos_sec1_start = html.rfind('<section', 0, pos_6b4)
    pos_sec2_end = html.find('</section>', pos_7255) + 10
    html = html[:pos_sec1_start] + new_smile_section + html[pos_sec2_end:]
elif pos_7255 != -1:
    pos_sec2_start = html.rfind('<section', 0, pos_7255)
    pos_sec2_end = html.find('</section>', pos_7255) + 10
    html = html[:pos_sec2_start] + new_smile_section + html[pos_sec2_end:]
elif pos_6b4 != -1:
    pos_sec1_start = html.rfind('<section', 0, pos_6b4)
    pos_sec1_end = html.find('</section>', pos_6b4) + 10
    html = html[:pos_sec1_start] + new_smile_section + html[pos_sec1_end:]

with open('e:/tdh/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated Smile with Confidence section successfully!")
