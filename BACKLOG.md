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

## 🔲 Share Recipe — Non-Logged-In Landing UX

**What:** When a non-logged-in user opens a `?recipe=ID` share link, they land on the login screen with no context. They should see a banner: "Someone shared a recipe with you — sign in to view it."

---

## 🔲 Retention: Cook Streak

**What:** Light gamification to pull users back. Show a streak counter for consecutive weeks where they logged at least one cook.

- Calculated from the `cook_logs` table (already exists)
- Display on home page or profile — "🔥 3-week streak"
- Reset if a full week passes with no cook logged
- Milestone toasts: "First cook!", "4-week streak 🔥"

---

## 🔲 Retention: Funnel Drop-off Tracking

**What:** Instrument the key moments where users abandon to understand where value isn't landing.

Key funnel stages:
1. Signed up → completed onboarding (or skipped at which step)
2. Completed onboarding → added first recipe (within first session)
3. Added first recipe → came back on day 3+
4. Returned → cooked a recipe (logged a cook)

Some `track()` calls already exist. Add a funnel conversion view to the analytics dashboard showing % at each step.

---

## 🔲 Retention: Re-engagement Email

**What:** If a user hasn't opened the app in 7 days, send an email nudging them back.

- Supabase scheduled function (pg_cron) that runs nightly
- Finds users where last `events` row is >7 days ago
- Sends via Resend: "You've got X recipes saved — here's one to cook this week" with a random recipe
- One email max per user per 14 days (add `last_nudge_sent_at` to profiles)

---
