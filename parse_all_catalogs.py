"""
Extract all product models, capacities, MRP, DP, and categories from all Nanobot PDFs
"""

import pymupdf
import json
import os
import re

def extract_pdf_data(pdf_path, output_name):
    doc = pymupdf.open(pdf_path)
    pages_list = []
    
    for i in range(len(doc)):
        page = doc[i]
        text = page.get_text("text")
        
        # Extract images
        image_list = page.get_images(full=True)
        img_paths = []
        for img_idx, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            if len(image_bytes) > 15000:
                name = f"{output_name}_p{i+1}_img{img_idx+1}.{ext}"
                path = os.path.join("images", name)
                with open(path, "wb") as f:
                    f.write(image_bytes)
                img_paths.append(f"images/{name}")
                
        # High-res crop of page
        pix = page.get_pixmap(dpi=150)
        preview_name = f"{output_name}_p{i+1}.png"
        pix.save(os.path.join("images", preview_name))
        
        pages_list.append({
            "page": i + 1,
            "text": text,
            "images": img_paths,
            "preview": f"images/{preview_name}"
        })
        
    with open(f"{output_name}.json", "w", encoding="utf-8") as f:
        json.dump(pages_list, f, indent=2, ensure_ascii=False)
        
    print(f"Extracted {len(pages_list)} pages from {pdf_path}")

os.makedirs("images", exist_ok=True)
extract_pdf_data(r"C:\Users\vikas\Downloads\Nanobot Price List W.E.F. July 2026 DP.pdf", "price_list_2026")
extract_pdf_data(r"C:\Users\vikas\Downloads\NANOBOT CATALOGUE.pdf", "nanobot_catalogue")
extract_pdf_data(r"C:\Users\vikas\Downloads\Nanobot_Catalogue_Ver01.pdf", "catalogue_ver01")
