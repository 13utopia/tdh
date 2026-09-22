with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=== LAST 12000 CHARACTERS OF LIVE INDEX.HTML ===")
print(html[-12000:])
