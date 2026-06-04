import re

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

print("=== Procurando icones/caracteres quebrados ===\n")

broken = []
for i, line in enumerate(lines, 1):
    # Comum mojibake patterns
    if 'â' in line or 'Ã' in line or '\ufffd' in line:
        broken.append((i, line.strip()[:120]))

print(f"Total linhas com possiveis caracteres quebrados: {len(broken)}")
print("\nAmostras:")
for lineno, text in broken[:30]:
    print(f"  Linha {lineno}: {text}")

print("\n\n=== Buscando icones especificos ===")
# Look for Font Awesome, emoji references
keywords = ['fa-', 'icon', 'emoji', '&#', '&amp;', '★', '✦', '◆', '►', '◄', '→', '←', '⬡', '⬢', '✓', '✕', '●', '○', '▶']
for kw in keywords:
    found = [(i+1, line.strip()[:100]) for i, line in enumerate(lines) if kw in line]
    if found:
        print(f"\n[{kw}] encontrado em {len(found)} linhas:")
        for ln, txt in found[:3]:
            print(f"  Linha {ln}: {txt}")
