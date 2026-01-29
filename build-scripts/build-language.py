#!/usr/bin/env python3
"""
Master build script for creating a language version of the Plutchik webapp
This script orchestrates all the steps needed to create a complete language version.

Usage: python build-language.py language-config.json
"""

import json
import sys
import subprocess
from pathlib import Path


def run_command(cmd, description):
    """Run a shell command and handle errors"""
    print(f"\n{'='*60}")
    print(f"📋 {description}")
    print(f"{'='*60}")

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.stdout:
        print(result.stdout)

    if result.returncode != 0:
        print(f"❌ Error: {description} failed")
        print(result.stderr)
        return False

    return True


def build_language(config_path):
    """Build a complete language version from configuration"""

    # Load configuration
    print(f"\n🌍 Loading configuration from: {config_path}")
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    lang_code = config['language_code']
    lang_name = config['language_name']

    print(f"\n{'='*60}")
    print(f"Building Plutchik Webapp: {lang_name} ({lang_code})")
    print(f"{'='*60}")

    # Get project root (parent of build-scripts)
    project_root = Path(__file__).parent.parent
    build_scripts_dir = Path(__file__).parent

    # Step 1: Convert Emotions CSV to JSON
    csv_file = project_root / config['csv_file']
    json_file = project_root / config['json_file']

    if csv_file.exists():
        cmd = f"python3 '{build_scripts_dir}/csv-to-json.py' '{csv_file}' '{json_file}'"
        if not run_command(cmd, f"Converting Emotions CSV to JSON for {lang_name}"):
            return False
    else:
        print(f"⚠️  Emotions CSV file not found: {csv_file}")
        print(f"   Skipping CSV conversion. Using existing JSON: {json_file}")

    # Step 1.5: Convert UI CSV to JSON
    ui_csv_file = project_root / config.get('ui_csv_file', '')
    ui_json_file = project_root / config.get('ui_json_file', '')

    if ui_csv_file and ui_csv_file.exists():
        cmd = f"python3 '{build_scripts_dir}/ui-csv-to-json.py' '{ui_csv_file}' '{ui_json_file}'"
        if not run_command(cmd, f"Converting UI CSV to JSON for {lang_name}"):
            return False
    else:
        if ui_csv_file:
            print(f"⚠️  UI CSV file not found: {ui_csv_file}")
            print(f"   Skipping UI CSV conversion.")

    # Step 2: Process SVG
    svg_input = project_root / config['svg_input']
    svg_processed = project_root / config['svg_processed']

    if svg_input.exists():
        cmd = f"python3 '{build_scripts_dir}/process-svg.py' '{svg_input}' '{svg_processed}'"
        if not run_command(cmd, f"Processing SVG for {lang_name}"):
            return False
    else:
        print(f"⚠️  SVG input file not found: {svg_input}")
        print(f"   Skipping SVG processing. Using existing: {svg_processed}")

    # Step 3: Generate language-specific files summary
    print(f"\n{'='*60}")
    print(f"✅ Build Complete for {lang_name}!")
    print(f"{'='*60}")
    print(f"\nGenerated files:")
    print(f"  📄 Emotions JSON: {json_file}")
    if ui_json_file and ui_json_file.exists():
        print(f"  📄 UI JSON:       {ui_json_file}")
    print(f"  🎨 SVG:           {svg_processed}")
    print(f"\nNext steps:")
    print(f"  1. Copy CSS and JS templates:")
    print(f"     cp css/styles-it.css {config['css_file']}")
    print(f"     cp js/scripts-it.js {config['js_file']}")
    print(f"  2. Update {config['js_file']} to load {config['json_file']}")
    print(f"  3. Copy HTML template:")
    print(f"     cp index-it.html {config['html_output']}")
    print(f"  4. Embed {svg_processed} into {config['html_output']}")
    print(f"  5. Update HTML references to CSS/JS files")
    if ui_json_file and ui_json_file.exists():
        print(f"\n💡 UI text is in {ui_json_file}")
        print(f"   You can use this to update the HTML manually or with a script.")

    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python build-language.py language-config.json")
        print("\nExample:")
        print("  python build-language.py languages/spanish-config.json")
        sys.exit(1)

    config_path = Path(sys.argv[1])

    if not config_path.exists():
        print(f"❌ Error: Config file not found: {config_path}")
        sys.exit(1)

    success = build_language(config_path)

    if success:
        print(f"\n🎉 Success! Language build completed.")
        sys.exit(0)
    else:
        print(f"\n❌ Build failed. Please check errors above.")
        sys.exit(1)
