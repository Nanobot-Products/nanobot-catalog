import os
import re

with open("js/products.js", "r", encoding="utf-8") as f:
    content = f.read()

image_matches = re.findall(r'imageUrl:\s*["\']([^"\']+)["\']', content)
print(f"Total product images linked: {len(image_matches)}")

all_ok = True
for img_path in image_matches:
    exists = os.path.exists(img_path)
    print(f"[{'EXISTS' if exists else 'MISSING'}] {img_path}")
    if not exists:
        all_ok = False

if all_ok:
    print("\nSUCCESS: All product images exist and are properly linked to PDF crops!")
else:
    print("\nWARNING: Some images are missing!")
