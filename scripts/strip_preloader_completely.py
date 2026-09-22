import os, re

files = ['e:/tdh/index.html', 'e:/tdh/about/index.html', 'e:/tdh/appointment/index.html']

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()

        # Regex to strip <div class="medizco-preloder">...</div>
        html_clean = re.sub(r'<div\s+class=[\"\']medizco-preloder[\"\'][^>]*>.*?</div>', '', html, flags=re.DOTALL)
        html_clean = re.sub(r'<div\s+class=[\"\']medizco-preloader[\"\'][^>]*>.*?</div>', '', html_clean, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html_clean)

        print(f"Stripped preloader HTML from {fpath}")
