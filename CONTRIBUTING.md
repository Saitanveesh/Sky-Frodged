# Contributing to SkyForged

SkyForged is a browser-based engineering learning and planning workspace. Contributions that make tools more accurate, easier to test or easier to understand are welcome for maintainer review.

> **License note:** This repository does not yet contain a top-level project license. Its public source is visible, but reuse and redistribution rights have not been specified. Before contributing substantial code or redistributing any part of the project, confirm the license policy with the maintainer.

## Contribution areas

- Correct component specifications with the **exact manufacturer datasheet URL, date and revision**.
- Add unit-tested RF, battery, propulsion or electrical calculations with declared assumptions.
- Improve keyboard navigation, mobile behavior and screen-reader support.
- Clarify which map and platform information is illustrative rather than authoritative.
- Fix broken links, incomplete documentation and local startup issues.
- Reduce the cost of maintaining the large static component catalogue.

## Workflow

1. Open an [issue](https://github.com/Saitanveesh/Sky-Frodged/issues) with the problem and a proposed, testable outcome.
2. Make focused changes to the relevant HTML, CSS, JavaScript or documentation.
3. Serve the site locally and verify affected pages in a browser.
4. Run the repository's source checks: `python scripts/check_site.py` and `node --check js/main.js` (CI checks all JavaScript).
5. Open a pull request with a short rationale, screenshots when visual behavior changes, and validation notes.

Use the [local development guide](docs/DEVELOPMENT.md) for platform-specific instructions.

## Evidence standard

A practical engineering reference needs traceable claims:

- Distinguish **computed estimates**, **manufacturer specifications**, and **direct measurements**.
- Do not label the educational map as an official DGCA source or a flight-permission decision.
- Do not present simplified range calculations as a guaranteed RF operating distance.
- When adding component data, cite original datasheets instead of guessing missing specs.
- Never commit personal information, private access tokens, credentials or images without the relevant rights.

## Pull requests

Keep a PR focused on a single module or issue. Describe the behavior before/after, relevant device/browser or dataset revision, and unresolved limitations.

Constructive review, including challenges to accuracy and safety claims, is encouraged.
