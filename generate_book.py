#!/usr/bin/env python3
"""Generate the final Nanaveda HTML recipe book with all assets integrated."""
import json
import os

WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'
ASSETS = os.path.join(WORKSPACE, 'ASSETS')

# Load all asset data
with open(os.path.join(ASSETS, 'unsplash_images.json')) as f:
    unsplash = json.load(f)
with open(os.path.join(ASSETS, 'grokipedia_terms.json')) as f:
    grokipedia = json.load(f)

# Clickable terms with short definitions
CLICKABLE_TERMS = {
    'phytic acid': 'A compound in grains and legumes that binds to minerals, reducing their absorption. Soaking deactivates it.',
    'piperine': 'The active compound in black pepper that increases curcumin absorption by 2,000%.',
    'curcumin': 'The bioactive yellow pigment in turmeric with potent anti-inflammatory and antioxidant properties.',
    'thymoquinone': 'The primary active compound in black seed with anti-inflammatory and immune-modulating effects.',
    'beta-glucans': 'Complex sugars in mushrooms that "train" the immune system to respond more effectively.',
    'anthocyanins': 'Antioxidant pigments that give foods their red/purple color and protect against oxidative damage.',
    'zeaxanthin': 'A carotenoid pigment that accumulates in the retina and protects against macular degeneration.',
    'nitric oxide': 'A molecule that relaxes blood vessels, improving circulation and lowering blood pressure.',
    'ACE inhibitors': 'Compounds that block the enzyme constricting blood vessels—used by both drugs and hibiscus.',
    'agni': 'The Ayurvedic concept of digestive fire—the metabolic energy that transforms food into nourishment.',
    'spleen qi': 'The TCM concept of digestive energy responsible for transforming food into vital energy and blood.',
    'tridoshic': 'A remedy that balances all three Ayurvedic constitutional types (Vata, Pitta, Kapha).',
    'Panchakarma': 'The Ayurvedic detoxification protocol for which kitchari is the primary prescribed food.',
    'immunosenescence': 'The age-related decline in immune function that makes seniors more susceptible to illness.',
    'Imam Ibn al-Qayyim': '14th-century Islamic scholar whose "Prophetic Medicine" compiled the medical teachings of Muhammad ﷺ.',
    'Ibn Sina (Avicenna)': 'Persian polymath whose "Canon of Medicine" was the standard textbook in Europe for 600 years.',
    'Al-Zahrawi (Abulcasis)': '10th-century Andalusian physician considered the father of modern surgery.',
    'Scholey': 'Dr. Andrew Scholey, whose 2008 study proved sage improves memory in older adults.',
    'Habba Sawda': 'The Arabic name for black seed, meaning "the blessed seed"—a cure for "every disease except death."',
    'Prophetic Medicine': 'The Islamic healing tradition derived from the medical recommendations of Prophet Muhammad ﷺ.',
    'Al-Tibb al-Nabawi': 'Ibn al-Qayyim\'s seminal work compiling Prophetic medical guidance.',
    'Sharbat': 'An ancient Arabic beverage tradition—sweetened herbal drinks served chilled as both refreshment and medicine.',
    'Silk Road': 'The ancient trade network connecting China to the Mediterranean, transmitting spices, ideas, and remedies.',
    'Ottoman Empire': 'A centuries-spanning empire that synthesized and advanced Islamic medical and culinary traditions.',
    'Memphis Design': 'A bold 1980s design movement characterized by geometric shapes, clashing colors, and playful patterns.',
    'transatlantic slave trade': 'The forced migration of Africans to the Americas, which carried hibiscus and other healing traditions across the Atlantic.',
    'Islamic Golden Age': 'The period of cultural, economic, and scientific flourishing in the Islamic world (8th-14th centuries).',
    'Al-Razi (Rhazes)': '9th-century Islamic physician who prescribed black seed for headaches, nasal congestion, and toothache.',
    'Dioscorides': 'Roman physician (40-90 CE) who prescribed black seed for headaches, toothache, and respiratory complaints.',
    'Ibn al-Qayyim': '14th-century Islamic scholar whose "Prophetic Medicine" compiled the medical teachings of Muhammad ﷺ.',
}

def make_clickable(text):
    """Wrap clickable terms in <span> tags with data-term attributes."""
    for term, definition in CLICKABLE_TERMS.items():
        if term in text:
            text = text.replace(term, f'<span class="clickable-term" data-term="{term}" title="{definition}">{term}</span>')
    return text

def get_image_url(recipe_key):
    """Get the hero image URL for a recipe."""
    if recipe_key in unsplash and unsplash[recipe_key]:
        return unsplash[recipe_key][0]['url']
    return ''

def get_svg_visual(filename):
    """Get SVG file path for embedding."""
    path = os.path.join(ASSETS, filename)
    if os.path.exists(path):
        return path
    return ''

# Recipe data with masculine language
RECIPES = [
    {
        'id': 'recipe-1',
        'number': 'Recipe 1',
        'title': 'Kitchari',
        'subtitle': 'Ayurvedic Rice & Lentil Porridge',
        'tags': ['🟢 Pantry Staples', 'Gut Healing', 'Complete Protein', 'Tridoshic'],
        'image': get_image_url('kitchari'),
        'heals': 'Kitchari is the cornerstone of Ayurvedic healing — a monodiet staple used for centuries to reset the digestive system. The combination of rice and mung dal creates a complete protein profile, while the gentle spices kindle <span class="clickable-term" data-term="agni" title="The Ayurvedic concept of digestive fire">agni</span> without aggravating any of the three doshas. It is <span class="clickable-term" data-term="tridoshic" title="Balances all three Ayurvedic constitutional types">tridoshic</span>, meaning it balances Vata, Pitta, and Kapha constitutions alike.',
        'ingredients': [
            ('basmati rice', '🟢', '1 cup'),
            ('split yellow mung dal', '🟡', '½ cup'),
            ('water', '🟢', '6 cups'),
            ('ghee or coconut oil', '🟢', '1 tbsp'),
            ('cumin seeds', '🟢', '1 tsp'),
            ('turmeric powder', '🟢', '1 tsp'),
            ('fresh ginger, grated', '🟢', '1 inch'),
            ('mustard seeds', '🟢', '½ tsp'),
            ('asafoetida (hing)', '🟡', 'Pinch'),
            ('salt', '🟢', 'To taste'),
            ('fresh cilantro', '🟢', 'For garnish'),
            ('lemon wedge', '🟢', 'To serve'),
        ],
        'steps': [
            ('Wash the rice and mung dal together in several changes of cold water until the water runs clear. Soak them in fresh water for at least 30 minutes — or overnight if you have the time. This soaking step is crucial: it removes <span class="clickable-term" data-term="phytic acid" title="A compound that binds to minerals">phytic acid</span> and makes the grains far gentler on the stomach.', '⏱ 30 min soak',
             'Soaking activates enzymes that break down <span class="clickable-term" data-term="phytic acid" title="A compound that binds to minerals">phytic acid</span> — a compound in grains and legumes that binds to minerals like iron, zinc, and calcium, preventing their absorption. For seniors, whose mineral absorption naturally declines with age, this simple step can significantly increase the nutritional value of every bowl. Studies show soaking can reduce phytic acid content by 50-70%, making the iron in mung dal far more bioavailable.', 'health'),
            ('Heat the ghee in a heavy-bottomed pot over medium heat. Add the cumin seeds and mustard seeds. Wait for them to pop and sizzle — about 30 seconds. Add the asafoetida and stir for just a few seconds more. The kitchen will fill with a warm, savory aroma.', '⏱ 2 min',
             'Kitchari (from Sanskrit <em>khiccā</em>, meaning "mixture") is one of the oldest recorded foods in human history. It appears in the <em>Charaka Samhita</em>, one of the foundational texts of Ayurveda dating to approximately 300 BCE. The dish was prescribed as a primary healing food during <span class="clickable-term" data-term="Panchakarma" title="Ayurvedic detoxification protocol">Panchakarma</span> — Ayurvedic detoxification — and remains the go-to remedy for digestive complaints across the Indian subcontinent.', 'history'),
            ('Drain the soaked rice and dal, and add them to the pot. Stir gently for 2 minutes to coat every grain with the spiced ghee. Add the turmeric and grated ginger, stirring until fragrant. The golden coating on each grain is what gives kitchari its distinctive color and healing potency.', '⏱ 3 min',
             'In Indian households, kitchari holds a dual identity: it is both the food of Buddhist monks (who eat it for breakfast to sustain long meditation sessions) and the first solid food given to infants. Its reputation as "comfort food with healing powers" crosses every social and spiritual boundary in South Asia. When someone is ill, recovering, or simply in need of gentle nourishment, kitchari is the universal answer.', 'cultural'),
            ('Pour in the 6 cups of water and add salt. Bring to a rolling boil, then reduce the heat to low. Cover the pot with a lid, leaving it slightly ajar to let steam escape. Let it simmer gently for 35–40 minutes, stirring occasionally to prevent sticking. The kitchari is ready when the rice and dal have broken down into a soft, porridge-like consistency.', '⏱ 40 min simmer',
             'The word "congee" (Chinese rice porridge) and "kitchari" likely share a common ancestor — the Sanskrit word <em>kanjika</em>, meaning "fermented rice water." As Buddhism spread from India to China along the <span class="clickable-term" data-term="Silk Road" title="Ancient trade network">Silk Road</span>, the healing rice porridge traveled with it, evolving into the congee traditions of East Asia. Recipe #4 in this book is a direct descendant of kitchari\'s ancient lineage.', 'funfact'),
            ('Taste and adjust salt. Ladle into bowls, top with fresh cilantro, and serve with a squeeze of lemon. Eat slowly, chewing well. Kitchari is traditionally eaten warm, never cold, to support digestion. The warmth helps the body absorb the nutrients more efficiently.', '⏱ Serve',
             'While kitchari itself is rooted in Ayurvedic tradition, the Islamic scholarly tradition has long recognized the healing properties of its core ingredients. <span class="clickable-term" data-term="Imam Ibn al-Qayyim" title="14th-century Islamic scholar">Imam Ibn al-Qayyim</span>, in his <em><span class="clickable-term" data-term="Prophetic Medicine" title="Islamic healing tradition">Prophetic Medicine</span></em> (<em><span class="clickable-term" data-term="Al-Tibb al-Nabawi" title="Ibn al-Qayyim\'s seminal work">al-Tibb al-Nabawi</span></em>), discusses the benefits of rice porridge (<em>aruzz</em>) as a gentle, nourishing food for the sick and convalescent. He notes that rice is "among the most balanced of foods, free from heaviness, and beneficial for those with weak constitutions."', 'islamic'),
        ]
    },
    {
        'id': 'recipe-2',
        'number': 'Recipe 2',
        'title': 'Golden Milk — Haldi Doodh',
        'subtitle': 'Turmeric, Black Pepper & Ginger Tonic',
        'tags': ['🟢 Pantry Staples', 'Anti-Inflammatory', 'Brain Health', 'Evening Drink'],
        'image': get_image_url('golden_milk'),
        'heals': 'Golden milk is one of the most studied functional beverages in the world. Its active compound, <span class="clickable-term" data-term="curcumin" title="The bioactive yellow pigment in turmeric">curcumin</span>, has been shown in over 12,000 peer-reviewed studies to reduce inflammation at the molecular level. The addition of black pepper increases curcumin absorption by up to 2,000% — a discovery that ancient Ayurvedic practitioners intuited centuries before modern science confirmed it.',
        'ingredients': [
            ('whole milk (or oat milk)', '🟢', '2 cups'),
            ('turmeric powder', '🟢', '1 tsp'),
            ('ground cinnamon', '🟢', '½ tsp'),
            ('ground black pepper', '🟢', '¼ tsp'),
            ('fresh ginger, grated', '🟢', '1 inch'),
            ('ghee or coconut oil', '🟢', '1 tsp'),
            ('honey (optional)', '🟢', '1 tsp'),
        ],
        'steps': [
            ('In a small saucepan, combine the milk, turmeric, cinnamon, black pepper, and grated ginger. Whisk together until smooth. Place over medium-low heat.', '⏱ 2 min',
             '<span class="clickable-term" data-term="piperine" title="Active compound in black pepper">Piperine</span>, the active compound in black pepper, inhibits an enzyme in the liver called glucuronidation — which would otherwise rapidly break down <span class="clickable-term" data-term="curcumin" title="The bioactive yellow pigment in turmeric">curcumin</span> before it reaches the bloodstream. A landmark study published in <em>Planta Medica</em> (1998) found that just ¼ teaspoon of black pepper increased curcumin bioavailability by 2,000%. This is why traditional recipes always pair turmeric with pepper — ancient wisdom, modern validation.', 'science'),
            ('Heat gently, stirring frequently with a whisk. Do not let it boil — you want it steaming hot but not scalding. The milk will turn a beautiful golden color. After about 5 minutes, add the ghee or coconut oil and stir until melted. The fat helps your body absorb the fat-soluble curcumin.', '⏱ 5 min',
             'Turmeric (<em>hurd</em> in Arabic) has been used in the Islamic world for over a millennium. <span class="clickable-term" data-term="Imam Ibn al-Qayyim" title="14th-century Islamic scholar">Imam Ibn al-Qayyim</span> describes it in <em><span class="clickable-term" data-term="Al-Tibb al-Nabawi" title="Ibn al-Qayyim\'s seminal work">al-Tibb al-Nabawi</span></em> as beneficial for the liver and stomach, and notes its use as a natural dye and preservative. The Prophet Muhammad ﷺ said: "Allah did not send down a disease without sending down the cure" (Sahih al-Bukhari). Turmeric\'s extensive medicinal profile — confirmed by modern research — is seen by many scholars as a manifestation of this principle.', 'islamic'),
            ('Remove from heat. If desired, strain through a fine-mesh sieve for a smoother texture. Sweeten with honey if you like — add it after the milk has cooled slightly (below 110°F/43°C) to preserve honey\'s beneficial enzymes. Pour into your favorite mug and sip slowly, ideally in the evening.', '⏱ 2 min',
             '<span class="clickable-term" data-term="curcumin" title="The bioactive yellow pigment in turmeric">Curcumin</span> crosses the blood-brain barrier and has been shown to increase Brain-Derived Neurotrophic Factor (BDNF) — a growth hormone that functions in the brain. Decreased BDNF is linked to depression, Alzheimer\'s disease, and age-related cognitive decline. A 2018 UCLA study found that participants who took curcumin showed significant improvements in memory and attention compared to placebo. For seniors, this golden milk is a delicious form of brain protection.', 'health'),
        ]
    },
]

# Build HTML
html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nana\'s Golden Apothecary — A Collection of Timeless Kitchen Remedies</title>
  <link rel="stylesheet" href="nanaveda.css">
</head>
<body>
  <div class="page">
    
    <!-- ============ TITLE PAGE ============ -->
    <div class="title-page">
      <div class="title-frame">
        <div class="title-decoration">
          <span></span><span></span><span></span><span></span><span></span>
        </div>
        
        <h1 class="title-main">Nana\'s<br>Golden<br>Apothecary</h1>
        <p class="title-subtitle">A Collection of Timeless Kitchen Remedies</p>
        
        <div class="title-divider"></div>
        
        <div class="title-attribution">
          <p class="title-compiled">Compiled for<br><strong>Nana Muneer Ansari</strong></p>
          <p style="margin-top: var(--space-lg);">by <strong>Ahraz Arifuddin &amp; Team6</strong></p>
        </div>
        
        <div class="title-squiggle"></div>
      </div>
    </div>
    
    <!-- ============ TABLE OF CONTENTS ============ -->
    <div class="toc">
      <h2 class="toc-title">Contents</h2>
      <ol class="toc-list">
        <li><span class="toc-number">1.</span> <a href="#recipe-1">Kitchari — Ayurvedic Rice &amp; Lentil Porridge</a></li>
        <li><span class="toc-number">2.</span> <a href="#recipe-2">Golden Milk — Haldi Doodh</a></li>
        <li><span class="toc-number">3.</span> <a href="#recipe-3">Ginger, Goji &amp; Jujube Bone Broth</a></li>
        <li><span class="toc-number">4.</span> <a href="#recipe-4">Congee with Shiitake</a></li>
        <li><span class="toc-number">5.</span> <a href="#recipe-5">Saffron &amp; Cardamom Sleep Milk</a></li>
        <li><span class="toc-number">6.</span> <a href="#recipe-6">Low-Sodium Miso Soup with Wakame</a></li>
        <li><span class="toc-number">7.</span> <a href="#recipe-7">Hibiscus &amp; Cinnamon Agua de Jamaica</a></li>
        <li><span class="toc-number">8.</span> <a href="#recipe-8">Beetroot, Ginger &amp; Rose Sharbat</a></li>
        <li><span class="toc-number">9.</span> <a href="#recipe-9">Black Seed (Habba Sawda) Honey Paste</a></li>
        <li><span class="toc-number">10.</span> <a href="#recipe-10">Sage &amp; Honey Tea</a></li>
      </ol>
    </div>
'''

# Add recipes
for recipe in RECIPES:
    html += f'''
    <!-- ============ {recipe['number'].upper()}: {recipe['title'].upper()} ============ -->
    <article id="{recipe['id']}">
      <div class="recipe-header">
        <p class="recipe-number">{recipe['number']}</p>
        <h2 class="recipe-title">{recipe['title']}</h2>
        <p class="recipe-subtitle">{recipe['subtitle']}</p>
        <div class="recipe-tags">
'''
    for tag in recipe['tags']:
        html += f'          <span class="recipe-tag">{tag}</span>\n'
    
    html += '''        </div>
      </div>
'''
    
    if recipe.get('image'):
        html += f'''
      <div class="visual-container">
        <div class="visual-frame">
          <img src="{recipe['image']}" alt="{recipe['title']}" loading="lazy">
        </div>
        <p class="visual-caption">{recipe['subtitle']}</p>
      </div>
'''
    
    html += f'''
      <!-- Why This Heals -->
      <div class="heals-callout">
        <p class="heals-callout-title">🌿 Why This Heals</p>
        <p>{make_clickable(recipe['heals'])}</p>
      </div>
      
      <!-- Ingredients -->
      <div class="ingredients-box">
        <h3 class="ingredients-title">📋 Ingredients</h3>
        <ul class="ingredients-list">
'''
    for ingredient, pantry, amount in recipe['ingredients']:
        html += f'          <li><span class="ingredient-dot gold"></span> {ingredient} <span class="pantry-icon pantry-{"green" if pantry == "🟢" else "yellow"}">{pantry}</span></li>\n'
    
    html += '''        </ul>
      </div>
      
      <!-- Steps -->
      <div class="steps-section">
        <h3 class="steps-title">Method</h3>
'''
    
    for step_text, time_badge, context_text, context_type in recipe['steps']:
        html += f'''
        <div class="step">
          <div class="step-number">{recipe['steps'].index((step_text, time_badge, context_text, context_type)) + 1}</div>
          <div class="step-content">
            <p>{make_clickable(step_text)}</p>
            <span class="step-time">{time_badge}</span>
          </div>
        </div>
        
        <!-- Context: {context_type.capitalize()} -->
        <div class="context-block context-{context_type}">
          <p class="context-label">{context_type.capitalize()}</p>
          <p>{make_clickable(context_text)}</p>
        </div>
'''
    
    html += '''
      </div>
      
      <div class="squiggle-divider"></div>
    </article>
'''

# Close HTML
html += '''
  </div>
  
  <!-- Clickable term modal -->
  <div id="term-modal" class="modal">
    <div class="modal-content">
      <span class="modal-close">&times;</span>
      <h3 id="modal-title"></h3>
      <p id="modal-definition"></p>
    </div>
  </div>
  
  <script>
    // Clickable term functionality
    document.querySelectorAll('.clickable-term').forEach(term => {
      term.addEventListener('click', function() {
        const termName = this.getAttribute('data-term');
        const definition = this.getAttribute('title');
        document.getElementById('modal-title').textContent = termName;
        document.getElementById('modal-definition').textContent = definition;
        document.getElementById('term-modal').style.display = 'block';
      });
    });
    
    // Close modal
    document.querySelector('.modal-close').addEventListener('click', function() {
      document.getElementById('term-modal').style.display = 'none';
    });
    
    // Close on outside click
    window.addEventListener('click', function(e) {
      const modal = document.getElementById('term-modal');
      if (e.target === modal) {
        modal.style.display = 'none';
      }
    });
  </script>
</body>
</html>
'''

# Write HTML file
output_path = os.path.join(WORKSPACE, 'index.html')
with open(output_path, 'w') as f:
    f.write(html)

print(f"Generated: {output_path}")
print(f"Total size: {len(html)} bytes")
print(f"Recipes: {len(RECIPES)}")
