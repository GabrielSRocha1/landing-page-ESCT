def fix():
    with open('index.html', 'rb') as f:
        content = f.read()
    
    replacements = {
        bytes.fromhex('c3a2c2adc290'): b'&#11088;',
        bytes.fromhex('c3b0c5b8c28fc281'): b'&#127937;',
        bytes.fromhex('c3b0c5b8c592c290'): b'&#128144;',
        bytes.fromhex('c3a2c5a1c2a1'): b'&#9889;',
        bytes.fromhex('c3a2c5a1c2a0c3afc2b8c28f'): b'&#9888;&#65039;',
        bytes.fromhex('c3a2c5a1e284a2c3afc2b8c28f'): b'&#9881;&#65039;',
        bytes.fromhex('c3b0c5b8c28fe28094c3afc2b8c28f'): b'&#127959;&#65039;',
        bytes.fromhex('c3b0c5b8c592c28d'): b'&#128141;'
    }
    
    for k, v in replacements.items():
        content = content.replace(k, v)
        
    with open('index.html', 'wb') as f:
        f.write(content)

if __name__ == '__main__':
    fix()
