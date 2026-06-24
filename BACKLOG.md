# Recipe Duck — Backlog / To-Do

---

## 🔲 Analytics Dashboard

**What:** Event tracking is live (`events` table in Supabase) but there's no UI to view it. Currently requires raw SQL queries to see anything useful.

**Ideas for what to build:**
- Admin-only panel showing key metrics: DAU/WAU, top viewed recipes, feature usage (AI, swipe, diet, scaler, shopping list), search queries with zero results, onboarding completion rate
- Could be a tab in the existing Settings modal (admin-only, already gated by `is_admin` flag)
- Simple number tiles and lists — no charting library needed at this user scale

---

## 🔲 Share Recipe — QR Code Deep Link on Non-Logged-In Landing

**What:** When a non-logged-in user opens a `?recipe=ID` share link, they land on the login screen with no context. They should see a banner explaining why they're there (e.g. "Someone shared a recipe with you — sign in to view it").

---

## 🔲 Share Recipe (with QR Code)

**What:** Add a "Share" button to the recipe detail action row that lets users share a specific recipe — both as a link and as a QR code.

**How it should work:**
- Button in the recipe detail action row (alongside Cook, Edit, etc.)
- On tap: opens a small modal/sheet with two options:
  1. **Share link** — same flow as "Invite a Friend" (`navigator.share` on mobile, clipboard copy fallback on desktop). Link format: `https://recipeduck.ai/?recipe=RECIPE_ID`
  2. **QR code** — generate a QR code image for that same URL, displayed inline in the modal so the user can screenshot it or show their phone screen
- QR code generation: use the free `api.qrserver.com` API (`https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=URL`) — no install needed, just an `<img>` tag
- The app needs to handle the `?recipe=RECIPE_ID` deep link on load: if present and user is signed in, call `loadDetail(recipeId)` automatically

---
