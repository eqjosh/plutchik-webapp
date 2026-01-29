#!/usr/bin/env python3
"""
Convert CSV translation file to JSON format for Plutchik webapp
Usage: python csv-to-json.py input.csv output.json
"""

import csv
import json
import sys
from pathlib import Path


def csv_to_json(csv_file_path, json_file_path):
    """Convert CSV emotion translations to JSON format"""

    emotions_data = {}

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            emotion = row['emotion'].strip()
            emotion_type = row['type'].strip()

            # Build the emotion object based on type
            emotion_obj = {}

            if emotion_type == 'base':
                # Base emotions have petal-color, intensity, +/-intense, opposite
                emotion_obj['petal-color'] = row['petal-color'].strip()
                emotion_obj['color'] = row['color'].strip()
                emotion_obj['intensity'] = row['intensity'].strip()

                if row['+intense'].strip():
                    emotion_obj['+intense'] = row['+intense'].strip()
                if row['-intense'].strip():
                    emotion_obj['-intense'] = row['-intense'].strip()

                emotion_obj['opposite'] = row['opposite'].strip()

            elif emotion_type == 'intermediate':
                # Intermediate emotions have combo-emotion-0, combo-emotion-1, combo-explanation
                emotion_obj['color'] = row['color'].strip()
                emotion_obj['combo-emotion-0'] = row['combo-emotion-0'].strip()
                emotion_obj['combo-emotion-1'] = row['combo-emotion-1'].strip()
                emotion_obj['combo-explanation'] = row['combo-explanation'].strip()

            # Common fields for all emotions
            emotion_obj['similar-words'] = row['similar-words'].strip()
            emotion_obj['sensations'] = row['sensations'].strip()
            emotion_obj['message'] = row['message'].strip()
            emotion_obj['purpose'] = row['purpose'].strip()

            emotions_data[emotion] = emotion_obj

    # Write to JSON file with proper formatting
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(emotions_data, jsonfile, ensure_ascii=False, indent=4)

    print(f"✅ Converted {len(emotions_data)} emotions from CSV to JSON")
    print(f"   Input:  {csv_file_path}")
    print(f"   Output: {json_file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv-to-json.py input.csv output.json")
        sys.exit(1)

    csv_path = Path(sys.argv[1])
    json_path = Path(sys.argv[2])

    if not csv_path.exists():
        print(f"❌ Error: CSV file not found: {csv_path}")
        sys.exit(1)

    # Create output directory if needed
    json_path.parent.mkdir(parents=True, exist_ok=True)

    csv_to_json(csv_path, json_path)
