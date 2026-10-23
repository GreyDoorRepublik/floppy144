# Floppy//144 website

A static, paper dossier website for the Floppy//144 Windows beta by Grey Door Republik. The copy is grounded in the public beta repository README, read on 22 October 2026. No game source files are changed.

## Contents

- `dist/index.html`: introduction and case dossier.
- `dist/overview.html`: spoiler-free game overview.
- `dist/screenshots.html`: seven supplied beta screenshots with links to the original captures.
- `dist/beta.html`: releases, installation, controls, feedback and FAQ.
- `dist/assets/style.css`: responsive layouts, focus states, reduced motion and print styles.

No dependency installation, build step, JavaScript, external fonts, cookies or analytics are required. All internal paths are relative so the site works below `/floppy144/`. The illustrated floppy disk on the home page is decorative artwork; it is not a screenshot.

## GitHub Pages

Intended public URL: https://greydoorrepublik.github.io/floppy144/

The included `.github/workflows/pages.yml` publishes `dist` to GitHub Pages. Put this source in the `GreyDoorRepublik/floppy144` repository, then set Settings → Pages → Build and deployment → Source to GitHub Actions. The workflow runs on the default branch, manual dispatch and changes to the site files.

Alternatively, put the contents of `dist` in the `floppy144/` directory of the existing `GreyDoorRepublik/greydoorrepublik.github.io` site. Preserve the rest of that website and its deployment process. Use one of these arrangements; both serve the requested URL.

The Sites preview is separate from GitHub Pages. The `.openai` directory configures the private Sites deployment and is not needed by GitHub Pages.

## Screenshots

Seven user-supplied captures live in `dist/assets/screenshots/`. Each is preserved byte for byte and displayed without cropping. The gallery links directly to the original PNG files for full-size viewing; the home page features reception. All images have descriptive alt text and explicit pixel dimensions. `docs/STATUS.md` records the selection and source mapping. Additional supplied screenshots are held back to avoid spoilers, a session-load error, or duplicating the credits.

To add or replace captures, update their figures and captions in `dist/screenshots.html`, the home teaser if relevant, and the expected image count in the checker. Preserve the dossier frames and the images' original aspect ratios.

## Check

Run `python3 checks/check_site.py` from the project root. This validates the four pages, local links and fragments, navigation, unique IDs, required external destinations, canonical URLs, image assets and dimensions and the absence of unintentional scripts or remote dependencies. It is not a substitute for browser or screen-reader testing.
