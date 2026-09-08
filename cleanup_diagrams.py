#!/usr/bin/env python3
"""Clean up duplicate diagram placeholders and add missing ones."""
import os

WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'

with open(os.path.join(WORKSPACE, 'index.html')) as f:
    html = f.read()

# Remove duplicate consecutive diagram-placeholder blocks
import re
html = re.sub(r'(<div class="diagram-placeholder">.*?</div>\s*)+', r'\1', html, flags=re.DOTALL)

# Add diagram for Recipe 3 (Bone Broth) — after the visual-frame div
old_br = '<div class="visual-frame"><img src="https://images.unsplash.com/photo-1469307517101-0b99d8fb0c33?w=800" alt="bone broth" loading="lazy"></div>\n        </div>\n        <div class="recipe-header">'
new_br = '<div class="visual-frame"><img src="https://images.unsplash.com/photo-1469307517101-0b99d8fb0c33?w=800" alt="bone broth" loading="lazy"></div>\n        </div>\n        <div class="diagram-placeholder">\n          <p class="diagram-prompt">MAP: Silk Road trade route showing China → Central Asia → Middle East → Europe. Highlight goji berries and jujube dates traveling westward. Aged parchment style, muted coral/teal/gold.</p>\n        </div>\n        <div class="recipe-header">'
html = html.replace(old_br, new_br, 1)

# Add diagram for Recipe 9 (Black Seed) — it has no image
old_bs = '<article>\n        <div class="recipe-header">\n          <p class="recipe-number">Recipe 9</p>'
new_bs = '<article>\n        <div class="diagram-placeholder">\n          <p class="diagram-prompt">ILLUSTRATION: Ancient Egyptian tomb interior with black seed and honey vessels. Historical illustration style, warm gold/brown palette.</p>\n        </div>\n        <div class="recipe-header">\n          <p class="recipe-number">Recipe 9</p>'
html = html.replace(old_bs, new_bs, 1)

with open(os.path.join(WORKSPACE, 'index.html'), 'w') as f:
    f.write(html)

print(f"Cleaned. Size: {len(html)} bytes")
print(f"Diagram placeholders: {html.count('diagram-placeholder')}")
