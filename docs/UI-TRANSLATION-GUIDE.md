# UI Translation System

## Two-File Translation Approach

Each language requires **two separate CSV files**:

1. **Emotions CSV** (`translations/[language].csv`) - The 32 emotions data
2. **UI CSV** (`translations/ui-[language].csv`) - Page text, buttons, and links

## Why Two Files?

### Emotions File
- Contains the core emotion data (32 emotions)
- Rarely changes once translated
- Same structure across all languages
- Used by JavaScript to populate the info panel

### UI File
- Contains page elements (title, links, buttons)
- May need updates when resources change
- URLs can be language-specific
- Easier for you to update without touching emotions

## UI CSV Structure

The UI CSV has these columns:

```csv
key,text,url,description
```

### Example (English):
```csv
key,text,url,description
page_title,Plutchik Emotions Wheel,,Browser tab title
learn_more_heading,Learn more:,,Heading above resource links
eq_what_text,What is Emotional Intelligence?,https://www.youtube.com/watch?v=7iB__2vYMxM,First video link
cta_intro,Want to start training your EQ?,,Call-to-action intro
cta_link_text,Start with the Practicing EQ Book,https://6seconds.org/practicing-eq-book/,CTA link
```

### Example (Italian):
```csv
key,text,url,description
page_title,Modello di Plutchik - Emozioni,,Browser tab title
learn_more_heading,Scopri di più:,,Heading above resource links
eq_what_text,Cos'è l'Intelligenza Emotiva?,https://www.youtube.com/watch?v=7iB__2vYMxM,First video link
cta_intro,Vuoi iniziare ad allenare la tua EQ?,,Call-to-action intro
cta_link_text,Inizia con il Practicing EQ Book,https://italia.6seconds.org/ebook-praticare-lintelligenza-emotiva-eq/,CTA link
```

## All UI Text Keys

Here are all the keys you need to translate:

| Key | Purpose | Has URL? |
|-----|---------|----------|
| `page_title` | Browser tab title | No |
| `learn_more_heading` | "Learn more:" heading | No |
| `eq_what_text` | "What is Emotional Intelligence?" link | Yes |
| `eq_iq_text` | "EQ & IQ" link | Yes |
| `seven_things_text` | "7 Things About Emotions" link | Yes |
| `cta_intro` | Call-to-action intro text | No |
| `cta_link_text` | Call-to-action link text | Yes |

## Build Process

When you run the build script, it:

1. Converts emotions CSV → `text-[lang].json`
2. Converts UI CSV → `ui-text-[lang].json`
3. Processes SVG

Then you (or Claude Code) use the `ui-text-[lang].json` to update the HTML manually.

## Workflow: Updating UI Text

### Option 1: Manual Update (Current)
1. Translator sends you `ui-spanish.csv`
2. Run: `python3 build-scripts/ui-csv-to-json.py translations/ui-spanish.csv ui-text-es.json`
3. Open `ui-text-es.json` and manually copy text into `index-es.html`

### Option 2: Use Claude Code
1. Get the UI JSON file
2. Ask Claude Code: "Update index-es.html with the text from ui-text-es.json"
3. Claude updates all the UI elements automatically

### Option 3: Automated HTML Generation (Future)
Create a script that:
- Takes the UI JSON
- Takes the processed SVG
- Generates complete HTML automatically

## Example: Updating Italian Page

You have:
- `ui-text-it.json` with translations

To update `index-it.html`:

```
You: "Update index-it.html using the text from ui-text-it.json"

Claude will:
1. Read ui-text-it.json
2. Update <title> tag with page_title
3. Update "Learn more:" heading with learn_more_heading
4. Update video/article link texts and URLs
5. Update CTA text and links
```

## Managing Language-Specific URLs

Some languages have localized content:

**English:**
- 6seconds.org
- Video: youtube.com/watch?v=...

**Italian:**
- italia.6seconds.org
- Same YouTube videos (no Italian version)

**Spanish (hypothetical):**
- 6seconds.org (no Spanish subdomain)
- Spanish YouTube videos available
- Update URLs in ui-spanish.csv

## Adding New UI Elements

If you want to add new UI text in the future:

1. Add a new row to `ui-template.csv`
2. Add the same row to all language files
3. Update `ui-csv-to-json.py` if special handling needed
4. Update HTML to use the new key

## Current Limitations

The UI JSON is generated but **not automatically applied to HTML**. You need to:
- Manually update HTML, or
- Use Claude Code to apply updates, or
- Build an HTML generator script (future enhancement)

This gives you flexibility to review changes before they go live.

## Future Enhancement: Full Automation

Possible future workflow:

```bash
python3 build-scripts/build-language.py languages/spanish-config.json --full

# Would generate:
# - text-es.json (emotions)
# - ui-text-es.json (UI)
# - Plutchik-spanish-processed.svg
# - index-es.html (fully generated!)
# - css/styles-es.css (copied from template)
# - js/scripts-es.js (with correct JSON reference)
```

Everything automated, zero manual steps.

## Summary

**Current state:**
- ✅ Emotions CSV → JSON (automated)
- ✅ UI CSV → JSON (automated)
- ⚠️ JSON → HTML (manual or with Claude Code)

**Why this approach:**
- Gives you control over HTML changes
- Easy to review before deploying
- Flexible for custom modifications
- Simple to understand and debug

**For now:**
Just send UI text updates to Claude Code and ask it to update the HTML. Fast and easy! 🚀
