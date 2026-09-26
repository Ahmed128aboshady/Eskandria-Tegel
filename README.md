# Eskandria Restaurant Berlin — Luxury Landing Page

Interactive luxury landing page for **Eskandria Restaurant** (Medebacher Weg 24, 13507 Berlin, Tegel). Built with GSAP 3 scroll-choreography, WebGL shaders, Lenis smooth scrolling, and an interactive full menu system.

---

## 🌟 Live Preview
- **Local:** Open `index.html` in any modern web browser.
- **GitHub Pages:** Go to repository **Settings** → **Pages** → Branch: `main` / `root` → **Save**.

---

## 📁 Repository Structure

```
Eskandria-Tegel/
├── index.html                   # Main production landing page (GitHub Pages root)
├── eskandria-landing-page.html   # Named backup copy of the landing page
├── eskandria_assets/            # All high-resolution images, cutouts & icons (145 files)
│   ├── hero_tajin_cutout.png    # 3D floating seafood tajin centerpiece (transparent PNG)
│   ├── harbor_alexandria.webp   # Historic harbor & Qaitbay citadel
│   ├── sayadia_seafood.webp     # Signature dish photo
│   ├── mahshi_calamari.webp     # Calamari dish photo
│   └── page_*_img_*.png         # Extracted dish photos from menu
├── tools/                       # Python automation and maintenance scripts
│   ├── generate_eskandria_html.py # Full generator script
│   ├── convert_all_to_english.py  # Localization utility
│   ├── inspect_kairo.py          # PDF text and asset extractor
│   └── menu_text_dump.txt        # Extracted February menu text dump
├── .gitignore
└── README.md
```

---

## 🎨 Design & Architecture

### 1. 3D Floating Tajin (Centerpiece Choreography)
- Animated along a responsive 9-point pose chain (`P` array inside `gsap.matchMedia`):
  - **01 Hero:** Center `(0vw, 3vh)`
  - **02 Story:** Left `(-24vw, 6vh)`
  - **03 Ingredients (Pillars):** Right `(27vw, 5vh)` — positioned to reveal all 4 ingredient cards
  - **04 Craft:** Right `(26vw, 6vh)`
  - **05 Spectrum:** Right `(19vw, 0vh)`
  - **06 Ritual:** Left `(-24vw, 6vh)`
  - **07 Signature Recipes:** Upper right `(38vw, -32vh)` above the hanging cloth canvas
  - **08 Voices:** Left small `(-15vw, 6vh)`
  - **09 Visit & Booking:** Center `(0vw, 3vh)`

### 2. Chapters Breakdown
1. **01 Hero:** Alexandria in Berlin, buffet badge (14.99€), scroll-down cue.
2. **02 Story:** Pharos Lighthouse & Citadel heritage, live stats counters.
3. **03 The Pillars:** Pinned 4-step ingredient scroll (Seafood, Aromatics, Tahina, Clay Tajins).
4. **04 The Craft:** Lava rock grill, 12-hour marinade, earthenware slow bake.
5. **05 The Spectrum:** Alexandrian flavor notes (Umami, Heat, Citrus).
6. **06 The Atmosphere:** Dining ritual, family board games, weekend buffet, shisha lounge.
7. **07 Signature Recipes:** Interactive hanging cloth physics canvas gallery.
8. **08 Guest Reviews:** Google Reviews (4.9★ rating), continuous marquee stream.
9. **09 Visit & Booking:** Direct table reservation form, Google Maps embed, social links.

### 3. Interactive Full Menu Modal
- **Pill Tab Filter:** All Dishes, Seafood & Fish, Lava Charcoal Grill, Street Food, Baked Tajins, Breakfast & Mezze, Sweets, Drinks & Shisha.
- **Card Design:**
  - 160px circular dish image with gold glow hover effect.
  - Dish name and price on single row in gold.
  - English descriptive subtitle.
  - Full ingredient description.
  - Dietary & allergen badges (GF, Halal, etc.).

---

## 🛠️ Editing from Another Machine

### How to make changes:
1. Clone the repository:
   ```bash
   git clone https://github.com/Ahmed128aboshady/Eskandria-Tegel.git
   cd Eskandria-Tegel
   ```
2. Open `index.html` in VS Code or any text editor.
3. **To update menu items or prices:**
   Search for `const MENU_DATABASE = [` in `index.html` (around line 3115).
   Each item follows this structure:
   ```javascript
   {
     cat: 'seafood',
     name: 'Sayadia Seafood Tajin',
     sub: 'Coastal Seafood Sayadia Casserole',
     price: '16.90€',
     desc: 'Traditional dark onion-infused Alexandrian rice with grilled seafood...',
     tags: 'K, F, G · Signature',
     img: 'eskandria_assets/sayadia_seafood.webp'
   }
   ```
4. **To adjust floating tajin positions:**
   Search for `const P = ctx.conditions.desk ? [` in `index.html` (around line 2884).
5. Save, commit and push:
   ```bash
   git add .
   git commit -m "Update menu prices and items"
   git push origin main
   ```

---

## 📍 Restaurant Details
- **Address:** Medebacher Weg 24, 13507 Berlin, Germany
- **Phone:** `+49 15567 318173`
- **Hours:**
  - Mon – Sun: 11:00 – 22:00
  - Friday: 14:00 – 22:00
  - Tuesday: Closed
- **Weekend Open Buffet:** Saturday & Sunday 12:00 – 16:00 (14.99€)
