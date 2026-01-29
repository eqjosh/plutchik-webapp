# Translator's Quick Guide

## What You Need to Do

You're translating the Plutchik Emotions Wheel into your language. This involves:
1. **32 emotions** (24 basic + 8 combined emotions) → `template.csv`
2. **UI text and links** (page title, buttons, links) → `ui-template.csv`

## Step 1: Get the CSV Templates

Ask the developer for TWO files:
1. **`template.csv`** - The 32 emotions
2. **`ui-template.csv`** - Page text and links

## Step 2: Fill Out the Spreadsheet

Open the CSV in Excel, Google Sheets, or any spreadsheet program.

### For Each Emotion, Translate These Fields:

| Field | What It Means | Example (English → Italian) |
|-------|---------------|----------------------------|
| **emotion** | The name of the emotion | joy → gioia |
| **similar-words** | Other words that mean similar things | Happiness → Felicità |
| **sensations** | How this emotion feels physically | Sense of energy and possibility → Senso di energia e possibilità |
| **message** | What this emotion is telling you | Things are going well → Le cose stanno andando bene |
| **purpose** | How this emotion helps you | Ignites creativity; connection; energizes → Accende creatività, connessione, dà energia |

### Fields You DON'T Change:

- `type` - Keep as "base" or "intermediate"
- `intensity` - Keep as "low", "medium", or "high"
- `petal-color` and `color` - Keep the hex codes (e.g., #ffca05)
- `+intense`, `-intense`, `opposite` - Translate the emotion names referenced here
- `combo-emotion-0`, `combo-emotion-1` - For intermediate emotions, translate the emotion names

### Special Notes:

1. **Use semicolons (;) to separate multiple words** in the `similar-words` field
   - Example: "Calm; Peace" not "Calm, Peace"

2. **Keep the emotion name simple** - usually one word
   - ✅ Good: "gioia", "tristezza"
   - ❌ Avoid: "la gioia profonda"

3. **Be natural** - Don't translate word-for-word. Use expressions that sound natural in your language.

4. **Stay gender-neutral** where possible
   - ✅ Italian: "Aiuta a..." (neutral)
   - ❌ Italian: "Ti aiuta a..." (can imply gender)

## Step 3: The 32 Emotions to Translate

### Base Emotions (24):

**Yellow Family (Joy):**
1. serenity (low intensity)
2. joy (medium intensity)
3. ecstasy (high intensity)

**Green Family (Trust):**
4. acceptance (low intensity)
5. trust (medium intensity)
6. admiration (high intensity)

**Teal Family (Fear):**
7. apprehension (low intensity)
8. fear (medium intensity)
9. terror (high intensity)

**Light Blue Family (Surprise):**
10. distraction (low intensity)
11. surprise (medium intensity)
12. amazement (high intensity)

**Blue Family (Sadness):**
13. pensiveness (low intensity)
14. sadness (medium intensity)
15. grief (high intensity)

**Purple Family (Disgust):**
16. boredom (low intensity)
17. disgust (medium intensity)
18. loathing (high intensity)

**Red Family (Anger):**
19. annoyance (low intensity)
20. anger (medium intensity)
21. rage (high intensity)

**Orange Family (Anticipation):**
22. interest (low intensity)
23. anticipation (medium intensity)
24. vigilance (high intensity)

### Intermediate Emotions (8):

These are combinations of two base emotions:

25. **aggressiveness** = anger + anticipation
26. **optimism** = anticipation + joy
27. **contempt** = disgust + anger
28. **awe** = fear + surprise
29. **love** = joy + trust
30. **remorse** = sadness + disgust
31. **disapproval** = surprise + sadness
32. **submission** = trust + fear

For these, you also need to translate the `combo-explanation` field, which explains how the two emotions combine.

## Step 4: Fill Out the UI Text File

The second file (`ui-template.csv`) contains page text and links.

### UI Text Fields to Translate:

| Key | What It Is | Example |
|-----|------------|---------|
| **page_title** | Browser tab title | "Rueda de Emociones de Plutchik" |
| **learn_more_heading** | Heading above resource links | "Aprende más:" |
| **eq_what_text** | First video link text | "¿Qué es la Inteligencia Emocional?" |
| **eq_iq_text** | Second video link text | "CI & CE" |
| **seven_things_text** | Article link text | "7 Cosas Sobre las Emociones" |
| **cta_intro** | Call-to-action intro | "¿Quieres empezar a entrenar tu CE?" |
| **cta_link_text** | Call-to-action link | "Comienza con el Libro Practicing EQ" |

### Links/URLs Column:

- If there are language-specific resources (like an Italian YouTube channel), update the URL
- If not, leave the English URL - it's fine to link to English resources
- Example: Italian version links to `italia.6seconds.org` instead of `6seconds.org`

## Step 5: Save and Send Back

1. Save your completed CSV files:
   - `spanish.csv` (emotions)
   - `ui-spanish.csv` (page text)
2. Send both back to the developer

## Common Questions

**Q: Can I add more emotions?**
A: No, stick to the standard 32 emotions in Plutchik's model.

**Q: What if my language doesn't have a word for an emotion?**
A: Use the closest equivalent or a short phrase. This is common!

**Q: Should I translate "Plutchik"?**
A: No, it's a proper name (Robert Plutchik, the psychologist who created this model).

**Q: What about links to videos and articles?**
A: If there are versions in your language, provide those URLs. Otherwise, English links are fine.

**Q: How precise should the translations be?**
A: The goal is to convey the emotional meaning, not literal word-for-word translation. Use what sounds natural to a native speaker.

**Q: I messed up the CSV format (commas everywhere!)**
A: That's okay! Send it back anyway and the developer can help fix formatting issues.

## Example Row (English to Italian)

```csv
gioia,base,medium,#ffca05,#ffdc7b,estasi,serenità,tristezza,Felicità,Senso di energia e possibilità,Le cose stanno andando bene,Accende creatività; connessione; dà energia,,,
```

This translates "joy" with:
- Type: base emotion
- Intensity: medium
- More intense: ecstasy
- Less intense: serenity
- Opposite: sadness
- Similar words: Happiness
- Sensations: Sense of energy and possibility
- Message: Things are going well
- Purpose: Ignites creativity; connection; energizes

## Need Help?

Contact the developer if:
- The CSV file won't open
- You're not sure how to translate a specific emotion
- You want to suggest a different approach
- You have questions about cultural appropriateness

Thank you for helping make emotional intelligence accessible in your language! 🌍❤️
