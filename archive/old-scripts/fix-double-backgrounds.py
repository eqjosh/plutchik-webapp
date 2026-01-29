#!/usr/bin/env python3
"""
Fix irritazione and apprensione to have both background shapes highlighted
"""
import xml.etree.ElementTree as ET

# Register namespace
ET.register_namespace('', 'http://www.w3.org/2000/svg')

# Parse the processed SVG
tree = ET.parse('Plutchik-italiano-processed.svg')
root = tree.getroot()

# For irritazione and apprensione, we need to fix the second path
# which is currently marked as "central-letter" but is actually a background shape

for emotion in ['irritazione', 'apprensione']:
    # Find the emotion group
    groups = root.findall(f".//*[@id='{emotion}']")
    if not groups:
        print(f"⚠️  Could not find: {emotion}")
        continue

    group = groups[0]
    print(f"✓ Found: {emotion}")

    # Find the nested group that contains the two background shapes
    nested_groups = group.findall('./{http://www.w3.org/2000/svg}g')
    if nested_groups:
        bg_group = nested_groups[0]  # First nested group has the backgrounds

        # Get all paths in this group
        paths = bg_group.findall('./{http://www.w3.org/2000/svg}path')

        if len(paths) >= 2:
            # First path is already correct (cls-42 or cls-9)
            # Second path needs to be changed from central-letter to filled-shape
            second_path = paths[1]

            current_class = second_path.get('class', '')
            if 'central-letter' in current_class:
                # Replace central-letter with petal-shape filled-shape
                new_class = current_class.replace('central-letter', f'petal-shape filled-shape {emotion}-color {emotion}')
                second_path.set('class', new_class)
                print(f"  → Fixed second background path")

print("\n✅ Writing updated SVG...")
tree.write('Plutchik-italiano-processed.svg', encoding='utf-8', xml_declaration=True)
print("✅ Done!")
