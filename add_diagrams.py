#!/usr/bin/env python3
"""Add diagram placeholders to remaining recipes."""
import os
import re

WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'

with open(os.path.join(WORKSPACE, 'index.html')) as f:
    html = f.read()

# Add diagram placeholders to recipes 2-10
additions = [
    ('recipe-2', 'DIAGRAM: Curcumin + Piperine absorption pathway — turmeric root → curcumin molecule → liver (glucuronidation blocked by piperine) → 2000% more curcumin reaching bloodstream. Clean medical illustration, coral/teal/gold palette, arrows showing pathway.'),
    ('recipe-3', 'MAP: Silk Road trade route showing China → Central Asia → Middle East → Europe. Highlight goji berries and jujube dates traveling westward. Aged parchment style, muted coral/teal/gold.'),
    ('recipe-5', 'DIAGRAM: Saffron crocus flower with stigmas being hand-harvested at dawn. Show 150,000 flowers = 1kg saffron. Botanical illustration style.'),
    ('recipe-6', 'MAP: Japan highlighting Okinawa island with Blue Zone designation. Clean modern map style.'),
    ('recipe-7', 'DIAGRAM: ACE Inhibition mechanism — blood vessel cross-section: ACE enzyme narrows vessels → hibiscus compounds block enzyme → vessels relax and widen. Before/after comparison. Medical illustration style.'),
    ('recipe-8', 'DIAGRAM: Nitric oxide pathway — dietary nitrates → nitric oxide → vasodilation → lower blood pressure. Clean diagram with arrows showing pathway.'),
    ('recipe-9', 'ILLUSTRATION: Ancient Egyptian tomb interior with black seed and honey vessels. Historical illustration style, warm gold/brown palette.'),
    ('recipe-10', 'ILLUSTRATION: Al-Zahrawi (Abulcasis) in a medieval Islamic medical setting, cataloguing herbs. Historical illustration, rich burgundy/gold tones.'),
]

for recipe_id, prompt in additions:
    # Find the visual-container div in this recipe and add diagram-placeholder after it
    pattern = rf'(<article id="{recipe_id}">.*?)</div>\s*(?=<div class="recipe-header">)'
    replacement = rf'\1</div>\n        <div class="diagram-placeholder">\n          <p class="diagram-prompt">{prompt}</p>\n        </div>\n        <div class="recipe-header">'
    html = re.sub(pattern, replacement, html, count=1, flags=re.DOTALL)

# Add CSS for diagram-placeholder if not present
css_path = os.path.join(WORKSPACE, 'nanaveda.css')
with open(css_path) as f:
    css = f.read()

if 'diagram-placeholder' not in css:
    css += '''

/* Diagram placeholder */
.diagram-placeholder {
  background: linear-gradient(135deg, var(--cream-dark), var(--cream-deeper));
  border: 3px dashed var(--gold);
  border-radius: var(--radius-md);
  padding: var(--space-xl);
  margin: var(--space-lg) 0;
  text-align: center;
  color: var(--text-muted);
}

.diagram-prompt {
  font-size: 0.9rem;
  line-height: 1.6;
  font-style: italic;
  color: var(--text-secondary);
}

.diagram-prompt::before {
  content: "🎨 ";
  font-size: 1.2rem;
}
'''
    with open(css_path, 'w') as f:
        f.write(css)
    print("Added diagram-placeholder CSS")

with open(os.path.join(WORKSPACE, 'index.html'), 'w') as f:
    f.write(html)

print(f"Added diagram placeholders for {len(additions)} recipes")
