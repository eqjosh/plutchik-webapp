# Italian Version of Plutchik Webapp

## Files Created

1. **text-it.json** - Italian translations of all emotion data (names, descriptions, messages, purposes)
2. **index-it.html** - Italian version of the webapp with updated emotion class names
3. **css/styles-it.css** - Italian version of CSS with translated color class names

## How It Works

The Italian version uses the same structure as the English version:

- **text-it.json** contains all Italian emotion names and their properties
- **index-it.html** loads `text-it.json` instead of the English JSON file
- All CSS class names have been translated (e.g., `serenity` → `serenità`, `joy` → `gioia`)
- The JavaScript dynamically populates emotion names and descriptions from the JSON

## Italian Emotion Mappings

### Base Emotions (8 petals)
- Gioia (Joy): serenità → gioia → estasi
- Fiducia (Trust): accettazione → fiducia → ammirazione
- Paura (Fear): apprensione → paura → terrore
- Sorpresa (Surprise): distrazione → sorpresa → stupore
- Tristezza (Sadness): pensierosità → tristezza → angoscia
- Disgusto (Disgust): noia → disgusto → odio
- Rabbia (Anger): irritazione → rabbia → collera
- Aspettativa (Anticipation): interesse → aspettativa → vigilanza

### Combination Emotions
- ottimismo (optimism) = aspettativa + gioia
- amore (love) = gioia + fiducia
- sottomissione (submission) = fiducia + paura
- soggezione (awe) = paura + sorpresa
- disapprovazione (disapproval) = sorpresa + tristezza
- rimorso (remorse) = tristezza + disgusto
- disprezzo (contempt) = disgusto + rabbia
- aggressività (aggressiveness) = rabbia + aspettativa

## Notes

### Text Labels in SVG
The current version has **English text labels** embedded as SVG paths in the emotion wheel graphic (lines 56-63, 71-73, etc. in index-it.html). These are vector shapes spelling out the English words.

To have Italian text labels visible in the wheel graphic itself, you would need to:
1. Export the Italian text as SVG paths from your Adobe Illustrator file
2. Replace the `<path class="central-letter">` elements in index-it.html with the Italian versions

However, **this is optional** because:
- The emotion names display dynamically in Italian when clicked (populated from text-it.json)
- The graphic colors and structure work perfectly
- Users click on colored petals, not the text labels

## Testing

To test the Italian version:
1. Open `index-it.html` in a web browser
2. Click on any emotion petal
3. The emotion name and all descriptions should appear in Italian

## Deployment

To deploy to S3:
1. Upload `text-it.json` to your S3 bucket
2. Upload `index-it.html` to your S3 bucket
3. Upload `css/styles-it.css` to your S3 bucket
4. Update the JSON URL in index-it.html if needed (currently set to load local file)
