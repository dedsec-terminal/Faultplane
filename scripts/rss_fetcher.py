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

try:
    from groq import Groq
except ImportError:
    Groq = None

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
    clean_title = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    if len(clean_title) > 60:
        clean_title = clean_title[:60].strip('-')
    
    date_prefix = "unknown"
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        date_prefix = dt.strftime("%Y-%m-%d")
    except ValueError:
        pass
        
    return f"{date_prefix}-{clean_title}"

def ask_groq_for_structured_data(title, description, source, category):
    api_key = os.getenv("GROQ_API_KEY")
    if not Groq or not api_key:
        return None
        
    prompt = f"""You are a cybersecurity analyst. Read the following article title and description and generate a structured JSON response.
Do NOT invent CVEs, threat actors, malware names, or details that are not in the text.
Summarize the facts concisely.

Article Title: {title}
Article Description: {description}
Original Source: {source}
Primary Category: {category}

Return ONLY valid JSON (no markdown wrapping) in this exact structure:
{{
  "title": "Normalized title string",
  "summary": "A 1-2 paragraph professional threat intel summary. Do not fabricate facts.",
  "tags": ["tag1", "tag2"]
}}"""

    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=500,
            response_format={"type": "json_object"}
        )
        
        content = response.choices[0].message.content.strip()
        parsed = json.loads(content)
        
        # Validation
        if not parsed.get("summary") or not parsed.get("title"):
            raise ValueError("Missing required fields in Groq JSON response.")
            
        return parsed
    except Exception as e:
        logger.warning(f"Groq API generation failed: {e}")
        return None

def fallback_summary(description):
    clean_desc = re.sub(r'<[^>]+>', '', str(description))
    if len(clean_desc) > 500:
        clean_desc = clean_desc[:497] + "..."
    return clean_desc

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
    feeds = load_feeds()
    state = load_state()
    seen_urls = set(state.get("seen_urls", []))
    
    session = requests.Session()
    session.headers.update({"User-Agent": "Faultplane-RSS/1.0"})
    
    new_items = []
    
    for feed in feeds:
        if not feed.get("enabled", True):
            continue
            
        entries = fetch_feed(feed, session)
        added_count = 0
        
        # We only process up to 5 items per feed per run to conserve Groq tokens
        for entry in entries[:5]:
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
                date_str = dt.isoformat()
            else:
                date_str = datetime.now(timezone.utc).isoformat()
                
            raw_description = entry.get("description", "") or entry.get("summary", "")
            
            logger.info(f"Processing new item: {raw_title}")
            
            # Use Groq for structured output
            groq_data = ask_groq_for_structured_data(raw_title, raw_description, feed["name"], feed.get("category", "research"))
            
            if groq_data:
                final_title = groq_data.get("title", raw_title)
                final_summary = groq_data.get("summary", fallback_summary(raw_description))
                final_tags = groq_data.get("tags", [feed.get("category", "research")])
            else:
                final_title = raw_title
                final_summary = fallback_summary(raw_description)
                final_tags = [feed.get("category", "research")]
                
            slug = generate_slug(final_title, date_str)
            
            new_items.append({
                "title": final_title,
                "description": final_summary[:150].replace('\n', ' ') + "...",
                "source": feed["name"],
                "source_url": norm_url,
                "published": date_str,
                "category": feed.get("category", "research"),
                "tags": final_tags,
                "slug": slug,
                "summary": final_summary
            })
            
            seen_urls.add(norm_url)
            added_count += 1
            
            # Rate limit Groq calls if making many
            time.sleep(1)
            
        logger.info(f"  -> Added {added_count} new items from {feed['name']}")
        
    # Write new items to markdown safely
    for item in new_items:
        tags_yaml = "\n".join([f'  - "{t}"' for t in item['tags']])
        md_content = f"""---
title: "{item['title'].replace('"', "'")}"
description: "{item['description'].replace('"', "'")}"
source: "{item['source']}"
source_url: "{item['source_url']}"
date: "{item['published']}"
category: "{item['category']}"
tags:
{tags_yaml}
slug: "{item['slug']}"
---

{item['summary']}

---
**Source:** [{item['source']}]({item['source_url']})
"""
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
