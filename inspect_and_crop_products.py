import os
import pymupdf # PyMuPDF
from PIL import Image

os.makedirs("images/products", exist_ok=True)

# 1. Open the Price List PDF (42 pages)
price_doc = pymupdf.open(r"C:\Users\vikas\Downloads\Nanobot Price List W.E.F. July 2026 DP.pdf")
print("Rendering high-res pages from Price List...")

for pno in range(len(price_doc)):
    page = price_doc[pno]
    pix = page.get_pixmap(dpi=200) # High quality
    out_path = f"images/products/page_{pno+1}_full.png"
    pix.save(out_path)
    
    # Also extract embedded images from the page
    image_list = page.get_images(full=True)
    for img_idx, img_info in enumerate(image_list):
        xref = img_info[0]
        base_img = price_doc.extract_image(xref)
        img_bytes = base_img["image"]
        ext = base_img["ext"]
        img_filename = f"images/products/page_{pno+1}_img_{img_idx+1}.{ext}"
        with open(img_filename, "wb") as f:
            f.write(img_bytes)

print(f"Extracted all images and full page renders from Price List PDF ({len(price_doc)} pages).")

# 2. Open Nanobot_Catalogue_Ver01.pdf (Brochure with studio photos)
cat_doc = pymupdf.open(r"C:\Users\vikas\Downloads\Nanobot_Catalogue_Ver01.pdf")
print(f"Rendering high-res pages from Catalogue Ver01 ({len(cat_doc)} pages)...")

for pno in range(len(cat_doc)):
    page = cat_doc[pno]
    pix = page.get_pixmap(dpi=200)
    out_path = f"images/products/catalogue_page_{pno+1}_full.png"
    pix.save(out_path)
    
    image_list = page.get_images(full=True)
    for img_idx, img_info in enumerate(image_list):
        xref = img_info[0]
        base_img = cat_doc.extract_image(xref)
        img_bytes = base_img["image"]
        ext = base_img["ext"]
        img_filename = f"images/products/catalogue_page_{pno+1}_img_{img_idx+1}.{ext}"
        with open(img_filename, "wb") as f:
            f.write(img_bytes)

print("Extraction completed successfully!")
