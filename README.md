# Guard the Flock

**A free, public educational resource on spiritual abuse**—what it is, how to recognise it, and where to find support and further reading.

🌐 **Live site:** [guardflock.github.io/guardtheflock/](https://guardflock.github.io/guardtheflock/)

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

## Important scope and editorial notes

This site is educational material, not a complaints platform. It does **not** name, rate, or maintain a database of individual churches, pastors, or leaders. Case links are manually curated from independent publishers. A reported allegation is not a finding of guilt; a settlement is not necessarily an admission of wrongdoing. Please read the linked publisher's reporting and verify time-sensitive support contacts before relying on them.

## Curating case reporting

The site intentionally has no automated headline feed. The maintainer reviews stories and manually adds selected, specific links under **Documented Cases**. Use FreshRSS privately if helpful for discovering articles, then verify the original publisher's report before adding a link. Prioritize Christian-authored or Christian-organization reporting about spiritual or sexual abuse, safeguarding, church financial misconduct, or institutional accountability. Keep publisher attribution and bylines where known; distinguish allegations, convictions, and settlements; don't infer guilt or build a database of identifiable people.

## Development and deployment

This is a static site hosted with GitHub Pages. The main page is `index.html`; there is no frontend build step or package install. Open `index.html` in a browser for a visual check. FreshRSS is not part of site hosting: it is an optional private reader on the maintainer's PC.

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

Built by [James CWK](https://github.com/jamescwk) with assistance from Claude (Anthropic). Content is sourced from published books, established organisations, and journalism. News articles remain the property and responsibility of their publishers.
