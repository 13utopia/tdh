import os

website_images = os.path.join('e:\\tdh', 'website-images')
if os.path.exists(website_images):
    files = os.listdir(website_images)
    print(f"Found {len(files)} files in website-images:")
    for f in sorted(files):
        if any(kw in f.lower() for kw in ['design', 'treatment', 'gallery', 'clinic', 'photo', '1-', '2-', '3-', '4-']):
            print(" -", f)
