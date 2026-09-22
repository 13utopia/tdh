import re
import os

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find the first elementor-section or main hero container
hero_match = re.search(r'(<section[^>]*class="[^"]*elementor-section[^"]*"[^>]*>.*?)(?:</section>)', html, re.DOTALL | re.IGNORECASE)
if hero_match:
    print("--- Hero Section HTML ---")
    print(hero_match.group(1)[:800])
else:
    print("Hero section not found")
