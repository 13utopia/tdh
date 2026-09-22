import os
import re
import shutil
import urllib.request
from urllib.parse import unquote
from PIL import Image

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBSITE_IMAGES_DIR = os.path.join(ROOT_DIR, "website-images")
UPLOADS_DIR = os.path.join(ROOT_DIR, "wp-content", "uploads")
os.makedirs(WEBSITE_IMAGES_DIR, exist_ok=True)

PAGES = [
    {
        "url": "https://tanyadentalhouse.in/",
        "local_rel": "index.html",
        "is_subdir": False,
    },
    {
        "url": "https://tanyadentalhouse.in/about/",
        "local_rel": os.path.join("about", "index.html"),
        "is_subdir": True,
    },
    {
        "url": "https://tanyadentalhouse.in/appointment/",
        "local_rel": os.path.join("appointment", "index.html"),
        "is_subdir": True,
    }
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# Step 1: Fetch pages
def fetch_pages():
    for p in PAGES:
        dest_path = os.path.join(ROOT_DIR, p["local_rel"])
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        try:
            req = urllib.request.Request(p["url"], headers=headers)
            with urllib.request.urlopen(req) as resp:
                content = resp.read().decode('utf-8', errors='ignore')
                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fetched {p['url']} ({len(content)} bytes)")
        except Exception as e:
            print(f"Error fetching {p['url']}: {e}")

# Step 2: Clean WP Bloat
def clean_wp_bloat(html_content, domain="tanyadentalhouse.in"):
    patterns = [
        r'<div id="wpadminbar".*?</div>',
        r'<meta name="generator".*?>',
        r'window\._wpemojiSettings.*?</script>',
        r'<link[^>]*wp-json[^>]*>',
        r'<link[^>]*xmlrpc[^>]*>',
        r'<link[^>]*wlwmanifest[^>]*>',
        r'<link[^>]*rel="EditURI"[^>]*>',
    ]
    for p in patterns:
        html_content = re.sub(p, '', html_content, flags=re.DOTALL | re.IGNORECASE)
        
    html_content = html_content.replace(f'https://{domain}/', '/')
    html_content = html_content.replace(f'http://{domain}/', '/')
    return html_content

# Mobile Nav Scripts & Accessibility
MOBILE_MENU_SCRIPT = """
<!-- Phase 3: Mobile Navigation JS -->
<script>
document.addEventListener('DOMContentLoaded', function() {
    var menuToggle = document.querySelector('.menu-toggle, .hamburger, .elementor-menu-toggle, [data-toggle="menu"]');
    var mobileMenu = document.querySelector('.mobile-menu, .nav-menu, #site-navigation, .elementor-nav-menu--dropdown');
    
    if (menuToggle && mobileMenu) {
        menuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            mobileMenu.classList.toggle('active');
            menuToggle.classList.toggle('active');
            document.body.classList.toggle('menu-open');
        });
        
        mobileMenu.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                mobileMenu.classList.remove('active');
                menuToggle.classList.remove('active');
                document.body.classList.remove('menu-open');
            });
        });
        
        document.addEventListener('click', function(e) {
            if (!mobileMenu.contains(e.target) && !menuToggle.contains(e.target)) {
                mobileMenu.classList.remove('active');
                menuToggle.classList.remove('active');
                document.body.classList.remove('menu-open');
            }
        });
    }
});
</script>
"""

MOBILE_MENU_CSS = """
<!-- Phase 3 & 4: Mobile CSS & Skip Link Styling -->
<style>
@media (max-width: 1024px) {
    .elementor-nav-menu--dropdown.active, .mobile-menu.active, .nav-menu.active {
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
        transform: translateX(0) !important;
    }
}
.skip-link {
    position: absolute;
    top: -50px;
    left: 0;
    background: #0B132B;
    color: #C59B27;
    padding: 10px 16px;
    z-index: 100000;
    transition: top 0.3s;
    font-weight: bold;
    text-decoration: none;
    border-radius: 0 0 8px 0;
}
.skip-link:focus {
    top: 0;
}
</style>
"""

SKIP_LINK_HTML = """<a href="#main-content" class="skip-link">Skip to content</a>"""

# Helper to find or convert image to WebP
converted_cache = {}

def get_or_convert_webp(img_rel_url):
    clean_url = unquote(img_rel_url.split('?')[0].split('#')[0])
    filename = os.path.basename(clean_url)
    if not filename:
        return None
        
    ext = os.path.splitext(filename)[1].lower()
    basename = os.path.splitext(filename)[0]
    
    if ext == '.svg':
        out_name = filename
    else:
        out_name = f"{basename}.webp"
        
    out_path = os.path.join(WEBSITE_IMAGES_DIR, out_name)
    
    if clean_url in converted_cache:
        return converted_cache[clean_url]
        
    # Search local wp-content/uploads for matching filename
    found_local = None
    for root, dirs, files in os.walk(UPLOADS_DIR):
        if filename in files:
            found_local = os.path.join(root, filename)
            break
            
    if found_local and os.path.exists(found_local) and not os.path.exists(out_path):
        try:
            if ext == '.svg':
                shutil.copy2(found_local, out_path)
            elif ext in ('.png', '.jpg', '.jpeg', '.gif', '.bmp'):
                with Image.open(found_local) as img:
                    if img.mode in ('RGBA', 'LA', 'P'):
                        img = img.convert('RGBA')
                    else:
                        img = img.convert('RGB')
                    img.save(out_path, 'WEBP', quality=82, method=4)
        except Exception as e:
            print(f"Error converting {found_local}: {e}")
            
    converted_cache[clean_url] = out_name
    return out_name

def process_all():
    fetch_pages()
    
    wp_img_pattern = re.compile(
        r'(?:https?://[^/"\'\s]+)?(?:/)?wp-content/uploads/([^"\'\s,\)\>]+?\.(?:png|jpg|jpeg|gif|webp|svg))',
        re.IGNORECASE
    )
    
    for p in PAGES:
        html_file = os.path.join(ROOT_DIR, p["local_rel"])
        if not os.path.exists(html_file):
            continue
            
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        content = clean_wp_bloat(content)
        
        # Replace all wp-content/uploads references with website-images/
        img_prefix = "../website-images/" if p["is_subdir"] else "website-images/"
        
        def replace_img_match(match):
            rel_path_in_uploads = match.group(1)
            webp_name = get_or_convert_webp(rel_path_in_uploads)
            if webp_name:
                return f"{img_prefix}{webp_name}"
            return match.group(0)
            
        content = wp_img_pattern.sub(replace_img_match, content)
        
        # Inject Head & Body scripts
        if '</head>' in content:
            content = content.replace('</head>', f'{MOBILE_MENU_CSS}\n</head>')
        if '<body' in content:
            content = re.sub(r'(<body[^>]*>)', r'\1\n' + SKIP_LINK_HTML, content, count=1, flags=re.IGNORECASE)
        if '</body>' in content:
            content = content.replace('</body>', f'{MOBILE_MENU_SCRIPT}\n</body>')
            
        # Ensure Heading Hierarchy (exactly ONE <h1> per page)
        h1_matches = list(re.finditer(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL | re.IGNORECASE))
        if len(h1_matches) == 0:
            # If no H1 found, convert the first main section title or hero title into H1
            content = re.sub(
                r'<h2([^>]*class="[^"]*(?:elementor-heading-title|title|hero)[^"]*"[^>]*)>(.*?)</h2>',
                r'<h1\1>\2</h1>',
                content,
                count=1,
                flags=re.IGNORECASE
            )
            # If still no H1, inject screen-reader H1
            if '<h1' not in content:
                page_title = "TDH Tanya's Dental House - Luxury Dental Clinic Shela Ahmedabad"
                sr_h1 = f'<h1 className="sr-only" style="position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);border:0;">{page_title}</h1>'
                content = re.sub(r'(<body[^>]*>)', r'\1\n' + sr_h1, content, count=1, flags=re.IGNORECASE)
        elif len(h1_matches) > 1:
            # Keep only first H1 as H1, convert rest to H2
            first = True
            def fix_h1(m):
                nonlocal first
                if first:
                    first = False
                    return m.group(0)
                return f'<h2{m.group(1)}>{m.group(2)}</h2>'
            content = re.sub(r'<h1([^>]*)>(.*?)</h1>', fix_h1, content, flags=re.DOTALL | re.IGNORECASE)
            
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Processed {html_file}")
        
    # Clean up WP cache directories
    for cd in ["al_opt_content", "cache", "wc-logs", "nitropack-logs"]:
        path = os.path.join(ROOT_DIR, "wp-content", "uploads", cd)
        if os.path.exists(path):
            shutil.rmtree(path, ignore_errors=True)
            print(f"Removed cache dir: {cd}")

if __name__ == "__main__":
    process_all()
