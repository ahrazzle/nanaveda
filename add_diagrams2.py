#!/usr/bin/env python3
"""Add diagram placeholders to remaining recipes — targeted approach."""
import os

WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'

with open(os.path.join(WORKSPACE, 'index.html')) as f:
    html = f.read()

# For each recipe, add diagram-placeholder after the visual-frame div
# Use unique context around each recipe header

replacements = [
    # Recipe 2 — Golden Milk
    (
        '<article>\n        <div class="visual-container" style="margin-left:0">\n          <div class="visual-frame"><img src="https://images.unsplash.com/photo-1604253412047-e4c697600f0b?w=800" alt="golden turmeric milk" loading="lazy"></div>\n          <p class="visual-caption">Photo by Alexey Khaneft · Unsplash</p>\n        </div>\n        <div class="recipe-header">\n          <p class="recipe-number">Recipe 2</p>',
        '<article id="recipe-2">\n        <div class="visual-container" style="margin-left:0">\n          <div class="visual-frame"><img src="https://images.unsplash.com/photo-1604253412047-e4c697600f0b?w=800" alt="golden turmeric milk" loading="lazy"></div>\n          <p class="visual-caption">Photo by Alexey Khaneft · Unsplash</p>\n        </div>\n        <div class="diagram-placeholder">\n          <p class="diagram-prompt">DIAGRAM: Curcumin + Piperine absorption pathway — turmeric root → curcumin molecule → liver (glucuronidation blocked by piperine) → 2000% more curcumin reaching bloodstream. Clean medical illustration, coral/teal/gold palette, arrows showing pathway.</p>\n        </div>\n        <div class="recipe-header">\n          <p class="recipe-number">Recipe 2</p>',
    ),
    # Recipe 3 — Bone Broth
    (
        '<article>\n        <div class="visual-container" style="margin-left:0">\n          <div class="visual-frame"><img src="https://images.unsplash.com/photo-1469307517101-0b99d8fb0c33?w=800" alt="bone broth" loading="lazy"></div>',
        '<article id="recipe-3">\n        <div class="visual-container" style="margin-left:0">\n          <div class="visual-frame"><img src="https://images.unsplash.com/photo-1469307517101-0b99d8fb0c33?w=800" alt="bone broth" loading="lazy"></div>\n        </div>\n        <div class="diagram-placeholder">\n          <p class="diagram-prompt">MAP: Silk Road trade route showing China → Central Asia → Middle East → Europe. Highlight goji berries and jujube dates traveling westward. Aged parchment style, muted coral/teal/gold.</p>\n        </div>\n        <div class="visual-caption">',
    ),
]

for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        print(f"Fixed: {old[:60]}...")
    else:
        print(f"NOT FOUND: {old[:60]}...")

with open(os.path.join(WORKSPACE, 'index.html'), 'w') as f:
    f.write(html)

print("\nDone")
