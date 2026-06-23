#!/usr/bin/env python3
"""Bulk import ChatGPT-export recipes into Recipe Duck with Pexels images."""

import json, time, urllib.request, urllib.parse

SUPA_URL  = "https://qrnfkgsxygkaqmzzbdbi.supabase.co"
ANON_KEY  = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFybmZrZ3N4eWdrYXFtenpiZGJpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA2NjMzNjEsImV4cCI6MjA5NjIzOTM2MX0.u2zVCsAXkbAS_cgMzCUrkf92lGFaeZ5hmhUAi5rSX6k"
IMG_FN    = f"{SUPA_URL}/functions/v1/image-search"
REST_URL  = f"{SUPA_URL}/rest/v1/recipes"

HEADERS = {
    "apikey": ANON_KEY,
    "Authorization": f"Bearer {ANON_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation",
}

CI = "ChatGPT Import"  # collection added to every recipe

# ---------------------------------------------------------------------------
# Recipe data  (ingredients / directions are plain text, newline-separated)
# ---------------------------------------------------------------------------
RECIPES = [

# ── 1 ───────────────────────────────────────────────────────────────────────
{"name": "Air Fry Crispy Wings – Two-Flavor Split",
 "categories": ["Poultry"],
 "collections": [CI, "Air Fryer"],
 "yield": "~30 wings (6 lbs)",
 "prep_time": "15 min",
 "cook_time": "40 min",
 "source": "ChatGPT",
 "image_query": "crispy air fry chicken wings dry rub",
 "ingredients": """Base Crisp Mix (ALL wings):
1 Tbsp baking powder (aluminum-free)
1½ tsp kosher salt

Bowl 1 – Frank's RedHot Dry Seasoning Wings (~3 lb):
2½ Tbsp Frank's RedHot Dry Seasoning
Optional: ½ tsp cayenne

Bowl 2 – Meat Church Holy Gospel BBQ Rub Wings (~3 lb):
2½ Tbsp Meat Church Holy Gospel BBQ Rub

Oil:
PAM Olive Oil spray""",
 "directions": """1. Dry wings thoroughly with paper towels the night before and refrigerate uncovered on a rack (or pat very dry just before cooking).
2. Toss ALL wings with baking powder and kosher salt until evenly coated.
3. Divide wings into two bowls (~3 lb each).
4. Toss Bowl 1 with Frank's RedHot Dry Seasoning (+ cayenne if desired).
5. Toss Bowl 2 with Meat Church Holy Gospel BBQ Rub.
6. Arrange wings on two wire racks set over foil-lined sheet pans. Space wings so they don't touch.
7. Lightly mist each tray with PAM Olive Oil – one quick pass is enough.
8. Place racks in upper-middle and lower-middle positions of the Frigidaire Professional oven.
9. Air Fry at 425°F for 25 minutes.
10. Flip all wings and swap rack positions.
11. Cook another 15 minutes, or add 5 more for extra dark/crispy.
12. Target internal temp 175–185°F.
13. Rest 3–5 minutes before serving. Optional: sprinkle a little extra rub just before serving.
Serve with ranch, blue cheese, honey, or extra Frank's for dipping.""",
 "notes": "Both rubs already contain salt – reduced base salt to 1½ tsp to avoid over-seasoning. Baking powder creates blistered, crispy skin. No sauce needed – serve sauce on the side to preserve crunch."},

# ── 2 ───────────────────────────────────────────────────────────────────────
{"name": "Traeger Smoked Rosemary Lamb with Baby Potatoes & Mint Chimichurri",
 "categories": ["Lamb"],
 "collections": [CI, "Smoker"],
 "yield": "6",
 "prep_time": "25 min",
 "cook_time": "3–4 hours",
 "source": "ChatGPT",
 "image_query": "smoked leg of lamb sliced with rosemary potatoes",
 "ingredients": """For the Lamb:
1 bone-in or boneless leg of lamb (4–6 lb)
2 Tbsp olive oil
4 Tbsp Traeger Anything Rub
1½ Tbsp fresh rosemary, finely crushed
4 cloves garlic, minced
1 Tbsp Dijon mustard (optional)
½ tsp black pepper
1 Tbsp fresh lemon juice

For the Rosemary Smoked Potatoes:
2–3 lb baby potatoes (Yukon Gold, red, or fingerling)
4 Tbsp olive oil
2 Tbsp butter, melted
3 Tbsp fresh rosemary, finely chopped (or 1½ Tbsp dried)
4 cloves garlic, minced
1 tsp kosher salt
½ tsp black pepper
½ tsp smoked paprika
½ tsp onion powder
Zest of ½ lemon (optional)
1 Tbsp lemon juice or white wine vinegar (for finishing)

Mint Chimichurri Sauce:
1 cup fresh mint leaves, finely chopped
½ cup fresh parsley, finely chopped
4 cloves garlic, minced
½ tsp crushed red pepper flakes
1 tsp kosher salt
½ tsp black pepper
2 Tbsp red wine vinegar
½ cup extra virgin olive oil
Zest of ½ lemon
1 Tbsp fresh lemon juice""",
 "directions": """Prepare the Lamb:
1. Pat lamb dry with paper towels.
2. Rub with olive oil and Dijon mustard.
3. Combine Anything Rub, rosemary, garlic, and black pepper.
4. Coat lamb generously on all sides.
5. Let rest at room temperature 30–45 minutes.

Prepare the Potatoes:
1. Wash and dry potatoes. Cut in half if larger than a golf ball.
2. In a large bowl combine olive oil, melted butter, rosemary, garlic, salt, pepper, smoked paprika, onion powder, and lemon zest.
3. Toss potatoes until fully coated.
4. Spread in a foil pan or cast iron skillet in a single layer. Cover tightly with foil.

Make the Chimichurri:
1. Combine mint, parsley, garlic, red pepper flakes, salt, and black pepper in a bowl.
2. Stir in red wine vinegar, lemon zest, and lemon juice.
3. Slowly whisk in olive oil.
4. Let sit at room temperature at least 20 minutes before serving.

Smoke:
1. Preheat Traeger to 225–250°F.
2. Place lamb on grill and insert thermometer.
3. Place covered potatoes on grill next to lamb.

Cook:
- Smoke lamb until internal temperature reaches 130–135°F for medium-rare, or 140–145°F for medium (about 3–4 hours).
- After potatoes cook covered for 60–75 minutes, remove foil, stir, and return uncovered for 30–45 minutes to brown and absorb smoke.

Finish:
1. Remove lamb from grill at target temp. Tent loosely and rest 20 minutes.
2. Drizzle potatoes with lemon juice or vinegar and a little olive oil. Toss.

Serve:
Slice lamb against the grain. Spoon mint chimichurri over the lamb and serve with rosemary smoked potatoes.""",
 "notes": "Use Traeger Anything Rub 45–90 minutes before cooking, not overnight – overnight salt will cure the surface and create a hammy texture instead of smoky juiciness. Leave lamb in netting while cooking to hold shape; remove netting after resting."},

# ── 3 ───────────────────────────────────────────────────────────────────────
{"name": "Rosemary Smoked Baby Potatoes (Traeger)",
 "categories": ["Vegetable"],
 "collections": [CI, "Smoker"],
 "yield": "4–6",
 "prep_time": "10 min",
 "cook_time": "90–120 min",
 "source": "ChatGPT",
 "image_query": "smoked baby potatoes rosemary garlic skillet",
 "ingredients": """2–3 lb baby potatoes (Yukon Gold, red, or fingerling)
4 Tbsp olive oil
2 Tbsp butter, melted
3 Tbsp fresh rosemary, finely chopped (or 1½ Tbsp dried)
4 cloves garlic, minced
1 tsp kosher salt
½ tsp black pepper
½ tsp smoked paprika
½ tsp onion powder
Zest of ½ lemon (optional)
1 Tbsp lemon juice or white wine vinegar (for finishing)""",
 "directions": """1. Wash and dry potatoes. If larger than a golf ball, cut in half; otherwise leave whole.
2. In a large bowl, combine olive oil, melted butter, rosemary, garlic, salt, pepper, smoked paprika, onion powder, and lemon zest. Add potatoes and toss until fully coated.
3. Spread potatoes in a single layer in a cast iron skillet, foil pan, or heavy-duty foil tray. Cover tightly with foil.
4. Place on Traeger at 225–250°F alongside protein (or alone). Cook covered for 60–75 minutes until potatoes are tender.
5. Remove foil, stir potatoes, and return uncovered to the smoker. Cook another 30–45 minutes until lightly browned and smoky.
6. Remove from grill. Drizzle with lemon juice or vinegar and a little extra olive oil. Toss and serve.""",
 "notes": "Designed for low-temperature smoking at 225–250°F. Keeping potatoes covered at first prevents drying and allows them to absorb smoke before browning. Great alongside smoked lamb, chicken, or pork."},

# ── 4 ───────────────────────────────────────────────────────────────────────
{"name": "Traeger Hickory Smoked SRF Gold Tomahawk + Smoked King Crab with Lemon Garlic Compound Butter",
 "categories": ["Beef", "Seafood"],
 "collections": [CI, "Smoker", "Surf & Turf"],
 "yield": "2",
 "prep_time": "25 min",
 "cook_time": "~1 hr 40 min",
 "source": "ChatGPT",
 "image_query": "tomahawk ribeye smoked with king crab legs",
 "ingredients": """1 Snake River Farms Gold Tomahawk (3.6 lb, 2.5" thick)
2–3 lbs king crab legs (fully cooked/frozen)
Hickory pellets
Traeger Anything Rub
Avocado oil (high smoke point)

Lemon Garlic Compound Butter:
1 stick (½ cup) unsalted butter, softened
3 cloves garlic, very finely minced
Zest of 1 lemon
1 Tbsp fresh lemon juice
1 Tbsp chopped parsley
1 tsp fresh thyme (optional)
Pinch kosher salt""",
 "directions": """Pre-Cook (–45 to 0 min):
- Remove steak from fridge 30–45 minutes before cook time.
- Pat completely dry. Season generously with Anything Rub. Leave uncovered while grill preheats.
- Make compound butter: combine all butter ingredients, mix thoroughly, roll in plastic wrap, refrigerate.

Grill Setup (0:00):
- Fill hopper with hickory pellets. Preheat Traeger to 225°F for 15 minutes.

Phase 1 – Smoke Steak (0:00–1:05 approx):
- 0:00 – Place steak on grill. Insert probe in thickest part away from bone.
- 0:55 – Begin monitoring temperature closely.
- 1:00–1:10 – Pull steak at 108–110°F internal (Wagyu carries over more than standard prime).
- Transition to Phase 2 at approximately 1:05.

Phase 2 – Rest Steak + Raise Grill Temp (1:05–1:15):
- Remove steak. Rest uncovered 10–15 minutes.
- Increase Traeger temperature to 375°F.

Phase 3 – Smoke Crab (1:15–1:35):
- Lightly brush crab legs with melted butter. Place directly on grill at 375°F.
- Cook 15–20 minutes until heated through (internal ~140°F).

Phase 4 – Cast Iron Reverse Sear (1:20–1:30):
- Heat flat side of cast iron griddle to 500–515°F (verify with laser thermometer).
- Add thin film of avocado oil.
- Sear steak: 60–75 sec first side, flip, 60–75 sec second side.
- Flip every 30 sec until internal hits 122–124°F. Total sear ~3–4 minutes.
- Pull steak and rest 10 minutes.

Phase 5 – Finish & Serve (1:30–1:40):
- Slice steak off bone and against the grain.
- Top hot steak slices and crab with 1–2 pats of compound butter.
- Serve with lemon wedges.""",
 "notes": "SRF Gold Wagyu carries over more aggressively than standard prime – pull earlier at 108–110°F. Target griddle: 500–515°F. Do NOT exceed 515°F to prevent Anything Rub scorching. Final steak temp after rest: 128–131°F (true medium rare). Always use flat side of griddle, not ribbed, for maximum crust on Wagyu."},

# ── 5 ───────────────────────────────────────────────────────────────────────
{"name": "Gas Grill Tri-Tip with Traeger Anything Rub",
 "categories": ["Beef"],
 "collections": [CI, "Grill"],
 "yield": "4–6",
 "prep_time": "10 min + 30 min rest",
 "cook_time": "~40 min",
 "source": "ChatGPT",
 "image_query": "tri tip steak sliced medium rare gas grill",
 "ingredients": """2.5 lb tri-tip roast
1–2 Tbsp olive oil
2–3 Tbsp Traeger Anything Rub
Optional: extra coarse black pepper""",
 "directions": """Prep:
1. Remove tri-tip from fridge 30–45 minutes before cooking.
2. Pat dry with paper towels.
3. Lightly coat with olive oil.
4. Apply Anything Rub generously on all sides. Add extra coarse black pepper if desired.
5. Season uncovered in fridge 20–40 minutes for best crust (important in warm climates).

Grill Setup:
1. Preheat gas grill to 450°F.
2. Create two heat zones: one side high heat, one side low or off.

Phase 1 – Indirect Cook:
1. Place tri-tip on the cool side of the grill. Close lid.
2. Cook until internal temp reaches 120°F. Estimated 25–35 minutes.
3. Flip once halfway through.

Phase 2 – Sear:
1. Move tri-tip to the high-heat side.
2. Sear 2–3 minutes per side, rotating to build crust.
3. Pull when internal temp reaches 130–135°F for medium-rare.

Phase 3 – Rest:
1. Remove from grill. Tent loosely with foil.
2. Rest 10–15 minutes. Temp will rise ~5°F.

Critical Step – Slicing:
1. Find where the grain changes direction (tri-tip has two grain directions).
2. Cut the roast in half at that point.
3. Slice each half thin and against the grain for maximum tenderness.""",
 "notes": "Do not leave raw beef out more than 1 hour in warm weather – season and refrigerate uncovered instead. Slicing against the grain (in two sections) is the most important step for tenderness."},

# ── 6 ───────────────────────────────────────────────────────────────────────
{"name": "Ronco Rotisserie Whole Chicken",
 "categories": ["Poultry"],
 "collections": [CI, "Oven"],
 "yield": "4",
 "prep_time": "15 min",
 "cook_time": "90–110 min",
 "source": "ChatGPT",
 "image_query": "rotisserie whole chicken golden crispy skin",
 "ingredients": """1 whole chicken (4–5 lbs)
1 Tbsp olive oil
1 Tbsp kosher salt
1 tsp black pepper
1 tsp garlic powder
1 tsp paprika
½–1 tsp baking powder (aluminum-free)
Optional: fresh thyme or rosemary
Kitchen twine (for trussing)""",
 "directions": """1. Remove giblets. Pat chicken completely dry with paper towels, inside and out.
2. Mix dry rub: salt, pepper, garlic powder, paprika, and baking powder.
3. Rub entire bird with olive oil, then apply dry rub all over including cavity.
4. Truss legs: slide twine under tail, pull ends up and cross over legs, wrap around drumstick ends, tie a firm knot. Tuck wing tips behind back.
5. Leave uncovered in fridge 45–60 minutes for best crispy skin.
6. Mount chicken securely and centered on Ronco spit.
7. Place drip tray underneath.
8. Set Ronco to cook. For a 4–5 lb bird: cook 90–110 minutes.
9. Start checking internal temp at 75 minutes. Target 165°F in thickest part of breast, 175°F in thigh.
10. Remove and rest 10–15 minutes. Skin will crisp more during rest.
11. Carve and serve.""",
 "notes": "Timing example for 6:30 PM dinner: start cooking at 4:45 PM, check at 6:15 PM, pull and rest at 6:20–6:30, carve at 6:35. Baking powder promotes blistered crispy skin – do not substitute baking soda."},

# ── 7 ───────────────────────────────────────────────────────────────────────
{"name": "Indoor Wagyu Ribeye with Basil Finishing Sauce",
 "categories": ["Beef"],
 "collections": [CI, "Stovetop", "Oven"],
 "yield": "1–2",
 "prep_time": "20 min",
 "cook_time": "~15 min",
 "source": "ChatGPT",
 "image_query": "wagyu ribeye pan seared cast iron basil sauce",
 "ingredients": """1 Snake River Farms Wagyu ribeye (1" thick, ~1.2 lb)
Kosher salt
Black pepper (optional, light)
1 tsp avocado oil
2 Tbsp butter
2 garlic cloves, smashed
1 sprig rosemary (optional)
Flaky salt (for finishing)

Basil Finishing Sauce:
½ cup fresh basil, finely chopped (packed)
2 Tbsp olive oil
1 tsp soy sauce
1 tsp lemon juice
1 small garlic clove, finely minced or grated
Pinch of salt
Optional: ¼ tsp honey""",
 "directions": """1. Salt steak generously on both sides. Let sit 30–45 minutes at room temperature.
2. Make basil finishing sauce: combine all sauce ingredients, stir, set aside to let flavors meld.
3. Right before cooking: add pepper (optional).
4. Preheat oven to 400°F.
5. Heat cast iron pan over medium-high to high heat (475–500°F surface via laser thermometer).
6. Add avocado oil. Sear steak 2–3 minutes first side (do not move). Flip and sear 2 minutes second side.
7. Reduce heat to medium. Add butter, smashed garlic, and rosemary. Tilt pan and spoon butter over steak for 1–2 minutes.
8. Transfer pan to oven. Cook until internal temp reaches 122–124°F for medium-rare (approx 4–6 minutes).
9. Remove steak from pan. Rest 10 minutes.
10. Slice against the grain. Sprinkle flaky salt.
11. Spoon basil finishing sauce lightly over the top. Garnish with torn fresh basil leaves.

Total time including thaw: ~1 hr 30 min""",
 "notes": "Wagyu cooks faster than normal steak due to high fat content. Do not add basil to the pan – it will burn and turn bitter. Salt = early, pepper = right before searing. Use sauce lightly – let the steak be the star."},

# ── 8 ───────────────────────────────────────────────────────────────────────
{"name": "Garlic Pork Belly Rice Cakes with Pole Beans & Green Onion",
 "categories": ["Pork"],
 "collections": [CI, "Stovetop", "Asian"],
 "yield": "3–4",
 "prep_time": "15 min",
 "cook_time": "25 min",
 "source": "ChatGPT",
 "image_query": "pork belly rice cakes stir fry green onion",
 "ingredients": """1 lb pork belly, skin-on, cut into thin slices or bite-sized pieces
2 cups Korean rice cakes (tteok), soaked in warm water 15 min if firm
1 cup pole beans or green beans, cut into 2-inch pieces
4 green onions, cut into 2-inch pieces
5 cloves garlic, minced
1 Tbsp soy sauce
1 Tbsp oyster sauce
1 Tbsp sesame oil
1 tsp sugar or honey
½ tsp black pepper
1 Tbsp neutral oil
Optional: 1 tsp gochujang or chili sauce""",
 "directions": """1. Soak rice cakes in warm water for 15 minutes if firm; drain and set aside.
2. Heat a large skillet or wok over high heat. Add neutral oil.
3. Add pork belly and cook until golden and fat is rendered, about 6–8 minutes. Remove excess fat if needed, leaving 1–2 Tbsp in pan.
4. Add garlic and stir-fry 30 seconds until fragrant.
5. Add rice cakes. Press gently and cook undisturbed 1–2 minutes to get some char, then toss.
6. Add pole beans. Stir-fry 3–4 minutes until beans are tender-crisp.
7. Mix together soy sauce, oyster sauce, sesame oil, sugar, pepper, and gochujang if using. Pour over the pan.
8. Toss everything together and cook 1–2 minutes until sauce coats everything and is slightly sticky.
9. Add green onion, toss once, and remove from heat immediately.
10. Serve hot.""",
 "notes": "Soak rice cakes before cooking or they will stay hard. High heat is important for good char on the rice cakes. Do not overcook the green onions – add at the very end so they stay fresh."},

# ── 9 ───────────────────────────────────────────────────────────────────────
{"name": "Crispy Soy-Garlic Pork Belly Bits",
 "categories": ["Pork"],
 "collections": [CI, "Stovetop", "Asian"],
 "yield": "2–3",
 "prep_time": "5 min",
 "cook_time": "18–20 min",
 "source": "ChatGPT",
 "image_query": "crispy pork belly bites soy garlic glaze Asian",
 "ingredients": """Pork belly strips (about 1" wide, ½" thick)
2 tsp soy sauce
1 tsp oyster sauce
1 tsp rice vinegar
1–2 tsp brown sugar or honey
½ tsp sesame oil
2 cloves garlic, minced
Optional: ½ tsp grated ginger
Optional: ½ tsp chili crisp or chili oil
Green onions for garnish
Sesame seeds (optional)""",
 "directions": """Prep:
1. Slice pork belly into ½-inch cubes. Pat dry with paper towel (dry surface = better browning).
2. Mix glaze: combine soy sauce, oyster sauce, rice vinegar, brown sugar, sesame oil, and ginger if using. Stir until sugar dissolves. Set aside.

Step 1 – Render & Crisp (8–10 min):
1. Place pork belly pieces in a COLD skillet (no oil). Spread evenly.
2. Turn heat to medium. Do not touch for the first 4–5 minutes.
3. Fat will render and pool in the pan. Flip and stir occasionally after 5 minutes.
4. Cook until golden brown, crispy edges, most fat rendered out (~8–10 min total).
5. If more than 2–3 Tbsp fat in pan, spoon some out (leave some for flavor).

Step 2 – Add Aromatics (1 min):
1. Lower heat to medium-low. Add garlic (and ginger if not in glaze).
2. Stir constantly 30–45 seconds. Do not let garlic brown dark.

Step 3 – Glaze & Reduce (2–3 min):
1. Pour in glaze. It will bubble immediately.
2. Simmer 1–2 minutes until sauce thickens and coats pork belly.

Finish:
Turn off heat. Sprinkle with green onions and sesame seeds. Serve immediately over noodles or alongside dumplings.""",
 "notes": "Start in a cold pan with no oil – the pork belly renders its own fat. Serve over noodles tossed with 2 Tbsp soy sauce, 1 tsp sesame oil, 1 tsp black vinegar, and a splash of pasta water for a complete meal."},

# ── 10 ──────────────────────────────────────────────────────────────────────
{"name": "Stovetop Sesame Chicken Thighs",
 "categories": ["Chicken"],
 "collections": [CI, "Stovetop", "Asian"],
 "yield": "3–4",
 "prep_time": "10 min",
 "cook_time": "15 min",
 "source": "ChatGPT",
 "image_query": "sesame chicken thighs skillet glossy sauce sesame seeds",
 "ingredients": """1–1.5 lbs boneless skinless chicken thighs, cut into bite-sized pieces
Salt + pepper
1–2 Tbsp neutral oil

Sauce:
3 Tbsp soy sauce
1 Tbsp sesame oil
2–3 Tbsp chili sauce (adjust to taste)
1 Tbsp honey or sugar (optional but recommended)
3 cloves garlic, minced
1 Tbsp fresh ginger, minced or grated
2–3 Tbsp water

Finish:
Sesame seeds
Sliced green onions""",
 "directions": """1. Heat pan over medium-high heat. Add oil.
2. Season chicken pieces with salt and pepper.
3. Cook chicken 5–7 minutes, stirring occasionally, until browned and cooked through. Let it get some color – don't stir constantly.

4. Push chicken to one side. Add garlic and ginger to the empty side.
5. Cook ~30 seconds until fragrant.

6. Add soy sauce, sesame oil, chili sauce, honey/sugar, and water.
7. Stir everything together and let sauce reduce 2–3 minutes until it thickens and coats the chicken.

8. Remove from heat. Top with sesame seeds and sliced green onions.
9. Serve over rice or noodles.""",
 "notes": "~25 minutes total. Adjust chili sauce amount to control heat level. Honey or sugar balances the salt and adds a nice glaze. Pairs well with steamed jasmine rice or noodles."},

# ── 11 ──────────────────────────────────────────────────────────────────────
{"name": "Crispy Pesto Chicken with Roasted Cherry Tomatoes",
 "categories": ["Chicken"],
 "collections": [CI, "Stovetop", "Oven"],
 "yield": "2",
 "prep_time": "15 min",
 "cook_time": "20 min",
 "source": "ChatGPT",
 "image_query": "crispy chicken breast breadcrumb pesto cherry tomatoes",
 "ingredients": """For the Chicken:
2 boneless skinless chicken breasts
½ cup Progresso Italian-style bread crumbs
2 Tbsp grated Parmesan (optional)
1 egg, lightly beaten
1 Tbsp olive oil
Salt & pepper to taste

For the Pan:
1 cup cherry tomatoes, halved
2 cloves garlic, minced
1 Tbsp olive oil
Pinch of red pepper flakes (optional)

For Finishing:
2 Tbsp pesto (store-bought or homemade)
1 Tbsp lemon juice
Fresh basil or extra Parmesan for garnish""",
 "directions": """1. Preheat oven to 400°F.
2. Pat chicken breasts dry and season with salt and pepper.
3. Set up two bowls: one with beaten egg, one with bread crumbs mixed with Parmesan.
4. Dip each chicken breast in egg, then coat thoroughly with bread crumb mixture, pressing to stick.
5. Heat oven-safe skillet over medium-high heat with a drizzle of olive oil.
6. Add breaded chicken and sear 3–4 minutes per side until golden brown. (Don't worry if not fully cooked – finishes in oven.)
7. Push chicken slightly to one side. Add cherry tomatoes, garlic, and a bit more olive oil to the other half. Toss gently, season with salt and red pepper flakes.
8. Transfer whole skillet to oven. Roast 8–10 minutes until chicken reaches 165°F and tomatoes begin to blister.
9. Remove from oven. Spoon pesto over each chicken breast while still hot.
10. Squeeze fresh lemon juice over top.
11. Slice and serve with pesto pasta or on its own. Garnish with fresh basil and extra Parmesan.""",
 "notes": "Optional: finish under broiler 1–2 minutes for extra crunch. Add baby spinach or arugula into hot pasta right before mixing for color and bite."},

# ── 12 ──────────────────────────────────────────────────────────────────────
{"name": "Classic Chicken Salad for Sandwiches",
 "categories": ["Chicken", "Sandwich"],
 "collections": [CI],
 "yield": "2 sandwiches",
 "prep_time": "10 min",
 "cook_time": "0 min",
 "source": "ChatGPT",
 "image_query": "chicken salad sandwich croissant creamy",
 "ingredients": """1 cooked chicken breast, shredded or diced
2–3 Tbsp mayonnaise
1–2 tsp Dijon mustard (optional)
1 Tbsp finely chopped celery or onion (or both)
1 Tbsp finely chopped dill pickles or sweet relish
1–2 tsp lemon juice or a splash of pickle juice
Salt & pepper to taste
Optional: 1 tsp fresh dill or chives, 1 Tbsp dried cranberries, 1 Tbsp sliced almonds, ½ tsp garlic powder, ½ tsp smoked paprika""",
 "directions": """1. Shred or dice the cooked chicken breast into small sandwich-friendly pieces.
2. In a bowl, combine mayo, Dijon, lemon juice (or pickle juice), salt, pepper, and any optional spices.
3. Stir in celery, onion, pickles/relish, and any herbs or nuts you're using.
4. Add chicken and gently fold until evenly coated. Taste and adjust seasoning.
5. Chill 15–20 minutes in the fridge for best flavor and texture.
6. Serve on toasted sourdough, brioche, croissants, in a wrap, or in lettuce cups.""",
 "notes": "Chilling 15–20 minutes lets the flavors meld and gives the perfect texture. Pairs well with sliced tomato, crisp lettuce, or bacon."},

# ── 13 ──────────────────────────────────────────────────────────────────────
{"name": "Garlic Butter Panko-Crusted Cod",
 "categories": ["Seafood"],
 "collections": [CI, "Stovetop"],
 "yield": "2",
 "prep_time": "10 min",
 "cook_time": "10 min",
 "source": "ChatGPT",
 "image_query": "panko crusted cod fish golden garlic butter",
 "ingredients": """Cod fillets (fresh or thawed)
1 cup panko breadcrumbs
1 egg, lightly beaten
Salt & pepper to taste
1–2 cloves garlic, minced
1 Tbsp butter
1 Tbsp olive oil or vegetable oil
Juice of ½ lemon
Optional garnish: chopped chive or cilantro

Optional sides: sautéed spinach, boiled yellow potatoes, lemon wedge""",
 "directions": """1. Pat cod dry with paper towels. Season both sides with salt and pepper.
2. Set up two shallow bowls: one with beaten egg, one with panko and a pinch of salt and pepper.
3. Dip each fillet in the egg, then press into the panko until fully coated.
4. Heat olive oil and butter in a pan over medium heat. Add garlic and cook 30 seconds to infuse the oil (don't let it brown too much).
5. Add the breaded cod fillets. Cook 3–4 minutes on the first side without moving until golden and crispy.
6. Carefully flip and cook another 2–3 minutes until cooked through and panko is golden.
7. Squeeze fresh lemon juice over the fish during the last 30 seconds of cooking.
8. Serve garnished with chopped chive or cilantro. Serve with sautéed spinach or boiled potatoes if desired.""",
 "notes": "Make sure pan is hot before adding fish to get proper crust. Cod is done when it flakes easily with a fork."},

# ── 14 ──────────────────────────────────────────────────────────────────────
{"name": "Cold-Cured Hot-Smoked Sockeye Salmon (Traeger)",
 "categories": ["Seafood"],
 "collections": [CI, "Smoker"],
 "yield": "4",
 "prep_time": "48 hours (cure + pellicle)",
 "cook_time": "25–45 min",
 "source": "ChatGPT",
 "image_query": "hot smoked salmon fillet Traeger golden",
 "ingredients": """1.94 lb (880g) wild sockeye salmon, 2 fillets

Cure (for 1.94 lb salmon – no scale version):
½ cup Diamond Crystal kosher salt (or ⅓ cup Morton)
⅓ cup brown sugar
Scant ½ tsp Prague Powder #1 (sodium nitrite cure – do not exceed)
Optional: 1 tsp cracked black pepper, 1 Tbsp fresh dill, ½ tsp lemon zest

Wood: Apple or Cherry pellets (avoid mesquite)""",
 "directions": """PHASE 1 – Cure (24 Hours):
1. Mix salt, sugar, and curing salt extremely thoroughly (60+ seconds). Distribution is critical.
2. Pat salmon completely dry. Line a rimmed baking sheet with plastic wrap.
3. Spread a thin layer of cure on the plastic. Lay fillets skin-side down.
4. Cover tops and sides with remaining cure. Use ALL of it. Press lightly to adhere.
5. Wrap tightly in plastic. No air gaps. Refrigerate in coldest part (not door).
6. At 12 hours: flip the package. Liquid will be present – this is normal.
7. At 24 hours: remove. Do not exceed 30 hours (sockeye is lean and will over-cure).

PHASE 2 – Rinse & Pellicle (8–24 Hours):
1. Rinse quickly under cold water. Do NOT soak.
2. Pat completely dry with paper towels.
3. Place on wire rack over baking sheet. Refrigerate uncovered.
4. After 6–8 hours the surface should feel tacky and slightly shiny – this is the pellicle.
5. Do not skip this step – it's critical for smoke adhesion.

PHASE 3 – Hot Smoke on Traeger at 165°F (Regular Mode, NOT Super Smoke):
1. Preheat Traeger to 165°F (regular mode).
2. Place salmon skin-side down on rack.
3. For ¾" thick fillets: start checking internal temp at 20 minutes.
4. Pull at 132–134°F internal – it will carry over to 136–138°F while resting.
5. Do NOT let it hit 145°F (will dry out). Total cook: 25–45 minutes.

PHASE 4 – Rest & Cool:
1. Leave on rack at room temp 15–20 minutes (carryover finishes gently).
2. Refrigerate uncovered 1–2 hours to cool fully before sealing.

PHASE 5 – Vacuum Seal & Freeze:
1. Leave fillets whole (slicing first causes faster dryout after thawing).
2. Vacuum seal tightly. Freeze immediately.
3. Best quality: 2–3 months frozen. Thaw ONLY in refrigerator overnight.""",
 "notes": "Using Prague Powder #1 is important if vacuum sealing and freezing – it provides nitrite protection against botulism in anaerobic storage. Do NOT add extra curing salt if using a pre-mixed cure that already contains nitrite. Measure curing salt precisely – do not heap the teaspoon."},

# ── 15 ──────────────────────────────────────────────────────────────────────
{"name": "Chinese Restaurant-Style Fried Rice (Same-Day Nishiki Method)",
 "categories": ["Rice"],
 "collections": [CI, "Stovetop", "Asian"],
 "yield": "3",
 "prep_time": "15 min + 2–4 hrs rice drying",
 "cook_time": "15 min",
 "source": "ChatGPT",
 "image_query": "Chinese fried rice wok eggs green onion takeout style",
 "ingredients": """2½–3 cups Nishiki medium-grain rice (cooked earlier, chilled)
2 eggs
2 Tbsp neutral oil (canola, avocado, peanut)
1 Tbsp butter (optional but restaurant-level good)
2 cloves garlic, minced
½ cup frozen peas & carrots (optional but classic)
2–3 green onions, sliced
2 Tbsp light soy sauce
1 tsp sesame oil
½ tsp sugar
White pepper to taste (better than black pepper here)
Salt if needed
Optional protein: shrimp, diced chicken, ham, or char siu

Same-Day Rice Prep:
1 cup Nishiki rice
1⅛ cups water (use slightly less than bag says)""",
 "directions": """Same-Day Rice Prep (do this 2–4 hours before cooking):
1. Rinse rice 2–3 times until water is mostly clear. Cook with 1⅛ cups water in rice cooker or pot.
2. When done, immediately spread rice in a thin layer on a sheet pan or large plate.
3. Let steam escape 10 minutes on counter.
4. Refrigerate UNCOVERED for 2–4 hours (or freeze 20 minutes if short on time).
5. Before frying: break up clumps gently with your hands.

Fried Rice:
1. Pre-mix soy sauce + sesame oil + sugar in a small bowl.
2. Beat eggs with a pinch of salt.
3. Heat wok or large skillet until screaming hot.
4. Add oil, swirl, then pour in eggs. Scramble quickly – soft-set only. Remove to a plate.
5. Add a little more oil. Add garlic for 5–10 seconds only.
6. Add rice – spread it out, let it fry undisturbed 30–45 seconds. Toss and repeat once for light browning.
7. Add peas/carrots and cooked protein if using.
8. Return eggs to pan.
9. Drizzle soy sauce mix around the EDGES of the pan (not directly on rice) – this caramelizes it.
10. Toss fast over high heat.
11. Add butter, green onions, white pepper. Kill heat, final toss, taste and adjust.""",
 "notes": "Key secrets: soy sauce around pan edge (not on rice) = caramelized flavor; butter + sesame oil combo; white pepper not black; slight sugar balances salt. Don't overcrowd – medium-grain rice holds more moisture so let it sit between tosses to drive off steam. Don't cover rice while in fridge or you'll undo the drying."},

# ── 16 ──────────────────────────────────────────────────────────────────────
{"name": "Kimchi Ribeye Fried Rice",
 "categories": ["Rice", "Beef"],
 "collections": [CI, "Stovetop", "Asian", "Korean"],
 "yield": "2",
 "prep_time": "10 min",
 "cook_time": "15 min",
 "source": "ChatGPT",
 "image_query": "kimchi fried rice ribeye beef Korean skillet",
 "ingredients": """2 cups cooked day-old rice (jasmine or short-grain)
6–8 oz ribeye steak (thin-sliced or leftover)
1 cup kimchi, chopped (with juices)
2 green onions, sliced
2 cloves garlic, minced
1 tsp sesame oil
1 Tbsp soy sauce
1 Tbsp gochujang (Korean chili paste)
1 tsp sugar
2 eggs
1 Tbsp neutral oil
Optional: sesame seeds, fried egg on top, nori strips""",
 "directions": """1. If using raw ribeye: slice very thin against the grain. Season lightly with salt and pepper.
2. Heat wok or large skillet over high heat with a drizzle of neutral oil.
3. Sear ribeye quickly – 1–2 minutes – until just cooked or lightly charred. Remove and set aside.
4. In the same pan, add a bit more oil. Add garlic, cook 10 seconds.
5. Add chopped kimchi (with some of its juices) and stir-fry 2–3 minutes until slightly caramelized.
6. Add gochujang. Stir and cook 30 seconds until fragrant.
7. Add cold rice. Break up any clumps. Press into pan and let fry undisturbed 1 minute, then toss.
8. Stir in soy sauce and sugar. Toss to combine.
9. Add ribeye back in. Toss to warm through.
10. Add sesame oil. Kill heat. Fold in green onions.
11. Serve topped with a fried egg and sesame seeds.""",
 "notes": "Day-old or cold rice is essential for proper fried rice texture – fresh rice steams instead of frying. Gochujang adds the authentic Korean chili flavor; adjust amount for heat preference."},

# ── 17 ──────────────────────────────────────────────────────────────────────
{"name": "Chipotle-Style Cilantro Lime Rice with Garlic (Jasmine)",
 "categories": ["Rice"],
 "collections": [CI, "Stovetop", "Copycat Recipes"],
 "yield": "6",
 "prep_time": "5 min",
 "cook_time": "25 min",
 "source": "ChatGPT",
 "image_query": "cilantro lime rice jasmine fluffy chipotle style",
 "ingredients": """2 cups jasmine rice
3 cups water
2 Tbsp oil or butter
1 tsp salt
2 bay leaves (optional)
2–3 cloves garlic, minced
Juice of 1–2 limes
Optional: small squeeze of lemon
4–6 Tbsp chopped fresh cilantro""",
 "directions": """1. Rinse rice under cold water until mostly clear.
2. In the pot, warm the oil or butter over medium heat.
3. Add minced garlic and cook 30–60 seconds, just until fragrant. Don't brown.
4. Add rice and stir 30 seconds to coat.
5. Add water, salt, and optional bay leaves.
6. Bring to a boil, cover, reduce heat to low, and cook 12–15 minutes.
7. Turn off heat and let sit covered for 10 minutes.
8. Remove bay leaves and fluff with a fork.
9. Stir in lime juice, optional lemon squeeze, and cilantro while rice is still warm.
10. Taste and adjust salt and lime.""",
 "notes": "Adding a tiny squeeze of lemon alongside lime makes it more authentically Chipotle-style. Toasting the garlic in oil before adding rice adds depth. Serves 6 as a side. For smaller batches, halve all ingredients and reduce water to 1.5 cups, cook time stays the same."},

# ── 18 ──────────────────────────────────────────────────────────────────────
{"name": "Chive Italian Sausage Pesto Garlic Fettuccine",
 "categories": ["Pasta", "Sausage"],
 "collections": [CI, "Stovetop"],
 "yield": "4",
 "prep_time": "10 min",
 "cook_time": "20 min",
 "source": "ChatGPT",
 "image_query": "Italian sausage pesto fettuccine pasta skillet",
 "ingredients": """12 oz fettuccine (fresh or dried)
1 lb Italian sausage (mild or spicy, casings removed)
4 cloves garlic, minced
½ cup fresh chives, finely chopped (reserve some for garnish)
½ cup pesto (basil-based, homemade or store-bought)
½ cup grated Parmesan cheese (plus more for serving)
¼ cup olive oil (or reserved pasta water if you prefer lighter)
½ cup heavy cream (optional, for a creamier sauce)
Salt & black pepper to taste
Red pepper flakes (optional, for heat)""",
 "directions": """1. Bring a large pot of salted water to a boil. Cook fettuccine until al dente. Reserve 1 cup pasta water, then drain.
2. In a large skillet over medium-high heat, cook Italian sausage, breaking into crumbles, until browned and fully cooked (6–8 minutes). Remove excess grease if needed.
3. Lower heat to medium. Add olive oil (or a drizzle of sausage drippings) to the skillet.
4. Stir in minced garlic and half the chopped chives. Cook just until fragrant, about 1 minute.
5. Stir in the pesto and heavy cream (if using). Toss well to combine with sausage.
6. Add Parmesan and stir until melted into the sauce.
7. Add drained fettuccine to the skillet. Toss, adding reserved pasta water a splash at a time until sauce clings to noodles.
8. Season with black pepper and red pepper flakes to taste.
9. Top with remaining chives and extra Parmesan. Serve with garlic bread or a simple arugula salad.""",
 "notes": "For a bright finish, squeeze a bit of lemon juice in before serving. Leftovers reheat well with a splash of cream or pasta water. Spicy Italian sausage works great for extra heat."},

# ── 19 ──────────────────────────────────────────────────────────────────────
{"name": "Baked Gnocchi with Ground Turkey, Tomato & Spinach",
 "categories": ["Pasta"],
 "collections": [CI, "Oven"],
 "yield": "4",
 "prep_time": "15 min",
 "cook_time": "25 min",
 "source": "ChatGPT",
 "image_query": "baked gnocchi ground turkey tomato spinach skillet",
 "ingredients": """1 lb gnocchi
1 shallot, finely chopped
2–3 garlic cloves, minced
1 large tomato, diced (or 1 cup cherry tomatoes, halved)
1–2 carrots, grated or finely diced
½ lb ground turkey (or beef)
2 cups baby spinach
Olive oil
Salt and pepper
Optional: shredded mozzarella or Parmesan cheese
Optional garnish: chopped parsley or cilantro""",
 "directions": """1. Preheat oven to 400°F.
2. Bring a pot of salted water to a boil. Cook gnocchi according to package directions. Drain and set aside.
3. Heat a splash of olive oil in an oven-safe skillet over medium heat.
4. Sauté shallot, garlic, and carrots for 2–3 minutes until softened.
5. Add ground turkey (or beef), season with salt and pepper, and cook until browned, breaking up into pieces.
6. Stir in diced tomato and cook until slightly softened, 2–3 minutes.
7. Stir in spinach until just wilted.
8. Add cooked gnocchi and mix everything to combine.
9. Optional: sprinkle cheese on top.
10. Transfer to oven and bake 10–15 minutes until bubbly and golden.
11. Sprinkle with chopped parsley or cilantro before serving.""",
 "notes": "This is a flexible one-pan meal – swap turkey for beef or ground pork. Cherry tomatoes work great and hold their shape better during baking. Adding mozzarella on top creates a great golden crust."},

# ── 20 ──────────────────────────────────────────────────────────────────────
{"name": "Cheddar Jalapeño Herb Grits",
 "categories": ["Vegetable"],
 "collections": [CI, "Stovetop"],
 "yield": "4",
 "prep_time": "10 min",
 "cook_time": "25 min",
 "source": "ChatGPT",
 "image_query": "cheddar grits jalapeño herb creamy bowl",
 "ingredients": """1 cup stone-ground grits (or quick grits)
4 cups water (or 2 cups milk + 2 cups water for creamier grits)
½ tsp salt
1 Tbsp butter
1 cup sharp cheddar cheese, shredded
1 jalapeño, finely diced (remove seeds for less heat)
2 Tbsp fresh basil, finely chopped
2 Tbsp fresh chives, finely chopped
Black pepper to taste
Optional: splash of cream or milk for extra richness""",
 "directions": """1. In a medium saucepan, bring water (or water/milk mix) and salt to a boil.
2. Slowly whisk in grits to prevent lumps.
3. Reduce heat to low and simmer, stirring often, until thick and tender (about 20–25 minutes for stone-ground, 5–7 minutes for quick grits).
4. Stir in butter, shredded cheddar, diced jalapeño, basil, and chives. Mix until cheese is melted and everything is combined.
5. If grits are too thick, add a splash of milk or cream to loosen.
6. Season with black pepper to taste.
7. Serve hot, optionally topped with extra chives or shredded cheddar.""",
 "notes": "Great as a savory breakfast base or side dish. Use the milk + water combo for significantly creamier texture. Stone-ground grits have a better flavor and texture but take longer to cook. Add crumbled bacon or fried eggs on top for a complete breakfast."},

# ── 21 ──────────────────────────────────────────────────────────────────────
{"name": "Chilaquiles Verdes with Pre-Cooked Steak, Barbacoa, Eggs & Cotija",
 "categories": ["Beef", "Egg"],
 "collections": [CI, "Stovetop"],
 "yield": "2",
 "prep_time": "15 min",
 "cook_time": "15 min",
 "source": "ChatGPT",
 "image_query": "chilaquiles verdes green salsa eggs cotija Mexican",
 "ingredients": """4–6 corn tortillas, cut into triangles
Green salsa (tomatillo-based)
Pre-cooked carne asada, bite-size pieces
Pre-cooked barbacoa, bite-size pieces
Small handful white onion, diced
2 eggs (1–2 per person)
Cotija cheese, crumbled
Cilantro
Lime wedges
Neutral oil
Salt""",
 "directions": """1. Fry tortilla pieces in hot oil until golden and crispy. Remove to paper towel and lightly salt. (Or dry-toast in pan for lighter chilaquiles.)

2. In the same pan, add a touch more oil over medium heat. Add onion and sauté 30–60 seconds.
3. Add carne asada and barbacoa. Toss briefly (30–45 seconds max) just to warm – do not let sit or meat will dry out. Remove from pan and set aside.

4. Reduce heat to medium-low. Pour green salsa into the skillet. Thin with a splash of water if thick. Warm 1–2 minutes.

5. Add tortilla chips to salsa. Toss gently 30–60 seconds – you want crispy edges and saucy centers. Pull pan off heat when edges soften but centers stay crisp.

6. Fold warmed meat back in. Toss once or twice to distribute.

7. Eggs – Fried (Recommended): Cook separately in a small pan. Set whites, runny yolks.
   Or Scramble: Push chilaquiles aside, soft scramble eggs, fold into skillet.

8. Plate chilaquiles, top with fried eggs.
9. Crumble cotija generously over everything.
10. Add cilantro and a big squeeze of fresh lime.""",
 "notes": "Cotija is salty – go light on salt earlier in the process. Runny egg yolk balances the heat from the green salsa beautifully. If chips soften too fast, you used too much salsa – add a few fresh chips to correct. For crunchy result: minimal sauce time. For traditional: 1–2 min soak. For comfort-style: more salsa + brief simmer."},

# ── 22 ──────────────────────────────────────────────────────────────────────
{"name": "Authentic Greek Tzatziki",
 "categories": ["Sauce", "Dip"],
 "collections": [CI, "Greece", "Condiments"],
 "yield": "4–6",
 "prep_time": "15 min + 1 hr chill",
 "cook_time": "0 min",
 "source": "ChatGPT",
 "image_query": "authentic Greek tzatziki dip cucumber yogurt",
 "ingredients": """2 cups (500g) full-fat strained Greek yogurt
1 medium cucumber (8–10 inches), peeled and grated
2–3 cloves garlic, finely minced or crushed into paste with salt
2 Tbsp extra virgin olive oil
1 Tbsp white wine vinegar (or fresh lemon juice)
1–2 Tbsp fresh dill, finely chopped (or mint)
Salt to taste
Optional: drizzle of olive oil for serving""",
 "directions": """1. Peel and grate the cucumber using the large side of a box grater.
2. Place grated cucumber in a clean kitchen towel or cheesecloth and squeeze out as much liquid as possible. This step is crucial so tzatziki isn't watery.
3. In a medium bowl, combine Greek yogurt, garlic, olive oil, and vinegar or lemon juice. Mix until smooth.
4. Stir in the drained cucumber and chopped dill (or mint). Mix well.
5. Taste and adjust with salt, garlic, or vinegar/lemon for sharpness.
6. Refrigerate at least 1 hour before serving to let flavors meld.
7. Serve cold with pita bread, grilled meats, vegetables, or as a dip. Drizzle extra olive oil on top.""",
 "notes": "Always use full-fat strained Greek yogurt for the right thickness and tang. The garlic should be raw and mashed into a paste with a little salt to release full flavor. Tzatziki should be thick enough to cling to your spoon – this is the traditional Greek style. Do not skip squeezing the cucumber."},

# ── 23 ──────────────────────────────────────────────────────────────────────
{"name": "Carrot Greens, Basil & Chive Pesto",
 "categories": ["Sauce"],
 "collections": [CI, "Condiments"],
 "yield": "~1 cup",
 "prep_time": "15 min",
 "cook_time": "0 min",
 "source": "ChatGPT",
 "image_query": "homemade herb pesto green sauce carrot tops basil",
 "ingredients": """1 cup carrot greens (young, tender leaves only – discard thick stems), packed
½ cup fresh basil leaves, packed
¼ cup fresh chives, roughly chopped
2–3 cloves garlic
¼ cup pine nuts (or walnuts, or toasted sunflower seeds)
½ cup extra virgin olive oil
¼–½ cup grated Parmesan (or Pecorino Romano)
Juice of ½ lemon
Salt & pepper to taste""",
 "directions": """1. Rinse carrot greens, basil, and chives thoroughly. Pat or spin dry.
2. Add garlic and pine nuts to a food processor and pulse 5–6 times until coarsely chopped.
3. Add carrot greens, basil, and chives. Pulse again until roughly combined.
4. With the processor running, slowly drizzle in olive oil until smooth but still textured. Don't over-process – some texture is good.
5. Add Parmesan, lemon juice, salt, and pepper. Pulse a few more times to combine.
6. Taste and adjust seasoning: more lemon for brightness, more cheese for richness, more salt as needed.
7. Use immediately or store in an airtight jar with a thin layer of olive oil on top (refrigerate up to 1 week, freeze up to 3 months).""",
 "notes": "Use only young tender carrot green leaves – older stems are more bitter. The chive version adds a mild onion note that complements the slight bitterness of the carrot greens. Great on pasta, grilled proteins, sandwiches, or as a dip. Works well with toasted sunflower seeds as a nut-free option."},

# ── 24 ──────────────────────────────────────────────────────────────────────
{"name": "Cilantro-Garlic Chimichurri (Spoonable Version)",
 "categories": ["Sauce"],
 "collections": [CI, "Condiments"],
 "yield": "~1 cup",
 "prep_time": "10 min",
 "cook_time": "0 min",
 "source": "ChatGPT",
 "image_query": "cilantro chimichurri sauce green herb garlic",
 "ingredients": """1 cup fresh cilantro, finely chopped (packed)
4–5 cloves garlic, minced or pressed
1 tsp kosher salt
½ tsp black pepper
½ tsp crushed red pepper flakes (adjust to taste)
3 Tbsp red wine vinegar
½ cup extra virgin olive oil
Optional: 2 Tbsp fresh parsley, finely chopped
Optional: ½ tsp dried oregano""",
 "directions": """1. Finely chop cilantro (and parsley if using). Mince garlic.
2. In a bowl, combine cilantro, garlic, salt, pepper, red pepper flakes, and oregano if using.
3. Add red wine vinegar and stir well.
4. Slowly whisk in olive oil until combined. Sauce should be spoonable, not pureed.
5. Taste and adjust: more vinegar for tang, more red pepper for heat, more salt as needed.
6. Let sit at room temperature for at least 15–30 minutes before serving so flavors meld.
7. Serve spooned over grilled meats, fish, vegetables, or as a dipping sauce.
Store in refrigerator up to 1 week. Bring to room temperature before serving.""",
 "notes": "This is the spoonable style (not blended) – keep it chunky. Great on carne asada, chicken, shrimp, or grilled vegetables. If cilantro is too grassy, add more parsley to balance."},

# ── 25 ──────────────────────────────────────────────────────────────────────
{"name": "Classic Buffalo Dipping Sauce",
 "categories": ["Sauce", "Dip"],
 "collections": [CI, "Condiments"],
 "yield": "¾ cup",
 "prep_time": "2 min",
 "cook_time": "5 min",
 "source": "ChatGPT",
 "image_query": "buffalo hot sauce dipping sauce Frank's butter",
 "ingredients": """½ cup Frank's RedHot Original sauce
¼ cup unsalted butter
Optional: pinch of garlic powder or onion powder""",
 "directions": """1. Melt the butter in a small saucepan over low heat.
2. Whisk in Frank's RedHot until fully combined.
3. Simmer gently for 1–2 minutes. Do not boil.
4. Taste and adjust if needed (more hot sauce for heat, more butter for richness).
5. Serve warm for dipping.

Variations:
- Extra Spicy: add ½–1 tsp cayenne or a few dashes of hotter hot sauce.
- Garlic Buffalo: add ½ tsp garlic powder or 1 small minced clove (sauté briefly in butter first).
- Creamy Buffalo Dip: combine ½ cup buffalo sauce with ¼ cup ranch or blue cheese dressing.
- Sweet Heat Buffalo: add 1–2 tsp honey or brown sugar.""",
 "notes": "If sauce separates as it cools, just re-whisk or warm slightly. Keeps well in the fridge 5–7 days; reheat gently. Classic ratio is 1:1 hot sauce to butter – adjust to taste."},

# ── 26 ──────────────────────────────────────────────────────────────────────
{"name": "Pickled Carrots & Green Beans (Refrigerator)",
 "categories": ["Vegetable"],
 "collections": [CI, "Pickling"],
 "yield": "1 quart",
 "prep_time": "20 min",
 "cook_time": "0 min (ready in 48 hrs)",
 "source": "ChatGPT",
 "image_query": "refrigerator pickled carrots green beans jar garlic jalapeño",
 "ingredients": """1 lb carrots, peeled and cut into sticks (or coins)
½ lb green beans, trimmed and cut to fit jar
3–4 cloves garlic, peeled
1–2 jalapeños, sliced (optional, adjust heat to taste)
1–2 Tbsp pickling spice (optional)

Brine:
1 cup white wine vinegar (or apple cider vinegar)
1 cup water
1 Tbsp kosher salt
1 Tbsp sugar""",
 "directions": """1. Wash and cut vegetables. Pack carrots and green beans tightly into a clean quart jar, alternating for a nice look.
2. Add garlic cloves, jalapeño slices, and pickling spice (if using) between the vegetables.
3. Make the brine: combine vinegar, water, salt, and sugar in a saucepan. Heat over medium, stirring until salt and sugar fully dissolve. Do not boil.
4. Pour hot brine over vegetables, making sure all vegetables are submerged. Leave ½ inch headspace.
5. Let cool to room temperature, then seal and refrigerate.
6. Ready to eat in 48 hours. Best flavor develops at 3–5 days.
7. Store in refrigerator up to 3–4 weeks.""",
 "notes": "Refrigerator pickles only – not shelf stable. For crisper pickles, refrigerate vegetables overnight before pickling and use cold brine. Can add fresh dill or whole peppercorns to the jar for extra flavor."},

# ── 27 ──────────────────────────────────────────────────────────────────────
{"name": "Pickled Smoked Eggs (Refrigerator)",
 "categories": ["Egg"],
 "collections": [CI, "Pickling"],
 "yield": "6 eggs",
 "prep_time": "15 min",
 "cook_time": "0 min (ready in 48 hrs)",
 "source": "ChatGPT",
 "image_query": "pickled smoked eggs jar pink beet or yellow",
 "ingredients": """6 hard-boiled eggs, peeled (smoked or regular)
3–4 cloves garlic, peeled
Optional: ½ tsp mustard seeds, ½ tsp whole peppercorns, 1–2 jalapeño slices, 1 tsp pickling spice

Brine:
1 cup white wine vinegar (or apple cider vinegar)
½ cup water
1 Tbsp kosher salt
1 Tbsp sugar
Optional: beet juice for pink color""",
 "directions": """1. Hard-boil eggs: cover with cold water, bring to boil, turn off heat, cover and rest 12 minutes. Transfer to ice bath immediately. Peel when cold.
2. Smoke eggs (optional): after peeling, cold-smoke or briefly hot-smoke eggs on Traeger at lowest setting for 30–60 minutes for smoke flavor. Cool completely.
3. Place peeled eggs (and any optional aromatics) into a clean quart jar.
4. Make the brine: combine vinegar, water, salt, and sugar. Heat and stir until dissolved.
5. Add beet juice if using for color. Let brine cool slightly.
6. Pour brine over eggs, ensuring eggs are fully submerged.
7. Seal and refrigerate at least 48 hours before eating. Best at 3–5 days.
8. Store in refrigerator up to 2 weeks.""",
 "notes": "Refrigerator only – not shelf stable. Smoked eggs have deeper, more complex flavor in the pickle brine. Add beet juice for beautiful pink-red color. Do not leave at room temperature after pickling."},

# ── 28 ──────────────────────────────────────────────────────────────────────
{"name": "Greek Orange Pie (Portokalopita)",
 "categories": ["Cake"],
 "collections": [CI, "Greece", "Oven"],
 "yield": "12",
 "prep_time": "30 min",
 "cook_time": "50 min",
 "source": "ChatGPT",
 "image_query": "Greek portokalopita orange phyllo syrup cake",
 "ingredients": """For the Cake:
1 lb (450g) phyllo dough sheets, thawed
1 cup plain Greek yogurt
½ cup vegetable oil (or olive oil)
4 eggs
1½ cups sugar
Zest of 2 oranges
Juice of 1 orange (about ½ cup)
1 tsp vanilla extract
1 tsp baking powder
½ tsp baking soda

For the Syrup:
1½ cups sugar
1 cup water
Juice of 2 oranges
Zest of 1 orange
Optional: 1–2 cinnamon sticks while simmering""",
 "directions": """Prepare Phyllo:
1. Unroll phyllo and lay sheets out on a clean surface. Let air-dry until crinkled and dry (or tear roughly into pieces and leave exposed 30–60 minutes). The goal is dried, shredded phyllo – not soft. This is key to texture.

Make the Batter:
2. In a large bowl, whisk together eggs and sugar until pale.
3. Add oil, yogurt, orange juice, orange zest, and vanilla. Mix until smooth.
4. Stir in baking powder and baking soda.
5. Add the dried, crinkled phyllo pieces to the batter. Fold and press until all phyllo is moistened and no dry pieces remain. Let sit 10–15 minutes so phyllo absorbs the batter.

Bake:
6. Preheat oven to 350°F (175°C). Grease a 9×13 inch baking pan.
7. Pour phyllo mixture into pan and spread evenly.
8. Bake 45–50 minutes until deep golden and set in the center. A toothpick should come out clean.

Make the Syrup (while cake bakes):
9. Combine sugar, water, orange juice, and zest in a saucepan. Bring to a boil, add cinnamon sticks if using, simmer 5 minutes. Remove from heat.

Finish:
10. Remove hot cake from oven. Immediately pour hot syrup slowly and evenly over the hot cake. The cake will sizzle and absorb the syrup.
11. Let cool completely before cutting (at least 1–2 hours). The syrup continues to absorb as it cools.""",
 "notes": "The key to authentic portokalopita is properly drying the phyllo before mixing – it should be crinkled and crisp, not soft. Pour hot syrup over hot cake – do not let either cool first. The cake keeps well at room temperature up to 3 days, actually improving in flavor as the syrup absorbs."},

# ── 29 ──────────────────────────────────────────────────────────────────────
{"name": "Peanut Butter Filled Pancakes",
 "categories": ["Bread"],
 "collections": [CI, "Stovetop"],
 "yield": "8–10 pancakes",
 "prep_time": "10 min",
 "cook_time": "20 min",
 "source": "ChatGPT",
 "image_query": "peanut butter filled fluffy pancakes stack",
 "ingredients": """1 box pancake mix (plus ingredients listed on the box, usually water/egg/oil)
½ cup creamy peanut butter (natural or commercial)
Optional: banana slices for inside or on top
Optional: honey or maple syrup for serving
Optional: crushed peanuts for garnish""",
 "directions": """1. Mix pancake batter according to package instructions. Let batter rest 5 minutes.
2. Heat non-stick skillet or griddle over medium heat. Lightly grease.
3. Pour a small amount of batter (about ¼ cup) for the base of each pancake.
4. While batter is still wet on top (about 1 minute), add a rounded teaspoon of peanut butter in the center.
5. Cover peanut butter with just enough additional batter to seal it in.
6. Cook until bubbles form and edges look set, about 2–3 minutes.
7. Flip gently and cook another 1–2 minutes until golden.
8. Repeat with remaining batter and peanut butter.
9. Serve immediately with maple syrup, honey, or banana slices on top.""",
 "notes": "For best results: use room temperature peanut butter (easier to portion). Natural peanut butter that's been stirred works well. Don't make pancakes too thick or the peanut butter won't warm through. These also work in a small waffle maker – same filling technique."},

# ── 30 ──────────────────────────────────────────────────────────────────────
{"name": "Ham Glaze for 10-lb Ham",
 "categories": ["Pork"],
 "collections": [CI, "Oven"],
 "yield": "~10",
 "prep_time": "10 min",
 "cook_time": "2.5–3.5 hours total",
 "source": "ChatGPT",
 "image_query": "glazed holiday ham brown sugar pineapple oven",
 "ingredients": """1 bone-in ham, fully cooked (about 10 lbs)

Glaze:
1 cup brown sugar, packed
¼ cup Dijon mustard
¼ cup honey
2 Tbsp apple cider vinegar
½ tsp ground cloves
½ tsp cinnamon
Optional: 1 Tbsp pineapple juice or orange juice""",
 "directions": """1. Remove ham from refrigerator 30–60 minutes before cooking to come to room temperature.
2. Preheat oven to 325°F.
3. Score the ham: use a sharp knife to cut a crosshatch pattern about ½ inch deep across the surface.
4. Place ham cut-side down in a roasting pan. Add a splash of water or juice to the bottom of the pan.
5. Cover tightly with foil and bake at 325°F for about 15 minutes per pound (about 2–2.5 hours for 10 lbs), until internal temp reaches 130°F.
6. Make the glaze: whisk together brown sugar, Dijon, honey, vinegar, cloves, cinnamon, and juice if using.
7. Remove foil. Brush ham generously with glaze. Increase oven to 400°F.
8. Return ham uncovered and bake 20–30 minutes more, brushing with additional glaze every 10 minutes, until caramelized and internal temp reaches 140°F.
9. Remove from oven, tent loosely with foil, and rest 20–30 minutes before carving.""",
 "notes": "For a 10-lb ham: total cook time is roughly 2.5–3.5 hours. A fully cooked ham just needs to be heated to 140°F – don't overcook. Apply glaze only in the final 20–30 minutes or the sugar will burn. Multiple glaze coats in the last phase build up a better caramelized crust."},

]  # end RECIPES list


# ---------------------------------------------------------------------------
# Helper: fetch image URL via edge function
# ---------------------------------------------------------------------------
def fetch_image(query: str) -> str | None:
    try:
        body = json.dumps({"query": query}).encode()
        req  = urllib.request.Request(IMG_FN, data=body,
                                      headers={"Content-Type": "application/json"},
                                      method="POST")
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
            urls = data.get("urls") or []
            return urls[0] if urls else None
    except Exception as e:
        print(f"  [img error] {e}")
        return None


# ---------------------------------------------------------------------------
# Helper: insert one recipe via REST API
# ---------------------------------------------------------------------------
def insert_recipe(recipe: dict) -> bool:
    payload = json.dumps({
        "name":        recipe["name"],
        "categories":  recipe["categories"],
        "collections": recipe["collections"],
        "source":      recipe.get("source", "ChatGPT"),
        "yield":       recipe.get("yield", ""),
        "prep_time":   recipe.get("prep_time", ""),
        "cook_time":   recipe.get("cook_time", ""),
        "ingredients": recipe.get("ingredients", ""),
        "directions":  recipe.get("directions", ""),
        "notes":       recipe.get("notes", ""),
        "image_url":   recipe.get("image_url"),
    }).encode()

    req = urllib.request.Request(
        REST_URL,
        data=payload,
        headers={**HEADERS, "Prefer": "return=minimal"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status in (200, 201)
    except urllib.error.HTTPError as e:
        print(f"  [insert error {e.code}] {e.read()[:200]}")
        return False
    except Exception as e:
        print(f"  [insert error] {e}")
        return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    ok = 0
    fail = 0
    for i, recipe in enumerate(RECIPES, 1):
        name = recipe["name"]
        print(f"[{i:02d}/{len(RECIPES)}] {name}")

        # Fetch image
        img = fetch_image(recipe.pop("image_query"))
        recipe["image_url"] = img
        print(f"  image: {img or 'none'}")

        # Insert
        success = insert_recipe(recipe)
        if success:
            print(f"  ✓ inserted")
            ok += 1
        else:
            print(f"  ✗ FAILED")
            fail += 1

        time.sleep(0.4)  # be polite to the API

    print(f"\n{'='*50}")
    print(f"Done: {ok} inserted, {fail} failed out of {len(RECIPES)}")
