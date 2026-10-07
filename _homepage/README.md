# Guangwei Gao's academic homepage

The live site uses the official **al-folio v0.16.3** template, pinned to commit
`b5ecd1a6bd3f94474a87710c76fd81cf9f0e0fa2`.

Edit the files in this folder to update the website:

- `about.md`: biography, research interests, and contact details.
- `publications.md`: papers, publication status, and links.
- `bio.md`: appointments, education, teaching, and talks.
- `CV.pdf`: downloadable curriculum vitae.
- `socials.yml`: email, GitHub, and CV icons.
- `config.yml`: name, address, and site options.
- `prepare.py`: removes template examples and applies site content and styles.

The `Deploy al-folio` GitHub Actions workflow checks out the pinned official
template into a disposable directory, applies this folder, builds the site,
checks local links and page content, and publishes the result to GitHub Pages.
Only the generated `_site` directory is published. The former template files
in the repository root are retained as a backup and are not part of the live site.

Photos and news are currently disabled. To add a portrait later, copy your image
to `assets/img/` in `prepare.py` and enable the `profile` block in `about.md`.

The al-folio template is MIT licensed. Its original license is retained in the
template checkout. The textual content was prepared from Guangwei Gao's CV.
