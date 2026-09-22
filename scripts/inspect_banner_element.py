import os
import re

with open(os.path.join('e:\\tdh', 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pos = html.find('id="rev_slider_4_1_wrapper"')
if pos != -1:
    print("--- RevSlider Wrapper HTML Snippet ---")
    print(html[pos:pos+1500])
else:
    print("rev_slider_4_1_wrapper not found")
