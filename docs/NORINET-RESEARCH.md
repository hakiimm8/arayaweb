# NORINET brochure review

Reviewed 9 October 2026, Asia/Jakarta. This is a content research note; no website section or production change is included in this documentation update.

## Sources and version

- Owner-supplied two-page brochure, supplied filename `FL-NORINET_V01.01-EN.pdf`. Its printed footer identifies **FL-NORINET-EN V01.02, 10/2019**; use the printed revision when describing its age. Original attachment and rendered pages are retained in the owner's local workspace, outside this public repository.
- [Current Noris remote access and telemetry page](https://www.noris-group.com/products-and-systems/maritime-system-solutions/remote-access-and-telemetry), checked on the review date.

Both brochure pages were extracted and visually inspected. The screenshots show manufacturer examples, not Araya installations, customers or measured results.

## Plain-language explanation

NORINET is Noris's vessel and fleet data platform. An onboard interface unit collects and processes information from machinery monitoring, alarm systems and navigation equipment. It transfers that information over the vessel's internet connection to an onshore cloud service. Staff can use a web browser to review vessel status, trends and reports across one or more ships.

Conceptual flow: **Vessel sensors / AMCS / navigation → onboard interface unit → vessel internet → cloud → office or mobile browser.**

| Area | What the supplied brochure describes |
| --- | --- |
| Machinery monitoring | Engine speed, load, alarms and operating measurements, subject to connected signals. |
| Navigation overview | Position, course, speed and other available navigation measurements. |
| Performance analysis | Fuel consumption, power and energy-flow views; hull/propeller and efficiency examples. |
| Reporting | Voyage, fuel and power reports using collected historical information. |
| Fleet management | Several vessels in a shared overview and permissions for different users. |
| Integration | NORICAN, Modbus and NMEA connections shown in the architecture; CSV export and API access. |
| Interrupted connectivity | Local data caching is described; shore-side live visibility depends on connectivity. |

The brochure describes MQTT transport and app-based customisation. Its GPRS/GSM and SKY DSL examples are historical architecture details, not a statement that current installations are restricted to those connections. Do not infer retention duration, buffer capacity, subscription terms, cybersecurity configuration or compatibility with every third-party device.

## Current manufacturer cross-check

The current Noris page describes two functions: remote access for service/support, and cloud collection of onboard monitoring/navigation data for analysis. It lists VPN remote connections, MQTT data transmission, browser dashboards, alarm/event history, charts, customised reports, vessel location and REST API integration. Current descriptions support a retrofit discussion, but actual interfaces and project requirements must be confirmed.

MQTT is a messaging protocol; security depends on the configured connection and access controls. Remote service access is not evidence that an operator can remotely steer or start a vessel. Do not present this as a substitute for onboard alarm, protection or navigation systems, or claim automatic failure prediction or guaranteed fuel savings.

## Relevance to Araya and proposed website wording

This would fit an additional **Remote monitoring & fleet performance** product area on the Noris page, linked from AMS/system retrofit work. The existing page currently covers seven other product families. No NORINET supply history, installed base, stock, exclusive relationship or implementation commitment has been established for Araya.

Suggested concise copy, subject to the agreed product scope:

> noriNet connects onboard monitoring and navigation data to a cloud-based view of your vessel or fleet. Explore remote diagnostics, operating trends, voyage reports and performance analysis with Araya. Integration depends on the available measurements, system interfaces and vessel connectivity.

Enquiry inputs: existing AMS/controller models, signal and protocol lists, vessel count, internet arrangements, required dashboards/reports, access roles and the intended service scope. Quantitative fuel/efficiency analysis also requires suitable measurement data and a defined calculation method; screenshots alone do not establish accuracy or savings.
