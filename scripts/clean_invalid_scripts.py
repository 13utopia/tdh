import re

with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Initial index.html length:", len(html))

# Find and remove any script/link pointing to /?cp_cpappb_resources=...
html_clean = re.sub(r'<script[^>]+src=[\"\']/\?cp_cpappb_resources=[^\"\']+[\"\'][^>]*>\s*</script>', '', html)
html_clean = re.sub(r'<link[^>]+href=[\"\']/\?cp_cpappb_resources=[^\"\']+[\"\'][^>]*>', '', html_clean)

# Also search for any unencoded & in URLs or bad tags
html_clean = html_clean.replace('/?cp_cpappb_resources=', '#deleted_cp_')

with open('e:/tdh/index.html', 'w', encoding='utf-8') as f:
    f.write(html_clean)

print("Cleaned index.html length:", len(html_clean))
