from PIL import Image
import os

artifacts_dir = r'C:\Users\Admin\.gemini\antigravity\brain\153a8b8e-c5d5-4393-961c-45d0ed9ad05b'
full_path = os.path.join(artifacts_dir, 'local_home_full.png')

img = Image.open(full_path)
width, height = img.size

print(f"Full image dimensions: {width}x{height}")

crops = [
    ('ss_part1_hero_choose.png', 0, 1800),
    ('ss_part2_treatments_health.png', 1800, 3600),
    ('ss_part3_booking_gallery.png', 3600, 5400),
    ('ss_part4_smile_footer.png', 5400, height)
]

for name, y1, y2 in crops:
    if y1 < height:
        y2 = min(y2, height)
        cropped = img.crop((0, y1, width, y2))
        out_p = os.path.join(artifacts_dir, name)
        cropped.save(out_p)
        print(f"Saved {name}: {width}x{y2-y1}")
