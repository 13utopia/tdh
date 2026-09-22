import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
print(f"Total <style> blocks in index.html: {len(styles)}")

for i, s in enumerate(styles):
    if 'Feature Box' in s or 'tdh-gallery' in s or 'cb87659' in s:
        print(f"\n--- Style block {i+1} ---")
        print(s[:2000])
