import os
import re
import urllib.request
from urllib.parse import unquote

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch_wp_includes():
    html_files = ['index.html', os.path.join('about', 'index.html'), os.path.join('appointment', 'index.html')]
    
    found_urls = set()
    pattern = re.compile(r'(?:src|href)=["\']([^"\']*wp-includes[^"\']*)["\']', re.IGNORECASE)
    
    for fpath in html_files:
        full_path = os.path.join(ROOT_DIR, fpath)
        if not os.path.exists(full_path):
            continue
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        for m in pattern.findall(content):
            clean_rel = unquote(m.split('?')[0].split('#')[0])
            found_urls.add(clean_rel)
            
    print(f"Found {len(found_urls)} unique wp-includes assets to fetch")
    
    for rel_url in sorted(found_urls):
        rel_clean = rel_url.lstrip('/')
        local_path = os.path.join(ROOT_DIR, rel_clean.replace('/', os.sep))
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
            print(f"Already exists: {rel_clean}")
            continue
            
        full_url = f"https://tanyadentalhouse.in/{rel_clean}"
        print(f"Fetching {full_url}...")
        try:
            req = urllib.request.Request(full_url, headers=headers)
            with urllib.request.urlopen(req) as resp:
                data = resp.read()
                with open(local_path, 'wb') as f:
                    f.write(data)
                print(f"Saved {local_path} ({len(data)} bytes)")
        except Exception as e:
            print(f"Failed to fetch {full_url}: {e}")

if __name__ == "__main__":
    fetch_wp_includes()
