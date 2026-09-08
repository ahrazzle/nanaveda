#!/usr/bin/env python3
"""Fix all three issues: duplicate terms, hourglass emojis, and diagram placeholders."""
import re
import os

WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'

with open(os.path.join(WORKSPACE, 'index.html')) as f:
    html = f.read()

# ============================================================
# FIX 1: Remove duplicate clickable terms within each recipe
# Only the first occurrence of each term per recipe should be clickable
# ============================================================

# Find all recipe blocks
recipe_pattern = re.compile(r'<article[^>]*id="recipe-(\d+)"[^>]*>(.*?)</article>', re.DOTALL)

for match in recipe_pattern.finditer(html):
    recipe_num = match.group(1)
    recipe_content = match.group(2)
    
    # Find all clickable terms in this recipe
    term_pattern = re.compile(r'<span class="term clickable-term" data-term="([^"]+)">([^<]+)</span>')
    seen_terms = set()
    
    def replace_term(m):
        term_key = m.group(1)
        term_text = m.group(2)
        if term_key in seen_terms:
            # Duplicate — remove clickable class, keep plain text
            return term_text
        seen_terms.add(term_key)
        return m.group(0)
    
    new_content = term_pattern.sub(replace_term, recipe_content)
    html = html.replace(recipe_content, new_content)

print("Fix 1: Removed duplicate clickable terms within recipes")

# ============================================================
# FIX 2: Remove hourglass emojis from Kitchari recipe
# The user reports stray hourglass emojis (⏳/⌛) cutting into UI
# ============================================================

# Remove any hourglass characters that might have been inserted
html = html.replace('⏳', '').replace('⌛', '')

# Also remove any CSS-generated hourglass via ::after if it exists
# The waiting-step class shouldn't have an hourglass pseudo-element
html = re.sub(r'\.context-block\.waiting-step\s*\.context-icon::after\s*\{[^}]*\}', '', html)
html = re.sub(r'\.waiting-step::after\s*\{[^}]*\}', '', html)

print("Fix 2: Removed hourglass emojis")

# ============================================================
# FIX 3: Create prompt containers for all 10 visual assets
# Replace existing SVG diagrams with placeholder containers
# ============================================================

# First, remove the existing broken SVG diagram containers
html = re.sub(r'<div class="svg-diagram"[^>]*>.*?</div>\s*<p class="visual-caption">.*?</p>', '', html, flags=re.DOTALL)

# Now add proper diagram containers at relevant locations
# For now, remove the broken SVG placeholders and add prompt containers
# The user will generate actual assets from these prompts

diagram_prompts = {
    'recipe-1': 'Map: Buddhist monks eating kitchari in a monastery — warm, peaceful scene. Illustration style consistent with book palette.',
    'recipe-2': 'Diagram: Curcumin + Piperine absorption pathway — turmeric root → curcumin molecule → liver (glucuronidation blocked by piperine) → 2000% more curcumin reaching bloodstream. Clean medical illustration, coral/teal/gold palette.',
    'recipe-3': 'Map: Silk Road trade route showing China → Central Asia → Middle East → Europe. Highlight goji berries and jujube dates traveling westward. Aged parchment style, muted coral/teal/gold.',
    'recipe-5': 'Diagram: Saffron crocus flower with stigmas being hand-harvested at dawn. Show 150,000 flowers = 1kg saffron. Botanical illustration style.',
    'recipe-6': 'Map: Japan highlighting Okinawa island with Blue Zone designation. Clean modern map style.',
    'recipe-7': 'Diagram: ACE Inhibition mechanism — blood vessel cross-section: ACE enzyme narrows vessels → hibiscus compounds block enzyme → vessels relax and widen. Before/after comparison. Medical illustration style.',
    'recipe-8': 'Diagram: Nitric oxide pathway — dietary nitrates → nitric oxide → vasodilation → lower blood pressure. Clean diagram with arrows showing pathway.',
    'recipe-9': 'Illustration: Ancient Egyptian tomb interior with black seed and honey vessels. Historical illustration style, warm gold/brown palette.',
    'recipe-10': 'Illustration: Al-Zahrawi (Abulcasis) in a medieval Islamic medical setting, cataloguing herbs. Historical illustration, rich burgundy/gold tones.',
}

for recipe_id, prompt in diagram_prompts.items():
    # Find the first context-block in each recipe and add diagram before it
    pattern = rf'(<article id="{recipe_id}".*?)(<div class="context-block)'
    replacement = rf'\1<div class="diagram-placeholder">\n        <p class="diagram-prompt">{prompt}</p>\n      </div>\n      \2'
    html = re.sub(pattern, replacement, html, count=1, flags=re.DOTALL)

print("Fix 3: Created diagram placeholder containers")

# Write the fixed HTML
with open(os.path.join(WORKSPACE, 'index.html'), 'w') as f:
    f.write(html)

print(f"\nFinal file size: {len(html)} bytes")
print("All fixes applied.")
