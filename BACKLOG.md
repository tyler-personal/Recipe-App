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

## 🚧 Retention: Weekly Digest Email (TEST MODE: Tyler only)

**Built:** `weekly-digest` edge function, `profiles.digest_enabled` / `digest_opt_out`, `digest_log`, `recipe_engaged` event (45s on a recipe), `?cooked=1` / `?onboarding=1` links, Settings → "Weekly digest (test mode)" with Preview and Send-test buttons.

Sections (only those with real content; skipped entirely if nothing worth saying, and feature tips are never sent alone): finish onboarding, "did you make it?", recommendations (similarity scoring + AI-written reasons), new from the community, features not yet tried.

**Safety:** hardcoded test allow-list in the function + opt-in flag + `DIGEST_LIVE` must be set to go beyond it. Unsubscribe link + List-Unsubscribe header in every email. Max 1 email / 6 days in batch runs.

**Still to do before anyone else gets it:**
- Add `RESEND_API_KEY` as an Edge Function secret (dashboard). `DIGEST_SECRET` is only needed later, for the weekly scheduler.
- Review real previews, tune thresholds/wording
- Weekly schedule (pg_cron calling the function in batch mode; pg_net is already installed)
- Add a physical mailing address to the footer (required for bulk email)
- Decide opt-in vs opt-out rollout, then set `DIGEST_LIVE=true`

---
