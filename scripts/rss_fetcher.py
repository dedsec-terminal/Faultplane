import os
import re
import json
import yaml
import time
import hashlib
import logging
from pathlib import Path
from datetime import datetime, timezone
import urllib.parse

import feedparser
import requests

from groq_client import GroqClient
from quote import get_random_quote

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "config" / "feeds.yaml"
STATE_FILE = BASE_DIR / "data" / "rss_state.json"
CONTENT_DIR = BASE_DIR / "content" / "posts"

CONTENT_DIR.mkdir(parents=True, exist_ok=True)
(BASE_DIR / "data").mkdir(parents=True, exist_ok=True)

def load_feeds():
    if not CONFIG_FILE.exists():
        logger.error(f"Config file not found: {CONFIG_FILE}")
        return []
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []

def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"seen_urls": []}
    return {"seen_urls": []}

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def normalize_url(url):
    parsed = urllib.parse.urlparse(url)
    # Remove tracking query parameters
    query = urllib.parse.parse_qsl(parsed.query)
    clean_query = [(k, v) for k, v in query if not k.startswith("utm_")]
    parsed = parsed._replace(query=urllib.parse.urlencode(clean_query), fragment="")
    return urllib.parse.urlunparse(parsed)

def generate_slug(title, date_str):
    clean_title = re.sub(r'[^a-z0-9]+', '-', str(title).lower()).strip('-')
    if len(clean_title) > 60:
        clean_title = clean_title[:60].strip('-')
    
    date_prefix = "unknown"
    try:
        dt = datetime.fromisoformat(str(date_str).replace('Z', '+00:00'))
        date_prefix = dt.strftime("%Y-%m-%d")
    except ValueError:
        pass
        
    return f"{date_prefix}-{clean_title}"

def ask_groq_for_structured_data(groq_client, title, description, source, category):
    clean_desc = re.sub(r'<[^>]+>', '', str(description))
    if len(clean_desc) > 3000:
        clean_desc = clean_desc[:3000] + "..."
        
    system_prompt = """You are a cybersecurity intelligence summarizer.
Return ONLY a valid JSON object with the following keys:
{
  "title": "Normalized title string (max 120 chars)",
  "summary": "Concise factual summary (max 600 chars)",
  "category": "One of: threat-intel, malware, vulnerabilities, cves, data-breaches, research, campaigns, other",
  "tags": ["tag1", "tag2"]
}"""

    user_prompt = f"""Article Title: {title}
Article Description: {clean_desc}
Original Source: {source}
Fallback Category: {category}"""

    parsed = groq_client.ask_groq_json(system_prompt, user_prompt, ["title", "summary"])
    if parsed:
        parsed["category"] = groq_client.validate_category(parsed.get("category", ""), category)
    return parsed

def fallback_summary(description):
    clean_desc = re.sub(r'<[^>]+>', '', str(description))
    clean_desc = ' '.join(clean_desc.split())
    if len(clean_desc) > 500:
        clean_desc = clean_desc[:497] + "..."
    return clean_desc or "No description provided."

def fetch_feed(feed_config, session):
    url = feed_config.get("url")
    if not url:
        return []
        
    logger.info(f"Fetching feed: {feed_config['name']} ({url})")
    try:
        response = session.get(url, timeout=15)
        response.raise_for_status()
        feed_data = feedparser.parse(response.content)
        return feed_data.entries
    except Exception as e:
        logger.error(f"Failed to fetch {feed_config['name']}: {e}")
        return []

def main():
    logger.info("Starting RSS Pipeline...")
    
    groq_client = GroqClient()
    ai_available = groq_client.validate_models()
    if not ai_available:
        logger.warning("AI Configuration unavailable. Falling back to rule-based ingestion.")

    feeds = load_feeds()
    state = load_state()
    seen_urls = set(state.get("seen_urls", []))
    
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Faultplane-RSS/1.0"})
    
    new_items = []
    
    for feed in feeds:
        if not feed.get("enabled", True):
            continue
            
        entries = fetch_feed(feed, session)
        added_count = 0
        
        # Process up to 3 items per feed per run to balance coverage across categories
        for entry in entries[:3]:
            raw_url = entry.get("link", "")
            if not raw_url:
                continue
                
            norm_url = normalize_url(raw_url)
            if norm_url in seen_urls:
                continue
                
            raw_title = entry.get("title", "Untitled").strip()
            
            # Parse date
            published_parsed = entry.get("published_parsed") or entry.get("updated_parsed")
            if published_parsed:
                dt = datetime(*published_parsed[:6], tzinfo=timezone.utc)
                orig_date_str = dt.isoformat()
            else:
                orig_date_str = datetime.now(timezone.utc).isoformat()
                
            # Use current ingestion time so it always gets pushed to the front of the feed
            date_str = datetime.now(timezone.utc).isoformat()
            
            # Small sleep to ensure unique timestamps for sorting
            time.sleep(0.1)
                
            raw_description = entry.get("description", "") or entry.get("summary", "")
            clean_overview = fallback_summary(raw_description)
            
            logger.info(f"Processing new item: {raw_title}")
            
            groq_data = None
            if ai_available:
                groq_data = ask_groq_for_structured_data(groq_client, raw_title, raw_description, feed["name"], feed.get("category", "other"))
            
            if groq_data:
                final_title = groq_data.get("title", raw_title)
                final_summary = groq_data.get("summary", clean_overview)
                final_category = groq_data.get("category", feed.get("category", "other"))
                final_tags = groq_data.get("tags", [final_category])
            else:
                final_title = raw_title
                final_summary = clean_overview
                final_category = feed.get("category", "other")
                final_tags = [final_category]
                
            slug = generate_slug(final_title, date_str)
            
            new_items.append({
                "title": final_title,
                "description": final_summary[:150].replace('\n', ' ') + "...",
                "source": feed["name"],
                "source_url": norm_url,
                "ingested_date": date_str,
                "published": orig_date_str,
                "category": final_category,
                "tags": final_tags,
                "slug": slug,
                "summary": final_summary,
                "overview": clean_overview
            })
            
            seen_urls.add(norm_url)
            added_count += 1
            
            # Gentle delay to prevent 429 rate limits
            if ai_available:
                time.sleep(1.5)
            
        logger.info(f"  -> Added {added_count} new items from {feed['name']}")
        
    # Write new items to markdown with structured Executive Summary & Metadata
    for item in new_items:
        tags_yaml = "\n".join([f'  - "{t}"' for t in item['tags']])
        q_data = get_random_quote()
        quote_text = q_data.get("quote", "").replace('"', "'").replace('\n', ' ')
        quote_author = q_data.get("author", "Unknown").replace('"', "'").replace('\n', ' ')
        
        overview_section = ""
        if item.get("overview") and item["overview"] != item["summary"]:
            overview_section = f"\n**Original Description:**\n{item['overview']}\n"
            
        md_content = f"""---
title: {json.dumps(item['title'])}
description: {json.dumps(item['description'])}
source: {json.dumps(item['source'])}
source_url: {json.dumps(item['source_url'])}
date: {json.dumps(item['ingested_date'])}
category: {json.dumps(item['category'])}
tags:
{tags_yaml}
slug: {json.dumps(item['slug'])}
quote: {json.dumps(quote_text)}
quote_author: {json.dumps(quote_author)}
---

### Executive Summary
{item['summary']}

---
**Intelligence Metadata**
- **Source Publisher:** {item['source']}
- **Published Date:** {item['published']}
- **Category:** {item['category']}
{overview_section}"""
        filepath = CONTENT_DIR / f"{item['slug']}.md"
        try:
            filepath.write_text(md_content, encoding="utf-8")
        except Exception as e:
            logger.error(f"Failed to write file {filepath}: {e}")
            
    # Update state
    state["seen_urls"] = list(seen_urls)
    save_state(state)
    logger.info(f"Pipeline finished. Total new items generated: {len(new_items)}")

if __name__ == "__main__":
    main()
