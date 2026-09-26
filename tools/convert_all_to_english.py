import pathlib, re, sys

path = pathlib.Path(r'C:\Users\Video Editor\.gemini\antigravity\scratch\eskandria-landing-page.html')
html = path.read_text(encoding='utf-8')

# 1. Update CSS: replace .menu-card__ar rules with .menu-card__sub
old_css = """    /* Arabic name */
    .menu-card__ar {
      font-family: var(--font-arabic, serif);
      color: rgba(212,175,55,.75);
      font-size: .9rem;
      margin: 0 0 10px;
      direction: rtl; text-align: right;
    }

    .menu-card__desc {
      margin: 0 0 14px;
      font-size: .88rem;
      color: rgba(246,242,234,.6);
      line-height: 1.55;
      flex-grow: 1;
    }

    /* hide Arabic card subtitle */
    .menu-card__ar { display: none; }"""

new_css = """    /* English culinary subtitle */
    .menu-card__sub {
      font-family: var(--font-body);
      color: var(--gold);
      font-size: .82rem;
      font-weight: 600;
      letter-spacing: .02em;
      margin: 0 0 8px;
      line-height: 1.35;
    }

    .menu-card__desc {
      margin: 0 0 14px;
      font-size: .88rem;
      color: rgba(246,242,234,.6);
      line-height: 1.55;
      flex-grow: 1;
    }"""

if old_css in html:
    html = html.replace(old_css, new_css)
    print("Replaced card CSS")
else:
    print("Warning: old_css not found directly, checking regex")
    html = re.sub(r'/\* Arabic name \*/[\s\S]*?/\* hide Arabic card subtitle \*/\s*\.menu-card__ar\s*\{\s*display:\s*none;\s*\}', new_css, html)

# 2. Update Canvas font and text in EskandriaGallery
old_canvas = """            bctx.fillStyle = '#d4af37';
            bctx.font = '700 16px Cairo, sans-serif';
            bctx.fillText(item.ar, 20, cardH * 0.80);"""

new_canvas = """            bctx.fillStyle = '#d4af37';
            bctx.font = '600 13px Manrope, sans-serif';
            bctx.fillText(item.sub || '', 20, cardH * 0.80);"""

if old_canvas in html:
    html = html.replace(old_canvas, new_canvas)
    print("Replaced canvas font & text")
else:
    print("Canvas text string search:")
    idx = html.find("bctx.font = '700 16px Cairo, sans-serif'")
    print("Index:", idx)

# 3. Update SIGNATURE_RECIPES
old_recipes = """    const SIGNATURE_RECIPES = [
      {
        idx: '01',
        image: 'eskandria_assets/sayadia_seafood.webp',
        title: 'Sayadia Seafood Tajin',
        ar: 'صيادية إسكندراني بالسي فود',
        ingredients: ['Jumbo Prawns', 'Calamari · Fish Fillet', 'Dark Caramelized Onion Rice'],
        time: '20 min', serves: 2
      },
      {
        idx: '02',
        image: 'eskandria_assets/mahshi_calamari.webp',
        title: 'Mahshi Calamari',
        ar: 'كالاماري محشي بالأرز والبهارات',
        ingredients: ['Tender Squid', 'Egyptian Herb Rice', 'Coastal Spiced Broth'],
        time: '25 min', serves: 2
      },
      {
        idx: '03',
        image: 'eskandria_assets/page_9_img_4.png',
        title: 'Hawawshi Eskandrani',
        ar: 'حواوشي إسكندراني بالجبنة',
        ingredients: ['Fresh Kneaded Dough', 'Spiced Veal Mince', 'Melted Mozzarella · Fries'],
        time: '15 min', serves: 1
      },
      {
        idx: '04',
        image: 'eskandria_assets/page_15_img_3.png',
        title: 'Kopiec Kreta (Mole Hill)',
        ar: 'كعكة التل البولندية الأصلية',
        ingredients: ['Chocolate Sponge', 'Fresh Cream · Bananas', 'Dark Cocoa Crumbs'],
        time: 'Fresh daily', serves: 2
      }
    ];"""

new_recipes = """    const SIGNATURE_RECIPES = [
      {
        idx: '01',
        image: 'eskandria_assets/sayadia_seafood.webp',
        title: 'Sayadia Seafood Tajin',
        sub: 'Alexandrian Coastal Seafood Tajin',
        ingredients: ['Jumbo Prawns', 'Calamari · Fish Fillet', 'Dark Caramelized Onion Rice'],
        time: '20 min', serves: 2
      },
      {
        idx: '02',
        image: 'eskandria_assets/mahshi_calamari.webp',
        title: 'Mahshi Calamari',
        sub: 'Herb Rice Stuffed Squid Tubes',
        ingredients: ['Tender Squid', 'Egyptian Herb Rice', 'Coastal Spiced Broth'],
        time: '25 min', serves: 2
      },
      {
        idx: '03',
        image: 'eskandria_assets/page_9_img_4.png',
        title: 'Hawawshi Eskandrani',
        sub: 'Alexandrian Spiced Dough & Melted Cheese',
        ingredients: ['Fresh Kneaded Dough', 'Spiced Veal Mince', 'Melted Mozzarella · Fries'],
        time: '15 min', serves: 1
      },
      {
        idx: '04',
        image: 'eskandria_assets/page_15_img_3.png',
        title: 'Kopiec Kreta (Mole Hill)',
        sub: 'Traditional Polish Mole Hill Cake',
        ingredients: ['Chocolate Sponge', 'Fresh Cream · Bananas', 'Dark Cocoa Crumbs'],
        time: 'Fresh daily', serves: 2
      }
    ];"""

if old_recipes in html:
    html = html.replace(old_recipes, new_recipes)
    print("Replaced SIGNATURE_RECIPES")
else:
    print("Warning: old_recipes not found directly")

# 4. Map dish English subtitles in MENU_DATABASE
sub_map = {
    'Wolfsbarsch (300-400g)': 'Royal Mediterranean Sea Bass',
    'Dorade Royale (300-400g)': 'Royal Sea Bream Charcoal Roasted',
    'Sayadia Seafood Tajin': 'Coastal Seafood Sayadia Casserole',
    'Mahshi Calamari': 'Herb-Stuffed Calamari',
    'Kees Gambari (Seafood Bag)': 'Alexandrian Cajun-Spiced Shrimp Boil',
    'Estakoza Eskandrani (400g)': 'Mediterranean Butter-Glazed Lobster',
    'Roz Seafood (Paella)': 'Egyptian Coastal Seafood Paella',
    'Gandofli Eskandrani': 'Alexandrian Garlic & Lemon Clams',

    'Moza Kharouf (Lamb Shank)': 'Slow-Braised Tender Lamb Shank',
    'Kofta Eskandrani': 'Charcoal-Grilled Spiced Veal Skewers',
    'Shish Kebab': 'Flame-Seared Marinated Veal Cubes',
    'Shish Tawook': 'Garlic & Herb Marinated Chicken Skewers',
    'Mix Grill Platter': 'Chef’s 4-Meat Mixed Grill Platter',
    'Kotelett Mashwi (Lamb Chops)': 'Fire-Grilled Tender Lamb Chops',

    'Hawawshi Eskandrani': 'Spiced Meat & Melted Cheese Flatbread',
    'Kebda Eskandrani (Liver)': 'Authentic Alexandrian Seared Liver',
    'Molokhia Combo': 'Velvety Jute Mallow Soup with Chicken',
    'Shawarma Bowl': 'Marinated Shawarma over Spiced Rice',
    'Koshary Eskandria': 'Traditional Egyptian Rice & Lentil Bowl',
    'Schabowy (Polish Cutlet)': 'Crispy Breaded Cutlet with Potatoes',

    'Béchamel Pasta Tajin': 'Baked Beef & Creamy Béchamel Casserole',
    'Gambari Tajin (Prawns)': 'Baked Scampi Casserole with Fresh Herbs',
    'Makrona Kebda': 'Spiced Alexandrian Liver Penne Casserole',
    'Frutti di Mare Tajin': 'Gratinated Mixed Seafood Pasta Casserole',

    'Egyptian Breakfast Deluxe': 'Complete Alexandrian Breakfast Spread',
    'Manakesh Mix & Cheese': 'Stone-Baked Levantine Flatbreads',
    'Hummus be Elahma': 'Whipped Chickpeas with Sautéed Spiced Veal',
    'Batata Harra & Mezze': 'Spicy Garlic & Coriander Roasted Potatoes',
    'Waraq Enab & Mahshi Kromb': 'Stuffed Vine Leaves & Cabbage Rolls',

    'Kopiec Kreta (Mole Hill Cake)': 'Signature Polish Cocoa & Banana Cake',
    'Cheesecake Deluxe': 'Pistachio & Lotus Cream Cheesecake',
    'Um Ali Orient': 'Egyptian Bread Pudding with Cream & Nuts',
    'Kunafa & Baklawa': 'Crispy Cheese Phyllo & Pistachio Baklava',
    'Waffel / Crepe Deluxe': 'Belgian Waffle & French Crepe Special',

    'Alexandria Limonade': 'Fresh Mint & Lemonade Crusher',
    'Zabado Fruit Shake': 'Egyptian Whipped Fruit & Yogurt Smoothie',
    'Virgin Mojito & Mocktails': 'Crafted Refreshing Fruit Mocktails',
    'Egyptian & Turkish Coffee': 'Traditional Cardamom Brewed Coffee',
    'Family Shisha Corner': 'Premium Lounge Shisha & Aromatics'
}

for name, sub in sub_map.items():
    # Replace ar: '...' with sub: '...'
    pattern = re.compile(rf"(name:\s*'{re.escape(name)}',\s*)ar:\s*'[^']*'", re.UNICODE)
    html, n = pattern.subn(rf"\1sub: '{sub}'", html)
    if n == 0:
        print(f"Notice: pattern for {name} did not match directly")

# 5. Update renderMenuItems function to output menu-card__sub instead of menu-card__ar
html = html.replace(
    "+ '<div class=\"menu-card__ar\">' + (item.ar || '') + '</div>'",
    "+ '<div class=\"menu-card__sub\">' + (item.sub || '') + '</div>'"
)

path.write_text(html, encoding='utf-8')
print("Complete conversion finished.")
