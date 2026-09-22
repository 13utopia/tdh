with open('e:/tdh/scripts/live_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos_footer = html.find('<footer')
if pos_footer != -1:
    print("=== LIVE FOOTER SECTION ===")
    print(html[pos_footer:min(len(html), pos_footer+6000)])

# Also search for footer in local index.html
with open('e:/tdh/index.html', 'r', encoding='utf-8') as f:
    local_html = f.read()

pos_local_footer = local_html.find('<footer')
if pos_local_footer != -1:
    print("\n=== LOCAL FOOTER SECTION ===")
    print(local_html[pos_local_footer:min(len(local_html), pos_local_footer+6000)])
