# Adding a New Language to the Plutchik Webapp

This guide explains how to add a new language version of the Plutchik Emotions Wheel webapp.

## Overview

The multi-language system uses a build-time approach where each language has:
- A CSV file with emotion translations (easy for non-technical translators)
- An SVG file with translated visible text (created in Adobe Illustrator)
- Generated JSON, processed SVG, and HTML files

## Quick Start

### 1. Prepare the Translation CSV

Copy the template and fill in translations:

```bash
cp translations/template.csv translations/spanish.csv
```

Edit `translations/spanish.csv` with translations for all 32 emotions (24 base + 8 intermediate).

**CSV Structure:**
- Each row is one emotion
- Columns: `emotion`, `type`, `intensity`, `petal-color`, `color`, `+intense`, `-intense`, `opposite`, `similar-words`, `sensations`, `message`, `purpose`
- For intermediate emotions, also fill: `combo-emotion-0`, `combo-emotion-1`, `combo-explanation`

**Important Notes:**
- Use semicolons (`;`) to separate multiple words in `similar-words` field
- The `emotion` column should contain the emotion name in your target language
- Keep `petal-color` and `color` hex codes the same as the template (these are standardized)
- The `type` should be either `base` or `intermediate`

### 2. Create the SVG in Adobe Illustrator

**Critical: Use English layer names!**

1. Open the English SVG template in Adobe Illustrator
2. **DO NOT rename any layers** - keep all layer names in English (e.g., "joy", "anger", "love")
3. Only change the visible text to your target language
4. Save as SVG: `svg-source/Plutchik-[language].svg`

**Why English layer names?**
The processing script looks for standardized English layer names. This ensures all language versions have the same structure and can be processed with the same script.

**Layer naming reference:**
- Base emotions: `serenity`, `joy`, `ecstasy`, `acceptance`, `trust`, `admiration`, `apprehension`, `fear`, `terror`, `distraction`, `surprise`, `amazement`, `pensiveness`, `sadness`, `grief`, `boredom`, `disgust`, `loathing`, `annoyance`, `anger`, `rage`, `interest`, `anticipation`, `vigilance`
- Intermediate emotions: `aggressiveness`, `optimism`, `contempt`, `awe`, `love`, `remorse`, `disapproval`, `submission`

### 3. Create Language Configuration

Create a config file in `languages/[language]-config.json`:

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
    "learn_more": "Aprende más:",
    "eq_question": "¿Qué es la Inteligencia Emocional?",
    "eq_video_url": "https://www.youtube.com/watch?v=...",
    "iq_eq_question": "CI & CE",
    "iq_eq_video_url": "https://www.youtube.com/watch?v=...",
    "seven_things_question": "7 Cosas Sobre las Emociones",
    "seven_things_url": "https://...",
    "cta_text": "¿Quieres empezar a entrenar tu CE?",
    "cta_link_text": "Comienza con el Libro Practicing EQ",
    "cta_url": "https://..."
  }
}
```

### 4. Run the Build Script

```bash
cd /Users/joshuafreedman/Documents/plutchik-webapp
python3 build-scripts/build-language.py languages/spanish-config.json
```

This will:
1. Convert your CSV to JSON format
2. Process your SVG to add interactive classes
3. Output the files you need

### 5. Create CSS and JS Files

**CSS File** (`css/styles-[language].css`):

Copy `css/styles-it.css` as a template and update:
- No changes needed! The CSS uses standardized English class names
- Just copy: `cp css/styles-it.css css/styles-es.css`

**JS File** (`js/scripts-[language].js`):

Copy `js/scripts-it.js` and update line 3 to load your JSON:
```javascript
$.getJSON("text-es.json", function(data) {
```

### 6. Create HTML File

Copy `index-it.html` as a template:

```bash
cp index-it.html index-es.html
```

Update the following in `index-es.html`:
1. Line 8: Change page title
2. Line 13: Update CSS reference to `css/styles-es.css`
3. Line 27-800+: Replace the entire `<svg>` element with contents from your processed SVG
4. Lines 882-901: Update UI text with translations from your config's `ui_text`
5. Line 909: Update JS reference to `js/scripts-es.js`

**How to embed the SVG:**
1. Open `Plutchik-spanish-processed.svg` in a text editor
2. Copy everything from `<svg ...>` to `</svg>`
3. Replace the corresponding section in your HTML file

### 7. Test Your Language Version

Open `index-es.html` in a browser and verify:
- ✅ All emotion names appear in your language
- ✅ Clicking on emotions shows the info panel
- ✅ Info panel text is in your language
- ✅ Intermediate emotions are gray by default
- ✅ Hovering shows colors for all emotions
- ✅ Links in the footer work correctly

## File Structure

```
plutchik-webapp/
├── build-scripts/
│   ├── csv-to-json.py           # Converts CSV to JSON
│   ├── process-svg.py            # Adds interactive classes to SVG
│   ├── build-language.py         # Master build script
│   └── language-config-template.json
├── translations/
│   ├── template.csv              # Empty template for translators
│   ├── italian.csv               # Italian translations
│   └── spanish.csv               # Your new language
├── languages/
│   ├── italian-config.json       # Italian build configuration
│   └── spanish-config.json       # Your new language config
├── svg-source/
│   ├── Plutchik-italiano.svg     # Italian source (English layer names)
│   └── Plutchik-spanish.svg      # Your new language source
├── text-it.json                  # Generated Italian JSON
├── text-es.json                  # Generated Spanish JSON
├── Plutchik-italiano-processed.svg
├── Plutchik-spanish-processed.svg
├── index-it.html
├── index-es.html
├── css/
│   ├── styles-it.css
│   └── styles-es.css
└── js/
    ├── scripts-it.js
    └── scripts-es.js
```

## Standardization Rules

### ✅ DO:
- Use English layer names in all SVGs
- Keep emotion names consistent with Plutchik's model
- Use the CSV template for translations
- Keep hex color codes consistent across languages
- Test thoroughly before deploying

### ❌ DON'T:
- Don't rename SVG layers to your target language
- Don't edit JSON files directly (use CSV instead)
- Don't change color schemes
- Don't add or remove emotions from the standard 32

## Troubleshooting

### "Could not find layer: [emotion]"
- Check that your SVG layers use English names exactly as listed above
- Layer names are case-sensitive: use `joy` not `Joy`

### Emotions not appearing
- Verify your SVG was processed correctly
- Check that the SVG is properly embedded in HTML
- Ensure CSS file is linked correctly

### Info panel shows English instead of your language
- Check that your JSON file is being loaded in the JS file
- Verify emotion names in JSON match the SVG layer names
- Open browser console (F12) to check for JavaScript errors

### Intermediate emotions not clickable
- The SVG processing script should have added `intermediate-word-bounding-box` class to rects
- Verify the processed SVG has these classes

## Tips for Translators

1. **Use Natural Language**: Don't translate word-for-word; use natural expressions in your language
2. **Gender Neutrality**: Try to use gender-neutral forms where possible
3. **Cultural Appropriateness**: Adapt emotion descriptions to be culturally appropriate
4. **Consistency**: Use consistent terminology throughout all 32 emotions
5. **Review**: Have a native speaker review your translations

## Example: Adding Spanish

1. Create `translations/spanish.csv` with all translations
2. Create Spanish SVG in Illustrator (English layer names, Spanish visible text)
3. Create `languages/spanish-config.json`
4. Run: `python3 build-scripts/build-language.py languages/spanish-config.json`
5. Copy CSS and update JS
6. Copy HTML template and embed processed SVG
7. Test and deploy!

## Getting Help

If you run into issues:
1. Check this documentation
2. Look at the Italian version as a working example
3. Verify all file paths in your config are correct
4. Check that Python scripts have execute permissions: `chmod +x build-scripts/*.py`

## Builder App (Future)

A visual builder app for managing translations is planned. This will provide:
- Web interface for editing translations
- Visual SVG editor
- One-click build and deploy
- Translation validation

For now, the CSV + build script approach provides a solid foundation that non-technical translators can use with basic spreadsheet software.
