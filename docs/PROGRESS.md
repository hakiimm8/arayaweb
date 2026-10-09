# Progress and release record

Updated 9 October 2026, Asia/Jakarta. Historical session evidence; no ongoing monitoring or fresh production audit is implied.

## Current release

- **Preview:** https://hakiimm8.github.io/arayaweb/
- **Website-content commit:** [`de91d39c7a1190b758179105f85349bc40ab5ced`](https://github.com/hakiimm8/arayaweb/commit/de91d39c7a1190b758179105f85349bc40ab5ced).
- **Deployment:** [Pages run 37868242535](https://github.com/hakiimm8/arayaweb/actions/runs/37868242535), succeeded.
- **Production:** https://arayainternusa.co.id/araya/ remains unchanged.
- **Design:** original Araya artwork and orange/charcoal/white Space Grotesk styling.
- **Publication:** only `public/`; all five pages intentionally `noindex, nofollow`.

| Page | Implemented scope |
| --- | --- |
| [Home](https://hakiimm8.github.io/arayaweb/) | Company, services, brand entry points, owner-supplied 1,500+ total and Indonesian regions, project-scope summaries, contacts. |
| [Marine](https://hakiimm8.github.io/arayaweb/marine/) | Eight scope areas spanning electrical/mechanical work, monitoring, control, navigation/manoeuvring and retrofit. |
| [Industrial](https://hakiimm8.github.io/arayaweb/industrial/) | Five scope areas: machinery, cranes, panels/motor controls, PLC/HMI/SCADA/instrumentation and generator control. |
| [Noris](https://hakiimm8.github.io/arayaweb/noris/) | Seven product areas: speed, temperature, pressure, instruments, signal processing, noriMos and noriStar. Brand profile, product pictures in every family, applications, references, enquiry brief and FAQs. |
| [ComAp](https://hakiimm8.github.io/arayaweb/comap/) | Six product areas: engine control, paralleling/load sharing, marine PMS, single-generator control, InteliSCADA and WebSupervisor. Brand profile, product pictures in every family, applications, references, enquiry brief and FAQs. |

WhatsApp is owner-supplied +62 81326396262, linked as https://wa.me/6281326396262. No enquiry message was sent during checks.

## Release history

The initial entries were recorded on 8 October 2026; subsequent navigation work is listed below them. Commits/runs identify the evidence more precisely than inferred times.

| Commit | Change | Deployment evidence |
| --- | --- | --- |
| `1102b80` → `a0a1dc6` | Existing-style homepage and initial brand pages; accessible orange contrast and sticky navigation correction. | [37751836932](https://github.com/hakiimm8/arayaweb/actions/runs/37751836932), succeeded for `a0a1dc6`. |
| `1f771a3` | Initial public audit/handoff documentation. | Documentation update; page-content baseline unchanged. |
| `c5dcb49` | Owner WhatsApp added to shared contact section. | [37754660622](https://github.com/hakiimm8/arayaweb/actions/runs/37754660622), succeeded. |
| `1465575` | Noris instruments/sensors; ComAp engine control/PMS/load sharing; owner project count and geography. | [37756296482](https://github.com/hakiimm8/arayaweb/actions/runs/37756296482), succeeded. |
| `2b45cc4` | Recreated SVG logo. **Rejected by owner and superseded; do not restore.** | [37775308617](https://github.com/hakiimm8/arayaweb/actions/runs/37775308617), succeeded historically. |
| `5495ed6` | Original transparent logo restored unchanged, original lockup proportions corrected; rejected SVG removed. | [37778054483](https://github.com/hakiimm8/arayaweb/actions/runs/37778054483), succeeded. |
| `7f169d7` | Marine/industrial pages, homepage scopes, initial product portfolios/images, CSS content-hash URL. | [37781023786](https://github.com/hakiimm8/arayaweb/actions/runs/37781023786), succeeded. |
| `e866993` | Researched dedicated brand guides, product indexes, profiles, applications, enquiry briefs and accessible FAQs. | [37782440114](https://github.com/hakiimm8/arayaweb/actions/runs/37782440114), succeeded. |
| `b34794b` | Consolidated documentation index, release history and current-state notes. | Documentation-only; public artifact unchanged. |
| `030a205` | Separate Noris/ComAp header links and homepage buttons. Header arrangement superseded by the following owner request; separate homepage buttons retained. | [37866938106](https://github.com/hakiimm8/arayaweb/actions/runs/37866938106), succeeded; published navigation checks passed. |
| `de91d39` | Eleven new manufacturer images; all 13 brand product sections illustrated, credited and lazy loaded. | [37868242535](https://github.com/hakiimm8/arayaweb/actions/runs/37868242535), succeeded; published desktop/mobile image checks passed. |
| `b51bc47` | Brand Partners dropdown containing separate Noris/ComAp links; header/footer links generated from shared brand data. | [37867253415](https://github.com/hakiimm8/arayaweb/actions/runs/37867253415), succeeded; published dropdown checks passed. |

The early navy design concepts and two generated logo attempts were not used in the current site. Preserve the restored original symbol and lettering.

## Verification evidence

| Check | Recorded result |
| --- | --- |
| Build/static audit | `python tools/build.py` and `python tools/check.py` passed; five routes, local assets/fragments, metadata, one H1, alt text, font, publication exclusions and no-PR workflow checked. |
| JavaScript / whitespace | `node --check public/assets/site.js` and `git diff --check` passed on the website release. |
| Brand layouts | Local and published pages checked at 1280×900 and 390×844 in separate headless Edge via bundled Playwright; Browser plugin/skill unavailable. |
| Runtime/assets | No page/console/HTTP errors, broken images or horizontal overflow observed in the final brand checks. Original logo and product photographs loaded. |
| Interaction | Homepage → Noris → ComAp passed; product-index anchors reached content below sticky header; FAQs opened/closed with Enter; WhatsApp destinations matched owner number. |
| Correction | Mobile application text initially occupied a narrow column. Grid placement fixed; repeat checks confirmed readable 299px content width at 390px. |
| Earlier service release | All five routes checked at desktop/mobile widths; homepage → marine → ComAp and mobile menu Escape closing passed. |
| Brand Partners dropdown | Local and published checks across all five routes at 1280px, 1024px and 390px passed: destinations, opening by click/Enter, Escape focus return, outside-click closing, mobile close after navigation, independent homepage buttons and no-JavaScript navigation. No overflow/page/console/HTTP errors. |

Local evidence is retained as `brand-guides-published-{noris,comap}-{1280,390}.png` and corresponding product/application/FAQ screenshots. Earlier five-route evidence uses `project-details-published-`. Full local verification notes and scripts are retained by the owner, outside this repository.

Latest navigation screenshots use `brand-dropdown-published-{1280,1024,390}.png`. The owner selected Brand Partners for future expansion; Noris and ComAp remain individual entries and dedicated pages. Native details/summary supplies the dropdown, with scripted closing/focus behaviour. JavaScript URLs now include a content hash as well as CSS URLs. Follow [Brand maintenance](BRAND-MAINTENANCE.md) to add a future partner; homepage featured cards are maintained separately.

## Evidence limits and open work

- Original production Lighthouse lab baseline: performance mobile 37/desktop 76; SEO 83 on both. Raw reports were not retained. No new production speed or ranking measurement is claimed.
- Static preview checks do not validate WordPress/Elementor editing, PHP/database behaviour, mail delivery, calling, production hosting or every browser/viewport.
- Distributor relationship, 1,500+ project total and geographic coverage are owner statements. Product portfolios are manufacturer examples, not confirmed stock, blanket approvals, exclusivity or completed Araya installations. Exact sources and image provenance are in [Content sources](CONTENT-SOURCES.md).
- Before production rollout: review copy/product scope, contact delivery and image permissions; establish verified backup and administrator/database access; apply selected content/settings changes; address demo URLs, metadata/schema/sitemap, contact destinations and performance findings from [Project notes](PROJECT-NOTES.md).
- Keep `/araya/` for the first release; review redirect or domain-root migration separately. Rerun comparable production audits and retain reports after deployment.

## Maintenance and publishing

Edit shared pages in `tools/build.py`, researched brand data in `tools/brand_profiles.py`, brand rendering in `tools/brand_pages.py`, styling in `public/assets/site.css` and menu behaviour in `public/assets/site.js`. Rebuild generated HTML after source changes. Manufacturer image refetch is optional via `tools/fetch_brand_assets.py`.

Validate the changed desktop/mobile flow, then publish the preview by pushing the reviewed change to `main`. Pages deploys on default-branch pushes or manual dispatch; no `pull_request` or `pull_request_target` triggers. Documentation-only pushes can redeploy the same public artifact. Record website-content commit separately from later documentation commits. Never include skip-CI instructions in merge commits.

For a preview rollback, revert the unwanted site commit on `main`, push, and verify the resulting Pages deployment. Select a known accepted release; the recreated-logo commit is rejected. Production rollback is separate and requires its own verified files/database backup.

After each change, update this record with request, sources, decision, affected routes/files, checks, defects/corrections, commit/run and pending work. Keep historical entries labelled when superseded.


## Product pictures — 9 October 2026

Owner requested more pictures on the Noris and ComAp pages. Added six Noris assets (marine temperature probes, pressure transmitter, noriMeter instrument, signal-processing devices, noriMos display and noriStar controls) and five ComAp assets (InteliDrive 700 Marine, InteliGen 1000 Marine, InteliLite 4 AMF 25, InteliSCADA and WebSupervisor). Each of the 13 product families now has a captioned, manufacturer-linked picture; the existing speed-sensor and InteliGen 500 G2 hero assets are reused in their product sections. New WebP assets total 285,534 bytes; below-hero images use lazy loading, async decoding, explicit dimensions and contain fit. Existing design, original logo, menu, contacts and preview noindex retained.

Local static/build/JavaScript/whitespace checks passed. Headless Edge via bundled Playwright checked both brands at 1280×900 and 390×844: all 26 product figure checks loaded, intrinsic dimensions matched, alt text and linked credits present, contain fit and lazy loading applied, no overflow or page/console/HTTP errors. Brand Partners navigation and keyboard Escape focus return passed. Screenshot review confirmed readable desktop/mobile product layouts. Local evidence: `brand-pictures-local-*.png`, `brand-pictures-local.json`, `check-brand-pictures.cjs` and manufacturer contact sheet, retained outside the public repository. Published release verification is recorded in the current-release entry when deployed. No new Lighthouse measurement or performance-score improvement is claimed.

Published verification: Pages run 37868242535 succeeded for de91d39. The same image checks passed on GitHub Pages at 1280x900 and 390x844: 26 loaded figures, correct dimensions/alt/source credits, no overflow or runtime/HTTP errors, and Brand Partners navigation/focus passed. Evidence: `brand-pictures-published-*.png` and `brand-pictures-published.json`, stored locally.
