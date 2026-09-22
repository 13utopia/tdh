import re
import os

with open(os.path.join('e:\\tdh', 'index_raw.html'), 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

# 1. Inspect icon box sections 0856ea6 and 1cdc1a3
pos = raw.find('Gallery of TDH')
if pos != -1:
    end_sec = raw.find('Smile with Confidence', pos)
    print("--- Gallery Section 0856ea6 & 1cdc1a3 Raw HTML ---")
    print(raw[pos:end_sec if end_sec != -1 else pos+8000])

# 2. Inspect section 7255830 (Smile with Confidence) right column
smile_pos = raw.find('Smile with Confidence')
if smile_pos != -1:
    print("\n--- Smile with Confidence Section 7255830 Raw HTML ---")
    print(raw[smile_pos:smile_pos+4000])
