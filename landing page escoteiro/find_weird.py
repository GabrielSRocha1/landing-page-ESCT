import re

def find_weird_chars():
    with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find all contiguous non-ascii characters excluding standard html entities
    # we just look for characters > 127
    weird = set()
    for match in re.findall(r'[^\x00-\x7F]+', content):
        weird.add(match)
        
    with open('more_emojis.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(weird))

if __name__ == '__main__':
    find_weird_chars()
