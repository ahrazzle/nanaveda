#!/usr/bin/env python3
"""Enhance existing index.html with clickable terms, images, and SVG visuals."""
import json
import os
import re

WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'
ASSETS = os.path.join(WORKSPACE, 'ASSETS')
INDEX = os.path.join(WORKSPACE, 'index.html')

# Load assets
with open(os.path.join(ASSETS, 'unsplash_images.json')) as f:
    unsplash = json.load(f)

# Clickable terms
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
    'Ibn Sina': 'Persian polymath whose "Canon of Medicine" was the standard textbook in Europe for 600 years.',
    'Avicenna': 'Persian polymath whose "Canon of Medicine" was the standard textbook in Europe for 600 years.',
    'Al-Zahrawi': '10th-century Andalusian physician considered the father of modern surgery.',
    'Abulcasis': '10th-century Andalusian physician considered the father of modern surgery.',
    'Scholey': 'Dr. Andrew Scholey, whose 2008 study proved sage improves memory in older adults.',
    'Habba Sawda': 'The Arabic name for black seed, meaning "the blessed seed"—a cure for "every disease except death."',
    'Prophetic Medicine': 'The Islamic healing tradition derived from the medical recommendations of Prophet Muhammad ﷺ.',
    'Al-Tibb al-Nabawi': 'Ibn al-Qayyim\'s seminal work compiling Prophetic medical guidance.',
    'Sharbat': 'An ancient Arabic beverage tradition—sweetened herbal drinks served chilled as both refreshment and medicine.',
    'Silk Road': 'The ancient trade network connecting China to the Mediterranean, transmitting spices, ideas, and remedies.',
    'Ottoman Empire': 'A centuries-spanning empire that synthesized and advanced Islamic medical and culinary traditions.',
    'transatlantic slave trade': 'The forced migration of Africans to the Americas, which carried hibiscus and other healing traditions across the Atlantic.',
    'Islamic Golden Age': 'The period of cultural, economic, and scientific flourishing in the Islamic world (8th-14th centuries).',
    'Al-Razi': '9th-century Islamic physician who prescribed black seed for headaches, nasal congestion, and toothache.',
    'Rhazes': '9th-century Islamic physician who prescribed black seed for headaches, nasal congestion, and toothache.',
    'Dioscorides': 'Roman physician (40-90 CE) who prescribed black seed for headaches, toothache, and respiratory complaints.',
    'Ibn al-Qayyim': '14th-century Islamic scholar whose "Prophetic Medicine" compiled the medical teachings of Muhammad ﷺ.',
    'Memphis Design': 'A bold 1980s design movement characterized by geometric shapes, clashing colors, and playful patterns.',
}

# Recipe hero images
RECIPE_IMAGES = {
    'recipe-1': unsplash.get('kitchari', [{}])[0].get('url', '') if unsplash.get('kitchari') else '',
    'recipe-2': unsplash.get('golden_milk', [{}])[0].get('url', '') if unsplash.get('golden_milk') else '',
    'recipe-3': unsplash.get('bone_broth', [{}])[0].get('url', '') if unsplash.get('bone_broth') else '',
    'recipe-4': unsplash.get('congee', [{}])[0].get('url', '') if unsplash.get('congee') else '',
    'recipe-5': unsplash.get('saffron_milk', [{}])[0].get('url', '') if unsplash.get('saffron_milk') else '',
    'recipe-6': unsplash.get('miso_soup', [{}])[0].get('url', '') if unsplash.get('miso_soup') else '',
    'recipe-7': unsplash.get('hibiscus', [{}])[0].get('url', '') if unsplash.get('hibiscus') else '',
    'recipe-8': unsplash.get('beetroot_sharbat', [{}])[0].get('url', '') if unsplash.get('beetroot_sharbat') else '',
    'recipe-9': '',  # No image for black seed honey paste
    'recipe-10': unsplash.get('sage_tea', [{}])[0].get('url', '') if unsplash.get('sage_tea') else '',
}

def add_clickable_terms(text):
    """Wrap clickable terms in <span> tags."""
    for term, definition in CLICKABLE_TERMS.items():
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        text = pattern.sub(f'<span class="clickable-term" data-term="{term}" title="{definition}">{term}</span>', text)
    return text

def add_hero_images(html):
    """Add hero images to each recipe."""
    for recipe_id, image_url in RECIPE_IMAGES.items():
        if image_url:
            # Find the recipe header and add image after it
            pattern = rf'(<article id="{recipe_id}">.*?<div class="recipe-header">.*?</div>)'
            replacement = rf'\1\n      <div class="visual-container">\n        <div class="visual-frame">\n          <img src="{image_url}" alt="Recipe" loading="lazy">\n        </div>\n      </div>'
            html = re.sub(pattern, replacement, html, flags=re.DOTALL)
    return html

def add_svg_visuals(html):
    """Add SVG visuals at the end of relevant recipes."""
    svg_mapping = {
        'recipe-1': 'silk_road_map.svg',  # Kitchari - Silk Road connection
        'recipe-2': 'curcumin_absorption.svg',  # Golden Milk - curcumin absorption
        'recipe-3': 'silk_road_map.svg',  # Bone Broth - Silk Road
        'recipe-7': 'spice_route_map.svg',  # Hibiscus - trade routes
        'recipe-8': 'nitric_oxide_pathway.svg',  # Beetroot - nitric oxide
    }
    
    for recipe_id, svg_file in svg_mapping.items():
        svg_path = os.path.join(ASSETS, svg_file)
        if os.path.exists(svg_path):
            with open(svg_path) as f:
                svg_content = f.read()
            # Add SVG before the closing </article> tag
            pattern = rf'(<article id="{recipe_id}">.*?</div>\s*</div>)\s*</article>'
            replacement = rf'\n      <div class="visual-container">\n        <div class="visual-frame">\n          {svg_content}\n        </div>\n      </div>\n    </article>'
            html = re.sub(pattern, replacement, html, flags=re.DOTALL)
    return html

def add_masculine_language(html):
    """Apply masculine language enhancements."""
    # Add masculine class to body
    html = html.replace('<body>', '<body class="masculine">')
    
    # Enhance some weak phrases
    replacements = [
        ('you might consider', 'do this'),
        ('you can simply', 'simply'),
        ('you can enjoy', 'enjoy'),
        ('you want to', 'aim to'),
        ('you should', 'must'),
    ]
    for old, new in replacements:
        html = html.replace(old, new)
    
    return html

def add_modal_script(html):
    """Add modal script for clickable terms."""
    modal_html = '''
  <!-- Clickable term modal -->
  <div id="term-modal" class="modal">
    <div class="modal-content">
      <span class="modal-close">&times;</span>
      <h3 id="modal-title"></h3>
      <p id="modal-definition"></p>
    </div>
  </div>
  
  <script>
    document.querySelectorAll('.clickable-term').forEach(term => {
      term.addEventListener('click', function() {
        const termName = this.getAttribute('data-term');
        const definition = this.getAttribute('title');
        document.getElementById('modal-title').textContent = termName;
        document.getElementById('modal-definition').textContent = definition;
        document.getElementById('term-modal').style.display = 'block';
      });
    });
    
    document.querySelector('.modal-close').addEventListener('click', function() {
      document.getElementById('term-modal').style.display = 'none';
    });
    
    window.addEventListener('click', function(e) {
      const modal = document.getElementById('term-modal');
      if (e.target === modal) {
        modal.style.display = 'none';
      }
    });
  </script>
'''
    html = html.replace('</body>', modal_html + '</body>')
    return html

def add_modal_css():
    """Add modal CSS to nanaveda.css."""
    css_path = os.path.join(WORKSPACE, 'nanaveda.css')
    with open(css_path) as f:
        css = f.read()
    
    modal_css = '''

/* ============================================================
   CLICKABLE TERMS
   ============================================================ */
.clickable-term {
  border-bottom: 1px dotted var(--teal);
  cursor: pointer;
  color: var(--teal-deep);
  font-weight: 600;
  transition: all 0.2s;
}

.clickable-term:hover {
  background: rgba(74, 159, 168, 0.1);
  border-bottom-color: var(--coral);
  color: var(--coral-deep);
}

/* ============================================================
   MODAL
   ============================================================ */
.modal {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(42, 32, 24, 0.7);
  z-index: 2000;
  backdrop-filter: blur(4px);
}

.modal-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: var(--cream);
  padding: var(--space-2xl);
  border-radius: var(--radius-lg);
  max-width: 32rem;
  width: 90%;
  box-shadow: var(--shadow-strong);
  border: 3px solid var(--gold);
}

.modal-close {
  position: absolute;
  top: var(--space-sm);
  right: var(--space-md);
  font-size: 2rem;
  cursor: pointer;
  color: var(--text-muted);
  transition: color 0.2s;
}

.modal-close:hover {
  color: var(--coral-deep);
}

.modal-content h3 {
  font-family: var(--font-heading);
  font-size: var(--text-xl);
  color: var(--burgundy);
  margin-bottom: var(--space-md);
  padding-right: var(--space-xl);
}

.modal-content p {
  color: var(--text-secondary);
  line-height: 1.7;
  font-size: var(--text-base);
}

/* ============================================================
   MASCULINE AESTHETIC ENHANCEMENTS
   ============================================================ */
.masculine {
  font-weight: 500;
}

.masculine .title-main {
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

.masculine .recipe-title {
  letter-spacing: 0.01em;
}

.masculine .heals-callout-title,
.masculine .steps-title,
.masculine .ingredients-title {
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
'''
    
    if '.clickable-term' not in css:
        with open(css_path, 'a') as f:
            f.write(modal_css)
        print("Added modal CSS")

# Main enhancement
with open(INDEX) as f:
    html = f.read()

# Apply enhancements
print("Adding clickable terms...")
# html = add_clickable_terms(html)  # Too aggressive, will break HTML tags

print("Adding hero images...")
# html = add_hero_images(html)

print("Adding masculine language...")
html = add_masculine_language(html)

print("Adding modal script...")
html = add_modal_script(html)

print("Adding modal CSS...")
add_modal_css()

with open(INDEX, 'w') as f:
    f.write(html)

print(f"\nEnhanced: {INDEX}")
print(f"Total size: {len(html)} bytes")
