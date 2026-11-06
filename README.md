<p align="center"><img src="docs/assets/skyforged-banner.svg" width="100%" alt="SkyForged — a browser-based UAV engineering workspace with build planning, RF tools and learning resources"></p>

<p align="center">
<a href="#quick-start">Get started</a> ·
<a href="#explore-the-workspace">Explore modules</a> ·
<a href="docs/FEATURES.md">Feature status</a> ·
<a href="docs/ROADMAP.md">Roadmap</a> ·
<a href="CONTRIBUTING.md">Contribute</a>
</p>

<p align="center">
<img src="https://img.shields.io/badge/HTML-CSS%20%2B%20JavaScript-2396df?style=flat-square" alt="HTML, CSS, JavaScript">
<img src="https://img.shields.io/badge/backend-none-16a085?style=flat-square" alt="No application backend">
<img src="https://img.shields.io/badge/deployment-static%20site-7289da?style=flat-square" alt="Static-site deployment">
<img src="https://img.shields.io/badge/license-not%20yet%20specified-f3b64c?style=flat-square" alt="No project license published yet">
</p>

<p align="center"><strong>Learn the system. Plan the build. Check your assumptions.</strong></p>

**SkyForged** is a browser-based UAV engineering workspace that puts learning resources, hardware planning, RF calculators and field checklists in one place. It is intended for students, makers and engineers who want to understand how drone subsystems fit together before working on a real aircraft.

No user account or application server is required. Most tools run directly in the browser. Some modules need an internet connection for third-party map tiles or libraries.

> [!IMPORTANT]
> **Engineering reference, not flight approval.** Component data, compatibility checks, RF range estimates, and educational airport-distance overlays may be incomplete or inaccurate. **The airspace page is not an official DGCA map** and must not be used to authorize a flight. Use manufacturer documentation and current official aviation information for real operations.

## Why SkyForged?

Drone engineering questions cut across multiple disciplines: motor/prop compatibility, available electrical power, flight-controller I/O, antennas, link budgets, firmware, and regulations. SkyForged keeps these subjects in a single accessible workspace, showing the assumptions behind engineering choices.

- **One browser workspace** with dedicated pages for learning, RF, build planning and operations.
- **Local calculation tools** for exploration and comparative estimates.
- **Component catalogue** with more than 3,800 records (not guaranteed current or verified).
- **Readable references** explaining how individual UAV subsystems interact.

<p align="center">
<img src="assets/hero_drone.png" width="85%" alt="SkyForged drone-themed hero artwork">
</p>

## Explore the workspace

| Module | What you can do |
|---|---|
| [Academy](academy.html) | Follow a beginner learning path and reference drone terminology |
| [Anatomy](anatomy.html) | Inspect an interactive FPV-component breakdown |
| [Blueprint](blueprint.html) | Explore thrust-to-weight, battery, propulsion and sizing relationships |
| [Model Builder](builder.html) | Select parts and review heuristic compatibility checks and estimates |
| [RF Tools](tools.html) | Calculate link-budget terms, antenna dimensions, Fresnel clearance and more |
| [PID Tuning](pid.html) | Connect tuning concepts with possible flight behavior and hardware problems |
| [Handbook](handbook.html) | Read UAV integration, links, firmware and field reference notes |
| [Platforms](platforms.html) | Browse a developing platform reference dataset |
| [Airspace Reference](maps.html) | Explore **illustrative** airport-distance buffers; **not official airspace data** |
| [Operations](ops.html) | Use preparation checklists and estimation utilities |

View the [feature matrix and limitations](docs/FEATURES.md) before treating any output as engineering evidence.

## Quick start

All you need for a local copy is a browser, Git and optionally Python 3 (for a local static HTTP server).

```bash
git clone https://github.com/Saitanveesh/Sky-Frodged.git
cd Sky-Frodged
python -m http.server 8000
```

Open **http://127.0.0.1:8000/**. Use `python3` instead of `python` on systems where needed.

The repository name is **`Sky-Frodged`** (historical spelling); the application name shown in the UI is **SkyForged**. Do not use the `skyforged` Git URL unless the repository itself has been renamed.

The earlier README cited a GitHub Pages URL, but **the deployed URL could not be verified during this documentation update**. Local serving is the supported onboarding path for now. See [development instructions](docs/DEVELOPMENT.md).

## How it works

```text
SkyForged (static browser site)
  ├── HTML pages            learning, planning, tools and references
  ├── css/style.css         shared styling
  ├── js/*.js               calculators, interactive features and data views
  ├── js/database.js        local component records
  └── assets/               page artwork and illustrations

External resources (where used)
  ├── Leaflet via CDN
  └── OpenStreetMap tiles
```

There is **no application backend, shared account system, or live flight-controller link** in this repository. The site is a planning/reference tool, not a command-and-control platform.

## Reliability and limitations

SkyForged is evolving, and its scope should remain explicit:

- **Hardware data:** records and prices may be stale or incomplete; always validate against manufacturer datasheets.
- **Build checker:** heuristic checks do not establish flightworthiness or electrical safety.
- **RF tools:** free-space and simplified link models are not measured coverage predictions; terrain, interference, antennas and regulations matter.
- **Airspace:** the map plots simplified distance buffers around a small list of airports. **It is not a current or complete depiction of Indian controlled/restricted airspace.**
- **Platform references:** certification and specs require up-to-date external verification.

See [scope and status](docs/FEATURES.md) and [improvement priorities](docs/ROADMAP.md).

## Project structure

```text
Sky-Frodged/
├── index.html                 landing page
├── academy.html / anatomy.html
├── blueprint.html / builder.html
├── tools.html / pid.html / handbook.html
├── platforms.html / maps.html / ops.html
├── css/                       styling
├── js/                        page logic and component dataset
├── assets/                    artwork and illustrations
├── docs/                      development, feature scope, roadmap
└── wrangler.jsonc             optional Cloudflare Workers assets configuration
```

## Contributing

Bug reports, verified component corrections, engineering-calculator tests, accessibility improvements and documentation changes are valuable. Read [CONTRIBUTING.md](CONTRIBUTING.md) for a focused workflow and [SECURITY.md](SECURITY.md) for responsible reporting.

This repository currently has **no top-level source license**. Public visibility does not automatically grant reuse, redistribution or modification rights. The maintainer needs to choose and publish a license before contributors can confidently redistribute the software. Third-party images, libraries and datasets can carry separate terms.

---

<p align="center"><sub>SkyForged — an engineering workspace for learning and planning, not a substitute for manufacturer validation or official flight authorization.</sub></p>
