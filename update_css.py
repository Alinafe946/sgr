import re
import os

# Get the directory
base_dir = r"c:\Users\ALINAFE BANDA\Desktop\SGR"

# Update dev.html
dev_file = os.path.join(base_dir, "dev.html")
with open(dev_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the style block and add CSS link
content = re.sub(
    r'<title>SGR-The developer</title>\s*<style>.*?</style>',
    '<link rel="stylesheet" href="styles.css">\n        <title>SGR-The developer</title>',
    content,
    flags=re.DOTALL
)

# Add classes to divs
content = content.replace('<div id="head">', '<div id="head" class="head-developer">')
content = re.sub(
    r'<div id="content">\s*<h2>Contact Info:</h2>',
    '<div id="content" class="dev-content">\n            <h2>Contact Info:</h2>',
    content
)

with open(dev_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('dev.html updated successfully')

# Update mcode files
mcode_dir = os.path.join(base_dir, "mcode")
mcode_files = [
    "anakonda.html", "drillPakwawo.html", "gonjesa.html", "landLady.html",
    "muzitolere.html", "ndimakumbukira.html", "pachiweekend.html", 
    "phokoso.html", "turnUp.html", "umenibeba.html"
]

for filename in mcode_files:
    filepath = os.path.join(mcode_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove inline style and add CSS link
    content = re.sub(
        r'<style>.*?</style>',
        '<link rel="stylesheet" href="../styles.css">',
        content,
        flags=re.DOTALL
    )
    
    # Add body class
    content = content.replace('<body>', '<body class="song-page">')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'{filename} updated successfully')

print('\nAll HTML files have been updated to use the external CSS file!')
