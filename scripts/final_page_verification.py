import urllib.request

pages = [
    ('Home', 'http://localhost:8000/'),
    ('Home (index.html)', 'http://localhost:8000/index.html'),
    ('About', 'http://localhost:8000/about/'),
    ('Appointment', 'http://localhost:8000/appointment/')
]

print("=== FINAL LOCALHOST PAGE TEST ===")
for name, url in pages:
    try:
        res = urllib.request.urlopen(url, timeout=3)
        html = res.read().decode('utf-8', errors='ignore')
        has_body = '<body' in html
        has_preloader_div = '<div class="medizco-preloder"' in html
        print(f"[{name}] {url} -> Status {res.status}, Length: {len(html)} bytes | Body: {has_body} | Preloader Div: {has_preloader_div}")
    except Exception as e:
        print(f"[{name}] {url} -> FAILED: {e}")
