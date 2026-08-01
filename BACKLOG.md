# Recipe Duck — Backlog / To-Do

---

## ✅ Analytics Dashboard (Admin)
Admin-only section in Settings, gated by `is_admin`. Date filter tabs (Today/7d/30d/All time), clickable tiles with drill-down: user table, top recipes by views, per-user feature breakdowns, delta vs prior period.

---

## ✅ Dietary Restrictions
- User dietary profile modal (checklist of 20+ tags, saved to `profiles.dietary_restrictions`)
- `dietary_tags` column on recipes, AI backfill button in Settings, auto-tagged on save
- "🥗 My Diet" filter tab on home page and in swipe session filter
- Dietary tag pills on recipe detail page
- "Adapt for my diet" AI modal — substitution table, adapted ingredients/directions, save as variant

---

## ✅ Share Recipe — Non-Logged-In Landing UX
When a non-logged-in user opens a `?recipe=ID` share link, the login screen shows a banner: "Someone shared a recipe with you — sign in or create a free account to view it." After auth they're taken directly to the recipe.

---

## ✅ Retention: Cook Streak
Weekly streak counter (consecutive Mon-based weeks with ≥1 cook logged via `recipe_ratings`). Streak pill on home page: "🔥 3-week streak". Resets on a missed week. Milestone toasts at 1/4/8/12 weeks.

---

## ✅ Retention: Funnel Drop-off Tracking
`track('cook_logged')` added. Conversion Funnel section in analytics dashboard (all-time): Signed up → Completed onboarding → Added first recipe → Came back day 3+ → Logged a cook, with % conversion and bar chart at each step.

---

## 🔲 Retention: Re-engagement Email

**What:** If a user hasn't opened the app in 7 days, send an email nudging them back.

- Supabase scheduled function (pg_cron) that runs nightly
- Finds users where last `events` row is >7 days ago
- Sends via Resend: "You've got X recipes saved — here's one to cook this week" with a random recipe
- One email max per user per 14 days (add `last_nudge_sent_at` to profiles)

---
