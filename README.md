# SkyForged

I built SkyForged because, while working with drones, I kept running into the same problem: the information I needed was spread across too many places.

Component specifications were in datasheets and product pages. RF calculations were somewhere else. Flight-controller documentation had another set of information. Build planning usually ended up in spreadsheets, and regulatory information had to be checked separately.

SkyForged is my attempt to bring the parts I actually use while learning, building and studying UAV systems into one browser-based workspace.

**Live site:** https://saitanveesh.github.io/skyforged/

---

## What SkyForged is

SkyForged is not a flight controller, ground-control station or replacement for manufacturer documentation.

It is a collection of tools, notes and interactive references that I use to understand a drone as a complete system rather than as a collection of independent parts.

The project currently covers hardware selection, RF links, flight-control concepts, build calculations, tuning, field preparation and UAV communication systems.

Everything runs directly in the browser.

No account or backend is required.

---

## Why I made it

When I started working more seriously with UAV hardware and UAV security, I realised that understanding individual components was not enough.

A motor may be perfectly fine on its own but still be a poor choice for a particular battery and propeller.

A telemetry radio may work correctly but still have a weak link budget because of antenna placement or terrain.

A flight controller may have enough processing power but not enough UARTs for the GPS, receiver, telemetry radio, VTX and other peripherals I want to connect.

The useful questions are usually about how the parts interact.

That is the idea behind SkyForged.

Instead of only listing specifications, I wanted a place where I could learn the theory, do the calculations and then use that information while planning a real system.

---

## What is inside

### Academy

A starting point for someone who is still learning how drone systems fit together.

It covers terminology, hardware, electronics, radios, firmware and basic flight concepts in a sequence instead of assuming that the reader already knows the vocabulary.

### Anatomy

An interactive exploded view of an FPV drone.

The purpose is simple: identify each major component, understand where it sits in the aircraft and understand what job it performs.

### Blueprint

This is the part I use before selecting hardware.

It explains the calculations and reasoning behind choices such as:

* thrust-to-weight ratio
* motor KV and battery voltage
* propeller selection
* ESC requirements
* battery sizing
* current and power requirements
* hardware constraints

The goal is to calculate first and buy later.

### Model Builder

The Builder lets me assemble a possible UAV configuration from the component dataset and check some of the relationships between the selected parts.

Current checks include things such as mounting compatibility, voltage limits, propeller/frame size, UART requirements and estimated aircraft weight.

It also calculates a basic build summary including component count, estimated weight and estimated cost.

The component dataset currently contains more than 3,800 records across different UAV hardware categories.

The database is still being cleaned and expanded, so it should be treated as a planning dataset rather than an authoritative product catalogue.

### RF Tools

A set of small calculators for the RF side of a drone system.

Current tools include calculations for:

* FPV channel planning
* harmonics
* radio link budgets
* estimated range
* Fresnel zones
* antenna element length
* frequency lookup
* VTX configuration
* other radio-related checks

I added these because RF problems are easy to underestimate until a drone is actually in the air.

### PID and Tuning

This section is meant to connect flight behaviour with possible mechanical, filtering and controller problems.

Instead of presenting PID values as magic numbers, I wanted to show the relationship between the aircraft, vibration, filters and controller response.

### Drone Integration Handbook

The Handbook contains the longer technical notes behind the project.

Topics currently include:

* RC links
* telemetry and command links
* video links
* RF fundamentals
* antennas
* link budgets
* Betaflight
* iNav
* ArduPilot
* PX4
* MSP
* MAVLink
* UART planning
* pre-flight checks
* Blackbox logs
* PID tuning
* companion computers
* mesh communication
* system integration

My main interest here is the point where embedded systems, communication networks and UAV security start overlapping.

### Platform Reference

A small reference section for studying different commercial, Indian and specialised UAV platforms.

This part is still being expanded. I would rather keep a smaller dataset that I can verify than claim hundreds of platforms without reliable specifications.

### Airspace Reference

SkyForged also contains an experimental map for understanding the idea of red, yellow and green operating zones.

The current map uses simplified airport-distance calculations for educational purposes. It is **not an official DGCA airspace map and must not be used as flight authorisation**.

For an actual flight in India, the current official DGCA/Digital Sky information should always be checked independently.

### Operations

The operations section collects calculations, checklists and field references that are more useful when preparing or testing an aircraft than when studying the theory.

---

## How it is built

I deliberately kept the project technically simple.

The main application uses:

* HTML
* CSS
* JavaScript
* Leaflet for interactive maps
* GitHub Pages for deployment

There is no application server and no user database.

Most of the calculations happen locally in the browser.

The project structure is roughly:

```text
skyforged/
│
├── index.html
├── academy.html
├── anatomy.html
├── blueprint.html
├── builder.html
├── handbook.html
├── maps.html
├── ops.html
├── pid.html
├── platforms.html
├── tools.html
│
├── css/
│
├── js/
│   ├── database.js
│   ├── builder.js
│   ├── tools.js
│   ├── maps.js
│   ├── platforms.js
│   └── ...
│
└── assets/
```

---

## Running it locally

Clone the repository:

```bash
git clone https://github.com/Saitanveesh/skyforged.git
cd skyforged
```

You can then serve it using any simple local HTTP server.

For example, with Python:

```bash
python -m http.server 8000
```

Open:

```text
http://localhost:8000
```

---

## Current status

SkyForged is a work in progress.

Some parts are already useful to me, while others are still experimental.

In particular:

* component specifications and prices can change
* some component records still need manual verification
* compatibility checks are not a substitute for manufacturer documentation
* calculated RF range is theoretical and real environments can behave very differently
* the platform database is still small
* the airspace map is an educational reference, not an official flight-planning source

I am keeping these limitations visible because I want the project to become more accurate over time rather than appear more complete than it actually is.

---

## Where I want to take it

The next step is not simply adding more pages.

I want to improve the quality of the underlying engineering data.

That includes:

* verifying component specifications against manufacturer sources
* improving electrical and mechanical compatibility checks
* adding better propulsion calculations
* connecting motor, propeller and battery data
* improving RF modelling
* expanding verified UAV platform information
* adding more real build examples
* documenting actual test results
* improving the UAV security and communication sections
* separating calculated values from measured values

Eventually I want SkyForged to become a practical reference that I can use alongside my own UAV builds and research.

---

## About me

I am Sai Tanveesh.

My main area of interest is cybersecurity, with a growing focus on UAV systems, embedded hardware and communication security.

A large part of my work involves understanding what happens between the different layers of a drone: the flight controller, sensors, radio links, telemetry, companion computers and ground station.

SkyForged grew out of that work.

Rather than keeping my calculations, notes and references scattered across different folders, I started putting them into one system.

This repository is that system.

---

**Built and maintained by Sai Tanveesh**

GitHub: https://github.com/Saitanveesh
