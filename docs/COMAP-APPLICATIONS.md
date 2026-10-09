# ComAp application guide research

Reviewed 9 October 2026, Asia/Jakarta.

## Owner brief and implementation

The owner supplied screenshots of ComAp’s Applications navigation and asked for detailed application explanations because product-module pictures alone do not explain the use case. The ComAp guide now leads with three application groups before the existing six product-family sections. It covers the 18 categories in the screenshots plus a dedicated generator synchronisation/load-sharing application, for 19 explanations in total.

Each explanation contains a short purpose, typical system, control functions, example product families, selection inputs and a manufacturer reference. Native details/summary sections keep the long guide navigable; the first application in each group is initially open. Group links, a primary applications hero button, product links and application deep links support navigation. CSS retains Araya’s orange/charcoal/white typography and flat section layout. Three real manufacturer diagrams complement the unchanged product photographs; full-size image links support closer reading.

This is an original summary of manufacturer applications, not a claim that Araya has completed every category, holds stock of every model or promises every feature. The page directs visitors to confirm product selection, configuration and agreed supply/integration scope with Araya. Application-specific families such as InteliNeo, InteliSys Gas, InteliBifuel and InteliMains are examples referenced from manufacturer sources, not added inventory listings.

## Important research distinctions

- Controller families are configurable but have different roles and limits. Do not describe one generic module as supporting every application.
- Engine supervision, AC generator paralleling, DC source coordination and electric propulsion are explained separately. DC architecture depends on conversion equipment; AC synchronisation language must not imply directly synchronising a DC bus.
- Emergency generation has a defined separate arrangement in the marine PMS reference. Do not imply every emergency generator belongs to normal load-sharing control.
- Datacentre redundancy and availability are system design matters; a controller does not confer a Tier rating. No fixed start-time or uninterrupted-transfer guarantee is copied.
- Bi-fuel/hydrogen applications require dedicated fuel hardware, protection and engine review. Standard generator controls alone do not convert the fuel system. No savings or emissions percentage is promised.
- BESS control coordinates battery management (BMS), power conversion (PCS) and auxiliaries; site-level EMS has a wider coordination role.
- SCADA is site visualisation and configured control; WebSupervisor covers connected fleet/cloud monitoring with access, connectivity and subscription dependencies.
- The current **Energy Market Integration** page explicitly restricts Spot Price Dispatch availability to **Australia and Singapore**. The application entry states this limit and does not offer it as an Indonesian tariff service.

## Primary sources

All 18 application pages and the existing InteliGen 500 G2 product reference were read directly from the official ComAp website. Research extraction is retained locally as `design/comap-application-research.json`; it is not republished wholesale. Summaries are written in original wording.

| Group | Application | Official reference |
| --- | --- | --- |
| Marine | AC / DC power management | [ComAp source](https://www.comap-control.com/application-areas/marine/ac-dc-power-management/) |
| Marine | Engine control | [ComAp source](https://www.comap-control.com/application-areas/marine/engine-control/) |
| Marine | Emissions reduction | [ComAp source](https://www.comap-control.com/application-areas/marine/emission-reduction/) |
| Marine | Propulsion control | [ComAp source](https://www.comap-control.com/application-areas/marine/propulsion-control/) |
| Power generation | Standby & automatic mains failure | [ComAp source](https://www.comap-control.com/application-areas/power-generation/standby/) |
| Power generation | Prime power | [ComAp source](https://www.comap-control.com/application-areas/power-generation/prime-power/) |
| Power generation | Generator synchronisation & load sharing | [ComAp source](https://www.comap-control.com/products/controllers/paralleling-gen-set-controllers/inteligen/inteligen-500-g2/) |
| Power generation | Hybrid power generation | [ComAp source](https://www.comap-control.com/application-areas/power-generation/hybrid/) |
| Power generation | Mission-critical power | [ComAp source](https://www.comap-control.com/application-areas/power-generation/mission-critical/) |
| Power generation | Datacentres | [ComAp source](https://www.comap-control.com/application-areas/power-generation/mission-critical/datacenters/) |
| Power generation | Combined heat & power (CHP) | [ComAp source](https://www.comap-control.com/application-areas/power-generation/chp/) |
| Power generation | Bi-fuel & hydrogen | [ComAp source](https://www.comap-control.com/application-areas/power-generation/bifuel-and-hydrogen/) |
| Power generation | Fuel cells | [ComAp source](https://www.comap-control.com/application-areas/power-generation/fuel-cells/) |
| Power generation | Rental, telecom & light towers | [ComAp source](https://www.comap-control.com/application-areas/power-generation/rental-telecom-and-light-towers/) |
| Smart energy management | Hybrid energy management | [ComAp source](https://www.comap-control.com/application-areas/smart-energy-management/hybrid-energy-management/) |
| Smart energy management | Energy storage system control | [ComAp source](https://www.comap-control.com/application-areas/smart-energy-management/energy-storage-system-control/) |
| Smart energy management | Fleet management | [ComAp source](https://www.comap-control.com/application-areas/smart-energy-management/fleet-management/) |
| Smart energy management | SCADA | [ComAp source](https://www.comap-control.com/application-areas/smart-energy-management/scada/) |
| Smart energy management | Energy market integration | [ComAp source](https://www.comap-control.com/application-areas/smart-energy-management/energy-market-integration/) |

## Diagram provenance

Manufacturer example system diagrams are stored unchanged as local WebP responses. They are not Araya design drawings, wiring instructions or installation photographs. Captions credit ComAp and link to the corresponding application page. Each image has explicit intrinsic dimensions, descriptive alt text and lazy loading. Existing marketing-permission confirmation before production remains recorded in CONTENT-SOURCES.md.

| Asset | Application source | Exact download |
| --- | --- | --- |
| `comap-application-marine-pms.webp` | [Marine AC PMS example](https://www.comap-control.com/application-areas/marine/ac-dc-power-management/) | [Official asset](https://imgproc.comap-control.com/Local/mediacontainer/comap/media/marine/comap_ac_pms_marine_scheme_web.png?f=WebP&w=900&h=900) |
| `comap-application-standby.webp` | [Single-generator standby example](https://www.comap-control.com/application-areas/power-generation/standby/) | [Official asset](https://imgproc.comap-control.com/Local/mediacontainer/comap/media/applications/power%20generation/standby/comap-standby-power-example.png?f=WebP&w=900&h=900) |
| `comap-application-hybrid.webp` | [Grid-connected hybrid microgrid example](https://www.comap-control.com/application-areas/smart-energy-management/hybrid-energy-management/) | [Official asset](https://imgproc.comap-control.com/Local/mediacontainer/comap/media/widgets/application%20example/asset-3microgrid_on_grid.png?f=WebP&w=900&h=900) |

Three diagram assets total 128,048 bytes. Normal HTML builds require no manufacturer requests; optional refetch helper includes their exact URLs. Broader claims about production SEO rankings, Lighthouse scores or Araya project history are not inferred from this update.
