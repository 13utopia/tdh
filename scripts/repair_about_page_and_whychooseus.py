import re

with open('e:/tdh/about/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original about/index.html length:", len(html))

# Replace Dedicated to Your Dental Health section
pos_ded = html.find('Dedicated to Your Dental Health')
if pos_ded != -1:
    pos_sec_start = html.rfind('<section', 0, pos_ded)
    pos_sec_end = html.find('</section>', pos_ded) + 10
    
    new_dedicated_section = '''<section class="elementor-section elementor-top-section elementor-element elementor-element-321456a elementor-section-boxed elementor-section-height-default" data-id="321456a" data-element_type="section" style="padding: 70px 0 !important; background-color: #ffffff !important;">
    <div class="elementor-container elementor-column-gap-default" style="max-width: 1140px; margin: 0 auto; display: block; clear: both;">
        
        <!-- Left Column: Double Offset Photo Frame -->
        <div class="elementor-column elementor-col-50" style="width: 50%; float: left; padding: 15px; box-sizing: border-box;">
            <div style="position: relative; width: 100%; max-width: 450px; margin: 0 auto;">
                <!-- Offset Shadow Frame -->
                <div style="position: absolute; top: 25px; left: 25px; right: -15px; bottom: -15px; background: #e2e8f0; border-radius: 12px; z-index: 1;"></div>
                <!-- Main Clinic Photo -->
                <div style="position: relative; z-index: 2; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.12); border: 4px solid #ffffff;">
                    <img src="../website-images/KMM_4034.webp" alt="TDH Clinic Surgery Facility" style="width: 100%; height: 420px; object-fit: cover; display: block;" />
                </div>
            </div>
        </div>

        <!-- Right Column: Dedicated to Your Dental Health Text & Cyan Button -->
        <div class="elementor-column elementor-col-50" style="width: 50%; float: left; padding: 20px 20px 20px 30px; box-sizing: border-box;">
            <h2 style="color: #1f2937 !important; font-size: 32px !important; font-weight: 700 !important; line-height: 1.3 !important; margin-top: 0 !important; margin-bottom: 20px !important;">
                Dedicated to Your Dental Health, Well-Being, and Beautiful Smiles.
            </h2>

            <p style="color: #4b5563 !important; font-size: 15px !important; line-height: 1.7 !important; margin-bottom: 15px !important;">
                At our dental hospital, we are unwavering in our commitment to your dental health and overall well-being. Our skilled team of experts combines advanced dentistry with a personalized touch, ensuring that you receive the highest quality care.
            </p>

            <p style="color: #4b5563 !important; font-size: 15px !important; line-height: 1.7 !important; margin-bottom: 30px !important;">
                We are dedicated to crafting and maintaining your beautiful, radiant smile.
            </p>

            <div>
                <a href="../appointment/" style="background-color: #26b4e8 !important; color: #ffffff !important; font-size: 15px !important; font-weight: 600 !important; padding: 12px 30px !important; border-radius: 30px !important; text-decoration: none !important; display: inline-block !important; box-shadow: 0 4px 15px rgba(38,180,232,0.3) !important;">
                    Book Now &gt;
                </a>
            </div>
        </div>

        <div style="clear: both;"></div>
    </div>
</section>'''

    html = html[:pos_sec_start] + new_dedicated_section + html[pos_sec_end:]

# Replace Why Choose Us section
pos_why = html.find('Why Choose Us?')
if pos_why != -1:
    pos_why_start = html.rfind('<section', 0, pos_why)
    pos_why_end = html.find('</section>', html.find('Emergency Care', pos_why)) + 10

    new_why_section = '''<section class="elementor-section elementor-top-section elementor-element elementor-element-whychooseus" data-id="whychooseus" data-element_type="section" style="padding: 70px 0 !important; background-color: #f4f5f7 !important;">
    <div class="elementor-container" style="max-width: 1000px; margin: 0 auto; padding: 0 15px;">
        
        <!-- Header -->
        <div style="text-align: center; margin-bottom: 40px;">
            <h2 style="color: #1f2937 !important; font-size: 34px !important; font-weight: 700 !important; margin-bottom: 12px !important;">Why Choose Us?</h2>
            <p style="color: #64748b !important; font-size: 15px !important; max-width: 650px; margin: 0 auto; line-height: 1.5 !important;">
                Choose us for our expert team, dedication to your dental well-being, commitment to lasting smiles, and unwavering pursuit of excellence in dentistry
            </p>
        </div>

        <!-- 2x3 White Card Container with Grid Lines & Soft Shadow (Matching Screenshot 1) -->
        <div class="tdh-why-grid" style="background: #ffffff !important; border-radius: 8px !important; box-shadow: 0 10px 40px rgba(0,0,0,0.06) !important; border: 1px solid #e2e8f0 !important; overflow: hidden !important; display: grid !important; grid-template-columns: repeat(2, 1fr) !important;">
            
            <!-- Card 1 -->
            <div style="padding: 35px 30px; text-align: center; border-right: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0;">
                <h3 style="color: #2b3a55 !important; font-size: 18px !important; font-weight: 600 !important; margin-top: 0 !important; margin-bottom: 12px !important;">Qualified Dental Professionals</h3>
                <p style="color: #64748b !important; font-size: 13.5px !important; line-height: 1.6 !important; margin: 0 !important;">Dental clinics are staffed by licensed and experienced dental professionals, including dentists, dental hygienists, and dental assistants.</p>
            </div>

            <!-- Card 2 -->
            <div style="padding: 35px 30px; text-align: center; border-bottom: 1px solid #e2e8f0;">
                <h3 style="color: #2b3a55 !important; font-size: 18px !important; font-weight: 600 !important; margin-top: 0 !important; margin-bottom: 12px !important;">Comprehensive Dental Services</h3>
                <p style="color: #64748b !important; font-size: 13.5px !important; line-height: 1.6 !important; margin: 0 !important;">Dental clinics offer a wide range of dental services, including routine check-ups, cleanings, fillings, extractions, root canals, orthodontic treatments, and more.</p>
            </div>

            <!-- Card 3 -->
            <div style="padding: 35px 30px; text-align: center; border-right: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0;">
                <h3 style="color: #2b3a55 !important; font-size: 18px !important; font-weight: 600 !important; margin-top: 0 !important; margin-bottom: 12px !important;">Appointment Scheduling</h3>
                <p style="color: #64748b !important; font-size: 13.5px !important; line-height: 1.6 !important; margin: 0 !important;">Most dental clinics offer flexible appointment scheduling to accommodate the needs of patients, including early morning, evening, and weekend appointments.</p>
            </div>

            <!-- Card 4 -->
            <div style="padding: 35px 30px; text-align: center; border-bottom: 1px solid #e2e8f0;">
                <h3 style="color: #2b3a55 !important; font-size: 18px !important; font-weight: 600 !important; margin-top: 0 !important; margin-bottom: 12px !important;">Patient-Focused Care</h3>
                <p style="color: #64748b !important; font-size: 13.5px !important; line-height: 1.6 !important; margin: 0 !important;">Dental clinics prioritize patient comfort and well-being, providing a welcoming and relaxing environment to reduce anxiety and fear often associated with dental visits</p>
            </div>

            <!-- Card 5 -->
            <div style="padding: 35px 30px; text-align: center; border-right: 1px solid #e2e8f0;">
                <h3 style="color: #2b3a55 !important; font-size: 18px !important; font-weight: 600 !important; margin-top: 0 !important; margin-bottom: 12px !important;">Dental Education</h3>
                <p style="color: #64748b !important; font-size: 13.5px !important; line-height: 1.6 !important; margin: 0 !important;">Dental clinics educate patients on oral care, covering brushing, flossing techniques, dietary guidance, and stressing regular check-ups for holistic oral health.</p>
            </div>

            <!-- Card 6 -->
            <div style="padding: 35px 30px; text-align: center;">
                <h3 style="color: #2b3a55 !important; font-size: 18px !important; font-weight: 600 !important; margin-top: 0 !important; margin-bottom: 12px !important;">Emergency Care</h3>
                <p style="color: #64748b !important; font-size: 13.5px !important; line-height: 1.6 !important; margin: 0 !important;">Many dental clinics offer emergency dental services to address sudden and severe dental issues, such as toothaches, broken teeth, or injuries.</p>
            </div>

        </div>
    </div>
</section>'''

    html = html[:pos_why_start] + new_why_section + html[pos_why_end:]

with open('e:/tdh/about/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Repaired about/index.html length:", len(html))
