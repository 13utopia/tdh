import os

with open(os.path.join('e:\\tdh', 'index_raw.html'), 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

pos = raw.find('cbc1f9b')
if pos != -1:
    print("--- HTML after cbc1f9b ---")
    print(raw[pos:pos+4000])
