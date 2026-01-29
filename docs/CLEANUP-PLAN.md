# Directory Cleanup Plan

## Proposed Structure

```
plutchik-webapp/
├── README.md                          # Main documentation
├── index.html                         # English version (main/default)
├── index-it.html                      # Italian version
├── index-es.html                      # Spanish version
│
├── css/                               # Stylesheets
│   ├── styles.css                     # English styles
│   ├── styles-it.css                  # Italian styles
│   └── styles-es.css                  # Spanish styles
│
├── js/                                # JavaScript
│   ├── scripts.js                     # English scripts
│   ├── scripts-it.js                  # Italian scripts
│   └── scripts-es.js                  # Spanish scripts
│
├── text-en.json                       # English emotion data (or move to data/?)
├── text-it.json                       # Italian emotion data
├── text-es.json                       # Spanish emotion data
├── ui-text-it.json                    # Italian UI text
├── ui-text-es.json                    # Spanish UI text
│
├── Plutchik-processed.svg             # English processed SVG (or Plutchik-english-processed.svg)
├── Plutchik-italiano-processed.svg    # Italian processed SVG
├── Plutchik-spanish-processed.svg     # Spanish processed SVG
│
├── build-scripts/                     # Build automation
│   ├── csv-to-json.py
│   ├── ui-csv-to-json.py
│   ├── process-svg.py
│   ├── build-language.py
│   ├── language-config-template.json
│   └── README.md
│
├── translations/                      # Translation source files
│   ├── template.csv
│   ├── ui-template.csv
│   ├── spanish.csv
│   ├── ui-es.csv
│   ├── italian.csv
│   └── ui-italian.csv
│
├── svg-source/                        # Original SVG files from Illustrator
│   ├── Plutchik-italiano.svg
│   └── Plutchik-spanish-1.svg
│
├── languages/                         # Language configs
│   ├── italian-config.json
│   ├── spanish-config.json
│   └── spanish-svg-mapping.json
│
├── docs/                              # Documentation
│   ├── ADDING-NEW-LANGUAGE.md
│   ├── TRANSLATOR-GUIDE.md
│   ├── UI-TRANSLATION-GUIDE.md
│   └── NEW-LANGUAGE-CHECKLIST.md
│
├── archive/                           # OLD/UNUSED FILES (to be deleted later)
│   ├── build-final-html.py            # Old build script
│   ├── fix-double-backgrounds.py      # Old fix script
│   ├── integrate-italian-svg.py       # Old integration script
│   ├── process-*.py                   # Old processing scripts
│   ├── index-it-*.html                # Old versions
│   ├── text-it.json.backup            # Backups
│   └── *.md (old docs)                # Old documentation
│
└── en/                                # English original (optional - could move to root)
    ├── index.html
    ├── css/
    ├── js/
    └── text.json
```

## Files to Move to archive/

- ITALIAN-VERSION-COMPLETE.md (old docs)
- README-ITALIAN.md (old docs)
- build-final-html.py (old script, replaced by build-scripts/)
- fix-double-backgrounds.py (old script, now integrated into process-svg.py)
- integrate-italian-svg.py (old script)
- process-*.py (all old processing scripts in root)
- index-it-final.html (old version)
- index-it-new.html (old version)
- index-en.html (duplicate of index.html?)
- text-it.json.backup (backup)

## Files to Keep in Root

- index.html (English main version)
- index-it.html (Italian)
- index-es.html (Spanish)
- text-*.json (emotion data)
- ui-text-*.json (UI text)
- Plutchik-*-processed.svg (processed SVGs)
- MULTI-LANGUAGE-SYSTEM.md (main overview - or move to docs/)
- UI-TRANSLATION-UPDATE.md (or move to docs/)

## Questions to Resolve

1. Should we move JSON files to a `data/` directory?
2. Should we keep `en/` directory or merge into root?
3. Should processed SVGs go in their own directory?
