import os
import yaml
import re
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).resolve().parent.parent
POSTS_DIR = BASE_DIR / "content" / "posts"

def migrate_posts():
    """
    Optional script to add 'ingested_at' to legacy posts that don't have it.
    It uses the existing 'date' field as the 'ingested_at' value to preserve sorting,
    without inventing arbitrary historical timestamps.
    """
    if not POSTS_DIR.exists():
        print(f"Directory {POSTS_DIR} not found.")
        return
        
    count = 0
    for md_file in POSTS_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        
        # Check if already migrated
        if "ingested_at:" in content:
            continue
            
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter_text = parts[1]
                try:
                    frontmatter = yaml.safe_load(frontmatter_text) or {}
                except Exception as e:
                    print(f"Error parsing {md_file.name}: {e}")
                    continue
                    
                if "date" in frontmatter and "ingested_at" not in frontmatter:
                    # We inject 'ingested_at' right after 'date' using regex for safe insertion
                    # without disturbing the yaml formatting or quotes of other fields
                    date_val = frontmatter["date"]
                    
                    # Pattern to find the date line
                    pattern = r"^(date:\s*.*?)$"
                    
                    def replacer(match):
                        date_line = match.group(1)
                        # We use the raw existing date string
                        return f"{date_line}\ningested_at: \"{date_val}\""
                        
                    new_frontmatter_text = re.sub(pattern, replacer, frontmatter_text, flags=re.MULTILINE)
                    
                    if new_frontmatter_text != frontmatter_text:
                        new_content = f"---{new_frontmatter_text}---{parts[2]}"
                        md_file.write_text(new_content, encoding="utf-8")
                        count += 1
                        print(f"Migrated {md_file.name}")
                        
    print(f"Migration complete. Updated {count} files.")

if __name__ == "__main__":
    migrate_posts()
