#!/usr/bin/env python3
"""
Generate language-specific HTML file from template
Usage: python generate-html.py config.json
"""

import json
import sys
from pathlib import Path
from string import Template


def generate_html(config_path):
    """Generate HTML file from template and config"""

    # Load configuration
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    lang_code = config['language_code']
    lang_name = config['language_name']

    print(f"🌍 Generating HTML for: {lang_name} ({lang_code})")

    # Read the HTML template
    template_path = Path(__file__).parent / 'template.html'
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # Create Template object
    template = Template(template_content)

    # Substitute variables
    html_content = template.substitute(
        LANG_CODE=lang_code,
        LANG_NAME=lang_name,
        PAGE_TITLE=config.get('page_title', f'Plutchik Emotions Wheel - {lang_name}'),
        EQ_QUESTION=config.get('eq_question', 'What is Emotional Intelligence?'),
        EQ_VIDEO_URL=config.get('eq_video_url', 'https://www.youtube.com/watch?v=7iB__2vYMxM'),
        IQ_EQ_QUESTION=config.get('iq_eq_question', 'IQ & EQ'),
        IQ_EQ_VIDEO_URL=config.get('iq_eq_video_url', 'https://www.youtube.com/watch?v=5-6mHyFJhno'),
        SEVEN_THINGS_QUESTION=config.get('seven_things_question', '7 Things About Emotions'),
        SEVEN_THINGS_URL=config.get('seven_things_url', 'https://6seconds.org/2020/06/03/7-things-emotions-know/'),
        CTA_TEXT=config.get('cta_text', 'Want to start training your EQ? Start with the Practicing EQ Book'),
        CTA_URL=config.get('cta_url', 'https://6seconds.org/practicing-eq-book/'),
        LEARN_MORE_TEXT=config.get('learn_more_text', 'Learn more:')
    )

    # Write output HTML
    output_path = Path(config['output_html'])
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✅ Generated: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate-html.py config.json")
        sys.exit(1)

    config_path = Path(sys.argv[1])

    if not config_path.exists():
        print(f"❌ Error: Config file not found: {config_path}")
        sys.exit(1)

    generate_html(config_path)
