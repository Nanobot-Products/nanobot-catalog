import os
import pymupdf
from PIL import Image

# Let's inspect the models and their pages in "Nanobot Price List W.E.F. July 2026 DP.pdf"
# Double Layer:
# Page 3: Therma Plain (350, 500, 750, 1000 ml)
# Page 4: Thermax Color (350, 500, 750, 1000 ml)
# Page 8: Kryo (350, 500, 750, 1000, 1500, 1800 ml)
# Page 10: Doro Double Layer (500, 750, 1000 ml)
# Page 11: Vepo Go Slim & Falcon (500, 700 ml)
# Page 12: Rover (500, 750 ml)
# Page 13: Hiker (500, 750 ml)
# Page 14: Mince (220, 400 ml)
# Page 15: Orion, Gruss & Crater (500, 700 ml)
# Page 16: Aura & Univa (350, 400, 460, 700 ml)
# Page 17: Vacuum Flask Combo Sets (Therma Duo, Trio, Quattro)
# Page 18: Kettl Carafe (350, 500, 750, 1000, 1500 ml)
# Page 20: Kettl Combo Sets (Trio, Quattro)
# Page 21: Lunch Therma (220, 330, 470 ml)
# Page 22-24: Tiffin Combo Sets

# Single Layer:
# Page 26: Doro Single Layer (750, 1000 ml)
# Page 27: Jr. Nero (400, 600 ml)
# Page 28: Twist (900 ml) & Energex (800 ml)
# Page 29: Vyoma (750, 1000 ml)
# Page 30: Pico (400 ml)
# Page 31: Ace & Whizzy & Agua (750, 1000 ml)
# Page 32: Black Panther & Tesla (700, 750 ml)
# Page 33: Thar & Thar Diamond (750, 1000 ml)
# Page 34: Akua (500, 700 ml)
# Page 35: Mizu & Neer (700, 800 ml)
# Page 36: Sleek (300, 500 ml)
# Page 37: Sip & Mist (750, 1000 ml)
# Page 38: Prisma (750, 1000 ml)
# Page 39: Neo (750, 1000 ml)
# Page 40: Oil Dispenser (1100 ml)
# Page 41: Eco Drink Sets (Mizu & Nero 700, 1000 ml)

doc = pymupdf.open(r"C:\Users\vikas\Downloads\Nanobot Price List W.E.F. July 2026 DP.pdf")

def crop_bottle_image(page_num, bbox_ratio, output_filename):
    """
    bbox_ratio = (x0_ratio, y0_ratio, x1_ratio, y1_ratio) from (0,0) to (1,1)
    """
    page = doc[page_num - 1]
    pix = page.get_pixmap(dpi=300)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    w, h = img.size
    box = (
        int(bbox_ratio[0] * w),
        int(bbox_ratio[1] * h),
        int(bbox_ratio[2] * w),
        int(bbox_ratio[3] * h)
    )
    cropped = img.crop(box)
    
    # Save optimized crop
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    cropped.save(output_filename, quality=95)
    print(f"Saved {output_filename} ({cropped.size})")

# Crop the clean bottle visual area (excluding text tables) for each key model:
crops = [
    # Double Layer
    (3, (0.05, 0.28, 0.95, 0.72), "images/products/nb-dl-therma.png"),
    (4, (0.05, 0.28, 0.95, 0.72), "images/products/nb-dl-thermax.png"),
    (8, (0.05, 0.26, 0.95, 0.70), "images/products/nb-dl-kryo.png"),
    (10, (0.05, 0.28, 0.95, 0.72), "images/products/nb-dl-doro.png"),
    (11, (0.05, 0.28, 0.95, 0.72), "images/products/nb-dl-vepo.png"),
    (12, (0.05, 0.28, 0.95, 0.72), "images/products/nb-dl-rover.png"),
    (13, (0.05, 0.28, 0.95, 0.72), "images/products/nb-dl-hiker.png"),
    (14, (0.05, 0.28, 0.95, 0.72), "images/products/nb-dl-mince.png"),
    (15, (0.05, 0.28, 0.95, 0.72), "images/products/nb-dl-orion.png"),
    (16, (0.05, 0.28, 0.95, 0.72), "images/products/nb-dl-aura.png"),
    (17, (0.05, 0.22, 0.95, 0.75), "images/products/nb-dl-combos.png"),
    (18, (0.05, 0.28, 0.95, 0.72), "images/products/nb-dl-kettl.png"),
    (20, (0.05, 0.22, 0.95, 0.75), "images/products/nb-dl-kettl-combos.png"),
    (21, (0.05, 0.22, 0.95, 0.75), "images/products/nb-dl-lunch.png"),
    
    # Single Layer
    (26, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-doro.png"),
    (27, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-nero.png"),
    (28, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-twist.png"),
    (29, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-vyoma.png"),
    (30, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-pico.png"),
    (31, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-agua.png"),
    (32, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-tesla.png"),
    (33, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-thar.png"),
    (34, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-akua.png"),
    (35, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-neer.png"),
    (36, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-sleek.png"),
    (37, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-sip-mist.png"),
    (38, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-prisma.png"),
    (39, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-neo.png"),
    (40, (0.05, 0.28, 0.95, 0.72), "images/products/nb-sl-oil.png"),
    (41, (0.05, 0.22, 0.95, 0.75), "images/products/nb-sl-eco-sets.png"),
]

for pno, bbox, out in crops:
    crop_bottle_image(pno, bbox, out)

print("All specific product bottle images cropped cleanly!")
