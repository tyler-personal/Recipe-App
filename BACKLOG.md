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
