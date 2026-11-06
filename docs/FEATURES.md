# Feature scope and limitations

This matrix describes what the source tree contains, not a certification or verification of engineering calculations.

| Module | Present in source | Scope | Key limitation |
|---|---|---|---|
| Academy | Yes | Learning resources and terminology | Educational content may need revision |
| Anatomy | Yes | Interactive FPV layout references | Not an electrical integration diagram |
| Blueprint | Yes | Hardware sizing and calculation guidance | Estimates require datasheet confirmation |
| Builder | Yes | Local component catalogue and compatibility heuristics | Does not prove safe or flight-ready configurations |
| RF Tools | Yes | Channel, budget, propagation and antenna calculators | Simplified models; not real-world coverage guarantees |
| PID | Yes | Concepts and troubleshooting reference | No automatic aircraft tuning or validation |
| Handbook | Yes | Integration, protocol and field topics | Reference text, not an official firmware manual |
| Platforms | Yes | Developing database of aircraft | Specs and certifications require current verification |
| Maps | Yes | Buffers around a curated airport list | **Not an official DGCA zone map or legal authorization** |
| Operations | Yes | Checklists and planning utilities | Not a substitute for a certified operational procedure |

## Current data provenance boundaries

The component dataset is bundled in `js/database.js`. Manufacturer specifications and prices can change. Treat entries as **planning references pending independent validation**, not an up-to-date catalog with guaranteed accuracy.

RF calculators operate on formulas and user inputs. Actual results vary with antenna pattern, regulatory limits, interference, obstructions, cable losses, installation and environmental conditions.

## Airspace demonstration

The source code in `js/maps.js` contains a **small hard-coded list of airports** and plots simplified 5 km and 12 km circular buffers around them. These distances serve as examples within the app's educational model; they are **not the official definition or full coverage of India's airspace zones**. Areas outside those circles are **not necessarily legal to fly in**.

The background map uses OpenStreetMap tiles; a map tile provider does not establish aviation data accuracy.

Always consult official, current sources and obtain any required approvals before flight.

## License status

No root `LICENSE` file is currently published for SkyForged. A source-available GitHub repository is not automatically open-source licensed. Choosing an explicit license is a maintainer decision; see [Roadmap](ROADMAP.md).
