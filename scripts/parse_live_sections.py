from bs4 import BeautifulSoup
import re

with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find main content container
main = soup.find('article') or soup.find('main') or soup.body

print("=== ALL MAIN SECTIONS IN LIVE SITE ===")
sections = soup.find_all('section', class_=re.compile('elementor-top-section'))
for idx, sec in enumerate(sections):
    sec_id = sec.get('data-id', '')
    text_snippet = ' '.join(sec.stripped_strings)[:120]
    imgs = [img.get('src') for img in sec.find_all('img')]
    print(f"\nSection #{idx+1} [id={sec_id}]:")
    print(f"  Snippet: {text_snippet}")
    print(f"  Images ({len(imgs)}): {imgs}")
