import os
import json
import time
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

try:
    from groq import Groq
    import groq
except ImportError:
    Groq = None

logger = logging.getLogger(__name__)

VALID_CATEGORIES = {"threat-intel", "malware", "vulnerabilities", "cves", "data-breaches", "research", "campaigns", "other"}

class GroqClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.primary_model = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")
        self.fallback_model = os.getenv("GROQ_FALLBACK_MODEL", "llama-3.1-8b-instant")
        self.active_model = None
        self.client = None

    def validate_models(self):
        if not self.api_key:
            logger.error("GROQ_API_KEY not found in environment.")
            return False
        
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            resp = requests.get("https://api.groq.com/openai/v1/models", headers=headers, timeout=10)
            if resp.status_code == 401 or resp.status_code == 403:
                logger.error("Groq API authentication failed. Check GROQ_API_KEY.")
                return False
                
            resp.raise_for_status()
            
            models = [m["id"] for m in resp.json().get("data", [])]
            if self.primary_model in models:
                logger.info(f"Primary Groq model '{self.primary_model}' is available.")
                self.active_model = self.primary_model
            else:
                logger.warning(f"Primary Groq model '{self.primary_model}' unavailable; attempting fallback.")
                if self.fallback_model in models:
                    logger.info(f"Fallback Groq model '{self.fallback_model}' is available.")
                    self.active_model = self.fallback_model
                else:
                    logger.error("Neither primary nor fallback Groq models are available. Aborting AI pipeline.")
                    return False
                    
            self.client = Groq(api_key=self.api_key)
            return True
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Network failure while validating Groq models: {e}")
            return False

    def validate_category(self, cat_str, fallback_category):
        cat = str(cat_str).lower().strip()
        if cat in VALID_CATEGORIES:
            return cat
            
        cat = cat.replace(" ", "-")
        if cat in VALID_CATEGORIES:
            return cat
            
        logger.warning(f"Invalid category '{cat_str}' returned by Groq. Falling back to '{fallback_category}'.")
        
        fallback = str(fallback_category).lower().strip()
        if fallback in VALID_CATEGORIES:
            return fallback
            
        return "other"

    def ask_groq_json(self, system_prompt, user_prompt, required_fields, retry_on_400=True):
        if not self.client or not self.active_model:
            return None
            
        max_retries = 3
        current_model = self.active_model
        
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=current_model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.1,
                    max_tokens=800,
                    response_format={"type": "json_object"}
                )
                
                content = response.choices[0].message.content.strip()
                parsed = json.loads(content)
                
                for field in required_fields:
                    if not parsed.get(field):
                        logger.error(f"Missing required field '{field}' in Groq JSON response.")
                        return None
                        
                return parsed
                
            except groq.BadRequestError as e:
                err_msg = str(e)
                if "json_validate_failed" in err_msg or "Failed to validate JSON" in err_msg or "Failed to generate JSON" in err_msg:
                    logger.warning(f"Groq API JSON validation failed (400).")
                    if retry_on_400:
                        logger.warning("Retrying with a simpler JSON prompt (once)...")
                        simplified_system = system_prompt + "\n\nCRITICAL: Return ONLY a valid JSON object. No markdown, no reasoning, no extra text. Do not exceed maximum tokens."
                        return self.ask_groq_json(simplified_system, user_prompt, required_fields, retry_on_400=False)
                    else:
                        logger.error("JSON validation failed again on retry. Aborting for this item.")
                        return None
                else:
                    logger.warning(f"Groq API Bad Request (400): {e}")
                    return None
                    
            except groq.RateLimitError as e:
                logger.warning(f"Groq API rate limit (429) hit. Retrying {attempt+1}/{max_retries}...")
                time.sleep(5 * (attempt + 1))
                continue
                
            except groq.NotFoundError as e:
                logger.warning(f"Model '{current_model}' not found (404).")
                if current_model != self.fallback_model:
                    logger.warning(f"Switching to fallback model '{self.fallback_model}'.")
                    current_model = self.fallback_model
                    self.active_model = self.fallback_model
                    continue
                else:
                    logger.error("Fallback model also not found. Aborting for this item.")
                    return None
                    
            except Exception as e:
                logger.warning(f"Groq API generation failed: {e}")
                return None
                
        return None
