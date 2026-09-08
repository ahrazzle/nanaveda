#!/usr/bin/env python3
"""Fix duplicate clickable terms in recipes 4 and 8."""
import os
import re

WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'

with open(os.path.join(WORKSPACE, 'index.html')) as f:
    html = f.read()

# Find all article blocks
article_pattern = re.compile(r'<article id="recipe-(\d+)"[^>]*>(.*?)</article>', re.DOTALL)

for match in article_pattern.finditer(html):
    recipe_num = match.group(1)
    recipe_content = match.group(2)
    
    # Find all clickable terms in this recipe
    term_pattern = re.compile(r'data-term="([^"]+)"')
    terms = term_pattern.findall(recipe_content)
    
    # Find duplicates
    seen = set()
    duplicates = set()
    for term in terms:
        if term in seen:
            duplicates.add(term)
        seen.add(term)
    
    for dup_term in duplicates:
        # Find all clickable spans for this term
        span_pattern = re.compile(r'<span class="term clickable-term" data-term="' + re.escape(dup_term) + r'" title="[^"]*">[^<]+</span>')
        spans = list(span_pattern.finditer(recipe_content))
        
        if len(spans) > 1:
            # Keep first, modify second
            second_span = spans[1]
            old_text = second_span.group(0)
            # Replace with non-clickable version
            new_text = re.sub(r'class="term clickable-term"', 'class="term"', old_text)
            recipe_content = recipe_content.replace(old_text, new_text, 1)
            print(f"Recipe {recipe_num}: Fixed duplicate '{dup_term}'")
    
    # Replace in main HTML
    html = html.replace(match.group(2), recipe_content)

with open(os.path.join(WORKSPACE, 'index.html'), 'w') as f:
    f.write(html)

# Verify
with open(os.path.join(WORKSPACE, 'index.html')) as f:
    html = f.read()

print(f"\nFinal counts:")
print(f"clickable-term spans: {html.count('clickable-term')}")
print(f"data-term spans: {html.count('data-term=')}")
