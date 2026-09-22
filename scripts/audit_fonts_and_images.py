import re

files = [
    ('Homepage', 'e:/tdh/index.html'),
    ('About Page', 'e:/tdh/about/index.html'),
    ('Appointment Page', 'e:/tdh/appointment/index.html')
]

print("=== FONTS & IMAGES COMPREHENSIVE AUDIT ===")

for name, fpath in files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    print(f"\n--- {name} ({fpath}) ---")
    
    # 1. Google Fonts import check
    has_fonts = 'fonts.googleapis.com' in html and ('Roboto' in html or 'Exo' in html)
    print("  [Google Fonts loaded]:", has_fonts)

    # 2. Check for missing / fallback images
    imgs = re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', html)
    print(f"  [Total <img> tags]: {len(imgs)}")
    broken_imgs = [img for img in imgs if 'placeholder' in img.lower() or 'untitled-design-32' in img.lower()]
    print("  [Broken / Placeholder images]:", broken_imgs if broken_imgs else "None (Clean)")

    # 3. Check for absolute live URLs that should be local
    remote_imgs = [img for img in imgs if img.startswith('http://') or img.startswith('https://')]
    print("  [Remote img URLs remaining]:", len(remote_imgs))
    for r in remote_imgs:
        print("    - Remote:", r)

    # 4. Check typography font-family declarations
    ff_declarations = re.findall(r'font-family:[^;\"\'<]+', html)
    print(f"  [Inline font-family declarations]: {len(ff_declarations)}")
    for ff in set(ff_declarations[:5]):
        print("    -", ff.strip())
