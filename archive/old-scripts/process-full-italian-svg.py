#!/usr/bin/env python3
"""
Process Italian SVG with named layers and add interactive classes
"""

import re
import xml.etree.ElementTree as ET

# Register SVG namespace
ET.register_namespace('', 'http://www.w3.org/2000/svg')

# Parse the SVG file
tree = ET.parse('Plutchik-italiano-layers.svg')
root = tree.getroot()

# Define the namespace
ns = {'svg': 'http://www.w3.org/2000/svg'}

# List of emotions to process
emotions = [
    'serenità', 'gioia', 'estasi',
    'accettazione', 'fiducia', 'ammirazione',
    'apprensione', 'paura', 'terrore',
    'distrazione', 'sorpresa', 'stupore',
    'pensierosità', 'tristezza', 'angoscia',
    'noia', 'disgusto', 'odio',
    'irritazione', 'rabbia', 'collera',
    'interesse', 'aspettativa', 'vigilanza',
    'aggressività', 'ottimismo', 'disprezzo',
    'soggezione', 'amore', 'rimorso',
    'disapprovazione', 'sottomissione'
]

processed_count = 0

# Process each emotion
for emotion in emotions:
    # Find the group with this ID
    groups = root.findall(f".//*[@id='{emotion}']")

    if not groups:
        print(f"⚠️  Could not find layer: {emotion}")
        continue

    group = groups[0]
    print(f"✓ Found: {emotion}")

    # Add classes to the group element
    current_class = group.get('class', '')
    new_classes = f"{current_class} emotion-container {emotion}".strip()
    group.set('class', new_classes)

    # Find the first path (the petal shape) and add classes
    paths = group.findall('.//{http://www.w3.org/2000/svg}path')
    if paths:
        petal_path = paths[0]
        current_path_class = petal_path.get('class', '')
        # Add petal-shape, filled-shape, and emotion-color classes
        new_path_class = f"{current_path_class} petal-shape filled-shape {emotion}-color {emotion}".strip()
        petal_path.set('class', new_path_class)
        print(f"  → Added classes to petal shape")

    # Add a class to text paths
    text_paths = paths[1:] if len(paths) > 1 else []
    for text_path in text_paths:
        current_text_class = text_path.get('class', '')
        if 'central-letter' not in current_text_class:
            new_text_class = f"{current_text_class} central-letter".strip()
            text_path.set('class', new_text_class)

    if text_paths:
        print(f"  → Added classes to {len(text_paths)} text paths")

    processed_count += 1

print(f"\n✅ Processed {processed_count} emotions")

# Write the modified SVG
tree.write('Plutchik-italiano-processed.svg', encoding='utf-8', xml_declaration=True)
print("✅ Saved to: Plutchik-italiano-processed.svg")
