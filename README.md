# Guangwei Gao — Academic Homepage

**Website:** https://ggw1995.github.io/

Built with the official [al-folio](https://github.com/alshedivat/al-folio) template and published with GitHub Pages.

## Updating the website

All current website content is in [`_homepage/`](./_homepage/):

| File | Content |
| --- | --- |
| [`about.md`](./_homepage/about.md) | Introduction, research interests, and contact |
| [`publications.md`](./_homepage/publications.md) | Publications and preprints |
| [`bio.md`](./_homepage/bio.md) | Academic experience, teaching, and talks |
| [`CV.pdf`](./_homepage/CV.pdf) | Downloadable CV |
| [`config.yml`](./_homepage/config.yml) | Site settings |
| [`socials.yml`](./_homepage/socials.yml) | Contact icons and links |

Saving changes in that folder automatically runs **Deploy al-folio**, checks the generated pages and local links, and publishes the new website.

The template is pinned to al-folio v0.16.3, commit `b5ecd1a6bd3f94474a87710c76fd81cf9f0e0fa2`, for reproducible builds. See [`_homepage/README.md`](./_homepage/README.md) for implementation details.

The former template's `contents/`, `static/`, and root `index.html` are kept for rollback only; they are not published by the current workflow. The old template's license remains in `LICENSE`; al-folio retains its upstream MIT license.
