# Local development

SkyForged is a static HTML/CSS/JavaScript application; there is no package installation or backend required for basic use.

## Start a local server

```bash
git clone https://github.com/Saitanveesh/Sky-Frodged.git
cd Sky-Frodged
python -m http.server 8000
```

Open `http://127.0.0.1:8000/` in a modern browser. On macOS/Linux, use `python3` if your system does not provide `python`.

**Windows PowerShell:**

```powershell
py -3 -m http.server 8000
```

Pages using remote CDN libraries or map tiles need a working network connection even though the site itself is static.

## Files worth knowing

- `index.html`: landing page and module navigation
- `css/style.css`: shared styles
- `js/main.js`: navigation and site search
- `js/database.js`: large component catalogue
- `js/builder.js`: build-selection and compatibility heuristics
- `js/tools.js`: RF calculation utilities
- `js/maps.js`: educational airport-distance overlays
- `wrangler.jsonc`: optional Cloudflare deployment configuration

## Quick checks

```bash
python scripts/check_site.py
```

This checks the presence of critical entrypoints, local resources referenced directly from HTML, and major navigation links. It is not a browser test.

If Node.js is available:

```bash
node --check js/main.js
# Check all JavaScript source files:
for file in js/*.js; do node --check "$file"; done
```

On PowerShell:

```powershell
Get-ChildItem js/*.js | ForEach-Object { node --check $_.FullName }
```

The CI workflow runs both link and JavaScript syntax checks.

## Deployment

Any static host capable of serving `.html`, `.css`, `.js` and image files can serve SkyForged. The project includes `wrangler.jsonc` for a Cloudflare-style asset deployment. The repository homepage is configured as `https://skyforged.saitanveesh.workers.dev/`. **Availability has not been independently verified from this environment**; use the local instructions above if that endpoint is inaccessible. A previously referenced GitHub Pages URL is not the current configured homepage.

## Data and operational limits

The site does not supply authoritative airspace, live regulatory status, or guaranteed component compatibility. Never use the simplified airport buffer demo as a substitute for official airspace information.
