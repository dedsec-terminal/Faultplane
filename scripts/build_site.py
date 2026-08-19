import os
import json
import math
import yaml
import markdown
import shutil
from pathlib import Path
from datetime import datetime

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
POSTS_DIR = BASE_DIR / "content" / "posts"
CVES_DIR = BASE_DIR / "content" / "cves"
SRC_DIR = BASE_DIR / "src"
DIST_DIR = BASE_DIR / "dist"
TEMPLATES_DIR = SRC_DIR / "templates"
DATA_DIR = DIST_DIR / "data"

POSTS_PER_PAGE = 20

def parse_frontmatter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1])
                body = parts[2]
                return frontmatter, body
            except Exception as e:
                print(f"Error parsing frontmatter: {e}")
    return {}, content

def load_markdown_files(directory):
    items = []
    if not directory.exists():
        return items
        
    for md_file in directory.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(content)
        
        if frontmatter.get("draft", False):
            continue
            
        html_body = markdown.markdown(body, extensions=['extra', 'codehilite', 'sane_lists'])
        
        slug = md_file.stem
        date_str = frontmatter.get("date", datetime.now().isoformat())
        if isinstance(date_str, datetime):
            date_str = date_str.isoformat()
            
        try:
            parsed_date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            formatted_date = parsed_date.strftime("%Y-%m-%d %H:%M")
        except ValueError:
            formatted_date = str(date_str)
            
        # Parse Category correctly based strictly on 'category' frontmatter (not tags)
        category = frontmatter.get("category", "other").lower().strip()
        tags = frontmatter.get("tags", [])

        item = {
            "title": frontmatter.get("title", "Untitled"),
            "date": date_str,
            "formatted_date": formatted_date,
            "category": category,
            "tags": tags,
            "slug": slug,
            "body": html_body,
            "type": "post" if directory == POSTS_DIR else "cve"
        }
        
        if item["type"] == "cve":
            item["url"] = f"/Faultplane/cves/{slug}.html"
            item["cve"] = frontmatter.get("cve", slug)
            item["cvss"] = frontmatter.get("cvss")
            item["severity"] = frontmatter.get("severity")
            item["kev"] = frontmatter.get("kev", False)
        else:
            item["url"] = f"/Faultplane/posts/{slug}.html"
            
        items.append(item)
    return items

def build_site():
    print("Starting static build process...")
    
    # Create dist directories
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    
    DIST_DIR.mkdir(parents=True)
    (DIST_DIR / "posts").mkdir(parents=True)
    (DIST_DIR / "cves").mkdir(parents=True)
    (DIST_DIR / "categories").mkdir(parents=True)
    (DIST_DIR / "feed").mkdir(parents=True)
    DATA_DIR.mkdir(parents=True)

    # Copy static assets (css, js, images)
    for asset_type in ["css", "js", "images"]:
        asset_src = SRC_DIR / asset_type
        if asset_src.exists():
            shutil.copytree(asset_src, DIST_DIR / asset_type)

    # Load templates
    try:
        base_tmpl = (TEMPLATES_DIR / "base.html").read_text(encoding="utf-8")
        index_tmpl = (TEMPLATES_DIR / "index.html").read_text(encoding="utf-8")
        post_tmpl = (TEMPLATES_DIR / "post.html").read_text(encoding="utf-8")
        landing_tmpl = (TEMPLATES_DIR / "landing.html").read_text(encoding="utf-8")
    except FileNotFoundError:
        print("Templates not found in src/templates/. Please ensure all templates exist.")
        return

    # Process all content
    posts = load_markdown_files(POSTS_DIR)
    cves = load_markdown_files(CVES_DIR)
    
    all_content = posts + cves
    all_content.sort(key=lambda x: x["date"], reverse=True)
    posts.sort(key=lambda x: x["date"], reverse=True)
    cves.sort(key=lambda x: x["date"], reverse=True)
    
    # Generate content.json for search
    search_index = []
    for item in all_content:
        search_index.append({
            "title": item["title"],
            "url": item["url"],
            "date": item["date"],
            "category": item["category"],
            "tags": item["tags"]
        })
    (DATA_DIR / "content.json").write_text(json.dumps(search_index), encoding="utf-8")
    
    # Generate individual pages
    for item in all_content:
        post_content = post_tmpl.replace("{{ title }}", item["title"]) \
                                .replace("{{ date }}", item["formatted_date"]) \
                                .replace("{{ body }}", item["body"])
        
        cat_html = f'<a href="/Faultplane/categories/{item["category"]}.html" class="category-tag">{item["category"]}</a> '
        post_content = post_content.replace("{{ categories }}", cat_html)
        
        full_html = base_tmpl.replace("{{ title }}", f"{item['title']} - Faultplane") \
                             .replace("{{ content }}", post_content)
        
        if item["type"] == "cve":
            (DIST_DIR / "cves" / f"{item['slug']}.html").write_text(full_html, encoding="utf-8")
        else:
            (DIST_DIR / "posts" / f"{item['slug']}.html").write_text(full_html, encoding="utf-8")
        
    # Categorize items (strictly by 'category')
    category_map = {}
    for item in all_content:
        cat = item["category"]
        if cat not in category_map:
            category_map[cat] = []
        category_map[cat].append(item)

    # Helper function to generate paginated indexes
    def generate_paginated_index(post_list, base_url, title, folder, filename_base="index"):
        total_pages = math.ceil(len(post_list) / POSTS_PER_PAGE)
        if total_pages == 0:
            total_pages = 1
            
        for page in range(1, total_pages + 1):
            start_idx = (page - 1) * POSTS_PER_PAGE
            end_idx = start_idx + POSTS_PER_PAGE
            page_posts = post_list[start_idx:end_idx]
            
            feed_html = '<ul class="post-list">'
            for p in page_posts:
                feed_html += f'<li><span class="post-meta">{p["formatted_date"]}</span> <a href="{p["url"]}">{p["title"]}</a></li>\n'
            feed_html += '</ul>'
            
            # Pagination links
            pagination_html = '<div class="pagination">'
            if page > 1:
                prev_link = f"{filename_base}.html" if page == 2 else f"{filename_base}-{page-1}.html"
                pagination_html += f'<a href="{prev_link}">&laquo; Prev</a>'
            if page < total_pages:
                next_link = f"{filename_base}-{page+1}.html"
                pagination_html += f'<a href="{next_link}">Next &raquo;</a>'
            pagination_html += '</div>'
            
            page_content = index_tmpl.replace("{{ feed }}", feed_html) \
                                     .replace("{{ pagination }}", pagination_html) \
                                     .replace("{{ title_header }}", title)
            
            full_html = base_tmpl.replace("{{ title }}", f"{title} - Faultplane") \
                                 .replace("{{ content }}", page_content)
            
            filename = f"{filename_base}.html" if page == 1 else f"{filename_base}-{page}.html"
            (folder / filename).write_text(full_html, encoding="utf-8")

    # Generate Chronological Feed
    generate_paginated_index(posts, "/Faultplane/feed/index", "Intelligence Feed", DIST_DIR / "feed")
    
    # Generate CVE Index
    generate_paginated_index(cves, "/Faultplane/cves/index", "Latest Vulnerabilities (CVEs)", DIST_DIR / "cves")
    
    # Generate Category indexes (Fixes the Malware 404)
    for cat, cat_items in category_map.items():
        generate_paginated_index(cat_items, f"/Faultplane/categories/{cat}", f"Category: {cat}", DIST_DIR / "categories", filename_base=cat)

    # Generate custom Landing Page (index.html)
    def render_list(items, limit=5):
        html = '<ul class="post-list">'
        for p in items[:limit]:
            html += f'<li><span class="post-meta">{p["formatted_date"]}</span> <a href="{p["url"]}">{p["title"]}</a></li>\n'
        html += '</ul>'
        return html
        
    malware_posts = category_map.get("malware", [])
    
    landing_content = landing_tmpl.replace("{{ latest_intel }}", render_list(posts, 7)) \
                                  .replace("{{ latest_cves }}", render_list(cves, 7)) \
                                  .replace("{{ latest_malware }}", render_list(malware_posts, 5))
                                  
    full_landing = base_tmpl.replace("{{ title }}", "Faultplane - Cyber Threat Intelligence") \
                            .replace("{{ content }}", landing_content)
                            
    (DIST_DIR / "index.html").write_text(full_landing, encoding="utf-8")

    print(f"Build complete! Generated {len(all_content)} items in {DIST_DIR}.")

if __name__ == "__main__":
    build_site()
