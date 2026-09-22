import os

files = ['e:/tdh/index.html', 'e:/tdh/about/index.html', 'e:/tdh/appointment/index.html']

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_preloader = 'medizco-preloder' in content
        print(f"File {fpath} has medizco-preloder:", has_preloader)
