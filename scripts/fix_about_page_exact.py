import re

with open('e:/tdh/about/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original about/index.html length:", len(html))

# 1. Fix malformed double URLs
html = html.replace('//tanyadentalhouse.in../', '../')

# 2. Replace Untitled-design-32.webp with KMM_4034.webp in photo frame
html = html.replace('../website-images/Untitled-design-32.webp', '../website-images/KMM_4034.webp')

# 3. Clean section containing "Dedicated to Your Dental Health"
pos = html.find('Dedicated to Your Dental Health')
if pos != -1:
    pos_sec_start = html.rfind('<section', 0, pos)
    pos_sec_end = html.find('</section>', pos) + 10

    new_about_section = '''<section class="elementor-section elementor-top-section elementor-element elementor-element-321456a elementor-section-boxed elementor-section-height-default" data-id="321456a" data-element_type="section" style="padding: 70px 0 !important; background-color: #ffffff !important;">
    <div class="elementor-container elementor-column-gap-default" style="max-width: 1140px; margin: 0 auto; display: flex; align-items: center; flex-wrap: wrap;">
        
        <!-- Left Column: Double Offset Photo Frame (Matching Screenshot 2) -->
        <div class="elementor-column elementor-col-50" style="flex: 1; min-width: 320px; padding: 20px; display: flex; justify-content: center;">
            <div style="position: relative; width: 100%; max-width: 460px; padding: 15px;">
                <!-- Offset Shadow Frame -->
                <div style="position: absolute; top: 30px; left: 30px; right: 0; bottom: 0; background: #e5e7eb; border-radius: 12px; z-index: 1;"></div>
                <!-- Main Clinic Photo -->
                <div style="position: relative; z-index: 2; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.12); border: 4px solid #ffffff;">
                    <img src="../website-images/KMM_4034.webp" alt="TDH Clinic Surgery Facility" style="width: 100%; height: 420px; object-fit: cover; display: block;" />
                </div>
            </div>
        </div>

        <!-- Right Column: Dedicated to Your Dental Health Text & Cyan Button -->
        <div class="elementor-column elementor-col-50" style="flex: 1; min-width: 320px; padding: 20px 20px 20px 40px;">
            <h2 style="color: #1f2937 !important; font-size: 32px !important; font-weight: 700 !important; line-height: 1.3 !important; margin: 0 0 20px 0 !important; max-width: 480px;">
                Dedicated to Your Dental Health, Well-Being, and Beautiful Smiles.
            </h2>

            <p style="color: #4b5563 !important; font-size: 15px !important; line-height: 1.7 !important; margin-bottom: 15px !important; max-width: 500px;">
                At our dental hospital, we are unwavering in our commitment to your dental health and overall well-being. Our skilled team of experts combines advanced dentistry with a personalized touch, ensuring that you receive the highest quality care.
            </p>

            <p style="color: #4b5563 !important; font-size: 15px !important; line-height: 1.7 !important; margin-bottom: 30px !important; max-width: 500px;">
                We are dedicated to crafting and maintaining your beautiful, radiant smile.
            </p>

            <div>
                <a href="../appointment/" style="background-color: #26b4e8 !important; color: #ffffff !important; font-size: 15px !important; font-weight: 600 !important; padding: 12px 30px !important; border-radius: 30px !important; text-decoration: none !important; display: inline-flex !alignment; align-items: center !important; gap: 6px !important; box-shadow: 0 4px 15px rgba(38,180,232,0.3) !important; transition: all 0.3s ease !important;">
                    Book Now &gt;
                </a>
            </div>
        </div>

    </div>
</section>'''

    html = html[:pos_sec_start] + new_about_section + html[pos_sec_end:]

with open('e:/tdh/about/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated about/index.html length:", len(html))
