// Serves the SPA for shared recipe links (/?recipe=ID) with recipe-specific Open Graph
// tags injected, so link previews (iMessage, Slack, WhatsApp, ...) show the recipe's
// name, photo and a short summary instead of the generic "Recipe Duck".
// Link-preview bots don't run JavaScript, so this has to be rendered server-side.
//
// The Supabase URL and anon key below are the same public values embedded in index.html.

const SUPA_URL = 'https://qrnfkgsxygkaqmzzbdbi.supabase.co';
const SUPA_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFybmZrZ3N4eWdrYXFtenpiZGJpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA2NjMzNjEsImV4cCI6MjA5NjIzOTM2MX0.u2zVCsAXkbAS_cgMzCUrkf92lGFaeZ5hmhUAi5rSX6k';
const UUID_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

const escAttr = (s) =>
  String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// "PT1H15M" -> "1 hr 15 min"
function prettyDuration(iso) {
  const m = /^PT(?:(\d+)H)?(?:(\d+)M)?$/i.exec(String(iso || '').trim());
  if (!m || (!m[1] && !m[2])) return String(iso || '').trim();
  return [m[1] ? `${m[1]} hr` : '', m[2] ? `${m[2]} min` : ''].filter(Boolean).join(' ');
}

function buildDescription(r) {
  const bits = [];
  const labels = [...(r.courses || []), ...(r.categories || [])].filter(Boolean);
  if (labels.length) bits.push(labels.slice(0, 3).join(', '));
  if (r.yield) bits.push(`Serves ${r.yield}`);
  const prep = prettyDuration(r.prep_time);
  const cook = prettyDuration(r.cook_time);
  if (prep) bits.push(`Prep ${prep}`);
  if (cook) bits.push(`Cook ${cook}`);
  const summary = bits.join(' · ');
  return summary ? `${summary} — shared on Recipe Duck` : 'Shared on Recipe Duck — open to see the full recipe.';
}

async function fetchPreview(id) {
  const r = await fetch(`${SUPA_URL}/rest/v1/rpc/get_recipe_preview`, {
    method: 'POST',
    headers: {
      apikey: SUPA_ANON_KEY,
      Authorization: `Bearer ${SUPA_ANON_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ p_id: id }),
  });
  if (!r.ok) return null;
  const rows = await r.json();
  return rows && rows[0] ? rows[0] : null;
}

module.exports = async function handler(req, res) {
  const proto = req.headers['x-forwarded-proto'] || 'https';
  const origin = `${proto}://${req.headers.host}`;
  const id = String((req.query && req.query.recipe) || '').trim();

  try {
    // The unmodified app shell. (/index.html is not matched by the rewrite, so no loop.)
    const shellRes = await fetch(`${origin}/index.html`);
    if (!shellRes.ok) throw new Error(`shell ${shellRes.status}`);
    let html = await shellRes.text();

    let recipe = null;
    if (UUID_RE.test(id)) {
      try { recipe = await fetchPreview(id); } catch (_) { /* fall through to the generic shell */ }
    }

    if (recipe && recipe.name) {
      const title = `${recipe.name} — Recipe Duck`;
      const desc = buildDescription(recipe);
      const image = recipe.image_url && /^https:\/\//i.test(recipe.image_url)
        ? recipe.image_url
        : `${origin}/apple-touch-icon.png`;
      const url = `${origin}/?recipe=${id}`;

      // /api/recipe-preview?recipe=ID&debug=1 shows what link-preview bots will see.
      if (req.query && req.query.debug) {
        res.setHeader('Content-Type', 'text/plain; charset=utf-8');
        res.setHeader('Cache-Control', 'no-store');
        return res.status(200).send(`function is running\ntitle: ${title}\ndescription: ${desc}\nimage: ${image}\nurl: ${url}\n`);
      }
      const tags = [
        `<meta name="description" content="${escAttr(desc)}">`,
        `<meta property="og:type" content="article">`,
        `<meta property="og:site_name" content="Recipe Duck">`,
        `<meta property="og:title" content="${escAttr(title)}">`,
        `<meta property="og:description" content="${escAttr(desc)}">`,
        `<meta property="og:image" content="${escAttr(image)}">`,
        `<meta property="og:url" content="${escAttr(url)}">`,
        `<meta name="twitter:card" content="summary_large_image">`,
        `<meta name="twitter:title" content="${escAttr(title)}">`,
        `<meta name="twitter:description" content="${escAttr(desc)}">`,
        `<meta name="twitter:image" content="${escAttr(image)}">`,
      ].join('\n');
      html = html
        .replace(/<title>[\s\S]*?<\/title>/i, () => `<title>${escAttr(title)}</title>`)
        .replace(/<\/head>/i, () => `${tags}\n</head>`);
    }

    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    res.setHeader('Cache-Control', 'public, s-maxage=300, stale-while-revalidate=86400');
    res.status(200).send(html);
  } catch (err) {
    // Never leave a real user on an error page: fall back to the plain app.
    res.setHeader('Cache-Control', 'no-store');
    res.redirect(302, `/index.html${id ? `?recipe=${encodeURIComponent(id)}` : ''}`);
  }
};
