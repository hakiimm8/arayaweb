# Araya design preview

Static review preview for PT Araya Internusa, preserving the existing website's orange/charcoal/white industrial styling and Space Grotesk typography.

Preview: https://hakiimm8.github.io/arayaweb/

Saved audit findings, design decisions, verification results and next steps: [Project notes](docs/PROJECT-NOTES.md).

Start with the [documentation index](docs/README.md), [progress/release record](docs/PROGRESS.md) and [content sources](docs/CONTENT-SOURCES.md). Latest website-content release is `de91d39`; later documentation commits leave its public artifact unchanged.

## Files

- `public/`: the complete published site, with home, marine, industrial, Noris and ComAp pages.
- `tools/build.py`: shared HTML template and page copy. Run `python tools/build.py` after editing.
- `tools/brand_profiles.py` and `tools/brand_pages.py`: researched brand content and dedicated brand-page layout.
- `.github/workflows/pages.yml`: publishes `public/` on push to main or manual dispatch. No PR triggers.

To preview locally, serve `public/` with a static HTTP server. WordPress and PHP are not required for this preview.

The **Brand Partners** dropdown and footer brand links are generated from `BRANDS` in `tools/brand_profiles.py`. See [adding a future partner](docs/BRAND-MAINTENANCE.md). The homepage has individual Noris and ComAp buttons.

## Scope and sources

This is a public design preview with noindex,nofollow metadata. The production WordPress site remains at https://arayainternusa.co.id/araya/. Preview hosting performance does not represent production WordPress performance.

Existing Araya logo, engineering photographs, company history, and displayed business contacts come from the owner's supplied website files and live site. Email/phone destinations have been aligned with their displayed labels; deliverability has not been tested. No enquiry is automatically sent. Service and brand links stay within the preview, with separate links to manufacturer references and the current website.

Marine and industrial pages describe project scopes provided by the owner and the existing service pages. They are capability descriptions, not invented named case studies. Product families, example models, and 13 manufacturer product images have source attribution in [Content sources](docs/CONTENT-SOURCES.md). Model availability and project suitability require discussion with Araya.

Dedicated Noris and ComAp guides include manufacturer background, a product-family index, application guidance, an Araya enquiry brief and accessible expandable FAQs. Noris covers seven product areas; ComAp covers six. These are Araya's local brand guides; manufacturer links lead to current product details and documents.

The owner states that Araya distributes Noris and ComAp in Indonesia. Authorization, exclusivity, specific product availability, warranties and certifications are not asserted.

Manufacturer application sources checked 2026-10-08:

- https://www.noris-group.com/industries/shipbuilding
- https://www.comap-control.com/products/controllers/

Space Grotesk is distributed under the SIL Open Font License; see `public/assets/fonts/OFL.txt` and https://github.com/google/fonts/tree/main/ofl/spacegrotesk.

WordPress files, database exports, private configuration, backups and logs are not part of this repository or deployment artifact.
