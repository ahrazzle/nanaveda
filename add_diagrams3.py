#!/usr/bin/env python3
"""Add remaining diagram placeholders using image URLs as anchors."""
import os

WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'

with open(os.path.join(WORKSPACE, 'index.html')) as f:
    html = f.read()

# Map image URLs to their diagram prompts
image_prompts = {
    'photo-1604253412047-e4c697600f0b': 'DIAGRAM: Curcumin + Piperine absorption pathway — turmeric root → curcumin molecule → liver (glucuronidation blocked by piperine) → 2000% more curcumin reaching bloodstream. Clean medical illustration, coral/teal/gold palette, arrows showing pathway.',
    'photo-1469307517101-0b99d8fb0c33': 'MAP: Silk Road trade route showing China → Central Asia → Middle East → Europe. Highlight goji berries and jujube dates traveling westward. Aged parchment style, muted coral/teal/gold.',
    'photo-1680420574628-225def8eea0a': 'MAP: Spread of congee from India to China via Buddhist monks along the Silk Road. Show evolution from kitchari to congee. Historical map style.',
    'photo-1596151163116-98a5033814c2': 'DIAGRAM: Saffron crocus flower with stigmas being hand-harvested at dawn. Show 150,000 flowers = 1kg saffron. Botanical illustration style.',
    'photo-1635999831910-4eacfc81ca3e': 'MAP: Japan highlighting Okinawa island with Blue Zone designation and longevity statistics. Clean modern map style.',
    'photo-1761040253521-f9e432adac89': 'DIAGRAM: ACE Inhibition mechanism — blood vessel cross-section: ACE enzyme narrows vessels → hibiscus compounds block enzyme → vessels relax and widen. Before/after comparison. Medical illustration style.',
    'photo-1732002115020-c9a26272bf05': 'DIAGRAM: Nitric oxide pathway — dietary nitrates → nitric oxide → vasodilation → lower blood pressure. Clean diagram with arrows showing pathway.',
    'photo-1780678852082-788c7be17e0f': 'ILLUSTRATION: Ancient Egyptian tomb interior with black seed and honey vessels. Historical illustration style, warm gold/brown palette.',
    'photo-1577385384956-7e9fab6f7e84': 'ILLUSTRATION: Al-Zahrawi (Abulcasis) in a medieval Islamic medical setting, cataloguing herbs including sage. Historical illustration, rich burgundy/gold tones.',
}

for image_id, prompt in image_prompts.items():
    # Find the visual-frame div with this image and add diagram-placeholder after its closing </div>
    old = f'<div class="visual-frame"><img src="https://images.unsplash.com/{image_id}'
    # Find the end of this visual-container div
    idx = html.find(old)
    if idx >= 0:
        # Find the next "</div>" after this image
        end_idx = html.find('</div>', idx)
        if end_idx >= 0:
            # Insert diagram-placeholder after this </div>
            insert = html[:end_idx + 6] + f'\n        <div class="diagram-placeholder">\n          <p class="diagram-prompt">{prompt}</p>\n        </div>' + html[end_idx + 6:]
            html = insert

with open(os.path.join(WORKSPACE, 'index.html'), 'w') as f:
    f.write(html)

print(f"Added diagram placeholders. File size: {len(html)} bytes")
