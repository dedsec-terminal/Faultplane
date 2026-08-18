import os
import re
import json
import logging
import hashlib
from pathlib import Path
from datetime import datetime, timezone

import feedparser
import requests
import trafilatura
from concurrent.futures import ThreadPoolExecutor

from quote import get_random_quote

try:
    from groq import Groq
except Exception:
    Groq = None

import ahocorasick

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content" / "posts"
SEEN_FILE = BASE_DIR / ".seen_posts.json"
CHECKPOINT_FILE = BASE_DIR / ".rss_checkpoint.json"

CONTENT_DIR.mkdir(parents=True, exist_ok=True)

RSS_FEEDS = [
    "https://feeds.feedburner.com/TheHackersNews",
    "https://krebsonsecurity.com/feed/",
    "https://www.bleepingcomputer.com/feed/",
    "https://securelist.com/feed/",
    "https://www.schneier.com/feed/atom/",
    "https://www.wired.com/feed/category/security/rss",
    "https://databreaches.net/feed/",
    "https://www.cisa.gov/cybersecurity-advisories/all.xml",
    "https://www.cisa.gov/uscert/ncas/alerts.xml",
    "https://www.zerodayinitiative.com/rss/published/",
    "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml",
    "https://blog.talosintelligence.com/feeds/posts/default",
    "https://unit42.paloaltonetworks.com/feed/",
    "https://cloud.google.com/blog/topics/threat-intelligence/rss/",
    "https://www.darkreading.com/rss.xml",
    "https://www.securityweek.com/feed/",
    "https://www.helpnetsecurity.com/feed/",
    
]

MIN_POSTS_PER_CATEGORY = 3

CATEGORY_KEYWORDS = {
    "threat-intel": [
        # Threat actors / campaigns
        "apt", "threat actor", "threat group",
        "campaign", "espionage", "nation-state",
        "actor", "intrusion", "compromise",
        "operation", "targeted attack",
        "cyberattack", "attacker", "threat intelligence",
        "iocs", "ttp", "kill chain",
        "command and control", "c2",
        "lateral movement", "credential theft",
        "initial access", "persistence",

        # Common actor names
        "lazarus", "apt28", "apt29",
        "cozy bear", "fancy bear",
        "sandworm", "mustang panda",
        "kimsuky", "volt typhoon",
        "ghostwriter", "lockbit",
        "black basta", "clop"
    ],

    "data-breaches": [
        "breach", "data breach",
        "leak", "data leak",
        "exposed", "exposure",
        "database leak", "database exposed",
        "compromised", "customer data",
        "records exposed", "unauthorized access",
        "credential leak", "sensitive information",
        "stolen data", "dumped",
        "hack exposed", "privacy incident",
        "information disclosure",
        "pii", "personally identifiable information",
        "email addresses leaked",
        "password dump", "ransom payment"
    ],

    "cves": [
        "cve-", "vulnerability",
        "zero-day", "0day",
        "exploit", "exploited",
        "actively exploited",
        "rce", "remote code execution",
        "privilege escalation",
        "kev", "known exploited vulnerability",
        "security flaw", "patch",
        "patch tuesday",
        "authentication bypass",
        "sandbox escape",
        "command injection",
        "sql injection",
        "xss", "csrf",
        "memory corruption",
        "buffer overflow",
        "arbitrary code execution",
        "use-after-free",
        "heap overflow",
        "kernel flaw",
        "firmware flaw"
    ],

    "malware": [
        "malware", "ransomware",
        "trojan", "worm",
        "rootkit", "spyware",
        "stealer", "infostealer",
        "dropper", "payload",
        "loader", "implant",
        "botnet", "backdoor",
        "rat", "remote access trojan",
        "keylogger", "malicious code",
        "cryptominer", "banking trojan",
        "malspam", "wiper",
        "cobalt strike", "emotet",
        "qakbot", "trickbot",
        "dridex", "darkgate",
        "lockbit", "blackcat",
        "akira", "ransom note"
    ],

    "research": [
        "research", "analysis",
        "report", "study",
        "deep dive", "technical analysis",
        "whitepaper", "findings",
        "security research",
        "investigation",
        "case study",
        "methodology",
        "benchmark",
        "statistics",
        "annual report",
        "quarterly report",
        "trend analysis",
        "forecast",
        "insights"
    ],
}

automaton = ahocorasick.Automaton()

# Combine categories for overlapping words
word_to_cats = {}
for cat, words in CATEGORY_KEYWORDS.items():
    for word in words:
        if word not in word_to_cats:
            word_to_cats[word] = []
        word_to_cats[word].append(cat)

for word, cats in word_to_cats.items():
    automaton.add_word(word, (cats, word))

automaton.make_automaton()

session = requests.Session()
session.headers.update({"User-Agent":"Mozilla/5.0"})

client = None
if Groq and os.getenv("GROQ_API_KEY"):
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        print("Groq enabled")
    except Exception:
        pass


def load_json(path, default):
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return default


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def clean_slug(title, link=None):
    slug = re.sub(r"[^a-z0-9\\s-]", "", title.lower())
    slug = re.sub(r"\\s+", "-", slug).strip("-")
    if len(slug) < 8:
        slug = "intel-" + hashlib.md5((link or title).encode()).hexdigest()[:8]
    return slug[:120]


def article_hash(link):
    return hashlib.sha256(link.encode()).hexdigest()


def parse_date(entry):
    for k in ("published_parsed", "updated_parsed"):
        if entry.get(k):
            return datetime(*entry[k][:6], tzinfo=timezone.utc)
    return datetime.now(timezone.utc)


def classify(title, text):
    content = (title + " " + text).lower()
    scores = {k:0 for k in CATEGORY_KEYWORDS}

    # words can belong to multiple categories
    # we want to count each unique word matched per category
    found_words = set()
    for end_index, (cats, word) in automaton.iter(content):
        found_words.add((tuple(cats), word))

    for cats, word in found_words:
        for cat in cats:
            scores[cat] += 1

    best = max(scores, key=scores.get)
    return best if scores[best] else "research"


def fetch_article(url):
    try:
        r = session.get(url, timeout=20)
        r.raise_for_status()
        return trafilatura.extract(r.text) or ""
    except requests.RequestException as e:
        logger.warning(f"Failed to fetch article from {url}: {e}")
        return ""
    except Exception as e:
        logger.error(f"Error processing {url}: {e}")
        return ""


def summarize(title, text):
    if not text:
        return None
    if client:
        try:
            r = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{
                    "role":"user",
                    "content":f"Summarize in 3 concise paragraphs:\\nTitle:{title}\\n{text[:10000]}"
                }],
                temperature=0.2,
                max_tokens=400
            )
            return r.choices[0].message.content.strip()
        except Exception:
            pass
    return text[:1000]


def main():
    print("Intel Balancer v4 Running")

    seen = set(load_json(SEEN_FILE, []))
    checkpoints = load_json(CHECKPOINT_FILE, {})

    category_count = {k:0 for k in CATEGORY_KEYWORDS}

    candidates = []

    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        last_seen = checkpoints.get(feed_url)

        for entry in feed.entries[:30]:
            link = entry.get("link")
            title = entry.get("title","").strip()
            if not title or not link:
                continue

            h = article_hash(link)
            if h in seen:
                continue

            published = parse_date(entry)

            if last_seen:
                try:
                    if published <= datetime.fromisoformat(last_seen):
                        continue
                except Exception:
                    pass

            raw = fetch_article(link)
            if len(raw) < 250:
                continue

            category = classify(title, raw)

            candidates.append({
                "title": title,
                "link": link,
                "published": published,
                "raw": raw,
                "category": category,
                "feed": feed_url,
                "hash": h,
            })

    candidates.sort(key=lambda x: x["published"], reverse=True)

    selected = []

    for category in category_count:
        cat_posts = [x for x in candidates if x["category"] == category]
        selected.extend(cat_posts[:MIN_POSTS_PER_CATEGORY])

    if len(selected) < MIN_POSTS_PER_CATEGORY * 5:
        remaining = [x for x in candidates if x not in selected]
        remaining.sort(key=lambda x: x["published"], reverse=True)
        selected.extend(remaining[:10])

    items_to_process = []
    temp_category_count = category_count.copy()
    for item in selected:
        cat = item["category"]
        if temp_category_count[cat] >= MIN_POSTS_PER_CATEGORY:
            continue

        slug = clean_slug(item["title"], item["link"])
        path = CONTENT_DIR / f"{slug}.md"
        if path.exists():
            continue

        items_to_process.append(item)
        temp_category_count[cat] += 1 # Pre-increment to keep count accurate while pre-selecting

    def process_item(item):
        summary = summarize(item["title"], item["raw"])
        if not summary:
            return None
        return item, summary

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(process_item, items_to_process)

    for result in results:
        if not result:
            continue

        item, summary = result
        cat = item["category"]
        slug = clean_slug(item["title"], item["link"])
        path = CONTENT_DIR / f"{slug}.md"

        markdown = f"""---
title: "{item['title'].replace('"', "'")}"
date: {item['published'].isoformat()}
draft: false
categories:
  - {cat}
author: "DedSec-Terminal"
---

{summary}

---

> *{get_random_quote()}*

Source: [{item['title']}]({item['link']})
"""

        path.write_text(markdown, encoding="utf-8")

        category_count[cat] += 1
        seen.add(item["hash"])
        checkpoints[item["feed"]] = item["published"].isoformat()

        print(f"[{cat}] {path.name}")

    save_json(SEEN_FILE, sorted(list(seen)))
    save_json(CHECKPOINT_FILE, checkpoints)

    print("\\nFinal Category Balance:")
    for k, v in category_count.items():
        print(k, v)


if __name__ == "__main__":
    main()

