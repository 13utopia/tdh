import urllib.request
import re

def fetch_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(url, headers=headers)
    try:
        return urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

print("=== FETCHING LIVE PAGES FOR AUDIT ===")
live_home = fetch_url('https://tanyadentalhouse.in/')
live_about = fetch_url('https://tanyadentalhouse.in/about/')
live_appointment = fetch_url('https://tanyadentalhouse.in/appointment/')

print(f"Live Home length: {len(live_home)} bytes")
print(f"Live About length: {len(live_about)} bytes")
print(f"Live Appointment length: {len(live_appointment)} bytes")

# Read Local Files
with open('e:/tdh/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    local_home = f.read()

with open('e:/tdh/about/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    local_about = f.read()

with open('e:/tdh/appointment/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    local_appointment = f.read()

print("\n=== AUDITING SECTION BY SECTION ===")

def extract_sections(html):
    # Find all h1, h2, h3 and section headings
    headings = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', html, re.DOTALL)
    clean_headings = []
    for h in headings:
        clean_h = re.sub(r'<[^>]+>', '', h).strip()
        if clean_h and len(clean_h) < 100 and not any(k in clean_h.lower() for k in ['deposit', 'casino', 'gambling']):
            clean_headings.append(clean_h)
    return clean_headings

print("\nLIVE HOMEPAGE HEADINGS:")
for h in extract_sections(live_home):
    print("  -", h)

print("\nLOCAL HOMEPAGE HEADINGS:")
for h in extract_sections(local_home):
    print("  -", h)

print("\nLIVE ABOUT HEADINGS:")
for h in extract_sections(live_about):
    print("  -", h)

print("\nLOCAL ABOUT HEADINGS:")
for h in extract_sections(local_about):
    print("  -", h)

print("\nLIVE APPOINTMENT HEADINGS:")
for h in extract_sections(live_appointment):
    print("  -", h)

print("\nLOCAL APPOINTMENT HEADINGS:")
for h in extract_sections(local_appointment):
    print("  -", h)
