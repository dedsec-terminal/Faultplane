import os
import re
import yaml
import markdown
import shutil
import math
from pathlib import Path
from datetime import datetime

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content" / "posts"
SRC_DIR = BASE_DIR / "src"
DIST_DIR = BASE_DIR / "dist"
TEMPLATES_DIR = SRC_DIR / "templates"

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

def build_site():
    print("Starting static build process...")
    
    # Create dist directories
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    
    DIST_DIR.mkdir(parents=True)
    (DIST_DIR / "posts").mkdir(parents=True)
    (DIST_DIR / "categories").mkdir(parents=True)

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
    except FileNotFoundError:
        print("Templates not found in src/templates/. Please create base.html, index.html, and post.html.")
        return

    # Process all posts
    posts = []
    
    for md_file in CONTENT_DIR.glob("*.md"):
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

        post = {
            "title": frontmatter.get("title", "Untitled"),
            "date": date_str,
            "formatted_date": formatted_date,
            "categories": frontmatter.get("tags", []),
            "slug": slug,
            "url": f"/Faultplane/posts/{slug}.html",
            "body": html_body
        }
        posts.append(post)

    # Sort posts by date descending
    posts.sort(key=lambda x: x["date"], reverse=True)
    
    # Generate post pages
    for post in posts:
        post_content = post_tmpl.replace("{{ title }}", post["title"]) \
                                .replace("{{ date }}", post["formatted_date"]) \
                                .replace("{{ body }}", post["body"])
        
        # Build category tags
        cat_html = ""
        for cat in post["categories"]:
            cat_html += f'<a href="/Faultplane/categories/{cat}.html" class="category-tag">{cat}</a> '
        post_content = post_content.replace("{{ categories }}", cat_html)
        
        full_html = base_tmpl.replace("{{ title }}", f"{post['title']} - Faultplane") \
                             .replace("{{ content }}", post_content)
        
        (DIST_DIR / "posts" / f"{post['slug']}.html").write_text(full_html, encoding="utf-8")
        
    # Categorize posts
    category_map = {}
    for post in posts:
        for cat in post["categories"]:
            if cat not in category_map:
                category_map[cat] = []
            category_map[cat].append(post)

    # Helper function to generate paginated indexes
    def generate_paginated_index(post_list, base_url, title, folder):
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
                prev_link = f"{base_url.split('/')[-1]}.html" if page == 2 else f"{base_url.split('/')[-1]}-{page-1}.html"
                pagination_html += f'<a href="{prev_link}">&laquo; Prev</a>'
            if page < total_pages:
                next_link = f"{base_url.split('/')[-1]}-{page+1}.html"
                pagination_html += f'<a href="{next_link}">Next &raquo;</a>'
            pagination_html += '</div>'
            
            page_content = index_tmpl.replace("{{ feed }}", feed_html) \
                                     .replace("{{ pagination }}", pagination_html) \
                                     .replace("{{ title_header }}", title)
            
            full_html = base_tmpl.replace("{{ title }}", f"{title} - Faultplane") \
                                 .replace("{{ content }}", page_content)
            
            filename = f"{base_url.split('/')[-1]}.html" if page == 1 else f"{base_url.split('/')[-1]}-{page}.html"
            (folder / filename).write_text(full_html, encoding="utf-8")

    # Generate main index
    generate_paginated_index(posts, "/Faultplane/index", "Intelligence Feed", DIST_DIR)
    
    # Generate category indexes
    for cat, cat_posts in category_map.items():
        generate_paginated_index(cat_posts, f"/Faultplane/categories/{cat}", f"Category: {cat}", DIST_DIR / "categories")

    print(f"Build complete! Generated {len(posts)} posts in {DIST_DIR}.")

if __name__ == "__main__":
    build_site()
