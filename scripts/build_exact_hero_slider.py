import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original index.html length:", len(html))

# Locate the hero slider section tag
pos_hero = html.find('data-id="hero-slider"')
if pos_hero != -1:
    pos_sec_start = html.rfind('<section', 0, pos_hero)
    pos_sec_end = html.find('</section>', pos_hero) + 10
    
    exact_hero_slider_html = '''<section class="elementor-section elementor-top-section elementor-element elementor-element-hero-slider elementor-section-full_width elementor-section-height-default" data-id="hero-slider" style="width: 100% !important; padding: 0 !important; margin: 0 !important; overflow: hidden !important; position: relative !important;">
    
    <div class="tdh-live-hero-slider" style="position: relative; width: 100%; height: 560px; overflow: hidden; background: #0b132b;">
        
        <!-- Slide 1: Dentist Treating Patient (Matching Screenshot 1) -->
        <div class="tdh-slide active" id="tdh-slide-1" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 1; transition: opacity 0.8s ease-in-out; z-index: 2;">
            <!-- Background Image -->
            <img src="website-images/KMM_4076.webp" alt="Radiant Dental Health Starts Here" fetchpriority="high" loading="eager" style="width: 100%; height: 100%; object-fit: cover; object-position: center; display: block;" />
            
            <!-- Book Now Cyan Pill Button (Positioned Right) -->
            <a href="appointment/" style="position: absolute; bottom: 110px; right: 90px; background: #26b4e8; color: #ffffff; padding: 12px 30px; border-radius: 30px; font-weight: 700; font-size: 15px; text-decoration: none; box-shadow: 0 4px 15px rgba(38,180,232,0.4); z-index: 10; display: inline-flex; align-items: center; gap: 6px;">
                Book Now &gt;
            </a>

            <!-- White Angled Slanted Badge Container (Bottom Right) -->
            <div style="position: absolute; bottom: 0; right: 0; background: #ffffff; padding: 25px 60px 20px 70px; clip-path: polygon(14% 0, 100% 0, 100% 100%, 0% 100%); z-index: 9; max-width: 580px; text-align: right;">
                <h2 style="color: #000000 !important; font-size: 34px !important; font-weight: 800 !important; line-height: 1.15 !important; margin: 0 !important; font-family: 'Roboto', sans-serif !important; letter-spacing: -0.5px;">
                    Radiant Dental Health<br>Starts Here
                </h2>
            </div>
        </div>

        <!-- Slide 2: Wide Clinic Interior Room (Matching Screenshot 2) -->
        <div class="tdh-slide" id="tdh-slide-2" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; transition: opacity 0.8s ease-in-out; z-index: 1;">
            <!-- Background Image -->
            <img src="website-images/KMM_4034.webp" alt="Smile Bright with Healthy Teeth Every Day" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; object-position: center; display: block;" />
            
            <!-- Book Now Cyan Pill Button (Positioned Bottom Left) -->
            <a href="appointment/" style="position: absolute; bottom: 110px; left: 70px; background: #26b4e8; color: #ffffff; padding: 12px 30px; border-radius: 30px; font-weight: 700; font-size: 15px; text-decoration: none; box-shadow: 0 4px 15px rgba(38,180,232,0.4); z-index: 10; display: inline-flex; align-items: center; gap: 6px;">
                Book Now &gt;
            </a>

            <!-- White Angled Slanted Badge Container (Bottom Left) -->
            <div style="position: absolute; bottom: 0; left: 0; background: #ffffff; padding: 25px 70px 20px 40px; clip-path: polygon(0 0, 86% 0, 100% 100%, 0 100%); z-index: 9; max-width: 580px; text-align: left;">
                <h2 style="color: #000000 !important; font-size: 34px !important; font-weight: 800 !important; line-height: 1.15 !important; margin: 0 !important; font-family: 'Roboto', sans-serif !important; letter-spacing: -0.5px;">
                    Smile Bright with<br>Healthy Teeth Every Day
                </h2>
            </div>
        </div>

        <!-- Vertical Slider Navigation Arrows (Right Edge) -->
        <div style="position: absolute; top: 50%; right: 0; transform: translateY(-50%); z-index: 20; display: flex; flex-direction: column;">
            <button onclick="changeTdhSlide(-1)" aria-label="Previous Slide" style="background: rgba(30,30,30,0.75); color: #ffffff; border: none; width: 46px; height: 46px; font-size: 20px; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: background 0.3s; border-bottom: 1px solid rgba(255,255,255,0.2);">
                &#10094;
            </button>
            <button onclick="changeTdhSlide(1)" aria-label="Next Slide" style="background: rgba(30,30,30,0.75); color: #ffffff; border: none; width: 46px; height: 46px; font-size: 20px; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: background 0.3s;">
                &#10095;
            </button>
        </div>

    </div>

    <!-- Interactive Auto-Slide Script -->
    <script>
    let currentTdhSlide = 1;
    function changeTdhSlide(dir) {
        const slide1 = document.getElementById('tdh-slide-1');
        const slide2 = document.getElementById('tdh-slide-2');
        if (!slide1 || !slide2) return;
        
        if (currentTdhSlide === 1) {
            slide1.style.opacity = '0';
            slide1.style.zIndex = '1';
            slide2.style.opacity = '1';
            slide2.style.zIndex = '2';
            currentTdhSlide = 2;
        } else {
            slide2.style.opacity = '0';
            slide2.style.zIndex = '1';
            slide1.style.opacity = '1';
            slide1.style.zIndex = '2';
            currentTdhSlide = 1;
        }
    }
    if (!window.tdhSliderTimer) {
        window.tdhSliderTimer = setInterval(function() { changeTdhSlide(1); }, 6000);
    }
    </script>
</section>'''

    html_updated = html[:pos_sec_start] + exact_hero_slider_html + html[pos_sec_end:]

    with open('e:/tdh/index.html', 'w', encoding='utf-8') as f:
        f.write(html_updated)

    print("Successfully built exact pixel-perfect live Hero Slider in index.html!")
else:
    print("hero-slider position not found!")
