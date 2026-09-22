import os
import subprocess

edge_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge_exe):
    edge_exe = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

artifacts_dir = r'C:\Users\Admin\.gemini\antigravity\brain\153a8b8e-c5d5-4393-961c-45d0ed9ad05b'

def capture(url, output_path, window_size="1440,7000"):
    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--screenshot={output_path}",
        f"--window-size={window_size}",
        url
    ]
    print(f"Capturing {url} -> {output_path}...")
    subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    print(f"Captured size: {os.path.getsize(output_path)} bytes")

if __name__ == '__main__':
    local_ss = os.path.join(artifacts_dir, 'local_home_full.png')
    capture('http://localhost:8000/', local_ss)
