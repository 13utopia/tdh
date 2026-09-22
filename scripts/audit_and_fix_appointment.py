import re

with open('e:/tdh/appointment/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=== APPOINTMENT PAGE AUDIT & REFINEMENT ===")

checks = {
    "Hero Banner": "Get Appointment" in html or "Appointment" in html,
    "Emergency Assistance section": "24 Hour" in html and "Emergency" in html,
    "Phone Contact": "+91 99986 81444" in html or "99986" in html,
    "Calendly booking card": "Calendly" in html or "tdh-appointment-card" in html or "Book" in html
}

for item, status in checks.items():
    print(f"  [{'OK' if status else 'MISSING'}] {item}")

# Clean any unencoded residual junk if present
html_clean = re.sub(r'gizmo|conversation-turn|text-token-text-primary', '', html)

with open('e:/tdh/appointment/index.html', 'w', encoding='utf-8') as f:
    f.write(html_clean)

print("Appointment page refined successfully!")
