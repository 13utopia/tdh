import re
import os

with open(os.path.join('e:\\tdh', 'index_raw.html'), 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

# 1. Search Gallery of TDH
gal_pos = raw.find('Gallery of TDH')
if gal_pos != -1:
    print("--- Gallery of TDH Section ---")
    print(raw[gal_pos-100:gal_pos+2000])
else:
    print("Gallery of TDH not found")

# 2. Search Smile with Confidence
smile_pos = raw.find('Smile with Confidence')
if smile_pos != -1:
    print("\n--- Smile with Confidence Section ---")
    print(raw[smile_pos-100:smile_pos+2000])
else:
    print("Smile with Confidence not found")
