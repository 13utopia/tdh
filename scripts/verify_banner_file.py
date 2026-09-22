import os
from PIL import Image

img_path = os.path.join('e:\\tdh', 'website-images', 'Banner-scaled.webp')
if os.path.exists(img_path):
    size = os.path.getsize(img_path)
    with Image.open(img_path) as img:
        print(f"Banner image path: {img_path}")
        print(f"File size: {size} bytes")
        print(f"Dimensions: {img.size[0]}x{img.size[1]} px, mode: {img.mode}")
else:
    print(f"ERROR: {img_path} does not exist!")
