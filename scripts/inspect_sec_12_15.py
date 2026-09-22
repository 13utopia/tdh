import re

with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections_to_check = ['5d8ecd4', '6b4cda1', '7255830', '76dcae4']

for sec_id in sections_to_check:
    pos = html.find(f'data-id="{sec_id}"')
    if pos != -1:
        chunk = html[pos:pos+5000]
        text_clean = re.sub(r'<[^>]+>', ' ', chunk)
        text_clean = ' '.join(text_clean.split())[:400]
        print(f"=== Section data-id={sec_id} ===")
        print(text_clean)
        print("-" * 50)
