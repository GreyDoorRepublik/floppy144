# Website handover — 22 October 2026

## Agreed brief

Create a standalone marketing website for Floppy//144 at https://greydoorrepublik.github.io/floppy144/. Use a paper dossier visual style (cream paper, dark ink, red stamps, file tabs), reserving terminal styling for the game. Include beta status, public beta repository links, a spoiler-free overview, a screenshot gallery and a breadcrumb to the main studio website.

## Implementation

Four static HTML pages with one shared stylesheet and a vector favicon. Relative internal URLs support the `/floppy144/` GitHub Pages path. No dependencies, build pipeline, scripting, external font requests or stored visitor data. Screenshot slots explicitly state images are pending. The home-page disk is decorative CSS artwork, not gameplay. Content and controls follow the beta repository README retrieved on 22 October 2026.

## Verification

- Static checker: PASS for four pages, links, fragment targets, active navigation, language, canonical URLs, external destinations and pending-image notices.
- Desktop visual inspection: home, overview, gallery and beta FAQ checked in the cloud browser.
- Responsive home visual inspection at 390px iframe width and 768px iframe width; beta at 320px. Each had equal HTML client and scroll widths (375/375, 753/753 and 305/305 respectively; iframe scrollbars reduce the CSS viewport).
- FAQ disclosure: expanding the save-progress question exposed its answer in both DOM state and screenshot.
- No game files changed; Windows compilation, gameplay regression tests and executable size checks do not apply to this static website.

## Public deployment status

Not deployed to GitHub Pages. GitHub returned 404 for `GreyDoorRepublik/floppy144` and `GreyDoorRepublik/greydoorrepublik.github.io`; the organisation repository listing returned no repositories. Direct access to the public `GreyDoorRepublik/Floppy144-beta` repository and its README succeeded. This establishes an access/destination blocker, not that the website repositories cannot exist.

A private Sites preview is maintained separately. The included Pages workflow publishes `dist` when committed to the target repository's default branch and Pages is configured to use GitHub Actions. A second supported deployment arrangement is placing the contents of `dist` in `/floppy144/` of the studio's existing GitHub Pages repository.

## Outstanding

1. Screenshot selection and integration completed on 23 October 2026; see below.
2. Identify and make accessible the repository serving the requested URL, then deploy the verified website there. Do not repurpose the beta game repository.
3. Full screen-reader testing and physical mobile-device testing have not been performed.


## Screenshot integration — 23 October 2026

Seven supplied beta captures now appear on the gallery page; reception is also featured on the home page. Each links to its original PNG. The received pixels and complete screenshot frame are preserved without retouching, cropping or scaling the asset files; only their CSS display size changes. Source filenames map to descriptive website assets as follows:

| Supplied timestamp | Website asset |
| --- | --- |
| 181103 | reception.png |
| 180926 | remote-session.png |
| 180938 | archive-terminal.png |
| 181013 | record-recovery.png |
| 181027 | recovery-index.png |
| 181039 | document-viewer.png |
| 181259 | desk-inspection.png |

Not selected: 180845 (session-load error visible), 180858 (studio credits rather than gameplay), 181456 (possible clue close-up), 181501 (later-room view), 181707 (full floor plan). The twelve supplied source files remain unchanged.

Gallery placeholders and pending-image notices have been removed. The local checker now verifies seven distinct image assets and their PNG dimensions. The GitHub Pages repository access blocker remains unresolved; this update publishes to the existing private Sites preview only.

Screenshot verification: static link/image checks passed; desktop gallery inspection confirmed all seven images loaded at their original 1282px width, and the reception full-size link opened the original image. A 390px phone iframe showed the gallery at a 375px CSS viewport with equal client/scroll widths and all seven displayed images preserving their original aspect ratio. The temporary QA page was removed before packaging.
