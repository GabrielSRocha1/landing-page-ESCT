import os

path = r'c:\Users\danie\OneDrive\Documentos\landing page escoteiro\index.html'

with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Fix the broken replacements
content = content.replace('<p class="hero-eyebrow">? Verum Crypto Ecosystem ?</p>', '<p class="hero-eyebrow">&#10022; Verum Crypto Ecosystem &#10022;</p>')
content = content.replace('âœ¦', '&#10022;')
content = content.replace('â—†', '&#9670;')
content = content.replace('â”€', '&#9472;')

# Also try the raw bytes if the strings don't match exactly due to interpretation
# âœ¦ (U+2726): E2 9C A6
# â—† (U+25C6): E2 97 86
# â”€ (U+2500): E2 94 80

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
