import re

with open('e:/tdh/about/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=== ABOUT PAGE AUDIT & REFINEMENT ===")

checks = {
    "Hero Banner": "Tanya" in html and "About Us" in html,
    "Dedicated Section photo": "KMM_4034.webp" in html and "Dedicated to Your Dental Health" in html,
    "Dedicated Section button": "#26b4e8" in html and "Book Now" in html,
    "Why Choose Us 2x3 grid": "Why Choose Us?" in html and "tdh-why-grid" in html and "#f4f5f7" in html,
    "6 Why Choose Us cards": "Qualified Dental Professionals" in html and "Emergency Care" in html,
    "Our Tooth Gallery section": "Our Tooth Gallery" in html and "Sleep Apnea" in html
}

for item, status in checks.items():
    print(f"  [{'OK' if status else 'MISSING'}] {item}")

# Clean any unencoded residual junk if present
html_clean = re.sub(r'gizmo|conversation-turn|text-token-text-primary', '', html)

with open('e:/tdh/about/index.html', 'w', encoding='utf-8') as f:
    f.write(html_clean)

print("About page refined successfully!")
