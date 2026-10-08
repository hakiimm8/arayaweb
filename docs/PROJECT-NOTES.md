# Araya project notes

Recorded 8 October 2026, Asia/Jakarta. Historical observations from the project session; not a fresh audit or ongoing monitoring.

## Purpose and decisions

Improve PT Araya Internusa's website and discoverability for Noris and ComAp in Indonesia. The owner states the distributor relationship; authorization/exclusivity, specific supplied models and support commitments remain unverified.

The owner selected the CURRENT LIVE website style: orange, charcoal and white, Space Grotesk, original logo and project photographs. The earlier navy mockups are superseded.

- Production: https://arayainternusa.co.id/araya/
- Preview: https://hakiimm8.github.io/arayaweb/
- GitHub Pages is a static review preview. Production WordPress is unchanged.
- VM staging is optional; not used for this release.
- No pull_request or pull_request_target Actions triggers. Publish on push/main or manual dispatch. No skip-CI merge instructions.

## Recorded production audit

Single Lighthouse 13.5.0 lab runs on 8 October 2026, approximately 08:30 Jakarta. Not field data or ranking measurements. Temporary raw reports were not retained; rerun and retain reports for future comparisons.

| Category | Mobile | Desktop |
| --- | ---: | ---: |
| Performance | 37 | 76 |
| Accessibility | 87 | 87 |
| Best practices | 96 | 96 |
| SEO | 83 | 83 |

Mobile LCP was 11.90 s, TBT 860 ms and CLS 0.089. The LCP element was cookie-notice text, so the observation includes the cookie-overlay layout.

Main findings:

- Weak Noris/ComAp positioning and no dedicated brand pages found in the original audit.
- Generic homepage title, long description, headings/image alternatives needing review, placeholder structured-data properties.
- Indexable demo/sample pages in the sitemap.
- Large external slider images, many CSS/JS requests, cross-origin errors and theme-demo asset references.
- Footer email/phone destinations did not match their displayed business details.
- Domain root redirected temporarily (302) to /araya/. Keep /araya/ initially; treat a root migration separately.
- Live loading overlay blocked exact screenshot comparison during preview work.

## Preview completed

- Homepage plus distinct Noris and ComAp pages with descriptive titles/headings and contact routes.
- Responsive layout/menu, Escape close/focus return, keyboard focus, reduced-motion support, optimized local images/font.
- Corrected preview contact destinations to match the original displayed details; calling/mail delivery not tested.
- Relevant orange text/button fill darkened to #cb4800 after independent accessibility review (approximately 4.70:1 contrast against white).
- Main vessel/control-room images reduced from approximately 2.9 MB combined to 234 KB. File-size reduction is not a measured production performance improvement.
- Desktop/mobile, deployed nested routes, metadata, image alt text, local assets/fragments and public artifact exclusions checked.
- Initial reviewed preview commit: a0a1dc6; Pages workflow run 37751836932 succeeded.

Only public/ is deployed. Preview uses noindex,nofollow. This does not test WordPress/Elementor/PHP, production hosting, form delivery or search rankings. Preservation follows observed live styling and original assets; exact pixel fidelity to the live page was not verified.

## Next steps

Contact update, 8 October 2026: the owner supplied WhatsApp +62 81326396262 and requested its publication. Added the displayed WhatsApp number and direct https://wa.me/6281326396262 link to the shared contact section on all three preview pages. No WhatsApp message was sent.

1. Review preview content and confirm distributor wording, supplied products, support scope and contacts.
2. Obtain WordPress administrator/database access and verified files + database backup before production edits.
3. Apply reviewed content/settings and custom code selectively to WordPress; avoid overwriting a current production database with an older copy.
4. Clean up demo URLs, titles/descriptions, schema, headings, internal links and sitemap.
5. Optimize production assets/scripts and investigate cookie/preloader issues.
6. Recheck production contact paths/crawlability/mobile rendering; rerun comparable Lighthouse measurements and retain evidence.

## Maintenance

Logo recreation, 8 October 2026: the original PNG had an opaque #ee5c03 background, while the header block used #ff6200. At the owner's request, recreated the logo as a transparent SVG with an outlined two-line wordmark and a clean interpretation of the circular monogram. Header orange matched to #ee5c03. Original PNG retained; header, footer and Organization logo use araya-logo-v2.svg. Text is converted to paths for font-independent display. The vector is a recreation, not an exact trace or a source trademark master. Rebuild with Windows PowerShell tools/build_logo.ps1 (Arial Bold outlines via System.Drawing). Two ImageGen attempts were rejected because their transparency introduced rough artifacts; neither was published.

Project experience update, 8 October 2026: the owner supplied the figure of more than 1,500 projects and coverage including Sumatra, Jawa, Kalimantan, Sulawesi, and Papua. The homepage now presents “1,500+ projects across Indonesia” and these five regions. This is an owner-provided aggregate; no per-region counts or individual project/client claims were added.

Brand emphasis update, 8 October 2026: at the owner's request, homepage and brand pages now highlight Noris Group GmbH instruments/sensors (speed, temperature, pressure, indicators and signal processing), and ComAp engine control, power management and load sharing. Manufacturer descriptions were checked against the sources below. Exact model/feature compatibility and availability remain subject to confirmation; no blanket feature or authorization claim was added.

Edit shared copy/templates in tools/build.py and regenerate with `python tools/build.py`. Check the artifact with `python tools/check.py` and `node --check public/assets/site.js`, then inspect changed desktop/mobile views.

Full technical findings and handoff notes are stored in the owner's local workspace. This public summary excludes hosting account information, local machine paths, credentials, databases and backups.

## Sources

- https://www.noris-group.com/industries/shipbuilding
- https://www.noris-group.com/industries/machinery-and-equipment
- https://www.comap-control.com/products/controllers/
- https://uk.comap-control.com/application-areas/marine/engine-control/
- https://www.comap-control.com/products/extended-features/extended-feature-load-sharing-power-management/
- https://developer.wordpress.org/advanced-administration/upgrade/migrating/
- https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
