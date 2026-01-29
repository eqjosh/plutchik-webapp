#!/usr/bin/env python3
"""
Process Plutchik SVG with standardized English layer names and add interactive classes
This script works with any language - the layer names in the SVG should always be in English,
only the visible text should be in the target language.

Usage: python process-svg.py input.svg output.svg
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

# Register SVG namespace
ET.register_namespace('', 'http://www.w3.org/2000/svg')

# Standardized English layer names for base emotions (24)
BASE_EMOTIONS = [
    'serenity', 'joy', 'ecstasy',
    'acceptance', 'trust', 'admiration',
    'apprehension', 'fear', 'terror',
    'distraction', 'surprise', 'amazement',
    'pensiveness', 'sadness', 'grief',
    'boredom', 'disgust', 'loathing',
    'annoyance', 'anger', 'rage',
    'interest', 'anticipation', 'vigilance'
]

# Standardized English layer names for intermediate/combination emotions (8)
INTERMEDIATE_EMOTIONS = [
    'aggressiveness', 'optimism', 'contempt',
    'awe', 'love', 'remorse',
    'disapproval', 'submission'
]

# Emotions that have double background shapes (need special handling)
DOUBLE_BACKGROUND_EMOTIONS = ['annoyance', 'apprehension']


def process_svg(input_path, output_path):
    """Process SVG and add interactive classes"""

    # Parse the SVG file
    tree = ET.parse(input_path)
    root = tree.getroot()

    all_emotions = BASE_EMOTIONS + INTERMEDIATE_EMOTIONS
    processed_count = 0

    # Process each emotion
    for emotion in all_emotions:
        # Find the group with this ID
        groups = root.findall(f".//*[@id='{emotion}']")

        if not groups:
            print(f"⚠️  Could not find layer: {emotion}")
            continue

        group = groups[0]
        print(f"✓ Found: {emotion}")

        # Determine if this is an intermediate emotion
        is_intermediate = emotion in INTERMEDIATE_EMOTIONS

        # Add classes to the group element
        current_class = group.get('class', '')
        new_classes = f"{current_class} emotion-container {emotion}".strip()
        group.set('class', new_classes)

        # For intermediate emotions, check if there's a rect (clickable target area)
        rects = group.findall('.//{http://www.w3.org/2000/svg}rect')
        if rects and is_intermediate:
            target_rect = rects[0]
            # Add white background class for clickability
            target_rect.set('class', 'intermediate-word-bounding-box')
            print(f"  → Added bounding box class to rect")

        # Find the first path (the petal shape) and add classes
        paths = group.findall('.//{http://www.w3.org/2000/svg}path')
        if paths:
            petal_path = paths[0]
            current_path_class = petal_path.get('class', '')

            if is_intermediate:
                # For intermediate emotions, first path is part of the text/graphic
                new_path_class = f"{current_path_class} intermediate-letter {emotion}".strip()
            else:
                # For base emotions, add petal-shape, filled-shape, and emotion-color classes
                new_path_class = f"{current_path_class} petal-shape filled-shape {emotion}-color {emotion}".strip()

            petal_path.set('class', new_path_class)
            print(f"  → Added classes to {'graphic path' if is_intermediate else 'petal shape'}")

        # Add a class to text paths
        text_paths = paths[1:] if len(paths) > 1 else []

        for text_path in text_paths:
            current_text_class = text_path.get('class', '')

            if is_intermediate:
                # Intermediate emotions get "intermediate-letter {emotion}" classes
                if 'intermediate-letter' not in current_text_class:
                    new_text_class = f"{current_text_class} intermediate-letter {emotion}".strip()
                    text_path.set('class', new_text_class)
            else:
                # Base emotions get "central-letter" class
                if 'central-letter' not in current_text_class:
                    new_text_class = f"{current_text_class} central-letter".strip()
                    text_path.set('class', new_text_class)

        if text_paths:
            letter_type = "intermediate" if is_intermediate else "text"
            print(f"  → Added classes to {len(text_paths)} {letter_type} paths")

        processed_count += 1

    print(f"\n✅ Processed {processed_count} emotions")

    # Special fix for emotions with double background shapes
    print(f"\n🔧 Applying double-background fix for {', '.join(DOUBLE_BACKGROUND_EMOTIONS)}...")
    for emotion in DOUBLE_BACKGROUND_EMOTIONS:
        groups = root.findall(f".//*[@id='{emotion}']")
        if not groups:
            print(f"⚠️  Could not find: {emotion}")
            continue

        group = groups[0]
        print(f"✓ Fixing: {emotion}")

        # Find the nested group that contains the two background shapes
        nested_groups = group.findall('./{http://www.w3.org/2000/svg}g')
        if nested_groups:
            bg_group = nested_groups[0]  # First nested group has the backgrounds

            # Get all paths in this group
            paths = bg_group.findall('./{http://www.w3.org/2000/svg}path')

            if len(paths) >= 2:
                # Second path needs to be changed from central-letter to filled-shape
                second_path = paths[1]

                current_class = second_path.get('class', '')
                if 'central-letter' in current_class:
                    # Replace central-letter with petal-shape filled-shape
                    new_class = current_class.replace('central-letter', f'petal-shape filled-shape {emotion}-color {emotion}')
                    second_path.set('class', new_class)
                    print(f"  → Fixed second background path")

    # Write the modified SVG
    tree.write(output_path, encoding='utf-8', xml_declaration=True)
    print(f"\n✅ Saved to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process-svg.py input.svg output.svg")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.exists():
        print(f"❌ Error: Input SVG file not found: {input_path}")
        sys.exit(1)

    # Create output directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)

    process_svg(input_path, output_path)
