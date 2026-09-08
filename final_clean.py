#!/usr/bin/env python3
"""Final clean rebuild with correct duplicate handling."""
import json
import os

WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'
ASSETS = os.path.join(WORKSPACE, 'ASSETS')

with open(os.path.join(ASSETS, 'unsplash_images.json')) as f:
    unsplash = json.load(f)

CT_DEFS = {
    'phytic_acid': 'A compound in grains and legumes that binds to minerals (iron, zinc, calcium), reducing their absorption. Soaking deactivates it — reducing content by 50-70%.',
    'piperine': 'The active alkaloid in black pepper. Inhibits liver glucuronidation, increasing curcumin bioavailability by 2,000% (Planta Medica, 1998).',
    'curcumin': 'The bioactive yellow polyphenolic pigment in turmeric. Modulates multiple molecular targets including NF-κB and COX-2, reducing inflammation. Human clinical trials number in the hundreds.',
    'thymoquinone': 'The primary active compound in Nigella sativa (black seed), comprising 30-48% of essential oil. A growing body of research documents anti-inflammatory and immune-modulating effects.',
    'beta_glucans': 'Complex polysaccharides in mushrooms that act as immunomodulators — training the immune system to respond more effectively. Unlike stimulants, they balance rather than push immune response.',
    'anthocyanins': 'Water-soluble flavonoid pigments that give foods their red/purple color. Function as powerful antioxidants, scavenging free radicals and reducing oxidative stress.',
    'zeaxanthin': 'A carotenoid pigment that accumulates in the macula of the human retina. Filters harmful blue light and protects against age-related macular degeneration (AMD).',
    'nitric_oxide': 'A signaling molecule that relaxes and dilates blood vessels. Dietary nitrates convert to NO via oral bacteria and stomach acid — effect peaks 2-3 hours after consumption.',
    'ace_inhibitors': 'Compounds that block angiotensin-converting enzyme, preventing blood vessel constriction. The same mechanism as prescription drugs like lisinopril. Hibiscus contains natural ACE-inhibitory compounds.',
    'agni': 'The Ayurvedic concept of digestive fire — the metabolic energy that transforms food into nourishment. Weak agni manifests as poor digestion, low energy, and accumulation of toxins (ama).',
    'spleen_qi': 'The TCM concept of digestive energy. The Spleen transforms food into qi and blood. Spleen qi deficiency manifests as fatigue, poor appetite, loose stools, and weak muscles.',
    'tridoshic': 'A remedy that balances all three Ayurvedic constitutional types (Vata, Pitta, Kapha) rather than aggravating any single one. Rare and highly valued — suitable for virtually any constitution.',
    'panchakarma': 'The traditional Ayurvedic detoxification and rejuvenation protocol consisting of five therapeutic procedures. Kitchari is the primary prescribed food because it provides complete nutrition while gently cleansing.',
    'immunosenescence': 'The age-related remodeling and functional decline of the immune system. Involves reduced naive T-cell production, decreased vaccine responsiveness, and chronic low-grade inflammation (inflammaging).',
    'ibn_qayyim': 'Imam Ibn Qayyim al-Jawziyya (1292-1350 CE). His work al-Tibb al-Nabawi (Prophetic Medicine) systematically compiled the medical teachings of Prophet Muhammad ﷺ, integrating spiritual, dietary, and herbal therapies.',
    'ibn_sina': 'Ibn Sina (980-1037 CE), known in the West as Avicenna. Persian polymath whose Canon of Medicine was the standard medical textbook in European universities for over 600 years.',
    'al_zahrawi': 'Abu al-Qasim al-Zahrawi (936-1013 CE), known in the West as Abulcasis. Andalusian physician considered the father of modern surgery. Authored the 30-volume medical encyclopedia al-Tasrif.',
    'scholey': 'Dr. Andrew Scholey, professor of psychopharmacology at Swinburne University. His 2008 study demonstrated that sage extract significantly improved memory and attention in healthy older adults.',
    'prophetic_medicine': 'The Islamic healing tradition (al-Tibb al-Nabawi) derived from the medical recommendations, dietary advice, and therapeutic practices attributed to Prophet Muhammad ﷺ.',
    'tibb_nabawi': 'Ibn al-Qayyim\'s seminal work compiling Prophetic medical guidance. He describes honey as "a food, a drink, a medicine, a sweet, a refreshment, and a delight."',
    'sharbat': 'An ancient Arabic beverage tradition (from "shariba," to drink) dating back over 1,000 years. Medieval Arabic cookbooks describe dozens of sharbat recipes using roses, pomegranates, lemons, and herbs.',
    'silk_road': 'The vast network of overland and maritime trade routes connecting China to the Mediterranean. Transmitted not just goods but ideas, medical knowledge, and healing ingredients for over 1,500 years.',
    'ottoman_empire': 'A centuries-spanning empire (1299-1922) that synthesized and advanced Islamic medical and culinary traditions. Ottoman physicians developed sophisticated herbal remedies using ingredients from across the empire.',
    'slave_trade': 'The forced migration of an estimated 12.5 million Africans to the Americas (16th-19th centuries). Carried not just human suffering but also agricultural knowledge, culinary traditions, and healing practices — including hibiscus.',
    'dioscorides': 'Pedanius Dioscorides (40-90 CE), Roman physician and pharmacologist. His work De Materia Medica prescribed black seed for headaches, toothache, and respiratory complaints — uses modern research has largely validated.',
    'habba_sawda': 'The Arabic name for Nigella sativa (black seed), meaning "the blessed seed" — called habbatul barakah because the Prophet Muhammad ﷺ described it as a cure for every disease except death (Sahih al-Bukhari 5688).',
}

def img(key):
    return unsplash.get(key, [{}])[0].get('url', '') if unsplash.get(key) else ''

def ct(name, text, recipe_terms):
    """Create clickable term span — only for first occurrence in recipe."""
    defn = CT_DEFS.get(name, '')
    if name in recipe_terms:
        return text  # Already used — return plain text
    recipe_terms.add(name)
    return f'<span class="term clickable-term" data-term="{name}" title="{defn}">{text}</span>'

RECIPES = [
    {
        'num': '1', 'page': 'page-recipe-1', 'id': 'recipe-1',
        'title': 'Kitchari', 'subtitle': 'Ayurvedic Rice & Lentil Porridge',
        'time': '30 min soak', 'diff': 'Easy', 'serves': '4',
        'evidence': 'evidence-traditional', 'evidence_label': 'Traditional',
        'tags': ['🟢 Pantry Staple', 'Gut Healing', 'Complete Protein', 'Tridoshic'],
        'img': img('kitchari'),
        'diagram': 'MAP / VISUAL: Buddhist monks eating kitchari in a monastery — warm, peaceful scene. Illustration style consistent with book palette (coral/teal/gold on cream).',
        'heals_fn': lambda t: f'Kitchari is the cornerstone of Ayurvedic healing — a monodiet staple used for centuries to reset the digestive system. The combination of rice and mung dal creates a complete protein profile, while the gentle spices kindle {ct("agni", "agni", t)} (digestive fire) without aggravating any of the three doshas. It is {ct("tridoshic", "tridoshic", t)}, meaning it balances Vata, Pitta, and Kapha constitutions alike.',
        'ings': [('basmati rice', '1 cup'), ('split yellow mung dal', '½ cup'), ('water', '6 cups'), ('ghee or coconut oil', '1 tbsp'), ('cumin seeds', '1 tsp'), ('turmeric powder', '1 tsp'), ('fresh ginger, grated', '1 inch'), ('mustard seeds', '½ tsp'), ('asafoetida (hing)', 'Pinch'), ('salt', 'To taste')],
        'steps_fn': lambda t: [
            ('Wash the rice and mung dal together in several changes of cold water until the water runs clear. Soak them in fresh water for at least 30 minutes — or overnight if you have the time. This soaking step is crucial: it removes phytic acid and makes the grains far gentler on the stomach.', '⏱ 30 min soak', f'Soaking activates enzymes that break down {ct("phytic_acid", "phytic acid", t)} — a compound in grains and legumes that binds to minerals like iron, zinc, and calcium, preventing their absorption. For seniors, whose mineral absorption naturally declines with age, this simple step can significantly increase the nutritional value of every bowl. Studies show soaking can reduce phytic acid content by 50-70%.', 'health', True),
            ('Heat the ghee in a heavy-bottomed pot over medium heat. Add the cumin seeds and mustard seeds. Wait for them to pop and sizzle — about 30 seconds. Add the asafoetida and stir for just a few seconds more.', '⏱ 2 min', f'Kitchari (from Sanskrit khiccā, meaning "mixture") is one of the oldest recorded foods in human history. It appears in the Charaka Samhita, one of the foundational texts of Ayurveda dating to approximately 300 BCE. The dish was prescribed as a primary healing food during {ct("panchakarma", "Panchakarma", t)} — Ayurvedic detoxification — and remains the go-to remedy for digestive complaints across the Indian subcontinent.', 'history', False),
            ('Drain the soaked rice and dal, and add them to the pot. Stir gently for 2 minutes to coat every grain with the spiced ghee. Add the turmeric and grated ginger, stirring until fragrant.', '⏱ 3 min', 'In Indian households, kitchari holds a dual identity: it is both the food of Buddhist monks (who eat it for breakfast to sustain long meditation sessions) and the first solid food given to infants. Its reputation as "comfort food with healing powers" crosses every social and spiritual boundary in South Asia.', 'cultural', False),
            ('Pour in the 6 cups of water and add salt. Bring to a rolling boil, then reduce the heat to low. Cover the pot with a lid, leaving it slightly ajar to let steam escape. Let it simmer gently for 35–40 minutes, stirring occasionally.', '⏱ 40 min simmer', f'The word "congee" (Chinese rice porridge) and "kitchari" likely share a common ancestor — the Sanskrit word kanjika, meaning "fermented rice water." As Buddhism spread from India to China along the {ct("silk_road", "Silk Road", t)}, the healing rice porridge traveled with it, evolving into the congee traditions of East Asia.', 'funfact', True),
            ('Taste and adjust salt. Ladle into bowls, top with fresh cilantro, and serve with a squeeze of lemon. Eat slowly, chewing well.', '⏱ Serve', f'While kitchari itself is rooted in Ayurvedic tradition, the Islamic scholarly tradition has long recognized the healing properties of its core ingredients. {ct("ibn_qayyim", "Imam Ibn al-Qayyim", t)}, in his {ct("prophetic_medicine", "Prophetic Medicine", t)} ({ct("tibb_nabawi", "al-Tibb al-Nabawi", t)}), discusses the benefits of rice porridge (aruzz) as a gentle, nourishing food for the sick and convalescent.', 'islamic', False),
        ]
    },
]

# Build recipe 1 block
r = RECIPES[0]
t = set()
heals = r['heals_fn'](t)
steps_raw = r['steps_fn'](t)

steps_html = ''
for i, (step_text, time_badge, context_text, context_type, is_waiting) in enumerate(steps_raw, 1):
    waiting_class = ' waiting-step' if is_waiting else ''
    steps_html += f'''        <div class="step">
          <div class="step-number">{i}</div>
          <div class="step-content">
            <p>{step_text}</p>
            <span class="step-time">{time_badge}</span>
          </div>
        </div>
        <div class="context-block context-{context_type}{waiting_class}">
          <p class="context-label">{context_type.capitalize()}</p>
          <p>{context_text}</p>
        </div>
'''

img_block = f'<div class="visual-container" style="margin-left:0"><div class="visual-frame"><img src="{r["img"]}" alt="{r["title"]}" loading="lazy"></div></div>' if r['img'] else ''
diagram_block = f'<div class="diagram-placeholder"><p class="diagram-prompt">{r["diagram"]}</p></div>' if r['diagram'] else ''
ings = ''.join(f'          <li><span class="ingredient-dot gold"></span> {ing[0]}</li>\n' for ing in r['ings'])
tags = ''.join(f'            <span class="recipe-tag">{tag}</span>\n' for tag in r['tags'])

block_1 = f'''
    <div class="page-view" id="{r['page']}">
      <article id="{r['id']}">
        {img_block}
        {diagram_block}
        <div class="recipe-header">
          <p class="recipe-number">Recipe {r['num']}</p>
          <h2 class="recipe-title">{r['title']}</h2>
          <p class="recipe-subtitle">{r['subtitle']}</p>
          <div class="recipe-meta">
            <span><i class="fas fa-clock"></i> {r['time']}</span>
            <span><i class="fas fa-fire"></i> {r['diff']}</span>
            <span><i class="fas fa-users"></i> {r['serves']}</span>
          </div>
          <div class="recipe-tags">
{tags}          </div>
        </div>
        <div class="heals-callout">
          <p class="heals-callout-title">Why This Heals <span class="evidence-badge {r['evidence']}">{r['evidence_label']}</span></p>
          <p>{heals}</p>
        </div>
        <div class="ingredients-box">
          <h3 class="ingredients-title"><i class="fas fa-carrot"></i> Ingredients</h3>
          <ul class="ingredients-list">
{ings}          </ul>
        </div>
        <div class="steps-section">
          <h3 class="steps-title">Method</h3>
{steps_html}        </div>
      </article>
      <div style="text-align:center;margin-top:var(--space-xl)">
        <a href="#" onclick="goToPage('page-toc'); return false;" class="back-to-toc"><i class="fas fa-arrow-up"></i> Back to Contents</a>
      </div>
      <div class="squiggle-divider"></div>
    </div>
'''

print(f"Block 1 generated. clickable-term count: {block_1.count('clickable-term')}")
term_matches = re.findall(r'data-term="([^"]+)"', block_1)
print(f"Unique terms in block 1: {len(term_matches)}")

# Just build recipe 1 as a test page for now
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nana's Golden Apothecary: Timeless Remedies for Modern Wellness</title>
  <link rel="stylesheet" href="nanaveda.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
</head>
<body class="masculine">
  <div class="text-controls">
    <button onclick="setTextSize('small')" title="Smaller text" id="ts-small">A-</button>
    <button onclick="setTextSize('medium')" title="Default text size" id="ts-medium" class="active">A</button>
    <button onclick="setTextSize('large')" title="Larger text" id="ts-large">A+</button>
  </div>
  <div class="page">
    <div class="page-view active" id="page-title">
      <div class="title-page">
        <div class="title-frame">
          <div class="title-decoration"><span></span><span></span><span></span><span></span><span></span></div>
          <h1 class="title-main">Nana's<br>Golden<br>Apothecary</h1>
          <p class="title-subtitle">Timeless Remedies for Modern Wellness</p>
          <div class="title-divider"></div>
          <div class="title-attribution">
            <p class="title-compiled">Compiled for<br><strong>Nana Muneer Ansari</strong></p>
            <p style="margin-top: var(--space-lg);">by <strong>Ahraz Arifuddin &amp; Team6</strong></p>
          </div>
          <div class="title-squiggle"></div>
        </div>
      </div>
    </div>
    <div class="page-view" id="page-toc">
      <div class="toc">
        <h2 class="toc-title">Contents</h2>
        <ol class="toc-list">
          <li><span class="toc-number">1.</span> <a href="#" onclick="goToPage('page-recipe-1'); return false;">Kitchari</a></li>
        </ol>
      </div>
    </div>
{block_1}
  </div>
  <nav class="page-nav" aria-label="Page navigation">
    <button id="prevBtn" onclick="prevPage()" disabled><i class="fas fa-arrow-left"></i> Previous</button>
    <span class="page-counter" id="pageCounter">Page 1 of 3</span>
    <button id="nextBtn" onclick="nextPage()">Next <i class="fas fa-arrow-right"></i></button>
  </nav>
  <div id="term-popup">
    <div id="term-popup-content">
      <button class="term-popup-close" onclick="closeTermPopup()">&times;</button>
      <h3 id="term-popup-title"></h3>
      <p id="term-popup-description"></p>
    </div>
  </div>
  <script>
    const pages = ["page-title", "page-toc", "page-recipe-1"];
    let currentPage = 0;
    function goToPage(pageId) {{ const idx = pages.indexOf(pageId); if (idx >= 0) currentPage = idx; updatePage(); }}
    function prevPage() {{ if (currentPage > 0) {{ currentPage--; updatePage(); }} }}
    function nextPage() {{ if (currentPage < pages.length - 1) {{ currentPage++; updatePage(); }} }}
    function updatePage() {{
      document.querySelectorAll(".page-view").forEach(p => p.classList.remove("active"));
      document.getElementById(pages[currentPage]).classList.add("active");
      document.getElementById("prevBtn").disabled = currentPage === 0;
      document.getElementById("nextBtn").disabled = currentPage === pages.length - 1;
      document.getElementById("pageCounter").textContent = "Page " + (currentPage + 1) + " of " + pages.length;
      window.scrollTo({{ top: 0, behavior: "instant" }});
    }}
    function setTextSize(size) {{
      document.documentElement.classList.remove("text-small", "text-medium", "text-large");
      document.documentElement.classList.add("text-" + size);
      document.querySelectorAll(".text-controls button").forEach(function(b) {{ b.classList.remove("active"); }});
      document.getElementById("ts-" + size).classList.add("active");
    }}
    document.addEventListener("keydown", function(e) {{
      if (e.key === "ArrowRight" || e.key === " ") {{ e.preventDefault(); nextPage(); }}
      if (e.key === "ArrowLeft") {{ e.preventDefault(); prevPage(); }}
    }});
    updatePage();
  </script>
</body>
</html>'''

with open(os.path.join(WORKSPACE, 'index.html'), 'w') as f:
    f.write(html)

print(f"Generated index.html: {len(html)} bytes")
print(f"clickable-term spans: {html.count('clickable-term')}")
print(f"data-term spans: {html.count('data-term=')}")
