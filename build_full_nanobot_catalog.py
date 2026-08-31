"""
Build complete Nanobot products.js with authentic data from Nanobot Price List & Catalogues
"""

import json

products = [
  # ==========================================
  # DOUBLE LAYER (VACUUM INSULATED FLASKS)
  # ==========================================
  {
    "id": "nb-dl-therma",
    "sku": "NB-DL-TH01",
    "name": "Nanobot Therma Vacuum Flask",
    "layerType": "double_layer",
    "category": "vacuum",
    "tagline": "Flagship Double Layer SUS 304 Vacuum Flask (24h Cold / 18h Hot)",
    "description": "Engineered with true vacuum double-wall technology and high-micron copper reflective coating. Keeps beverages hot for 18 hours or cold for 24 hours with zero sweat.",
    "steelGrade": "SUS 304 (18/8) Virgin Food Grade",
    "insulation": "Double Layer Vacuum + Copper Shield",
    "hotHours": 18,
    "coldHours": 24,
    "lidType": "Precision Screw Cap with Stainless Steel Accent",
    "imageUrl": "images/price_list_2026_p3.png",
    "isBestseller": True,
    "isNew": False,
    "variants": [
      { "capacity": "350 ml", "mrp": 719, "dpPrice": 360, "price": 719, "wholesalePrice": 360, "weight": "289g" },
      { "capacity": "500 ml", "mrp": 809, "dpPrice": 405, "price": 809, "wholesalePrice": 405, "weight": "332g" },
      { "capacity": "750 ml", "mrp": 1079, "dpPrice": 540, "price": 1079, "wholesalePrice": 540, "weight": "484g" },
      { "capacity": "1000 ml", "mrp": 1199, "dpPrice": 600, "price": 1199, "wholesalePrice": 600, "weight": "556g" }
    ],
    "colors": [
      { "name": "Brushed Plain Steel", "hex": "#cbd5e1", "textColor": "#111827" },
      { "name": "Matte Black", "hex": "#1a1a1a", "textColor": "#ffffff" },
      { "name": "Royal Blue", "hex": "#1e3a8a", "textColor": "#ffffff" },
      { "name": "Sky Blue", "hex": "#38bdf8", "textColor": "#0f172a" },
      { "name": "Lavender", "hex": "#c084fc", "textColor": "#ffffff" },
      { "name": "Raspberry Pink", "hex": "#f43f5e", "textColor": "#ffffff" }
    ],
    "moqBulk": 25,
    "bottleStyle": "flask"
  },
  {
    "id": "nb-dl-kryo",
    "sku": "NB-DL-KR02",
    "name": "Nanobot Kryo Double Layer Flask",
    "layerType": "double_layer",
    "category": "vacuum",
    "tagline": "High-Volume Vacuum Expedition Flask (Up to 1800ml)",
    "description": "Heavy-duty double wall vacuum flask for long journeys, corporate executive desks, and all-day outdoor hydration.",
    "steelGrade": "SUS 304 Heavy Gauge",
    "insulation": "Double Layer Deep Vacuum",
    "hotHours": 24,
    "coldHours": 36,
    "lidType": "Heavy-Duty Insulated Stopper Lid with Cup",
    "imageUrl": "images/price_list_2026_p8.png",
    "isBestseller": True,
    "isNew": False,
    "variants": [
      { "capacity": "350 ml", "mrp": 699, "dpPrice": 350, "price": 699, "wholesalePrice": 350, "weight": "290g" },
      { "capacity": "500 ml", "mrp": 839, "dpPrice": 420, "price": 839, "wholesalePrice": 420, "weight": "340g" },
      { "capacity": "750 ml", "mrp": 1039, "dpPrice": 520, "price": 1039, "wholesalePrice": 520, "weight": "460g" },
      { "capacity": "1000 ml", "mrp": 1249, "dpPrice": 625, "price": 1249, "wholesalePrice": 625, "weight": "560g" },
      { "capacity": "1500 ml", "mrp": 1899, "dpPrice": 950, "price": 1899, "wholesalePrice": 950, "weight": "750g" },
      { "capacity": "1800 ml", "mrp": 1999, "dpPrice": 1000, "price": 1999, "wholesalePrice": 1000, "weight": "840g" }
    ],
    "colors": [
      { "name": "Brushed Steel", "hex": "#cbd5e1", "textColor": "#111827" },
      { "name": "Onyx Black", "hex": "#1e293b", "textColor": "#ffffff" },
      { "name": "Military Green", "hex": "#3f4f34", "textColor": "#ffffff" }
    ],
    "moqBulk": 20,
    "bottleStyle": "summit"
  },
  {
    "id": "nb-dl-doro",
    "sku": "NB-DL-DO03",
    "name": "Nanobot Doro Vacuum Bottle",
    "layerType": "double_layer",
    "category": "vacuum",
    "tagline": "Modern Ergonomic Double Wall Vacuum Hydration Bottle",
    "description": "Clean silhouette with smooth rolled sipping lip and double wall thermal insulation for home, car, and office.",
    "steelGrade": "SUS 304 (18/8) Food Safe",
    "insulation": "Double Layer Vacuum",
    "hotHours": 18,
    "coldHours": 24,
    "lidType": "Hermetic SS Screw Cap",
    "imageUrl": "images/price_list_2026_p10.png",
    "isBestseller": True,
    "isNew": False,
    "variants": [
      { "capacity": "500 ml", "mrp": 799, "dpPrice": 399, "price": 799, "wholesalePrice": 399, "weight": "320g" },
      { "capacity": "750 ml", "mrp": 939, "dpPrice": 469, "price": 939, "wholesalePrice": 469, "weight": "420g" },
      { "capacity": "1000 ml", "mrp": 1099, "dpPrice": 550, "price": 1099, "wholesalePrice": 550, "weight": "510g" }
    ],
    "colors": [
      { "name": "Matte Plain Steel", "hex": "#d1d5db", "textColor": "#111827" },
      { "name": "Midnight Black", "hex": "#111827", "textColor": "#ffffff" },
      { "name": "Rose Gold", "hex": "#be7c72", "textColor": "#ffffff" }
    ],
    "moqBulk": 25,
    "bottleStyle": "flask"
  },
  {
    "id": "nb-dl-vepo-goslim",
    "sku": "NB-DL-VG04",
    "name": "Nanobot Vepo Go Slim & Falcon",
    "layerType": "double_layer",
    "category": "vacuum",
    "tagline": "Ultra-Slim Double Wall Vacuum Flask for Backpacks & Handbags",
    "description": "Space-saving slimline vacuum bottle that slips effortlessly into compact briefcases, laptop bags, and side pockets.",
    "steelGrade": "SUS 304 Food Grade",
    "insulation": "Ultra-Slim Double Layer Vacuum",
    "hotHours": 14,
    "coldHours": 20,
    "lidType": "Compact Twist Cap with Silicone Seal",
    "imageUrl": "images/price_list_2026_p11.png",
    "isBestseller": False,
    "isNew": True,
    "variants": [
      { "capacity": "500 ml", "mrp": 699, "dpPrice": 350, "price": 699, "wholesalePrice": 350, "weight": "270g" },
      { "capacity": "700 ml", "mrp": 799, "dpPrice": 400, "price": 799, "wholesalePrice": 400, "weight": "340g" }
    ],
    "colors": [
      { "name": "Brushed Steel", "hex": "#cbd5e1", "textColor": "#111827" },
      { "name": "Matte Charcoal", "hex": "#27272a", "textColor": "#ffffff" },
      { "name": "Cyan Blue", "hex": "#06b6d4", "textColor": "#ffffff" }
    ],
    "moqBulk": 25,
    "bottleStyle": "infuser"
  },
  {
    "id": "nb-dl-rover-hiker",
    "sku": "NB-DL-RH05",
    "name": "Nanobot Rover & Hiker Sports Flask",
    "layerType": "double_layer",
    "category": "sports",
    "tagline": "Active Sports Vacuum Flask with Rugged Grip & Loop Cap",
    "description": "Engineered for outdoor trekking and gym hydration with ergonomic carry handle and high-impact base.",
    "steelGrade": "SUS 304 High Impact",
    "insulation": "Double Layer Vacuum",
    "hotHours": 12,
    "coldHours": 24,
    "lidType": "Sports Loop Handle Cap",
    "imageUrl": "images/price_list_2026_p12.png",
    "isBestseller": False,
    "isNew": True,
    "variants": [
      { "capacity": "500 ml", "mrp": 749, "dpPrice": 375, "price": 749, "wholesalePrice": 375, "weight": "310g" },
      { "capacity": "750 ml", "mrp": 799, "dpPrice": 400, "price": 799, "wholesalePrice": 400, "weight": "390g" }
    ],
    "colors": [
      { "name": "Stealth Black", "hex": "#18181b", "textColor": "#ffffff" },
      { "name": "Army Green", "hex": "#3f4f34", "textColor": "#ffffff" },
      { "name": "Desert Sand", "hex": "#c2b280", "textColor": "#111827" }
    ],
    "moqBulk": 25,
    "bottleStyle": "sports"
  },
  {
    "id": "nb-dl-kettl-carafe",
    "sku": "NB-DL-KT06",
    "name": "Nanobot Kettl Vacuum Tabletop Carafe",
    "layerType": "double_layer",
    "category": "vacuum",
    "tagline": "Executive Tabletop Thermal Pot & Coffee/Tea Kettle",
    "description": "Double wall vacuum dispenser carafe with push-pour lever for boardrooms, dining tables, hotels, and cafes.",
    "steelGrade": "SUS 304 Interior & Exterior",
    "insulation": "Heavy Double Layer Thermal Shield",
    "hotHours": 24,
    "coldHours": 36,
    "lidType": "Thumb-Press Spout with Heat Stopper",
    "imageUrl": "images/price_list_2026_p18.png",
    "isBestseller": True,
    "isNew": True,
    "variants": [
      { "capacity": "350 ml", "mrp": 899, "dpPrice": 450, "price": 899, "wholesalePrice": 450, "weight": "380g" },
      { "capacity": "500 ml", "mrp": 1049, "dpPrice": 525, "price": 1049, "wholesalePrice": 525, "weight": "440g" },
      { "capacity": "750 ml", "mrp": 1149, "dpPrice": 575, "price": 1149, "wholesalePrice": 575, "weight": "530g" },
      { "capacity": "1000 ml", "mrp": 1249, "dpPrice": 625, "price": 1249, "wholesalePrice": 625, "weight": "610g" },
      { "capacity": "1500 ml", "mrp": 1499, "dpPrice": 750, "price": 1499, "wholesalePrice": 750, "weight": "740g" }
    ],
    "colors": [
      { "name": "Brushed Satin Steel", "hex": "#cbd5e1", "textColor": "#111827" },
      { "name": "Onyx Matte Black", "hex": "#18181b", "textColor": "#ffffff" },
      { "name": "Ruby Maroon", "hex": "#881337", "textColor": "#ffffff" }
    ],
    "moqBulk": 15,
    "bottleStyle": "carafe"
  },
  {
    "id": "nb-dl-univa",
    "sku": "NB-DL-UN07",
    "name": "Nanobot Univa Vacuum Flask",
    "layerType": "double_layer",
    "category": "vacuum",
    "tagline": "Compact Daily Double Layer Office Flask",
    "description": "Minimalist double-wall stainless steel bottle designed for tea, coffee, and fresh cold water.",
    "steelGrade": "SUS 304 Food Safe",
    "insulation": "Double Layer Vacuum",
    "hotHours": 14,
    "coldHours": 20,
    "lidType": "Insulated Twist Stopper",
    "imageUrl": "images/price_list_2026_p16.png",
    "isBestseller": False,
    "isNew": False,
    "variants": [
      { "capacity": "350 ml", "mrp": 569, "dpPrice": 285, "price": 569, "wholesalePrice": 285, "weight": "260g" },
      { "capacity": "460 ml", "mrp": 739, "dpPrice": 370, "price": 739, "wholesalePrice": 370, "weight": "310g" }
    ],
    "colors": [
      { "name": "Brushed Steel", "hex": "#cbd5e1", "textColor": "#111827" },
      { "name": "Matte Black", "hex": "#1e293b", "textColor": "#ffffff" }
    ],
    "moqBulk": 30,
    "bottleStyle": "flask"
  },
  {
    "id": "nb-dl-combo-sets",
    "sku": "NB-DL-CB08",
    "name": "Nanobot Therma & Kettl Gift Combo Sets",
    "layerType": "double_layer",
    "category": "vacuum",
    "tagline": "Premium Corporate Gifting Vacuum Flask + Double Wall SS Cups Sets",
    "description": "Luxury executive gift boxes including 1 vacuum bottle with 2, 3, or 4 double-walled stainless steel cups in rigid gift packaging.",
    "steelGrade": "SUS 304 Food Safe",
    "insulation": "Double Layer Vacuum",
    "hotHours": 18,
    "coldHours": 24,
    "lidType": "Insulated Pour Stopper",
    "imageUrl": "images/price_list_2026_p17.png",
    "isBestseller": True,
    "isNew": True,
    "variants": [
      { "capacity": "Therma Duo (Flask + 2 Cups)", "mrp": 1049, "dpPrice": 525, "price": 1049, "wholesalePrice": 525, "weight": "650g" },
      { "capacity": "Therma Trio (Flask + 3 Cups)", "mrp": 1299, "dpPrice": 649, "price": 1299, "wholesalePrice": 649, "weight": "780g" },
      { "capacity": "Therma Quattro (Flask + 4 Cups)", "mrp": 1599, "dpPrice": 799, "price": 1599, "wholesalePrice": 799, "weight": "920g" }
    ],
    "colors": [
      { "name": "Corporate Matte Black", "hex": "#1a1a1a", "textColor": "#ffffff" },
      { "name": "Royal Blue", "hex": "#1e3a8a", "textColor": "#ffffff" },
      { "name": "Brushed Steel", "hex": "#cbd5e1", "textColor": "#111827" }
    ],
    "moqBulk": 10,
    "bottleStyle": "flask"
  },

  # ==========================================
  # SINGLE LAYER (STAINLESS STEEL FRIDGE BOTTLES)
  # ==========================================
  {
    "id": "nb-sl-doro-fridge",
    "sku": "NB-SL-DF01",
    "name": "Nanobot Doro Single Layer Fridge Bottle",
    "layerType": "single_layer",
    "category": "fridge",
    "tagline": "Pure SUS 304 Single Layer Rapid Refrigerator Chilling Bottle",
    "description": "The healthy, durable replacement for plastic fridge bottles. Made from virgin 304 food-grade stainless steel that rapidly absorbs fridge coldness.",
    "steelGrade": "SUS 304 (18/8) Virgin Food Grade",
    "insulation": "Single Layer (Fast Fridge Chill)",
    "hotHours": 0,
    "coldHours": 0,
    "lidType": "Precision Leakproof SS Cap with Silicone Gasket",
    "imageUrl": "images/price_list_2026_p26.png",
    "isBestseller": True,
    "isNew": False,
    "variants": [
      { "capacity": "750 ml", "mrp": 359, "dpPrice": 162, "price": 359, "wholesalePrice": 162, "weight": "170g" },
      { "capacity": "1000 ml", "mrp": 399, "dpPrice": 180, "price": 399, "wholesalePrice": 180, "weight": "210g" }
    ],
    "colors": [
      { "name": "Mirror Gloss Steel", "hex": "#e5e7eb", "textColor": "#111827" },
      { "name": "Brushed Matte Steel", "hex": "#cbd5e1", "textColor": "#111827" },
      { "name": "Matte Black", "hex": "#1e293b", "textColor": "#ffffff" },
      { "name": "Royal Blue", "hex": "#1d4ed8", "textColor": "#ffffff" }
    ],
    "moqBulk": 50,
    "bottleStyle": "fridge"
  },
  {
    "id": "nb-sl-jr-nero",
    "sku": "NB-SL-JN02",
    "name": "Nanobot Jr. Nero Single Layer Bottle",
    "layerType": "single_layer",
    "category": "kids",
    "tagline": "Compact Single Layer Steel Bottle for School & Daily Hydration",
    "description": "Featherlight, unbreakable SUS 304 school bottle with ergonomic cap and rounded child-safe base.",
    "steelGrade": "SUS 304 Food Safe",
    "insulation": "Single Layer",
    "hotHours": 0,
    "coldHours": 0,
    "lidType": "Easy-Grip Cap with Carry Ring",
    "imageUrl": "images/price_list_2026_p27.png",
    "isBestseller": True,
    "isNew": False,
    "variants": [
      { "capacity": "400 ml", "mrp": 299, "dpPrice": 135, "price": 299, "wholesalePrice": 135, "weight": "135g" },
      { "capacity": "600 ml", "mrp": 329, "dpPrice": 148, "price": 329, "wholesalePrice": 148, "weight": "160g" }
    ],
    "colors": [
      { "name": "Gloss Steel", "hex": "#e2e8f0", "textColor": "#111827" },
      { "name": "Matte Black", "hex": "#18181b", "textColor": "#ffffff" },
      { "name": "Sky Cyan", "hex": "#0284c7", "textColor": "#ffffff" }
    ],
    "moqBulk": 50,
    "bottleStyle": "kids"
  },
  {
    "id": "nb-sl-vyoma-agua",
    "sku": "NB-SL-VA03",
    "name": "Nanobot Vyoma & Agua Fridge Bottle",
    "layerType": "single_layer",
    "category": "fridge",
    "tagline": "Full 1 Litre Single Layer Dining Table & Fridge Bottle",
    "description": "Sleek cylindrical fridge door bottle with hermetic silicone-ring stainless steel cap.",
    "steelGrade": "SUS 304 Virgin Steel",
    "insulation": "Single Layer",
    "hotHours": 0,
    "coldHours": 0,
    "lidType": "Stainless Steel Threaded Cap",
    "imageUrl": "images/price_list_2026_p29.png",
    "isBestseller": True,
    "isNew": False,
    "variants": [
      { "capacity": "750 ml", "mrp": 369, "dpPrice": 166, "price": 369, "wholesalePrice": 166, "weight": "175g" },
      { "capacity": "1000 ml", "mrp": 419, "dpPrice": 189, "price": 419, "wholesalePrice": 189, "weight": "215g" }
    ],
    "colors": [
      { "name": "Mirror Plain Steel", "hex": "#cbd5e1", "textColor": "#111827" },
      { "name": "Midnight Black", "hex": "#111827", "textColor": "#ffffff" },
      { "name": "Emerald Green", "hex": "#047857", "textColor": "#ffffff" }
    ],
    "moqBulk": 50,
    "bottleStyle": "fridge"
  },
  {
    "id": "nb-sl-thar-diamond",
    "sku": "NB-SL-TD04",
    "name": "Nanobot Thar & Thar Diamond Series",
    "layerType": "single_layer",
    "category": "fridge",
    "tagline": "Geometric Faceted Textured Single Layer Stainless Steel Bottle",
    "description": "Unique diamond-cut faceted grip body for superior tactile feel and modern aesthetic on dining tables.",
    "steelGrade": "SUS 304 High-Tensile Steel",
    "insulation": "Single Layer",
    "hotHours": 0,
    "coldHours": 0,
    "lidType": "Ergonomic Diamond Texture SS Cap",
    "imageUrl": "images/price_list_2026_p33.png",
    "isBestseller": False,
    "isNew": True,
    "variants": [
      { "capacity": "750 ml", "mrp": 469, "dpPrice": 211, "price": 469, "wholesalePrice": 211, "weight": "190g" },
      { "capacity": "1000 ml", "mrp": 549, "dpPrice": 247, "price": 549, "wholesalePrice": 247, "weight": "230g" }
    ],
    "colors": [
      { "name": "Diamond Satin Steel", "hex": "#cbd5e1", "textColor": "#111827" },
      { "name": "Matte Jet Black", "hex": "#18181b", "textColor": "#ffffff" },
      { "name": "Bronze Gold", "hex": "#b45309", "textColor": "#ffffff" }
    ],
    "moqBulk": 40,
    "bottleStyle": "fridge"
  },
  {
    "id": "nb-sl-sleek-pico",
    "sku": "NB-SL-SP05",
    "name": "Nanobot Sleek & Pico Slim Bottle",
    "layerType": "single_layer",
    "category": "fridge",
    "tagline": "Ultra-Compact 300ml - 500ml Single Layer Pocket Steel Bottle",
    "description": "Ultra slim body designed for kids bags, handbag carrying, and quick hydration.",
    "steelGrade": "SUS 304 Baby-Safe Grade",
    "insulation": "Single Layer",
    "hotHours": 0,
    "coldHours": 0,
    "lidType": "Thread Cap with SS Ring",
    "imageUrl": "images/price_list_2026_p36.png",
    "isBestseller": False,
    "isNew": False,
    "variants": [
      { "capacity": "300 ml", "mrp": 259, "dpPrice": 117, "price": 259, "wholesalePrice": 117, "weight": "115g" },
      { "capacity": "500 ml", "mrp": 289, "dpPrice": 130, "price": 289, "wholesalePrice": 130, "weight": "145g" }
    ],
    "colors": [
      { "name": "Mirror Steel", "hex": "#e2e8f0", "textColor": "#111827" },
      { "name": "Matte Black", "hex": "#1e293b", "textColor": "#ffffff" }
    ],
    "moqBulk": 50,
    "bottleStyle": "kids"
  },
  {
    "id": "nb-sl-sip-mist",
    "sku": "NB-SL-SM06",
    "name": "Nanobot Sip & Mist Sports Bottle",
    "layerType": "single_layer",
    "category": "sports",
    "tagline": "Dual-Function Single Layer Sports Bottle with Refreshing Mist Spray",
    "description": "Combines drinking nozzle and built-in fine mist sprayer to cool down during intense workouts and outdoor sports.",
    "steelGrade": "SUS 304 Food Safe",
    "insulation": "Single Layer",
    "hotHours": 0,
    "coldHours": 0,
    "lidType": "Sip & Mist Dual Trigger Mechanism",
    "imageUrl": "images/price_list_2026_p37.png",
    "isBestseller": True,
    "isNew": True,
    "variants": [
      { "capacity": "750 ml", "mrp": 578, "dpPrice": 260, "price": 578, "wholesalePrice": 260, "weight": "210g" },
      { "capacity": "1000 ml", "mrp": 638, "dpPrice": 287, "price": 638, "wholesalePrice": 287, "weight": "250g" }
    ],
    "colors": [
      { "name": "Cobalt Blue", "hex": "#1d4ed8", "textColor": "#ffffff" },
      { "name": "Matte Black", "hex": "#18181b", "textColor": "#ffffff" },
      { "name": "Silver Gloss", "hex": "#cbd5e1", "textColor": "#111827" }
    ],
    "moqBulk": 30,
    "bottleStyle": "sports"
  },
  {
    "id": "nb-sl-prisma-neo",
    "sku": "NB-SL-PN07",
    "name": "Nanobot Prisma & Neo Fridge Bottle",
    "layerType": "single_layer",
    "category": "fridge",
    "tagline": "Contemporary Textured Prism Pattern Fridge Bottle",
    "description": "Multi-faceted prism design reflecting light beautifully with quick fridge cooling capability.",
    "steelGrade": "SUS 304 Food Grade",
    "insulation": "Single Layer",
    "hotHours": 0,
    "coldHours": 0,
    "lidType": "Leakproof Stainless Steel Cap",
    "imageUrl": "images/price_list_2026_p38.png",
    "isBestseller": False,
    "isNew": True,
    "variants": [
      { "capacity": "750 ml", "mrp": 399, "dpPrice": 180, "price": 399, "wholesalePrice": 180, "weight": "180g" },
      { "capacity": "1000 ml", "mrp": 489, "dpPrice": 220, "price": 489, "wholesalePrice": 220, "weight": "220g" }
    ],
    "colors": [
      { "name": "Brushed Steel", "hex": "#cbd5e1", "textColor": "#111827" },
      { "name": "Matte Charcoal", "hex": "#27272a", "textColor": "#ffffff" }
    ],
    "moqBulk": 40,
    "bottleStyle": "fridge"
  }
]

# Wholesale Volume Discount Tiers Configuration
WHOLESALE_TIERS = [
  { "minQty": 1, "maxQty": 9, "label": "Retail Tier (MRP)", "discountPercent": 0, "tag": "MRP Rate" },
  { "minQty": 10, "maxQty": 49, "label": "Dealer Base Tier (DP Rate)", "discountPercent": 0, "tag": "Dealer Price (DP)" },
  { "minQty": 50, "maxQty": 199, "label": "Corporate Bulk Tier", "discountPercent": 10, "tag": "10% Extra on DP" },
  { "minQty": 200, "maxQty": 499, "label": "Super Stockist Tier", "discountPercent": 15, "tag": "15% Extra on DP" },
  { "minQty": 500, "maxQty": 999999, "label": "Factory Direct OEM/ODM", "discountPercent": 22, "tag": "Best Factory Rate" }
]

BRANDING_OPTIONS = [
  { "id": "none", "name": "Plain / Nanobot Factory Finish", "pricePerUnit": 0, "moq": 1, "desc": "Standard unbranded or Nanobot signature logo" },
  { "id": "laser", "name": "Precision Fiber Laser Engraving", "pricePerUnit": 25, "moq": 10, "desc": "Permanent crisp metallic silver mark, never fades" },
  { "id": "uv_print", "name": "Full Color UV Digital Print", "pricePerUnit": 45, "moq": 25, "desc": "High-resolution full color photo & gradient printing" },
  { "id": "screen_print", "name": "Single/Dual Color Screen Print", "pricePerUnit": 20, "moq": 50, "desc": "Cost-effective vibrant solid color printing for large runs" }
]

content = f"""/**
 * Nanobot Official Product Catalog Data
 * Loaded from official Nanobot July 2026 Price List & Catalog
 */

const DEFAULT_PRODUCTS = {json.dumps(products, indent=2)};

const WHOLESALE_TIERS = {json.dumps(WHOLESALE_TIERS, indent=2)};

const BRANDING_OPTIONS = {json.dumps(BRANDING_OPTIONS, indent=2)};
"""

with open("js/products.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated js/products.js successfully with all real Nanobot catalog models!")
