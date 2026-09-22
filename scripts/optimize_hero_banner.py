import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original index.html length:", len(html))

# Find the section containing rev_slider_4_1_wrapper
pos_slider = html.find('id="rev_slider_4_1_wrapper"')
if pos_slider == -1:
    pos_slider = html.find('rev_slider_4_1')

if pos_slider != -1:
    pos_sec_start = html.rfind('<section', 0, pos_slider)
    pos_sec_end = html.find('</section>', pos_slider) + 10

    # Build an optimized, instant-loading, pixel-perfect hero slider matching https://tanyadentalhouse.in/
    optimized_hero_banner = '''<section class="elementor-section elementor-top-section elementor-element elementor-element-hero-slider elementor-section-full_width elementor-section-height-default" data-id="hero-slider" data-element_type="section" style="width: 100% !important; padding: 0 !important; margin: 0 !important; overflow: hidden !important; background: #000000 !important;">
    <div class="tdh-hero-banner-container" style="position: relative; width: 100%; max-width: 100%; margin: 0 auto; overflow: hidden;">
        
        <!-- Primary Slide (Instant Eager Loaded WebP Banner) -->
        <div class="tdh-hero-slide active" style="width: 100%; display: block; position: relative;">
            <picture>
                <source srcset="website-images/Banner-scaled.webp" type="image/webp">
                <img src="website-images/Banner-scaled.webp" alt="Tanya Dental House Superior Dental Care Banner" fetchpriority="high" loading="eager" style="width: 100%; height: auto; min-height: 380px; max-height: 650px; object-fit: cover; object-position: center; display: block; border: none;" />
            </picture>
        </div>

    </div>
</section>'''

    html_updated = html[:pos_sec_start] + optimized_hero_banner + html[pos_sec_end:]

    # Remove conflicting inline CSS overrides for rev_slider that cause fixed height distortion
    html_updated = re.sub(r'<style id="tdh-hero-fix">.*?</style>', '', html_updated, flags=re.DOTALL)
    
    with open('e:/tdh/index.html', 'w', encoding='utf-8') as f:
        f.write(html_updated)

    print("Optimized Hero Banner successfully in index.html!")
else:
    print("rev_slider position not found!")
