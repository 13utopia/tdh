import os

with open(os.path.join('e:\\tdh', 'index_raw.html'), 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

pos = raw.find('cb87659')
if pos != -1:
    print("--- HTML inside Column cb87659 ---")
    print(raw[pos:pos+2500])
