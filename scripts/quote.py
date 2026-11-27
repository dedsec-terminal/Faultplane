import json
import logging
import random
from pathlib import Path

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"
QUOTES_FILE = DATA_DIR / "quotes.json"

DEFAULT_QUOTE = {
    "quote": "Vision without action is a daydream. Action without vision is a nightmare.",
    "author": "Japanese proverb",
}


def load_quotes():
    """Load, sanitize, and deduplicate curated quotes from disk."""
    quotes = []
    seen = set()
    try:
        if QUOTES_FILE.exists():
            with open(QUOTES_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, list):
                for item in data:
                    if not isinstance(item, dict):
                        continue
                    raw_text = (
                        item.get("quote")
                        or item.get("text")
                        or item.get("content")
                        or item.get("quoteText")
                    )
                    raw_author = (
                        item.get("author")
                        or item.get("by")
                        or item.get("source")
                        or item.get("quoteAuthor")
                    )

                    if not isinstance(raw_text, str):
                        continue
                    clean_quote = raw_text.replace(" \ufffd ", " — ").replace("\ufffd", "—").strip()
                    if not clean_quote:
                        continue

                    key = clean_quote.casefold()
                    if key in seen:
                        continue
                    seen.add(key)

                    clean_author = (
                        raw_author.strip()
                        if isinstance(raw_author, str) and raw_author.strip()
                        else "Unknown"
                    )
                    quotes.append({"quote": clean_quote, "author": clean_author})
    except Exception as e:
        logger.warning(f"Failed to load quotes from {QUOTES_FILE}: {e}")

    if not quotes:
        logger.warning("No quotes loaded, falling back to default quote.")
        quotes.append(DEFAULT_QUOTE)

    return quotes


QUOTES_CACHE = load_quotes()


def get_random_quote():
    """Return a random quote dictionary with 'quote' and 'author' keys."""
    if not QUOTES_CACHE:
        return DEFAULT_QUOTE
    return random.choice(QUOTES_CACHE)


if __name__ == "__main__":
    print(json.dumps(get_random_quote(), indent=2))
