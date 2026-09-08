# Nanaveda

## Idea
Traditional recipes and formulas for healthy consumables.

---

## Project: Nana's Golden Apothecary

### Title
**"Nana's Golden Apothecary: Timeless Remedies for Modern Wellness"**
- Compiled for Nana Muneer Ansari
- by Ahraz Arifuddin and Team6

### 10 Recipes (Final)
| # | Recipe | Origin |
|---|--------|--------|
| 1 | Kitchari | India (Ayurvedic) |
| 2 | Golden Milk / Haldi Doodh | India |
| 3 | Ginger, Goji & Jujube Bone Broth | China (TCM) |
| 4 | Congee with Shiitake | China/Japan |
| 5 | Saffron & Cardamom Sleep Milk | Middle East |
| 6 | Low-Sodium Miso Soup with Wakame | Japan |
| 7 | Hibiscus & Cinnamon Agua de Jamaica | Latin America |
| 8 | Beetroot, Ginger & Rose Sharbat | Middle East |
| 9 | Black Seed (Habba Sawda) Honey Paste | Arabic/Prophetic |
| 10 | Sage & Honey Tea | Mediterranean |

**Replacements:** Ashwagandha Moon Milk and Chyawanprash were swapped for Saffron & Cardamom Milk and Sage & Honey Tea — both more senior-accessible, both with Islamic/Middle Eastern roots. Tulsi Tea swapped for Hibiscus Agua de Jamaica — adds Latin American variety.

---

## Target Audience
- **Primary:** Nana Muneer Ansari — 60+ senior, devout Muslim
- **Secondary:** His wife — also 60+
- **Priority:** Senior readability (large type, high contrast, generous spacing)
- **Physical accessibility:** No intense physical demands. No heavy lifting, rapid chopping, or complex techniques without guidance.

---

## Design Direction
- **Body text:** 18px+, 1.6+ line height, warm serif (DM Serif Text or Lora)
- **Background:** Warm cream/ivory with subtle paper texture
- **Headings:** Deep teal or burgundy — high contrast, elegant
- **Accents:** Coral, teal, gold — used sparingly in title treatment, dividers, geometric borders
- **Layout:** One recipe per spread, large numbered steps, ingredient boxes clearly differentiated
- **Masculine aesthetic:** Strong typography, structured layout, bold headings, confident tone
- **Details:** "Why This Heals" callout, vintage botanical line art, ornamental section dividers

---

## Content Requirements

### Scope: Full depth. Every recipe goes deep.

### Deep Context (woven between steps)
Each recipe includes woven contextual information between steps:
- Why it was chosen — selection rationale
- Origins and history — where it comes from, how it spread
- Health benefits — in-depth explanation of effects on the body
- Cultural context — traditions, ceremonies, daily practices
- Religious/Islamic context — connection to Islamic history, narrative, theology
- Fun facts — interesting tidbits, lesser-known uses

### Weaving Pattern
Different types of context after different steps, especially during waiting/repetitive tasks:
- Health explanation after one step
- Historical context after another
- Fun fact after another
- Islamic connection after another
- etc.

### Islamic Context Approach
- **Don't force theology.** Find and explore connections to Islam, Islamic history, Islamic narrative wherever they are real.
- Present cultural origins honestly. Note where Islamic world adopted/valued recipes.
- For recipes with strong Ayurvedic/Buddhist roots (Kitchari, Congee): present origins honestly, highlight any authentic Islamic scholarly connections to the ingredients themselves.
- For recipes with direct Islamic grounding (Black Seed, Saffron, Sage, Honey, Ginger): highlight those connections fully — Quranic references, verified hadith, scholarly consensus.
- Distinguish between Islamic, Ayurvedic, and Buddhist traditions where they overlap.

### Visual Accompaniment
- Visuals, images, diagrams whenever possible, relevant, and tasteful
- **No faces of Islamic figures** (per Islamic rules)
- Any tasteful illustration is acceptable — botanical, geometric, landscape, food, diagram, calligraphy, etc.
- Images sourced from Unsplash API

### Interactive Features
- **Clickable terms:** Hover over highlighted terms for instant definitions
- **Pantry-availability icons:** 🟢 Pantry staple | 🟡 Easy to find | 🔴 Specialty store
- **Evidence-level badges:** High / Moderate / Traditional on each recipe's health claims
- **Safety warnings:** Hot liquid cautions, senior-specific modifications
- **Navigation:** Skip links, Back to Contents on every recipe, fixed top nav

---

## Safety Notes
- No astragalus or ginseng (warfarin interaction risk)
- No ashwagandha (blood pressure/thyroid concerns for seniors)
- No multi-ingredient complexity (48-ingredient jams, etc.)
- **Pantry-availability icons:** 🟢 Pantry staple | 🟡 Easy to find | 🔴 Specialty store
- All health claims honestly labeled with evidence levels
- Jujube/Sidr distinction clarified (Chinese jujube ≠ Quranic sidr)

---

## Deliverables
| File | Description |
|------|-------------|
| `index.html` | Full 10-recipe HTML book with woven context, visuals, interactive features |
| `nanaveda.css` | Complete design system with masculine aesthetic |
| `IDEA.md` | This file — project scope and direction |
| `PHYSICAL_AUDIT.md` | Senior physical demands audit for all 10 recipes |
| `image-manifest.json` | Unsplash image references |

---

## Folder Structure
- `PROJECTS/` — Active project files
- `OUTPUTS/` — Completed outputs for delivery
- `TEMPLATES/` — Reusable templates
- `LOG/` — Session logs and progress tracking
- `RESEARCH/` — Ingredients, formulations, reference material
- `ASSETS/` — Images, media, non-text resources

---

## Change Log
- 2026-08-22: Project created. IDEA.md written.
- 2026-08-22: Model config set to VeniceAI/stealth-ox-alpha across all profiles.
- 2026-08-22: Scope expanded — deep context, Islamic focus, visuals, senior accessibility.
- 2026-08-22: User confirmed full depth, Islamic authenticity, no-faces visual policy.
- 2026-08-22: Recipes 5 & 10 swapped — Ashwagandha→Saffron Cardamom Milk, Chyawanprash→Sage & Honey Tea.
- 2026-08-22: Full HTML book built with real Unsplash images, clickable terms, evidence badges, safety warnings, navigation, masculine aesthetic.
