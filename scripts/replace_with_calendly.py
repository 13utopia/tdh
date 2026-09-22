import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CALENDLY_HTML = """
<!-- Calendly Integration Section -->
<div className="calendly-booking-container" style="width: 100%; max-width: 900px; margin: 0 auto; padding: 20px; background: #ffffff; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); border: 1px solid #e2e8f0; text-align: center;">
    <div style="margin-bottom: 20px;">
        <span style="display: inline-block; padding: 4px 14px; background: rgba(197, 155, 39, 0.15); color: #C59B27; border-radius: 20px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Online Appointment Scheduling</span>
        <h3 style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 28px; color: #0B132B; margin: 10px 0 6px 0; font-weight: 700;">Select Your Preferred Date & Time</h3>
        <p style="font-size: 14px; color: #64748b; margin: 0 0 16px 0;">Schedule your dental consultation directly with TDH Tanya's Dental House via Calendly.</p>
        <a href="https://calendly.com" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 8px; background: linear-gradient(135deg, #C59B27 0%, #D4AF37 100%); color: #0B132B; font-weight: 700; padding: 12px 28px; border-radius: 30px; text-decoration: none; font-size: 14px; box-shadow: 0 4px 15px rgba(197, 155, 39, 0.3); transition: transform 0.2s;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            Open Booking Calendar (Calendly)
        </a>
    </div>

    <!-- Calendly Inline Widget -->
    <div class="calendly-inline-widget" data-url="https://calendly.com" style="min-width:320px;height:700px;border-radius:12px;overflow:hidden;"></div>
    <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
</div>
"""

def update_forms():
    # 1. Update index.html
    index_file = os.path.join(ROOT_DIR, "index.html")
    if os.path.exists(index_file):
        with open(index_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Replace cp_appbooking form
        pattern = re.compile(r'<form[^>]*id=["\']?cp_appbooking_pform_1["\']?.*?</form>', re.DOTALL | re.IGNORECASE)
        if pattern.search(content):
            content = pattern.sub(CALENDLY_HTML, content)
            print("Replaced cp_appbooking form in index.html with Calendly integration")
        else:
            print("cp_appbooking form not found in index.html")
            
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)

    # 2. Update appointment/index.html
    app_file = os.path.join(ROOT_DIR, "appointment", "index.html")
    if os.path.exists(app_file):
        with open(app_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        pattern = re.compile(r'<form[^>]*metform-form-content.*?></form>', re.DOTALL | re.IGNORECASE)
        if pattern.search(content):
            content = pattern.sub(CALENDLY_HTML, content)
            print("Replaced metform in appointment/index.html with Calendly integration")
        else:
            # Replace main section if metform tag regex didn't match full element
            content = re.sub(r'<div[^>]*class="[^"]*metform-form-wrapper[^"]*"[^>]*>.*?</div>\s*</div>\s*</div>', CALENDLY_HTML, content, flags=re.DOTALL | re.IGNORECASE)
            print("Updated appointment/index.html with Calendly integration")
            
        with open(app_file, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    update_forms()
