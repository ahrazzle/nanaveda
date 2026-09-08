#!/usr/bin/env python3
"""Research and asset collection script for Nanaveda recipe book."""
import json
import os
import time
import requests
from grokipedia_api import GrokipediaClient

# Configuration
UNSPLASH_ACCESS_KEY = 'U-EmS--yFXUR3-qdQ_vEYdgAeB9vosk1W2iJBdRP8zU'
WORKSPACE = '/Users/kethuda/Documents/ai work/Hermes/nanaveda/wrk/nvt6'
OUTPUT_DIR = os.path.join(WORKSPACE, 'ASSETS')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize Grokipedia client
client = GrokipediaClient()

# Key terms for clickable content
KEY_TERMS = {
    'health': ['phytic acid', 'curcumin', 'piperine', 'thymoquinone', 'beta-glucans', 
               'anthocyanins', 'zeaxanthin', 'nitric oxide', 'ACE inhibitors', 'agni',
               'tridoshic', 'Panchakarma', 'immunosenescence', 'spleen qi'],
    'history': ['Silk Road', 'Islamic Golden Age', 'Ottoman Empire', 'transatlantic slave trade'],
    'figures': ['Ibn al-Qayyim', 'Ibn Sina', 'Avicenna', 'Al-Zahrawi', 'Scholey'],
    'religious': ['Prophetic Medicine', 'Habba Sawda', 'Al-Tibb al-Nabawi']
}

# Recipe image queries for Unsplash
RECIPE_IMAGES = {
    'kitchari': 'rice lentil porridge bowl',
    'golden_milk': 'turmeric golden milk',
    'bone_broth': 'bone broth soup',
    'congee': 'congee rice porridge mushroom',
    'saffron_milk': 'saffron milk drink',
    'miso_soup': 'miso soup japanese',
    'hibiscus': 'hibiscus tea drink',
    'beetroot_sharbat': 'beetroot juice drink',
    'black_seed': 'black seed honey',
    'sage_tea': 'sage tea honey'
}

def search_grokipedia():
    """Search Grokipedia for all key terms."""
    print("=== Searching Grokipedia ===")
    results = {}
    all_terms = []
    for category, terms in KEY_TERMS.items():
        all_terms.extend(terms)
    
    for term in all_terms:
        try:
            print(f"  Searching: {term}")
            result = client.search(term)
            results[term] = result
            time.sleep(0.5)  # Rate limit
        except Exception as e:
            print(f"    Error: {e}")
            results[term] = None
    
    # Save results
    with open(os.path.join(OUTPUT_DIR, 'grokipedia_terms.json'), 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Saved {len(results)} Grokipedia results")
    return results

def source_unsplash():
    """Source images from Unsplash for each recipe."""
    print("\n=== Sourcing Unsplash Images ===")
    results = {}
    
    for recipe, query in RECIPE_IMAGES.items():
        try:
            print(f"  Searching: {query}")
            url = 'https://api.unsplash.com/search/photos'
            params = {
                'query': query,
                'per_page': 5,
                'client_id': UNSPLASH_ACCESS_KEY
            }
            r = requests.get(url, params=params)
            if r.status_code == 200:
                data = r.json()
                images = []
                for item in data.get('results', []):
                    images.append({
                        'id': item['id'],
                        'url': item['urls']['regular'],
                        'thumb': item['urls']['small'],
                        'alt': item.get('alt_description', ''),
                        'photographer': item['user']['name']
                    })
                results[recipe] = images
                print(f"    Found {len(images)} images")
            else:
                print(f"    Error: {r.status_code}")
                results[recipe] = []
            time.sleep(1)  # Rate limit
        except Exception as e:
            print(f"    Error: {e}")
            results[recipe] = []
    
    # Save results
    with open(os.path.join(OUTPUT_DIR, 'unsplash_images.json'), 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Saved Unsplash results for {len(results)} recipes")
    return results

def download_sample_images():
    """Download sample images for recipes."""
    print("\n=== Downloading Sample Images ===")
    with open(os.path.join(OUTPUT_DIR, 'unsplash_images.json')) as f:
        images = json.load(f)
    
    downloaded = {}
    for recipe, imgs in images.items():
        if imgs:
            try:
                img = imgs[0]  # Get first image
                print(f"  Downloading: {recipe}")
                r = requests.get(img['url'], timeout=10)
                if r.status_code == 200:
                    filename = f"{recipe}_hero.jpg"
                    filepath = os.path.join(OUTPUT_DIR, filename)
                    with open(filepath, 'wb') as f:
                        f.write(r.content)
                    downloaded[recipe] = filepath
                    print(f"    Saved: {filename} ({len(r.content)} bytes)")
                time.sleep(0.5)
            except Exception as e:
                print(f"    Error: {e}")
    
    print(f"Downloaded {len(downloaded)} images")
    return downloaded

if __name__ == '__main__':
    grokipedia_results = search_grokipedia()
    unsplash_results = source_unsplash()
    downloaded = download_sample_images()
    
    print("\n=== Summary ===")
    print(f"Grokipedia terms researched: {len(grokipedia_results)}")
    print(f"Unsplash recipes sourced: {len(unsplash_results)}")
    print(f"Images downloaded: {len(downloaded)}")
    print(f"Assets saved to: {OUTPUT_DIR}")
