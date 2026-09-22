import re
import os

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pos = html.find('rev_slider_4_1')
if pos != -1:
    print("Found rev_slider_4_1 at pos", pos)
    print(html[max(0, pos-100):min(len(html), pos+1200)])
else:
    print("rev_slider_4_1 not found")
