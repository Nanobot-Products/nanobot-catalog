import json

with open("catalog_summary.txt", "w", encoding="utf-8") as out:
    try:
        with open("nanobot_catalogue.json", "r", encoding="utf-8") as f:
            nanobot_cat = json.load(f)
        out.write("=== NANOBOT CATALOGUE.pdf ===\n")
        for p in nanobot_cat:
            out.write(p["text"] + "\n")
    except Exception as e:
        out.write(f"Error: {e}\n")
        
    try:
        with open("catalogue_ver01.json", "r", encoding="utf-8") as f:
            cat_ver1 = json.load(f)
        out.write("\n=== Nanobot_Catalogue_Ver01.pdf ===\n")
        for p in cat_ver1:
            out.write(f"--- Page {p['page']} ---\n")
            out.write(p["text"] + "\n")
    except Exception as e:
        out.write(f"Error: {e}\n")

    try:
        with open("price_list_2026.json", "r", encoding="utf-8") as f:
            price_list = json.load(f)
        out.write("\n=== Nanobot Price List W.E.F. July 2026 DP.pdf ===\n")
        for p in price_list:
            out.write(f"--- Page {p['page']} ---\n")
            out.write(p["text"] + "\n")
    except Exception as e:
        out.write(f"Error: {e}\n")

print("Done writing catalog_summary.txt")
