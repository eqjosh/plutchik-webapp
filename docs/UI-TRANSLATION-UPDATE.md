# UI Translation System - UPDATE

## What Changed

I added a **second CSV file** system for translating UI text (page title, links, buttons) separately from emotions.

## The Two-File System

Each language now has:

### 1. Emotions CSV (`translations/[language].csv`)
- 32 emotions with all their data
- Rarely changes
- Example: `translations/italian.csv`

### 2. UI Text CSV (`translations/ui-[language].csv`) ← **NEW!**
- Page title, link text, button text
- Easier to update
- Can have language-specific URLs
- Example: `translations/ui-italian.csv`

## What I Created

### 📄 New Files

**Templates:**
- `translations/ui-template.csv` - Empty template for translators
- `translations/ui-italian.csv` - Italian example (working reference)

**Build Script:**
- `build-scripts/ui-csv-to-json.py` - Converts UI CSV → JSON

**Documentation:**
- `docs/UI-TRANSLATION-GUIDE.md` - Complete guide to UI translation system
- Updated `docs/TRANSLATOR-GUIDE.md` - Now mentions both files

**Updated:**
- `build-scripts/build-language.py` - Now processes both CSV files
- `build-scripts/language-config-template.json` - Includes UI file paths
- `languages/italian-config.json` - Updated with UI file references

### 🧪 Tested

Generated `ui-text-it.json` successfully from the Italian CSV:
```json
{
    "page_title": {
        "text": "Modello di Plutchik - Emozioni",
        "url": null
    },
    "eq_what_text": {
        "text": "Cos'è l'Intelligenza Emotiva?",
        "url": "https://www.youtube.com/watch?v=7iB__2vYMxM"
    },
    ...
}
```

## How It Works

### For Translators:
1. Fill out TWO CSV files:
   - `spanish.csv` (emotions)
   - `ui-spanish.csv` (page text)
2. Send both back to you

### For You:
1. Run build script (processes both CSVs):
   ```bash
   python3 build-scripts/build-language.py languages/spanish-config.json
   ```
   This generates:
   - `text-es.json` (emotions)
   - `ui-text-es.json` (UI text) ← **NEW!**
   - `Plutchik-spanish-processed.svg`

2. Apply UI text to HTML - **Three options:**

   **Option A: Ask Claude Code (Easiest)**
   ```
   "Update index-es.html using the text from ui-text-es.json"
   ```
   Claude reads the JSON and updates all UI elements automatically.

   **Option B: Manual Copy-Paste**
   - Open `ui-text-es.json`
   - Copy text into HTML manually
   - Update links

   **Option C: Build a Script** (Future)
   - Automate HTML generation from JSON
   - One command does everything

## UI CSV Format

The UI CSV has these fields:

```csv
key,text,url,description
page_title,Plutchik Emotions Wheel,,Browser tab title
learn_more_heading,Learn more:,,Heading above resource links
eq_what_text,What is Emotional Intelligence?,https://www.youtube.com/watch?v=...,Video link
cta_intro,Want to start training your EQ?,,Call-to-action
cta_link_text,Start with the Practicing EQ Book,https://6seconds.org/...,CTA link
```

**All 7 keys to translate:**
1. `page_title` - Browser tab title
2. `learn_more_heading` - "Learn more:" heading
3. `eq_what_text` - "What is EQ?" video link
4. `eq_iq_text` - "EQ & IQ" video link
5. `seven_things_text` - "7 Things" article link
6. `cta_intro` - CTA intro text
7. `cta_link_text` - CTA link text

## Benefits

✅ **Easier for translators** - UI text separate from complex emotions data
✅ **Easier to update** - Change links without touching emotions
✅ **Language-specific URLs** - Italian can link to italia.6seconds.org
✅ **Flexible** - You choose how to apply: Claude Code, manual, or script
✅ **Version control friendly** - Small files, clear changes

## Example Workflow: Adding Spanish

**Translator's work:**
```
1. Fill out spanish.csv (32 emotions)
2. Fill out ui-spanish.csv (7 UI elements)
3. Send both to you
```

**Your work:**
```bash
# 1. Create config (one time)
cp build-scripts/language-config-template.json languages/spanish-config.json
# Edit: set language_code to "es", update file paths

# 2. Run build
python3 build-scripts/build-language.py languages/spanish-config.json
# Generates: text-es.json, ui-text-es.json, Plutchik-spanish-processed.svg

# 3. Copy CSS/JS templates
cp css/styles-it.css css/styles-es.css
cp js/scripts-it.js js/scripts-es.js
# Edit js/scripts-es.js line 3: $.getJSON("text-es.json", ...)

# 4. Create HTML
cp index-it.html index-es.html

# 5. Update HTML with Claude Code
"Update index-es.html:
1. Use text from ui-text-es.json for all UI elements
2. Embed the SVG from Plutchik-spanish-processed.svg
3. Update CSS reference to css/styles-es.css
4. Update JS reference to js/scripts-es.js"

# Done! Test and deploy.
```

## My Recommendation

**For now: Use Claude Code for UI updates**

It's the sweet spot between:
- ❌ Fully manual (tedious, error-prone)
- ❌ Fully automated (more complex, less flexible)
- ✅ **Claude Code** (fast, flexible, you review changes)

**Process:**
1. Translator sends CSVs
2. You run build script (generates JSONs + SVG)
3. You ask Claude Code to update HTML from JSON
4. You review and deploy

**Future:** If you're adding many languages, we can build full HTML automation.

## What to Send Translators

Send both templates:
1. `translations/template.csv` - For emotions
2. `translations/ui-template.csv` - For UI text
3. `docs/TRANSLATOR-GUIDE.md` - Instructions

Italian versions are working examples they can reference.

## Testing

Want to test? I can help you:
1. Generate a sample Spanish UI CSV
2. Show how to use Claude Code to apply it to HTML
3. Build the full automation if you prefer

Let me know what works best for your workflow! 🚀
