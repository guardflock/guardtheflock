# Guard the Flock

**A free, public educational resource on spiritual abuse**—what it is, how to recognise it, and where to find support and further reading.

🌐 **Live site:** [https://guardtheflock.pages.dev/](https://guardtheflock.pages.dev/)  
🔒 **Source repository:** Private GitHub repository (`guardflock/guardtheflock`). The website remains publicly accessible; repository privacy does not make the Cloudflare Pages site private.

## Current version

**v8.2.1** — includes the Resources/Discussion Guide updates and audited link repairs; case reporting is manually curated, with FreshRSS optional for private discovery. See [Versioning](#versioning) and the [changelog](CHANGELOG.md).

## What the site covers

- **What Is Spiritual Abuse?** — a definition and common forms
- **Warning Signs** — nine patterns to help readers identify concerning behaviour
- **How to Respond** — guidance for people affected and for leaders or witnesses
- **Resources** — books, Christian support organizations, recovery guides, and journalism from Malaysia, Asia, and globally
- **Small-group Discussion Guide** — included under Resources for cell and small groups, and alongside the discernment framework
- **Documented Cases** — manually curated links to specific Christian/church-related reporting, with distinctions between allegations, convictions, and settlements
- **Get Help** — support contacts for Malaysia, Singapore, and globally
- **FAQ** — including guidance for cell-group leaders and pastoral workers

## Navigation and accessibility

- **Path chooser:** On a first visit, readers can choose a starting path for discernment, personal support, or church-leader guidance. The section tabs remain available after entering the guide.
- **Need Help shortcut:** A persistent shortcut opens Get Help / Respond, including when the path chooser is displayed.
- **Progressive disclosure:** The warning signs remain visible; deeper tests, decision tools, and group-study material can be opened when needed.
- **Documented Cases content note:** A distressing-content warning appears immediately above the case list. The cases remain visible below it; visitors are not required to click through a separate reveal gate.
- **Keyboard accessibility:** A skip-to-content link and visible keyboard-focus indicators help visitors navigate the page.

## Important scope and editorial notes

This site is educational material, not a complaints platform. It does **not** operate a directory or ranking of churches, pastors, or leaders. The Documented Cases section links to selected public reporting; it does not investigate or adjudicate cases independently. Case links are manually curated from independent publishers. A reported allegation is not a finding of guilt; a settlement is not necessarily an admission of wrongdoing. Please read the linked publisher's reporting and verify time-sensitive support contacts before relying on them.

## Case reporting and latest headlines

**Documented Cases** is manually curated. The maintainer reviews stories and adds selected, specific links with appropriate context under that section. Use FreshRSS privately if helpful for discovering articles, then verify the original publisher's report before adding a case link. Prioritize Christian-authored or Christian-organization reporting about spiritual or sexual abuse, safeguarding, church financial misconduct, or institutional accountability. Keep publisher attribution and bylines where known; distinguish allegations, convictions, and settlements; do not infer guilt or build a database of identifiable people.

The separate **Latest News** section is an automated headline-discovery feed. It is not a case database or an endorsement of the linked stories. The GitHub Actions workflow runs scripts/update_news.py every four hours, at 17 minutes past each fourth UTC hour, and when the workflow or script changes are pushed to main. The script reads public publisher RSS/Atom feeds and writes a static snapshot to data/news.json; the website loads that JSON file rather than requesting RSS feeds directly from each visitor's browser. Headlines link to publishers' original articles and are not independently verified case records. Feed availability and relevance can vary, so check the original publisher's report and use editorial judgement before adding a story to Documented Cases. Preview branches may show their committed snapshot without independently refreshing it.

## Development and deployment

The site is a static website published at [guardtheflock.pages.dev](https://guardtheflock.pages.dev/) using **Cloudflare Pages**. The source is maintained in the private GitHub repository `guardflock/guardtheflock`; the public website is served separately by Cloudflare Pages.

- **Production branch:** `main`.
- **Pre-production branch:** `pre-production-v2` (used for staging changes; it is not the production branch unless Cloudflare Pages is separately configured to publish a preview deployment).
- **Root directory:** repository root (`/`).
- **Build command:** none; this is plain HTML, CSS, JavaScript, and static data.
- **Build output directory:** repository root (`/` or `.` in the Cloudflare Pages setting).
- **Main page:** `index.html`.

When Cloudflare Pages Git integration is connected to this private repository, commits to the configured production branch trigger production deployments. Preview deployments for other branches depend on the Cloudflare Pages branch/deployment settings. The Git integration must retain permission to access the private repository. If a commit does not appear on the site or preview, check the Cloudflare Pages deployment log.

For a local visual check, open `index.html` in a browser. FreshRSS is not part of site hosting: it is an optional private reader on the maintainer's PC. The Latest News section uses the generated `data/news.json` snapshot. The scheduled workflow is normally run from the repository's default branch; a non-default preview branch may display its committed snapshot without independently refreshing it.
## Versioning

The project uses [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

- **MAJOR**: incompatible changes to the site's public structure or content/data contract.
- **MINOR**: backward-compatible features or substantial new sections.
- **PATCH**: backward-compatible fixes, corrections, and maintenance.

The version is documented in `VERSION` and changes are recorded in `CHANGELOG.md`. Version labels are repository release metadata; they do not alter the static page's runtime. Tag releases as `vX.Y.Z` when publishing a GitHub Release.

## Wiki

The repository wiki is maintained separately by GitHub and is not included in a normal clone. See [`docs/wiki/`](docs/wiki/) for maintained source pages, including project scope and support/resource guidance. When the wiki pages change, publish their contents to the GitHub Wiki if that feature is enabled for the repository.

## Contributing

Contributions are welcome, especially:

- Additional, verified support contacts for other countries
- Corrections to phone numbers, availability, or URLs
- Additional reputable books and organisations
- Translations into Bahasa Malaysia or Mandarin
- Fixes to accessible page behaviour

Please open an Issue or Pull Request. Do not submit private survivor information or unverified allegations about identifiable individuals.

## License

MIT License — free to use, adapt, and share with attribution. See [`LICENSE`](LICENSE).

## Credits

Built with assistance from Claude (Anthropic). Content is sourced from published books, established organisations, and journalism. News articles remain the property and responsibility of their publishers.
