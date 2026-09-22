import os
from PIL import Image

uploads_dir = os.path.join('e:\\tdh', 'wp-content', 'uploads')

found = []
for root, dirs, files in os.walk(uploads_dir):
    if any(skip in root for skip in ['al_opt_content', 'cache', 'wc-logs', 'nitropack-logs']):
        continue
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        if ext in ['.jpg', '.jpeg', '.png', '.webp']:
            full_path = os.path.join(root, f)
            try:
                size = os.path.getsize(full_path)
                if size > 20000: # larger than 20KB
                    found.append((f, full_path, size))
            except:
                pass

print(f"Found {len(found)} candidate images > 20KB in wp-content/uploads:")
for f, path, sz in sorted(found, key=lambda x: x[0]):
    print(f" - {f} ({sz} bytes) -> {path}")
