import re

def fix_all_emojis():
    with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Replace all unicode characters with code point > 8000 to their HTML entity equivalent
    fixed_content = ""
    for char in content:
        if ord(char) > 8000:
            fixed_content += f"&#{ord(char)};"
        else:
            fixed_content += char

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(fixed_content)

if __name__ == '__main__':
    fix_all_emojis()
