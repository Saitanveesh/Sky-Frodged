# Security and responsible reporting

SkyForged is currently a static web application, not an authenticated service. It does not provide a flight-controller command link, remote administration or user accounts.

## Reporting a security issue

For a potentially sensitive issue, avoid publishing exploitable details or private data in a public issue. Contact the maintainer via an established private channel shown on their GitHub profile, or ask them privately for a reporting route. Do not attack third-party infrastructure or probe systems without authorization.

For non-sensitive defects such as broken links, client-side crashes and documentation corrections, use [GitHub Issues](https://github.com/Saitanveesh/Sky-Frodged/issues).

## Boundaries

The site may load Leaflet from a CDN and map tiles from an external provider. Users should review those providers' policies as appropriate.

Flight-safety and regulatory decisions must not depend on SkyForged calculator or map outputs alone.
