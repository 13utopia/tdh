import os
import re

with open(os.path.join('e:\\tdh', 'index_raw.html'), 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

pos = raw.find('Gallery of TDH')
if pos != -1:
    # Search for ekit-portfolio or gallery or images in section 1fce90b
    sec_end = raw.find('Smile with Confidence', pos)
    print("--- Section between Gallery of TDH and Smile with Confidence ---")
    print(raw[pos:sec_end if sec_end != -1 else pos+15000])
