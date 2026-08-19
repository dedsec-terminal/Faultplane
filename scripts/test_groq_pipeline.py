import os
import sys
import logging
from groq_client import GroqClient

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting controlled Groq test...")
    
    # 1. Check API Key
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        logger.error("GROQ_API_KEY is not set.")
        sys.exit(1)
        
    # 2. Init Client
    client = GroqClient()
    
    # 3. Validate Models
    logger.info("Validating Groq models...")
    if not client.validate_models():
        logger.error("Model validation failed.")
        sys.exit(1)
        
    logger.info(f"Groq connectivity: PASS")
    logger.info(f"Primary model: {client.primary_model}")
    logger.info(f"Selected model: {client.active_model}")
    
    # 4. Static mock RSS article
    title = "Test Malware Outbreak"
    description = "A new ransomware called LockTest has been observed encrypting files in the healthcare sector."
    source = "Test Feed"
    fallback_category = "other"
    
    system_prompt = """You are a cybersecurity intelligence summarizer.
Return ONLY the requested JSON object.
Summarize the supplied article accurately.
Do not invent facts.
Keep the summary concise.
Choose exactly one category from the provided taxonomy.
Return no Markdown, explanation, reasoning, or additional text.

JSON Schema (Strictly required):
{
  "title": "Normalized title string (max 120 chars)",
  "summary": "Concise factual summary (max 600 chars)",
  "category": "One of: threat-intel, malware, vulnerabilities, cves, data-breaches, research, campaigns, other",
  "tags": ["tag1", "tag2"]
}"""

    user_prompt = f"""Article Title: {title}
Article Description: {description}
Original Source: {source}
Fallback Category: {fallback_category}"""

    logger.info("Sending static payload to Groq...")
    parsed = client.ask_groq_json(system_prompt, user_prompt, ["title", "summary"])
    
    if not parsed:
        logger.error("Failed to get structured JSON from Groq.")
        sys.exit(1)
        
    logger.info(f"Structured output: PASS")
    
    category = parsed.get("category", "")
    valid_cat = client.validate_category(category, fallback_category)
    
    logger.info(f"Category: {valid_cat}")
    logger.info("Category validation: PASS")
    
    # 5. Static mock CVE article
    cve_id = "CVE-2026-9999"
    cve_desc = "A critical remote code execution vulnerability exists in TestApp 2.0 when processing crafted packets."
    kev_status = True
    kev_warning = "This CVE is actively exploited in the wild (CISA KEV)." if kev_status else "Not currently listed in CISA KEV."
    
    cve_system_prompt = """You are a cybersecurity intelligence summarizer.
Return ONLY the requested JSON object.
Summarize the supplied CVE details accurately.
Do not invent facts.
Keep the summary concise.
Return no Markdown, explanation, reasoning, or additional text.

JSON Schema (Strictly required):
{
  "summary": "Concise professional impact summary (max 700 chars)",
  "tags": ["tag1", "tag2"]
}"""

    cve_user_prompt = f"""CVE ID: {cve_id}
Original Description: {cve_desc}
KEV Status: {kev_warning}"""

    logger.info("Sending static CVE payload to Groq...")
    cve_parsed = client.ask_groq_json(cve_system_prompt, cve_user_prompt, ["summary"])
    
    if not cve_parsed:
        logger.error("Failed to get structured JSON for CVE from Groq.")
        sys.exit(1)
        
    logger.info("Structured CVE output: PASS")
    logger.info("Controlled CVE test completed successfully.")
    
    logger.info("ALL CONTROLLED TESTS PASS")
    
    logger.info("Controlled test completed successfully.")
    
if __name__ == "__main__":
    main()
