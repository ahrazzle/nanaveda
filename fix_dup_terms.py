#!/usr/bin/env python3
"""Fix duplicate clickable terms in recipes 4 and 8."""
import os
import re

WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'

with open(os.path.join(WORKSPACE, 'index.html')) as f:
    html = f.read()

# For each recipe, find duplicate terms and remove clickable-term from second occurrence
recipe_pattern = re.compile(r'<article id="recipe-(\d+)"[^>]*>(.*?)</article>', re.DOTALL)

for match in recipe_pattern.finditer(html):
    recipe_num = match.group(1)
    recipe_content = match.group(2)
    
    # Find all clickable terms in this recipe
    terms = re.findall(r'data-term="([^"]+)"', recipe_content)
    duplicates = [t for t in set(terms) if terms.count(t) > 1]
    
    for dup_term in duplicates:
        # Find all occurrences of this term
        term_pattern = re.compile(r'<span class="term clickable-term" data-term="' + re.escape(dup_term) + r'">([^<]+)</span>')
        occurrences = list(term_pattern.finditer(recipe_content))
        
        # Keep first, remove clickable class from second
        if len(occurrences) > 1:
            second_occurrence = occurrences[1]
            old_span = second_occurrence.group(0)
            new_span = f'<span data-term="{dup_term}">{second_occurrence.group(1)}</span>'
            recipe_content = recipe_content.replace(old_span, new_span, 1)
            print(f"Recipe {recipe_num}: Removed duplicate clickable for '{dup_term}'")
    
    # Replace the recipe content in the full HTML
    html = html.replace(match.group(2), recipe_content)

with open(os.path.join(WORKSPACE, 'index.html'), 'w') as f:
    f.write(html)

print("Fixed.")
