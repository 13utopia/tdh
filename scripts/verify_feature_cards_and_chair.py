import os

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

has_kmm = 'KMM_4076.webp' in html and 'KMM_4092.webp' in html and 'KMM_4124.webp' in html
has_chair = 'tdh-dental-chair-oval-container' in html and 'treatment-1.webp' in html

print(f"Feature Box Background Photos Present: {has_kmm}")
print(f"Oval Dental Chair Image Present: {has_chair}")
