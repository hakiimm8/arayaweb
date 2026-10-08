# Araya design preview

Static review preview for PT Araya Internusa, preserving the existing website's orange/charcoal/white industrial styling and Space Grotesk typography.

Preview: https://hakiimm8.github.io/arayaweb/

Saved audit findings, design decisions, verification results and next steps: [Project notes](docs/PROJECT-NOTES.md).

## Files

- `public/`: the complete published site, with home, Noris and ComAp pages.
- `tools/build.py`: shared HTML template and page copy. Run `python tools/build.py` after editing.
- `.github/workflows/pages.yml`: publishes `public/` on push to main or manual dispatch. No PR triggers.

To preview locally, serve `public/` with a static HTTP server. WordPress and PHP are not required for this preview.

## Scope and sources

This is a public design preview with noindex,nofollow metadata. The production WordPress site remains at https://arayainternusa.co.id/araya/. Preview hosting performance does not represent production WordPress performance.

Existing Araya logo, photographs, company history, and displayed business contacts come from the owner's supplied website files and live site. Email/phone destinations have been aligned with their displayed labels; deliverability has not been tested. No enquiry is automatically sent. Some service-detail links intentionally open the existing production pages.

The owner states that Araya distributes Noris and ComAp in Indonesia. Authorization, exclusivity, specific product availability, warranties and certifications are not asserted.

Manufacturer application sources checked 2026-10-08:

- https://www.noris-group.com/industries/shipbuilding
- https://www.comap-control.com/products/controllers/

Space Grotesk is distributed under the SIL Open Font License; see `public/assets/fonts/OFL.txt` and https://github.com/google/fonts/tree/main/ofl/spacegrotesk.

WordPress files, database exports, private configuration, backups and logs are not part of this repository or deployment artifact.
