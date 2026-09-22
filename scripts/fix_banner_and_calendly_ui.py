import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE_IMAGES_DIR = os.path.join(ROOT_DIR, "website-images")

# Clean Simple UI Appointment Form connected to Calendly Popup
CLEAN_CALENDLY_FORM_HTML = """
<!-- Phase 3: Simple Clean UI Appointment Form connected to Calendly -->
<link rel="stylesheet" href="https://assets.calendly.com/assets/external/widget.css" />
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>

<div id="simple-calendly-booking" style="background: #ffffff; padding: 25px; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-family: sans-serif; max-width: 480px; margin: 0 auto;">
    <form id="tdh-appointment-form" onsubmit="return handleCalendlySubmit(event);">
        <div style="margin-bottom: 15px;">
            <label style="display:block; font-size: 13px; font-weight: 600; color: #1e293b; margin-bottom: 6px;">Appointment Service *</label>
            <select id="tdh-service" style="width: 100%; padding: 10px 14px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 14px; color: #0f172a; background: #f8fafc;">
                <option value="General Dental Consultation">General Dental Service</option>
                <option value="Dental Implants">Dental Implants</option>
                <option value="Single-Sitting Root Canal">Root Canal Treatment (RCT)</option>
                <option value="Orthodontics & Clear Aligners">Orthodontics & Aligners</option>
                <option value="Teeth Whitening & Veneers">Cosmetic Veneers & Whitening</option>
                <option value="Zirconia Crowns & Bridges">Crowns & Bridges</option>
            </select>
        </div>

        <div style="margin-bottom: 15px;">
            <label style="display:block; font-size: 13px; font-weight: 600; color: #1e293b; margin-bottom: 6px;">Preferred Date *</label>
            <input type="date" id="tdh-date" required style="width: 100%; padding: 10px 14px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 14px; color: #0f172a; background: #f8fafc;" />
        </div>

        <div style="margin-bottom: 15px;">
            <label style="display:block; font-size: 13px; font-weight: 600; color: #1e293b; margin-bottom: 6px;">Preferred Time Slot *</label>
            <div style="display: grid; grid-template-cols: repeat(3, 1fr); gap: 8px;">
                <button type="button" class="tdh-time-btn active" onclick="selectTimeSlot(this)" style="padding: 8px; font-size: 12px; border: 1px solid #0891b2; background: #ecfeff; color: #0891b2; border-radius: 20px; cursor: pointer; font-weight: 600;">10:00 AM</button>
                <button type="button" class="tdh-time-btn" onclick="selectTimeSlot(this)" style="padding: 8px; font-size: 12px; border: 1px solid #cbd5e1; background: #f8fafc; color: #475569; border-radius: 20px; cursor: pointer;">11:30 AM</button>
                <button type="button" class="tdh-time-btn" onclick="selectTimeSlot(this)" style="padding: 8px; font-size: 12px; border: 1px solid #cbd5e1; background: #f8fafc; color: #475569; border-radius: 20px; cursor: pointer;">01:00 PM</button>
                <button type="button" class="tdh-time-btn" onclick="selectTimeSlot(this)" style="padding: 8px; font-size: 12px; border: 1px solid #cbd5e1; background: #f8fafc; color: #475569; border-radius: 20px; cursor: pointer;">02:30 PM</button>
                <button type="button" class="tdh-time-btn" onclick="selectTimeSlot(this)" style="padding: 8px; font-size: 12px; border: 1px solid #cbd5e1; background: #f8fafc; color: #475569; border-radius: 20px; cursor: pointer;">04:00 PM</button>
                <button type="button" class="tdh-time-btn" onclick="selectTimeSlot(this)" style="padding: 8px; font-size: 12px; border: 1px solid #cbd5e1; background: #f8fafc; color: #475569; border-radius: 20px; cursor: pointer;">05:30 PM</button>
            </div>
        </div>

        <div style="margin-bottom: 15px;">
            <label style="display:block; font-size: 13px; font-weight: 600; color: #1e293b; margin-bottom: 6px;">Email Address *</label>
            <input type="email" id="tdh-email" required placeholder="your.email@example.com" style="width: 100%; padding: 10px 14px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 14px; color: #0f172a; background: #f8fafc;" />
        </div>

        <div style="margin-bottom: 18px; font-size: 12px; color: #475569; display: flex; align-items: center; gap: 6px;">
            <input type="checkbox" id="tdh-terms" required checked style="cursor: pointer;" />
            <label for="tdh-terms">Accept terms and conditions*</label>
        </div>

        <button type="submit" style="width: 100%; padding: 12px; background: linear-gradient(135deg, #0B132B 0%, #1C2541 100%); color: #D4AF37; font-weight: 700; font-size: 15px; border: 1px solid #C59B27; border-radius: 8px; cursor: pointer; transition: background 0.2s;">
            Book Appointment (Submit)
        </button>
    </form>
</div>

<script>
var selectedTime = "10:00 AM";

function selectTimeSlot(btn) {
    document.querySelectorAll('.tdh-time-btn').forEach(function(b) {
        b.style.background = "#f8fafc";
        b.style.color = "#475569";
        b.style.border = "1px solid #cbd5e1";
    });
    btn.style.background = "#ecfeff";
    btn.style.color = "#0891b2";
    btn.style.border = "1px solid #0891b2";
    selectedTime = btn.innerText;
}

function handleCalendlySubmit(e) {
    e.preventDefault();
    var email = document.getElementById('tdh-email').value;
    var service = document.getElementById('tdh-service').value;
    
    if (window.Calendly) {
        Calendly.initPopupWidget({
            url: 'https://calendly.com',
            prefill: {
                email: email,
                customAnswers: {
                    a1: service
                }
            }
        });
    } else {
        window.open('https://calendly.com', '_blank');
    }
    return false;
}
</script>
"""

def fix_site():
    html_files = [
        ("index.html", False),
        (os.path.join("about", "index.html"), True),
        (os.path.join("appointment", "index.html"), True)
    ]
    
    for rel_path, is_subdir in html_files:
        full_path = os.path.join(ROOT_DIR, rel_path)
        if not os.path.exists(full_path):
            continue
            
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        img_prefix = "../website-images/" if is_subdir else "website-images/"
        
        # 1. Fix escaped slashes in data-settings and unescape background image URLs
        def fix_data_settings_url(match):
            raw_val = match.group(1)
            # Replace wp-content\/uploads\/YYYY\/MM\/filename.ext with website-images/filename.webp
            fixed_val = re.sub(
                r'(?:https?:\\/\\/[^"\'\s,\\]+)?(?:\\/)?wp-content\\/uploads\\/[^"\'\s,\\]*?\\/([^"\'\s,\\]+?\.(?:png|jpg|jpeg|gif|webp|svg))',
                lambda m: f"{img_prefix}{os.path.splitext(m.group(1))[0]}.webp",
                raw_val,
                flags=re.IGNORECASE
            )
            return f'data-settings="{fixed_val}"'
            
        content = re.sub(r'data-settings=["\']([^"\']+)["\']', fix_data_settings_url, content)
        
        # 2. Extract background image URLs from data-settings to generate direct CSS fallback rules
        css_fallbacks = []
        pattern_bg = re.compile(r'class=["\']([^"\']*elementor-element-[a-zA-Z0-9]+[^"\']*)["\'][^>]*data-settings=["\']([^"\']+)["\']', re.IGNORECASE)
        for m_class, m_ds in pattern_bg.findall(content):
            # Extract section id/class
            class_match = re.search(r'elementor-element-([a-zA-Z0-9]+)', m_class)
            if class_match:
                el_id = class_match.group(1)
                # Find image URL inside data-settings
                url_match = re.search(r'website-images/([^"\'\\]+)', m_ds)
                if url_match:
                    img_name = url_match.group(1)
                    css_fallbacks.append(f'.elementor-element-{el_id} {{ background-image: url("{img_prefix}{img_name}") !important; background-size: cover !important; background-position: center !important; }}')
                    
        if css_fallbacks:
            fallback_style = f"\n<style>\n" + "\n".join(css_fallbacks) + "\n</style>\n"
            if '</head>' in content:
                content = content.replace('</head>', f'{fallback_style}</head>')

        # 3. Replace calendly container / booking forms with Clean Simple UI Form
        if 'cp_appbooking' in content or 'calendly-booking-container' in content or 'metform' in content:
            content = re.sub(
                r'(?:<div[^>]*class="[^"]*calendly-booking-container[^"]*"[^>]*>.*?</div>\s*</div>|<form[^>]*id="cp_appbooking[^"]*"[^>]*>.*?</form>|<form[^>]*metform-form-content[^>]*>.*?</form>)',
                CLEAN_CALENDLY_FORM_HTML,
                content,
                flags=re.DOTALL | re.IGNORECASE
            )

        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated {full_path} with banner CSS & Simple Calendly Form")

if __name__ == "__main__":
    fix_site()
