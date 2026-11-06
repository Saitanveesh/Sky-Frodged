# Licensing and third-party notices

## SkyForged original code and documentation

The repository maintainer offers the **original SkyForged source code and original project documentation** under the [MIT License](LICENSE), copyright © 2026 Sai Tanveesh.

**This notice does not relicense third-party works.** Third-party libraries, data, images, icons or other assets retain their own copyrights and licenses. The provenance and redistribution rights of some included assets and component-data records have **not been independently documented**, so the MIT notice must **not** be interpreted as a blanket rights guarantee for all content under `assets/` or `js/database.js`.

A contributor who wants to redistribute the project as a complete package should first verify the permissions for each third-party asset and dataset involved. The maintainer can gradually add per-file provenance metadata and separate notices; see the [roadmap](docs/ROADMAP.md).

## Leaflet

The application loads **Leaflet** version 1.9.4 from an external CDN on certain pages.

- Project: https://leafletjs.com/
- Source and license: https://github.com/Leaflet/Leaflet/blob/main/LICENSE
- License: **BSD-2-Clause**
- Original copyright notice: Copyright © 2010–2026 Volodymyr Agafonkin; Copyright © 2010–2011 CloudMade.

This project's MIT license does not replace Leaflet's BSD-2-Clause terms. If you bundle Leaflet's source or binary files rather than loading them externally, retain the upstream notice and conditions.

## OpenStreetMap

Some pages request OpenStreetMap map tiles. OpenStreetMap contributors own the mapping data.

- Copyright and license information: https://www.openstreetmap.org/copyright
- OSM data: Open Database License (ODbL)
- Tile usage policy: https://operations.osmfoundation.org/policies/tiles/

Appropriate attribution and tile-use compliance remain required. The OpenStreetMap map background **does not supply official aviation restrictions or DGCA flight authorization**.

## Image assets and component dataset

Images in `assets/`, the existing UI illustrations, and information in `js/database.js` may have different origins. This audit did not establish their complete chain of ownership, source attribution, or redistribution permissions. Do not infer that an asset is freely redistributable merely because it is visible in this public repository.

If an asset's license cannot be verified, replace it with a verified original or properly licensed asset before distributing packaged copies.

## Reporting an attribution problem

Open a GitHub issue identifying the file, original author/source and applicable license, avoiding private information. The maintainer can then preserve the correct notice, replace the material or remove it as appropriate.
