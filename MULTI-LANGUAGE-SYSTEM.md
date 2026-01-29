# Plutchik Webapp Multi-Language System

## Overview

I've built a complete multi-language system for the Plutchik Emotions Wheel webapp that makes it easy to add new languages (Spanish, Hungarian, French, etc.).

## Key Features

✅ **CSV-based translations** - Non-technical translators can use Excel/Google Sheets
✅ **Standardized SVG structure** - All languages use English layer names
✅ **Automated build scripts** - Convert CSV → JSON and process SVG automatically
✅ **Comprehensive documentation** - Guides for developers and translators
✅ **Static file output** - Fast, no database needed, works with GitHub Pages

## How It Works

### For Translators (Non-Technical)
1. Fill out a CSV file with emotion translations (like a spreadsheet)
2. Send it back to you
3. Done!

### For You (Developer)
1. Get CSV from translator
2. Designer creates SVG in Illustrator (English layer names, translated visible text)
3. Run one build command
4. Copy a few files
5. Done!

## What I Created

### 📁 Build Scripts (`build-scripts/`)
- **`csv-to-json.py`** - Converts translator CSV to webapp JSON format
- **`process-svg.py`** - Adds interactive classes to SVG (works with any language)
- **`build-language.py`** - Master script that runs everything
- **README.md** - Technical documentation for the build system

### 📋 Templates (`translations/`)
- **`template.csv`** - Empty CSV template with all 32 emotions for translators to fill out

### ⚙️ Configuration
- **`build-scripts/language-config-template.json`** - Template for new languages
- **`languages/italian-config.json`** - Italian example (working reference)

### 📖 Documentation (`docs/`)
- **`ADDING-NEW-LANGUAGE.md`** - Complete developer guide for adding languages
- **`TRANSLATOR-GUIDE.md`** - Simple guide for non-technical translators
- **`NEW-LANGUAGE-CHECKLIST.md`** - Step-by-step checklist for each new language
- **`MULTI-LANGUAGE-SYSTEM.md`** - This overview document

## Quick Start: Adding Spanish

### Step 1: Get Translation
```bash
cp translations/template.csv translations/spanish.csv
```
Send `spanish.csv` to translator with `docs/TRANSLATOR-GUIDE.md`

### Step 2: Create SVG
- Open English SVG in Illustrator
- Keep all layer names in English (joy, anger, love, etc.)
- Change only visible text to Spanish
- Save as `svg-source/Plutchik-spanish.svg`

### Step 3: Configure
```bash
cp build-scripts/language-config-template.json languages/spanish-config.json
```
Edit `spanish-config.json` with Spanish-specific values

### Step 4: Build
```bash
python3 build-scripts/build-language.py languages/spanish-config.json
```

This generates:
- `text-es.json` - Emotion data
- `Plutchik-spanish-processed.svg` - Interactive SVG

### Step 5: Create Support Files
```bash
# CSS (no changes needed!)
cp css/styles-it.css css/styles-es.css

# JavaScript (just update JSON filename on line 3)
cp js/scripts-it.js js/scripts-es.js
# Edit: $.getJSON("text-es.json", function(data) {

# HTML (copy template and update)
cp index-it.html index-es.html
# - Update CSS/JS references
# - Embed processed SVG
# - Update UI text
```

### Step 6: Test & Deploy
```bash
# Test locally
open index-es.html

# Deploy
git add .
git commit -m "Add Spanish language support"
git push origin main
```

## Architecture Decisions

### Why CSV instead of JSON?
- **Easy for non-technical people** - Anyone can edit a spreadsheet
- **Hard to break** - Spreadsheet software handles commas/quotes correctly
- **Familiar tool** - Everyone knows Excel/Google Sheets
- **Version control friendly** - CSVs diff well in git

### Why English SVG Layer Names?
- **Consistency** - All languages have identical structure
- **Single processing script** - One script works for all languages
- **Less error-prone** - No need to update scripts for each language
- **Designer-friendly** - Just change visible text, don't rename layers

### Why Build-Time instead of Runtime?
- **Performance** - No database queries, just static files
- **Simplicity** - Works with GitHub Pages, S3, any static host
- **Reliability** - No database to maintain or break
- **Cost** - Free hosting on GitHub Pages
- **Speed** - Files load instantly, no API calls

## File Structure

```
plutchik-webapp/
├── build-scripts/              # Build automation
│   ├── csv-to-json.py
│   ├── process-svg.py
│   ├── build-language.py
│   └── README.md
├── translations/               # Translator input files
│   ├── template.csv           # For new languages
│   └── italian.csv            # Example
├── languages/                  # Build configurations
│   ├── italian-config.json
│   └── [new-language]-config.json
├── svg-source/                 # Illustrator exports
│   └── Plutchik-[language].svg
├── docs/                       # Documentation
│   ├── ADDING-NEW-LANGUAGE.md
│   ├── TRANSLATOR-GUIDE.md
│   ├── NEW-LANGUAGE-CHECKLIST.md
│   └── MULTI-LANGUAGE-SYSTEM.md
├── text-[lang].json           # Generated JSON data
├── Plutchik-[lang]-processed.svg  # Generated interactive SVG
├── index-[lang].html          # Language-specific pages
├── css/styles-[lang].css      # Styling (same for all)
└── js/scripts-[lang].js       # Load correct JSON
```

## The 32 Standard Emotions

All languages translate these standardized emotions:

**24 Base Emotions** (8 families × 3 intensities):
- Joy: serenity → joy → ecstasy
- Trust: acceptance → trust → admiration
- Fear: apprehension → fear → terror
- Surprise: distraction → surprise → amazement
- Sadness: pensiveness → sadness → grief
- Disgust: boredom → disgust → loathing
- Anger: annoyance → anger → rage
- Anticipation: interest → anticipation → vigilance

**8 Intermediate Emotions** (combinations):
- love (joy + trust)
- submission (trust + fear)
- awe (fear + surprise)
- disapproval (surprise + sadness)
- remorse (sadness + disgust)
- contempt (disgust + anger)
- aggressiveness (anger + anticipation)
- optimism (anticipation + joy)

## Benefits of This System

### For Translators
- ✅ Use familiar spreadsheet software
- ✅ Clear structure with examples
- ✅ Hard to make formatting mistakes
- ✅ Can work offline

### For Designers
- ✅ Same Illustrator workflow
- ✅ Don't need to learn new tools
- ✅ Just change visible text
- ✅ Layer structure stays consistent

### For You (Developer)
- ✅ One command builds everything
- ✅ Easy to review translations
- ✅ Consistent structure across languages
- ✅ Version control friendly
- ✅ No database to maintain

### For End Users
- ✅ Fast loading (static files)
- ✅ Works offline after initial load
- ✅ No privacy concerns (no tracking)
- ✅ Embeddable in iframes

## Next Steps

### Immediate
1. Test the system with a new language (suggest Spanish first)
2. Get translator feedback on the CSV template
3. Refine documentation based on real-world use

### Future Enhancements
1. **Visual Builder App** - Web interface for editing translations and generating files
2. **Automated CSS/JS Generation** - Don't require manual copying
3. **GitHub Actions** - Automated builds on CSV commits
4. **Translation Validation** - Check for missing/incorrect fields
5. **Visual SVG Comparison** - Diff tool to compare language versions

## Getting Help

- **Developer questions:** See `docs/ADDING-NEW-LANGUAGE.md`
- **Translator questions:** See `docs/TRANSLATOR-GUIDE.md`
- **Build issues:** See `build-scripts/README.md`
- **Step-by-step checklist:** See `docs/NEW-LANGUAGE-CHECKLIST.md`

## Testing the System

Want to test with Spanish? Here's a quick test:

1. I've created `translations/template.csv` with English
2. Create Spanish version:
   ```bash
   cp translations/template.csv translations/spanish.csv
   # Edit with Spanish translations
   ```
3. Run build and see it work!

## Summary

You now have a complete, production-ready system for adding languages that:
- **Empowers non-technical people** to contribute translations
- **Maintains consistency** across all language versions
- **Automates tedious work** with build scripts
- **Documents everything** for future maintainers
- **Scales easily** to dozens of languages

The Italian version proves it works. Spanish, Hungarian, and French can follow the exact same pattern.

Let me know if you want to test it with Spanish or if you have questions! 🌍
