with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(r"\'", "'")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Cleaned backslashes successfully.")
