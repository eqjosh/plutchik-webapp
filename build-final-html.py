#!/usr/bin/env python3
"""
Build final Italian HTML by integrating processed SVG
"""

# Read the processed Italian SVG
with open('Plutchik-italiano-processed.svg', 'r') as f:
    italian_svg_content = f.read()

# Remove XML declaration
italian_svg_content = italian_svg_content.replace('<?xml version="1.0" encoding="utf-8"?>\n', '')

# Read the original HTML template
with open('index.html', 'r') as f:
    html_content = f.read()

# Find where the SVG starts and ends
import re
svg_start = re.search(r'<svg id="Layer_1"[^>]*>', html_content)
svg_end = re.search(r'</svg>\s*</div>\s*<div class=\'words column\'>', html_content)

if not svg_start or not svg_end:
    print("Error: Could not find SVG boundaries")
    exit(1)

# Extract parts
html_before = html_content[:svg_start.start()]
html_after = html_content[svg_end.start():]

# Fix the closing - need to find the actual </svg> tag
html_after = '</svg>' + html_after[html_after.find('</svg>') + 6:]

# Build the new HTML
new_html = html_before
new_html += italian_svg_content
new_html += html_after

# Make Italian-specific changes
new_html = new_html.replace('<title>Colorful Picture</title>', '<title>Modello di Plutchik - Emozioni</title>')
new_html = new_html.replace('css/styles.css', 'css/styles-it.css')
new_html = new_html.replace(
    'https://6secus.s3.amazonaws.com/website/plutchik-webapp-testing/plutchik-webapp/text.json',
    'text-it.json'
)
new_html = new_html.replace('Click any word to explore', 'Fai clic su una parola per esplorare')
new_html = new_html.replace(
    'Use this interactive Plutchik\'s Model to learn more about your emotions!',
    'Usa questo Modello interattivo di Plutchik per saperne di più sulle tue emozioni!'
)
new_html = new_html.replace('Similar words:', 'Parole simili:')
new_html = new_html.replace('Typical sensations:', 'Sensazioni tipiche:')
new_html = new_html.replace('What is', 'Cosa ti dice')
new_html = new_html.replace('telling you?', '?')
new_html = new_html.replace('How can', 'Come può')
new_html = new_html.replace('help you?', 'aiutarti?')
new_html = new_html.replace('Change Intensity', 'Cambia Intensità')
new_html = new_html.replace('Intensity:', 'Intensità:')
new_html = new_html.replace('Explore the opposite:', 'Esplora l\'opposto:')
new_html = new_html.replace('Learn more:', 'Per saperne di più:')

# Write the final HTML
with open('index-it-final.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("✅ Created index-it-final.html")
print("✅ Fully integrated Italian Plutchik webapp!")
