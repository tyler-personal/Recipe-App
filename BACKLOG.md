# Recipe Duck — Backlog / To-Do

---

## 🔲 Analytics Dashboard (Admin)

**What:** Event tracking is live (`events` table in Supabase) but there's no UI to view it. Currently requires raw SQL queries to see anything useful.

**What to build:**
- Admin-only tab in Settings modal (gated by `is_admin` flag)
- Key metrics: total users, new this week, DAU/WAU
- Recipe stats: total, created this week, top viewed
- Feature usage tiles: AI generations, swipes, imports, shopping list adds, PDF shares
- Onboarding: completion rate, skip rate
- All pulled from the `events` table with simple SQL — no charting library needed

---

## 🔲 Share Recipe — Non-Logged-In Landing UX

**What:** When a non-logged-in user opens a `?recipe=ID` share link, they land on the login screen with no context. They should see a banner explaining why they're there (e.g. "Someone shared a recipe with you — sign in to view it").

---

## 🔲 Retention: Funnel Drop-off Tracking

**What:** Instrument the key moments where users abandon to understand where value isn't landing.

**Key funnel stages to track:**
1. Signed up → completed onboarding (or skipped at which step)
2. Completed onboarding → added first recipe (within first session)
3. Added first recipe → came back on day 3+
4. Returned → cooked a recipe (logged a cook)

**How:** Add `track()` calls at each stage (most are already there), then surface a funnel view in the analytics dashboard showing conversion % at each step.

---

## 🔲 Retention: Re-engagement Email

**What:** If a user hasn't opened the app in 7 days, send an email nudging them back.

**How it could work:**
- Supabase scheduled function (pg_cron) that runs nightly
- Finds users where last `events` row is >7 days ago
- Sends a simple email via Resend: "You've got X recipes saved — here's one to cook this week" with a random recipe from their collection
- One email max per user per 14 days (add a `last_nudge_sent_at` column to profiles)

---

## 🔲 Retention: Cook Streak

**What:** Light gamification to pull users back. Show a streak counter for consecutive weeks where they logged at least one cook.

**How it could work:**
- Calculated from the `cook_logs` table (already exists)
- Display on home page or profile — "🔥 3-week streak"
- Reset if a full week passes with no cook logged
- Milestone toasts: "First cook!", "4-week streak 🔥"

---
