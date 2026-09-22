import os

with open(os.path.join('e:\\tdh', 'index_raw.html'), 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

pos = raw.find('57, Orchid Sky')
if pos != -1:
    print("--- HTML after Address ---")
    print(raw[pos:pos+4000])
