# Plutchik Emotions Wheel - Multi-Language Webapp

Interactive visualization of Plutchik's Wheel of Emotions in multiple languages.

## 🌍 Available Languages

- **English**: [index.html](index.html) | [Demo](https://eqjosh.github.io/plutchik-webapp/)
- **Italian**: [index-it.html](index-it.html) | [Demo](https://eqjosh.github.io/plutchik-webapp/index-it.html)
- **Spanish**: [index-es.html](index-es.html) | [Demo](https://eqjosh.github.io/plutchik-webapp/index-es.html)

## 🚀 Quick Start

### For Users
Just open any of the HTML files above in a web browser, or visit the live demo links.

### For Translators
Want to add a new language? See [docs/TRANSLATOR-GUIDE.md](docs/TRANSLATOR-GUIDE.md)

### For Developers
Want to build a new language version? See [docs/ADDING-NEW-LANGUAGE.md](docs/ADDING-NEW-LANGUAGE.md)

## 📁 Project Structure

```
plutchik-webapp/
├── index.html, index-it.html, index-es.html  # Language versions
├── text-*.json, ui-text-*.json               # Emotion & UI data
├── Plutchik-*-processed.svg                  # Processed graphics
│
├── css/                    # Stylesheets for each language
├── js/                     # JavaScript for each language
├── build-scripts/          # Build automation tools
├── translations/           # CSV source files for translators
├── svg-source/             # Original SVG files from Illustrator
├── languages/              # Language build configurations
├── docs/                   # Documentation
└── en/                     # English original version
```

## 🛠️ Adding a New Language

**Quick version:**
1. Copy `translations/template.csv` and `translations/ui-template.csv`
2. Fill in your translations (emotion data + UI text)
3. Create SVG in Illustrator with your language text (keep layer names in target language)
4. Run build script
5. Done!

**Detailed guide:** See [docs/ADDING-NEW-LANGUAGE.md](docs/ADDING-NEW-LANGUAGE.md)

## 📖 Documentation

- **[MULTI-LANGUAGE-SYSTEM.md](MULTI-LANGUAGE-SYSTEM.md)** - Complete overview of the multi-language system
- **[docs/ADDING-NEW-LANGUAGE.md](docs/ADDING-NEW-LANGUAGE.md)** - Developer guide for adding languages
- **[docs/TRANSLATOR-GUIDE.md](docs/TRANSLATOR-GUIDE.md)** - Simple guide for translators
- **[docs/UI-TRANSLATION-GUIDE.md](docs/UI-TRANSLATION-GUIDE.md)** - Guide for UI text translation
- **[docs/NEW-LANGUAGE-CHECKLIST.md](docs/NEW-LANGUAGE-CHECKLIST.md)** - Step-by-step checklist
- **[build-scripts/README.md](build-scripts/README.md)** - Build system documentation

## 🔧 Build Scripts

Located in `build-scripts/`:
- `csv-to-json.py` - Convert translator CSV to JSON
- `ui-csv-to-json.py` - Convert UI text CSV to JSON
- `process-svg.py` - Add interactive classes to SVG
- `build-language.py` - Master build script

**Usage:**
```bash
python3 build-scripts/build-language.py languages/spanish-config.json
```

## 📝 Translation Files

All translation files are in `translations/`:
- `template.csv` - Template for emotions (32 emotions)
- `ui-template.csv` - Template for UI text (7 elements)
- `spanish.csv`, `italian.csv` - Language-specific emotions
- `ui-es.csv`, `ui-italian.csv` - Language-specific UI text

## 🎨 SVG Source Files

Original SVG files from Adobe Illustrator are in `svg-source/`:
- `Plutchik-italiano.svg` - Italian source
- `Plutchik-spanish-1.svg` - Spanish source

**Important:** Layer names should match the target language (Italian SVG has Italian layer IDs, Spanish SVG has Spanish layer IDs, etc.)

## 🏗️ Development

### Local Testing

```bash
# Start local server
python3 -m http.server 8000

# Open in browser
open http://localhost:8000/index-es.html
```

### Deploying to GitHub Pages

```bash
git add .
git commit -m "Add Spanish language support"
git push origin main
```

## 📦 What's What

### Active Files (Don't Delete!)
- All `index-*.html` files
- All `text-*.json` and `ui-text-*.json` files
- All `Plutchik-*-processed.svg` files
- Everything in `css/`, `js/`, `build-scripts/`, `translations/`, `languages/`, `docs/`

### Archive (Can Delete)
- `archive/` - Old scripts, old HTML versions, old docs, backups

## ❓ Common Tasks

**Add a new language:**
See [docs/ADDING-NEW-LANGUAGE.md](docs/ADDING-NEW-LANGUAGE.md)

**Update existing translations:**
1. Edit the CSV files in `translations/`
2. Run `python3 build-scripts/csv-to-json.py translations/spanish.csv text-es.json`
3. Refresh browser

**Fix SVG issues:**
1. Update source SVG in `svg-source/`
2. Run `python3 build-scripts/process-svg.py svg-source/Plutchik-spanish-1.svg Plutchik-spanish-processed.svg`
3. Embed new SVG in HTML

## 🤝 Contributing

Contributions welcome! Especially:
- New language translations
- Bug fixes
- Documentation improvements
- Builder app development

## 📄 License

[Add license here]

## 🙏 Credits

- Based on Robert Plutchik's Wheel of Emotions
- Built with jQuery and vanilla JavaScript
- Hosted on GitHub Pages

---

**Need Help?** Check the [docs/](docs/) folder or open an issue!
