import os
import shutil
import json
from PIL import Image

def convert_images():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    uploads_dir = os.path.join(root_dir, "wp-content", "uploads")
    output_dir = os.path.join(root_dir, "public", "website-images")
    os.makedirs(output_dir, exist_ok=True)
    
    img_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.svg')
    
    found_files = []
    if os.path.exists(uploads_dir):
        for root, dirs, files in os.walk(uploads_dir):
            # Skip cache / temp folders
            if any(skip in root for skip in ['al_opt_content', 'cache', 'wc-logs', 'nitropack-logs', 'ShortpixelBackups']):
                continue
            for f in files:
                ext = os.path.splitext(f)[1].lower()
                if ext in img_extensions:
                    found_files.append(os.path.join(root, f))
    
    print(f"Found {len(found_files)} image files in wp-content/uploads")
    
    used_names = {}
    path_mapping = {}
    
    converted_count = 0
    copied_count = 0
    
    for local_path in sorted(found_files):
        ext = os.path.splitext(local_path)[1].lower()
        basename = os.path.splitext(os.path.basename(local_path))[0]
        
        # Determine output filename
        if ext == '.svg':
            out_name = os.path.basename(local_path)
        else:
            out_name = f"{basename}.webp"
        
        # Deduplicate filename collisions if different contents
        if out_name in used_names and used_names[out_name] != local_path:
            counter = 2
            while f"{basename}_{counter}.webp" in used_names:
                counter += 1
            out_name = f"{basename}_{counter}.webp"
            
        used_names[out_name] = local_path
        out_path = os.path.join(output_dir, out_name)
        
        rel_src = os.path.relative_path = os.path.relpath(local_path, root_dir).replace('\\', '/')
        rel_dst = f"/website-images/{out_name}"
        path_mapping[rel_src] = rel_dst
        path_mapping[os.path.basename(local_path)] = rel_dst
        
        if os.path.exists(out_path):
            continue
            
        try:
            if ext == '.svg':
                shutil.copy2(local_path, out_path)
                copied_count += 1
            elif ext in ('.png', '.jpg', '.jpeg', '.gif', '.bmp'):
                with Image.open(local_path) as img:
                    if img.mode in ('RGBA', 'LA', 'P'):
                        img = img.convert('RGBA')
                    else:
                        img = img.convert('RGB')
                    img.save(out_path, 'WEBP', quality=82, method=4)
                converted_count += 1
            elif ext == '.webp':
                shutil.copy2(local_path, out_path)
                copied_count += 1
        except Exception as e:
            print(f"Error processing {local_path}: {e}")
            
    mapping_file = os.path.join(root_dir, "scripts", "image_mapping.json")
    with open(mapping_file, "w", encoding="utf-8") as f:
        json.dump(path_mapping, f, indent=2)
        
    print(f"Successfully converted {converted_count} images to WebP and copied {copied_count} files into public/website-images/")
    print(f"Image mapping saved to {mapping_file}")

if __name__ == "__main__":
    convert_images()
