import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CLEAN_CARD_HTML = """
<div id="tdh-appointment-card" style="background: #ffffff; padding: 24px; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid #cbd5e1; font-family: system-ui, sans-serif; max-width: 440px; margin: 0 auto; color: #1e293b;">
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
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px;">
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

<link rel="stylesheet" href="https://assets.calendly.com/assets/external/widget.css" />
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>
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

def force_update():
    index_path = os.path.join(ROOT_DIR, "index.html")
    with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Replace dummy.png in RevSlider with direct WebP banner image
    content = re.sub(
        r'src="[^"]*dummy\.png"[^>]*data-lazyload="([^"]+)"',
        r'src="\1" data-lazyload="\1"',
        content,
        flags=re.IGNORECASE
    )
    
    # 2. Replace shortcode container with clean appointment card
    content = re.sub(
        r'<div class="elementor-shortcode">.*?</div>\s*</div>\s*</div>',
        f'<div class="elementor-shortcode">{CLEAN_CARD_HTML}</div></div></div>',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Forced direct image src & injected clean appointment card into index.html")

if __name__ == "__main__":
    force_update()
