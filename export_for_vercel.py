"""
Nanobot Vercel Export Helper
Creates a clean, deployment-ready ZIP file of the catalog for 1-click upload to Vercel / GitHub.
"""

import os
import zipfile

def create_vercel_zip():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    zip_path = os.path.join(base_dir, "nanobot-catalog-vercel.zip")
    
    # Files/folders to include
    include_items = ["index.html", "vercel.json", "README.md", "css", "js"]
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in include_items:
            item_path = os.path.join(base_dir, item)
            if os.path.isfile(item_path):
                zipf.write(item_path, arcname=item)
            elif os.path.isdir(item_path):
                for root, _, files in os.walk(item_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        rel_path = os.path.relpath(file_path, base_dir)
                        zipf.write(file_path, arcname=rel_path)

    print("="*60)
    print("Vercel Deployment Package Created Successfully!")
    print(f"ZIP Archive: {zip_path}")
    print("="*60)

if __name__ == "__main__":
    create_vercel_zip()
