import re

def fix():
    path = "index.html"
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    replacements = {
        'ðŸŒ ': '&#127760;', 
        'ðŸ”—': '&#128279;', 
        'ðŸ  ': '&#128640;', 
        'ðŸ —ï¸ ': '&#127959;&#65039;', 
        'ðŸŽ“': '&#127891;', 
        'ðŸ”¥': '&#128293;', 
        'ðŸŒ±': '&#127793;', 
        'ðŸ“ˆ': '&#128200;', 
        'ðŸª™': '&#129689;'
    }
    
    for k, v in replacements.items():
        content = content.replace(k, v)
        
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    fix()
