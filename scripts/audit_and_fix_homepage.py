import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=== HOMEPAGE AUDIT & REFINEMENT ===")

# Verify key elements
checks = {
    "Topbar phone number": "+91 99986 81444" in html,
    "RevSlider banners": "Banner-scaled.webp" in html and "Black-Minimalist-Business-Growth-Banner" in html,
    "Dr. Tanya section": "Doctor-Image.webp" in html and "Superior Dental Care" in html,
    "9 Treatment boxes": "Dental Implants" in html and "Gum Disease Treatment" in html,
    "Why Choose TDH center image": "treatment-1.webp" in html and "Ensures Your Best Dental Health Ever" in html,
    "Gallery of TDH dark banner": "#2b3036" in html and "Gallery of TDH" in html,
    "Smile with Confidence section": "Smile with Confidence" in html and "#00aef0" in html and "57, Orchid Sky" in html,
    "Testimonials section": "Service Recipient Says" in html and "4-1.webp" in html,
    "Calendly appointment card": "Calendly" in html or "tdh-appointment-card" in html
}

for item, status in checks.items():
    print(f"  [{'OK' if status else 'MISSING'}] {item}")

# Clean any unencoded residual junk if present
html_clean = re.sub(r'gizmo|conversation-turn|text-token-text-primary', '', html)

with open('e:/tdh/index.html', 'w', encoding='utf-8') as f:
    f.write(html_clean)

print("Homepage refined successfully!")
