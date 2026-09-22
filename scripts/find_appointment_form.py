import os
import re

for page in ['index.html', os.path.join('about', 'index.html'), os.path.join('appointment', 'index.html')]:
    full_path = os.path.join('e:\\tdh', page)
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        matches = re.findall(r'<form[^>]*id=["\']?cp_appbooking[^"\']*["\']?.*?</form>', content, re.DOTALL | re.IGNORECASE)
        print(f"Page {page}: found {len(matches)} appointment form matches")
