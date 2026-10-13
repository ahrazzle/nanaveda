#!/usr/bin/env python3
"""Verify no duplicate clickable terms within the same recipe."""
import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(WORKSPACE, 'index.html')) as f:
    html = f.read()

# Extract each recipe block
recipe_pattern = re.compile(r'<article id="recipe-(\d+)"[^>]*>(.*?)</article>', re.DOTALL)

for match in recipe_pattern.finditer(html):
    recipe_num = match.group(1)
    recipe_content = match.group(2)
    
    # Find all clickable terms in this recipe
    terms = re.findall(r'data-term="([^"]+)"', recipe_content)
    duplicates = [t for t in set(terms) if terms.count(t) > 1]
    
    if duplicates:
        print(f"Recipe {recipe_num}: DUPLICATES FOUND - {duplicates}")
    else:
        print(f"Recipe {recipe_num}: All terms unique")
