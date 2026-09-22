import os

with open(os.path.join('e:\\tdh', 'index_raw.html'), 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

pos = raw.find('Gallery of TDH')
if pos != -1:
    print(raw[pos:pos+5000])
