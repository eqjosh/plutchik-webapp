# Plutchik Webapp Build Scripts

This directory contains scripts for building multi-language versions of the Plutchik Emotions Wheel webapp.

## Scripts Overview

### 1. `csv-to-json.py`
Converts translator-friendly CSV files to JSON format used by the webapp.

**Usage:**
```bash
python3 csv-to-json.py translations/spanish.csv text-es.json
```

**Input:** CSV file with emotion translations
**Output:** JSON file in webapp format

### 2. `process-svg.py`
Processes SVG files exported from Illustrator, adding interactive CSS classes.

**Usage:**
```bash
python3 process-svg.py svg-source/Plutchik-spanish.svg Plutchik-spanish-processed.svg
```

**What it does:**
- Finds emotion layers by English names
- Adds `emotion-container` class to groups
- Adds `petal-shape`, `filled-shape`, `{emotion}-color` classes to base emotions
- Adds `intermediate-letter` class to intermediate emotions
- Adds `intermediate-word-bounding-box` class to clickable rects
- Fixes double-background emotions (annoyance, apprehension)

**Important:** SVG layers must have standardized English names!

### 3. `build-language.py`
Master build script that orchestrates the entire build process.

**Usage:**
```bash
python3 build-language.py languages/spanish-config.json
```

**What it does:**
1. Reads language configuration
2. Converts CSV → JSON
3. Processes SVG → adds classes
4. Outputs summary of generated files

## Configuration Files

Language configurations are stored in `../languages/` directory.

**Example:** `languages/spanish-config.json`
```json
{
  "language_code": "es",
  "language_name": "Spanish",
  "page_title": "Rueda de Emociones de Plutchik",
  "csv_file": "translations/spanish.csv",
  "json_file": "text-es.json",
  "svg_input": "svg-source/Plutchik-spanish.svg",
  "svg_processed": "Plutchik-spanish-processed.svg",
  "html_output": "index-es.html",
  "css_file": "css/styles-es.css",
  "js_file": "js/scripts-es.js",
  "ui_text": {
    "learn_more": "...",
    "eq_question": "...",
    ...
  }
}
```

## Workflow for Adding a New Language

1. **Translator fills out CSV:**
   ```bash
   cp translations/template.csv translations/spanish.csv
   # Translator edits spanish.csv
   ```

2. **Designer creates SVG in Illustrator:**
   - Use English layer names (joy, anger, love, etc.)
   - Only change visible text to target language
   - Export as SVG to `svg-source/Plutchik-spanish.svg`

3. **Create configuration file:**
   ```bash
   cp build-scripts/language-config-template.json languages/spanish-config.json
   # Edit with language-specific values
   ```

4. **Run build script:**
   ```bash
   python3 build-scripts/build-language.py languages/spanish-config.json
   ```

5. **Create CSS and JS files:**
   ```bash
   cp css/styles-it.css css/styles-es.css
   cp js/scripts-it.js js/scripts-es.js
   # Update line 3 in scripts-es.js to load text-es.json
   ```

6. **Create HTML file:**
   ```bash
   cp index-it.html index-es.html
   # Update CSS/JS references
   # Embed processed SVG
   # Update UI text
   ```

7. **Test and deploy!**

## File Dependencies

```
CSV Translation
    ↓
[csv-to-json.py]
    ↓
JSON Data
    ↓
  (loaded by JS)
    ↓
Webapp

SVG Source (Illustrator)
    ↓
[process-svg.py]
    ↓
Processed SVG
    ↓
  (embedded in HTML)
    ↓
Webapp
```

## Standard Emotion Names (English)

These are the layer names that MUST be used in all SVG files:

**Base Emotions (24):**
- serenity, joy, ecstasy
- acceptance, trust, admiration
- apprehension, fear, terror
- distraction, surprise, amazement
- pensiveness, sadness, grief
- boredom, disgust, loathing
- annoyance, anger, rage
- interest, anticipation, vigilance

**Intermediate Emotions (8):**
- aggressiveness, optimism, contempt, awe
- love, remorse, disapproval, submission

## Requirements

- Python 3.6+
- No additional packages needed (uses only standard library)

## Troubleshooting

### CSV conversion fails
- Check CSV encoding (should be UTF-8)
- Verify all required columns are present
- Check for stray commas inside fields

### SVG processing fails
- Verify layer names are in English
- Check that layers are properly named groups in Illustrator
- Ensure SVG is saved with proper settings from Illustrator

### Build script can't find files
- Check all paths in config are relative to project root
- Verify files exist at specified paths
- Check file permissions

## Future Enhancements

### Planned:
- Automatic CSS generation from JSON color data
- Automatic JS generation with proper JSON reference
- HTML template with variable substitution
- Builder web app for visual editing
- Validation scripts to check translations
- Automated testing for each language

### Consider:
- GitHub Actions for automated builds
- Translation memory for consistency across languages
- Visual diff tool for comparing SVGs
- Emoji support in translations

## Contributing

When adding new build scripts:
1. Follow the existing naming convention
2. Add comprehensive docstrings
3. Include usage examples in comments
4. Update this README
5. Test with multiple languages

## License

Same as main project.
