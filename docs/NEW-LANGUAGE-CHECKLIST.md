# New Language Checklist

Use this checklist when adding a new language to the Plutchik webapp.

## Language: _________________ (Code: ____)

### Phase 1: Translation
- [ ] Copy `translations/template.csv` to `translations/[language].csv`
- [ ] Send CSV to translator with `docs/TRANSLATOR-GUIDE.md`
- [ ] Receive completed translation CSV
- [ ] Review translations for completeness (32 emotions)
- [ ] Verify CSV format is valid (no stray commas)

### Phase 2: SVG Creation
- [ ] Open English SVG in Adobe Illustrator
- [ ] **Verify all layer names are in English** (critical!)
- [ ] Change only visible text to target language
- [ ] Export as SVG to `svg-source/Plutchik-[language].svg`
- [ ] Verify SVG file is clean (no embedded images, proper text paths)

### Phase 3: Configuration
- [ ] Copy `build-scripts/language-config-template.json` to `languages/[language]-config.json`
- [ ] Fill in all configuration fields:
  - [ ] `language_code` (e.g., "es", "fr", "hu")
  - [ ] `language_name` (e.g., "Spanish")
  - [ ] `page_title`
  - [ ] `csv_file` path
  - [ ] `json_file` path
  - [ ] `svg_input` path
  - [ ] `svg_processed` path
  - [ ] `html_output` path
  - [ ] `css_file` path
  - [ ] `js_file` path
  - [ ] All `ui_text` fields translated
  - [ ] URLs for language-specific resources (or use English URLs)

### Phase 4: Build
- [ ] Run build script:
  ```bash
  python3 build-scripts/build-language.py languages/[language]-config.json
  ```
- [ ] Verify JSON file was created
- [ ] Verify processed SVG was created
- [ ] Check build output for any warnings or errors

### Phase 5: CSS Setup
- [ ] Copy Italian CSS as template:
  ```bash
  cp css/styles-it.css css/styles-[language].css
  ```
- [ ] No changes needed (uses standardized English class names)

### Phase 6: JavaScript Setup
- [ ] Copy Italian JS as template:
  ```bash
  cp js/scripts-it.js js/scripts-[language].js
  ```
- [ ] Update line 3 to load correct JSON file:
  ```javascript
  $.getJSON("text-[language].json", function(data) {
  ```

### Phase 7: HTML Setup
- [ ] Copy Italian HTML as template:
  ```bash
  cp index-it.html index-[language].html
  ```
- [ ] Update `<title>` tag (line ~8)
- [ ] Update CSS reference to `css/styles-[language].css` (line ~13)
- [ ] Open `Plutchik-[language]-processed.svg` in text editor
- [ ] Copy entire SVG content
- [ ] Replace SVG section in HTML (lines ~27-800+)
- [ ] Update "Learn more:" text (line ~882)
- [ ] Update "What is EQ?" link and text (line ~883-886)
- [ ] Update "EQ & IQ" link and text (line ~888-891)
- [ ] Update "7 Things" link and text (line ~893-896)
- [ ] Update CTA text and link (line ~901)
- [ ] Update JS reference to `js/scripts-[language].js` (line ~909)

### Phase 8: Testing
Test locally by opening `index-[language].html` in browser:

**Visual Tests:**
- [ ] All emotion names appear in target language
- [ ] SVG loads without errors
- [ ] No missing or broken graphics
- [ ] Colors look correct
- [ ] Intermediate emotions are gray by default

**Interaction Tests:**
- [ ] Click on a base emotion → info panel appears
- [ ] Info panel shows correct text in target language
- [ ] All info fields populated (similar words, sensations, message, purpose)
- [ ] Click on intermediate emotion → shows combination explanation
- [ ] Opposite emotion indicator works
- [ ] More/less intense indicators work (when applicable)

**Hover Tests:**
- [ ] Hover over base emotion → darker color appears
- [ ] Hover over intermediate emotion → blended color appears
- [ ] No white flashing or color glitches

**Link Tests:**
- [ ] "What is EQ?" video link works
- [ ] "EQ & IQ" video link works
- [ ] "7 Things" article link works
- [ ] CTA link works
- [ ] All links open in new tab

**Console Tests:**
- [ ] Open browser console (F12)
- [ ] No JavaScript errors
- [ ] No 404s for missing files
- [ ] JSON loads successfully

### Phase 9: Deployment
- [ ] Add files to git:
  ```bash
  git add translations/[language].csv
  git add languages/[language]-config.json
  git add svg-source/Plutchik-[language].svg
  git add text-[language].json
  git add Plutchik-[language]-processed.svg
  git add css/styles-[language].css
  git add js/scripts-[language].js
  git add index-[language].html
  ```
- [ ] Commit with clear message:
  ```bash
  git commit -m "Add [Language] language support"
  ```
- [ ] Push to GitHub:
  ```bash
  git push origin main
  ```
- [ ] Wait for GitHub Pages deployment
- [ ] Test live version
- [ ] Update main README with new language link

### Phase 10: Documentation
- [ ] Add language to main README
- [ ] Update language list in documentation
- [ ] Note any language-specific quirks or issues
- [ ] Share live URL with stakeholders

## Troubleshooting Reference

If you encounter issues, check:
1. `docs/ADDING-NEW-LANGUAGE.md` - Detailed guide
2. `docs/TRANSLATOR-GUIDE.md` - For translation questions
3. `build-scripts/README.md` - For build script issues
4. Italian version files - Working example to compare against

## Common Issues

**"Could not find layer: [emotion]"**
→ SVG layers must use English names, not translated names

**Info panel shows wrong language**
→ Check JS file is loading correct JSON file

**Intermediate emotions not clickable**
→ Verify processed SVG has `intermediate-word-bounding-box` class on rects

**Colors not showing**
→ CSS file must be properly linked in HTML

**JSON not loading**
→ Check file path in JS, check browser console for 404 errors

## Notes

Language: _______________________

Date started: ____________________

Date completed: __________________

Translator: ______________________

Reviewer: _______________________

Issues encountered:
___________________________________
___________________________________
___________________________________

Live URL: __________________________
