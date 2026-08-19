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
                frontmatter = yaml.safe_load(parts[1]) or {}
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
            parsed_date = datetime.fromisoformat(str(date_str).replace("Z", "+00:00"))
            formatted_date = parsed_date.strftime("%Y-%m-%d %H:%M")
        except ValueError:
            formatted_date = str(date_str)
            
        published = frontmatter.get("published")
        published_formatted = ""
        if published:
            if isinstance(published, datetime):
                published = published.isoformat()
            try:
                pub_dt = datetime.fromisoformat(str(published).replace("Z", "+00:00"))
                published_formatted = pub_dt.strftime("%b %d, %Y %H:%M UTC")
            except ValueError:
                published_formatted = str(published)
                
        ingested_at = frontmatter.get("ingested_at")
        ingested_formatted = ""
        if ingested_at:
            if isinstance(ingested_at, datetime):
                ingested_at = ingested_at.isoformat()
            try:
                ing_dt = datetime.fromisoformat(str(ingested_at).replace("Z", "+00:00"))
                ingested_formatted = ing_dt.strftime("%b %d, %Y %H:%M UTC")
            except ValueError:
                ingested_formatted = str(ingested_at)

        category = str(frontmatter.get("category", "other")).lower().strip()
        tags = frontmatter.get("tags", [])

        # Persistent quote from frontmatter — never mutate existing posts
        quote = frontmatter.get("quote")
        quote_author = frontmatter.get("quote_author")

        item = {
            "title": frontmatter.get("title", "Untitled"),
            "date": str(date_str),
            "formatted_date": formatted_date,
            "published": str(published) if published else None,
            "published_formatted": published_formatted,
            "ingested_at": str(ingested_at) if ingested_at else None,
            "ingested_formatted": ingested_formatted,
            "category": category,
            "tags": tags,
            "slug": slug,
            "body": html_body,
            "type": "post" if directory == POSTS_DIR else "cve",
            "quote": quote,
            "quote_author": quote_author or "Unknown",
            "source": frontmatter.get("source"),
            "source_url": frontmatter.get("source_url")
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
    all_content.sort(key=lambda x: x.get("ingested_at") or x["date"], reverse=True)
    posts.sort(key=lambda x: x.get("ingested_at") or x["date"], reverse=True)
    cves.sort(key=lambda x: x["date"], reverse=True)
    
    # Generate content.json for search
    search_index = []
    for item in all_content:
        search_index.append({
            "title": item["title"],
            "url": item["url"],
            "date": item["date"],
            "published": item.get("published"),
            "ingested_at": item.get("ingested_at"),
            "category": item["category"],
            "tags": item["tags"]
        })
    (DATA_DIR / "content.json").write_text(json.dumps(search_index), encoding="utf-8")
    
    # Generate individual pages
    for item in all_content:
        quote_html = ""
        if item.get("quote"):
            author = item.get("quote_author") or "Unknown"
            quote_html = f'\n<blockquote class="post-quote"><p>"{item["quote"]}"</p><cite>&mdash; {author}</cite></blockquote>\n'
            
        source_html = ""
        if item.get("source_url"):
            source_name = item.get("source") or "Original Article"
            source_html = f'\n<div class="post-source"><strong>Source:</strong> <a href="{item["source_url"]}" target="_blank" rel="noopener noreferrer">{source_name}</a></div>\n'
            
        date_html = ""
        if item.get("published") and item.get("ingested_at"):
            date_html = f'<span class="date">Published: {item["published_formatted"]}</span>\n            <span class="date">Ingested: {item["ingested_formatted"]}</span>'
        else:
            date_html = f'<span class="date">{item["formatted_date"]}</span>'

        post_content = post_tmpl.replace("{{ title }}", item["title"]) \
                                .replace("{{ date_html }}", date_html) \
                                .replace("{{ body }}", item["body"]) \
                                .replace("{{ quote_html }}", quote_html) \
                                .replace("{{ source_html }}", source_html)
        
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
            if not page_posts:
                feed_html += '<li class="empty-state">No articles found in this category.</li>'
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
    
    # Generate Category indexes (Threat Intel, Malware, Data Breaches, Research, etc.)
    # Guarantee the core categories exist even if empty
    core_categories = ["threat-intel", "malware", "data-breaches", "research", "cves"]
    for core_cat in core_categories:
        if core_cat not in category_map:
            category_map[core_cat] = []
            
    for cat, cat_items in category_map.items():
        pretty_title = cat.replace("-", " ").title()
        generate_paginated_index(cat_items, f"/Faultplane/categories/{cat}", f"Category: {pretty_title}", DIST_DIR / "categories", filename_base=cat)

    # Generate custom Landing Page (index.html)
    def render_list(items, limit=4):
        if not items:
            return '<p class="empty-state">No recent activity found for this category.</p>'
        html = '<ul class="post-list">'
        for p in items[:limit]:
            html += f'<li><span class="post-meta">{p["formatted_date"]}</span> <a href="{p["url"]}">{p["title"]}</a></li>\n'
        html += '</ul>'
        return html
        
    threat_intel = category_map.get("threat-intel", [])
    malware = category_map.get("malware", [])
    breaches = category_map.get("data-breaches", [])
    research = category_map.get("research", [])
    
    landing_content = landing_tmpl.replace("{{ latest_intel }}", render_list(threat_intel, 4)) \
                                  .replace("{{ latest_cves }}", render_list(cves, 4)) \
                                  .replace("{{ latest_malware }}", render_list(malware, 4)) \
                                  .replace("{{ latest_breaches }}", render_list(breaches, 4)) \
                                  .replace("{{ latest_research }}", render_list(research, 4))
                                  
    full_landing = base_tmpl.replace("{{ title }}", "Faultplane - Cyber Threat Intelligence") \
                            .replace("{{ content }}", landing_content)
                            
    (DIST_DIR / "index.html").write_text(full_landing, encoding="utf-8")

    print(f"Build complete! Generated {len(all_content)} items in {DIST_DIR}.")

if __name__ == "__main__":
    build_site()
