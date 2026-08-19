import os
import json
import time
import logging
from pathlib import Path
from datetime import datetime, timedelta, timezone
import urllib.parse

import requests
from groq_client import GroqClient
from quote import get_random_quote

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
STATE_FILE = BASE_DIR / "data" / "cve_state.json"
CVE_DIR = BASE_DIR / "content" / "cves"
KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

CVE_DIR.mkdir(parents=True, exist_ok=True)
(BASE_DIR / "data").mkdir(parents=True, exist_ok=True)

def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"seen_cves": {}, "last_run": None}
    return {"seen_cves": {}, "last_run": None}

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def ask_groq_for_cve_summary(groq_client, cve_id, description, kev_status):
    kev_warning = "This CVE is actively exploited in the wild (CISA KEV)." if kev_status else "Not currently listed in CISA KEV."
    
    clean_desc = str(description)
    if len(clean_desc) > 3000:
        clean_desc = clean_desc[:3000] + "..."
    
    system_prompt = """You are a cybersecurity intelligence summarizer.
Return ONLY a valid JSON object with the following keys:
{
  "summary": "Concise professional impact summary (max 700 chars)",
  "tags": ["tag1", "tag2"]
}"""

    user_prompt = f"""CVE ID: {cve_id}
Original Description: {clean_desc}
KEV Status: {kev_warning}"""

    return groq_client.ask_groq_json(system_prompt, user_prompt, ["summary"])

def extract_nvd_metadata(cve_item):
    cve_data = cve_item.get("cve", {})
    cve_id = cve_data.get("id", "Unknown")
    
    # Description
    descriptions = cve_data.get("descriptions", [])
    desc = next((d.get("value") for d in descriptions if d.get("lang") == "en"), "No description provided.")
    
    # CVSS
    metrics = cve_data.get("metrics", {})
    cvss = "Unknown"
    severity = "Unknown"
    for metric_type in ["cvssMetricV31", "cvssMetricV30", "cvssMetricV2"]:
        if metric_type in metrics and len(metrics[metric_type]) > 0:
            metric_data = metrics[metric_type][0]
            cvss_data = metric_data.get("cvssData", {})
            cvss = str(cvss_data.get("baseScore", "Unknown"))
            severity = cvss_data.get("baseSeverity", metric_data.get("baseSeverity", "Unknown"))
            break
            
    published = cve_data.get("published", "")
    modified = cve_data.get("lastModified", "")
    
    return {
        "id": cve_id,
        "description": desc,
        "cvss": cvss,
        "severity": severity,
        "published": published,
        "modified": modified
    }

def main():
    logger.info("Starting Two-Source CVE Pipeline...")
    
    groq_client = GroqClient()
    ai_available = groq_client.validate_models()
    if not ai_available:
        logger.warning("AI Configuration unavailable. Falling back to raw CVE descriptions.")

    state = load_state()
    seen_cves = state.get("seen_cves", {})
    last_run = state.get("last_run")
    
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 Faultplane-CVE-Fetcher/1.0"})
    
    # 1. Fetch CISA KEV Enrichment Data
    kev_dict = {}
    try:
        logger.info("Fetching CISA KEV JSON...")
        response = session.get(KEV_URL, timeout=15)
        response.raise_for_status()
        data = response.json()
        for vuln in data.get("vulnerabilities", []):
            if "cveID" in vuln:
                kev_dict[vuln["cveID"]] = vuln.get("dateAdded", "")
    except Exception as e:
        logger.error(f"Failed to fetch CISA KEV JSON: {e}")
        
    # 2. Fetch NVD Data
    now = datetime.now(timezone.utc)
    if not last_run:
        start_date = now - timedelta(hours=12)
    else:
        try:
            start_date = datetime.fromisoformat(last_run)
            if (now - start_date).days > 90:
                start_date = now - timedelta(days=30)
        except ValueError:
            start_date = now - timedelta(hours=12)
            
    start_str = start_date.strftime("%Y-%m-%dT%H:%M:%S.000")
    end_str = now.strftime("%Y-%m-%dT%H:%M:%S.000")
    
    params = {
        "lastModStartDate": start_str,
        "lastModEndDate": end_str,
        "resultsPerPage": 30
    }
    
    logger.info(f"Fetching NVD modified CVEs from {start_str} to {end_str}...")
    try:
        nvd_response = session.get(NVD_URL, params=params, timeout=30)
        if nvd_response.status_code == 403:
             logger.warning("NVD API rate limited (403). Waiting 10s and retrying...")
             time.sleep(10)
             nvd_response = session.get(NVD_URL, params=params, timeout=30)
        nvd_response.raise_for_status()
        nvd_data = nvd_response.json()
        nvd_items = nvd_data.get("vulnerabilities", [])
    except Exception as e:
        logger.error(f"Failed to fetch NVD CVE API: {e}")
        return
        
    logger.info(f"Found {len(nvd_items)} recently modified CVEs.")
    
    processed_count = 0
    
    for item in nvd_items:
        if processed_count >= 8:
            logger.info("Reached maximum CVE processing limit for this run.")
            break
            
        meta = extract_nvd_metadata(item)
        cve_id = meta["id"]
        
        last_modified = meta["modified"]
        if cve_id in seen_cves and seen_cves[cve_id] == last_modified:
            continue
            
        logger.info(f"Processing CVE: {cve_id}")
        
        kev_date = kev_dict.get(cve_id)
        kev_status = bool(kev_date)
        
        groq_data = None
        if ai_available:
            groq_data = ask_groq_for_cve_summary(groq_client, cve_id, meta["description"], kev_status)
        
        if groq_data:
            summary = groq_data.get("summary", meta["description"])
            tags = groq_data.get("tags", ["vulnerability"])
        else:
            summary = meta["description"]
            tags = ["vulnerability"]
            
        tags_yaml = "\n".join([f'  - "{t}"' for t in tags])
        
        try:
            pub_dt = datetime.fromisoformat(meta["published"].replace("Z", "+00:00"))
            fmt_date = pub_dt.isoformat()
        except:
            fmt_date = now.isoformat()
            
        kev_yaml = ""
        if kev_status:
            kev_yaml = f'kev: true\nkev_added: "{kev_date}"\n'
            
        q_data = get_random_quote()
        quote_text = q_data.get("quote", "").replace('"', "'").replace('\n', ' ')
        quote_author = q_data.get("author", "Unknown").replace('"', "'").replace('\n', ' ')
            
        md_content = f"""---
title: {json.dumps(cve_id)}
description: {json.dumps(summary[:150] + "...")}
source: "NVD"
source_url: "https://nvd.nist.gov/vuln/detail/{cve_id}"
date: {json.dumps(fmt_date)}
category: "cves"
cve: {json.dumps(cve_id)}
cvss: {json.dumps(str(meta['cvss']))}
severity: {json.dumps(str(meta['severity']))}
{kev_yaml}tags:
{tags_yaml}
slug: {json.dumps(cve_id.lower())}
quote: {json.dumps(quote_text)}
quote_author: {json.dumps(quote_author)}
---

### Executive Summary
{summary}

---
**Authoritative CVE Metadata**
- **CVSS Base Score:** {meta['cvss']} ({meta['severity']})
- **Published:** {meta['published']}
- **Last Modified:** {meta['modified']}
"""
        if kev_status:
            md_content += f"\n> [!CAUTION]\n> **Known Exploited Vulnerability:** YES (CISA KEV Added: {kev_date})\n"

        md_content += f"\n**Original Description:**\n{meta['description']}\n"

        filepath = CVE_DIR / f"{cve_id}.md"
        try:
            filepath.write_text(md_content, encoding="utf-8")
            seen_cves[cve_id] = last_modified
            processed_count += 1
        except Exception as e:
            logger.error(f"Failed to write file {filepath}: {e}")
            
        if ai_available:
            time.sleep(1.5)
            
    # Update state
    state["seen_cves"] = seen_cves
    state["last_run"] = (now - timedelta(minutes=5)).isoformat()
    save_state(state)
    logger.info(f"CVE Pipeline finished. Processed {processed_count} CVEs.")

if __name__ == "__main__":
    main()
