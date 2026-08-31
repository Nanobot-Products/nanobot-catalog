# 🍾 Nanobot - Stainless Steel Bottle Digital Catalog & Quotation Portal

A modern, interactive digital product showcase and order/quotation portal built for **Nanobot** (Stainless Steel Vacuum Bottle & Fridge Bottle Manufacturers).

---

## 🚀 How to Deploy on Vercel (Step-by-Step)

Your project is completely pre-configured for Vercel with [`vercel.json`](./vercel.json)!

### Option 1: Deploy via GitHub + Vercel (Recommended for Auto-Updates)
1. Go to [GitHub.com](https://github.com) and create a new repository named `nanobot-catalog`.
2. Click **"uploading an existing file"** on GitHub, drag all files from this folder (`index.html`, `vercel.json`, `css/`, `js/`), and click **Commit changes**.
3. Go to [Vercel.com](https://vercel.com) and log in.
4. Click **"Add New..."** > **"Project"**.
5. Select your `nanobot-catalog` GitHub repository and click **"Deploy"**.
6. In ~15 seconds, Vercel will give you a live link like `https://nanobot-catalog.vercel.app` (or connect your custom domain like `catalog.nanobot.in`)!

---

### Option 2: Deploy using Vercel CLI (If Node.js is installed)
Run the following in PowerShell/terminal inside this folder:
```powershell
npx vercel
```
- When asked `Set up and deploy?`, press `y`.
- Accept all default prompts by pressing `Enter`.
- Done! You will get an instant `https://...vercel.app` link.

---

### Option 3: Deploy via Drag & Drop on Netlify (Instant 20-second alternative)
1. Go to [app.netlify.com/drop](https://app.netlify.com/drop).
2. Drag and drop the `nanobot-catalog` folder.
3. Your live link is generated immediately.

---

## 🌟 Key Features

1. **Complete Factory Catalog**:
   - **Double-Wall Vacuum Insulated Flasks**: 24h Cold / 18h Hot temperature retention, copper thermal lock, leakproof caps.
   - **Single-Wall Stainless Steel Fridge Bottles**: Rapid fridge chilling, 100% food-grade SUS 304, ergonomic grip.
   - **Sports, Kids, Tumblers & Tabletop Carafes**: Full range of hydration models.
   - Dynamic capacity selector (350ml to 2000ml) & real-time metallic color swatch switcher.

2. **Interactive Live Laser Customizer**:
   - Live visual simulation of custom branding / fiber laser engraving on the bottle body.
   - Allows typing company names, custom text, or uploading logos (PNG/SVG).

3. **Retail vs. Wholesale / Bulk Tier Pricing**:
   - Instant toggle between single-piece retail pricing and volume discount wholesale tiers (20% to 48% OFF).

4. **1-Click Ordering & Quotation Sharing**:
   - **WhatsApp Order Generator**: Creates a formatted message with selected models, SKUs, colors, quantities, laser engraving details, and estimated total ready to send to your sales desk.
   - **Instant PDF Quotation / Proforma Invoice**: Generates official branded PDF quotation with itemized table, specs, and conditions directly in the browser.
   - **Shareable Link**: Encodes the configured quotation cart into a shareable URL to send to prospective clients.

5. **Side-by-Side Model Comparison**:
   - Compare up to 3 bottle models on steel grade, thermal hours, lid mechanism, capacities, and pricing.

6. **Admin Catalog Management**:
   - Built-in portal to edit model prices, update wholesale rates, export/import JSON catalogs, or add new bottles.
