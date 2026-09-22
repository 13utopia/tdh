import urllib.request

urls = [
    'http://localhost:8000/',
    'http://localhost:8000/index.html',
    'http://localhost:8000/about/',
    'http://localhost:8000/appointment/'
]

for url in urls:
    try:
        req = urllib.request.urlopen(url, timeout=3)
        print(f"URL: {url} -> Status {req.status}, Length {len(req.read())}")
    except Exception as e:
        print(f"URL: {url} -> FAILED: {e}")
