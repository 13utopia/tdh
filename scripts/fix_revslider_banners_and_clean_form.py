import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CLEAN_APPOINTMENT_CARD_HTML = """
<!-- Simple Clean UI Appointment Booking Form connected to Calendly -->
<link rel="stylesheet" href="https://assets.calendly.com/assets/external/widget.css" />
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>

<div id="tdh-appointment-card" style="background: #ffffff; padding: 24px; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); border: 1px solid #e2e8f0; font-family: inherit; max-width: 460px; margin: 0 auto; color: #1e293b;">
    <h4 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 24px; font-weight: 700; color: #0B132B; margin: 0 0 4px 0; text-align: center;">Book Dental Appointment</h4>
    <p style="font-size: 13px; color: #64748b; margin: 0 0 16px 0; text-align: center;">Select your service & date below to schedule with TDH.</p>
    
    <form id="tdh-booking-form" onsubmit="return handleCalendlySubmit(event);">
        <div style="margin-bottom: 12px;">
            <label style="display:block; font-size: 12px; font-weight: 600; color: #334155; margin-bottom: 4px;">Appointment Service *</label>
            <select id="tdh-service-select" style="width: 100%; padding: 10px 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 13px; color: #0f172a; background: #f8fafc; outline: none;">
                <option value="General Dental Consultation">Dental Service (General Consultation)</option>
                <option value="Dental Implants">Dental Implants & Rehabilitation</option>
                <option value="Single-Sitting Root Canal">Root Canal Treatment (RCT)</option>
                <option value="Orthodontics & Clear Aligners">Orthodontics & Invisible Aligners</option>
                <option value="Teeth Whitening & Veneers">Cosmetic Veneers & Whitening</option>
                <option value="Zirconia Crowns & Bridges">Crowns, Bridges & Dentures</option>
            </select>
        </div>

        <div style="margin-bottom: 12px;">
            <label style="display:block; font-size: 12px; font-weight: 600; color: #334155; margin-bottom: 4px;">Select Date *</label>
            <input type="date" id="tdh-date-input" required style="width: 100%; padding: 10px 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 13px; color: #0f172a; background: #f8fafc; outline: none;" />
        </div>

        <div style="margin-bottom: 12px;">
            <label style="display:block; font-size: 12px; font-weight: 600; color: #334155; margin-bottom: 6px;">Available Time Slots *</label>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px;" id="tdh-time-grid">
                <button type="button" class="tdh-slot active" onclick="pickSlot(this)" style="padding: 7px 4px; font-size: 11px; border: 1px solid #0891b2; background: #ecfeff; color: #0891b2; border-radius: 16px; cursor: pointer; font-weight: 600;">10:00 AM</button>
                <button type="button" class="tdh-slot" onclick="pickSlot(this)" style="padding: 7px 4px; font-size: 11px; border: 1px solid #cbd5e1; background: #f8fafc; color: #475569; border-radius: 16px; cursor: pointer;">11:30 AM</button>
                <button type="button" class="tdh-slot" onclick="pickSlot(this)" style="padding: 7px 4px; font-size: 11px; border: 1px solid #cbd5e1; background: #f8fafc; color: #475569; border-radius: 16px; cursor: pointer;">01:00 PM</button>
                <button type="button" class="tdh-slot" onclick="pickSlot(this)" style="padding: 7px 4px; font-size: 11px; border: 1px solid #cbd5e1; background: #f8fafc; color: #475569; border-radius: 16px; cursor: pointer;">02:30 PM</button>
                <button type="button" class="tdh-slot" onclick="pickSlot(this)" style="padding: 7px 4px; font-size: 11px; border: 1px solid #cbd5e1; background: #f8fafc; color: #475569; border-radius: 16px; cursor: pointer;">04:00 PM</button>
                <button type="button" class="tdh-slot" onclick="pickSlot(this)" style="padding: 7px 4px; font-size: 11px; border: 1px solid #cbd5e1; background: #f8fafc; color: #475569; border-radius: 16px; cursor: pointer;">05:30 PM</button>
            </div>
        </div>

        <div style="margin-bottom: 12px;">
            <label style="display:block; font-size: 12px; font-weight: 600; color: #334155; margin-bottom: 4px;">Email Address *</label>
            <input type="email" id="tdh-email-input" required placeholder="name@example.com" style="width: 100%; padding: 10px 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 13px; color: #0f172a; background: #f8fafc; outline: none;" />
        </div>

        <div style="margin-bottom: 14px; font-size: 12px; color: #475569; display: flex; align-items: center; gap: 6px;">
            <input type="checkbox" id="tdh-terms-check" required checked style="cursor: pointer;" />
            <label for="tdh-terms-check">Accept terms and conditions*</label>
        </div>

        <button type="submit" style="width: 100%; padding: 12px; background: #0B132B; color: #D4AF37; font-weight: 700; font-size: 14px; border: 1px solid #C59B27; border-radius: 8px; cursor: pointer; transition: all 0.2s;">
            Submit & Open Calendly
        </button>
    </form>
</div>

<script>
function pickSlot(btn) {
    document.querySelectorAll('.tdh-slot').forEach(function(b) {
        b.style.background = "#f8fafc";
        b.style.color = "#475569";
        b.style.border = "1px solid #cbd5e1";
    });
    btn.style.background = "#ecfeff";
    btn.style.color = "#0891b2";
    btn.style.border = "1px solid #0891b2";
}

function handleCalendlySubmit(e) {
    e.preventDefault();
    var email = document.getElementById('tdh-email-input').value;
    var service = document.getElementById('tdh-service-select').value;
    
    if (window.Calendly) {
        Calendly.initPopupWidget({
            url: 'https://calendly.com',
            prefill: {
                email: email,
                customAnswers: { a1: service }
            }
        });
    } else {
        window.open('https://calendly.com', '_blank');
    }
    return false;
}
</script>
"""

def fix_all():
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
        
        # 1. Remove fbuilder-public.js and metform script tags that dynamically overwrite forms
        content = re.sub(r'<script[^>]*fbuilder-public\.js[^>]*></script>', '', content, flags=re.IGNORECASE)
        content = re.sub(r'<script[^>]*metform/build/frontend[^>]*></script>', '', content, flags=re.IGNORECASE)
        
        # 2. Fix RevSlider banner lazyload and src URLs
        # Replace //tanyadentalhouse.inwebsite-images/ or corrupted prefixes
        content = re.sub(
            r'(?:https?:)?//tanyadentalhouse\.in(?:/)?(?:website-images/|wp-content/uploads/[^"\'\s,\)\\]*?/)([^"\'\s,\)\\]+?\.(?:png|jpg|jpeg|gif|webp|svg))',
            rf'{img_prefix}\1',
            content,
            flags=re.IGNORECASE
        )
        
        # Replace data-lazyload and data-thumb attributes in RevSlider
        def fix_rev_img(m):
            attr_name = m.group(1) # data-lazyload, data-thumb, src
            val = m.group(2)
            fname = os.path.basename(val.split('?')[0].split('#')[0])
            ext = os.path.splitext(fname)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png']:
                fname = f"{os.path.splitext(fname)[0]}.webp"
            return f'{attr_name}="{img_prefix}{fname}"'
            
        content = re.sub(
            r'(data-lazyload|data-thumb|data-src)=["\']([^"\']+)["\']',
            fix_rev_img,
            content,
            flags=re.IGNORECASE
        )
        
        # Replace revslider dummy.png with direct image if revslider lazyload fails
        content = content.replace(
            f'src="{img_prefix}dummy.png" alt="" title="Banner" width="2560" height="1280" class="rev-slidebg tp-rs-img rs-lazyload" data-lazyload="{img_prefix}Banner-scaled.webp"',
            f'src="{img_prefix}Banner-scaled.webp" alt="" title="Banner" width="2560" height="1280" class="rev-slidebg tp-rs-img"'
        )
        
        # 3. Inject explicit CSS rule for RevSlider banner slide background
        rev_css = f"""
<style>
rs-slide, rs-slide img, .rev-slidebg {{
    opacity: 1 !important;
    visibility: visible !important;
}}
.elementor-element-c0b8969, .elementor-element-31518f8, .elementor-section-height-min-height {{
    background-image: url("{img_prefix}Banner-scaled.webp") !important;
    background-size: cover !important;
    background-position: center center !important;
}}
</style>
"""
        if rev_css not in content and '</head>' in content:
            content = content.replace('</head>', f'{rev_css}</head>')
            
        # 4. Replace appointment booking forms with Clean Appointment Card HTML
        if 'simple-calendly-booking' in content or 'calendly-booking-container' in content or 'cp_appbooking' in content or 'metform' in content:
            content = re.sub(
                r'(?:<div[^>]*id="simple-calendly-booking"[^>]*>.*?</div>\s*<script>.*?</script>|<div[^>]*class="[^"]*calendly-booking-container[^"]*"[^>]*>.*?</div>\s*</div>|<form[^>]*id="cp_appbooking[^"]*"[^>]*>.*?</form>|<form[^>]*metform-form-content[^>]*>.*?</form>)',
                CLEAN_APPOINTMENT_CARD_HTML,
                content,
                flags=re.DOTALL | re.IGNORECASE
            )

        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated {full_path} - RevSlider Banner & Clean Form Fixed")

if __name__ == "__main__":
    fix_all()
