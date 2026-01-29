#!/usr/bin/env python3
"""
Convert UI text CSV to JSON format
Usage: python ui-csv-to-json.py input.csv output.json
"""

import csv
import json
import sys
from pathlib import Path


def ui_csv_to_json(csv_file_path, json_file_path):
    """Convert UI CSV to JSON format"""

    ui_data = {}

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            key = row['key'].strip()
            text = row['text'].strip()
            url = row['url'].strip()

            # Store both text and URL
            ui_data[key] = {
                'text': text,
                'url': url if url else None
            }

    # Write to JSON file
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(ui_data, jsonfile, ensure_ascii=False, indent=4)

    print(f"✅ Converted {len(ui_data)} UI elements from CSV to JSON")
    print(f"   Input:  {csv_file_path}")
    print(f"   Output: {json_file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ui-csv-to-json.py input.csv output.json")
        sys.exit(1)

    csv_path = Path(sys.argv[1])
    json_path = Path(sys.argv[2])

    if not csv_path.exists():
        print(f"❌ Error: CSV file not found: {csv_path}")
        sys.exit(1)

    # Create output directory if needed
    json_path.parent.mkdir(parents=True, exist_ok=True)

    ui_csv_to_json(csv_path, json_path)
