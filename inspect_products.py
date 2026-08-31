import json

with open('extracted_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages:
    txt = p['text'].strip()
    if txt:
        first_lines = [line.strip() for line in txt.split('\n') if line.strip()]
        print(f"Page {p['page']}: {first_lines[:10]}")
