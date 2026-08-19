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
    
    prompt = f"""You are a cybersecurity analyst. Read the following article title and description and generate a structured JSON response.
Do NOT invent CVEs, threat actors, malware names, or details that are not in the text.
Summarize the facts concisely.

Article Title: {title}
Article Description: {description}
Original Source: {source}
Fallback Category: {fallback_category}

Return ONLY valid JSON (no markdown wrapping) in this exact structure:
{{
  "title": "Normalized title string",
  "summary": "A 1-2 paragraph professional threat intel summary. Do not fabricate facts.",
  "category": "MUST be exactly one of: threat-intel, malware, vulnerabilities, cves, data-breaches, research, campaigns, other",
  "tags": ["tag1", "tag2"]
}}"""

    logger.info("Sending static payload to Groq...")
    parsed = client.ask_groq_json(prompt, ["title", "summary"])
    
    if not parsed:
        logger.error("Failed to get structured JSON from Groq.")
        sys.exit(1)
        
    logger.info(f"Structured output: PASS")
    
    category = parsed.get("category", "")
    valid_cat = client.validate_category(category, fallback_category)
    
    logger.info(f"Category: {valid_cat}")
    logger.info("Category validation: PASS")
    
    logger.info("Controlled test completed successfully.")
    
if __name__ == "__main__":
    main()
