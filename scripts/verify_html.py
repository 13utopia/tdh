import re
import os

def audit_html():
    pattern_old_imgs = re.compile(r'wp-content/uploads/[^"\'\s]+\.(?:png|jpg|jpeg|gif|webp|svg)', re.IGNORECASE)
    pattern_adminbar = re.compile(r'id="wpadminbar"', re.IGNORECASE)
    pattern_h1 = re.compile(r'<h1[^>]*>', re.IGNORECASE)
    
    html_files = ['index.html', os.path.join('about', 'index.html'), os.path.join('appointment', 'index.html')]
    
    for fpath in html_files:
        full_path = os.path.join('e:\\tdh', fpath)
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        old_imgs = pattern_old_imgs.findall(content)
        admin_bars = pattern_adminbar.findall(content)
        h1_tags = pattern_h1.findall(content)
        has_skip_link = 'class="skip-link"' in content
        
        print(f"File: {fpath}")
        print(f"  - Old wp-content/uploads image refs: {len(old_imgs)}")
        print(f"  - Admin bar divs: {len(admin_bars)}")
        print(f"  - Skip link present: {has_skip_link}")
        print(f"  - H1 tag count: {len(h1_tags)}")

if __name__ == "__main__":
    audit_html()
