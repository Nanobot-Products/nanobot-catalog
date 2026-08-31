import json
import os

with open('js/products.js', 'r', encoding='utf-8') as f:
    text = f.read()

json_str = text.split('const DEFAULT_PRODUCTS = ')[1].split(';\n\nconst WHOLESALE_TIERS')[0]
products = json.loads(json_str)

print(f"Total authentic products loaded: {len(products)}")
for p in products:
    img = p.get('imageUrl', '')
    status = "OK" if os.path.exists(img) else "MISSING"
    print(f"[{status}] {p['name']} ({p['layerType']}) -> {img}")
