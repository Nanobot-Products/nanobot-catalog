"""
Extract all products, pricing, specs, and images from Nanobot PDF catalog
"""

import pymupdf
import os
import json
import re

PDF_PATH = r"C:\Users\vikas\Downloads\Nanobot Price List W.E.F. July 2026 DP.pdf"
IMG_DIR = r"C:\Users\vikas\.gemini\antigravity\scratch\nanobot-catalog\images"

os.makedirs(IMG_DIR, exist_ok=True)

def parse_pdf():
    doc = pymupdf.open(PDF_PATH)
    print(f"Total pages: {len(doc)}")
    
    pages_data = []
    
    for page_index in range(len(doc)):
        page = doc[page_index]
        text = page.get_text("text")
        
        # Extract images from page
        image_list = page.get_images(full=True)
        saved_imgs = []
        
        for img_idx, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # Filter tiny icons / logos (< 15KB)
            if len(image_bytes) > 20000:
                img_name = f"page_{page_index+1}_img_{img_idx+1}.{image_ext}"
                img_path = os.path.join(IMG_DIR, img_name)
                with open(img_path, "wb") as f:
                    f.write(image_bytes)
                saved_imgs.append(f"images/{img_name}")
        
        # Also render a high-res page crop if product image extraction missed
        pix = page.get_pixmap(dpi=150)
        page_img_name = f"page_{page_index+1}_preview.png"
        pix.save(os.path.join(IMG_DIR, page_img_name))
        
        pages_data.append({
            "page": page_index + 1,
            "text": text,
            "images": saved_imgs,
            "page_image": f"images/{page_img_name}"
        })
        
    with open("extracted_pages.json", "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=2)
        
    print(f"Saved {len(pages_data)} pages data to extracted_pages.json")

if __name__ == "__main__":
    parse_pdf()
