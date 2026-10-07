"""Apply site-owned content to a clean, pinned al-folio checkout."""
from pathlib import Path
import shutil
import sys

content = Path(sys.argv[1]).resolve()
theme = Path(sys.argv[2]).resolve()
if theme == content or not (theme / "_layouts/about.liquid").is_file():
    raise SystemExit("Expected a separate al-folio template checkout")

# Remove the template's example content from the disposable build checkout.
for name in ["_pages", "_posts", "_news", "_projects", "_books", "_teachings", "_bibliography"]:
    path = theme / name
    if path.exists():
        shutil.rmtree(path)
    path.mkdir()
for name in ["audio", "html", "img", "json", "jupyter", "pdf", "plotly", "video"]:
    path = theme / "assets" / name
    if path.exists():
        shutil.rmtree(path)
    path.mkdir()
for path in (theme / "_data").iterdir():
    if path.is_file():
        path.unlink()

for name in ["about.md", "publications.md", "bio.md"]:
    shutil.copy2(content / name, theme / "_pages" / name)
shutil.copy2(content / "socials.yml", theme / "_data/socials.yml")
shutil.copy2(content / "CV.pdf", theme / "assets/pdf/CV.pdf")
shutil.copy2(content / "pale-blue-dot.jpg", theme / "assets/img/pale-blue-dot.jpg")
# Use a descriptive alternative text for the photograph.
layout = theme / "_layouts/about.liquid"
layout.write_text(
    layout.read_text().replace("alt=page.profile.image\n", "alt=page.profile.image_alt\n"),
    encoding="utf-8",
)
(theme / "_bibliography/papers.bib").write_text("", encoding="utf-8")
(theme / "_pages/404.md").write_text(
    '---\nlayout: page\ntitle: Page not found\npermalink: /404.html\n---\n\n'
    'The page you requested could not be found. [Return to the homepage](/).\n',
    encoding="utf-8",
)

# Blue links and generous list spacing, matching the restrained reference style.
styles = theme / "_sass/_themes.scss"
styles.write_text(styles.read_text().replace("#{$purple-color}", "#2b6f91"), encoding="utf-8")
custom = theme / "assets/css/main.scss"
with custom.open("a", encoding="utf-8") as handle:
    handle.write('''
/* Personal academic page refinements. */
.post article > ol > li { margin-bottom: 1.65rem; }
.post article > ul > li { margin-bottom: .65rem; }
.post article h2 { margin-top: 2rem; margin-bottom: 1rem; }
.post .desc { color: var(--global-text-color-light); line-height: 1.6; }
.post article table { width: 100%; margin-bottom: 1.5rem; }
.post article th, .post article td { padding: .5rem .7rem; text-align: left; border-bottom: 1px solid var(--global-divider-color); }
footer.sticky-bottom { margin-top: 3rem; }
.profile .more-info { font-family: inherit; }
.profile .pale-blue-dot-caption { font-size: .8rem; line-height: 1.55; color: var(--global-text-color-light); }
.profile .pale-blue-dot-caption p { display: block; margin: 0 0 .65rem; }
''')
print("Prepared Guangwei Gao's al-folio site.")
