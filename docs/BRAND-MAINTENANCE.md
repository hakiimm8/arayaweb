# Adding a brand partner

The shared header uses a **Brand Partners** dropdown with separate Noris and ComAp links. Dropdown links, footer brand links and generated brand routes come from `BRANDS` in `tools/brand_profiles.py`. The homepage keeps separate Explore Noris / Explore ComAp buttons.

## Add a confirmed future partner

1. Add a new entry to `BRANDS` using an existing entry as the structure. Use a unique URL-safe key such as the confirmed brand's slug; its route becomes `/<key>/` under the GitHub project path.
2. Fill in the name, metadata, heading, profile, product families, applications, enquiry checklist, FAQs and relevant service connections. Use accurate Araya relationship wording and manufacturer sources. Adapt model and compatibility statements to the brand.
3. Set the `other` cross-brand link to an existing brand key, and provide its link label.
4. Add a permitted product image under `public/assets/images/` and specify its file, actual dimensions, alt text, source page and attribution. If useful, add its download to the optional `tools/fetch_brand_assets.py` helper. Do not generate or redraw manufacturer logos/products.
5. Run `python tools/build.py`. It generates the new page and adds its menu/footer link on every page. The renderer is shared in `tools/brand_pages.py`; no separate menu markup is required.
6. If the new brand should appear prominently on the homepage, add a card/button in `HOME` inside `tools/build.py`. Homepage featured cards/buttons are curated separately from the full partner menu.
7. Update [content sources](CONTENT-SOURCES.md), [project notes](PROJECT-NOTES.md) and [progress](PROGRESS.md). Record any unconfirmed inventory, approvals, service scope or image rights.
8. Run `python tools/check.py`, `node --check public/assets/site.js` and `git diff --check`. Check desktop/mobile dropdown behaviour, keyboard access, the new route, images, metadata, enquiry links and relative paths from nested pages before publishing.

## Dropdown behaviour

- Native HTML details/summary provides click and keyboard opening, including without JavaScript.
- Escape closes the dropdown and returns focus to its summary. On mobile, a further Escape closes the outer navigation.
- Outside clicks and focus moving out of the partner group close it. Choosing a link closes navigation.
- The mobile dropdown expands within the navigation; desktop uses an anchored panel.
- CSS and JavaScript URLs include content hashes so new markup gets matching changed assets.

There is no practical brand-count limit in the data model, but retest the dropdown height and mobile navigation when adding more entries. Add only confirmed partners and real content; no placeholder partner is included in the current menu.


## Product-section pictures

Each product entry can include an optional `image` dictionary: `file`, actual `width` and `height`, descriptive `alt`, and a short `caption`. Place the real manufacturer WebP file in `public/assets/images/`; the shared renderer adds a lazy-loaded figure below the family heading and credits the brand with a link to that product’s `source`. It contains the complete image without cropping or stretching. Example software screens must be described as examples. Keep download URLs in `tools/fetch_brand_assets.py` and provenance in `CONTENT-SOURCES.md`. Omit the image dictionary when no suitable image is available. Rebuild and check both desktop and mobile after changing images.
