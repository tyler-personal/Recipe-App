# Recipe Duck — Backlog / To-Do

---

## 🔲 Supabase Password Reset Email Branding

**What:** The password reset email currently comes from "Supabase Auth" with no Recipe Duck branding, making it confusing for users who don't know what it's for.

**How to fix (manual — requires dashboard access):**
1. Go to supabase.com → your project → **Authentication → Email Templates → Reset Password**
2. Update the subject to: `Reset your Recipe Duck password`
3. Replace the body with the branded HTML template (duck logo, green palette, clear Recipe Duck identity) — see conversation history for the full HTML, or ask Claude to regenerate it.

While there, also update the **Confirm signup** template to match.

---

## 🔲 Analytics Dashboard

**What:** Event tracking is live (`events` table in Supabase) but there's no UI to view it. Currently requires raw SQL queries to see anything useful.

**Ideas for what to build:**
- Admin-only panel showing key metrics: DAU/WAU, top viewed recipes, feature usage (AI, swipe, diet, scaler, shopping list), search queries with zero results, onboarding completion rate
- Could be a tab in the existing Settings modal (admin-only, already gated by `is_admin` flag)
- Simple bar/number tiles, no need for a charting library — plain numbers and lists are fine at this user scale

---
