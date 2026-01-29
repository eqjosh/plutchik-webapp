#!/usr/bin/env python3
"""
Script to integrate Italian SVG with interactive webapp structure
"""

import re

# Read the Italian SVG
with open('Plutchik-italiano.svg', 'r') as f:
    italian_svg = f.read()

# Read the original HTML to get the wrapper structure
with open('index.html', 'r') as f:
    original_html = f.read()

# Extract the HTML wrapper (everything before and after the SVG)
# Find where SVG starts and ends in original
svg_start_match = re.search(r'<svg[^>]*id="Layer_1"', original_html)
svg_end_match = re.search(r'</svg>\s*</div>\s*<div', original_html)

if not svg_start_match or not svg_end_match:
    print("Error: Could not find SVG boundaries in original HTML")
    exit(1)

html_before_svg = original_html[:svg_start_match.start()]
html_after_svg_match = re.search(r'</svg>', original_html[svg_end_match.start():])
html_after_svg = original_html[svg_end_match.start() + html_after_svg_match.end():]

# Extract just the SVG content from Italian file (remove XML declaration)
italian_svg_content = re.sub(r'<\?xml[^>]*\?>\s*', '', italian_svg)

# Now we need to add interactive classes to the Italian SVG
# Map of colors to emotion names (based on the petal fill colors)
color_emotion_map = {
    '#ffed9f': 'serenità',  # serenity - lightest yellow
    '#ffdc7b': 'gioia',      # joy - medium yellow
    '#ffca05': 'estasi',     # ecstasy - bright yellow
    '#cadf8b': 'accettazione', # acceptance - light green
    '#abd26a': 'fiducia',    # trust - medium green
    '#8ac650': 'ammirazione', # admiration - bright green
    '#7ac698': 'apprensione', # apprehension - light teal
    '#30b575': 'paura',      # fear - medium green-teal
    '#00a551': 'terrore',    # terror - dark green
    '#89c7e4': 'distrazione', # distraction - light blue
    '#36aed7': 'sorpresa',   # surprise - medium blue
    '#0099cd': 'stupore',    # amazement - bright blue
    '#a0c0e5': 'pensierosità', # pensiveness - light blue-purple
    '#74a8da': 'tristezza',  # sadness - medium blue
    '#2983c5': 'angoscia',   # grief - dark blue
    '#b9aad3': 'noia',       # boredom - light purple
    '#a390c4': 'disgusto',   # disgust - medium purple
    '#8973b3': 'odio',       # loathing - dark purple
    '#f48d80': 'irritazione', # annoyance - light red
    '#f2736d': 'rabbia',     # anger - medium red
    '#f05b61': 'collera',    # rage - bright red
    '#fcc487': 'interesse',  # interest - light orange
    '#f9ad66': 'aspettativa', # anticipation - medium orange
    '#f6923d': 'vigilanza',  # vigilance - bright orange
}

# Intermediate emotions
intermediate_color_map = {
    '#f3774f': 'aggressività',
    '#fbae21': 'ottimismo',
    '#bd678a': 'disprezzo',
    '#009f8f': 'soggezione',
    '#c5c82b': 'amore',
    '#597bbc': 'rimorso',
    '#158ec9': 'disapprovazione',
    '#45b651': 'sottomissione',
}

print("Italian SVG integration script")
print(f"Found {len(color_emotion_map)} base emotion colors")
print(f"Found {len(intermediate_color_map)} intermediate emotion colors")

# For now, just output the structure - we'll need to manually add classes
# based on visual inspection of the paths

print("\nTo complete integration, you need to:")
print("1. Identify emotion petal paths in Italian SVG by their position/color")
print("2. Add classes like 'petal-shape emotion-container serenità' to those paths")
print("3. Wrap emotion label text paths in <svg class='emotion-container serenità'>  groups")

print("\nCreating basic HTML structure...")

# Create new HTML with Italian title
new_html = html_before_svg
new_html = new_html.replace('<title>Colorful Picture</title>', '<title>Emozioni di Plutchik</title>')
new_html = new_html.replace('css/styles.css', 'css/styles-it.css')
new_html += italian_svg_content
new_html += html_after_svg

# Update the text.json reference to text-it.json
new_html = new_html.replace(
    'https://6secus.s3.amazonaws.com/website/plutchik-webapp-testing/plutchik-webapp/text.json',
    'text-it.json'
)

# Write out the new HTML
with open('index-it-new.html', 'w') as f:
    f.write(new_html)

print("\nBasic structure written to index-it-new.html")
print("Manual work needed: Add interactive classes to SVG paths")
